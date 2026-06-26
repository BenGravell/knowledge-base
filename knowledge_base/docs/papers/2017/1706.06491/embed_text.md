## Introduction

Reinforcement learning (RL) is a principled mathematical framework for experience-based autonomous learning of control policies. Its trial-and-error learning process is one of the most distinguishing features of RL. Despite many recent advances in RL, a main limitation of current RL algorithms remains its data inefficiency, i.e., the required number of interactions with the environment is impractically high. For example, many RL approaches in problems with low-dimensional state spaces and fairly benign dynamics require thousands of trials to learn. This *data inefficiency* makes learning in real control/robotic systems without task-specific priors impractical and prohibits RL approaches in more challenging scenarios.

A promising way to increase the data efficiency of RL without inserting task-specific prior knowledge is to learn models of the underlying system dynamics. When a good model is available, it can be used as a faithful proxy for the real environment, i.e., good policies can be obtained from the model without additional interactions with the real system. However, modelling the underlying transition dynamics accurately is challenging and inevitably leads to model errors. To account for model errors, it has been proposed to use probabilistic models. By explicitly taking model uncertainty into account, the number of interactions with the real system can be substantially reduced. For example, , the authors use Gaussian processes (GPs) to model the dynamics of the underlying system. The PILCO algorithm propagates uncertainty through time for long-term planning and learns parameters of a feedback policy by means of gradient-based policy search. It achieves an unprecedented data efficiency for learning control policies for from scratch.

While the PILCO algorithm is data efficient, it has few shortcomings: 1) Learning closed-loop feedback policies needs the full planning horizon to stabilise the system, which results in a significant computational burden; 2) It requires us to specify a parametrised policy a priori, often with hundreds of parameters; 3) It cannot handle state constraints; 4) Control constraints are enforced by using a differentiable squashing function that is applied to the RBF policy. This allows PILCO to explicitly take control constraints into account during planning. However, this kind of constraint handling can produce unreliable predictions near constraint boundaries.

In this paper, we develop an RL algorithm that is a) data efficient, b) does not require to look at the full planning horizon, c) handles constraints naturally, d) does not require a parametrised policy, e) is theoretically justified. The key idea is to reformulate the optimal control problem with learned GP models as an equivalent deterministic problem, an idea similar to. This reformulation allows us to exploit Pontryagin's maximum principle to find optimal control signals while handling constraints in a principled way. We propose probabilistic model predictive control (MPC) with learned GP models, while propagating uncertainty through time. The MPC formulation allows to plan ahead for relatively short horizons, which limits the computational burden and allows for infinite-horizon control applications. Our approach can find optimal trajectories in constrained settings, offers an increased robustness to model errors and an unprecedented data efficiency compared to the state of the art.

### Related Work

Model-based RL: A recent survey of model based RL in robotics highlights the importance of models for building adaptable robots. Instead of GP dynamics model with a zero prior mean (as used in this paper) an RBF network and linear mean functions are proposed. This accelerates learning and facilitates transferring a learned model from simulation to a real robot. Even implicit model learning can be beneficial: The UNREAL learner proposed in learns a predictive model for the environment as an auxiliary task, which helps learning.

MPC with GP transition models: GP-based predictive control was used for boiler and building control, but the model uncertainty was discarded. In, the predictive variances were used within a GP-MPC scheme to actively reject periodic disturbances, although not in an RL setting. Similarly, , the authors used a GP prior to model additive noise and model is improved episodically. In, the authors considered MPC problems with GP models, where only the GP's posterior mean was used while ignoring the variance for planning. MPC methods with deterministic models are useful only when model errors and system noise can be neglected in the problem.

Optimal Control: The application of optimal control theory for the models based on GP dynamics employs some structure in the transition model, i.e., there is an explicit assumption of control affinity and linearisation via locally quadratic approximations. The AICO model uses approximate inference with (known) locally linear models. The probabilistic trajectories for model-free RL in are obtained by reformulating the stochastic optimal control problem as KL divergence minimisation. We implicitly linearise the transition dynamic via moment matching approximation.

### Contribution

