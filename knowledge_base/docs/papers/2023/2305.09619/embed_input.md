<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Power of Learned Locally Linear Models for Nonlinear Policy Optimization

Topics include Reinforcement learning, Trajectory optimization, Nonlinear control, Linear models, iLQR, Data-driven control, Model-based.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Provides theoretical grounding for why locally linear models learned from data combined with model-based trajectory optimization (iLQR) can achieve sample efficiency for control of nonlinear systems with unknown dynamics.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A common pipeline in learning-based control is to iteratively estimate a model of system dynamics, and apply a trajectory optimization algorithm - e.g. iLQR - on the learned model to minimize a target cost. This paper conducts a rigorous analysis of a simplified variant of this strategy for general nonlinear systems. We analyze an algorithm which iterates between estimating local linear models of nonlinear system dynamics and performing iLQR-like policy updates. We demonstrate that this algorithm attains sample complexity polynomial in relevant problem parameters, and, by synthesizing locally stabilizing gains, overcomes exponential dependence in problem horizon. Experimental results validate the performance of our algorithm, and compare to natural deep-learning baselines.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Machine learning methods such as model-based reinforcement learning have lead to a number of breakthroughs in key applications across robotics and control. A popular technique in these domains is learning-based model-predictive control (MPC), wherein a model learned from data is used to repeatedly solve online planning problems to control the real system. It has long been understood that solving MPC *exactly*--both with perfectly accurate dynamics and minimization to globally optimality for each planning problem--enjoys numerous beneficial control-theoretic properties.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Unfortunately, the above situation is not reflective of practice. For one, most systems of practical interest are *nonlinear*, and therefore exact global recovery of system dynamics suffers from a curse of dimensionality. And second, the nonlinear dynamics render any natural trajectory planning problem nonconvex, making global optimality elusive. In this work, we focus on learning-based trajectory optimization, the "inner-loop" in MPC. We ask *when can we obtain rigorous guarantees about the solutions to nonlinear trajectory optimization under unknown dynamics?*

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We take as our point of departure the $\mathtt{i}\mathtt{L}\mathtt{Q}\mathtt{R}$ algorithm. Initially proposed under known dynamics, $\mathtt{i}\mathtt{L}\mathtt{Q}\mathtt{R}$ solves a planning objective by solving an iterative linear control problem around a first-order Taylor expansion (the *Jacobian linearization*) of the dynamics, and second-order Taylor expansion of the control costs. In solving this objective, $\mathtt{i}\mathtt{L}\mathtt{Q}\mathtt{R}$ synthesizes a sequence of locally-stabilizing feedback gains, and each $\mathtt{i}\mathtt{L}\mathtt{Q}\mathtt{R}$-update can be interpreted as a gradient-step through the closed-loop linearized dynamics in feedback with these gains. This has the dual benefit of proposing a locally stabilizing policy (not just an open-loop trajectory), and of stabilizing the gradients to circumvent exponential blow-up in planning horizon.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

$\mathtt{i}\mathtt{L}\mathtt{Q}\mathtt{R}$, and its variants, are now ubiquitous in robotics and control applications; and, when dynamics are unknown or uncertain, one can simply substitute the exact dynamics model with an estimate (e.g. Levine and Koltun ). In this case, dynamics are typically estimated with neural networks. Thus, Jacobian linearizations can be computed by automated differentiation (AutoDiff) through the learned model.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions. We propose and analyze an alternative to the aforementioned approach of first learning a deep neural model of dynamics, and then performing AutoDiff to conduct the $\mathtt{i}\mathtt{L}\mathtt{Q}\mathtt{R}$ update. We consider a simplified setting with fixed initial starting condition. Our algorithm maintains a *policy*, specified by an open-loop input sequence and a sequence of stabilizing gains, and loops two steps: (a) it learns local linear model of the closed-loop linearized dynamics (in feedback with these gains), which we use to perform a gradient update; (b) it re-estimates a linear model after the gradient step, and synthesizes a new set of set gains from this new model. In contrast to past approaches, our algorithm *only ever estimates linear models of system dynamics.*

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

