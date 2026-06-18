<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Planning with Learned Dynamics: Probabilistic Guarantees on Safety and Reachability via Lipschitz Constants

Topics include Learned dynamics, Feedback motion planning, Safety guarantees, Reachability, Lipschitz constants, Sampling-based planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Plans with learned control-affine dynamics while bounding model error through estimated Lipschitz constants and feedback-law existence constraints. The result is a sampling-based planner that returns nominal plans with probabilistic safety, reachability, and local goal-stability guarantees under the learned-model trust region.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a method for feedback motion planning of systems with unknown dynamics which provides probabilistic guarantees on safety, reachability, and goal stability. To find a domain in which a learned control-affine approximation of the true dynamics can be trusted, we estimate the Lipschitz constant of the difference between the true and learned dynamics, and ensure the estimate is valid with a given probability. Provided the system has at least as many controls as states, we also derive existence conditions for a one-step feedback law which can keep the real system within a small bound of a nominal trajectory planned with the learned dynamics. Our method imposes the feedback law existence as a constraint in a sampling-based planner, which returns a feedback policy around a nominal plan ensuring that, if the Lipschitz constant estimate is valid, the true system is safe during plan execution, reaches the goal, and is ultimately invariant in a small set about the goal. We demonstrate our approach by planning using learned models of a 6D quadrotor and a 7DOF Kuka arm. We show that a baseline which plans using the same learned dynamics without considering the error bound or the existence of the feedback law can fail to stabilize around the plan and become unsafe.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Planning and control with guarantees on safety and reachability for systems with unknown dynamics has long been sought-after in the robotics and control community. Model-based optimal control can achieve this if the dynamics are precisely modeled, but modeling assumptions inevitably break down when applied to real physical systems due to unmodeled effects from friction, slip, flexing, etc. To account for this gap, data-driven machine learning methods and robust control seek to sidestep the need to precisely model the dynamics a priori. While robust control can provide strong guarantees when the unmodeled component of the dynamics is small and satisfies strong structural assumptions, such methods requires an accurate prior which may not be readily available. In contrast, machine learning methods are flexible but often lack formal guarantees, precluding their use in safety-critical applications. For instance, small perturbations from training data cause drastically poor and costly predictions in stock prices and power consumption. Since even small perturbations from the training distribution can yield untrustworthy results, applying AI systems to predict dynamics can lead to unsafe, unpredictable behavior.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

To address this gap, we propose a method for planning with learned dynamics which yields probabilistic guarantees on safety, reachability, and goal invariance in execution on the true system. Our core insight is that we can determine where a learned model can be trusted for planning using the Lipschitz constant of the error (the difference between the true and learned dynamics), which also informs how well the training data covers the task-relevant domain. Under the assumption of deterministic true dynamics, we can plan trajectories in this trusted domain with strong safety guarantees for an important class of learned dynamical systems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Specifically, with a Lipschitz constant, we can bound the difference in dynamics between a novel point (that our model was not trained on) and a training point. Since the bound grows with the distance to training points, we can naturally define a domain where the model can be trusted as the set of points within a certain distance to training points. Conversely, to obtain a small bound over a desired domain, it is necessary to have good training data coverage in the task-relevant domain. At a high level, to obtain a small bound on the error in a domain, we want to have good coverage over the domain and regularity of the learned model via the Lipschitz constant of the error.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Our safety and reachability guarantees ultimately rely on an overestimate of the smallest Lipschitz constant. To find an estimate that exceeds the smallest Lipschitz constant with a given probability $\rho$, we use a statistical approach based on Extreme Value Theory and validate its result with a Kolmogorov-Smirnov goodness-of-fit test. If the test validates our estimate, we can choose a confidence interval with an upper bound that overestimates the true Lipschitz constant with probability $\rho$. Our method requires the estimation of three Lipschitz constants, translating to system safety and reachability guarantees which hold with a probability of at least $\rho^{3}$. This guarantee is fairly strong as it holds for all time, unlike many methods offering probabilistic guarantees on a per trajectory or episode basis.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

