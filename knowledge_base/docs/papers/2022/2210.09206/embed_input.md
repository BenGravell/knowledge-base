<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Model Predictive Control via On-Policy Imitation Learning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we leverage the rapid advances in imitation learning, a topic of intense recent focus in the Reinforcement Learning (RL) literature, to develop new sample complexity results and performance guarantees for data-driven Model Predictive Control (MPC) for constrained linear systems. In its simplest form, imitation learning is an approach that tries to learn an expert policy by querying samples from an expert. Recent approaches to data-driven MPC have used the simplest form of imitation learning known as behavior cloning to learn controllers that mimic the performance of MPC by online sampling of the trajectories of the closed-loop MPC system. Behavior cloning, however, is a method that is known to be data inefficient and suffer from distribution shifts. As an alternative, we develop a variant of the forward training algorithm which is an on-policy imitation learning method proposed by Ross et al.. Our algorithm uses the structure of constrained linear MPC, and our analysis uses the properties of the explicit MPC solution to theoretically bound the number of online MPC trajectories needed to achieve optimal performance. We validate our results through simulations and show that the forward training algorithm is indeed superior to behavior cloning when applied to MPC.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optimization-based control methods such as model predictive control (MPC) have been among the most versatile techniques in feedback control design for more than 40 years. Such techniques have been successfully applied to control of dynamic systems in a variety of domains such as autonomous vehicles, chemical plants, humanoid robots, and many others. Nonetheless, MPC's versatility comes at a cost. Having to solve optimization problems online makes it difficult to deploy MPC on high-dimensional systems that have strict latency requirements and limited computational or energy resources. To mitigate this issue, considerable effort went into developing faster, tailored optimization methods for MPC.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Instead of following these approaches, we pursue a data-driven methodology. We propose and study a scheme to collect data interactively from a dynamical system in feedback with an MPC controller and in order to learn an explicit controller that maps states to inputs. Such approaches are known in the reinforcement learning literature as imitation learning and they are well suited for MPC because one can query MPC for the next input at any desired state; all that is needed is to solve the corresponding optimization problem. Nonetheless, in order to learn controllers that are guaranteed to stabilize dynamical systems, to satisfy state and action constraints, and to obtain low cost, we would need to exploit several properties of MPC.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our goal of obtaining an explicit map from states to inputs that encapsulates an MPC controller falls under the purview of explicit MPC, which aims to pre-compute and store the solutions of the optimization problems that might be encountered at runtime.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In general, explicit MPC aims to pre-compute an exact representation of the MPC controller while we aim to learn a controller that performs as well as MPC with high probability. In the same vain, Hertneck et al. and Karg and Lucia suggest learning a controller from data. However, their approaches collect all the trajectory data using MPC before any learning occurs and do not interact with the dynamics further. The lack of interaction in imitation learning is known to lead to sub-optimal performance because small learning errors would cause a controller produced by such a method to result in states with a different distribution than those produced by MPC during training. In other words, distribution shift leads to error compounding. Our proposed approach completely avoids this issue. To this end, our contributions in this paper can be summarized as follows: We start by analyzing the imitation learning method known as the forward training algorithm (Forward) in the setting of control affine systems.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We modify Forward to make it suitable for MPC applications with constraints. Firstly, Forward learns a different controller for each distinct time step and hence it cannot be applied straightforwardly to problems with long or infinite horizons. Fortunately, after sufficiently many times steps, the MPC controller applied to time invariant linear systems becomes equivalent to the classical linear quadratic regulator (LQR). We exploit this property; we modify Forward to switch to LQR after a number of time steps estimated from data. Secondly, to improve the robustness of our method we require Forward to imitate robust MPC instead of standard MPC. We refer to our modified method as Forward-switch.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We theoretically guarantee that a controller learned with Forward-switch stabilizes linear systems and satisfies their constraints as long as certain amount of data is available. Moreover, we bound the cost suboptimality of the learned controller, showing that it approaches optimal performance as more data becomes available. None of the previous works on imitating MPC included such guarantees. We also provide theoretical sample complexity bounds using state of the art tools of high dimensional statistics and statistical learning theory.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We validate the efficacy of the modified forward training algorithm on simulated MPC problems, showing that it surpasses non-interactive approaches.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The Forward Training Algorithm for Control", "weight": 1.0} -->

