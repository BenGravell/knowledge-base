<!-- arxiv-full-text:v1 {"arxiv_id": "2606.00317", "source": "arxiv-html"} -->

## Introduction

Model Predictive Path Integral (MPPI) \[undef, undefa\] is a widely used sampling-based method for nonlinear optimal control. Its strong empirical performance, together with modern parallel simulation tools such as Mujoco \[undefb\] and Isaac Gym \[undefc\], has enabled real-time control in a broad range of robotic settings, including whole-body control \[undefd\], quadrotor navigation \[undefe\], and online policy adaptation \[undeff\]. MPPI updates control sequences by sampling noisy trajectories, evaluating their costs, and forming a weighted average of sampled controls, resulting in a simple update rule that can be efficiently parallelized.

Most existing derivations of MPPI are rooted in stochastic optimal control and control-as-inference viewpoints \[undef, undefa, undefg\], in which trajectory optimality is recast as an inference problem over trajectories. These perspectives explain the exponential weighting structure underlying the MPPI update, but they do not by themselves provide a general optimization-theoretic characterization of the algorithm or its convergence behavior. Recent works have started to study MPPI convergence properties \[undefh, undefi\]. However, a general optimization perspective that links the MPPI update to a classical iterative optimization algorithm remains lacking.

Contributions. In this work, we show that MPPI can be interpreted as an instance of the Expectation--Maximization (EM) algorithm. This perspective yields a unified probabilistic and optimization-theoretic interpretation of MPPI, and naturally suggests algorithmic generalizations beyond the standard Gaussian setting. Building on this perspective, we analyze the convergence of a general EM-MPPI algorithm and establish a monotonic improvement condition for exponential-family distributions with strongly convex log-partition functions. We then specialize the analysis to standard MPPI, for which we derive explicit convergence guarantees and characterize the resulting rate in closed form.

## Related Work

Control as Probabilistic Inference. Stochastic optimal control can be formulated as probabilistic inference by introducing optimality variables whose likelihood depends exponentially on trajectory cost or reward \[undefj, undefg\]. This yields a posterior trajectory distribution proportional to a prior distribution Boltzmann-reweighted by the negative cost, and optimal control can be interpreted as computing or approximating expectations under this posterior. This viewpoint has been developed in control as inference \[undefk\] and variational-inference MPC \[undefl\], where MPPI \[undef\], the Cross-Entropy Method (CEM) \[undefm\], and Covariance Matrix Adaptation Evolution Strategy (CMA-ES) \[undefn\] arise under different choices of trajectory distributions and update rules. Closely related to our work, \[undefo\] derives a weighted maximum-likelihood projection onto a parametric variational family; For mixture-of-Gaussian families, this projection can be solved using an inner EM algorithm. In contrast, we identify the exact expectation-based MPPI update itself as an EM iteration.

Expectation--Maximization Methods for Control. The EM algorithm \[undefp, undefq\], originally developed for latent-variable inference \[undefr\], has also been applied to reinforcement learning and optimal control. \[undefs\] interpreted certain reinforcement-learning updates as EM by treating actions as latent variables and rewards as observations. \[undeft\] proposed an EM approach for solving (Partially Observed) Markov Decision Processes by introducing a random horizon, so that trajectories and horizons are optimized as latent variables. EM has also been used for stochastic optimal control under linear--Gaussian dynamics and policies \[undefu\]. These works demonstrate the value of EM in control, but they do not identify standard MPPI itself as an EM iteration or analyze MPPI convergence from this viewpoint. Our work fills this gap by deriving MPPI as an EM-type algorithm over a parameterized control distribution and using this interpretation to establish convergence guarantees.

Theoretical Analysis of MPPI. Despite MPPI's empirical success, its theoretical analysis remains limited. Existing works mainly study the standard sampling-based update. For example, \[undefh\] establishes linear convergence rates for quadratic problems, including time-varying LQR, and extends the analysis to nonlinear systems. \[undefi\] studies optimality and suboptimality properties of MPPI in stochastic and deterministic settings. These results provide important guarantees for the standard MPPI update under assumptions on the objective, dynamics, and sampling covariance. In contrast, we identify the EM structure underlying MPPI and use it to derive convergence guarantees from a latent-variable maximum-likelihood perspective.

