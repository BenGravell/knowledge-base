<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Fast Non-Episodic Adaptive Tuning of Robot Controllers with Online Policy Optimization

Topics include Reinforcement learning, Robotics, Aerial robotics, Online algorithms, Optimization, Control, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study online algorithms to tune the parameters of a robot controller in a setting where the dynamics, policy class, and optimality objective are all time-varying. The system follows a single trajectory without episodes or state resets, and the time-varying information is not known in advance. Focusing on nonlinear geometric quadrotor controllers as a test case, we propose a practical implementation of a single-trajectory model-based online policy optimization algorithm, M-GAPS,along with reparameterizations of the quadrotor state space and policy class to improve the optimization landscape. In hardware experiments,we compare to model-based and model-free baselines that impose artificial episodes. We show that M-GAPS finds near-optimal parameters more quickly, especially when the episode length is not favorable. We also show that M-GAPS rapidly adapts to heavy unmodeled wind and payload disturbances, and achieves similar strong improvement on a 1:6-scale Ackermann-steered car. Our results demonstrate the hardware practicality of this emerging class of online policy optimization that offers significantly more flexibility than classic adaptive control, while being more stable and data-efficient than model-free reinforcement learning.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

We study the problem of optimizing a parameterized non-linear robot control policy in an online setting. A deployed robot may face unpredictable changes in both environment and task, and must adapt to them immediately. Therefore, we consider a protocol where the dynamics, policy class, and cost functions are all time-varying and revealed online: the optimization algorithm has no knowledge of how they will vary in the future. The algorithm is evaluated on a single trajectory without episodes or state resets. As a case study, we focus on nonlinear trajectory tracking control for quadrotors.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Policy optimization has been widely studied in the control and machine learning communities from varying perspectives. We are interested in methods that: Can be applied to general nonlinear dynamics and costs.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optimize a given policy class (vs. prescribe their own).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Are adaptive -- do not rely on stationarity assumptions on the dynamics or costs.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Are efficient enough to run onboard a microcontroller.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The criteria 1-2 rule out most adaptive control methods, which involve a co-designed policy and adaptive law and have limited ability to optimize costs besides quadratic tracking. Reinforcement learning (RL) is more general, but the criteria 3-4 rule out methods but that rely on a replay memory, which assumes stationarity and is computationally expensive. Policy gradient RL avoids these issues, but popular methods assume that dynamics and costs are unknown, leading to slow, data-inefficient learning that that impedes adaptivity.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

For many practical robotic systems, adaptive control is too restrictive, but RL is too general. Engineers often design the cost function and know an approximate dynamics model, but model-free policy gradient RL fails to use this information. New automatic differentiation algorithms and software have broadened the scope of differentiable policy classes and dynamics models, including general rigid bodies, finite element models, and fluids, among many others. However, differentiable models are still approximate, and not always useful. Therefore, in this work we include an "apples-to-apples" comparison of model-based and model-free methods in real time on hardware.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our protocol is structurally similar to online optimization. In *stateless* online optimization with certain convex functions, it has been shown that online gradient descent yields minimax-optimal regret. However, in the *stateful* online *policy* optimization problem, it is not obvious how to apply the same algorithmic principle. One simple approach is to artificially impose episodes, but this fails to account for the influence of previous actions on each episode's initial state. It also causes large step changes in policy and adds another hyperparameter to tune. On the other hand, a simple non-episodic method was shown to obtain optimal regret in linear systems when the closed-loop dynamics under the policy class satisfy a form of contractiveness. However, in nonlinear systems, the analysis only provides a *local regret* bound analogous to tracking a moving stationary point, leaving it unclear if this method works well in practice.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions. We conduct real-hardware experiments comparing three algorithms that extend the online gradient descent principle to online policy optimization: a model-free episodic method OPRF, a model-based episodic method DiffTune, and a model-based non-episodic method M-GAPS. We propose reparameterizations of the quadrotor state space and policy class to improve the optimization landscape for all methods. We study three scenarios: 1) initialization with suboptimal parameters, 2) a strong time-varying wind, and 3) a heavy unmodeled payload. In setting 1, we find that M-GAPS performs best overall. DiffTune is close when the episode length is optimal, but significantly worse otherwise; OPRF lags further. In settings 2-3, we confirm that M-GAPS outperforms an expert hand-tuned baseline despite an imperfect dynamics model. Setting 3 also demonstrates fast adaptivity to strongly time-varying dynamics. We verify that these positive results extend to other hardware with an experiment on a 1:6-scale off-road car.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Together, our results show that the model-based, non-episodic algorithm M-GAPS is a promising approach for general-purpose, data-efficient, and fully-online robotic controller tuning.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Protocol", "weight": 1.0} -->

Finally, the learner observes the partial derivatives of $\pi_{t}$, $f_{t}$, and $g_{t}$ about $(x_{t},u_{t},\theta_{t})$. This protocol repeats along a single trajectory, without any resetting or episodes, for $T$ timesteps. The learner's goal is to select the parameters $\theta_{t}$ online to minimize the total cost $\sum_{t = 0}^{T - 1}{c_{t}{(x_{t},u_{t})}}$. Note that our setting can express known time-invariant dynamics with unknown adversarial additive disturbances as a special case.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Adaptive Control", "weight": 1.0} -->

