## Introduction

Optimization techniques, particularly gradient descent (GD) and its numerous variants, have become fundamental in modern control and machine learning. These methods are broadly classified into two categories when applied to control systems: GD-based control, where gradient methods optimize controller parameters, and controlled GD, where control-theoretic tools improve the convergence properties of a gradient-based optimizer. GD-based methods have demonstrated significant success in learning controllers for uncertain environments, as well as in system identification and adaptive control.

Despite their effectiveness, a key challenge persists: the closed-loop trajectory behavior---how system states evolve over time---is typically an indirect outcome of weight tuning or cost-function optimization. Traditional methods rely on defining an objective function, applying an optimization algorithm, and then observing the resulting state trajectories. If these trajectories do not meet performance expectations, the objective function often requires manual adjustments, leading to a cumbersome iterative tuning process. Furthermore, this process is susceptible to "reward hacking," where the optimized policy achieves a low-cost function value but deviates from the designer's intended behavior.

In our previous work, we proposed a fundamentally different perspective by directly shaping system trajectories through a gradient-descent-like closed-loop approach. We introduced a novel parameterization of the stable closed-loop dynamics where $A,B$ are the system matrices, $K$ is a feedback gain, and ${\Gamma,P} \succ 0$ represent a GD step and a quadratic Lyapunov cost matrix, respectively. This formulation ensures that the closed-loop system behaves analogously to a GD update applied to the Lyapunov function ${V{(x_{k})}} = {x_{k}^{\top}Px_{k}}$, leading to the explicit trajectory update dynamic Rather than iteratively adjusting an unknown cost function to produce desired state trajectories, we directly impose a controlled gradient flow on the system states.

This trajectory-oriented perspective offers several advantages. Firstly, it provides explicit trajectory control. The gradient formulation provides direct control over the trajectory shape, eliminating the need for trial-and-error cost function tuning. Secondly, it quantifies robustness by the step size. For a small step size, closed-loop eigenvalues have small variations. Lastly, it unifies with a Linear Quadratic Regulator (LQR). We established theoretical connections between our approach and classical optimal control, showing that LQR solutions can be naturally represented in this setting.

One of the key challenges in the proposed approach is the definition of the preconditioning matrix $\Gamma$, which is generally non-trivial. To address this issue, we use a natural GD framework as the update rule for the state-space evolution. We demonstrate that, in this formulation, $\Gamma$ corresponds to the covariance matrix of the state vector of the closed-loop system, providing a meaningful interpretation: the magnitude of updates in state space is directly influenced by the uncertainty level, as quantified by the covariance matrix. This insight establishes a direct link between control adjustments and the available information in the system. Furthermore, we derive theoretical stability conditions and step-size constraints to ensure robust implementation. The effectiveness of the proposed approach is validated through simulations on the Quanser rotary inverted pendulum benchmark, demonstrating predictable closed-loop behavior compared to the LQR method.

Notation: Let ${\mathbb{R}}^{m \times n}$ denote the real linear space for all real matrices with dimensions $m \times n$. $\mathbb{N}$ is the set of natural numbers. A positive (semi) definite matrix $P \in {\mathbb{R}}^{n \times n}$ is denoted by $P \succ {0,{({P \succcurlyeq 0})}}$. The transpose of a matrix $Q$ is denoted by $Q^{\top}$. The eigenvalues of a square matrix $A \in {\mathbb{R}}^{n \times n}$ are denoted by ${{{\lambda_{i}{(A)}},i} = 1},{\ldots,n}$ and the spectral radius of $A$ is denoted by ${\rho{(A)}} = {\max{\{{|\lambda_{1}|},\ldots,{|\lambda_{n}|}\}}}$. The gradient of the function ${f{(x)}} \in {\mathbb{R}}$ with respect to $x \in {\mathbb{R}}^{n}$ is denoted by ${{\nabla_{x}f}{(x)}} \in {\mathbb{R}}^{n}$.

## System Model and Problem Description