## Preliminaries

### Optimal Control and MPC

Consider the finite-horizon optimal control problem Here $u=[u_{1},\dots,u_{H}]$ denotes the control sequence, $f_{h}:\mathbb{R}^{n_{x}}\times\mathbb{R}^{n_{u}}\rightarrow\mathbb{R}^{n_{x}}$ represents the system dynamics, $c_{h}:\mathbb{R}^{n_{x}}\times\mathbb{R}^{n_{u}}\rightarrow\mathbb{R}$ is the stage cost, and $c_{f}:\mathbb{R}^{n_{x}}\rightarrow\mathbb{R}$ is the terminal cost. We assume $J$ is bounded below with optimal value $J^{*}=\min_{u}J(u)$. In MPC, problem (3.1) is repeatedly solved in a receding-horizon manner. At each time step, the current state is used as the initial state $x_{1}$, an optimal control sequence is computed, and only the first control action $u_{1}$ is applied to the system. The horizon is then shifted forward, and the optimization problem is solved again (usually warm-started by shifting the control sequence obtained at the previous MPC step) after measuring the next state.

### MPPI

While nonlinear programming methods are widely used for solving (3.1), their applicability may be limited when the dynamics $f_{h}$ are non-differentiable or available only through a simulator. For example, in contact-rich systems, the dynamics may itself be defined implicitly through an optimization problem, making gradient-based methods difficult to apply. In such scenarios, MPPI control provides a sampling-based alternative. Starting from a nominal control sequence $u$, MPPI generates candidate control sequences by sampling perturbations around $u$, evaluates their rollout costs, and updates the nominal sequence via a cost-weighted average: where $\tau>0$ is a temperature parameter and $\{u[i]\}_{i=1}^{N}$ are sampled control sequences. Each $u[i]=[u[i]_{1},\dots,u[i]_{H}]$ represents a control trajectory drawn from the Gaussian distribution centered at the current nominal control sequence $u$. In practice, the update may be repeated multiple times within a single MPC step before applying the first control action, as implemented in practical systems.

## Generalized MPPI from EM

To formulate problem (3.1) as an inference problem, instead of directly searching for a single optimal control sequence $u$, we consider a distribution $p(u;\theta)$ parameterized by $\theta$. We introduce an optimality variable $\mathcal{O}$ conditioned on $\mathcal{U}$, defined as a Bernoulli random variable with conditional probability where $\tau>0$ is a temperature parameter controlling the sharpness of the optimality likelihood: smaller $\tau$ concentrates probability on trajectories with costs close to $J^{*}$, while larger $\tau$ gives broader weight to near-optimal trajectories. This construction ensures $P(\mathcal{O}=1\mid\mathcal{U}=u)\in(0,1]$ and assigns higher probability to sequences with lower cost. The marginal log likelihood of the optimality event under $p(u;\theta)$ is Provided the integral is finite, this defines a well-posed objective over $\theta$, and the constant is independent of $\theta$. This objective becomes large when $p(u;\theta)$ assigns more probability to control sequences that have lower trajectory costs. Therefore, instead of solving (3.1) by directly optimizing a single control sequence, we optimize $\theta$ so that the induced sampling distribution increasingly favors low-cost trajectories. This maximum-likelihood viewpoint naturally leads to an EM procedure for updating $\theta$.

In the probabilistic formulation above, the control sequence $\mathcal{U}$ plays the role of a latent variable, while the optimality event $\mathcal{O}=1$ is the observed variable. The goal is to maximize the marginal log likelihood $\ell(\theta):=\log P(\mathcal{O}=1;\theta)$ with respect to $\theta$. Since this is a latent-variable maximum-likelihood problem, it can be addressed using the EM algorithm. To derive the EM updates, let $q(u)$ be an auxiliary distribution over control sequences. Then from we have where the inequality follows from Jensen's inequality applied to the concave logarithm. is the evidence lower bound (ELBO), which is tight when $q(u)$ is chosen as the posterior distribution of $\mathcal{U}$ conditioned on the observation $\mathcal{O}=1$.

