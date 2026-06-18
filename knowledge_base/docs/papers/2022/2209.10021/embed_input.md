<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

DiffTune: Auto-Tuning through Auto-Differentiation

Topics include Robotics, Aerial robotics, Graphs, Online algorithms, Optimization, Control, DiffTune.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The performance of robots in high-level tasks depends on the quality of their lower-level controller, which requires fine-tuning. However, the intrinsically nonlinear dynamics and controllers make tuning a challenging task when it is done by hand. In this paper, we present DiffTune, a novel, gradient-based automatic tuning framework. We formulate the controller tuning as a parameter optimization problem. Our method unrolls the dynamical system and controller as a computational graph and updates the controller parameters through gradient-based optimization. The gradient is obtained using sensitivity propagation, which is the only method for gradient computation when tuning for a physical system instead of its simulated counterpart. Furthermore, we use L_1 adaptive control to compensate for the uncertainties (that unavoidably exist in a physical system) such that the gradient is not biased by the unmodelled uncertainties. We validate the DiffTune on a Dubin's car and a quadrotor in challenging simulation environments. In comparison with state-of-the-art auto-tuning methods, DiffTune achieves the best performance in a more efficient manner owing to its effective usage of the first-order information of the system.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Experiments on tuning a nonlinear controller for quadrotor show promising results, where DiffTune achieves 3.5x tracking error reduction on an aggressive trajectory in only 10 trials over a 12-dimensional controller parameter space.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robotic systems are at the forefront of executing intricate tasks, relying on the prowess of their low-level controllers to deliver precise and agile motions. An optimal controller design starts with a meticulous analysis to ensure stability, followed by parameter tuning to achieve the intended performance on real-world robotic platforms. Traditionally, controller tuning is done either by hand using trial-and-error or proven methods for specific controllers (e.g., Ziegler--Nichols method for proportional-integral-derivative (PID) controller tuning ). Nevertheless, manual tuning often demands seasoned experts and is inefficient, particularly for systems with lengthy loop times or extensive parameter space.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To improve efficiency and performance, automatic tuning (or auto-tuning) methods have been investigated. Such methods integrate system knowledge, expert experience, and software tools to determine the best set of controller parameters, especially for the widely used PID controllers. Commercial auto-tuning products have been available since 1980s. A desirable auto-tuning scheme should have the following three qualities: i) stability of the target system; ii) compatibility with physical systems' data; and iii) efficiency for online deployment, possibly in real-time. However, how to design the auto-tuning scheme, simultaneously having the above three qualities, for general controllers, is still a challenge.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Existing auto-tuning methods can be categorized into model-based and model-free. Both approaches iteratively select the next set of parameters for evaluation that is likely to improve the performance over the previous trials. Model-based auto-tuning methods leverage the knowledge of the system model to improve performance, often using the gradient of the performance criterion (e.g., tracking error) and applying gradient descent so that the performance can improve based on the local gradient information. Stability can be ensured by explicitly leveraging knowledge about the system dynamics. However, model-based auto-tuning might not work in a real environment, where the knowledge about the dynamical model might be imperfect. This issue is especially severe when controller parameters are tuned in simulation and then deployed to a physical system.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model-free auto-tuning methods approximate gradient or a surrogate model to improve the performance. Representative approaches include Markov chain Monte Carlo (MCMC), deep neural network (DNN), and Bayesian optimization (BO). Such approaches often make no assumptions about the model and have the advantage of compatibility with physical systems' data owing to their data-driven nature. However, it is hard to establish stability guarantees with most of the data-driven methods (e.g., MCMC and DNN), where empirical methods are often applied. Bayesian optimization has the advantage of establishing stability/safety guarantees, but it can be inefficient when tuning in high-dimensional (e.g., $>$`<!-- -->`{=html}20) parameter spaces.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To overcome the challenges in the auto-tuning scheme, we present DiffTune: an auto-tuning method based on auto-differentiation (AD). Our method is inspired by the "end-to-end" idea from the machine learning community. Specifically, in the proposed scheme, the gradient of the loss function (evaluating the performance of the controller) with respect to the controller parameters can be directly obtained and then applied to gradient descent to improve the performance. DiffTune is generally applicable to tune all the controller parameters as long as the system dynamics and controller are differentiable (we will define "differentiable" in Section III), which is the case with most of the systems. For example, algebraically computed controllers, e.g., with the structure of gain-times-error, are differentiable. Moreover, following the seminal work that differentiates the argmin operator using the Implicit Function Theorem, one can see that controllers relying on solutions of an optimization problem to generate control actions (e.g., model predictive control (MPC), optimal control, safe controllers enabled by control barrier function, linear-quadratic regulator (LQR) ) are also differentiable.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We build DiffTune by unrolling the dynamical system into a computational graph and then applying AD to compute the gradient. Since the structure of the dynamics and controller are untouched by the unrolling operation, the system is still interpretable, which is a distinctive feature compared to the NN-structured dynamics or controllers (widely applied in reinforcement learning). Furthermore, existing tools that support AD (e.g., PyTorch, TensorFlow, JAX, and CasADi ) can be conveniently applied for gradient computation.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, when tuning physical systems, we need gradient information based on the data collected from such systems. In this scenario, the computational graph is broken because the states of the system are obtained from sensors rather than by evaluating the dynamics function. The broken graph forbids the usage of AD over the computational graph. We present an alternative way of gradient computation, called sensitivity propagation, which is based on the sensitivity equation of a dynamical system. It propagates the sensitivity of the system state to the controller parameters in the forward direction in parallel to the dynamics' propagation. Lastly, the gradient of the loss to controller parameters is simply a weighted sum of the sensitivities. Furthermore, uncertainties and disturbances exist in physical systems. If they are not dealt, the resulting gradient based on the nominal dynamics (free of uncertainty and disturbance) will be biased. We propose to use $\mathcal{L}_{1}$ adaptive control to compensate for the uncertainties and disturbances so that the physical system behaves similarly to the nominal system. The uncertainty compensation will preserve the gradient from being biased, thus resulting in more efficient tuning.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

