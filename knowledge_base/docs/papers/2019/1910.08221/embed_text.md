## Introduction

We present a convergence analysis of the classical iterative linear quadratic exponential Gaussian controller (ILEQG) for finite-horizon risk-sensitive or safe nonlinear control. The ILEQG algorithm is particularly popular in robotics applications and can be seen as a risk-sensitive counterpart of the iterative linear quadratic Gaussian (ILQG) algorithm. We adopt here the viewpoint of the modern complexity analysis of first-order optimization algorithms as done by Roulet et al. for ILQG.

We address the following questions: (i) what is the convergence rate of ILEQG to a stationary point? (ii) how can we set the step-size to guarantee a decreasing objective along the iterations? The analysis we present here sheds light on these questions by highlighting the objective minimized by ILEQG which is a Gaussian approximation of a risk-sensitive cost around the linearized trajectory. We underscore the importance of the addition of a proximal regularization component for ILEQG to guarantee a worst-case convergence to a stationary point of the objective.

The main result of the paper is Theorem 2.5, where a sufficient decrease condition to choose the strength of the proximal regularization is given. The result also yields a complexity bound in terms of calls to a dynamic programming procedure implementable in a "differentiable programming" framework, that is, a computational framework equipped with an automatic differentiation software library. We illustrate the variant of the iterative regularized linear quadratic exponential Gaussian controller we recommend on simple risk-sensitive nonlinear control examples.

### Related work

The linear exponential quadratic Gaussian algorithm is a fundamental algorithm for risk-sensitive or safe control. The algorithm builds upon a risk-sensitive measure, a less conservative and more flexible framework than the H^∞^ theory also used for robust control; see and references therein. An excellent review of the classical results in abstract dynamic programming and control theory, in particular for risk-sensitive control, was done by Bertsekas. Risk-measures were analyzed as instances of the optimized certainty equivalent applied to specific utility functions. Risk-averse model predictive control was also studied to account for ambiguity in the knowledge of the underlying probability distribution.

Algorithms for nonlinear control problems are usually derived by analogy to the linear case, which is solved in linear time with respect to the horizon by dynamic programming. In particular, the iterative linear quadratic regulator (ILQR) and iterative linear quadratic Gaussian (ILQG) algorithms are usually informally motivated as iterative linearization algorithms. A risk-sensitive variant with a straightforward optimization algorithm without theoretical guarantees was considered by Farshidian and Buchli; Ponton et al..

On the first-order optimization front, optimization sub-problems such as Newton or Gauss-Newton-steps were shown to be implementable by using dynamic programming in classical works. Iterative linearized methods such as ILQR or ILQG were recently analyzed as Gauss-Newton-type algorithms and improved using proximal regularization and acceleration by extrapolation . This work shares the same viewpoint and establishes worst-case complexity bounds for iterative linear quadratic exponential Gaussian controller (ILEQG) algorithms.

The companion code is available at All proofs and notations are provided in the Appendix.

## Risk-sensitive control

### Problem formulation

We consider discretized control problems stemming from continuous time settings with finite-horizon, see Appendix E for the discretization step. Those are off-line control problems used for example at each step of a model predictive control framework. We focus on the control of a trajectory of length $\tau$ composed of state variables ${x_{1},\ldots,x_{\tau}} \in {\mathbb{R}}^{d}$ and controlled by parameters ${u_{0},\ldots,u_{\tau - 1}} \in {\mathbb{R}}^{p}$ through dynamics $\psi_{t}$ perturbed by i.i.d. white noise $w_{t} \sim {\mathcal{N}{(0,{\sigma^{2}I_{q}})}}$ such that for $t = {0,\ldots,{\tau - 1}}$, where ${\hat{x}}_{0}$ is a fixed starting point and the functions $\psi_{t}:{{{\mathbb{R}}^{d} \times {\mathbb{R}}^{p} \times {\mathbb{R}}^{q}}\rightarrow{\mathbb{R}}^{d}}$ are assumed to be continuously differentiable. Precise assumptions for convergence are detailed in Sec. 2.

