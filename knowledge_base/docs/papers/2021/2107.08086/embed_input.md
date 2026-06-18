<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

An Information-state Based Approach to the Optimal Output Feedback Control of Nonlinear Systems

Topics include Optimal control, Trajectory optimization, Uncertainty, Online algorithms, Generalization, Optimization, Control, ARMA, Nonlinear systems, Linear quadratic regulator.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper develops a data-based approach to the closed-loop output feedback control of nonlinear dynamical systems with a partial nonlinear observation model. We propose an information state based approach to rigorously transform the partially observed problem into a fully observed problem where the information state consists of the past several observations and control inputs. We further show the equivalence of the transformed and the initial partially observed optimal control problems and provide the conditions to solve for the deterministic optimal solution. We develop a data based generalization of the iterative Linear Quadratic Regulator (iLQR) to partially observed systems using a local linear time varying model of the information state dynamics approximated by an Autoregressive moving average (ARMA) model, that is generated using only the input-output data. This open-loop trajectory optimization solution is then used to design a local feedback control law, and the composite law then provides an optimum solution to the partially observed feedback design problem. The efficacy of the developed method is shown by controlling complex high dimensional nonlinear dynamical systems in the presence of model and sensing uncertainty.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The optimal stochastic control of a nonlinear dynamical system is computationally intractable for complex high-order systems due to the 'curse of dimensionality' associated with solving dynamic programming. The problem becomes more challenging when the model of the system is unknown and even more formidable when only some of the states are available for measurement, i.e., under partial state observation. However, in practice, most problems tend to be partially observed and subject to noise. In this work, we propose a data-based approach for learning to optimally control complex partially observed stochastic nonlinear dynamical systems. The primary idea is to generate Autoregressive--Moving-Average (ARMA) models along a nominal trajectory using input-output perturbation data and then defining a suitable linear time-varying system using the resulting information state which is comprised of past several measurements and controls.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The proposed approach then generalizes the iLQR algorithm to partially observed problems by iteratively generating linear time-varying state-space models, represented in the information state, to obtain the optimized nominal information space trajectory. This optimized nominal information state trajectory is utilized to design a local Linear Quadratic Gaussian (LQG) controller. The resulting method, which we term Partially Observed Decoupled Data-based Control (POD2C), results in a composite perturbation feedback design in the information state that can then be used to control the system online in the presence of partial state observation, process and sensor noise.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Related Work: The iLQR is a "local" trajectory-based method, similar to Differential Dynamic Programming (DDP), but only uses first-order dynamics information as opposed to second-order derivatives of the system dynamics needed in DDP. Previous work such as employed finite differencing in computing the Jacobians using complete state information as opposed to this work which utilizes ARMA models to compute linear models using only output information, and thus, this work suitably generalizes the iLQR method to partially observed systems in a systematic fashion. Another work on motion planning under motion and sensing uncertainty uses a belief space variant of iterative LQG (iLQG) to find a locally optimal solution. Our work is related to this paper, in the sense, that we generate the nominal trajectory using a generalized information state version of the iLQR method, but is $O{(n_{x})}$ in its complexity versus $O{({n_{x} + n_{x}^{2}})}$ in the case of the above reference, where $n_{x}$ is the state space dimension.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The control of unknown dynamical systems with noisy partial state observation have been extensively studied as a belief space planning problem, where the belief state is defined as the probability distribution over the states and provides a basis for acting under uncertainty. However, challenges such as a suitable parametrization of the probability distribution over the state, the under-actuated nature of the belief space problem, and stochasticity due to future observations still persist. To overcome these issues, the so-called Gaussian belief space planning approaches assume a Gaussian belief that can be compactly parametrized in terms of the mean and covariance of the distribution. Platt et. al. assumed maximum likelihood observations to approximate the problem and showed that a simple LQR controller in belief state (B-LQR) is equivalent to the LQG controller for linear dynamics and observation models with Gaussian noise. Another method called "Trajectory-optimized LQG" (T-LQG) uses a coupled design of trajectory and estimator to find the optimal underlying trajectory and then uses the separation principle to design an LQR controller around the optimal trajectory.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, this class of techniques still require a state representation that is $O{({n_{x} + n_{x}^{2}})}$, where $n_{x}$ is the dimension of the underlying state space, and thus, are intractable for the higher dimensional and complex robotic problems considered in this paper. In a related development, it was shown that local optimal plans can be computed more efficiently by optimizing over control and mean states only (partial collocation) without including the state covariance in the trajectory optimization. In this paper, we optimize the trajectory of a partially observed system utilizing the "nominal information state" which is defined as $q$ past most likely (zero noise) observations (of dimension $n_{z}$), with ${q \times n_{z}} \leq n_{x}$, and is estimated from system output data using the ARMA framework.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

