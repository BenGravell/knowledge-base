<!-- arxiv-full-text:v1 {"arxiv_id": "2606.07193", "source": "arxiv-html"} -->

## Introduction

Contact-conditioned reinforcement learning (RL) policies have shown dynamic locomotion across diverse morphologies. By accepting desired contact locations as input and mapping them to low-level joint commands, these policies decouple high-level contact planning from PD target or torque generation. These policies demonstrate strong task performance, but lack an active mechanism to prevent safety violations in the environment. This is especially problematic when deployment introduces obstacles or spatial constraints that were not present during training.

Large-scale training or finetuning of the RL policy with safety objectives is impractical for all possible cases. An alternative is a *safety filter*: a post-hoc layer that intervenes when a violation is imminent. For example, Hamilton-Jacobi (HJ) reachability, Control Barrier Functions (CBF), and Model Predictive Shielding (MPS) provide rigorous guarantees. However, they scale poorly to whole-body models, require hand-crafted certificates that fail under unmodeled contact, or resort to conservative recovery controllers that sacrifice performance (see Sec. 2).

Hence, we propose a shielding method that addresses MPS conservatism while maintaining task objectives by operating on *contact locations*. Our key insight is that these serve as a useful kinematic abstraction for enforcing contact-related safety constraints, such as whole-body collision avoidance, in legged robots. For a quadruped, this means optimizing over desired foot placements, and the same principle applies to humanoids or manipulators (which we leave for future work). However, most existing safety filters that exploit this contact structure use reduced-order models, whereas we employ a full-physics simulator to enable whole-body reasoning without sacrificing model fidelity.

Our choice for this is motivated by three factors. First, whole-body collisions during locomotion are primarily determined by where the feet land, so redirecting footsteps indirectly steers the whole body around or over obstacles. Second, contact locations constitute a plan that the policy smoothly tracks over time. This allows the safety optimizer to run asynchronously at a lower frequency. This decoupling is essential for deploying very long and expensive, full-physics rollouts online, which is not possible with direct torque control. Third, although the dimensionality equals that of joint torques in a 12DOF quadruped, the effective search space is far smaller; contact locations are physically interpretable, and the policy provides a smooth learned mapping from contacts to joint targets.

At each control step, our filter rolls out the nominal contact plan from a planner or command input. If a safety violation is predicted within a receding horizon, a warm-started sampling-based optimizer searches for safer alternative contact sequences that maximize a finite-horizon return bootstrapped by a learned value function and remain close to the nominal plan. Further, we make the optimization tractable through three components: (i) a geometric projection of sampled contact locations onto the feasible set, (ii) a momentum-augmented update that accelerates convergence, and (iii) a Replica Exchange strategy that maintains exploration and escapes shallow local minima.

To summarize, our contributions are: A predictive safety filter operating on contact locations fed to RL policies, enabling whole-body collision avoidance without policy modification.

A sampling-based optimization scheme with three tractability-enabling components, namely geometric projection, momentum-augmented updates, and replica exchange that improve the performance of the sampling-based predictive controller.

Simulation and real-world validation on a quadruped, demonstrating substantial reductions in safety violations over long horizons in nonsmooth contact landscapes.

## Related Works

Sampling‑Based Zero‑Order Optimization: Zero‑order optimizers such as Model Predictive Path Integral (MPPI) and the Cross‑Entropy Method (CEM) have been applied to legged locomotion for full‑order torque‑level control, combined with learned value functions for planning, and learned dynamics. These methods handle discontinuous cost landscapes and contact dynamics well, but they require extensive sampling and iterations in joint space for real-time long-horizon safety filtering.

Hamilton-Jacobi Reachability: Hamilton-Jacobi (HJ) reachability provides rigorous guarantees by computing an offline value function whose sub-zero level set defines unsafe states. While effective for low-dimensional systems, it scales exponentially with state dimension, making whole-body legged models intractable. Moreover, the value function must be recomputed for new scenario changes, precluding online adaptation.