In this section, we present the imitation learning method Forward and bound the distance between the trajectories produced by the learned controller and those produced by the expert when the dynamics are control-affine. In subsequent sections, we specialize our analysis to the case where the expert is a MPC controller applied to constrained linear systems.

<!-- chunk {"id": "body-0011", "role": "body", "section": "The Forward Training Algorithm for Control", "weight": 1.0} -->

Imitation learning aims to learn from demonstrations a controller $\hat{\pi}$ that imitates the behavior of a target controller $\pi^{\star}$, called *expert policy* or simply *expert* in the reinforcement learning literature. Imitation learning is valuable when $\pi^{\star}$ lacks a closed-form expression or is expensive to query in general. For instance, $\pi^{\star}$ could be a human performing a task or a MPC controller. More formally, in imitation learning it is assumed that for a state $x$ we can access the input $\pi^{\star}{(x)}$. Then, the aim is to use data $\{ x_{i},{\pi^{\star}{(x_{i})}}\}$ to learn a controller $\hat{\pi}$ such that ${\hat{\pi}{(x)}} \approx {\pi^{\star}{(x)}}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "The Forward Training Algorithm for Control", "weight": 1.0} -->

Behavior cloning (BC) is the simplest imitation learning method. It consists of collecting $m$ independent trajectories $\varphi_{t}{(x_{0}^{(i)};\pi^{\star})}$ with initial states $x_{0}^{}$, $x_{0}^{}$,..., $x_{0}^{(m)}$ sampled randomly from an initial distribution $\mathcal{D}$. Then, BC produces a controller ${\hat{\pi}}_{\mathsf{B}\mathsf{C}}$ through empirical risk minimization (ERM): where $\Pi$ is a class of models that map the state space to the input space and $\left. \parallel \cdot \parallel \right.$ is any norm (although it could be replaced by a more general loss function). All our results assume that $\pi^{\star} \in \Pi$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Distribution Shift", "weight": 1.0} -->

The states collected using the expert $\pi^{\star}$ have a particular distribution $\mathcal{D}^{\star}$. BC produces a controller ${\hat{\pi}}_{\mathsf{B}\mathsf{C}}$ that, when evaluated on samples from $\mathcal{D}^{\star}$, behaves similarly to the expert $\pi^{\star}$. However, ${\hat{\pi}}_{\mathsf{B}\mathsf{C}}$ is not a perfect copy of the expert and hence the states encountered during its deployment have a different distribution than $\mathcal{D}^{\star}$. This discrepancy is well known and leads to errors compounding in practice. More explicitly, consider an initial state $x_{0}$ sampled from $\mathcal{D}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Distribution Shift", "weight": 1.0} -->

Then, at the first time step ${\hat{\pi}}_{\mathsf{B}\mathsf{C}}$ and $\pi^{\star}$ perform similarly since ${\hat{\pi}}_{\mathsf{B}\mathsf{C}}$ was trained using data sampled from $\mathcal{D}$. However, at the second time step the distributions over states produced by ${\hat{\pi}}_{\mathsf{B}\mathsf{C}}$ and $\pi^{\star}$ are different, which means that at the second time step ${\hat{\pi}}_{\mathsf{B}\mathsf{C}}$ would be evaluated on a distribution different than the one on which it was trained. Hence, with each time step, ${\hat{\pi}}_{\mathsf{B}\mathsf{C}}$ can take the dynamical system to parts of the state space that are less and less covered by the training trajectories resulting in error compounding.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Distribution Shift", "weight": 1.0} -->

Since BC does not account for the intrinsic distribution shift in imitation learning, the number of training trajectories it requires to guarantee a good learned controller can be large (e.g. exponential in the number of time steps or dimension). The methods for learning a MPC controller due to Hertneck et al., and Karg and Lucia are variants of behavior cloning and hence also suffer from the presence of distribution shift. Instead, we use and theoretically analyze the forward training algorithm that was initially used by Ross and Bagnell for the tabular MDP setting.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Forward Training Algorithm", "weight": 1.0} -->

Forward Training Algorithm. ‣ Forward Training Algorithm: ‣ 2 The Forward Training Algorithm for Control ‣ Model Predictive Control via On-Policy Imitation Learning") learns a time-varying feedback controller ${\hat{\pi}}_{0:{T - 1}}$ in an inductive fashion: during stage $0$, it obtains ${\hat{\pi}}_{0}$ from the ERM (2.2. ‣ Forward Training Algorithm: ‣ 2 The Forward Training Algorithm for Control ‣ Model Predictive Control via On-Policy Imitation Learning")). The controller ${\hat{\pi}}_{0}$ is used in the dynamical system just at the initial time step.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Forward Training Algorithm", "weight": 1.0} -->

