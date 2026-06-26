<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Differentiable Model Predictive Control on the GPU

Topics include Model predictive control, Differentiable optimization, Graphics processing unit acceleration, Sequential quadratic programming, Differentiable programming.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces a GPU-oriented differentiable MPC solver based on SQP and a structured preconditioned conjugate-gradient routine. The paper targets the hardware bottleneck that makes differentiable MPC attractive in principle but difficult to scale in learning pipelines.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Differentiable model predictive control (MPC) offers a powerful framework for combining learning and control. However, its adoption has been limited by the inherently sequential nature of traditional optimization algorithms, which are challenging to parallelize on modern computing hardware like GPUs. In this work, we tackle this bottleneck by introducing a GPU-accelerated differentiable optimization tool for MPC. This solver leverages sequential quadratic programming and a custom preconditioned conjugate gradient (PCG) routine with tridiagonal preconditioning to exploit the problem's structure and enable efficient parallelization. We demonstrate substantial speedups over CPU- and GPU-based baselines, significantly improving upon state-of-the-art training times on benchmark reinforcement learning and imitation learning tasks. Finally, we showcase the method on the challenging task of reinforcement learning for driving at the limits of handling, where it enables robust drifting of a Toyota Supra through water puddles.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Differentiable optimization tools enable leveraging the structured and precise outputs of optimization algorithms as inductive biases in machine learning, reducing data requirements and enforcing constraints. These methods also enable data-driven tuning of optimization algorithms, reducing time-consuming manual expert-driven development using data. In particular, differentiable model predictive control has many applications, such as in motion planning, parameter estimation and tuning, reinforcement learning, imitation learning, and end-to-end planning and control.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, the adoption of differentiable optimization is hindered by the sequential nature of optimization tools: Efficient parallelization on graphics processing units (GPUs) remains difficult, both for solving the optimization problem (the forward pass) and for computing gradients (the backward pass). Recent methods for differentiable optimal control, such as only run on central processing units (CPUs) to leverage the time-induced sparsity of optimal control problems (OCPs) via sequential algorithms such as the iterative linear quadratic regulator (iLQR). Overcoming this computational bottleneck could enable scaling up to large datasets and expressive architectures, fully utilizing the benefits of modern deep learning.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose Differentiable Model Predictive Control (DiffMPC): a new tool for differentiable optimal control to solve and differentiate through optimal control problems of the form where the costs, equality constraints, and initial conditions are parametrized by parameters $\theta$, which could represent the weights of a neural network (parameterizing the cost $c(\cdot)$ or constraints $f(\cdot)$), the outputs of an intermediate neural network layer, or the parameters of a physics-based model. DiffMPC is tailored for execution on the GPU by leveraging the structure of OCP: The core of the solver is a preconditioned conjugate gradient (PCG) routine introduced in to solve the linear system arising from the optimality conditions of OCP. This routine leverages the sparse structure of OCP to expose parallelism over time $t$, and enables warm-starting across problem instances. DiffMPC is written in JAX to simplify deployment in machine learning applications.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Numerical and experimental results using DiffMPC show the following: Significant acceleration on the GPU: Comprehensive benchmarking against the state-of-the-art differentiable optimization libraries mpc.pytorch, trajax, and Theseus show consistent speedups of more than $4\times$ when solving and differentiating OCP. These experiments include reinforcement learning (RL) and imitation learning (IL) examples, which are common applications of differentiable optimal control. These speedups primarily come from a PCG routine tailored for GPU execution and several related design choices in DiffMPC that exploit problem structure for parallelization.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reliably drifting a Toyota Supra via domain randomization and reinforcement learning: We use DiffMPC to automatically tune an MPC controller for driving at the limits of handling and ensure robustness to model mismatch, such as water puddles on the road. Specifically, we use domain randomization over the nonlinear dynamics to learn cost and vehicle parameters for the controller via reinforcement learning. In this application, due to the unstable nature of driving at the limits of handling where tire forces are saturated and the vehicle is prone to spinning out, large batches are conducive to robust training, motivating the use of the proposed GPU-accelerated differentiable optimization framework. Results demonstrate significantly improved performance on a Toyota Supra drifting through water puddles (Figure 8).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Primer on Differentiable Optimization", "weight": 1.0} -->