Control Barrier Functions: CBFs enforce forward invariance via quadratic programming, and have been applied to legged robots using reduced-order models. However, constructing valid CBFs for intermittent multi-contact dynamics remains exceptionally difficult, and the guarantee relies on accurate model knowledge that unmodeled contacts in reduced-order models can easily violate, rendering the formal guarantees infeasible in practice.

Predictive Safety Filters / Model Predictive Shielding: MPS forward‑simulates candidate actions and overrides the nominal policy with a recovery controller when a safety violation is predicted. MPS avoids the curse of dimensionality and does not require an analytical barrier function, but its main limitation is the conservatism of standard recovery policies, which are safe but task‑agnostic. Dynamic MPS mitigates this by planning over a receding horizon with a learned value function that captures long‑term returns. For legged systems, prior work has exploited contact-location abstraction within reduced-order models, or learned game-theoretic fallbacks that switch policies online; however, these either lack whole-body reasoning or perform only binary switching without online optimization. casts safety filtering in a nonlinear model predictive control (MPC) but requires a recoverable (viable) set, which is exceedingly hard to characterize for general locomotion problems.

Figure 1: Landscape of safety filters for legged locomotion across search-space complexity and model fidelity. * performs runtime policy switching only, without online optimization.

Safe Reinforcement Learning with Formal Guarantees: Several works integrate safety into RL training while providing formal guarantees. combines a task policy with a backup safety policy trained via the safety Bellman equation (derived from HJ reachability) and uses a shielding mechanism. learns an agile policy and a recovery policy whose switching is governed by a reach‑avoid value network rooted in HJ theory. predicts a control‑theoretic safety value function online from LiDAR observations to construct an adaptive safety filter for quadrupedal navigation. While such methods achieve strong safety performance within their training distributions, they remain vulnerable to out‑of‑distribution scenarios.

Positioning: Figure 1 contextualizes our approach within the landscape of safety filters for legged robots. Rather than relying on a task‑agnostic recovery policy as in standard MPS, we re‑cast the safety intervention to be minimally invasive, i.e., deviate minimally from the nominal/desired behavior. Furthermore, as motivated in Sec. 1, contact locations offer a principled middle ground to intervene : expressive enough for whole-body reasoning, yet tractable enough for online sampling-based optimization. We now detail our safety filter framework that instantiates this design choice in the next section.

## Methodology

### Preliminaries

We consider a quadruped robot controlled by a contact‑conditioned locomotion policy $\pi$ that maps the current state and desired foot placements to low‑level joint commands. Let $s_{t}\in\mathbb{R}^{n_{s}}$ denote the robot's proprioceptive observation at discrete time $t$; it includes joint angles, joint velocities, the body's linear and angular velocity (in the base frame), and the 3D Cartesian positions of the four feet relative to the base. The policy outputs an action $a_{t}=\pi(s_{t},p_{t})$, where $p_{t}\in\mathbb{R}^{12}$ is the vector of desired foot contact locations (one 3D point per foot). In our implementation, $a_{t}$ is a vector of target joint positions, which are tracked by a PD controller producing joint torques. The closed‑loop transition dynamics are given by $s_{t+1}=f(s_{t},a_{t})$, where $f$ is the full physics simulation provided by the MuJoCo MJX solver. This high‑fidelity model eliminates the approximation errors typical of simplified reduced‑order models.

The locomotion reward $r(s_{t},a_{t})$ encodes the high‑level task (e.g., tracking a desired contact location while penalizing energy consumption) and is identical to the reward used to train $\pi$. A high‑level planner produces a sequence of nominal contact locations $\{\bar{p}_{t+\tau}\}_{\tau=0}^{H-1}$ for a horizon $H$. However, neither $\pi$ nor the nominal contact plan may have a mechanism to actively enforce safety constraints. Hence, we introduce our general safety framework in the next section.

