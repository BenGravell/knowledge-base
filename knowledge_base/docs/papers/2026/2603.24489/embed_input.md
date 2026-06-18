<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Model Predictive Path Integral Control as Preconditioned Gradient Descent

Topics include Gradient descent, Trajectory optimization, Sampling-based methods, Optimization, Control, Sampling, Model predictive path integral control, KL.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Model Predictive Path Integral (MPPI) control is a widely used sampling-based method for trajectory optimization, yet its convergence properties remain only partially understood. This paper provides a direct convergence analysis using variational optimization. By lifting constrained trajectory optimization to a Kullback-Leibler (KL) regularized problem over decision distributions, we derive a reduced free-energy objective defined over a parametric sampling family. For general parametric families, we derive gradient and Hessian representations of this reduced objective and analyze preconditioned gradient descent on the sampling-distribution parameters. In the fixed-covariance Gaussian case, the classical MPPI update is recovered exactly as a unit-step preconditioned gradient update. We prove descent and stationarity guarantees for the exact expectation-based iteration when the Hessian of the reduced objective is bounded in the metric induced by the preconditioner. For the Gaussian family, we further show that the preconditioned Hessian is governed by the covariance of the Gibbs-tilted distribution relative to the covariance of the sampling distribution, yielding a covariance-dependent sufficient condition for the descent of exact unit-step MPPI.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Numerical experiments illustrate the theory and the effect of key hyperparameters.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model Predictive Path Integral (MPPI) control, e.g. is a widely used sampling-based method for trajectory optimization in nonlinear and nonconvex settings, owing to its simplicity, parallelizability, and ability to handle nondifferentiable dynamics and costs. In its standard form, MPPI updates the sampling distribution by drawing perturbed control sequences, reweighting them according to their trajectory costs, and shifting the nominal control toward a weighted average of the sampled rollouts. Despite its empirical success in robotics and real-time control, this update is typically introduced through stochastic optimal control or control-as-inference arguments, which do not directly expose its underlying optimization structure. As a result, basic questions such as how MPPI relates to gradient-based methods, when its update is guaranteed to decrease a well-defined objective, and how its hyperparameters influence stability and convergence remain only partially understood. These gaps motivate the need for a direct optimization-theoretic interpretation of MPPI.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Contributions", "weight": 1.0} -->

This paper provides a variational, optimization-theoretic analysis of MPPI, with the goal of establishing convergence guarantees beyond special cases. Starting from constrained trajectory optimization, we lift the problem to a KL-regularized distributional formulation and eliminate the auxiliary decision distribution to obtain a reduced negative log-partition, or free-energy, objective over a tractable sampling family. For a general parametric sampling family, we derive exact gradient and Hessian formulas for this reduced objective, which allow us to analyze the convergence of preconditioned gradient descent on the sampling-distribution parameters. Our framework enables three concrete consequences. First, it yields descent and stationarity guarantees, including an $O{({1/K})}$ ergodic stationarity rate, for the exact preconditioned-gradient iteration when the Hessian of the reduced objective is bounded in the metric induced by the preconditioner.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Contributions", "weight": 1.0} -->

Second, in the fixed-covariance Gaussian family, it recovers classical MPPI exactly as a unit-step preconditioned gradient update and shows that the preconditioned Hessian of the reduced objective is governed by the covariance of the Gibbs-tilted distribution relative to the sampling covariance. This leads to an explicit covariance-dependent sufficient condition for descent of exact unit-step MPPI. Third, it provides a principled basis for selecting the algorithm hyperparameters, including step size, multiple inner updates, and stopping criteria based on stationarity. Numerical experiments support the theory and illustrate the effect of key hyperparameters on performance.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Probabilistic Inference Perspective", "weight": 1.0} -->

Inference-based formulations recast control as posterior inference over action sequences conditioned on an optimality variable, leading to updates closely related to MPPI. This viewpoint has been developed extensively in reinforcement learning and control. In particular, introduced a variational inference MPC framework that recovers several sampling-based optimization methods, including MPPI, CEM, and CMA-ES \[3")\] as special cases. Our contribution is complementary: rather than deriving MPPI through inference, we show that it can be obtained directly as a preconditioned gradient step on a KL-regularized free-energy objective.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Diffusion Perspective", "weight": 1.0} -->