This allows us to solve a large class of complex and high dimensional partially observed robotic control problems in a highly efficient fashion since the complexity is $O{(n_{x})}$ rather than $O{({n_{x} + n_{x}^{2}})}$ for typical Gaussian belief space planning problems. In this regard, we distinguish belief space planning problems into two classes: 1) ones that seek to control the robotic system from start to goal under noisy partial state observations, and 2) others that seek the dual "information-seeking" behavior of control. In the context of Gaussian belief space planning, most methods mentioned above fall under the second category while our POD2C approach and the reference belong to the first category.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Gaussian belief space planning, system linearization is assumed to be valid along a nominal trajectory, which requires that the covariance along the trajectory be small, and hence, the cost due to the covariance in the total planning cost is negligible, given that the belief space cost function is induced by an underlying state space cost, i.e., ${c{(b,u)}} = {\int{c{(x,u)}b{(x)}{dx}}}$, where $b{(.)}$ denotes the belief state. In Section III, we provide a detailed justification for the above observation, and hence, the sufficiency of planning on the nominal information state (dimension of $O{(n_{x})}$) in such problems.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The approach proposed here, POD2C, is a generalization of the so-called decoupled data-based control (D2C) approach for designing a feedback controller, that designs an open-loop optimal trajectory followed by a local feedback controller in a data-based manner but is limited to fully observed systems, to partially observed systems. The D2C approach was used for partially observed systems where the open-loop optimization problem is solved using a general nonlinear programming solver, in contrast, this paper uses the highly efficient ARMA based information-state iLQR, and further generates a local closed-loop feedback design by generating a suitable LTV system in the information state rather than the time-varying eigensystem realization algorithm used.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper is organized as follows: Section II provides the optimal control problem formulation for the stochastic nonlinear system. Section III provides the ARMA based methodology for open-loop trajectory design using partially-observed model-free iLQR. Section IV gives the details of the POD2C closed-loop feedback control design and the complete POD2C algorithm is given in Section V. Finally, empirical results are shown for the partially observed control of complex robotic systems, including challenging cases of hard-to-model soft contact constraints and dynamic fluid-structure interactions, in the presence of process and sensor noise.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

where $x_{t}$ is the state, $u_{t}$ is the control, $w_{t}$ is a white noise perturbation to the system, and $\epsilon$ is a small parameter that modulates the noise in the system. Let us assume the observation model to be of form: ${z_{t} = {h{(x_{t},v_{t})}}},$ where $v_{t}$ is the measurement noise.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

where $c{(x,u)}$ denotes a running incremental cost, $\phi{(x)}$ denotes a terminal cost function and $E{\lbrack \cdot \rbrack}$ is an expectation operator taken over the sample paths of the system. For the case of partially observed states, the above problem turns into a planning problem on the belief state, $b_{t}{(x)}$, which is the filtered density of the state given the past observations and controls: $\mathcal{Z}_{t} = {\{ z_{0},u_{0},z_{1},{u_{1}\cdotsu_{t - 1}},z_{t}\}}$ till the time $t$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

where the costs ${\overline{c}{(b,u)}} = {\int{c{(x,u)}b{(x)}{dx}}}$, and ${\Phi{(b)}} = {\int{\phi{(x)}b{(x)}{dx}}}$ either flow from the underlying costs in the state space, or alternatively, can also be defined directly on the belief state.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Most Likely Belief Space Trajectory", "weight": 1.0} -->

