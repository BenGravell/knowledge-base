<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Policy Gradient for LQR with Domain Randomization

Topics include Robustness, Control, Policy gradients, DR, Linear quadratic regulator.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Domain randomization (DR) enables sim-to-real transfer by training controllers on a distribution of simulated environments, with the goal of achieving robust performance in the real world. Although DR is widely used in practice and is often solved using simple policy gradient (PG) methods, understanding of its theoretical guarantees remains limited. Toward addressing this gap, we provide the first convergence analysis of PG methods for domain-randomized linear quadratic regulation (LQR). We show that PG converges globally to the minimizer of a finite-sample approximation of the DR objective under suitable bounds on the heterogeneity of the sampled systems. We also quantify the sample-complexity associated with achieving a small performance gap between the sample-average and population-level objectives. Additionally, we propose and analyze a discount-factor annealing algorithm that obviates the need for an initial jointly stabilizing controller, which may be challenging to find. Empirical results support our theoretical findings and highlight promising directions for future work, including risk-sensitive DR formulations and stochastic PG algorithms.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Domain randomization (DR) has emerged as a dominant paradigm to enable transfer of policies optimized in simulation to the real world by randomizing simulator parameters during training. In doing so, just as with robust control, DR accounts for discrepancies between the model used in simulation to synthesize a policy and the system that it is deployed. However, unlike conventional robust control approaches, DR minimizes an average control objective over the uncertainty in the system rather than a worst case objective. Since DR does not solely focus on optimizing the worst-case performance, it can result in less conservative controller performance while still ensuring robust stability with high probability. Furthermore, DR can be easily implemented via first order methods. This makes it straightforward to incorporate into a wide variety of reinforcement learning schemes and to benefit from the increasing availability of parallel computation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite the ease with which DR can be implemented using first order methods, ensuring convergence of these methods remains a critical challenge, with practitioners relying upon complex scheduling of various hyperparameters in the optimization procedure. Motivated by this challenge, we rigorously study the convergence of policy gradient methods for DR in the setting of the linear quadratic regulator.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Domain Randomization", "weight": 1.0} -->

Domain randomization, introduced by Tobin et al., is widely used for enabling *sim-to-real transfer*. By randomizing simulator parameters during training, it aims to produce policies robust to simulator variations, thereby enabling transfer to the real-world. The sampling distribution may be a design variable in the synthesis problem, or come from a learning procedure, e.g. as the posterior distribution of a Bayesian identification procedure. Recently, the approach has been applied in areas like autonomous racing and robotic control. The control community has used similar randomized approaches to achieve high-probability guarantees (e.g. scenario optimization and related methods ). Recent work has explored generalization of domain randomization in discrete Markov Decision Processes and for continuous control. However, finding optimization procedures which minimize the domain randomization objective remains a challenge, with many empirical studies relying on heurisic approaches like curriculum learning. In this work, we rigorously study the convergence of policy gradient for minimizing the domain randomization objective for linear quadratic control.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Policy Gradient Methods", "weight": 1.0} -->

Global convergence of policy gradient methods was first established for linear quadratic control, relying upon a condition known as *gradient dominance* to demonstrate that driving the gradient to zero suffices to ensure convergence to the optimal solution. Subsequently, the results have been extended to a multitude of settings including mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$, Markovian jump systems, and output estimation. Hu et al. provide a comprehensive survey on convergence studies of policy optimization methods for continuous control. There are two works closely related to domain randomization: Gravell et al. and Wang et al.. Gravell et al. study a related setting with multiplicative noise on the system, which resembles domain randomization but with variations drawn independently at each time step. Consequently, the resulting optimal controller exhibits robustness primarily in an average sense, rather than explicitly accounting for structured uncertainty as in domain randomization. Wang et al. study a federated approach to minimize the average LQR cost over a collection of systems; however, they prove convergence only up to a gap defined in terms of the heterogeneity between the systems.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Policy Gradient Methods", "weight": 1.0} -->

In contrast, we prove that as long as the systems are sufficiently similar, an approximate gradient domination condition suffices to ensure convergence of policy gradient methods to the globally optimal solution. We focus exclusively on model-based analysis; the extension of our results to the model free setting involves routine extension of the analysis for the variance of gradient estimates from prior work.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

We study the convergence of policy gradient methods applied to the domain randomized LQR objective and establish the following results: DR Objective Approximation: We propose optimizing a sample average approximation of the DR objective defined in terms of a finite number of sampled systems. We characterize the excess cost incurred by the solution to the approximate problem on the original objective.

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