Next, we provide background on differentiable optimization (DO) used in the design of DiffMPC. Consider the generic parametric, equality-constrained, optimization problem where $z\in\mathbb{R}^{n}$ are optimization variables, $\theta\in\mathbb{R}^{p}$ are parameters, $f:\mathbb{R}^{n}\times\mathbb{R}^{p}\to\mathbb{R}$ is a cost function, and $g:\mathbb{R}^{n}\times\mathbb{R}^{p}\to\mathbb{R}^{q}$ defines equality constraints.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Primer on Differentiable Optimization", "weight": 1.0} -->

The solution $z=z(\theta)$ and its associated Karush-Kuhn-Tucker (KKT) multipliers $\lambda=\lambda(\theta)\in\mathbb{R}^{q}$ must satisfy the KKT conditions where $L(z,\lambda,\theta):=f(z,\theta)+\lambda^{\top}g(z,\theta)$ is the Lagrangian of P.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Primer on Differentiable Optimization", "weight": 1.0} -->

The forward pass consists of solving the optimization problem P. Many solvers leverage the structure of P and its KKT conditions, such as its sparsity, to enable efficient numerical resolution. In the context of optimal control, for instance, the iLQR method leverages the sparse-in-time structure of OCP and uses Riccati recursions to break the optimization problem into smaller one-step problems that are solved recursively over time $t=0,\dots,T$. These operations are, however, iterative and do not fully leverage the parallelism of GPUs.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Primer on Differentiable Optimization", "weight": 1.0} -->

The backward pass computes the sensitivities of the solution to P with respect to the parameters $\theta$. For efficiency, many methods use the implicit function theorem (IFT) for this sensitivity computation: By defining the primal-dual pair $w{=}(z,\lambda)$ solving P, where we used $F(z,\lambda,\theta)=0$ so that $\frac{\mathrm{d}F}{\mathrm{d}\theta}=0$ in the first equality. The invertibility of the KKT matrix $\frac{\partial F}{\partial w}$ follows from the IFT under suitable assumptions. Thus, computing the sensitivity matrix $\frac{\partial w}{\partial\theta}$ requires solving $p$ linear systems $\frac{\partial F}{\partial w}\frac{\partial w}{\partial\theta_{i}}=-\frac{\partial F}{\partial\theta_{i}}$, which enables computing Jacobian-vector products (JVP) for downstream uses.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Primer on Differentiable Optimization", "weight": 1.0} -->

In machine learning applications, one typically uses the gradient of a function $\ell:\mathbb{R}^{n}\to\mathbb{R}$ of the solution $z$ to P. Such gradients can be more efficiently computed using the vector-Jacobian product (VJP) Computing the VJP in only requires solving one linear system $\frac{\partial F}{\partial w}\xi=(\frac{\partial\ell}{\partial z},0)$, and is thus more efficient than using a JVP, see Appendix A.1 vs Jacobian-vector products (JVPs) ‣ Appendix A Solver: Additional Details ‣ Differentiable Model Predictive Control on the GPU") for further details.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Primer on Differentiable Optimization", "weight": 1.0} -->

Efficient differentiable solvers leverage the structure of P to quickly compute solutions $z$, and exploit the sparsity structure of the KKT matrix $\frac{\partial F}{\partial w}$ to solve the linear system $\frac{\partial F}{\partial w}\xi=(\frac{\partial\ell}{\partial z},0)$ to evaluate the VJPs. In the next section, we describe such a solver for optimal control problems that is designed to leverage parallelism to run efficiently on the GPU.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Differentiable Model Predictive Control on the GPU", "weight": 1.0} -->

