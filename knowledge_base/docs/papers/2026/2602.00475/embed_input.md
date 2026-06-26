<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Parallel Stochastic Gradient-Based Planning for World Models

Topics include World models, Planning, Gradient-based planning, Stochastic optimization, Collocation, Visual control, Long-horizon planning, Differentiable models.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces GRASP, a planner that optimizes virtual states and actions inside differentiable visual world models using stochastic, parallelizable gradient-based search. By relaxing dynamics constraints and altering the gradient structure, the method avoids fragile backpropagation through high-dimensional video models while improving long-horizon planning relative to CEM and vanilla gradient descent.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

World models simulate environment dynamics from raw sensory inputs like video. However, using them for planning can be challenging due to the vast and unstructured search space. We propose a robust and highly parallelizable planner that leverages the differentiability of the learned world model for efficient optimization, solving long-horizon control tasks from visual input. Our method treats states as optimization variables ("virtual states") with soft dynamics constraints, enabling parallel computation and easier optimization. To facilitate exploration and avoid local optima, we introduce stochasticity into the states. To mitigate sensitive gradients through high-dimensional vision-based world models, we modify the gradient structure to descend towards valid plans while only requiring action-input gradients. Our planner, which we call GRASP (Gradient RelAxed Stochastic Planner), can be viewed as a stochastic version of a non-condensed or collocation-based optimal controller. We provide theoretical justification and experiments on video-based world models, where our resulting planner outperforms existing planning algorithms like the cross-entropy method (CEM) and vanilla gradient-based optimization (GD) on long-horizon experiments, both in success rate and time to convergence.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Intelligent agents carry a small-scale model of external reality which allows them to simulate actions, reason about their consequences, and choose the ones that lead to the best outcome. Attempts to build such models date back to control theory, and in recent years researchers have made progress in building world models using deep neural networks trained directly from the raw sensory input (e.g., vision). For example, recent world models have shown success modeling computer games (valevski2024diffusion), navigating real-world environments (bar2025navigation; genie3), and robot arm motion commands (goswami2025world). World models have numerous impactful applications from simulating complex medical procedures (koju2025surgical) to testing robots in visually realistic environments (guo2025ctrl).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Current planning algorithms used with world models often rely on 0^th^-order optimization methods such as the Cross-Entropy Method (CEM rubinstein2004cross) or in general *shooting methods* which plan by iteratively rolling out trajectories and choosing actions from the optimal rollout (bock1984multiple; piovesan2009randomized). These approaches are simple and robust, but their performance degrades with longer planning horizons and higher action dimensionality (bharadhwaj2020model), motivating the use of gradient information when differentiable world models are available.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Gradient-based planners exploit the differentiability of learned world models to directly optimize action sequences, enabling more sample-efficient planning and finer-grained improvement than zero-order methods. However, there are two main challenges to this optimization approach: local minima (jyothir2023gradient) and instability due to differentiating through the full rollout, akin to backpropagation through time (werbos2002backpropagation). While prior methods have formulated the optimization for better conditioning (e.g., multiple shooting and direct collocation (von1993numerical)), these techniques are typically developed for known dynamical systems and do not scale as well to deep neural dynamics (often in latent spaces) with brittle or poorly calibrated Jacobians.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we introduce a novel gradient-based planning method for learned world models that decouples temporal dynamics into parallel optimized states (rather than serial rollouts) while remaining robust at long horizons and in high-dimensional state spaces. Rather than planning exclusively through a deep, sequential rollout of the dynamics model, our approach optimizes over *lifted intermediate states* that are treated as independent optimization variables. Our approach makes two fundamental additions that help solve issues for gradient-based planning in higher dimensions: gradient sensitivity and local minima.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Firstly, a fundamental difficulty arises in the setting of vision-based world models. In high-dimensional learned state spaces, gradients with respect to state inputs can be brittle or adversarial, allowing the optimizer to exploit sensitive Jacobian structure rather than discovering physically meaningful transitions. To mitigate this issue, our planner deliberately stops gradients through the state inputs of the world model, while retaining gradients with respect to actions, which we find behave more reasonably. This alone would promote trajectories near the starting state, but with a dense one-step goal loss over the full trajectory, converged trajectories for these noisy iterations tend towards the goal.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Secondly, to address the remaining non-convexity of the lifted state approach, our planner incorporates Langevin-style stochastic updates on the lifted state variables, explicitly injecting noise during optimization to promote exploration of the state space and facilitate escape from unfavorable basins. This stochastic relaxation allows the planner to search over diverse intermediate trajectories while still favoring solutions that approximately satisfy the learned dynamics. Finally, we intermittently apply a small GD step to fine-tune stochastically optimized trajectories towards fully-optimized paths.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Together, these components yield a practical gradient-based planner for learned visual dynamics that remains stable at long horizons while avoiding the failure modes commonly encountered when backpropagating through deep world-model rollouts. We call our planner GRASP (Gradient RelAxed Stochastic Planner) to emphasize its primary components: using gradient information, relaxing the dynamics constraints, and stochastic optimization for exploration. In various settings, we achieve up to +10% success rate at less than half the compute time cost. We also provide a theoretical model for our planner to further illustrate its role. We demonstrate our planner on visual world models trained on problems in D4RL (fu2020d4rl) and the DeepMind control suite (tassa2018deepmind).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Our main object of interest is a learned world model $F_{\theta}:\mathcal{S}\times\mathcal{A}\rightarrow\mathcal{S}$ that predicts the next state given the current state and action. For visual domains, states are typically represented in a learned latent space to handle high-dimensional observations. Here we assume $\mathcal{A}=\mathbb{R}^{k}$ is a continuous Euclidean action space.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