The advantage of this method is that at time step $t$ during deployment the controller ${\hat{\pi}}_{t}$ would be evaluated on the same distribution as that on which it was trained. Other recent works have also proposed learning inductively time-varying policies as a way to avoid distribution shifts.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Forward Training Algorithm", "weight": 1.0} -->

Forward Training Algorithm (Ross and Bagnell).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Forward Training Algorithm", "weight": 1.0} -->

Given n and T, a time-varying policy π̂0: T − 1 is computed iteratively according to the following procedure: Stage 0: Sample n initial states x0, ⋯, x0(n) ∼ 𝒟 and solve the following ERM: ${{\hat{\pi}}_{0} \in {\underset{\pi \in \Pi}{\arg\min}\mspace{21mu}{\frac{1}{n}{\sum\limits_{i = 1}^{n}{\|{{\pi^{\star}{(x_{0}^{(i)})}} - {\pi{(x_{0}^{(i)})}}}\|}}}}}.$ (2.2) Stage t: Sample fresh initial states x0, ⋯, x0(nt) ∼ 𝒟, where nt ≔ c n t ⌈ln2(t + 1)⌉ + n and $c ≔ {\sum_{t =

<!-- chunk {"id": "body-0020", "role": "body", "section": "Forward Training Algorithm", "weight": 1.0} -->

1}^{\infty}{1/{({t{\ln^{2}{({t + 1})}}})}}}$, then evaluate the states x̂t(i) ≔ φt (x0(i); π̂0: t − 1), using the controllers π̂0: t − 1 learned in previous stages.

<!-- chunk {"id": "body-0021", "role": "body", "section": "The Sample Complexity of Learning a Controller with Forward Training Algorithm. ‣ Forward Training Algorithm: ‣ 2 The Forward Training Algorithm for Control ‣ Model Predictive Control via On-Policy Imitation Learning\")", "weight": 1.0} -->

In this section, we discuss our statistical guarantees of the controllers produced by Forward Training Algorithm. ‣ Forward Training Algorithm: ‣ 2 The Forward Training Algorithm for Control ‣ Model Predictive Control via On-Policy Imitation Learning"). For simplicity, in this section we consider the setting without state constraints, i.e., $\mathcal{X} = {\mathbb{R}}^{d_{x}}$. Before we can state the main results of this section, we need to make an assumption on the class of controllers $\Pi$ used by Forward.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

The second part of the assumption just guarantees that $\Pi$ enforces the input constraints. Any controller class can be modified to satisfy this property by projecting the outputs of the controllers onto $\mathcal{U}$. We assume that the controller class $\Pi$ is finite for simplicity. In this case, our sample complexity guarantees scale with $\ln{|\Pi|}$---a quantity that arises through a standard generalization bound. When $\Pi$ is not finite, one can replace $\ln{|\Pi|}$ by learning-theoretic complexity measures such as the Rademacher complexity. Finally, in the MPC application we care about, the assumption $\pi^{\star} \in \Pi$ is easily satisfied. In the case of constrained linear dynamics with quadratic costs the optimal MPC controller is piecewise affine and it can be expressed as a neural network with ReLU activations as extensively discussed by Karg and Lucia \[16, Section I-D\] (see also ).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

Now we are ready to state the main result of this section. Its proof relies on the empirical Bernstein inequality and is deferred to Subsection C.1.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Infinite Model Classes", "weight": 1.0} -->

The results presented in this section assume $\Pi$ is finite for simplicity. This assumption can be easily relaxed. For example, to get an analogue of the result of Theorem 2.1 for a infinite class $\Pi$, one can use the empirical Bernstein inequality \[24, Lemma 6\], which replaces $\ln{|\Pi|}$ by the logarithm of a "growth function" for the class $\Pi$ (see Appendix A). In the case where $\Pi$ is a class of ReLU Neural Networks, the latter quantity can be bounded by $\overset{\sim}{O}{(N_{\mathsf{p}\mathsf{a}\mathsf{r}\mathsf{a}\mathsf{m}\mathsf{s}})}$, where $N_{\mathsf{p}\mathsf{a}\mathsf{r}\mathsf{a}\mathsf{m}\mathsf{s}}$ is the number of parameters of the Neural Networks in $\Pi$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Trajectory Guarantees", "weight": 1.0} -->

