<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Global Sampling-Based Trajectory Optimization for Contact-Rich Manipulation via KernelSOS

Topics include Trajectory optimization, Robustness, Sampling-based methods, Optimization, Sampling, KernelSOS.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Contact-rich manipulation is challenging due to its high dimensionality, the requirement for long time horizons, and the presence of hybrid contact dynamics. Sampling-based methods have become a popular approach for this class of problems, but without explicit mechanisms for global exploration, they are susceptible to converging to poor local minima. In this paper, we introduce Global-MPPI, a unified trajectory optimization framework that integrates global exploration and local refinement. At the global level, we leverage kernel sum-of-squares optimization to identify globally promising regions of the solution space. To enable reliable performance for the non-smooth landscapes inherent to contact-rich manipulation, we introduce a graduated non-convexity strategy based on log-sum-exp smoothing, which transitions the optimization landscape from a smoothed surrogate to the original non-smooth objective. Finally, we employ the model-predictive path integral method to locally refine the solution. We evaluate Global-MPPI on high-dimensional, long-horizon contact-rich tasks, including the PushT task and dexterous in-hand manipulation. Experimental results demonstrate that our approach robustly uncovers high-quality solutions, achieving faster convergence and lower final costs compared to existing baseline methods.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contact-rich manipulation, such as pushing, grasping, and in-hand manipulation, is a fundamental task in modern robotics. These tasks typically involve high-dimensional, underactuated systems and hybrid contact dynamics, resulting in highly non-convex, non-smooth optimization landscapes. As a result, computing long-horizon optimal plans and control policies for contact-rich tasks remains a core challenge.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address this challenge, sampling-based optimization has recently received significant attention. By relying solely on function evaluations, these methods can handle highly nonlinear, non-smooth contact dynamics that induce complex cost landscapes, without requiring higher-order information such as gradients. In addition, enabled by recent advances in GPU-accelerated parallel simulation, sampling-based methods can efficiently evaluate large numbers of candidate control trajectories via massive parallel rollouts. These aspects make sampling-based methods particularly appealing for the contact-rich trajectory optimization problem.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Popular sampling-based approaches include Model Predictive Path Integral (MPPI), Cross-Entropy Method (CEM), and Covariance Matrix Adaptation Evolution Strategy (CMA-ES). These methods perform iterative stochastic optimization by sampling candidate trajectories and updating the solution based on the observed performance of those samples. A recent approach, DIAL-MPC, extends MPPI by incorporating annealing strategies to balance coverage and convergence, demonstrating promising performance on contact-rich problems. However, all of these methods are primarily local in nature, often leading to suboptimal convergence or task failure in contact-rich settings. This limitation becomes pronounced as task complexity, planning horizon, and system dimensionality increase. To improve global exploration, regularization terms that maximize entropy during sampling can be added to such formulations, yielding better exploration properties.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper highlights the potential of a recent global optimization method, Kernel Sum of Squares (KernelSOS), to overcome those limitations. KernelSOS provides a means to identify globally promising regions in non-parametric optimization settings. Unlike local sampling-based methods, KernelSOS constructs a global surrogate of the cost landscape from samples and performs global minimization of this surrogate via solving a Semidefinite Program (SDP). KernelSOS has been previously studied in domains such as optimal control and estimation in robotics, but its application to high-dimensional, long-horizon contact-rich problems has been out of reach.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, proposes a model-based first-order local solver to refine the coarse solution candidate, but fast and reliable local solvers are harder to come by in contact-rich problems. The method also requires extensive manual tuning for the problem class. However, for long-horizon tasks such as contact-rich manipulation, the cost landscape can vary significantly due to frequent contact mode switches and discontinuous dynamics, and there may not be a single optimal set of hyperparameters. Finally, the high non-convexity of contact-rich tasks, the sparse information content (large areas with no gradient where no contact happens), and difficult-to-discover local minima are a challenge for global sampling methods like KernelSOS. As a result, identifying promising regions of the search space may require prohibitively large numbers of samples, leading to computationally intractable SDP problems.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce Global-MPPI, a global sampling-based trajectory optimization framework for contact-rich problems, which addresses these challenges one by one. Our main contributions are as follows.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

