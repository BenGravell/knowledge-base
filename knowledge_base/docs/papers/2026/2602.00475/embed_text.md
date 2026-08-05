<!-- arxiv-full-text:v1 {"arxiv_id": "2602.00475", "source": "arxiv-html"} -->

## Introduction

Figure 1: Difficulty of the planning problem. Subfigure (a) shows the distance to the goal in L2 norm throughout a successful trajectory. This illustrates the difficulty of planning optimization away from a minimizer: successful trajectories often have to first move away from the goal to successfully plan towards it later, resulting in greedy strategies failing. Subfigures (b)-(c) depict the loss landscape at convergence of standard rollout-based planners vs. our planner. The example given is in the Push-T environment at horizon length 50. The axes plotted over are with respect to two random, orthogonal, unit-norm directions in the full action space ℝ50 × 2. Our planner loss is taken as in Eq., and for GD the loss is taken as in Eq..

Intelligent agents carry a small-scale model of external reality which allows them to simulate actions, reason about their consequences, and choose the ones that lead to the best outcome. Attempts to build such models date back to control theory, and in recent years researchers have made progress in building world models using deep neural networks trained directly from the raw sensory input (e.g., vision). For example, recent world models have shown success modeling computer games (valevski2024diffusion), navigating real-world environments (bar2025navigation; genie3), and robot arm motion commands (goswami2025world). World models have numerous impactful applications from simulating complex medical procedures (koju2025surgical) to testing robots in visually realistic environments (guo2025ctrl).

Current planning algorithms used with world models often rely on 0^th^-order optimization methods such as the Cross-Entropy Method (CEM rubinstein2004cross) or in general *shooting methods* which plan by iteratively rolling out trajectories and choosing actions from the optimal rollout (bock1984multiple; piovesan2009randomized). These approaches are simple and robust, but their performance degrades with longer planning horizons and higher action dimensionality (bharadhwaj2020model), motivating the use of gradient information when differentiable world models are available.

Gradient-based planners exploit the differentiability of learned world models to directly optimize action sequences, enabling more sample-efficient planning and finer-grained improvement than zero-order methods. However, there are two main challenges to this optimization approach: local minima (jyothir2023gradient) and instability due to differentiating through the full rollout, akin to backpropagation through time (werbos2002backpropagation). While prior methods have formulated the optimization for better conditioning (e.g., multiple shooting and direct collocation (von1993numerical)), these techniques are typically developed for known dynamical systems and do not scale as well to deep neural dynamics (often in latent spaces) with brittle or poorly calibrated Jacobians.

In this work, we introduce a novel gradient-based planning method for learned world models that decouples temporal dynamics into parallel optimized states (rather than serial rollouts) while remaining robust at long horizons and in high-dimensional state spaces. Rather than planning exclusively through a deep, sequential rollout of the dynamics model, our approach optimizes over *lifted intermediate states* that are treated as independent optimization variables. Our approach makes two fundamental additions that help solve issues for gradient-based planning in higher dimensions: gradient sensitivity and local minima.

Firstly, a fundamental difficulty arises in the setting of vision-based world models. In high-dimensional learned state spaces, gradients with respect to state inputs can be brittle or adversarial, allowing the optimizer to exploit sensitive Jacobian structure rather than discovering physically meaningful transitions. To mitigate this issue, our planner deliberately stops gradients through the state inputs of the world model, while retaining gradients with respect to actions, which we find behave more reasonably. This alone would promote trajectories near the starting state, but with a dense one-step goal loss over the full trajectory, converged trajectories for these noisy iterations tend towards the goal.

Secondly, to address the remaining non-convexity of the lifted state approach, our planner incorporates Langevin-style stochastic updates on the lifted state variables, explicitly injecting noise during optimization to promote exploration of the state space and facilitate escape from unfavorable basins. This stochastic relaxation allows the planner to search over diverse intermediate trajectories while still favoring solutions that approximately satisfy the learned dynamics. Finally, we intermittently apply a small GD step to fine-tune stochastically optimized trajectories towards fully-optimized paths.