Policy Gradient Convergence: We prove that a first order policy gradient algorithm converges to the globally optimal solution for the sample average approximation of the DR objective. This is the first result showing that policy gradient methods converge to the optimal solution for domain randomized LQR problems, removing the heterogeneity bias that appears in prior work.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

Joint Stabilization: We propose a first order gradient descent algorithm based on discount factor annealing which provably converges to a controller stabilizing a collection of dynamical systems, extending prior work to the multi-system setting.

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

The above contributions establish the convergence properties of first order gradient-based algorithms applied to the DR objective for continuous control. Given the prevalence of DR for the practice of learning-enabled robotic control and the engineering challenges involved in achieving convergent optimization procedures for the DR objective, we view this result as an important step towards the analysis and design of reliable reinforcement learning algorithms for sim-to-real transfer. Motivated by this, we include a number of empirical results highlighting limitations and open questions regarding the analysis of this work. These include the generalization of the DR objective to risk metrics other than the expectation and the convergence of stochastic policy gradient algorithms.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

For a fixed parameter $\theta$, we define the infinite horizon linear quadratic regulation cost function in terms of positive definite matrices $Q \succeq I$ and $R = I$ as where the superscript $K$ indicates that the expectation is taken under the feedback policy $u_{t} = {Kx_{t}}$.^22^2Generalization to $Q \nsucceq I$ $R \neq I$ can be achieved by rescaling the cost by ${1/\lambda_{\min}}{(Q)}$ and the input as ${B{(\theta)}}\leftarrow{B{(\theta)}R^{- {1/2}}}$. The goal of DR is to determine a controller $K$ which minimizes the expectation of the LQR objective over a distribution of systems, as in prior work on sampling-based control. Such a distribution can be hand-designed to capture parametric uncertainty, or learned through Bayesian system identification. In particular, we let $\Theta$ be a random variable with density $p_{\Theta}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The domain randomization problem is then to find $K_{DR}^{\star} \triangleq {{\operatorname{argmin}_{K}J_{DR}}{(K)}}$, with To solve this problem, we propose applying gradient descent to a finite sample approximation to objective. We use $M$ independently sampled systems ${\theta_{1},\ldots,\theta_{M}} \sim p_{\Theta}$ to construct such a finite-sample approximation: and apply policy gradient methods to find its minimizer.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

In particular, we start from a controller $K_{0}$, and iteratively update the controller as where $\alpha$ is a fixed stepsize and, as shown in Fazel et al., the gradient ${\nabla_{K}J}{(K,\theta_{i})}$ for system $i$ is given by In the above expression, $\Sigma_{K}^{i}$ is the steady state covariance of system $i$ under controller $K$, and $E_{K}^{i}$ can be written in terms of the Lyapunov equation defining the LQR cost of applying controller $K$ to system $i$: The primary technical challenge in proving convergence of the above scheme to the minimizer of is that the approach to show gradient domination by Fazel et al. does not generalize to the sample average LQR cost for $M \geq 2$. Consequently, we introduce an additional assumption which ensures the support of the distribution $p_{\Theta}$ is suitably small.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption II.1 (Heterogeneity bound)", "weight": 1.0} -->

The bound on $\varepsilon_{\mathsf{H}\mathsf{E}\mathsf{T}}$ is a technical condition for our analysis. It scales inversely with $\left\| {B{(\theta)}} \right\|$ and the trace of the Riccati equation. In particular, if the systems are too heterogeneous, our analysis cannot guarantee convergence.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption II.1 (Heterogeneity bound)", "weight": 1.0} -->

Given the above condition, we demonstrate the convergence of policy gradient methods. The proof consists of three parts. We first show that policy gradient methods converge to the minimizer of the sample average objective $J_{SA}{(K)}$ starting from an initial controller $K_{0}$ which simultaneously stabilizes $\theta_{1},\ldots,\theta_{M}$ and achieves a sufficiently small cost $J_{SA}{(K_{0})}$. We then introduce a discount factor scheduling scheme to achieve convergence from an arbitrary initial controller. Finally, we characterize the discrepancy between the empirical objective and its population counterpart.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Policy Gradient Convergence", "weight": 1.0} -->

We now prove convergence of the gradient update to the minimizer of the sample average LQR objective. Denote this minimizer by ${K_{SA}^{\star} \triangleq {{\operatorname{argmin}_{K}J_{SA}}{(K)}}}.$ To show convergence, we impose an additional assumption that the initial controller simultaneously stabilizes all systems.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption III.1 (Simultaneous Stabilization)", "weight": 1.0} -->