A fully sampling-based framework: Global-MPPI integrates KernelSOS for global exploration and MPPI for local refinement. Both are sampling-based and thus do not require differentiable contact modeling, making them suitable for integrating complex and accurate physics simulators.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Graduating smoothing: We introduce a Graduated Non-Convexity (GNC) strategy based on log-sum-exp (LSE) smoothing, which provides a general mechanism for iteratively smoothing the optimization landscape, improving the exploration capabilities of KernelSOS.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Auto calibration for KernelSOS: We propose a calibration method that automatically and continuously adapts appropriate kernel parameters in KernelSOS based on maximizing the marginal likelihood of the function fit.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Validation on contact-rich tasks: We validate the performance of the proposed method on contact-rich manipulation tasks based on a GPU-accelerated physics simulator, including the PushT task and dexterous in-hand manipulation. The open-source implementation is made publicly available.^11^1Code will be released upon acceptance of the manuscript.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper is organized as follows. After reviewing contact-rich problems and sampling-based optimization methods for robotics in Sec. II, we formally state the problem formulation for contact-rich trajectory optimization in Sec. III. We then detail the proposed method in Sec. IV and present numerical experiments in Sec. V. We conclude with a discussion of the results and limitations in Sec. VI.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Contact-rich Optimization in Robotics", "weight": 1.0} -->

In recent years, learning-based methods, such as deep reinforcement learning and behavior cloning, have demonstrated impressive robustness in contact-rich tasks such as real-world quadruped locomotion and robotic manipulation. However, these methods typically require careful hyperparameter tuning and initialization, time-consuming training, and, in some cases, extensive data collection. The resulting policies are heavily dependent on the training setup, limiting their generalization to unseen tasks and environments.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Contact-rich Optimization in Robotics", "weight": 1.0} -->

The above methods implicitly handle complex contact interactions using stochastic approximations of system dynamics. An alternative line of work exploits these contact models and approximations more explicitly in optimal control frameworks, sometimes using complementarity-based formulations. Although they have demonstrated promising performance, these methods are inherently local and often require high-quality initial guesses, which are difficult to obtain in practice. Alternatively, contact-rich problems have also been studied through global optimization formulations. These methods typically cast the problem as a combinatorial optimization problem, which can be solved using mixed-integer programming or via convex relaxation,. Although such approaches can provide optimality guarantees, they do not scale with dimension and the number of contact modes and have therefore been limited to relatively simple systems.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B Sampling-based Methods", "weight": 1.0} -->

Sampling-based or zero-order methods have been widely applied in robotics due to their flexibility in handling arbitrary non-smooth dynamics and constraints, as well as parallelizability. These approaches rely solely on function evaluations and do not require gradient or higher-order derivative information, making them well-suited for incorporating non-differentiable simulators or real-world rollouts. Prominent methods such as MPPI and CMA-ES perform stochastic optimization by repeatedly sampling around a nominal solution and updating the sampling distribution. Although robust to non-smooth objectives, those methods remain fundamentally local in nature. Bayesian optimization (BO), on the other hand, incorporates global exploration by fitting a surrogate model of the objective and selecting new samples by maximizing an acquisition function that trades off exploration and exploitation. While the acquisition function is typically easier to optimize than the original objective, its maximization remains a non-convex problem and may be prone to local maxima. A recent contender among zero-order methods is KernelSOS. Like BO, KernelSOS constructs a global surrogate model within a prescribed function class.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Sampling-based Methods", "weight": 1.0} -->

However, instead of iteratively optimizing an acquisition function, KernelSOS directly minimizes the surrogate in a single step via solving an SDP, providing global optimality guarantees within the surrogate space.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-C Graduated Non-Convexity", "weight": 1.0} -->