Another line of work connects MPPI to model-based diffusion. In, building on the score estimation result from that Mscore-estimation result, it is shown on a Gaussian-smoothed Gibbs distribution. Although this interpretation explains the mechanism of MPPI, it still does not directly reveal its convergence properties.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Optimization Perspective", "weight": 1.0} -->

MPPI has also been studied through optimization-based perspectives, particularly mirror descent (MD) and its accelerated variants. These methods perform distribution-space updates that are then restricted or projected onto tractable parametric families; for Gaussian families, this recovers standard MPPI. Closest to our work, Wagener et al. considered utility-transformed trajectory objectives and showed that the exponential-utility case yields classical MPPI under a fixed-covariance Gaussian family with unit step size. In contrast, our free-energy objective arises by exactly eliminating the decision distribution in a KL-regularized variational formulation of the original constrained trajectory optimization problem.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Theoretical Analysis of MPPI", "weight": 1.0} -->

Motivated by the empirical success of MPPI, several recent works have begun to study its theoretical properties. In particular, CoVO-MPC analyzes the convergence behavior of MPPI using contraction theory, proving at least linear convergence for (time-varying) LQR. However, the contraction result cannot be extended to general nonlinear settings without making extra regularity assumptions. Separately, studies the optimality and suboptimality of MPPI in stochastic and deterministic settings, with an emphasis on deterministic MPPI and its approximation error. Our analysis is complementary to these works: we analyze the convergence for general nonlinear systems and cost, with bounded feasible set being the main requirement.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Trajectory Optimization as Constrained Minimization", "weight": 1.0} -->

We consider finite-horizon trajectory optimization over an open-loop control sequence $u:={(u_{0},u_{1},\ldots,u_{T - 1})} \in {\mathbb{R}}^{dT}$ applied to a dynamical system

<!-- chunk {"id": "body-0012", "role": "body", "section": "Trajectory Optimization as Constrained Minimization", "weight": 1.0} -->

possibly nonlinear and nonsmooth, from a given initial condition $x_{0}$. Let $f_{0}{(u)}$ denote the trajectory objective (e.g., cumulative stage costs and a terminal cost), and $C \subset {\mathbb{R}}^{dT}$ denote the set of feasible control sequences, encoding constraints such as obstacle avoidance, state bounds, or input limits. Throughout, we assume that $C$ is nonempty and compact and that $f_{0}$ is continuous. The resulting trajectory optimization problem is

<!-- chunk {"id": "body-0013", "role": "body", "section": "KL-Regularized Distributional Formulation", "weight": 1.0} -->

Following the framework of variational optimization, e.g.

<!-- chunk {"id": "body-0014", "role": "body", "section": "KL-Regularized Distributional Formulation", "weight": 1.0} -->

Here, $\rho$ denotes a *decision distribution* over $u$. This unregularized lifted problem is equivalent to the original pointwise problem and collapses to a Dirac measure at a minimizer of $f_{0}$ over $C$. To obtain a nondegenerate distributional formulation, we introduce a *base*, or sampling, distribution $\pi$ over the same control-sequence space and regularize $\rho$ relative to $\pi$ using the KL divergence. We require $\rho \ll \pi$; otherwise, ${{KL}{({\rho \parallel \pi})}} = {+ \infty}$. For a regularization parameter $\tau > 0$, consider

<!-- chunk {"id": "body-0015", "role": "body", "section": "KL-Regularized Distributional Formulation", "weight": 1.0} -->

The support constraint enforces the hard feasibility of the decision distribution. Problem trades off low expected trajectory cost under $\rho$ with proximity to the sampling distribution $\pi$. As $\tau\rightarrow 0$, the regularization vanishes and optimal solutions concentrate on the optimal set ${U^{\star} = {{\arg{\min_{u \in C}f_{0}}}{(u)}}}.$

<!-- chunk {"id": "body-0016", "role": "body", "section": "Optimizing the Base Distribution", "weight": 1.0} -->

where both minimizations are taken over distributions $\rho$ supported on $C$, and the equality follows by choosing $\rho$ as a Dirac measure at any minimizer of $f_{0}$ over $C$. Note that the upper bound is a function of $\pi$. Therefore, we can optimize over $\pi$ to seek the tightest such upper bound. However, if we optimize over $\pi$ without restriction, the pair $(\rho,\pi)$ may collapse (e.g., $\pi = \rho$), undermining stability and exploration. We therefore restrict $\pi$ to a tractable family $\Pi$ (e.g., Gaussians with bounded covariance), and consider

