<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Generalized Model Predictive Path Integral Control as Expectation-Maximization

Topics include Model predictive path integral control, Expectation maximization, Sampling-based control, Optimal control, Trajectory optimization, Path integral control, Control theory.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Recasts generalized model predictive path integral control through the lens of expectation-maximization. This perspective clarifies the update structure of MPPI-style methods and links sampling-based control to a broader probabilistic optimization template.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Model Predictive Path Integral (MPPI) control is a powerful sampling-based method for solving stochastic optimal control problems and has enabled real-time control in complex robotic systems. Despite its empirical success, its theoretical understanding remains limited. In this work, we show that MPPI can be interpreted as a special case of the Expectation-Maximization (EM) algorithm applied to a probabilistic inference formulation of optimal control. This perspective leads to a generalized EM-MPPI framework that extends MPPI beyond the commonly used Gaussian parameterization. We analyze the convergence behavior of this algorithm and characterize the local convergence rate in terms of the covariance of the posterior trajectory distribution and the exploration distribution. For exponential-family distributions, we establish a sufficient increase property of the log-likelihood when the log-partition function is strongly convex. Specializing the analysis to Gaussian MPPI yields explicit global and local convergence characterizations. The code for the experiments will be available upon acceptance.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model Predictive Path Integral (MPPI) \[undef, undefa\] is a widely used sampling-based method for nonlinear optimal control. Its strong empirical performance, together with modern parallel simulation tools such as Mujoco \[undefb\] and Isaac Gym \[undefc\], has enabled real-time control in a broad range of robotic settings, including whole-body control \[undefd\], quadrotor navigation \[undefe\], and online policy adaptation \[undeff\]. MPPI updates control sequences by sampling noisy trajectories, evaluating their costs, and forming a weighted average of sampled controls, resulting in a simple update rule that can be efficiently parallelized.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Most existing derivations of MPPI are rooted in stochastic optimal control and control-as-inference viewpoints \[undef, undefa, undefg\], in which trajectory optimality is recast as an inference problem over trajectories. These perspectives explain the exponential weighting structure underlying the MPPI update, but they do not by themselves provide a general optimization-theoretic characterization of the algorithm or its convergence behavior. Recent works have started to study MPPI convergence properties \[undefh, undefi\]. However, a general optimization perspective that links the MPPI update to a classical iterative optimization algorithm remains lacking.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions. In this work, we show that MPPI can be interpreted as an instance of the Expectation--Maximization (EM) algorithm. This perspective yields a unified probabilistic and optimization-theoretic interpretation of MPPI, and naturally suggests algorithmic generalizations beyond the standard Gaussian setting. Building on this perspective, we analyze the convergence of a general EM-MPPI algorithm and establish a monotonic improvement condition for exponential-family distributions with strongly convex log-partition functions. We then specialize the analysis to standard MPPI, for which we derive explicit convergence guarantees and characterize the resulting rate in closed form.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Optimal Control and MPC", "weight": 1.0} -->

Consider the finite-horizon optimal control problem

<!-- chunk {"id": "body-0008", "role": "body", "section": "Optimal Control and MPC", "weight": 1.0} -->

In MPC, problem (3.1) is repeatedly solved in a receding-horizon manner. At each time step, the current state is used as the initial state $x_{1}$, an optimal control sequence is computed, and only the first control action $u_{1}$ is applied to the system. The horizon is then shifted forward, and the optimization problem is solved again (usually warm-started by shifting the control sequence obtained at the previous MPC step) after measuring the next state.

<!-- chunk {"id": "body-0009", "role": "body", "section": "MPPI", "weight": 1.0} -->

While nonlinear programming methods are widely used for solving (3.1), their applicability may be limited when the dynamics $f_{h}$ are non-differentiable or available only through a simulator. For example, in contact-rich systems, the dynamics may itself be defined implicitly through an optimization problem, making gradient-based methods difficult to apply. In such scenarios, MPPI control provides a sampling-based alternative.

<!-- chunk {"id": "body-0010", "role": "body", "section": "MPPI", "weight": 1.0} -->

