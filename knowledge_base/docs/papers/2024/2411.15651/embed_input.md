<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Model Predictive Trees: Sample-Efficient Receding Horizon Planning with Reusable Tree Search

Topics include Model predictive control, Tree search, Monte Carlo tree search, Receding horizon planning, Motion planning, Robotics, Sample efficiency.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proposes reusing the entire optimal subtree (not just the best trajectory) across receding horizon planning steps, enabling simultaneous refinement toward better solutions and away from worse ones.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present Model Predictive Trees (MPT), a receding horizon tree search algorithm that improves its performance by reusing information efficiently. Whereas existing solvers reuse only the highest-quality trajectory from the previous iteration as a "hotstart", our method reuses the entire optimal subtree, enabling the search to be simultaneously guided away from the low-quality areas and towards the high-quality areas. We characterize the restrictions on tree reuse by analyzing the induced tracking error under time-varying dynamics, revealing a tradeoff between the search depth and the timescale of the changing dynamics. In numerical studies, our algorithm outperforms state-of-the-art sampling-based cross-entropy methods with hotstarting. We demonstrate our planner on an autonomous vehicle testbed performing a nonprehensile manipulation task: pushing a target object through an obstacle field. Code associated with this work will be made available at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Gradient-free optimization techniques are an attractive framework for decision making and motion planning on robotic systems where high-fidelity models may not be differentiable and descent algorithms can get caught in local minima. As a motivating example, we consider nonprehensile manipulation, a setting where a robot uses pushing, pulling, or other means of manipulation without grasping the target object with appendages. This task is challenging for conventional gradient-based optimization because of its hybrid dynamics and sparse reward structure.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

uct, a variant of \\acmcts, is a powerful gradient-free technique that strategically explores the space of possible future trajectories, with guaranteed convergence to the optimal trajectory as its runtime increases. Although \\acuct is widely applicable to a large class of decision-making problems, its performance is dependent on its computational resources and accumulating enough samples to make an accurate value estimate. With this context, there is clear benefit in reusing past simulations to improve the quality of search and reduce sample complexity. In this work, we propose an efficient sub-tree recycling procedure and characterize the conditions under changing dynamics where tree recycling is not possible and instead must be recomputed from scratch.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Contributions", "weight": 1.0} -->

We present \\acmpt, a receding horizon tree-based planner that reuses past subtree information, reducing the cost of searching while greatly boosting the quality of solutions. Saving even low-quality trajectories benefits the search by shifting computational effort from re-generating poor solutions to refining high-quality solutions. We demonstrate our proposed method on a nonprehensile manipulation task performed by an autonomous car in simulation and performing in real-time on onboard hardware. We furthermore provide theoretical guarantees on stability and robustness in the face of changing dynamics. Our method automatically discovers high-level behavior, strategically making and breaking contact with a target object while maneuvering around obstacles to push the target to the goal.

<!-- chunk {"id": "body-0007", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

Our related work spans sampling-based planning, strategies for reusing data from previous iterations, control-aware planning, and nonprehensile manipulation.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-A1 Sampling-Based Planners", "weight": 1.0} -->

Sampling-based tree search is common in robotics, with foundational techniques including \\acrrt), RRT\* and variations, and \\acprm as well-tested and theoretically-grounded algorithms. These methods use a local planner to connect states and search for a goal region. The stable sparse RRT variation relaxes the need for a local planner.

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-A1 Sampling-Based Planners", "weight": 1.0} -->

In contrast, our method uses tree search algorithms investigated in theoretical computer science, in particular the \\acuct algorithm. \\acuct and variants have been applied in a variety of problem settings, including robotic task planning, motion planning, and active sensing. The advantage of using \\acuct is that our method can plan and execute through hybrid contact dynamics, where the sparse reward and non-smooth contacts make local planning and the restriction to a goal region-objective difficult, therefore limiting the applicability of RRT-based algorithms.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-A2 Data Reuse in Receding Horizon Planning", "weight": 1.0} -->

Real-time planning is commonly implemented with a receding horizon approach, also known as model-predictive control, where the solver iteratively computes and follows a finite-horizon trajectory until the process is terminated. In this setting, there are various strategies to reuse information from the previous solver iterations in the current iteration. \\accem and \\acmppi are sampling-based methods that initialize the sampling distribution of the next iteration with the mean of the optimal solution from the previous iteration. This approach, sometimes called "hotstarting", averages many simulated trajectories into a summary statistic and throws away a large amount of information.

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-A2 Data Reuse in Receding Horizon Planning", "weight": 1.0} -->

