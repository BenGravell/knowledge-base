<!-- arxiv-full-text:v1 {"arxiv_id": "2604.22149", "source": "arxiv-html"} -->

## INTRODUCTION

In safety-critical control systems such as autonomous vehicles, control inputs must be generated with rigorous safety assurances to prevent catastrophic failures. However, nominal controllers, often designed via reinforcement learning or heuristic methods, are typically optimized for performance rather than safety. Providing formal guarantees for such policies remains a significant challenge, necessitating an additional supervisory mechanism to ensure safe operation. Safety filters offer a practical, modular solution by monitoring the nominal controller's inputs and intervening only when necessary to enforce safety constraints.

Safety filters can be categorized by their certification mechanism. Some rely on precomputed certificates, such as Hamilton--Jacobi (HJ) reachability or control barrier functions (CBF). While these approaches are computationally efficient at runtime, HJ value function computation scales poorly with system dimensions, and CBF synthesis remains a nontrivial challenge. Alternatively, methods based on model predictive control (MPC) verify safety online by predicting future trajectories over a finite horizon. While these eliminate the need for explicit certificate construction, gradient-based formulations often struggle with non-smooth objectives, non-convex constraints, and numerical infeasibility.

In this paper, we propose a sampling-based safety filter that operates entirely online. Our method is inspired by sampling-based MPC algorithms, such as model predictive path integral (MPPI), the cross-entropy method (CEM), and Stein variational MPC (SV-MPC), which are particularly effective in non-differentiable or non-convex settings. Our method evaluates the nominal input by approximating a safety-conditioned posterior distribution over future control sequences and sampling from it. These sampled sequences are propagated through discrete-time dynamics and evaluated via a level function encoding the safety constraints. By maintaining a candidate safe sequence as a backup at each timestep, the filter intervenes whenever all sampled trajectories fail to satisfy the safety requirements.

Our approach differs from prior work in two key respects. First, we leverage SV-MPC to capture the multimodal structure of safe control distributions. In contrast, existing sampling-based safety filters typically draw control sequences from a unimodal Gaussian distribution, which limits their ability to effectively represent disjoint or non-convex safe regions. Second, we provide a probabilistic guarantee on the filter's restrictiveness by leveraging the scenario approach. In particular, the filter overrides the nominal input only when it is unlikely that a safe future control sequence exists under the sampling distribution. To the best of our knowledge, this is the first work to provide a formal probabilistic guarantee on the restrictiveness of a sampling-based safety filter under a finite number of samples.

The contributions of this paper are as follows: We propose a sampling-based safety filter that provides a probabilistic guarantee on its restrictiveness using the scenario approach.

We incorporate Stein variational model predictive control (SV-MPC) into the filter to represent the multimodal safety-conditioned posterior distribution over control sequences.

We validate the proposed filter on collision avoidance tasks in both single- and multi-vehicle scenarios with different nominal controllers.

This paper is organized as follows. Section II formulates the safety filtering problem, and Section III presents the proposed safety filter, including the filter algorithm, the construction of the sampling distribution, and the theoretical properties of the filter. Section IV demonstrates the proposed method in single- and multi-vehicle scenarios. Finally, Section V concludes the paper.

## PROBLEM STATEMENT

Consider a discrete-time dynamical system $\mathbf{x}_{t+1}=f(\mathbf{x}_{t},\mathbf{u}_{t})$, where $\mathbf{x}_{t}\in\mathcal{X}$ denotes the state and $\mathbf{u}_{t}\in\mathcal{U}$ denotes the control input at time $t$. Let $l:\mathcal{X}\rightarrow\mathbb{R}$ be a level function whose subzero level set defines the failure set The failure set represents unsafe states such as collisions or constraint violations. Therefore, ensuring safety means that the system state remains outside $\mathcal{L}$.