DiffTune enjoys the three earlier mentioned qualities simultaneously: stability is inherited from the controllers with stability guarantees by design; compatibility with physical systems' data is enabled by the sensitivity propagation; efficiency is provided since the sensitivity propagation runs forward in time and in parallel to the system's evolution. We have validated DiffTune in both simulations and experiments. DiffTune achieves smaller loss more efficiently than strong baseline auto-tuning methods AutoTune and SafeOpt in simulations. Notably, in experiments, DiffTune achieves a 3.5x reduction in tracking error in only 10 trials when tuning a nonlinear controller (12-dimensional parameter space) of a quadrotor for tracking an aggressive trajectory, demonstrating the efficacy of the proposed approach.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our contributions are summarized as follows: i) We propose an auto-tuning method for controller parameters over nonlinear dynamical systems and controllers in general forms by formulating the tuning problem as a parameter optimization problem. Only differentiability of the dynamics, controller, and loss function (for tuning) is required. ii) We treat the unrolled system as a computational graph, over which we use auto-differentiation to compute the gradient efficiently. Specifically, we propose sensitivity propagation, which is compatible with data collected from a physical system and can be efficiently computed online. iii) We combine tuning with the $\mathcal{L}_{1}$ adaptive control to compensate for the model uncertainties in a physical system that can bias the computed gradient for tuning. iv) We validate the proposed approach in extensive simulations and experiments, where the compatibility with physical data, stability, and efficiency of DiffTune are demonstrated.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

A previously published paper has studied an extension of DiffTune for hyperparameter-free auto-tuning by optimizing the gradient update, with results validated only by simulated systems. In this article, our focus is to introduce DiffTune to solve the auto-tuning problem with a physical system, which has been validated through extensive experiments in Section VI. We show that simulation-based auto-tuning can lead to parameter overfitting to a particular simulated system, which does not apply to or even fail the physical system (details in Section VI-E). To handle the uncertainties that can bias the gradient used in the auto-tuning of a physical system, we use the $\mathcal{L}_{1}$ adaptive control for uncertainty compensation with the methodology introduced in Section IV-B and experimental results detailed in Section VI-D.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of the paper is organized as follows: Sections II and III review related work and background, respectively, of this paper. Section IV describes our auto-tuning method and sensitivity propagation. We also discuss uncertainty handling when using physical systems' data. Section V shows the simulation results on a Dubins' car and on a quadrotor. Section VI demonstrates the experimental results on a quadrotor. Finally, Section VII concludes the paper.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

where ${\mathbf{θ}} \in {\mathbb{R}}^{p}$ denotes the parameters of the controller, e.g., ${\mathbf{θ}} \in {\mathbb{R}}^{2}$ may represent the P- and D-gain in a PD controller. We assume that the state ${\mathbf{x}}_{k}$ can be measured directly or, if not, an appropriate state estimator is used. Furthermore, we assume the dynamics and controller are differentiable, i.e., the Jacobians $\nabla_{\mathbf{x}}f$, $\nabla_{\mathbf{u}}f$, $\nabla_{\mathbf{x}}h$, and $\nabla_{\mathbf{θ}}h$ exist, which widely applies to general systems.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The tuning task adjusts $\mathbf{θ}$ to minimize an evaluation criterion, denoted by $L{( \cdot )}$, which is a differentiable function of the desired states $\overline{\mathbf{x}}$, actual states $\mathbf{x}$, and control ations $\mathbf{u}$ over a time interval of length $N$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Note that problem (P) searches for controller parameter $\mathbf{θ}$ to minimize the loss $L$ subject to the system's dynamics and a chosen controller (to be tuned). Problem (P) is generally nonconvex due to the nonlinearity in dynamics $f$ and controller $h$. We will introduce our method, DiffTune, in Section IV for auto-tuning, especially for tuning a controller for a physical system.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Method", "weight": 1.0} -->

We use a gradient-based method to solve problem (P) due to its nonconvexity, where the system performance is gradually improved by adjusting the controller parameters using gradient descent. We unroll the dynamical system and controller into a computational graph. Figure illustrates the unrolled system, which stacks the iterative procedure of state update via the "dynamics" and control-action generation via the "controller." The gradient $\nabla_{\mathbf{θ}}L$ is then applied to update the parameters $\mathbf{θ}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Method", "weight": 1.0} -->

where $\mathcal{P}_{\Theta}$ is the projection operator that projects its operand into the set $\Theta$, and $\alpha$ is the learning rate. The feasible set $\Theta$ is used here to ensure the stability of the system, where $\Theta$ can be determined via the Lyapunov analysis or empirically determined by engineering practice.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Method", "weight": 1.0} -->

What remains to be done is to compute the gradient $\nabla_{\mathbf{θ}}L$, for which AD can be used when the computational graph is complete (e.g., in simulations). AD can be conveniently implemented using off-the-shelf tools like PyTorch, TensorFlow, JAX, or CasADi: one will program the computational graph using the dynamics and controller and set the parameter $\mathbf{θ}$ with respect to which the loss function will be differentiated.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Method", "weight": 1.0} -->

However, AD methods cannot incorporate data (state and control) from a physical system because AD relies on a complete computation graph, whereas the computational graph corresponding to a physical system is broken. Specifically, the dynamics have to be evaluated each time to obtain a new state, which is not the case in a physical system: the states are obtained through sensor measurements or state estimation rather than evaluating the dynamics (see the comparison in Figs. 2(a) and 2(b)). This explains why the computational graph is broken when considered for a physical system. Thus, AD can only be applied to auto-tuning in simulations, forbidding its usage with physical systems' data. We introduce sensitivity propagation next to address the compatibility with physical systems' data.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The sensitivity propagation and forward-mode AD share the same formula as in and. The difference lies in what type of data is applied. Two types of data are considered: The first type is from simulation, where $\mathbf{x}_{k}$ is obtained by the computation $\mathbf{x}_{k} = {f{(\mathbf{x}_{k - 1},\mathbf{u}_{k - 1})}}$; the second type is sampled from a physical system, where $\mathbf{x}_{k}$ is obtained by either sensor measurements or state estimation, which cannot be represented as the evaluation a mathematical expression. In principle, forward-mode AD can only work with data of the first type, which limits its application to auto-tuning in simulations only. Sensitivity propagation, however, can work with both types of data. The most significant usage is associated with the second-type data, which provides a straightforward method of tuning a physical system. When applied to the first type of data, the sensitivity propagation is equivalent to the forward-mode AD.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 2", "weight": 1.0} -->

