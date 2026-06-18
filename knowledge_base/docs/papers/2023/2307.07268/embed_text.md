## Introduction

The interplay between machine learning, system identification and adaptive control has unveiled a fertile area of research which has the potential to answer some of the standing research questions in the field of learning-based control. Recent advances in online learning techniques have provided new perspectives on the design of algorithms where unknown systems can be controlled by acquiring knowledge through repeated interactions with the unknown environment Hazan & Singh. This has close connections with adaptive control Astrom & Wittenmark and in general with learning-based control techniques Benosman. Minimax adaptive control is taken in this work as a prototypical example of the latter line of works to draw connections with regret, i.e. the performance metrics used in online learning. Design of minimax control for uncertain systems was investigated as early as in Salmon; Didinsky & Basar. Subsequently, the design of minimax adaptive control was investigated for scalar systems with unknown input matrix sign in Rantzer, for finite sets of linear systems in Rantzer; Cederberg et al. and for the output feedback case in Kjellqvist & Rantzer, respectively. There have been earlier works on robust adaptive control in Chichka & Speyer; Yoneyama et al. where uncertainties in system dynamics were considered. Minimax adaptive control problems are generally challenging as obtaining exact $\ell_{2}$-gain bounds as explained in French & Trenn; Vinnicombe; Rantzer can be hard for multiple input multiple outputs systems with finite set of linear models and optimality can only be achieved if the exploration and exploitation trade-off is exactly captured.\
The recent interest developed towards analyzing control algorithms for systems with unknown dynamics through the lens of regret analysis has the promise to enable a better understanding of this trade-off. There are quantities that are of interest but are unknown in advance to the online controller. We refer to such unknown entity as *Quantity of Interest (QI)*. Lack of knowledge about a QI determines an accumulated cost, with respect to a control designed with perfect knowledge, which denotes the notion of regret. For instance, the growth of expected regret in linear quadratic control was investigated in Jedra & Proutiere when matrices $(A,B)$ were unknown. Regret bounds have been investigated in Boffi et al. for adaptive control problems in stochastic setting. This paper proposes an online learning analysis of minimax adaptive control of linear-time invariant systems featuring adversarial disturbance and a priori knowledge of a finite set of systems. One of the distinctive novelty is a new definition of regret, suitable for this setting in which the QIs are both the system dynamics and the exogenous disturbance. From an online learning perspective, efficient adaptive control algorithms are characterized by limiting the growth of regret over time. To quantify the regret, we usually require an optimal control policy (policy regret) or a sequence of best control actions (dynamic regret) available in hindsight as in Goel & Hassibi. Here, we propose studying the policy regret associated with the minimax adaptive controller by comparing it against the standard $\mathcal{H}_{\infty}$ control which knows the dynamics.\
Recently, Karapetyan et al. investigated the regret of robustness of an $\mathcal{H}_{\infty}$ controller (whose QI is just the adversarial disturbance) when compared to an oracle controller which has knowledge of the future disturbance trajectory. Also related is the work in Hazan et al., which investigated the regret analysis for the generic non-stochastic control problem and their system identification approach employed random inputs before controlling it using disturbance-based policy. Similarly, Agarwal et al. studied online control with adversarial disturbances and proposed a disturbance action control policy based efficient algorithm to obtain nearly tight regret bounds. On the contrary, our work looks at nonlinear adaptive state feedback policy which *concurrently* controls the system under adversarial disturbance and implicitly learns the system dynamics. This gives rise to an interesting trade-off in the adversary strategy, whereby the worst-case disturbance is the one that delays the learning process of the controller while minimizing the energy spent (which is penalized in the total cost).\

Contributions: We provide a detailed analysis for the minimax adaptive control algorithm proposed in Rantzer with the aim to improve our understanding on the role of the adaptation mechanism and the adversary disturbance on the regret. Since an explicit expression for the optimal minimax adaptive controller is not known, we apply our analysis to the candidate sub-optimal minimax adaptive control algorithm^11^1The distinction between the optimal and the sub-optimal minimax adaptive control policies will be made clear at appropriate places. developed in Rantzer; Cederberg et al.. Specifically, the main contributions are:

