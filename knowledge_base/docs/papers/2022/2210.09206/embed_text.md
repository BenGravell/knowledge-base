## Introduction

Optimization-based control methods such as model predictive control (MPC) have been among the most versatile techniques in feedback control design for more than 40 years. Such techniques have been successfully applied to control of dynamic systems in a variety of domains such as autonomous vehicles, chemical plants, humanoid robots, and many others. Nonetheless, MPC's versatility comes at a cost. Having to solve optimization problems online makes it difficult to deploy MPC on high-dimensional systems that have strict latency requirements and limited computational or energy resources. To mitigate this issue, considerable effort went into developing faster, tailored optimization methods for MPC.

Instead of following these approaches, we pursue a data-driven methodology. We propose and study a scheme to collect data interactively from a dynamical system in feedback with an MPC controller and in order to learn an explicit controller that maps states to inputs. Such approaches are known in the reinforcement learning literature as imitation learning and they are well suited for MPC because one can query MPC for the next input at any desired state; all that is needed is to solve the corresponding optimization problem. Nonetheless, in order to learn controllers that are guaranteed to stabilize dynamical systems, to satisfy state and action constraints, and to obtain low cost, we would need to exploit several properties of MPC.

Our goal of obtaining an explicit map from states to inputs that encapsulates an MPC controller falls under the purview of explicit MPC, which aims to pre-compute and store the solutions of the optimization problems that might be encountered at runtime.

In general, explicit MPC aims to pre-compute an exact representation of the MPC controller while we aim to learn a controller that performs as well as MPC with high probability. In the same vain, Hertneck et al. and Karg and Lucia suggest learning a controller from data. However, their approaches collect all the trajectory data using MPC before any learning occurs and do not interact with the dynamics further. The lack of interaction in imitation learning is known to lead to sub-optimal performance because small learning errors would cause a controller produced by such a method to result in states with a different distribution than those produced by MPC during training. In other words, distribution shift leads to error compounding. Our proposed approach completely avoids this issue. To this end, our contributions in this paper can be summarized as follows:

We start by analyzing the imitation learning method known as the forward training algorithm (Forward) in the setting of control affine systems.

We modify Forward to make it suitable for MPC applications with constraints. Firstly, Forward learns a different controller for each distinct time step and hence it cannot be applied straightforwardly to problems with long or infinite horizons. Fortunately, after sufficiently many times steps, the MPC controller applied to time invariant linear systems becomes equivalent to the classical linear quadratic regulator (LQR). We exploit this property; we modify Forward to switch to LQR after a number of time steps estimated from data. Secondly, to improve the robustness of our method we require Forward to imitate robust MPC instead of standard MPC. We refer to our modified method as Forward-switch.

We theoretically guarantee that a controller learned with Forward-switch stabilizes linear systems and satisfies their constraints as long as certain amount of data is available. Moreover, we bound the cost suboptimality of the learned controller, showing that it approaches optimal performance as more data becomes available. None of the previous works on imitating MPC included such guarantees. We also provide theoretical sample complexity bounds using state of the art tools of high dimensional statistics and statistical learning theory.

We validate the efficacy of the modified forward training algorithm on simulated MPC problems, showing that it surpasses non-interactive approaches.

## The Forward Training Algorithm for Control

In this section, we present the imitation learning method Forward and bound the distance between the trajectories produced by the learned controller and those produced by the expert when the dynamics are control-affine. In subsequent sections, we specialize our analysis to the case where the expert is a MPC controller applied to constrained linear systems.

Imitation learning aims to learn from demonstrations a controller $\hat{\pi}$ that imitates the behavior of a target controller $\pi^{\star}$, called *expert policy* or simply *expert* in the reinforcement learning literature. Imitation learning is valuable when $\pi^{\star}$ lacks a closed-form expression or is expensive to query in general. For instance, $\pi^{\star}$ could be a human performing a task or a MPC controller. More formally, in imitation learning it is assumed that for a state $x$ we can access the input $\pi^{\star}{(x)}$. Then, the aim is to use data $\{ x_{i},{\pi^{\star}{(x_{i})}}\}$ to learn a controller $\hat{\pi}$ such that ${\hat{\pi}{(x)}} \approx {\pi^{\star}{(x)}}$.

In this section, we consider control-affine dynamical systems with constraints:

where $\mathcal{X} \subset {\mathbb{R}}^{d_{x}}$ is the state space and $\mathcal{U} \subset {\mathbb{R}}^{d_{u}}$ is the input space. We also find it useful to denote $\varphi_{t}{(x_{0},{\{ u_{t}\}}_{t \geqslant 0})}$ the state $x_{t}$ that evolves according to $x_{t + 1} = {{f{(x_{t})}} + {g{(x_{t})}u_{t}}}$ and starts at the initial state $x_{0}$. When the dynamics evolve according to a time-varying feedback controller $\pi = \pi_{0:{t - 1}}$ (i.e. $\pi_{0}$ is used at time $0$, $\pi_{1}$ at time $1$, etc.) we denote the state at time $t$ by $\varphi_{t}{(x_{0};\pi_{0:{t - 1}})}$. If the controller $\pi$ is time-invariant, we simply write $\varphi_{t}{(x_{0};\pi)}$.

Behavior cloning (BC) is the simplest imitation learning method. It consists of collecting $m$ independent trajectories $\varphi_{t}{(x_{0}^{(i)};\pi^{\star})}$ with initial states $x_{0}^{}$, $x_{0}^{}$,..., $x_{0}^{(m)}$ sampled randomly from an initial distribution $\mathcal{D}$. Then, BC produces a controller ${\hat{\pi}}_{\mathsf{B}\mathsf{C}}$ through empirical risk minimization (ERM):

where $\Pi$ is a class of models that map the state space to the input space and $\left. \parallel \cdot \parallel \right.$ is any norm (although it could be replaced by a more general loss function). All our results assume that $\pi^{\star} \in \Pi$.

### Distribution Shift

The states collected using the expert $\pi^{\star}$ have a particular distribution $\mathcal{D}^{\star}$. BC produces a controller ${\hat{\pi}}_{\mathsf{B}\mathsf{C}}$ that, when evaluated on samples from $\mathcal{D}^{\star}$, behaves similarly to the expert $\pi^{\star}$. However, ${\hat{\pi}}_{\mathsf{B}\mathsf{C}}$ is not a perfect copy of the expert and hence the states encountered during its deployment have a different distribution than $\mathcal{D}^{\star}$. This discrepancy is well known and leads to errors compounding in practice. More explicitly, consider an initial state $x_{0}$ sampled from $\mathcal{D}$. Then, at the first time step ${\hat{\pi}}_{\mathsf{B}\mathsf{C}}$ and $\pi^{\star}$ perform similarly since ${\hat{\pi}}_{\mathsf{B}\mathsf{C}}$ was trained using data sampled from $\mathcal{D}$. However, at the second time step the distributions over states produced by ${\hat{\pi}}_{\mathsf{B}\mathsf{C}}$ and $\pi^{\star}$ are different, which means that at the second time step ${\hat{\pi}}_{\mathsf{B}\mathsf{C}}$ would be evaluated on a distribution different than the one on which it was trained. Hence, with each time step, ${\hat{\pi}}_{\mathsf{B}\mathsf{C}}$ can take the dynamical system to parts of the state space that are less and less covered by the training trajectories resulting in error compounding.

