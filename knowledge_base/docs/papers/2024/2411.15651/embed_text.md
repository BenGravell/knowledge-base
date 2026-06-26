## Introduction

Gradient-free optimization techniques are an attractive framework for decision making and motion planning on robotic systems where high-fidelity models may not be differentiable and descent algorithms can get caught in local minima. As a motivating example, we consider nonprehensile manipulation, a setting where a robot uses pushing, pulling, or other means of manipulation without grasping the target object with appendages. This task is challenging for conventional gradient-based optimization because of its hybrid dynamics and sparse reward structure. uct, a variant of \\acmcts, is a powerful gradient-free technique that strategically explores the space of possible future trajectories, with guaranteed convergence to the optimal trajectory as its runtime increases. Although \\acuct is widely applicable to a large class of decision-making problems, its performance is dependent on its computational resources and accumulating enough samples to make an accurate value estimate. With this context, there is clear benefit in reusing past simulations to improve the quality of search and reduce sample complexity. In this work, we propose an efficient sub-tree recycling procedure and characterize the conditions under changing dynamics where tree recycling is not possible and instead must be recomputed from scratch.

### Contributions

We present \\acmpt, a receding horizon tree-based planner that reuses past subtree information, reducing the cost of searching while greatly boosting the quality of solutions. Saving even low-quality trajectories benefits the search by shifting computational effort from re-generating poor solutions to refining high-quality solutions. We demonstrate our proposed method on a nonprehensile manipulation task performed by an autonomous car in simulation and performing in real-time on onboard hardware. We furthermore provide theoretical guarantees on stability and robustness in the face of changing dynamics. Our method automatically discovers high-level behavior, strategically making and breaking contact with a target object while maneuvering around obstacles to push the target to the goal.

Figure 1: Top: Five seconds of real-time generated trees in our hardware experiment, in which the autonomous vehicle testbed pushes a target to a goal region behind an obstacle. On average, 2100 simulated trajectories are grown every 0.2 s. The trees are colored by the time they were grown. Bottom: The proposed tree growth algorithm visualized over four time steps. At each iteration (I - IV), new nodes and branches are added to the tree, and the best first-level child is selected as the next root. In subsequent iterations, older parts of the tree are discarded and new nodes are added.

### I-A Related Work

Our related work spans sampling-based planning, strategies for reusing data from previous iterations, control-aware planning, and nonprehensile manipulation.

### I-A1 Sampling-Based Planners

Sampling-based tree search is common in robotics, with foundational techniques including \\acrrt), RRT\* and variations, and \\acprm as well-tested and theoretically-grounded algorithms. These methods use a local planner to connect states and search for a goal region. The stable sparse RRT variation relaxes the need for a local planner.

In contrast, our method uses tree search algorithms investigated in theoretical computer science, in particular the \\acuct algorithm. \\acuct and variants have been applied in a variety of problem settings, including robotic task planning, motion planning, and active sensing. The advantage of using \\acuct is that our method can plan and execute through hybrid contact dynamics, where the sparse reward and non-smooth contacts make local planning and the restriction to a goal region-objective difficult, therefore limiting the applicability of RRT-based algorithms.

### I-A2 Data Reuse in Receding Horizon Planning

Real-time planning is commonly implemented with a receding horizon approach, also known as model-predictive control, where the solver iteratively computes and follows a finite-horizon trajectory until the process is terminated. In this setting, there are various strategies to reuse information from the previous solver iterations in the current iteration. \\accem and \\acmppi are sampling-based methods that initialize the sampling distribution of the next iteration with the mean of the optimal solution from the previous iteration. This approach, sometimes called "hotstarting", averages many simulated trajectories into a summary statistic and throws away a large amount of information.

Deterministic nonlinear model predictive control uses a similar technique to provide an initial guess for the optimization solver with the optimal solution to the previous iteration. Other works have examined tree reuse and tree correction in a control task and with changing obstacles.

In contrast to other tree reuse strategies, our method saves the entire selected subtree from the previous iteration, leveraging much more information to refine its search. Our experimental results demonstrate that hotstarting with a subtree provides a larger improvement than hotstarting with the optimal solution, validating our intuition about information reuse. In addition, our reuse approach does not require iteration over the entire tree, a time-consuming requirement that limits real-time deployment.