Definition of the: model-based regret corresponding to a specific model in the uncertainty set characterizing the accumulated cost with respect to an optimal controller in hindsight which knows the true dynamics; total regret as the worst-case model-based regret corresponding to any model in the uncertainty set.

Construction of an adversarial disturbance policy which provably prevents the minimax adaptive controller from learning the true dynamics (Theorem 1).

Despite the possible difficulty in the identification of the true dynamics, we show that the minimax adaptive controller enjoys a sub-linear regret rate with respect to the best $\mathcal{H}_{\infty}$ controller in hindsight (Theorem 2).

The rest of the paper is organised as follows. The problem formulation is discussed in §2. The online learning analysis is performed in §3, and some of its features are further elucidated through numerical simulation in §4. Finally, the main findings of the paper are summarized in §5.

Notation and Preliminaries. The cardinality of the set $A$ is denoted by $|A|$. The set of real numbers, integers and the natural numbers are denoted by ${\mathbb{R}},{\mathbb{Z}}$, and $\mathbb{N}$ respectively. For a matrix $A \in {\mathbb{R}}^{n \times n}$, we denote its transpose and its trace by $A^{\top}$ and ${\mathbf{T}\mathbf{r}}{(A)}$ respectively. We denote by ${\mathbb{S}}^{n}$, the set of symmetric matrices in ${\mathbb{R}}^{n \times n}$. For $A \in {\mathbb{S}}^{n}$, we write $A \succ 0$ and $A \succeq 0$ to say that $A$ is positive definite and positive semi-definite, respectively. An identity matrix of dimension $n$ is denoted by $I_{n}$. Given ${x \in {\mathbb{R}}^{n}},{{A \in {\mathbb{R}}^{n \times n}},{B \in {\mathbb{R}}^{n \times n}}}$, the notations $\left\| x \right\|_{A}^{2}$ and $\left\| B \right\|_{A}^{2}$ mean $x^{\top}Ax$ and ${\mathbf{T}\mathbf{r}}\left( {B^{\top}AB} \right)$ respectively. A signal $\{ x_{k}\}$ is said to be in $\ell_{2}$ space if it has finite energy meaning that ${\sum_{k = 0}^{\infty}x_{k}^{2}} < \infty$. For any time $T \in {\mathbb{N}}$, if the truncation of a signal $\{ x_{k}\}$ to the interval $\lbrack 0,T\rbrack$ lies in the $\ell_{2}$ space, then the signal is said to be lying in the extended $\ell_{2}$ space denoted by $\ell_{2e}$.

## Problem Formulation Using Minimax Adaptive Control

In this section we introduce the minimax adaptive control subject of our investigations through online learning.

### Minimax adaptive control with finite set of linear systems

Consider the following discrete-time linear system

where $x_{k} \in {\mathbb{R}}^{n}$ and $u_{k} \in {\mathbb{R}}^{m}$ denote the system states and control inputs, respectively, and the additive disturbance $w_{k} \in {\mathbb{R}}^{n}$ is assumed to be adversarial. The true system matrices $A \in {\mathbb{R}}^{n \times n}$ and $B \in {\mathbb{R}}^{n \times m}$ are unknown but assumed to belong to a set $\mathcal{M}$ with $|\mathcal{M}| = \mathcal{F} \in {\mathbb{N}}$ defined such that ${M_{i}:={(A_{i},B_{i})} \in \mathcal{M}},{i = {1,\ldots,\mathcal{F}}}$, where all pairs are assumed throughout to be stabilizable. For instance, control of a discrete-time linearized inverted pendulum dynamics falls under the above setting when the pendulum length is uncertain. Generally, minimax adaptive control approach can be a suitable design solution when multiple systems who do not share common Lyapunov function need to be controlled by a single controller. Let us denote by $\Pi$ the set of admissible control policies such that