### General Framework

Our safety filter is agnostic to the internals of $\pi$ and requires only that the policy accepts contact locations as input. At each control step, given the current state $s_{t}$ and a sequence of nominal contact locations $\{\bar{p}_{t+\tau}\}_{\tau=0}^{H-1}$ from the planner, the filter performs the following steps: Predict: Roll out the nominal sequence using the full dynamics $f$ and the policy $\pi$ over the horizon $H$. Check whether any safety constraint (Sec. 3.3) would be violated.

Intervene only if needed: If no violation is detected, the nominal contact $\bar{p}_{t}$ is sent directly to $\pi$. If a violation is predicted, the filter activates a sampling‑based optimizer that searches for an alternative contact sequence $\{p_{t}^{*},\dots,p_{t+H-1}^{*}\}$.

Optimize: The optimizer maximizes a finite-horizon objective that balances task reward and safety, using the nominal sequence as a warm start, Fig. 2.

Execute: The first optimized contact location ($p_{t}^{*}$) is fed to $\pi$, which produces joint-level actions $a_{t}$. The process repeats at the next time step in a receding horizon fashion.

Formally, the optimization problem solved when the intervention occurs is: | | $\displaystyle\max_{p_{0},\dots,p_{H-1}}$ | $\displaystyle\mathbb{E}\left[\sum_{t=0}^{H-1}\gamma^{t}r(s_{t},a_{t})+\gamma^{H}V(s_{H})\right]$ | | \(1\) | | | s.t. | $\displaystyle g(s_{t},p_{t})\leq 0,\quad a_{t}=\pi(s_{t},p_{t}),\quad s_{t+1}=f(s_{t},a_{t}),\quad\forall\,t=0,\dots,H-1.$ | | | where $g$ encodes safety constraints. $V$ is the value function that bootstraps the finite-horizon return. We employ a scheme similar to, where $V$ is trained offline via temporal‑difference (TD) learning on trajectories collected by the sampling-based optimizer in simulation (more details are provided in the Appendix D.3).

Figure 2: Predictive safety filtering pipeline. Unsafe nominal contact plans are refined through sampling-based optimization with parallel full-physics rollouts.

### Safety Constraints, $g$

We evaluate two complementary safety constraints at each forward rollout and integrate them as soft penalties. Crucially, the penalty depends on the actual foot positions observed in the simulated state (denoted $h_{t}$), not on the commanded $p_{t}$, thereby capturing the true closed‑loop outcome. The filter assumes that the geometry and poses of all obstacles are known a priori (e.g., from a map), and in our simulation experiments, they are perfectly known. The extension to the online perception with uncertainty is left for future work.

Foot Contact Penalty: All obstacles are modeled as geometric primitives (spheres, cylinders, boxes, or capsules). For each foot position $h_{t}$ (a 3D point per foot extracted from $s_{t}$) and obstacle $j$, we compute the signed distance function (SDF) $\mathcal{D}_{j}$, defined in closed form for each geometric primitive (see Appendix D.2). Then the soft penalty for that foot is given by $d_{t}=\sum_{j}\max(m-\mathcal{D}_{j}(h_{t}),\,0)^{\kappa}$, where $m$ is a safety margin and $\kappa$ controls the steepness.

Whole-Body Collision: We query MuJoCo's contact data for every simulation step and extract a binary indicator $\mathbf{1}_{\mathrm{col}}(s_{t})\in\{0,1\}$ that equals $1$ if any robot link contacts an obstacle. Trajectories that trigger this indicator receive a large penalty, ensuring whole-body collisions are likely to be rejected. Thus, the objective function from with relaxed safety constraints becomes: where $M\ggg 0$ is chosen large enough to strongly reject colliding trajectories.

### Sampling-Based Optimization