### I-A3 Nonprehensile Manipulation

Although our approach can be applied to a wide class of problems, we focus on nonprehensile manipulation as a motivating example because of its inherent complexity for conventional techniques due to the need to plan through contact. In previous work, the authors demonstrate nonprehensile manipulation with a smoothed contact model. In contrast, we do not make a smooth approximation of the contact model, but plan directly in the underlying sparse reward and hybrid dynamical landscape. Whereas other methods use constraints to maintain contact, our method does not require contact to be maintained: \\acmpt demonstrates high-level behavior, such as backing-up and re-positioning, where the vehicle maneuvers around the object to execute a better push.

Finally, deep reinforcement learning has been applied to nonprehensile manipulation in simulation. However, this family of methods requires a large amount of offline training data and lacks theoretical guarantees of optimality and stability.

## Model Predictive Trees

### II-A Problem Setting

We consider the problem of making decisions over an infinite horizon. For a compact state space $X \subset {\mathbb{R}}^{n}$, compact action space $U \subset {\mathbb{R}}^{m}$, consider a discrete-time control system characterized by known nominal dynamics $F_{\text{nom}}:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{m}}\rightarrow{\mathbb{R}}^{n}}$ and an unknown time-varying disturbance $\mathbf{d}:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{m} \times {\mathbb{Z}}_{\geq 0}}\rightarrow{\mathbb{R}}^{n}}$, with a bounded reward function $R:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{m}}\rightarrow{\lbrack 0,1\rbrack}}$. Given an initial condition $\mathbf{x}_{0}$, the decision-making problem is to maximize the sum of the reward function over an infinite horizon: where $0 \leq \gamma < 1$ is a discount factor and $k$ is the physical time. The problem is a discounted infinite-horizon Markov Decision Process, given by the tuple $\langle X,U,F,R,D,\gamma\rangle$ with $F:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{m}}\rightarrow{\mathbb{R}}^{n}}$ being the nominal dynamics plus disturbance. Manipulation problems are challenging because $F$ is a nondifferentiable function that carries information about the contact between bodies. For example, these dynamics can be modeled with a linear complementarity problem. Here $\mathbf{x}_{\infty} = {\lbrack\mathbf{x}_{1},\mathbf{x}_{2},\ldots\rbrack}$ denotes an infinite sequence of states, and likewise for $\mathbf{u}_{\infty}$.

### II-B Model Predictive Trees (MPT) Method

Our proposed algorithm, specified in Algorithm 1 Method ‣ II Model Predictive Trees ‣ Model Predictive Trees: Sample-Efficient Receding Horizon Planning with Reusable Tree Search"), has two components: a receding horizon \\acuct-based planner and a contraction-theoretic controller. The planner provides a real-time desired trajectory, and the controller provides exponential stability to the desired trajectory. Moreover, contraction-theoretic control guarantees robust stability and provides a framework to analyze the limitations of tree reuse.

As part of \\acmpt, we incorporate a time-varying estimate of the disturbance $\mathbf{d}$ into the planner. By combining with the user's choice of an online estimator (with some possibilities being adaptive control, basis library regression, or Bayesian filtering), \\acmpt uses estimates of the disturbance ${\hat{\mathbf{d}}}_{k}:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{m}}\rightarrow{\mathbb{R}}^{n}}$ to plan over the model: The design and stability of the controller have important implications for the accuracy of subtree reuse under changing dynamics, a connection analyzed in Sec. III.

The planning portion of the \\acmpt algorithm (Algorithm 1 Method ‣ II Model Predictive Trees ‣ Model Predictive Trees: Sample-Efficient Receding Horizon Planning with Reusable Tree Search")) performs sequential tree searches in receding horizon fashion, building an incrementally lengthening desired trajectory. We make a distinction between two time indices: physical time is the passing of time in the real-world and is denoted with $k$, and simulation time is the time index used in the internal simulation of the tree search and is denoted with $j$.

At each physical time step $k = {1,2,\ldots}$, \\acmpt performs a search with the \\acuct algorithm. The search runs a large number of fixed-depth trajectories $\ell = {1,\ldots,L}$, approximating the infinite-horizon problem as a $K$-depth problem with a value estimate $\hat{V}$. The objective of Equation is modified to ${\sum_{k = 1}^{K}{\gamma^{k - 1}R{(\mathbf{x}_{k},\mathbf{u}_{k})}}} + {\hat{V}{(\mathbf{x}_{K})}}$, for $\hat{V}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}_{\geq 0}}$.