Theorem 2.1 guarantees that Forward produces a controller $\hat{\pi}$ that generates inputs to the system that are close to those outputted by $\pi^{\star}$. However, this result does not immediately imply that $\hat{\pi}$ and $\pi^{\star}$ follow similar trajectories (errors could compound over time, causing $\hat{\pi}$'s trajectories to diverge from those of $\pi^{\star}$). Following the main ideas of Tu et al. and Pfrommer et al., one can in fact show guarantees in terms of trajectories when the closed-loop system under $\pi^{\star}$ is robust in an appropriate sense. See Appendix B the details.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Trajectory Guarantees", "weight": 1.0} -->

In subsequent sections, we refine the results presented so far to the case of MPC.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Unconstrained Optimal Control", "weight": 1.0} -->

More specifically, let $P^{\mathsf{l}\mathsf{q}\mathsf{r}}$ be the unique positive definite solution to the discrete algebraic Riccati equation Then, the optimal controller for (LQR) is given by One important property of $\pi^{\mathsf{l}\mathsf{q}\mathsf{r}}$ is that the closed-loop system induced by the controller is stable. In other words, if $A_{K^{\mathsf{l}\mathsf{q}\mathsf{r}}} ≔ {A + {BK^{\mathsf{l}\mathsf{q}\mathsf{r}}}}$, we have ${\rho{(A_{K^{\mathsf{l}\mathsf{q}\mathsf{r}}})}} < 1$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Constrained Linear Dynamics and MPC", "weight": 1.0} -->

Suppose we wish to design a controller for the dynamics (3.1) such that $x_{t} \in \mathcal{X}$ and $u_{t} \in \mathcal{U}$ for all $t \geqslant 0$ and suppose we still wish to minimize the quadratic cost shown in (LQR). However, solving an infinite horizon problem under the constraints $x_{t} \in \mathcal{X}$, $u_{t} \in \mathcal{U}$ is computationally challenging. Moreover, it is not sufficient to find an optimal sequence of inputs $\{ u_{t}\}$ because open-loop control is brittle in the presence of noise.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Constrained Linear Dynamics and MPC", "weight": 1.0} -->

MPC precisely resolves these issues by designing a feedback controller using the following finite horizon $N$-step optimal control problem. For any given initial state $x \in \mathcal{X}$ and a sequence of control inputs ${\mathbf{u}} = {(u_{0},u_{1},\cdots,u_{N - 1})}$, where ${P_{\mathsf{f}},Q} \succcurlyeq 0$ and $R \succ 0$. Then, the finite horizon problem is: where $\mathcal{X},\mathcal{U},\mathcal{X}_{\mathsf{f}}$ are constraint sets that are closed and contain the origin.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Constrained Linear Dynamics and MPC", "weight": 1.0} -->

When the constraint sets are convex the finite-horizon problem is a convex optimization problem that can be solved efficiently. Let ${u_{0}^{\star}{(x)}},{u_{1}^{\star}{(x)}},\ldots,{u_{N - 1}^{\star}{(x)}}$ be the optimal solution to (MPC). To obtain a feedback controller, instead of deploying all inputs ${u_{0}^{\star}{(x)}},{u_{1}^{\star}{(x)}},\ldots,{u_{N - 1}^{\star}{(x)}}$, MPC only deploys the first input $u_{0}^{\star}{(x)}$. Then, it observes the next state of the system and solves another $N$-step problem starting at the new state.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Constrained Linear Dynamics and MPC", "weight": 1.0} -->

In particular, given the initial state $x_{0}$, the MPC controller is defined as ${\pi^{\mathsf{m}\mathsf{p}\mathsf{c}}{(x_{0})}} ≔ {u_{0}^{\star}{(x_{0})}}$. After controlling the system for a single step using $u_{0}^{\star}{(x_{0})}$, and say that the next state is $x_{1}$, MPC then resolves another $N$-step finite horizon problem starting from $x_{1}$ and use $u_{0}^{\star}{(x_{1})}$ and so. Since the window of time over which the finite horizon problem is solved is shifting to the right by one at each step, MPC is also referred to as *receding horizon control (RHC*). We refer readers to textbooks (e.g., Morari and Lee, Rawlings et al., Borrelli et al. ) for extensive background.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Constrained Linear Dynamics and MPC", "weight": 1.0} -->

MPC is a popular and successful control strategy because it can systematically handle multi-input-multi-output systems, nonlinearities, as well as constraints. The main drawback of MPC is that MPC must solve an optimization problem at each time step. For this reason, traditional applications were limited to slow systems such as chemical processes.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Constrained Linear Dynamics and MPC", "weight": 1.0} -->

Now let us discuss the feasible domain of the optimization problem (MPC). See, e.g., \[3, Ch. 10-12\] for more context and details.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Persistent Feasibility and Stability", "weight": 1.0} -->

Ensuring the optimization problems (MPC) are feasible at each time step and ensuring that MPC stabilizes the underlying dynamics requires careful arguments. Merely having $x_{0} \in \mathcal{X}_{0}$ does not necessarily imply persistent feasibility, and a careful choice of terminal cost $P_{\mathsf{f}}$ and terminal constraint $\mathcal{X}_{\mathsf{f}}$ has to be made. Here, persistent feasibility means that if $x_{0} \in \mathcal{X}_{0}$ then ${\varphi_{t}{(x_{0};\pi^{\mathsf{m}\mathsf{p}\mathsf{c}})}} \in \mathcal{X}_{0}$, for all $t \geqslant 1$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Persistent Feasibility and Stability", "weight": 1.0} -->

A sufficient condition for persistent feasibility is to choose $\mathcal{X}_{\mathsf{f}}$ as a control invariant set \[3, Theorem 12.1\], and for concreteness, we consider the set that is invariant with respect to the LQR controller $\pi^{\mathsf{l}\mathsf{q}\mathsf{r}}$ as below.

<!-- chunk {"id": "body-0036", "role": "body", "section": "On-policy Imitation Learning for MPC", "weight": 1.0} -->

In this section, we discuss how to adapt Forward to imitate MPC and we offer refined guarantees on the performance of the modified Forward method. We consider the dynamics, where unlike in Section 2, we allow $\mathcal{X} \subsetneq {\mathbb{R}}^{d_{x}}$: All imitation learning methods need a choice of model class $\Pi$. We follow Karg and Lucia and choose $\Pi$ to be a class of neural networks with ReLU activations. This choice is appropriate because MPC implements a piecewise affine controller with the different pieces supported on polytopic regions when the constraints on the dynamics are polytopes. The main challenge in precomputing the piecewise affine controller implied by MPC is that the number of polytopic regions is exponential in the horizon $N$ and other problem dependent terms. However, polynomially many parameters are sufficient in order to express the MPC controller as a ReLU NN.

<!-- chunk {"id": "body-0037", "role": "body", "section": "On-policy Imitation Learning for MPC", "weight": 1.0} -->

In order for Forward Training Algorithm. ‣ Forward Training Algorithm: ‣ 2 The Forward Training Algorithm for Control ‣ Model Predictive Control via On-Policy Imitation Learning") to imitate MPC efficiently, we modify it in the following ways: Robust MPC as the Expert Policy: A guarantee of the form $\left. \parallel{{\pi^{\star}{({\hat{x}}_{t})}} - {{\hat{\pi}}_{t}{({\hat{x}}_{t})}}}\parallel \right. \leqslant \varepsilon$ does not necessarily ensure that the learned policy stabilizes the system: $\varepsilon$-deviations from the expert at each iteration can compound and lead to instability. To mitigate this issue, we use robust MPC *à la* Mayne et al. as the expert, which we detail in Subsection 4.1. Hertneck et al. also chose robust MPC as the expert, but their method is a form of behavior cloning that requires an extra validation step.

<!-- chunk {"id": "body-0038", "role": "body", "section": "On-policy Imitation Learning for MPC", "weight": 1.0} -->

Sample-efficient Implementation: Forward learns a time-varying controller, which allows it to elude the challenge of distribution shift. However, as explained by Ross and Bagnell, learning a time-varying controller implies that the sample complexity grows with the number of stages $T$. Therefore, with a straightforward application of Forward it would not be possible to stabilize a dynamical system over an infinite horizon. To address this drawback, we use an insight of Sznaier and Damborg. Namely, after using MPC for a certain a number of time steps the state of the dynamics reaches a region on which MPC and the infinite horizon LQR agree. Therefore, our version of Forward estimates the number of time steps to switch to the time-invariant LQR controller.

<!-- chunk {"id": "body-0039", "role": "body", "section": "On-policy Imitation Learning for MPC", "weight": 1.0} -->

We refer to the modified method as Forward-Switch, and we present its performance guarantees.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Robust MPC as the Expert Policy", "weight": 1.0} -->

Before discussing the theoretical guarantees of our learned controller, we first review the robust MPC method that we use as the expert $\pi^{\star}$. Although we consider noiseless dynamics, it is useful to introduce disturbances in order to account for the errors introduced by the learned controller. Robust MPC is a controller that is robust against disturbances $w \in \mathcal{W}$ at each step, where $\mathcal{W}$ is a compact set. The robust MPC controller proposed by Mayne et al.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 4.2 (Time Step to Reach Positive Invariance)", "weight": 1.0} -->

Next, we use the robust MPC and propose an efficient implementation of Forward.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Forward-Switch: Efficient Application of Forward Training Algorithm. ‣ Forward Training Algorithm: ‣ 2 The Forward Training Algorithm for Control ‣ Model Predictive Control via On-Policy Imitation Learning\") to MPC", "weight": 1.0} -->