Consider a linear time-invariant (LTI) stochastic discrete-time system of the form where $k \in {\mathbb{N}}$, $x_{k} \in {\mathbb{R}}^{n}$ is the system's state, and $u_{k} \in {\mathbb{R}}^{m}$ is the control input. In addition, $A$ and $B$ are transition and input matrices of appropriate dimensions, respectively. The noise of the system $\omega_{k} \in {\mathbb{R}}^{n}$ is governed by a Gaussian distribution $\mathcal{N}{(0,W)}$ where $W \in {\mathbb{R}}^{n \times n} \succ 0$ is its covariance matrix. Throughout this paper, a linear control policy is used The dynamical system evolves stochastically due to the additive Gaussian noise $\omega_{k}$. Using the linear control policy, the distribution of the state $x_{k}$ at time $k$ is given by $x_{k} \sim {\mathcal{N}{(\mu_{k},\Sigma_{k})}}$, where the mean $\mu_{k}$ and the covariance $\Sigma_{k}$ are updated respectively as follows The term ${({A + {BK}})}\Sigma_{k}{({A + {BK}})}^{\top}$ captures how the closed-loop dynamics influence the propagation of uncertainty.

A key challenge in closed-loop controller design using LQR is ensuring that the resulting trajectories exhibit desired convergence properties while minimizing deviations due to disturbances. Traditional methods, such as optimal control and reinforcement learning, typically optimize a predefined cost function to tune $K$, indirectly shaping the closed-loop behavior. If the resulting optimal control solution is not satisfactory, the cost parameter must be adjusted. However, the map from the cost parameters to the low-level system behavior is unknown, which makes it challenging to achieve the designer's intention by adjusting the cost parameter. In this work, we propose an alternative approach where the closed-loop dynamics are parameterized in a GD-inspired framework. This formulation ensures that the state updates follow a gradient-descent-like behavior. We gain direct control over trajectory shaping rather than relying on cost-function tuning. This approach provides a geometric interpretation of closed-loop control.

### Basics of Gradients

Gradients play a fundamental role in optimization and control. In the context of machine learning and control systems, gradients are used to iteratively adjust parameters in order to minimize a given cost function. Traditional gradient-based methods rely on first-order derivatives to provide a direction of improvement, while more advanced techniques, such as natural gradients, refine this approach by incorporating information about the underlying geometry of the parameter space.

### GD Algorithm

In the standard GD, the update rule for minimizing a cost function $J{(\theta)}$ with respect to parameters $\theta$ is where $\alpha > 0$ is the step size. This method works in an Euclidean parameter space, assuming that all directions have equal importance and are scaled uniformly. However, when the parameter space is curved or highly anisotropic, standard GD can suffer from slow convergence.

### Natural GD Algorithm

Natural gradients are an extension of GD that accounts for the geometry of the parameter space. Instead of using the Euclidean gradient, the natural gradient uses an alternative direction based on the local curvature of the space. The natural gradient update is defined as where $G{(\theta_{k})}$ is the Fisher Information Matrix (FIM), defined as with $p_{\theta_{k}}{(z_{k})}$ being the Probability Distribution Function (PDF) parameterized by $\theta_{k}$. $G{(\theta_{k})}^{- 1}$ serves as a preconditioner, transforming the gradient into a coordinate system that respects the curvature of the cost surface. The preconditioning approach significantly improves convergence in ill-conditioned landscapes, ensuring more stable and efficient parameter updates.

## From Basic GD to Natural GD in state-space

This section explores the evolution of GD methods applied in state space, beginning from the standard formulation and advancing towards natural gradient techniques that account for system curvature and structure.

### Standard GD

Noise-free linear dynamical systems are considered in Esmzad and Modares. GD updates for this case is given by where $V{(x_{k})}$ and $\alpha > 0$ are the cost function and a step size respectively. This method assumes an isotropic state space where all directions are equally important. However, when the landscape of $V{(x_{k})}$ is highly anisotropic (e.g., elongated level sets), standard GD can suffer from slow convergence and oscillatory behavior.

### Preconditioned GD

