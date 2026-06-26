<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Convergence of the Iterative Linear Exponential Quadratic Gaussian Algorithm to Stationary Points

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A classical method for risk-sensitive nonlinear control is the iterative linear exponential quadratic Gaussian algorithm. We present its convergence analysis from a first-order optimization viewpoint. We identify the objective that the algorithm actually minimizes and we show how the addition of a proximal term guarantees convergence to a stationary point.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present a convergence analysis of the classical iterative linear quadratic exponential Gaussian controller (ILEQG) for finite-horizon risk-sensitive or safe nonlinear control. The ILEQG algorithm is particularly popular in robotics applications and can be seen as a risk-sensitive counterpart of the iterative linear quadratic Gaussian (ILQG) algorithm. We adopt here the viewpoint of the modern complexity analysis of first-order optimization algorithms as done by Roulet et al. for ILQG.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We address the following questions: (i) what is the convergence rate of ILEQG to a stationary point? (ii) how can we set the step-size to guarantee a decreasing objective along the iterations? The analysis we present here sheds light on these questions by highlighting the objective minimized by ILEQG which is a Gaussian approximation of a risk-sensitive cost around the linearized trajectory. We underscore the importance of the addition of a proximal regularization component for ILEQG to guarantee a worst-case convergence to a stationary point of the objective.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main result of the paper is Theorem 2.5, where a sufficient decrease condition to choose the strength of the proximal regularization is given. The result also yields a complexity bound in terms of calls to a dynamic programming procedure implementable in a "differentiable programming" framework, that is, a computational framework equipped with an automatic differentiation software library. We illustrate the variant of the iterative regularized linear quadratic exponential Gaussian controller we recommend on simple risk-sensitive nonlinear control examples.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

We consider discretized control problems stemming from continuous time settings with finite-horizon, see Appendix E for the discretization step. Those are off-line control problems used for example at each step of a model predictive control framework. We focus on the control of a trajectory of length $\tau$ composed of state variables ${x_{1},\ldots,x_{\tau}} \in {\mathbb{R}}^{d}$ and controlled by parameters ${u_{0},\ldots,u_{\tau - 1}} \in {\mathbb{R}}^{p}$ through dynamics $\psi_{t}$ perturbed by i.i.d.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

The standard objective consists in minimizing the expected cost ${{\min_{\overline{u} \in {\mathbb{R}}^{\taup}}{{\mathbb{E}}_{\overline{x} \sim {p{(\cdot;\overline{u})}}}\left\lbrack {h{(\overline{x})}} \right\rbrack}} + {g{(\overline{u})}}},$ where $\overline{x}$ is a random variable following the model. We focus on risk-sensitive applications by minimizing for a given positive parameter $\theta > 0$. If the dynamics are bounded, the risk-sensitive objective is well defined for any $\overline{u}$, otherwise it is only defined for small enough values of $\theta$ as illustrated in the linear quadratic case of Prop.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

1.1. The risk-sensitive objective seeks to minimize not only the expected objective but also higher moments as can be seen by expanding it around $\theta = 0$, which also shows that for $\theta\rightarrow 0$ we retrieve the expected cost. In Fig. 1 we illustrate the smoothness effect of the risk-sensitive objective, which, for larger values of $\theta$, tends to select the most stable minimizers, i.e., the ones with the largest valley, see for a detailed discussion. An application of the risk-sensitive cost is to make the controller robust to a random disturbance noise that would affect the dynamics at a given time (like a kick on the machine). Although the risk-sensitive controller may not pick the minimal cost of the original function, we can expect the risk-sensitive controller to be robust against disturbance noise as illustrated in Fig. 2.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Linear Quadratic Exponential Gaussian control", "weight": 1.0} -->

The resolution of non-linear risk-sensitive control problems rest on the linear quadratic case whose properties are recalled below.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Iterative Linearized Quadratic Exponential Gaussian", "weight": 1.0} -->

