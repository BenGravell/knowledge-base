## Introduction

Model Predictive Path Integral (MPPI) control, e.g. is a widely used sampling-based method for trajectory optimization in nonlinear and nonconvex settings, owing to its simplicity, parallelizability, and ability to handle nondifferentiable dynamics and costs. In its standard form, MPPI updates the sampling distribution by drawing perturbed control sequences, reweighting them according to their trajectory costs, and shifting the nominal control toward a weighted average of the sampled rollouts. Despite its empirical success in robotics and real-time control, this update is typically introduced through stochastic optimal control or control-as-inference arguments, which do not directly expose its underlying optimization structure. As a result, basic questions such as how MPPI relates to gradient-based methods, when its update is guaranteed to decrease a well-defined objective, and how its hyperparameters influence stability and convergence remain only partially understood. These gaps motivate the need for a direct optimization-theoretic interpretation of MPPI.

### Contributions

This paper provides a variational, optimization-theoretic analysis of MPPI, with the goal of establishing convergence guarantees beyond special cases. Starting from constrained trajectory optimization, we lift the problem to a KL-regularized distributional formulation and eliminate the auxiliary decision distribution to obtain a reduced negative log-partition, or free-energy, objective over a tractable sampling family. For a general parametric sampling family, we derive exact gradient and Hessian formulas for this reduced objective, which allow us to analyze the convergence of preconditioned gradient descent on the sampling-distribution parameters. Our framework enables three concrete consequences. First, it yields descent and stationarity guarantees, including an $O(1/K)$ ergodic stationarity rate, for the exact preconditioned-gradient iteration when the Hessian of the reduced objective is bounded in the metric induced by the preconditioner. Second, in the fixed-covariance Gaussian family, it recovers classical MPPI exactly as a unit-step preconditioned gradient update and shows that the preconditioned Hessian of the reduced objective is governed by the covariance of the Gibbs-tilted distribution relative to the sampling covariance. This leads to an explicit covariance-dependent sufficient condition for descent of exact unit-step MPPI. Third, it provides a principled basis for selecting the algorithm hyperparameters, including step size, multiple inner updates, and stopping criteria based on stationarity. Numerical experiments support the theory and illustrate the effect of key hyperparameters on performance.

### Related Work

### Probabilistic Inference Perspective