### E-Step

For fixed $\theta$, the ELBO in is maximized over $q$ when Jensen's inequality is tight, i.e., when $p(u;\theta)\exp(-\frac{J(u)}{\tau})/q(u)$ is constant in $u$. Using Bayes' rule, the optimal auxiliary distribution that maximizes the ELBO for the current $\theta$ is Therefore, for a fixed $\theta$, the ELBO is maximized over $q$ by choosing $q(u)=q(u;\theta)$, which corresponds to the posterior distribution $p(u\mid\mathcal{O}=1;\theta)$. Thus, the E-step recovers the standard optimal-control posterior obtained by Boltzmann reweighting of the current proposal distribution.

### M-Step

Given the ELBO constructed in the previous section, which is tight at the current $\theta$, the M-step updates the parameter by maximizing the ELBO with respect to $\theta$ to find the next iterate $\theta_{+}$, while fixing $q$ obtained from the E-step. Since the term $\mathbb{E}_{u\sim q}[J(u)]$ in does not depend on $\theta_{+}$, this is equivalent to minimizing the Kullback--Leibler divergence between $q$ and the parametric distribution $p(\cdot;\theta_{+})$: Thus, the M-step recovers the standard variational projection step: it approximates the Boltzmann-reweighted optimal-control distribution by the next proposal $p(\cdot;\theta_{+})$ within the chosen parametric family. Substituting the expression of $q(u;\theta)$ from the E-step yields which can be approximated using Monte Carlo estimation as (4.2) is a weighted maximum likelihood estimate, where $u[i]$ are sampled from $p(u;\theta)$ and the weights $w[i]$ are computed as Combining the E-step and M-step yields the complete EM algorithm, which we refer to as *Generalized MPPI*, summarized in Algorithm 1. Note that although the E-step has the closed-form solution, the posterior distribution is never explicitly computed. Instead, it is implicitly used in the M-step through Monte Carlo sampling and weight computation. Importantly, the algorithm naturally generalizes to any parametric distribution $p(\cdot;\theta)$ provided that samples can be efficiently drawn from $p(\cdot;\theta)$ and the weighted maximum likelihood problem (4.2) can be efficiently solved.

1:: Initial parameter θ0, number of samples N 3: Sample $u,...,u[N]\overset{\text{i.i.d.}}{\sim}p(u;\theta_{k})$ 4: Compute weights using Algorithm 1 Generalized MPPI

### Convergence

The EM interpretation of MPPI induces the fixed-point iteration Thus, MPPI can be analyzed through the convergence theory of EM-type algorithms.

### Assumption 1

In this paper, we make the following assumptions $\theta\in\Omega$ where $\Omega\subseteq\mathbb{R}^{n_{p}}$ is a closed set, $\forall u\text{ s.t. }\|u\|<\infty,\ \lim_{\|\theta\|\rightarrow\infty}p(u;\theta)=0$, $\forall M>0$, there exists a constant $C_{M}<\infty$ such that $p(u;\theta)\leq C_{M},\quad\forall\theta\in\Omega,\ \forall u\in\mathbb{R}^{d}\text{ with }\|u\|\leq M,$ $p(u;\theta)$ is twice continuously differentiable in $\theta$, $\lim_{M\rightarrow\infty}\inf\{J(u):\|u\|\geq M\}=\infty$, admits a maximizer for every $\theta$.