The above belief space planning problem is intractable due to the infinite dimensional nature of the belief state, which compounds Bellman's "Curse of Dimensionality" with the "Curse of History" inherent in the infinite dimensional nature of the belief state. The reference introduced the concept of the most likely observation sequence, and the associated most likely belief state evolution. The most likely observation given a belief state $b{( \cdot )}$ is simply: ${z^{\ast} = {{\max_{z}p}{({z/b})}}},$ where ${p{({z/b})}} = {\int{p{({z/x})}b{(x)}}}$. It can then be seen that the evolution of the most likely belief state, we shall also call it the nominal belief state, is deterministic.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Most Likely Belief Space Trajectory", "weight": 1.0} -->

where, note that there is no expectation in the cost above since we consider the nominal belief state ${\overline{b}}_{t}$, and the optimization is now over the control sequence $\{ u_{t}\}$, rather than over the sequence of feedback policies $\{{\pi_{t}{( \cdot )}}\}$ in eq. 3 for Complex Robotic Systems"). This makes the "open-loop" problem above far easier to solve than the "closed-loop" problem in eq. 3 for Complex Robotic Systems"). Nonetheless, we note that this is a heuristic, and we do not consider the question of the closeness of the solution of eq. 4 for Complex Robotic Systems") to that of eq.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A Most Likely Belief Space Trajectory", "weight": 1.0} -->

3 for Complex Robotic Systems").\
The rest of the paper is devoted to proposing a highly efficient way to solve the open-loop belief space planning problem above for complex nonlinear robotic systems, which can then either be: 1) repeatedly solved in an MPC fashion, or as we do in this paper, 2) allied with a local feedback controller around the planned nominal path, to yield a feedback solution.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Open-Loop Belief Space Trajectory Design using Partially Observed Model-free iLQR (POM-iLQR)", "weight": 1.0} -->

This section details the algorithm for open-loop trajectory design using POM-iLQR. The advantage of iLQR is that the equations involved in it are explicit in system dynamics and their gradients. Hence, to make it a model-free algorithm, it is sufficient if we could explicitly write the linearized model (the estimates of Jacobians) around the iterated nominals. Since iLQR/DDP is a well-established framework, we skip the details and instead present the essential equations in Algorithm 1 for Complex Robotic Systems"), Algorithm 2 for Complex Robotic Systems") and Algorithm 3 for Complex Robotic Systems"), where we also reflect the choice of our regularization scheme.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Information State Problem", "weight": 1.0} -->

We first present the key insight to the efficiency of our solution.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A Information State Problem", "weight": 1.0} -->

where the underlying dynamics model is used as a blackbox, and only output measurements are used to identify linear time-varying system. The information state is "nominal" in that we use the most likely observation sequence by zeroing out the process and measurement noise above. As we shall show below, the number of past values $q$ that we require to form the information state is small, in fact, ${q \times n_{z}} \leq n_{x}$, where $n_{x}$ and $n_{z}$ are the dimensions of the state and output spaces respectively.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Information State Problem", "weight": 1.0} -->

We note that the Information Space problem above is an approximation of the open loop belief space problem eq. 4 for Complex Robotic Systems"). In general, the belief state $b_{t}$ is the filtered density of the state given the complete information state ${\mathcal{Z}_{t} = {\{ z_{0},u_{0},z_{1},{u_{1}\cdotsu_{t - 1}},z_{t}\}}},$ and thus, may be written as $b_{t} = {\tau{(b_{0},\mathcal{Z}_{t})}}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A Information State Problem", "weight": 1.0} -->

Therefore, in general, ${\overline{c}{(b_{t},u_{t})}} = {c^{\mathcal{Z}}{(\mathcal{Z}_{t},u_{t})}} = {{\overline{c}}^{Z}{(Z_{t},Z_{t - 1},{\cdotsZ_{0}},u)}}$, in terms of the nominal information state $Z_{t}$ defined above, for suitably defined functions ${{\overline{c}}^{\mathcal{Z}}{( \cdot )}},{{\overline{c}}^{Z}{( \cdot )}}$. Thus, the cost used in eq. 5 ‣ Partially-Observed Decoupled Data-based Control (POD2C) for Complex Robotic Systems"), which is only a function of the current information state $Z_{t}$ with only $q$ of the past values is an approximation.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A Information State Problem", "weight": 1.0} -->