Inference-based formulations recast control as posterior inference over action sequences conditioned on an optimality variable, leading to updates closely related to MPPI. This viewpoint has been developed extensively in reinforcement learning and control. In particular, introduced a variational inference MPC framework that recovers several sampling-based optimization methods, including MPPI, CEM, and CMA-ES \[3")\] as special cases. Our contribution is complementary: rather than deriving MPPI through inference, we show that it can be obtained directly as a preconditioned gradient step on a KL-regularized free-energy objective.

### Diffusion Perspective

Another line of work connects MPPI to model-based diffusion. In, building on the score estimation result from that Mscore-estimation result , it is shown on a Gaussian-smoothed Gibbs distribution. Although this interpretation explains the mechanism of MPPI, it still does not directly reveal its convergence properties.

### Optimization Perspective

MPPI has also been studied through optimization-based perspectives, particularly mirror descent (MD) and its accelerated variants. These methods perform distribution-space updates that are then restricted or projected onto tractable parametric families; for Gaussian families, this recovers standard MPPI. Closest to our work, Wagener et al. considered utility-transformed trajectory objectives and showed that the exponential-utility case yields classical MPPI under a fixed-covariance Gaussian family with unit step size. In contrast, our free-energy objective arises by exactly eliminating the decision distribution in a KL-regularized variational formulation of the original constrained trajectory optimization problem.

### Theoretical Analysis of MPPI

Motivated by the empirical success of MPPI, several recent works have begun to study its theoretical properties. In particular, CoVO-MPC analyzes the convergence behavior of MPPI using contraction theory, proving at least linear convergence for (time-varying) LQR. However, the contraction result cannot be extended to general nonlinear settings without making extra regularity assumptions. Separately, studies the optimality and suboptimality of MPPI in stochastic and deterministic settings, with an emphasis on deterministic MPPI and its approximation error. Our analysis is complementary to these works: we analyze the convergence for general nonlinear systems and cost, with bounded feasible set being the main requirement.

### Notation

For a symmetric matrix $A$, $A\succeq 0$ and $A\succ 0$ denote positive semidefiniteness and positive definiteness. The identity matrix is $I$, and $\lambda_{\min}(A)$, $\lambda_{\max}(A)$ denote the extreme eigenvalues of $A$. We use $\|\cdot\|$ for both the Euclidean and spectral norms. For $P\succ 0$, let $\|x\|_{P}^{2}=x^{\top}Px$. For a density $\pi$, $\mathbb{E}_{\pi}[\cdot]$, $\mathrm{Cov}_{\pi}(\cdot)$, and $\mathrm{supp}(\pi)$ denote expectation, covariance, and support. We write $\pi(u)=\mathcal{N}(u;\mu,\Sigma)$ for a Gaussian density and $\mathrm{KL}(\rho\|\pi)$ for the Kullback--Leibler divergence. The notation $\rho\ll\pi$ means that $\rho$ is absolutely continuous with respect to $\pi$. For a differentiable function $F$, $\nabla F$ and $\nabla^{2}F$ denote its gradient and Hessian. For a set $C$, $\mathbf{1}_{C}$ denotes its indicator function.

## Variational Formulation

### Trajectory Optimization as Constrained Minimization

We consider finite-horizon trajectory optimization over an open-loop control sequence $u:=(u_{0},u_{1},\dots,u_{T-1})\in\mathbb{R}^{dT}$ applied to a dynamical system possibly nonlinear and nonsmooth, from a given initial condition $x_{0}$. Let $f_{0}(u)$ denote the trajectory objective (e.g., cumulative stage costs and a terminal cost), and $C\subset\mathbb{R}^{dT}$ denote the set of feasible control sequences, encoding constraints such as obstacle avoidance, state bounds, or input limits. Throughout, we assume that $C$ is nonempty and compact and that $f_{0}$ is continuous. The resulting trajectory optimization problem is

### KL-Regularized Distributional Formulation

Following the framework of variational optimization, e.g. we first lift the pointwise trajectory optimization problem to an optimization problem over probability distributions on the open-loop control sequence $u$: Here, $\rho$ denotes a *decision distribution* over $u$. This unregularized lifted problem is equivalent to the original pointwise problem and collapses to a Dirac measure at a minimizer of $f_{0}$ over $C$. To obtain a nondegenerate distributional formulation, we introduce a *base*, or sampling, distribution $\pi$ over the same control-sequence space and regularize $\rho$ relative to $\pi$ using the KL divergence. We require $\rho\ll\pi$; otherwise, $\mathrm{KL}(\rho\|\pi)=+\infty$. For a regularization parameter $\tau>0$, consider The support constraint enforces the hard feasibility of the decision distribution. Problem trades off low expected trajectory cost under $\rho$ with proximity to the sampling distribution $\pi$. As $\tau\to 0$, the regularization vanishes and optimal solutions concentrate on the optimal set $U^{\star}=\arg\min_{u\in C}f_{0}(u).$

### Optimizing the Base Distribution

For any fixed base distribution $\pi$, provides an upper bound on the optimal value of the original constrained problem: where both minimizations are taken over distributions $\rho$ supported on $C$, and the equality follows by choosing $\rho$ as a Dirac measure at any minimizer of $f_{0}$ over $C$. Note that the upper bound is a function of $\pi$. Therefore, we can optimize over $\pi$ to seek the tightest such upper bound. However, if we optimize over $\pi$ without restriction, the pair $(\rho,\pi)$ may collapse (e.g., $\pi=\rho$), undermining stability and exploration. We therefore restrict $\pi$ to a tractable family $\Pi$ (e.g., Gaussians with bounded covariance), and consider For a fixed $\pi\in\Pi$, the minimizer over $\rho$ in is given by the truncated Gibbs tilt where $Z(\pi)$ is the normalizing constant See the Appendix for a full derivation. Since $\pi$ is positive on $C$, we have $Z(\pi)>0$. Thus, $\rho^{\star}_{\pi}$ is obtained by reweighting the base distribution $\pi$ according to trajectory cost and feasibility: lower-cost feasible control sequences receive larger probability mass, whereas infeasible sequences receive zero mass. Substituting into the inner objective yields Therefore, the joint optimization problem reduces to the finite-dimensional optimization problem over the negative log-partition or free-energy objective, This objective is precisely the $\pi$-dependent upper bound obtained after eliminating the auxiliary distribution $\rho$.

## Optimization over a Parametric Sampling Family

In this section, we specialize the reduced problem to a parametric family of sampling distributions $\Pi:=\{\pi_{\theta}:\theta\in\Theta\}$, where $\Theta\subseteq\mathbb{R}^{p}$ is the parameter space. For each $\theta\in\Theta$, the corresponding optimal decision distribution is Accordingly, the reduced problem becomes We make the following assumption, under which the reduced objective $F$ becomes twice differentiable.

### Assumption 1

The family $\{\pi_{\theta}\}_{\theta\in\Theta}$ is strictly positive on $C$, twice continuously differentiable in $\theta$, and such that differentiation under the integral sign is valid for $Z(\theta)$ up to second order.

### Preconditioned Gradient Descent

In contrast to the original constrained trajectory optimization problem, the reduced problem is differentiable in the distribution parameters and is therefore amenable to gradient-based optimization. The following result provides expressions for the gradient and Hessian of $F(\theta)$ that will be useful for algorithm design and convergence analysis.

### Lemma 1 (Gradient and Hessian Representations)

### Proof 3.1

The gradient representations in Lemma 1 ‣ 3.1 Preconditioned Gradient Descent ‣ 3 Optimization over a Parametric Sampling Family ‣ Model Predictive Path Integral Control as Preconditioned Gradient Descent") naturally motivate a preconditioned gradient method for minimizing the reduced objective $F(\theta)$. Given a symmetric positive definite preconditioner $P\succ 0$ and a step size $\eta>0$, the exact preconditioned gradient descent is 1:Initial parameter θ0, number of samples N, number of iterations K 3:while Convergence condition not met. do 4: Sample $u^{},...,u^{(N)}\overset{\text{i.i.d.}}{\sim}\pi_{\theta_{k-1}}(u)$ Algorithm 1 Multi-step MPPI In practice, the expectation with respect to $\rho_{\theta_{k}}$ is generally intractable. Using (11 ‣ 3.1 Preconditioned Gradient Descent ‣ 3 Optimization over a Parametric Sampling Family ‣ Model Predictive Path Integral Control as Preconditioned Gradient Descent")), we can sample from $\pi_{\theta_{k}}$ instead. Specifically, we draw samples $u^{(j)}\sim\pi_{\theta_{k}},\ j=1,\dots,N$, and define the self-normalized importance weights This yields the self-normalized Monte Carlo estimator of, This update has the standard structure of a weighted sample average used in policy search and sampling-based control methods, and recovers MPPI as a special case under a suitable Gaussian parameterization.