Again for noise free linear dynamical system in Esmzad and Modares, one can consider a preconditioning matrix $\Gamma$, which rescales the gradient update where $\Gamma$ is a positive definite matrix that adjusts the step size in different directions. If $\Gamma$ is chosen appropriately, this method can significantly accelerate convergence by better aligning the update with the geometry of $V{(x_{k})}$. However, it requires fine-tuning.

### Natural GD

In this paper, we consider linear systems subject to Gaussian noise so we will give the natural GD update for $\mu_{k}$. The natural gradient method refines preconditioned GD by using the inverse FIM, $G{(\mu_{k})}$, as the preconditioner where $G{(\mu_{k})}$ accounts for the curvature of the state space and $\alpha > 0$. Unlike standard GD, which uses the Euclidean gradient, the natural gradient follows the Riemannian structure of the space, leading to more efficient updates. $G{(\mu_{k})}$ can be replaced by a Hessian approximation or another metric tensor that captures the local curvature of $V{(x_{k})}$. In control applications, such matrices arise naturally in system identification and adaptive control, where the uncertainty in the state of the system can be quantified through inverse covariance matrices as it is outlined in the next section.

## Natural GD for Control

Natural gradient methods have been widely recognized for their ability to enhance convergence rates in optimization by accounting for the curvature of the cost landscape. Similarly, in the context of state-space control, the use of a positive-definite preconditioning matrix $\Gamma$ provides a powerful mechanism for improving convergence rates. The gradient preconditioning adapts the descent direction and magnitude to the underlying geometry of the system dynamics, ensuring more efficient convergence.

### Computing the FIM

The FIM, $G{(\mu_{k})}$, quantifies the curvature of the likelihood $p{(x_{k})}$ in the state space and provides insight into the sensitivity of the likelihood to state changes. For the stochastic system dynamical system, the PDF of the state $x_{k} \sim {\mathcal{N}{(\mu_{k},\Sigma_{k})}}$ is given by the following Gaussian distribution The log-likelihood of $p{(x_{k})}$ is given by Taking the gradient of ${\log p}{(x_{k})}$ with respect to $\mu_{k}$ Substituting into the FIM definition in yields The FIM, $G{(\mu_{k})}$, provides a measure of the amount of information that the state $x_{k}$ carries about the underlying system trajectories. Here, it reduces to the inverse covariance matrix $\Sigma_{k}^{- 1}$, reflecting the precision (inverse uncertainty) in the Gaussian model. We will use the covariance matrix of the state of the closed-loop system as a natural preconditioner in the GD-based control framework and in the next section, we derive explicit formulations for designing the control gain $K$.

### Controller Design Using Stationary Covariance

To simplify the derivations and facilitate the analysis of the proposed control framework, we consider the steady state covariance matrix, i.e., $\Sigma_{k + 1} = \Sigma_{k} = \Sigma$. Theorem 1 encapsulates the core contribution of this work.

### Theorem 1

Consider the system and assume that $(A,B)$ is controllable. Assume that $\alpha > 0$ is given and $0 < \lambda < 1$. Let $Y,F,\Sigma,M$ denote a feasible solution to the following linear problem Then, the preconditioned natural GD control in with ${V{(x_{k})}} = {{\mathbb{E}}_{x_{k} \sim {\mathcal{N}{(\mu_{k},\Sigma_{k})}}}\left\lbrack {x_{k}^{\top}Y^{- 1}x_{k}} \right\rbrack}$ and ${G{(\mu_{k})}} = \Sigma^{- 1}$ makes the closed-loop dynamics $A + {BK}$ with $K = {FY^{- 1}}$ $\lambda -$contractive (and thus stable).

### Proof

Let $P = Y^{- 1}$. Consider the following Lyapunov candidate and let ${G{(\mu_{k})}} = \Sigma^{- 1}$. As a result, the natural GD reads By selecting $\alpha$, one can ensure the natural GD is contractive and thus stable; i.e. ${\rho{({I - {2\alpha\Sigma P}})}} < 1$.