For a finite horizon $H$, let $U_{t}:=(\mathbf{u}_{t},\cdots,\mathbf{u}_{t+H-1})$ denote the control sequence starting at time $t$, and $X_{t}:=(\mathbf{x}_{t},\cdots,\mathbf{x}_{t+H})$ the corresponding state sequence. Since the dynamics are deterministic, $X_{t}$ is uniquely determined by $\mathbf{x}_{t}$ and $U_{t}$. We define an auxiliary binary random variable $\mathcal{O}_{\tau_{t}}\in\{0,1\}$ for the state-action trajectory $\tau_{t}=(X_{t},U_{t})$ as This means that $\mathcal{O}_{\tau_{t}}=1$ if the trajectory $\tau_{t}$ is safe over the horizon $H$, and $\mathcal{O}_{\tau_{t}}=0$ otherwise.

At each timestep $t$, a nominal controller generates a control input $\mathbf{u}^{\mathrm{nom}}_{t}\in\mathcal{U}$, which may be designed for arbitrary objectives and may not explicitly account for safety constraints. Therefore, directly applying $\mathbf{u}^{\mathrm{nom}}_{t}$ does not in general guarantee avoidance of $\mathcal{L}$.

In this paper, we design a sampling-based safety filter that samples $N$ candidate control sequences at each time step to assess the safety of the nominal input. Specifically, given the current state $\mathbf{x}_{t}$ and a nominal input $\mathbf{u}_{t}^{\mathrm{nom}}$, we first compute the next state $\mathbf{x}_{t+1}=f(\mathbf{x}_{t},\mathbf{u}_{t}^{\mathrm{nom}})$. We then sample $N$ candidate control sequences $U_{t+1}^{i}$, $i\in[1,N]$, and propagate each sequence from $\mathbf{x}_{t+1}$ to generate a trajectory $\tau_{t+1}^{i}$. The safety filter outputs the control input $\mathbf{u}_{t}^{\mathrm{safe}}$ as where $\mathbf{u}_{t}^{\mathrm{backup}}$ denotes a known safe control input. The $N$ control sequences are sampled from a distribution $\tilde{q}_{t+1}(U)$. The construction of $\tilde{q}_{t+1}(U)$ is described in Section III-B.

We aim to design a safety filter that satisfies the following two properties: Safety: For any $\mathbf{x}_{t}\notin\mathcal{L}$, there exists a control sequence $U_{t+1}$ such that from $\mathbf{x}_{t+1}=f(\mathbf{x}_{t},\mathbf{u}_{t}^{\mathrm{safe}})$, the trajectory $\tau_{t+1}$ is safe, i.e., $\mathcal{O}_{\tau_{t+1}}=1$. If this holds, we say that the filter guarantees safety at time $t$. $\epsilon$-restrictiveness: The filter overrides the nominal input only when it is unlikely that a safe future control sequence exists. Formally, an intervention implies that the probability of drawing a safe sequence from the sampling distribution $\tilde{q}_{t+1}(U)$ is bounded by $\epsilon$, that is, In the definition of $\epsilon$-restrictiveness, $\epsilon\in$ denotes a restrictiveness parameter, and the uncertainty in $\mathcal{O}_{\tau_{t+1}}$ arises from the sampled control sequence $U_{t+1}\sim\tilde{q}_{t+1}$. Smaller $\epsilon$ leads to less restrictive interventions. The least-restrictive case corresponds to $\epsilon=0$, where intervention occurs only when no safe trajectory exists after applying $\mathbf{u}^{\mathrm{nom}}_{t}$.

## Sampling-Based Safety Filter

In this section, we present the proposed sampling-based safety filter in detail. We first describe the overall algorithm and the construction of the sampling distribution. We then establish the safety guarantee and restrictiveness of the proposed filter.

### III-A Safety Filter Algorithm

