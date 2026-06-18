## Introduction

Trajectory Optimization (TO) is a fundamental technique for enabling robotic and autonomous systems to navigate safely and efficiently. From an optimization perspective, TO in robotics is characterized by nonlinear dynamics, state and actuation constraints, and complex environmental geometries, such as cluttered environments with multiple obstacles. The interplay of these factors induces a non-convex cost landscape. A canonical example is found in navigation tasks in cluttered environments, where the presence of multiple local minima, i.e., different topological paths around obstacles, creates multiple solutions.

To make trajectory optimization computationally tractable, researchers have traditionally relied on local approximations of this landscape. Consequently, gradient-based families of algorithms, such as Differential Dynamic Programming (DDP) and Sequential Quadratic Programming (SQP) for dynamical systems, have been widely used.

DDP and its variants, such as the iterative Pontryagin Maximum Principle (iPMP), utilize a forward-backward sweep architecture to propagate value functions or costates, arising from quadratic or linear approximation of cost and dynamics. Although this structure offers scalability and speed, it relies on local information (gradient) and approximations around nominal trajectories. Similarly, SQP addresses TO by solving quadratic subproblems derived from quadratic approximation of the cost and linearized dynamics.

Because both families rely strictly on local first- and second-order information, they are both vulnerable to being captured by sub-optimal solutions. In the context of robotic tasks, this may correspond to situations where the robot gets stuck at a dead end or finds an inefficient path even if it reaches the target. In addition, the local nature makes the algorithm sensitive to the initial condition and incremental.

On the opposite side of gradient-based approach, sampling-based Stochastic Optimization (SO) methods overcome the limitations of locality. These algorithms, typically deployed in a Model Predictive Control (MPC) fashion, have been successfully used across diverse robotic systems. The most representative algorithms in this approach are Cross-Entropy (CE) and Model Predictive Path Integral control (MPPI) and its variations. The algorithms sample dynamics forward and with perturbed control and refine their policy by weighting the trajectories based on the cost associated with the samples.

Because these algorithms do not require derivatives of the cost and dynamics, they are easily applied to non-smooth systems. Furthermore, the stochastic sampling process enables broader exploration, allowing algorithms to explore multiple local solutions that gradient-based methods cannot. The drawback of MPPI is that the resulting optimal decisions are noisy, and this can result in undesirable stochastic behavior and slow convergence.

Recent efforts to mitigate the negative effect of noise include sampling from colored noise to have temporal correlation for a smoother trajectory, and using Hessian of cost as sampling covariance for improving convergence. Furthermore, techniques such as spline parameterization of control can effectively reduce control jitter. Although they all alleviate the negative effect, often do so at the cost of expressive flexibility or by reintroducing differentiability requirements.

While the sampling aspect of SO provides a way to handle complex objective functions, this feature does not completely address the issue. Naive sampling can often be inefficient in exploring the state space. These limitations motivated the work on multimodality. One common strategy involves a coarse global search followed by local refinement. The method proposed by Osa utilizes a Gaussian Mixture Model (GMM) to coarsely fit multiple candidate solutions in a reduced basis-function space, followed by a gradient-based optimization to refine them. Although this approach works well in a robotic arm as presented, it is fundamentally kinematic in nature. Because the first sampling phase is decoupled with the system dynamics, it would become a bottleneck for underactuated systems where the manifold of feasible trajectories is much more strict. Sundaralingam et al. adapts this concepts for the GPU era by adding massive parallelization. It uses MPPI-like stage to seed a kinematic gradient-based optimizer. Kim et al. runs MPPI to produce coarse but diverse trajectory, then refines it with gradient based interior-point DDP solver.

Similar, but another way to combine the two optimization techniques, i.e., gradient and sampling, to handle multimodality is to perturb a single-seed gradient-based optimization via sampling. In Schulman et al., SQP-based trajectory optimizer is perturbed by randomly sampled noise during optimization to find better local solutions. Authors in Zucker et al. perturb gradient-based kinematic optimizer by sampling momentum from energy-like distribution induced by the cost of the trajectory to jump to a better local solution.

Beyond purely optimization-based methods, recent research has explored the use of generative models to provide multimodal priors for planning. For instance, Urain et al. utilize an energy-based model to represent multimodal distributions, which are then integrated into gradient-based and stochastic optimizers. Similarly, Carvalho et al. employ a diffusion model to capture complex trajectory priors from large-scale datasets. Authors in Huang et al. leverage a generative prior to initialize the parallelized optimization mentioned earlier in an informed way. While these methods excel at representing the multimodality present in historical data, they are fundamentally data-dependent.

Le et al. utilizes Optimal Transport to handle multimodality, they often rely on a simplified linear Gaussian transition to enforce smoothness. This formulation implicitly treats dynamics as a soft smoothness penalty rather than following the true nonlinear dynamics. While Pan et al. adopts the nomenclature of generative diffusion, its underlying mechanism is a multi-step adaptation of the CEM using a noise-annealing schedule.

Alternative algorithms Lambert et al.; Lambert and Boots; Power and Berenson explore multimodality by making use of Stein Variational Gradient Descent (SVGD). SVGD is a particle-based optimization method that actively maintains solution diversity by using a kernel-based repulsive force. The work in Lambert et al.; Lambert and Boots can be seen as SV extensions of MPPI. The method is also applied in kinematic planners, such as, and as a parallelized search algorithm. In Power and Berenson; Lee et al., a constrained SV TO algorithm is proposed. However, the approach scales unfavorably with the dimensionality of control, state variables, time horizon, and the number of equality/inequality constraints. In Barcelos et al., the authors proposed signature-based repulsion, which, unlike pointwise diversity metrics that often yield redundant temporal variations of a single path, ensures that exploration occurs over topologically distinct and geometrically meaningful trajectories.

Motivated by the complementary strengths of these methods, we propose a framework that couples sampling- and gradient-based optimization. Specifically, we investigate two mechanisms that combine sampling- and gradient-based optimization to address the challenges of MPC in non-convex landscapes. One of the primary objectives is to provide a more rigorous analytical understanding of how these hybrid structures prevent optimization from becoming trapped in sub-optimal local minima.

The first mechanism is a schedule of optimization steps consisting of several Newton/second-order steps followed by an iteration that relies on sampling. The motivation for this hybrid process is that while Newton steps can locally optimize the objective function, the sampling phase promotes the escape of the trajectory from poor local minima. In the context of TO for robotics, this mechanism was first introduced in Maximum Entropy DDP (ME-DDP) with Shannon's entropy and then extended to the broader class of Tsallis entropy in unconstrained settings. It is also interesting to note that this hybrid optimization mechanism was also proposed in the area of business administration and management science Harford as a mental model to enhance creativity and improve innovation.

The second mechanism provides a further extension of ME-DDP through Stein Variational DDP (SV-DDP). Based on the Stein Variational Newton's Method (SVNM), SV-DDP is a kernel-based extension of ME-DDP. In SV-DDP, the optimization process alternates between two phases as in ME-DDP. Starting from different initial trajectories, the first phase consists of multiple DDP updates performed in parallel fashion, resulting in optimized state and control trajectories. In the second phase, the control trajectories are updated with the rule based on SVNM to generate the new state trajectories. This phase facilitates exploration by pushing the trajectories apart using a kernel-based repulsion force.

A preliminary version of this work appeared in Aoyama et al.. This journal version expands on the previous work by providing a unified mathematical derivation of the algorithm family, a rigorous interpretation of exploration via Hessian, extensive simulation-based comparisons, and hardware validation.

## Background

In this section, we establish theoretical preliminaries for dynamic optimization and entropic regularization. We first formalize the entropic regularization of a dynamic optimization, followed by a review of DDP and ME-DDP. To align with standard conventions in information-theoretic literature, we denote the natural logarithm as $\ln$ throughout this section.

### Entropic-regularized Dynamic Optimization

With the deterministic dynamics $x_{t + 1} = {f{(x_{t},u_{t})}}$, with state $x \in {\mathbb{R}}^{n_{x}}$ and control $u \in {\mathbb{R}}^{n_{u}}$, we consider the following TO problem:

subject to the dynamics. Here, we define state and control trajectories as $X = {\lbrack x_{1},\cdots,x_{T}\rbrack}$ and $U = {\lbrack u_{1},\cdots,u_{T - 1}\rbrack}$. The scalar-valued functions $l{( \cdot, \cdot )}$, $\Phi{( \cdot )}$, and $J{( \cdot, \cdot )}$ denote the running, terminal, and total cost of the problem, respectively. There exist several second-order solvers that can solve the problem above. Typically, they solve Quadratic Programming (QP) with a quadratic approximation of the cost under constraints from dynamics. Two well-known classes of algorithms are DDP and SQP. With quadratic approximation of dynamics, DDP effectively splits the problem into a sequence of stage-wise subproblems and solves them efficiently. SQP solves a large QP over trajectories under linearized dynamics, although there exist methods to solve QP efficiently with LQR Rao et al.. Both of these methods are successfully used in robotic applications. However, since they are relying on local information on the cost and dynamics, i.e., gradient and Hessian, they are vulnerable to being trapped at a poor local solution as mentioned in Introduction.