Optimality is measured through convex costs $h_{t}$, $g_{t}$, on the state and control variables $x_{t}$, $u_{t}$ respectively, defining the objective where $\overline{x} = {(x_{1};\ldots;x_{\tau})} \in {\mathbb{R}}^{\taud}$ is the trajectory, $\overline{u} = {(u_{0};\ldots;u_{\tau - 1})} \in {\mathbb{R}}^{\taup}$ is the command, ${h{(\overline{x})}} = {\sum_{t = 1}^{\tau}{h_{t}{(x_{t})}}}$ and ${g{(\overline{u})}} = {\sum_{t = 0}^{\tau - 1}{g_{t}{(u_{t})}}}$, and in the following we denote by $\overline{w} = {(w_{0};\ldots;w_{\tau - 1})} \in {\mathbb{R}}^{\tauq}$ the noise. For a given command $\overline{u}$, the dynamics in define a probability distribution on the trajectories $\overline{x}$ that we denote $p{(\overline{x};\overline{u})}$.

The standard objective consists in minimizing the expected cost ${{\min_{\overline{u} \in {\mathbb{R}}^{\taup}}{{\mathbb{E}}_{\overline{x} \sim {p{(\cdot;\overline{u})}}}\left\lbrack {h{(\overline{x})}} \right\rbrack}} + {g{(\overline{u})}}},$ where $\overline{x}$ is a random variable following the model. We focus on risk-sensitive applications by minimizing for a given positive parameter $\theta > 0$. If the dynamics are bounded, the risk-sensitive objective is well defined for any $\overline{u}$, otherwise it is only defined for small enough values of $\theta$ as illustrated in the linear quadratic case of Prop. 1.1. The risk-sensitive objective seeks to minimize not only the expected objective but also higher moments as can be seen by expanding it around $\theta = 0$, which also shows that for $\theta\rightarrow 0$ we retrieve the expected cost. In Fig. 1 we illustrate the smoothness effect of the risk-sensitive objective, which, for larger values of $\theta$, tends to select the most stable minimizers, i.e., the ones with the largest valley, see for a detailed discussion. An application of the risk-sensitive cost is to make the controller robust to a random disturbance noise that would affect the dynamics at a given time (like a kick on the machine). Although the risk-sensitive controller may not pick the minimal cost of the original function, we can expect the risk-sensitive controller to be robust against disturbance noise as illustrated in Fig. 2.

Figure 1: Effect of the risk-sensitive parameter θ for ${f_{\theta}{(x)}} = {\frac{1}{\theta}{\log{{\mathbb{E}}_{w \sim {\mathcal{N}{}}}\left\lbrack {{\exp{\thetaF}}{({x + w})}} \right\rbrack}}}$ with F illustrated by the black line.

Figure 2: Expected behavior of the risk-sensitive controllers for increasing disturbance noise.

### Linear Quadratic Exponential Gaussian control

The resolution of non-linear risk-sensitive control problems rest on the linear quadratic case whose properties are recalled below.

### Proposition 1.1