The collection of rollouts form a decision tree $\mathtt{T}_{k + 1}$ that holds information about the cumulative reward (in the manner of Eq. ) and number of visits to each node of the tree. The index $k + 1$ of $\mathtt{T}_{k + 1}$ indicates that the root of the decision tree grown at time $k$ has corresponding time $k + 1$.

The exploration-exploitation tradeoff of the \\acuct algorithm guarantees convergence to the optimal solution of a decision-making problem. Exploration encourages the tree search to investigate new areas of the space of trajectories and exploitation encourages a refinement of the search in parts of the space that have yielded high rewards, with sampled trajectories quickly concentrating to high-valued regions of space. The upper confidence bound formula is as follows, where at each parent node p, the value decides through which child node c to further refine the search: where "$.V$" and "$.N$" refer to the cumulative value and number of visits to a node, respectively. Upon completing $L$ \\acuct-guided rollouts, the search returns the best action and resulting state out of the search tree $\mathtt{T}_{k + 1}$.

The key novelty of our algorithm is the reuse of the selected subtree from the previous iteration to hotstart the tree search at the current time step. When an action $\mathbf{u}_{k + 1}$ and corresponding child state $\mathbf{x}_{k + 1}$ are selected as "best" out of tree $\mathtt{T}_{k}$, we trim the search tree $\mathtt{T}_{k}$ at the connection between $\mathbf{x}_{k}$ and $\mathbf{x}_{k + 1}$, keeping the trajectories that start at $\mathbf{x}_{k + 1}$. The subtree reuse procedure is shown in Figure 1. Analyzed in Sec. IV, tree reuse enables a more effective search, through which computational power is spent refining high-quality regions of the space of trajectories, rather than re-searching from scratch.

Running in receding horizon fashion, we budget one time step of computational time to the planner, beginning the next iteration's solve with the predicted state $\mathbf{x}_{k + 1}$ while the controller is following the trajectory from $\mathbf{x}_{k}$ to $\mathbf{x}_{k + 1}$.

To ensure the system arrives near state $\mathbf{x}_{k + 1}$ when the tree rooted there is ready, we compose our planner with a contraction-theoretic controller, denoted $C$ in the pseudocode. This controller provides exponential stability to the desired trajectory produced by the planner. We analyze the stability of our proposed control method and the size of steady-state error as a function of the disturbance $\mathbf{d}$ and the disturbance estimates $\hat{\mathbf{d}}$ in Sec. III.