where $\tau > 0$ is a temperature parameter and ${\{{u{\lbrack i\rbrack}}\}}_{i = 1}^{N}$ are sampled control sequences. Each ${u{\lbrack i\rbrack}} = {\lbrack{u{\lbrack i\rbrack}_{1}},\ldots,{u{\lbrack i\rbrack}_{H}}\rbrack}$ represents a control trajectory drawn from the Gaussian distribution centered at the current nominal control sequence $u$. In practice, the update may be repeated multiple times within a single MPC step before applying the first control action, as implemented in practical systems.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Generalized MPPI from EM", "weight": 1.0} -->

To formulate problem (3.1) as an inference problem, instead of directly searching for a single optimal control sequence $u$, we consider a distribution $p{(u;\theta)}$ parameterized by $\theta$. We introduce an optimality variable $\mathcal{O}$ conditioned on $\mathcal{U}$, defined as a Bernoulli random variable with conditional probability

<!-- chunk {"id": "body-0012", "role": "body", "section": "Generalized MPPI from EM", "weight": 1.0} -->

where $\tau > 0$ is a temperature parameter controlling the sharpness of the optimality likelihood: smaller $\tau$ concentrates probability on trajectories with costs close to $J^{\ast}$, while larger $\tau$ gives broader weight to near-optimal trajectories. This construction ensures ${P{({\mathcal{O} = {1 \mid \mathcal{U}} = u})}} \in {(0,1\rbrack}$ and assigns higher probability to sequences with lower cost. The marginal log likelihood of the optimality event under $p{(u;\theta)}$ is

<!-- chunk {"id": "body-0013", "role": "body", "section": "Generalized MPPI from EM", "weight": 1.0} -->

Provided the integral is finite, this defines a well-posed objective over $\theta$, and the constant is independent of $\theta$. This objective becomes large when $p{(u;\theta)}$ assigns more probability to control sequences that have lower trajectory costs. Therefore, instead of solving (3.1) by directly optimizing a single control sequence, we optimize $\theta$ so that the induced sampling distribution increasingly favors low-cost trajectories. This maximum-likelihood viewpoint naturally leads to an EM procedure for updating $\theta$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Generalized MPPI from EM", "weight": 1.0} -->

In the probabilistic formulation above, the control sequence $\mathcal{U}$ plays the role of a latent variable, while the optimality event $\mathcal{O} = 1$ is the observed variable. The goal is to maximize the marginal log likelihood ${\ell{(\theta)}}:={{\log P}{({\mathcal{O} = {1;\theta}})}}$ with respect to $\theta$. Since this is a latent-variable maximum-likelihood problem, it can be addressed using the EM algorithm. To derive the EM updates, let $q{(u)}$ be an auxiliary distribution over control sequences. Then from we have

<!-- chunk {"id": "body-0015", "role": "body", "section": "Generalized MPPI from EM", "weight": 1.0} -->

where the inequality follows from Jensen's inequality applied to the concave logarithm. is the evidence lower bound (ELBO), which is tight when $q{(u)}$ is chosen as the posterior distribution of $\mathcal{U}$ conditioned on the observation $\mathcal{O} = 1$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "E-Step", "weight": 1.0} -->

For fixed $\theta$, the ELBO in is maximized over $q$ when Jensen's inequality is tight, i.e., when ${{p{(u;\theta)}{\exp{({- \frac{J{(u)}}{\tau}})}}}/q}{(u)}$ is constant in $u$. Using Bayes' rule, the optimal auxiliary distribution that maximizes the ELBO for the current $\theta$ is

<!-- chunk {"id": "body-0017", "role": "body", "section": "E-Step", "weight": 1.0} -->

Therefore, for a fixed $\theta$, the ELBO is maximized over $q$ by choosing ${q{(u)}} = {q{(u;\theta)}}$, which corresponds to the posterior distribution $p{({{u \mid \mathcal{O}} = {1;\theta}})}$. Thus, the E-step recovers the standard optimal-control posterior obtained by Boltzmann reweighting of the current proposal distribution.

<!-- chunk {"id": "body-0018", "role": "body", "section": "M-Step", "weight": 1.0} -->

Given the ELBO constructed in the previous section, which is tight at the current $\theta$, the M-step updates the parameter by maximizing the ELBO with respect to $\theta$ to find the next iterate $\theta_{+}$, while fixing $q$ obtained from the E-step.

<!-- chunk {"id": "body-0019", "role": "body", "section": "M-Step", "weight": 1.0} -->

Thus, the M-step recovers the standard variational projection step: it approximates the Boltzmann-reweighted optimal-control distribution by the next proposal $p{( \cdot;\theta_{+})}$ within the chosen parametric family. Substituting the expression of $q{(u;\theta)}$ from the E-step yields

<!-- chunk {"id": "body-0020", "role": "body", "section": "M-Step", "weight": 1.0} -->

which can be approximated using Monte Carlo estimation as

<!-- chunk {"id": "body-0021", "role": "body", "section": "M-Step", "weight": 1.0} -->

(4.2) is a weighted maximum likelihood estimate, where $u{\lbrack i\rbrack}$ are sampled from $p{(u;\theta)}$ and the weights $w{\lbrack i\rbrack}$ are computed as

<!-- chunk {"id": "body-0022", "role": "body", "section": "M-Step", "weight": 1.0} -->

Combining the E-step and M-step yields the complete EM algorithm, which we refer to as *Generalized MPPI*, summarized in Algorithm 1. Note that although the E-step has the closed-form solution, the posterior distribution is never explicitly computed. Instead, it is implicitly used in the M-step through Monte Carlo sampling and weight computation. Importantly, the algorithm naturally generalizes to any parametric distribution $p{( \cdot;\theta)}$ provided that samples can be efficiently drawn from $p{( \cdot;\theta)}$ and the weighted maximum likelihood problem (4.2) can be efficiently solved.

<!-- chunk {"id": "body-0023", "role": "body", "section": "M-Step", "weight": 1.0} -->

1:: Initial parameter θ0, number of samples N
3: Sample ${u{\lbrack 1\rbrack}},\ldots,{u{\lbrack N\rbrack}\overset{\text{i.i.d.}}{\sim}p{(u;\theta_{k})}}$
4: Compute weights using
Algorithm 1 Generalized MPPI

<!-- chunk {"id": "body-0024", "role": "body", "section": "Convergence", "weight": 1.0} -->

The EM interpretation of MPPI induces the fixed-point iteration

<!-- chunk {"id": "body-0025", "role": "body", "section": "Convergence", "weight": 1.0} -->

Thus, MPPI can be analyzed through the convergence theory of EM-type algorithms.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

In this paper, we make the following assumptions

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

$p{(u;\theta)}$ is twice continuously differentiable in $\theta$,

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

admits a maximizer for every $\theta$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Assumption 1 is mainly a regularity condition on the sampling family and the trajectory cost. The coercivity condition on $J$ (Assumption 1.5) is also natural, since large control sequences are either directly penalized through control effort or lead to large terminal/running costs. The existence of the M-step maximizer (Assumption 1.6) is mild in the fixed-covariance Gaussian case, where the weighted maximum-likelihood problem has a closed-form solution (see ). Importantly, Assumption 1 does not require differentiability of the dynamics or of the rollout cost $J$; it only requires smoothness of the chosen sampling density $p{(u;\theta)}$ with respect to its parameter. Thus, the analysis remains compatible with nonsmooth or simulator-defined robotic tasks, including navigation with obstacle penalties or contact-rich interactions.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 4.4 (Interpretation of the local assumptions)", "weight": 1.0} -->

The additional assumptions in Theorem 2 are local nondegeneracy conditions for the EM fixed-point map that describe the behavior of EM-MPPI once the iterates enter a neighborhood of a locally attracting solution. In the fixed-covariance Gaussian case, the M-step is locally unique because the weighted maximum-likelihood problem is strictly concave in the mean parameter. The nonsingularity of ${\nabla_{11}^{2}Q}{(\theta^{\ast},\theta^{\ast})}$ rules out degenerate local curvature, while differentiability of $M$ holds locally when the weighted moments vary smoothly with the current proposal parameter. Thus, Theorem 1 gives a global monotonic-improvement interpretation under broad regularity conditions, whereas Theorem 2 characterizes the local linear rate near a nondegenerate fixed point.

<!-- chunk {"id": "body-0031", "role": "body", "section": "EM-MPPI for Exponential Family", "weight": 1.0} -->

A particularly important case is when $p{(u;\theta)}$ belongs to the exponential family, i.e.,

<!-- chunk {"id": "body-0032", "role": "body", "section": "EM-MPPI for Exponential Family", "weight": 1.0} -->

where $h{(u)}$ is the base density, $\eta{(\theta)}$ is the natural parameter, $T{(u)}$ denotes the sufficient statistics, and $A{(\eta)}$ is the log-partition function, which is convex in $\eta$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "EM-MPPI for Exponential Family", "weight": 1.0} -->