Assumption 1 is mainly a regularity condition on the sampling family and the trajectory cost. The coercivity condition on $J$ (Assumption 1.5) is also natural, since large control sequences are either directly penalized through control effort or lead to large terminal/running costs. The existence of the M-step maximizer (Assumption 1.6) is mild in the fixed-covariance Gaussian case, where the weighted maximum-likelihood problem has a closed-form solution (see ). Importantly, Assumption 1 does not require differentiability of the dynamics or of the rollout cost $J$; it only requires smoothness of the chosen sampling density $p(u;\theta)$ with respect to its parameter. Thus, the analysis remains compatible with nonsmooth or simulator-defined robotic tasks, including navigation with obstacle penalties or contact-rich interactions.

### Theorem 1 (Convergence of EM-MPPI)

Let 1 hold and $\{\theta_{k}\}$ be the sequence generated by EM-MPPI. Then the following properties hold: $\ell(\theta_{k+1})>\ell(\theta_{k})\ \forall\theta_{k}$ that is not a stationary point, the sequence $\{\ell(\theta_{k})\}$ converges, every limit point $\theta^{*}$ of $\{\theta_{k}\}$ is a stationary point of the log-likelihood, i.e., $\nabla_{\theta}\ell(\theta^{*})=0$,

### Proof 4.2

Under 1, we can show that the super level set $S=\{\theta:\ell(\theta)\geq\ell(\theta_{0})\}$ is compact, $\ell(\theta)$ is continuously differentiable, and that $Q(\theta_{+},\theta)$ is continuous in both argument. Then the result follows directly from classical convergence results for the EM algorithm \[undefv, undefq\], since the proposed EM-MPPI update is an instance of an EM iteration. A more detailed proof of the compactness of $S$ will be available in the longer version.

Furthermore, the EM-MPPI iteration enjoys a local linear convergence rate.

### Theorem 4.3 (Local linear convergence)

Assume that 1 holds, and further suppose that $\nabla^{2}_{\theta}\ell(\theta^{*})\prec 0$, the optimization problem has a unique solution in a neighborhood of $\theta^{*}$, $\nabla^{2}_{11}Q(\theta^{*},\theta^{*})$ is nonsingular, $M(\theta)$ is continuously differentiable in a neighborhood of $\theta^{*}$, then there exists a neighborhood $\mathcal{N}$ of $\theta^{*}$ such that for any $\theta_{0}\in\mathcal{N}$, the sequence $\{\theta_{k}\}$ generated by EM-MPPI converges to $\theta^{*}$. Moreover, the convergence is locally linear: where the Jacobian of the EM mapping is with $\rho(\partial M(\theta^{*}))<1$. Here $\rho(\partial M(\theta^{*}))$ denotes the spectral radius of the Jacobian of the EM mapping at $\theta^{*}$, and $\nabla_{ij}^{2}Q$ denotes the second derivative of $Q$ with respect to its $i$-th and $j$-th arguments.

The local convergence result follows directly from \[undefq, Sec 3.9\] and Ostrowski Theorem \[undefw, Thm 10.1.3\]. A more detailed proof will be available in the longer version.

### Remark 4.4 (Interpretation of the local assumptions)

The additional assumptions in Theorem 2 are local nondegeneracy conditions for the EM fixed-point map that describe the behavior of EM-MPPI once the iterates enter a neighborhood of a locally attracting solution. In the fixed-covariance Gaussian case, the M-step is locally unique because the weighted maximum-likelihood problem is strictly concave in the mean parameter. The nonsingularity of $\nabla^{2}_{11}Q(\theta^{*},\theta^{*})$ rules out degenerate local curvature, while differentiability of $M$ holds locally when the weighted moments vary smoothly with the current proposal parameter. Thus, Theorem 1 gives a global monotonic-improvement interpretation under broad regularity conditions, whereas Theorem 2 characterizes the local linear rate near a nondegenerate fixed point.

## EM-MPPI for Exponential Family

A particularly important case is when $p(u;\theta)$ belongs to the exponential family, i.e., where $h(u)$ is the base density, $\eta(\theta)$ is the natural parameter, $T(u)$ denotes the sufficient statistics, and $A(\eta)$ is the log-partition function, which is convex in $\eta$.