We assume that $K_{0} \in \mathcal{K}$ where To achieve sufficient conditions to ensure that converges starting from such a $K_{0}$, we introduce a definition that characterizes the cost of a controller on a particular sample in terms of the sample average cost of that controller.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Stabilization", "weight": 1.0} -->

The previous section analyzed the convergence of the policy gradient method on a collection of sampled instances starting from an initial stabilizing controller. Here, we remove the requirement that we have access to an initial controller which simultaneously stabilizes all systems and incurs a small cost. We do so by incorporating a discounting factor annealing scheme. In particular, consider scaling the matrices $A{(\theta_{i})}$ and $B{(\theta_{i})}$ by a factor $\sqrt{\gamma}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Stabilization", "weight": 1.0} -->

Therefore, if we start from a small discount factor, run several iterations of, and then increase the discount factor, we will be able to ensure convergence to a controller that simultaneously stabilizes all systems. Algorithm 1 extends a similar scheme proposed in Perdomo et al. for the single system setting to the multi-system setting we consider. We let $J_{SA}{( \cdot |\gamma)}$ denote the sample average cost evaluated on the discounted systems $({\sqrt{\gamma}A{(\theta_{i})}},{\sqrt{\gamma}B{(\theta_{i})}})$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Stabilization", "weight": 1.0} -->

