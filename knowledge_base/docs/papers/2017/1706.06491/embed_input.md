<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Data-Efficient Reinforcement Learning with Probabilistic Model Predictive Control

Topics include Reinforcement learning, Model predictive control, Predictive control, Robotics, Uncertainty, Gaussian processes, Neural networks, Probabilistic models, Planning, Control, Learning, Trial-and-error based reinforcement learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Trial-and-error based reinforcement learning (RL) has seen rapid advancements in recent times, especially with the advent of deep neural networks. However, the majority of autonomous RL algorithms require a large number of interactions with the environment. A large number of interactions may be impractical in many real-world applications, such as robotics, and many practical systems have to obey limitations in the form of state space or control constraints. To reduce the number of system interactions while simultaneously handling constraints, we propose a model-based RL framework based on probabilistic Model Predictive Control (MPC). In particular, we propose to learn a probabilistic transition model using Gaussian Processes (GPs) to incorporate model uncertainty into long-term predictions, thereby, reducing the impact of model errors. We then use MPC to find a control sequence that minimises the expected long-term cost. We provide theoretical guarantees for first-order optimality in the GP-based transition models with deterministic approximate inference for long-term planning. We demonstrate that our approach does not only achieve state-of-the-art data efficiency, but also is a principled way for RL in constrained environments.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement learning (RL) is a principled mathematical framework for experience-based autonomous learning of control policies. Its trial-and-error learning process is one of the most distinguishing features of RL. Despite many recent advances in RL, a main limitation of current RL algorithms remains its data inefficiency, i.e., the required number of interactions with the environment is impractically high. For example, many RL approaches in problems with low-dimensional state spaces and fairly benign dynamics require thousands of trials to learn. This *data inefficiency* makes learning in real control/robotic systems without task-specific priors impractical and prohibits RL approaches in more challenging scenarios.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A promising way to increase the data efficiency of RL without inserting task-specific prior knowledge is to learn models of the underlying system dynamics. When a good model is available, it can be used as a faithful proxy for the real environment, i.e., good policies can be obtained from the model without additional interactions with the real system. However, modelling the underlying transition dynamics accurately is challenging and inevitably leads to model errors. To account for model errors, it has been proposed to use probabilistic models. By explicitly taking model uncertainty into account, the number of interactions with the real system can be substantially reduced. For example the authors use Gaussian processes (GPs) to model the dynamics of the underlying system. The PILCO algorithm propagates uncertainty through time for long-term planning and learns parameters of a feedback policy by means of gradient-based policy search. It achieves an unprecedented data efficiency for learning control policies for from scratch.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

While the PILCO algorithm is data efficient, it has few shortcomings: 1) Learning closed-loop feedback policies needs the full planning horizon to stabilise the system, which results in a significant computational burden; 2) It requires us to specify a parametrised policy a priori, often with hundreds of parameters; 3) It cannot handle state constraints; 4) Control constraints are enforced by using a differentiable squashing function that is applied to the RBF policy. This allows PILCO to explicitly take control constraints into account during planning. However, this kind of constraint handling can produce unreliable predictions near constraint boundaries.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we develop an RL algorithm that is a) data efficient, b) does not require to look at the full planning horizon, c) handles constraints naturally, d) does not require a parametrised policy, e) is theoretically justified. The key idea is to reformulate the optimal control problem with learned GP models as an equivalent deterministic problem, an idea similar to. This reformulation allows us to exploit Pontryagin's maximum principle to find optimal control signals while handling constraints in a principled way. We propose probabilistic model predictive control (MPC) with learned GP models, while propagating uncertainty through time. The MPC formulation allows to plan ahead for relatively short horizons, which limits the computational burden and allows for infinite-horizon control applications. Our approach can find optimal trajectories in constrained settings, offers an increased robustness to model errors and an unprecedented data efficiency compared to the state of the art.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Contribution", "weight": 1.0} -->

The contributions of this paper are the following: 1) We propose a new 'deterministic' formulation for probabilistic MPC with learned GP models and uncertainty propagation for long-term planning. 2) This reformulation allows us to apply Pontryagin's Maximum Principle (PMP) for the open-loop planning stage of probabilistic MPC with GPs. Using the PMP we can handle control constraints in a principled fashion while still maintaining necessary conditions for optimality. 3) The proposed algorithm is not only theoretically justified by optimal control theory, but also achieves a state-of-the-art data efficiency in RL while maintaining the probabilistic formulation. 4) Our method can handle state and control constraints while preserving its data efficiency and optimality properties.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Controller Learning via Probabilistic MPC", "weight": 1.0} -->