The field of adaptive control focuses on specific structures of unknown time-varying dynamics. The most widely studied nonlinear systems are those of the form $x_{t + 1} = {{g_{t}{(x_{t},u_{t})}} + {\phi{(x_{t})}^{\top}a_{t}}}$, where the nominal model $g_{t}$ is known, $\phi:{{\mathbb{R}}^{n}\mapsto{\mathbb{R}}^{n \times k}}$ is a known feature mapping, and $a_{t} \in {\mathbb{R}}^{k}$ is unknown. A proxy ${\hat{a}}_{t}$ for $a_{t}$ is updated by the adaptive law and used in the policy.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Adaptive Control", "weight": 1.0} -->

In estimation-based laws, ${\hat{a}}_{t}$ is updated to reduce the prediction error $\left\| {x_{t + 1} - {g{(x_{t},u_{t})}} - {\phi{(x_{t})}^{\top}{\hat{a}}_{t}}} \right\|_{2}^{2}$, which is not directly related to any optimality criterion. However, in tracking-based laws, ${\hat{a}}_{t}$ is updated to reduce the tracking error $\left\| {x_{t + 1} - x_{t + 1}^{d}} \right\|_{2}^{2}$ where $x^{d}$ is a desired state, making them interpretable as a form of policy optimization. Composite laws combine both objectives.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Adaptive Control", "weight": 1.0} -->

In the highly-studied "matched-disturbance" case, the dynamics take a restricted form that enables straightforward adaptive controllers with Lyapunov stability analysis. Although recent work has relaxed the matched-disturbance condition, the policy class still takes a prescribed form incompatible with the quadrotor controller considered in this paper. Also, while Lyapunov analysis delivers exponential contraction of $\left\| {x_{t} - x_{t}^{d}} \right\|_{2}^{2}$, it lacks guarantees for general time-varying costs.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Adaptive Control", "weight": 1.0} -->

Other tools from control theory related to our setting are iterative learning control (ILC) and self-tuning regulators (STRs). ILC accounts for realized (not worst-case) nonstochastic disturbances, but it assumes a cyclic setting, whereas we allow arbitrary changes. STRs perform online system identification and repeatedly solve optimal control synthesis on the estimated model. This implies that control synthesis is easy given the model, which does not hold in our setting. Many adaptive control schemes have been proposed specifically for quadrotors, but we consider algorithms that can be applied to general systems and use quadrotors as a test case.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Adaptive Control", "weight": 1.0} -->

Although the methods we investigate are more expressive than typical adaptive control in terms of policy optimization, they are complementary in terms of dynamics learning. Adaptive control with a pure estimation-based law can work *in tandem* to provide online estimates of the dynamics $g_{t}$ consumed by the online policy optimization algorithm. The resulting estimator-optimizer combination can be theoretically sound under assumptions not significantly stronger than those required by each in isolation.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

RL is generally divided into *value-based* methods that approximate the optimal value function, and *policy-based* methods that optimize a parameterized class of policies. In the latter case, when the system model is unknown, this optimization is both stochastic and derivative-free. Algorithms can be based on exploration in the action space (REINFORCE and descendants ), or in the parameter space. In either case, these methods deploy the same policy parameter $\theta$ for a horizon of $H$ steps and construct an unbiased estimator of $\nabla_{\theta}{\sum_{s = t}^{{t + H} - 1}{f_{s}{(x_{t},u_{t})}}}$. Typical analysis assumes the episodic structure comes from the problem itself, and the state is reset to a fixed distribution for each episode. However, under suitable mixing assumptions or infinite-horizon discounted objectives, one can enact the episode divisions artificially and still obtain results in the single-trajectory setting.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

But the choice of episode length becomes a hyperparameter, and these methods do not use any knowledge of the $g_{t},f_{t}$, so they are data-hungry.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

If a model is available, one can compute the episode cost gradient $\nabla_{\theta}{\sum_{s = t}^{{t + H} - 1}{f_{s}{(x_{t},u_{t})}}}$ analytically. However, naive optimization in simulation without any trajectory data from the real system is prone to exploiting model errors, and may be counterproductive for stiff or discontinuous systems even when the model is correct. The method of uses a model-based gradient taken about the true system trajectories in an episodic manner, and is one of the baselines we study in this work. Many other methods have been proposed to mitigate model error exploitation for policy optimization under learned models or to improve the optimization conditioning. Most of this work focuses on time-invariant but complex settings and is computationally expensive, whereas we consider time-varying settings and simpler algorithms.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

In contrast to typical policy-based RL, value-based RL methods targeting infinite-horizon discounted objectives can often handle the single-trajectory protocol without imposing artificial episodes. Although their objective is not formally compatible with fast-changing $g,f$, they can work in slowly time-varying settings. Methods based on $Q$-learning struggle with real-time application in continuous action spaces because taking ${\operatorname{argmax}_{u}Q}{(x,u)}$ is a hard nonconvex optimization problem. A more suitable family is the actor-critic methods, which optimize a policy and value function simultaneously. If a dynamics model is available, actor-critic methods can approximate the state-value function instead of the more complex (state, action)-value $Q$ function. However, even the simplest possible algorithm in this class requires many tuning and design decisions. For the baselines in this work, we focus on methods in the policy gradient family that are simple and computationally lightweight.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Online Policy Optimization", "weight": 1.0} -->