Since BC does not account for the intrinsic distribution shift in imitation learning, the number of training trajectories it requires to guarantee a good learned controller can be large (e.g. exponential in the number of time steps or dimension). The methods for learning a MPC controller due to Hertneck et al., and Karg and Lucia are variants of behavior cloning and hence also suffer from the presence of distribution shift. Instead, we use and theoretically analyze the forward training algorithm that was initially used by Ross and Bagnell for the tabular MDP setting.

### Forward Training Algorithm

Forward Training Algorithm. ‣ Forward Training Algorithm: ‣ 2 The Forward Training Algorithm for Control ‣ Model Predictive Control via On-Policy Imitation Learning") learns a time-varying feedback controller ${\hat{\pi}}_{0:{T - 1}}$ in an inductive fashion: during stage $0$, it obtains ${\hat{\pi}}_{0}$ from the ERM (2.2. ‣ Forward Training Algorithm: ‣ 2 The Forward Training Algorithm for Control ‣ Model Predictive Control via On-Policy Imitation Learning")). The controller ${\hat{\pi}}_{0}$ is used in the dynamical system just at the initial time step. Then, given already learned controllers ${\hat{\pi}}_{0},\cdots,{\hat{\pi}}_{t - 1}$, to learn the policy ${\hat{\pi}}_{t}$ for time step $t$, Forward samples states ${\hat{x}}_{t}^{(i)} = {\varphi_{t}{(x_{0}^{(i)};{\hat{\pi}}_{0:{t - 1}})}}$, where $x_{0}^{},x_{0}^{},\cdots$ are sampled i.i.d. from the initial state distribution $\mathcal{D}$.

The advantage of this method is that at time step $t$ during deployment the controller ${\hat{\pi}}_{t}$ would be evaluated on the same distribution as that on which it was trained. Other recent works have also proposed learning inductively time-varying policies as a way to avoid distribution shifts.

Forward Training Algorithm (Ross and Bagnell ).
Given n and T, a time-varying policy π̂0: T − 1 is computed iteratively according to the following procedure:

Stage 0: Sample n initial states x0, ⋯, x0(n) ∼ 𝒟 and solve the following ERM: ${{\hat{\pi}}_{0} \in {\underset{\pi \in \Pi}{\arg\min}\mspace{21mu}{\frac{1}{n}{\sum\limits_{i = 1}^{n}{\|{{\pi^{\star}{(x_{0}^{(i)})}} - {\pi{(x_{0}^{(i)})}}}\|}}}}}.$ (2.2) Stage t: Sample fresh initial states x0, ⋯, x0(nt) ∼ 𝒟, where nt ≔ c n t ⌈ln2(t+1)⌉ + n and $c ≔ {\sum_{t = 1}^{\infty}{1/{({t{\ln^{2}{({t + 1})}}})}}}$, then evaluate the states x̂t(i) ≔ φt (x0(i);π̂0: t − 1), using the controllers π̂0: t − 1 learned in previous stages. Then, select π̂t s.t. ${{\hat{\pi}}_{t} \in {\underset{\pi \in \Pi}{\arg\min}\mspace{21mu}{\frac{1}{n_{t}}{\sum\limits_{i = 1}^{n_{t}}{\|{{\pi^{\star}{({\hat{x}}_{t}^{(i)})}} - {\pi{({\hat{x}}_{t}^{(i)})}}}\|}}}}}.$ (2.3) Since π⋆ is only defined on 𝒳 and since x̂t(i) could lie outside 𝒳, we define π⋆ (x) = π⋆ (proj𝒳x).
Output: The time-varying controller π̂ = π̂0: T − 1.

### The Sample Complexity of Learning a Controller with Forward Training Algorithm. ‣ Forward Training Algorithm: ‣ 2 The Forward Training Algorithm for Control ‣ Model Predictive Control via On-Policy Imitation Learning")

In this section, we discuss our statistical guarantees of the controllers produced by Forward Training Algorithm. ‣ Forward Training Algorithm: ‣ 2 The Forward Training Algorithm for Control ‣ Model Predictive Control via On-Policy Imitation Learning"). For simplicity, in this section we consider the setting without state constraints, i.e., $\mathcal{X} = {\mathbb{R}}^{d_{x}}$. Before we can state the main results of this section, we need to make an assumption on the class of controllers $\Pi$ used by Forward.

### Assumption 2.1

The model class $\Pi$ is a finite and contains $\pi^{\star}$. Moreover, for any $\pi \in \Pi$ and any $x \in \mathcal{X}$ we have ${\pi{(x)}} \in \mathcal{U}$.

The second part of the assumption just guarantees that $\Pi$ enforces the input constraints. Any controller class can be modified to satisfy this property by projecting the outputs of the controllers onto $\mathcal{U}$. We assume that the controller class $\Pi$ is finite for simplicity. In this case, our sample complexity guarantees scale with $\ln{|\Pi|}$---a quantity that arises through a standard generalization bound. When $\Pi$ is not finite, one can replace $\ln{|\Pi|}$ by learning-theoretic complexity measures such as the Rademacher complexity. Finally, in the MPC application we care about, the assumption $\pi^{\star} \in \Pi$ is easily satisfied. In the case of constrained linear dynamics with quadratic costs the optimal MPC controller is piecewise affine and it can be expressed as a neural network with ReLU activations as extensively discussed by Karg and Lucia \[16, Section I-D\] (see also ).

Now we are ready to state the main result of this section. Its proof relies on the empirical Bernstein inequality and is deferred to Subsection C.1.

### Theorem 2.1

Let $T \geqslant 1$ be the target time step, $\delta \in {}$, $n \geqslant 2$, and ${\mathfrak{B}}_{u} ≔ {\sup_{u \in \mathcal{U}}{\| u\|}}$. Let ${\hat{x}}_{t} = {\varphi_{t}{(x_{0};{\hat{\pi}}_{0:{t - 1}})}}$. When 2.1 holds, then under an event $\mathcal{E}$ of probability at least $1 - \delta$ $($over the randomness in the training process$)$, Forward Training Algorithm. ‣ Forward Training Algorithm: ‣ 2 The Forward Training Algorithm for Control ‣ Model Predictive Control via On-Policy Imitation Learning") produces a time-varying controller ${\hat{\pi}}_{0:{T - 1}}$ that satisfies

where $n_{t} ≔ {{cnt{\lceil{\ln^{2}{({t + 1})}}\rceil}} + n}$, $c ≔ {\sum_{t = 1}^{\infty}{1/{({t{\ln^{2}{({t + 1})}}})}}}$, and the expectation in (2.4) is with respect to the randomness in the initial state.