### Convergence Analysis

We now analyze the exact preconditioned gradient iteration with a constant step size $\eta>0$, and derive conditions under which it yields descent and convergence of the reduced objective. Since the iteration is preconditioned by $P$, the relevant notion of smoothness is naturally expressed in the metric induced by $P$.

### Assumption 2

For the chosen positive definite matrix $P\succ 0$, there exists a constant $L_{P}>0$ such that The following lemma is an immediate consequence of Assumption 2.

### Lemma 3.2

Under Assumption 2, for all $\theta,\theta+\Delta\theta\in\Theta$,

### Proof 3.3

### Theorem 3.4

Suppose Assumption 2 holds, and let $\{\theta^{k}\}$ be generated by with a constant step size $\eta>0$. If then the following hold: Descent: for every $k$, Summability of preconditioned gradients: Stationarity: for every $K\geq 1$, In particular, $\lim_{k\to\infty}\|\nabla F(\theta^{k})\|_{P}=0$.

### Proof 3.5

Applying the smoothness bound with $\Delta\theta=-\eta P\nabla F(\theta^{k})$, we obtain after simplification. Since $0<\eta<2/L_{P}$, the coefficient is positive, so $F(\theta^{k})$ is nonincreasing. Summing from $k=0$ to $K-1$ and using $\inf_{\theta\in\Theta}F(\theta)\leq F(\theta^{K})$ Letting $K\to\infty$ gives. Dividing by $K$ gives, and summability implies $\|\nabla F(\theta^{k})\|_{P}\to 0$.

Theorem 3.4 shows that the exact multi-step iteration is a descent method for the free-energy objective $F(\theta)$: for a sufficiently small step size, $F(\theta^{k})$ decreases monotonically and the iterates converge toward stationarity. This result also suggests a natural stopping criterion based on the preconditioned gradient norm $\|\nabla F(\theta^{k})\|_{P}$. See Algorithm 1 for a summary of the method.

## Optimization over Gaussian Family with Fixed Covariance