For our analysis, we treat the underlying system dynamics as continuous and policy as discrete; this reflects real physical systems, is representative of discrete-time simulated environments which update on smaller timescales than learned policies, and renders explicit the effect of discretization size on sample complexity. We consider an interaction model where we query an oracle for trajectories corrupted with measurement (but not process) noise. Our approach enjoys the following theoretical properties.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Using a number of iterations and oracle queries *polynomial* in relevent problem parameters and tolerance $\epsilon$, it computes a policy $\pi$ whose input sequence is an $\epsilon$-first order stationary point for the $\mathtt{i}\mathtt{L}\mathtt{Q}\mathtt{R}$ approximation of the planning objective (i.e., the gradient through the closed-loop linearized dynamics has norm $\leq \epsilon$). Importantly, learning the linearized model at each iteration obviates the need for global dynamics models, allowing for sample complexity polynomial in dimension.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that contribution $\mathbf{1}$ implies convergence to a local-optimality criterion we call an $\epsilon$-approximate *Jacobian Stationary Point* ($\epsilon$-$\mathtt{J}\mathtt{S}\mathtt{P}$); this roughly equates to the open-loop trajectory under $\pi$ having cost within $\epsilon$-*globally optimal* for the linearized dynamics about its trajectory.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

$\mathtt{J}\mathtt{S}\mathtt{P}$s are purely a property of the open-loop inputs, allowing comparison of the quality of the open-loop plan with differing gains. Moreover, the results of Westenbroek et al. show that an approximate $\mathtt{J}\mathtt{S}\mathtt{P}$s for certain planning objective enjoy favorable *global properties*, despite (as we show) being computable from (local) gradient-based search (see Section B.2 ‣ Appendix B Discussion and Extensions ‣ Part I Analysis ‣ The Power of Learned Locally Linear Models for Nonlinear Policy Optimization") for elaboration).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Experimental Findings", "weight": 1.0} -->

We validate our algorithms on standard models of the quadrotor and inverted pendulum, finding an improved performance as iteration number increases, and that the synthesized gains prescribed by $\mathtt{i}\mathtt{L}\mathtt{Q}\mathtt{R}$ yield improved performance over vanilla gradient updates.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Discretization and Feedback Policies", "weight": 1.0} -->

Because digital controllers cannot represent continuous open-loop inputs, we compute $\epsilon$-$\mathtt{J}\mathtt{S}\mathtt{P}$s $\mathbf{u} \in \mathcal{U}$ which are the zero-order holds of discrete-time control sequences. We let $\tau \in {(0,T\rbrack}$ be a discretization size, and set $K = {\lfloor{T/\tau}\rfloor}$. Going forward, we denote discrete-time quantities in colored, bold-seraf font.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Optimization Criteria", "weight": 1.0} -->

Due to nonlinear dynamics, the objectives $\mathcal{J}_{T},\mathcal{J}_{T}^{\pi}$ are nonconvex, so we can only aim for local optimality. Approximate first-order stationary points ($\mathtt{F}\mathtt{O}\mathtt{S}$) are a natural candidate.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Oracle Model and Problem Desideratum", "weight": 1.0} -->

In light of the above discussion, we aim to compute a approximately stationary policy, whose open-loop is therefore an approximate $\mathtt{J}\mathtt{S}\mathtt{P}$ for the original objective. To do so, we assume access to an oracle which can perform feedback with respect to gains $\mathtt{K}_{k}^{\pi}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Oracle 2.1", "weight": 1.0} -->

In words, 2.1 returns entire trajectories by applying feedback along the gains $\mathtt{K}_{k}^{\pi}$. The addition of measurement noise is to introduce statistical tradeoffs that prevent near-exact zero-order differentiation; we discuss extensions to process noise in Section B.4. Because of this, the oracle trajectory in Definition 2.5. ‣ Oracle Model and Problem Desideratum. ‣ 2 Setting ‣ The Power of Learned Locally Linear Models for Nonlinear Policy Optimization") differs from the trajectory dynamics in Definition 2.1 in that the feedback does not subtract off the normal $\mathtt{x}_{k}^{\pi}$; thus, the oracle can be implemented without noiseless access to the nominal trajectory. Still, we assume that the feedback applied by the oracle is exact. Having defined our oracle, we specify the following problem desideratum (note below that $M$ is scaled by $1/\tau$ to capture the computational burden of finer discretization).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Desideratum 1", "weight": 1.0} -->