An optimal adaptive control policy should interact with the system in order to extract information about the unknown system matrices $A,B$ while also guaranteeing good performance and robustness to the adversarial disturbance. This can be achieved by optimizing the following minimax cost

where ${c{(x^{\pi},u^{\pi},Q,R)}}:={\left. \parallel x^{\pi}\parallel \right._{Q}^{2} + \left. \parallel u^{\pi}\parallel \right._{R}^{2}}$ for given penalty matrices ${Q \succ 0},{R \succ 0}$; $x^{\pi}$ denotes the evolution of the state of starting from $x_{0}$ under the control input $u^{\pi}$ from the policy $\pi$; and $\gamma > 0$ quantifies the desired level of robustness to the external disturbance (higher $\gamma$ resulting in weaker robustness requirements). The optimal minimax control policy $\pi^{\dagger}$ and the associated cost are given by

and the resulting disturbance attenuation level achieved by the control policy $\pi^{\dagger}$ from disturbance to the regulated output $\zeta:=\begin{bmatrix}
\end{bmatrix}^{\top}$ is denoted by $\gamma^{\dagger}$ and is defined as

This formulation provides a family of minimax control policy parameterized by $\gamma$, which are guaranteed to exist ${\forall\gamma} > \gamma^{\dagger}$. We cast the problem as a zero-sum dynamic game with the control policy $\pi$ being the minimizing player and the adversaries $(w,A,B)$ being the maximizing players Rantzer. The solution boils down to solving a minimax dynamic programming problem, which is intractable in most cases. An approximate (i.e. sub-optimal) solution has been recently proposed in Rantzer; Cederberg et al., and this will be the subject of this study. The following lemma summarizes the main result of Rantzer, i.e. an explicit expression for an adaptive controller satisfying a pre-specified $\ell_{2}$-gain bound from disturbance to error.

### Lemma 1

Given a compact set of linear models $\mathcal{M}$, and positive definite penalty matrices ${Q \in {\mathbb{R}}^{n \times n}},{R \in {\mathbb{R}}^{m \times m}}$, suppose that there exists ${K_{1},\ldots,K_{\mathcal{F}}} \in {\mathbb{R}}^{m \times n}$ and matrices $P_{ij} \in {\mathbb{R}}^{n \times n}$ with $0 \prec P_{ij} = P_{ji} \prec {\gamma^{2}I}$ such that

where ${\overline{A}}_{il} = {A_{i} - {B_{i}K_{l}}}$ denotes the closed loop system matrix for $x \in {\mathbb{R}}^{n}$ with ${i,j,l} \in {\{ 1,\ldots,\mathcal{F}\}}$. Then, the bound $J_{\overline{\pi}}{(x_{0},\gamma)} \leq \max_{i,j}\left. \parallel x_{0}\parallel \right._{P_{ij}}^{2}$ is valid for the minimax adaptive control policy $\overline{\pi}$ defined by

$l_{k}$ ${:={\operatorname{argmin}\limits_{i \in {\{ 1,\ldots,\mathcal{F}\}}}\underset{:=\alpha_{i}}{\underbrace{\underset{\tau=0}{\overset{k-1}{\sum}}\left. \parallel{x_{\tau+1}-{A_{i}x_{\tau}}-{B_{i}u_{\tau}}}\parallel \right.^{2}}}}}.$ (7b)

The controller defined in (7a), and denoted by $\overline{\pi}$ in the reminder, is sub-optimal compared to $\pi^{\dagger}$, i.e. the associated $\ell_{2}$ gain is $\overline{\gamma} > \gamma^{\dagger}$. Further, the cost $J_{\overline{\pi}}{(x_{0},\gamma)}$ is finite as long as $\gamma > \overline{\gamma}$. The control input (7a) is nonlinear as it depends on all the past history, an approach based on least squares estimation from Didinsky & Basar.

### Known Dynamics Case: Standard $\mathcal{H}_{\infty}$ Control