We additionally use a tree reset condition to close the loop on the planning process (Line 1 Method ‣ II Model Predictive Trees ‣ Model Predictive Trees: Sample-Efficient Receding Horizon Planning with Reusable Tree Search")). This condition limits the drift between the simulated tree state and the physical state, resetting the tree at a threshold to ensure the simulated tree state and physical state do not diverge.

Parameters: τ: Reset threshold def (x0; ⟨X, U, F, R, D, γ⟩, C): // create an initial tree 2 T1′.root = (x0, 0 0, 0); F̂1 = Fnom; for k = 1, …, ∞ do Tk = UCT_search(Tk′; ⟨X, U, F̂k, R, D, γ⟩); // extract desired trajectory Tk.root.best_child = arg max {c.V/c.N} for c in Tk.root.children; xkd = Tk.root.x; ukd = Tk.root.best_child.u; // follow desired trajectory uk + 1 = C(xk, xkd, uk + 1d; F̂k); xk + 1 = rollout(xk, uk + 1); // estimate disturbance ${\hat{\mathbf{d}}}_{k + 1} = {\text{dynamics_estimate}{(\ldots)}}$; ${{\hat{F}}_{k + 1}{(\cdot, \cdot)}} = {{F_{\text{nom}}{(\cdot, \cdot)}} + {{\hat{\mathbf{d}}}_{k + 1}{(\cdot, \cdot)}}}$; // trim tree 3 Tk + 1′.root = Tk.root.best_child; if ∥ Tk + 1′..x − xk + 1 ∥ > τ then Search parameters: L: Number of iterations, b: Branching factor, K: Search depth, ϵ: Exploration constant def (Tk; ⟨X, U, F, R, D, γ⟩): path = [Tk.root]; // rollout 4 next_node = (xj + 1, uj + 1 0, 0); path[−1].children.append(next_node) 6 $\text{next_node} = {\underset{\text{c}\in{\text{path}⁢{\lbrack{-1}\rbrack}}}{\arg ⁢\max}\left\{ {\frac{\text{c}.V}{\text{c}.N} + {\epsilon\sqrt{\frac{\log{(\text{path}{\lbrack - 1\rbrack}.N)}}{\text{c}.N}}}} \right\}}$; 7 path.append(next_node) 9 node.N+ = 1; node.V+ = cumulative_reward; cumulative_reward = γ ⋅ cumulative_reward + R(node.x, node.u) Controller parameters: Q: State cost, R: Input cost def C(xk, xkd, uk + 1d; F): 1 $A = \frac{\partial F}{\partial x}|_{\mathbf{x}_{k}^{d},\mathbf{u}_{k + 1}^{d}}$, $B = \frac{\partial F}{\partial u}|_{\mathbf{x}_{k}^{d},\mathbf{u}_{k + 1}^{d}}$; M = DARE(A, B, Q, R); K = (B⊤MB + R)−1B⊤MA; u = uk + 1d − K(xk − xkd); returnu Algorithm 1 Model Predictive Trees As the disturbance may be drifting over time, past subtree information will have used an old estimate ${\hat{\mathbf{d}}}_{k'}$ that is not up-to-date at the current time $k$. Re-integrating all trajectories in the tree with the up-to-date dynamics information would require a pass over every single node in the tree, removing the intended benefit of reusing the tree.

Our analysis shows that for slowly-changing dynamics, the steady-state tracking error introduced by the use of past estimates is bounded. Furthermore, understanding the connection between dynamics error, steady-state tracking error, and the contraction metric used to stabilize the system allows us to perform informed hyperparameter tuning. We analyze this connection in Sec. III.

### Pseudocode Notes

In Algorithm 1 Method ‣ II Model Predictive Trees ‣ Model Predictive Trees: Sample-Efficient Receding Horizon Planning with Reusable Tree Search"), a node is a tuple $(\mathbf{x},\mathbf{u},\text{children},V,N)$ consisting of a state, the action that led to the state, its list of child nodes, the cumulative value in the subtree below this node, and the total number of visits to this node, respectively. Line 1 Method ‣ II Model Predictive Trees ‣ Model Predictive Trees: Sample-Efficient Receding Horizon Planning with Reusable Tree Search") is taken to be the real-world application of $\mathbf{u}_{k + 1}$. $DARE{(A,B,Q,R)}$ is the Discrete Algebraic Riccati Equation. In Line 1 Method ‣ II Model Predictive Trees ‣ Model Predictive Trees: Sample-Efficient Receding Horizon Planning with Reusable Tree Search"), we put a placeholder for the user's choice of dynamics estimator, which may be a function of time $k$, the state/input $(\mathbf{x}_{k},\mathbf{u}_{k})$, desired state/input $(\mathbf{x}_{k}^{d},\mathbf{u}_{k}^{d})$, or other latent variables.

## Theoretical Results

In this section, we review discrete contraction analysis, derive the robust stability of our controller, and relate the tree reuse to the steady-state error of the proposed controller. Whereas previous work has used contraction theory in planning to stabilize local trajectories to an existing global plan, both in the optimization and learning context, we use contraction theory to analyze the tree reset procedure.

### Notations

All norms are the standard 2-norm unless otherwise specified. $\mathtt{I}_{p}$ denotes the $p \times p$ identity matrix. A square symmetric matrix $A$ is positive definite ($A \succ 0$), positive semidefinite ($A \succeq 0$), negative definite ($A \prec 0$), or negative semidefinite ($A \preceq 0$) if its eigenvalues are positive, nonnegative, negative, or nonpositive, respectively. $\lambda_{\text{max}}{(A)}$ and $\lambda_{\text{min}}{(A)}$ are the largest and smallest eigenvalues of $A$.

### III-A Discrete-Time Contraction Theory