Graduated Non-Convexity (GNC) is a widely used strategy for optimizing non-convex objective functions and has been successfully applied across domains, such as computer vision and machine learning. Existing GNC formulations, however, are often tailored to specific loss functions. For example, Yang et al. propose dedicated GNC strategies for the Geman--McClure and truncated least-squares losses. While effective, such formulations are inherently function-specific and therefore lack generality for arbitrary non-convex cost functions.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-C Graduated Non-Convexity", "weight": 1.0} -->

Motivated by these limitations, we propose a global, training-free, and non-parametric trajectory optimization framework for contact-rich problems. Our approach integrates a general, function-agnostic GNC strategy with KernelSOS for global optimization and MPPI for local refinement, both of which are sampling-based and particularly well-suited to contact-rich settings with non-convex, non-smooth cost landscapes.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Here, $x_{t}$ and $u_{t}$ denote the state and control input at time step $t$ and $T$ is the planning horizon. The control sequence is denoted by $\mathbf{u} = {\{ u_{0},u_{1},\ldots,u_{T - 1}\}}$. The functions $\ell_{t}{( \cdot )}$ and $\ell_{T}{( \cdot )}$ represent the stage cost and the terminal cost, respectively, $f_{dyn}{( \cdot )}$ denotes the contact-implicit dynamics, and $\mathcal{U}$ is the feasible control set. In practice, we employ the single-shooting formulation, in which the unknown state trajectory and dynamics constraints are eliminated by rolling out the system dynamics $f_{dyn}{( \cdot )}$ starting from the initial condition $x_{init}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

The problem thus simplifies to computing a feasible control sequence $\mathbf{u}$ that minimizes the resulting cumulative cost $\mathcal{J}{(\mathbf{u})}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

This problem is challenging due to several factors: First, the contact-implicit dynamics $f_{dyn}{( \cdot )}$ introduces non-smooth and highly non-convex behavior as contact modes change. As a result, the cost landscape often exhibits sharp, asymmetric basins and pronounced non-smoothness, which hinder efficient global exploration and may cause local methods to get trapped in suboptimal solutions. Second, as the task dimensionality increases, the search space of the control sequence $\mathbf{u}$ grows exponentially, substantially increasing the computational burden and the difficulty of achieving global coverage. Finally, successful manipulation typically requires long horizons, thereby further increasing the problem's dimensionality.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Method", "weight": 1.0} -->

To address the challenges of contact-rich trajectory optimization discussed in Section III, we introduce Global-MPPI, a global sampling-based trajectory optimization framework tailored for contact-rich problems. We start by providing an overview of the algorithm and methodological insights to explain why Global-MPPI enables effective global optimization over non-smooth landscapes. We then present technical details for each component of the algorithm, along with practical considerations for its successful application to contact-rich tasks.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-A Overview of Global-MPPI", "weight": 1.0} -->

Global-MPPI is a global sampling-based trajectory optimization framework designed to address contact-rich tasks. Fig. 2 provides a univariate example to illustrate its high-level idea. Our approach integrates three coupled components that enable reliable global exploration and local convergence toward the global optimum (orange star) in highly non-smooth, non-convex cost functions (orange curve). First, we employ a GNC strategy based on LSE smoothing. By gradually decreasing the smoothing parameter $\sigma_{lse}$, the optimization landscape transitions from a smoothed convex function to the original non-smooth cost function (green curve), allowing coarse-to-fine global exploration. Second, at each stage, we leverage KernelSOS to identify the global solution (green cross) through surrogate minimization (dashed curve) via solving an SDP. Crucially, KernelSOS operates on the smoothed cost function, which, as we will show, leads to better performance than if we were to use the original function evaluations. Finally, we employ MPPI as a local optimizer, initialized with the global solution candidate from KernelSOS, to perform local refinement (red cross) of the LSE-smoothed surrogate function.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-A Overview of Global-MPPI", "weight": 1.0} -->