Together, these components yield a practical gradient-based planner for learned visual dynamics that remains stable at long horizons while avoiding the failure modes commonly encountered when backpropagating through deep world-model rollouts. We call our planner GRASP (Gradient RelAxed Stochastic Planner) to emphasize its primary components: using gradient information, relaxing the dynamics constraints, and stochastic optimization for exploration. In various settings, we achieve up to +10% success rate at less than half the compute time cost. We also provide a theoretical model for our planner to further illustrate its role. We demonstrate our planner on visual world models trained on problems in D4RL (fu2020d4rl) and the DeepMind control suite (tassa2018deepmind).

## Problem formulation

Figure 2: Graphical depiction of (a) a standard serial-based setup for optimization-based planning, where states are rolled out using the actions and the loss is evaluated on the goal state, (b) our setup, which parallelizes the world model evaluations by optimizing “virtual states” directly and only supervising pairwise dynamics satisfaction. The crossed lines and skipped connections for our method’s depiction (b) are detailed in Section 3.3, which keeps the full planning graph connected while not requiring state gradients of the dynamics Fθ. For our planner, we find it helpful to alternate between (a) and (b) throughout the planning optimization.

Our main object of interest is a learned world model $F_{\theta}:\mathcal{S}\times\mathcal{A}\rightarrow\mathcal{S}$ that predicts the next state given the current state and action. For visual domains, states are typically represented in a learned latent space to handle high-dimensional observations. Here we assume $\mathcal{A}=\mathbb{R}^{k}$ is a continuous Euclidean action space.

We consider the problem of fixed-goal path planning: finding an action sequence $\mathbf{a}=(a_{0},a_{1},\ldots,a_{T-1})$ that, with respect to the dynamics of the world model $F_{\theta}$ and a given initial state $s_{0}\in\mathcal{S}$, reaches a set goal state $g\in\mathcal{S}$: where the terminal state $s_{T}$ is generated recursively through the update rule $s_{t+1}=F_{\theta}(s_{t},a_{t})$: We can sufficiently compute $\mathbf{a}^{*}$ by solving the following optimization problem: Optimizing Eq. directly is challenging due to two main problems. First, it requires $T$ applications of $F_{\theta}$ (see Eq. 2), which is computationally expensive and difficult to optimize due to the poor conditioning arising from repeated applications of $F_{\theta}$ (see Appendix 8.1 for details). Second, it is susceptible to local minima and a jagged loss landscape---see Figure 1. Due to these reasons, existing planners are based on zero-order optimization algorithms like CEM and MPPI (williams2016aggressive) which are highly stochastic and do not require gradient computation.

In what follows, we propose a gradient-based planner which alleviates these difficulties, while also using the differentiability of the model $F_{\theta}$. In Section 3, we lift the optimization problem by also optimizing over states, which leads to faster convergence and better conditioning. In Section 3.2, we introduce stochasticity, which helps escape local minima.

## Decoupling dynamics for gradient-based planning

We consider planning with a world model $F_{\theta}$ and horizon $T$. Given an initial state $s_{0}\in\mathcal{S}$ and goal state $g\in\mathcal{S}$, we optimize an action sequence $\mathbf{a}=(a_{0},\dots,a_{T-1})$ such that the rolled-out state $s_{T}(\mathbf{a})$ is as close to $g$ as possible. A standard approach defines a trajectory by rolling out the model, but backpropagating through a deep composition of $F_{\theta}$ can be unstable and ill-conditioned. Following prior work on lifted planning (tamimi2009nonlinear; rybkin2021model), we introduce auxiliary states $\mathbf{z}=(z_{1},\dots,z_{T})$ and enforce dynamics consistency through a penalty function.

### Parallelized planning

We first want to decouple the states from the explicit rollout outputs. Writing Eq. in terms of each intermediate dynamics condition, we get the following: The minimization in Eq. is equivalent to Eq. in that they share global minimizers.

Immediately, this gives a great benefit in that *all world model evaluations are parallel*; there is no need to do serial rollouts like what is required in Eq.. There are however two main issues with optimizing this loss directly: *Local minima*. When optimizing with respect to states, the states might be stuck in an unphysical region; for example, Figure 7 shows a case where states go straight through a barrier. To address this, we propose to use Langevin state updates which promote exploration (see Section 3.2).

*World model sensitivity for high-dimensional states.* When optimizing $s$ directly over a higher dimensional space (e.g. vision-based), we observe that the Jacobian $J_{s}F_{\theta}(s,a)$ does not necessarily have any nice low-dimensional or convex structure; in practice, the world model can be easily steered toward outputting any desired output state, as depicted in Figure 3. We address this in Section 3.3 with a reshaping of the descent directions.