Deterministic nonlinear model predictive control uses a similar technique to provide an initial guess for the optimization solver with the optimal solution to the previous iteration. Other works have examined tree reuse and tree correction in a control task and with changing obstacles.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-A2 Data Reuse in Receding Horizon Planning", "weight": 1.0} -->

In contrast to other tree reuse strategies, our method saves the entire selected subtree from the previous iteration, leveraging much more information to refine its search. Our experimental results demonstrate that hotstarting with a subtree provides a larger improvement than hotstarting with the optimal solution, validating our intuition about information reuse. In addition, our reuse approach does not require iteration over the entire tree, a time-consuming requirement that limits real-time deployment.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-A3 Nonprehensile Manipulation", "weight": 1.0} -->

Although our approach can be applied to a wide class of problems, we focus on nonprehensile manipulation as a motivating example because of its inherent complexity for conventional techniques due to the need to plan through contact. In previous work, the authors demonstrate nonprehensile manipulation with a smoothed contact model. In contrast, we do not make a smooth approximation of the contact model, but plan directly in the underlying sparse reward and hybrid dynamical landscape. Whereas other methods use constraints to maintain contact, our method does not require contact to be maintained: \\acmpt demonstrates high-level behavior, such as backing-up and re-positioning, where the vehicle maneuvers around the object to execute a better push.

<!-- chunk {"id": "body-0014", "role": "body", "section": "I-A3 Nonprehensile Manipulation", "weight": 1.0} -->

Finally, deep reinforcement learning has been applied to nonprehensile manipulation in simulation. However, this family of methods requires a large amount of offline training data and lacks theoretical guarantees of optimality and stability.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Problem Setting", "weight": 1.0} -->

We consider the problem of making decisions over an infinite horizon.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Problem Setting", "weight": 1.0} -->

where $0 \leq \gamma < 1$ is a discount factor and $k$ is the physical time. The problem is a discounted infinite-horizon Markov Decision Process, given by the tuple $\langle X,U,F,R,D,\gamma\rangle$ with $F:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{m}}\rightarrow{\mathbb{R}}^{n}}$ being the nominal dynamics plus disturbance. Manipulation problems are challenging because $F$ is a nondifferentiable function that carries information about the contact between bodies. For example, these dynamics can be modeled with a linear complementarity problem. Here $\mathbf{x}_{\infty} = {\lbrack\mathbf{x}_{1},\mathbf{x}_{2},\ldots\rbrack}$ denotes an infinite sequence of states, and likewise for $\mathbf{u}_{\infty}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Model Predictive Trees (MPT) Method", "weight": 1.0} -->

Our proposed algorithm, specified in Algorithm Method ‣ II Model Predictive Trees ‣ Model Predictive Trees: Sample-Efficient Receding Horizon Planning with Reusable Tree Search"), has two components: a receding horizon \\acuct-based planner and a contraction-theoretic controller. The planner provides a real-time desired trajectory, and the controller provides exponential stability to the desired trajectory. Moreover, contraction-theoretic control guarantees robust stability and provides a framework to analyze the limitations of tree reuse.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Model Predictive Trees (MPT) Method", "weight": 1.0} -->

As part of \\acmpt, we incorporate a time-varying estimate of the disturbance $\mathbf{d}$ into the planner.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Model Predictive Trees (MPT) Method", "weight": 1.0} -->

The design and stability of the controller have important implications for the accuracy of subtree reuse under changing dynamics, a connection analyzed in Sec. III.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B Model Predictive Trees (MPT) Method", "weight": 1.0} -->

The planning portion of the \\acmpt algorithm ) performs sequential tree searches in receding horizon fashion, building an incrementally lengthening desired trajectory. We make a distinction between two time indices: physical time is the passing of time in the real-world and is denoted with $k$, and simulation time is the time index used in the internal simulation of the tree search and is denoted with $j$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B Model Predictive Trees (MPT) Method", "weight": 1.0} -->

At each physical time step $k = {1,2,\ldots}$, \\acmpt performs a search with the \\acuct algorithm. The search runs a large number of fixed-depth trajectories $\ell = {1,\ldots,L}$, approximating the infinite-horizon problem as a $K$-depth problem with a value estimate $\hat{V}$. The objective of Equation is modified to ${\sum_{k = 1}^{K}{\gamma^{k - 1}R{(\mathbf{x}_{k},\mathbf{u}_{k})}}} + {\hat{V}{(\mathbf{x}_{K})}}$, for $\hat{V}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}_{\geq 0}}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B Model Predictive Trees (MPT) Method", "weight": 1.0} -->

