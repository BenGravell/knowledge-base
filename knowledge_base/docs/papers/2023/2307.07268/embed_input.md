<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

An Online Learning Analysis of Minimax Adaptive Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present an online learning analysis of minimax adaptive control for the case where the uncertainty includes a finite set of linear dynamical systems. Precisely, for each system inside the uncertainty set, we define the model-based regret by comparing the state and input trajectories from the minimax adaptive controller against that of an optimal controller in hindsight that knows the true dynamics. We then define the total regret as the worst case model-based regret with respect to all models in the considered uncertainty set. We study how the total regret accumulates over time and its effect on the adaptation mechanism employed by the controller. Moreover, we investigate the effect of the disturbance on the growth of the regret over time and draw connections between robustness of the controller and the associated regret rate.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The interplay between machine learning, system identification and adaptive control has unveiled a fertile area of research which has the potential to answer some of the standing research questions in the field of learning-based control. Recent advances in online learning techniques have provided new perspectives on the design of algorithms where unknown systems can be controlled by acquiring knowledge through repeated interactions with the unknown environment Hazan & Singh. This has close connections with adaptive control Astrom & Wittenmark and in general with learning-based control techniques Benosman. Minimax adaptive control is taken in this work as a prototypical example of the latter line of works to draw connections with regret, i.e. the performance metrics used in online learning. Design of minimax control for uncertain systems was investigated as early as in Salmon; Didinsky & Basar. Subsequently, the design of minimax adaptive control was investigated for scalar systems with unknown input matrix sign in Rantzer, for finite sets of linear systems in Rantzer; Cederberg et al. and for the output feedback case in Kjellqvist & Rantzer, respectively. There have been earlier works on robust adaptive control in Chichka & Speyer; Yoneyama et al. where uncertainties in system dynamics were considered.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Minimax adaptive control problems are generally challenging as obtaining exact $\ell_{2}$-gain bounds as explained in French & Trenn; Vinnicombe; Rantzer can be hard for multiple input multiple outputs systems with finite set of linear models and optimality can only be achieved if the exploration and exploitation trade-off is exactly captured.\
The recent interest developed towards analyzing control algorithms for systems with unknown dynamics through the lens of regret analysis has the promise to enable a better understanding of this trade-off. There are quantities that are of interest but are unknown in advance to the online controller. We refer to such unknown entity as *Quantity of Interest (QI)*. Lack of knowledge about a QI determines an accumulated cost, with respect to a control designed with perfect knowledge, which denotes the notion of regret. For instance, the growth of expected regret in linear quadratic control was investigated in Jedra & Proutiere when matrices $(A,B)$ were unknown. Regret bounds have been investigated in Boffi et al. for adaptive control problems in stochastic setting.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper proposes an online learning analysis of minimax adaptive control of linear-time invariant systems featuring adversarial disturbance and a priori knowledge of a finite set of systems. One of the distinctive novelty is a new definition of regret, suitable for this setting in which the QIs are both the system dynamics and the exogenous disturbance. From an online learning perspective, efficient adaptive control algorithms are characterized by limiting the growth of regret over time. To quantify the regret, we usually require an optimal control policy (policy regret) or a sequence of best control actions (dynamic regret) available in hindsight as in Goel & Hassibi. Here, we propose studying the policy regret associated with the minimax adaptive controller by comparing it against the standard $\mathcal{H}_{\infty}$ control which knows the dynamics.\
Recently, Karapetyan et al. investigated the regret of robustness of an $\mathcal{H}_{\infty}$ controller (whose QI is just the adversarial disturbance) when compared to an oracle controller which has knowledge of the future disturbance trajectory.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Also related is the work in Hazan et al., which investigated the regret analysis for the generic non-stochastic control problem and their system identification approach employed random inputs before controlling it using disturbance-based policy. Similarly, Agarwal et al. studied online control with adversarial disturbances and proposed a disturbance action control policy based efficient algorithm to obtain nearly tight regret bounds. On the contrary, our work looks at nonlinear adaptive state feedback policy which *concurrently* controls the system under adversarial disturbance and implicitly learns the system dynamics. This gives rise to an interesting trade-off in the adversary strategy, whereby the worst-case disturbance is the one that delays the learning process of the controller while minimizing the energy spent (which is penalized in the total cost).\

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide a detailed analysis for the minimax adaptive control algorithm proposed in Rantzer with the aim to improve our understanding on the role of the adaptation mechanism and the adversary disturbance on the regret. Since an explicit expression for the optimal minimax adaptive controller is not known, we apply our analysis to the candidate sub-optimal minimax adaptive control algorithm^11^1The distinction between the optimal and the sub-optimal minimax adaptive control policies will be made clear at appropriate places. developed in Rantzer; Cederberg et al..

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Definition of the: model-based regret corresponding to a specific model in the uncertainty set characterizing the accumulated cost with respect to an optimal controller in hindsight which knows the true dynamics; total regret as the worst-case model-based regret corresponding to any model in the uncertainty set.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Construction of an adversarial disturbance policy which provably prevents the minimax adaptive controller from learning the true dynamics (Theorem 1).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite the possible difficulty in the identification of the true dynamics, we show that the minimax adaptive controller enjoys a sub-linear regret rate with respect to the best $\mathcal{H}_{\infty}$ controller in hindsight (Theorem 2).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper is organised as follows. The problem formulation is discussed in §2. The online learning analysis is performed in §3, and some of its features are further elucidated through numerical simulation in §4. Finally, the main findings of the paper are summarized in §5.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Formulation Using Minimax Adaptive Control", "weight": 1.0} -->