Consider quadratic objectives and linear dynamics defined by where $H_{t} \succeq 0$, $G_{t} \succ 0$, $w_{t} \sim {\mathcal{N}{(0,{\sigma^{2}I_{q}})}}$. and denote by $H,\overset{\sim}{B},\overset{\sim}{C},{\overset{\sim}{x}}_{0}$ the matrices and vector such that for any trajectory $\overline{x}$, $H = {{\nabla^{2}h}{(\overline{x})}}$, $\overline{x} = {{\overset{\sim}{B}\overline{u}} + {\overset{\sim}{C}\overline{w}} + {\overset{\sim}{x}}_{0}}$. We have that the risk sensitive control problem is equivalent to^11^1By equivalent, we mean that the two problems share the same set of minimizers. where $Q$ is a quadratic in $\overline{u},\overline{w}$ obtained from the right hand side by expressing $\overline{x}$ in terms of $\overline{u},\overline{w}$, if ${({\theta\sigma^{2}})}^{- 1} < {\lambda_{\max}{({{\overset{\sim}{C}}^{\top}H\overset{\sim}{C}})}}$ the quadratic $Q$ is not concave in $\overline{w}$ such that the risk-sensitive objective is not defined, if ${({\theta\sigma^{2}})}^{- 1} > {\lambda_{\max}{({{\overset{\sim}{C}}^{\top}H\overset{\sim}{C}})}}$, the quadratic $Q$ is strongly concave in $\overline{w}$ and the risk-sensitive problem can be solved analytically by dynamic programming.

The resolution of the control problem by dynamic programming checks if the quadratic defining the objective is concave in $\overline{w}$ during the backward pass, otherwise the problem is not defined. Each cost-to-go function is indeed a quadratic whose positive-definiteness determines the feasibility of the problem. The detailed implementation is provided in Appendix B.

### Iterative Linearized Quadratic Exponential Gaussian

A common method to tackle the non-linear risk-sensitive control problem is the Iterative Linearized Quadratic Exponential Gaussian (ILEQG) algorithm, that (i) linearizes the dynamics and approximates quadratically the objectives around the current command and associated noiseless trajectory, (ii) solves the associated linear quadratic problem to get an update direction, (iii) moves along the update direction using a line-search.

Formally, at a given command ${\overline{u}}^{(k)}$ with associated noiseless trajectory ${\overline{x}}^{(k)}$ given by $x_{0}^{(k)} = {\hat{x}}_{0}$, $x_{t + 1}^{(k)} = {\psi_{t}{(x_{t}^{(k)},u_{t}^{(k)},0)}}$, am update direction is given by the solution ${\overline{v}}^{\ast}$, if it exists, of The next command is given by where $\gamma$ is a step-size chosen by line-search. The complete pseudo-code is presented in Appendix C. The objective of this work is to understand the relevance of this method and to improve its implementation by answering the following questions: Does ILEQG ensure the decrease of the risk-sensitive objective? If yes, what is its rate of convergence?

How can the step-size be chosen to ensure the monotonicity of the algorithm in a principled way?

## Iterative linearized risk-sensitive control

### Model minimization

We analyze the ILEQG method as a model-minimization scheme. To ease the exposition, we consider the case of additive noise, i.e., dynamics of the form, for bounded continuously differentiable dynamics $\phi_{t}:{{{\mathbb{R}}^{d} \times {\mathbb{R}}^{p}}\rightarrow{\mathbb{R}}^{d}}$. Note that it implies $p = q$ in the previous framework. The algorithm and its interpretation can be extended to the general case, see Appendix C and D.