The contributions of this paper are the following: 1) We propose a new 'deterministic' formulation for probabilistic MPC with learned GP models and uncertainty propagation for long-term planning. 2) This reformulation allows us to apply Pontryagin's Maximum Principle (PMP) for the open-loop planning stage of probabilistic MPC with GPs. Using the PMP we can handle control constraints in a principled fashion while still maintaining necessary conditions for optimality. 3) The proposed algorithm is not only theoretically justified by optimal control theory, but also achieves a state-of-the-art data efficiency in RL while maintaining the probabilistic formulation. 4) Our method can handle state and control constraints while preserving its data efficiency and optimality properties.

## Controller Learning via Probabilistic MPC

We consider a stochastic dynamical system with states ${\mathbf{x}} \in {\mathbb{R}}^{D}$ and admissible controls (actions) ${\mathbf{u}} \in \mathcal{U} \subset {\mathbb{R}}^{U}$, where the state follows Markovian dynamics with an (unknown) transition function $f$ and i.i.d. system noise ${\mathbf{w}} \sim {\mathcal{N}{(\mathbf{0},{\mathbf{Q}})}}$, where ${\mathbf{Q}} = {\text{diag}{(\sigma_{1}^{2},\ldots,\sigma_{D}^{2})}}$. In this paper, we consider an RL setting where we seek control signals ${\mathbf{u}}_{0}^{\ast},\ldots,{\mathbf{u}}_{T - 1}^{\ast}$ that minimise the expected long-term cost where $\Phi{({\mathbf{x}}_{T})}$ is a terminal cost and $\ell{({\mathbf{x}}_{t},{\mathbf{u}}_{t})}$ the stage cost associated with applying control ${\mathbf{u}}_{t}$ in state ${\mathbf{x}}_{t}$. We assume that the initial state is Gaussian distributed, i.e., ${p{({\mathbf{x}}_{0})}} = {\mathcal{N}{({\mathbf{μ}}_{0},\mathbf{\Sigma}_{0})}}$.

For data efficiency, we follow a model-based RL strategy, i.e., we learn a model of the unknown transition function $f$, which we then use to find open-loop^11^1'Open-loop' refers to the fact that the control signals are independent of the state, i.e., there is no state feedback incorporated. optimal controls ${\mathbf{u}}_{0}^{\ast},\ldots,{\mathbf{u}}_{T - 1}^{\ast}$ that minimise. After every application of the control sequence, we update the learned model with the newly acquired experience and re-plan. Section 2.1 summarises the model learning step; Section 2.2 details how to obtain the desired open-loop trajectory.

### Probabilistic Transition Model

We learn a probabilistic model of the unknown underlying dynamics $f$ to be robust to model errors. In particular, we use a Gaussian process (GP) as a prior $p{(f)}$ over plausible transition functions $f$.

A GP is a probabilistic non-parametric model for regression. In a GP, any finite number of function values is jointly Gaussian distributed. A GP is fully specified by a mean function $m{( \cdot )}$ and a covariance function (kernel) $k{( \cdot, \cdot )}$.

The inputs for the dynamics GP are given by tuples ${\overset{\sim}{\mathbf{x}}}_{t}:={({\mathbf{x}}_{t},{\mathbf{u}}_{t})}$, and the corresponding targets are ${\mathbf{x}}_{t + 1}$. We denote the collections of training inputs and targets by $\overset{\sim}{\mathbf{X}},{\mathbf{y}}$, respectively. Furthermore, we assume a Gaussian (RBF, squared exponential) covariance function where $\sigma_{f}^{2}$ is the signal variance and ${\mathbf{L}} = {\text{diag}{(l_{1},\ldots,l_{D + U})}}$ is a diagonal matrix of length-scales $l_{1},\ldots,l_{D + U}$. The GP is trained via the standard procedure of evidence maximisation.

