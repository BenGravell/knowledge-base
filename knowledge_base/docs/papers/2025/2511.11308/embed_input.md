<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Policy Optimization for Unknown Systems Using Differentiable Model Predictive Control

Topics include Model predictive control, Predictive control, Uncertainty, Real-time systems, Online algorithms, Optimization, Planning, Control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Model-based policy optimization often struggles with inaccurate system dynamics models, leading to suboptimal closed-loop performance. This challenge is especially evident in Model Predictive Control (MPC) policies, which rely on the model for real-time trajectory planning and optimization. We introduce a novel policy optimization framework for MPC-based policies combining differentiable optimization with zeroth-order optimization. Our method combines model-based and model-free gradient estimation approaches, achieving faster transient performance compared to fully data-driven approaches while maintaining convergence guarantees, even under model uncertainty. We demonstrate the effectiveness of the proposed approach on a nonlinear control task involving a 12-dimensional quadcopter model.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Policy optimization is the problem of designing a control policy that minimizes a prescribed performance objective. In reinforcement learning (RL), the problem is typically formulated as a search over a parameterized policy class \[sutton2002reinforcement\]. *Model-based* RL methods use a model of the dynamics to guide policy updates, improving sample efficiency \[atkeson1997comparison\].

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A growing line of work studies policy optimization problems where the policy is a model predictive controller (MPC) \[amos2018differentiable, gros2019data, agrawal2020learning, drgovna2022differentiable, zuliani2023bp, zuliani2024closed\]. MPC-based policies generate predictions of future state trajectories using a system model and naturally incorporate constraints into their decision-making process, offering stronger safety guarantees and greater interpretability compared to model-free approaches.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Existing MPC-based policy optimization schemes typically assume that the dynamics model is exact, and convergence results rely on this assumption \[zuliani2023bp\]; obtaining convergence guarantees when the model is inaccurate remains an open problem. In this paper, we propose a novel policy optimization algorithm with convergence guarantees inspired by \[he2024gray\] blending model-based gradient information with zeroth-order updates that is robust to inexact models. A key feature of our method is that it can smoothly trade off between model-based and zeroth-order components, putting more weight on the model whenever it is trusted and relying more on model-free information otherwise. To handle the nonsmoothness of MPC policies, we leverage the tools of \[bolte2021conservative\]. We valide our approach on a 12-dimensional nonlinear quadcopter.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Related work: Zeroth-order optimization addresses the problem of minimizing an objective function when first-order information is unavailable. The foundations of the approach used in this paper trace back to the seminal work of \[flaxman2004online\], which introduced a smoothing-based approximation technique enabling gradient-free optimization for possibly nonsmooth functions. Subsequent research extended these ideas to convex settings: see \[duchi2012randomized\] and \[nesterov2017random\] for one-point gradient estimators, or \[shamir2017optimal\] for a two-point estimator. More recently, \[lin2022gradient\] generalized the two-point approach to nonconvex problems, demonstrating its effectiveness beyond the convex regime. Closest to our work is \[he2024gray\], which combines a one-point zeroth-order estimator with model-based gradient information to improve convergence speed, a direction we further build upon in this paper.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notation: $\mathcal{X}^{n}$ denotes the $n$-fold Cartesian product of the set $\mathcal{X}$. Given a path-differentiable function $g$ of two arguments $x$ and $y$, $\mathcal{J}_{g,x}$ and $\mathcal{J}_{g,y}$ denote the projection of the conservative Jacobian $\mathcal{J}_{g}$ onto the $x$ and $y$ entries. $\mathbb{B}$ and $\mathbb{S}$ are the unit ball and sphere in the Euclidean norm. $U{({\mathbb{B}})}$ and $U{({\mathbb{S}})}$ denote uniform distributions over $\mathbb{B}$ and $\mathbb{S}$. $\mathcal{N}_{\mathcal{X}}$ is the tangent cone of the set $\mathcal{X}$ in the sense of Clarke.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

$\operatorname{dist}\limits_{p}{(a,B)}$ is the distance between point $a$ and set $B$ in the $p$-norm.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Conservative Jacobians", "weight": 1.0} -->

The notion of Conservative Jacobians, introduced in \[bolte2021conservative\], extends the concept of derivatives to locally Lipschitz, almost everywhere differentiable functions.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Stationary points in nonsmooth optimization", "weight": 1.0} -->

The *Clarke Jacobian* of a locally Lipschitz function $f:{{\mathbb{R}}^{\ltimes}\rightarrow{\mathbb{R}}}$ is the outer-semicontinuous map

<!-- chunk {"id": "body-0011", "role": "body", "section": "Stationary points in nonsmooth optimization", "weight": 1.0} -->

