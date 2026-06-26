<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Natural Gradient Descent for Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper bridges optimization and control, and presents a novel closed-loop control framework based on natural gradient descent, offering a trajectory-oriented alternative to traditional cost-function tuning. By leveraging the Fisher Information Matrix, we formulate a preconditioned gradient descent update that explicitly shapes system trajectories. We show that, in sharp contrast to traditional controllers, our approach provides flexibility to shape the system's low-level behavior. To this end, the proposed method parameterizes closed-loop dynamics in terms of stationary covariance and an unknown cost function, providing a geometric interpretation of control adjustments. We establish theoretical stability conditions. The simulation results on a rotary inverted pendulum benchmark highlight the advantages of natural gradient descent in trajectory shaping.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optimization techniques, particularly gradient descent (GD) and its numerous variants, have become fundamental in modern control and machine learning. These methods are broadly classified into two categories when applied to control systems: GD-based control, where gradient methods optimize controller parameters, and controlled GD, where control-theoretic tools improve the convergence properties of a gradient-based optimizer. GD-based methods have demonstrated significant success in learning controllers for uncertain environments, as well as in system identification and adaptive control.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite their effectiveness, a key challenge persists: the closed-loop trajectory behavior---how system states evolve over time---is typically an indirect outcome of weight tuning or cost-function optimization. Traditional methods rely on defining an objective function, applying an optimization algorithm, and then observing the resulting state trajectories. If these trajectories do not meet performance expectations, the objective function often requires manual adjustments, leading to a cumbersome iterative tuning process. Furthermore, this process is susceptible to "reward hacking," where the optimized policy achieves a low-cost function value but deviates from the designer's intended behavior.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In our previous work, we proposed a fundamentally different perspective by directly shaping system trajectories through a gradient-descent-like closed-loop approach. We introduced a novel parameterization of the stable closed-loop dynamics where $A,B$ are the system matrices, $K$ is a feedback gain, and ${\Gamma,P} \succ 0$ represent a GD step and a quadratic Lyapunov cost matrix, respectively. This formulation ensures that the closed-loop system behaves analogously to a GD update applied to the Lyapunov function ${V{(x_{k})}} = {x_{k}^{\top}Px_{k}}$, leading to the explicit trajectory update dynamic Rather than iteratively adjusting an unknown cost function to produce desired state trajectories, we directly impose a controlled gradient flow on the system states.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This trajectory-oriented perspective offers several advantages. Firstly, it provides explicit trajectory control. The gradient formulation provides direct control over the trajectory shape, eliminating the need for trial-and-error cost function tuning. Secondly, it quantifies robustness by the step size. For a small step size, closed-loop eigenvalues have small variations. Lastly, it unifies with a Linear Quadratic Regulator (LQR). We established theoretical connections between our approach and classical optimal control, showing that LQR solutions can be naturally represented in this setting.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

One of the key challenges in the proposed approach is the definition of the preconditioning matrix $\Gamma$, which is generally non-trivial. To address this issue, we use a natural GD framework as the update rule for the state-space evolution. We demonstrate that, in this formulation, $\Gamma$ corresponds to the covariance matrix of the state vector of the closed-loop system, providing a meaningful interpretation: the magnitude of updates in state space is directly influenced by the uncertainty level, as quantified by the covariance matrix. This insight establishes a direct link between control adjustments and the available information in the system. Furthermore, we derive theoretical stability conditions and step-size constraints to ensure robust implementation. The effectiveness of the proposed approach is validated through simulations on the Quanser rotary inverted pendulum benchmark, demonstrating predictable closed-loop behavior compared to the LQR method.

<!-- chunk {"id": "body-0008", "role": "body", "section": "System Model and Problem Description", "weight": 1.0} -->