1:Input: collection of systems, θ1, …, θM, optimization tolerance ε 3:Find the largest γ ∈ (0, 1] satisfying 5: Set K ← K′, where K′ is such that ${{{J_{SA}{(\left. K' \middle| \gamma \right.)}} - {\inf\limits_{\overset{\sim}{K}}{J_{SA}{(\left.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Stabilization", "weight": 1.0} -->

\overset{\sim}{K} \middle| \gamma \right.)}}}} \leq d_{\mathsf{X}}}.$ 6: Find a discount factor γ′ ∈ [γ, 1] such that 2.5JSA(K|γ) ≤ JSA(K|γ′) ≤ 4JSA(K|γ) 8:Run starting from K to find K′ such that $${{{J_{SA}{(K')}} - {\inf\limits_{\overset{\sim}{K}}{J_{SA}{(\overset{\sim}{K})}}}} \leq \varepsilon}.$$ Algorithm 1 Discount Annealing Subproblems and can be solved via bisection, while subproblem can be solved with algorithm starting from $K_{0}\leftarrow K$ by choosing an appropriate stepsize, and running sufficiently many iterations, as in Theorem III.1. ‣ III Policy Gradient Convergence ‣ Policy Gradient for LQR with Domain Randomization").

<!-- chunk {"id": "body-0023", "role": "body", "section": "Stabilization", "weight": 1.0} -->

Extending the analysis of \[21, Theorem 1\] to the setting of multiple systems leads to the following result.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Sampling", "weight": 1.0} -->

The previous sections provided guarantees ensuring that a gradient-based algorithm converges to the minimizer of objective. In this section, we bound the suboptimality incurred by optimizing the sample average cost rather than the desired domain randomization objective. In particular, let $\overset{\sim}{K}$ be a the iterate of running the aforementioned gradient procedure.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Sampling", "weight": 1.0} -->

Note that if ${J{(K,\theta)}} \leq \mathcal{J}$, then by Hoeffding's inequality, it holds that with probability at least $1 - \delta$, To establish the bound $\mathcal{J}$, consider ${\overset{\sim}{\theta},\theta} \in \mathcal{S}$. We show in Lemma IX.9 that under Assumption II.1. ‣ II Problem Formulation ‣ Policy Gradient for LQR with Domain Randomization"), ${J{(K_{DR}^{\star},\overset{\sim}{\theta})}} \leq {6J{({K{(\theta)}},\theta)}}$ and ${J{(\overset{\sim}{K},\overset{\sim}{\theta})}} \leq {48J{({K{(\theta)}},\theta)}}$. This leads to the following characterization of the excess cost.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We conduct numerical experiments on the discretized and linearized inverted pendulum defined by We suppose that the parameters ${dt} = 0.01$ and $g = 10$ are known. The unknown parameters $m$ and $\ell$ are modeled with a uniform distribution over the interval $\lbrack 0.75,1.25\rbrack$. For policy update in Algorithm 1, we run 20 iterations of with a stepsize $\alpha = {1 \times 10^{- 3}}$ instead of explicitly evaluating the inequality. Refer to the code for more details.^44^4Code available at this GitHub repository

<!-- chunk {"id": "body-0027", "role": "body", "section": "Alternative Risk Metrics", "weight": 1.0} -->

We can consider risk metrics other than the expectation for defining the objective. For example, we could replace the expectation the entropic risk measure of temperature $t$: The gradient-based optimization of a Monte Carlo approximation proposed in the previous sections can still be applied in this setting by replacing the average gradient of with the gradient of: We lack theoretical convergence guarantees for this approach; however, Figure 2 validates it numerically. We see that the proposed algorithm still converges with this alternative risk metric and achieves the optimal controller for the risk-sensitive objective. This result opens the future direction of risk-sensitive domain randomized control.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Stochastic Gradient Descent", "weight": 1.0} -->

Prior experiments verified that the approach analyzed in sections Section III-V is valid for the numerical example of stabilizing a pendulum linearized about the upright position. In Figure 3, we demonstrate a stochastic gradient descent approach which samples a new system at every iteration and takes a gradient step with that system, detailed in Algorithm 2.^55^5The update is performed with the gradient of the discounted cost for the sampled system. The discounting ensures stabilization by the current iterate. This also converges, although we lack theoretical guarantees theoretical convergence guarantees. The figure plots the mean and standard deviation over 5 random seeds. The cost $J_{DR}{(K)}$ is approximated via Monte Carlo, as in the previous experiments. The initial stepsize is chosen as $\alpha = {2 \times 10^{- 4}}$ and the discount coefficient is $\gamma_{0} = 0.99$. We see that the controller converges to achieve approximately the same cost on the domain randomization objective as the batch algorithm with $M = 500$ samples from Figure 1.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Stochastic Gradient Descent", "weight": 1.0} -->

1:Input: distribution pΘ, iterations N, stepsize α, discount coefficient γ0 Algorithm 2 Stochastic Gradient Descent Figure 3: Stochastic Gradient Descent (Algorithm 2) applied to the linearized inverted pendulum of.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Rotary Inverted Pendulum Experiments", "weight": 1.0} -->

We also verify the Algorithm 1 on a Quanser Qube Servo 2 rotary inverted pendulum to study how it can help to overcome the sim-to-real gap. We consider the scenario where we have coarse estimates of several physical parameters, and compare the controller synthesized with DR against the LQR controller which takes these coarse estimates as ground truth. The DR controller achieves a higher success rate by holding a pendulum upright and around the center.^66^6The experiment video can be found at this YouTube link. Details are deferred to the appendix.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Discussion", "weight": 1.5} -->

There are several exciting possibilities for theoretical and empirical extensions of the results presented in this paper.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Discussion", "weight": 1.5} -->

Relaxed heterogeneity assumptions: Our theory required strong requirements on the distance between systems. These requirements can almost certainly be made weaker; however, it is unclear the extent to which they are fundamental. Our numerical experiments failed to discover any instances where policy gradient did not converge due to a large distance between systems, unless it was impossible to simultaneously stabilize these systems.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Discussion", "weight": 1.5} -->

Extensions of the convergence analysis: Our numerical experiments tested a variation of the algorithm (stochastic gradient descent) and an alternative risk metric (entropic risk) for domain randomization for which we do not have theoretical convergence guarantees, and saw empirical success. It would be interesting to provide convergence proofs for these approaches. In particular, stochastic gradient descent closer resembles the way that domain randomization is implemented in practice. Meanwhile, the entropic risk (or alternative metrics) may better represent the goal of domain randomization to provide robustness to uncertainty. Indeed, entropic risk interpolates between DR as $t\rightarrow 0$, and robust control as $t\rightarrow\infty$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Discussion", "weight": 1.5} -->

Practical implications: The study conducted in this paper provides a better understanding of the application of gradient-based approaches for reinforcement learning with domain randomization. It may be possible to use this perspective to design alternative hyperparameter schedules for domain randomization as applied in practice.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our work proves the convergence of policy gradient methods applied to linear quadratic control with domain randomization. The analysis relies upon a generalization of the gradient domination condition from prior work. This generalization results in guarantees that are sensitive to the initialization; however, a curriculum learning approach with an appropriate schedule can bypass this sensitivity. We believe that this line of analysis has potential to demystify and improve heuristic approaches for taming the optimization landscape of DR from the robot learning literature.