Assuming the mapping between $\theta$ and natural parameter $\eta$ is invertible, instead of studying convergence in $\theta$, we can analyze convergence in the natural parameter $\eta$. Two useful identities for exponential families are

<!-- chunk {"id": "body-0034", "role": "body", "section": "EM-MPPI for Exponential Family", "weight": 1.0} -->

Note that when $p{(u;\theta)}$ belongs to the exponential family, the joint distribution $p{(u,\mathcal{O} = 1;\theta)}$ also has an exponential-family form with a modified base density. This observation significantly simplifies the analysis. The EM iteration can be written as

<!-- chunk {"id": "body-0035", "role": "body", "section": "EM-MPPI for Exponential Family", "weight": 1.0} -->

where $q{(u;\eta)}$ is the distribution obtained from the E-step. Since $A{(\eta)}$ is convex in $\eta$, the optimization problem is convex. Combining the optimality condition with yields

<!-- chunk {"id": "body-0036", "role": "body", "section": "EM-MPPI for Exponential Family", "weight": 1.0} -->

which shows that the M-step corresponds to moment matching in the sufficient statistics $T{(u)}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 5.7 (Monte Carlo approximation)", "weight": 1.0} -->

Theorem 5.5. ‣ 5 EM-MPPI for Exponential Family ‣ Generalized Model Predictive Path Integral Control as Expectation–Maximization") is stated for the population EM update. In Algorithm 1, the exact posterior moment ${\mathbb{E}}_{q{(u;\eta)}}{\lbrack{T{(u)}}\rbrack}$ is replaced by its self-normalized estimate. Repeating the proof of Theorem 5.5. ‣ 5 EM-MPPI for Exponential Family ‣ Generalized Model Predictive Path Integral Control as Expectation–Maximization") shows that the sufficient-increase bound holds up to an additional term proportional to the estimation error in this moment. Under finite-second-moment assumptions, this error is $O{(N^{- {1/2}})}$. Thus, the deterministic guarantee is recovered in the large-sample limit, while finite-sample monotonicity is approximate.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Gaussian MPPI", "weight": 1.0} -->