A common method to tackle the non-linear risk-sensitive control problem is the Iterative Linearized Quadratic Exponential Gaussian (ILEQG) algorithm, that (i) linearizes the dynamics and approximates quadratically the objectives around the current command and associated noiseless trajectory, (ii) solves the associated linear quadratic problem to get an update direction, (iii) moves along the update direction using a line-search.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Iterative Linearized Quadratic Exponential Gaussian", "weight": 1.0} -->

Formally, at a given command ${\overline{u}}^{(k)}$ with associated noiseless trajectory ${\overline{x}}^{(k)}$ given by $x_{0}^{(k)} = {\hat{x}}_{0}$, $x_{t + 1}^{(k)} = {\psi_{t}{(x_{t}^{(k)},u_{t}^{(k)},0)}}$, am update direction is given by the solution ${\overline{v}}^{\ast}$, if it exists, of The next command is given by where $\gamma$ is a step-size chosen by line-search. The complete pseudo-code is presented in Appendix C. The objective of this work is to understand the relevance of this method and to improve its implementation by answering the following questions: Does ILEQG ensure the decrease of the risk-sensitive objective? If yes, what is its rate of convergence?

<!-- chunk {"id": "body-0012", "role": "body", "section": "Iterative Linearized Quadratic Exponential Gaussian", "weight": 1.0} -->

How can the step-size be chosen to ensure the monotonicity of the algorithm in a principled way?

<!-- chunk {"id": "body-0013", "role": "body", "section": "Model minimization", "weight": 1.0} -->

We analyze the ILEQG method as a model-minimization scheme. To ease the exposition, we consider the case of additive noise, i.e., dynamics of the form, for bounded continuously differentiable dynamics $\phi_{t}:{{{\mathbb{R}}^{d} \times {\mathbb{R}}^{p}}\rightarrow{\mathbb{R}}^{d}}$. Note that it implies $p = q$ in the previous framework. The algorithm and its interpretation can be extended to the general case, see Appendix C and D.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Model minimization", "weight": 1.0} -->

The risk sensitive objective can then be written as where, here and thereafter, $\overline{w} \sim {\mathcal{N}{(0,{\sigma^{2}I_{\taup}})}}$ unless specified differently.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Model minimization", "weight": 1.0} -->

As the following proposition clarifies, the update direction computed by ILEQG in is given by minimizing directly the model $m_{f_{\theta}}$. Yet, from an optimization viewpoint, a regularization term must be added to this minimization to ensure that the solutions stay in a region where the model is valid. Formally, we consider a regularized variant of ILEQG, we call RegILEQG, that starts at a point ${\overline{u}}^{}$ and defines the next iterate as where $\gamma_{k}$ is the step-size: the smaller $\gamma_{k}$ is, the closer the solution is to the current iterate. The following proposition shows that the minimization step amounts to a linear quadratic exponential Gaussian risk-sensitive control problem.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Convergence analysis", "weight": 1.0} -->

We analyze the behavior of the regularized variant of ILEQG for quadratic convex costs $h_{t}$, $g_{t}$, a common setting in applications. Our main contribution is to show that the algorithm can be seen to minimize a surrogate of the risk-sensitive cost. The algorithm can indeed be decomposed in two different approximations: the random trajectories are approximated by Gaussians defined by the linearization of the dynamics, the non-linear control of the trajectory is approximated by a linear control defined by the linearization of the dynamics.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Convergence analysis", "weight": 1.0} -->

We show that the first approximation makes the algorithm work on a surrogate of the true risk-sensitive objective. By identifying this surrogate, we can improve the implementation of the algorithm.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Surrogate risk-sensitive cost", "weight": 1.0} -->

By approximating the noisy trajectory by a Gaussian variable using first-order information of the trajectory, we define the surrogate risk-sensitive objective as follows The surrogate risk-sensitive objective is essentially the log-partition function of a Gaussian distribution defined by the linearized trajectory as shown in the following proposition.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Convergence to stationary points", "weight": 1.0} -->

We make the following assumptions for our analysis.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption 2.4", "weight": 1.0} -->