Consider a linear time-invariant (LTI) stochastic discrete-time system of the form where $k \in {\mathbb{N}}$, $x_{k} \in {\mathbb{R}}^{n}$ is the system's state, and $u_{k} \in {\mathbb{R}}^{m}$ is the control input. In addition, $A$ and $B$ are transition and input matrices of appropriate dimensions, respectively. The noise of the system $\omega_{k} \in {\mathbb{R}}^{n}$ is governed by a Gaussian distribution $\mathcal{N}{(0,W)}$ where $W \in {\mathbb{R}}^{n \times n} \succ 0$ is its covariance matrix. Throughout this paper, a linear control policy is used The dynamical system evolves stochastically due to the additive Gaussian noise $\omega_{k}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "System Model and Problem Description", "weight": 1.0} -->

Using the linear control policy, the distribution of the state $x_{k}$ at time $k$ is given by $x_{k} \sim {\mathcal{N}{(\mu_{k},\Sigma_{k})}}$, where the mean $\mu_{k}$ and the covariance $\Sigma_{k}$ are updated respectively as follows The term ${({A + {BK}})}\Sigma_{k}{({A + {BK}})}^{\top}$ captures how the closed-loop dynamics influence the propagation of uncertainty.

<!-- chunk {"id": "body-0010", "role": "body", "section": "System Model and Problem Description", "weight": 1.0} -->

A key challenge in closed-loop controller design using LQR is ensuring that the resulting trajectories exhibit desired convergence properties while minimizing deviations due to disturbances. Traditional methods, such as optimal control and reinforcement learning, typically optimize a predefined cost function to tune $K$, indirectly shaping the closed-loop behavior. If the resulting optimal control solution is not satisfactory, the cost parameter must be adjusted. However, the map from the cost parameters to the low-level system behavior is unknown, which makes it challenging to achieve the designer's intention by adjusting the cost parameter. In this work, we propose an alternative approach where the closed-loop dynamics are parameterized in a GD-inspired framework. This formulation ensures that the state updates follow a gradient-descent-like behavior. We gain direct control over trajectory shaping rather than relying on cost-function tuning. This approach provides a geometric interpretation of closed-loop control.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Basics of Gradients", "weight": 1.0} -->

Gradients play a fundamental role in optimization and control. In the context of machine learning and control systems, gradients are used to iteratively adjust parameters in order to minimize a given cost function. Traditional gradient-based methods rely on first-order derivatives to provide a direction of improvement, while more advanced techniques, such as natural gradients, refine this approach by incorporating information about the underlying geometry of the parameter space.

<!-- chunk {"id": "body-0012", "role": "body", "section": "GD Algorithm", "weight": 1.0} -->

In the standard GD, the update rule for minimizing a cost function $J{(\theta)}$ with respect to parameters $\theta$ is where $\alpha > 0$ is the step size. This method works in an Euclidean parameter space, assuming that all directions have equal importance and are scaled uniformly. However, when the parameter space is curved or highly anisotropic, standard GD can suffer from slow convergence.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Natural GD Algorithm", "weight": 1.0} -->

Natural gradients are an extension of GD that accounts for the geometry of the parameter space. Instead of using the Euclidean gradient, the natural gradient uses an alternative direction based on the local curvature of the space. The natural gradient update is defined as where $G{(\theta_{k})}$ is the Fisher Information Matrix (FIM), defined as with $p_{\theta_{k}}{(z_{k})}$ being the Probability Distribution Function (PDF) parameterized by $\theta_{k}$. $G{(\theta_{k})}^{- 1}$ serves as a preconditioner, transforming the gradient into a coordinate system that respects the curvature of the cost surface. The preconditioning approach significantly improves convergence in ill-conditioned landscapes, ensuring more stable and efficient parameter updates.

<!-- chunk {"id": "body-0014", "role": "body", "section": "From Basic GD to Natural GD in state-space", "weight": 1.0} -->

This section explores the evolution of GD methods applied in state space, beginning from the standard formulation and advancing towards natural gradient techniques that account for system curvature and structure.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Standard GD", "weight": 1.0} -->

Noise-free linear dynamical systems are considered in Esmzad and Modares. GD updates for this case is given by where $V{(x_{k})}$ and $\alpha > 0$ are the cost function and a step size respectively. This method assumes an isotropic state space where all directions are equally important. However, when the landscape of $V{(x_{k})}$ is highly anisotropic (e.g., elongated level sets), standard GD can suffer from slow convergence and oscillatory behavior.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Preconditioned GD", "weight": 1.0} -->