One may notice that the sensitivity state $\partial{\mathbf{x}_{0}/{\partial{\mathbf{θ}}}}$ is set to a zero matrix. This initialization relates to how the sensitivity state is interpreted. Suppose we have sampled the sequence of state ${\{\mathbf{x}_{k}\}}_{{k = 0}:N}$ and control ${\{\mathbf{u}_{k}\}}_{{k = 0}:{N - 1}}$ subject to a certain parameter $\mathbf{θ}$. Consider a small perturbation $\mathbf{\epsilon} \in {\mathbb{R}}^{p}$ to $\mathbf{θ}$. The sensitivity states allow inferring about the state and control sequence subject to the parameter being ${\mathbf{θ}} + \mathbf{\epsilon}$ using first-order approximation (without implementing the controller with the parameter ${\mathbf{θ}} + \mathbf{\epsilon}$ and then sampling the data).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 2", "weight": 1.0} -->

The sensitivity state $\partial{\mathbf{x}_{k}/{\partial{\mathbf{θ}}}}$ is initialized at zero such that ${\mathbf{x}_{0}{({{\mathbf{θ}} + \mathbf{\epsilon}})}} = {\mathbf{x}_{0}{({\mathbf{θ}})}}$ to ensure the same initial state despite parameter change. Therefore, how the state $\mathbf{x}_{k}{({{\mathbf{θ}} + \mathbf{\epsilon}})}$ will change subject to the $\mathbf{\epsilon}$ parameter perturbation can be inferred from the sensitivity $\partial{\mathbf{x}_{k}/{\partial{\mathbf{θ}}}}$ which simply evolves with the sensitivity equation. Furthermore, the sensitivity states allow for auto-tuning without hyperparameters (e.g., learning rate $\alpha$), which is detailed.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Although AD cannot be applied to the entire computational graph when using data from a physical system, it can still be applied to obtain the Jacobians $\nabla_{\mathbf{x}_{k}}f$, $\nabla_{\mathbf{u}_{k}}f$, $\nabla_{\mathbf{x}_{k}}h$, and $\nabla_{\mathbf{θ}}h$. Since the iterative structure in remains the same among iterations, AD packages like PyTorch, TensorFlow, JAX, and CasADi can be applied for evaluating these Jacobians.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 3", "weight": 1.0} -->

0: Initial state ${\overset{\sim}{\mathbf{x}}}_{0}$, initial parameter θ0, feasible set Θ, horizon N, desired state ${\{{\overline{\mathbf{x}}}_{k}\}}_{{k = 0}:N}$, step size α, formulas of the Jacobians {∇xf, ∇uf, ∇xh, ∇θh}, and termination condition 𝒞.
3: Set ${\mathbf{x}}_{0}\leftarrow{\overset{\sim}{\mathbf{x}}}_{0}$ and ∂x0/∂θ ← 0.
5: Obtain xk from system and compute uk using.
6: Update ∂xk + 1/∂θ and ∂uk/∂θ using.
8: Store ∂xk + 1/∂θ, ∂uk/∂θ, ∂L/∂xk and ∂L/∂uk in memory.
10: Compute ∇θL using and update θ.
12: return the tuned parameter θ* ← θ.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 3", "weight": 1.0} -->

The unique aspect of sensitivity propagation is its compatibility with data from a physical system. Using such data for tuning is vital because the ultimate goal is to improve the performance of a physical system instead of its simulated counterpart. Despite the fidelity of the model in simulation, the physical system will have discrepancies with the model, leading to sub-optimal performance if the parameters come from simulation-based tuning. This phenomenon is part of the sim-to-real gap, which leads to degraded performance on physical systems compared to their simulated counterparts. The sensitivity propagation, unlike the forward- or reverse-mode AD, can still be applied to compute the gradient while using data collected from the physical system.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-B Auto-tuning with data from physical systems", "weight": 1.0} -->

The core of DiffTune is to obtain $\nabla_{\mathbf{θ}}L$ from physical systems' data and then apply projected gradient descent.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-B Auto-tuning with data from physical systems", "weight": 1.0} -->

However, model uncertainties and noise have to be carefully handled when using such data. Controller design usually uses the nominal model of the system, which is uncertainty- and noise-free. However, both uncertainties and noise exist in a physical system. If not dealt, then the uncertainties and noise will contaminate the sensitivity propagation, leading to biased sensitivities and, thus, biased gradient $\nabla_{\mathbf{θ}}L$, which results in inefficient parameter update. Since noise can be efficiently addressed by filtering or state estimation, our focus will be on handling the model uncertainties.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-B Auto-tuning with data from physical systems", "weight": 1.0} -->

Existing methods that can compensate for the uncertainties can be applied to mitigate this issue. For example, the $\mathcal{L}_{1}$ adaptive control ($\mathcal{L}_{1}$AC) is a robust adaptive control architecture that has the advantage of decoupling estimation from control, thereby allowing for arbitrarily fast adaptation subject only to hardware limitations. It can be augmented to the controller to be tuned such that the resulting system, even though suffering from model uncertainties, behaves like a nominal system by $\mathcal{L}_{1}$AC's compensation for the uncertainties. To proceed with the illustration of how $\mathcal{L}_{1}$AC works, we use continuous-time dynamics to stay consistent with the notation in the majority of the $\mathcal{L}_{1}$AC references.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-B Auto-tuning with data from physical systems", "weight": 1.0} -->

where we use ${\mathbf{x}}^{\star}$ to denote the nominal state, $B_{\text{m}} \in {\mathbb{R}}^{n \times m}$ to denote the control input matrix and $\mathbf{u}$ to denote the control input to the system. For example, in the tuning setup, $\mathbf{u}$ is chosen as the baseline control ${\mathbf{u}}_{h}$ from the to-be-tuned controller $h$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-B Auto-tuning with data from physical systems", "weight": 1.0} -->

The adaptive control ${\mathbf{u}}_{\text{ad}}$ aims to cancel out the matched uncertainty ${\mathbf{σ}}_{\text{m}}$, i.e., ${\parallel{{\mathbf{σ}}_{\text{m}} + {\mathbf{u}}_{\text{ad}}}\parallel} \approx 0$ (see for details of how $\mathcal{L}_{1}$AC is implemented). Specifically, $\mathcal{L}_{1}$AC estimates the uncertainty $\mathbf{σ}$ based on a state predictor and adaptation law. The state predictor propagates the state prediction $\hat{\mathbf{x}}$ based on the estimated uncertainty $\hat{\mathbf{σ}}$ and control inputs ${\mathbf{u}}_{h}$ and ${\mathbf{u}}_{\text{ad}}$, i.e.,

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-B Auto-tuning with data from physical systems", "weight": 1.0} -->