We make the standard assumption that the GPs for each target dimension of the transition function $f:{{{\mathbb{R}}^{D} \times \mathcal{U}}\rightarrow{\mathbb{R}}^{D}}$ are independent. For given hyper-parameters, training inputs $\overset{\sim}{\mathbf{X}}$, training targets $\mathbf{y}$ and a new test input ${\overset{\sim}{\mathbf{x}}}_{\ast}$, the GP yields the predictive distribution ${p{(\left. {f{({\overset{\sim}{\mathbf{x}}}_{\ast})}} \middle| {\overset{\sim}{\mathbf{X}},{\mathbf{y}}} \right.)}} = {\mathcal{N}{(\left. {f{({\overset{\sim}{\mathbf{x}}}_{\ast})}} \middle| {{m{({\overset{\sim}{\mathbf{x}}}_{\ast})}},{\Sigma{({\overset{\sim}{\mathbf{x}}}_{\ast})}}} \right.)}}$, where for all predictive dimensions $d = {1,\ldots,D}$.

### Open-Loop Control

To find the desired open-loop control sequence ${\mathbf{u}}_{0}^{\ast},\ldots,{\mathbf{u}}_{T - 1}^{\ast}$, we follow a two-step procedure proposed . 1) Use the learned GP model to predict the long-term evolution ${p{({\mathbf{x}}_{1})}},\ldots,{{\mathbf{p}}{({\mathbf{x}}_{T})}}$ of the state for a given control sequence ${\mathbf{u}}_{0},\ldots,{\mathbf{u}}_{T - 1}$. 2) Compute the corresponding expected long-term cost and find an open-loop control sequence ${\mathbf{u}}_{0}^{\ast},\ldots,{\mathbf{u}}_{T - 1}^{\ast}$ that minimises the expected long-term cost. In the following, we will detail these steps.

### Long-term Predictions

To obtain the state distributions ${p{({\mathbf{x}}_{1})}},\ldots,{p{({\mathbf{x}}_{T})}}$ for a given control sequence ${\mathbf{u}}_{0},\ldots,{\mathbf{u}}_{T - 1}$, we iteratively predict for ${t = {0,\ldots,{T - 1}}},$ by making a *deterministic* Gaussian approximation to $p{(\left. {\mathbf{x}}_{t + 1} \middle| {\mathbf{u}}_{t} \right.)}$ using moment matching. This approximation has been shown to work well in practice in RL contexts and can be computed in closed form when using the Gaussian kernel.

A key property that we exploit is that moment matching allows us to formulate the uncertainty propagation in as a 'deterministic system function' where ${\mathbf{μ}}_{t},\mathbf{\Sigma}_{t}$ are the mean and the covariance of $p{({\mathbf{x}}_{t})}$. For a deterministic control signal ${\mathbf{u}}_{t}$ we further define the moments of the control-augmented distribution $p{({\mathbf{x}}_{t},{\mathbf{u}}_{t})}$ as such that can equivalently be written as the deterministic system equation

### Optimal Open-Loop Control Sequence

To find the optimal open-loop sequence ${\mathbf{u}}_{0}^{\ast},\ldots,{\mathbf{u}}_{T - 1}^{\ast}$, we first compute the expected long-term cost $J$ in using the Gaussian approximations ${p{({\mathbf{x}}_{1})}},\ldots,{p{({\mathbf{x}}_{T})}}$ obtained via for a given open-loop control sequence ${\mathbf{u}}_{0},\ldots,{\mathbf{u}}_{T - 1}$. Second, we find a control sequence that minimises the expected long-term cost. In the following, we detail these steps.

### Computing the Expected Long-Term Cost

To compute the expected long-term cost, we sum up the expected immediate costs for $t = {0,\ldots,{T - 1}}$. We choose $\ell$, such that this expectation and the partial derivatives $\partial{{{\mathbb{E}}{\lbrack{\ell{({\mathbf{x}}_{t},{\mathbf{u}}_{t})}}\rbrack}}/{\partial{\mathbf{x}}_{t}}}$, $\partial{{{\mathbb{E}}{\lbrack{\ell{({\mathbf{x}}_{t},{\mathbf{u}}_{t})}}\rbrack}}/{\partial{\mathbf{u}}_{t}}}$ can be computed analytically.^22^2Choices for $\ell$ include the standard quadratic (polynomial) cost, but also costs expressed as Fourier series expansions or radial basis function networks with Gaussian basis function.

Similar to, this allows us to define deterministic mappings that map the mean and covariance of $\overset{\sim}{\mathbf{x}}$ onto the corresponding expected costs.

### Remark 1