The collection of rollouts form a decision tree $\mathtt{T}_{k + 1}$ that holds information about the cumulative reward (in the manner of Eq. ) and number of visits to each node of the tree. The index $k + 1$ of $\mathtt{T}_{k + 1}$ indicates that the root of the decision tree grown at time $k$ has corresponding time $k + 1$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-B Model Predictive Trees (MPT) Method", "weight": 1.0} -->

The exploration-exploitation tradeoff of the \\acuct algorithm guarantees convergence to the optimal solution of a decision-making problem. Exploration encourages the tree search to investigate new areas of the space of trajectories and exploitation encourages a refinement of the search in parts of the space that have yielded high rewards, with sampled trajectories quickly concentrating to high-valued regions of space.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-B Model Predictive Trees (MPT) Method", "weight": 1.0} -->

where "$.V$" and "$.N$" refer to the cumulative value and number of visits to a node, respectively. Upon completing $L$ \\acuct-guided rollouts, the search returns the best action and resulting state out of the search tree $\mathtt{T}_{k + 1}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-B Model Predictive Trees (MPT) Method", "weight": 1.0} -->

The key novelty of our algorithm is the reuse of the selected subtree from the previous iteration to hotstart the tree search at the current time step. When an action $\mathbf{u}_{k + 1}$ and corresponding child state $\mathbf{x}_{k + 1}$ are selected as "best" out of tree $\mathtt{T}_{k}$, we trim the search tree $\mathtt{T}_{k}$ at the connection between $\mathbf{x}_{k}$ and $\mathbf{x}_{k + 1}$, keeping the trajectories that start at $\mathbf{x}_{k + 1}$. The subtree reuse procedure is shown in Figure. Analyzed in Sec. IV, tree reuse enables a more effective search, through which computational power is spent refining high-quality regions of the space of trajectories, rather than re-searching from scratch.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-B Model Predictive Trees (MPT) Method", "weight": 1.0} -->

Running in receding horizon fashion, we budget one time step of computational time to the planner, beginning the next iteration's solve with the predicted state $\mathbf{x}_{k + 1}$ while the controller is following the trajectory from $\mathbf{x}_{k}$ to $\mathbf{x}_{k + 1}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-B Model Predictive Trees (MPT) Method", "weight": 1.0} -->

To ensure the system arrives near state $\mathbf{x}_{k + 1}$ when the tree rooted there is ready, we compose our planner with a contraction-theoretic controller, denoted $C$ in the pseudocode. This controller provides exponential stability to the desired trajectory produced by the planner. We analyze the stability of our proposed control method and the size of steady-state error as a function of the disturbance $\mathbf{d}$ and the disturbance estimates $\hat{\mathbf{d}}$ in Sec. III.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-B Model Predictive Trees (MPT) Method", "weight": 1.0} -->

We additionally use a tree reset condition to close the loop on the planning process ). This condition limits the drift between the simulated tree state and the physical state, resetting the tree at a threshold to ensure the simulated tree state and physical state do not diverge.

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-B Model Predictive Trees (MPT) Method", "weight": 1.0} -->

Parameters: τ: Reset threshold def (x0;⟨X, U, F, R, D, γ⟩,C): // create an initial tree 2 T1′.root = (x0,0 0,0); F̂1 = Fnom; for k = 1, …, ∞ do Tk = UCT_search(Tk′;⟨X, U, F̂k, R, D, γ⟩); // extract desired trajectory Tk.root.best_child = arg max {c.V/c.N} for c in Tk.root.children; xkd = Tk.root.x; ukd = Tk.root.best_child.u; // follow desired trajectory uk + 1 = C(xk,xkd,uk + 1d;F̂k); xk + 1 = rollout(xk,uk + 1); // estimate disturbance ${\hat{\mathbf{d}}}_{k + 1} = {\text{dynamics\_estimate}{(\ldots)}}$; ${{\hat{F}}_{k +

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-B Model Predictive Trees (MPT) Method", "weight": 1.0} -->