If the learned dynamics have at least as many controls as states and are control-affine (note we do not assume the true dynamics are also control-affine), then we also determine conditions for the existence of a feedback controller that tightly tracks the planned trajectory in execution under the true dynamics. The tight tracking error bound yields favorable properties for our planner and controller: if we have a valid Lipschitz constant estimate for a sufficiently-accurate learned model, 1) we guarantee safety if no obstacle is within the tracking error of the trajectory, 2) we guarantee we can reach the goal within a small tolerance, and 3) if we can assert a feedback law that keeps the system at the goal exists, then the closed-loop system is guaranteed to remain in a small region around the goal. In this paper, we assume the learned dynamics are control-affine, deterministic, and have at least as many controls as states (such as a robotic arm under velocity control), the true dynamics are deterministic, and that independent samples of the true dynamics can be taken in the domain of interest.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

A method to bound error between two general dynamics functions in a domain by using a Lipschitz constant

<!-- chunk {"id": "body-0010", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

A condition for uncertain control-affine systems that guarantees the existence of a feasible feedback law

<!-- chunk {"id": "body-0011", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

A planner that probabilistically guarantees safety and closed-loop stability-like properties about the goal for learned dynamics with as many controls as states

<!-- chunk {"id": "body-0012", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Evaluation on a 7DOF Kuka arm and a 6D quadrotor

<!-- chunk {"id": "body-0013", "role": "body", "section": "METHOD", "weight": 1.0} -->

Secs. IV-A - IV-B and IV-C - IV-D cover our approaches to Probs. 1 and 2, respectively. In Sec. IV-A, we show how $L_{f - g}$ can establish a trusted domain and how $L_{f - g}$ can be estimated in Sec. IV-B. In Sec. IV-C, we design a planner that ensures safety, that the system remains in the trusted domain, and that a feedback law maintaining minimal tracking error exists. We present the full algorithm in Sec. IV-D.

<!-- chunk {"id": "body-0014", "role": "body", "section": "IV-A The trusted domain", "weight": 1.0} -->

For many systems, we are only interested in a task-relevant domain, and it is often impossible to collect data everywhere in state space, especially for high-dimensional systems. Hence, it is natural that our learned model is only accurate near training data. With a Lipschitz constant of the error, we can precisely define how accurate the learned dynamics are in a domain constructed from the training data. We note this derivation can also be done for systems without the control-affine assumption on the learned dynamics, and thus it can still be useful for determining where a broader class of learned models can be trusted. However, removing the control-affine structure makes controller synthesis much more difficult, and is the subject of future work.

<!-- chunk {"id": "body-0015", "role": "body", "section": "IV-A The trusted domain", "weight": 1.0} -->

Consider a single training point $(\overline{x},\overline{u})$ and a novel point $(x,u)$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "IV-A The trusted domain", "weight": 1.0} -->

The above relation describes the error at a novel point, but we can also generalize to any domain $D$. Define $b_{T}$ to be the dispersion of $\mathcal{S} \cap D$ in $D$ and define $e_{T}$ to be the maximum training error of the learned model. Explicitly,

<!-- chunk {"id": "body-0017", "role": "body", "section": "IV-A The trusted domain", "weight": 1.0} -->

Then, we can uniformly bound the error across the entire set $D$ to yield a simple and exact relation between $f$ and $g$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-A The trusted domain", "weight": 1.0} -->

See Fig. 1 for an example of these quantities.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A The trusted domain", "weight": 1.0} -->

In the next section we discuss selection of $\mathcal{S}_{D}$, its role in estimating $L_{f - g}$, and how $r$ is selected.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-B Estimating the Lipschitz constant", "weight": 1.0} -->

For to hold over all of $D$, we require that $L_{f - g}$ is a Lipschitz constant for the error. We use results from Extreme Value Theory to obtain an estimate ${\hat{L}}_{f - g}$ that overestimates $L_{f - g}$, i.e. ${\hat{L}}_{f - g} \geq L_{f - g}$, with a user-defined probability $\rho$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B Estimating the Lipschitz constant", "weight": 1.0} -->

We build on -, which find an estimate ${\hat{L}}_{h}$ of the Lipschitz constant $L_{h}$ for a function $h{(z)}$ over a domain $\mathcal{Z}$ by estimating the location parameter $\gamma$ of a three-parameter reverse Weibull distribution, which for a random variable $W$ has the cumulative distribution function (CDF)

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-B Estimating the Lipschitz constant", "weight": 1.0} -->

From the Fisher-Tippett-Gnedenko Theorem, $s$ follows one of the Frechet, reverse Weibull, or Gumbel distributions in the limit as $N_{L}$ approaches infinity. If $s$ follows the reverse Weibull distribution, which we validate in our results using the Kolmogorov-Smirnov (KS) goodness-of-fit test with a significance value of 0.05 (the same threshold used in ), then $L_{h}$ is finite and equals $\gamma$. We estimate $L_{h}$ using the location parameter $\hat{\gamma}$ of a reverse Weibull distribution fit via maximum likelihood to $N_{S}$ samples of $s$. Finally, we compute a confidence interval $c = {\Phi^{- 1}{(\rho)}\xi}$ on $\hat{\gamma}$. Here $\xi$ is the standard error of the fit $\hat{\gamma}$, which correlates with the quality of the fit, and $\Phi{( \cdot )}$ is the standard normal CDF.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B Estimating the Lipschitz constant", "weight": 1.0} -->

We select the upper end of the confidence interval as our estimate ${\hat{L}}_{h} = {\hat{\gamma} + c}$, which overestimates $L_{h}$ with probability $\rho$. Note that increasing $\rho$ increases $c$, improving the safety probability at the cost of loosening ${\hat{L}}_{h}$, which can make planning more conservative. We also note that this probability is valid in the limit as $N_{L}$ approaches infinity, due to the Fisher-Tippett-Gnedenko theorem making claims only on the asymptotic distribution. We summarize the estimation method in Alg. 1.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B Estimating the Lipschitz constant", "weight": 1.0} -->

5fit reverse Weibull to {sj} to obtain γ̂ and standard error ξ
6 validate fit using KS test with significance level 0.05
if validated return L̂h = γ̂ + Φ−1 (ρ) ξ else return failure
Algorithm 1 Lipschitz estimation for h (z) over 𝒵

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B Estimating the Lipschitz constant", "weight": 1.0} -->

We wish to choose $D$ to be large enough for planning while also keeping $L_{f - g}$ small. To achieve this, we use a filtering procedure to reduce the impact of outliers in $\mathcal{S}$. Let $\mu$ and $\sigma$ be the mean and standard deviation of the error over $\mathcal{S}$. Then, let $\mathcal{S}_{D} = \left. \{{{(\overline{x},\overline{u})} \in \mathcal{S}} \middle| {{\|{{f{(\overline{x},\overline{u})}} - {g{(\overline{x},\overline{u})}}}\|} \leq {\mu + {a\sigma}}}\} \right.$ where $a$ is a user-defined parameter. Then, we run Alg. 2 in order to grow $D$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-B Estimating the Lipschitz constant", "weight": 1.0} -->

This method works by proposing values of $r$, estimating $L_{f - g}$, and increasing $r$ until $r > \epsilon$ or $L_{f - g} \geq 1$. Finding $D$ with $r > \epsilon$ and $L_{f - g} < 1$ is useful for planning (described further in Sec. IV-C, see ). Note that, in Euclidean spaces, $r \geq b_{T}$. If no filtering is done, $r = b_{T}$, since no point in $D$ is further than a distance $r$ from $\mathcal{S}_{D}$ and the furthest any point in $D$ can lie from a point in $\mathcal{S}_{D}$ is $r$; however, filtering shrinks $D$ and thus decreases the dispersion, making it possible that $r \geq b_{T}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-B Estimating the Lipschitz constant", "weight": 1.0} -->

The parameter $a$ should be chosen to balance the size of $D$ against the magnitude of $L_{f - g}$, which we tune heuristically.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-B Estimating the Lipschitz constant", "weight": 1.0} -->

This filtering lets us exclude regions where our learned model is less accurate, yielding smaller $e_{T}$. Note that filtering does not affect the i.i.d. property of the samples needed for Alg. 1; it only applies a mask to the domain. We also note that Alg. 2 returns a minimum value for $r$, but a larger $r$ can be chosen as long as $L_{f - g}$ is estimated with Alg. 1. A larger $r$ makes planning easier by expanding the trusted domain.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-B Estimating the Lipschitz constant", "weight": 1.0} -->

4 construct D using equation
5 estimate Lf − g using Alg. 1 and Ψ
6 calculate ϵ using equation
7 if Lf − g ≥ 1 then return failure
8 if r &gt; ϵ then return r and D
9 else r ← ϵ + α // α is a small constant
Algorithm 2 Selecting r and D

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-B Estimating the Lipschitz constant", "weight": 1.0} -->

While we never explicitly address the assumption that the true dynamics are deterministic, the estimated Lipschitz constant may be unbounded in the stochastic case, such as when two samples have the same inputs but different outputs due to noise, causing a division by 0 in line 3 of Alg. 1.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-B Estimating the Lipschitz constant", "weight": 1.0} -->

$L_{g_{0}}$ and $L_{g_{1}}$ may also be estimated with Alg. 1, which we employ in the results. Alternatively, can give tight upper bounds on the Lipschitz constant of neural networks, though it could not scale to the networks used in our results. Other approaches improve scalability at the cost of looser Lipschitz upper bounds, and will be examined in the future.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-C Planning", "weight": 1.0} -->

We want to plan a trajectory from start $x_{I}$ to goal $x_{G}$ using the learned dynamics while remaining in $\mathcal{X}_{\text{safe}}$ in execution. We constrain the system to stay inside $D$, as model accuracy may degrade outside of the trusted domain. We develop a planner similar to a kinodynamic RRT, growing a search tree $\mathcal{T}$ by sampling controls that steer towards novel states until we reach the goal. If a path is found the we can ensure the goal is reachable with safety guarantees.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-C1 Staying inside $D$", "weight": 1.0} -->

To remain inside the set $D$, we introduce another set $D_{\epsilon}:={D \ominus {\mathcal{B}_{\epsilon}{}}}$, which is the Minkowski difference between $D$ and a ball of radius $\epsilon$. Every point in $D_{\epsilon}$ is at least a distance of $\epsilon$ from any point in the complement of $D$. Since the learned dynamics differs from the true dynamics by at most $\epsilon$ in $D$, controlling to a point in $D_{\epsilon}$ under the learned dynamics ensures the system remains within $D$ under the true dynamics (see Fig. 2).

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-C1 Staying inside $D$", "weight": 1.0} -->

How do we determine if a query point $(x,u)$ is inside of $D_{\epsilon}$? Since we define $D$ to be a union of balls, it would suffice to find a subset of training points $\mathcal{W} \subset S_{D}$ such that the union of $r$-balls about the training points completely covers an $\epsilon$-ball about $(x,u)$. Explicitly,

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-C1 Staying inside $D$", "weight": 1.0} -->

In general, checking is difficult, but if $L_{f - g} < 1$ and

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-C1 Staying inside $D$", "weight": 1.0} -->

then only one training point within a distance $r - \epsilon$ is needed to ensure a query point is in $D_{\epsilon}$ (see Fig. 3). Note by Alg. 2 lines 2-2, either is guaranteed or $L_{f - g} \geq 1$, in which we return failure.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-C2 One step feedback law", "weight": 1.0} -->

To prevent drift in execution, we also seek to ensure the trajectory planned with RRT can be tracked with minimal error. One key requirement to guarantee a feedback law exists is that the system is sufficiently actuated under the learned dynamics. This requires that ${\text{dim}{(\mathcal{U})}} \geq {\text{dim}{(\mathcal{X})}}$. The check for sufficient actuation is done on a per state basis and can be done as we grow $\mathcal{T}$. This feedback law ensures that, under the learned dynamics, we can return to a planned trajectory in exactly one step.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-C2 One step feedback law", "weight": 1.0} -->

Suppose we are executing a trajectory $(x_{0},\ldots,x_{K})$ with corresponding control $(u_{0},\ldots,u_{K - 1})$ planned with the learned dynamics, and the system is currently at $x_{k - 1}$. Under the learned dynamics, the plan is to move to $x_{k} = {g{(x_{k - 1},u_{k - 1})}}$, but, under the true dynamics, the system will end up at some ${\overset{\sim}{x}}_{k} = {f{(x_{k - 1},u_{k - 1})}}$ which is no more than an $\epsilon$ distance from $x_{k}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-C2 One step feedback law", "weight": 1.0} -->

Our goal is to find an input ${\overset{\sim}{u}}_{k}$ such that $x_{k + 1} = {g{({\overset{\sim}{x}}_{k},{\overset{\sim}{u}}_{k})}}$. If this one-step feedback law exists for all $1 \leq k \leq {K - 1}$, it ensures the executed trajectory stays within $\epsilon$ distance of the planned trajectory (see Fig. 4).

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-C2 One step feedback law", "weight": 1.0} -->

With Lipschitz constants $L_{g_{0}}$ and $L_{g_{1}}$, we can bound how much the learned dynamics varies in the $\epsilon$-ball about $x_{k}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-C2 One step feedback law", "weight": 1.0} -->

Prior to execution, we seek to answer two questions: when does ${\overset{\sim}{u}}_{k}$ exist and does ${\overset{\sim}{u}}_{k}$ lie in the control space $\mathcal{U}$ (for instance in the presence of box constraints)? Results from the literature give a bound on the difference between the nominal solution $u_{k}$ and perturbed solution ${\overset{\sim}{u}}_{k}$,

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-C2 One step feedback law", "weight": 1.0} -->

If ${\overset{\sim}{u}}_{k}$ exists and satisfies the control constraints for all $1 \leq k \leq {K - 1}$, then we ensure that the system will track the path up to an $\epsilon$ error under the one-step feedback law. In planning, we add the existence of a valid one step feedback law as a check when growing the search tree.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-C3 Ensuring safety and invariance about the goal", "weight": 1.0} -->

The exact nature of this check depends on the system and definition of $\mathcal{X}_{\text{unsafe}}$. For example, in our experiments on quadrotor, the state includes the quadrotor's position in ${\mathbb{R}}^{3}$ and $\mathcal{X}_{\text{unsafe}}$ is defined by unions of boxes in ${\mathbb{R}}^{3}$. By defining a bounding sphere that completely contains the quadrotor, we can verify a path is safe via sphere-box intersection. With the Kuka arm, we randomly sample joint configurations in an $\epsilon$-ball about states, transform the joint configurations via forward kinematics, and check collisions in workspace. While this method is not guaranteed to validate the entire ball around a state, in practice no collisions resulted from execution of plans. Another approach computes a free-space bubble around a given state $x$ and check if it contains $\mathcal{B}_{\epsilon}{(x)}$, however this is known to be conservative.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-C3 Ensuring safety and invariance about the goal", "weight": 1.0} -->

To stay near the goal after executing the trajectory, we use the same perturbed linear equation to ensure the existence of a one-step feedback law. Here, rather than checking the next state along the trajectory is reachable from the previous, we check that the final state is reachable from itself, i.e. $x_{K}$ is reachable from $x_{K}$. Similar to the arguments above, we can repeatedly execute the feedback law to ensure the system remains in an $({\epsilon + \lambda})$-ball about the goal.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-D Algorithm", "weight": 1.0} -->

We present our full method, Learned Models in Trusted Domains (LMTD-RRT), in Alg. 3. In practice, we implemented SampleState and SampleControl in two different ways: uniform sampling and perturbations from training data. Sampling perturbations (up to a norm of $r - \epsilon$) does not exclude valid $(x,u)$ pairs since all points in $D_{\epsilon}$ lie within $r - \epsilon$ from a training point, and, in cases where $D_{\epsilon}$ is a relatively small volume, can yield a faster search. However, it also biases samples near regions where training data is more dense. We define the set $\mathcal{S}_{\mathcal{X}} = \left.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-D Algorithm", "weight": 1.0} -->

\{\overline{x} \middle| {{\exists{\overline{u}\text{s.t.}{(\overline{x},\overline{u})}}} \in \mathcal{S}_{D}}\} \right.$ to describe the optimistic check described in Sec. IV-C1. NN finds the nearest neighbor and OneStep checks that a valid feedback exists as described in Sec. IV-C2. Model evaluates the learned dynamics and InCollision checks if an $\epsilon$-ball is in $\mathcal{X}_{\text{safe}}$ as described in Sec. IV-C3.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-D Algorithm", "weight": 1.0} -->

Input: xI, xG, S𝒳, SD, r, ϵ, λ, Nsamples, goal_bias
6 xnew← SampleState(goal_bias)
19 ubest ← u, xbest ← xnext

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-D Algorithm", "weight": 1.0} -->

Once a plan has been computed, it can be executed in closed-loop with Alg. 4. ModelG0 and ModelG1 evaluate $g_{0}$ and $g_{1}$ of the learned model. SolveLE solves the linear equation and Dynamics executes the true dynamics $f$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "RESULTS", "weight": 1.0} -->

We present results on 1) a 2D system to illustrate the need for remaining near the trusted domain, 2) a 6D quadrotor to show scaling to higher-dimensional systems, and 3) a 7DOF Kuka arm simulated in Mujoco to show scaling to complex dynamics that are not available in closed form. Using $\rho = 0.975$, we plan with LMTD-RRT and rollout the plans in open-loop (no computation of ${\overset{\sim}{u}}_{k}$) and closed-loop (Alg. 4). We compare with a naïve kinodynamic RRT that skips the checks on lines 3, 3, 3-3 of Alg. 3 in both open and closed loop. See the video for experiment visualizations.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-A 2D Sinusoidal Model", "weight": 1.0} -->

