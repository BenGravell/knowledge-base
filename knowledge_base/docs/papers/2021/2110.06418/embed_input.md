<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Stabilizing Dynamical Systems via Policy Gradient Methods

Topics include Policy gradients, Stabilization, Dynamical systems, Linear quadratic regulator, Model-free control, Reinforcement learning, Nonlinear systems.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Shows that direct policy search can be used to find stabilizing controllers without starting from an already-stabilizing policy. The method follows a continuation path through discounted LQR problems, increasing the discount factor until it recovers a stabilizing controller for linear systems and locally for smooth nonlinear systems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Stabilizing an unknown control system is one of the most fundamental problems in control systems engineering. In this paper, we provide a simple, model-free algorithm for stabilizing fully observed dynamical systems. While model-free methods have become increasingly popular in practice due to their simplicity and flexibility, stabilization via direct policy search has received surprisingly little attention. Our algorithm proceeds by solving a series of discounted LQR problems, where the discount factor is gradually increased. We prove that this method efficiently recovers a stabilizing controller for linear systems, and for smooth, nonlinear systems within a neighborhood of their equilibria. Our approach overcomes a significant limitation of prior work, namely the need for a pre-given stabilizing control policy. We empirically evaluate the effectiveness of our approach on common control benchmarks.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Stabilizing an unknown control system is one of the most fundamental problems in control systems engineering. A wide variety of tasks - from maintaining a dynamical system around a desired equilibrium point, to tracking a reference signal (e.g a pilot's input to a plane) - can be recast in terms of stability. More generally, synthesizing an initial stabilizing controller is often a necessary first step towards solving more complex tasks, such as adaptive or robust control design.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we consider the problem of finding a stabilizing controller for an unknown dynamical system via direct policy search methods. We introduce a simple procedure based off policy gradients which provably stabilizes a dynamical system around an equilibrium point. Our algorithm only requires access to a simulator which can return rollouts of the system under different control policies, and can efficiently stabilize both linear and smooth, nonlinear systems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Relative to model-based approaches, model-free procedures, such as policy gradients, have two key advantages: they are conceptually simple to implement, and they are easily adaptable; that is, the same method can be applied in a wide variety of domains without much regard to the intricacies of the underlying dynamics. Due to their simplicity and flexibility, direct policy search methods have become increasingly popular amongst practitioners, especially in settings with complex, nonlinear dynamics which may be challenging to model. In particular, they have served as the main workhorse for recent breakthroughs in reinforcement learning and control.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite their popularity amongst practitioners, model-free approaches for continuous control have only recently started to receive attention from the theory community. While these analyses have begun to map out the computational and statistical tradeoffs that emerge in choosing between model-based and model-free approaches, they all share a common assumption: that the unknown dynamical system in question is stable, or that an initial stabilizing controller is known. As such, they do not address the perhaps more basic question, *how do we arrive at a stabilizing controller in the first place?*

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contributions", "weight": 1.0} -->

We establish a reduction from stabilizing an unknown dynamical system to solving a series of discounted, infinite-horizon LQR problems via policy gradients, for which no knowledge of an initial stable controller is needed. Our approach, which we call *discount annealing*, gradually increases the discount factor and yields a control policy which is near optimal for the undiscounted LQR objective. To the best of our knowledge, our algorithm is the first model-free procedure shown to provably stabilize unknown dynamical systems, thereby solving an open problem from Fazel et al..

<!-- chunk {"id": "body-0009", "role": "body", "section": "Contributions", "weight": 1.0} -->

We begin by studying linear, time-invariant dynamical systems with full state observation and assume access to *inexact* cost and gradient evaluations of the discounted, infinite-horizon LQR cost of a state-feedback controller $K$. Previous analyses (e.g., ) establish how such evaluations can be implemented with access to (finitely many, finite horizon) trajectories sampled from a simulator. We show that our method recovers the controller $K_{\star}$ which is the optimal solution of the *undiscounted* LQR problem in a bounded number of iterations, up to optimization and simulator error. The stability of the resulting $K_{\star}$ is guaranteed by known stability margin results for LQR.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Stabilizing Linear Dynamical Systems", "weight": 1.0} -->

We now present our main results establishing how our algorithm, discount annealing, provably stabilizes linear dynamical systems via a reduction to direct policy search methods. We begin with the following preliminaries on the Linear Quadratic Regulator (LQR).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Stabilizing Nonlinear Dynamical Systems", "weight": 1.0} -->

We now extend the guarantees of the discount annealing algorithm to smooth, nonlinear systems. Whereas our study of linear systems explicitly leveraged the equivalence of discounted costs and damped dynamics, our analysis for nonlinear systems *requires* access to system rollouts under damped dynamics, since the previous equivalence between discounting and damping breaks down in nonlinear settings.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Stabilizing Nonlinear Dynamical Systems", "weight": 1.0} -->

More specifically, in this section, we assume access to a simulator which given a controller $K$, returns trajectories generated according to $\mathbf{x}_{t + 1} = {\sqrt{\gamma}G_{nl}{(\mathbf{x}_{t},{K\mathbf{x}_{t}})}}$ for any damping factor $\gamma \in {(0,1\rbrack}$, where $G_{nl}$ is the transition operator for the nonlinear system. While such trajectories may be infeasible to generate on a physical system, we believe these are reasonable to consider when dynamics are represented using software simulators, as is often the case in practice.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Stabilizing Nonlinear Dynamical Systems", "weight": 1.0} -->

The discount annealing algorithm for nonlinear systems is almost identical to the algorithm for linear systems. It again works by repeatedly solving a series of quadratic cost objectives on the nonlinear dynamics as defined below, and progressively increasing the damping factor $\gamma$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 1 (Local Smoothness)", "weight": 1.0} -->

The transition map $G_{nl}$ is continuously differentiable. Furthermore, there exist ${r_{nl},\beta_{nl}} > 0$ such that for all ${(\mathbf{x},\mathbf{u})} \in {\mathbb{R}}^{d_{x} + d_{u}}$ with ${{\|\mathbf{x}\|} + {\|\mathbf{u}\|}} \leq r_{nl}$, For simplicity, we assume $\beta_{nl} \geq 1$ and $r_{nl} \leq 1$. Using Assumption 1. ‣ 3 Stabilizing Nonlinear Dynamical Systems ‣ Stabilizing Dynamical Systems via Policy Gradient Methods"), we can apply Taylor's theorem to rewrite $G_{nl}$ as its Jacobian linearization around the equilibrium point, plus a nonlinear remainder term.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we evaluate the ability of the discount annealing algorithm to stabilize a simulated nonlinear system. Specifically, we consider the familiar cart-pole, with $d_{x} = 4$ (positions and velocities of the cart and pole), and $d_{u} = 1$ (horizontal force applied to the cart). The goal is to stabilize the system with the pole in the unstable 'upright' equilibrium position. For further details, including the precise dynamics, see Section D.1. The system was simulated in discrete-time with a simple forward Euler discretization, i.e., $\mathbf{x}_{t + 1} = {\mathbf{x}_{t} + {T_{s}{\overset{˙}{\mathbf{x}}}_{t}}}$, where ${\overset{˙}{\mathbf{x}}}_{t}$ is given by the continuous time dynamics, and $T_{s} = 0.05$ (20Hz). Simulations were carried out in PyTorch and run on a single GPU.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Experiments", "weight": 1.0} -->

Setup. The discounted annealing algorithm of Figure 1 was implemented as follows.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Experiments", "weight": 1.0} -->

We used $N = 5000$ and $H = 1000$ in our experiments. For the cost function, we used $Q = {T_{s} \cdot I}$ and $R = T_{s}$. We compute unbiased approximations of the gradients using automatic differentiation on the finite horizon objective $J_{nl}^{(H)}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Experiments", "weight": 1.0} -->

Instead of using SGD updates for policy gradients, we use Adam with a learning rate of $\eta = {0.01/r}$. Furthermore, we replace the policy gradient termination criteria in Step 2 (Eq. 2.2) by instead halting after a fixed number $({M = 200})$ of gradient descent steps. We wish to emphasize that the hyperparameters $(N,H,\eta,M)$ were not optimized for performance. In particular, for $r = 0.1$, we found that as few as $M = 40$ iterations of policy gradient and horizons as short as $H = 400$ were sufficient. Finally, we used an initial discount factor $\gamma_{0} = {0.9 \cdot {\| A_{jac}\|}_{2}^{- 2}}$, where $A_{jac}$ denotes the linearization of the (discrete-time) cart-pole about the vertical equilibrium.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Experiments", "weight": 1.0} -->

Results. We now proceed to discuss the performance of the algorithm, focusing on three main properties of interest: i) the number of iterations of discount annealing required to find a stabilizing controller (that is, increase $\gamma_{t}$ to 1), ii) the maximum radius $r$ of the ball of initial conditions $\mathbf{x}_{0} \sim {r \cdot \mathcal{S}^{d_{x} - 1}}$ for which discount annealing succeeds at stabilizing the system, and iii) the radius $r_{\text{roa}}$ of the largest ball contained within the region of attraction (ROA) for the policy returned by discount annealing. Although the true ROA (the set of all initial conditions such that the closed-loop system converges asymptotically to the equilibrium point) is not necessarily shaped like a ball (as the system is more sensitive to perturbations in the position and velocity of the pole than the cart), we use the term region of attraction radius to refer to the radius of the largest ball contained in the ROA.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Experiments", "weight": 1.0} -->