1}{( \cdot, \cdot )}} = {{F_{\text{nom}}{( \cdot, \cdot )}} + {{\hat{\mathbf{d}}}_{k + 1}{( \cdot, \cdot )}}}$; // trim tree 3 Tk + 1′.root = Tk.root.best_child; if ∥ Tk + 1′..x − xk + 1 ∥ &gt; τ then Search parameters: L: Number of iterations, b: Branching factor, K: Search depth, ϵ: Exploration constant def (Tk;⟨X, U, F, R, D, γ⟩): path = [Tk.root]; // rollout 4 next_node = (xj + 1,uj + 1 0,0); path[−1].children.append(next_node) 6 $\text{next\_node} =

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-B Model Predictive Trees (MPT) Method", "weight": 1.0} -->

As the disturbance may be drifting over time, past subtree information will have used an old estimate ${\hat{\mathbf{d}}}_{k^{\prime}}$ that is not up-to-date at the current time $k$. Re-integrating all trajectories in the tree with the up-to-date dynamics information would require a pass over every single node in the tree, removing the intended benefit of reusing the tree.

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-B Model Predictive Trees (MPT) Method", "weight": 1.0} -->

Our analysis shows that for slowly-changing dynamics, the steady-state tracking error introduced by the use of past estimates is bounded. Furthermore, understanding the connection between dynamics error, steady-state tracking error, and the contraction metric used to stabilize the system allows us to perform informed hyperparameter tuning. We analyze this connection in Sec. III.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Pseudocode Notes", "weight": 1.0} -->

In Algorithm Method ‣ II Model Predictive Trees ‣ Model Predictive Trees: Sample-Efficient Receding Horizon Planning with Reusable Tree Search"), a node is a tuple $(\mathbf{x},\mathbf{u},\text{children},V,N)$ consisting of a state, the action that led to the state, its list of child nodes, the cumulative value in the subtree below this node, and the total number of visits to this node, respectively. Line Method ‣ II Model Predictive Trees ‣ Model Predictive Trees: Sample-Efficient Receding Horizon Planning with Reusable Tree Search") is taken to be the real-world application of $\mathbf{u}_{k + 1}$. $DARE{(A,B,Q,R)}$ is the Discrete Algebraic Riccati Equation.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Pseudocode Notes", "weight": 1.0} -->

In Line Method ‣ II Model Predictive Trees ‣ Model Predictive Trees: Sample-Efficient Receding Horizon Planning with Reusable Tree Search"), we put a placeholder for the user's choice of dynamics estimator, which may be a function of time $k$, the state/input $(\mathbf{x}_{k},\mathbf{u}_{k})$, desired state/input $(\mathbf{x}_{k}^{d},\mathbf{u}_{k}^{d})$, or other latent variables.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Theoretical Results", "weight": 1.0} -->

In this section, we review discrete contraction analysis, derive the robust stability of our controller, and relate the tree reuse to the steady-state error of the proposed controller. Whereas previous work has used contraction theory in planning to stabilize local trajectories to an existing global plan, both in the optimization and learning context, we use contraction theory to analyze the tree reset procedure.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Notations", "weight": 1.0} -->

All norms are the standard 2-norm unless otherwise specified. $\mathtt{I}_{p}$ denotes the $p \times p$ identity matrix. A square symmetric matrix $A$ is positive definite ($A \succ 0$), positive semidefinite ($A \succeq 0$), negative definite ($A \prec 0$), or negative semidefinite ($A \preceq 0$) if its eigenvalues are positive, nonnegative, negative, or nonpositive, respectively. $\lambda_{\text{max}}{(A)}$ and $\lambda_{\text{min}}{(A)}$ are the largest and smallest eigenvalues of $A$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-A Discrete-Time Contraction Theory", "weight": 1.0} -->

Consider a discrete-time, time-varying dynamical system

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-A Discrete-Time Contraction Theory", "weight": 1.0} -->

We consider the infinitesimal variation of our system: ${{\delta\mathbf{q}_{k + 1}} = {\frac{\partial F}{\partial\mathbf{q}}{(\mathbf{q}_{k},k)}\delta\mathbf{q}_{k}}}.$ We say the system is contracting if all solutions exponentially converge to a single trajectory.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-B Exponential Convergence to a Desired Trajectory", "weight": 1.0} -->

With the tools of discrete-time contraction, we proceed to analyze the tracking performance of our proposed algorithm.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-B Exponential Convergence to a Desired Trajectory", "weight": 1.0} -->

The proposed controller is a locally-linearized Ricatti controller that, under suitable assumptions, stabilizes the system to a desired trajectory $(\mathbf{x}_{k}^{d},\mathbf{u}_{k}^{d})$ for $k \in {\mathbb{Z}}_{\geq 0}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

For positive definite cost matrices $Q$ and $R$, we assume the linearized system at each $k$ given by