where ${\DeltaT} = 0.2$. We are given 9000 training points $(x_{i},u_{i},{f{(x_{i},u_{i})}})$, where $x_{i}$ is drawn uniformly from an 'L'-shaped subset of $\mathcal{X}$ (see Fig. 5) and $u_{i}$ is drawn uniformly from $\mathcal{U} = {\lbrack{- 1},1\rbrack}^{2}$. $g_{0}{(x)}$ and $g_{1}{(x)}$ are modeled with separate neural networks with one hidden layer of size 128 and 512, respectively. We select $a = 3$ in Alg. 2. 1000 more samples are used to estimate $L_{f - g}$ via Alg. 1, which we validate with a KS test with a $p$ value of $0.56$, far above the $0.05$ threshold significance value.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-A 2D Sinusoidal Model", "weight": 1.0} -->

See Fig. 5 for examples of the nominal, open-loop, and closed-loop trajectories planned with LMTD-RRT and a naïve kinodynamic RRT. The plan computed with LMTD-RRT remains in regions where we can trust the learned model (i.e. within $D_{\epsilon}$) and the closed-loop execution of the trajectory converges to $\mathcal{B}_{\epsilon + \lambda}{(x_{G})}$. In contrast, both the open-loop and closed-loop execution of the naïve RRT plan diverge.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-A 2D Sinusoidal Model", "weight": 1.0} -->