DiffMPC enables solving and differentiating through optimal control problems (OCPs) of the form with separable costs $c_{t}^{x,\theta},c_{t}^{u,\theta}$, equality constraints $f_{t}^{\theta}$, and initial conditions $x_{s}^{\theta}$ parametrized by $\theta$. In the next sections, we describe its forward pass (solving OCP), its backward pass (computing gradients with respect to $\theta$), and discuss design choices for efficient deployment on the GPU.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Forward Pass: Solving OCP via Sequential Quadratic Programming (SQP)", "weight": 1.0} -->

To solve OCP, which is in general non-convex, we use the sequential quadratic programming (SQP) scheme with a line search in Algorithm 1. At each iteration of the SQP scheme, given an initial guess for the solution $z$, we approximate the cost of OCP by a linear-quadratic function and linearize the dynamics constraints, to obtain the parametric quadratic program (QP): where $z=(x_{0},u_{0},\dots,x_{T-1},u_{T-1},x_{T})$, and $(Q,q,R,r,A^{+},A,B,C)$ depend on the parameters $\theta$, and are computed in parallel over OCP problem instances and time steps $t=0,\dots,T$: and

<!-- chunk {"id": "body-0017", "role": "body", "section": "Forward Pass: Solving OCP via Sequential Quadratic Programming (SQP)", "weight": 1.0} -->

To ensure that the matrices $(Q,R)$ are positive definite, we project them onto the positive definite cone as.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Backward Pass: Computing Sensitivities via the Implicit Function Theorem", "weight": 1.0} -->

Given a solution $z$ to OCP computed via SQP, DiffMPC computes the sensitivities with respect to $\theta$ using (see Algorithm 2). The most expensive step consists of solving the linear system This linear system is the same as the linear system in (6 ‣ 3 Differentiable Model Predictive Control on the GPU ‣ Differentiable Model Predictive Control on the GPU")) used for the forward pass, with $(-b,d)$ replaced with $(\frac{\partial\ell}{\partial z},0)$. Importantly, the KKT matrix is pre-computed in the forward pass.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Solving the Linear Systems while Leveraging Parallelism", "weight": 1.0} -->

The efficiency of DiffMPC relies on an efficient and GPU-friendly routine for solving the linear systems (6 ‣ 3 Differentiable Model Predictive Control on the GPU ‣ Differentiable Model Predictive Control on the GPU")) and that leverages the structure of the KKT matrix in (5 ‣ 3 Differentiable Model Predictive Control on the GPU ‣ Differentiable Model Predictive Control on the GPU")). Specifically, DiffMPC uses the preconditioned conjugate gradient (PCG) method with tridiagonal preconditioning introduced. We briefly describe this method below.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Solving the Linear Systems while Leveraging Parallelism", "weight": 1.0} -->

To solve the linear system (6 ‣ 3 Differentiable Model Predictive Control on the GPU ‣ Differentiable Model Predictive Control on the GPU")), we first form the Schur complement of the KKT system and solve for $\lambda$ and $z$ sequentially: Solving is done similarly, by replacing $(-b,d)$ with $(\frac{\partial\ell}{\partial z},0)$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Solving the Linear Systems while Leveraging Parallelism", "weight": 1.0} -->

Similarly, for the second step, using the structure present in $(G,H)$, the variables $z_{t}=(x_{t},u_{t})$ are computed in parallel over $t=0,\dots,T$ to maximize efficiency on the GPU: for all $t=0,\dots,T-1$, with $A_{-1}^{+}=I$ with the last state given by $x_{T}=-Q_{T}^{-1}\left(q_{T}+A_{T-1}^{+\top}\lambda_{T}\right)$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Solving the Linear Systems while Leveraging Parallelism", "weight": 1.0} -->

While PCG is an iterative routine, we found that it is particularly suitable for differentiable optimization on the GPU as 1) the preconditioner $\Phi^{-1}$ reduces the condition number of $S$ while retaining the parallel-friendly block-tridiagonal structure of $S$, thus enabling parallelization, and 2) its warm-starting capabilities, which are useful when repeating calls to DiffMPC in an MPC setting.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Additional Implementation Details and Properties of DiffMPC", "weight": 1.0} -->