The costs $h$ and $g$ are convex quadratics with smoothness constants $L_{h},L_{g}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 2.4", "weight": 1.0} -->

The following proposition shows stationary convergence for the regularized variant of ILEQG as an optimization method of the surrogate risk-sensitive cost. The additional constant term is due to the truncation of the gradient of the surrogate risk-sensitive cost.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Experimental setting", "weight": 1.0} -->

Detailed description of the parameters setting can be found in Appendix E.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Control settings", "weight": 1.0} -->

We apply the risk-sensitive framework to two classical continuous time control settings: swinging-up a pendulum and moving a two-link arm robot, both detailed in Appendix E. Their discretization leads to dynamics of the form for $t = {0,{{\ldots\tau} - 1}}$, where $x_{1},x_{2}$ describe the position and the speed of the system respectively, $f$ defines the dynamics derived by Newton's law, $\delta$ is the time step, $u$ is a force that controls the system.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Noise modeling", "weight": 1.0} -->

The risk-sensitive cost is defined by an additional noisy force applied to the dynamics. Formally, the discretized dynamics are modified as for $t = {0,\ldots,{\tau - 1}}$, where $w_{t} \sim {\mathcal{N}{(0,{\sigma^{2}I_{p}})}}$ and $\sigma$ is chosen to avoid chaotic behavior, see Appendix E.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Noise modeling", "weight": 1.0} -->

We test the optimized expected or risk-sensitive costs on a setting where the dynamics are perturbed at a given time $t_{w}$ by a force of amplitude $\rho$. This models the robustness of the control against kicking the robot. Formally, we analyze the performance of the solutions of the expected cost (denoted $\theta = 0$) or the risk-sensitive cost on dynamics of the form for $t = {0,\ldots,{\tau - 1}}$, where $\rho \sim {\mathcal{N}{(0,{\sigma_{test}I_{p}})}}$ with the same cost $h{(\overline{x})}$ computed as an average on $n = 100$ simulations. We call this cost the test cost.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Convergence", "weight": 1.0} -->

In Fig. 5 we compare the convergence on the pendulum problem of RegILEQG and ILEQG. For both algorithms, we use a constant step-size sequence tuned after a burn-in phase of 5 iterations on a grid of step-sizes $2^{i}$ for $i \in {\lbrack{- 5},10\rbrack}$. The surrogate risk-sensitive cost was used to tune the step-sizes. The best step-sizes found were $0.5$ for ILEQG and $16$ for RegILEQG. We plot the minimum values obtained until now, as the true function can be approximated. We observe that both ILEQG and RegILEQG minimize well the surrogate risk-sensitive cost. Yet, the regularized variant provides smoother convergence. We leave as future work the implementation of line-search procedures as done for Levenberg-Marquardt methods.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Risk-sensitive cost approximation", "weight": 1.0} -->

We observe that the approximation ${\hat{f}}_{\theta}{({\overline{u}}^{(k)})}$ is close to the approximation by Monte-Carlo. The sequence of compositions defining the trajectory leads to highly non-smooth functions (i.e. large smoothness constants), which contributes to the high variance of gradients computed by Monte-Carlo.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Robustness", "weight": 1.0} -->

In Fig. 5, we plot the test cost obtained by the expected or risk-sensitive optimizers on the movement perturbed by a Dirac of increasing strength. We use our RegILEQG algorithm with constant-step-size tuned after a burn-in phase. The risk-sensitive approach provides smaller costs against perturbed trajectories. On the two-link-arm problem, we did not observe significant changes when varying the risk-sensitivity parameter. We leave the analysis of the choice of the parameter for future work.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We dissected the ILEQG algorithm to understand its correct implementation, this revealed: (i) the objective it minimizes, that is not the risk-sensitive cost but an approximation of it, (ii) the necessary introduction from an optimization viewpoint of a regularization inside the step, (iii) a sufficient decrease condition that ensures proven stationary convergence to a near-stationary point.