We provide statistics in Table I of maximum $\ell_{2}$ tracking error $\max_{i \in {\{ 1,\ldots,T\}}}{\|{{\overset{\sim}{x}}_{i} - x_{i}}\|}$ and final $\ell_{2}$ distance to the goal ${\|{{\overset{\sim}{x}}_{T} - x_{G}}\|}_{2}$ for both the open loop (OL) and closed loop (CL) variants, averaged over 70 random start/goal states. To give the baseline an advantage, we fix the start/goal states and plan with naïve RRT using two different dynamics models: 1) the same learned dynamics model used in LMTD-RRT and 2) a learned dynamics model with the same hyperparameters trained on the full dataset ($10^{4}$ datapoints), and report the statistics on the minimum of the two errors.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-A 2D Sinusoidal Model", "weight": 1.0} -->

The worst case tracking error for the plan computed with LMTD-RRT was $0.199$, which is within the guaranteed tracking error bound of $\epsilon = 0.215$, while despite the data advantage, plans computed with naïve RRT suffer from higher tracking error. Average planning times for LMTD-RRT and naïve RRT are 4.5 and 17 seconds, respectively. Overall, this suggests that planning with LMTD-RRT avoids regions where model error may lead to poor tracking, unlike planning with a naïve RRT.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-B 6D Quadrotor Model", "weight": 1.0} -->