When the system matrices $A,B$ are known, problem reduces to the standard $\mathcal{H}_{\infty}$ control. That is, a control input ${u = {Kx}},{K \in {\mathbb{R}}^{m \times n}}$ is sought such that it minimizes the $\mathcal{H}_{\infty}$ norm of the closed loop system from $d$ to $\zeta$

where $T_{d\rightarrow\zeta}$ is related to the cost function in by appropriate choice of matrices $Q,R$. Using this observation, we define for every system model $M_{i}:={(A_{i},B_{i})} \in \mathcal{M}$, the associated $\mathcal{H}_{\infty}$ control policy $\pi_{i}^{\star} \in \Pi$, which can be found by solving the coupled Riccati equations below Başar & Bernhard

The dynamic game has an unique saddle point solution

where $K_{i}^{\star} = {R^{- 1}B_{i}^{\top}\mathbf{M}_{i}\Lambda_{i}^{- 1}A_{i}}$ and $L_{i}^{\star} = {{(\gamma_{i}^{\star})}^{- 2}\mathbf{M}_{i}\Lambda_{i}^{- 1}A_{i}}$. Here, $\psi_{i}^{\star}$ denotes the worst case adversarial disturbance policy and it is, like $\pi_{i}^{\star}$, a linear function of $x_{k}$. The quantity

denotes the corresponding worst-case $\ell_{2}$ gain from the disturbance to the regulated output for the model ${M_{i},i} \in \mathcal{M}$.

## Regret of Minimax Adaptive Control

Regret analysis compares the performance of an online algorithm that takes decisions in the presence of uncertainty with respect to a clairvoyant policy with hindsight knowledge. For this reason, it is used here in order to better understand the performance achieved when controlling the system using minimax adaptive control algorithm.

### Definition 1

Regret of an online control algorithm $\mathcal{A}$ operating in the presence of uncertainty is defined as the additional cost incurred by the algorithm $\mathcal{A}$ in comparison to an optimal controller in hindsight that operates by knowing the uncertainty.

We choose here the $\mathcal{H}_{\infty}$ controller associated with the true system as the optimal policy in hindsight. Note that ${\forall i} \in {1,\ldots,\mathcal{F}}$, ${J_{\pi_{i}^{\star}}{(x_{0},\gamma)}} < {J^{\dagger}{(x_{0},\gamma)}}$ as the minimax adaptive control policy $\pi^{\dagger}$ can never do better than the $\mathcal{H}_{\infty}$ policy $\pi_{i}^{\star}$ of the corresponding true system. It is possible to use a different policy other than the $\mathcal{H}_{\infty}$ policy for the comparison. One could compare against a control policy that solves the linear quadratic problem with known disturbance but the true ${(A,B)} \in \mathcal{M}$ being unknown. However, to the best of our knowledge, there is no *causal* solution for the optimal control policy to that problem. In principle, the optimal policy in hindsight should know apriori about any of the QIs that minimax does not know and also have a closed form causal solution.

The study of the minimax adaptive control problem through online learning is divided in three steps: investigation of adversarial disturbance strategies that can lead to performance deterioration of the policy $\overline{\pi}$; definition of suitable notions of regret for this problem; investigation of the regret properties of the policy $\overline{\pi}$. We do not advocate the regret as a metric to measure the robustness of a control policy. Rather, we suggest to use the regret as a tool to identify areas of improvement of an online control policy by comparing it against multiple optimal policies in hindsight. Regret analysis could also give insights for the online control design to foresee and counteract against several possible strategies of adversaries trying to worsen its performance. One such possible strategy of an adversary with respect to the policy $\overline{\pi}$ is illustrated below.

### Adversarial disturbance strategies for minimax control

The key adaptive mechanism of policy $\overline{\pi}$ in can be interpreted as an implicit identification of the underlying plant. It is then natural to ask whether this is provably able to eventually converge to the correct estimate for the system. The following theorem gives a negative answer by constructing an adversarial disturbance strategy preventing the controller from optimally controlling the true system.