Nonetheless, this is a good approximation if considering a Gaussian belief, and a cost function ${\overline{c}{(b,u)}} = {\int{c{(x,u)}b{(x)}{dx}}}$ that arises from an underlying state space cost. The Gaussian belief space representation requires system linearization to be valid, this may be modeled by assuming that the initial condition, the process and measurement noise covariances are modulated by a suitably small parameter $\epsilon < 1$, i.e., ${P_{0} = {\epsilon^{2}{\overline{P}}_{0}}},{{Q = {\epsilon^{2}\overline{Q}}},{R = {\epsilon^{2}\overline{R}}}}$, where $P_{0}$, $Q$ and $R$ are the initial state, process and measurement noise covariances respectively.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A Information State Problem", "weight": 1.0} -->

Then, the random variable representing the hidden state may be represented as: ${x_{t} = {{\overline{x}}_{t} + {\epsilon{\overset{\sim}{x}}_{t}}}},$ where ${\overline{x}}_{t}$ is the mean of the nominal belief, ${\overset{\sim}{x}}_{t}$ is the deviation from the mean. Now, if the underlying cost is written in state-space, for example, say quadratic in $x_{t}$, then

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A Information State Problem", "weight": 1.0} -->

and therefore, given a small $\epsilon$, the cost corresponding to the covariance is insignificant, and thus need not be, and in fact, cannot be, considered in the information space planning problem. We shall see below that this approximation helps us solve a very large class of complex partially observed robotic control problems. Therefore, we distinguish this paper from the class of problems where measurement noise is state-dependent and the planning requires that the dual "information-seeking" effect of the control be considered. In fact, as we have shown above, such information seeking behavior is infeasible to obtain for Gaussian beliefs if the cost is induced by an underlying state space cost, and a suitable belief space cost has to be defined instead.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A Information State Problem", "weight": 1.0} -->

The linearized model given in eq. 7 ‣ Partially-Observed Decoupled Data-based Control (POD2C) for Complex Robotic Systems") is represented in a much smaller dimension (system-order $O{(n)}$) as compared to belief state dimension $O{({n + n^{2}})}$ even after assuming Gaussian belief space). This allows us to do the motion planning much more efficiently and forms the basis for using POM-iLQR.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B Linear Time-Varying System Identification using ARMA", "weight": 1.0} -->

The standard least square method is used to estimate the linear parameters from input-output experiment data.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B Linear Time-Varying System Identification using ARMA", "weight": 1.0} -->

All the perturbations are zero-mean, i.i.d, Gaussian noise with covariance matrix $\sigmaI$. The covariance $\sigma$ is a $o{(u)}$ small value selected by the user.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B Linear Time-Varying System Identification using ARMA", "weight": 1.0} -->

where the blank part of the matrix is filled so that the complete matrix is symmetric.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B Linear Time-Varying System Identification using ARMA", "weight": 1.0} -->

and $U = {E{\lbrack{\deltau_{k}\deltau_{k}^{\mathsf{T}}}\rbrack}}$ is the input perturbation covariance at any time $k$. Notice that this is a computationally efficient way of estimating the parameters but the standard least square method can also be used for parameter estimation.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-C Condition for ARMA Model", "weight": 1.0} -->

This subsection provides the condition on the order ($q = p$) of the ARMA model to exactly match a linear system. The output observation $z_{t}$ is to be modeled using the past few observations and past few excitation inputs $u_{t}$, where excitation input is modeled as independent identically distributed random variables (i.i.d.) with zero means.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark III.1", "weight": 1.0} -->

For the examples we have tried, we observed that the $q$ value does not change at each time-step and most likely would not change for physical/mechanical systems.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-D System Dynamics in Information State", "weight": 1.0} -->