For data efficiency, we follow a model-based RL strategy, i.e., we learn a model of the unknown transition function $f$, which we then use to find open-loop^11^1'Open-loop' refers to the fact that the control signals are independent of the state, i.e., there is no state feedback incorporated. optimal controls ${\mathbf{u}}_{0}^{\ast},\ldots,{\mathbf{u}}_{T - 1}^{\ast}$ that minimise. After every application of the control sequence, we update the learned model with the newly acquired experience and re-plan. Section 2.1 summarises the model learning step; Section 2.2 details how to obtain the desired open-loop trajectory.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Probabilistic Transition Model", "weight": 1.0} -->

We learn a probabilistic model of the unknown underlying dynamics $f$ to be robust to model errors. In particular, we use a Gaussian process (GP) as a prior $p{(f)}$ over plausible transition functions $f$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Probabilistic Transition Model", "weight": 1.0} -->

A GP is a probabilistic non-parametric model for regression. In a GP, any finite number of function values is jointly Gaussian distributed. A GP is fully specified by a mean function $m{( \cdot )}$ and a covariance function (kernel) $k{( \cdot, \cdot )}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Probabilistic Transition Model", "weight": 1.0} -->

The inputs for the dynamics GP are given by tuples ${\overset{\sim}{\mathbf{x}}}_{t}:={({\mathbf{x}}_{t},{\mathbf{u}}_{t})}$, and the corresponding targets are ${\mathbf{x}}_{t + 1}$. We denote the collections of training inputs and targets by $\overset{\sim}{\mathbf{X}},{\mathbf{y}}$, respectively. Furthermore, we assume a Gaussian (RBF, squared exponential) covariance function where $\sigma_{f}^{2}$ is the signal variance and ${\mathbf{L}} = {\text{diag}{(l_{1},\ldots,l_{D + U})}}$ is a diagonal matrix of length-scales $l_{1},\ldots,l_{D + U}$. The GP is trained via the standard procedure of evidence maximisation.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Open-Loop Control", "weight": 1.0} -->

To find the desired open-loop control sequence ${\mathbf{u}}_{0}^{\ast},\ldots,{\mathbf{u}}_{T - 1}^{\ast}$, we follow a two-step procedure proposed. 1) Use the learned GP model to predict the long-term evolution ${p{({\mathbf{x}}_{1})}},\ldots,{{\mathbf{p}}{({\mathbf{x}}_{T})}}$ of the state for a given control sequence ${\mathbf{u}}_{0},\ldots,{\mathbf{u}}_{T - 1}$. 2) Compute the corresponding expected long-term cost and find an open-loop control sequence ${\mathbf{u}}_{0}^{\ast},\ldots,{\mathbf{u}}_{T - 1}^{\ast}$ that minimises the expected long-term cost.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Open-Loop Control", "weight": 1.0} -->

In the following, we will detail these steps.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Long-term Predictions", "weight": 1.0} -->

To obtain the state distributions ${p{({\mathbf{x}}_{1})}},\ldots,{p{({\mathbf{x}}_{T})}}$ for a given control sequence ${\mathbf{u}}_{0},\ldots,{\mathbf{u}}_{T - 1}$, we iteratively predict for ${t = {0,\ldots,{T - 1}}},$ by making a *deterministic* Gaussian approximation to $p{(\left. {\mathbf{x}}_{t + 1} \middle| {\mathbf{u}}_{t} \right.)}$ using moment matching. This approximation has been shown to work well in practice in RL contexts and can be computed in closed form when using the Gaussian kernel.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Long-term Predictions", "weight": 1.0} -->

A key property that we exploit is that moment matching allows us to formulate the uncertainty propagation in as a 'deterministic system function' where ${\mathbf{μ}}_{t},\mathbf{\Sigma}_{t}$ are the mean and the covariance of $p{({\mathbf{x}}_{t})}$. For a deterministic control signal ${\mathbf{u}}_{t}$ we further define the moments of the control-augmented distribution $p{({\mathbf{x}}_{t},{\mathbf{u}}_{t})}$ as such that can equivalently be written as the deterministic system equation