### Theorem 1

Given a compact set of models $\mathcal{M}$ with $|\mathcal{M}| = \mathcal{F}$ including the true model of the system, consider the policy $\overline{\pi}$ given by. Let $j \in {\{ 1,\ldots,\mathcal{F}\}}$ denote the index of the true model unknown to the policy $\overline{\pi}$. Then, ${\forall k} \in {\mathbb{N}}$, ${\exists\theta_{f,k}} \in {\mathbb{R}}$, $f = {1,\ldots,\mathcal{F}}$ such that the disturbance given by

lets $\overline{\pi}$ to determine a minimizer $l_{k} \neq j$ in (7b).

### Proof

Recall from (7b) that when $i = j$, we simply get $\alpha_{j} = {\sum_{\tau = 0}^{k - 1}\left. \parallel w_{\tau}\parallel \right.^{2}}$. For other cases when $i \neq j$, we expand $\alpha_{i}$ using the $w_{k}$ given by to get

with $v_{\tau}^{(i)} = {{{({{\theta_{j,k}A_{j}} - A_{i}})}x_{\tau}} + {{({{\theta_{j,k}B_{j}} - B_{i}})}u_{\tau}}}$. Then, the disturbance can let the controller choose $l_{k} = i$ as per (7b) deviating from the true value of $j$ through the appropriate selection of the constants ${\{\theta_{f,k}\}}_{f = 1}^{\mathcal{F}}$ such that $\alpha_{i} < \alpha_{j}$. One simple choice would be to choose ${\theta_{j,k} = {- 1}},{\theta_{i,k} = 1}$ and ${\{\theta_{f,k}\}}_{{f = 1},{{f \neq i},{f \neq j}}}^{\mathcal{F}} = 0$ at time $k$ such that $\alpha_{i} = 0$ in. Such a disturbance strategy would let the controller choose $l_{k} = i$ rather than $j$. Note that the adversary has the freedom to make $\alpha_{i} = 0$ for its own choice of ${i \in {\{ 1,\ldots,\mathcal{F}\}}},{i \neq j}$ at any time step $k$ using ${\{\theta_{f,k}\}}_{f = 1}^{\mathcal{F}}$. ∎

Remarks: Disturbances with smaller magnitudes maximise the cost given in. Though, the disturbance given by can make the learning hard for the controller, it need not have a smaller magnitude for a given $\gamma > 0$ and ${\{\theta_{f,k}\}}_{f = 1}^{\mathcal{F}}$, and hence it may *not* lead to the worse cost. Further, for certain range of ${\{\theta_{f,k}\}}_{f = 1}^{\mathcal{F}}$, the associated closed loop system may turn out to be unstable. The negative result formulated in Theorem 1 justifies further analysis on the sub-optimality faced by the minimax adaptive controller, which is studied in the next sections through the concept of regret.

### Regret Definitions

Note that each model ${(A_{i},B_{i})} \in \mathcal{M}$ suffers different regret when compared against the optimal $\mathcal{H}_{\infty}$ controller in hindsight. Hence, we quantify the regret of each model in the set $\mathcal{M}$ in the following definition.

### Definition 2

Given a model ${M_{i}:={(A_{i},B_{i})} \in \mathcal{M}},{i \in {\{ 1,\ldots,\mathcal{F}\}}}$, we define the model-based regret of the minimax adaptive control policy $\pi^{\dagger} \in \Pi$ with respect to the optimal control policy $\pi_{i}^{\star}$ for $\gamma \geq \gamma^{\dagger} > \gamma_{i}^{\star}$ and time $T \in {\mathbb{N}}$ as

Any disturbance that is not in the $\ell_{2e}$ space will result in diverging states. We note that the choice of regret metric is not conventional, as the standard approach would be to define it as difference of costs, that is,