Next, we describe details and design choices of DiffMPC that optimize for speed and parallelism.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Additional Implementation Details and Properties of DiffMPC", "weight": 1.0} -->

Line search: After solving QP, a standard line search is used to select an appropriate step towards the solution of OCP. The merit function is defined as a weighted sum of the cost and constraints, and is evaluated in parallel over different predefined step sizes to further leverage GPU parallelism. Details about the line search are in Appendix A.3.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Additional Implementation Details and Properties of DiffMPC", "weight": 1.0} -->

Warm-starting and reusing computations: The forward and backward passes of DiffMPC can be warm-started with previously computed solutions to the SQP and PCG loops. Also, since the KKT matrix for the forward pass is the same for the backward pass, multiple matrices from the forward pass are passed to the backward pass instead of being recomputed. Figure 2 summarizes data flows.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Additional Implementation Details and Properties of DiffMPC", "weight": 1.0} -->

Exact SQP vs iLQR: To form QP, an exact SQP scheme would use cost matrices corresponding to the Hessian of the Lagrangian of OCP $(Q,R):=\nabla^{2}_{z}L=\nabla^{2}_{z}c+\nabla^{2}_{z}\lambda^{\top}f$, which requires using the KKT multipliers associated with the equality constraints and additional modifications (e.g., Gauss-Newton approximations) to ensure reliable descent on the problem and that $(Q,R)$ are positive definite. Similarly, the constraints curvature could be accounted for in the backward pass, leading to a different KKT matrix (see, e.g., Frey et al. ). As in (and as is standard practice in SQP and done in iLQR), we neglect the curvature of the dynamics to formulate the cost matrices of QP as $(Q,R):=\nabla^{2}_{z}c$ and rely on a line search for robustness.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Additional Implementation Details and Properties of DiffMPC", "weight": 1.0} -->

This scheme may result in degraded accuracy for the gradients. However, it is easier to implement, works well in many applications, and does not require computing second-order derivatives of the constraints that can be computationally expensive to evaluate.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Additional Implementation Details and Properties of DiffMPC", "weight": 1.0} -->

Parallelism, DiffMPC vs iLQR: Classical algorithms for solving OCP such as iLQR use Riccati recursions, and thus operate sequentially over time $t=0,\dots,T$ to solve OCP. In contrast, DiffMPC benefits from multiple sources of parallelism over time steps. First, all matrices are evaluated in parallel for each SQP iteration (e.g., $(Q_{t},R_{t},A_{t},\dots)$ and blocks of $(S,\Phi^{-1})$). Second, while the PCG routine (Algorithm 3) is iterative, it leverages parallelization over time $t$ for both the forward and backward passes. The warm-starting capabilities of PCG enable fast numerical resolution in MPC applications, whereas the Riccati recursions of iLQR do not leverage warm-starting over problem instances. Leveraging parallelism, warm-starting capabilities, and batching over problem instances makes DiffMPC well-suited for learning policies on the GPU.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Additional Implementation Details and Properties of DiffMPC", "weight": 1.0} -->

1:Inputs: Initial guess (x, u, λ), Tolerance ϵ 3:while not converged do 7: Evaluate QP solution $(x^{+}\hskip-4.0pt,u^{+})$ Eq. 11 8: $(x,u)\leftarrow\text{Linesearch}(x^{+}\hskip-4.0pt,u^{+}\hskip-4.0pt,x,u)$ Sec. A.3 9:Return: Solution (x, u, λ), QP matrices (Q, R, …), Schur matrices (S, Φ−1) Algorithm 1 Forward Pass (SQP).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Additional Implementation Details and Properties of DiffMPC", "weight": 1.0} -->