In this section, we study the convergence of the commonly used Gaussian MPPI and derive an explicit convergence result using the results from previous sections. In Gaussian MPPI, the control distribution is

<!-- chunk {"id": "body-0039", "role": "body", "section": "Gaussian MPPI", "weight": 1.0} -->

where $\theta = {\{\mu\}}$ is the parameter and $\Sigma$ is a fixed covariance matrix. In this case, $p{(u;\theta)}$ is smooth in $\mu$, locally bounded on compact sets of controls, and satisfies ${p{(u;\theta)}}\rightarrow 0$ for each fixed $u$ as ${\|\theta\|}\rightarrow\infty$. The weighted log-likelihood estimation (4.2) admits a closed-form solution

<!-- chunk {"id": "body-0040", "role": "body", "section": "Gaussian MPPI", "weight": 1.0} -->

which reduces exactly to the standard MPPI update. Using the result from Theorem 4.3. ‣ 4.3 Convergence ‣ 4 Generalized MPPI from EM ‣ Generalized Model Predictive Path Integral Control as Expectation–Maximization"), the Jacobian of the EM mapping at a stationary point is ${{\partial{M{(\theta^{\ast})}}} = {{Cov}_{q{(u;\theta^{\ast})}}{\lbrack u\rbrack}\Sigma^{- 1}}},$ which characterizes the local convergence rate. This shows that the local convergence is governed by the product of the covariance of the importance-weighted distribution and the inverse exploration covariance.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Gaussian MPPI", "weight": 1.0} -->