Again for noise free linear dynamical system in Esmzad and Modares, one can consider a preconditioning matrix $\Gamma$, which rescales the gradient update where $\Gamma$ is a positive definite matrix that adjusts the step size in different directions. If $\Gamma$ is chosen appropriately, this method can significantly accelerate convergence by better aligning the update with the geometry of $V{(x_{k})}$. However, it requires fine-tuning.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Natural GD", "weight": 1.0} -->

In this paper, we consider linear systems subject to Gaussian noise so we will give the natural GD update for $\mu_{k}$. The natural gradient method refines preconditioned GD by using the inverse FIM, $G{(\mu_{k})}$, as the preconditioner where $G{(\mu_{k})}$ accounts for the curvature of the state space and $\alpha > 0$. Unlike standard GD, which uses the Euclidean gradient, the natural gradient follows the Riemannian structure of the space, leading to more efficient updates. $G{(\mu_{k})}$ can be replaced by a Hessian approximation or another metric tensor that captures the local curvature of $V{(x_{k})}$. In control applications, such matrices arise naturally in system identification and adaptive control, where the uncertainty in the state of the system can be quantified through inverse covariance matrices as it is outlined in the next section.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Natural GD for Control", "weight": 1.0} -->

Natural gradient methods have been widely recognized for their ability to enhance convergence rates in optimization by accounting for the curvature of the cost landscape. Similarly, in the context of state-space control, the use of a positive-definite preconditioning matrix $\Gamma$ provides a powerful mechanism for improving convergence rates. The gradient preconditioning adapts the descent direction and magnitude to the underlying geometry of the system dynamics, ensuring more efficient convergence.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Computing the FIM", "weight": 1.0} -->

The FIM, $G{(\mu_{k})}$, quantifies the curvature of the likelihood $p{(x_{k})}$ in the state space and provides insight into the sensitivity of the likelihood to state changes. For the stochastic system dynamical system, the PDF of the state $x_{k} \sim {\mathcal{N}{(\mu_{k},\Sigma_{k})}}$ is given by the following Gaussian distribution The log-likelihood of $p{(x_{k})}$ is given by Taking the gradient of ${\log p}{(x_{k})}$ with respect to $\mu_{k}$ Substituting into the FIM definition in yields The FIM, $G{(\mu_{k})}$, provides a measure of the amount of information that the state $x_{k}$ carries about the underlying system trajectories.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Computing the FIM", "weight": 1.0} -->

Here, it reduces to the inverse covariance matrix $\Sigma_{k}^{- 1}$, reflecting the precision (inverse uncertainty) in the Gaussian model. We will use the covariance matrix of the state of the closed-loop system as a natural preconditioner in the GD-based control framework and in the next section, we derive explicit formulations for designing the control gain $K$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Controller Design Using Stationary Covariance", "weight": 1.0} -->

To simplify the derivations and facilitate the analysis of the proposed control framework, we consider the steady state covariance matrix, i.e., $\Sigma_{k + 1} = \Sigma_{k} = \Sigma$. Theorem 1 encapsulates the core contribution of this work.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Note that the range for $\alpha$ in (25 ‣ 4.2 Controller Design Using Stationary Covariance ‣ 4 Natural GD for Control ‣ Natural Gradient Descent for Control")) cannot be verified before design as the values of $\Sigma$ and $P$ depend on the value of $\alpha$. However, this range tells us that smaller values of $\alpha$ will decrease the convergence rate and larger values of $\alpha$ will increase the convergence speed. So, $\alpha$ can serve as an intuitive closed-loop behavior-tweaking variable.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Discussion", "weight": 1.5} -->

Stability conditions ensure the existence of a Lyapunov function that decreases along system trajectories, guaranteeing stability. However, these conditions do not necessarily provide an explicit mechanism for *shaping* the trajectories themselves. In contrast, our framework leverages a GD-like formulation to directly influence how the state evolves at each step, thereby offering more transparency over closed-loop behavior.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Discussion", "weight": 1.5} -->