Consider a discrete-time, time-varying dynamical system for time $k \in {\mathbb{Z}}_{\geq 0}$, state $\mathbf{q}:{{\mathbb{Z}}_{\geq 0}\rightarrow{\mathbb{R}}^{n}}$, and a bounded transition function $F:{{{\mathbb{R}}^{n} \times {\mathbb{Z}}_{\geq 0}}\rightarrow{\mathbb{R}}^{n}}$.

We consider the infinitesimal variation of our system: ${{\delta\mathbf{q}_{k + 1}} = {\frac{\partial F}{\partial\mathbf{q}}{(\mathbf{q}_{k},k)}\delta\mathbf{q}_{k}}}.$ We say the system is contracting if all solutions exponentially converge to a single trajectory.

### Theorem 1

A necessary and sufficient condition for to be contracting is the existence of a uniformly positive definite matrix ${M{(\mathbf{q},k)}} = {\Theta{(\mathbf{q},k)}^{\top}\Theta{(\mathbf{q},k)}} \in {\mathbb{R}}^{n \times n}$, called a contraction metric, where $\Theta$ defines a smooth and invertible coordinate transformation ${\delta\mathbf{p}} = {\Theta{(\mathbf{q},k)}\delta\mathbf{q}}$, which ${\forall\mathbf{q}},k$: for constant $0 \leq \alpha < 1$, called the contraction rate.

Contraction analysis also extends to discrete-time systems with disturbances. Consider now a perturbed system:

### Theorem 2

Let the system be a contracting system with metric $M = {\Theta^{\top}\Theta}$, contraction rate $0 \leq \alpha < 1$, and a particular solution $\mathbf{x}_{k}$. If ${\mathcal{L}^{\infty}{({\Theta\sigma})}} < \infty$, then any solution $\mathbf{z}_{k}$ to the perturbed system converges exponentially to an error ball around $\mathbf{x}_{k}$. Furthermore, if we assume $M$ is uniformly bounded as ${\underset{¯}{m}\mathtt{I}_{n}} \preceq M \preceq {\overline{m}\mathtt{I}_{n}}$ and ${\mathcal{L}^{\infty}{(\sigma)}} \leq \overline{\sigma}$, the solutions satisfy, for all $k$:

### Proof

The proof is shown . ∎

### III-B Exponential Convergence to a Desired Trajectory

With the tools of discrete-time contraction, we proceed to analyze the tracking performance of our proposed algorithm. So far in the analysis we have considered dynamical systems without control inputs; we now present a constructive proof for a feedback law that guarantees the contraction of a discrete-time control system: The proposed controller is a locally-linearized Ricatti controller that, under suitable assumptions, stabilizes the system to a desired trajectory $(\mathbf{x}_{k}^{d},\mathbf{u}_{k}^{d})$ for $k \in {\mathbb{Z}}_{\geq 0}$.

### Assumption 1

For positive definite cost matrices $Q$ and $R$, we assume the linearized system at each $k$ given by satisfies $(A,B)$ are stabilizable and $(A,Q^{\frac{1}{2}})$ are observable. This guarantees a unique positive definite solution exists to the Discrete Algebraic Riccati Equation (DARE): Furthemore, we assume the solution to DARE is uniformly bounded over the state space as ${\underset{¯}{m}\mathtt{I}_{n}} \preceq M \preceq {\overline{m}\mathtt{I}_{n}}$.

### Theorem 3

Under Assumption 1, consider the feedback law with $K = {{({R + {B^{\top}MB}})}^{- 1}{({B^{\top}MA})}}$ and $M$ the solution to $DARE{(A,B,Q,R)}$. The feedback law in yields a closed-loop system that contracts to $\mathbf{x}_{k}^{d}$ with metric $M$ and rate $1 > \alpha \geq \sqrt{1 - \frac{\lambda_{\text{min}}{(Q)}}{\overline{m}}}$.

### Proof

Our goal is to show that, for $A_{cl} = {A - {BK}}$, ${{A_{cl}^{\top}MA_{cl}} - {\alpha^{2}M}} \preceq 0$ holds ${\forall\mathbf{x}},k$. Manipulating, Plugging in the definition of $K$, note that ${K^{\top}B^{\top}MBK} = {{K^{\top}B^{\top}MA} - {K^{\top}RK}}$, and consequently, the above becomes As $M$ solves $DARE{(A,B,Q,R)}$, the above becomes where ${{{({1 - \alpha^{2}})}M} - Q - {K^{\top}RK}} \preceq 0$ holds if ${{{({1 - \alpha^{2}})}M} - Q} \preceq 0$, which holds if ${{{({1 - \alpha^{2}})}\overline{m}} - {\lambda_{\text{min}}{(Q)}}} \leq 0$. Thus, the system is contracting with rate $\alpha \geq \sqrt{1 - \frac{\lambda_{\text{min}}{(Q)}}{\overline{m}}}$. ∎