T= Imitation learning times steps. τ̂∞ is initialized as τ̂∞ = T. We use Forward Training Algorithm with π⋆ chosen as the robust MPC controller π to learn ${\overset{\sim}{\pi}}_{0:{T - 1}}$ as per the following procedure: Forward training until positive invariance: At the end of each stage of Forward Training Algorithm, say the (t − 1)-th stage, we sample ℓ trajectories according to our learned controller π̂0: t − 1 to generate x̂t(i), i = 1, 2, …, ℓ. - If ${\hat{x}}_{t}^{(i)} \in {\overline{\mathcal{O}}}_{\infty}$ for all i = 1, 2, …, ℓ, then we terminate Forward early and set τ̂∞ = t. - Otherwise, proceed to the next stage.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Forward-Switch: Efficient Application of Forward Training Algorithm. ‣ Forward Training Algorithm: ‣ 2 The Forward Training Algorithm for Control ‣ Model Predictive Control via On-Policy Imitation Learning\") to MPC", "weight": 1.0} -->

We are finally ready to formally present the modified Forward method---Forward-Switch. As explained by Ross and Bagnell \[39, Section 3\], the main limitation of Forward Training Algorithm. ‣ Forward Training Algorithm: ‣ 2 The Forward Training Algorithm for Control ‣ Model Predictive Control via On-Policy Imitation Learning") is that the number of stages increases with the horizon length $T$. We modify the method so that with high probability we only need $\tau_{\infty}^{\star}$ stages, where $\tau_{\infty}^{\star}$ is the time step required for RMPC to reach ${\overline{\mathcal{O}}}_{\infty}$ (see 4.2. ‣ 4.1 Robust MPC as the Expert Policy ‣ 4 On-policy Imitation Learning for MPC ‣ Model Predictive Control via On-Policy Imitation Learning")) that is independent of $T$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Forward-Switch: Efficient Application of Forward Training Algorithm. ‣ Forward Training Algorithm: ‣ 2 The Forward Training Algorithm for Control ‣ Model Predictive Control via On-Policy Imitation Learning\") to MPC", "weight": 1.0} -->