We consider the problem of fixed-goal path planning: finding an action sequence $\mathbf{a}=(a_{0},a_{1},\ldots,a_{T-1})$ that, with respect to the dynamics of the world model $F_{\theta}$ and a given initial state $s_{0}\in\mathcal{S}$, reaches a set goal state $g\in\mathcal{S}$: where the terminal state $s_{T}$ is generated recursively through the update rule $s_{t+1}=F_{\theta}(s_{t},a_{t})$: We can sufficiently compute $\mathbf{a}^{*}$ by solving the following optimization problem: Optimizing Eq. directly is challenging due to two main problems.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

First, it requires $T$ applications of $F_{\theta}$ (see Eq. 2), which is computationally expensive and difficult to optimize due to the poor conditioning arising from repeated applications of $F_{\theta}$ (see Appendix 8.1 for details). Second, it is susceptible to local minima and a jagged loss landscape---see Figure 1. Due to these reasons, existing planners are based on zero-order optimization algorithms like CEM and MPPI (williams2016aggressive) which are highly stochastic and do not require gradient computation.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

In what follows, we propose a gradient-based planner which alleviates these difficulties, while also using the differentiability of the model $F_{\theta}$. In Section 3, we lift the optimization problem by also optimizing over states, which leads to faster convergence and better conditioning. In Section 3.2, we introduce stochasticity, which helps escape local minima.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Decoupling dynamics for gradient-based planning", "weight": 1.0} -->

We consider planning with a world model $F_{\theta}$ and horizon $T$. Given an initial state $s_{0}\in\mathcal{S}$ and goal state $g\in\mathcal{S}$, we optimize an action sequence $\mathbf{a}=(a_{0},\dots,a_{T-1})$ such that the rolled-out state $s_{T}(\mathbf{a})$ is as close to $g$ as possible. A standard approach defines a trajectory by rolling out the model, but backpropagating through a deep composition of $F_{\theta}$ can be unstable and ill-conditioned. Following prior work on lifted planning (tamimi2009nonlinear; rybkin2021model), we introduce auxiliary states $\mathbf{z}=(z_{1},\dots,z_{T})$ and enforce dynamics consistency through a penalty function.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Parallelized planning", "weight": 1.0} -->

We first want to decouple the states from the explicit rollout outputs. Writing Eq. in terms of each intermediate dynamics condition, we get the following: The minimization in Eq. is equivalent to Eq. in that they share global minimizers.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Parallelized planning", "weight": 1.0} -->

Immediately, this gives a great benefit in that *all world model evaluations are parallel*; there is no need to do serial rollouts like what is required in Eq.. There are however two main issues with optimizing this loss directly: *Local minima*. When optimizing with respect to states, the states might be stuck in an unphysical region; for example, Figure 7 shows a case where states go straight through a barrier. To address this, we propose to use Langevin state updates which promote exploration (see Section 3.2).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Parallelized planning", "weight": 1.0} -->

