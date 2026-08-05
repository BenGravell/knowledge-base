<!-- arxiv-full-text:v1 {"arxiv_id": "1908.07615", "source": "ar5iv"} -->

## Introduction

Finite horizon discrete time nonlinear control has been studied for decades, with applications ranging from spacecraft dynamics to robot learning. Popular nonlinear control algorithms, such as differential dynamic programming or iterative linear quadratic Gaussian algorithms, are commonly derived using a linearization argument relating the nonlinear control problem to a linear control problem.

We examine nonlinear control algorithms based on iterative linearization techniques through the lens of the modern complexity analysis of first-order optimization algorithms. We first reformulate the problem as the minimization of an objective that is written as a composition of functions. Owing to this reformulation, we can frame several popular nonlinear control algorithms as first-order optimization algorithms applied to this objective.

We highlight the equivalence of dynamic programming and gradient back-propagation in this framework and underline the central role of the corresponding automatic differentiation oracle in the complexity analysis in terms of convergence to a stationary point of the objective. We show that the number of calls to this automatic differentiation oracle is the relevant complexity measure given the outreach of machine learning software libraries such as PyTorch or TensorFlow.

Along the way we propose several improvements to the iterative linear quadratic regulator (ILQR) algorithm, resulting in an accelerated regularized Gauss-Newton algorithm enjoying a complexity bound in terms of convergence to a stationary point and displaying stable convergence behavior in practice. Regularized Gauss-Newton algorithms give a template for the design of algorithms based on partial linearization with guaranteed convergence. The proposed accelerated regularized Gauss-Newton algorithm is based on a Gauss-Newton linearization step stabilized by a proximal regularization and boosted by a Catalyst extrapolation scheme, potentially accelerating convergence while preserving the worst-case guarantee.

### Related work

Differential dynamic programming (DDP) and iterative linearization algorithms are popular algorithms for finite horizon discrete time nonlinear control. DDP is based on approximating the Bellman equation at the current trajectory in order to use standard dynamic programming. Up to our knowledge, the complexity analysis of DDP has been limited; see for classical analyses of DDP.

Iterative linearization algorithms such as the iterative linear quadratic regulator (ILQR) or the iterative linearized Gaussian algorithm (ILQG) linearize the trajectory in order to use standard dynamic programming. Again, the complexity analysis of ILQR for instance has been limited. In this paper, we refer to the definitions of ILQR and ILQG as given in the original papers, the same names have been then used for variants of those algorithms that use a roll-out phase on the true trajectory as , e.g., where line-searches were proposed. Line-searches akin to the Levenberg-Marquardt method were proposed but without convergence rates. It is worthwhile to mention related approaches in the nonlinear model predictive control area.

We adopt the point of view of the complexity theory of first-order optimization algorithms. The computation of a Gauss-Newton step (or a Newton step) through dynamic programming for nonlinear control problems is classical; see. However, while the importance of the addition of a proximal term in Gauss-Newton algorithms is now well-understood, several popular nonlinear control algorithms involving such steps, such as ILQR, have not been revisited yet. Our work shows how to make these improvements.

We also show how gradient back-propagation, i.e., automatic differentiation, a popular technique usually derived using either a chain rule argument or a Lagrangian framework, allows one to solve the dynamic programming problems arising in linear quadratic control. Consequently, the subproblems that arise when using iterative linearization for nonlinear control can be solved with calls to an automatic differentiation oracle implementable in PyTorch or TensorFlow.

The regularized Gauss-Newton method was extensively studied to minimize the nonlinear least squares objectives arising in inverse problems. The complexity-based viewpoint used in informs our analysis and offers generalizations to locally Lipschitz objectives. We build upon these results in particular when equipping the proposed regularized Gauss-Newton algorithm with an extrapolation scheme in the spirit of.

All notations are presented in Appendix A. The code for this project is available at

## Discrete time control

We first present the framework of finite horizon discrete time nonlinear control.

### Exact dynamics

Given state variables $x \in {\mathbb{R}}^{d}$ and control variables $u \in {\mathbb{R}}^{p}$, we consider the control of finite trajectories $\overline{x} = {(x_{1};\ldots;x_{\tau})} \in {\mathbb{R}}^{\taud}$ of horizon $\tau$ whose dynamics are controlled by a command $\overline{u} = {(u_{0};\ldots;u_{\tau - 1})} \in {\mathbb{R}}^{\taup}$, through starting from a given ${\hat{x}}_{0} \in {\mathbb{R}}^{d}$, where the functions $\phi_{t}:{{{\mathbb{R}}^{d} \times {\mathbb{R}}^{p}}\rightarrow{\mathbb{R}}^{d}}$ are assumed to be differentiable.

Optimality is measured through convex costs $h_{t}$, $g_{t}$, on the state and control variables $x_{t}$, $u_{t}$ respectively, defining the discrete time nonlinear control problem where, here and thereafter, the dynamics must be satisfied for $t = {0,\ldots,{\tau - 1}}$.

### Noisy dynamics

The discrepancy between the model and the dynamics can be taken into account by considering noisy dynamics as where $w_{t} \sim {\mathcal{N}{(0,I_{q})}}$ for $t = {0,\ldots,{\tau - 1}}$. The resulting discrete time control problem consists of optimizing the average cost under the noise $\overline{w} = {(w_{0};\ldots;w_{\tau - 1})}$ as | | \min\limits_{\substack{{x_{0},\ldots,x_{\tau}} \in {\mathbb{R}}^{d} \\ {u_{0},\ldots,u_{\tau - 1}} \in {\mathbb{R}}^{p}}} & {{{\mathbb{E}}_{\overline{w}}\left\lbrack {\sum\limits_{t = 1}^{\tau}{h_{t}{(x_{t})}}} \right\rbrack} + {\sum\limits_{t = 0}^{\tau - 1}{g_{t}{(u_{t})}}}} \\ | | |

### Costs and penalties

The costs on the trajectory can be used to force the states to follow a given orbit ${\hat{x}}_{1},\ldots,{\hat{x}}_{\tau}$ as which gives a quadratic tracking problem, while the regularization penalties on the control variables are typically quadratic functions The regularization penalties can also encode constraints on the control variable such as the indicator function of a box where $\iota_{S}$ denotes the indicator function of a set $S$.

### Iterative Linear Control algorithms

We are interested in the complexity analysis of algorithms such as the iterative linear quadratic regulator (ILQR) algorithm as defined, used for exact dynamics, which iteratively computes the solution of where ${\overline{u}}^{(k)}$ is the current command, ${\overline{x}}^{(k)}$ is the corresponding trajectory given, $q_{h_{t}},q_{g_{t}}$ are quadratic approximations of the costs $h_{t},g_{t}$ around respectively $x_{t}^{(k)},u_{t}^{(k)}$ and $\ell_{\phi_{t}}$ is the linearization of $\phi_{t}$ around $(x_{t}^{(k)},u_{t}^{(k)})$. The next iterate is then given by ${\overline{u}}^{({k + 1})} = {{\overline{u}}^{(k)} + {\alpha{\overline{v}}^{\ast}}}$ where ${\overline{v}}^{\ast}$ is the solution of and $\alpha$ is a step-size given by a line-search method. To understand this approach, we frame the problem as the minimization of a composition of functions.

Note that the term ILQR or ILQG has then been used to refer to a variant of the above algorithm that uses the feedback gains computed in the resolution of the linear control problem to control to move along the true trajectory, see.

### Formulation as a composite optimization problem