While captures how close the systems controlled by the minimax adaptive controller and the optimal $\mathcal{H}_{\infty}$ controller in hindsight are in terms of the performance, it does not provide information on how close the two state and inputs trajectories are. Further, cannot account for the direction of the control input being applied to the system. For these reasons, we propose to use as the definition of model-based regret in this work. Note that the model-based regret in is a function of the chosen level of robustness $\gamma$ because this parameter affects the two policies $\pi^{\dagger}$ and $\pi_{i}^{\star}$ (this dependence is omitted for the sake of clarity). The regret is defined for $\gamma \geq \gamma^{\dagger} > \gamma_{i}^{\star}$ to ensure that a fair comparison is made between the resulting trajectories from controllers that share the same level of disturbance attenuation capabilities. To compute, we need to characterize the trajectories of the system $x_{k}^{\pi^{\dagger}}$ and $x_{k}^{\pi_{i}^{\star}}$ given by under the same sequence of adversarial disturbance inputs affecting the system using the control policies $\pi^{\dagger}$ and $\pi_{i}^{\star}$ respectively. This naturally leads us to investigate what would be the worst-case model-based regret corresponding to any arbitrary model $M_{i} \in \mathcal{M}$, i.e., the total regret.

### Definition 3

The total regret of the minimax adaptive controller is defined as

While comparing policies, it is important to compare their disturbance attenuation levels too. Sub-optimality gap indicates a room for improvement in terms of the robustness. Since, minimax adaptive controller can never match the $\mathcal{H}_{\infty}$ controller, the difference in their disturbance attenuation level is referred as the *model-based sub-optimality gap*.

### Definition 4

Given a model ${{(A_{i},B_{i})} \in \mathcal{M}},{i \in {\{ 1,\ldots,\mathcal{F}\}}}$, the model-based sub-optimality gap of the minimax adaptive control policy $\pi^{\dagger}$ is defined as

The model-based sub-optimality gap satisfies by definition ${\mathcal{O}{(\pi^{\dagger},\pi_{i}^{\star})}} \geq 0$ and characterizes how the lack of knowledge about the QIs results in a worst disturbance attentuation level of the minimax adaptive controller (or reduction in robust performance). In a similar spirit to the definition of total regret, we define below the minimal and the maximal sub-optimality gaps, which are by definition both non-negative.

### Definition 5

The minimal sub-optimality gap and the maximal sub-optimality gap of the minimax adaptive control policy $\pi^{\dagger}$ are respectively defined as

### Study of Minimax Adaptive Control Regret

The following theorem establishes the asymptotic behaviour of the total regret associated with the minimax adaptive control policy $\Re{({\overline{\pi}}^{\dagger},T)}$.

### Theorem 2

Consider the uncertain linear dynamical system given by with the uncertainty described by $\mathcal{M}$. If the disturbance signal is in $\ell_{2}$ space, then the associated total regret is sub-linear, i.e.

### Proof

Recall that both minimax adaptive control policy $\overline{\pi}$ given by (7a) and $\mathcal{H}_{\infty}$ control policy given by are stabilising (with exponential decay of states and controls) for any adversarial disturbance in $\ell_{2}$ space. That is, given any disturbance signal $w_{k}$ in $\ell_{2}$ space for plant model $i \in {\{ 1,\ldots,\mathcal{F}\}}$, we have

Then, this means that ${\lim_{k\rightarrow\infty}\left. \parallel{x_{k}^{{\overline{\pi}}^{\dagger}} - x_{k}^{\pi_{i}^{\star}}}\parallel \right._{Q}^{2}} = 0$. Since at any time $k \in {\mathbb{N}}$ both minimax adaptive control input $u_{k}^{{\overline{\pi}}^{\dagger}}$ given by (7a) and the $\mathcal{H}_{\infty}$ control input $u_{k}^{\pi_{i}^{\star}}$ given by are functions of the states $x_{k}^{{\overline{\pi}}^{\dagger}}$ and $x_{k}^{\pi_{i}^{\star}}$ respectively that decay to zero asymptotically, we infer that