<!-- chunk {"id": "body-0017", "role": "body", "section": "Optimizing the Base Distribution", "weight": 1.0} -->

For a fixed $\pi \in \Pi$, the minimizer over $\rho$ in is given by the truncated Gibbs tilt

<!-- chunk {"id": "body-0018", "role": "body", "section": "Optimizing the Base Distribution", "weight": 1.0} -->

See the Appendix for a full derivation. Since $\pi$ is positive on $C$, we have ${Z{(\pi)}} > 0$. Thus, $\rho_{\pi}^{\star}$ is obtained by reweighting the base distribution $\pi$ according to trajectory cost and feasibility: lower-cost feasible control sequences receive larger probability mass, whereas infeasible sequences receive zero mass. Substituting into the inner objective yields

<!-- chunk {"id": "body-0019", "role": "body", "section": "Optimizing the Base Distribution", "weight": 1.0} -->

Therefore, the joint optimization problem reduces to the finite-dimensional optimization problem over the negative log-partition or free-energy objective,

<!-- chunk {"id": "body-0020", "role": "body", "section": "Optimizing the Base Distribution", "weight": 1.0} -->

This objective is precisely the $\pi$-dependent upper bound obtained after eliminating the auxiliary distribution $\rho$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Optimization over a Parametric Sampling Family", "weight": 1.0} -->

In this section, we specialize the reduced problem to a parametric family of sampling distributions $\Pi:={\{\pi_{\theta}:{\theta \in \Theta}\}}$, where $\Theta \subseteq {\mathbb{R}}^{p}$ is the parameter space. For each $\theta \in \Theta$, the corresponding optimal decision distribution is

<!-- chunk {"id": "body-0022", "role": "body", "section": "Optimization over a Parametric Sampling Family", "weight": 1.0} -->

Accordingly, the reduced problem becomes

<!-- chunk {"id": "body-0023", "role": "body", "section": "Optimization over a Parametric Sampling Family", "weight": 1.0} -->

We make the following assumption, under which the reduced objective $F$ becomes twice differentiable.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The family ${\{\pi_{\theta}\}}_{\theta \in \Theta}$ is strictly positive on $C$, twice continuously differentiable in $\theta$, and such that differentiation under the integral sign is valid for $Z{(\theta)}$ up to second order.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Preconditioned Gradient Descent", "weight": 1.0} -->

In contrast to the original constrained trajectory optimization problem, the reduced problem is differentiable in the distribution parameters and is therefore amenable to gradient-based optimization. The following result provides expressions for the gradient and Hessian of $F{(\theta)}$ that will be useful for algorithm design and convergence analysis.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

We now analyze the exact preconditioned gradient iteration with a constant step size $\eta > 0$, and derive conditions under which it yields descent and convergence of the reduced objective. Since the iteration is preconditioned by $P$, the relevant notion of smoothness is naturally expressed in the metric induced by $P$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

For the chosen positive definite matrix $P \succ 0$, there exists a constant $L_{P} > 0$ such that

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The following lemma is an immediate consequence of Assumption 2.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Optimization over Gaussian Family with Fixed Covariance", "weight": 1.0} -->

We now specialize the preceding results to the fixed-covariance Gaussian family

<!-- chunk {"id": "body-0030", "role": "body", "section": "Optimization over Gaussian Family with Fixed Covariance", "weight": 1.0} -->

where the mean $\mu \in {\mathbb{R}}^{m}$ is the optimization variable. In this case, the score and log-Hessian are given by

<!-- chunk {"id": "body-0031", "role": "body", "section": "Optimization over Gaussian Family with Fixed Covariance", "weight": 1.0} -->

Substituting these expressions into Lemma 1 ‣ 3.1 Preconditioned Gradient Descent ‣ 3 Optimization over a Parametric Sampling Family ‣ Model Predictive Path Integral Control as Preconditioned Gradient Descent") yields

<!-- chunk {"id": "body-0032", "role": "body", "section": "Optimization over Gaussian Family with Fixed Covariance", "weight": 1.0} -->

Using, the exact preconditioned gradient step becomes

<!-- chunk {"id": "body-0033", "role": "body", "section": "Optimization over Gaussian Family with Fixed Covariance", "weight": 1.0} -->