We call an optimization problem a *composite optimization problem* if it consists in the minimization of a composition of functions. For a fixed command $\overline{u} \in {\mathbb{R}}^{\taup}$, denote by ${\overset{\sim}{x}{(\overline{u})}} = {({{\overset{\sim}{x}}_{1}{(\overline{u})}};\ldots;{{\overset{\sim}{x}}_{\tau}{(\overline{u})}})} \in {\mathbb{R}}^{\taud}$ the trajectory given by the exact dynamics, which reads Similarly denote by ${\overset{\sim}{x}{(\overline{u},\overline{w})}} \in {\mathbb{R}}^{\taud}$ the trajectory in the noisy case. Denoting the total cost by ${h{(\overline{x})}} = {\sum_{t = 1}^{\tau}{h_{t}{(x_{t})}}}$, the total penalty by ${g{(\overline{u})}} = {\sum_{t = 0}^{\tau - 1}{g_{t}{(u_{t})}}}$, the control problem with exact dynamics reads and with noisy dynamics, i.e., we obtain a composite optimization problem whose structure can be exploited to derive oracles on the objective.

## Oracles in discrete time control

We adopt here the viewpoint of the complexity theory of first-order optimization. Given the composite problem, what are the relevant oracles and what are the complexities of calls to these oracles? We first consider exact dynamics $\phi_{t}$ of the form and unconstrained cost penalties such as.

### Exact and unconstrained setting

### Model minimization

Each step of the optimization algorithm is defined by the minimization of a regularized model of the objective. For example, a *gradient step* on a point $\overline{u}$ with step-size $\gamma$ corresponds to linearizing both $h$ and $\overset{\sim}{x}$ and defining the linear model of the objective $f$, where ${\ell_{h}{({\overline{x} + \overline{y}};\overline{x})}} = {{h{(\overline{x})}} + {{\nabla h}{(\overline{x})}^{\top}\overline{y}}}$ and $\ell_{g}{({\overline{u} + \overline{v}};\overline{u})}$ is defined similarly. Then, this model with a proximal regularization is minimized in order to get the next iterate Different models can be defined to better approximate the objective. For example, if only the mapping $\overset{\sim}{x}$ is linearized, this corresponds to defining the convex model at a point $\overline{u}$ We get then a *regularized Gauss-Newton step* on a point $\overline{u} \in {\mathbb{R}}^{\taup}$ with step size $\gamma > 0$ as Although this model better approximates the objective, its minimization may be computationally expensive for general functions $h$ and $g$. We can use a quadratic approximation of $h$ around the current mapping $\overset{\sim}{x}{(\overline{u})}$ and linearize the trajectory around $\overline{u}$ which defines the quadratic model where ${q_{h}{({\overline{x} + \overline{y}};\overline{x})}} \triangleq {{h{(\overline{x})}} + {{\nabla h}{(\overline{x})}^{\top}\overline{y}} + {{{\overline{y}}^{\top}{\nabla^{2}h}{(\overline{x})}\overline{y}}/2}}$ and $q_{g}{({\overline{u} + \overline{v}};\overline{u})}$ is defined similarly. A *Levenberg-Marquardt step* with step-size $\gamma$ consists in minimizing the model with a proximal regularization

### Model-minimization steps by linear optimal control

Though the chain rule gives an analytic form of the gradient, we can use the definition of a gradient step as an optimization sub-problem to understand its implementation. Formally, the above steps define a model $m_{f}$ of the objective $f$ in on a point $\overline{u}$, as where $m_{h} = {\sum_{t = 1}^{\tau}m_{h_{t}}}$, $m_{g} = {\sum_{t = 0}^{\tau - 1}m_{g_{t}}}$ are models of $h$ and $g$ respectively, composed of models on the individual variables. The model-minimization step with step-size $\gamma$, amounts then to a linear control problem as shown in the following proposition.

### Proposition 2.1

The model-minimization step for control problem written as is given by ${\overline{u}}^{+} = {\overline{u} + {\overline{v}}^{\ast}}$ where ${\overline{v}}^{\ast} = {(v_{0}^{\ast};\ldots,v_{\tau - 1}^{\ast})}$ is the solution of where $\Phi_{t,x} = {{\nabla_{x}\phi_{t}}{(x_{t},u_{t})}}$, $\Phi_{t,u} = {{\nabla_{u}\phi_{t}}{(x_{t},u_{t})}}$ and $x_{t} = {{\overset{\sim}{x}}_{t}{(\overline{u})}}$.

### Proof

Recall that the trajectory defined by $\overline{u}$ reads where $F_{t} = {e_{t + 1} \otimes I_{p}} \in {\mathbb{R}}^{{\taup} \times p}$, $e_{t} \in {\mathbb{R}}^{\tau}$ is the $t$^th^ canonical vector in ${\mathbb{R}}^{\tau}$, such that ${F_{t}^{\top}\overline{u}} = u_{t}$. The gradient reads ${{\nabla{\overset{\sim}{x}}_{1}}{(\overline{u})}} = {F_{0}{\nabla_{u}\phi_{0}}{(x_{0},u_{0})}}$ followed by where $x_{t} = {{\overset{\sim}{x}}_{t}{(\overline{u})}}$ and $x_{0} = {\hat{x}}_{0}$. For a given $\overline{v} = {(v_{0};\ldots;v_{\tau - 1})}$, the product $\overline{y} = {(y_{1};\ldots;y_{\tau})} = {{\nabla\overset{\sim}{x}}{(\overline{u})}^{\top}\overline{v}}$ reads $y_{1} = {{\nabla_{u}\phi_{0}}{(x_{0},u_{0})}^{\top}v_{0}}$ followed by where we used that $y_{t} = {{\nabla{\overset{\sim}{x}}_{t}}{(\overline{u})}^{\top}\overline{v}}$. Plugging this into gives the result. ∎

### Dynamic programming

If the models used in are linear or quadratic, the resulting linear control problems can be solved efficiently using dynamic programming, i.e., with a linear cost in $\tau$, as presented in the following proposition. The cost is $\mathcal{O}{({\taup^{3}d^{3}})}$. Details on the implementation for quadratic costs are provided in Appendix B.

Since the leading dimension of the discrete time control problem is the length of the trajectory $\tau$, all of the above optimization steps have roughly the same cost. This means that, in discrete time control problems, *second order steps such as are roughly as expensive as gradient steps*.

### Proposition 2.2

Model-minimization steps of the form for discrete time control problem written as with linear or quadratic convex models $m_{h}$ and $m_{g}$ can be solved in linear time with respect to the length of the trajectory $\tau$ by dynamic programming.

The proof of the proposition relies on the dynamic programming approach explained below. The linear optimal control problem can be divided into smaller subproblems and then solved recursively. Consider the linear optimal control problem as where $\ell_{t}$ is a linear dynamic in state and control variables, $q_{g_{t}}$ are strongly convex quadratics and $q_{h_{t}}$ are convex quadratic or linear functions. For $0 \leq t \leq \tau$, given ${\hat{y}}_{t}$, define the cost-to-go from ${\hat{y}}_{t}$, as the solution of The cost-to-go functions can be computed recursively by the Bellman equation for $t \in {\{{\tau - 1},\ldots,0\}}$, solved for ${v_{t}^{\ast}{({\hat{y}}_{t})}} = {{\arg\min}_{v_{t}}\left\{ {{q_{g_{t}}{(v_{t})}} + {c_{t + 1}{({\ell_{t}{({\hat{y}}_{t},v_{t})}})}}} \right\}}$. The final cost initializing the recursion is defined as ${c_{\tau}{({\hat{y}}_{\tau})}} = {q_{h_{\tau}}{({\hat{y}}_{\tau})}}$. For quadratic costs and linear dynamics, the problems defined in are themselves quadratic problems that can be solved analytically to get an expression for $c_{t}$.

The solution of is given by computing $c_{0}{}$, which amounts to iteratively solving the Bellman equations starting from ${\hat{y}}_{0} = 0$. Formally, starting form $t = 0$ and ${\hat{y}}_{0} = 0$, it iteratively gets the optimal control $v_{t}^{\ast}$ at time $t$ defined by the analytic form of the cost-to-go function and moves along the dynamics to get the corresponding optimal next state, The cost of the overall dynamic procedure that involves a *backward* pass to compute the cost-to-go functions and a *roll-out* pass to compute the optimal controls is therefore linear in the length of the trajectory $\tau$. The main costs lie in solving quadratic problems in the Bellman equation which only depend on the state and control dimensions $d$ and $p$.