Classical LQR designs the gain matrix by minimizing a quadratic cost function, but there is no straightforward, systematic way to target specific *transient* behaviors beyond fine-tuning the weighting matrices $Q$ and $R$. The proposed natural GD approach, on the other hand, utilizes a step-size parameter $\alpha$ and a preconditioning (covariance) matrix $\Sigma$ to shape the trajectory explicitly. Adjusting $\alpha$ translates directly into changing the rate of convergence ($\Sigma$ defines how strongly each direction in the state space is scaled in the gradient step) where smaller $\alpha$ yields smoother but slower convergence, and larger $\alpha$ leads to faster convergence, albeit at the risk of oscillations if too large.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

To evaluate the proposed natural gradient control method's performance, we conducted simulations on a widely used benchmark platform Quanser rotary pendulum (model QUBE-Servo 2) ^11^1 shown in Figure 1. The system dynamics are represented in discrete time with a sampling interval of $T_{s} = 0.01$ seconds. The state vector is defined as $x = \begin{bmatrix} \theta & \delta & \overset{˙}{\theta} & \overset{˙}{\delta} \end{bmatrix}^{T}$, where $\theta$ (rad) is the rotary arm angle and $\delta$ (rad) is the pendulum angle.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

The control input $u$ (V) is the voltage applied to the motor. Here, we considered linearized dynamics around its upright equilibrium point. The control strategy aims to stabilize the pendulum in its upright equilibrium while ensuring smooth control effort. Both the natural gradient control method and LQR are employed to regulate the trajectory of the state vector. The discrete-time state-space matrices used in the simulation are given by We compared the natural gradient control method for different values of the step size parameter $\alpha$ with the standard LQR for various choices of weighting matrices $Q$ and $R$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

For the natural gradient control method, we choose $\lambda = 0.99$, and the step size values ${\alpha \in {\{ 0.01,0.018,0.025\}}}.$ For the LQR controller, we considered different state and control weighting matrices $Q_{1} = {0.001I}$, $Q_{2} = I$, $Q_{3} = {5000I}$,$R_{1} = 100$, $R_{2} = 1$, and ${R_{3} = 0.001}.$ The comparison between the natural GD approach and LQR control highlights key differences in trajectory shaping and optimal control. In the natural GD method, state evolution is influenced by the step size parameter $\alpha$, with larger values leading to faster convergence but potentially introducing oscillations. This approach provides direct control over trajectory shaping, allowing for intuitive adjustments to the system's behavior.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

Figures 2 and 3 show the results of the proposed and LQR approaches, respectively. LQR control optimally balances state regulation and control effort through the careful selection of weighting matrices $Q$ and $R$, ensuring smooth and stable convergence. However, a fundamental limitation of LQR is that the trajectory behavior is not explicitly predictable based on $Q$ and $R$ adjustments. While these matrices influence the control law, their effect on the system's transient response is often indirect and requires trial-and-error tuning. Consequently, achieving a specific trajectory shape in LQR can be challenging, as the resulting state evolution emerges from the Riccati equation rather than being explicitly controlled. On the other hand, the GD-based approach offers a geometric perspective on control, where trajectory updates follow a well-defined GD process. This enables a more transparent and predictable way to shape trajectories directly. If precise trajectory shaping is the priority, the natural GD approach provides greater interpretability. In contrast, LQR remains a reliable choice for energy-efficient and well-balanced state regulation but at the cost of requiring heuristic tuning for transient behavior control.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Conclusion and Future Directions", "weight": 1.5} -->

This paper introduced a novel closed-loop control framework based on natural GD, using the closed-loop covariance matrix as a preconditioner. By directly shaping system trajectories through a gradient-descent-like update, the proposed approach eliminates the need for indirect cost-function tuning, offering improved interpretability. Theoretical analysis established stability conditions and step-size constraints.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Conclusion and Future Directions", "weight": 1.5} -->

Future research directions include extending the framework to nonlinear and time-varying systems, incorporating state-dependent covariance adaptation, and exploring its integration with reinforcement learning and model predictive control. Additionally, investigating robustness properties under model uncertainties and external disturbances could further enhance the practical applicability of this approach in real-world scenarios.