We now specialize the preceding results to the fixed-covariance Gaussian family where the mean $\mu\in\mathbb{R}^{m}$ is the optimization variable. In this case, the score and log-Hessian are given by Substituting these expressions into Lemma 1 ‣ 3.1 Preconditioned Gradient Descent ‣ 3 Optimization over a Parametric Sampling Family ‣ Model Predictive Path Integral Control as Preconditioned Gradient Descent") yields Using, the exact preconditioned gradient step becomes Using the ratio-of-expectations representation in (11 ‣ 3.1 Preconditioned Gradient Descent ‣ 3 Optimization over a Parametric Sampling Family ‣ Model Predictive Path Integral Control as Preconditioned Gradient Descent")), the expectation $\mathbb{E}_{\rho_{\mu_{k}}}[u]$ can be approximated by self-normalized importance sampling. Accordingly, if $u^{(j)}\sim\mathcal{N}(\mu_{k},\Sigma)$ and the normalized weights $\bar{w}_{j}$ are defined as, a Monte Carlo implementation of is In particular, by choosing $P=\frac{1}{\tau}\Sigma,\ \eta=1$, the exact preconditioned gradient update reduces to where $w(u)=\exp(-f_{0}(u)/\tau)\mathbf{1}_{C}(u)$, and the last equality follows from the ratio-of-expectations in Lemma 1 ‣ 3.1 Preconditioned Gradient Descent ‣ 3 Optimization over a Parametric Sampling Family ‣ Model Predictive Path Integral Control as Preconditioned Gradient Descent"). Correspondingly, the Monte Carlo implementation becomes which is precisely the classical MPPI update.

### Convergence analysis

We now analyze the exact Gaussian update through the lens of preconditioned gradient descent. Although is well defined for any positive definite preconditioner $P$, the choice is especially natural for two reasons. First, when $\eta=1$, this choice exactly recovers the classical MPPI update, as shown in the previous subsection. Therefore, convergence guarantees established under $P=\Sigma/\tau$ immediately apply to MPPI, as well as to its relaxed version with arbitrary step size $\eta>0$. Second, this preconditioner is intrinsic to the geometry of the fixed-covariance Gaussian family. Indeed, by Lemma 1 ‣ 3.1 Preconditioned Gradient Descent ‣ 3 Optimization over a Parametric Sampling Family ‣ Model Predictive Path Integral Control as Preconditioned Gradient Descent"), Hence, with $P=\Sigma/\tau$, Thus, in the metric induced by $P=\Sigma/\tau$, the curvature of the reduced objective is determined entirely by the covariance of the tilted distribution $\rho_{\mu}$ relative to the sampling covariance $\Sigma$. In particular, the explicit dependence on the temperature $\tau$ disappears after preconditioning. This makes $P=\Sigma/\tau$ the natural scaling for the convergence analysis.

Accordingly, throughout this subsection we specialize to the update which we refer to as the *exact relaxed MPPI update*. To state the convergence result, define By, $L_{\Sigma}$ is the operator-norm bound on the Hessian of $F$ in the metric induced by $\Sigma/\tau$, and hence the corresponding smoothness constant in that metric. In the next theorem, we state the convergence result.

Figure 1: Ablation study of the parameters Σ (left) and τ (middle), and comparison with finite differences (right) on the LQR benchmark.

### Theorem 4.6

Consider the fixed-covariance Gaussian family, and the exact preconditioned gradient update. Assume that the feasible set $C\subset\mathbb{R}^{m}$ is bounded, with diameter $D_{\Sigma^{-1}}:=\sup_{u,v\in C}\|\Sigma^{-1/2}(u-v)\|$. Then the metric smoothness constant satisfies Consequently, the exact relaxed MPPI update satisfies the descent and convergence conclusions of Theorem 3.4 whenever

### Proof 4.7

### Implication for MPPI with unit step size

The exact MPPI iteration is recovered by setting $\eta=1$. Hence, convergence of the exact MPPI iteration follows from Theorem 4.6 whenever the unit step size satisfies the admissibility condition for $0<1<\frac{2}{L_{\Sigma}}$, which is equivalent to $L_{\Sigma}<2$. Using the bound, a sufficient condition is therefore $D^{2}_{\Sigma^{-1}}<12$. Since $D^{2}_{\Sigma^{-1}}\leq\frac{D^{2}}{\lambda_{\min}(\Sigma)}$, where $D$ is the Euclidean diameter of $C$, this condition is guaranteed when $\lambda_{\min}(\Sigma)\geq\frac{D^{2}}{12}.$ Thus, if the covariance matrix is sufficiently large, then the exact MPPI iteration with $\eta=1$ satisfies the descent and convergence guarantees of Theorem 3.4. In particular, this gives a simple design rule: the exploration covariance must not be too small relative to the diameter of the feasible set. Equivalently, overly concentrated sampling distributions can destroy the global descent guarantee, whereas sufficiently diffuse sampling is enough to ensure it.

### Remark 4.8