### Gradient back-propagation as dynamic programming

We illustrate the derivations for a gradient step in the following proposition that shows a cost of $\mathcal{O}{({\tau{({{pd} + d^{2}})}})}$. We recover the well-known gradient back-propagation algorithm used to compute the gradient of the objective. The dynamic programming viewpoint provides here a natural derivation.

### Proposition 2.3

A gradient step for discrete time control problem written as and solved by dynamic programming amounts to a *forward* pass that computes the derivatives ${\nabla_{x}\phi_{t}}{(x_{t},u_{t})}$, ${\nabla_{u}\phi_{t}}{(x_{t},u_{t})}$, ${\nabla h_{t}}{(x_{t})}$, ${\nabla g_{t}}{(u_{t})}$ for $t = {0,\ldots,\tau}$ along the trajectory given by $x_{t + 1} = {\phi_{t}{(x_{t},u_{t})}}$ for $t = 0 \ldots,\tau - 1$, a *backward* pass that computes linear cost-to-go functions as ${c_{t}{(y_{t})}} = {{\lambda_{t}^{\top}y_{t}} + \mu_{t}}$ where $\lambda_{\tau} = {{\nabla h_{\tau}}{(x_{\tau})}}$, $\lambda_{t} = {{{\nabla h_{t}}{(x_{t})}} + {{\nabla_{x}\phi_{t}}{(x_{t},u_{t})}\lambda_{t + 1}}}$, for $t = {{\tau - 1},{\ldots0}}$, a *roll-out* pass that outputs $v_{t}^{\ast} = {- {\gamma{({{{\nabla_{u}\phi_{t}}{(x_{t},u_{t})}\lambda_{t + 1}} + {{\nabla g_{t}}{(u_{t})}}})}}}$, for $t = {0,{{\ldots\tau} - 1}}$.

### Proof

Recall that a gradient step is given as ${\overline{u}}^{+} = {\overline{u} + {\overline{v}}^{\ast}}$ where ${\overline{v}}^{\ast}$ is the solution of where ${\ell_{h}{({\overline{x} + \overline{y}};\overline{x})}} = {{h{(\overline{x})}} + {{\nabla h}{(\overline{x})}^{\top}\overline{y}}}$ and $\ell_{g}{({\overline{u} + \overline{v}};\overline{u})}$ is defined similarly. From Prop. 2.1, we get that it amounts to a linear optimal control problem of the form where $a_{t} = {{\nabla h_{t}}{(x_{t})}}$, $b_{t} = {{\nabla g_{t}}{(u_{t})}}$, $\Phi_{t,x} = {{\nabla_{x}\phi_{t}}{(x_{t},u_{t})}}$, $\Phi_{t,u} = {{\nabla_{u}\phi_{t}}{(x_{t},u_{t})}}$ and $x_{t} = {{\overset{\sim}{x}}_{t}{(\overline{u})}}$. The definition of the linear problem is the *forward* pass.

When solving with dynamic programming, cost-to-go functions are linear, ${c_{t}{(y)}} = {{\lambda_{t}^{\top}y} + \mu_{t}}$. Recursion starts with $\lambda_{\tau} = a_{\tau}$, $\mu_{\tau} = 0$. Then, assuming ${c_{t + 1}{(y)}} = {{\lambda_{t + 1}^{\top}y} + \mu_{t + 1}}$ for $t \in {\{{\tau - 1},\ldots,0\}}$, we get and so we identify $\lambda_{t} = {a_{t} + {\Phi_{t,x}\lambda_{t + 1}}}$ and $\mu_{t} = {\mu_{t + 1} + {\frac{\gamma}{2}{\|{b_{t} + {\Phi_{t,u}\lambda_{t + 1}}}\|}_{2}^{2}}}$ that define the cost-to-go function at time $t$. This defines the *backward* pass.

The optimal control variable at time $t$ is then independent of the starting state and reads, This defines the *roll-out* pass. ∎

### Noisy or constrained settings

### Noisy dynamics

For inexact dynamics defining the problem, we consider a Gaussian approximation of the linearized trajectory around the exact current trajectory. Formally, the Gaussian approximation of the random linearized trajectory ${\ell_{\overset{\sim}{x}}{({\overline{u} + \overline{v}};\overline{u},\overline{w})}} = {{\overset{\sim}{x}{(\overline{u},\overline{w})}} + {{\nabla_{\overline{u}}\overset{\sim}{x}}{(\overline{u},\overline{w})}^{\top}\overline{v}}}$ around the exact linearized trajectory given for $\overline{w} = 0$ reads which satisfies ${{\mathbb{E}}_{\overline{w}}{\lbrack{{\hat{\ell}}_{\overset{\sim}{x}}{({\overline{u} + \overline{v}};\overline{u},\overline{w})}}\rbrack}} = {{\overset{\sim}{x}{(\overline{u},0)}} + {{\nabla_{\overline{u}}\overset{\sim}{x}}{(\overline{u},0)}^{\top}\overline{v}}}$, see Appendix A for gradient and tensor notations.

The model we consider for the state cost is then of the form For simple dynamics $\phi_{t}$, their minimization with an additional proximal term amounts to a linear quadratic Gaussian control problem as stated in the following proposition.

### Proposition 2.4

Assume $\nabla_{xx}^{2}\phi_{t}$, $\nabla_{xw}^{2}\phi_{t}$ and $\nabla_{ux}^{2}\phi_{t}$ to be zero. The model minimization step for model is given by ${\overline{u}}^{+} = {\overline{u} + {\overline{v}}^{\ast}}$ where ${\overline{v}}^{\ast}$ is the solution of where $\Phi_{t,x} = {{\nabla_{x}\phi_{t}}{(x_{t},u_{t},0)}}$, $\Phi_{t,u} = {{\nabla_{u}\phi_{t}}{(x_{t},u_{t},0)}}$, $\Phi_{t,w} = {{\nabla_{w}\phi_{t}}{(x_{t},u_{t},0)}}$, $\phi_{t,u,w} = {{\nabla_{uw}^{2}\phi_{t}}{(x_{t},u_{t},0)}}$, $x_{t} = {{\overset{\sim}{x}}_{t}{(\overline{u},0)}}$.

### Proof