1:Given: Trajectory cost function C(⋅) 2:Input: Current state xt, nominal input utnom, safe control sequence $U^{\mathrm{safe}}_{t}=(\bar{\mathbf{u}}_{t},\cdots,\bar{\mathbf{u}}_{t+H-1})$ 3:Output: Safe input utsafe, safe control sequence Ut + 1safe 10: utsafe ← utnom, Ut + 1safe ← Ut + 1i* 12: $\mathbf{u}^{\mathrm{safe}}_{t}\leftarrow\bar{\mathbf{u}}_{t},\;U^{\mathrm{safe}}_{t+1}\leftarrow\text{Shift}(U^{\mathrm{safe}}_{t})$ 13:return utsafe, Ut + 1safe Algorithm 1 Sampling-Based Safety Filter Our safety filtering algorithm is summarized in Algorithm 1. At each timestep $t$, the algorithm first predicts the next state $\mathbf{x}_{t+1}$ using the nominal control input $\mathbf{u}^{\mathrm{nom}}_{t}$ (line 1). It then samples $N$ control input sequences $U^{i}_{t+1}\;(i=1,\cdots,N)$ of length $H$ and rolls them out from $\mathbf{x}_{t+1}$ to generate $N$ corresponding state trajectories $X^{i}_{t+1}\;(i=1,\cdots,N)$ (lines 2--4). The safety of each trajectory is evaluated using the cost function where $C(\tau_{t+1}^{i})<0$ for safe trajectories and $C(\tau_{t+1}^{i})\geq 0$ otherwise. In our setting, the cost depends only on the state trajectory $X_{t+1}^{i}=(\mathbf{x}_{t+1}^{i},\cdots,\mathbf{x}_{t+H+1}^{i})$; however, we use the state-action trajectory notation $\tau$ for generality.

The filter then selects the control sequence with the minimum cost among all samples (line 5). If the minimum cost is negative, the nominal input $\mathbf{u}^{\mathrm{nom}}_{t}$ is applied without intervention, and $U^{\mathrm{safe}}_{t+1}$ is updated to the minimum-cost sample $U^{i^{*}}_{t+1}$ (lines 6--7). Otherwise, the filter applies the backup safe input $\mathbf{u}^{\mathrm{safe}}_{t}$ from the previously stored safe sequence $U^{\mathrm{safe}}_{t}$, and constructs $U^{\mathrm{safe}}_{t+1}$ by shifting $U^{\mathrm{safe}}_{t}$ forward by one step (lines 8--9). The last input of the shifted sequence is chosen to drive the system toward, or keep it inside, a safe control invariant set. Details are provided in Section III-C. The applied safe input $\mathbf{u}^{\mathrm{safe}}_{t}$ is then executed, and the updated safe sequence $U^{\mathrm{safe}}_{t+1}$ is stored for the next timestep (line 10).

### III-B Sampling Distribution

In line 3 of Algorithm 1, we draw samples to evaluate the safety of the nominal input $\mathbf{u}^{\mathrm{nom}}_{t}$. The efficacy of the safety filter depends on its ability to thoroughly explore the safe control space. Because the filter intervenes only when it fails to identify at least one safe candidate, a more comprehensive search directly reduces the frequency of unnecessary interventions. Furthermore, any safe sequence identified during this exploration serves as a potential safe backup $U^{\mathrm{safe}}_{t+1}$ for fallback control in subsequent timesteps.

To this end, we define a safety-conditioned posterior $p_{t+1}(U|\mathcal{O}_{\tau_{t+1}}=1)$. In this framework, we treat the search for safe control sequences as a Bayesian inference problem. By Bayes' rule, the safety-conditioned posterior is given by For brevity, we write $\mathcal{O}_{\tau_{t+1}}$ instead of $\mathcal{O}_{\tau_{t+1}}=1$ whenever the meaning is clear.