Assuming the mapping between $\theta$ and natural parameter $\eta$ is invertible, instead of studying convergence in $\theta$, we can analyze convergence in the natural parameter $\eta$. Two useful identities for exponential families are Note that when $p(u;\theta)$ belongs to the exponential family, the joint distribution $p(u,\mathcal{O}=1;\theta)$ also has an exponential-family form with a modified base density. This observation significantly simplifies the analysis. The EM iteration can be written as where $q(u;\eta)$ is the distribution obtained from the E-step. Since $A(\eta)$ is convex in $\eta$, the optimization problem is convex. Combining the optimality condition with yields which shows that the M-step corresponds to moment matching in the sufficient statistics $T(u)$.

### Theorem 5.5 (Sufficient Increase in Exponential Family)

Assume $A(\eta)$ is $\alpha$-strongly convex in $\eta$. Then the EM iteration satisfies

### Proof 5.6

See appendix for the proof.

Note that this sufficient increase property also holds when Algorithm 1 performs only a single update per iteration, which is commonly done in practice.

### Remark 5.7 (Monte Carlo approximation)

Theorem 5.5. ‣ 5 EM-MPPI for Exponential Family ‣ Generalized Model Predictive Path Integral Control as Expectation–Maximization") is stated for the population EM update. In Algorithm 1, the exact posterior moment $\mathbb{E}_{q(u;\eta)}[T(u)]$ is replaced by its self-normalized estimate. Repeating the proof of Theorem 5.5. ‣ 5 EM-MPPI for Exponential Family ‣ Generalized Model Predictive Path Integral Control as Expectation–Maximization") shows that the sufficient-increase bound holds up to an additional term proportional to the estimation error in this moment. Under finite-second-moment assumptions, this error is $O(N^{-1/2})$. Thus, the deterministic guarantee is recovered in the large-sample limit, while finite-sample monotonicity is approximate.

## Special Cases

### Gaussian MPPI

In this section, we study the convergence of the commonly used Gaussian MPPI and derive an explicit convergence result using the results from previous sections. In Gaussian MPPI, the control distribution is where $\theta=\{\mu\}$ is the parameter and $\Sigma$ is a fixed covariance matrix. In this case, $p(u;\theta)$ is smooth in $\mu$, locally bounded on compact sets of controls, and satisfies $p(u;\theta)\to 0$ for each fixed $u$ as $\|\theta\|\to\infty$. The weighted log-likelihood estimation (4.2) admits a closed-form solution which reduces exactly to the standard MPPI update. Using the result from Theorem 4.3. ‣ 4.3 Convergence ‣ 4 Generalized MPPI from EM ‣ Generalized Model Predictive Path Integral Control as Expectation–Maximization"), the Jacobian of the EM mapping at a stationary point is $\partial M(\theta^{*})=\mathrm{Cov}_{q(u;\theta^{*})}[u]\Sigma^{-1},$ which characterizes the local convergence rate. This shows that the local convergence is governed by the product of the covariance of the importance-weighted distribution and the inverse exploration covariance.

Next we study the global sufficient increase property of Gaussian MPPI. A Gaussian distribution with fixed covariance can be written in exponential-family form as The mapping between $\mu$ and $\eta$ is therefore invertible. Moreover, the log-partition function $A(\eta)$ is $\alpha$-strongly convex with $\alpha=\lambda_{\min}(\Sigma)$ where $\lambda_{\min}(\Sigma)$ is the minimum eigenvalue of $\Sigma$. Applying Theorem 5.5. ‣ 5 EM-MPPI for Exponential Family ‣ Generalized Model Predictive Path Integral Control as Expectation–Maximization"), Gaussian MPPI satisfies the global sufficient increase

### Mixture of Gaussian (MoG) MPPI