The main idea is that after at most $\tau_{\infty}^{\star}$ steps, the robust exponential stability of the MPC controller ensures that states enter the positively invariant set ${\overline{\mathcal{O}}}_{\infty}$ under any sequence of $\varepsilon$-bounded disturbances. Whenever the state enters the positively invariant set ${\overline{\mathcal{O}}}_{\infty}$, due to the choice of the terminal cost $P_{\mathsf{f}} = P^{\mathsf{l}\mathsf{q}\mathsf{r}}$, we know that the MPC controller $\overline{\pi}$ coincides with $\pi^{\mathsf{l}\mathsf{q}\mathsf{r}}$, which can be computed explicitly and stored efficiently, and so there is nothing more to learn.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Forward-Switch: Efficient Application of Forward Training Algorithm. ‣ Forward Training Algorithm: ‣ 2 The Forward Training Algorithm for Control ‣ Model Predictive Control via On-Policy Imitation Learning\") to MPC", "weight": 1.0} -->

This insight, which goes back to Sznaier and Damborg, was in fact already used in the control literature to come up with an efficient algorithm for computing the constrained LQR controller.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Forward-Switch: Efficient Application of Forward Training Algorithm. ‣ Forward Training Algorithm: ‣ 2 The Forward Training Algorithm for Control ‣ Model Predictive Control via On-Policy Imitation Learning\") to MPC", "weight": 1.0} -->