*World model sensitivity for high-dimensional states.* When optimizing $s$ directly over a higher dimensional space (e.g. vision-based), we observe that the Jacobian $J_{s}F_{\theta}(s,a)$ does not necessarily have any nice low-dimensional or convex structure; in practice, the world model can be easily steered toward outputting any desired output state, as depicted in Figure 3. We address this in Section 3.3 with a reshaping of the descent directions.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Parallelized planning", "weight": 1.0} -->

We now describe our approach to address these two fundamental problems with lifted-states approaches to planning.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Exploration via Langevin state updates", "weight": 1.0} -->

The lifted optimization in Eq. is still non-convex and can get trapped in poor local minima. In practice, we frequently observe that deterministic joint updates in $(\mathbf{a},\mathbf{s})$ converge to "bad" stationary points where the intermediate variables settle into an unfavorable basin; for example, a linear route that ignores barriers or walls like in Figure 7. To circumvent this, we inject stochasticity directly into the state iterates, yielding a Langevin-style update that encourages exploration in the lifted state space.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Langevin dynamics on state iterates", "weight": 1.0} -->

Consider the optimization induced by Eq.. A standard way to escape spurious basins is to replace deterministic gradient descent on $\mathbf{s}$ with overdamped Langevin dynamics (gelfand1991recursive), whose Euler discretization takes the following form: where $\xi_{t}^{k}\sim\mathcal{N}(0,I)$. That is, each optimization step performs a gradient descent update on the intermediate states, followed by an isotropic Gaussian perturbation. Intuitively, the noise allows the iterates to "hop" between nearby basins of the lifted loss landscape.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Noise on states vs. actions", "weight": 1.0} -->

By only noising the states, we can still condition on more dynamically feasible trajectories, while still allowing exploration over a wider distribution. Intuitively, planning problems often have a single (or small number of) intermediate states to find for the solution, and being able to noise directly over states rather than actions allows us to find these intermediate states faster. See Appendix 8.3 for a characterization of the sampled distribution.

<!-- chunk {"id": "body-0023", "role": "body", "section": "A note on adversarial robustness of state gradients", "weight": 1.0} -->

In practice, $F_{\theta}$ is learned and can have brittle local geometry. When optimizing Eq. by gradient descent in both $\mathbf{a}$ and $\mathbf{s}$, we observed empirically that gradients with respect to the state inputs, $\nabla_{s}F_{\theta}(s,a)$, can be exploited: for any local goal-reaching objective of the following form: instead of the optimizer learning to find an $s$ on-manifold such that applying the action $a$ leads to end state $y$, the optimizer can find a nearby ambient $s+\delta$, $\|\delta\|_{2}\ll 1$ such that the loss is practically minimized: $y\approx F_{\theta}(s+\delta,a)$, *regardless of the starting state $s$*.

<!-- chunk {"id": "body-0024", "role": "body", "section": "A note on adversarial robustness of state gradients", "weight": 1.0} -->

This is analogous to the adversarial robustness issue of image classifiers (szegedy2013intriguing; shamir2021dimpled): high-dimensional input spaces for trained neural networks can have high Lipschitz constants, hindering optimization performance.

<!-- chunk {"id": "body-0025", "role": "body", "section": "A note on adversarial robustness of state gradients", "weight": 1.0} -->

Unfortunately, any loss function over $\mathbf{s}$ and $\mathbf{a}$ whose minimizers are feasible dynamics must depend on the state gradient $\nabla_{s}F$ in a meaningful way. We provide the informal theorem here, with formalization and proof in Appendix 8.4.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Grad-cut dynamics loss", "weight": 1.0} -->

We begin by applying a gradient stop to the state inputs in the dynamics loss: This objective is differentiable with respect to $\mathbf{a}$ and the *next* states $s_{t+1}$, but does not backpropagate through $s_{t}$ via $F_{\theta}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Dense goal shaping on one-step predictions", "weight": 1.0} -->