Together, these components enable Global-MPPI to systematically explore highly non-smooth, non-convex cost landscapes, avoid local minima, and progressively converge to high-quality solutions in non-parametric, contact-rich settings.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-B Graduated Non-Convexity via Log-Sum-Exp Smoothing", "weight": 1.0} -->

To address non-convex and non-smooth optimization landscapes, we adopt a GNC approach that solves a sequence of surrogate optimization problems with gradually increasing non-convexity, enabling coarse-to-fine exploration of the optimization landscape. The key idea of GNC is to first optimize a strongly smoothed, convex surrogate of the original problem, which is easier to optimize, and then gradually increase the level of non-convexity until the original non-convex objective is recovered. The solution obtained at each stage is used to warm-start the subsequent optimization stage. This continuation process effectively enlarges the basin of attraction of low-cost solutions and improves robustness with respect to initialization and sampling variability. Moreover, the theoretical guarantees of KernelSOS rely on smoothness assumptions on the objective function. The smoothed functions produced by GNC make it easier for KernelSOS to fit accurate surrogates and identify high-quality solutions compared to the original non-smooth objective.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-B Graduated Non-Convexity via Log-Sum-Exp Smoothing", "weight": 1.0} -->

In this work, we propose a general GNC strategy based on LSE smoothing, which is applicable to arbitrary non-convex, non-smooth functions. Given a cost function $\mathcal{J}{(\mathbf{u})}$, the LSE-smoothed surrogate function $\mathcal{J}_{lse}{(\mathbf{u},\sigma_{lse})}$ is defined as

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-B Graduated Non-Convexity via Log-Sum-Exp Smoothing", "weight": 1.0} -->

where $\mathbf{\epsilon}$ contains *i.i.d.* samples $\epsilon_{i} \sim {\mathcal{N}{(0,I)}}$, $\lambda > 0$ is temperature parameter and $\sigma_{lse} > 0$ is a GNC smoothing parameter.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-B Graduated Non-Convexity via Log-Sum-Exp Smoothing", "weight": 1.0} -->

As illustrated in Fig. 2, large values of $\sigma_{lse}$ produce a strongly smoothed, nearly convex surrogate, while small values recover the original non-smooth cost function. By gradually reducing $\sigma_{lse}$ across restart phases, the optimization landscape transitions from a smoothed, nearly convex surrogate to the original cost function. Moreover, LSE smoothing places greater weight on global minima and attenuates local minima, thereby enlarging the basins of attraction around high-quality solutions. This effect facilitates an effective global exploration of the solution space in our framework.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-C KernelSOS for Global Optimization", "weight": 1.0} -->

Importantly, we expect the smoothed function to still exhibit non-convexity, and local solvers would be at risk of getting trapped in local minima. Instead, we use KernelSOS, which is a global sampling-based optimization method introduced. The key idea of KernelSOS is to generalize classical sum-of-squares global optimization by replacing fixed polynomial bases with kernel functions, enabling a convex relaxation that allows to retrieve approximate global minima of general, non-parametric objectives. Since it only uses finite function and kernel evaluations, it is suitable for sampling-based optimization pipelines for contact-rich problems.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-C KernelSOS for Global Optimization", "weight": 1.0} -->

We define the kernel matrix $K_{\sigma} = \left( {k_{\sigma}{(\mathbf{u}^{(i)},\mathbf{u}^{(j)})}} \right)_{{i,j} \in {\lbrack N\rbrack}}$, where $k_{\sigma}$ is a chosen positive-definite kernel, $\sigma$ is the kernel parameter and $N$ is the finite number of samples. We denote its Cholesky decomposition by $K_{\sigma} = {R^{\top}R}$, with $R$ an upper-triangular matrix.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-C KernelSOS for Global Optimization", "weight": 1.0} -->

As shown, the relaxation gap between the solution of and the true global optimum $c^{\star}$ satisfies $c_{ksos}^{\star} \leq c^{\star}$ if ${\mathcal{J}{(\mathbf{u})}} - c$ lies in the chosen reproducing kernel Hilbert space (RKHS). In this case, the relaxation gap is guaranteed to asymptotically approach zero as $N\rightarrow\infty$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-C KernelSOS for Global Optimization", "weight": 1.0} -->