To design the controller gain $K$ from the preconditioned GD control design, we introduce a new parametrization of the closed-loop dynamics as ${A + {BK}} = {I - {\alpha\Sigma P}}$, which is equivalent to (17a). Now, we show that $K = {FY^{- 1}}$ makes the mean of the closed-loop system $\lambda -$contractive. The controller gain $K$ makes the closed loop system $\lambda$-contractive, if Multiplying both sides of the above inequality with $P^{- 1} = Y$ from left and right and using ${A + {BK}} = {I - {2\alpha\Sigma P}}$, one gets which is equivalent to (17b) using the Schur complement lemma. In the preconditioned GD control, we select the FIM as ${G{(\mu_{k})}} = \Sigma^{- 1}$. The stationary closed-loop covariance using the controller gain $K$ reads which couples the unknown variables $\Sigma$ and $K$ and thus should be incorporated in the design. One can write as or equivalently $M^{- 1} \preceq {P\Sigma P}$ meaning that there exists a $\Pi \succeq 0$ such that ${{P\Sigma P} - M^{- 1} - \Pi} = 0$. Using ${P\Sigma P} = {M^{- 1} + \Pi}$, one gets where the last term in the right hand side is positive because $\Pi \succeq 0$. As a result, one has Inequalities and are equivalent to (17d) and (17c) respectively by the Schur complement. This completes the proof. ∎

### Theorem 2 (Range of $\alpha$ for closed-Loop stability)

Consider the dynamical system . Assume that $(A,B)$ is controllable. Assume that the controller gain $K$ is designed according to Theorem 1. Then, the closed-loop dynamics $A + {BK}$ is asymptotically stable if and only if

### Proof