Concerning (i), discount annealing reliably returned a stabilizing policy in less than 9 iterations. Specifically, over 5 independent trials for each initial radius $r \in {\{ 0.1,0.3,0.5,0.7\}}$ (giving 20 independent trials, in total) the algorithm never required more than 9 iterations to return a stabilizing policy.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Experiments", "weight": 1.0} -->

Concerning (ii), discount annealing reliably stabilized the system for $r \leq 0.7$. For $r \approx 0.75$, we observed trials in which the state of the damped system ($\gamma < 1$) diverged to infinity. For such a rollout, the gradient of the cost is not well-defined, and policy gradient is unable to improve the policy, which prevents discount annealing from finding a stabilizing policy.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Experiments", "weight": 1.0} -->

Concerning (iii), in Table 1 we report the final radius $r_{\text{roa}}$ for the region of attraction of the final controller returned by discount annealing as a function of the training radius $r$. We make the following observations. Foremost, the policy returned by discount annealing extends the radius of the ROA beyond the radius used during training, i.e. $r_{\text{roa}} > r$. Moreover, for each $r >.1$, the $r_{\text{roa}}$ achieved by discount annealing is greater than the $r_{\text{roa}} = 0.703$ achieved by the exact optimal LQR controller *and* the $r_{\text{roa}} = 0.506$ achieved by the exact optimal $\mathcal{H}_{\infty}$ controller for the system's Jacobian linearization (see Table 1).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Experiments", "weight": 1.0} -->