In practice, the magnitude of the relaxation gap thus depends on the choice of kernel and its associated hyperparameters, since they define the RKHS. Without careful calibration of the kernel parameters, the KernelSOS surrogate function may fail to accurately approximate the original objective $\mathcal{J}{(\mathbf{u})}$. Furthermore, there may not be a single function class that accurately approximates the landscape over the long-horizon task, particularly as we switch between contact modes. Therefore, we propose to automatically select the kernel parameter in KernelSOS, using a data-driven linear-to-quadratic auto-calibration strategy based on an empirical Bayes approach.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-C KernelSOS for Global Optimization", "weight": 1.0} -->

Specifically, we estimate the kernel parameter by minimizing the negative log-marginal likelihood (NLL) with respect to the linear Gaussian process surrogate model. This marginal likelihood maximization provides a statistically principled, computationally efficient, and numerically well-conditioned approach to kernel parameter estimation. Although KernelSOS uses a quadratic surrogate, we found that the optimal kernel identified using the linear surrogate, which is significantly easier to obtain, transferred well enough for our purposes.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-C KernelSOS for Global Optimization", "weight": 1.0} -->

Since ${NLL}{(\sigma)}$ is generally non-convex, we adopt a two-stage kernel selection strategy that first performs a coarse grid search over a predefined candidate set $\mathcal{S}$, followed by local gradient-based refinement to minimize the NLL. The calibrated kernel parameter is $\sigma_{ksos} = {{\arg{\min_{\sigma \in \mathcal{S}}{NLL}}}{(\sigma)}}$. This automatic linear-to-quadratic calibration strategy leverages linear models to select kernel parameters, eliminating the need for ad hoc heuristics and exhaustive hyperparameter tuning.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-D MPPI for local refinement", "weight": 1.0} -->

While KernelSOS can discover globally promising solutions across the entire action space, it is less accurate than local solvers in high-dimensional settings. In particular, due to the curse of dimensionality and the limited number of samples, the KernelSOS surrogate may fail to accurately approximate the original cost function, leading to suboptimal solutions. In contrast, local solvers are computationally efficient and well-suited to refine solutions within a basin of attraction once a high-quality initialization is available.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-D MPPI for local refinement", "weight": 1.0} -->

In our framework, we employ MPPI as a local refinement method. MPPI is particularly well-suited for this role because its sampling-based update can be interpreted as a natural stochastic gradient-descent step on the LSE-smoothed objective, which naturally aligns with the GNC scheme adopted in our method.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-D MPPI for local refinement", "weight": 1.0} -->

Overall, because MPPI relies solely on cost evaluations and does not require analytic models or gradients, it serves as an effective local refinement method in contact-rich environments.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-E Final Algorithm and Implementation Details", "weight": 1.0} -->

Having introduced the key algorithmic components, we formally present our methods in Algorithm 1. The algorithm operates in a receding-horizon setting and alternates between global exploration and local refinement across a sequence of GNC restart stages. At each stage, the sampling radius and LSE smoothing parameter $\sigma_{lse}$ are gradually reduced to enable a coarse-to-fine global exploration and local convergence. To enforce trajectory smoothness and reduce the dimensionality of the optimization problem, we adopt a spline-based control parameterization mentioned, in which trajectories are represented by cubic splines over a set of control points. The input constraints are incorporated by clipping the solution whenever it falls outside the admissible control range. The algorithm terminates once the objective improvement satisfies $\left| {{\mathcal{J}{(\mathbf{u}_{t + 1}^{opt})}} - {\mathcal{J}{(\mathbf{u}_{t}^{opt})}}} \right| < \delta$ for a predefined tolerance $\delta$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-E Final Algorithm and Implementation Details", "weight": 1.0} -->

The default values of all hyperparameters in Algorithm 1 are summarized in Table I.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-E Final Algorithm and Implementation Details", "weight": 1.0} -->