Given $\epsilon,\epsilon^{\prime}$ and unknown dynamical system $f_{dyn}{( \cdot, \cdot )}$, compute a policy $\pi$ for which (a) $\pi$ is $\epsilon$-stationary, and (b) $\mathbf{u}^{\pi}$ is an $\epsilon^{\prime}$-$\mathtt{J}\mathtt{S}\mathtt{P}$ of $\mathcal{J}_{T}$, using $M$ calls to 2.1, where $M/\tau$ is polynomial in $1/\epsilon$, $1/\epsilon^{\prime}$, and relevant problem parameters.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Algorithm", "weight": 1.0} -->

Our iterative approach is summarized in Algorithm 1 and takes in a time step $\tau > 0$, horizon $T$, a per iteration sample size $N$, iteration number $n_{iter}$, a noise variance $\sigma_{w}$, a gradient step size $\eta > 0$ and a controllability parameter $k_{0}$. The algorithm produces a sequence of polices $\pi^{(n)} = {(\mathtt{u}_{1:K}^{(n)},\mathtt{K}_{1:K}^{(n)})}$, where $K = {\lfloor{T/\tau}\rfloor}$ is the number of time steps per roll-out.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Algorithm", "weight": 1.0} -->

Our algorithm uses the primitive $\text{EstMarkov}{(\pi;N,\sigma_{w})}$ (Algorithm 2), which makes $N$ calls to the oracle to produce estimates ${\hat{\mathtt{x}}}_{1:{K + 1}}$ of the nominal state trajectory, and another $N$ calls with randomly-perturbed inputs of perturbation-variance $\sigma_{w}$ to produce estimates ${({\hat{\mathtt{\Psi}}}_{j,k})}_{k < j}$ of the closed-loop Markov parameters associated to the current policy $\mathtt{\Psi}_{{cl},j,k}^{\pi}$, defined in Definition 4.6. ‣ 4.1 Analysis Overview ‣ 4 Algorithm Analysis ‣ The Power of Learned Locally Linear Models for Nonlinear Policy Optimization"). We use a method-of-moments estimator for simplicity.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Algorithm", "weight": 1.0} -->

At each iteration $n$, Algorithm 1 calls calls $\text{EstMarkov}{(\pi;N,\sigma_{w})}$ first to produce an estimate of the gradient of the closed-loop objective with respect to the current discrete-time nominal inputs.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Algorithm", "weight": 1.0} -->

The form of this estimate corresponds to a natural plug-in estimate of the gradient of the discrete-time objective defined in Definition 4.4. ‣ 4.1 Analysis Overview ‣ 4 Algorithm Analysis ‣ The Power of Learned Locally Linear Models for Nonlinear Policy Optimization"). We use this gradient in Eq. 3.1 to update the current input; this update is rolled-out in feedback with the current feedback controller to produce the nominal input $\mathtt{u}_{1:K}^{({n + 1})}$ for the next iteration (Algorithm 1, 5). Finally, we call EstGains (Algorithm 3), which synthesizes gains for the new policy using a Ricatti-type recursion along a second estimate of the linearized dynamics, produced by unrolling the system with the new nominal input and old gains described above. The algorithm then terminates at $n_{iter}$ iterations and chooses the policy with the smallest estimated gradient that was observed.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Condition 4.1", "weight": 1.0} -->

If $\pi$ and ${\overset{\sim}{\pi}}^{(n)}$ produce bounded inputs, and the resulting state trajectories also remain bounded, then Condition 4.1 will hold for $R_{feas} > 0$ sufficiently large. This is a common assumption in the control literature (see e.g. Jadbabaie and Hauser ), as physical systems, such as those with Lagrangian dynamics, will remain bounded under bounded inputs (see Section B.3 for discussion).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 4.2 (Cost regularity)", "weight": 1.0} -->

To take advantage of stabilizing gains, we require two additional assumptions, which are defined in terms of the $\mathtt{J}\mathtt{L}$ dynamics.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 4.3 (Stabilizability)", "weight": 1.0} -->

The assumption on $\pi^{}$ can easily be generalized to accomodate initial policies with stabilizing gains. Our final assumption is controllability (see e.g. Anderson and Moore ), which is necesssary for identification of system parameters to synthesize stabilizing gains.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 4.4 (Controllability)", "weight": 1.0} -->

There exists constants ${t_{ctrl},\nu_{ctrl}} > 0$ such that, for all feasible $\pi$ and $t \in {\lbrack t_{ctrl},T\rbrack}$,

<!-- chunk {"id": "body-0027", "role": "body", "section": "Analysis Overview", "weight": 1.0} -->