While Eq. improves robustness, it introduces a new degeneracy: paths gravitate towards the current rollout, regardless of proximity to the goal. To provide a task-aligned signal at every time step without state-input gradients, we add a goal loss on the one-step predictions: This encourages each predicted next state to move toward the goal, supplying gradient information to every action $a_{t}$ while maintaining the grad-cut on $s_{t}$. This is depicted visually in Figure 2, and theoretically in Appendix 8.4. Crucially, due to the stop-gradient $\bar{s}_{t}$, gradients through $F_{\theta}(\bar{s}_{t},a_{t})$ flow only with respect to $a_{t}$ (and not $s_{t}$), which prevents the optimizer from exploiting adversarial state-input directions.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Dense goal shaping on one-step predictions", "weight": 1.0} -->

Resulting noisy dynamics. The final resulting dynamics, after explicitly writing out $\nabla_{a}\mathcal{L}$, are as follows: where $\xi_{t}^{k}\sim\mathcal{N}(0,I)$. Importantly, while the action dynamics still follow a gradient flow, the states do not follow a true gradient vector field, and thus *the resulting dynamics are not Langevin.* What results are still noisy dynamics that bias towards valid goal-oriented trajectories, but whose efficiency will require an extra synchronization step as described in the following section.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Full-rollout synchronization", "weight": 1.0} -->

The no-state-gradient updates are designed to be robust to brittle state-input Jacobians of the learned world model. However, the stochastic optimization in Eq. still needs a method of strict descent towards true minima. In practice, we found it beneficial to periodically "sync" the plan by briefly running standard full-gradient planning on the original rollout objective.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Full-gradient rollout step", "weight": 1.0} -->

Every $K_{\mathrm{sync}}$ iterations, we perform $J_{\mathrm{sync}}$ steps of gradient descent on the original planning loss where $s_{T}(\mathbf{a},s_{0})$ is computed by sequentially rolling out the world model During this synchronization phase we update only the actions, using full backpropagation through the $T$-step rollout. By keeping these GD steps small relative to the stochastic dynamics of Eq., we benefit from the smoothed loss landscape in Figure 1c for wider exploration, and the sharp but brittle landscape in Figure 1b for refinement.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Results", "weight": 1.0} -->

We evaluate our proposed planner GRASP across two complementary classes of environments designed to test (i) nonconvex long-horizon planning with obstacles and (ii) data-driven visual control under learned dynamics. Concretely, these experiments aim to answer three questions: Can the proposed planner overcome the greedy local minima that often trap shooting methods?

<!-- chunk {"id": "body-0032", "role": "body", "section": "Results", "weight": 1.0} -->

Does the method remain robust as the planning horizon increases?

<!-- chunk {"id": "body-0033", "role": "body", "section": "Results", "weight": 1.0} -->

Does the proposed planner converge to plans faster than rollout-based planners?

<!-- chunk {"id": "body-0034", "role": "body", "section": "Results", "weight": 1.0} -->

We provide self-ablations in Table 2, demonstrating the value of various components of our planner: using the state gradient detaching, the GD sync steps, and the level of the noise.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Baselines", "weight": 1.0} -->

We compare against three commonly used planners. CEM optimizes action sequences by iteratively sampling candidate trajectories, selecting elites, and refitting a sampling distribution. GD directly optimizes the action sequence by backpropagating through the dynamics model. LatCo (rybkin2021model) optimizes in a lifted latent/state-space by jointly adjusting intermediate latent variables and actions. This setting is different than the original LatCo method, which was originally applied in a model-based RL environment, but it still provides an important baseline for performance if we were to purely focus on direct optimization of Eq..

<!-- chunk {"id": "body-0036", "role": "body", "section": "Baselines", "weight": 1.0} -->

For all methods, we sweep over hyperparameters and report results using the best-performing setting for each environment and horizon. For our planner, we initialize the states $\{s_{t}\}_{t=0}^{T}$ as noised around the linear interpolation between $s_{0}$ and $g$: $s_{t}=\frac{t}{T}g+(1-\frac{t}{T})s_{0}+z$, $z\sim\mathcal{N}(0,\epsilon I)$, and actions initialized at zeros: $a_{t}=0$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Environments and evaluation protocol", "weight": 1.0} -->