<!-- chunk {"id": "body-0016", "role": "body", "section": "Optimal Open-Loop Control Sequence", "weight": 1.0} -->

To find the optimal open-loop sequence ${\mathbf{u}}_{0}^{\ast},\ldots,{\mathbf{u}}_{T - 1}^{\ast}$, we first compute the expected long-term cost $J$ in using the Gaussian approximations ${p{({\mathbf{x}}_{1})}},\ldots,{p{({\mathbf{x}}_{T})}}$ obtained via for a given open-loop control sequence ${\mathbf{u}}_{0},\ldots,{\mathbf{u}}_{T - 1}$. Second, we find a control sequence that minimises the expected long-term cost. In the following, we detail these steps.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Computing the Expected Long-Term Cost", "weight": 1.0} -->

To compute the expected long-term cost, we sum up the expected immediate costs for $t = {0,\ldots,{T - 1}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Computing the Expected Long-Term Cost", "weight": 1.0} -->

We choose $\ell$, such that this expectation and the partial derivatives $\partial{{{\mathbb{E}}{\lbrack{\ell{({\mathbf{x}}_{t},{\mathbf{u}}_{t})}}\rbrack}}/{\partial{\mathbf{x}}_{t}}}$, $\partial{{{\mathbb{E}}{\lbrack{\ell{({\mathbf{x}}_{t},{\mathbf{u}}_{t})}}\rbrack}}/{\partial{\mathbf{u}}_{t}}}$ can be computed analytically.^22^2Choices for $\ell$ include the standard quadratic (polynomial) cost, but also costs expressed as Fourier series expansions or radial basis function networks with Gaussian basis function.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Computing the Expected Long-Term Cost", "weight": 1.0} -->

Similar to, this allows us to define deterministic mappings that map the mean and covariance of $\overset{\sim}{\mathbf{x}}$ onto the corresponding expected costs.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The open-loop optimisation turns out to be sparse. However, optimisation via the value function or dynamic programming is valid only for unconstrained controls. To address this practical shortcoming, we define Pontryagin's Maximum Principle that allows us to formulate the constrained problem while maintaining the sparsity. We detail this sparse structure for the constrained GP dynamics problem in section 3.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Feedback Control with MPC", "weight": 1.0} -->

Thus far, we presented a way for efficiently determining an open-loop controller. However, an open-loop controller cannot stabilise the system. Therefore, it is essential to obtain a feedback controller. MPC is a practical framework for this. While interacting with the system MPC determines an $H$-step open-loop control trajectory ${\mathbf{u}}_{0}^{\ast},\ldots,{\mathbf{u}}_{H - 1}^{\ast}$, starting from the current state ${\mathbf{x}}_{t}$^33^3A state distribution $p{({\mathbf{x}}_{t})}$ would work equivalently in our framework.. Only the first control signal ${\mathbf{u}}_{0}^{\ast}$ is applied to the system.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Feedback Control with MPC", "weight": 1.0} -->

When the system transitions to ${\mathbf{x}}_{t + 1}$, we update the GP model with the newly available information, and MPC re-plans ${\mathbf{u}}_{0}^{\ast},\ldots,{\mathbf{u}}_{H - 1}^{\ast}$. This procedure turns an open-loop controller into an implicit closed-loop (feedback) controller by repeated re-planning $H$ steps ahead from the current state. Typically, $H \ll T$, and MPC even allows for $T = \infty$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Feedback Control with MPC", "weight": 1.0} -->

In this section, we provided an algorithmic framework for probabilistic MPC with learned GP models for the underlying system dynamics, where we explicitly use the GP's uncertainty for long-term predictions. In the following section, we will justify this using optimal control theory. Additionally, we will discuss how to account for constrained control signals in a principled way without the necessity to warp/squash control signals as.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Theoretical Justification", "weight": 1.0} -->

Bellman's optimality principle yields a recursive formulation for calculating the total expected cost and gives a sufficient optimality condition. PMP provides the corresponding necessary optimality condition. PMP allows us to compute gradients $\partial{J/{\partial{\mathbf{u}}_{t}}}$ of the expected long-term cost w.r.t. the variables that only depend on variables with neighbouring time index, i.e., $\partial{J/{\partial{\mathbf{u}}_{t}}}$ depends only variables with index $t$ and $t + 1$. Furthermore, it allows us to explicitly deal with constraints on states and controls. In the following, we detail how to solve the optimal control problem (OCP) with PMP for learned GP dynamics and deterministic uncertainty propagation. We additionally provide a computationally efficient way to compute derivatives based on the maximum principle.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Theoretical Justification", "weight": 1.0} -->

To facilitate our discussion we first define some notation. Practical control signals are often constrained. We formally define a class of admissible controls $\mathcal{U}$ that are piecewise continuous functions defined on a compact space $U \subset {\mathbb{R}}^{U}$. This definition is fairly general, and commonly used zero-order-hold or first-order-hold signals satisfy this requirement. Applying admissible controls to the deterministic system dynamics $f_{MM}$ defined in yields a set $\mathcal{Z}$ of admissible controlled trajectories. We define the tuple $(\mathcal{Z},f_{MM},\mathcal{U})$ as our control system.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Theoretical Justification", "weight": 1.0} -->

For a single admissible control trajectory ${\mathbf{u}}_{0:{H - 1}}$, there will be a unique trajectory ${\mathbf{z}}_{0:H}$, and the pair $({\mathbf{z}}_{0:H},{\mathbf{u}}_{0:{H - 1}})$ is called an admissible controlled trajectory.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Theoretical Justification", "weight": 1.0} -->

We now define the control-Hamiltonian for this control system as This formulation of the control-Hamiltonian is the centre piece of the Pontryagin's approach to the OCP. The vector ${\mathbf{λ}}_{t + 1}$ can be viewed as a Lagrange multiplier for dynamics constraints associated with the OCP.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Theoretical Justification", "weight": 1.0} -->

To successfully apply PMP we need the system dynamics to have a unique solution for a given control sequence. Traditionally, this is interpreted as the system is 'deterministic'. This interpretation has been considered a limitation of PMP. In this paper, however, we exploit the fact that the moment-matching approximation is a deterministic operator, similar to the projection used in EP. This yields the 'deterministic' system equations, that map moments of the state distribution at time $t$ to moments of the state distribution at time $t + 1$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Existence/Uniqueness of a Local Solution", "weight": 1.0} -->

To apply the PMP we need to extend some of the important characteristics of ODEs to our system. In particular, we need to show the existence and uniqueness of a (local) solution to our difference equation.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Existence/Uniqueness of a Local Solution", "weight": 1.0} -->

For existence of a solution we need to satisfy the difference equation point-wise over the entire horizon and for uniqueness we need the system to have only one singularity. For our discrete-time system equation (via the moment-matching approximation) in we have the following

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 2", "weight": 1.0} -->

The minimum condition can be used to find an optimal control. The Hamiltonian is minimised point-wise over the admissible control set $\mathcal{U}$: For every $t = {0,\ldots,{H - 1}}$ we find optimal controls ${\mathbf{u}}_{t}^{\ast} \in {{\arg{\min_{\mathbf{ν}}\mathcal{H}}}{({\mathbf{λ}}_{t + 1},{\mathbf{z}}_{t}^{\ast},{\mathbf{ν}})}}$. The minimisation problem possesses additional variables ${\mathbf{λ}}_{t + 1}$. These variables can be interpreted as Lagrange multipliers for the optimisation. They capture the impact of the control ${\mathbf{u}}_{t}$ over the whole trajectory and, hence, these variables make the optimisation problem sparse.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 2", "weight": 1.0} -->

For the GP dynamics we compute the multipliers ${\mathbf{λ}}_{t}$ in closed form, thereby, significantly reducing the computational burden to minimise the expected long-term cost $J$. We detail this calculation in section 3.3.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 3", "weight": 1.0} -->

In the optimal control problem, we aim to find an admissible control trajectory that minimizes the cost subject to possibly additional constraints. PMP gives first-order optimality conditions over these admissible controlled trajectories and can be generalised to handle additional state and control constraints.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 4", "weight": 1.0} -->

The Hamiltonian $\mathcal{H}$ in is constant for unconstrained controls in time-invariant dynamics and equals $0$ everywhere when the final time $H$ is not fixed.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 5", "weight": 1.0} -->

For linear dynamics the proposed method is a generalisation of iLQG: The moment matching transition $f_{MM}$ implicitly linearises the transition dynamics at each time step, whereas in iLQG an explicit local linear approximation is made. For a linear $f_{MM}$ and a quadratic cost $\ell$ we can write the LQG case as shown in Theorem 1. If we iterate with successive corrections to the linear approximations we obtain iLQG.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Efficient Gradient Computation", "weight": 1.0} -->

With the definition of the Hamiltonian $\mathcal{H}$ in we can efficiently calculate the gradient of the expected total cost $J$. For a time horizon $H$ we can write the accumulated cost as the Bellman recursion for $t = {{H - 1},\ldots,0}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Efficient Gradient Computation", "weight": 1.0} -->

Since the (open-loop) control ${\mathbf{u}}_{t}$ only impacts the future costs via ${\mathbf{z}}_{t + 1} = {f_{MM}{({\mathbf{z}}_{t},{\mathbf{u}}_{t})}}$ the derivative of the total cost with ${\mathbf{u}}_{t}$ is given by Comparing this expression with the definition of the Hamiltonian, we see that if we make the substitution ${\mathbf{λ}}_{t + 1}^{T} = \frac{\partial J_{t + 1}}{\partial{\mathbf{z}}_{t + 1}}$ we obtain This implies that the gradient of the expected long-term cost w.r.t. ${\mathbf{u}}_{t}$ can be efficiently computed using the Hamiltonian.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Efficient Gradient Computation", "weight": 1.0} -->

Next we show that the substitution ${\mathbf{λ}}_{t + 1}^{T} = \frac{\partial J_{t + 1}}{\partial{\mathbf{z}}_{t + 1}}$ is valid for the entire horizon $H$. For the terminal cost $\Phi_{MM}{({\mathbf{z}}_{H})}$ this is valid by the transversality condition. For other time steps we differentiate w.r.t. ${\mathbf{z}}_{t}$, which yields which is identical to the ad-joint equation. Hence, in our setting, PMP implies that *gradient descent on the Hamiltonian $\mathcal{H}$ is equivalent to gradient descent on the total cost*.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Efficient Gradient Computation", "weight": 1.0} -->

Algorithmically, in an RL setting, we find the optimal control sequence ${\mathbf{u}}_{0}^{\ast},\ldots,{\mathbf{u}}_{H - 1}^{\ast}$ as follows: For a given initial (random) control sequence ${\mathbf{u}}_{0:{H - 1}}$ we follow the steps described in section 2.2.1 to determine the corresponding trajectory ${\mathbf{z}}_{1:H}$. Additionally, we compute Lagrange multipliers ${\mathbf{λ}}_{t + 1}^{T} = \frac{\partial J_{t + 1}}{\partial{\mathbf{z}}_{t + 1}}$ during the forward propagation. Note that traditionally ad-joint equations are propagated backward to find the multipliers.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Efficient Gradient Computation", "weight": 1.0} -->

Given ${\mathbf{λ}}_{t}$ and a cost function $\ell_{MM}$ we can determine the Hamiltonians $\mathcal{H}_{1:H}$. Then we find a new control sequence ${\mathbf{u}}_{0:{H - 1}}^{\ast}$ via any gradient descent method using.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Efficient Gradient Computation", "weight": 1.0} -->

We use Sequential Quadratic Programming (SQP) with BFGS for Hessian updates. The Lagrangian of SQP is a partially separable function. In the PMP, this separation is explicit via the Hamiltonians, i.e., the $\mathcal{H}_{t}$ is a function of variables with index $t$ or $t + 1$. This leads to a block-diagonal Hessian of SQP Lagrangian. The structure can be exploited to approximate the Hessian via block-updates within BFGS

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

We evaluate the quality of our algorithm in two ways: First, we assess whether probabilistic MPC leads to faster learning compared with PILCO, the current state of the art in terms of data efficiency. Second, we assess the impact of state constraints while performing the same task.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

We consider two RL benchmark problems: the under-actuated cart-pole-swing-up and the fully actuated double-pendulum swing-up. In both tasks, PILCO is the most data-efficient RL algorithm to date.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Under-actuated Cart-Pole Swing-Up", "weight": 1.0} -->

The cart pole system is an under-actuated system with a freely swinging pendulum of $50{cm}$ mounted on a cart. The swing-up and balancing task cannot be solved using a linear model. The cart-pole system state space consists of the position of the cart $x$, cart velocity $\overset{˙}{x}$, the angle $\theta$ of the pendulum and the angular velocity $\overset{˙}{\theta}$. A horizontal force $u \in {\lbrack{- 10},10\rbrack}$ N can be applied to the cart. Starting in a position where the pendulum hangs downwards, the objective is to automatically learn a controller that swings the pendulum up and balances it in the inverted position in the middle of the track.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Constrained Cart-Pole Swing-Up", "weight": 1.0} -->

For the state-space constraint experiment we place a wall on the track near the target, see Fig. 1(a). The wall is at -70 cm, which, along with force limitations, requires the system to swing from the right side.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Fully-actuated Double-Pendulum", "weight": 1.0} -->

The double pendulum system is a two-link robot arm (links lengths: $1m$) with two actuators at each joint. The state space consists of 2 angles and 2 angular velocities $\lbrack\theta_{1},\theta_{2},{\overset{˙}{\theta}}_{1},{\overset{˙}{\theta}}_{2}\rbrack$. The torques $u_{1}$ and $u_{2}$ are limited to $\lbrack{- 2},2\rbrack$ Nm. Starting from a position where both links are in a downwards position, the objective is to learn a control strategy that swings the double-pendulum up and balances it in the inverted position.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Constrained Double-Pendulum", "weight": 1.0} -->

The double-pendulum has a constraint on the angle of the inner pendulum, so that it only has a $340^{\circ}$ motion range, i.e., it cannot spin through, see Fig. 1(b). The constraint blocks all clockwise swing-ups. The system is underpowered, and it has to swing clockwise first for a counter-clockwise swing-up without violating the constraints.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Trials", "weight": 1.0} -->

The general setting is as follows: All RL algorithms start off with a single short random trajectory, which is used for learning the dynamics model. As in the GP is used to predict state differences ${\mathbf{x}}_{t + 1} - {\mathbf{x}}_{t}$. The learned GP dynamics model is then used to determine a controller based on iterated moment matching, which is then applied to the system, starting from ${\mathbf{x}}_{0} \sim {p{({\mathbf{x}}_{0})}}$. Model learning, controller learning and application of the controller to the system constitute a 'trial'. After each trial, the hyper-parameters of the model are updated with the newly acquired experience and learning continues.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Baselines", "weight": 1.0} -->

We compare our GP-MPC approach with the following baselines: the PILCO algorithm and a zero-variance GP-MPC algorithm (in the flavour of ) for RL, where the GP's predictive variances are discarded. Due to the lack of exploration, such a zero-variance approach within PILCO (a policy search method) does not learn anything useful as already demonstrated, and we do not include this baseline.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Baselines", "weight": 1.0} -->

We average over 10 independent experiments, where every algorithm is initialised with the same first (random) trajectory. The performance differences of the RL algorithms are therefore due to different approaches to controller learning and the induced exploration.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Data Efficiency", "weight": 1.0} -->

In both benchmark experiments (cart-pole and double pendulum), we use the exact saturating cost, which penalises the Euclidean distance of the tip of the (outer) pendulum from the target position, i.e., we are in a setting in which PILCO performs very well.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Data Efficiency", "weight": 1.0} -->

Fig. 2(a) shows that both our MPC-based controller (blue) and the zero-variance approach successfully^44^4We define 'success' if the pendulum tip is closer than $8{cm}$ to the target position for ten consecutive time steps. complete the task in fewer trials than the state-of-the-art PILCO method (red). From the repeated trials we see that GP-MPC learns faster and more reliably than PILCO. In particular, GP-MPC and the zero-variance approach can solve the cart-pole task with high probability (90%) after three trials (9 seconds), where the first trial was random. PILCO needs two additional trials. The reason why the zero-variance approach (no model uncertainties) works in an MPC context but not within a policy search setting is that we include every observed state transition immediately in the GP dynamics model, which makes MPC fairly robust to model errors. It even allows for model-based RL with deterministic models in simple settings.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Data Efficiency", "weight": 1.0} -->

Fig. 2(b) highlights that our proposed GP-MPC approach (yellow) requires on average only six trials ($18s$) of experience to achieve a 90% success rate^55^5The tip of outer pendulum is closer than $22{cm}$ to the target., including the first random trial. PILCO requires four additional trials, whereas the zero-variance MPC approach completely fails in this RL setting. The reason for this failure is that the deterministic predictions with a poor model in this complicated state space do not allow for sufficient exploration. We also observe that GP-MPC is more robust to the variations amongst trials.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Data Efficiency", "weight": 1.0} -->

In both experiments, our proposed GP-MPC requires only 60% of PILCO's experience, such that we report an unprecedented learning speed for these benchmarks, even with settings for which PILCO performs very well.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Data Efficiency", "weight": 1.0} -->

We identify two key ingredients that are responsible for the success and learning speed of our approach: the ability to immediately react to observed states by adjusting the long-term plan and augment the training set of the GP model on the fly as soon as a new state transition is observed (hyper-parameters are not updated at every time step). These properties turn out to be crucial in the very early stages of learning when very little information is available. If we ignored the on-the-fly updates of the GP dynamics model, our approach would still successfully learn, although the learning efficiency would be slightly decreased.

<!-- chunk {"id": "body-0056", "role": "body", "section": "State Constraints", "weight": 1.0} -->

A scenario in which PILCO struggles is a setting with state space constraints. We modify the cart-pole and the double-pendulum tasks to such a setting. Both tasks are symmetric, and we impose state constraints in such a way that only one direction of the swing-up is feasible. For the cart-pole system, we place a wall near the target position of the cart, see Fig. 1(a); the double pendulum has a constraint on the angle of the inner pendulum, so that it only has a $340^{\circ}$ motion range, i.e., it cannot spin through, see Fig. 1(b). These constraints constitute linear constraints on the state.

<!-- chunk {"id": "body-0057", "role": "body", "section": "State Constraints", "weight": 1.0} -->

We use a quadratic cost that penalises the Euclidean distance between the tip of the pendulum and the target. This, along with the 'implicit' linearisation, makes the optimal control problem an 'implicit' QP. If a rollout violates the state constraint we immediately abort that trial and move on to the next trial. We use the same experimental set-up as data efficiency experiments.

<!-- chunk {"id": "body-0058", "role": "body", "section": "State Constraints", "weight": 1.0} -->

The state constraints are implemented as *expected violations*, i.e., ${{\mathbb{E}}{\lbrack{\mathbf{x}}_{t}\rbrack}} < {\mathbf{x}}_{\text{limit}}$ and *chance constraints* ${p{({{\mathbf{x}}_{t} < {\mathbf{x}}_{\text{limit}}})}} \geq 0.95$. Fig. 1(a) shows that our MPC-based controller with chance constraint (blue) successfully completes the task with a small acceptable number of violations, see Table 1. The expected violation approach, which only considers the predicted mean (yellow) fails to complete the task due to repeated constraint violations. PILCO uses its saturating cost (there is little hope for learning with quadratic cost ) and has partial success in completing the task, but it struggles, especially during initial trials due to repeated state violations.

<!-- chunk {"id": "body-0059", "role": "body", "section": "State Constraints", "weight": 1.0} -->

One of the key points we observe from the Table 1 is that the incorporation of uncertainty into planning is again crucial for successful learning. If we use only predicted means to determine whether the constraint is violated, learning is not reliably 'safe'. Incorporation of the predictive variance, however, results in significantly fewer constraint violations.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

We proposed an algorithm for data-efficient RL that is based on probabilistic MPC with learned transition models using Gaussian processes. By exploiting Pontryagin's maximum principle our algorithm can naturally deal with state and control constraints. Key to this theoretical underpinning of a practical algorithm was the re-formulation of the optimal control problem with uncertainty propagation via moment matching into an deterministic optimal control problem. MPC allows the learned model to be updated immediately, which leads to an increased robustness with respect to model inaccuracies. We provided empirical evidence that our framework is not only theoretically sound, but also extremely data efficient, while being able to learn in settings with hard state constraints.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

One of the most critical components of our approach is the incorporation of model uncertainty into modelling and planning. In complex environments, model uncertainty drives targeted exploration. It additionally allows us to account for constraints in a risk-averse way, which is important in the early stages of learning.