We solve with MPPI, which is a derivative‑free, sampling‑based optimizer. These are well‑suited to the non‑smooth, discontinuous cost landscape induced by contact dynamics. In our approach, we approximate the optimal solution by iteratively updating the contact location sequence $\mu_{t}\triangleq(p_{t},\ldots,p_{t+H-1})$. At each iteration, $K$ perturbations $\{\xi_{t}^{(k)}\}_{k=1}^{K}$ are drawn from $\mathcal{N}(0,\Sigma_{t})$ to form candidates $\mu_{t}^{(k)}=\mu_{t}+\xi_{t}^{(k)}$.

Projection: Prior to rollout evaluation, each candidate contact location is projected onto the collision-free set $\mathcal{F}\triangleq\bigl\{\mathbf{p}\mid\mathcal{D}_{j}(\mathbf{p})\geq\varepsilon_{\text{safe}},\ \forall\,j\bigr\}$ via the projection operator $\tilde{p}_{t}^{(k)}=\Pi_{\mathcal{F}}\big(p_{t}^{(k)}\big)$, yielding the candidate sequence $\tilde{\mu}_{t}^{(k)}\triangleq(\tilde{p}_{t}^{(k)},\ldots,\tilde{p}_{t+H-1}^{(k)})$. We solve this projection as a Quadratic Program (QP) by linearizing each SDF constraint about the current candidate, as the safety penalty in alone does not guarantee constraint satisfaction. Further details and an analysis of the projection's effect on solution quality are provided in the Appendix C.

Then, for each projected candidate $\tilde{\mu}_{t}^{(k)}$, we roll out the dynamics to compute the weights and update the sequence with an exponentially weighted average: where $\lambda$ is the inverse temperature. We stabilize the weights $w_{k}$ by subtracting the batch maximum. It is important to note that, since the projection is only on the sampled contact targets, the actual foot locations in the rollout may violate safety constraints due to poor tracking by the RL policy.