The open-loop optimisation turns out to be sparse. However, optimisation via the value function or dynamic programming is valid only for unconstrained controls. To address this practical shortcoming, we define Pontryagin's Maximum Principle that allows us to formulate the constrained problem while maintaining the sparsity. We detail this sparse structure for the constrained GP dynamics problem in section 3.

### Feedback Control with MPC

Thus far, we presented a way for efficiently determining an open-loop controller. However, an open-loop controller cannot stabilise the system. Therefore, it is essential to obtain a feedback controller. MPC is a practical framework for this. While interacting with the system MPC determines an $H$-step open-loop control trajectory ${\mathbf{u}}_{0}^{\ast},\ldots,{\mathbf{u}}_{H - 1}^{\ast}$, starting from the current state ${\mathbf{x}}_{t}$^33^3A state distribution $p{({\mathbf{x}}_{t})}$ would work equivalently in our framework.. Only the first control signal ${\mathbf{u}}_{0}^{\ast}$ is applied to the system. When the system transitions to ${\mathbf{x}}_{t + 1}$, we update the GP model with the newly available information, and MPC re-plans ${\mathbf{u}}_{0}^{\ast},\ldots,{\mathbf{u}}_{H - 1}^{\ast}$. This procedure turns an open-loop controller into an implicit closed-loop (feedback) controller by repeated re-planning $H$ steps ahead from the current state. Typically, $H \ll T$, and MPC even allows for $T = \infty$.

In this section, we provided an algorithmic framework for probabilistic MPC with learned GP models for the underlying system dynamics, where we explicitly use the GP's uncertainty for long-term predictions. In the following section, we will justify this using optimal control theory. Additionally, we will discuss how to account for constrained control signals in a principled way without the necessity to warp/squash control signals as .

## Theoretical Justification

Bellman's optimality principle yields a recursive formulation for calculating the total expected cost and gives a sufficient optimality condition. PMP provides the corresponding necessary optimality condition. PMP allows us to compute gradients $\partial{J/{\partial{\mathbf{u}}_{t}}}$ of the expected long-term cost w.r.t. the variables that only depend on variables with neighbouring time index, i.e., $\partial{J/{\partial{\mathbf{u}}_{t}}}$ depends only variables with index $t$ and $t + 1$. Furthermore, it allows us to explicitly deal with constraints on states and controls. In the following, we detail how to solve the optimal control problem (OCP) with PMP for learned GP dynamics and deterministic uncertainty propagation. We additionally provide a computationally efficient way to compute derivatives based on the maximum principle.

To facilitate our discussion we first define some notation. Practical control signals are often constrained. We formally define a class of admissible controls $\mathcal{U}$ that are piecewise continuous functions defined on a compact space $U \subset {\mathbb{R}}^{U}$. This definition is fairly general, and commonly used zero-order-hold or first-order-hold signals satisfy this requirement. Applying admissible controls to the deterministic system dynamics $f_{MM}$ defined in yields a set $\mathcal{Z}$ of admissible controlled trajectories. We define the tuple $(\mathcal{Z},f_{MM},\mathcal{U})$ as our control system. For a single admissible control trajectory ${\mathbf{u}}_{0:{H - 1}}$, there will be a unique trajectory ${\mathbf{z}}_{0:H}$, and the pair $({\mathbf{z}}_{0:H},{\mathbf{u}}_{0:{H - 1}})$ is called an admissible controlled trajectory.

We now define the control-Hamiltonian for this control system as This formulation of the control-Hamiltonian is the centre piece of the Pontryagin's approach to the OCP. The vector ${\mathbf{λ}}_{t + 1}$ can be viewed as a Lagrange multiplier for dynamics constraints associated with the OCP.

To successfully apply PMP we need the system dynamics to have a unique solution for a given control sequence. Traditionally, this is interpreted as the system is 'deterministic'. This interpretation has been considered a limitation of PMP. In this paper, however, we exploit the fact that the moment-matching approximation is a deterministic operator, similar to the projection used in EP. This yields the 'deterministic' system equations, that map moments of the state distribution at time $t$ to moments of the state distribution at time $t + 1$.

### Existence/Uniqueness of a Local Solution

To apply the PMP we need to extend some of the important characteristics of ODEs to our system. In particular, we need to show the existence and uniqueness of a (local) solution to our difference equation.