We now describe our approach to address these two fundamental problems with lifted-states approaches to planning.

### Exploration via Langevin state updates

The lifted optimization in Eq. is still non-convex and can get trapped in poor local minima. In practice, we frequently observe that deterministic joint updates in $(\mathbf{a},\mathbf{s})$ converge to "bad" stationary points where the intermediate variables settle into an unfavorable basin; for example, a linear route that ignores barriers or walls like in Figure 7. To circumvent this, we inject stochasticity directly into the state iterates, yielding a Langevin-style update that encourages exploration in the lifted state space.

### Langevin dynamics on state iterates

Consider the optimization induced by Eq.. A standard way to escape spurious basins is to replace deterministic gradient descent on $\mathbf{s}$ with overdamped Langevin dynamics (gelfand1991recursive), whose Euler discretization takes the following form: where $\xi_{t}^{k}\sim\mathcal{N}(0,I)$. That is, each optimization step performs a gradient descent update on the intermediate states, followed by an isotropic Gaussian perturbation. Intuitively, the noise allows the iterates to "hop" between nearby basins of the lifted loss landscape.

### Noise on states vs. actions

By only noising the states, we can still condition on more dynamically feasible trajectories, while still allowing exploration over a wider distribution. Intuitively, planning problems often have a single (or small number of) intermediate states to find for the solution, and being able to noise directly over states rather than actions allows us to find these intermediate states faster. See Appendix 8.3 for a characterization of the sampled distribution.

Figure 3: Sensitivity of state gradient structure. Examples of three states far away from the goal on the right (either in-distribution or out-of-distribution), such that taking a small step along the gradient s′ = s − ϵ∇sℒ(s), ℒ(s) = ∥Fθ(s, a = 0) − g∥22, leads to a nearby state s′ that solves the planning problem in a single step: Fθ(s′, 0) = g. Thus, optimizing states directly through the world model Fθ can be quite challenging.

### Sensitivity to state gradients

### A note on adversarial robustness of state gradients

In practice, $F_{\theta}$ is learned and can have brittle local geometry. When optimizing Eq. by gradient descent in both $\mathbf{a}$ and $\mathbf{s}$, we observed empirically that gradients with respect to the state inputs, $\nabla_{s}F_{\theta}(s,a)$, can be exploited: for any local goal-reaching objective of the following form: instead of the optimizer learning to find an $s$ on-manifold such that applying the action $a$ leads to end state $y$, the optimizer can find a nearby ambient $s+\delta$, $\|\delta\|_{2}\ll 1$ such that the loss is practically minimized: $y\approx F_{\theta}(s+\delta,a)$, *regardless of the starting state $s$*. This is analogous to the adversarial robustness issue of image classifiers (szegedy2013intriguing; shamir2021dimpled): high-dimensional input spaces for trained neural networks can have high Lipschitz constants, hindering optimization performance.

Unfortunately, any loss function over $\mathbf{s}$ and $\mathbf{a}$ whose minimizers are feasible dynamics must depend on the state gradient $\nabla_{s}F$ in a meaningful way. We provide the informal theorem here, with formalization and proof in Appendix 8.4.

### Theorem 1 (informal)

A differentiable loss function over state/action trajectories $\mathcal{L}:\mathcal{S}^{T}\times\mathcal{A}^{T}\to\mathbb{R}$ given a world model $F_{\theta}:\mathcal{S}\times\mathcal{A}\to\mathcal{S}$ cannot satisfy both of the following at the same time: Minimizers of $\mathcal{L}$ correspond to dynamically feasible trajectories: $F_{\theta}(s_{t},a_{t})=s_{t+1}$, $\mathcal{L}$ is insensitive to the world model state gradient $\nabla_{s}F_{\theta}$.

To address this adversarial sensitivity, we detach gradients through the *state inputs* of the world model, while still differentiating with respect to the actions. We denote by $\bar{s}_{t}$ a stop-gradient copy of $s_{t}$ (i.e., $\bar{s}_{t}=s_{t}$ in value, but treated as constant during differentiation).