$\underset{\deltaZ_{t}}{\underbrace{\begin{bmatrix} \end{bmatrix}}} = {{\underset{A_{t - 1}}{\underbrace{\begin{bmatrix} \alpha_{t-1} &amp; \alpha_{t-2} &amp; \cdots &amp; \alpha_{{t-q}+1} &amp; \alpha_{t-q} &amp; &amp; \beta_{t-2} &amp; \beta_{t-3} &amp; \cdots &amp; \beta_{{t-q}+1} &amp; \beta_{t-q} \\ 1 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 &amp; &amp; 0 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 \\ 0 &amp; 1 &amp; \cdots &amp; 0 &amp; 0 &amp; &amp; 0 &amp; 0 &amp;

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-D System Dynamics in Information State", "weight": 1.0} -->

\cdots &amp; 0 &amp; 0 \\ \vdots &amp; &amp; \ddots &amp; &amp; \vdots &amp; &amp; \vdots &amp; &amp; \ddots &amp; \vdots &amp; 0 \\ 0 &amp; 0 &amp; \cdots &amp; 1 &amp; 0 &amp; &amp; 0 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 \\ &amp; &amp; &amp; &amp; &amp; &amp; &amp; &amp; &amp; &amp; \\ 0 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 &amp; &amp; 0 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 \\ 0 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 &amp; &amp; 1 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 \\ 0 &amp; 0 &amp; \cdots &amp; 0

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-D System Dynamics in Information State", "weight": 1.0} -->

&amp; 0 &amp; &amp; 0 &amp; 1 &amp; \cdots &amp; 0 &amp; 0 \\ \vdots &amp; &amp; \ddots &amp; &amp; \vdots &amp; &amp; \vdots &amp; &amp; \ddots &amp; &amp; \vdots \\ 0 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 &amp; &amp; 0 &amp; 0 &amp; \cdots &amp; 1 &amp; 0 \end{bmatrix}}}\underset{\deltaZ_{t - 1}}{\underbrace{\begin{bmatrix} \end{bmatrix}}}} + {\underset{B_{t - 1}}{\underbrace{\begin{bmatrix} \end{bmatrix}}}\deltau_{t - 1}} + {\underset{D_{t - 1}}{\underbrace{\begin{bmatrix}

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-D System Dynamics in Information State", "weight": 1.0} -->

After identifying the system parameters $\alpha_{t - 1},\cdots,\alpha_{t - q}$ and $\beta_{t - 1},\cdots,\beta_{t - q}$ for all $t = {\{{0\cdotsT}\}}$, now, we write the linear perturbation system in the information state as given in Eq. (15 ‣ Partially-Observed Decoupled Data-based Control (POD2C) for Complex Robotic Systems")), where $\gamma_{t - 1}$ is given as: ${\gamma_{t - 1} = {\beta_{t - 1} + \beta_{t - 2} + \cdots + \beta_{t - q}}},$ as the random noise sequence $\{ w_{t - 1},w_{t - 2},\cdots,w_{t - q}\}$ is independent and assuming the noise to enter the same channel as the control input.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-D System Dynamics in Information State", "weight": 1.0} -->

This is based on the idea that if the output $z_{t}$ depends on last $q$ control inputs, then it would also depend on last $q$ disturbance terms. Now, we can use the identified $A_{t - 1}$, $B_{t - 1}$ to find the optimal nominal using iLQR, and in the next section, design an LQG controller for the information state, i.e., ${\deltau_{t}} = {K_{t}\deltaZ_{t}}$, where note that the current control input depends on the past observations as well as the control inputs.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Partially-Observed Decoupled Data-based Control (POD2C) Algorithm", "weight": 1.0} -->

In this section, we propose an extension to the so-called decoupled data-based control (D2C) algorithm. The D2C algorithm is a highly data-efficient Reinforcement Learning (RL) method that has shown to be much superior to the state-of-the-art RL algorithms such as the Deep Deterministic Policy Gradient (DDPG) in terms of data efficiency and training stability while retaining similar or better performance. In the following, we detail the extension that allows for the generation of the closed-loop output feedback policy, i.e., the feedback as a function of the past few observations. The main observation for the extension is that the partially observed case might be treated similarly to the fully observed case by noting that the information state in the problem comprises of past few observations and past few control inputs.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Partially-Observed Decoupled Data-based Control (POD2C) Algorithm", "weight": 1.0} -->

The D2C algorithm then proposes a 3 step procedure to approximate the solution to the above problem. First, a noiseless open-loop optimization problem is solved to find an optimal control sequence, ${\overline{u}}_{t}^{\ast}$. Second, from rollouts, we estimate a linear perturbation model for the information state ${\deltaZ_{t}} = {{A_{t - 1}\deltaZ_{t - 1}} + {B_{t - 1}\deltau_{t - 1}}}$ around the nominal to obtain Linear-Time Varying (LTV) system. Third, an LQG controller for the above time varying linear system is designed whose time varying gain is given by $K_{t}$. Finally, the control applied to the system is given by $u_{t} = {{\overline{u}}_{t}^{\ast} - {K_{t}\deltaZ_{t}}}$. The details for the first two-steps are already presented in Section III.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Partially-Observed Decoupled Data-based Control (POD2C) Algorithm", "weight": 1.0} -->

The following subsection provides the details for the closed-loop control law design with a specific-LQG method.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-A1 Simplified LQR design", "weight": 1.0} -->

For the case of noiseless measurements, a simplified LQR design can be used for the closed-loop feedback control with $u_{t} = {{\overline{u}}_{t}^{\ast} - {K_{t}\deltaZ_{t}}}$ where $K_{t}$ is calculated using eqs. 16 Algorithm ‣ Partially-Observed Decoupled Data-based Control (POD2C) for Complex Robotic Systems") and 17 Algorithm ‣ Partially-Observed Decoupled Data-based Control (POD2C) for Complex Robotic Systems") only.

<!-- chunk {"id": "body-0042", "role": "body", "section": "The Complete Algorithm", "weight": 1.0} -->

The complete POD2C algorithm: to determine the optimal nominal trajectory in a model-free fashion and closed-loop feedback law is summarized together in Algorithm 1 for Complex Robotic Systems"), Algorithm 2 for Complex Robotic Systems") and Algorithm 3 for Complex Robotic Systems"). As shown, we use regularization parameter $\mu$ to keep the optimization from divergence, and line search parameter $\alpha$ to find a good step size for a policy update.

<!-- chunk {"id": "body-0043", "role": "body", "section": "The Complete Algorithm", "weight": 1.0} -->

⇒ Open-loop trajectory design via POM-iLQR
Initialization: Set state x = x0, initial trajectory 𝕋0, line search parameter α = 0.3, regularization μ = 10−6, iteration counter k = 0, convergence coefficient ϵ = 0.001.
while costk/costk − 1) &lt; 1 + ϵ do
while cost reduction not acceptable do

<!-- chunk {"id": "body-0044", "role": "body", "section": "The Complete Algorithm", "weight": 1.0} -->

⇒ The closed-loop feedback design
2. Calculate observer and feedback gains L0: N − 1 and K0: N − 1 from sections IV-A, IV-A, 16 and 17.
3. Full closed-loop control policy:
$u_{t} = {{\overline{u}}_{t}^{\ast} - {K_{t}\delta{\hat{Z}}_{t}}}$,
Algorithm 1 Complete Partially-observed Decoupled Data-based Control (POD2C) Algorithm

<!-- chunk {"id": "body-0045", "role": "body", "section": "The Complete Algorithm", "weight": 1.0} -->

Input: Previous iteration nominal trajectory - 𝕋k, iLQR gains - {k0: N − 1, K0: N − 1}.
Get observation, state and control trajectory - ${\{{\overline{z}}_{t}^{prev},{\overline{u}}_{t}^{prev}\}}\leftarrow{\mathbb{T}}_{k}$, 0 ≤ t ≤ N − 1.
Start from t = 0, c o s t = 0, ${\overline{x}}_{0} = x_{0}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "The Complete Algorithm", "weight": 1.0} -->