(The $\mathcal{H}_{\infty}$ optimal controller mitigates the effect of worst-case additive state disturbances on the cost; cf. Section D.2 for details).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Experiments", "weight": 1.0} -->

One may hypothesize that this is due to the fact that discount annealing directly operates on the true nonlinear dynamics whereas the other baselines (LQR and $\mathcal{H}_{\infty}$ control), find the optimal controller for an idealized linearization of the dynamics. Indeed, there is evidence to support this hypothesis.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Experiments", "weight": 1.0} -->

That is, as discount annealing increases the discount factor $\gamma$ and the closed-loop trajectories explore regions of the state space where the dynamics are increasingly nonlinear, $K_{\text{pg}}^{\star}$ begins to diverge from $K_{\text{lin}}^{\star}$. Moreover, at the conclusion of discount annealing $K_{\text{pg}}^{\star}{}$ achieves a lower cost, namely \[15.2, 15.4\] vs \[16.5, 16.8\] (here $\lbrack a,b\rbrack$ denotes \[$\min$, $\max$\] over 5 trials) and larger $r_{\text{roa}}$, namely \[0.769, 0.777\] vs \[0.702, 0.703\], than $K_{\text{lin}}^{\star}{}$, suggesting that the method has indeed adapted to the nonlinearity of the system.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experiments", "weight": 1.0} -->

Similar observations as to the behavior of controllers fine tuned via policy gradient methods are predicted by the theoretical results from Qu et al..

<!-- chunk {"id": "body-0027", "role": "body", "section": "Discussion", "weight": 1.5} -->

This works illustrates how one can provably stabilize a broad class of dynamical systems via a simple model-free procedure based off policy gradients. In line with the simplicity and flexibility that have made model-free methods so popular in practice, our algorithm works under relatively weak assumptions and with little knowledge of the underlying dynamics. Furthermore, we solve an open problem from previous work and take a step towards placing model-free methods on more solid theoretical footing. We believe that our results raise a number of interesting questions and directions for future work.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Discussion", "weight": 1.5} -->

In particular, our theoretical analysis states that discount annealing returns a controller whose stability properties are similar to those of the optimal LQR controller for the system's Jacobian linearization. We were therefore quite surprised when in experiments, the resulting controller had a significantly better radius of attraction than the exact optimal LQR and $\mathcal{H}_{\infty}$ controllers for the linearization of the dynamics. It is an interesting and important direction for future work to gain a better understanding of exactly when and how model-free procedures are adaptive to the nonlinearities of the system and improve upon these model-based baselines. Furthermore, for our analysis of nonlinear systems, we require access to damped system trajectories. It would be valuable to understand whether this is indeed necessary or whether our analysis could be extended to work without access to damped trajectories.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Discussion", "weight": 1.5} -->

As a final note, in this work we reduce the problem of stabilizing dynamical systems to running policy gradients on a discounted LQR objective. This choice of reducing to LQR was in part made for simplicity to leverage previous analyses. However, it is possible that overall performance could be improved if rather than reducing to LQR, we instead attempted to run a model-free method that directly tries to optimize a robust control objective (which explicitly deals with uncertainty in the system dynamics). We believe that understanding these tradeoffs in objectives and their relevant sample complexities is an interesting avenue for future inquiry.