Figure 4: Virtual states learned through planning. All examples are instantiations of our planner at horizon 50 in the Point-Maze, Wall-Single, and Push-T environments. Regardless of the dynamics constraint relaxation and state noising, directly optimized states find realistic, non-greedy paths towards the goal.

### Grad-cut dynamics loss

We begin by applying a gradient stop to the state inputs in the dynamics loss: This objective is differentiable with respect to $\mathbf{a}$ and the *next* states $s_{t+1}$, but does not backpropagate through $s_{t}$ via $F_{\theta}$.

### Dense goal shaping on one-step predictions

While Eq. improves robustness, it introduces a new degeneracy: paths gravitate towards the current rollout, regardless of proximity to the goal. To provide a task-aligned signal at every time step without state-input gradients, we add a goal loss on the one-step predictions: This encourages each predicted next state to move toward the goal, supplying gradient information to every action $a_{t}$ while maintaining the grad-cut on $s_{t}$. This is depicted visually in Figure 2, and theoretically in Appendix 8.4. Crucially, due to the stop-gradient $\bar{s}_{t}$, gradients through $F_{\theta}(\bar{s}_{t},a_{t})$ flow only with respect to $a_{t}$ (and not $s_{t}$), which prevents the optimizer from exploiting adversarial state-input directions. The final energy that is sampled from is then the following: | | $\displaystyle\begin{split}\mathcal{L}(\mathbf{s},\mathbf{a})=&\sum_{t=0}^{T-1}\big\|F_{\theta}(\bar{s}_{t},a_{t})-s_{t+1}\big\|_{2}^{2}\\ | | \(10\) | | | &\quad+\gamma\sum_{t=0}^{T-1}\big\|F_{\theta}(\bar{s}_{t},a_{t})-g\big\|_{2}^{2},\end{split}$ | | | where $\gamma>0$ is fixed.

Resulting noisy dynamics. The final resulting dynamics, after explicitly writing out $\nabla_{a}\mathcal{L}$, are as follows: where $\xi_{t}^{k}\sim\mathcal{N}(0,I)$. Importantly, while the action dynamics still follow a gradient flow, the states do not follow a true gradient vector field, and thus *the resulting dynamics are not Langevin.* What results are still noisy dynamics that bias towards valid goal-oriented trajectories, but whose efficiency will require an extra synchronization step as described in the following section.

### Full-rollout synchronization

The no-state-gradient updates are designed to be robust to brittle state-input Jacobians of the learned world model. However, the stochastic optimization in Eq. still needs a method of strict descent towards true minima. In practice, we found it beneficial to periodically "sync" the plan by briefly running standard full-gradient planning on the original rollout objective.

### Full-gradient rollout step

Every $K_{\mathrm{sync}}$ iterations, we perform $J_{\mathrm{sync}}$ steps of gradient descent on the original planning loss where $s_{T}(\mathbf{a},s_{0})$ is computed by sequentially rolling out the world model During this synchronization phase we update only the actions, using full backpropagation through the $T$-step rollout. By keeping these GD steps small relative to the stochastic dynamics of Eq., we benefit from the smoothed loss landscape in Figure 1c for wider exploration, and the sharp but brittle landscape in Figure 1b for refinement.

## Results

We evaluate our proposed planner GRASP across two complementary classes of environments designed to test (i) nonconvex long-horizon planning with obstacles and (ii) data-driven visual control under learned dynamics. Concretely, these experiments aim to answer three questions: Can the proposed planner overcome the greedy local minima that often trap shooting methods?

Does the method remain robust as the planning horizon increases?

Does the proposed planner converge to plans faster than rollout-based planners?

We provide self-ablations in Table 2, demonstrating the value of various components of our planner: using the state gradient detaching, the GD sync steps, and the level of the noise.

Table 1: Open-loop planning results on long range Push-T. Reported are success rate (%) and median success time (seconds; successful trials only) across planning horizons. 500 trials per setting. Each cell reports Success / Time.

Figure 4 visualizes planning iterations in several navigation environments, illustrating how trajectories initialized far from dynamically consistent rollouts converge to feasible plans that satisfy the learned dynamics.

### Baselines

We compare against three commonly used planners. CEM optimizes action sequences by iteratively sampling candidate trajectories, selecting elites, and refitting a sampling distribution. GD directly optimizes the action sequence by backpropagating through the dynamics model. LatCo (rybkin2021model) optimizes in a lifted latent/state-space by jointly adjusting intermediate latent variables and actions. This setting is different than the original LatCo method, which was originally applied in a model-based RL environment, but it still provides an important baseline for performance if we were to purely focus on direct optimization of Eq..