### Remark 1

We note that the linearizations in the controller are made about the desired trajectory $(\mathbf{x}_{k}^{d},\mathbf{u}_{k + 1}^{d})$, but if Assumption 1 holds for the true state and desired input $(\mathbf{x}_{k},\mathbf{u}_{k + 1}^{d})$, we can linearize there.

The proposed feedback law also enjoys a straightforward robustness result. Consider a trajectory $(\mathbf{x}_{k}^{d},\mathbf{u}_{k}^{d})$ that is a solution to the system, and consider the disturbed system:

### Lemma 1

Under Assumption 1, the proposed control law renders the closed-loop system exponentially stable to an error ball around the desired trajectory: where ${\mathcal{L}^{\infty}{(\sigma)}} \leq \overline{\sigma}$ and $\alpha = \sqrt{1 - \frac{\lambda_{\text{min}}{(Q)}}{\overline{m}}}$.

### Proof

The proof follows from the application of Theorem 2 to the closed-loop system in Theorem 3. ∎ We apply this robustness result by analyzing the error introduced by reusing subtrees as the disturbance changes over time. Past subtrees will have been built with an old estimate, introducing error in the difference between the past and current dynamics estimates. We first characterize the effect of a time-varying disturbance.

### Assumption 2

Consider the disturbance $\mathbf{d}$ in Equation. We suppose that $\mathbf{d}$ is "slowly changing": that the temporal difference of $\mathbf{d}$ is bounded. Furthermore, we assume the dynamics estimate available to the algorithm at a time $k$ is $\varepsilon$-accurate. There exists ${\eta,\varepsilon} \in {\mathbb{R}}_{+}$ such that for all $\mathbf{x},\mathbf{u},k$: Under these assumptions, we can quantify the error introduced by reusing incorrect information from the past and understand the effect it has on the tracking error.

### Theorem 4

Under Assumptions 1-2, the steady-state tracking error in \\acmpt is bounded as: for $K$ the depth of the tree search and $\alpha = \sqrt{1 - \frac{\lambda_{\text{min}}{(Q)}}{\overline{m}}}$.

### Proof

At time step $i$, with corresponding dynamics estimate ${\hat{\mathbf{d}}}_{i}$, the trajectories in the search run for simulation time $j = {{i + 1},\ldots,{i + K + 1}}$. As such, the maximal time difference between a dynamics estimate and when a tree branch using that dynamics estimate becomes part of the desired trajectory is $K + 1$ time steps. Therefore, when the physical time is $k = {i + K + 1}$, by Assumption 2, As the desired trajectory at $k = {i + K + 1}$ satisfies the dynamics $\mathbf{x}_{k + 1} = {{F_{\text{nom}}{(\mathbf{x}_{k},\mathbf{u}_{k + 1})}} + {{\hat{\mathbf{d}}}_{i}{(\mathbf{x}_{k},\mathbf{u}_{k + 1})}}}$ and the actual rollout satisfies $\mathbf{x}_{k + 1} = {{F_{\text{nom}}{(\mathbf{x}_{k},\mathbf{u}_{k + 1})}} + {\mathbf{d}{(\mathbf{x}_{k},\mathbf{u}_{k + 1},k)}}}$, the tracking error of following the desired trajectory is: Letting $k\rightarrow\infty$ yields a steady-state tracking error: The expression dictates the limit of tree reuse in the presence of changing dynamics. With this understanding of how the depth of the tree search affects the steady-state tracking error, we can conduct informed parameter design when planning our tree search. For a given steady-state error threshold, a tradeoff exists between how quickly the disturbance is changing (given by $\eta$) and how far in the future we can search with tree reuse.

## Experimental Results and Discussion

We demonstrate \\acmpt on an autonomous vehicle testbed in simulation and hardware.

### IV-A Experimental Setup