with $T_{s}$ being the sample time of $\mathcal{L}_{1}$AC, expm$( \cdot )$ denoting matrix exponential, and $I$ being the identity matrix. The uncertainty's estimation error $\parallel{{\mathbf{σ}} - \hat{\mathbf{σ}}}\parallel$ is shown to be uniformly bounded under a set of mild regularity assumptions. Once the estimated uncertainty $\hat{\mathbf{σ}}$ is computed, the compensation ${\mathbf{u}}_{\text{ad}}$ is obtained by low-pass filtering $\hat{\mathbf{σ}}$, i.e.,

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-B Auto-tuning with data from physical systems", "weight": 1.0} -->

with $s$ being the complex variable in the frequency domain, and $C{(s)}$ is the transfer function of the low-pass filter (LPF). The LPF is used here because the compensation is limited by the bandwidth of the actuator, where only the low-frequency components of $\hat{\mathbf{σ}}$ can be implemented by the actuator. It can be shown that the residual $\parallel{{\mathbf{σ}}_{\text{m}} + {\mathbf{u}}_{\text{ad}}}\parallel$ is bounded, and the error norm $\parallel{{\mathbf{x}}^{\star} - {\mathbf{x}}}\parallel$ between the nominal state ${\mathbf{x}}^{\star}$ and the closed-loop state $\mathbf{x}$ in is uniformly bounded both in transient and steady-state, which renders the uncertain system behaving similar to the nominal system.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-B Auto-tuning with data from physical systems", "weight": 1.0} -->

Therefore, the sensitivity propagation remains unchanged while $\mathcal{L}_{1}$AC handles the uncertainties. We will illustrate how the $\mathcal{L}_{1}$AC facilitates the auto-tuning of a physical system in Sections V and VI.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 4", "weight": 1.0} -->

Note that $\mathbf{u}_{\text{ad}}$ is not applied to the sensitivity propagation (only $\mathbf{u}_{h}$ is applied) because $\mathbf{u}_{\text{ad}}$ is used to cancel out the uncertainty ${\mathbf{σ}}_{\text{m}}$ to preserve the validity of the nominal dynamics.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-C Open-source DiffTune toolset", "weight": 1.0} -->

Our toolset DiffTuneOpenSource is publicly available, which facilitates users' DiffTune applications in two ways. First, it enables the automatic generation of the partial derivatives required in sensitivity propagation. In this way, a user only needs to program the dynamics and controller, eliminating the need for additional programming of the partial derivatives. Second, we provide a template that allows users to quickly set up DiffTune for custom systems and controllers. The Dubin's car and quadrotor cases used in Section V are used as examples to illustrate the usage of the template.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Simulation results", "weight": 1.0} -->

In this section, we implement DiffTune for a Dubin's car and a quadrotor in simulations, where the controller in each case is differentiable. For all simulations, we use ode45 to obtain the system states by integrating the continuous-time dynamics (mimicking the continuous-time process on a physical system). The states are sampled at discrete-time steps. We use the sensitivity propagation to compute $\nabla_{\mathbf{θ}}L$, where the discrete-time dynamics in are obtained by forward-Euler discretization.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Simulation results", "weight": 1.0} -->

We intend to answer the following questions through the simulation study: 1. How does DiffTune compare to other auto-tuning methods? Since equipment wear is not an issue for tuning in simulations, we conduct sufficiently many trials to understand the asymptotic performance of auto-tuning methods for comparison. 2. How can the tuned parameters generalize to other unseen trajectories during tuning? 3. How does $\mathcal{L}_{1}$AC help tuning when the system has uncertainties? We show our main results in the following subsections while supplying the details of configurations in Appendices A and B.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-A Dubin's car", "weight": 1.0} -->

where the state contains five scalar variables, $(x,y,\psi,v,\omega)$, which stand for horizontal position, vertical position, yaw angle, linear speed in the forward direction, and angular speed. The control actions in this model include the force $F \in {\mathbb{R}}$ in the forward direction of the vehicle and the moment $M \in {\mathbb{R}}$. The vehicle's mass and moment of inertia are known and denoted by $m$ and $J$, respectively. The feedback tracking controller with tunable parameter ${\mathbf{θ}} = {(k_{\mathbf{p}},k_{\mathbf{v}},k_{\psi},k_{\omega})}$ is given by

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-A Dubin's car", "weight": 1.0} -->

Comparison to other methods: We compare DiffTune with strong baseline auto-tuning methods: AutoTune, SafeOpt, and GIBO. Note that these baseline methods are model-free probabilistic approaches that do not require knowledge of system dynamics and control. We compare the tuning performance on a circular trajectory and assign 100 trials in each method. Other details of implementation are available in Appendix A. The results are shown in Fig.. The final tracking errors obtained by all methods are similar, and all are below 0.05 m. DiffTune achieves the fastest error reduction in the first 20 trials due to its efficient usage of the system's first-order information that can effectively guide the parameter search. After 20 trials, GIBO achieves the minimum error, indicating that the GP model has captured the mapping from the control parameters to the objective function. The performance of AutoTune and SafeOpt is inferior to that of DiffTune and GIBO, with a slower error reduction and larger errors at the end of 100 trials.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-A Dubin's car", "weight": 1.0} -->

However, GIBO and AutoTune are limited to auto-tuning in simulations because they require randomly sampled parameters for controller implementation and rollouts for performance evaluation, and then decide how to pick the next candidate parameter. This procedure leads to huge mechanical wear and tear when applied to auto-tuning of a physical system. SafeOpt can produce acceptable performance by the end of the 100 trials, albeit the RMSE reduction is not smooth. The performance of SafeOpt relies on both prior knowledge (including the kernel function and its parameters and the range of feasible parameters) and the parameter space's discretization (for searching maximizers), both of which are difficult to tune (as hyperparameters in auto-tuning).

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-A Dubin's car", "weight": 1.0} -->