Since the posterior is generally intractable, we approximate $p_{t+1}(U|\mathcal{O}_{\tau_{t+1}})$ using variational inference. Specifically, we seek a distribution $q^{*}(U)$ in a tractable family $Q$ that minimizes the Kullback-Leibler (KL) divergence to the target posterior: Using, this optimization can be rewritten as | | $\displaystyle q^{*}=\arg\min_{q\in Q}\bigl\{-$ | $\displaystyle\mathbb{E}_{q}\left[\log p_{t+1}(\mathcal{O}_{\tau_{t+1}}|U)\right]$ | | \(6\) | To evaluate the safety-conditioned likelihood, we define a non-negative cost-likelihood function $L(\tau_{t+1})\propto p_{t+1}(\mathcal{O}_{\tau_{t+1}}\mid U)$, which maps the predicted trajectory $\tau_{t+1}$ to a safety-informed weight. A standard formulation for this likelihood is $L(\tau_{t+1})=\exp(-\alpha C(\tau_{t+1}))$ where $\alpha>0$ is a temperature parameter and $C(\tau_{t+1})$ is the trajectory cost. This exponential form ensures that trajectories with higher costs, those nearing or entering the failure set $\mathcal{L}$, are exponentially less likely to be represented in the posterior. With this definition, becomes which is the variational formulation used in sampling-based MPC.

1:Given: Trajectory cost function C(⋅), kernel k(⋅, ⋅), number of particles m, number of iterations iters, inverse-temperature α, step-size η 2:Input: Predicted state xt + 1 3:Output: Safety-conditioned posterior q̃t + 1(U) 4:Initialize q̃t + 1(U) and sample {U}i = 1m ∼ q̃t + 1(U) 5:for iter ← 1 to iters do 8: = ∇Uilog 𝔼[exp (−αC(τi))] + ∇Uilog q̃t + 1(Ui) 11: $\leftarrow\frac{1}{m}\sum\limits_{j=1}^{m}k(U^{j},U^{i})\nabla_{U^{j}}\log p_{t+1}(U^{i}|\mathcal{O}_{\tau^{i}}=1)$ 15:$w^{i}\leftarrow\frac{w^{i}}{\sum_{j=1}^{m}w^{j}}$ 16:return $\tilde{q}_{t+1}(U)=\sum_{i=1}^{m}w^{i}\mathcal{N}(U|U^{i},\Sigma)$ Algorithm 2 SV-MPC for Safety Filtering To solve, we adapt SV-MPC, which uses Stein variational gradient descent (SVGD) to construct a particle-based approximation of the posterior. The procedure is summarized in Algorithm 2.

Specifically, the distribution $q\in Q$ is represented by $m$ particles $\{U^{i}\}^{m}_{i=1}$. This particle-based representation allows the approximation to capture complex, potentially multimodal structures that cannot be represented by unimodal Gaussian distributions. SVGD iteratively updates each particle according to line 6 of Algorithm 2. The update consists of two components: the kernel $k(\cdot,\cdot)$ acts as a similarity weight that enables particles to share gradient information, while its derivative $\nabla_{U^{j}}k(U^{j},U^{i})$ introduces a repulsive force that prevents particles from collapsing to a single mode. Together, these terms allow the particles to "spread out" and approximate the target posterior more effectively. We use the radial basis function (RBF) kernel $k(U,U^{\prime})=\exp(-\frac{1}{h}\|U-U^{\prime}\|_{2}^{2})$, where $h=\text{med}^{2}/\log m$ and med denotes the median pairwise particle distance. This mechanism is critical for achieving comprehensive coverage of the safe control space; by maintaining a diverse set of candidate trajectories, the filter can simultaneously capture multiple, potentially disjoint, safe modes.

At the beginning of Algorithm 2, $m$ particles are initialized from a zero-mean Gaussian distribution (line 1). The algorithm then computes the gradient of the log posterior for each particle (lines 3--4), which provides the update direction for minimizing the objective . The particles are subsequently updated (lines 5--7). The second term $\nabla_{U^{j}}k(U^{j},U^{i})$ in line 6 acts as a repulsive force between particles, enabling the approximation to capture multimodality. After the updates, the particle weights $w_{i}$ are computed based on the trajectory cost (lines 8--9). The algorithm then constructs a Gaussian mixture $\tilde{q}(U)=\sum^{m}_{i=1}w_{i}\mathcal{N}(U|U^{i},\Sigma)$, where $\mathcal{N}(U|U^{i},\Sigma)$ denotes a Gaussian density with mean $U^{i}$ and covariance $\Sigma$ (line 10). The resulting $\tilde{q}$ is used as the sampling distribution in Algorithm 1.

### III-C Safety Guarantee

We now establish the safety guarantee of the proposed filter.

### Proposition 1

Let $\mathbf{x}_{t}$ be the current state. If $\mathbf{u}_{t}^{\mathrm{safe}}=\mathbf{u}_{t}^{\mathrm{nom}}$, then the proposed filter guarantees safety at time $t$.

### Proof

If $\mathbf{u}_{t}^{\mathrm{safe}}=\mathbf{u}_{t}^{\mathrm{nom}}$, then by Algorithm 1, the filter has stored a control sequence $U_{t+1}^{\mathrm{safe}}$ with negative cost. By and, the trajectory induced by $U_{t+1}^{\mathrm{safe}}$ from $\mathbf{x}_{t+1}$ is safe. Therefore, the proposed filter guarantees safety at time $t$. ∎ However, this argument does not directly apply when $\mathbf{u}_{t}^{\mathrm{safe}}\neq\mathbf{u}_{t}^{\mathrm{nom}}$, i.e., when the nominal input is overridden. In this case, the filter applies the first input of $U_{t}^{\mathrm{safe}}$ and constructs $U_{t+1}^{\mathrm{safe}}$ by shifting $U_{t}^{\mathrm{safe}}$ by one step, as in line 9 of Algorithm 1. To guarantee safety at the next timestep, we must ensure that the shifted sequence can be safely extended. To this end, we define a safe control invariant set.

### Definition 1 (Safe control invariant set)

A set $\mathcal{C}\subseteq\mathcal{X}$ is a safe control invariant set if $\mathbf{x}\notin\mathcal{L},\;\forall\mathbf{x}\in\mathcal{C}$, and for every $\mathbf{x}\in\mathcal{C}$, there exists a control input $\mathbf{u}^{\mathrm{inv}}(\mathbf{x})\in\mathcal{U}$ such that $f(\mathbf{x},\mathbf{u}^{\mathrm{inv}})\in\mathcal{C}.$ For many robotic systems, a decelerating sequence can drive the system to a known safe control invariant set. In the single-robot experiment in Section IV-A, candidate backup sequences are sampled from control sequences that bring the robot to a complete stop at the terminal timestep $H$. Once the robot has stopped, the shifted sequence is extended by appending a terminal input that maintains the stopped state, so that a safe control sequence exists at all subsequent timesteps. This motivates Proposition 2.

### Proposition 2

Let the sampling space be restricted to control sequences whose terminal state lies in $\mathcal{C}$. Suppose there exists a known invariance control law $\mathbf{u}^{\mathrm{inv}}(\mathbf{x})$ such that for any $\mathbf{x}\in\mathcal{C}$, the next state remains in $\mathcal{C}$.

If the filter does not intervene at $t=0$, i.e., $\mathbf{u}_{0}^{\mathrm{safe}}=\mathbf{u}_{0}^{\mathrm{nom}}$, then the filter guarantees safety at all timestep $t\geq 0$.

### Proof

We prove the claim by induction on $t$. By Proposition 1, the condition $\mathbf{u}_{0}^{\mathrm{safe}}=\mathbf{u}_{0}^{\mathrm{nom}}$ implies that the filter guarantees safety at $t=0$. Furthermore, the corresponding safe control sequence $U_{1}^{\mathrm{safe}}$ steers the terminal state into $\mathcal{C}$ by the construction of the sampling space.

For the induction step, assume that at time $t$, the filter guarantees safety with a safe control sequence $U_{t+1}^{\mathrm{safe}}=(\bar{\mathbf{u}}_{t+1},\cdots,\bar{\mathbf{u}}_{t+H})$ whose terminal state $\mathbf{x}_{t+H+1}$ lies in $\mathcal{C}$.

At time $t+1$, if $\mathbf{u}_{t+1}^{\mathrm{safe}}=\mathbf{u}_{t+1}^{\mathrm{nom}}$, by Proposition 1, the filter guarantees safety at time $t+1$ with a safe control sequence whose terminal state lies in $\mathcal{C}$ due to the sampling space. Otherwise, the filter overrides $\mathbf{u}_{t+1}^{\mathrm{nom}}$ and applies $\mathbf{u}_{t+1}^{\mathrm{safe}}=\bar{\mathbf{u}}_{t+1}$. Since the terminal state induced by $U_{t+1}^{\mathrm{safe}}$ lies in $\mathcal{C}$, we can construct a candidate safe sequence $U_{t+2}^{\mathrm{safe}}=(\bar{\mathbf{u}}_{t+2},\cdots,\bar{\mathbf{u}}_{t+H},\mathbf{u}^{\mathrm{inv}}(\mathbf{x}_{t+H+1}))$. Hence, there exists a safe control sequence $U_{t+2}^{\mathrm{safe}}$ that keeps the terminal state in $\mathcal{C}$, and the filter guarantees safety at time $t+1$. ∎

### Remark 1

To ensure all-time safety with a braking-based backup, the horizon $H$ must exceed the stopping time under maximum braking. This allows the filter to drive the system to a safe stationary state within the horizon.

### Remark 2

From the CBF perspective, the cost function can also be defined as where $\gamma\in$ denotes the decay rate. This formulation also guarantees safety, often yields smoother control actions, and is closely related to MPC-CBF.

### III-D Restrictiveness

The proposed safety filter intervenes when the minimum cost among the sampled trajectories is nonnegative. Ideally, the filter should intervene only when every possible control sequence from $\mathbf{x}_{t+1}=f(\mathbf{x}_{t},\mathbf{u}^{\mathrm{nom}}_{t})$ is unsafe, that is, when the minimum cost over the entire control space is nonnegative. Since this quantity cannot be evaluated exactly, the filter relies on $N$ sampled sequences to assess the safety of the nominal input. We derive a probabilistic guarantee on the restrictiveness induced by this finite-sample approximation, based on the scenario approach.

### Theorem 1

Given a restrictiveness parameter $\epsilon\in$ and a confidence parameter $\beta\in$, let the sample size $N$ satisfy If the filter in Algorithm 1 intervenes, i.e., $\mathbf{u}_{t}^{\mathrm{safe}}\neq\mathbf{u}_{t}^{\mathrm{nom}}$, then with probability at least $1-\beta$, the probability of sampling a safe control sequence $U_{t+1}$ from $\tilde{q}_{t+1}$ is at most $\epsilon$:

### Proof

If the filter intervenes, then the minimum sampled cost satisfies $\min_{i}C(\tau^{i}_{t+1})\geq 0$. The problem of finding this minimum cost can be formulated as which is the same form as the scenario optimization problem. Therefore, by Theorem 1, if the sample size $N$ satisfies, then $\Pr_{U_{t+1}\sim\tilde{q}_{t+1}}\!\left(g^{*}-C(\tau_{t+1})>0\right)\leq\epsilon$. If the filter intervenes, then $g^{*}>0$. Hence, By and, this implies. ∎

### Remark 3

The probabilistic guarantee in Theorem 1 holds for any sampling distribution $\tilde{q}_{t+1}$. However, the practical utility of the filter depends on the choice of this distribution. A more accurate approximation of the safety-conditioned posterior, achieved in this paper through the multimodal coverage of SV-MPC, reduces unnecessary interventions by effectively exploring the safe control space.

## EXAMPLES

In this section, we evaluate the proposed safety filter in two examples. We first consider a single-robot obstacle avoidance task to compare the sampling distributions induced by SV-MPC and CEM-based safety filters, and to examine the restrictiveness of the resulting filters. We then apply the proposed method to a multi-vehicle intersection scenario using a reinforcement learning-based nominal controller.

### IV-A Single-Robot Obstacle Avoidance

We demonstrate the proposed safety filter on a system with the following dynamics: where $x$ and $y$ denote the robot position, $\theta$ is the heading angle, and $v\in$ is the speed. The control inputs are the angular velocity $\omega\in[-1.5,1.5]$ and the acceleration $a\in$, with a timestep of $\Delta t=0.1$.

Figure 1: Comparison of closed-loop trajectories obtained under filters based on (a) SV-MPC and (b) CEM.

As shown in Fig. 1, the robot is tasked with reaching the goal position, marked by a purple star, while avoiding the gray obstacles. The robot is depicted as a hollow green circle. To evaluate safety, we define the level function as which is used to compute the cost $C(\tau^{i})$. Here, $d_{\min}$ denotes the minimum distance from the robot position to the obstacle centers, and $r_{\mathrm{robot}}=0.1$ and $r_{\mathrm{obs}}=0.1$ are the radii of the robot and the obstacles, respectively. The minimum-distance operation leads to a nonsmooth and nonconvex level function, which motivates the use of the proposed sampling-based filter. We apply the filter with $N=757$ and $H=20$. The sample size $N=757$ is determined from with $\beta=10^{-16}$ and $\epsilon=0.1$. For the SV-MPC procedure, we set $m=12$, $iters=5$, $\alpha=0.1$, and $\eta=0.25$.

Fig. 1 illustrates the experimental results. Trajectories are shown in red when the filter intervenes and in blue otherwise. As the nominal controller, we use an MPC that seeks only to reach the goal without considering safety constraints. As shown in Fig. 1(a), when the filter uses SV-MPC to construct the sampling distribution, the robot successfully reaches the goal along a safe trajectory. In contrast, when the filter uses CEM, the robot becomes stuck in a deadlock and fails to reach the goal, as shown in Fig. 1(b).

Figure 2: Comparison of samples generated by the filter using (a) SV-MPC and (b) CEM to construct the sampling distribution.

In Fig. 2, we visualize the samples generated by the two filters to better understand this difference. Fig. 2(a) shows samples generated using SV-MPC, which captures the multimodal structure of the safety-conditioned posterior and thereby enables broader exploration of safe trajectories. Fig. 2(b) shows samples generated using a CEM-based distribution constructed with five iterations, which is the same number of iterations used in SV-MPC. This procedure is similar to the distribution update in Algorithm 1 of. Because this distribution is unimodal Gaussian, the resulting samples concentrate around a single mode, leading to limited diversity. As a result, depending on initialization and sampling, the distribution may converge to an unfavorable direction and become stuck in the deadlock shown in Fig. 1(b).

Max. Safe Sample Rate TABLE I: Comparison of Filter Restrictiveness We also examine the restrictiveness of the filters. To this end, we test whether the filter intervenes for all feasible $(x,y)$ positions in the same environment as in Fig. 1 and Fig. 2, while fixing $v=1$ and $\theta=0$. The region is discretized on a grid with resolution $0.01\times 0.01$, and the number of states where the filter intervenes is reported as Num. Intervened in TABLE I. For each intervened state, we then draw an additional 100,000 control sequences from the same sampling distribution used by the filter and compute the fraction of safe samples, i.e., samples with negative cost. The maximum of these fractions over all intervened states is reported as the Max. Safe Sample Rate. This analysis is performed with $H=20$ and $N=379/757/7569$, which correspond to $\epsilon=0.2/0.1/0.01$, respectively, when $\beta=10^{-16}$. The results are summarized in TABLE I.

As shown in TABLE I, the filter based on SV-MPC intervenes less frequently than the filter based on CEM, indicating that SV-MPC better approximates the posterior. In both methods, the number of interventions decreases as the sample size $N$ increases. The safe sample rates are smaller than the corresponding restrictiveness parameter $\epsilon$ in all cases, consistent with the bound $\epsilon$ in Theorem 1.

### IV-B Multi-Vehicle Intersection

This subsection demonstrates the proposed safety filter in a multi-vehicle scenario. We consider an unsignalized intersection consisting of a single-lane four-way crossing with multiple vehicles as shown in Fig. 3. Each vehicle is randomly initialized with an entry time, entry location, and destination. To model the longitudinal motion of each vehicle, we employ double integrator dynamics. The state of vehicle $i$ at time $t$ is defined as $s_{i,t}:=(x_{i,t},y_{i,t},v_{i,t}),$ where $(x,y)$ denotes the position and $v\in$ denotes the velocity. The overall system state is formed by concatenating the states of all vehicles, i.e., $(s_{1,t},s_{2,t},s_{3,t},\cdots)$. The control input for each vehicle is defined as the longitudinal acceleration $a_{i,t}\in[-1.5,1.5]$. The paths of all vehicles toward their destinations are predetermined, and the control action affects only their longitudinal motion along these paths.

As the nominal controller, we adopt the GPT-based Decision Transformer (DT) proposed . This offline reinforcement learning architecture treats the control task as a sequence-modeling problem, mapping historical states and desired returns-to-go to optimal actions. The DT is trained to minimize intersection traversal time while simultaneously reducing inter-vehicle collisions.

We apply the proposed safety filter to this nominal controller. The level function is defined as where $d=\min(d_{12},d_{23},d_{31})$ denotes the minimum pairwise distance between the vehicle polytopes. This piecewise-defined level function is discontinuous, which makes the setting well-suited to the proposed sampling-based approach. The filter uses $N=757$ samples and a horizon $H=67$. For SV-MPC, we set $m=12$, $iters=5$, $\alpha=0.1$ and $\eta=0.15$.

TABLE II: Collision Rate and Filter Intervention Statistics TABLE II summarizes the experimental results for scenarios with 3, 4, and 5 vehicles. We randomly select 100 test cases not included in the training dataset to evaluate the effect of the safety filter. Without the filter, the nominal controller results in collisions in 4, 12, and 15 cases for 3-, 4-, and 5-vehicle settings, respectively. When the filter is applied, all collision cases are eliminated, although it also intervenes in some cases that would not have resulted in collisions.

Figure 3: Visualization of a test case. (a) Vehicle 2 collides with vehicle 3 without the filter. (b) With the filter applied, vehicle 2 avoids the collision with vehicle 3. (c) Velocity profiles of the three vehicles.

We visualize an example test case, from the 3-vehicle setting, in which a collision occurs without the filter. As shown in Fig. 3(a), vehicle 2 collides with vehicle 3 without the filter. With the filter applied, however, vehicle 2 slows down and avoids the collision, as shown in Fig. 3(b). Fig. 3(c) shows the velocity profiles of all three vehicles.

## CONCLUSION

In this paper, we propose a sampling-based safety filter. We establish a finite-sample probabilistic guarantee on restrictiveness via the scenario approach. By adapting SV-MPC to approximate a safety-conditioned posterior over control sequences, the proposed filter can identify safe samples more effectively and thereby reduce unnecessary interventions. Experimental results show that, with a sufficiently long horizon, the proposed method eliminates collisions entirely in both single- and multi-vehicle scenarios while being less restrictive than a CEM-based filter.

The probabilistic restrictiveness guarantee in this work depends on the sampling distribution and therefore cannot serve as an absolute measure of filter restrictiveness. In future work, we plan to relate the notion of filter restrictiveness directly to the backward reachable tube.