We select $a = 6$ in Alg. 2. We use $10^{6}$ more samples in Alg. 1 to estimate $L_{f - g}$, and conduct a KS test resulting in a $p$-value of $0.43 \gg 0.05$. We obtain $\hat{\gamma} = 0.205$, $c = 0.011$, and $\epsilon = 0.134$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-B 6D Quadrotor Model", "weight": 1.0} -->

See Fig. 6 for examples of the planned, open-loop, and closed-loop trajectories planned with LMTD-RRT and a naïve RRT. The trajectory planned with LMTD-RRT remains close to the training data, and the closed-loop system tracks the planned path with $\epsilon$-accuracy converging to $\mathcal{B}_{\epsilon + \lambda}{(x_{G})}$. We note that using the feedback controller to track trajectories planned with naïve RRT tends to worsen the tracking error, implying our learned model is highly inaccurate outside of the domain. We provide statistics in Table II for maximum tracking error and distance to goal, averaged over 100 random start/goal states. The worst case closed-loop tracking error for trajectories planned with LMTD-RRT is $0.011$, again much smaller than $\epsilon$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-B 6D Quadrotor Model", "weight": 1.0} -->

As with the 2D example, we give the baseline an advantage in computing tracking error statistics by reporting the minimum of the two errors when planning with 1) the same model used in LMTD-RRT and 2) a model trained on the full dataset ($10^{7}$ points). Despite the data advantage, the plans computed using naïve RRT have much higher tracking error. Average planning times for our unoptimized code are 100 sec. for LMTD-RRT and 15 min. for naïve RRT, suggesting that sampling focused near the training data can improve planning efficiency.

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-B 6D Quadrotor Model", "weight": 1.0} -->