where $D_{f} \subset {\mathbb{R}}^{\ltimes}$ is the full-measure set on which $f$ is differentiable, and $\operatorname{co}$ denotes the convex hull. There is a close connection between Clarke and conservative Jacobians \[bolte2021conservative\]

<!-- chunk {"id": "body-0012", "role": "body", "section": "Stationary points in nonsmooth optimization", "weight": 1.0} -->

If $x$ is a local minimizer of $f$, then $0 \in {\partial_{c}{f{(x)}}}$ (and similarly $0 \in {{\operatorname{co}\mathcal{J}_{f}}{(x)}}$). Hence, in nonsmooth optimization, one typically searches for *Clarke stationary points*, that is, points $x$ with $0 \in {\partial_{c}{f{(x)}}}$. In our setting, however, identifying Clarke stationary points is infeasible due to the lack of exact knowledge of the true system dynamics. A weaker notion of stationarity is that of a *Goldstein $\delta$-critical point*, defined as any $x$ such that $0 \in {\partial_{\delta}{f{(x)}}}$, where

<!-- chunk {"id": "body-0013", "role": "body", "section": "Stationary points in nonsmooth optimization", "weight": 1.0} -->

is the Goldstein $\delta$-subdifferential of $f$. As shown in \[zhang2020complexity\], ${\lim_{\delta \downarrow 0}{\partial_{\delta}{f{(x)}}}} = {\partial_{c}{f{(x)}}}$, making Goldstein $\delta$-stationarity a meaningful optimality condition for nonsmooth problems.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Stationary points in nonsmooth optimization", "weight": 1.0} -->

For constrained problems, such as minimizing $f{(x)}$ subject to ${h{(x)}} = 0$, $x \in \mathcal{X}$, we consider a generalized stationarity concept adapted from \[grimmer2025goldstein\]. A point $x$ is said to satisfy the *Goldstein Fritz-John $\delta$-critical condition* if there exist multipliers ${\lambda_{0},\lambda_{1}} \geq 0$ such that

<!-- chunk {"id": "body-0015", "role": "body", "section": "Stationary points in nonsmooth optimization", "weight": 1.0} -->

This condition parallels the classical Fritz-John optimality conditions, with the gradients replaced by Goldstein $\delta$-subdifferentials. If $\lambda_{0} > 0$, the point is called a *Goldstein KKT $\delta$-critical point*.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

where $\theta \in \Theta$ is a tunable parameter that determines the behavior of the policy and $\Theta \subset {\mathbb{R}}^{\ltimes_{\theta}}$ is a parameter set. Despite not knowing the dynamics in (2a) exactly, we assume existence of a model $g:{{{\mathbb{R}}^{\ltimes_{\curvearrowleft}} \times {\mathbb{R}}^{\ltimes_{\approxeq}}}\rightarrow{\mathbb{R}}^{\ltimes_{\curvearrowleft}}}$ such that ${g{(x,u)}} \approx {f{(x,u)}}$ for all $x$ and $u$. We consider the constraints

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

where $\mathcal{X} \subseteq {\mathbb{R}}^{\ltimes_{\curvearrowleft}}$ and $\mathcal{U} \subseteq {\mathbb{R}}^{\ltimes_{\approxeq}}$ are known convex sets. The input $u_{t} = {\operatorname{MPC}{(x_{t},\theta)}}$ depends on the state $x_{t}$ (last constraint in (2b)) and the parameters $\theta$. It is computed by solving the problem

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

where $\ell_{\theta}$ and $\ell_{N,\theta}$ are parameterized cost functions, and applying $u_{t} = u_{0|t}$. Throughout, we assume that is a quadratic program (QP) meeting the conditions of Theorem A.2. ‣ Appendix A Differentiating Solutions of Optimization Problems ‣ Policy Optimization for Unknown Systems using Differentiable Model Predictive Control") in Appendix A. If $g$ is a nonlinear function, one can use the linearization techniques in \[zuliani2023bp, Section VI-A\] to obtain an MPC that can be expressed as a quadratic program.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Our emphasis is on QP-based MPC policies, which often deliver strong performance even on nonlinear control problems. Nonetheless, the framework can easily be extended to fully nonlinear policies using the differentiation methods in \[zuliani2025differentiable\]. Similarly, this method can accommodate nonconvex upper-level constraints in as long as the MPC satisfies Assumption 1. Note additionally that while in this work we restrict $\theta$ to parameters appearing in the cost of (2b), extending it to also affect the constraints or dynamics of the MPC is straightforward.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Out goal is to obtain an MPC design $\theta^{\ast}$ that minimizes a known objective function $C{(x,u)}$, where $x = {(x_{0},\ldots,x_{T})}$ and $u = {(u_{0},\ldots,u_{T - 1})}$, tipically with $T \gg N$, are the closed-loop trajectories obtained by combining (2a) and (2b), while satisfying for all $t$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Since $f$ is unknown, problem cannot be solved directly.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Solving the problem when dynamics are known", "weight": 1.0} -->