In this section, we provide a high-level sketch of the analysis. Appendix A provides the formal proof, and carefully outlines the organization of the subsequent appendices which establish the subordinate results.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Analysis Overview", "weight": 1.0} -->

As our policies consists of zero-order hold discrete-time inputs, our analysis is mostly performed in discrete-time.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Taylor expansion of the dynamics", "weight": 1.0} -->

To begin, we derive perturbation bounds for solutions to the stabilized ordinary differential equations. Specifically, we provide bounds for when $\mathtt{u}_{1:K}^{\pi}$ is perturbed by a sufficiently small input $\delta\mathtt{u}_{1:K}$. Our formal proposition, Section A.6 states perturbations in both the $\ell_{\infty}$ and normalized $\ell_{2}$-norms; for simplicity, state the special case for $\ell_{\infty}$-perturbation.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Estimation of linearizations and gradients", "weight": 1.0} -->

The last step here is to argue that we also approximately recover $\mathtt{A}_{{ol},k}^{\pi},\mathtt{B}_{{ol},k}^{\pi}$ in Algorithm 3 for synthesizing the gains: for all $k \geq k_{0}$,

<!-- chunk {"id": "body-0031", "role": "body", "section": "Estimation of linearizations and gradients", "weight": 1.0} -->

This consists of two steps: using controllability to show the matrices ${\hat{\mathcal{C}}}_{k,{in}}$ in Algorithm 3 are well-conditioned and using closeness of the Markov operators to show that ${\hat{\mathcal{C}}}_{k,{in}}$ and ${\hat{\mathcal{C}}}_{k,{out}}$ concentrate around their idealized values. Crucially, we only estimate system matrices for $k \geq k_{0}$ to ensure ${\hat{\mathcal{C}}}_{k,{in}}$ is well-defined, and we use window $k_{0} \geq {k_{ctrl} + 2}$ to ensure ${\hat{\mathcal{C}}}_{k,{out}}$ is sufficiently well-conditioned.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Concluding the proof", "weight": 1.0} -->

Sections A.8 and A.9 conclude the proof with two steps: first, we show that cost-function decreases during the gradient step Algorithm 1 at round $n \in {\lbrack n_{iter}\rbrack}$ in proportion to $- {\|{\hat{\nabla}}_{k}^{(n)}\|}^{2}$ (a consequence ofthe standard smooth descent argument). Here, we also apply the aforementioned result that small gradient steps preserve stability: $\mu_{{\overset{\sim}{\pi}}^{(n)}, \star} \leq {2\mu_{\pi^{(n)}, \star}}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Concluding the proof", "weight": 1.0} -->

Second, we argue that the gains synthesized by Algorithm 3 ensure that the Lyapunov stability modulus of $\pi^{({n + 1})}$ and the magnitude of its gains stay bounded by an algorithm-independent constant: $\mu_{\pi^{({n + 1})}, \star} \leq {4\mu_{ric}} = {\mathcal{O}_{\star}{}}$ and $L_{\pi^{({n + 1})}} \leq {\mathcal{O}_{\star}{}}$; we use a novel certainty-equivalence analysis for discretized, time-varying linear systems which may be of independent interest (Appendix F). By combining these two results, we inductively show that all policies constructed satisfy (4.3), namely they have $\mu_{\pi, \star}$ and $L_{\pi}$ at most $\mathcal{O}_{\star}{}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Concluding the proof", "weight": 1.0} -->

We then combine this with the typical analysis of nonconvex smooth gradient descent to argue that the policy $\pi^{(n_{out})}$ has small discretized gradient, as needed.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

Our experiments evaluate the performance of our proposed trajectory optimization algorithm (Algorithm 1) and compare it with the well-established model-based baseline of trajectory optimization ($\mathtt{i}\mathtt{L}\mathtt{Q}\mathtt{R}$) on top of learned dynamics (e.g. Levine and Koltun ). Though our analysis considers a fixed horizon, we perform experiments in a receeding horizon control (RHC) fashion. We consider two control tasks: (a) a pendulum swing up task, and (b) a 2D quadrotor stabilization task. We implement our experiments using the jax Bradbury et al. ecosystem. More details regarding the environments, tasks, and experimental setup details are found in Appendix J. Though our analysis considers the noisy oracle model, all experiments assume *noiseless* observations.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Least-squares vs. Method-of-Moments", "weight": 1.0} -->