Momentum-based Updates: To accelerate convergence, we propose using momentum-augmented updates derived from an Accelerated Proximal Natural Gradient Descent formulation. Further, these updates can be easily combined with CEM- and MPPI-like weighting $w_{k}$ Thus, using this formulation, the update for the contact sequence becomes: and the updates for the covariance are computed: where $\beta\in0,1)$ is the momentum factor and $0\leq\alpha<\frac{\beta+1}{2}$ is an entropy coefficient. Importantly, $\beta\in$ yields accelerated updates that extrapolate in the direction of improvement. We provide a detailed derivation for Eqs. ([4) and in the Appendix B.

Replica Exchange for Exploration: To avoid premature convergence to poor local optima, we employ a replica‑exchange (parallel tempering) strategy. We maintain $L$ MPPI replicas with inverse temperatures $\lambda_{1}<\lambda_{2}<\dots<\lambda_{L}$. After each optimizer iteration, adjacent replica pairs $(i,\,i+1)$ swap their contact-sequences according to the Metropolis--Hastings criterion: where $\bar{\mathcal{S}}_{i}$ is the average total return from of replica $i$'s sample set. Samples themselves are discarded after each swap, as they are temperature-specific. This allows high-temperature replicas to explore broadly while low-temperature replicas exploit promising solutions, enabling escape from shallow local minima.

Additionally, at each new planning step, we shift the previously optimized contact sequence forward by one time step (dropping the first element) and append a nominal contact at the end. This shifted sequence serves as a warm start for the optimizer when intervention is required, thereby promoting temporal consistency. The complete safety filter is summarized as Algorithm 1 in the Appendix.

## Experiments

We evaluate our predictive safety filter on whole-body collision-avoidance tasks for a Unitree Go2 quadruped in the MuJoCo physics simulator and the real world. The filter is deployed at a planning frequency of $3\,\mathrm{Hz}$, with $H=5$ footsteps (effectively $\sim$`<!-- -->`{=html}150 full physics update steps into the future), $K=512$, and $N=3$ iterations per planning cycle. All experiments are run on a single NVIDIA RTX 3090, with rollouts accounting for the bulk of the computation. The locomotion policy is trained offline using the procedure described in and remains frozen throughout while running at $50\,\mathrm{Hz}$. In all experiments, the nominal planner produces footstep targets using a trotting-gait heuristic driven by a user input. Additional implementation details are in the Appendix D.4.

Scenarios: Our tests consider a dense, cluttered environment consisting of obstacles of different categories and dimensions that mimic real-world objects such as phones, packages, and cables, on which the robot must not step. We also qualitatively test our proposed safety filter for navigating large obstacles to reach the goal and for simple dynamic collision avoidance (see Appendix E).

Baselines: We compare to a *CBF* and an *HJ* baseline that implements a unicycle approximation for a quadruped. For our method, we compare three different optimizers that solve the same optimization problem Eq.: *MPPI* with a fixed temperature, *CEM*, and *Replica Exchange MPPI*. Further, while our sampling-based optimizer incurs higher per-cycle computation than CBF or HJ, this cost is already reflected in all reported metrics: the asynchronous design ensures the low-level policy continues executing at $50\,\mathrm{Hz}$ regardless of planner latency, so wall-clock optimization time affects planning staleness but never robot stability. For completeness, we also report the performance of the unfiltered nominal contact locations plan, which serves as a lower bound on safety.

Metrics: We report three metrics averaged across episodes: (i) *Tracking Cost*, the cumulative tracking error between nominal and filtered contact locations plan; (ii) *Planner Violations*, the number of planning steps in which the optimized contact sequence triggers a safety violation; (iii) *Actual Violations*, the number of timesteps in which the robot makes physical contact with an obstacle.

### Simulation Results

Figure 3: Comparison of tracking cost, planner violations, and actual violations across baselines and our optimizer variants. Lower is better for all metrics. Error bars show the standard error over 10 random seeds. Notably, nominal incurs zero tracking cost by definition, but serves as the lower bound on task invasiveness and upper bound on safety violations.

## Planner Viol

## Actual Viol

## Planner Viol

## Actual Viol

Ours w/ Replica Exchange

## Planner Viol

## Actual Viol

Table 1: Ablation on the number of iterations (N) and horizon length (H) for three optimizers with our approach. Best in each column bolded. Mean ± std over 10 seeds.

Figure 3 shows the simulation results across three key metrics. The nominal plan has no tracking cost by definition, but incurs many violations since it lacks a mechanism to enforce safety. Both CBF and HJ Reachability reduce planner violations substantially compared to the nominal case. However, compared to our method, both incur higher tracking costs and more actual violations, suggesting that the reduced-order approximation is not suitable for dense, cluttered environments.

Our method, evaluated with any of the sampling-based optimizers, achieves the best safety-tracking trade-off. All three variants reduce actual violations to $\sim 30$ while maintaining competitive tracking costs. Notably, ours with Replica Exchange achieves the lowest tracking cost ($0.0086$), whereas MPPI and CEM perform similarly on all metrics. These results demonstrate that optimizing directly over foot contact locations with a full-physics model, rather than reduced-order dynamics, more effectively enables collision avoidance in cluttered scenes with minimal deviation from the nominal plan. However, we acknowledge that there remains a gap between planned and actual violations. The majority of these actual violations arise from swing-leg trajectories and the RL policy taking intermediate steps rather than unsafe contact locations.

We also ablate two key parameters of the sampling-based optimizer: the number of iterations $N$ and the planning horizon $H$, with results reported in Table 1. Increasing the computational budget, whether through more iterations or longer horizons, often increases actual collisions, as motion plans become stale in the asynchronous setting. This indicates a trade-off we believe is fundamental to asynchronous predictive safety filters. A moderate budget ($N=3$, $H\in[4\ldots 6]$) provides a good balance. All three optimizers behave similarly across most metrics, with Replica Exchange occasionally achieving lower tracking costs at the expense of substantially higher optimization time. We report an additional ablation on the number of samples $K$ in the Appendix C.

Figure 4: Percentage improvement in tracking cost relative to the baseline (β = 0, dashed), evaluated across the three optimizers at N = {1, 3, 6} iterations. All runs are evaluated over 10 seeds.

To understand the contribution of the momentum-augmented update (Sec. 3.4), we analyze how the tracking cost improves as a function of the number of optimizer iterations $N$ and the momentum coefficient $\beta$. Figure 4 reports the percentage improvement in tracking cost relative to the no-momentum baseline ($\beta=0$, dashed). Across all three optimizers, non-zero $\beta$ yields consistent gains, with $\beta=0.1$ achieving the best or near-best performance in most configurations. MPPI benefits most at low iteration counts, reaching ${\sim}40\%$ improvement at a single iteration, while CEM and Replica Exchange show larger gains as $N$ increases. Higher values ($\beta=0.5$) exhibit greater variance, particularly in Replica Exchange, suggesting a trade-off between momentum and stability.

### Real World Validation

We deploy the predictive safety filter on a Unitree Go2 hardware, where the proprioceptive state is streamed to an external PC running the optimizer, while the computed contact targets are returned to the robot via a tethered connection.

Figure 5 (left) shows keyframes from both the dense and the large obstacle scenarios. In the top sequence, the nominal contact plan would place a foot directly on an object; the filter redirects the contact to a safe gap between the objects. In the bottom sequence, the robot navigates around a white box and a set of poles; the filter steers the body laterally by adjusting foot placements.

Figure 5 (right) plots the online statistics for two horizon lengths during representative trials. With $H=8$, the filter looks farther ahead and therefore intervenes less aggressively, resulting in lower tracking and optimizer costs. The price is optimization time: $H=8$ requires $\sim$$400$ ms per cycle, whereas $H=6$ finishes in $\sim$$200$ ms. Because the policy tracks contact targets at $50\,\mathrm{Hz}$, the robot remains stable even when the asynchronous optimizer is slow. This empirically validates the decoupled design: the filter can afford longer horizons when computation permits, or fall back to shorter horizons for faster reactivity, without jeopardizing low-level stability.

Figure 5: Hardware validation on a Unitree Go2 navigating cluttered environments. Left: Keyframes from the two scenarios. Right: Online asynchronous planning statistics comparing H = 6 and H = 8. All hardware runs completed successfully.

## Conclusion

This work presents a sampling-based predictive safety filter that operates directly in the contact-location space of a contact-conditioned RL policy. The filter optimizes foot contact targets through full-physics rollouts, bootstrapped by a learned value function and accelerated by geometric projection, momentum, and replica-exchange exploration. We validate the approach in dense, cluttered simulation environments and in physical hardware experiments, demonstrating a substantial reduction in safety violations while remaining minimally invasive to the nominal gait.

Limitations & Future Work: Despite strong empirical results, our method lacks theoretical guarantees of optimality or safety. The filtered contact plan can deviate from the true safe set in regions where the sampling-based optimizer converges to a local optimum. Furthermore, the current geometric projection is a heuristic and may not preserve the optimizer's convergence properties.

Actual violations in our experiments were due to the policy generating intermediate swing-stance phase configurations that violate safety despite safe contact targets. To mitigate this, future work could implement safe online learning or fine-tuning using data collected by the optimizer.

The framework is described in general terms for any contact-conditioned legged robot, yet our validation is thus far limited to a quadruped on flat terrains. Multi-terrain and humanoid loco-manipulation introduce additional complexities in whole-body coordination and stability that remain to be tested, and scenarios requiring active torso twisting cannot be captured by contact-location optimization alone. Finally, integrating an online perception pipeline to enable fully autonomous deployment in unseen environments is an important direction for future work.