Figure 5: Success rate over time at a fixed horizon. Success rate over fixed set of open-loop planning tasks for CEM, GD, LatCo (rybkin2021model), and our planner for a fixed horizon of 50. Curves summarize how quickly each planner makes progress under the learned world model setting when evaluated at a fixed planning horizon. Shaded regions are Wald 95% confidence intervals.

For all methods, we sweep over hyperparameters and report results using the best-performing setting for each environment and horizon. For our planner, we initialize the states $\{s_{t}\}_{t=0}^{T}$ as noised around the linear interpolation between $s_{0}$ and $g$: $s_{t}=\frac{t}{T}g+(1-\frac{t}{T})s_{0}+z$, $z\sim\mathcal{N}(0,\epsilon I)$, and actions initialized at zeros: $a_{t}=0$.

### Environments and evaluation protocol

We evaluate planning on three visual control environments with learned dynamics: *PointMaze*, *Wall-Single*, and *Push-T*. World models are trained using the DINO-wm framework (zhou2024dino), following the original paper's setup, where the world model $F_{\theta}(s,a)$ takes 5 actions and predicts 5 steps ahead; that is, if $\text{dim}(\mathcal{A})=2$, then $F_{\theta}$ takes actions as vectors of stacked actions $\mathbf{a}\in\mathbb{R}^{10}$.

All reported metrics measure task success under the learned world model. Success is defined as reaching the goal region within the planning horizon.

### Long-term planning and horizon scaling

We evaluate planners in the long-horizon regime, where our parallelized stochastic planner is more intended; greedy local minima and optimization instability become the dominant challenges.

Table 2: Ablation Studies over the GD sync steps, level of noise for Langevin dynamics, and whether we use our detached gradient approach with the goal-reaching objective or not. GD sync happens every 100 stochastic steps. Ablations done on the Push-T environment at horizon H = 40. Time reported is median over successful trials, which only beats our method when the accuracy is much smaller.

GRASP remains reliable as the planning horizon increases: it solves more tasks and finishes a majority of its successful trials faster, showing stronger robustness to long horizons than the baselines as shown in Table 1. Beyond the median completion times, we provide further illustration of the solving speed of our planner in Figure 5, showing further that most of its plans converge at an earlier time. At the longer horizons for Push-T, where it is more important for the planner to explore non-greedy optima, GRASP finds more success than the baselines and is able to find the needed non-greedy trajectories, as visualized in Figure 6.

Table 3: Short Term Planning. Success rate (%) for Push-T, PointMaze, and WallSingle. 500 trials per setting. Our method has comparable success rate while having a consistently low completion time (Table 4).

Table 4: Median completion times (seconds) across short-term experiments. 500 trials per setting. Our method has a consistently low completion time with a comparable success rate (Table 3).

### Short-term planning

We also evaluate short-horizon planning, to demonstrate that our planner can match performance on shorter, easier tasks. Table 3 reports success rates across environments for horizons ranging from $H=10$ to $H=30$, while Table 4 reports median wall-clock planning times.

Across all environments and short horizons, the proposed planner achieves success rates comparable to the baselines. Alongside similar success rates, our proposed planner exhibits consistently low planning times. As shown in Table 4, it is among the fastest methods across all environments and horizons, often significantly faster than sampling-based approaches and competitive with gradient-based optimization, sacrificing some speed for a higher success rate. These results indicate that even in relatively short and easy planning regimes, our planner remains competitive with the baselines.

Overall, these results demonstrate that GRASP consistently matches strong baselines in short-term planning, while outperforming them in long-horizon settings by avoiding greedy failures and converging more quickly in wall-clock time.

## Related work

World modeling has shown significant improvement in sample efficiency for model-based reinforcement learning (hafner2025mastering). By learning to predict future states given current states and actions, world models enable planning without access to an interactive environment (ding2024understanding). Recent work has focused on learning latent-space representations to handle high-dimensional observations assran2025v, with models now demonstrating the ability to scale and generalize across diverse environments (bar2025navigation). In this paper, we develop an efficient planning algorithm for action-conditioned video models.