For existence of a solution we need to satisfy the difference equation point-wise over the entire horizon and for uniqueness we need the system to have only one singularity. For our discrete-time system equation (via the moment-matching approximation) in we have the following

### Lemma 1

The moment matching mapping $f_{MM}$ is Lipschitz continuous for controls defined over a compact set $\mathcal{U}$.

The proof is based on bounding the gradient of $f_{MM}$ and detailed in the supplementary material. Existence and uniqueness of the trajectories for the moment matching difference equation are given by

### Lemma 2

A solution of ${\mathbf{z}}_{t + 1} = {f_{MM}{({\mathbf{z}}_{t},{\mathbf{u}}_{t})}}$ exists and is unique.

### Proof Sketch

Difference equations always yield an answer for a given input. Therefore, a solution trivially exists. Uniqueness directly follows from the Picard-Lindelöf theorem, which we can apply due to Lemma 1. This theorem requires the discrete-time system function to be deterministic (see Appendix B of ). Due to our re-formulation of the system dynamics, this follows directly, such that the ${\mathbf{z}}_{1:T}$ for a given control sequence ${\mathbf{u}}_{0:{T - 1}}$ are unique.

### Pontryagin's Maximum Principle for GP Dynamics

With Lemmas 1 2 and the definition of the control-Hamiltonian 15 we can now state PMP for the control system $({\mathbf{Z}},f_{MM},\mathcal{U})$ as follows:

### Theorem 1

Let $(\mathbf{z}_{t}^{\ast},\mathbf{u}_{t}^{\ast})$, $0 \leq t \leq {H - 1}$ be an admissible controlled trajectory defined over the horizon $H$. If $(\mathbf{z}_{0:H}^{\ast},\mathbf{u}_{0:{H - 1}}^{\ast})$ is optimal, then there exists an ad-joint vector ${\mathbf{λ}}_{t} \in {{\mathbb{R}}^{D} \smallsetminus {\{\mathbf{0}\}}}$ satisfying the following conditions: Ad-joint equation: The ad-joint vector ${\mathbf{λ}}_{t}$ is a solution to the discrete difference equation Transversality condition: At the endpoint the ad-joint vector ${\mathbf{λ}}_{H}$ satisfies Minimum Condition: For $t = {0,\ldots,{H - 1}}$, we have for all ${\mathbf{ν}} \in \mathcal{U}$.

### Remark 2

The minimum condition can be used to find an optimal control. The Hamiltonian is minimised point-wise over the admissible control set $\mathcal{U}$: For every $t = {0,\ldots,{H - 1}}$ we find optimal controls ${\mathbf{u}}_{t}^{\ast} \in {{\arg{\min_{\mathbf{ν}}\mathcal{H}}}{({\mathbf{λ}}_{t + 1},{\mathbf{z}}_{t}^{\ast},{\mathbf{ν}})}}$. The minimisation problem possesses additional variables ${\mathbf{λ}}_{t + 1}$. These variables can be interpreted as Lagrange multipliers for the optimisation. They capture the impact of the control ${\mathbf{u}}_{t}$ over the whole trajectory and, hence, these variables make the optimisation problem sparse. For the GP dynamics we compute the multipliers ${\mathbf{λ}}_{t}$ in closed form, thereby, significantly reducing the computational burden to minimise the expected long-term cost $J$ . We detail this calculation in section 3.3.

### Remark 3

In the optimal control problem, we aim to find an admissible control trajectory that minimizes the cost subject to possibly additional constraints. PMP gives first-order optimality conditions over these admissible controlled trajectories and can be generalised to handle additional state and control constraints.

### Remark 4

The Hamiltonian $\mathcal{H}$ in is constant for unconstrained controls in time-invariant dynamics and equals $0$ everywhere when the final time $H$ is not fixed.

### Remark 5

For linear dynamics the proposed method is a generalisation of iLQG: The moment matching transition $f_{MM}$ implicitly linearises the transition dynamics at each time step, whereas in iLQG an explicit local linear approximation is made. For a linear $f_{MM}$ and a quadratic cost $\ell$ we can write the LQG case as shown in Theorem 1 . If we iterate with successive corrections to the linear approximations we obtain iLQG.