In this section we introduce the minimax adaptive control subject of our investigations through online learning.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Minimax adaptive control with finite set of linear systems", "weight": 1.0} -->

Consider the following discrete-time linear system

<!-- chunk {"id": "body-0014", "role": "body", "section": "Minimax adaptive control with finite set of linear systems", "weight": 1.0} -->

For instance, control of a discrete-time linearized inverted pendulum dynamics falls under the above setting when the pendulum length is uncertain. Generally, minimax adaptive control approach can be a suitable design solution when multiple systems who do not share common Lyapunov function need to be controlled by a single controller. Let us denote by $\Pi$ the set of admissible control policies such that

<!-- chunk {"id": "body-0015", "role": "body", "section": "Minimax adaptive control with finite set of linear systems", "weight": 1.0} -->

An optimal adaptive control policy should interact with the system in order to extract information about the unknown system matrices $A,B$ while also guaranteeing good performance and robustness to the adversarial disturbance. This can be achieved by optimizing the following minimax cost

<!-- chunk {"id": "body-0016", "role": "body", "section": "Minimax adaptive control with finite set of linear systems", "weight": 1.0} -->

where ${c{(x^{\pi},u^{\pi},Q,R)}}:={\left. \parallel x^{\pi}\parallel \right._{Q}^{2} + \left. \parallel u^{\pi}\parallel \right._{R}^{2}}$ for given penalty matrices ${Q \succ 0},{R \succ 0}$; $x^{\pi}$ denotes the evolution of the state of starting from $x_{0}$ under the control input $u^{\pi}$ from the policy $\pi$; and $\gamma > 0$ quantifies the desired level of robustness to the external disturbance (higher $\gamma$ resulting in weaker robustness requirements). The optimal minimax control policy $\pi^{\dagger}$ and the associated cost are given by

<!-- chunk {"id": "body-0017", "role": "body", "section": "Minimax adaptive control with finite set of linear systems", "weight": 1.0} -->

and the resulting disturbance attenuation level achieved by the control policy $\pi^{\dagger}$ from disturbance to the regulated output $\zeta:=\begin{bmatrix}
\end{bmatrix}^{\top}$ is denoted by $\gamma^{\dagger}$ and is defined as

<!-- chunk {"id": "body-0018", "role": "body", "section": "Minimax adaptive control with finite set of linear systems", "weight": 1.0} -->