/* start from the terminal time */
Compute JxN and JxN xN using boundary conditions.
/* obtain the augmented Jacobians using ARMA model from eq. 15 */
/* obtain the partials of the Q function as follows */

<!-- chunk {"id": "body-0047", "role": "body", "section": "The Complete Algorithm", "weight": 1.0} -->

if Qut ut is positive-definite then
kt = −Qut ut−1 Qut, Kt = −Qut ut−1 Qut zt. Decrease μ.

<!-- chunk {"id": "body-0048", "role": "body", "section": "The Complete Algorithm", "weight": 1.0} -->

Restart backward pass for current time-step.
/* obtain the partials of the value function Jt as follows */

<!-- chunk {"id": "body-0049", "role": "body", "section": "Empirical Results", "weight": 1.0} -->

We use MuJoCo, a physics engine, as a black-box to provide the data to design the nominal trajectory and closed-loop feedback gain. First, we list the details of the MuJoCo models used in our simulations.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Empirical Results", "weight": 1.0} -->

Cart-Pole: The state of a four-dimension under-actuated cart-pole comprises the angle of the pole, cart's horizontal position, and their rates. Within a given horizon, the task is to swing-up the pole and balance it in the middle of the rail by applying a horizontal force on the cart. Figure 2 for Complex Robotic Systems")(a) shows the initial position of the cart-pole system.\
15-link Swimmer: The 15-link swimmer model has 17 degrees of freedom and together with their rates, the system is described by 34 state variables. Controls can only be applied in the form of torques to the 14 joints with the initial configuration given in Figure 2 for Complex Robotic Systems")(b).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Empirical Results", "weight": 1.0} -->