We also evaluate LMTD-RRT on an obstacle avoidance problem (Fig. 7). We perform collision checking as described in Sec. IV-C3. As the tracking error tubes (of radius $\epsilon = 0.134$) centered around the nominal trajectories never intersect with any obstacles, we can guarantee that the system never collides in execution. Empirically, in running Alg. 3 over 500 random seeds to obtain different nominal paths, the closed-loop trajectory never collides. In contrast, the naïve RRT plan fails to be tracked and collides (Fig. 7, right).

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-C 7DOF Kuka Arm in Mujoco", "weight": 1.0} -->

We evaluate our method on a 7DOF Kuka iiwa arm simulated in Mujoco using a Kuka model. We train two models using different datasets, one for evaluating tracking error without the presence of obstacles (Table III), and the other for obstacle avoidance. For both models, $g_{0}{(x)}$ is again set to be $x$ while $g_{1}{(x)}$ is learned with a neural network with one hidden layer of size 4000. For the results in Table III, we are provided 2475 training data tuples, which are collected by recording continuous state-control trajectories from an expert and evaluating $f{(x,u)}$ on the trajectories and on random state-control perturbations locally around the trajectories. We select $a = 5$ in Alg. 2. 275 more samples are used in Alg. 1 to estimate $L_{f - g}$, validated with a KS test with a $p$ value of $0.58 \gg 0.05$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "V-C 7DOF Kuka Arm in Mujoco", "weight": 1.0} -->