<!-- chunk {"id": "body-0042", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

satisfies $(A,B)$ are stabilizable and $(A,Q^{\frac{1}{2}})$ are observable.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Furthemore, we assume the solution to DARE is uniformly bounded over the state space as ${\underset{¯}{m}\mathtt{I}_{n}} \preceq M \preceq {\overline{m}\mathtt{I}_{n}}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Remark 1", "weight": 1.0} -->

We note that the linearizations in the controller are made about the desired trajectory $(\mathbf{x}_{k}^{d},\mathbf{u}_{k + 1}^{d})$, but if Assumption holds for the true state and desired input $(\mathbf{x}_{k},\mathbf{u}_{k + 1}^{d})$, we can linearize there.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The proposed feedback law also enjoys a straightforward robustness result.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Consider the disturbance $\mathbf{d}$ in Equation. We suppose that $\mathbf{d}$ is "slowly changing": that the temporal difference of $\mathbf{d}$ is bounded. Furthermore, we assume the dynamics estimate available to the algorithm at a time $k$ is $\varepsilon$-accurate.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Under these assumptions, we can quantify the error introduced by reusing incorrect information from the past and understand the effect it has on the tracking error.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Experimental Results and Discussion", "weight": 1.0} -->

We demonstrate \\acmpt on an autonomous vehicle testbed in simulation and hardware.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-A Experimental Setup", "weight": 1.0} -->

In our experiments, our algorithm solves a planar nonprehensile manipulation task, with reward given for pushing a cylindrical object (a barrel) to a goal position. Let the state be $\mathbf{x} = {\lbrack x,y,\theta,x_{o},y_{o}\rbrack}^{\top} \in {\mathbb{R}}^{5}$, where $(x,y)$ is the inertial position of the vehicle in meters, $\theta$ is the heading in radians, and $(x_{o},y_{o})$ is the position of the center of the barrel in meters. The control inputs are $\mathbf{u} = {\lbrack V,\delta\rbrack}^{\top} \in {\mathbb{R}}^{2}$, where $V$ is speed in meters per second and $\delta$ is steering angle in radians, describing an Ackermann car.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-A Experimental Setup", "weight": 1.0} -->

with $\Delta t$ being the time step and $l$ the wheelbase length. The states $x_{o}$, $y_{o}$ are found by numerically solving the non-penetration constraints with respect to the car geometry in Fig. as a linear complementarity problem (LCP), as.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-A Experimental Setup", "weight": 1.0} -->

for normalizing constant $D$. This reward is sparse because when the vehicle is not in contact with the barrel, no improvement in reward is available until first, contact is made and second, the barrel is pushed toward the goal.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-A Experimental Setup", "weight": 1.0} -->

The input limits are ${{|V|} \leq {{1m}/s}},{{|\delta|} \leq {0.42{rad}}}$, according to the steering limits of our platform. For \\acmpt (and the \\acuct baseline below), we discretize the action space as ${(V,\delta)} \in {\{{},{({\pm 1},0)},{({\pm 1},{\pm 0.42})}\}}$, sampling uniformly without replacement during tree growth.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-B Baselines", "weight": 1.0} -->

We compare our method against 3 baselines: \\acuct deployed with no tree reuse, referred to as "\\acuct" in our experiments. This algorithm operates in the same way as \\acmpt, but the next root node contains no children from the previous iteration; a cross-entropy motion planner (\\accem) implemented based with a Gaussian input distribution, ten iterations, and 10% elite particle fraction; and \\accem that hotstarts sampling with the optimal solution of the previous iteration (\\accem-Reuse).

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-C Numerical Experiments", "weight": 1.0} -->

In Fig., we compare the performance of MPT against the baselines of UCT, CEM, and CEM-Reuse on a grid of initial states. For ${\theta_{0} = 0},{x_{o,0} = y_{o,0} = 0}$, we vary the initial $x$ and $y$ position of the car over a $4$m $\times$ $4$m space. The goal is to push the barrel from its initial position at $$ to ${(x_{g},y_{g})} = {}$. Here, the value is calculated as the realized (undiscounted) cumulative reward of running each planner in receding horizon fashion for 100 time steps, executing the first proposed action and replanning at each time step.

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-C Numerical Experiments", "weight": 1.0} -->

The value produced by each method averaged over the state space is summarized below. Information reuse results in a significant improvement between \\acuct and \\acmpt. Whereas \\acuct is outperformed by \\accem, the improvement due to reusing information results in \\acmpt having a $29.9\%$ higher value than \\accem-Reuse, the next best method.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-C Numerical Experiments", "weight": 1.0} -->

In the task, \\accem methods are unable to reliably find a solution unless the car is initialized close to the barrel. Each method performs most consistently when the vehicle starts directly to the left of the barrel, where driving forward will push the barrel to the goal.

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-C Numerical Experiments", "weight": 1.0} -->

mpt is able to find high-valued solutions even when the initial position is far from the barrel. \\acmpt can quickly find these "needle in a haystack" solutions that require a coordinated maneuver to make contact with then push the barrel to the goal. The reuse of the search trees of previous iterations allows \\acmpt to quickly concentrate its search on high-valued trajectories, without wasting computational effort re-searching through low-valued trajectories.

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-D Sample Efficiency", "weight": 1.0} -->

We examine sample efficiency by considering one initial condition $\begin{bmatrix}
\end{bmatrix}^{\top} = \begin{bmatrix}
\end{bmatrix}^{\top}$ and goal position ${(x_{g},y_{g})} = {}$. We deploy each algorithm in receding horizon fashion where at each time step, $L$ simulations are run and the first step of the plan is taken. As before, we evaluate the cumulative reward. We visualize this metric in Fig. vs. the number of simulations $L$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-D Sample Efficiency", "weight": 1.0} -->

Our proposed algorithm greatly outperforms the baselines, with a rapid rise in value, reaching an asymptotic limit at $L = 180$. The competing baselines exhibit a much slower increase in value, highlighting the sample efficiency of \\acmpt. Furthermore, the value estimates produced by the baselines are significantly noisier than that of \\acmpt. We extend the simulation count to see where the average value produced by each baseline draws level to the asymptotic limit found by \\acmpt, with \\acuct not catching up in the considered range.

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-E Hardware Results", "weight": 1.0} -->

We verify the ability of \\acmpt to be deployed on hardware by implementing our algorithm on the autonomous vehicle testbed shown in Fig.. We task \\acmpt to solve the barrel-pushing task in an environment with three obstacles. \\acmpt is able to plan in real time and execute a $12 -$second pushing operation that maneuvers the barrel around the obstacles to the goal position. The trajectory of the vehicle and the barrel around the obstacles are shown in Fig..

<!-- chunk {"id": "body-0061", "role": "body", "section": "IV-E Hardware Results", "weight": 1.0} -->

Our algorithm is able to plan through high-level behaviors of making and breaking contact with the barrel. Halfway through the experiment, the vehicle stops, backs up, and re-positions itself behind the barrel to make a push around an obstacle. Such a maneuver is only possible if planning through the hybrid dynamics, a distinct advantage of our proposed method. We show that state-of-the-art baselines are either too sample-inefficient or unable to plan through the dynamics, rendering the observed behavior unique to \\acmpt.

<!-- chunk {"id": "body-0062", "role": "body", "section": "IV-E Hardware Results", "weight": 1.0} -->

At each planning iteration, we check the tree reset condition with $\tau = 0.5$. At three times in the experiment, the tree is reset when the state of the vehicle or barrel diverge from the simulated state. The resets are all triggered by a mismatch in the $\theta$ state or the object position, meaning the dynamics mismatch is occurring in the steering model and contact dynamics. In this task, we use a constant estimated dynamics model, but the real physics of the contact include friction effects, deformation, and other unmodeled dynamics that contribute to the model mismatch, resulting in resets.

<!-- chunk {"id": "body-0063", "role": "body", "section": "IV-E Hardware Results", "weight": 1.0} -->

In this experiment, our \\acmpt planner is running at $5$ Hz on an onboard NVIDIA Jetson Orin, running approximately 2100 simulations every 0.2 s. We measure the position of our vehicle and the barrel with motion capture. For our numerical and hardware experiments, we use a value estimate $\hat{V} \equiv 0$. If data is available, an option is to train a neural network value estimator, as in related works in tree search.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We present \\acmpt, a new receding horizon planning framework that reuses a rich set of information from prior solver iterations to solve challenging planning problems. Our theoretical analysis guarantees the stability of our method and robustness to model mismatch, characterizing the limitations of tree reuse. We use our planner to produce solutions in real-time for a challenging nonprehensile manipulation task to push a target barrel through an obstacle field. We demonstrate the performance improvement of our algorithm against state-of-the-art sampling-based planners, isolating the effect of replanning with partial and complete information reuse. Our results suggest information reuse is an important area of study that can provide significant improvement to a wide variety of algorithms and applications.