To implement this idea, Forward-Switch must first estimate the number of steps the learned controller $\hat{\pi}$ requires to drive the state to ${\overline{\mathcal{O}}}_{\infty}$. Given that Forward Training Algorithm. ‣ Forward Training Algorithm: ‣ 2 The Forward Training Algorithm for Control ‣ Model Predictive Control via On-Policy Imitation Learning") learns the controller incrementally for each time step, one can estimate the number of steps $t$ by checking if all the states at stage $t$ from the generated trajectories have reached ${\overline{\mathcal{O}}}_{\infty}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Forward-Switch: Efficient Application of Forward Training Algorithm. ‣ Forward Training Algorithm: ‣ 2 The Forward Training Algorithm for Control ‣ Model Predictive Control via On-Policy Imitation Learning\") to MPC", "weight": 1.0} -->

‣ 4.1 Robust MPC as the Expert Policy ‣ 4 On-policy Imitation Learning for MPC ‣ Model Predictive Control via On-Policy Imitation Learning") and 2.2. The full details can be found in Subsection C.3.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Remark 4.3 (Sample Complexity of Forward-Switch)", "weight": 1.0} -->

Since Theorem 4.3 guarantees ${\hat{\tau}}_{\infty} \leqslant \tau_{\infty}^{\star}$, the total number of expert demonstrations is thus upper bounded by $\overset{\sim}{O}{(\frac{\tau_{\infty}^{\star} \land T}{\epsilon\delta^{2}})}$. Crucially, for large enough imitation learning horizon $T$ (in particular, for $T \geqslant \tau_{\infty}^{\star}$), the number of required trajectories depends only logarithmically on the horizon $T$ (since $\tau_{\infty}^{\star}$ is to be treated as a system's constant independent of $T$---see 4.2. ‣ 4.1 Robust MPC as the Expert Policy ‣ 4 On-policy Imitation Learning for MPC ‣ Model Predictive Control via On-Policy Imitation Learning")).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Remark 4.3 (Sample Complexity of Forward-Switch)", "weight": 1.0} -->

We are left to quantify the cost achieved by the learned controller, which we do next.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we demonstrate our theoretical results for the MPC application through a set of experiments. We demonstrate that Behavior Cloning can indeed suffer from distribution shift and destabilize the system, while Forward can cope with this issue.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

For $d \in {\{ 3,5\}}$, we consider an open-loop unstable dynamical system $x_{t + 1} = {{Ax_{t}} + {Bu_{t}}}$, where $A \in {\mathbb{R}}^{d \times d}$ is chosen as an upper triangular matrix whose diagonal entries are $1.1$ and the upper diagonal entries are chosen from the uniform distribution over $\lbrack{- 2},2\rbrack$ (see Appendix E for the $A$ matrices used for the plots), and $B \in {\mathbb{R}}^{d \times 1}$ is chosen as ${\lbrack{0\ 0\cdots1}\rbrack}^{\top}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

We impose the constraints $x_{t} \in {\lbrack{- 100},100\rbrack}^{d}$, $u_{t} \in {\lbrack{- 10},10\rbrack}$ and choose the initial state distribution $\mathcal{D}$ as the uniform distribution over ${\lbrack 8,10\rbrack}^{d}$. We set the horizon $N$ of MPC to be $20$ and the number of imitation learning time steps $T$ to be $30$, and we use pyMPC for implementing MPC demonstrations. In the MPC optimization, we did not impose the terminal constraint.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

To parametrize the policies we use a fully connected neural network with three hidden layers. Each layer has $50$ neurons followed by ReLU activations. For optimization, we use the Adam optimizer with a learning rate of $0.001$. We train the policies for $500$ epochs.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Results", "weight": 1.0} -->

We first compare the performance of Behavior Cloning and Forward. For each algorithm, we measure the normalized cost ${{J^{\mathsf{a}\mathsf{l}\mathsf{g}\mathsf{o}\mathsf{r}\mathsf{i}\mathsf{t}\mathsf{h}\mathsf{m}}{(x_{0})}}/J^{\mathsf{m}\mathsf{p}\mathsf{c}}}{(x_{0})}$ for $20$ different test initial states $x_{0}$ sampled from $\mathcal{D}$. Moreover, we report the constraint satisfaction ratio along the test trajectories. We repeat each setting in the experiment for $50$ times and report the $95\%$ confidence intervals with error bars. The results are reported in Figure 1. As one can see from Figure 1, for these systems, there is a significant difference in performance between the two algorithms.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Results", "weight": 1.0} -->

For $d = 3$, the mean normalized cost of Forward is less than $1.2$ for all settings, while that of Behavior Cloning is greater than $40$ even with $900$ MPC demonstrations. For $d = 5$, the normalized cost-to-go of Forward is less than $1.13$ with $450$ MPC demonstrations, while that of Behavior Cloning is higher than $240$ even with $900$ MPC demonstrations.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Results", "weight": 1.0} -->

In order to visualize the results, we plot the first two coordinates of the sample trajectories produced by each controller in Figure 2. As one can see from the figure, Behavior Cloning indeed suffers from the distribution shift issue: small errors in the learned controller pile up along time steps and lead the trajectory to a region where the learned controller cannot stabilize the system.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Remark 5.1 (Results for 2D systems)", "weight": 1.0} -->

We also tried several $2$-dimensional systems, including (i) the $d = 2$ case of our simulated system and (ii) double integrators (especially, the versions in \[5, Section VI-A\] and \[15, Section VI-A\]). Interestingly, for these systems we tried, we did not see much difference in the performance between the two algorithms.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Remark 5.1 (Results for 2D systems)", "weight": 1.0} -->

We now test the performance of our proposed method Forward-Switch. For the same systems as before, we estimate ${\hat{\tau}}_{\infty}$ as per the procedure described in Forward-Switch, where we check if the sample trajectory ${\hat{x}}_{t}^{(i)}$ lies in a subset^11^1For ease of implementation, we use the subset that is defined by the level set of the terminal cost, i.e., $p_{\mathsf{f}} ≔ {x^{\top}P^{\mathsf{l}\mathsf{q}\mathsf{r}}x}$. It is well-known that the level set of $p_{\mathsf{f}}$ is positive invariant w.r.t. the LQR Controller.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Remark 5.1 (Results for 2D systems)", "weight": 1.0} -->

In Figure 3, we report the mean normalized cost-to-go and the constraint satisfaction ratio of Forward-Switch. Notably, Forward-Switch achieves the mean normalized cost-to-go of $\approx 1.034$ with only $180$ MPC demonstrations, while Forward achieves the mean normalized cost-to-go of $\approx 35$ when trained using $210$ MPC demonstrations. Hence, our experiment indicates that Forward-Switch is indeed more sample-efficient in some situations.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Remark 5.1 (Results for 2D systems)", "weight": 1.0} -->

We also compare the performance of Forward-Switch with its Behavior Cloning counterpart. For a fair comparison, we also train Behavior Cloning for $T = 12$ steps and then for time steps greater than $12$, we employ the LQR controller. In Figure 3, we report the mean normalized cost-to-go and the constraint satisfaction ratio of Forward-Switch and its Behavior Cloning counterpart. Although $T = 12$ is smaller than the previous experiment setting where $T = 30$, we still see a noticeable difference in the performance between the two algorithms.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we leverage techniques from imitation learning to circumvent MPC's reliance on online optimization. More specifically, we adapt an interactive imitation learning algorithm called the forward training algorithm to take advantage of MPC's properties. When presented with a constrained linear system we show that our modified method learns a controller that stabilizes the dynamics, satisfies the state and input constraints, and achieves cost as good as that obtained by MPC. We validate our results through simulations and compare the modified forward training algorithm with other data-driven methods.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We conclude this paper with interesting future directions. An alternative approach to ours is to learn the value function instead of the policy. In particular, it is known that the MPC value function is convex and piecewise quadratic. It might be interesting to see whether such properties make the approach based on learning value functions more desirable. More broadly, whether the value of each expert demonstration can be used to improve performance of imitation learning algorithms would be of great interest. Lastly, combining our approach with a direct policy optimization approach (e.g., Chen et al. ) would be of great practical interest, given that a direct policy optimization typically requires more samples.