In our experiments, our algorithm solves a planar nonprehensile manipulation task, with reward given for pushing a cylindrical object (a barrel) to a goal position. Let the state be $\mathbf{x} = {\lbrack x,y,\theta,x_{o},y_{o}\rbrack}^{\top} \in {\mathbb{R}}^{5}$, where $(x,y)$ is the inertial position of the vehicle in meters, $\theta$ is the heading in radians, and $(x_{o},y_{o})$ is the position of the center of the barrel in meters. The control inputs are $\mathbf{u} = {\lbrack V,\delta\rbrack}^{\top} \in {\mathbb{R}}^{2}$, where $V$ is speed in meters per second and $\delta$ is steering angle in radians, describing an Ackermann car. The nonlinear dynamics are: with $\Delta t$ being the time step and $l$ the wheelbase length. The states $x_{o}$, $y_{o}$ are found by numerically solving the non-penetration constraints with respect to the car geometry in Fig. 2 as a linear complementarity problem (LCP), as.

Figure 2: Left: The states and collision geometry of the simulation model used in the experiments. Right: The autonomous vehicle platform and barrel equipped with sensors for state estimation and compute for running our algorithm.

The reward function is the sum of a nominal reward and a term that increases as the object position approaches $(x_{g},y_{g})$: for normalizing constant $D$. This reward is sparse because when the vehicle is not in contact with the barrel, no improvement in reward is available until first, contact is made and second, the barrel is pushed toward the goal.

The input limits are ${{|V|} \leq {{1m}/s}},{{|\delta|} \leq {0.42{rad}}}$, according to the steering limits of our platform. For \\acmpt (and the \\acuct baseline below), we discretize the action space as ${(V,\delta)} \in {\{{},{({\pm 1},0)},{({\pm 1},{\pm 0.42})}\}}$, sampling uniformly without replacement during tree growth.

### IV-B Baselines

We compare our method against 3 baselines: \\acuct deployed with no tree reuse, referred to as "\\acuct" in our experiments. This algorithm operates in the same way as \\acmpt, but the next root node contains no children from the previous iteration; a cross-entropy motion planner (\\accem) implemented based on with a Gaussian input distribution, ten iterations, and 10% elite particle fraction; and \\accem that hotstarts sampling with the optimal solution of the previous iteration (\\accem-Reuse).

### IV-C Numerical Experiments

In Fig. 3, we compare the performance of MPT against the baselines of UCT, CEM, and CEM-Reuse on a grid of initial states. For ${\theta_{0} = 0},{x_{o,0} = y_{o,0} = 0}$, we vary the initial $x$ and $y$ position of the car over a $4$m $\times$ $4$m space. The goal is to push the barrel from its initial position at $$ to ${(x_{g},y_{g})} = {}$. Here, the value is calculated as the realized (undiscounted) cumulative reward of running each planner in receding horizon fashion for 100 time steps, executing the first proposed action and replanning at each time step.

Figure 3: For a grid of (x, y) initial car positions, we color each point according to the accumulated value of running each algorithm (CEM, CEM-Reuse, UCT, MPT). Purple indicates higher value. These simulations were generated with L = 200, a planning horizon of 10, and a simulation depth of 100. The value shown is averaged across ten runs at each initial condition. Our proposed method, \acmpt, provides the best average cumulative reward of all methods, with a significant improvement over the baseline \acuct method.

The value produced by each method averaged over the state space is summarized below. Information reuse results in a significant improvement between \\acuct and \\acmpt. Whereas \\acuct is outperformed by \\accem, the improvement due to reusing information results in \\acmpt having a $29.9\%$ higher value than \\accem-Reuse, the next best method.

In the task, \\accem methods are unable to reliably find a solution unless the car is initialized close to the barrel. Each method performs most consistently when the vehicle starts directly to the left of the barrel, where driving forward will push the barrel to the goal. mpt is able to find high-valued solutions even when the initial position is far from the barrel. \\acmpt can quickly find these "needle in a haystack" solutions that require a coordinated maneuver to make contact with then push the barrel to the goal. The reuse of the search trees of previous iterations allows \\acmpt to quickly concentrate its search on high-valued trajectories, without wasting computational effort re-searching through low-valued trajectories.

### IV-D Sample Efficiency