Then, this means that ${\lim_{k\rightarrow\infty}\left. \parallel{u_{k}^{{\overline{\pi}}^{\dagger}} - u_{k}^{\pi_{i}^{\star}}}\parallel \right._{R}^{2}} = 0$. Therefore, the difference term decays as well to zero meaning that ${\lim_{k\rightarrow\infty}{d_{k}{({\overline{\pi}}^{\dagger},\pi_{i}^{\star})}}} = 0$. Hence, the result follows. ∎

An insight gathered from the proof is that stability of the policy implies certain regret properties. This has connections with recent findings in Karapetyan et al. which studied the relationship between stability and regret for disturbances in $\ell_{\infty}$ space.

## Numerical Simulation

In this section, we exemplify our analysis using a linear dynamical system with a model uncertainty consisting of four different linear models.

(a) Minimax &amp; ℋ∞ States: $x_{k}^{{\overline{\pi}}^{\dagger}}$

(b) Minimax &amp; ℋ∞ Controls: xkπ2⋆

(c) Regret scaling vs time

Figure 1: Simulation results with states and controls from the minimax adaptive controller and the ℋ∞ controller are plotted here along with the corresponding regret scaling over time. Only the first state of the system is plotted for the demonstration purpose. Note that the quantities $\mathcal{R}{({\overline{\pi}}^{\dagger},\pi_{2}^{\star},T)}$ and $\frac{\mathcal{R}{({\overline{\pi}}^{\dagger},\pi_{2}^{\star},T)}}{T}$ are abbreviated as ℛ and $\overset{\sim}{\mathcal{R}}$ respectively. The text in the subscript of quantities in all sub-plots denotes the type of disturbance being used.

### Problem Setup

We consider the following numerical example of a linear dynamical system with four possible models. The state and control penalty matrices were ${Q = I_{3}},{R = 1}$ and $T = 50$. We simulated the system using the minimax adaptive controller and the $\mathcal{H}_{\infty}$ controller available in hindsight separately when the pair $(A_{2},B_{2})$ (corresponds to $j = 2$ as per Theorem 1) was the true model.

Three different disturbances constructions were used

worst case disturbance signal obtained from the dynamic game based $\mathcal{H}_{\infty}$ approach given by.

sinusoidal disturbance with unit amplitude and its frequency being selected as the frequency where the $\mathcal{H}_{\infty}$ norm of $T_{d\rightarrow\zeta}{\lbrack K\rbrack}{(z)}$ given by was maximum.

the disturbance given by used in the proof of Theorem 1 with $i = 3$ and tuned so that the controller always choose the optimal controller for $(A_{3},B_{3})$.