2:Notation: ut:= (ut,…,ut + H − 1) denotes a control sequence over a horizon of length H;
6: ut(i) ∼ Unif (utopt − Δ,utopt + Δ), i ∈ [N]
14: utopt ← MPPI(utref,σl s e)
19: ut + 1opt ← shift (utopt)
20: if |𝒥 (ut + 1opt)−𝒥 (utopt)| &lt; δ then
Algorithm 1 Global-MPPI algorithm

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-E Final Algorithm and Implementation Details", "weight": 1.0} -->

Initial control sequence: 0.5 (umax+umin)

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-E Final Algorithm and Implementation Details", "weight": 1.0} -->

Initial sampling radius: 0.5 (umax−umin)

<!-- chunk {"id": "body-0044", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we evaluate Global-MPPI on two contact-rich benchmark tasks: the PushT task and dexterous in-hand manipulation. We compare the performance of our approach against several state-of-the-art sampling-based optimization methods, including Predictive Sampling, vanilla MPPI, and DIAL-MPC, to demonstrate its ability to explore high-quality solutions in non-smooth, non-convex optimization landscapes.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-A Experiment setting", "weight": 1.0} -->

Our experiments were conducted in MuJoCo, a GPU-accelerated physics simulator. We ran the benchmarks on a workstation equipped with an Intel i9 CPU and an RTX 4090 GPU. To ensure fair comparisons, all methods were tested in the same environments, initialized from the same states, and run with the same seeds. Unless otherwise specified, Global-MPPI uses the same hyperparameters for all experiments as summarized in Table I. In our implementation, sampling, rollouts, function evaluation, LSE smoothing, and MPPI updates are executed on the GPU to leverage parallel computation, while KernelSOS is performed on the CPU. We use a custom interior-point solver for SDP to exploit the rank-one structure of the KernelSOS constraints, which is computationally faster than off-the-shelf SDP solvers such as MOSEK or SCS.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-B PushT task", "weight": 1.0} -->

The PushT task is a planar contact-rich manipulation task in which a robotic pusher moves a T-shaped object to a specified target pose. The task involves discontinuous contact dynamics, frictional interactions, and frequent contact mode switches. Consequently, the optimization landscape is highly non-smooth and non-convex. As a result, small perturbations in the control sequence can lead to qualitatively different object motions, turning the PushT task into a particularly challenging planning problem.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-B PushT task", "weight": 1.0} -->

We evaluate the performance of Global-MPPI on the PushT task. The system state $x_{t}$ consists of both the object pose and the pusher pose, and the control input $u_{t}$ corresponds to the pusher's position. Starting from an initial configuration, the objective is to compute a control sequence for the robot pusher that drives the object to a desired target pose.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-B PushT task", "weight": 1.0} -->

Here, the object pose at time $t$ is represented by ${(p_{t},q_{t})} \in {{{\mathbb{R}}^{2} \times {SO}}{}}$, and the target pose is ${(p_{g},q_{g})} \in {{{\mathbb{R}}^{2} \times {SO}}{}}$. $\Deltat$ denotes the time step, and the weight $w$ is used to balance translational and rotational errors. The operator $\otimes$ denotes rotation composition, and $\log{( \cdot )}$ maps the relative rotation $q_{g}^{- 1} \otimes q_{t}$ to the Lie algebra of ${SO}{}$, from which we extract a scalar rotation error.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-B PushT task", "weight": 1.0} -->

In our PushT experiments, we set the weight $w = 0.3$ and the time step ${\Deltat} = 0.01$ over a 1-second planning horizon. We use six control points for the cubic spline parameterization, resulting in a 12-dimensional control sequence $\mathbf{u}$. The benchmark results are summarized in the left panel of Fig. 3. Global-MPPI outperforms baseline methods, achieving faster convergence, lower final costs, and reduced variance. MPPI and DIAL-MPC, as more local optimization methods, often become trapped in poor local minima and sometimes struggle to reduce the cost. Predictive sampling is more robust to local minima but converges more slowly and with higher variance. We also conduct an ablation study of Global-MPPI by removing GNC, local refinement, and automatic calibration. The results are summarized in the left panel of Fig. 4. Removing local refinement or automatic calibration leads to higher final costs and increased variance. Although removing GNC yields a slightly lower final cost, incorporating GNC improves convergence speed and stability, suggesting that adaptive GNC strategies warrant further investigation.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-B PushT task", "weight": 1.0} -->

The robot trajectories produced by different methods in the PushT task are shown in Fig. 5, where the dashed red region denotes the target pose of the T-shaped object. Under the same initial and goal configurations, Global-MPPI achieves shorter trajectories, faster convergence, and lower final costs, outperforming the baseline methods. Notably, although the cost function does not explicitly penalize path length, Global-MPPI consistently identifies low-cost actions that efficiently reduce the task objective, yielding shorter, more efficient robot trajectories. In contrast, predictive sampling can successfully push the object into the target region, but incurs higher intermediate costs and generates less efficient trajectories. MPPI and DIAL-MPC, as local optimization methods, become trapped in suboptimal local minima and fail to move the object to the target region.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-C Dexterous in-hand manipulation", "weight": 1.0} -->

We further evaluate our approach on a high-dimensional dexterous in-hand manipulation task, which requires a multi-fingered hand to rotate and stabilize a cube to a desired target orientation while maintaining a stable grasp. This task involves intermittent multi-point contacts, frequent contact-mode switches, and highly nonlinear dynamics, resulting in a complex optimization landscape with many local minima.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-C Dexterous in-hand manipulation", "weight": 1.0} -->

Due to the small-scale joint motions of the dexterous hand, we parameterize the control trajectory using four control points over a 0.25-second horizon. We use a 16-DoF LEAP hand for this dexterous in-hand manipulation experiment. The dimension of the control sequence $\mathbf{u}$ is 64. The right panel of Fig. 3 shows the cost convergence comparison across different methods. Global-MPPI achieves the fastest convergence and the lowest final cost, demonstrating robust performance in the high-dimensional contact-rich problem. Predictive sampling shows limited improvement and plateaus at a significantly higher cost due to inefficient exploration in the high-dimensional action space. MPPI frequently converges to suboptimal local minima or fails to maintain stable object manipulation, resulting in inferior final performance. DIAL-MPC demonstrates improved performance compared with the PushT task; however, it attains higher final costs than Global-MPPI and converges slower, with Global-MPPI reaching the final best performance of DIAL-MPC already after less than 40 iterations, effectively halving the iteration time.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-C Dexterous in-hand manipulation", "weight": 1.0} -->

The ablation results are shown in the right panel of Fig. 4. Although all methods achieve almost similar final costs, the full Global-MPPI converges faster, reaching the final cost within approximately 30 iterations.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented Global-MPPI, a global sampling-based trajectory optimization framework tailored for contact-implicit trajectory optimization in contact-rich manipulation problems. By combining graduated non-convexity, kernelized global surrogates, and efficient local refinement, Global-MPPI enables global exploration and robust local convergence toward high-quality solutions.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Despite its effectiveness, the proposed approach has several limitations. First, scalability remains a challenge. As the problem dimension and planning horizon increase, the computational cost of SDP scales cubically with the number of samples. Future improvements can explore GPU-accelerated SDP solvers and efficient sampling to further advance real-time and large-scale applications.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Second, our approach relies on a parallelizable physics-based simulator to rollout trajectories and evaluate sample costs. Therefore, the performance of our approach depends on both the fidelity and computational efficiency of the simulator. Inaccurate modeling of complex dynamics may introduce a sim-to-real gap when deploying our approach on real-world systems. In practice, this issue can be partially mitigated by the receding-horizon MPC framework, which enables frequent re-planning and helps reduce the impact of model mismatch. We leave a comprehensive real-world implementation and validation to future work.