Fish: The torso of the fish is a rigid body with 6 DOF and the system is described by 27 dimensions of states (including a set of quaternions) and 6 control channels. Controls are applied in the form of torques to the joints that connect the fins and tails with the torso. Figure 3 for Complex Robotic Systems")(a) shows the initial configuration of the fish.\
T2D1 Robotic Arm: The $T_{2}D_{1}$ tensegrity model is a 3D robotic arm consisting of 33 bars (orange) and 46 strings (grey). The bars are connected by ball joints and the initial configuration is given in Fig. 3 for Complex Robotic Systems")(b). Controls are applied in the form of tension in the strings and the feedback is based on the coordinates of some of the nodes.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Empirical Results", "weight": 1.0} -->

The final configuration of all the four models is given in Figs. 1 for Complex Robotic Systems") and 4 for Complex Robotic Systems"). The final configurations are obtained at the end of the horizon with the partially-observed D2C algorithm. The videos for the simulation are given as supplementary files. The output number values in Table I for Complex Robotic Systems") represent the minimum number of state measurements needed to obtain a good fit of the ARMA model from the output data with $q$ values representing the order of the ARMA model. Notice that a relatively smaller number of measurements are needed to control the structure with increasing complexity (higher number of states) of the model. The cart-pole is a classic underactuated robotics example where the cart's horizontal position and angle of the pole are needed as feedback. The 15-link swimmer and fish present the performance of our method when applied to high-dimensional multi-body robots in a fluid environment. The 15-link swimmer needs only angular positions of the 1st, 3rd, 5th, 7th, 9th, 11th, 13th, and 15th joints. The fish needs only the angular positions of the fins and tails.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Empirical Results", "weight": 1.0} -->

The $T_{2}D_{1}$ robotic arm case shows the application to high-dimensional soft-body models. Here only the positions of 8 evenly chosen nodes are needed out of the total 25 nodes. Notice that velocity or rate feedback is not needed in the control design as the value of the state for rates can always be calculated from the past 2 observations of positions (refer to Corollary III.2 ‣ Partially-Observed Decoupled Data-based Control (POD2C) for Complex Robotic Systems")). The rule of thumb for measurement selection is that we only measure the positions that contain the most information and avoid redundant information.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Empirical Results", "weight": 1.0} -->

Open-loop training with POM-iLQR: As described in Sec. IV Algorithm ‣ Partially-Observed Decoupled Data-based Control (POD2C) for Complex Robotic Systems"), we obtain the nominal trajectory from POM-iLQR training. The 15-link swimmer and the fish take more iterations to converge as they have higher non-linearity brought by the fluid-structure interaction in the swimming motion. However, the training is much more time-efficient compared with the first-order gradient descend method as well as the DDPG RL method. The T2D1 arm system also takes smaller time and iterations to converge despite the high dimensionality of the model and limited outputs. The time taken and iteration numbers during POD2C algorithm execution for the above cases are shown in Fig. 5 for Complex Robotic Systems") and Table I for Complex Robotic Systems"). Notice that the POM-iLQR can converge smoothly and efficiently with partial observations, even for systems with high non-linearity and high dimensionality. The results are obtained using MatLab code and MuJoCo as the physics simulator on a Ryzen 3700 personal PC.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Empirical Results", "weight": 1.0} -->