We obtain $\hat{\gamma} = 0.087$ and $c = 0.001$, leading to $\epsilon = 0.111$. In Table III, we provide statistics on maximum tracking error and distance to goal under plans with LMTD-RRT and the naïve RRT baseline (with a model trained on the full dataset of 2750 points), averaged over 25 runs of each method. Notably, closed-loop tracking of plans found with LMTD-RRT have lowest error, with a worst case error much smaller than $\epsilon = 0.111$. Planning takes on average 1.552 and 0.167 sec. for LMTD-RRT and naïve RRT, respectively. We suspect the naïve RRT exploits poor dynamics outside of $D$, expediting planning.

<!-- chunk {"id": "body-0060", "role": "body", "section": "V-C 7DOF Kuka Arm in Mujoco", "weight": 1.0} -->

For the obstacle avoidance example (Fig. 8), we are provided 15266 datapoints, which again take the form of continuous trajectories plus perturbations. We select $a = 8$ in Alg. 2, and use 1696 more points to estimate $L_{f - g}$ using Alg. 1, which we validate with a KS test with a $p$ value of $0.37 \gg 0.05$. We obtain $\hat{\gamma} = 0.156$ and $c = 0.010$, leading to $\epsilon = 0.111$. In planning, as described in Sec. IV-C3, we perform collision checking by randomly sampling configurations in an $\epsilon$-ball about each point along the trajectory. Though this collision checker is not guaranteed to detect collision, in running LMTD-RRT over 20 random seeds, we did not observe collisions in execution for any of the 20 plans, and the arm safely reaches the goal without collision. Over these trajectories, the worst case tracking error is $0.107$, which remains within $\epsilon = 0.111$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "V-C 7DOF Kuka Arm in Mujoco", "weight": 1.0} -->