Generalization: We illustrate the generalization of DiffTune in a batch tuning example. We select nine trajectories as the batch tuning set. These trajectories are generated by composing constant, sinusoidal, and cosinusoidal signals for the desired linear and angular velocities. The maximum linear speed and angular speed are set to 1 m/s and 1 rad/s, respectively, to represent trajectories in one operating region. The four control parameters are all initialized at 2. The tuning proceeds by batch gradient descent on the tuning set. The controller parameters converge to ${(k_{\mathbf{p}},k_{\mathbf{v}},k_{\psi},k_{\omega})} = {(18.83,6.69,14.97,2.66)}$. We then test the tuned parameters on four testing trajectories (unseen in the tuning set) with lemon-, twist-, peanut-, and spiral-shape, as shown in Fig.. The tuned parameters lead to better tracking performance than the untuned ones.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-A Dubin's car", "weight": 1.0} -->

The loss on the testing set is compared to the untuned parameters in Table I. It can be observed that the tuned parameters generalize well and are robust to the previously unseen trajectories.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-A Dubin's car", "weight": 1.0} -->

Handling uncertainties: In this simulation, we implement the $\mathcal{L}_{1}$AC to facilitate the compensation for the uncertainties during tuning. For the $\mathcal{L}_{1}$AC, we use the piecewise-constant adaptation law and a 1st-order low-pass filter with 20 rad/s bandwidth. In this simulation, we inject additive force $0.1a_{1}{\sin{(t)}}$ and moment $0.1a_{2}{\cos{(t)}}$ to the control channels in the dynamics as uncertainties from the environment. To understand how the performance is impacted by the uncertainties, we set $(a_{1},a_{2})$ to a $10 \times 10$ grid such that $a_{1}$ and $a_{2}$ take integer values from 1 to 10, representing gradually intensified uncertainties. The four control parameters are all initialized at 10.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-A Dubin's car", "weight": 1.0} -->

We tune the controller parameters with both $\mathcal{L}_{1}$ on and $\mathcal{L}_{1}$ off, where the sensitivity propagation in both cases is based on the nominal model. Different from the generalization test, we only tune the parameters on one trajectory (the focus is on how to reduce the impact of the uncertainties that are not considered in the nominal dynamics). The step size and termination criterion remain the same as before. To clearly understand the individual role of DiffTune and the $\mathcal{L}_{1}$AC in tuning, we conduct an ablation study. The losses are shown in Fig.. It can be observed that both DiffTune and $\mathcal{L}_{1}$AC improve the performance, and a combination of both achieves the best overall performance: the $\mathcal{L}_{1}$AC does so by compensating for the uncertainties, whereas DiffTune does so by driving the parameters to achieve smaller tracking error.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-A Dubin's car", "weight": 1.0} -->

Although the two heatmaps with $\mathcal{L}_{1}$ on show indistinguishable colors within each itself, the actual loss values have minor fluctuations.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-B Quadrotor", "weight": 1.0} -->

where ${\mathbf{p}} \in {\mathbb{R}}^{3}$ and ${\mathbf{v}} \in {\mathbb{R}}^{3}$ are the position and velocity of the quadrotor, respectively, $R \in {SO{}}$ is the rotation matrix describing the quadrotor's attitude, $\mathbf{\Omega} \in {\mathbb{R}}^{3}$ is the angular velocity, $g$ is the gravitational acceleration, $m$ is the vehicle mass, $J \in {\mathbb{R}}^{3 \times 3}$ is the moment of inertia (MoI) matrix, $f$ is the collective thrust, and ${\mathbf{M}} \in {\mathbb{R}}^{3}$ is the moment applied to the vehicle.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-B Quadrotor", "weight": 1.0} -->