First, we consider the noiseless trajectory as a function $\overset{\sim}{x}:{{\mathbb{R}}^{\taup}\rightarrow{\mathbb{R}}^{\taud}}$ of the control variables, decomposed as ${\overset{\sim}{x}{(\overline{u})}} = {({{\overset{\sim}{x}}_{1}{(\overline{u})}};\ldots;{{\overset{\sim}{x}}_{\tau}{(\overline{u})}})}$ where such that the noisy trajectory is given by $\overset{\sim}{x}{({\overline{u} + \overline{w}})}$. The risk sensitive objective can then be written as where, here and thereafter, $\overline{w} \sim {\mathcal{N}{(0,{\sigma^{2}I_{\taup}})}}$ unless specified differently. Now, at a current command $\overline{u}$, for a given control deviation $\overline{v}$, the random trajectory $\overset{\sim}{x}{({\overline{u} + \overline{v} + \overline{w}})}$ is approximated as a perturbed trajectory of $\overset{\sim}{x}{(\overline{u})}$, by The objective is then approximated as ${f_{\theta}{({\overline{u} + \overline{v}})}} \approx {m_{f_{\theta}}{({\overline{u} + \overline{v}};\overline{u})}}$, where ${q_{h}{({\overline{x} + \overline{y}};\overline{x})}} \triangleq {{h{(\overline{x})}} + {{\nabla h}{(\overline{x})}^{\top}\overline{y}} + {{{\overline{y}}^{\top}{\nabla^{2}h}{(\overline{x})}\overline{y}}/2}}$, $q_{g}{({\overline{u} + \overline{v}};\overline{u})}$ is defined similarly and $\overline{x} = {\overset{\sim}{x}{(\overline{u})}}$ is the noiseless trajectory. As the following proposition clarifies, the update direction computed by ILEQG in is given by minimizing directly the model $m_{f_{\theta}}$. Yet, from an optimization viewpoint, a regularization term must be added to this minimization to ensure that the solutions stay in a region where the model is valid. Formally, we consider a regularized variant of ILEQG, we call RegILEQG, that starts at a point ${\overline{u}}^{}$ and defines the next iterate as where $\gamma_{k}$ is the step-size: the smaller $\gamma_{k}$ is, the closer the solution is to the current iterate. The following proposition shows that the minimization step amounts to a linear quadratic exponential Gaussian risk-sensitive control problem.

### Proposition 2.1

The model minimization step is given as ${\overline{u}}^{({k + 1})} = {{\overline{u}}^{(k)} + {\overline{v}}^{\ast}}$ where ${\overline{v}}^{\ast}$ is the solution, if it exists, of where, denoting $x_{t}^{(k)} = {{\overset{\sim}{x}}_{t}{({\overline{u}}^{(k)})}}$, Each model-minimization step can then be performed by dynamic programming. The overall algorithm for general dynamics of the form is presented in Appendix C. Note that for simplified dynamics, the matrix $C_{t}$ defined in reduces to $B_{t}$. As detailed in Appendix C, ILEQG is indeed an instance of RegILEQG with infinite step-size. If the costs depend only on the final state, i.e., ${h{(\overline{x})}} = {h_{\tau}{(x_{\tau})}}$, the steps can be computed more efficiently by making calls to automatic differentiation oracles, see Appendix C for more details.

### Convergence analysis

We analyze the behavior of the regularized variant of ILEQG for quadratic convex costs $h_{t}$, $g_{t}$, a common setting in applications. Our main contribution is to show that the algorithm can be seen to minimize a surrogate of the risk-sensitive cost. The algorithm can indeed be decomposed in two different approximations: the random trajectories are approximated by Gaussians defined by the linearization of the dynamics, the non-linear control of the trajectory is approximated by a linear control defined by the linearization of the dynamics.

We show that the first approximation makes the algorithm work on a surrogate of the true risk-sensitive objective. By identifying this surrogate, we can improve the implementation of the algorithm.

### Surrogate risk-sensitive cost

By approximating the noisy trajectory by a Gaussian variable using first-order information of the trajectory, we define the surrogate risk-sensitive objective as follows The surrogate risk-sensitive objective is essentially the log-partition function of a Gaussian distribution defined by the linearized trajectory as shown in the following proposition.

### Proposition 2.2

For $\overline{u} \in {\mathbb{R}}^{\taup}$ with $\overline{x} = {\overset{\sim}{x}{(\overline{u})}}$, if the surrogate ${\hat{\eta}}_{\theta}$ in is well-defined and is the scaled log-partition function of which is the density of a Gaussian $\mathcal{N}{({\overline{w}}_{\ast},\Sigma)}$ with where $X = {{\nabla\overset{\sim}{x}}{(\overline{u})}}$, ${\overset{\sim}{h} = {{\nabla h}{(\overline{x})}}},{H = {{\nabla^{2}h}{(\overline{x})}}}$ and $\overline{x} = {\overset{\sim}{x}{(\overline{u})}}$. Therefore, the surrogate risk-sensitive objective can be computed analytically.