A well-known limitation of Gaussian MPPI is its inability to represent multi-modal distributions. For example, in a car navigation scenario with obstacle avoidance, going left and going right around an obstacle may both be valid choices, while their average trajectory may collide with the obstacle. Motivated by this issue, we consider a mixture of Gaussian distributions where $L$ is the number of Gaussian components and $\theta=\{\pi_{1},\mu_{1},\dots,\pi_{L},\mu_{L}\}$ denotes the parameters. For simplicity, we assume that the covariance matrices are fixed and identical across components. In this case, the weighted maximum likelihood estimation (4.2) can be solved using an inner EM algorithm with the following update rule: Mixture-of-Gaussian control distributions for MPPI have also been explored in prior work on variational-inference control \[undefo\]. This formulation naturally fits into the EM-MPPI framework, where the E-step computes trajectory weights and the M-step updates the mixture parameters.

## Experiments

In this section, we consider a Dubins car navigation problem with obstacle avoidance where $Q=\mathrm{diag}(1,1,0.01)$, $R=0.001$, and $x_{h}=[\mathtt{x}_{h},\mathtt{y}_{h},\mathtt{\theta}_{h}]$ contains the planar position and orientation, and $d$ is that goal state. The control input is $u_{h}=[\omega_{h}]$, representing the angular velocity, with actuation bound $\omega_{h}\in[-\frac{3}{2}\pi,\frac{3}{2}\pi]$. The system dynamics are where $v$ is a constant forward velocity and $\delta t$ is the Euler integration step. We sample at least 1024 feasible trajectories for each update.

### Sufficient Increase of Gaussian MPPI

We first verify the sufficient increase property of Gaussian MPPI in by considering a simple navigation problem without obstacles. The car starts from the state $x_{1}=[0,0,\pi/2]$ and the target is $d=$. We run Algorithm 1 for 20 iterations. In Figure 1, we show the sampled trajectories at different iterations. We also plot the function $F(\eta_{k})=\log(\tfrac{1}{N}\sum_{i=1}^{N}\exp(-\tfrac{J(u[i])}{\tau})),$ which provides a Monte Carlo estimate of the likelihood (up to a constant), and $F(\eta_{k})+\frac{\lambda_{\min}(\Sigma)}{2}\|\eta_{k+1}-\eta_{k}\|_{2}^{2},$ which is the lower bound on $F(\eta_{k+1})$ implied .

(a) Sampled trajectories at different iterations Figure 1: Convergence of Gaussian MPPI on a simple Dubins-car navigation problem.

### Cluttered Environment Navigation

Next, we consider a more cluttered environment where the car must reach the goal while avoiding multiple obstacles. We compare Gaussian MPPI and MoG MPPI with two Gaussian components. For both methods, we perform either 1 or 5 iterations of Algorithm 1 before executing each action. It can be seen in Figure 2 that, as the car approaches an obstacle, the feasible trajectories split into two modes corresponding to passing the obstacle from the left or the right. MoG MPPI naturally captures these modes through its mixture distribution. In contrast, Gaussian MPPI approximates the bimodal distribution with a single Gaussian and therefore averages the two directions. As a result, the mean control tends to keep the car moving straight toward the obstacle, producing many infeasible samples. Table 1 shows the total number of sampled trajectories and the fraction of rejected trajectories.

(a) Gaussian, 1 inner iteration (b) MoG, 1 inner iteration (c) Gaussian, 5 inner iteration (d) MoG, 5 inner iteration Figure 2: Behavior of Gaussian MPPI and MoG MPPI in a cluttered environment.

Table 1: Total number of sampled trajectories and rejected by MPPI with different distributions and number of iterations

## Conclusion

We reinterpret Model Predictive Path Integral (MPPI) control as an Expectation--Maximization (EM) algorithm, showing that repeated MPPI updates perform likelihood ascent on a latent-variable optimality model. This view clarifies the connection between Boltzmann reweighting and weighted maximum-likelihood projection, enables generalized proposal families beyond Gaussians, and yields convergence, local-rate, and sufficient-increase results through classical EM theory. Our analysis focuses on the exact expectation-based iteration; finite-sample Monte Carlo effects and receding-horizon closed-loop behavior remain important directions for future work.