This result guarantees that the time-varying controller learned by Forward is close in expectation to the optimal controller. The following corollary to Theorem 2.1 bounds this difference with high probability using Markov's inequality (see Subsection C.2 for a proof):

### Corollary 2.2

Let $\delta \in {}$, $n \geqslant 2$, and ${\mathfrak{B}}_{u} ≔ {\sup_{u \in \mathcal{U}}{\| u\|}}$. Let ${\hat{x}}_{t} = {\varphi_{t}{(x_{0};{\hat{\pi}}_{0:{t - 1}})}}$. When 2.1 holds, then under the event $\mathcal{E}$ of probability at least $1 - \delta$ $($over the randomness in the training process$)$, Forward Training Algorithm. ‣ Forward Training Algorithm: ‣ 2 The Forward Training Algorithm for Control ‣ Model Predictive Control via On-Policy Imitation Learning") produces a time-varying controller ${\hat{\pi}}_{0:{T - 1}}$ such that

where the probability is with respect to the randomness in the initial state.

### Infinite Model Classes

The results presented in this section assume $\Pi$ is finite for simplicity. This assumption can be easily relaxed. For example, to get an analogue of the result of Theorem 2.1 for a infinite class $\Pi$, one can use the empirical Bernstein inequality \[24, Lemma 6\], which replaces $\ln{|\Pi|}$ by the logarithm of a "growth function" for the class $\Pi$ (see Appendix A). In the case where $\Pi$ is a class of ReLU Neural Networks, the latter quantity can be bounded by $\overset{\sim}{O}{(N_{\mathsf{p}\mathsf{a}\mathsf{r}\mathsf{a}\mathsf{m}\mathsf{s}})}$, where $N_{\mathsf{p}\mathsf{a}\mathsf{r}\mathsf{a}\mathsf{m}\mathsf{s}}$ is the number of parameters of the Neural Networks in $\Pi$.

### Trajectory Guarantees