1:Inputs: Forward pass solution z = (x, u) and matrices (S, Φ−1), Loss gradient $\frac{\partial\ell}{\partial z}$, Initial guess λ̃ 2:Evaluate γ̃ using $(-b,d)\leftarrow(\frac{\partial\ell}{\partial z},0)$ Eq. 8 5:Evaluate $\frac{\partial\ell}{\partial\theta}\leftarrow-\frac{\partial F}{\partial\theta}^{\top}{\begin{bmatrix}\widetilde{z}\\\widetilde{\lambda}\end{bmatrix}}$ Eq. 3 6:Return: Gradient $\frac{\partial\ell}{\partial\theta}$, solution λ̃ Algorithm 2 Backward Pass (sensitivities).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Reinforcement Learning and Imitation Learning", "weight": 1.0} -->

DiffMPC is a fully differentiable policy, making it compatible with standard learning paradigms such as reinforcement learning (RL) and imitation learning (IL): with an MPC policy $\pi^{\theta}$ parametrized in $\theta$: In, $R$ is a reward function, SimEnv is a simulator for the environment, and $\mathcal{D}_{\text{initial states}}$ is a distribution over initial states. In, $\mathcal{D}_{\text{demonstrations}}$ provides demonstration samples for imitation learning. In this work, we conduct RL using a differentiable simulation environment, though this is not required as DiffMPC could be used as a component of other differentiable policy architectures. Compared to black-box policies, DiffMPC can leverage physics-informed inductive biases through its dynamics model and through solving OCP. Its gradients can be computed as described in the previous section. Since the algorithm is tailored for GPUs, large batch sizes can be used for training.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Faster Solves and Learning on the GPU", "weight": 1.0} -->

We implement DiffMPC in JAX and evaluate it on reinforcement learning and imitation learning tasks. We compare it with three state-of-the-art differentiable solvers: the PyTorch-based nonlinear least-squares solver Theseus, the PyTorch-based iLQR solver mpc.pytorch, and the JAX-based iLQR solver Trajax.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Timing Results for Reinforcement Learning", "weight": 1.0} -->

We consider randomly-generated MPC problems with quadratic costs and affine dynamics constraints. Details about problem randomization are in the appendix. Since the problems are convex, we disable the line search for all methods and restrict all solvers to a single iteration, which enables a fairer comparison. The RL task consists of maximizing the reward $R(x,u):=-(\|x\|_{2}^{2}+\|u\|_{2}^{2})$ aggregated over $50$ environment time steps for a batch size of $64$ randomized environments, by learning the MPC's quadratic cost parameters. Forward- and backward-pass computation times measure the time to compute the aggregate reward over batched rollouts and their gradients with respect to the cost parameters. Statistics for each problem are averaged over 10 seeds. Details are in Appendix B.1 along with additional results on other problems.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Timing Results for Reinforcement Learning", "weight": 1.0} -->

Comparison of computation times. Figure 3 compares solve times of the different solvers. First, for this problem (and all tested, see Table 3 in the appendix), Theseus is the slowest, exceeding 80 sec when run on the CPU. This slowdown is likely due to not sufficiently exploiting the time-induced sparse structure of OCP. Second, mpc.pytorch and trajax are not significantly faster on the GPU than on the CPU, which can be attributed to their design based on sequential-in-time Riccati recursions. Third, on the CPU, DiffMPC lies in-between mpc.pytorch and trajax, so trajax should be preferred on the CPU as sequential Riccati recursions are better suited for CPU execution. However, on the GPU, DiffMPC is significantly faster than other solvers, with a 4 times speedup over the fastest baseline for this problem. This speedup is likely due to DiffMPC better leveraging parallelism over time in OCP.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Timing Results for Reinforcement Learning", "weight": 1.0} -->

In Appendix B.1, we provide additional results on other problems (including a nonlinear attitude stabilization task), where we also observe significant speedups ranging from $4$-$7$ times over trajax (the fastest baseline) across all tested problems.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Timing Results for Reinforcement Learning", "weight": 1.0} -->