The Gaussian approximation ${\hat{\ell}}_{\overset{\sim}{x}}{({\overline{u} + \overline{v}};\overline{u},\overline{w})}$ can be decomposed as in Prop. 2.1. Recall that the trajectory reads where $F_{t} = {e_{t + 1} \otimes I_{p}}$, $G_{t} = {e_{t + 1} \otimes I_{q}}$ and $e_{t}$ is the $t$^th^ canonical vector in ${\mathbb{R}}^{\tau}$, such that ${F_{t}^{\top}\overline{u}} = u_{t}$ and ${G_{t}^{\top}\overline{w}} = w_{t}$. We have then Finally denoting for clarity $\overset{\sim}{x} = {\overset{\sim}{x}{(\overline{u},\overline{w})}}$ and $\phi_{t} = {\phi_{t}{({\overset{\sim}{x}}_{t},u_{t},w_{t})}}$, Denote $a = {{\nabla_{\overline{u}}\overset{\sim}{x}}{(\overline{u},0)}^{\top}\overline{v}}$, $b = {{\nabla_{\overline{w}}\overset{\sim}{x}}{(\overline{u},0)}^{\top}\overline{w}}$ and $c = {{\nabla_{\overline{u}\overline{w}}^{2}\overset{\sim}{x}}{(\overline{u},0)}{\lbrack\overline{v},\overline{w}, \cdot \rbrack}}$, with ${a,b,c} \in {\mathbb{R}}^{\taud}$. Those can be decomposed as, e.g., $a = {(a_{1};\ldots;a_{\tau})}$ with $a_{t} = {{\nabla_{\overline{u}}{\overset{\sim}{x}}_{t}}{(\overline{u},0)}^{\top}\overline{v}}$ and we denote similarly $b_{t} = {{\nabla_{\overline{w}}{\overset{\sim}{x}}_{t}}{(\overline{u},0)}^{\top}\overline{w}}$, $c_{t} = {{\nabla_{\overline{u}\overline{w}}^{2}{\overset{\sim}{x}}_{t}}{(\overline{u},0)}{\lbrack\overline{v},\overline{w}, \cdot \rbrack}}$ the decomposition of $b$ and $c$ in $\tau$ slices. Assuming $\nabla_{xx}^{2}\phi_{t}$ $\nabla_{xw}^{2}\phi_{t}$ and $\nabla_{ux}^{2}\phi_{t}$ to be zero, we get as in Prop. 2.1, where $\Phi_{t,x} = {{\nabla_{x}\phi_{t}}{(x_{t},u_{t},0)}}$, $\Phi_{t,u} = {{\nabla_{u}\phi_{t}}{(x_{t},u_{t},0)}}$, $\Phi_{t,w} = {{\nabla_{w}\phi_{t}}{(x_{t},u_{t},0)}}$, $\phi_{t,u,w} = {{\nabla_{uw}^{2}\phi_{t}}{(x_{t},u_{t},0)}}$ and $x_{t} = {{\overset{\sim}{x}}_{t}{(\overline{u},0)}}$. Therefore the variable $y = {a + b + c} = {{{\nabla_{\overline{u}}\overset{\sim}{x}}{(\overline{u},0)}^{\top}\overline{v}} + {{\nabla_{\overline{w}}\overset{\sim}{x}}{(\overline{u},0)}^{\top}\overline{w}} + {{\nabla_{\overline{u}\overline{w}}^{2}\overset{\sim}{x}}{(\overline{u},0)}{\lbrack\overline{v},\overline{w}, \cdot \rbrack}}}$ decomposed as $y = {(y_{1};\ldots;y_{\tau})}$ satisfies Plugging this in the model-minimization step gives the result. ∎ The linear control problem can again be solved by dynamic programming by modifying the Bellman equation in the backward pass, i.e., by solving analytically for white noise $w_{t}$, The complete resolution for quadratics is provided in Appendix C.

### Dealing with constraints

For constrained control problems with exact dynamics, the model-minimization steps will amount to linear control problems under constraints, which cannot be solved directly by dynamic programming. However their resolution by an interior point method boils down to solving linear quadratic control problems each of which has a low computational cost as shown before.

Formally, the resulting subproblems we are interested in are linear quadratic control problems under constraints of the form where $\mathcal{U}_{t} = {\{ u:{{C_{t}u} \leq d_{t}}\}}$, $q_{h_{t}}$ are convex quadratics, $q_{g_{t}}$ are strongly convex quadratics and $\ell_{t}$ are linear dynamics. Interior point methods introduce a log-barrier function ${\mathcal{B}_{t}{(u)}} = {\log{({d_{t} - {C_{t}u}})}}$ and minimize where $\mu_{k}$ increases along the iterates $k$ of the interior point method. We leave the exploration of constrained problems to future work.

## Automatic-differentiation oracle

The iterative composition structure we studied so far appears not only in control but more generally in optimization problems that involve successive transformations of a given input as for example in The identification of such structures led to the development of efficient *automatic-differentiation* software libraries able to compute gradients in any graph of computations both in CPUs and GPUs. We present then implementations and complexities of the optimization methods presented before where automatic-differentiation is the computational bottleneck.

### Functions and problem definition

We first recall the definition of decomposable functions along the trajectories.

### Definition 3.1