The approximation error induced by using the surrogate instead of the original risk-sensitive cost is illustrated in Sec. 3. Note that the surrogate ${\hat{\eta}}_{\theta}{(\overline{u})}$ in shares similar properties as the original cost, since it can be extended around $\theta = 0$ to Namely, it accounts not only for the cost of the noiseless trajectory but also for the variance defined by the linearized trajectories. Provided that condition holds, the gradient of the surrogate risk-sensitive cost reads (see Appendix D) where $\hat{p}{(\cdot;\overline{u})}$ is defined. The analysis of the algorithm requires to define also the truncated gradient of the surrogate risk-sensitive cost as We link the model-minimization steps of the regularized variant of ILEQG to the truncated gradient in the following proposition.

### Proposition 2.3

Consider the regularized iterative linear exponential Gaussian iteration, if condition holds on ${\overline{u}}^{(k)}$, the model $m_{f_{\theta}}$ in is well-defined and convex and the step reads and $X = {{\nabla\overset{\sim}{x}}{({\overline{u}}^{(k)})}}$, $H = {{\nabla^{2}h}{(\overline{x})}}$, $G = {{\nabla^{2}g}{({\overline{u}}^{(k)})}}$, $\overline{x} = {\overset{\sim}{x}{({\overline{u}}^{(k)})}}$.

### Convergence to stationary points

We make the following assumptions for our analysis.

### Assumption 2.4

The dynamics $\phi_{t}$ are twice differentiable, bounded, Lipschitz, smooth such that the trajectory function $\overset{\sim}{x}$ is also twice differentiable, bounded, Lipschitz and smooth. Denote by $\ell_{\overset{\sim}{x}}$ and $L_{\overset{\sim}{x}}$ the Lipschitz continuity and smoothness constants respectively of $\overset{\sim}{x}$ and define $M_{\overset{\sim}{x}} = {\max_{\overline{u} \in {\mathbb{R}}^{\taup}}{{dist}{({\overset{\sim}{x}{(\overline{u})}},X^{\ast})}}}$, where $X^{\ast} = {{{\arg\min}_{\overline{x} \in {\mathbb{R}}^{\taud}}h}{(\overline{x})}}$.

The costs $h$ and $g$ are convex quadratics with smoothness constants $L_{h},L_{g}$.

The risk-sensitivity parameter is chosen such that ${\overset{\sim}{\sigma}}^{- 2} = {\sigma^{- 2} - {\thetaL_{h}\ell_{\overset{\sim}{x}}^{2}}} > 0$, which ensures that condition holds for any $\overline{u} \in {\mathbb{R}}^{\taup}$.

The following proposition shows stationary convergence for the regularized variant of ILEQG as an optimization method of the surrogate risk-sensitive cost. The additional constant term is due to the truncation of the gradient of the surrogate risk-sensitive cost.

### Theorem 2.5

Under Asm. 2.4, suppose that the step-sizes of the regularized iterative linear exponential Gaussian iteration are chosen such that with $\gamma_{k} \in {\lbrack\gamma_{\min},\gamma_{\max}\rbrack}$. Then, the surrogate objective ${\hat{f}}_{\theta}$ decreases and after $K$ iterations we have Previous proposition gives a criterion for line-searches. We show in Appendix D that there exists a step-size $\hat{\gamma}$ such that condition is satisfied along the iterations. With this step-size, the number of steps to get an $\epsilon + \delta$ stationary point is at most

## Numerical experiments

### Experimental setting

Detailed description of the parameters setting can be found in Appendix E.

### Control settings

We apply the risk-sensitive framework to two classical continuous time control settings: swinging-up a pendulum and moving a two-link arm robot, both detailed in Appendix E. Their discretization leads to dynamics of the form for $t = {0,{{\ldots\tau} - 1}}$, where $x_{1},x_{2}$ describe the position and the speed of the system respectively, $f$ defines the dynamics derived by Newton's law, $\delta$ is the time step, $u$ is a force that controls the system.