Warm-starting. Using DiffMPC's PCG routine for solving the KKT systems enables warm-starting both the forward and backward passes. Figure 9 in the appendix reports speedups from warm-starting, computed as the ratio $\frac{\textrm{cold}-\textrm{warm}}{\textrm{cold}}$ comparing the RL computation times using DiffMPC and of DiffMPC with zero initial guesses provided to PCG. For the PCG exit tolerance $\epsilon=10^{-12}$ that is used in this section's results, warm-starting gives modest speedups of $4\%$ for both the forward and backward passes. These speedups increase to $11\%$ and $9\%$ for the forward and backward passes, respectively, if the tolerance is set to $\epsilon=10^{-4}$. Thus, we expect additional speedups for low tolerances and in applications where DiffMPC is used to replan at high frequencies.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Timing Results for Imitation Learning", "weight": 1.0} -->

Next, we evaluate the method on an imitation learning task with nonlinear dynamics. Following the setup, we use a cart-pole environment and cost parameters corresponding to expert imitation data collected by solving OCP. To this end, we minimize a standard mean-square-error imitation learning loss, as defined. The goal of this experiment is to evaluate end-to-end training speed on an imitation learning task, with each training loop consisting of solving a batch of nonlinear optimization problems, computing the imitation loss, backpropagating gradients, and updating weights. Details are in Appendix B.2. On the GPU, we compare DiffMPC against trajax, as it is the fastest baseline from the previous section. Figure 4 reports the training loss and model loss, defined as $\|\theta-\theta^{\star}\|_{2}$ where $\theta^{\star}$ are the true parameters of the policy used to generate the data. The losses are shown as a function of measured training time, stopping at 200 epochs. DiffMPC trains substantially faster (approximately a 2 times speedup), highlighting its efficiency for imitation learning.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Application to domain randomization for driving at the limits", "weight": 1.0} -->

Finally, we demonstrate the practical utility of DiffMPC in learning robust controllers for driving at the limits of handling under model mismatch. Existing methods for drifting remain sensitive to modeling errors, as unstable dynamics can cause small errors to quickly amplify and destabilize the vehicle. While prior works have developed learning-based and adaptive controllers, online adaptation alone may fail to recover control of a vehicle driving through varying road conditions due to limited actuation. Developing controllers that are robust to disturbances such as sudden friction loss from water puddles, and simplifying their tuning process that can be slow and expensive, is crucial for enabling safety-critical applications.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Application to domain randomization for driving at the limits", "weight": 1.0} -->

To this end, we use DiffMPC within an RL framework for the task of robustly drifting trajectories using domain randomization. We vary the simulator model $\mathcal{E}^{i}$ by adding water puddles on the road at random locations that reduce available tire forces by modifying physical parameters such as tire friction coefficients, and starting the simulations from varying starting conditions $x_{0}^{i}$. For each initial state-environment tuple $(x_{0}^{i},\mathcal{E}^{i})$, we generate closed-loop rollouts of 200 steps by repeatedly solving the MPC problem, applying the control $u_{t}^{\theta}$, and simulating the evolution of the system given the sampled environments $\mathcal{E}^{i}$. These simulation environments use high-accuracy dynamics integrators and account for control delays, which would be difficult to do in the MPC controller without increasing the complexity of OCP.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Application to domain randomization for driving at the limits", "weight": 1.0} -->

The total reward is aggregated over the batched rollouts, then backpropagated to learn the policy parameters $\theta$, which consist of the cost weights and the tire friction parameters in OCP. We found that using a large episode length ($>100$ time steps) and batch size ($\geq 32$) is necessary for robust training. We train the policy for 1000 steps with a batch size of 32, taking $14$ hours on an NVIDIA GeForce RTX 4090. Further details are in Appendix B.3.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Application to domain randomization for driving at the limits", "weight": 1.0} -->