One such plan computed by LMTD-RRT and the corresponding open-loop and closed-loop tracking trajectories, is shown in the top row of Fig. 8. The three trajectories nearly overlap exactly due to small tracking error. In contrast, the naïve RRT plan cannot be accurately tracked, even with closed-loop control, due to planning outside of the trusted domain, causing the executed trajectories to diverge and collide with the table.

<!-- chunk {"id": "body-0062", "role": "body", "section": "DISCUSSION AND CONCLUSION", "weight": 1.5} -->

We present a method to bound the difference between learned and true dynamics in a given domain and derive conditions that guarantee a one-step feedback law exists. We combine these two properties to design a planner that can guarantee safety, goal reachability, and that the closed-loop system remains in a small region about the goal.

<!-- chunk {"id": "body-0063", "role": "body", "section": "DISCUSSION AND CONCLUSION", "weight": 1.5} -->

While the method presented has strong guarantees, it also has limitations which are interesting targets for future work. First, the true dynamics are assumed to be deterministic. Stochastic dynamics may be possible by estimating the Lipschitz constant of the mean dynamics while also appropriately modeling the noise. Second, the actuation requirement limits the systems that this method can be applied to. For systems with ${\text{dim}{(\mathcal{U})}} < {\text{dim}{(\mathcal{X})}}$, it may be possible to construct a similar feedback law that guarantees the learned dynamics will lie within a tolerance of planned states which, in turn, could still give strong guarantees on safety and reachability.