The most time-consuming procedure is running simulations to collect data for fitting the ARMA model, which is run in serial for now. However, these rollouts are independent of each other, thus can be easily distributed to parallel simulations, which we believe could further improve the time efficiency and have the potential for real-time operation.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Empirical Results", "weight": 1.0} -->

Robustness to measurement noise: Figure 6 for Complex Robotic Systems") shows the plots for the episodic cost of the four examples with the variation in the measurement noise. The figure compares the open-loop control policy and the closed-loop control policy under different measurement noise levels, while the process noise standard deviation is set to 10% of the maximal nominal control. The measurement noise level on the x-axis is the percentage of the measurement noise standard deviation w.r.t. the maximal measurement noise. Note that both the measurement and process noise is added as zero-mean Gaussian i.i.d. noise to all measurement and control channels at each step.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Empirical Results", "weight": 1.0} -->

As the measurement noise does not influence the open-loop, the open-loop cost curves are shown to be almost flat with invariant variance. The closed-loop cost has a significantly smaller mean and variance than the open-loop cost, which proves the robustness to measurement noise of the closed-loop policy. Note that although the figure is plotted for a large measurement noise level, the closed-loop policy can successfully finish the task with smaller noise levels than what is indicated by the black threshold lines in the figure. Also, the variance of the open-loop policy, as well as the variance of the closed-loop policy at zero measurement noise, come from the fixed 10% process noise. The spikes in the open-loop curves are due to numerical error from the Monte-Carlo simulations.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Empirical Results", "weight": 1.0} -->

Robustness to process noise: Figure 7 for Complex Robotic Systems") shows similar plots as shown in Fig. 6 for Complex Robotic Systems") except we vary the process noise level along the x-axis with fixed 10% measurement noise. Under the open-loop policy, the process noise drives the model off the nominal trajectory and results in high episodic cost, while the closed-loop feedback can help the system stay close to the nominal trajectory and reach the target position. This can be seen from the figure as the episodic cost mean and variance of the closed-loop policy is much smaller than the open-loop policy on the entire tested noise range, although both policies fail the task when the process noise becomes larger than what the black threshold line indicates. The above analysis regarding the performance of control policy under noise proves that the LQG closed-loop feedback wrapped around the nominal trajectory makes the full closed-loop policy robust to both measurement and process noise.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Empirical Results", "weight": 1.0} -->

Comparison with a Direct RL Method: In a direct RL method such as DDPG, deep neural networks are used to represent the complete closed-loop control policy. Direct RL methods require full state observation and it is not clear how to generalize them to partially observed problems. Thus, we run the DDPG method on the fish example with the same information states as used by POD2C. After training for 20 hours, the fish still cannot swim to the target as shown in Fig. 8 for Complex Robotic Systems").

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusions", "weight": 1.0} -->

The paper presented a decoupled data-based approach to control complex robotic systems with partial state observations. The paper shows that the exact linear state-space model can be matched by the $q$^th^-order ARMA model generated using the input-output data. The ARMA model then can be used to write an LTV system in the information state which allows designing the optimal nominal trajectory using iLQR and also allows for designing the closed-loop feedback law using only the partially-observed states. Empirical results are also shown for complex robotic systems under motion as well as sensing uncertainty. In our opinion, the POD2C approach is a highly efficient method for RL in partially observed problems, however, questions regarding optimality remain and shall be explored in future work. Future work will explore fully and partially observed non-smooth motion planning scenarios such as those in legged robots. Another direction would be problems that require information seeking behavior which will require considering the dual effect of control. We conjecture that a hybrid of our POD2C approach and dual effect Gaussian belief space planning might be useful in this regard.