The eigenvalues of $A + {BK}$ are given by Note that the eigenvalues of $\Sigma P$; i.e. $\lambda_{i}{({\Sigma P})}$ are all real, and that is because $\Sigma P$ is similar to a positive definite matrix. To see this point, take the similarity transform as $T = P^{- \frac{1}{2}}$. Then ${T^{- 1}\Sigma PT} = {P^{\frac{1}{2}}\Sigma P^{\frac{1}{2}}}$ which is a positive definite matrix and has real eigenvalues. Since $\Sigma P$ is similar to $P^{\frac{1}{2}}\Sigma P^{\frac{1}{2}}$, $\lambda_{i}{({\Sigma P})}$ are also real. As a result, is simplified to which simplifies to (25 ‣ 4.2 Controller Design Using Stationary Covariance ‣ 4 Natural GD for Control ‣ Natural Gradient Descent for Control")) ∎

### Remark 1

Note that the range for $\alpha$ in (25 ‣ 4.2 Controller Design Using Stationary Covariance ‣ 4 Natural GD for Control ‣ Natural Gradient Descent for Control")) cannot be verified before design as the values of $\Sigma$ and $P$ depend on the value of $\alpha$. However, this range tells us that smaller values of $\alpha$ will decrease the convergence rate and larger values of $\alpha$ will increase the convergence speed. So, $\alpha$ can serve as an intuitive closed-loop behavior-tweaking variable.

### Corollary 1

(Sensitivity to Step Size). The sensitivity of the closed-loop eigenvalues to the step size $\alpha$ is given by The sensitivity of eigenvalues increases linearly with $\alpha$.

### Proof

The eigenvalues of $A + {BK}$ are Differentiating with respect to $\alpha$ results. ∎

### Discussion

Stability conditions ensure the existence of a Lyapunov function that decreases along system trajectories, guaranteeing stability. However, these conditions do not necessarily provide an explicit mechanism for *shaping* the trajectories themselves. In contrast, our framework leverages a GD-like formulation to directly influence how the state evolves at each step, thereby offering more transparency over closed-loop behavior.

Classical LQR designs the gain matrix by minimizing a quadratic cost function, but there is no straightforward, systematic way to target specific *transient* behaviors beyond fine-tuning the weighting matrices $Q$ and $R$. The proposed natural GD approach, on the other hand, utilizes a step-size parameter $\alpha$ and a preconditioning (covariance) matrix $\Sigma$ to shape the trajectory explicitly. Adjusting $\alpha$ translates directly into changing the rate of convergence ($\Sigma$ defines how strongly each direction in the state space is scaled in the gradient step) where smaller $\alpha$ yields smoother but slower convergence, and larger $\alpha$ leads to faster convergence, albeit at the risk of oscillations if too large.

Figure 1: Quanser’s Qube-Servo 2 platform In contrast to methods where the cost function is purely chosen by the designer, our approach *derives* a cost function *by design* from the natural GD-based parameterization. This decouples the choice of cost function from the low-level behavior.

## Simulation Results

To evaluate the proposed natural gradient control method's performance, we conducted simulations on a widely used benchmark platform Quanser rotary pendulum (model QUBE-Servo 2) ^11^1 shown in Figure 1. The system dynamics are represented in discrete time with a sampling interval of $T_{s} = 0.01$ seconds. The state vector is defined as $x = \begin{bmatrix} \theta & \delta & \overset{˙}{\theta} & \overset{˙}{\delta} \end{bmatrix}^{T}$, where $\theta$ (rad) is the rotary arm angle and $\delta$ (rad) is the pendulum angle.

Figure 2: The evolution of the state variables (top four plots) and the control input (the fifth plot) using the natural GD design for various α.

Figure 3: The evolution of the state variables (top four plots) and the control input (the fifth plot) using LQR approach with various Q and R.

The control input $u$ (V) is the voltage applied to the motor. Here, we considered linearized dynamics around its upright equilibrium point. The control strategy aims to stabilize the pendulum in its upright equilibrium while ensuring smooth control effort. Both the natural gradient control method and LQR are employed to regulate the trajectory of the state vector. The discrete-time state-space matrices used in the simulation are given by We compared the natural gradient control method for different values of the step size parameter $\alpha$ with the standard LQR for various choices of weighting matrices $Q$ and $R$. For the natural gradient control method, we choose $\lambda = 0.99$, and the step size values ${\alpha \in {\{ 0.01,0.018,0.025\}}}.$ For the LQR controller, we considered different state and control weighting matrices $Q_{1} = {0.001I}$, $Q_{2} = I$, $Q_{3} = {5000I}$,$R_{1} = 100$, $R_{2} = 1$, and ${R_{3} = 0.001}.$ The comparison between the natural GD approach and LQR control highlights key differences in trajectory shaping and optimal control. In the natural GD method, state evolution is influenced by the step size parameter $\alpha$, with larger values leading to faster convergence but potentially introducing oscillations. This approach provides direct control over trajectory shaping, allowing for intuitive adjustments to the system's behavior.

Figures 2 and 3 show the results of the proposed and LQR approaches, respectively. LQR control optimally balances state regulation and control effort through the careful selection of weighting matrices $Q$ and $R$, ensuring smooth and stable convergence. However, a fundamental limitation of LQR is that the trajectory behavior is not explicitly predictable based on $Q$ and $R$ adjustments. While these matrices influence the control law, their effect on the system's transient response is often indirect and requires trial-and-error tuning. Consequently, achieving a specific trajectory shape in LQR can be challenging, as the resulting state evolution emerges from the Riccati equation rather than being explicitly controlled. On the other hand, the GD-based approach offers a geometric perspective on control, where trajectory updates follow a well-defined GD process. This enables a more transparent and predictable way to shape trajectories directly. If precise trajectory shaping is the priority, the natural GD approach provides greater interpretability. In contrast, LQR remains a reliable choice for energy-efficient and well-balanced state regulation but at the cost of requiring heuristic tuning for transient behavior control.

## Conclusion and Future Directions

This paper introduced a novel closed-loop control framework based on natural GD, using the closed-loop covariance matrix as a preconditioner. By directly shaping system trajectories through a gradient-descent-like update, the proposed approach eliminates the need for indirect cost-function tuning, offering improved interpretability. Theoretical analysis established stability conditions and step-size constraints.

Future research directions include extending the framework to nonlinear and time-varying systems, incorporating state-dependent covariance adaptation, and exploring its integration with reinforcement learning and model predictive control. Additionally, investigating robustness properties under model uncertainties and external disturbances could further enhance the practical applicability of this approach in real-world scenarios.