Even with perfect model knowledge, is difficult to solve due to the nonsmooth constraints imposed by the MPC function. In \[zuliani2023bp\] we introduced a gradient-based method specifically designed for such problems, which solves an unconstrained reformulation of. To cast as an unconstrained problem, let $x:{\Theta\rightarrow{\mathbb{R}}^{{\mathbb{T}}\ltimes_{\curvearrowleft}}}$ and $u:{\Theta\rightarrow{\mathbb{R}}^{{({{\mathbb{T}} - \nVdash})}\ltimes_{\approxeq}}}$ be the closed-loop trajectories obtained by combining (2b) and (2a) over the entire horizon $t \in {\mathbb{Z}}_{\lbrack\nvdash,{\mathbb{T}}\rbrack}$. Then becomes

<!-- chunk {"id": "body-0023", "role": "body", "section": "Imperfect Gradient Information using an Inexact Model", "weight": 1.0} -->

Since (2a) is unknown, the exact Jacobian $\mathcal{J}_{\mathcal{C}}$ cannot be computed, and the exact update cannot be applied directly. Instead, we approximate $\mathcal{J}_{\mathcal{C}}$ using the available model $g$ of the true dynamics $f$. First, we recursively build approximations $J_{x}{(\theta)}$ and $J_{u}{(\theta)}$ of $\mathcal{J}_{x}{(\theta)}$ and $\mathcal{J}_{u}{(\theta)}$ via

<!-- chunk {"id": "body-0024", "role": "body", "section": "Model-free Gradient Estimation", "weight": 1.0} -->

The update of Section 4.2 is appealing because it only relies on the approximate model. However, without further assumptions on the model accuracy, it is impossible to derive convergence guarantees. To address this issue, we construct gradient-like directions purely from data, for which convergence can be established under mild conditions.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Model-free Gradient Estimation", "weight": 1.0} -->

Working with $\mathcal{C}^{\delta}$ instead of $\mathcal{C}$ has two key benefits: (i) the Lipschitz continuity of $\mathcal{C}$ implies smoothness of $\mathcal{C}^{\delta}$, and (ii) one can estimate $\nabla\mathcal{C}^{\delta}$ solely using function evaluations. For this, we use the following one-point estimator

<!-- chunk {"id": "body-0026", "role": "body", "section": "Model-free Gradient Estimation", "weight": 1.0} -->

where $v_{k}$ is sampled i.i.d. from $U{({\mathbb{S}})}$ for each $k \in {\mathbb{N}}$. We have the following.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Proposed Algorithm", "weight": 1.0} -->

Our algorithm combines the model-based update of Section 4.2 with the model-free update of Section 5, following the *gray-box* scheme of \[he2024gray\]. At iteration $k$, we update $\theta^{k}$ as follows

<!-- chunk {"id": "body-0028", "role": "body", "section": "Proposed Algorithm", "weight": 1.0} -->

where ${\{\alpha_{k}\}}_{k \in {\mathbb{N}}} \subset {\mathbb{R}}_{> \nvdash}$ is a sequence of vanishing stepsizes, and ${\{\eta_{k}\}}_{k \in {\mathbb{N}}} \subset {\lbrack 0,1\rbrack}$ weights the relative contribution of the two update directions. Choosing $\eta_{k} \approx 1$ prioritizes the model-based direction $J_{\mathcal{C}}{(\theta_{k})}$, whereas $\eta_{k} \approx 0$ makes the update closer to zeroth order via $J_{\mathcal{C}^{\delta}}{(\theta_{k},v_{k})}$. Generally, selecting $\eta_{k}$ is a design choice that should reflect the trustworthiness of the model.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Proposed Algorithm", "weight": 1.0} -->

We showcase how the converge speed is affected by different choices of $\eta_{k}$ in simulation in Section 7.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Convergence to a Goldstein \\\\texorpdfstring$\\delta$delta-Critical Point", "weight": 1.0} -->

Our convergence analysis builds on Lemma 5.1 and standard results on stochastic projected gradient methods for nonsmooth, nonconvex objectives \[davis2020stochastic\]. We first impose regularity assumptions ensuring that the closed-loop map and the objective are locally Lipschitz and definable.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The true dynamics $f$, the model $g$, the cost function $C$, the penalty $P$, and the MPC function $\operatorname{MPC}:{{{\mathbb{R}}^{\ltimes_{\curvearrowleft}} \times \Theta}\rightarrow{\mathbb{R}}^{\ltimes_{\approxeq}}}$ are locally Lipschitz and definable in an o-minimal structure.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Under Assumption 1, the closed-loop trajectories $x{(\theta)}$ and $u{(\theta)}$ are locally Lipschitz and definable in $\theta$, allowing the definition of conservative Jacobians. Assumption 1 is not restrictive, as definable functions cover almost all functions of interest in control and optimization, and the MPC function satisfies Assumption 1 under the mild conditions laid out in Appendix A. To ensure feasibility of the MPC, one can resort to the technique in \[zuliani2023bp, Section VI-D\].