This formulation provides a family of minimax control policy parameterized by $\gamma$, which are guaranteed to exist ${\forall\gamma} > \gamma^{\dagger}$. We cast the problem as a zero-sum dynamic game with the control policy $\pi$ being the minimizing player and the adversaries $(w,A,B)$ being the maximizing players Rantzer. The solution boils down to solving a minimax dynamic programming problem, which is intractable in most cases. An approximate (i.e. sub-optimal) solution has been recently proposed in Rantzer; Cederberg et al., and this will be the subject of this study. The following lemma summarizes the main result of Rantzer, i.e. an explicit expression for an adaptive controller satisfying a pre-specified $\ell_{2}$-gain bound from disturbance to error.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Known Dynamics Case: Standard $\\mathcal{H}_{\\infty}$ Control", "weight": 1.0} -->

When the system matrices $A,B$ are known, problem reduces to the standard $\mathcal{H}_{\infty}$ control. That is, a control input ${u = {Kx}},{K \in {\mathbb{R}}^{m \times n}}$ is sought such that it minimizes the $\mathcal{H}_{\infty}$ norm of the closed loop system from $d$ to $\zeta$

<!-- chunk {"id": "body-0020", "role": "body", "section": "Known Dynamics Case: Standard $\\mathcal{H}_{\\infty}$ Control", "weight": 1.0} -->

where $T_{d\rightarrow\zeta}$ is related to the cost function in by appropriate choice of matrices $Q,R$. Using this observation, we define for every system model $M_{i}:={(A_{i},B_{i})} \in \mathcal{M}$, the associated $\mathcal{H}_{\infty}$ control policy $\pi_{i}^{\star} \in \Pi$, which can be found by solving the coupled Riccati equations below Başar & Bernhard

<!-- chunk {"id": "body-0021", "role": "body", "section": "Known Dynamics Case: Standard $\\mathcal{H}_{\\infty}$ Control", "weight": 1.0} -->

The dynamic game has an unique saddle point solution

<!-- chunk {"id": "body-0022", "role": "body", "section": "Known Dynamics Case: Standard $\\mathcal{H}_{\\infty}$ Control", "weight": 1.0} -->

denotes the corresponding worst-case $\ell_{2}$ gain from the disturbance to the regulated output for the model ${M_{i},i} \in \mathcal{M}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Regret of Minimax Adaptive Control", "weight": 1.0} -->

Regret analysis compares the performance of an online algorithm that takes decisions in the presence of uncertainty with respect to a clairvoyant policy with hindsight knowledge. For this reason, it is used here in order to better understand the performance achieved when controlling the system using minimax adaptive control algorithm.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Adversarial disturbance strategies for minimax control", "weight": 1.0} -->

The key adaptive mechanism of policy $\overline{\pi}$ in can be interpreted as an implicit identification of the underlying plant. It is then natural to ask whether this is provably able to eventually converge to the correct estimate for the system. The following theorem gives a negative answer by constructing an adversarial disturbance strategy preventing the controller from optimally controlling the true system.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Regret Definitions", "weight": 1.0} -->

Note that each model ${(A_{i},B_{i})} \in \mathcal{M}$ suffers different regret when compared against the optimal $\mathcal{H}_{\infty}$ controller in hindsight. Hence, we quantify the regret of each model in the set $\mathcal{M}$ in the following definition.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Study of Minimax Adaptive Control Regret", "weight": 1.0} -->

The following theorem establishes the asymptotic behaviour of the total regret associated with the minimax adaptive control policy $\Re{({\overline{\pi}}^{\dagger},T)}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Numerical Simulation", "weight": 1.0} -->

In this section, we exemplify our analysis using a linear dynamical system with a model uncertainty consisting of four different linear models.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

We consider the following numerical example of a linear dynamical system with four possible models. The state and control penalty matrices were ${Q = I_{3}},{R = 1}$ and $T = 50$. We simulated the system using the minimax adaptive controller and the $\mathcal{H}_{\infty}$ controller available in hindsight separately when the pair $(A_{2},B_{2})$ (corresponds to $j = 2$ as per Theorem 1) was the true model.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

Three different disturbances constructions were used