Theorem 2.1 guarantees that Forward produces a controller $\hat{\pi}$ that generates inputs to the system that are close to those outputted by $\pi^{\star}$. However, this result does not immediately imply that $\hat{\pi}$ and $\pi^{\star}$ follow similar trajectories (errors could compound over time, causing $\hat{\pi}$'s trajectories to diverge from those of $\pi^{\star}$). Following the main ideas of Tu et al. and Pfrommer et al., one can in fact show guarantees in terms of trajectories when the closed-loop system under $\pi^{\star}$ is robust in an appropriate sense. See Appendix B the details.

In subsequent sections, we refine the results presented so far to the case of MPC.

## Background on the Control of Linear Systems

In this section, we review some background material on the control of linear systems, with a focus on the linear quadratic regulator (LQR) and on MPC. This section is not intended to be exhaustive; we only cover the notions needed in this work. We consider the linear dynamical system

which clearly maps to the control-affine setting (2.1) with ${f{(x_{t})}} = {Ax_{t}}$ and ${g{(x_{t})}} = B$.

### Unconstrained Optimal Control

Suppose we desire to solve the following infinite horizon optimal control problem

where $R \succ 0$ and $Q \succcurlyeq 0$. Then, the optimal controller can be computed in closed form. More specifically, let $P^{\mathsf{l}\mathsf{q}\mathsf{r}}$ be the unique positive definite solution to the discrete algebraic Riccati equation

Then, the optimal controller for (LQR) is given by

One important property of $\pi^{\mathsf{l}\mathsf{q}\mathsf{r}}$ is that the closed-loop system induced by the controller is stable. In other words, if $A_{K^{\mathsf{l}\mathsf{q}\mathsf{r}}} ≔ {A + {BK^{\mathsf{l}\mathsf{q}\mathsf{r}}}}$, we have ${\rho{(A_{K^{\mathsf{l}\mathsf{q}\mathsf{r}}})}} < 1$.

### Constrained Linear Dynamics and MPC

Suppose we wish to design a controller for the dynamics (3.1) such that $x_{t} \in \mathcal{X}$ and $u_{t} \in \mathcal{U}$ for all $t \geqslant 0$ and suppose we still wish to minimize the quadratic cost shown in (LQR). However, solving an infinite horizon problem under the constraints $x_{t} \in \mathcal{X}$, $u_{t} \in \mathcal{U}$ is computationally challenging. Moreover, it is not sufficient to find an optimal sequence of inputs $\{ u_{t}\}$ because open-loop control is brittle in the presence of noise.

MPC precisely resolves these issues by designing a feedback controller using the following finite horizon $N$-step optimal control problem. For any given initial state $x \in \mathcal{X}$ and a sequence of control inputs ${\mathbf{u}} = {(u_{0},u_{1},\cdots,u_{N - 1})}$,

where ${P_{\mathsf{f}},Q} \succcurlyeq 0$ and $R \succ 0$. Then, the finite horizon problem is:

where $\mathcal{X},\mathcal{U},\mathcal{X}_{\mathsf{f}}$ are constraint sets that are closed and contain the origin.

When the constraint sets are convex the finite-horizon problem is a convex optimization problem that can be solved efficiently. Let ${u_{0}^{\star}{(x)}},{u_{1}^{\star}{(x)}},\ldots,{u_{N - 1}^{\star}{(x)}}$ be the optimal solution to (MPC). To obtain a feedback controller, instead of deploying all inputs ${u_{0}^{\star}{(x)}},{u_{1}^{\star}{(x)}},\ldots,{u_{N - 1}^{\star}{(x)}}$, MPC only deploys the first input $u_{0}^{\star}{(x)}$. Then, it observes the next state of the system and solves another $N$-step problem starting at the new state. In particular, given the initial state $x_{0}$, the MPC controller is defined as ${\pi^{\mathsf{m}\mathsf{p}\mathsf{c}}{(x_{0})}} ≔ {u_{0}^{\star}{(x_{0})}}$. After controlling the system for a single step using $u_{0}^{\star}{(x_{0})}$, and say that the next state is $x_{1}$, MPC then resolves another $N$-step finite horizon problem starting from $x_{1}$ and use $u_{0}^{\star}{(x_{1})}$ and so on. Since the window of time over which the finite horizon problem is solved is shifting to the right by one at each step, MPC is also referred to as *receding horizon control (RHC*). We refer readers to textbooks (e.g., Morari and Lee, Rawlings et al., Borrelli et al. ) for extensive background.

MPC is a popular and successful control strategy because it can systematically handle multi-input-multi-output systems, nonlinearities, as well as constraints. The main drawback of MPC is that MPC must solve an optimization problem at each time step. For this reason, traditional applications were limited to slow systems such as chemical processes.

Now let us discuss the feasible domain of the optimization problem (MPC). See, e.g., \[3, Ch. 10-12\] for more context and details.

### Definition 3.1 (Feasible Domain of MPC)

Let $\mathcal{X}$, $\mathcal{U}$ be constraint sets and $\mathcal{X}_{\mathsf{f}}$ be a terminal set and recursively define the set $\mathcal{X}_{N},\mathcal{X}_{N - 1},\ldots,\mathcal{X}_{0}$ as $\mathcal{X}_{N} = \mathcal{X}_{\mathsf{f}}$, and $\mathcal{X}_{i} ≔ {\{{x \in \mathcal{X}}:{{\exists u} \in {{\mathcal{U}\text{s.t.}Ax} + {Bu}} \in \mathcal{X}_{i + 1}}\}}$, for $i = {{N - 1},{N - 2},\ldots,0}$. Then, $\mathcal{X}_{0}$ is the feasible domain of (MPC) w.r.t. $(\mathcal{X},\mathcal{U},\mathcal{X}_{\mathsf{f}})$.

### Persistent Feasibility and Stability

Ensuring the optimization problems (MPC) are feasible at each time step and ensuring that MPC stabilizes the underlying dynamics requires careful arguments. Merely having $x_{0} \in \mathcal{X}_{0}$ does not necessarily imply persistent feasibility, and a careful choice of terminal cost $P_{\mathsf{f}}$ and terminal constraint $\mathcal{X}_{\mathsf{f}}$ has to be made. Here, persistent feasibility means that if $x_{0} \in \mathcal{X}_{0}$ then ${\varphi_{t}{(x_{0};\pi^{\mathsf{m}\mathsf{p}\mathsf{c}})}} \in \mathcal{X}_{0}$, for all $t \geqslant 1$.

A sufficient condition for persistent feasibility is to choose $\mathcal{X}_{\mathsf{f}}$ as a control invariant set \[3, Theorem 12.1\], and for concreteness, we consider the set that is invariant with respect to the LQR controller $\pi^{\mathsf{l}\mathsf{q}\mathsf{r}}$ as below.

### Definition 3.2 (Positive Invariance w.r.t. LQR Controller)

Let ${\pi^{\mathsf{l}\mathsf{q}\mathsf{r}}{(x)}} = {K^{\mathsf{l}\mathsf{q}\mathsf{r}}x}$ denote the unconstrained LQR controller. We say that a set $\mathcal{O}$ is *positively invariant* with respect to $(\mathcal{X},\mathcal{U})$, if $\mathcal{O} \subseteq \mathcal{X}$ and whenever $x_{0} \in \mathcal{O}$, $x_{t} \in \mathcal{O}$ and ${\pi^{\mathsf{l}\mathsf{q}\mathsf{r}}{(x_{t})}} = {K^{\mathsf{l}\mathsf{q}\mathsf{r}}x_{t}} \in \mathcal{U}$, for all $t \geqslant 0$, where $x_{t + 1} = {{({A + {BK^{\mathsf{l}\mathsf{q}\mathsf{r}}}})}x_{t}}$. Let $\mathcal{O}_{\infty}^{\mathsf{l}\mathsf{q}\mathsf{r}}{(\mathcal{X},\mathcal{U})}$ be the *maximal positively invariant* set with respect to $(\mathcal{X},\mathcal{U})$.

As detailed in Borrelli et al. \[3, Sec. 10.2\], the maximal positively invariant set $\mathcal{O}_{\infty}^{\mathsf{l}\mathsf{q}\mathsf{r}}{(\mathcal{X},\mathcal{U})}$ (or its polytopic inner approximations) can be computed using polytopic computations.

Finally, we discuss a sufficient condition for the stability of the dynamics in feedback with MPC. It is well known that the MPC controller stabilizes the system (i.e. $\left. \parallel x_{t}\parallel \right.\rightarrow 0$ as $t\rightarrow\infty$) if it uses a Control Lyapunov Function (CLF) $p_{\mathsf{f}}$ as the terminal cost, where $p_{\mathsf{f}}$ is a CLF if

where ${\ell{(x,u)}} = {{x^{\top}Qx} + {u^{\top}Ru}}$ denotes the stage cost. The MPC objective in (3.4) has the function ${p_{\mathsf{f}}{(x)}} = {x^{\top}P_{\mathsf{f}}x}$ as the terminal cost, which can be made to fulfill (3.5) by choosing $P_{\mathsf{f}} = P^{\mathsf{l}\mathsf{q}\mathsf{r}}$ and $\mathcal{X}_{\mathsf{f}} = {\mathcal{O}_{\infty}^{\mathsf{l}\mathsf{q}\mathsf{r}}{(\mathcal{X},\mathcal{U})}}$. With these choices, we also have the following useful property that we use later:

See, e.g., \[35, Sec. 2.5.4\] for details. At a high level, when $x \in \mathcal{O}_{\infty}^{\mathsf{l}\mathsf{q}\mathsf{r}}$, the inputs produced by the LQR controller $\pi^{\mathsf{l}\mathsf{q}\mathsf{r}}$ correspond to the optimal solution of (MPC) since they are the optimal solution to the unconstrained objective $V_{N}$ thanks to the choice $P_{\mathsf{f}} = P^{\mathsf{l}\mathsf{q}\mathsf{r}}$ and the positive invariance of $\mathcal{O}_{\infty}^{\mathsf{l}\mathsf{q}\mathsf{r}}$---see 3.2. ‣ Persistent Feasibility and Stability: ‣ 3 Background on the Control of Linear Systems ‣ Model Predictive Control via On-Policy Imitation Learning"). Now, we are ready to discuss the main method and result of this work.

## On-policy Imitation Learning for MPC

In this section, we discuss how to adapt Forward to imitate MPC and we offer refined guarantees on the performance of the modified Forward method. We consider the dynamics, where unlike in Section 2, we allow $\mathcal{X} \subsetneq {\mathbb{R}}^{d_{x}}$:

All imitation learning methods need a choice of model class $\Pi$. We follow Karg and Lucia and choose $\Pi$ to be a class of neural networks with ReLU activations. This choice is appropriate because MPC implements a piecewise affine controller with the different pieces supported on polytopic regions when the constraints on the dynamics are polytopes. The main challenge in precomputing the piecewise affine controller implied by MPC is that the number of polytopic regions is exponential in the horizon $N$ and other problem dependent terms. However, polynomially many parameters are sufficient in order to express the MPC controller as a ReLU NN.

In order for Forward Training Algorithm. ‣ Forward Training Algorithm: ‣ 2 The Forward Training Algorithm for Control ‣ Model Predictive Control via On-Policy Imitation Learning") to imitate MPC efficiently, we modify it in the following ways:

Robust MPC as the Expert Policy: A guarantee of the form $\left. \parallel{{\pi^{\star}{({\hat{x}}_{t})}} - {{\hat{\pi}}_{t}{({\hat{x}}_{t})}}}\parallel \right. \leqslant \varepsilon$ does not necessarily ensure that the learned policy stabilizes the system: $\varepsilon$-deviations from the expert at each iteration can compound and lead to instability. To mitigate this issue, we use robust MPC *à la* Mayne et al. as the expert, which we detail in Subsection 4.1. Hertneck et al. also chose robust MPC as the expert, but their method is a form of behavior cloning that requires an extra validation step.

Sample-efficient Implementation: Forward learns a time-varying controller, which allows it to elude the challenge of distribution shift. However, as explained by Ross and Bagnell, learning a time-varying controller implies that the sample complexity grows with the number of stages $T$. Therefore, with a straightforward application of Forward it would not be possible to stabilize a dynamical system over an infinite horizon. To address this drawback, we use an insight of Sznaier and Damborg. Namely, after using MPC for a certain a number of time steps the state of the dynamics reaches a region on which MPC and the infinite horizon LQR agree. Therefore, our version of Forward estimates the number of time steps to switch to the time-invariant LQR controller.

We refer to the modified method as Forward-Switch, and we present its performance guarantees.

### Robust MPC as the Expert Policy

Before discussing the theoretical guarantees of our learned controller, we first review the robust MPC method that we use as the expert $\pi^{\star}$. Although we consider noiseless dynamics, it is useful to introduce disturbances in order to account for the errors introduced by the learned controller. Robust MPC is a controller that is robust against disturbances $w \in \mathcal{W}$ at each step, where $\mathcal{W}$ is a compact set. The robust MPC controller proposed by Mayne et al. differs from standard MPC in two ways:

robust MPC shrinks the constraint sets $\mathcal{X}$ and $\mathcal{U}$ in order to account for the disturbances,

robust MPC takes the first input produced by the MPC optimization problem and it linearly interpolates it with a stabilizing controller:

Before we can discuss the details of robust MPC, we introduce the following notion:

### Definition 4.1 (Disturbance Invariant Set \[18\])

Given a compact disturbance set $\mathcal{W}$, we say that $\Delta_{\mathcal{W}}$ is a disturbance invariant set if it is a neighborhood around the origin that satisfies ${{A_{K^{\mathsf{l}\mathsf{q}\mathsf{r}}}\Delta_{\mathcal{W}}} + \mathcal{W}} \subseteq \Delta_{\mathcal{W}}$, where $A_{K^{\mathsf{l}\mathsf{q}\mathsf{r}}} ≔ {A + {BK^{\mathsf{l}\mathsf{q}\mathsf{r}}}}$ (recall that ${\rho{(A_{K^{\mathsf{l}\mathsf{q}\mathsf{r}}})}} < 1$).

Kolmanovsky and Gilbert \[18, Section 4\] show that the minimal disturbance invariant set is

In our case, we let $\mathcal{W}$ be the ball of radius $\varepsilon > 0$ centered at the origin, i.e. $\mathcal{W} = {\mathsf{B}{(\varepsilon)}}$. Below, we estimate the radius of $\Delta_{\mathcal{W}}^{\min}$ based on the fact that $A_{K^{\mathsf{l}\mathsf{q}\mathsf{r}}}$ is stable. Since $A_{K^{\mathsf{l}\mathsf{q}\mathsf{r}}}$ is stable, there exists $\rho \in {({\rho{(A_{K^{\mathsf{l}\mathsf{q}\mathsf{r}}})}},1)}$ and $\tau > 0$ such that $\left. \parallel A_{K^{\mathsf{l}\mathsf{q}\mathsf{r}}}^{k}\parallel \right. \leqslant {\tau \cdot \rho^{k}}$ for all $k$ (see, e.g., \[22, eq \]).

### Claim 4.1

For $\varepsilon > 0$ let $\mathcal{W} = {\mathsf{B}{(\varepsilon)}}$. Then, $\Delta_{\mathcal{W}}^{\min} \subseteq {\mathsf{B}{({\kappa \cdot \varepsilon})}}$ with $\kappa ≔ \frac{\tau}{1 - \rho}$.

### Proof

From the fact $\left. \parallel A_{K^{\mathsf{l}\mathsf{q}\mathsf{r}}}\parallel \right.^{k} \leqslant {\tau \cdot \rho^{k}}$ for all $k$, it follows that $\left. \parallel{A_{K^{\mathsf{l}\mathsf{q}\mathsf{r}}}^{k}\mathcal{W}}\parallel \right. \leqslant {\tau\rho^{k}\varepsilon}$ for all $k$. This implies that ${A_{K^{\mathsf{l}\mathsf{q}\mathsf{r}}}^{k}\mathcal{W}} \subset {\mathsf{B}{({\tau\rho^{k}\varepsilon})}}$. Thus, $\Delta_{\mathcal{W}}^{\min} \subseteq {\sum_{k = 0}^{\infty}{\mathsf{B}{({\tau\rho^{k}\varepsilon})}}} = {\mathsf{B}{({\frac{\tau}{1 - \rho} \cdot \varepsilon})}}$. ∎

In light of 4.1, here and below readers can consider

Now, for a given state $x$, let us consider MPC with slightly stricter constraints. We begin with a notation: for two arbitrary sets $\mathcal{X}$ and $\mathcal{Y}$, $\mathcal{X} \ominus \mathcal{Y}$ is defined as ${\mathcal{X} \ominus \mathcal{Y}} ≔ \left. \{{x \in \mathcal{X}} \middle| {{x + \mathcal{Y}} \subseteq \mathcal{X}}\} \right.$. With this notation, we consider the following constraint sets, terminal set, and the positive invariant set:

$\overline{\mathcal{X}} ≔ {\mathcal{X} \ominus \Delta_{\mathcal{W}}}$ and $\overline{\mathcal{U}} ≔ {\mathcal{U} \ominus {K^{\mathsf{l}\mathsf{q}\mathsf{r}}\Delta_{\mathcal{W}}}}$.

${\overline{\mathcal{X}}}_{\mathsf{f}}$ is chosen as ${\overline{\mathcal{O}}}_{\infty} ≔ {\mathcal{O}_{\infty}^{\mathsf{l}\mathsf{q}\mathsf{r}}{(\overline{\mathcal{X}},\overline{\mathcal{U}})}}$, where $\mathcal{O}_{\infty}^{\mathsf{l}\mathsf{q}\mathsf{r}}{(\overline{\mathcal{X}},\overline{\mathcal{U}})}$ is the maximal positive invariant set with respect to $(\overline{\mathcal{X}},\overline{\mathcal{U}})$---see 3.2. ‣ Persistent Feasibility and Stability: ‣ 3 Background on the Control of Linear Systems ‣ Model Predictive Control via On-Policy Imitation Learning").

Using the new constraints and the terminal set, consider

where $V_{N}$ is defined in (3.4). The set of initial states ${\overline{\mathcal{X}}}_{0}$ for which $\overline{\mathsf{M}\mathsf{P}\mathsf{C}}$ admits a solution is the feasible domain of MPC with respect to the constraint sets $(\overline{\mathcal{X}},\overline{\mathcal{U}},{\overline{\mathcal{X}}}_{\mathsf{f}})$---see 3.1. ‣ Constrained Linear Dynamics and MPC: ‣ 3 Background on the Control of Linear Systems ‣ Model Predictive Control via On-Policy Imitation Learning"). Let $\overline{\pi}$ be the MPC controller defined by $\overline{\mathsf{M}\mathsf{P}\mathsf{C}}$; that is, for each $x \in {\overline{\mathcal{X}}}_{0}$, $\overline{\pi}{(x)}$ is given by

Henceforth, we assume that the initial state distribution $\mathcal{D}$ is almost surely supported within the feasibility set ${\overline{\mathcal{X}}}_{0}$.

Then, the key idea of Mayne et al. is to include the initial point $x_{0}$ as a parameter of the optimization problem: given $x \in {{({\mathcal{X}_{0} \oplus \Delta_{\mathcal{W}}})} \cap \mathcal{X}}$,

Letting ${{\overline{x}}_{0}{(x)}},{{\overline{u}}_{0}{(x)}},{{\overline{u}}_{1}{(x)}},\ldots,{{\overline{u}}_{N - 1}{(x)}}$ be the optimal solution to RMPC, the robust MPC controller of Mayne et al. is defined as

The following result establishes a key property of the robust MPC controller $\mathbf{π}$. We include the proof in Appendix D ‣ Model Predictive Control via On-Policy Imitation Learning") for completeness.

### Proposition 4.2 (\[27, Proposition 3 and Theorem 1\])

For any $x \in {{({\mathcal{X}_{0} \oplus \Delta_{\mathcal{W}}})} \cap \mathcal{X}}$, the robust MPC controller $\mathbf{π}$ robustly stabilizes the system with disturbances

in the sense that there exists a constant $\zeta \in {}$ such that $\left. \parallel{{\overline{x}}_{0}{(x_{t})}}\parallel \right. = {O{({\zeta^{t}\left. \parallel{{\overline{x}}_{0}{(x)}}\parallel \right.})}}$ for all $t \in {\mathbb{N}}$.

### Remark 4.2 (Time Step to Reach Positive Invariance)

Note that the conclusion $\left. \parallel{{\overline{x}}_{0}{(x_{t})}}\parallel \right. = {O{({\zeta^{t}\left. \parallel{{\overline{x}}_{0}{(x)}}\parallel \right.})}}$ holds for any choices of disturbances $\{ w_{t}\}$ as long as $w_{t} \in \mathcal{W}$, for all $t \in {\lbrack T\rbrack}$. Hence, for such disturbances, as long as the support of $\mathcal{D}$ is almost surely bounded, there must exist $\tau_{\infty}^{\star}$ such that ${{\overline{x}}_{0}{(x_{\tau_{\infty}^{\star}})}} \in {{\overline{\mathcal{O}}}_{\infty} \ominus \Delta_{\mathcal{W}}}$. Note that $\tau_{\infty}^{\star}$ depends solely on the system parameters and can be regarded as an absolute constant. Then, since $x_{\tau_{\infty}^{\star}} \in {{{\overline{x}}_{0}{(x_{\tau_{\infty}^{\star}})}} \oplus \Delta_{\mathcal{W}}}$, it follows that ${\forall{\{ w_{t}\}}} \in \mathcal{W}$, $x_{\tau_{\infty}^{\star}} \in {\overline{\mathcal{O}}}_{\infty}$.

Next, we use the robust MPC and propose an efficient implementation of Forward.

### Forward-Switch: Efficient Application of Forward Training Algorithm. ‣ Forward Training Algorithm: ‣ 2 The Forward Training Algorithm for Control ‣ Model Predictive Control via On-Policy Imitation Learning") to MPC

T= Imitation learning times steps. τ̂∞ is initialized as τ̂∞ = T. We use Forward Training Algorithm with π⋆ chosen as the robust MPC controller π to learn ${\overset{\sim}{\pi}}_{0:{T - 1}}$ as per the following procedure:
Forward training until positive invariance: At the end of each stage of Forward Training Algorithm, say the (t−1)-th stage, we sample ℓ trajectories according to our learned controller π̂0: t − 1 to generate x̂t(i), i = 1, 2, …, ℓ. - If ${\hat{x}}_{t}^{(i)} \in {\overline{\mathcal{O}}}_{\infty}$ for all i = 1, 2, …, ℓ, then we terminate Forward early and set τ̂∞ = t. - Otherwise, proceed to the next stage. Output policy: Output a time-varying policy ${\overset{\sim}{\pi}}_{0:{T - 1}}$ defined as ${\overset{\sim}{\pi}}_{t} ≔ \left\{ \begin{array}{ll}
{{\hat{\pi}}_{t},} &amp; {{{\text{if~}t} &lt; {\hat{\tau}}_{\infty}},} \\
{\pi^{\mathsf{l}\mathsf{q}\mathsf{r}},} &amp; {{{\text{if~}{\hat{\tau}}_{\infty}} \leqslant t \leqslant {T - 1}},}
\end{array} \right.$ (4.7) where πlqr is the unconstrained infinite horizon LQR controller defined in (3.3).

We are finally ready to formally present the modified Forward method---Forward-Switch. As explained by Ross and Bagnell \[39, Section 3\], the main limitation of Forward Training Algorithm. ‣ Forward Training Algorithm: ‣ 2 The Forward Training Algorithm for Control ‣ Model Predictive Control via On-Policy Imitation Learning") is that the number of stages increases with the horizon length $T$. We modify the method so that with high probability we only need $\tau_{\infty}^{\star}$ stages, where $\tau_{\infty}^{\star}$ is the time step required for RMPC to reach ${\overline{\mathcal{O}}}_{\infty}$ (see 4.2. ‣ 4.1 Robust MPC as the Expert Policy ‣ 4 On-policy Imitation Learning for MPC ‣ Model Predictive Control via On-Policy Imitation Learning")) that is independent of $T$. The main idea is that after at most $\tau_{\infty}^{\star}$ steps, the robust exponential stability of the MPC controller ensures that states enter the positively invariant set ${\overline{\mathcal{O}}}_{\infty}$ under any sequence of $\varepsilon$-bounded disturbances. Whenever the state enters the positively invariant set ${\overline{\mathcal{O}}}_{\infty}$, due to the choice of the terminal cost $P_{\mathsf{f}} = P^{\mathsf{l}\mathsf{q}\mathsf{r}}$, we know that the MPC controller $\overline{\pi}$ coincides with $\pi^{\mathsf{l}\mathsf{q}\mathsf{r}}$, which can be computed explicitly and stored efficiently, and so there is nothing more to learn. This insight, which goes back to Sznaier and Damborg, was in fact already used in the control literature to come up with an efficient algorithm for computing the constrained LQR controller.