### Efficient Gradient Computation

With the definition of the Hamiltonian $\mathcal{H}$ in we can efficiently calculate the gradient of the expected total cost $J$. For a time horizon $H$ we can write the accumulated cost as the Bellman recursion for $t = {{H - 1},\ldots,0}$. Since the (open-loop) control ${\mathbf{u}}_{t}$ only impacts the future costs via ${\mathbf{z}}_{t + 1} = {f_{MM}{({\mathbf{z}}_{t},{\mathbf{u}}_{t})}}$ the derivative of the total cost with ${\mathbf{u}}_{t}$ is given by Comparing this expression with the definition of the Hamiltonian, we see that if we make the substitution ${\mathbf{λ}}_{t + 1}^{T} = \frac{\partial J_{t + 1}}{\partial{\mathbf{z}}_{t + 1}}$ we obtain This implies that the gradient of the expected long-term cost w.r.t. ${\mathbf{u}}_{t}$ can be efficiently computed using the Hamiltonian. Next we show that the substitution ${\mathbf{λ}}_{t + 1}^{T} = \frac{\partial J_{t + 1}}{\partial{\mathbf{z}}_{t + 1}}$ is valid for the entire horizon $H$. For the terminal cost $\Phi_{MM}{({\mathbf{z}}_{H})}$ this is valid by the transversality condition. For other time steps we differentiate w.r.t. ${\mathbf{z}}_{t}$, which yields which is identical to the ad-joint equation. Hence, in our setting, PMP implies that *gradient descent on the Hamiltonian $\mathcal{H}$ is equivalent to gradient descent on the total cost*.

Algorithmically, in an RL setting, we find the optimal control sequence ${\mathbf{u}}_{0}^{\ast},\ldots,{\mathbf{u}}_{H - 1}^{\ast}$ as follows: For a given initial (random) control sequence ${\mathbf{u}}_{0:{H - 1}}$ we follow the steps described in section 2.2.1 to determine the corresponding trajectory ${\mathbf{z}}_{1:H}$. Additionally, we compute Lagrange multipliers ${\mathbf{λ}}_{t + 1}^{T} = \frac{\partial J_{t + 1}}{\partial{\mathbf{z}}_{t + 1}}$ during the forward propagation. Note that traditionally ad-joint equations are propagated backward to find the multipliers.

Given ${\mathbf{λ}}_{t}$ and a cost function $\ell_{MM}$ we can determine the Hamiltonians $\mathcal{H}_{1:H}$. Then we find a new control sequence ${\mathbf{u}}_{0:{H - 1}}^{\ast}$ via any gradient descent method using.

Return to 1 or exit when converged.

We use Sequential Quadratic Programming (SQP) with BFGS for Hessian updates. The Lagrangian of SQP is a partially separable function. In the PMP, this separation is explicit via the Hamiltonians, i.e., the $\mathcal{H}_{t}$ is a function of variables with index $t$ or $t + 1$. This leads to a block-diagonal Hessian of SQP Lagrangian. The structure can be exploited to approximate the Hessian via block-updates within BFGS

## Experimental Results

We evaluate the quality of our algorithm in two ways: First, we assess whether probabilistic MPC leads to faster learning compared with PILCO, the current state of the art in terms of data efficiency. Second, we assess the impact of state constraints while performing the same task.

We consider two RL benchmark problems: the under-actuated cart-pole-swing-up and the fully actuated double-pendulum swing-up. In both tasks, PILCO is the most data-efficient RL algorithm to date.

(a) Cart-pole with constraint.

(b) Double pendulum with constraint.

Figure 1: State constraints in RL benchmarks. 1(a) The position of the cart is constrained on the left side by a wall. 1(b) The angle of the inner pendulum cannot enter the grey region.

### Under-actuated Cart-Pole Swing-Up

The cart pole system is an under-actuated system with a freely swinging pendulum of $50{cm}$ mounted on a cart. The swing-up and balancing task cannot be solved using a linear model. The cart-pole system state space consists of the position of the cart $x$, cart velocity $\overset{˙}{x}$, the angle $\theta$ of the pendulum and the angular velocity $\overset{˙}{\theta}$. A horizontal force $u \in {\lbrack{- 10},10\rbrack}$ N can be applied to the cart. Starting in a position where the pendulum hangs downwards, the objective is to automatically learn a controller that swings the pendulum up and balances it in the inverted position in the middle of the track.