<!-- chunk {"id": "body-0030", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

worst case disturbance signal obtained from the dynamic game based $\mathcal{H}_{\infty}$ approach given.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

sinusoidal disturbance with unit amplitude and its frequency being selected as the frequency where the $\mathcal{H}_{\infty}$ norm of $T_{d\rightarrow\zeta}{\lbrack K\rbrack}{(z)}$ given by was maximum.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

the disturbance given by used in the proof of Theorem 1 with $i = 3$ and tuned so that the controller always choose the optimal controller for $(A_{3},B_{3})$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

The gains for the sub-optimal minimax adaptive controller were calculated using the method from Cederberg et al. which is an improved version of Theorem 3 in Rantzer and we used the Yalmip toolbox with the MOSEK solver to solve the associated convex optimization problem with linear matrix inequality constraints. The code corresponding to the figures given in the paper is made publicly available at

<!-- chunk {"id": "body-0034", "role": "body", "section": "Results & Discussions", "weight": 1.0} -->

The results of simulating system with minimax adaptive controller and $\mathcal{H}_{\infty}$ controller with three different disturbance strategies are shown in Figure 1. The sub-figures 1(a), and 1(b) depict the difference of states and inputs respectively from the minimax adaptive controller and the $\mathcal{H}_{\infty}$ controller and precisely these are the main contributing factors of regret as per. The regret quantities $\mathcal{R}{({\overline{\pi}}^{\dagger},\pi_{2}^{\star},T)}$ and $\frac{\mathcal{R}{({\overline{\pi}}^{\dagger},\pi_{2}^{\star},T)}}{T}$ are abbreviated as $\mathcal{R}$ and $\overset{\sim}{\mathcal{R}}$ respectively are plotted in the sub-figure 1(c).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Results & Discussions", "weight": 1.0} -->

When adversarial disturbance constructed from the worst case disturbance policy given by was used, the associated regret was bounded as seen in sub-figure 1(c). Moreover, the shown results fulfils as both the control policies were stabilising and the disturbance was regulated to zero as it was a linear function of the system states (as per ) which decayed in exponential time. When a sinusoidal disturbance with unit amplitude was employed with its frequency being selected as the frequency where the $\mathcal{H}_{\infty}$ norm of $T_{d\rightarrow\zeta}{\lbrack K\rbrack}{(z)}$ given by was maximum (for $(A_{2},B_{2})$ this happens at ${\pi{rad}}/s$), the regret was not bounded anymore as the sinusoidal disturbance does not belong to the $\ell_{2}$ space.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Results & Discussions", "weight": 1.0} -->

However, the ratio namely ${\mathcal{R}{({\overline{\pi}}^{\dagger},\pi_{2}^{\star},T)}}/T$ went to zero asymptotically as the terms contributing to the regret namely the differences of states and controls remained small and did grow slower than linearly. When the disturbance given by was used, it ensured that the $l_{k}$ value chosen by the minimax adaptive control policy ${\overline{\pi}}^{\dagger}$ according to (7b) was never equal to ${j = 2},{{\forall k} \in {\lbrack 0,T\rbrack}}$. Even though the ratio ${\mathcal{R}{({\overline{\pi}}^{\dagger},\pi_{2}^{\star},T)}}/T$ went to zero asymptotically as disturbance was still a function of exponentially decaying states, it can be observed that the disturbance signal had a larger magnitude than the one.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Results & Discussions", "weight": 1.0} -->

This shows that the disturbance that hardens the learning process need not necessarily worsen the performance as measured by because it results in a decrease of the total cost.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conclusion", "weight": 1.5} -->

An online learning-inspired analysis for a recently proposed solution for a class of minimax adaptive control problems has been presented. Model-based regret and total regret for the minimax adaptive control policy were defined by comparing the state and input trajectories against that of the optimal $\mathcal{H}_{\infty}$ controller in hindsight (i.e. having knowledge of the true system dynamics). One of the highlights of the analysis is that the total regret is sub-linear for exogenous disturbances in the $\ell_{2}$ space, confirming links between system theoretic properties and regret for control systems. Future research will seek to characterize transient properties of regret, and their connections with the exploration-exploitation trade-off inherently captured by the minimax adaptive control algorithms. Starting from the definitions of regret proposed here, designing regret-optimal adaptive controllers that lower the conservatism of minimax solutions is also an important research question lying ahead.