To implement this idea, Forward-Switch must first estimate the number of steps the learned controller $\hat{\pi}$ requires to drive the state to ${\overline{\mathcal{O}}}_{\infty}$. Given that Forward Training Algorithm. ‣ Forward Training Algorithm: ‣ 2 The Forward Training Algorithm for Control ‣ Model Predictive Control via On-Policy Imitation Learning") learns the controller incrementally for each time step, one can estimate the number of steps $t$ by checking if all the states at stage $t$ from the generated trajectories have reached ${\overline{\mathcal{O}}}_{\infty}$. The next theorem justifies the step (4.7) of Forward-Switch that switches the learned controller ${\hat{\pi}}_{t}$ to $\pi^{\mathsf{l}\mathsf{q}\mathsf{r}}$ for $t \geqslant {\hat{\tau}}_{\infty}$: we show that with high probability, it holds that ${\hat{\tau}}_{\infty} \leqslant \tau_{\infty}^{\star}$ and ${\hat{x}}_{{\hat{\tau}}_{\infty}}$ lies in ${\overline{\mathcal{O}}}_{\infty}$ (in which the expert policy is indeed $\pi^{\mathsf{l}\mathsf{q}\mathsf{r}}$). The proof of the next theorem relies on 4.2. ‣ 4.1 Robust MPC as the Expert Policy ‣ 4 On-policy Imitation Learning for MPC ‣ Model Predictive Control via On-Policy Imitation Learning") and 2.2. The full details can be found in Subsection C.3.