Recently, ideas from online optimization have been applied to obtain regret-optimal algorithms for control problems with online time-varying dynamics and/or costs, as in our setting. Initial work considered only adversarial disturbances and cost functions with a known linear time-invariant system. Although later extended to unknown time-invariant, known time-varying, and partially observed systems, this family prescribes specialized policy classes that depend strongly on the linearity of the dynamics. A different line of work focuses on optimizing arbitrary policy classes when the closed-loop dynamics satisfy a particular notion of contractiveness. These methods recover optimal regret when instantiated with linear dynamics and appropriate policy classes, but also provide a weaker "local regret" guarantee under contractive dynamics but nonconvex optimization, as elaborated in §III-A ‣ III Methods ‣ Fast Non-Episodic Adaptive Tuning of Robot Controllers with Online Policy Optimization"). This case is especially relevant for the complex nonlinear systems encountered in robotics. We select the algorithm of for our experiments, as it has the lightest memory and computation needs.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Methods", "weight": 1.0} -->

In this section, we define the three algorithms used in our experiments. As discussed in §I, each algorithm can be interpreted as applying the algorithmic spirit of online gradient descent to the online policy optimization problem.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A Single-trajectory method (M-GAPS)", "weight": 1.0} -->

parameter θ0, learning rate η. Observe xt + 1 and derivatives of gt and ft. Algorithm 1 Non-episodic, model-based (M-GAPS) The non-episodic online policy optimization algorithm M-GAPS was introduced and analyzed in a meta-framework alongside online dynamics estimation. Here, we consider a simplified case where (approximate) dynamics are known and the parameter set $\Theta$ is an unconstrained Euclidean space. M-GAPS provides theoretical guarantees in nonlinear, nonconvex settings. To state these guarantees precisely, we introduce the concept of *surrogate cost* to evaluate a policy parameter $\theta$ at a particular timestep.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A Single-trajectory method (M-GAPS)", "weight": 1.0} -->

When $F_{t}$ is convex in $\theta$ for all timesteps $t$, M-GAPS targets the metric of *policy regret*, where $x_{t},u_{t}$ are the states and actions visited by the online learner. Examples of convex $F_{t}$ include linear dynamics with disturbance-action control or model-predictive control with disturbance predictions and confidence coefficients. In the convex case, the online gradient descent (OGD) update $\theta_{t + 1}\leftarrow{\theta_{t} - {\eta{\nabla F_{t}}{(\theta_{t})}}}$ with a suitable learning rate $\eta$ is minimax-optimal for minimizing $R_{P}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A Single-trajectory method (M-GAPS)", "weight": 1.0} -->

However, quadrotor and car dynamics are nonlinear, making the $F_{t}$ nonconvex. In this case, M-GAPS targets the *local regret* an online analog to stationary-point conditions in nonconvex optimization. In both cases, performing OGD on the surrogate costs $F_{t}$ is well-motivated theoretically. However, it requires more computation and information than is practical. To see this, we apply one step of the chain rule to ${\nabla F_{t}}{(\theta)}$, obtaining All derivative dependence on past dynamics and policy functions is encapsulated in the "sensitivity" term $\partial{x_{t}^{\theta}/{\partial\theta}}$, which is computed recursively via the chain rule as $\left.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-A Single-trajectory method (M-GAPS)", "weight": 1.0} -->

\partial x_{0}^{\theta}/\partial\theta = \mathbf{0} \right.$ and In the hypothetical case where we deploy a constant ${\theta_{0},\ldots,\theta_{t - 1}} = \theta$, the recursive step (4 ‣ III Methods ‣ Fast Non-Episodic Adaptive Tuning of Robot Controllers with Online Policy Optimization")) computes $\partial{x_{t}^{\theta}/{\partial\theta}}$ from a previously computed $\partial{x_{t - 1}^{\theta}/{\partial\theta}}$ in $O{}$ time. However, if the online algorithm is changing $\theta$ constantly, then the intermediate steps used to compute $\partial{x_{t - 1}^{\theta_{t - 1}}/{\partial\theta_{t - 1}}}$ are useless for computing $\partial{x_{t}^{\theta_{t}}/{\partial\theta_{t}}}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-A Single-trajectory method (M-GAPS)", "weight": 1.0} -->

Instead, the complete state trajectory $x_{0}^{\theta_{t}},\ldots,x_{t}^{\theta_{t}}$ must be "re-simulated". This incurs $\Omega{(t)}$ computational cost, which quickly becomes intractable. It also requires oracle access to ${(f_{s},\pi_{s})}_{s = 0}^{t}$ and ${(g_{s})}_{s = 0}^{t - 1}$ at the "re-simulated" states, which may be unreasonable.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-A Single-trajectory method (M-GAPS)", "weight": 1.0} -->