Sampling-based planning in world models traditionally relies on methods like the Cross-Entropy Method (CEM rubinstein2004cross) and random shooting. While these methods are robust and simple to implement, they suffer from serial evaluation bottlenecks and poor scaling with planning horizon length (bharadhwaj2020model). Recent work proposes performance improvements---such as faster CEM variants with action correlation and memory, parallelized sampling via diffeomorphic transforms, and massively parallel strategies---but fundamental limitations remain for very long horizons (pinneri2021sample; lai2022parallelised).

Gradient-based planning leverages the differentiability of neural world models to optimize action sequences directly (jyothir2023gradient). Early approaches applied backpropagation through time to optimize actions (thrun1990planning), but face challenges with vanishing/exploding gradients and poor conditioning over long horizons. Hybrid strategies combining gradient descent with sampling-based methods---such as interleaving CEM with gradient updates---have shown promise. CEM-GD variants interleave backwards passes through the learned model with population-based search for improved convergence and scalability (bharadhwaj2020model; huang2021cem). Recent work improves gradient-based planners by training world models to be adversarially robust to improve gradient-based planning (parthasarathy2025closing); our method instead tries to improve gradient-based planning for more general world models, without any pretraining modifications.

State optimization and multiple shooting in optimal control. The idea of treating states as optimization variables separate from dynamics constraints has a rich history in classical optimal control. Non-condensed QP formulations in MPC (jerez2011condensed) decouple state and input optimization for improved numerical properties. Multiple shooting methods (tamimi2009nonlinear; diedam2018global) break long-horizon problems into shorter segments with continuity constraints. Direct collocation approaches (bordalba2022direct; nie2025reliable) optimize state and control trajectories simultaneously while enforcing dynamics through collocation constraints. These methods have primarily been applied to systems with known analytical dynamics. Trajectory optimization methods in robotics have developed parallel shooting techniques and GPU-accelerated planning algorithms (guhathakurta2022fast), but most approaches still face fundamental limitations when applied to learned world models, particularly visual world models where dynamics are approximate and high-dimensional.

Noise and regularization in optimization. Stochastic optimization techniques and noise injection have long been recognized for their ability to improve optimization outcomes (robbins1951stochastic), and can help regularize and explore complex loss landscapes (welling2011bayesian; xu2018global; bras2023langevin; foret2020sharpness). In the context of planning, noise is commonly used in sampling-based methods, but its systematic incorporation into gradient-based planning for learned models remains underexplored.

## Limitations and future work

Although the proposed planner shows clear advantages in long-horizon settings, its benefits are more limited at short horizons. As demonstrated in our experiments, for small planning horizons the planner typically achieves success rates and completion times that are comparable to strong baselines such as CEM and gradient-based optimization, rather than strictly outperforming them. This suggests that the primary gains of the method arise in regimes where long-horizon reasoning and non-greedy planning are essential, rather than in short-horizon settings where simpler methods already perform well.

Hybrid planners (that combine iterations of a rollout-based planner like CEM and a gradient-based planner like GD) have been implemented to get the "best of both worlds" from the two approaches (huang2021cem), and there are many ways to "hybridize" our planner as well. We leave exploration of such methods for future work.

Several components of the planner are designed to mitigate the unreliability of state gradients in learned world models. While effective, these modifications introduce additional structure and hyperparameters that would ideally be unnecessary. If state representations induced by the world model were smoother or more geometrically well-behaved in the state space, many of these stabilization mechanisms could be removed, potentially leading to further speed improvements. Promising directions toward this goal include improved representation learning through adversarial training, diffusion-based world models, or other techniques that explicitly regularize the geometry of the learned state space.

## Conclusion

World models provide a powerful framework for planning in complex environments, but existing approaches struggle with long horizons, high-dimensional actions, and serial computation. We propose GRASP, a new gradient-based planning algorithm with two key contributions: (a) a lifted planner that optimizes actions together with "virtual states" in a time-parallel manner, yielding more stable and scalable optimization while allowing direct control over exploration via stochastic state updates, and (b) an action-gradient-only planning variant for learned visual world models that avoids brittle state-input gradients while still exploiting differentiability with respect to actions. Experiments on visual world-model benchmarks show that our approach remains robust as horizons grow and finds non-greedy solutions at a faster rate than commonly used planners such as CEM or vanilla GD.