Changes in parameters after training: MPC parameters pre- and post-training are in Figure 10 in the appendix. Baseline weights were manually tuned using domain knowledge and tests on a vehicle in nominal dry conditions. The learned policy has significantly decreased the rear tire friction coefficient in its prediction model (change of -13%) and decreased the cost term associated with sideslip angle errors in the objective function of OCP (change of -58%). These learned parameters are physically reasonable, but they would have been difficult to obtain by hand, given the surprisingly asymmetric reduction in rear tire friction coefficients. Using these parameters enables the policy to trade off higher sideslip tracking errors for increased robustness to water puddles, and selecting lower engine torques, resulting in more robust drifting as shown next.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Application to domain randomization for driving at the limits", "weight": 1.0} -->

Improved robustness in simulation: Figure 6 shows twenty roll-outs over randomized environments for the baseline and learned policies, as described in Appendix B.3. The learned policy is significantly more robust, succeeding in 100% of the trials compared to the 70% success rate of the baseline policy. The learned policy selects smaller steering angles and motor torques than the baseline. These actions result in drifting with lower sideslip (the angle between the longitudinal axis and the velocity vector of the vehicle) and lower wheel speed, which gives additional buffers to avoid saturating actuation limits and spinning out after drifting through water puddles. These changes result in significant robustness gains despite model mismatch.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Application to domain randomization for driving at the limits", "weight": 1.0} -->

Results on a Toyota Supra: The learned MPC policy is then deployed on a Toyota Supra drifting a donut trajectory through water puddles. Results are shown in Figures 8 and 8. Although RL training is only conducted on figure-8 trajectories, the learned policy transfers successfully to drifting a circle without additional tuning, thanks to the inductive biases of MPC. In contrast to the baseline that consistently spins out due to the water puddle, the learned policy applies lower engine torques to reduce wheel speeds and maintain lower controlled sideslip angles $\beta$ throughout the drifting manoeuver. Further results for drifting the figure 8 trajectory are in the appendix. Overall, these results show that training a differentiable MPC policy via RL and domain randomization can produce robust, transferable controllers for driving at the limits of handling.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Discussion and Limitations", "weight": 1.5} -->

While differentiable optimization tools often rely on iterative algorithms (such as gradient descent, SQP, and PCG), exploiting parallelism in the problem structure gives opportunities to leverage GPUs to efficiently solve such optimization problems. In this work, we exploit the time-induced sparsity of optimal control problems to yield an efficient differentiable optimization tool for model predictive control that outperforms existing tools when run on the GPU, even for modest batch sizes. This tool offers the strong inductive biases of model-based control in a package that better scales to the demands of data-driven methods, enabling integration of model-based and learning-based approaches.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Discussion and Limitations", "weight": 1.5} -->

Limitations and future work: First, additional inequality constraints can be accounted for in OCP by penalizing them in the cost, and control bounds can be accounted for in the dynamics (e.g., control bounds are enforced in the simulator for RL in Section 5). Handling such inequality constraints via augmented Lagrangian or interior-point methods might lead to more reliable convergence and higher-quality solutions. However, reliably differentiating through such problems remains challenging, since gradients can be discontinuous at the boundary of the constraints. Second, since DiffMPC is tailored to the GPU and implemented in JAX, it runs slower on the CPU than on the GPU. Rewriting the solver in C / C++ would give speedups over our JAX implementation, albeit other approaches using Riccati recursions might outperform DiffMPC on the CPU. Fourth, DiffMPC does not explicitly support tuning solver hyperparameters such as the maximum number of iterations or the PCG tolerance, though its ability to run in parallel over problem instances on the GPU might help tune such hyperparameters.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Discussion and Limitations", "weight": 1.5} -->

Finally, poor initial guesses for the solutions and parameters of differentiable MPC tools can result in divergence of the solver and hinder the downstream training pipeline, motivating future work towards robust initializations for differentiable optimization pipelines.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Discussion and Limitations", "weight": 1.5} -->

Acknowledgments. We thank Michael Thompson, Paul Brunzema, William Kettle, Jon Goh, Jenna Lee, Zachary Conybeare, Phung Nguyen, and Steven Goldine for their support with the experiments and the test platform.