Therefore, the ideal of OGD on the surrogate costs $F_{t}$ is not a practical algorithm. Instead, M-GAPS forms a computationally efficient approximation of ${\nabla F_{t}}{(\theta_{t})}$ with error small enough to yield optimal regret. M-GAPS computes the recursion as in (4 ‣ III Methods ‣ Fast Non-Episodic Adaptive Tuning of Robot Controllers with Online Policy Optimization")) *without* re-simulation, essentially "ignoring" the fact that $\theta_{t}$ is changing online.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-A Single-trajectory method (M-GAPS)", "weight": 1.0} -->

Specifically, it maintains an internal state $y_{t} \in {\mathbb{R}}^{n \times d}$ that approximates the sensitivity $\partial{x^{\theta_{t}}/{\partial\theta_{t}}}$, with the dynamics All derivatives are taken about the actually-visited trajectory ${(x_{s},u_{s})}_{s = 0}^{t}$, so previously computed results are never invalidated and only $O{}$ computation is used per step. M-GAPS then performs an approximate online gradient descent update $\theta_{t + 1} = {\theta_{t} - {\eta G_{t}}}$, where $\eta > 0$ is the learning rate and The algorithm steps are summarized in Algorithm 1 ‣ III Methods ‣ Fast Non-Episodic Adaptive Tuning of Robot Controllers with Online Policy Optimization").

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A1 Contractiveness and guarantees", "weight": 1.0} -->

M-GAPS's gradient approximation $G_{t}$ is valid when the closed-loop dynamics of the system and policy class are *contractive*.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-A1 Contractiveness and guarantees", "weight": 1.0} -->

Intuitively, each policy parameter $\theta$ steers the state towards its "preferred trajectory" $x_{t}^{\theta}$ with exponential convergence if deployed for several steps in a row. If contractiveness holds, along with a careful choice of learning rate $\eta$ and mild smoothness assumptions, then the policy parameter $\theta_{t}$ changes slowly enough to guarantee that $G_{t}$ is a good approximation of the ideal ${\nabla F_{t}}{(\theta)}$ for OGD. This, in turn, leads to the regret (1 ‣ III Methods ‣ Fast Non-Episodic Adaptive Tuning of Robot Controllers with Online Policy Optimization")) and local regret (2 ‣ III Methods ‣ Fast Non-Episodic Adaptive Tuning of Robot Controllers with Online Policy Optimization")) guarantees of M-GAPS.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-A1 Contractiveness and guarantees", "weight": 1.0} -->