The gains for the sub-optimal minimax adaptive controller were calculated using the method from Cederberg et al. which is an improved version of Theorem 3 in Rantzer and we used the Yalmip toolbox with the MOSEK solver to solve the associated convex optimization problem with linear matrix inequality constraints. The code corresponding to the figures given in the paper is made publicly available at [https://github.com/venkatramanrenganathan/minimaxadaptivecontrolregret](https://github.com/venkatramanrenganathan/minimaxadaptivecontrolregret).

### Results & Discussions

The system dynamics with ${\{{(A_{i},B_{i})}\}}_{i = 1}^{4}$ given by was solved for the minimax adaptive control policy $\overline{\pi}$ to get ${\overline{\gamma}}^{\dagger} = 31.0086$. Then, the corresponding $\mathcal{H}_{\infty}$ controller was obtained using $\gamma = {\overline{\gamma}}^{\dagger}$. The optimal $\ell_{2}$ gains, namely ${\{\gamma_{i}^{\star}\}}_{i = 1}^{4}$ corresponding to the optimal $\mathcal{H}_{\infty}$ controller for the plants ${\{{(A_{i},B_{i})}\}}_{i = 1}^{4}$ were $1.266,4.544,2.913,2.298$ respectively. The model-based sub-optimality gaps were found using as ${\mathcal{O}{({\overline{\pi}}^{\dagger},\pi_{1}^{\star})}} = 29.7426$, ${\mathcal{O}{({\overline{\pi}}^{\dagger},\pi_{2}^{\star})}} = 26.4646$, ${\mathcal{O}{({\overline{\pi}}^{\dagger},\pi_{3}^{\star})}} = 28.0956$, and ${\mathcal{O}{({\overline{\pi}}^{\dagger},\pi_{4}^{\star})}} = 28.7106$. Further, the minimal and maximal sub-optimality gaps were ${\underset{¯}{\mathcal{O}}{({\overline{\pi}}^{\dagger})}} = 26.4646$ and ${\overline{\mathcal{O}}{({\overline{\pi}}^{\dagger})}} = 29.7426$ respectively.

The results of simulating system with minimax adaptive controller and $\mathcal{H}_{\infty}$ controller with three different disturbance strategies are shown in Figure 1. The sub-figures 1(a), and 1(b) depict the difference of states and inputs respectively from the minimax adaptive controller and the $\mathcal{H}_{\infty}$ controller and precisely these are the main contributing factors of regret as per. The regret quantities $\mathcal{R}{({\overline{\pi}}^{\dagger},\pi_{2}^{\star},T)}$ and $\frac{\mathcal{R}{({\overline{\pi}}^{\dagger},\pi_{2}^{\star},T)}}{T}$ are abbreviated as $\mathcal{R}$ and $\overset{\sim}{\mathcal{R}}$ respectively are plotted in the sub-figure 1(c). When adversarial disturbance constructed from the worst case disturbance policy given by was used, the associated regret was bounded as seen in sub-figure 1(c). Moreover, the shown results fulfils as both the control policies were stabilising and the disturbance was regulated to zero as it was a linear function of the system states (as per ) which decayed in exponential time. When a sinusoidal disturbance with unit amplitude was employed with its frequency being selected as the frequency where the $\mathcal{H}_{\infty}$ norm of $T_{d\rightarrow\zeta}{\lbrack K\rbrack}{(z)}$ given by was maximum (for $(A_{2},B_{2})$ this happens at ${\pi{rad}}/s$), the regret was not bounded anymore as the sinusoidal disturbance does not belong to the $\ell_{2}$ space. However, the ratio namely ${\mathcal{R}{({\overline{\pi}}^{\dagger},\pi_{2}^{\star},T)}}/T$ went to zero asymptotically as the terms contributing to the regret namely the differences of states and controls remained small and did grow slower than linearly. When the disturbance given by was used, it ensured that the $l_{k}$ value chosen by the minimax adaptive control policy ${\overline{\pi}}^{\dagger}$ according to (7b) was never equal to ${j = 2},{{\forall k} \in {\lbrack 0,T\rbrack}}$. Even though the ratio ${\mathcal{R}{({\overline{\pi}}^{\dagger},\pi_{2}^{\star},T)}}/T$ went to zero asymptotically as disturbance was still a function of exponentially decaying states, it can be observed that the disturbance signal had a larger magnitude than the one from. This shows that the disturbance that hardens the learning process need not necessarily worsen the performance as measured by because it results in a decrease of the total cost.

## Conclusion

An online learning-inspired analysis for a recently proposed solution for a class of minimax adaptive control problems has been presented. Model-based regret and total regret for the minimax adaptive control policy were defined by comparing the state and input trajectories against that of the optimal $\mathcal{H}_{\infty}$ controller in hindsight (i.e. having knowledge of the true system dynamics). One of the highlights of the analysis is that the total regret is sub-linear for exogenous disturbances in the $\ell_{2}$ space, confirming links between system theoretic properties and regret for control systems. Future research will seek to characterize transient properties of regret, and their connections with the exploration-exploitation trade-off inherently captured by the minimax adaptive control algorithms. Starting from the definitions of regret proposed here, designing regret-optimal adaptive controllers that lower the conservatism of minimax solutions is also an important research question lying ahead.