To alleviate the issue, we consider a stochastic control policy $\Pi{(\left. U \middle| X \right.)}$ and introduce expected entropy of the policy:

where $P{(X)}$ is the marginal distribution of the state trajectory induced by the policy $\Pi$, and ${P{(X,U)}} = {P{(X)}\Pi{(\left. U \middle| X \right.)}}$ is the resulting joint distribution of the state and control trajectories. Here, we use the term expected entropy because it represents the conditional entropy of the control trajectory, marginalized over the state trajectory distribution. We add it to the objective to promote exploration. Incorporating the dynamics and taking expectation over a trajectory, we have a new objective:

The temperature parameter $\tau$ acts as a thermodynamic scaling factor. The intuition here is that, at high temperatures, the control (thermodynamic particles) has high kinetic energy, spreading across the cost landscape to maximize entropy. This prevents the optimizer from collapsing into a local minimum. In contrast, when the temperature is low, the control acts like a crystal, which does not explore the landscape.

With the objective with the entropy, the TO problem seeks a stochastic policy that minimizes the original objective while maximizing the corresponding entropy. The resulting policy can explore multiple local solutions and is robust to being captured by poor ones. There exist multiple approaches to solve the problem. One of the simplest cases is with a feedforward control $\Pi{(\left. U \middle| x_{1} \right.)}$ which gives

where $Z_{0}$ is a partition function Liu et al.. In this work, we use DDP to effectively obtain and utilize the feedback policy.

### Differential Dynamic Programming

In this section, we review DDP. Although this is a classic work, we highlight its inherent quadratic structure and treatment of its Hessian. This is because the Hessian plays a key role in the exploration strategies developed in the following sections.

We consider the cost-to-go at time step $t = i$, i.e., cost starting from $t = i$ to $N$, denoted by $J_{i}{(X_{i},U_{i})}$. This is given by

with trajectories starting from time step $i$: $X_{i} = {\lbrack x_{i},\ldots,x_{N}\rbrack}$, $U_{i} = {\lbrack u_{i},\ldots,u_{N - 1}\rbrack}$. The value function is defined as the minimum cost-to-go in each state and time step $t$ via ${V_{t}{(x_{t})}}:={{\min_{u_{t}}J_{t}}{(X_{t},U_{t})}}$. Given Bellman's principle of optimality that provides the following rule

where $Q_{t}{(x_{t},u_{t})}$ is action-state, or simply $Q$ function, DDP finds local solutions to the minimization of by expanding about nominal trajectories $\overline{X}$ and $\overline{U}$.

The first step of the minimization is to perform quadratic expansions of $Q_{t}$ about nominal pair (${\overline{x}}_{t}$, ${\overline{u}}_{t}$) with the deviation ${\deltax_{t}} = {x_{t} - {\overline{x}}_{t}}$, ${\deltau_{t}} = {u_{t} - {\overline{u}}_{t}}$, obtaining

where we drop the time index $t$ for $Q$. For readability, we drop the time subscript $t$ where the time dependency can be recovered from the arguments or associated variables (e.g., writing $Q_{u}^{\mathsf{T}}\deltau_{t}$ instead of $Q_{u,t}^{\mathsf{T}}\deltau_{t}$), hereafter.

The quadratic approximation is a standard process in nonlinear optimization, as used in Newton's method.

Assuming that the Hessian $Q_{uu}$ is Positive Definite (PD), we can explicitly optimize $Q$ approximated in with respect to $\deltau_{t}$ by computing a partial derivative of with respect to $\deltau_{t}$ and setting it zero. This minimization yields the following local optimal control law

where $\kappa$ and $K$ are known as feedforward and feedback gains, respectively.

DDP has backward and forward passes. In the backward pass, the derivatives of $Q$ functions which is later introduced , gains in are computed backward in time. In the forward pass, the new control ${\overline{u}}_{t} + {\deltau_{t}^{\ast}}$ is propagated forward in time to give a new pair of nominal trajectories.

### Backward pass

To obtain the derivatives of $Q$ functions that are required to compute gains, we perform a similar expansion on the term ${l{(x_{t},u_{t})}} + {V_{t + 1}{(x_{t + 1})}}$ given in the definition of $Q$ function , and eliminate $\deltax_{t + 1}$ using quadratic approximation of the dynamics:

where $f_{x}$ and $f_{u}$ denote the state and control Jacobians, while the block-matrix in the last term contains the Hessian tensors. Specifically, $f_{xx}$ and $f_{uu}$ represent the second-order sensitivities with respect to state and control, respectively, and $f_{xu}$ accounts for their coupling. Mapping the terms on both sides of quadratic approximation of ${Q{(x_{t},u_{t})}} = {{l{(x_{t},u_{t})}} + {V_{t + 1}{(x_{t + 1})}}}$, we obtain the derivatives of $Q$ (evaluated on $\overline{X}$ and $\overline{U}$) as follows.

where derivatives of the running cost and dynamics are evaluated at time $t$, and $\cdot$ for Hessians and $V_{x,{t + 1}}$ is tensor contraction along the first (state) axis.

Now, $\deltau_{t}^{\ast}$ is computed using $V_{x,{t + 1}}$ and $V_{{xx},{t + 1}}$, which are in one time step ahead. To propagate derivatives of $V_{t}{(x)}$ back in time, we consider the quadratic expansion of $V_{t}{(x)}$, that is,

and equate the equation with the quadratic expansion of $Q$ in through. Since we now have a solution of the $\min_{u_{t}}$ in the right-hand side of, by substituting $\deltau^{\ast}$ for $\deltau$, the $\min$ operator vanishes. This allows us to compare the coefficients of $\deltax_{t}$ by mapping the terms, giving the backward recursions:

with the terminal condition

We note that in our implementation, we drop the second-order information of the dynamics and use a linear approximation, which corresponds to iterative LQR.

### Forward pass

In the forward pass, the new control ${\overline{u}}_{t} + {\deltau_{t}^{\ast}}$ is propagated forward in time to give a new pair of nominal trajectories, typically with a backtracking line search to absorb the discrepancy between the quadratic cost model, linear or quadratic dynamics model, and the actual ones.

### Regularization

To compute the optimal gains by minimizing, the Hessian $Q_{uu}$ must be PD. Furthermore, established convergence analysis relies on PD $Q_{uu}$ or on the convexity of the surrogate model formed with regularized $Q_{uu}$. When the $Q_{uu}$ is not PD, it must be regularized. One of the well-known strategies is

which is equivalent to adding a cost penalizing large $\deltau_{t}$ via a quadratic trust-region penalty.

In practical implementations of DDP, if cost reduction is not achieved with a small step size in the forward pass, the backward pass is rerun with a larger regularization parameter.

This effectively restricts the optimization to a smaller, more reliable neighborhood of the nominal trajectory where the local approximation remains valid, and therefore, cost reduction is expected.

### Maximum Entropy Differential Dynamic Programming

This section provides a review of ME-DDP and demonstrates its efficacy in solving the entropy-regularized dynamic optimization problem. We also introduce its unimodal and multimodal policies. We have a detailed derivation in the Appendix.

Using the Markovian assumption Puterman, we decompose the policy defined over the trajectories into multiple of policies at each time step:

Then, the expected total entropy of the policy $\mathcal{H}{\lbrack\Pi\rbrack}$ becomes the sum of stage-wise entropy:

With this decomposition, we consider the stage-wise minimization of given state $x_{t}$,

which can be seen as an entropic regularized version of. Here, we use $\overset{\sim}{V}$ to denote the value function of the entropic regularized problem. The minimization in results in the optimal control policy $\pi_{t}^{\ast}$:

where $Z{(x)}$ is the corresponding partition function and ${{\overset{\sim}{Q}}_{t}{(x_{t},u_{t})}} = {{l{(x_{t},u_{t})}} + {{\overset{\sim}{V}}_{t + 1}{(x_{t + 1})}}}$. The relationship represents a smooth approximation of the Bellman optimality operator. The intuition here is that, by exponentiating the negative $Q$ function, the lowest value are magnified relative to higher ones. The subsequent operation with $\ln$ and negation returns the result to the original scale. This operation effectively acts as a Soft-min operator.

### Unimodal Gaussian Policy

Combined with the quadratic approximation of $Q$ function utilized in DDP, indicates that the optimal policy has a form of unimodal Gaussian ${\pi^{\ast}{(\left. {\deltau} \middle| {\deltax} \right.)}} \sim {\mathcal{N}{({\deltau^{\ast}},{\tauQ_{uu}^{- 1}})}}$, where $\deltau^{\ast}$ is a solution of deterministic DDP .

### Multimodal Gaussian Policy