### Theorem 4.3

Let ${\delta,\varepsilon} \in {}$ and ${\mathfrak{B}}_{u} ≔ {\sup_{u \in \mathcal{U}}{\| u\|}}$. Suppose 2.1 holds and that the support of $\mathcal{D}$ is almost surely bounded. Choose $n \geqslant \frac{14\ell\left. \parallel B\parallel \right.{\mathfrak{B}}_{u}{\ln{({{2T\ell{|\Pi|}}/\delta})}}}{\varepsilon\delta}$ and $\ell$ such that $\ell \geqslant \frac{10{\ln{({T/\delta})}}}{\delta}$. Then, under an event $\overline{\mathcal{E}}$ of probability at least $1 - {3\delta}$ $($over the randomness in the training process$)$, the stopping time ${\hat{\tau}}_{\infty}$ in Forward-Switch satisfies ${\hat{\tau}}_{\infty} \leqslant \tau_{\infty}^{\star}$ ($\tau_{\infty}^{\star}$ defined in 4.2. ‣ 4.1 Robust MPC as the Expert Policy ‣ 4 On-policy Imitation Learning for MPC ‣ Model Predictive Control via On-Policy Imitation Learning")) and

$${{{\mathbb{P}}{\lbrack{{\hat{x}}_{{\hat{\tau}}_{\infty}} \in {{\overline{\mathcal{O}}}_{\infty} \mid {{\hat{\tau}}_{\infty},\hat{\pi}}}}\rbrack}} \geqslant {1 - \delta}},$$ (4.8a)
$${{{\mathbb{P}}\left\lbrack {{{\forall t} = {0,\ldots,{{\hat{\tau}}_{\infty} - 1}}},{\left. \parallel{{{\mathbf{π}}{({\hat{x}}_{t})}} - {{\hat{\pi}}_{t}{({\hat{x}}_{t})}}}\parallel \right. \leqslant \left. {\varepsilon/{\| B\|}} \middle| {{\hat{\tau}}_{\infty},\hat{\pi}} \right.}} \right\rbrack} \geqslant {1 - \delta}},$$ (4.8b)

where the probabilities are over the randomness in the initial state. Further, under $\overline{\mathcal{E}}$ and the events in (4.8), the controller ${\overset{\sim}{\pi}}_{0:{T - 1}}$ does not violate any constraints.

### Remark 4.3 (Sample Complexity of Forward-Switch)

Note that under the setting of Theorem 4.3, the total number of expert demonstrations required by Forward-Switch is upper bounded by ${\overset{\sim}{O}{({n{\hat{\tau}}_{\infty}})}} = {\overset{\sim}{O}{(\frac{\ell{\hat{\tau}}_{\infty}}{\varepsilon\delta})}} = {\overset{\sim}{O}{(\frac{{\hat{\tau}}_{\infty}}{\varepsilon\delta^{2}})}}$, where $\overset{\sim}{O}$ hides polylog factors in $T$, $\delta$, and $|\Pi|$. Since Theorem 4.3 guarantees ${\hat{\tau}}_{\infty} \leqslant \tau_{\infty}^{\star}$, the total number of expert demonstrations is thus upper bounded by $\overset{\sim}{O}{(\frac{\tau_{\infty}^{\star} \land T}{\epsilon\delta^{2}})}$. Crucially, for large enough imitation learning horizon $T$ (in particular, for $T \geqslant \tau_{\infty}^{\star}$), the number of required trajectories depends only logarithmically on the horizon $T$ (since $\tau_{\infty}^{\star}$ is to be treated as a system's constant independent of $T$---see 4.2. ‣ 4.1 Robust MPC as the Expert Policy ‣ 4 On-policy Imitation Learning for MPC ‣ Model Predictive Control via On-Policy Imitation Learning")).

We are left to quantify the cost achieved by the learned controller, which we do next.

### Performance Guarantees

In this subsection, we bound the suboptimality of the controller $\overset{\sim}{\pi}$ learned by Forward-Switch. For the theoretical analysis, we first define the Q-function of the reference controller $\overline{\pi}$ defined in $\overline{\mathsf{M}\mathsf{P}\mathsf{C}}$. Let ${\overline{J}}_{t}:{{\overline{\mathcal{X}}}_{0}\rightarrow{\mathbb{R}}}$ be the $t$-step cost function of $\overline{\pi}$, i.e., for $x_{0} \in {\overline{\mathcal{X}}}_{0}$ and ${\overline{x}}_{s} ≔ {\varphi_{s}{(x_{0};\overline{\pi})}}$,

where ${\ell{(x,u)}} = {{x^{\top}Qx} + {u^{\top}Ru}}$ denotes the stage cost. For $x \in {\overline{\mathcal{X}}}_{0}$, and an input $u \in \overline{\mathcal{U}}$ such that ${{Ax} + {Bu}} \in {\overline{\mathcal{X}}}_{0}$, define

Let ${\overset{\sim}{J}}_{t}$ be the $t$-step cost of the learned policy $\overset{\sim}{\pi}$ from Forward-Switch (defined in a similar way to ${\overline{J}}_{t}$). We now state the performance guarantee of Forward-Switch.

### Theorem 4.4 (Performance Guarantee)

Let ${\delta,\varepsilon} \in {}$ and assume the same conditions as Theorem 4.3. Then, under the same event $\overline{\mathcal{E}}$ as Theorem 4.3 and for any $x_{0}$ satisfying the events in (4.8), we have

where $O{( \cdot )}$ hides an absolute constant that depends on the system parameters and $\tau_{\infty}^{\star}$ is a system's constant independent of $T$---see 4.2. ‣ 4.1 Robust MPC as the Expert Policy ‣ 4 On-policy Imitation Learning for MPC ‣ Model Predictive Control via On-Policy Imitation Learning").

The proof of this result is deferred to Subsection C.4.

## Experiments

In this section, we demonstrate our theoretical results for the MPC application through a set of experiments. We demonstrate that Behavior Cloning can indeed suffer from distribution shift and destabilize the system, while Forward can cope with this issue.

Figure 1: The results for the normalized cost-to-go and the constraint satisfaction ratio for the trajectory length T = 30. The first row contains the results for d = 3, and the second row shows the results for d = 5.

### Experimental Setup

For $d \in {\{ 3,5\}}$, we consider an open-loop unstable dynamical system $x_{t + 1} = {{Ax_{t}} + {Bu_{t}}}$, where $A \in {\mathbb{R}}^{d \times d}$ is chosen as an upper triangular matrix whose diagonal entries are $1.1$ and the upper diagonal entries are chosen from the uniform distribution over $\lbrack{- 2},2\rbrack$ (see Appendix E for the $A$ matrices used for the plots), and $B \in {\mathbb{R}}^{d \times 1}$ is chosen as ${\lbrack{0\ 0\cdots1}\rbrack}^{\top}$. We impose the constraints $x_{t} \in {\lbrack{- 100},100\rbrack}^{d}$, $u_{t} \in {\lbrack{- 10},10\rbrack}$ and choose the initial state distribution $\mathcal{D}$ as the uniform distribution over ${\lbrack 8,10\rbrack}^{d}$. We set the horizon $N$ of MPC to be $20$ and the number of imitation learning time steps $T$ to be $30$, and we use pyMPC for implementing MPC demonstrations. In the MPC optimization, we did not impose the terminal constraint.

To parametrize the policies we use a fully connected neural network with three hidden layers. Each layer has $50$ neurons followed by ReLU activations. For optimization, we use the Adam optimizer with a learning rate of $0.001$. We train the policies for $500$ epochs.

### Results

We first compare the performance of Behavior Cloning and Forward. For each algorithm, we measure the normalized cost ${{J^{\mathsf{a}\mathsf{l}\mathsf{g}\mathsf{o}\mathsf{r}\mathsf{i}\mathsf{t}\mathsf{h}\mathsf{m}}{(x_{0})}}/J^{\mathsf{m}\mathsf{p}\mathsf{c}}}{(x_{0})}$ for $20$ different test initial states $x_{0}$ sampled from $\mathcal{D}$. Moreover, we report the constraint satisfaction ratio along the test trajectories. We repeat each setting in the experiment for $50$ times and report the $95\%$ confidence intervals with error bars. The results are reported in Figure 1. As one can see from Figure 1, for these systems, there is a significant difference in performance between the two algorithms. For $d = 3$, the mean normalized cost of Forward is less than $1.2$ for all settings, while that of Behavior Cloning is greater than $40$ even with $900$ MPC demonstrations. For $d = 5$, the normalized cost-to-go of Forward is less than $1.13$ with $450$ MPC demonstrations, while that of Behavior Cloning is higher than $240$ even with $900$ MPC demonstrations.

Figure 2: The first two coordinates of the sample trajectories produced by MPC, Forward, Behavior Cloning. The left plot is for d = 3, and the right column is for d = 5.

In order to visualize the results, we plot the first two coordinates of the sample trajectories produced by each controller in Figure 2. As one can see from the figure, Behavior Cloning indeed suffers from the distribution shift issue: small errors in the learned controller pile up along time steps and lead the trajectory to a region where the learned controller cannot stabilize the system.

### Remark 5.1 (Results for 2D systems)

We also tried several $2$-dimensional systems, including (i) the $d = 2$ case of our simulated system and (ii) double integrators (especially, the versions in \[5, Section VI-A\] and \[15, Section VI-A\]). Interestingly, for these systems we tried, we did not see much difference in the performance between the two algorithms.

We now test the performance of our proposed method Forward-Switch. For the same systems as before, we estimate ${\hat{\tau}}_{\infty}$ as per the procedure described in Forward-Switch, where we check if the sample trajectory ${\hat{x}}_{t}^{(i)}$ lies in a subset^11^1For ease of implementation, we use the subset that is defined by the level set of the terminal cost, i.e., $p_{\mathsf{f}} ≔ {x^{\top}P^{\mathsf{l}\mathsf{q}\mathsf{r}}x}$. It is well-known that the level set of $p_{\mathsf{f}}$ is positive invariant w.r.t. the LQR Controller. We simply choose the maximal level set of $p_{\mathsf{f}} ≔ {x^{\top}P^{\mathsf{l}\mathsf{q}\mathsf{r}}x}$ in which the constraints are not violated under the LQR controller. of ${\overline{\mathcal{O}}}_{\infty}$. Our estimated ${\hat{\tau}}_{\infty}$ for the $d = 5$ case is $12$.

In Figure 3, we report the mean normalized cost-to-go and the constraint satisfaction ratio of Forward-Switch. Notably, Forward-Switch achieves the mean normalized cost-to-go of $\approx 1.034$ with only $180$ MPC demonstrations, while Forward achieves the mean normalized cost-to-go of $\approx 35$ when trained using $210$ MPC demonstrations. Hence, our experiment indicates that Forward-Switch is indeed more sample-efficient in some situations.

We also compare the performance of Forward-Switch with its Behavior Cloning counterpart. For a fair comparison, we also train Behavior Cloning for $T = 12$ steps and then for time steps greater than $12$, we employ the LQR controller. In Figure 3, we report the mean normalized cost-to-go and the constraint satisfaction ratio of Forward-Switch and its Behavior Cloning counterpart. Although $T = 12$ is smaller than the previous experiment setting where $T = 30$, we still see a noticeable difference in the performance between the two algorithms.

Figure 3: The performance comparison between Forward-Switch and its Behavior Cloning counterpart. The result is for d = 5. Here the estimated number of steps τ̂∞ to reach the positive invariant set ${\overline{\mathcal{O}}}_{\infty}$ is 12.

## Conclusion

In this work, we leverage techniques from imitation learning to circumvent MPC's reliance on online optimization. More specifically, we adapt an interactive imitation learning algorithm called the forward training algorithm to take advantage of MPC's properties. When presented with a constrained linear system we show that our modified method learns a controller that stabilizes the dynamics, satisfies the state and input constraints, and achieves cost as good as that obtained by MPC. We validate our results through simulations and compare the modified forward training algorithm with other data-driven methods.

We conclude this paper with interesting future directions. An alternative approach to ours is to learn the value function instead of the policy. In particular, it is known that the MPC value function is convex and piecewise quadratic. It might be interesting to see whether such properties make the approach based on learning value functions more desirable. More broadly, whether the value of each expert demonstration can be used to improve performance of imitation learning algorithms would be of great interest. Lastly, combining our approach with a direct policy optimization approach (e.g., Chen et al. ) would be of great practical interest, given that a direct policy optimization typically requires more samples.