These theoretical conditions naturally generalize a key property of linear dynamical systems under stabilizing policies. However, they are conservative, and verification can be hard. They are sufficient conditions for the local regret bound of M-GAPS, but they are not known to be necessary. Further, even when they are verified and the local regret bound (2 ‣ III Methods ‣ Fast Non-Episodic Adaptive Tuning of Robot Controllers with Online Policy Optimization")) holds, it does not preclude the possibility of getting stuck in bad local minima. We emphasize that M-GAPS can be instantiated even when these assumptions cannot be proven. It is important to validate its performance empirically in these cases. parameter θ1, learning rate η, episode length H. for each episode k ∈ 1, …, ⌈T/H⌉ do Observe xt + 1 and derivatives of gt and ft. Update y as in using parameter θk. Algorithm 2 Episodic, model-based (DiffTune)

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-B Episodic methods", "weight": 1.0} -->

As discussed in the related work §II, we compare M-GAPS to episodic policy gradient methods but consider the episode length $H$ a tunable hyperparameter in a non-episodic world. For each episode $k \in {1,\ldots,{\lceil{T/H}\rceil}}$, these methods deploy a constant parameter $\theta_{k}$ and approximate the gradient We call this an approximation because it is computed as if the initial state $x_{{({k - 1})}H}$ were fixed by nature, whereas it actually depends on previously deployed parameters $\theta_{1},\ldots,\theta_{k - 1}$. We consider a *model-based* variant from the literature that maintains a sensitivity state recursively, similar to M-GAPS, and a *model-free* variant that applies a state-of-the-art algorithm for derivative-free online optimization.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-B1 Episodic, model-based (DiffTune )", "weight": 1.0} -->

With known dynamics, we can compute $G_{pg}$ analytically. In contrast to model-based policy gradient methods that use a simulator in a sim-to-real paradigm, such as, we take the gradient about the real system's state trajectory and only use the model for derivatives. We use the same sensitivity state $y$ and recurrence (5 ‣ III Methods ‣ Fast Non-Episodic Adaptive Tuning of Robot Controllers with Online Policy Optimization")) of M-GAPS to compute the gradient efficiently, yielding Algorithm 2 ‣ III Methods ‣ Fast Non-Episodic Adaptive Tuning of Robot Controllers with Online Policy Optimization"). Cheng et al. proposed this method and conducted hardware experiments similar to ours. However, they treat episodes as part of "nature" and do not consider the effect of imposing episodes on a non-episodic problem. parameter θ1, learning rate η, episode length H, perturbation radius ϵ.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-B1 Episodic, model-based (DiffTune )", "weight": 1.0} -->

for each episode k ∈ 1, …, ⌈T/H⌉ do Sample perturbed “query” parameter: $\theta_{k + 1}\leftarrow{\theta_{k} - {\frac{\eta}{\epsilon}{({J_{k} - J_{k - 1}})}h_{k}}}$. Algorithm 3 Episodic, model-free (OPRF)

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-B2 Episodic, model-free (OPRF )", "weight": 1.0} -->

While M-GAPS and DiffTune use differentiable models, it is also possible (and common in practice) to optimize policy parameters without knowing derivatives. The most widely-used model-free policy gradient methods use action-space randomness to estimate $G_{pg}$. This is problematic for us because our quadrotor controller runs at $500\ {Hz}$, far above the bandwidth of the physical system, so i.i.d. randomness at each step will be filtered away. Instead, we test a parameter-space policy gradient, which was shown to compete well against action-space methods when the parameter $\theta$ is low-dimensional.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-B2 Episodic, model-free (OPRF )", "weight": 1.0} -->

We again apply ideas from online optimization for the time-varying setting. In bandit online convex optimization with multiple queries allowed at each step, a two-point gradient method that queries at symmetrically perturbed parameters $\theta_{k} - h_{k}$, $\theta_{k} + h_{k}$, where $h_{k}$ is i.i.d. from a radially symmetric distribution, is essentially optimal. However, when episodes are imposed on a single-trajectory setting, it is not possible to evaluate the same episode cost twice. Instead, we apply *One-Point Residual Feedback* (OPRF, ), where past cost evaluations can reduce variance of single-point queries if costs change gradually. In simulations, OPRF improved substantially upon one-point methods without residual feedback. We instantiate it for our setting in Algorithm 3 ‣ III-B Episodic methods ‣ III Methods ‣ Fast Non-Episodic Adaptive Tuning of Robot Controllers with Online Policy Optimization").

<!-- chunk {"id": "body-0040", "role": "body", "section": "Quadrotor Dynamics and Policy Class", "weight": 1.0} -->

In this section we introduce our policy class and the quadrotor dynamics model used by M-GAPS and DiffTune. Our policy follows a standard nonlinear geometric control structure with simplifications to speed up derivative computation. We also propose reparameterizations of the state and policy to improve the optimization landscape.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-A Dynamics and Representation", "weight": 1.0} -->

Our dynamics model uses the Lie algebra ${\mathfrak{s}}{\mathfrak{o}}{}$ of the special orthogonal group ${SO}{}$ to represent 3D rotation state. Elements of ${\mathfrak{s}}{\mathfrak{o}}{}$ are skew-symmetric matrices interpretable as 3D angular velocities. We denote the natural isomorphism from ${\mathbb{R}}^{3}$ to ${\mathfrak{s}}{\mathfrak{o}}{}$ by $\left\lfloor \cdot \right\rfloor_{\times}$: if ${x,y} \in {\mathbb{R}}^{3}$, then ${\left\lfloor x \right\rfloor_{\times}y} = {x \times y}$, where $\times$ denotes the vector cross product.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-A Dynamics and Representation", "weight": 1.0} -->

The exponential map $\exp:{{{\mathfrak{s}}{\mathfrak{o}}{}}\mapsto{{SO}{}}}$ gives the rotation reached after turning at the given angular velocity for one unit of time. The logarithmic map $\log:{{{SO}{(n)}}\mapsto{{\mathfrak{s}}{\mathfrak{o}}{(n)}}}$ is a continuous function satisfying ${\exp\left( {\log R} \right)} = R$, ${\log\left( I_{n} \right)} = \mathbf{0}$. The coordinates of ${\mathfrak{s}}{\mathfrak{o}}{}$ provide a three-dimensional parameterization of ${SO}{}$, making the quadrotor state space $\mathcal{X}$ Euclidean instead of a manifold embedded in a higher-dimensional space.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-A Dynamics and Representation", "weight": 1.0} -->

This avoids the potential issue of the M-GAPS state $y_{t}$ departing the tangent space of $\mathcal{X}$ at $x_{t}$ due to compounded numerical errors. The drawback is multiple-covering: the exponential map is many-to-one. However, our experiments do not involve quadrotor flips and therefore will avoid this complication.^11^1 Representation of ${SO}{}$ by full matrices is the only way to avoid multiple covering, but applying M-GAPS on the resulting manifold state space requires differential geometric considerations left for future work.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-A Dynamics and Representation", "weight": 1.0} -->

The quadrotor state is defined by a position $p \in {\mathbb{R}}^{3}$ and velocity $v \in {\mathbb{R}}^{3}$ in the inertial frame, a logarithmic coordinate $r \in {{\mathfrak{s}}{\mathfrak{o}}{}}$ such that $\exp(r)$ rotates from the body frame to the inertial frame, and an angular velocity $\omega \in {{\mathfrak{s}}{\mathfrak{o}}{}}$ in the body frame. We consider an input space of $u = {(\xi,\tau)}$, where $\xi \geq 0$ is a mass-normalized thrust and $\tau = {\lbrack\tau_{r},\tau_{p},\tau_{y}\rbrack}^{\top} \in {\mathbb{R}}^{3}$ is the desired angular acceleration in the body frame.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-A Dynamics and Representation", "weight": 1.0} -->

We discretize the rotation dynamics with Lie group integration and the other states with forward Euler integration, yielding where $\delta > 0$ is the discretization time interval and $g$ is the gravitational constant. Our model is equivalent to having unit mass and identity moment of inertia. For simplicity, we assume that a lower-level thrust allocator can realize $u$ based on known mass, inertia, motor, and propeller characteristics.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-A Dynamics and Representation", "weight": 1.0} -->

By the quadrotor's differential flatness, one can compute a desired body-frame angular velocity $\omega_{t}^{d}$ from higher-order derivatives of $p^{d}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-B Policy class", "weight": 1.0} -->

Our policy class follows a widely-used structure for quadrotor trajectory-tracking controllers. An outer loop of position control calculates a desired mass-normalized thrust vector $z \in {\mathbb{R}}^{3}$, and an inner loop of geometric attitude control orients the quadrotor's body towards $z$. The outer-loop law is where $K_{i},K_{p},K_{v}$ are positive-definite diagonal gain matrices. The scalar thrust command $\xi$ is computed by projecting $z$ onto the body thrust axis: $\xi = {z^{\top}{\exp(r)}e_{z}}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-B Policy class", "weight": 1.0} -->

The inner loop begins by constructing a desired attitude $r_{d} \in {{\mathfrak{s}}{\mathfrak{o}}{}}$ as the shortest rotation that takes $e_{z}$ to $z$, given by or $r_{d} = \mathbf{0}$ when ${e_{z} \times z} = \mathbf{0}$, and $\left\| z \right\| > 0$ by assumption that the acceleration and error terms in are sufficiently small. Unlike many quadrotor controllers, ours has no concept of desired heading (yaw). The yaw portion of $r_{d}$ will be near zero when $z$ is near $e_{z}$. This simplifies the derivatives needed by M-GAPS considerably and is adequate for our experiments, but a desired yaw could be added.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-B Policy class", "weight": 1.0} -->

The desired angular acceleration $\tau$ is determined by where $K_{r},K_{\omega}$ are positive-definite diagonal gain matrices, ${{softclamp}{(x,y)}} = {y{\tanh\left({x/y} \right)}}$ is applied elementwise, and ${B_{xy},B_{z}} > 0$ are user-defined upper bounds. The $softclamp$ is critical for high-gain attitude control using this cascaded structure. Without it, large attitude errors may lead to commands that cannot be realized without setting some of the motor thrusts to zero, causing instability and altitude loss.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-C Contractiveness", "weight": 1.0} -->

A geometric controller similar to ours was shown to be exponentially stabilizing when the attitude error is less than 90 degrees. In Euclidean state spaces, exponential stability for tracking controllers is generally sufficient for contractiveness in the sense required by M-GAPS. However, the analysis of considers exponential stability directly on the ${SO}{}$ manifold, whereas we use the logarithmic parameterization of rotations to avoid a manifold state space. Deriving contractiveness of $r$ from exponential stability of $\exp(r)$ requires differential geometry arguments beyond the scope of this work. Also, the analysis of does not account for actuation limits, which we found to be critical and addressed by the $softclamp$ in our design. Still, we conjecture that with suitable assumptions on the initial error and disturbances, our controller and state parameterization is contractive.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-D Logarithmic Policy Reparameterization", "weight": 1.0} -->

To improve the optimization landscape conditioning, we use a logarithmic reparameterization of the feedback gains. In our policy class, $K_{i,p,v,r,\omega}$ are nonnegative diagonal matrices whose entries can range over several orders of magnitude. In the expert-tuned baseline $\theta^{m}$ discussed in §V, the largest gain is $\approx 1000$, while the smallest is $\approx 1$. Further, because the elements of $\theta$ have highly distinct physical meanings, the sensitivity of the surrogate cost $F_{t}$ is nonuniform: from empirical observations, we have that $\left| {\nabla F_{t}} \right|$ with respect to each entry $k$ is roughly proportional to $1/|k|$. To handle this simply, we let $\theta$ determine the *logarithms* of the gains.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-D Logarithmic Policy Reparameterization", "weight": 1.0} -->

Due to the geometric symmetries of the quadrotor, we use equal gains for the two horizontal axes, e.g. $K_{r} = {{diag}{(k_{r}^{xy},k_{r}^{xy},k_{r}^{z})}}$. This yields the "raw" parameter and the reparameterization $\theta = {\log(\vartheta)}$, which we optimize with M-GAPS, DiffTune, and OPRF. We fix the cost function for all experiments and all timesteps $t$ as This mainly penalizes position tracking error, with other terms acting to regularize against high control effort. Regularization constants were chosen empirically to be as small as possible while preventing any tendency towards attitude oscillations.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Quadrotor Experiments", "weight": 1.0} -->

Our quadrotor is a Bitcraze Crazyflie 2.0 with the manufacturer's thrust upgrade bundle and a larger battery. For the analytic derivatives needed by M-GAPS and DiffTune (5 ‣ III Methods ‣ Fast Non-Episodic Adaptive Tuning of Robot Controllers with Online Policy Optimization")-6 ‣ III Methods ‣ Fast Non-Episodic Adaptive Tuning of Robot Controllers with Online Policy Optimization")), we use the SymForce package, which includes symbolic differentiation of Lie algebraic operations and generates C++ code suitable for embedded systems. All algorithms run at $500\ {Hz}$ on the Crazyflie 2.0's $168\ {MHz}$ onboard microcontroller with $192\ {kB}$ memory. The controlling PC runs the Crazyswarm package. As a baseline for comparison, we have access to expert controller parameters $\theta^{m}$ manually tuned over several days of effort.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Quadrotor Experiments", "weight": 1.0} -->

We start with a trajectory tracking experiment where the disturbances are small (Subsections A-B), and test how quickly each policy optimization algorithm approaches the near-optimal behavior of $\theta^{m}$ when initialized with a suboptimal parameter. Then, we experiment with larger disturbances from time-varying wind or a heavy payload (Subsection C), which $\theta^{m}$ is not tuned to handle. If M-GAPS outperforms $\theta^{m}$ in such settings, it suggests that no fixed parameter is near-optimal in all circumstances, motivating online policy optimization. When applicable, all figures use shorthand names for optimizers and fixed parameter values given in Table I. θt = θm∀t. θm = Manually tuned, near-optimal. θt = θm − log 2∀t. Stabilizing but far from optimal.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Quadrotor Experiments", "weight": 1.0} -->

Algorithm 2 with hindsight best episode length.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Quadrotor Experiments", "weight": 1.0} -->

Algorithm 2 with hindsight worst episode length.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Quadrotor Experiments", "weight": 1.0} -->

Algorithm 3 using DiffTune⋆’s episode length.

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-A Detuned initialization", "weight": 1.0} -->

We simulate the process of controller tuning with a new robot or policy class by initializing each algorithm with the "detuned" parameter $\theta_{0} = {\theta^{m} - {\log 2}}$, which corresponds with halving the feedback gains due to our logarithmic policy reparameterization. This gives a policy that stabilizes near hover, but is less suited for aggressive trajectories. We deploy M-GAPS, DiffTune, and OPRF in an aggressive figure-8 trajectory moving in a diagonal plane, such that high thrust and roll/pitch torques are needed.

<!-- chunk {"id": "body-0059", "role": "body", "section": "V-A Detuned initialization", "weight": 1.0} -->

The trajectories for the expert $\theta^{m}$, detuned $\theta_{0}$, and each of the optimization algorithms are shown Figure 1. To illustrate the impact of episode length, DiffTune is shown with two different episode lengths, with *DiffTune^⋆^* indicating the best-performing length in hindsight, and *DiffTune* the worst (details in §V-B). Color corresponds to time. The expert and detuned trajectories are nearly unchanging, as expected. In contrast, all algorithms significantly alter the trajectory. M-GAPS is initially near *detune*, but after 2-3 laps (8-12 sec) is near *expert*. DiffTune with optimal episode length does not improve on the first lap but jumps near *expert* after its first update, while the improvement is much slower with a suboptimal episode length. OPRF improves some, but is much slower than the model-based methods.

<!-- chunk {"id": "body-0060", "role": "body", "section": "V-A Detuned initialization", "weight": 1.0} -->

The improvement is shown quantitatively in Figure 2. We are interested in the policy regret (1 ‣ III Methods ‣ Fast Non-Episodic Adaptive Tuning of Robot Controllers with Online Policy Optimization")), but since the true clairvoyant optimal $\theta$ is unknown, we use the manually-tuned $\theta^{m}$ as a surrogate, and plot the cumulative cost difference from $\theta^{m}$ for each method, henceforth called *quasi-regret*. This scenario is disturbance-free, so $\theta^{m}$ is near-optimal. We see M-GAPS quickly reduces cost and converges to constant quasi-regret against $\theta^{m}$. DiffTune with optimal episode length converges to a larger constant quasi-regret. However, with a bad episode length its quasi-regret is significantly degraded and still growing as the experiment ends. The model-free OPRF has substantially higher quasi-regret.

<!-- chunk {"id": "body-0061", "role": "body", "section": "V-A Detuned initialization", "weight": 1.0} -->

The evolution of parameters for each algorithm are shown in Figure 3. The model-free OPRF produces noisy parameter changes due to its randomized queries and high-variance gradient estimate. The model-based episodic gradient of DiffTune behaves more similarly to M-GAPS, but illustrates the additional drawback of large steps in the policy parameters. The large steps caused jitter in the quadrotor's attitude, which was visible in person but is not clear in the position trajectory or quasi-regret plots.

<!-- chunk {"id": "body-0062", "role": "body", "section": "V-B DiffTune sensitivity to episode length", "weight": 1.0} -->

In Figure 4, we expand the comparison of M-GAPS and DiffTune. Total costs in the detuned initialization scenario are shown for M-GAPS and DiffTune with various episode lengths. The figure-8 trajectory lasts $4\ \sec$ and is symmetric. Therefore, with our $500\ {Hz}$ controller, episodes of $1000$ and $2000$ are especially well-aligned, as the data confirms. In real-world applications that are not periodic, the optimal episode length may not be so obvious, and might also change over time. Episode length becomes another hyperparameter to empirically tune. In contrast, learning rate is the only hyperparameter of M-GAPS.

<!-- chunk {"id": "body-0063", "role": "body", "section": "V-C1 Time-varying wind", "weight": 1.0} -->

To study short-term adaptivity, we create a periodic wind disturbance with three household box fans side-by-side. To simulate the powerful wind disturbances of outdoor flight, we attach a cardboard panel to the quadrotor that presents a large "sail" to the wind, magnifying its effect. We fly a linear back-and-forth pattern in front of the fan array, with each "lap" taking $4\ \sec$. The fan power is toggled every 3 laps ($12\ \sec$). Tracking error is shown in Figure 5. We see that M-GAPS substantially improves tracking accuracy in both fan-on (shaded) and fan-off phases. The evolution of each parameter is plotted in Figure 6. Several parameters show significant transient responses when the phase switches. In particular, $k_{p}^{xy}$ approaches oscillation. This confirms that M-GAPS adapts quickly to scenario changes on the scale of ten seconds. The dynamics model used by M-GAPS is unchanged from nominal, demonstrating robustness against model error.

<!-- chunk {"id": "body-0064", "role": "body", "section": "V-C2 Heavy payload", "weight": 1.0} -->

To further study robustness against modeling error, we attach a heavy weight to the quadrotor while leaving the dynamics model used by M-GAPS unchanged from the nominal mass. Our quadrotor's mass is $39\ g$. We attach a $23\ g$ steel weight near its center, increasing mass by $60\ \%$ and acting as a large, near-constant disturbance force. This is near the quadrotor's thrust limit, so we fly in a horizontally-oriented circle that does not require excess thrust. The parameter $\theta^{m}$ was not tuned to handle such large disturbances. In Figure 7, we observe that M-GAPS is able to substantially reduce the tracking error compared to $\theta^{m}$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "V-C3 Parameter comparison between disturbance types", "weight": 1.0} -->

In Figure 8, we compare the parameter evolution for the time-varying-wind and heavy-payload scenarios. We observe large differences. In particular, $k_{p}^{z}$ has the largest change in the heavy-payload scenario, but changes minimally in the wind scenario. The weight acts in the $z$-axis while the fan acts in the $y$-axis. This confirms that M-GAPS is adapting to the specific disturbances experienced in each scenario, rather than (or in addition to) the intrinsic properties of the quadrotor.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Ackermann-Steered Car Experiment", "weight": 1.0} -->

To evaluate the versatility of M-GAPS with respect to robot type, we deploy it on an Ackermann-steered 1:6-scale remote-control car (Traxxas X-Maxx) with onboard visual-inertial localization, driving in a circle on grass and concrete. Details of the state representation, dynamics model, policy class, and cost function are given in Section -A. We use M-GAPS to tune the controller after finding a suboptimal stabilizing controller with limited manual effort. M-GAPS optimizes squared tracking error with small angular velocity error and steering angle regularization terms. Results are shown in Figure 9. M-GAPS reduces the tracking error by a factor of around $5$ within $10\ \sec$ of being enabled -- less than one full circle period. This shows that 1) the positive results of M-GAPS are not restricted to quadrotors, and 2) M-GAPS can be useful for automatic tuning on new hardware or a new controller design, even if online adaptivity is not the main goal.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We experimentally evaluated algorithms that apply the principle of online gradient descent to the online policy optimization problem for nonlinear robot controllers. For tuning a geometric quadrotor controller for aggressive flight from a suboptimal initialization, the non-episodic model-based M-GAPS performed best, finding a near-optimal policy in about $15\ \sec$. The model-based episodic DiffTune performed nearly as well when its episode length was ideal, but degraded with other episode lengths. The model-free episodic OPRF further lagged the model-based methods. We also validated M-GAPS in a similar bad-initialization experiment on a small off-road car, showing versatility with respect to robot platforms.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Conclusion", "weight": 1.5} -->

To further evaluate M-GAPS, we compared it to the expert-tuned parameter $\theta^{m}$ under disturbances from a heavy weight and periodic wind. In both scenarios, M-GAPS improved substantially from $\theta^{m}$ while finding very different optimized parameters. This shows that M-GAPS adapts to the specific problem instance, and can improve performance even when the dynamics model is not perfect. More broadly, our results show the benefit of online adaptivity in general: by allowing the core controller parameters to change moment-to-moment in response to current real-world conditions, we achieve strong performance in a wide range of scenarios.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Limitations", "weight": 1.5} -->

The requirement of a differentiable dynamics may limit the applicability of M-GAPS and DiffTune to systems with discontinuities, such as walking robots. Unstable behavior near discontinuities can degrade gradient-based optimization, even when the discontinuities form a set of measure zero. Further testing and development is needed on such systems.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Limitations", "weight": 1.5} -->

The contractiveness required for the local regret guarantee of M-GAPS can be difficult to verify, and does not rule out the possibility of bad local minima. Similar to other applications of gradient-based nonconvex optimization, one must do empirical validation (like this work) before deploying M-GAPS in complex real-world robotic systems.