We evaluate planning on three visual control environments with learned dynamics: *PointMaze*, *Wall-Single*, and *Push-T*. World models are trained using the DINO-wm framework (zhou2024dino), following the original paper's setup, where the world model $F_{\theta}(s,a)$ takes 5 actions and predicts 5 steps ahead; that is, if $\text{dim}(\mathcal{A})=2$, then $F_{\theta}$ takes actions as vectors of stacked actions $\mathbf{a}\in\mathbb{R}^{10}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Environments and evaluation protocol", "weight": 1.0} -->

All reported metrics measure task success under the learned world model. Success is defined as reaching the goal region within the planning horizon.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Long-term planning and horizon scaling", "weight": 1.0} -->

We evaluate planners in the long-horizon regime, where our parallelized stochastic planner is more intended; greedy local minima and optimization instability become the dominant challenges.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Long-term planning and horizon scaling", "weight": 1.0} -->

GRASP remains reliable as the planning horizon increases: it solves more tasks and finishes a majority of its successful trials faster, showing stronger robustness to long horizons than the baselines as shown in Table 1. Beyond the median completion times, we provide further illustration of the solving speed of our planner in Figure 5, showing further that most of its plans converge at an earlier time. At the longer horizons for Push-T, where it is more important for the planner to explore non-greedy optima, GRASP finds more success than the baselines and is able to find the needed non-greedy trajectories, as visualized in Figure 6.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Short-term planning", "weight": 1.0} -->

We also evaluate short-horizon planning, to demonstrate that our planner can match performance on shorter, easier tasks. Table 3 reports success rates across environments for horizons ranging from $H=10$ to $H=30$, while Table 4 reports median wall-clock planning times.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Short-term planning", "weight": 1.0} -->

Across all environments and short horizons, the proposed planner achieves success rates comparable to the baselines. Alongside similar success rates, our proposed planner exhibits consistently low planning times. As shown in Table 4, it is among the fastest methods across all environments and horizons, often significantly faster than sampling-based approaches and competitive with gradient-based optimization, sacrificing some speed for a higher success rate. These results indicate that even in relatively short and easy planning regimes, our planner remains competitive with the baselines.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Short-term planning", "weight": 1.0} -->

Overall, these results demonstrate that GRASP consistently matches strong baselines in short-term planning, while outperforming them in long-horizon settings by avoiding greedy failures and converging more quickly in wall-clock time.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Limitations and future work", "weight": 1.5} -->

Although the proposed planner shows clear advantages in long-horizon settings, its benefits are more limited at short horizons. As demonstrated in our experiments, for small planning horizons the planner typically achieves success rates and completion times that are comparable to strong baselines such as CEM and gradient-based optimization, rather than strictly outperforming them. This suggests that the primary gains of the method arise in regimes where long-horizon reasoning and non-greedy planning are essential, rather than in short-horizon settings where simpler methods already perform well.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Limitations and future work", "weight": 1.5} -->

Hybrid planners (that combine iterations of a rollout-based planner like CEM and a gradient-based planner like GD) have been implemented to get the "best of both worlds" from the two approaches (huang2021cem), and there are many ways to "hybridize" our planner as well. We leave exploration of such methods for future work.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Limitations and future work", "weight": 1.5} -->

Several components of the planner are designed to mitigate the unreliability of state gradients in learned world models. While effective, these modifications introduce additional structure and hyperparameters that would ideally be unnecessary. If state representations induced by the world model were smoother or more geometrically well-behaved in the state space, many of these stabilization mechanisms could be removed, potentially leading to further speed improvements. Promising directions toward this goal include improved representation learning through adversarial training, diffusion-based world models, or other techniques that explicitly regularize the geometry of the learned state space.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusion", "weight": 1.5} -->

World models provide a powerful framework for planning in complex environments, but existing approaches struggle with long horizons, high-dimensional actions, and serial computation. We propose GRASP, a new gradient-based planning algorithm with two key contributions: (a) a lifted planner that optimizes actions together with "virtual states" in a time-parallel manner, yielding more stable and scalable optimization while allowing direct control over exploration via stochastic state updates, and (b) an action-gradient-only planning variant for learned visual world models that avoids brittle state-input gradients while still exploiting differentiability with respect to actions. Experiments on visual world-model benchmarks show that our approach remains robust as horizons grow and finds non-greedy solutions at a faster rate than commonly used planners such as CEM or vanilla GD.