A function $f:{{\mathbb{R}}^{\taud}\rightarrow{\mathbb{R}}^{\taud'}}$ is a *multivariate $\tau$-decomposable function* if it is composed of $\tau$ functions $f_{t}:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d'}}$ such that for $\overline{x} = {(x_{1};\ldots;x_{\tau})} \in {\mathbb{R}}^{\taud}$, we have ${f{(\overline{x})}} = {({f_{1}{(x_{1})}};\ldots;{f_{\tau}{(x_{\tau})}})} \in {\mathbb{R}}^{\taud'}$.

A function $f:{{\mathbb{R}}^{\taud}\rightarrow{\mathbb{R}}}$ is a *real $\tau$-decomposable function* if it is composed of $\tau$ functions $f_{t}:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ such that for $\overline{x} = {(x_{1};\ldots;x_{\tau})} \in {\mathbb{R}}^{\taud}$, we have ${f{(\overline{x})}} = {\sum_{t = 1}^{\tau}{f_{t}{(x_{t})}}}$.

We denote by $\mathcal{D}^{\tau}{({\mathbb{R}}^{\taud},{\mathbb{R}}^{\taud'})}$ and $\mathcal{D}^{\tau}{({\mathbb{R}}^{\taud})}$ the sets of multivariate and real, respectively, $\tau$-decomposable functions whose components $f_{t}$ are differentiable.

For a given decomposable function $f \in {\mathcal{D}^{\tau}{({\mathbb{R}}^{\taud},{\mathbb{R}}^{\taud'})}}$ and a point $\overline{z} \in {\mathbb{R}}^{\taud'}$, the gradient-vector product reads ${{\nabla f}{(\overline{x})}\overline{z}} = {({{\nabla f_{1}}{(x_{1})}z_{1}};\ldots;{{\nabla f_{\tau}}{(x_{\tau})}z_{\tau}})} \in {\mathbb{R}}^{\taud}$, i.e., it can be computed directly from the components defining $f$. Similarly, the convex conjugate of a real decomposable function $f \in {\mathcal{D}^{\tau}{({\mathbb{R}}^{\taud})}}$ is directly given by the convex conjugate of its components.

We formalize now the class of trajectory functions.

### Definition 3.2 (Trajectory function)

A function $\overset{\sim}{x}:{{\mathbb{R}}^{\taup}\rightarrow{\mathbb{R}}^{\taud}}$ is a *trajectory function of horizon $\tau$* if it is defined by an input ${\hat{x}}_{0} \in {\mathbb{R}}^{d}$ and $\tau$ compositions of functions $\phi_{t}:{{{\mathbb{R}}^{d} \times {\mathbb{R}}^{p}}\rightarrow{\mathbb{R}}^{d}}$ such that for $\overline{u} = {(u_{0};\ldots;u_{\tau - 1})} \in {\mathbb{R}}^{\taup}$, we have ${\overset{\sim}{x}{(\overline{u})}} = {({{\overset{\sim}{x}}_{1}{(\overline{u})}};\ldots;{{\overset{\sim}{x}}_{\tau}{(\overline{u})}})}$ defined by We denote by $\mathcal{T}^{\tau}{({\mathbb{R}}^{\taup},{\mathbb{R}}^{\taud})}$ the set of trajectory functions of horizon $\tau$ whose dynamics $\phi_{t}$ are differentiable.

As presented in Section 2, the gradient back-propagation is divided in two main phases: (i) the forward pass that computes and store the gradients of the dynamics along the trajectory given by a command, (ii) the backward and roll-out passes that compute the gradient of the objective given the gradients of the costs and penalties along the trajectory. We can decouple the two phases by computing and storing once and for all the gradients of the dynamics along the trajectory, then making calls to the backward and roll-out passes for any dual inputs, i.e., not restricting ourselves to the gradients of the costs and penalties along the trajectories.

Formally, given $\overset{\sim}{x} \in {\mathcal{T}^{\tau}{({\mathbb{R}}^{\taup},{\mathbb{R}}^{\taud})}}$ and $\overline{u} \in {\mathbb{R}}^{\taup}$, we use that, once $\overset{\sim}{x}{(\overline{u})}$ is computed and the successive gradients are stored, any gradient vector product of the form ${\nabla\overset{\sim}{x}}{(\overline{u})}\overline{z}$ for $\overline{z} \in {\mathbb{R}}^{\taud}$ can be computed in linear time with respect to $\tau$ by a dynamic programming procedure (specifically an automatic-differentiation software) that solves ${\min_{\overline{v} \in {\mathbb{R}}^{\taup}} - {{\overline{z}}^{\top}{\nabla\overset{\sim}{x}}{(\overline{u})}^{\top}\overline{v}}} + {\frac{1}{2}{\|\overline{v}\|}_{2}^{2}}$. The main difference with classical optimization oracles is that *we do not compute or store the gradient ${{\nabla\overset{\sim}{x}}{(\overline{u})}} \in {\mathbb{R}}^{{{\taup} \times \tau}d}$ but yet have access to gradient-vector products $\overline{z}\rightarrow{{\nabla\overset{\sim}{x}}{(\overline{u})}\overline{z}}$*. This lead us to define oracles for trajectory functions as calls to an automatic-differentiation procedure as follows.

### Definition 3.3 (Automatic-differentiation oracle)

An *automatic-differentiation oracle* is any procedure that, given $\overset{\sim}{x} \in {\mathcal{T}^{\tau}{({\mathbb{R}}^{\taup},{\mathbb{R}}^{\taud})}}$ and $\overline{u} \in {\mathbb{R}}^{\taup}$, computes Derivatives of the gradient vector product can then be computed themselves by back-propagation as recalled in the following lemma.

### Lemma 3.4

Given a trajectory function $\overset{\sim}{x} \in {\mathcal{T}^{\tau}{({\mathbb{R}}^{\taup},{\mathbb{R}}^{\taud})}}$, a command $\overline{u} \in {\mathbb{R}}^{\taup}$ and a real decomposable function $f \in {\mathcal{D}^{\tau}{({\mathbb{R}}^{\taup})}}$, the derivative of $\overline{z}\rightarrow{f{({{\nabla\overset{\sim}{x}}{(\overline{u})}\overline{z}})}}$ requires two calls to an automatic-differentiation procedure.

### Proof

We describe the backward pass of Prop. 2.3 as a function of $\overline{z}$, the computations are the same except that $\overline{a}$ is replaced by $- \overline{z}$. Given $\overline{z} = {(z_{1};\ldots;z_{\tau})} \in {\mathbb{R}}^{\taud}$, the backward pass that computes ${\nabla\overset{\sim}{x}}{(\overline{u})}\overline{z}$ defines a linear trajectory function $\overset{\sim}{\lambda}:{\overline{z}\rightarrow{({{\overset{\sim}{\lambda}}_{1}{(\overline{z})}};\ldots;{{\overset{\sim}{\lambda}}_{\tau}{(\overline{z})}})} \in {\mathbb{R}}^{\taud}}$ and a linear decomposable function $\overset{\sim}{\theta}:{\overline{\lambda}\rightarrow{\overset{\sim}{\theta}{(\overline{\lambda})}} = {({{\overset{\sim}{\theta}}_{0}{(\lambda_{1})}};{\ldots{\overset{\sim}{\theta}}_{\tau - 1}{(\lambda_{\tau})}})} \in {\mathbb{R}}^{\taup}}$ as where $\Phi_{t,x} = {{\nabla_{x}\phi_{t}}{(x_{t},u_{t})}}$, $\Phi_{t,u} = {{\nabla_{u}\phi_{t}}{(x_{t},u_{t})}}$ and $x_{t} = {{\overset{\sim}{x}}_{t}{(\overline{u})}}$. The function we are interested in reads then ${f{({{\nabla\overset{\sim}{x}}{(\overline{u})}\overline{z}})}} = {f{({\overset{\sim}{\theta}{({\overset{\sim}{\lambda}{(\overline{z})}})}})}}$. Its derivative amounts then to compute the linear trajectory function $\overset{\sim}{\lambda}{(\overline{z})}$ by one call to an automatic differentiation procedure, then to back-propagate through this linear trajectory function by another call to an automatic-differentiation procedure. The derivatives of the decomposable functions can be directly computed from their individual components. ∎ We focus on problems that involve only a final state cost as in or in the experiments presented in Section 5. Formally those problems read where $\overset{\sim}{x}$ is trajectory function of horizon $\tau$, $h$ is a cost function and $g$ is a real $\tau$-decomposable penalty. Denote by $P{(\overset{\sim}{x},h,g)}$, the problem for a given choice of $\overset{\sim}{x},h,g$. We present complexities of the oracles defined before for classes of problems ${\mathcal{P}{(\mathcal{T},\mathcal{H},\mathcal{G})}} = {\{{P{(\overset{\sim}{x},h,g)}}:{{\overset{\sim}{x} \in \mathcal{T}},{{h \in \mathcal{H}},{g \in \mathcal{G}}}}\}}$ defined by a class of trajectory functions $\mathcal{T} \subset {\mathcal{T}^{\tau}{({\mathbb{R}}^{\taup},{\mathbb{R}}^{\taud})}}$, a class of state cost $\mathcal{H} \subset {\mathcal{F}{({\mathbb{R}}^{d})}} = {\{ f:{{\mathbb{R}}^{d}\rightarrow{{\mathbb{R}},{f\text{differentiable}}}}\}}$ and a class of decomposable penalty function $\mathcal{G} \subset {\mathcal{D}^{\tau}{({\mathbb{R}}^{\taud})}}$. Inclusions of classes of functions define inclusions of the problems. The class of problems for which we can provide iteration complexity is defined by $\mathcal{T} = {\mathcal{T}_{\alpha}^{\tau}{({\mathbb{R}}^{\taup},{\mathbb{R}}^{\taud})}}$ the class of trajectory functions of horizon $\tau$ with $\alpha$-continuously differentiable dynamics, $\mathcal{H} = {\mathcal{Q}_{L}{({\mathbb{R}}^{d})}}$ the class of quadratic convex functions $L$-smooth, $\mathcal{G} = {\mathcal{Q}_{L}^{\tau}{({\mathbb{R}}^{\taup})}} = {{\mathcal{Q}_{L}{({\mathbb{R}}^{\taup})}} \cap {\mathcal{D}^{\tau}{({\mathbb{R}}^{\taup})}}}$ the class of quadratic $\tau$-decomposable functions $L$-smooth.

Note that any $\overset{\sim}{x} \in {\mathcal{T}_{\alpha}^{\tau}{({\mathbb{R}}^{\taup},{\mathbb{R}}^{\taud})}}$ is $\alpha$-continuously differentiable. In the rest of this section we provide the oracle complexity of oracles for this problem general classes of problems detailed each time.

### Model-minimization steps with automatic-differentiation oracles

Now we precise the feasibility and the complexity of the inner-steps of the steps defined in Section 2 in terms of the class of problems and the automatic-differentiation oracle defined above. The total complexity of the algorithms, when available, are presented in Section 4.

### Gradient step

For any problem belonging to $\mathcal{P}{({\mathcal{T}^{\tau}{({\mathbb{R}}^{\taup},{\mathbb{R}}^{\taud})}},{\mathcal{F}{({\mathbb{R}}^{d})}},{\mathcal{D}^{\tau}{({\mathbb{R}}^{\taup})}})}$, a gradient step amounts to compute ${\nabla{\overset{\sim}{x}}_{\tau}}{(\overline{u})}{\nabla h}{({{\overset{\sim}{x}}_{\tau}{(\overline{u})}})}$ and ${\nabla g}{(\overline{u})}$ by a single call to an automatic-differentiation oracle.

### Regularized Gauss-Newton step

In the setting, the regularized Gauss-Newton step amounts to solve For smooth objectives $h$ and $g$, this is a smooth strongly convex problem that can be solved approximately by a linearly convergent first order method, leading to the inexact regularized Gauss-Newton procedures described. The overall cost of an approximated regularized Gauss-Newton step is then given by the following proposition. We define (i) $\mathcal{T}_{\alpha,L_{0},\ldots,L_{\alpha}}^{\tau}{({\mathbb{R}}^{\taup},{\mathbb{R}}^{\taud})}$ the class of trajectory functions of horizon $\tau$ whose dynamics $\phi_{t}$ are $L_{\beta}$-Lipschitz-continuous for all $\beta \leq \alpha$, (ii) $\mathcal{C}_{\alpha,\beta,L_{\beta}}{({\mathbb{R}}^{d})}$ the class of convex functions $\alpha$-differentiable whose $\beta$-derivative, for $\beta \leq \alpha$, is $L_{\beta}$-Lipschitz continuous and (iii) ${\mathcal{C}_{\alpha,\beta,L_{\beta}}^{\tau}{({\mathbb{R}}^{\taup})}} = {{\mathcal{C}_{\alpha,\beta,L_{\beta}}{({\mathbb{R}}^{\taup})}} \cap {\mathcal{D}^{\tau}{({\mathbb{R}}^{\taup})}}}$ the class of $\tau$-decomposable convex functions with corresponding smoothness properties. Note that any $\overset{\sim}{x} \in {\mathcal{T}_{\alpha,L_{0},\ldots,L_{\alpha}}^{\tau}{({\mathbb{R}}^{\taup},{\mathbb{R}}^{\taud})}}$ has a Lipschitz continuous $\beta$-derivative for $\beta \leq \alpha$.

### Proposition 3.5

For problems belonging to $\mathcal{P}{({\mathcal{T}_{1,L_{0},L_{1}}{({\mathbb{R}}^{\taup},{\mathbb{R}}^{\taud})}},{\mathcal{C}_{1,1,L_{1}^{h}}{({\mathbb{R}}^{d})}},{\mathcal{C}_{1,1,L_{1}^{g}}^{\tau}{({\mathbb{R}}^{\taup})}})}$ defined, an approximate regularized Gauss-Newton step given by is solved up to $\varepsilon$ accuracy by a fast gradient method with at most calls to an automatic differentiation oracle, where $M_{0}$ is the Lipschitz-continuity of ${\overset{\sim}{x}}_{\tau}$.

### Proof

For problems $\mathcal{P}{({\mathcal{T}_{1,L_{0},L_{1}}{({\mathbb{R}}^{\taup},{\mathbb{R}}^{\taud})}},{\mathcal{C}_{1,1,L_{1}^{h}}{({\mathbb{R}}^{d})}},{\mathcal{C}_{1,1,L_{1}^{g}}^{\tau}{({\mathbb{R}}^{\taup})}})}$, the regularized Gauss-Newton subproblem is ${L_{1}^{h}M_{0}^{2}} + L_{1}^{g} + \gamma^{- 1}$ smooth and $\gamma^{- 1}$ strongly convex. Therefore to achieve $\varepsilon$ accuracy, a fast gradient method requires at most $\mathcal{O}{({\sqrt{{({{L_{1}^{h}M_{0}^{2}} + L_{1}^{g} + \gamma^{- 1}})}/\gamma^{- 1}}{\log{(\varepsilon)}}})}$ calls to first order oracles of $\overline{v}\rightarrow{{h{({{{\overset{\sim}{x}}_{\tau}{(\overline{u})}} + {{\nabla{\overset{\sim}{x}}_{\tau}}{(\overline{u})}^{\top}\overline{v}}})}} + {g{({\overline{u} + \overline{v}})}} + {\frac{1}{2\gamma}{\|\overline{v}\|}_{2}^{2}}}$. Each call requires to compute ${\nabla{\overset{\sim}{x}}_{\tau}}{(\overline{u})}^{\top}\overline{v}$, that is the derivative of $z\rightarrow{v^{\top}{\nabla{\overset{\sim}{x}}_{\tau}}{(\overline{u})}z}$ for $z \in {\mathbb{R}}^{d}$, which costs two calls to an automatic differentiation procedure according to Lem. 3.4. An additional call to an automatic differentiation oracle is then needed to compute ${\nabla{\overset{\sim}{x}}_{\tau}}{(\overline{u})}{\nabla h}{({{{\overset{\sim}{x}}_{\tau}{(\overline{u})}} + {{\nabla{\overset{\sim}{x}}_{\tau}}{(\overline{u})}^{\top}\overline{v}}})}$. ∎

### Levenberg-Marquardt step

In the setting, the Levenberg-Marquardt step amounts to solve where $q_{h}$ and $q_{g}$ are quadratic approximations of $h$ and $g$ respectively, both being assumed to be twice differentiable. Here, duality offers a fast resolution of the step as shown in the following proposition. It shows that its cost is only ${2d} + 1$ times more than one of a gradient step. Recall also that for $h$, $g$ quadratics the Levenberg-Marquardt step amounts to a regularized Gauss-Newton step. We define (i) $\mathcal{C}_{\alpha}{({\mathbb{R}}^{d})}$ the class of convex functions $\alpha$-continuously differentiable and (ii) ${\mathcal{C}_{\alpha}^{\tau}{({\mathbb{R}}^{\taup})}} = {{\mathcal{C}_{\alpha}{({\mathbb{R}}^{\taup})}} \cap {\mathcal{D}^{\tau}{({\mathbb{R}}^{\taup})}}}$ the class of $\tau$-decomposable convex functions with corresponding differentiation properties.

### Proposition 3.6

For problems belonging to $\mathcal{P}{({\mathcal{T}^{\tau}{({\mathbb{R}}^{\taup},{\mathbb{R}}^{\taud})}},{\mathcal{C}_{2}{({\mathbb{R}}^{d})}},{\mathcal{C}_{2}^{\tau}{({\mathbb{R}}^{\taup})}})}$ defined , a Levenberg-Marquardt step is solved exactly with at most ${2d} + 1$ calls to an automatic differentiation oracle.

### Proof

The dual problem of the Levenberg-Marquardt step reads where ${r{(x)}} = {q_{h}\left({{{\overset{\sim}{x}}_{\tau}{(\overline{u})}} + x};{{\overset{\sim}{x}}_{\tau}{(\overline{u})}} \right)}$, ${s{(\overline{v})}} = {{q_{g}{({\overline{u} + \overline{v}};\overline{u})}} + {\frac{1}{2\gamma}{\|\overline{v}\|}_{2}^{2}}}$ and $r^{\ast},s^{\ast}$ are their respective conjugate functions that can be computed in closed form. Note that, as $s$ is $\tau$ decomposable, so is $s^{\ast}$. The dual problem can then be solved in $d$ iterations of a conjugate gradient method, each iteration requires to compute the gradient of $s^{\ast}{({- {{\nabla{\overset{\sim}{x}}_{\tau}}{(\overline{u})}z}})}$. According to Lem. 3.4 this amounts to two calls to an automatic differentiation oracle. A primal solution is then given by ${\overline{v}}^{\ast} = {{\nabla s^{\ast}}{({- {{\nabla{\overset{\sim}{x}}_{\tau}}{(\overline{u})}z^{\ast}}})}}$ which is given by an additional call to an automatic differentiation oracle. ∎

## Composite optimization

Before analyzing the methods of choice for composite optimization, we review classical algorithms for nonlinear control and highlight improvements for better convergence behavior. All algorithms are completely detailed in Appendix C.

### Optimal control methods

### Differential Dynamic Programming

Differential Dynamic Programming (DDP) is presented as a dynamic programming procedure applied to a second order approximation of the Bellman equation. Formally at a given command $\overline{u}$ with associated trajectory $\overline{x} = {\overset{\sim}{x}{(\overline{u})}}$, it consists in approximating the cost-to-go functions as where for a function $f{(y)}$, $q_{f}{(y;x)}$ denotes its second order approximation around $x$. The roll-out pass is then performed on the true trajectory as normally done in a dynamic programming procedure. We present an interpretation of DDP as an optimization on the state variables in Appendix D.

### ILQR, ILQG

DDP was superseded by the Iterative Linearized Quadratic Regulator (ILQR) method, presented in Section 1. In the case of noisy dynamics, the Linear Quadratic Regulator problem was replaced by a Linear Quadratic Gaussian problem where the objectives are averaged with respect to the noise, the iterative procedure was then called ILQG as presented .

Prop. 2.1 clarifies that these procedures, as defined, amount to compute to perform a line-search along its direction such that ${f{({\overline{u} + {\alpha{\overline{v}}^{\ast}}})}} \leq {f{(\overline{u})}}$. For ILQR the model $q_{f}$ is defined as, while for ILQG this corresponds to the model defined in with quadratic models $q_{f}$ and $q_{g}$. Compared to a Levenberg-Marquardt step, that reads we see that those procedures do not take into account the inaccuracy of the model far from the current point. Although a line-search can help ensuring convergence, no rate of convergence is known. For quadratics $h_{t},g_{t}$, the Levenberg-Marquardt steps become regularized Gauss-Newton steps whose analysis shows the benefits of the regularization term in (35. ‣ 4.1 Optimal control methods ‣ 4 Composite optimization ‣ Iterative Linearized Control: Stable Algorithms and Complexity Guarantees")) to ensure convergence to a stationary point.

### ILQG

The term ILQG has often been used to refer to an algorithm combining ideas from DDP and ILQR resp.. The general structure proposed then is akin to DDP in the sense that it uses a dynamic programming approach where the cost-to-go functions are approximated. However, as in ILQR, only the first order derivatives of the dynamics are taken into account to approximate the cost-to-go functions. Formally, at a given command $\overline{u}$ with associated trajectory $\overline{x} = {\overset{\sim}{x}{(\overline{u})}}$, ILQG consists in approximating the cost-to-go functions as While the cost-to-go functions are the same as, the roll-out pass is then performed on the true trajectory and not the linearized one. The analysis is therefore similar to the one of DDP. We leave it for future work and focus on the original definition of ILQR given.

### Regularized ILQR via regularized Gauss-Newton

We present convergence guarantees of the regularized Gauss-Newton method for composite optimization problems of the form where $h:{{\mathbb{R}}^{\taud}\rightarrow{\mathbb{R}}}$ and $g:{{\mathbb{R}}^{\taup}\rightarrow{\mathbb{R}}}$ are convex quadratic, and $\overset{\sim}{x}:{{\mathbb{R}}^{\taup}\rightarrow{\mathbb{R}}^{\taud}}$ is differentiable with continuous gradients. The regularized Gauss-Newton method then naturally leads to a regularized ILQR. In the following, we denote by $L_{h}$ and $L_{g}$ the smoothness constants of respectively $h$ and $g$ and by $\ell_{\overset{\sim}{x},S}$ the Lipschitz constant of $\overset{\sim}{x}$ on the initial sub-level set $S = {\{\overline{u}:{{f{(\overline{u})}} \leq {f{({\overline{u}}_{0})}}}\}}$.

The regularized Gauss-Newton method consists in iterating, starting from a given ${\overline{u}}_{0}$, We use ${\overline{u}}_{k + 1} = {\text{GN}{(u_{k};\gamma_{k})}}$ to denote hereafter. The convergence is stated in terms of the difference of iterates that, in this case, can directly be linked to the norm of the gradient, denoting $H = {{\nabla^{2}h}{(\overline{x})}}$ and $G = {{\nabla^{2}g}{(\overline{u})}}$, The convergence to a stationary point is guaranteed as long as we are able to get a sufficient decrease condition when minimizing this model as stated in the following proposition.

### Proposition 4.1

Consider a composite objective $f$ as in with convex models $c_{f}{(\cdot;\overline{u})}$ defined. Assume that the step sizes $\gamma_{k}$ of the regularized Gauss-Newton method are chosen such that and $\gamma_{\min} \leq \gamma_{k} \leq \gamma_{\max}$.

Then the objective value decreases over the iterations and the sequence of iterates satisfies where $L = {{\max_{\gamma \in {\lbrack\gamma_{\min},\gamma_{\max}\rbrack}}\gamma}{({{\ell_{\overset{\sim}{x},S}^{2}L_{h}} + L_{g} + \gamma^{- 1}})}^{2}}$ and $f^{\ast} = {\lim_{k\rightarrow{+ \infty}}{f{({\overline{u}}_{k})}}}$.

To ensure the sufficient decrease condition, one needs the model to approximate the objective up to a quadratic error which is ensured on any compact set as stated in the following proposition.

### Lemma 4.2

Consider a composite objective $f$ as in with convex models $c_{f}{(\cdot;\overline{u})}$ defined. For any compact set $C \subset {\mathbb{R}}^{\taup}$ there exists $M_{C} > 0$ such that for any ${\overline{u},\overline{v}} \in C$, Finally one needs to ensure that the iterates stay in a bounded set which is the case for sufficiently small step-sizes such that the sufficient decrease condition is satisfied along the sequence of iterates generated by the algorithm.

### Lemma 4.3

Consider a composite objective $f$ as. For any $k$ such that ${\overline{u}}_{k} \in S$, where $S = {\{\overline{u}:{{f{(\overline{u})}} \leq {f{({\overline{u}}_{0})}}}\}}$ is the initial sub-level set, any step-size ensures that the sufficient decrease condition is satisfied, where $\ell_{f,S}$ is the Lipschitz constant of $f$ on $S$, $C = {S + B_{1}}$ with $B_{1}$ the unit Euclidean ball centered at 0 and $M_{C}$ ensures.

Combining Prop. 4.1 and Lem. 4.2, we can guarantee that the iterates stay in the initial sub-level set and satisfy the sufficient decrease condition for sufficiently small step-sizes $\gamma_{k}$. At each iteration the step-size can be found by a line-search guaranteeing sufficient decrease; see Appendix E for details. The final complexity of the algorithm with line-search then follows.

### Corollary 4.4

For a composite objective $f$ as, the regularized Gauss-Newton method with a decreasing line-search starting from $\gamma_{0} \geq \hat{\gamma}$ with decreasing factor $\rho$ finds an $\varepsilon$-stationary point after at most calls to the regularized Gauss-Newton oracle, with $\hat{\gamma}$ defined, $f^{\ast} = {\lim_{k\rightarrow{+ \infty}}{f{({\overline{u}}_{k})}}}$ and Global convergence guarantee Number of calls to auto-differentiation oracle Cost per call to auto-differentiation oracle Table 1: Convergence properties and oracle costs of Gradient Descent (GD), ILQR, and regularized ILQR (RegILQR) for problem with quadratic h, g. The automatic-differentiation oracle cost is stated for problems of the form.

### Accelerated ILQR via accelerated Gauss-Newton

In Algo. 1 we present an accelerated variant of the regularized Gauss-Newton algorithm that blends a regularized Gauss-Newton step and an extrapolated step to potentially capture convexity in the objective. See Appendix F for the proof.

### Proposition 4.5

Consider Algo. 1 applied to a composite objective $f$ as in with decreasing step-sizes ${(\gamma_{k})}_{k \geq 0}$ and ${(\delta_{k})}_{k \geq 0}$. Then Algo. 1 satisfies the convergence of the regularized Gauss-Newton method with line-search as presented in Cor. 4.4. Moreover, if the convex models $c_{f}{(\overline{v};\overline{u})}$ defined in lower bound the objective as for any ${\overline{u},\overline{v}} \in {\mathbb{R}}^{\taup}$, then after $N$ iterations of Algo. 1, where $\delta = {\min_{k \in {\{ 1,{\ldotsN}\}}}\delta_{k}}$, $f^{\ast} = {{\min_{\overline{u}}f}{(\overline{u})}}$ and ${\overline{u}}^{\ast} \in {{{\arg\min}_{\overline{u}}f}{(\overline{u})}}$.

1:Input: Composite objective f in with convex models cf as. Initial ${\overline{u}}_{0} \in {\mathbb{R}}^{\taup}$, desired accuracy ε. 2:Initialize: α1:= 1, ${\overline{z}}_{0}:={\overline{u}}_{0}$ 4:Compute regularized step 5:Get ${\overline{v}}_{k} = {\text{GN}{({\overline{u}}_{k - 1};\gamma_{k})}}$ by line-search on γk s.t.

$${{f{({\overline{v}}_{k})}} \leq {{c_{f}{({\overline{v}}_{k};{\overline{u}}_{k - 1})}} + {\frac{1}{2\gamma_{k}}{\|{{\overline{v}}_{k} - {\overline{u}}_{k - 1}}\|}_{2}^{2}}}}.$$ 6:Compute extrapolated step 7:- Set${{\overline{y}}_{k} = {{\alpha_{k}{\overline{z}}_{k - 1}} + {{({1 - \alpha_{k}})}{\overline{u}}_{k - 1}}}}.$ 8:- Get ${\overline{w}}_{k} = {\text{GN}{({\overline{y}}_{k};\delta_{k})}}$ by line-search on δk s.t.

$${{f{({\overline{w}}_{k})}} \leq {{c_{f}{({\overline{w}}_{k};{\overline{y}}_{k})}} + {\frac{1}{2\delta_{k}}{\|{{\overline{w}}_{k} - {\overline{y}}_{k}}\|}_{2}^{2}}}}.$$ 9:- Set ${{\overline{z}}_{k} = {{\overline{u}}_{k - 1} + {{({{\overline{w}}_{k} - {\overline{u}}_{k - 1}})}/\alpha_{k}}}}.$ 11:Pick best of two steps 12: Choose ${\overline{u}}_{k}$ such that $${f{({\overline{u}}_{k})}} \leq {\min{\{{f{({\overline{v}}_{k})}},{f{({\overline{w}}_{k})}}\}}}$$ 13:until ε-near stationarity $\left\| {{\nabla f}{({\overline{u}}_{k})}} \right\| < \varepsilon$ Algorithm 1 Accelerated Regularized Gauss-Newton

### Total complexity with automatic-differentiation oracles

Previous results allow us to state the total complexity of the regularized ILQR algorithm in terms of calls to automatic differentiation oracles as done in the following corollary that combines Cor. 4.4 and Prop. 4.5 with Prop. 3.6. A similar result can be obtained for the accelerated variant. Table 1 summarizes then convergence properties and computational costs of classical methods for discrete time non-linear control.

### Corollary 4.6

Consider problems $\mathcal{P}{({\mathcal{T}_{1}{({\mathbb{R}}^{\taup},{\mathbb{R}}^{\taud})}},{\mathcal{Q}_{L_{h}}{({\mathbb{R}}^{d})}},{\mathcal{Q}_{L_{g}}^{\tau}{({\mathbb{R}}^{\taup})}})}$ defined. The regularized Gauss-Newton method with a decreasing line-search starting from $\gamma_{0} \geq \hat{\gamma}$ with decreasing factor $\rho$ finds an $\varepsilon$-stationary point after at most calls to an automatic differentiation oracle, with $\hat{\gamma}$ defined, ${L = {{\max_{\gamma \in {\lbrack\hat{\gamma},\gamma_{0}\rbrack}}\gamma}{({{\ell_{\overset{\sim}{x},S}^{2}L_{h}} + L_{g} + \gamma^{- 1}})}^{2}}},$ $\ell_{\overset{\sim}{x},S}$ is the Lipschitz constant of $\overset{\sim}{x}$ on the initial sub-level set $S = {\{\overline{u}:{{f{(\overline{u})}} \leq {f{({\overline{u}}_{0})}}}\}}$ and $f^{\ast} = {\lim_{k\rightarrow{+ \infty}}{f{({\overline{u}}_{k})}}}$

## Experiments

We illustrate the performance of the algorithms considered in Sec. 4 including the proposed accelerated regularized Gauss-Newton algorithm on two classical problems drawn : swing-up a pendulum, and move a two-link robot arm.

### Control settings

The physical systems we consider below are described by continuous dynamics of the form where ${z{(t)}},{\overset{˙}{z}{(t)}},{\overset{¨}{z}{(t)}}$ denote respectively the position, the speed and the acceleration of the system and $u{(t)}$ is a force applied on the system. The state ${x{(t)}} = {({x_{1}{(t)}},{x_{2}{(t)}})}$ of the system is defined by the position ${x_{1}{(t)}} = {z{(t)}}$ and the speed ${x_{2}{(t)}} = {\overset{˙}{z}{(t)}}$ and the continuous cost is defined as where $T$ is the time of the movement and $h,g$ are given convex costs. The discretization of the dynamics with a time step $\delta$ starting from a given state ${\hat{x}}_{0} = {(z_{0},0)}$ reads then where $\tau = {\lceil{T/\delta}\rceil}$ and the discretized cost reads Figure 1: Control settings considered. From left to right: pendulum, two-link arm robot.

### Pendulum

We consider a simple pendulum illustrated in Fig. 1, where $m = 1$ denotes the mass of the bob, $l = 1$ denotes the length of the rod, $\theta$ describes the angle subtended by the vertical axis and the rod, and $\mu = 0.01$ is the friction coefficient. The dynamics are described by The goal is to make the pendulum swing up (i.e. make an angle of $\pi$ radians) and stop at a given time $T$. The cost writes as

### Two-link arm

We consider the arm model with two joints (shoulder and elbow), moving in the horizontal plane presented in and illustrated in 1. The dynamics are described by where $\theta = {(\theta_{1},\theta_{2})}$ is the joint angle vector, ${M{(\theta)}} \in {\mathbb{R}}^{2 \times 2}$ is a positive definite symmetric inertia matrix, ${C{(\theta,\overset{˙}{\theta})}} \in {\mathbb{R}}^{2}$ is a vector centripetal and Coriolis forces, $B \in {\mathbb{R}}^{2 \times 2}$ is the joint friction matrix, and ${u{(t)}} \in {\mathbb{R}}^{2}$ is the joint torque that we control. We drop the dependence on $t$ for readability. The dynamics are then The expressions of the different variables and parameters are given by where $b_{11} = b_{22} = 0.05$, $b_{12} = b_{21} = 0.025$, $l_{i}$ and $k_{i}$ are respectively the length (30cm, 33cm) and the moment of inertia (0.025kgm^2^, 0.045kgm^2^) of link $i$, $m_{2}$ and $d_{2}$ are respectively the mass (1kg) and the distance (16cm) from the joint center to the center of the mass for the second link.

The goal is to make the arm reach a feasible target $\theta^{\ast}$ and stop at that point. The objective reads

### Results

We use the automatic differentiation capabilities of PyTorch to implement the automatic differentiation oracles introduced in Sec. 3. The Gauss-Newton-type steps in Algo. 1 are computed by solving the dual problem associated as presented in Sec. 3.

In Figure 2, we compare the convergence, in terms of function value and gradient norm, of ILQR (based on Gauss-Newton), regularized ILQR (based on regularized Gauss-Newton), and accelerated regularized ILQR (based on accelerated regularized Gauss-Newton). These algorithms were presented in Sec. 4.

For ILQR, we use an Armijo line-search to compute the next step. For both the regularized ILQR and the accelerated regularized ILQR, we use a constant step-size sequence tuned after a burn-in phase of 5 iterations. We leave the exploration of more sophisticated line-search strategies for future work.

The plots show stable convergence of the regularized ILQR on these problems. The proposed accelerated regularized Gauss-Newton algorithm displays stable and fast convergence. Applications of accelerated regularized Gauss-Newton algorithms to reinforcement learning problems would be interesting to explore.

Figure 2: Convergence of ILQR, regularized ILQR and accelerated regularized ILQR on the inverted pendulum (top) and two-link arm (bottom) control problems for an horizon τ = 100.