Next we study the global sufficient increase property of Gaussian MPPI. A Gaussian distribution with fixed covariance can be written in exponential-family form as

<!-- chunk {"id": "body-0042", "role": "body", "section": "Gaussian MPPI", "weight": 1.0} -->

The mapping between $\mu$ and $\eta$ is therefore invertible. Moreover, the log-partition function $A{(\eta)}$ is $\alpha$-strongly convex with $\alpha = {\lambda_{\min}{(\Sigma)}}$ where $\lambda_{\min}{(\Sigma)}$ is the minimum eigenvalue of $\Sigma$. Applying Theorem 5.5. ‣ 5 EM-MPPI for Exponential Family ‣ Generalized Model Predictive Path Integral Control as Expectation–Maximization"), Gaussian MPPI satisfies the global sufficient increase

<!-- chunk {"id": "body-0043", "role": "body", "section": "Mixture of Gaussian (MoG) MPPI", "weight": 1.0} -->

A well-known limitation of Gaussian MPPI is its inability to represent multi-modal distributions. For example, in a car navigation scenario with obstacle avoidance, going left and going right around an obstacle may both be valid choices, while their average trajectory may collide with the obstacle. Motivated by this issue, we consider a mixture of Gaussian distributions

<!-- chunk {"id": "body-0044", "role": "body", "section": "Mixture of Gaussian (MoG) MPPI", "weight": 1.0} -->

where $L$ is the number of Gaussian components and $\theta = {\{\pi_{1},\mu_{1},\ldots,\pi_{L},\mu_{L}\}}$ denotes the parameters. For simplicity, we assume that the covariance matrices are fixed and identical across components. In this case, the weighted maximum likelihood estimation (4.2)

<!-- chunk {"id": "body-0045", "role": "body", "section": "Mixture of Gaussian (MoG) MPPI", "weight": 1.0} -->

Mixture-of-Gaussian control distributions for MPPI have also been explored in prior work on variational-inference control \[undefo\]. This formulation naturally fits into the EM-MPPI framework, where the E-step computes trajectory weights and the M-step updates the mixture parameters.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we consider a Dubins car navigation problem with obstacle avoidance

<!-- chunk {"id": "body-0047", "role": "body", "section": "Experiments", "weight": 1.0} -->

where $v$ is a constant forward velocity and $\deltat$ is the Euler integration step. We sample at least 1024 feasible trajectories for each update.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Sufficient Increase of Gaussian MPPI", "weight": 1.0} -->

We first verify the sufficient increase property of Gaussian MPPI in by considering a simple navigation problem without obstacles. The car starts from the state $x_{1} = {\lbrack 0,0,{\pi/2}\rbrack}$ and the target is $d = {\lbrack 2,1,0\rbrack}$. We run Algorithm 1 for 20 iterations. In Figure 1, we show the sampled trajectories at different iterations.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Cluttered Environment Navigation", "weight": 1.0} -->

Next, we consider a more cluttered environment where the car must reach the goal while avoiding multiple obstacles. We compare Gaussian MPPI and MoG MPPI with two Gaussian components. For both methods, we perform either 1 or 5 iterations of Algorithm 1 before executing each action. It can be seen in Figure 2 that, as the car approaches an obstacle, the feasible trajectories split into two modes corresponding to passing the obstacle from the left or the right. MoG MPPI naturally captures these modes through its mixture distribution. In contrast, Gaussian MPPI approximates the bimodal distribution with a single Gaussian and therefore averages the two directions. As a result, the mean control tends to keep the car moving straight toward the obstacle, producing many infeasible samples. Table 1 shows the total number of sampled trajectories and the fraction of rejected trajectories.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We reinterpret Model Predictive Path Integral (MPPI) control as an Expectation--Maximization (EM) algorithm, showing that repeated MPPI updates perform likelihood ascent on a latent-variable optimality model. This view clarifies the connection between Boltzmann reweighting and weighted maximum-likelihood projection, enables generalized proposal families beyond Gaussians, and yields convergence, local-rate, and sufficient-increase results through classical EM theory. Our analysis focuses on the exact expectation-based iteration; finite-sample Monte Carlo effects and receding-horizon closed-loop behavior remain important directions for future work.