### Constrained Cart-Pole Swing-Up

For the state-space constraint experiment we place a wall on the track near the target, see Fig. 1(a). The wall is at -70 cm, which, along with force limitations, requires the system to swing from the right side.

### Fully-actuated Double-Pendulum

The double pendulum system is a two-link robot arm (links lengths: $1m$) with two actuators at each joint. The state space consists of 2 angles and 2 angular velocities $\lbrack\theta_{1},\theta_{2},{\overset{˙}{\theta}}_{1},{\overset{˙}{\theta}}_{2}\rbrack$. The torques $u_{1}$ and $u_{2}$ are limited to $\lbrack{- 2},2\rbrack$ Nm. Starting from a position where both links are in a downwards position, the objective is to learn a control strategy that swings the double-pendulum up and balances it in the inverted position.

### Constrained Double-Pendulum

The double-pendulum has a constraint on the angle of the inner pendulum, so that it only has a $340^{\circ}$ motion range, i.e., it cannot spin through, see Fig. 1(b). The constraint blocks all clockwise swing-ups. The system is underpowered, and it has to swing clockwise first for a counter-clockwise swing-up without violating the constraints.

### Trials

The general setting is as follows: All RL algorithms start off with a single short random trajectory, which is used for learning the dynamics model. As in the GP is used to predict state differences ${\mathbf{x}}_{t + 1} - {\mathbf{x}}_{t}$. The learned GP dynamics model is then used to determine a controller based on iterated moment matching, which is then applied to the system, starting from ${\mathbf{x}}_{0} \sim {p{({\mathbf{x}}_{0})}}$. Model learning, controller learning and application of the controller to the system constitute a 'trial'. After each trial, the hyper-parameters of the model are updated with the newly acquired experience and learning continues.

### Baselines

We compare our GP-MPC approach with the following baselines: the PILCO algorithm and a zero-variance GP-MPC algorithm (in the flavour of ) for RL, where the GP's predictive variances are discarded. Due to the lack of exploration, such a zero-variance approach within PILCO (a policy search method) does not learn anything useful as already demonstrated , and we do not include this baseline.

We average over 10 independent experiments, where every algorithm is initialised with the same first (random) trajectory. The performance differences of the RL algorithms are therefore due to different approaches to controller learning and the induced exploration.

### Data Efficiency

(a) Under-actuated cart-pole swing-up.

(b) Fully-actuated double-pendulum swing-up.

Figure 2: Performance of RL algorithms. Error bars represent the standard error. 2(a) Cart-pole; 2(b) Double pendulum. GP-MPC (blue) consistently outperforms PILCO (red) and the zero-variance MPC approach (yellow) in terms of data efficiency. While the zero-variance MPC approach works well on the cart-pole task, it fails in the double-pendulum task. We attribute this to the inability to explore the state space sufficiently well.

(a) Cart-pole with constraint.

(b) Double pendulum with constraint.

Figure 3: Performance with state-space constraints. Error bars represent the standard error. 1(a) Cart-pole; 1(b) Double pendulum.GP-MPC with chance constraints. GP-MPC-Var (blue) is the only method that is able to consistently solve the problem. Expected violations constraint GP-MPC-Mean (yellow) fails in cart-pole. PILCO (red) violates state constraints and struggles to complete the task.

In both benchmark experiments (cart-pole and double pendulum), we use the exact saturating cost , which penalises the Euclidean distance of the tip of the (outer) pendulum from the target position, i.e., we are in a setting in which PILCO performs very well.

Fig. 2(a) shows that both our MPC-based controller (blue) and the zero-variance approach successfully^44^4We define 'success' if the pendulum tip is closer than $8{cm}$ to the target position for ten consecutive time steps. complete the task in fewer trials than the state-of-the-art PILCO method (red). From the repeated trials we see that GP-MPC learns faster and more reliably than PILCO. In particular, GP-MPC and the zero-variance approach can solve the cart-pole task with high probability (90%) after three trials (9 seconds), where the first trial was random. PILCO needs two additional trials. The reason why the zero-variance approach (no model uncertainties) works in an MPC context but not within a policy search setting is that we include every observed state transition immediately in the GP dynamics model, which makes MPC fairly robust to model errors. It even allows for model-based RL with deterministic models in simple settings.