We examine sample efficiency by considering one initial condition $\begin{bmatrix} \end{bmatrix}^{\top} = \begin{bmatrix} \end{bmatrix}^{\top}$ and goal position ${(x_{g},y_{g})} = {}$. We deploy each algorithm in receding horizon fashion where at each time step, $L$ simulations are run and the first step of the plan is taken. As before, we evaluate the cumulative reward. We visualize this metric in Fig. 4 vs. the number of simulations $L$.

Figure 4: The value of the trajectory produced by each planning method versus the number of simulations. For each L, 100 trials are run, and the average value is plotted with one standard deviation error bar. Our proposed algorithm (\acmpt) significantly outperforms the baselines and has a less noisy estimate.

Our proposed algorithm greatly outperforms the baselines, with a rapid rise in value, reaching an asymptotic limit at $L = 180$. The competing baselines exhibit a much slower increase in value, highlighting the sample efficiency of \\acmpt. Furthermore, the value estimates produced by the baselines are significantly noisier than that of \\acmpt. We extend the simulation count to see where the average value produced by each baseline draws level to the asymptotic limit found by \\acmpt, with \\acuct not catching up in the considered range.

### IV-E Hardware Results

Figure 5: Our algorithm plans for and executes a solution onboard an autonomous vehicle testbed. I: The trajectory of the vehicle (solid line) and the pushed object (dashed line) are shown, with the planned trajectory in red and the actual trajectory in blue. The tree resets are circled in red. II: An overlay of the trajectory of the vehicle and barrel over the course of the experiment in the Caltech Center for Autonomous Systems and Technologies. III: The states as simulated by the tree (blue) and as measured by the motion capture (orange). The tree reset instances are each shown as a pair of red lines. IV: The number of simulations saved by reusing the tree is shown. On average, one third of the new simulations are carried over to the next planning iteration. Near the end of the experiment, when the optimal behavior is easy to find, the number of reused simulations rises dramatically. The decision trees grown here are highly concentrated to the optimal actions at each depth.

We verify the ability of \\acmpt to be deployed on hardware by implementing our algorithm on the autonomous vehicle testbed shown in Fig. 2. We task \\acmpt to solve the barrel-pushing task in an environment with three obstacles. \\acmpt is able to plan in real time and execute a $12 -$second pushing operation that maneuvers the barrel around the obstacles to the goal position. The trajectory of the vehicle and the barrel around the obstacles are shown in Fig. 5.

Our algorithm is able to plan through high-level behaviors of making and breaking contact with the barrel. Halfway through the experiment, the vehicle stops, backs up, and re-positions itself behind the barrel to make a push around an obstacle. Such a maneuver is only possible if planning through the hybrid dynamics, a distinct advantage of our proposed method. We show that state-of-the-art baselines are either too sample-inefficient or unable to plan through the dynamics, rendering the observed behavior unique to \\acmpt.

At each planning iteration, we check the tree reset condition with $\tau = 0.5$. At three times in the experiment, the tree is reset when the state of the vehicle or barrel diverge from the simulated state. The resets are all triggered by a mismatch in the $\theta$ state or the object position, meaning the dynamics mismatch is occurring in the steering model and contact dynamics. In this task, we use a constant estimated dynamics model, but the real physics of the contact include friction effects, deformation, and other unmodeled dynamics that contribute to the model mismatch, resulting in resets.

In this experiment, our \\acmpt planner is running at $5$ Hz on an onboard NVIDIA Jetson Orin, running approximately 2100 simulations every 0.2 s. We measure the position of our vehicle and the barrel with motion capture. For our numerical and hardware experiments, we use a value estimate $\hat{V} \equiv 0$. If data is available, an option is to train a neural network value estimator, as in related works in tree search.

## Conclusion

We present \\acmpt, a new receding horizon planning framework that reuses a rich set of information from prior solver iterations to solve challenging planning problems. Our theoretical analysis guarantees the stability of our method and robustness to model mismatch, characterizing the limitations of tree reuse. We use our planner to produce solutions in real-time for a challenging nonprehensile manipulation task to push a target barrel through an obstacle field. We demonstrate the performance improvement of our algorithm against state-of-the-art sampling-based planners, isolating the effect of replanning with partial and complete information reuse. Our results suggest information reuse is an important area of study that can provide significant improvement to a wide variety of algorithms and applications.