Using the ratio-of-expectations representation in (11 ‣ 3.1 Preconditioned Gradient Descent ‣ 3 Optimization over a Parametric Sampling Family ‣ Model Predictive Path Integral Control as Preconditioned Gradient Descent")), the expectation ${\mathbb{E}}_{\rho_{\mu_{k}}}{\lbrack u\rbrack}$ can be approximated by self-normalized importance sampling. Accordingly, if $u^{(j)} \sim {\mathcal{N}{(\mu_{k},\Sigma)}}$ and the normalized weights ${\overline{w}}_{j}$ are defined as, a Monte Carlo implementation of is

<!-- chunk {"id": "body-0034", "role": "body", "section": "Optimization over Gaussian Family with Fixed Covariance", "weight": 1.0} -->

In particular, by choosing ${P = {\frac{1}{\tau}\Sigma}},{\eta = 1}$, the exact preconditioned gradient update reduces to

<!-- chunk {"id": "body-0035", "role": "body", "section": "Optimization over Gaussian Family with Fixed Covariance", "weight": 1.0} -->

where ${w{(u)}} = {{\exp{({- {{f_{0}{(u)}}/\tau}})}}\mathbf{1}_{C}{(u)}}$, and the last equality follows from the ratio-of-expectations in Lemma 1 ‣ 3.1 Preconditioned Gradient Descent ‣ 3 Optimization over a Parametric Sampling Family ‣ Model Predictive Path Integral Control as Preconditioned Gradient Descent"). Correspondingly, the Monte Carlo implementation becomes

<!-- chunk {"id": "body-0036", "role": "body", "section": "Optimization over Gaussian Family with Fixed Covariance", "weight": 1.0} -->

which is precisely the classical MPPI update.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Convergence analysis", "weight": 1.0} -->

We now analyze the exact Gaussian update through the lens of preconditioned gradient descent. Although is well defined for any positive definite preconditioner $P$, the choice

<!-- chunk {"id": "body-0038", "role": "body", "section": "Convergence analysis", "weight": 1.0} -->

is especially natural for two reasons. First, when $\eta = 1$, this choice exactly recovers the classical MPPI update, as shown in the previous subsection. Therefore, convergence guarantees established under $P = {\Sigma/\tau}$ immediately apply to MPPI, as well as to its relaxed version with arbitrary step size $\eta > 0$. Second, this preconditioner is intrinsic to the geometry of the fixed-covariance Gaussian family. Indeed, by Lemma 1 ‣ 3.1 Preconditioned Gradient Descent ‣ 3 Optimization over a Parametric Sampling Family ‣ Model Predictive Path Integral Control as Preconditioned Gradient Descent"),

<!-- chunk {"id": "body-0039", "role": "body", "section": "Convergence analysis", "weight": 1.0} -->

Thus, in the metric induced by $P = {\Sigma/\tau}$, the curvature of the reduced objective is determined entirely by the covariance of the tilted distribution $\rho_{\mu}$ relative to the sampling covariance $\Sigma$. In particular, the explicit dependence on the temperature $\tau$ disappears after preconditioning. This makes $P = {\Sigma/\tau}$ the natural scaling for the convergence analysis.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Convergence analysis", "weight": 1.0} -->

Accordingly, throughout this subsection we specialize to the update

<!-- chunk {"id": "body-0041", "role": "body", "section": "Convergence analysis", "weight": 1.0} -->

which we refer to as the *exact relaxed MPPI update*. To state the convergence result, define

<!-- chunk {"id": "body-0042", "role": "body", "section": "Convergence analysis", "weight": 1.0} -->

By, $L_{\Sigma}$ is the operator-norm bound on the Hessian of $F$ in the metric induced by $\Sigma/\tau$, and hence the corresponding smoothness constant in that metric. In the next theorem, we state the convergence result.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Implication for MPPI with unit step size", "weight": 1.0} -->

The exact MPPI iteration is recovered by setting $\eta = 1$. Hence, convergence of the exact MPPI iteration follows from Theorem 4.6 whenever the unit step size satisfies the admissibility condition for $0 < 1 < \frac{2}{L_{\Sigma}}$, which is equivalent to $L_{\Sigma} < 2$. Using the bound, a sufficient condition is therefore $D_{\Sigma^{- 1}}^{2} < 12$. Since $D_{\Sigma^{- 1}}^{2} \leq \frac{D^{2}}{\lambda_{\min}{(\Sigma)}}$, where $D$ is the Euclidean diameter of $C$, this condition is guaranteed when ${{\lambda_{\min}{(\Sigma)}} \geq \frac{D^{2}}{12}}.$

<!-- chunk {"id": "body-0044", "role": "body", "section": "Implication for MPPI with unit step size", "weight": 1.0} -->

Thus, if the covariance matrix is sufficiently large, then the exact MPPI iteration with $\eta = 1$ satisfies the descent and convergence guarantees of Theorem 3.4. In particular, this gives a simple design rule: the exploration covariance must not be too small relative to the diameter of the feasible set. Equivalently, overly concentrated sampling distributions can destroy the global descent guarantee, whereas sufficiently diffuse sampling is enough to ensure it.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 4.8", "weight": 1.0} -->

Theorems 3.4--4.6 analyze the exact expectation-based iteration. The sampled update instead uses a self-normalized importance-sampling estimator, which is generally biased. To see how this affects the descent guarantee, write

<!-- chunk {"id": "body-0046", "role": "body", "section": "Remark 4.8", "weight": 1.0} -->

Thus, the exact descent guarantee is preserved up to two terms controlled by the finite-sample gradient estimation error. A complete non-asymptotic analysis of the bias and variance of the self-normalized estimator is an important direction for future work.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Linear Quadratic Regulator (LQR)", "weight": 1.0} -->

We consider a finite-horizon LQR trajectory optimization problem with double-integrator dynamics

<!-- chunk {"id": "body-0048", "role": "body", "section": "Linear Quadratic Regulator (LQR)", "weight": 1.0} -->

where $Q \succeq 0$, and $c$ can be computed accordingly. The constraint set $\mathcal{C}$ enforces both the control bounds ${|u|} \leq 1$ and the state constraints $x \in {{\lbrack{- 5},5\rbrack} \times {\lbrack{- 1},1\rbrack}}$. A detailed derivation of the resulting QP is provided in the Appendix.2. We set a budget of $N = 1000$ samples per iteration. Figure 1 shows the results for different choices of the parameters. Figure 1 illustrates the convergence behavior predicted. In the first two figures, we fix one parameter among $\tau$ and $\Sigma$, and compare the choices of MPPI $\eta = 1$ (dashed lines), and suggested by our theories ($\eta = {1/L_{\Sigma}}$) (solid lines).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Linear Quadratic Regulator (LQR)", "weight": 1.0} -->

In the left plot, we fix $\tau = 1$ and compare two choices of $\Sigma = {\sigma^{2}I}$, and in the middle plot, we fix $\Sigma = {10^{- 4}I}$, and compare two choices of $\tau$. Since the LQR objective is quadratic, $L_{\Sigma}$ can be computed explicitly. When the Lipschitz constant is small (e.g., $L_{\Sigma} = 0.1$), the choice $\eta = 1$ becomes conservative, and a larger step size leads to a faster convergence rate. We also compare Multi-step MPPI (M-MPPI) with finite differences (FD) in the right figure, where our method outperforms FD. More details regarding the setup can be found in Appendix.2.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Dubins Car", "weight": 1.0} -->

We then consider a trajectory optimization task in a cluttered environment, where a Dubins car must reach a given destination. At each time, the optimization problem is formulated as

<!-- chunk {"id": "body-0051", "role": "body", "section": "Dubins Car", "weight": 1.0} -->

where $v = 4$ is the constant velocity and the control $w_{t} \in {\lbrack{- {\frac{3}{2}\pi}},{\frac{3}{2}\pi}\rbrack}$, and we set $N = 1024$. Figure 2 shows the trajectory chosen by the algorithm with $K = 1$ (MPPI) and $K = 10$. Since MPPI does not iterate until convergence, it selects a suboptimal path. More details on this setup and comparison with Log-MPPI are in Table 1, where we show that increasing $K$ improves the average cost, at the expense of runtime. The reported results are averaged over 3 seeds.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we showed that MPPI admits a direct variational and optimization-theoretic interpretation. By lifting constrained trajectory optimization to a KL-regularized problem over distributions, we obtained a free-energy objective whose optimization over a parametric sampling family yields a preconditioned gradient method. In the Gaussian fixed-covariance setting, this recovers classical MPPI exactly and leads to explicit descent and stationarity guarantees, as well as a simple covariance-dependent design rule for unit-step MPPI. These results help demystify MPPI from an optimization viewpoint and open the door to principled extensions of sampling-based control methods. Our analysis focuses on the exact expectation-based iteration; understanding the full finite-sample and receding-horizon closed-loop behavior remains an important direction for future work.