The wedge operator $\cdot^{\times}:{\mathbb{R}}^{3}\rightarrow{\mathfrak{s}}{\mathfrak{o}}{}$ denotes the mapping to the space of skew-symmetric matrices. The control actions $f$ and $\mathbf{M}$ are computed using the geometric controller. The geometric controller has a 12-dimensional parameter space, which splits into four groups of parameters: ${\mathbf{k}}_{\mathbf{p}}$, ${\mathbf{k}}_{\mathbf{v}}$, ${\mathbf{k}}_{R}$, ${\mathbf{k}}_{\mathbf{\Omega}}$ (applying to the tracking errors in position, linear velocity, attitude, and angular velocity, respectively). Each group is a 3-dimensional vector (associated with the $x$-, $y$-, and $z$-component in each's corresponding tracking error).

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-B Quadrotor", "weight": 1.0} -->

The feasible sets of controller parameters are set as ${\mathbf{k}}_{\mathbf{p}} \in {\lbrack 15,24\rbrack}$, ${\mathbf{k}}_{\mathbf{v}} \in {\lbrack 4,16\rbrack}$, ${\mathbf{k}}_{\mathbf{R}} \in {\lbrack 8,12\rbrack}$, and ${\mathbf{k}}_{\mathbf{\Omega}} \in {\lbrack 0.1,3\rbrack}$. We set the loss function as the squared norm of the position tracking error, summed over a horizon of 10 s. We add zero-mean Gaussian noise to the position, linear velocity, and angular velocity (with standard deviation 0.1 m, 0.1 m/s, 1e-3 rad/s, respectively).

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-B Quadrotor", "weight": 1.0} -->

Comparison to other methods: We compare DiffTune with strong baselines AutoTune, SafeOpt-PSO, and GIBO. Note that these baseline methods are model-free probabilistic approaches that do not require knowledge of system dynamics and control. The middle is a variant of the SafeOpt, which applies Particle Swarm Optimization (PSO) to enable adaptive discretization of the parameter space. The original SafeOpt is not applicable because it requires fine discretization of the parameter space to search for the maximizer, which suffers from the curse of dimensionality. Specifically, auto-tuning of the geometric controller requires at least $12^{M}$ discretization points if each parameter admits at least $M$ discretization points.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-B Quadrotor", "weight": 1.0} -->

The detailed settings of AutoTune and SafeOpt in this example are shown in Appendix B. We compare the three auto-tuning methods on three trajectories, where 100 trials are performed for each method on each trajectory. The results are shown in Fig., where DiffTune achieves the minimum tracking RMSE with the best efficiency. Note that the auto-tuning of the quadrotor is more complicated than that of Dubin's car due to the former's higher dimensional parameter space and stronger nonlinearities in dynamics and control. In the auto-tuning on the 2D/3D circular trajectories, the RMSEs show oscillation near the end of the tuning trials, indicating the learning rate might be too large when the loss is close to a (local) minimum. In terms of the final RMSE, AutoTune, SafeOpt-PSO, and GIBO demonstrate similar performance, all inferior to that of DiffTune. AutoTune and GIBO have a smoother RMSE reduction than SafeOpt-PSO.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-B Quadrotor", "weight": 1.0} -->

Moreover, the three baseline methods are less favorable for practical usage since they demand more hyperparameters to be tuned (e.g., the variance of the transition model for each parameter in AutoTune; kernel functions, lower/upper bound of each parameter, safety thresholds, and swarm size for SafeOpt-PSO; kernel functions, local search bounds, learning rate, and number of queries for GIBO) than the number of controller parameters for auto-tuning. In contrast, DiffTune only requires tuning the learning rate as the sole hyperparameter, yet still delivering the best outcome.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-B Quadrotor", "weight": 1.0} -->

Handling uncertainties: In this simulation, we consider the uncertainty caused by the imprecise knowledge of the moment of inertia (MoI) $J$. We set the vehicle's true MoI as $\beta J$ for $\beta$ from 0.5 to 4 and use $J$ in the controller design as our best knowledge of the system. The scaled MoI can be treated as an unknown control input gain (see (16b)), leading to decreased ($\beta > 1$) or increased ($\beta < 1$) moment in reality compared to the commanded moment by the geometric controller. However, the uncertainty caused by the perturbed MoI can be well handled by $\mathcal{L}_{1}$AC, which is adopted in the simulation. We conduct an ablation study to understand the roles of DiffTune and $\mathcal{L}_{1}$AC by comparing the root-mean-square error (RMSE) of position tracking, as shown in Table II (where the tuning is conducted over a 3D figure 8 trajectory in 100 trials with a learning rate of $\alpha = 0.005$).

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-B Quadrotor", "weight": 1.0} -->

It can be seen that tuning and $\mathcal{L}_{1}$ can individually reduce the tracking RMSE. The best performance is achieved when DiffTune and $\mathcal{L}_{1}$AC are applied jointly.

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-C Discussion", "weight": 1.0} -->

The advantage of DiffTune is its efficient usage of the first-order information (gradient $\nabla_{\mathbf{θ}}L$) of the target system. Compared with DiffTune, the baseline auto-tuning methods (AutoTune, SafeOpt/SafeOpt-PSO, and GIBO) have the advantage of requiring less prior information (e.g., explicit formulas for dynamics and controller ) than DiffTune. All baseline methods use probabilistic approaches (Metropolis-Hastings algorithm or Bayesian optimization) to explore candidates of parameters and iteratively improve the performance based on observed input-output (i.e., parameters-performance) pairs. However, when the knowledge of the system is perceived through such "sampling" procedures, sufficiently many trials are needed to gain enough information and infer the optimal parameter choice, and the number of trials scales badly with the dimension of the parameter space. However, in practice, many physical systems have models obtained by physics or first principles, which can provide sufficiently useful first-order information to guide parameter searches.

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-C Discussion", "weight": 1.0} -->

Such information will significantly reduce the number of trials in auto-tuning compared to when one uses "sampling" to obtain this information, which is clear in the comparison shown in Figs. and. For BO-based approaches (SafeOpt/SafeOpt-PSO and GIBO), the assumption that the objective function is a sample from a known GP prior may not fit the auto-tuning scenario, especially when the system dynamics or controller hold strong nonlinearities. This conclusion is drawn from the observation of BO-based approaches' inferior performance to DiffTune for quadrotor auto-tuning in Fig., in contrast to the similar performance obtained by DiffTune and BO-based approaches for the auto-tuning of Dubin's car (whose dynamics and controller exhibit less nonlinearities than those of the quadrotor) in Fig.. We will illustrate the efficiency of auto-tuning using the first-order information with the experimental results in Section VI next.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Experiment results", "weight": 1.0} -->

We validate and evaluate DiffTune on a quadrotor in experiments, through which we would like to answer the following four questions: 1. How is the performance improvement using DiffTune with only limited tuning budgets (e.g., 10 trials)? 2. How do the tuned parameters generalize to trajectories that are unseen during tuning? 3. What are the individual role of DiffTune and $\mathcal{L}_{1}$AC in terms of performance improvement? 4. How is the real-flight performance compared between parameters auto-tuned with experimental data and those auto-tuned with simulation data?

<!-- chunk {"id": "body-0059", "role": "body", "section": "VI-A Experiment setup", "weight": 1.0} -->

We use the same dynamics and controller as used in Section V-B. The controller's initial parameters are shown in Table VII. We only permit 10 tuning trials as the budget to limit the time and mechanical wear of the tuning. The loss function is chosen as the sum of the translational and rotational tracking errors to penalize undesirable tracking performance in these two perspectives, i.e., $L = {{\parallel{{\mathbf{p}} - \overline{\mathbf{p}}}\parallel}^{2} + {{\text{tr}{({I - {{\overline{R}}^{\top}R}})}}/2}}$. A horizon of 7 s is used to collect the data and perform sensitivity propagation. The data contains the full state and control actions sampled at 400 Hz (by the design of Ardupilot), where the state is obtained via the original EKF developed by Ardupilot, with Vicon providing only position and yaw measurements of the quadrotor.

<!-- chunk {"id": "body-0060", "role": "body", "section": "VI-A Experiment setup", "weight": 1.0} -->

The data are logged onboard and downloaded to a laptop to compute the new controller parameter $\mathbf{θ}$. We use learning rate $\alpha = 0.1$ together with gradient clipping such that the parameters in the next trial ${\mathbf{θ}}_{j + 1}$ will always fall within 10% of the current parameters ${\mathbf{θ}}_{j}$, i.e., ${\mathbf{θ}}_{j + 1} \in {\lbrack{0.9{\mathbf{θ}}_{j}},{1.1{\mathbf{θ}}_{j}}\rbrack}$. Such a saturation scheme is used to (i) prevent the parameters from turning negative when the gradient is large and (ii) enforce a "trust region" around the current parameters to avoid overly large parameter changes.

<!-- chunk {"id": "body-0061", "role": "body", "section": "VI-A Experiment setup", "weight": 1.0} -->

The laptop has an Intel i9-8950HK CPU, and the run time for sensitivity propagation to update the sensitivity states in one iteration (from $k$ to $k + 1$) is $91 \pm {13\mu}$s (in MATLAB).

<!-- chunk {"id": "body-0062", "role": "body", "section": "VI-B Run DiffTune on three trajectories", "weight": 1.0} -->

We use a circular trajectory for tuning, where the speeds are set to $\lbrack 1,2,3\rbrack$ m/s for a spectrum of agility from slow to aggressive. The controller is tuned individually for these three speeds^11^1The video recordings of the 0th, 3rd, 6th, and 10th trials while tuning for the 3 m/s circular trajectory are available in the supplementary material, in which one can see the performance improvement through the trials., and we denote the final parameters by P1, P2, and P3 (associated with the speeds of 1, 2, and 3 m/s, respectively). The parameters P2 are obtained in seven trials because the quadrotor experiences oscillations after the seventh trial, and we decided to use the parameters tuned at the last non-oscillating trial. The reduction of the tracking RMSE is shown in Fig.. Comparing the tracking performance at the last trial to the initial trial, the RMSE has achieved 1.5x, 2.5x, and 3.5x reduction on the 1, 2, and 3 m/s circular trajectories, respectively.

<!-- chunk {"id": "body-0063", "role": "body", "section": "VI-B Run DiffTune on three trajectories", "weight": 1.0} -->

Furthermore, all the tuned parameters achieve lower tracking RMSEs than the hand-tuned parameters. While the reduction in tracking RMSE is monotone in the 2 and 3 m/s cases, for the case of 1 m/s, a minor fluctuation is superposed on the monotone reduction of the tracking RMSE. This phenomenon happens since the dominant $z$-axis RMSE fluctuates, which is caused by the large learning rate for $z$-axis tracking when the parameters are close to the (local) minimum of $z$-axis error (observe the $z$-axis RMSE reduces only from 6.8 to 5.5 cm). For the $x$- and $y$-axis tracking RMSE, we observe a monotone reduction in all three speeds. Notably, we observe the sensitivity of the angular velocity gains ${\mathbf{k}}_{\mathbf{\Omega}_{x}}$ and ${\mathbf{k}}_{\mathbf{\Omega}_{y}}$ are larger than the other parameters (by at least a magnitude).

<!-- chunk {"id": "body-0064", "role": "body", "section": "VI-B Run DiffTune on three trajectories", "weight": 1.0} -->

In other words, the partial derivatives $\partial{L/{\partial{\mathbf{k}}_{\mathbf{\Omega}_{x}}}}$ and $\partial{L/{\partial{\mathbf{k}}_{\mathbf{\Omega}_{y}}}}$ are large, which leads to significant changes in the gains ${\mathbf{k}}_{\mathbf{\Omega}_{x}}$ and ${\mathbf{k}}_{\mathbf{\Omega}_{y}}$. This reduction leads to a more agile response in rotational tracking on the roll and pitch commands, which efficiently improves the position tracking performance on the $x$- and $y$-axis. The trajectories on the horizontal plane through the tuning trials are shown in Fig.. For the 3 m/s circular tuning trajectory, we show the stacked images during the flight in Fig. LABEL:fig:\_exp_stacked_images_3mps. It is clear that the quadrotor's tracking of the circular trajectory becomes better as more trials are conducted.

<!-- chunk {"id": "body-0065", "role": "body", "section": "VI-B Run DiffTune on three trajectories", "weight": 1.0} -->

The evolution of the parameters in the tuning trials is shown in Fig.. Overall, the parameters tend to converge following one direction, except for the derivative gain ${\mathbf{k}}_{\mathbf{\Omega}}$ for angular tracking. Specifically, near the end of the tuning, ${\mathbf{k}}_{\mathbf{\Omega}}$ shows a change of evolution direction, which indicates that the mapping from these parameters to the loss function is likely to lie on a nonlinear manifold. Such a nonlinear manifold is difficult for a human to perceive and understand in hand-tuning unless sufficiently many, possibly pessimistically unrealistically many, trials are provided, which leads to the challenges in tuning a nonlinear controller by hand. Furthermore, another challenge of hand tuning is that one may alter one or (at most) two parameters in each trial since humans essentially perform coordinate-wise finite differences via trial and error to tune the controller. These two factors combined result in inefficient tuning by hand, especially when the dimension of parameter space is high. We display the tuned parameters in Table VII in Appendix C, along with the initial parameters and hand-tuned parameters for comparison.

<!-- chunk {"id": "body-0066", "role": "body", "section": "VI-C Generalization", "weight": 1.0} -->

We conducted experiments to test the generalization capability of the tuned parameters in Section VI-B. The testing set contains circular, 3D figure 8, and vertical figure 8 trajectories, with their coordinates shown in Table III and shapes shown in Fig. (in the Appendix C). The latter two trajectories are considered here for their wide range of speed and acceleration (see Table IV), which is in contrast to those static values of the circular trajectories. We test the three groups of tuned parameters P1, P2, and P3 on circular trajectories with 1, 2, and 3 m/s speed, respectively. The tracking performance of these tuned parameters on the testing trajectories is shown in Table IV, in which we also include the baseline of hand-tuned parameters.

<!-- chunk {"id": "body-0067", "role": "body", "section": "VI-C Generalization", "weight": 1.0} -->

When tested on the circular trajectories, the tuned parameters perform the best on the speed that they were tuned, i.e., P$n$ performs the best on trajectory $C{(n)}$ for $n \in {\{ 1,2,3\}}$. The same phenomenon has been observed (although the controller therein is different from the one used here), where parameters perform the best over the trajectories that they are auto-tuned. This behavior is similar to an overfitted NN in machine learning. In our case, this type of "overfitting" is expected since the proportional-derivative structure of the geometric controller determines that there does not exist a group of parameters that work well for all conditions (e.g., the aggressive trajectory $C{}$ demands a distinct parameter combination than for the slow trajectory $C{}$). However, the parameters can still generalize to the 3D figure 8 and vertical figure 8 trajectories that are not used for tuning.

<!-- chunk {"id": "body-0068", "role": "body", "section": "VI-C Generalization", "weight": 1.0} -->

Specifically, P2 and P3, which are tuned for increasingly aggressive maneuvers with fast-changing directions of velocity and acceleration, generalize to the two variants of the figure 8 trajectory that demands fast-changing speed and acceleration. P3 demonstrates better agility, which shows the best performance on $DF{}$ and $VF{}$. However, P3 is overly agile for the speed and acceleration in $DF{}$ and $VF{}$, which leads to minimum RMSE compared to P1 and P2, albeit with minor oscillations on the pitch angle.

<!-- chunk {"id": "body-0069", "role": "body", "section": "VI-D Ablation Study", "weight": 1.0} -->

We conduct an ablation study of how much contribution DiffTune and $\mathcal{L}_{1}$AC provide to performance improvement. We repeat the tuning in Section VI-B but with $\mathcal{L}_{1}$AC in the loop, which results in different sets of parameters for the three trajectories denoted by Pn-$\mathcal{L}_{1}$ for $n \in {\{ 1,2,3\}}$ and shown in Table VII in Appendix C. Our implementation follows. Unlike the simulations in Section V-B where we deliberately introduce uncertainties in MoI, in the experiment, we do not introduce uncertainties. The quadrotor naturally has uncertainties existing in the system (e.g., varying battery voltage in flight and mismatch between the actual MoI and estimated MoI through CAD computation), in which case $\mathcal{L}_{1}$AC can help compensate for these uncertainties and thus improve the tracking performance. The results are shown in Table V.

<!-- chunk {"id": "body-0070", "role": "body", "section": "VI-D Ablation Study", "weight": 1.0} -->

Here, "DiffTune off" shows the performance of the initial parameters (no tuning occurs); "DiffTune on" shows the tracking performance in the final tuning trial. "$\mathcal{L}_{1}$ on/off" indicate whether $\mathcal{L}_{1}$AC is used or not during the tuning trials. We conclude that 1. DiffTune alone can improve the tracking performance, albeit the system has uncertainties and measurement noise. 2. When $\mathcal{L}_{1}$AC is combined with DiffTune, $\mathcal{L}_{1}$AC helps improve the performance in two ways: (i) compensating for the uncertainties so that the uncertainties' degradation to system performance is mitigated; and (ii) DiffTune can proceed with less biased gradient thanks to the uncertainties being "canceled out" by $\mathcal{L}_{1}$AC, which leads to more efficient tuning.

<!-- chunk {"id": "body-0071", "role": "body", "section": "VI-D Ablation Study", "weight": 1.0} -->

Intuitively, DiffTune raises the performance's upper limit (in an ideal case subject to no uncertainty), whereas $\mathcal{L}_{1}$AC keeps the actual performance (in a realistic case subject to uncertainties) close to the upper limit. When the two are used together, the best performance is achieved.

<!-- chunk {"id": "body-0072", "role": "body", "section": "VI-E Comparison of Parameters Auto-tuned in Experiments with Those Obtained in Simulations", "weight": 1.0} -->

In this subsection, we compare the parameters auto-tuned in experiments (detailed in Section VI-B) with those obtained in simulations. For the latter, we apply Algorithm to a quadrotor system in simulation, where the vehicle's physical parameters (mass and inertia) are identical to the quadrotor used in the experiments. Furthermore, to stay consistent with the setup in experiments, we use the same initial controller parameters, loss function, horizon of evaluation, gradient clipping, and sampling time as in Section VI-B. Since equipment wear and tear is not an issue in simulation, we raise the auto-tuning budget to 50 trials and reduce the learning rate $\alpha$ to 0.01. We auto-tune parameters for the circular trajectories at speeds of 1, 2, and 3 m/s. In Fig., we show the tracking errors through the trials. The tracking error shows a monotone reduction in the beginning and ends with small oscillations when it terminates after 50 trials, which indicates that the best performance is achieved with the selected learning rate. We deploy the parameters auto-tuned in simulations on the real quadrotor used in the previous experiments in Section VI-B.

<!-- chunk {"id": "body-0073", "role": "body", "section": "VI-E Comparison of Parameters Auto-tuned in Experiments with Those Obtained in Simulations", "weight": 1.0} -->

Furthermore, we test the parameters obtained in the 10th, 30th, and 50th trials in the simulation to examine the performance at different stages of the auto-tuning. The results are shown in Table VI. In general, one can observe the reduced tracking error from the parameters that have been obtained through more trials in simulation, for example, with trajectories $C{}$ and $C{}$. However, the crashes seen on trajectories $C{}$ and $C{}$ with relatively more simulation trials indicate the common issue of sim-to-real gap: as the parameters evolve on simulation data, they inevitably (over)fit the simulation rather than the real system. The new results indicate the benefit of experiment-based auto-tuning, which is conditioned on the model-based gradient on data from a real system, and thus provides the best knowledge of parameter change for performance improvement. Nevertheless, the parameters extracted from the 10th trial in simulations result in tracking errors close to the errors with the hand-tuned parameters, which may be used as initial parameters or warm start for further performance improvement in experiment-based auto-tuning.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we propose DiffTune: an auto-tuning method using auto-differentiation, with the advantage of stability, compatibility with data from physical systems, and efficiency. Given a performance metric, DiffTune gradually improves the performance using gradient descent, where the gradient is computed using sensitivity propagation that is compatible with physical systems' data. We also show how to use $\mathcal{L}_{1}$AC to mitigate the discrepancy between the nominal model and the associated physical system when the latter suffers from uncertainties. Simulation results (on a Dubin's car and a quadrotor) and experimental results (on a quadrotor) both show that DiffTune can efficiently improve the system's performance. When uncertainties are present in a system, $\mathcal{L}_{1}$ adaptive control facilitates tuning by compensating for the uncertainties. Generalization of the tuned parameters to unseen trajectories during tuning is also illustrated in both simulation and experiments.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Conclusion", "weight": 1.5} -->

One limitation of the proposed approach is that it only applies to systems with differentiable dynamics and controllers. The requirement on differentiability is not met in contact-rich applications (e.g., legged robots and dexterous manipulation ) and systems with actuation limits (e.g., saturations in magnitude or changing rate). Although subgradients generally exist at the points of discontinuity, the impact of surrogate gradient on the tuning efficiency is unknown, which will be investigated in the future. Another limitation of this work is the convergence to a local minimum due to the usage of gradient descent. Future work will investigate conditions for convergence to a global minimum or methods that can help escape from local minimums.