<!-- chunk {"id": "body-0033", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Our last technical requirement simplifies the analysis by ensuring boundedness of the gradients.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The set $\Theta$ is convex, compact and definable in an o-minimal structure.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

To ensure convergence, we require the following conditions on $\alpha_{k}$ and $\eta_{k}$

<!-- chunk {"id": "body-0036", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

These conditions hold, for example, if $\alpha_{k} = {1/{({k + 1})}^{\gamma}}$ and $\eta_{k} = {1/{({k + 1})}^{\beta - \gamma}}$, with $\gamma \in {(0.5,1\rbrack}$ and $\beta > 1$. This allows for a wide range of possible stepsizes and, crucially, for different decrease rates for $\eta_{k}$. This last feature, in particular, allows us to accomodate situations where the model $J_{\mathcal{C}}$ is deemed trustworthy, and thus $\eta_{k}$ should have larger values, but also situations where $J_{\mathcal{C}}$ is less trusted and the zeroth-order estimation is preferred. Observe that $\eta_{k} \downarrow 0$, meaning that eventually the information obtained using the model is discarded and the algorithm relies solely on data.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

We evaluate our approach on the 12-dimensional quadcopter model from \[abdulkareem2022modeling\] whose state vector comprises the position $(p_{x},p_{y},p_{z})$, velocity $(v_{x},v_{y},v_{z})$, Euler angles $(\phi,\vartheta,\psi)$, and angular velocity $(p,q,r)$ in the body frame.^11^1The code will be made available at The control inputs are the rotation speeds $\omega_{i}$ of the four rotors.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

To handle constraint violations, we relax the state constraints using slack variables, which are penalized using both a quadratic and a linear penalty (scaled by a factor of $25$). We model the system as linear choosing ${g{(x,u)}} = {{Ax} + {Bu}}$, where the matrices $A$ and $B$ are identified via least-squares regression on 100 closed-loop trajectories collected near the target point under a stabilizing MPC controller. In practice, if such a controller is not available, these trajectories could instead be generated by a human pilot. The upper-level cost is

<!-- chunk {"id": "body-0039", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

We choose $\delta = 10^{- 4}$, $\alpha_{k} = {{{5 \cdot 10^{- 5}}{\log k}} + {2/{({k + 1})}^{0.75}}}$ and $\eta_{k} = {1/{({k + 1})}^{\gamma}}$, with $\gamma \in {\{ 0.25,0.5,0.75\}}$, and train for $200$ iterations starting with $Q = \mathcal{Q}$, $R = \mathcal{R}$, and $P$ obtained by solving the DARE with the identified dynamics and cost given by $\mathcal{Q}$ and $\mathcal{R}$. To isolate the contribution of each optimization component, we additionally train using the same stepsizes and initial conditions with $\eta_{k} = 1$ and $\eta_{k} = 0$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

The behavior of the tracking cost and the constraint violation across iterations can be seen in Figure 1. The proposed approach demonstrates the most efficient convergence, whereas the purely model-based method exhibits rapid improvement during the initial iterations but later becomes unstable and fails to converge. The purely zeroth-order method, on the other hand, achieves consistent progress, but at a significantly slower rate. The proposed hybrid strategy benefits from fast initial transients, enabled by the model, and improved long-term convergence, supported by zeroth-order correction. Notably, smaller values of $\gamma$, corresponding to greater reliance on the model, lead to faster initial convergence, but also to more pronounced instability.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

To further assess policy quality, we compare the trajectory generated by the trained controller with that obtained from tuning using the exact nonlinear model. As shown in Figure 2, the two trajectories exhibit strong qualitative agreement across all states. Quantitatively, the trained controller achieves a final cost of $1111.71$, compared to $1103.04$ for the controller optimized with perfect model knowledge. This corresponds to less than $1\%$ suboptimality, indicating that the learned parameters are nearly optimal despite using an approximate model and noisy gradients.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

We introduced a policy optimization framework for MPC policies that combines model-based gradient information with zeroth-order achieving fast learning transients while guaranteeing convergence to a critical point even under imperfect models. This approach is well-suited to settings where accurate modeling is difficult, offering robustness without sacrificing efficiency. We demonstrated the effectiveness of our algorithm on a nonlinear quadcopter task, showing that it achieves near-optimal performance while outperforming purely model-based and model-free baselines. Future work will focus on strenghtening the safety guarantees of the approach.