Algorithm 1 prescribes the method-of-moments estimator to simplify the analysis; in our implementation, we find that estimating the transition operators using regularized least-squares instead yields to more sample efficient gradient estimation. This choice can also be analyzed with minor modifications (see e.g. Oymak and Ozay; Simchowitz et al. ).

<!-- chunk {"id": "body-0037", "role": "body", "section": "$\\mathtt{i}\\mathtt{L}\\mathtt{Q}\\mathtt{R}$ baseline", "weight": 1.0} -->

We first collect a training dataset according to a prescribed exploration strategy, then train a neural network dynamics model on these dynamics, and finally optimize our policy by applying the $\mathtt{i}\mathtt{L}\mathtt{Q}\mathtt{R}$ algorithm directly on the learned model. We consider several variants of our $\mathtt{i}\mathtt{L}\mathtt{Q}\mathtt{R}$ baseline which use different exploration strategies and different supervision signals for model learning.

<!-- chunk {"id": "body-0038", "role": "body", "section": "$\\mathtt{i}\\mathtt{L}\\mathtt{Q}\\mathtt{R}$ baseline", "weight": 1.0} -->

Sampling strategies: We consider two sampling strategies; (a) Opt runs $\mathtt{i}\mathtt{L}\mathtt{Q}\mathtt{R}$ with the ground truth cost and dynamics in a receeding horizon fashion, performing noiseless rollouts and perturbing the resulting trajectories with noise to encourage exploration, and (b) Rand executes rollouts with random inputs starting from random initial conditions. The rationale is that the Opt strategy provides better data coverage for the desired task than Rand.

<!-- chunk {"id": "body-0039", "role": "body", "section": "$\\mathtt{i}\\mathtt{L}\\mathtt{Q}\\mathtt{R}$ baseline", "weight": 1.0} -->

Loss supervision: The standard loss supervision for learning dynamics is to regress against the next state transition. Inspired by our analysis, we also consider an idealized oracle that augments the supervision to also include noiseless the Jacobians of the ground truth model with respect to both the state and control input; we refer to this augmentation as JacReg.

<!-- chunk {"id": "body-0040", "role": "body", "section": "$\\mathtt{i}\\mathtt{L}\\mathtt{Q}\\mathtt{R}$ baseline", "weight": 1.0} -->

Model architecture: We use a fully connected three layer MLP network to for fitting the dynamics of the environment. Specifically, our model takes in input $(\mathtt{x}_{k},\mathtt{u}_{k})$ and predicts the state difference $\mathtt{x}_{k + 1} - \mathtt{x}_{k}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Discussion", "weight": 1.5} -->

We observe that Algorithm 1 with feedback-gains consistently outperforms Algorithm 1 without gains, validating the important of locally-stabilized dynamics. Second, we see that the performance of the $\mathtt{i}\mathtt{L}\mathtt{Q}\mathtt{R}$ baselines does not significantly improve as more trajectory data is collected. We find that our learned models achieve very low train and test error, over the sampling distribution (i.e., Opt or Rand) used for learning. For Rand, we postulate that the distribution shift incurred by performing RHC via trajectory optimization on the learned model limits the closed-loop performance of our baseline.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Discussion", "weight": 1.5} -->

However, we note that Opt+JacReg achieves stellar performance early, suggesting that (a) the Opt data collection method suffices for strong closed-loop performance (notice that Rand+JacReg fares far worse), and (b) that a second limiting factor is that estimating *dynamics* and performing automated differentiation is less favorable than directly estimating *Jacobians*, which are the fundamental quantities used by the $\mathtt{i}\mathtt{L}\mathtt{Q}\mathtt{R}$ algorithm. This gap between estimation of dynamics and derivatives has been observed in prior work Pfrommer et al..

<!-- chunk {"id": "body-0043", "role": "body", "section": "Discussion", "weight": 1.5} -->

Though we find that our method outperforms deep-learning baselines (excluding OPT+JacReg) on the simpler inverted pendulum environment, the learning+$\mathtt{i}\mathtt{L}\mathtt{Q}\mathtt{R}$ approaches fare better on the quadrotor. We suspect that this is attributable to data-reuse, as Algorithm 1 estimates an entirely new model of system dynamics at each iteration. We believe that finding a way to combine the advantages of directly estimating linearized dynamics (observed in Algorithm 1, as well as OPT+JacReg) with the advantages of data-reuse.