In the multimodal case, we consider $N$ trajectories or modes:

with $n = {1,\ldots,N}$ and the LogSumExp approximation of the value function

where the superscript $(n)$ denotes the $n$ th trajectory. The exponential transformation ${\mathcal{E}_{\tau}{(y)}} = {\exp{({- {y/\tau}})}}$ of the value function results in a control policy represented as a mixture of Gaussians whose categorical distribution is proportional to the value function of each trajectory. This multimodal policy is represented as follows:

The intuition here is that the policy decides which modes to sample based on the value function and then samples from the corresponding Gaussian. We note that while theoretically allows the policy to be multimodal, in practice these modes may collapse into a single dominant local minimum. This numerical collapse significantly diminishes the exploratory benefit of ME-DDP.

To mitigate the issue, we introduce a heuristic in our implementation with a lower bound $\omega_{\min}$ on the weights. The weights are updated as ${\hat{\omega}}^{(n)} = {\max{(\omega^{(n)},\omega_{\min})}}$ and subsequently renormalized.

### Exploration (sampling) vs Exploitation (gradient)

In the ME-DDP framework, the entropic term facilitates exploration, while the deterministic DDP part governs exploitation. As the title suggests, excessive exploration can wash out the signal provided by the gradient. If the temperature $\tau$ is too high, the optimizer may not identify the underlying cost structure, leading to poor convergence. To mitigate this, the authors of So et al. suggest that sampling should not happen at all iterations. Instead, perturbations are introduced periodically to allow the nominal trajectory to stabilize between exploratory phases. Although the original work was in the unconstrained setting, we observe that this is even more important when constraints are handled via DDP. Furthermore, following the spirit of Dong and Tong, we implement a heuristic that preserves the trajectory with the best metric without sampling. This approach ensures that the high-precision convergence properties of the deterministic DDP are maintained for the current mode.

## Stein Variational Dynamic Optimization

In this section, we introduce SV-DDP, a kernel extension of the ME-DDP framework. By incorporating a kernel-based repulsive force, the algorithm actively prevents particle collapse and preserves a diverse set of modes during the exploration process.

To provide the theoretical basis, we first review SVGD and its connection to functional gradient descent. We then discuss the SVNM method as a second-order extension. Subsequently, we apply these techniques to the DDP framework to derive SV-DDP. Finally, we discuss the essential components of the algorithm.

### Stein Variational Gradient Descent and Newton's Method

SVGD minimizes the Kullback-Leibler (KL) divergence between a set of particles and a target distribution by performing functional gradient descent in a Reproducing Kernel Hilbert Space (RKHS). SVNM incorporates the Hessian to accelerate convergence and better capture the geometry of the underlying distribution.

For comprehensive treatments, we refer the reader to Liu and Wang; Liu for SVGD and to Detommaso et al. for SVNM. In this subsection, $x \in {\mathbb{R}}^{d}$ denotes a generic optimization variable rather than the system state, and $x_{n} \in {\mathbb{R}}^{d}$ represents a specific sampled point (particle).

### Stein Variational Gradient Descent

Let $p$ on ${\mathbb{R}}^{d}$ be a target distribution that we wish to approximate using a collection of samples. We specify the argument of $p{( \cdot )}$, when we evaluate it at a point $x_{n}$ as $p{(x_{n})}$. With samples $\{ x_{n}\}$ from a tractable reference distribution $q$ on ${\mathbb{R}}^{d}$, SVGD iteratively computes a transport map $\mathcal{T}:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}}$ so that the transformed samples of $q$, i.e., $\{{\mathcal{T}{(x_{n})}}\}$ can empirically approximate $p$. This map is obtained by solving the following optimization problem:

where ${\mathcal{T}_{\#}q^{l}} = q^{l + 1}$ and $l$ stands for $l$-th iteration. Here, $D_{KL}$ is KL divergence that measures the difference between the two distributions. To simplify this problem, SVGD considers the vector-valued Reproducing Kernel Hilbert Space (RKHS) $\mathcal{F}^{d} = {\mathcal{F} \times \cdots \times \mathcal{F}}$, where $\mathcal{F}$ is a scalar-valued RKHS with kernel $k{(x,x^{\prime})}$. This framework allows us to represent functions as weighted compositions of kernels centered at the samples. Furthermore, it also allows us to solve the optimization problem in functional space by solving the corresponding problem with the weights using standard optimization techniques. To solve, we define the map $\mathcal{T}$ as a perturbation $\mathcal{P}$ of the identity map $I$ in $\mathcal{F}^{d}$ as

With the map, we reformulate the objective of the problem as

To minimize the objective ${\hat{J}}_{q^{l}}{\lbrack\mathcal{P}\rbrack}$, we consider a perturbation $\mathcal{P}$ in the direction of the functional gradient. Specifically, we define the descent direction as the negative functional gradient of ${\hat{J}}_{q^{l}}$ evaluated at the identity map (represented by the zero perturbation $\mathbf{0}$):

where ${\nabla_{\mathcal{P}}{\hat{J}}_{q^{l}}}{\lbrack\mathcal{P}\rbrack}$ denotes the functional derivative of the objective with respect to $\mathcal{P}$. This formulation allows us to treat the transformation of the distribution as a steepest descent process in the space of maps. By selecting $\mathcal{P} = {- {\alpha{\nabla_{\mathcal{P}}{\hat{J}}_{q^{l}}}{\lbrack\mathbf{0}\rbrack}}}$, we shift the current distribution $q^{l}$ towards the target $p$ in the direction that yields the most rapid decrease in KL divergence. This construction provides a direct link between standard gradient descent on a point $x$ and the functional update of the entire distribution $q$.

The descent direction satisfies the following condition with $S \in \mathcal{F}^{d}$:

where we drop $l$. Here, the left-hand side is the first variation of ${\hat{J}}_{q}$ at $S$ along $V$ defined as follows:

The authors of Liu and Wang showed that the functional gradient at $\mathbf{0}$ is empirically approximated by $N$ particles:

where the first term in the summation follows the gradient direction, and the second term spreads the particles apart from each other. Thus, it is known as the repulsive force. Finally, the update rule for samples is given by setting $\phi^{\ast} = {- {{\nabla{\hat{J}}_{q}}{\lbrack\mathbf{0}\rbrack}}}$ and with a step size $\alpha$ as follows:

### Stein Variational Newton Method

SVGD constructs a vector field and evaluates it at a single point to determine how a particle moves. SVNM additionally incorporates second-order information by approximating the Hessian of the KL functional, which is an operator rather than a vector. Operators act on functions and therefore require two evaluation points. To reduce indices, we adopt the following notation: $z$ represents the point where the input function is evaluated (input location), and $y$ represents the location where the output of the operator is evaluated (output location). Let us consider a function $f_{0}$ and an operator $H_{0}$, then applying the operator to the function gives

where the kernel $k{(y,z)}$ defines the coupling of $z$ and $y$.

For second-order optimization in functional space, we define the second variation of ${\hat{J}}_{q}$ at $\mathbf{0}$ along the pair of directions ${\mathcal{V},W} \in \mathcal{F}^{d}$ as:

The Newton direction $W$ is obtained by the optimality condition given by the following equation.

which gives the transformation map of the Newton direction as a perturbation of the identity map as ${\mathcal{T} = {I + {\alphaW}}}.$ The authors in Detommaso et al. proved that the Newton direction $W = {(w_{1},\cdots,w_{d})}^{\mathsf{T}}$ satisfies for all $\mathcal{V} = {(v_{1},{\cdotsv_{d}})}^{\mathsf{T}} \in \mathcal{F}^{d}$,

In the same work, the Galerkin approximation of the solution of $W$ is also proposed, where $W$ is expanded on $\mathcal{F}^{d} = {{span}{\{{k{(x_{1}, \cdot )}},\cdots,{k{(x_{N}, \cdot )}}\}}}$. The expansion leads to the following approximation with coefficients $\beta^{n} \in {\mathbb{R}}^{d}$

where the superscripts $n$ indicate the $n$-th particle. The coefficients $\beta$s are given as a solution of linear systems:

where the Hessian is denoted as $H_{i,j}^{s,n} = {h_{ij}{(x_{s},x_{n})}}$.

The authors also propose the block-diagonal approximation of the system for parallelization, by transforming the system as:

which means that the off-diagonal blocks are approximated to zero $H^{s,n} = O_{d}$ for $s \neq n$, where $O_{d} \in {\mathbb{R}}^{d \times d}$ is a zero matrix. A detailed explanation with an example is provided in the appendix. SVNM repeats the process of solving the linear systems above and updating particles with

to approximate the optimal distribution.

### ME-DDP with Functional Gradient and Hessian

In this section, we apply SVNM to ME-DDP to derive a new algorithm SV-DDP. The motivation here is that, by using a kernel-based repulsive force, the algorithm can keep trajectories representing the modes diverse. This mechanism prevents mode collapse and maintains high exploration capability.

We consider $N$ trajectories optimized by DDP to compose policy as in the MG-ME-DDP. Here, we assume that the global $Q$ is approximated by $Q^{(n)}$ around the trajectories $\lbrack x^{(n)},u^{(n)}\rbrack$.

We initially considered a GMM to approximate $Q$. However, since each DDP trajectory is local in nature, treating the ensemble as a global PDF via GMM interpolation is physically inconsistent. Such an approach would require evaluating local policy in regions far from their nominal trajectories, where the underlying quadratic approximations are not valid.

By substituting the optimal policy $\pi^{\ast}{(u)}$ for $p$ in the functional gradient, we obtain

for $s = {1,\cdots,N}$. We consider the quadratic approximation of $Q$ function and deviation of trajectories. Due to the linearity of the deviation, derivative with respect to $u$ is now equivalent to that of $\deltau$. As in the case of ME-DDP, the optimizer alternates optimization and exploration. Here, we assume that DDP refinement can bring the trajectory to a locally convex region with PD $Q_{uu}$, and consider the optimal control $u^{\ast}$ computed by DDP. By substituting the optimal control back into the quadratic approximation of $Q$, we have

where the derivatives of $Q$ are evaluated at ${\overline{u}}^{(n)}$. The coefficient of the kernel $k{( \cdot, \cdot )}$ is zero because of the optimality condition in the derivation of DDP. Thus, we are left with the repulsive force terms. This seems attractive for spreading trajectories. However, since the temperature $\tau$ is lost, this formulation cannot capture the relative importance of the entropy in the objective.

To recover the temperature, we use SVNM. By substituting $\pi^{\ast}{(u)}$ for $p{(x)}$ in the approximated Hessian with the terms in (3.1.2), and performing empirical approximation, the Hessian for SV Newton's method is obtained as:

where we drop optimality $\ast$ for readability. By plugging this into and solving the equations, we get the SV update (or sample) of control:

where $K$ is feedback gain of DDP.

Consequently, the temperature $\tau$ is naturally recovered within the Hessian $H^{s,s}$. We therefore propose that this approach is the consistent formulation for incorporating SV methods into the DDP framework. In, the second term is an expected outer product of the gradient, which captures information on the variation in all directions like its Hessian Trivedi et al.. Thus, $H^{s,s}$ can be seen as a sum of the Hessians of the objective and kernels. We analyze how the Hessian interacts with the repulsive force term in section Inverse Hessian as covariance. We note that the SV framework is deterministic. In this method, stochasticity enters the system only via the random sampling used for initialization. Nevertheless, we conceptualize and refer to this behavior as an exploration mechanism, maintaining conceptual continuity with the ME-DDP framework.

We provide the schematic of ME-DDP variants in Fig.1. We note that the update is not applied to the best trajectory, ensuring that at least one mode shows a monotonic cost reduction to preserve the convergence property of DDP as in So et al.; Dong and Tong. The proposed optimization framework, detailed in Algorithm 1, where an exploration mechanism based on the SV method is provided in 2. We have alternative mechanisms, i.e., UG- and MG-ME-DDPs in appendix.

Input: x1: Initial state, $\overline{u}$: Initial nominal sequence
Σ0: Initial covariance, N: Number of modes
m: Sampling frequency, I: Max iterations
IDDP: DDP iterations per mode
U: Batched control trajectory {U(n)}n = 1N
X: Batched state trajectory {X(n)}n = 1N
Qu u: Batched Hessian sequences {Qu u, 1: T − 1(n)}n = 1N
K: Batched feedback gain sequences {K1: T − 1(n)}n = 1N
5 $U^{(n)}\leftarrow{\{{u_{t}^{(n)} \sim {\mathcal{N}{({\overline{u}}_{t},\Sigma_{0})}}}\}}_{t = 1}^{T - 1}$
Best mode index
Exploitation via Parallel DDP
Algorithm 1 Entropic Regularized DDP

Output: Updated trajectories X, U
1 Compute Newton coefficients via and
4 Solve Htn, n βt(n) = −∇Ĵq (ut(n)) $w_{t}^{(n)}\leftarrow{\sum_{n^{\prime} = 1}^{N}{\beta_{t}^{(n^{\prime})}k{(u_{t}^{(n)},u_{t}^{(n^{\prime})})}}}$
1exApply update to all modes except the current best
Algorithm 2 Stein Variational Exploration

Figure 1: Schematic of algorithms in a trajectory optimization setting. The optimizer initializes N trajectories, optimizing each via DDP for several iterations in parallel. The current best trajectory is marked (*). For illustrative clarity, we assume that the cost function is dominated by the distance to the target. Policies are composed based on the specific algorithm: UG-ME-DDP uses a unimodal Gaussian centered on the best trajectory, MG-ME-DDP captures all trajectories in a multimodal distribution, and SV-DDP applies kernel-based repulsive forces to maintain diversity. Note that although the policies are constructed in control space, they are visualized here in state space for simplicity. New trajectories are sampled from these policies for exploration, excluding the current best. The cycle repeats. Although the best trajectory may get stuck at a poor local solution, the sampling mechanism and trajectories ran in parallel allows trajectories to be re-initialized into more promising areas to reach the target.

### Essential Components in SV-DDP

In this subsection, we first discuss the choice and properties of the kernel function, which serves as the core of the SV method and governs the behavior of the repulsive force. We then proceed with the selection of the step size for the SV update rule.

### Kernel and resampling

As in other SV literature in robotics, we use the RBF kernel ${k{(x,x^{\prime})}} = {\exp{({- {{\|{x - x^{\prime}}\|}^{2}/h}})}}$ and choose its length parameter by median heuristic

. We note that while kernels such as the Inverse Quadratic (IQ) kernel are frequently used in static optimization and sampling to leverage heavy-tailed characteristics that induce repulsion at greater distances, the RBF kernel remains dominant in robotics. Fig. 2 shows the RBF kernel and its derivatives. We argue that in high-dimensional robotics problems, local repulsion of RBF is more effective than far-field interaction of IQ.

Although the exponential decay of the RBF kernel is a fundamental property, it poses a challenge in high-dimensional spaces where the concentration of measure increases the average Euclidean distance between particles. In such regimes, the kernel value $k{(u^{(i)},u^{(j)})}$, and consequently its gradient, tends to vanish, as the exponential decay outpaces the linear growth of the distance vector. This leads to a vanishing repulsive force, making the SV method less effective. The sum of local kernels alleviates this problem and is used in robotic applications. This is because, in these works, the input of the kernel is a full horizon of control sequence whose dimension is $n_{u}{({T - 1})}$. In our work, due to the stage-wise formulation of DDP, the input dimension is only $n_{u}$. Thus, it works well without the technique mentioned above.

The derivative of the kernel drives the repulsive force term. It reaches local extremum before decaying as the distance between points approaches zero. Consequently, while the force pushes trajectories apart at moderate distances, it vanishes when trajectories nearly coincide, potentially leading to mode collapse. To counteract this issue, we monitor the distance of the trajectories normalized by the time horizon and dimension $\left\| {u_{i} - u_{j}} \right\|/\sqrt{Tn_{u}}$. If the distance falls below a threshold, we keep the elite trajectory and resample the remaining redundant ones to ensure continuous exploration.

Figure 2: RBF kernel (a) and its gradient (b) across different bandwidths. The gradient represents the repulsive force of SV methods.

### Step size selection

Since the step size $\alpha$ determines the extent of the exploration, its choice is critical. While the SV literature often employs backtracking line search based on the Armijo condition, robotic applications frequently tune task-specific fixed sizes.

In our implementation, we observe that the repulsive force naturally pushes trajectories toward higher-cost regions, especially near obstacle boundaries. Consequently, a standard line search often prefers near zero $\alpha$. To address this, we implement a cost-bounded heuristic: we accept the largest $\alpha \in {(0,1\rbrack}$ that keeps the trajectory cost within a factor $c_{c}$ (e.g., say 10-20) of the current minimum. This approach prioritizes global exploration while maintaining numerical stability.

## Geometric Analysis and Algorithmic Synthesis

This section provides a formal justification for using the inverse Hessian as a covariance in sampling. Although utilizing $Q_{uu}^{- 1}$, as a sampling covariance has been previously proposed in policy search literature, we present a more rigorous analysis to demonstrate why this choice is theoretically principled in the context of DDP. Subsequently, we provide how constraints are incorporated into our framework. Finally, we conclude with the implementation details for Model Predictive Control (MPC).

### Inverse Hessian as covariance

To understand the efficacy of the sampling scheme, i.e., the inverse of the Hessian as the covariance, we first examine a simple quadratic function and its Hessian to establish the mathematical relationship. Then, we extend the intuition to a more general static optimization problem. The static examples here are highly relevant because DDP can be seen as a sequence of local static sub-problems. Therefore, the insights gained here apply directly to ME-DDP. Using the same example, we analyze the effect of Hessian regularization on the sampling covariance. This analysis is essential for practical applications. Because the underlying problem is non-convex, the optimizer must robustly handle non-PD Hessians while maintaining meaningful exploration. Finally, we discuss regularization itself.

Figure 3: Surface plot of the quadratic function (a) and the resulting covariance ellipse overlaid on the contour plot (b). The blue and red arrows denote the principal directions of the covariance ellipse induced by the inverse of the Hessian H.

### Property of Hessian

We consider a two-dimensional function with a diagonal Hessian:

The surface plot and the covariance ellipse induced by the inverse of the Hessian ($H^{- 1}$) are shown in Fig. 3. The Hessian has eigenvalues $\lambda_{1} = 4$, $\lambda_{2} = 1$ with corresponding eigenvectors ${e_{1} = {\lbrack 1,0\rbrack}^{\mathsf{T}}},{e_{2} = {\lbrack 0,1\rbrack}^{\mathsf{T}}}$. This means that the function changes the most rapidly along $e_{1}$ and the least rapidly along $e_{2}$. In the contour plot, the levels are denser along the $x$-direction, reflecting the higher curvature in that dimension.

When the Hessian is inverted, the eigenvalues become the reciprocals of the original ones, while the eigenvectors are preserved. Consequently, the eigenpairs are $({{1/\lambda_{1}} = {0.25,e_{1}}})$ and $({{1/\lambda_{2}} = {1.0,e_{2}}})$. As illustrated by the covariance ellipse, using $H^{- 1}$ as covariance, the sampling scheme samples more in directions where the function increases the least and less in directions where the objective increases the most, which is important when combined with optimization.

### Static problem

In the previous example, we only analyzed the Hessian in a simple setting. Here, we consider the interaction between the local gradient and the geometry defined by the Hessian, and examine the sampling scheme in a more general setting.

We consider an optimization problem with an objective function $f_{0}{(x)}$ with $x \in {\mathbb{R}}^{n}$ and solve it with Newton's method by iteratively applying quadratic approximation and solving the subproblem. This process is fundamentally aligned with DDP. The subproblem with the approximation is given by

where $\overline{x}$ is the current point, and we assume that the Hessian $H$ is PD. Although a gradient-based step (${\deltax^{\ast}} = {H^{- 1}{\nabla f_{0}}{(\overline{x})}}$) reduces the cost of the quadratic model of the term $\deltax^{\mathsf{T}}{\nabla f_{0}}{(\overline{x})}$, the PD Hessian serves as a local metric of cost sensitivity. It characterizes the sensitivity of the objective to deviations and how much step the optimizer can take. For example, when the Hessian has a large eigenvalue, the quadratic term ($\deltax^{\mathsf{T}}H\deltax$) provides a large (positive) penalty that may counteract the descent term from the gradient.

To facilitate exploration, we consider the situation where we perturb the solution by ${\deltax} + \xi$, where $\xi \sim {\mathcal{N}{(0,H^{- 1})}}$ once in a few iterations as we do in ME-DDP. As we examined in the previous example, the eigenvectors of the Hessian indicate the principal axes of curvature. When the inverse Hessian is used as the covariance matrix, the sampling scheme becomes anisotropic: it prioritizes exploration along the axis of minimal sensitivity, where the quadratic model is flat and therefore safe to explore. Furthermore, it restricts sampling along the axis of maximal sensitivity, where even small perturbations would drive the cost up, making exploration unsafe. Here, we use the term "safety" to refer to the preservation of the optimization signal. When exploration imposes too high a cost, it essentially washes out the information of the gradient, which makes the update pure random sampling. The choice of covariance allows the optimizer to exploit information from the gradient without being perturbed by overly costly samples. Therefore, the choice provides a rigorous framework for broad exploration while preserving the efficiency of the optimization via gradient.

Another interpretation can be obtained by investigating the change of cost induced by sampling. We consider the perturbation ${\deltax} + \xi$, with noise $\xi \sim {\mathcal{N}{(0,\Sigma)}}$, where we specify the covariance $\Sigma$, later. By substituting the perturbed $\deltax$ in the quadratic approximation and taking expectation of the stochastic components with $\xi$, we obtain:

where we take the covariance as a scaled inverse Hessian $\Sigma = {\tauH^{- 1}}$ and use the fact that the trace of a scalar is the scalar itself. Generally, stochastic exploration imposes a penalty on the objective, particularly in regions of high curvature (large eigenvalue), where small perturbations can cause significant spikes. By this choice of covariance, we cancel the local geometry of the cost landscape. The optimizer explores more in the safe region and less in the unsafe region. This ensures that the expected cost of exploration remains constant and independent of the Hessian's eigenvalues, effectively normalizing the risk of sampling high-cost regions.

Figure 4: Surface plot of the objective function (a). Quadratic approximation of the objective at a locally convex point A and the approximation at a locally concave point B with original (not PD) and regularized (PD) Hessian (b). A contour plot of the objective function and the sampling covariance obtained at the two points A and B (c). The covariance ellipses, scaled by two temperatures, are drawn.

### Regularization and covariance

In the previous example, we assume that the Hessian is PD. In a practical setting, however, the Hessian may become indefinite or negative definite. To illustrate this, let us consider the two-dimensional example with three local minima whose surface plot is shown in Fig. 4 (a).

As illustrated in Fig. 4 (b), when the function is locally convex, the quadratic approximation for Newton's method is obtained with the original Hessian. Observe that the approximation yields a convex surface. In the same figure, we also perform a quadratic approximation at a locally concave point, where the Hessian is negative definite. At this point, we regularize the Hessian to obtain a valid quadratic model for minimization. Because regularization preserves the original eigenvectors and shifts the eigenvalues, it maps the most negative eigenvalues of the original Hessian to the smallest positive eigenvalues of the regularized PD surrogate. Consequently, the resulting inverse covariance prioritizes exploration along the directions of the steepest descent. This ensures that sampling is performed more extensively along the primary axes of the manifold, facilitating escape from saddle points, local maxima, and landscapes similar to them.

Fig. 4 (c) illustrates the covariance ellipsoids induced by the approximations in Fig. 4 (b). To demonstrate the effect of temperature as a scaling factor, covariances at two different temperatures are projected onto the objective's contour plot. The higher temperature corresponds to broader exploration, and therefore, the corresponding covariance is large.

### Regularization with PD Hessian

In Background section, we presented the importance of the regularization in DDP, however, with the first-order approximation of the dynamics and a proper choice of the cost function, i.e., PD Hessian with respect to state and control, $Q_{uu}$ is theoretically guaranteed to be PD (see Appendix for detailed analysis).

Even in such cases, regularization is still triggered to achieve cost reduction or to make $Q_{uu}$ well-conditioned for computing gains. In these cases, since $Q_{uu}$ is originally PD, covariance samples within a tighter region around the nominal trajectory effectively serve as an implicit trust-region mechanism. This mechanism ensures that exploration remains within the vicinity where the approximations are valid.

### Inverse Hessian and Repulsive Force

One can observe that the underlying principle of how the Hessian influences the repulsive force in SVNM and, by extension, SV-DDP is the same as the inverse Hessian acting as a covariance matrix.

When solving, the repulsive force term is scaled by the inverse of the sum of Hessians of the $Q$ function and that of the kernel. Consequently, the repulsive force is amplified in directions where the joint curvature is small. This ensures that the rescaling does not impede the primary optimization objective, nor does it obstruct the spreading of trajectories. Recalling that the kernel value is highest when trajectories are in close proximity, this scaling mechanism steers the particles into low-sensitivity subspaces, facilitating efficient exploration.

### Constrained handing via Relaxed log- barrier Function

This subsection details the integration of constraints into the ME-DDP framework (DDP and sampling). We begin by reviewing the standard $\log$-barrier approach and its application in optimal control, followed by the introduction of the relaxed log-barrier formulation. Finally, we discuss the limitations of the method.

One common approach to incorporating constraints into an objective function is through the $\log$-barrier function. These functions are powerful tools for static optimization and have been widely employed Murray and Wright; Cho; O'Neill and Wright. The function is also used in the field of optimal control, specifically, in trajectory optimization and MPC under constraints.

A key limitation of standard log-barrier methods is that they cannot handle infeasible trajectories due to the domain restrictions of the $\log$ function. This is problematic in our setting because the exploration is only implicitly aware of constraints. To address this issue, we utilize relaxed-$\log$ barrier function. We define the scalar relaxed barrier $\mathcal{B}_{r,i}{(g_{i};\mu,\delta_{\mu})}$ for a single constraint ${g_{i}{(x)}} < 0$ as

When ${g{(x)}} \in {\mathbb{R}}^{w}$, the total penalty is then given by the sum ${\mathcal{B}_{r}{({g{(x)}})}} = {\sum_{i = 1}^{w}{\mathcal{B}_{r,i}{({g_{i}{(x)}})}}}$. In this formulation, the function smoothly transitions from a logarithmic form to a polynomial approximation while maintaining $C^{2}$ continuity, allowing for infeasible trajectories.

The relaxed formulation has found applications in MPC and robotics. For instance, Feller and Ebenbauer applies it to a linear MPC problem and provides a detailed performance analysis. In Aguiar et al., the function is incorporated into a projection-based motion planning algorithm Hauser, achieving constrained trajectory optimization. The efficacy of the formulation with DDP/LQR is validated through hardware experiments on a quadruped in Grandia et al.. Since it can handle infeasible trajectories, the formulation can be used that requires exploration that may cause constraint violation, such as reinforcement learning as proposed in Zhang et al..

### Properties of the function

Figure 5: Relaxed log-barrier function ℬr (x) for various switching points δμ. The right panel provides a magnified view near the origin to highlight the behavior around the boundary (g (x) = 0). Dashed vertical lines indicate the respective switching points δμ where the barrier transitions from a logarithmic to a quadratic form.

Fig. 5 provides the function with different relaxation parameters $\delta_{\mu}$. The parameter governs how closely the relaxed barrier approximates the exact logarithmic barrier and, consequently, the degree of constraint satisfaction. As $\delta_{\mu}\rightarrow 0$, the relaxed formulation converges to the exact $\log$-barrier, yielding increasingly strict constraint satisfaction. However, this increased accuracy comes at the cost of numerical conditioning: steep gradients and large curvature arise near the constraint boundary, leading to ill-conditioned gradient and Hessian, which is critical in second-order optimization methods. Consequently, excessively small values of $\delta_{\mu}$ recover the numerical instabilities of the exact $\log$ barrier. In practice, $\delta_{\mu}$ is chosen to balance constraint satisfaction and numerical robustness. We note that even with a small $\delta_{\mu}$, the resulting conditioning issues are mitigated by appropriate scaling and regularization of gradient and Hessian terms.

In the original formulation for static problems, the penalty parameter $\mu$ is reduced towards zero as optimization proceeds. In practice, however, a small fixed $\mu$ often provides sufficient accuracy while improving numerical stability. We present how the barrier function is incorporated into DDP in appendix.

### Limitations

Numerical instability can be mitigated by the method described above, but numerical sensitivity, i.e., the amplification of small differences near the constraint boundary and hard branching, cannot be fully removed. We provide a detailed analysis in the appendix. We consider this to be an inherent limitation of the barrier approach compared with other constrained optimization methods, such as the Augmented Lagrangian (AL) method, which incorporates Lagrangian multipliers for constraint satisfaction. The use of multipliers enables the algorithm to satisfy constraints and optimality conditions without requiring excessively large penalty parameters, which are a known source of numerical ill-conditioning and instability. Nevertheless, we employ the barrier function because it can rapidly divert trajectories away from infeasible regions during the early stages of optimization.

### Receding Horizon Implementation

To meet real-time requirements in highly nonlinear environments, as we will see in our experiments, we adopt an MPC formulation. A critical observation in our implementation is the necessity of consecutive optimization iterations for constraint satisfaction. Because the exploration process is not explicitly aware of the constraints, raw samples often violate constraints. We observe that overly frequent sampling is counterproductive, as it disrupts the optimizer's ability to recover feasibility. By restricting exploration to the initiation of the MPC cycle and prioritizing successive DDP iterations, we ensure the control sequence is both diverse and respects constraints.

A challenge in warm-starting is the coupling between the sampling covariance $\Sigma{(Q_{uu}^{- 1})}$ and the nominal trajectories. While the control sequence $U^{(n)}$ can be shifted for warm-starting, the state sequence $X^{(n)}$ obtained by shifting inevitably diverges from those obtained by applying $U^{(n)}$ to the system with initial state $x_{t}$. Because feedback gains $K$ and sampling covariances $\Sigma$ are local approximations, this mismatch in state trajectory yields the simple temporal shift of feedback gain and covariance invalid. Consequently, a re-evaluation of the system's sensitivity via a backward pass is necessary at each time step to ensure the exploration remains aligned with the current local geometry.

We perform an initial backward pass at the start of each MPC loop to generate feedback gain and covariance. When the backward pass fails due to an ill-conditioned $Q_{uu}$, the algorithm samples with a pre-specified fixed covariance used in the initialization.

## Experiments

In this section, we provide two experimental results.

First, we conduct extensive simulations across four robotic systems, comparing seven algorithms, including DDP, ME-DDP variants, and MPPI variants. Second, we present a hardware experiment with a quadrotor to validate the performance and real-time feasibility of the ME-DDP variants.

### Numerical Experiments

The purpose of the experiment is to observe the properties of gradient-based (DDP), sampling-based (MPPI), and hybrid (ME-DDP) algorithms. We have comparison in performance and computational efficiency.

### Dynamics and Tasks

We tested four dynamics: 2D car, quadrotor, Ant, and Barkour (quadruped). The Ant and Barkour are simulated in the Jax-based physics engine Brax. The task for each system is to reach targets while navigating obstacle fields. We use circular (2D) or cylindrical (3D) obstacles, generated in a pseudo-random fashion. To ensure rigorous testing, we manually introduce additional obstacles in certain configurations to create challenging non-convex landscapes, including local-minima traps. Here, we provide brief descriptions of the systems. Ant and Barkour are shown in Fig. 6.

Figure 6: Experimental overview of Ant and Barkour. The task here is to reach the target while avoiding cylindrical obstacles.

### 2D car

The state $x \in {\mathbb{R}}^{3}$ comprises 2D positions and heading angle. The control $u \in {\mathbb{R}}^{2}$ consists of transitional and angular velocities. The discretization interval is 0.02 s. To investigate the effect of the MPC look-ahead horizon, we tested short (50 steps) and long (70 steps) horizons.

### Quadrotor

The state $x \in {\mathbb{R}}^{12}$ includes 3D positions, Euler angles, and their time derivatives. The control $u \in {\mathbb{R}}^{4}$ is the thrust force generated by four rotors. We follow the dynamics established in Luukkonen. The discretization interval is 0.01 s. We have short (50 steps) and long (70 steps) horizons as in the case of the 2D car.

### Ant

The Ant has four legs, with two joints. The state $x \in {\mathbb{R}}^{29}$ contains the 3D position and orientation of the body in the quaternion, the angles of the legs, and their time derivatives. The control $u \in {\mathbb{R}}^{8}$ is torque applied to the joints. The control loop runs at 0.01 s with a simulation step of 0.002 s, integrating 5 substeps per control cycle.

### Barkour

The quadruped has state $x \in {\mathbb{R}}^{37}$ comprising the 3D position, the body quaternion, and the three joint angles for each of the four legs, including the abductors, hips, and knees. The control $u \in {\mathbb{R}}^{12}$ is the command for the joint angles of the legs relative to the default angles that correspond to the standing posture. The control loop runs at 0.02 s with a simulation step of 0.006 s, integrating 3 substeps per control cycle.

We note that despite the higher dimensionality of the quadruped compared to the Ant, the use of a position-based (or angle-based) control interface provides a more structured search space, especially for MPPI. Position-level actions effectively abstract away the high-frequency dynamics and stability issues of torque-level control. This allows MPPI to discover task-relevant trajectories more efficiently. Typically, with torque-based control, many trajectories are wasted because random torque cannot even let robots stand stably. With position-based control, the optimizer can search for candidate trajectories within quasi-static equilibrium poses; therefore, the search space is significantly reduced to a region of low-cost configurations.

### Algorithms

We compare seven algorithms across three families: normal DDP, three ME-DDP variants, and three MPPI variants. For the Ant and Barkour tasks, the DDP-based algorithms are modified to operate on the manifold $S^{3}$ to handle quaternions. We project quaternion deviations into the tangent space. This ensures that the quadratic approximations remain valid while the unit-norm constraint is maintained via retraction back to the manifold.

For MPPIs, we have three different policy parameterizations and update rules. They are Unimodal Gaussian MPPI (UG-MPPI), Multimodal Gaussian MPPI (MG-MPPI), and UG policy with SV update (SV-MPPI). Here, the policy parameterizations correspond to UG-, MG-ME-DDP, and SV-DDP. The experiment is performed in MPC fashion.

A key distinction between these DDP and MPPI families lies in their mechanism for constraint satisfaction. Due to the requirement of differentiability, DDP-based methods incorporate constraints into the cost function using barrier functions explained in section Essential Components in SV-DDP. While this allows for gradient-based optimization, it can permit the algorithm to violate constraints. In contrast, MPPI utilizes indicator functions with a prohibitive cost to encode constraints. The control update in MPPI is a weighted average of the sampled control trajectories based on their associated costs. Consequently, infeasible trajectories are assigned negligible weights. This mechanism effectively excludes unsafe trajectories from the control computation. Although it does not theoretically guarantee constraint satisfaction, our experiments show that it works well in practice to maintain feasibility given that MPPIs find a path to the targets.

### Parameter Tuning and Optimization

The performance of both ME-DDP and MPPI is affected by hyperparameter selection, such as the sampling covariance in MPPI or the temperature parameter $\tau$ in ME-DDP. Although the sampling covariance in the ME-DDP variants arises naturally from the inverse Hessian of the $Q$ function, the temperature must still be tuned to balance exploration and exploitation. To ensure a fair comparison, we acknowledge that different algorithms may require different cost weightings to achieve peak performance, even when the underlying structure (e.g., quadratic in position error to goal) is shared.

Consequently, we utilize a Bayesian hyperparameter optimization framework, specifically the Tree-structured Parzen Estimator (TPE), to tune both the policy parameters and the cost weights for every algorithm using an open-source Neural Network Intelligence (NNI) toolkit.

For the tuning process, we define a high-level objective that prioritizes early entry into the target region and remaining within it for a prescribed duration, while penalizing the failure to reach the target within the specified time steps.

We use a fixed number of modes/trajectories $N = 8$ in ME-DDP variants. The samples/trajectories of MPPIs vary with the complexity of the system. For multimodal policies of MPPI, i.e., MG- and SV-MPPI, we use the same number of modes $N = 8$ and distribute an equal number of particles per mode.

### 2D Car and Quadrotor

We utilize two sparse and two dense obstacle environments for tuning. This diversity is necessary because algorithms tuned solely on simple environments tend to converge toward low temperatures or narrow sampling covariances, which fail to generalize to complex, non-convex landscapes. The number of samples used in MPPI is 2048 for the 2D car and 8000 for the quadrotor.

### Ant

Due to the higher computational cost of these high-dimensional systems, we utilize a single representative environment for the tuning process. The number of samples in MPPI is 8192.

### Barkour

As in the case of Ant, we use one environment for tuning, and the number of samples in MPPI is 8192.

A primary challenge in tuning the cost function for the quadruped Barkour is to balance its performance with the requirement for gait realism. When the yaw rotation has less penalty compared to the position, the quadruped rotates while avoiding obstacles and moving forward. Although it can successfully reach the target without colliding, we prefer a realistic gait to spinning as provided in Fig. 7.

Figure 7: Impact of independent coordinate tuning on Barkour. The absence of yaw-position coupling leads to excessive angular excursions and rotational instability, despite the optimizer, UG-MPPI, successfully hitting the target.

To mitigate the issue, we introduce coupled weights of position and yaw during the parameter search. This coupling ensures that when the tuner commands a high penalty on the position, the angle is also penalized to prevent spinning.

In our experiments, we observed a divergence in how optimizers responded to this coupling. While the coupling significantly improved the qualitative trajectory quality (realistic gait) of the DDP-based solvers, it led to a degeneration in the success rate of MPPIs. Consequently, while MPPI can achieve comparable or even higher performance in unconstrained scenarios, it produces physically controversial behaviors that are less suitable for realistic hardware deployment than DDPs.

All (Including Infeasible Trajectories)

Decouple position and yaw weights of the cost during tuning.

Table 1: Benchmark results comparing optimization-based ME-DDP variants and sampling-based MPPI baselines. The results are categorized into feasible and all (including infeasible) trajectories. Success rate shows the percentage of the trajectories that reach the goal. Time is the average first time step when the trajectory enter the goal region and stays there for ten time steps. Path is the average trajectory length. Violation is constraint violation computed over infeasible trajectories. The arrow ↑ indicates a higher value is preferred, while ↓ indicates a lower value is preferred.

(a) Sparse Environment for 2D Car

(b) Dense Environment for 2D Car

(c) Sparse Environment for Quadrotor

(d) Dense Environment for Quadrotor

Figure 8: Trajectory comparisons for 2D Car and Quadrotor environments. Within each panel, the left image shows DDP, and the right shows MPPI.

Figure 9: Result of Ant experiments. Trajectories get stuck at poor local minima, and three distinctive trajectories that successfully reach the target via SV-DDP are presented.

Figure 10: Result of Barkour experiments. Trajectories get stuck at poor local minima, and three distinctive trajectories that successfully reach the target via SV-DDP are presented.

### Results

To capture the stochastic nature of the algorithms, we run ten trials per environment except for the normal deterministic DDP. We have 16 environments for 2D car and quadrotor (comprising eight sparse and eight dense configurations), and ten environments for Ant and Barkour. This resulted in a total of 160 trials for the car and quadrotor experiments and 100 trials for the Ant and Barkour, from which we provide statistics. The overviews of the experiments are shown in Fig. 8 for the 2D car and quadrotor, Fig. 9 for Ant, and Fig. 10 for Barkour.

### Performance

Table. 1 shows the statistics of the results. We have two categories of results based on the constraint violation. The first group is feasible trajectories. This group includes trials where the system successfully reached the goal region (defined by an $L_{2}$ norm less than $0.3$) while maintaining a maximum obstacle constraint violation of less than $10^{- 6}$. For this group, we report the Success rate \[%\], the mean time step to steady state denoted as Time. This metric is defined as the first time step the agent enters and remains in the goal region for at least 10 consecutive steps. Finally, we report the mean path length denoted as Path. The second group relaxes the requirement of constraint satisfaction. This group represents a broader set of trials that reached the goal but allowed for constraint violations. In addition to the three metrics mentioned above, we provide the average constraint violation (Violation). We have the movies of the 2D car in [extension 1](2606.00737v1/anc/extension1.mp4), Quadrotor in [extension 2](2606.00737v1/anc/extension2.mp4), Ant in [extension 3](2606.00737v1/anc/extension3.mp4), and Barkour in [extension 4](2606.00737v1/anc/extension4.mp4). For Barkour, we also provide the results for MPPIs without position-yaw coupling as described in the Parameter Tuning and Optimization section.

The ME-DDP variants consistently outperform standard deterministic DDP, demonstrating that the exploration mechanism helps optimizers explore and find better local minima.

In low-dimensional systems (e.g., 2D car, quadrotor), gradient-based methods exhibit a superior success rate and efficiency through shorter time and path length. Our mechanism using local geometric information, e.g., the gradient and Hessian for optimization and the Hessian for sampling covariance, outperforms purely sampling methods. This suggests that for these systems, local geometric information, specifically the gradient and Hessian, is sufficient to characterize the cost landscape.

In high-dimensional locomotion, the cost landscape is characterized by numerous local minima, making the role of exploration critical. The results demonstrate that while ME-DDP achieves a higher overall success rate, MPPI is capable of steering the system more aggressively, as evidenced by shorter completion times and path lengths. This suggests that while gradient-based methods like ME-DDP often converge to the local basins of their nominal trajectories, MPPIs can discover solutions that DDPs cannot find, such as the yaw-rotation in Barkour (Fig. 7) or the jumping gait in the Ant environment presented in extension 3. Essentially, MPPI can potentially find superior, high-energy modes that DDP cannot, at the cost of a higher failure rate due to the lack of gradient-guided refinement.

Although multimodal policies are designed to capture diverse paths, the results suggest that their efficacy depends heavily on the degree of mode separation and the quality of representative trajectories. In our experiments, we observed that an unimodal policy can sometimes outperform other policies in both DDPs and MPPIs. This is because when the policy fails to separate the trajectories into distinct, meaningful classes, it has a lower local sampling density than the unimodal policy. Furthermore, it fails to provide a broader exploration capability. Consequently, they cannot be as efficient as a focused unimodal policy. While it remains challenging to draw a universal conclusion on which algorithm consistently outperforms the others across all domains, SV-DDP demonstrates remarkable reliability, consistently maintaining a success rate equal to or greater than 80 %.

Table 2: Computational performance benchmark. Comparison of mean execution time and standard deviation [ms] of one time step for the 2D car and quadrotor systems across two look-ahead horizons (TMPC = 50, 70).

### Computational Time

We compare computational performance of the DDP, ME-DDP variants, and UG-MPPI using both 2D car and quadrotor dynamics across two look-ahead horizons ($T_{mpc} = 50$ and $T_{mpc} = 70$). Both algorithms are implemented in JAX Bradbury et al.. Statistics were computed over 200 MPC time steps. As shown in Table 2, MPPI exhibits significantly faster computational speed compared to DDP-based methods. This is because MPPI bypasses the computation of the gradient and Hessian that are required for DDPs during their backward pass. Although the exploration mechanisms in ME-DDP variants introduce additional computational overhead to the normal deterministic DDP, they still meet real-time requirements. Specifically, given the discretization intervals of 20 ms for the 2D car and 10 ms for the quadrotor, the optimization finishes before the next control cycle, ensuring the feasibility of the proposed approach for robotic control. Furthermore, the low execution variance observed across all methods indicates a highly deterministic timing profile, which is critical for maintaining stable control of systems.

For the computational benchmark, we focus on the 2D car and quadrotor to ensure that the timings reflect the algorithmic complexity of the optimizers rather than the overhead of the physics engine. Using simple dynamics, we isolate the problem of heavy computation of the propagation of dynamics and other steps in the optimization loop. By doing so, we can provide a clearer assessment of the real-time feasibility of the algorithms.

All timing comparison experiments were conducted on a system equipped with an Intel i9-13900K CPU, a 64Gb of system memory, and an NVIDIA RTX4090 GPU.

### Hardware Experiments

To validate the real-time performance and robustness of the proposed ME-DDP framework, we conducted a series of hardware experiments using a quadrotor platform. While simulations provide a controlled environment for algorithmic comparison, physical hardware introduces real-world challenges such as sensor noise and aerodynamic turbulence. In this section, we provide experimental setup and results.

### Hardware and Experimental Setup

The experimental platform is a custom-built quadrotor, as illustrated in Fig. 11. The system architecture is divided into three primary components: sensing, computation, and flight control.

Figure 11: The quadrotor platform used for experimental validation.

### State Estimation

To provide global state estimation, we utilize a VICON motion capture system. The quadrotor's full state is estimated from VICON data using EKF of the PX4-based flight controller.

### Ground Station and Optimization

A ground station receives the state telemetry via a Local Area Network. This station serves as the primary computational resource, computing the DDPs in MPC for trajectory optimization. The optimized control sequences are then sent back to the vehicle via a dedicated Wi-Fi link. The control frequency is set to 10 Hz.

### Onboard Systems

The vehicle is equipped with a Raspberry Pi onboard computer, which acts as the bridge between the ground station and the flight hardware. The onboard computer communicates with a flight controller. The controller runs position control based on the optimal state trajectory computed by DDPs. The controller translates the received control commands (positions) into low-level motor signals.

### Results

We test the performance of the DDP family, i.e., standard deterministic DDP and three ME variants (UG-ME-DDP, MG-ME-DDP, and SV-DDP), across two environments with different cylindrical obstacle configurations. An overview of the experiment is visualized in Fig. 12. To evaluate the robustness of each algorithm and characterize the stochastic behavior inherent in the ME-DDP variants, we conduct multiple trials for each algorithm across different environments.

Instead of physical obstacles, we used virtual representations. For qualitative evaluation, these virtual obstacles are overlaid on a top-down camera feed of the experimental arena. In [extension 5](2606.00737v1/anc/extension5.mp4) and [extension 6](2606.00737v1/anc/extension6.mp4), we present a synchronized side-by-side visualization, with the overlaid real-world video on one side and the corresponding ROS visualization on the other.

Figure 12: 3D visualization of a hardware experiment.

(a) Environment 1: Forest of obstacles

(b) Environment 2: Forest with poor local minima/deadlocks

Figure 13: Representative resulting trajectories from hardware experiments in two different environments. The drone positions were captured at 0.5 s intervals. Obstacles are colored based on their states. Blue indicates a collision-free, while red denotes a collision verified by ground truth position. In the left panel of (b), the quadrotor is captured at a deadlock.

The results of the experiments are provided in Table. 3, and the trajectories of the quadrotor and overlaid obstacle are shown in Fig 13. Environment 1 shown in Fig 13 (a) is a forest of obstacles. As illustrated by the overlaid trajectories, without exploration, the algorithm finds a simple straight path, which acts as a detour to avoid the obstacles. With exploration, on the other hand, it actively explores the cost landscape and discovers shorter, more direct passages through the forest.

Environment 2 in Fig 13 (b) has some specific concave configurations designed to induce multiple poor local minima that can cause deadlocks. In addition to these, the environment incorporates forest-type configurations, as in environment 1. This environment tests the capability of the proposed sampling-based policies to escape these local minima. Furthermore, it simultaneously examines the exploration capability demonstrated in environment 1.

In Table 3, we classify each trial into four categories. First, a trial is classified as Safe Success, when the quadrotor reaches the target without violating constraints. This represents the ideal outcomes. Second, the category Goal with Coll. is for the cases where the quadrotor reaches the target but hits obstacles. For these two categories, we provide the average time to reach the target. Finally, Failure to Goal represents cases where the quadrotor fails to hit the target, which we further divide into two groups based on the failure modes. Deadlock without Coll. occurs when the quadrotor is captured by a poor local minimum and spends too much time there. Coll. is for cases where the quadrotor can escape from the deadlock, but subsequently collides with an obstacle and times out. We distinguish between these two modes to provide a more granular analysis of constraint satisfaction.

Overall, the sampling mechanism facilitates exploration, and since the constraints are encoded as part of the cost, it also facilitates constraint satisfaction.

The hardware results confirm the trends observed in simulation, where the multimodal policy fails to provide better solutions compared to the standard unimodal one. We observed that without an explicit separation mechanism, the multimodal policy essentially becomes a unimodal one with fewer trajectories.

In this case, the multimodal policy has a lower local sampling density than the unimodal policy. Furthermore, it fails to provide a broader exploration capability. Consequently, it may act as a middle ground of poor performance: it is not as efficient as a focused unimodal policy, nor as diverse as a SV policy.

This phenomenon explains the higher deadlock rates observed for the MG-ME-DDP. The policy wasted its exploration budget without successfully identifying alternative routes. In contrast, the unimodal UG-ME-DDP prioritizes a high-resolution search around the most viable candidate.

Goal with Coll.

Deadlock without Coll.[%]

Table 3: Hardware Performance Analysis. Outcomes are categorized into successful runs and failures with collision. Failures are further distinguished by whether the quadrotor reached the target (Goal with Coll.) or spent too much time on a poor local solution and cannot reach the target with or without collision (Deadlock without Coll./Coll.). The sum of the four outcome categories for each method equals 100 %.

## Conclusion

This work builds upon the Maximum Entropy (ME) framework to provide a unified perspective on the hybrid control mechanism that combines gradient- and sampling-based optimization.

While the core objectives of the ME framework have been previously established, we provide an analytical foundation that clarifies the role of the control Hessian $Q_{uu}$. Specifically, we provide a rigorous way of understanding the physical and mathematical interpretations of sampling from the inverse of $Q_{uu}$, revealing how this mechanism interacts with the non-convex cost landscapes inherent in robotics.

Our benchmarking across four systems in simulation reveals a distinct trade-off between structured optimization and stochastic exploration, advocating for a hybrid optimization approach that moves beyond pure sampling:

Low-Dimensional Systems (2D Car, Quadrotor): In these systems, ME-DDP variants demonstrate the benefits of leveraging local information for optimization and exploration. We found that the local gradient and Hessian provided by the DDP backward pass achieve superior success rate, and more efficient path lengths compared to MPPIs that rely on pure sampling.

High-Dimensional Systems (Ant, Barkour): In complex systems, ME-DDP remains highly reliable, maintaining a high overall success rate due to its structured refinement. However, we observed that MPPI is capable of discovering global modes that DDP-based methods may miss. While MPPI can struggle with success rates due to the lack of gradient-based refinement, its exploratory nature offers a unique advantage in discovering non-local solutions.

Regarding practical implementation, we demonstrate that while MPPI is computationally efficient per iteration, our DDP-based variants are sufficiently fast for real-time quadrotor control. We validate the efficacy of the algorithms through hardware experiments with a quadrotor navigating cluttered environments, proving that the proposed hybrid approach is robust for real-world deployment.

We conclude that for most robotics applications, providing a rigorous local structure through the ME-DDP framework offers a reliable path to high-performance control while remaining computationally feasible for hardware deployment.

Future research directions include implementing the full feedback structure of the optimal controller on hardware, exploring alternative mechanisms for constraint satisfaction beyond relaxed-$\log$ barrier functions, and establishing theoretical convergence guarantees and conditions.

## Author Contributions

Yuichiro Aoyama: Conceptualization, Formal analysis, Investigation, Software, Methodology, Visualization, Writing-original draft. Minchan Jung: Conceptualization, Formal analysis, Investigation, Software, Methodology, Visualization, Validation, Writing-review & editing. Akash Ratheesh: Investigation, Software, Methodology, Visualization, Writing-review & editing. Evangelos A. Theodorou: Conceptualization, Supervision, Project administration, Writing-review & editing.

## Statements and Declarations

### Ethical considerations

This article does not contain any studies with human or animal participants.

### Consent to participate

This article does not contain any studies with human or animal participants.

### Consent for publication

Not applicable. {dci} The author(s) declared no potential conflicts of interest with respect to the research, authorship, and/or publication of this article. {funding} The author(s) disclosed receipt of the following financial support for the research, authorship, and/or publication of this article:

Akash Ratheesh and Evangelos A. Theodorou were supported by the National Aeronautics and Space Administration under University Leadership Initiative \[grant number 80NSSC22M0070\] and the Army Research Office \[grant number W911NF2010151\].

Minchan Jung was supported by Korea Institute for Advancement of Technology (KIAT) grant funded by the Korea Government (MOTIE), Human Resource Development Program for Industrial Innovation (Global) \[grant number RS-2024-00435406\].