### Noise modeling

The risk-sensitive cost is defined by an additional noisy force applied to the dynamics. Formally, the discretized dynamics are modified as for $t = {0,\ldots,{\tau - 1}}$, where $w_{t} \sim {\mathcal{N}{(0,{\sigma^{2}I_{p}})}}$ and $\sigma$ is chosen to avoid chaotic behavior, see Appendix E.

We test the optimized expected or risk-sensitive costs on a setting where the dynamics are perturbed at a given time $t_{w}$ by a force of amplitude $\rho$. This models the robustness of the control against kicking the robot. Formally, we analyze the performance of the solutions of the expected cost (denoted $\theta = 0$) or the risk-sensitive cost on dynamics of the form for $t = {0,\ldots,{\tau - 1}}$, where $\rho \sim {\mathcal{N}{(0,{\sigma_{test}I_{p}})}}$ with the same cost $h{(\overline{x})}$ computed as an average on $n = 100$ simulations. We call this cost the test cost.

### Results

Figure 3: Convergence of iterative linearized methods, RegILEQG and ILEQG, on the pendulum problem. Figure 4: Risk-sensitive and gradient approximations. Figure 5: Robustness of controllers against disturbance noise.

### Convergence

In Fig. 5 we compare the convergence on the pendulum problem of RegILEQG and ILEQG. For both algorithms, we use a constant step-size sequence tuned after a burn-in phase of 5 iterations on a grid of step-sizes $2^{i}$ for $i \in {\lbrack{- 5},10\rbrack}$. The surrogate risk-sensitive cost was used to tune the step-sizes. The best step-sizes found were $0.5$ for ILEQG and $16$ for RegILEQG. We plot the minimum values obtained until now, as the true function can be approximated. We observe that both ILEQG and RegILEQG minimize well the surrogate risk-sensitive cost. Yet, the regularized variant provides smoother convergence. We leave as future work the implementation of line-search procedures as done for Levenberg-Marquardt methods.

### Risk-sensitive cost approximation

In Fig. 5, we compare ${{\hat{f}}_{\theta}{({\overline{u}}^{(k)})}},{\|{{\nabla{\hat{f}}_{\theta}}{({\overline{u}}^{(k)})}}\|}_{2}$ computed by the Gaussian approximation given in and ${f_{\theta}{({\overline{u}}^{(k)})}},{\|{{\nabla f_{\theta}}{({\overline{u}}^{(k)})}}\|}_{2}$ approximated by Monte-Carlo for $N = 100$ samples and 10 runs. We plot these values along the iterations of the RegILEQG method for the pendulum (same experiment as in Fig. 5). We observe that the approximation ${\hat{f}}_{\theta}{({\overline{u}}^{(k)})}$ is close to the approximation by Monte-Carlo. The sequence of compositions defining the trajectory leads to highly non-smooth functions (i.e. large smoothness constants), which contributes to the high variance of gradients computed by Monte-Carlo.

### Robustness

In Fig. 5, we plot the test cost obtained by the expected or risk-sensitive optimizers on the movement perturbed by a Dirac of increasing strength. We use our RegILEQG algorithm with constant-step-size tuned after a burn-in phase. The risk-sensitive approach provides smaller costs against perturbed trajectories. On the two-link-arm problem, we did not observe significant changes when varying the risk-sensitivity parameter. We leave the analysis of the choice of the parameter for future work.

## Conclusion

We dissected the ILEQG algorithm to understand its correct implementation, this revealed: (i) the objective it minimizes, that is not the risk-sensitive cost but an approximation of it, (ii) the necessary introduction from an optimization viewpoint of a regularization inside the step, (iii) a sufficient decrease condition that ensures proven stationary convergence to a near-stationary point.