Theorems 3.4--4.6 analyze the exact expectation-based iteration. The sampled update instead uses a self-normalized importance-sampling estimator, which is generally biased. To see how this affects the descent guarantee, write where $b_{k}:=\mathbb{E}[\widehat{\nabla F}(\theta_{k})\mid\theta_{k}]-\nabla F(\theta_{k})$ is the bias of the self-normalized estimator, and $\mathbb{E}[\xi_{k}\mid\theta_{k}]=0$ captures its zero-mean random fluctuation. Applying the same smoothness argument as in Theorem 3.4, Thus, the exact descent guarantee is preserved up to two terms controlled by the finite-sample gradient estimation error. A complete non-asymptotic analysis of the bias and variance of the self-normalized estimator is an important direction for future work.

## Numerical Analysis

### Linear Quadratic Regulator (LQR)

We consider a finite-horizon LQR trajectory optimization problem with double-integrator dynamics We define the cost to be $J(u)=\sum_{t=1}^{T}\|x_{t}\|^{2}+\|u_{t}\|^{2},$ where horizon $T=10$, $u:=(u_{0},\cdots,u_{T-1})\in\mathbb{R}^{10}$ is the stacked control vector, $x_{0}=(2.5,0)$. Rolling out the trajectories yields the quadratic program where $Q\succeq 0$, and $c$ can be computed accordingly. The constraint set $\mathcal{C}$ enforces both the control bounds $|u|\leq 1$ and the state constraints $x\in\times$. A detailed derivation of the resulting QP is provided in the Appendix.2. We set a budget of $N=1000$ samples per iteration. Figure 1 shows the results for different choices of the parameters. Figure 1 illustrates the convergence behavior predicted. In the first two figures, we fix one parameter among $\tau$ and $\Sigma$, and compare the choices of MPPI $\eta=1$ (dashed lines), and suggested by our theories ($\eta=1/L_{\Sigma}$) (solid lines). In the left plot, we fix $\tau=1$ and compare two choices of $\Sigma=\sigma^{2}I$, and in the middle plot, we fix $\Sigma=10^{-4}I$, and compare two choices of $\tau$. Since the LQR objective is quadratic, $L_{\Sigma}$ can be computed explicitly. When the Lipschitz constant is small (e.g., $L_{\Sigma}=0.1$), the choice $\eta=1$ becomes conservative, and a larger step size leads to a faster convergence rate. We also compare Multi-step MPPI (M-MPPI) with finite differences (FD) in the right figure, where our method outperforms FD. More details regarding the setup can be found in Appendix.2.

### Dubins Car

We then consider a trajectory optimization task in a cluttered environment, where a Dubins car must reach a given destination. At each time, the optimization problem is formulated as where $T=20$, $Q=\mathrm{diag}(1,1,0.01)$, $R=0.001$, $x_{0}=(0,0,\pi/2)$, and $x_{d}=$. The system dynamics $x_{t}=[p^{x}_{t},p^{y}_{t},\mathtt{\theta}_{t}]^{\top}$ are where $v=4$ is the constant velocity and the control $w_{t}\in[-\frac{3}{2}\pi,\frac{3}{2}\pi]$, and we set $N=1024$. Figure 2 shows the trajectory chosen by the algorithm with $K=1$ (MPPI) and $K=10$. Since MPPI does not iterate until convergence, it selects a suboptimal path. More details on this setup and comparison with Log-MPPI are in Table 1, where we show that increasing $K$ improves the average cost, at the expense of runtime. The reported results are averaged over 3 seeds.

Figure 2: Comparison of the trajectories chosen by MPPI and 10-step MPPI on the Dubins car benchmark in a cluttered environment. The blue and red lines denote the safe and unsafe trajectories, respectively.

Table 1: Comparison of runtime, sample acceptance rate %, and average cost of the chosen trajectory for various methods.

## Conclusion

In this paper, we showed that MPPI admits a direct variational and optimization-theoretic interpretation. By lifting constrained trajectory optimization to a KL-regularized problem over distributions, we obtained a free-energy objective whose optimization over a parametric sampling family yields a preconditioned gradient method. In the Gaussian fixed-covariance setting, this recovers classical MPPI exactly and leads to explicit descent and stationarity guarantees, as well as a simple covariance-dependent design rule for unit-step MPPI. These results help demystify MPPI from an optimization viewpoint and open the door to principled extensions of sampling-based control methods. Our analysis focuses on the exact expectation-based iteration; understanding the full finite-sample and receding-horizon closed-loop behavior remains an important direction for future work.