Fig. 2(b) highlights that our proposed GP-MPC approach (yellow) requires on average only six trials ($18s$) of experience to achieve a 90% success rate^55^5The tip of outer pendulum is closer than $22{cm}$ to the target., including the first random trial. PILCO requires four additional trials, whereas the zero-variance MPC approach completely fails in this RL setting. The reason for this failure is that the deterministic predictions with a poor model in this complicated state space do not allow for sufficient exploration. We also observe that GP-MPC is more robust to the variations amongst trials.

In both experiments, our proposed GP-MPC requires only 60% of PILCO's experience, such that we report an unprecedented learning speed for these benchmarks, even with settings for which PILCO performs very well.

We identify two key ingredients that are responsible for the success and learning speed of our approach: the ability to immediately react to observed states by adjusting the long-term plan and augment the training set of the GP model on the fly as soon as a new state transition is observed (hyper-parameters are not updated at every time step). These properties turn out to be crucial in the very early stages of learning when very little information is available. If we ignored the on-the-fly updates of the GP dynamics model, our approach would still successfully learn, although the learning efficiency would be slightly decreased.

### State Constraints

A scenario in which PILCO struggles is a setting with state space constraints. We modify the cart-pole and the double-pendulum tasks to such a setting. Both tasks are symmetric, and we impose state constraints in such a way that only one direction of the swing-up is feasible. For the cart-pole system, we place a wall near the target position of the cart, see Fig. 1(a); the double pendulum has a constraint on the angle of the inner pendulum, so that it only has a $340^{\circ}$ motion range, i.e., it cannot spin through, see Fig. 1(b). These constraints constitute linear constraints on the state.

We use a quadratic cost that penalises the Euclidean distance between the tip of the pendulum and the target. This, along with the 'implicit' linearisation, makes the optimal control problem an 'implicit' QP. If a rollout violates the state constraint we immediately abort that trial and move on to the next trial. We use the same experimental set-up as data efficiency experiments.

The state constraints are implemented as *expected violations*, i.e., ${{\mathbb{E}}{\lbrack{\mathbf{x}}_{t}\rbrack}} < {\mathbf{x}}_{\text{limit}}$ and *chance constraints* ${p{({{\mathbf{x}}_{t} < {\mathbf{x}}_{\text{limit}}})}} \geq 0.95$. Fig. 1(a) shows that our MPC-based controller with chance constraint (blue) successfully completes the task with a small acceptable number of violations, see Table 1. The expected violation approach, which only considers the predicted mean (yellow) fails to complete the task due to repeated constraint violations. PILCO uses its saturating cost (there is little hope for learning with quadratic cost ) and has partial success in completing the task, but it struggles, especially during initial trials due to repeated state violations.

Table 1: State constraint violations. The number of trials that resulted in state constraint violation corresponding to the trial data shown in the the Fig. 3.

One of the key points we observe from the Table 1 is that the incorporation of uncertainty into planning is again crucial for successful learning. If we use only predicted means to determine whether the constraint is violated, learning is not reliably 'safe'. Incorporation of the predictive variance, however, results in significantly fewer constraint violations.

## Conclusion and Discussion

We proposed an algorithm for data-efficient RL that is based on probabilistic MPC with learned transition models using Gaussian processes. By exploiting Pontryagin's maximum principle our algorithm can naturally deal with state and control constraints. Key to this theoretical underpinning of a practical algorithm was the re-formulation of the optimal control problem with uncertainty propagation via moment matching into an deterministic optimal control problem. MPC allows the learned model to be updated immediately, which leads to an increased robustness with respect to model inaccuracies. We provided empirical evidence that our framework is not only theoretically sound, but also extremely data efficient, while being able to learn in settings with hard state constraints.

One of the most critical components of our approach is the incorporation of model uncertainty into modelling and planning. In complex environments, model uncertainty drives targeted exploration. It additionally allows us to account for constraints in a risk-averse way, which is important in the early stages of learning.
