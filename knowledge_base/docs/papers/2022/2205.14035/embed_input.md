<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning to Control Linear Systems Can Be Hard

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we study the statistical difficulty of learning to control linear systems. We focus on two standard benchmarks, the sample complexity of stabilization, and the regret of the online learning of the Linear Quadratic Regulator (LQR). Prior results state that the statistical difficulty for both benchmarks scales polynomially with the system state dimension up to system-theoretic quantities. However, this does not reveal the whole picture. By utilizing minimax lower bounds for both benchmarks, we prove that there exist non-trivial classes of systems for which learning complexity scales dramatically, i.e. exponentially, with the system dimension. This situation arises in the case of underactuated systems, i.e. systems with fewer inputs than states. Such systems are structurally difficult to control and their system theoretic quantities can scale exponentially with the system dimension dominating learning complexity. Under some additional structural assumptions (bounding systems away from uncontrollability), we provide qualitatively matching upper bounds. We prove that learning complexity can be at most exponential with the controllability index of the system, that is the degree of underactuation.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In stochastic linear control, the goal is to design a controller for a system of the form where $x_{k} \in {\mathbb{R}}^{n}$ is the system internal state, $u_{k} \in {\mathbb{R}}^{p}$ is some exogenous input, and $w_{k} \in {\mathbb{R}}^{r}$ is some random disturbance sequence. Matrices $A,B,H$ determine the evolution of the state, based on the previous state, control input, and disturbance respectively. Control theory has a long history of studying how to design controllers for system when its model is *known*. However, in reality system might be *unknown* and we might not have access to its model. In this case, we have to learn how to control based on data.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Controlling unknown dynamical systems has also been studied from the perspective of Reinforcement Learning (RL). Although the setting of tabular RL is relatively well-understood, it has been challenging to analyze the continuous setting, where the state and/or action spaces are infinite. Recently, there has been renewed interest in learning to control linear systems. Indeed, linear systems are simple enough to allow for an in-depth theoretical analysis, yet exhibit sufficiently rich behavior so that we can draw conclusions about continuous control of more general system classes. In this paper we focus on the following two problems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Regret of online LQR. A fundamental benchmark for continuous control is the Linear Quadratic Regulator (LQR) problem, where the goal is to compute a policy ^11^1A policy decides the current control input $u_{t}$ based on past state-input values --see Section 2 for details. $\pi$ that minimizes where $Q \in {\mathbb{R}}^{n \times n}$, $R \in {\mathbb{R}}^{p \times p}$ are the state and input penalties respectively; these penalties control the tradeoff between state regulation and control effort. When model is known, LQR enjoys a closed-form solution; the optimal policy is a linear feedback law ${\pi_{\star,t}{(x_{t})}} = {K_{\star}x_{t}}$, where the control gain $K_{\star}$ is given by solving the celebrated Algebraic Riccati Equation (ARE). If model is unknown, we have to learn the optimal policy from data.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the online learning setting, the goal of the learner is to find a policy that adapts online and competes with the optimal LQR policy that has access to the true model. The suboptimality of the online learning policy at time $T$ is captured by the *regret* The learning task is to find a policy with as small regret as possible.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Sample Complexity of Stabilization Another important benchmark is the problem of stabilization from data. The goal is to learn a linear gain $K \in {\mathbb{R}}^{m \times n}$ such that the closed-loop system $A + {BK}$ is stable, i.e., such that its spectral radius $\rho{({A + {BK}})}$ is less than one. Many algorithms for online LQR require the existence of such a stabilizing gain to initialize the online learning policy. Furthermore, stabilization is a problem of independent interest. In this setting, the learner designs an exploration policy $\pi$ and an algorithm that uses batch state-input data $x_{0},\ldots,x_{N},u_{0},\ldots,u_{N - 1}$ to output a control gain ${\hat{K}}_{N}$, at the end of the exploration phase. Here we focus on *sample complexity*, i.e., the minimum number of samples $N$ required to find a stabilizing gain.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since the seminal papers by Abbasi-Yadkori and Szepesvári and Dean et al. both LQR and stabilization have been studied extensively in the literature -- see Section 1.1. Current state-of-the-art results state that the regret of online LQR and the sample complexity of stabilization scale at most polynomially with system dimension $n$ where $C_{1}^{sys},C_{2}^{sys}$ are system specific constants that depend on several control theoretic quantities of system. However, the above statements might not reveal the whole picture.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In fact, system theoretic parameters $C_{1}^{sys},C_{2}^{sys}$ can actually hide dimensional dependence on $n$. This dependence has been overlooked in prior work. As we show in this paper, there exist non-trivial classes of linear systems for which system theoretic parameters scale dramatically, i.e. exponentially, with the dimension $n$. As a result, the system theoretic quantities $C_{1}^{sys},C_{2}^{sys}$ might be very large and in fact *dominate* the ${poly}{(n)}$ term in the upper bounds. This phenomenon especially arises in systems which are structurally difficult to control, such as for example underactuated systems. Then, the upper bounds suggest that learning might be difficult for such instances. This brings up the following questions. *Can learning LQR or stabilizing controllers indeed be hard for such systems? How does system structure affect difficulty of learning?* To answer the first question, we need to establish lower bounds.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

As we discuss in Section 1.1, existing lower bounds for online LQR might not always reveal the dependence on control theoretic parameters. Chen and Hazan provided exponential lower bounds for the start-up regret of stabilization. Still, to the best of our knowledge, there are no existing lower bounds for the *sample complexity* of stabilization. Recently, it was shown that the sample complexity of system identification can grow exponentially with the dimension $n$. However, it is not clear if difficulty of identification translates into difficulty of control. Besides, we do not always need to identify the whole system in order to control it. To answer the second question, we need to provide upper bounds for several control theoretic parameters. Our contributions are the following: Exp($n$) Stabilization Lower Bounds. We prove an information-theoretic lower bound for the problem of learning stabilizing controllers, showing that it can indeed be statistically hard for underactuated systems. In particular, we show that the sample complexity of stabilizing an unknown underactuated linear system can scale exponentially with the state dimension $n$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

To the best of our knowledge this is the first paper to address this issue and consider lower bounds in this setting.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Exp($n$) LQR Regret Lower Bounds. We show that the regret of online LQR can scale exponentially with the dimension as ${\exp{(n)}}\sqrt{T}$. In fact, even common integrator-like systems can exhibit this behavior. To prove our result, we leverage recent regret lower bounds, which provide a refined analysis linking regret to system theoretic parameters. Chen and Hazan first showed that the start-up cost of the regret (terms of low order) can scale exponentially with $n$. Here, we show that this exponential dependence can also affect multiplicatively the dominant $\sqrt{T}$ term.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Exponential Upper Bounds. Under some additional structural assumptions (bounding systems away from uncontrollability), we provide matching global upper bounds. We show that the sample complexity of stabilization and the regret of online LQR can be at most exponential with the dimension $n$. In fact, we prove a stronger result, that they can be at most exponential with the *controllability index* of the system, which captures the structural difficulty of control -- see Section 3. This implies that if the controllability index is small with respect to the dimension $n$, then learning is guaranteed to be easy.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

System is characterized by the matrices ${A \in {\mathbb{R}}^{n \times n}},{{B \in {\mathbb{R}}^{n \times p}},{H \in {\mathbb{R}}^{n \times r}}}$. We assume that $w_{k} \sim {\mathcal{N}{(0,I_{r})}}$ is i.i.d. Gaussian with unit covariance. Without loss of generality the initial state is assumed to be zero $x_{0} = 0$. In a departure from prior work, we do not necessarily assume that the noise is isotropic. Instead, we consider a more general model, where the noise $Hw_{k}$ is allowed to be degenerate--see also Remark 1. ‣ 4 Difficulty of Stabilization ‣ Learning to Control Linear Systems can be Hard").

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Matrices $A,B,H$ and the noise dimension $r \leq n$ are all unknown. The unknown matrices are bounded, i.e. ${{\| A\|}_{2},{\| B\|}_{2},{\| H\|}_{2}} \leq M$, for some positive constant $M \geq 1$. Matrices $B,H$ have full column rank ${{rank}{(B)}} = p \leq n$, ${{rank}{(H)}} = r \leq n$. We also assume that the system is non-explosive ${\rho{(A)}} \leq 1$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The boundedness assumption on the state parameters allows us to argue about global sample complexity upper bounds. To simplify the presentation, we make the assumption that the system is non-explosive ${\rho{(A)}} \leq 1$. This setting includes marginally stable systems and is rich enough to provide insights about the difficulty of learning more general systems.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Let ${\mathbb{P}}_{S,\pi}$ (${\mathbb{E}}_{S,\pi}{( \cdot )}$) denote the probability distribution (expectation) of the input-state data when the true system is equal to $S$ and we apply a policy $\pi$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Difficulty of Stabilization", "weight": 1.0} -->

In the stabilization problem, the goal is to find a state-feedback control law $u = {Kx}$, where $K$ renders the closed-loop system $A + {BK}$ stable with spectral radius less than one, i.e., ${\rho{({A + {BK}})}} < 1$. We assume that we collect data $x_{0},\ldots,x_{N},u_{0},\ldots,u_{N}$, which are generated by system using any exploration policy $\pi$, e.g. white-noise excitation, active learning etc. Since we care only about sample complexity, the policy is allowed to be maximally exploratory. To make the problem meaningful, we restrict the average control energy.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Next, we define a notion of learning difficulty for classes of linear systems. By $\mathcal{C}_{n}$ we will denote a class of systems with dimension $n$. We will define as easy, classes of linear system that exhibit ${poly}{(n)}$ sample complexity.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem 1", "weight": 1.0} -->

Are there linear system classes which are not ${poly}{(n)}$-stabilizable? When can we guarantee ${poly}{(n)}$-stabilizability?

<!-- chunk {"id": "body-0021", "role": "body", "section": "Difficulty of Online LQR", "weight": 1.0} -->

Consider the LQR objective. Let the state penalty matrix $Q \in {\mathbb{R}}^{n \times n} \succ 0$ be positive definite, with the input penalty matrix $R \in {\mathbb{R}}^{p \times p}$ also positive definite. When the model is known, the optimal policy is a linear feedback law $\pi_{\star} = \left\{ {K_{\star}x_{k}} \right\}_{k = 0}^{T - 1}$, where $K_{\star}$ is given by and $P$ is the unique positive definite solution to the Algebraic Riccati Equation (ARE) Throughout the paper, we will assume that $Q_{T} = P$. If the model of is unknown, the goal of the learner is to find an online learning policy $\pi$ that leads to minimum regret $R_{T}{(S)}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Difficulty of Online LQR", "weight": 1.0} -->

In the setting of online LQR, the data are revealed sequentially, i.e. $x_{t + 1}$ is revealed after we select $u_{t}$. Contrary to the stabilization problem, here we study regret, i.e. there is a tradoff between exploration and exploitation. We will define a class-specific notion of learning difficulty based on the ratio between the regret and $\sqrt{T}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Problem 2", "weight": 1.0} -->

Are there classes of systems for which poly$(n)$-regret is impossible? When is poly$(n)$-regret guaranteed?

<!-- chunk {"id": "body-0024", "role": "body", "section": "Classes with Rich Controllability Structure", "weight": 1.0} -->

Before we present our learning guarantees, we need to find classes of systems, where learning is meaningful. To make sure that the stabilization and the LQR problems are well-defined, we assume that system is controllable^22^2We can slightly relax the condition to $(A,B)$ stabilizable. To avoid technicalities we leave that for future work..

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

System is $(A,B)$ *controllable*, i.e. matrix has full column rank ${{rank}{({\mathcal{C}_{k}{(A,B)}})}} = n$, for some $k \leq n$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

Unsurprisingly, the class of all controllable systems does not exhibit finite sample complexity/regret, let alone polynomial sample complexity/regret. The main issue is that there exist systems which satisfy the rank condition but are arbitrarily close to uncontrollability. For example, consider the following controllable system, which we want to stabilize The only way to stabilize the system is indirectly by using the second state $x_{k,2}$, via the coupling coefficient $\alpha$. However, we need to know the sign of $\alpha$. If $\alpha$ is allowed to be arbitrarily small, i.e. the system is arbitrarily close to uncontrollability, then an arbitrarily large number of samples is required to learn the sign of $\alpha$, leading to infinite complexity. To obtain classes with finite sample complexity/regret we need to bound the system instances away from uncontrollability.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

One way is to consider the least singular value of the controllability Gramian $\Gamma_{k}{(A,B)}$ at time $k$: An implicit assumption in prior literature is that ${\sigma_{\min}^{- 1}{({\Gamma_{k}{(A,B)}})}} \leq {{poly}{(n)}}$. We will not assume this here, since it might exclude many systems of interest, such as integrator-like systems, also known as underactuated systems, or networks. Instead, we will relax this requirement to allow richer system structures.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

To avoid pathologies, we will lower bound the coupling between states in the case of indirectly controlled systems. To formalize this idea, let us review some notions from system theory. The *controllability index* is defined as follows i.e., it is the minimum time such that the controllability rank condition is satisfied. It captures the degree of underactuation and reflects the structural difficulty of control.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

Based on the fact that the rank of the controllability matrix at time $\kappa$ is $n$, we can show that the pair $(A,B)$ admits the following canonical representation, under a unitary similarity transformation. It is called the Staircase or Hessenberg form of system.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Difficulty of Stabilization", "weight": 1.0} -->

In this section, we show that there exist non-trivial classes of linear systems for which the problem of stabilization from data is hard. In fact, the class of robustly coupled systems requires at least an exponential, in the state dimension $n$, number of samples.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 1 (Singular noise)", "weight": 1.0} -->

Our stabilization lower bound exploits the fact that the constructed system has low-rank noise, such that system identification is hard. It is an open problem whether we can construct examples of systems that are not ${{poly}{(n)}} -$stabilizable even though they are excited by full-rank noise. Nonetheless, in our regret lower bounds, we allow the noise to be full-rank.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Sample complexity upper bounds", "weight": 1.0} -->

As we show below, sample complexity cannot be worse than exponential under the assumption of robust coupling. If the exploration policy is a white noise input sequence, then using a least squares identification algorithm, and a robust control design scheme, the sample complexity can be upper bounded by a function which is at most exponential with the dimension $n$. In fact, we provide a more refined result, directly linking sample complexity to the controllability index $\kappa$. Our proof relies on bounding control theoretic quantities like the least singular value of the controllablility Gramian. The details of the proof and the algorithm can be found in Section D.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Difficulty of online LQR", "weight": 1.0} -->

In the following theorem, we prove that classes of robustly coupled systems can exhibit minimax expected regret which grows at least exponentially with the dimension $n$. Let $\mathcal{C}_{n,\kappa}^{\mu}$ denote the class of $\mu$-robustly coupled systems $S = {(A,B,H)}$ of state dimension $n$ and controllability index $\kappa$. Define the $\epsilon$-dilation $\mathcal{C}_{n,\kappa}^{\mu}{(\epsilon)}$ of $\mathcal{C}_{n,\kappa}^{\mu}$ as which consists of every system in $\mathcal{C}_{n,\kappa}^{\mu}$ along with its $\epsilon -$ball around it.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Sketch of Lower Bound Proof", "weight": 1.0} -->

Let $S_{0} = {(A_{0},B_{0},I_{n - 1})} \in \mathcal{C}_{{n - 1},\kappa}^{\mu}$ be a $\mu -$robustly coupled system of state dimension $n - 1$, input dimension $p - 1$ and controllability index $\kappa \leq {n - 1}$. Let $P_{0}$ be the solution of the Riccati equation for $Q_{0} = I_{n - 1}$, $R_{0} = I_{p - 1}$, with $K_{\star,0}$ the corresponding optimal gain. Define the steady-state covariance of the closed-loop system Now, consider the composite system: with ${Q = I_{n}},{R = I_{p}}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Sketch of Lower Bound Proof", "weight": 1.0} -->

Let $\Delta$ be structured as, for some arbitrary $\Delta_{1}$ of unit norm ${\|\Delta_{1}\|}_{2} = 1$. The Riccati matrix of the composite system is denoted by $P$ and the corresponding gain by $K_{\star}$. Consider the parameterization: for any $\theta \in {\mathbb{R}}$. Let $\mathcal{B}{(\theta,\epsilon)}$ denote the open Euclidean ball of radius $\epsilon$ around $\theta$. For every $\epsilon > 0$, define the local class of systems around $S$ as ${\mathcal{C}_{S}{(\epsilon)}} \triangleq \left\{ {{{({A{(\theta)}},{B{(\theta)}},I_{n})},\theta} \in {\mathcal{B}{(0,\epsilon)}}} \right\}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Sketch of Lower Bound Proof", "weight": 1.0} -->

Based on the above construction and Theorem 1 of Ziemann and Sandberg, a general information-theoretic regret lower bound, we prove the following lemma.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Regret Upper Bounds", "weight": 1.0} -->

Similar to the stabilization problem, we show that under the assumption of robust coupling, the regret cannot be worse than ${\exp{(\kappa)}}\sqrt{T}$ with high probability. As we prove in Lemma 3. ‣ Appendix B System Theoretic Bounds for Robustly Coupled Systems ‣ Learning to Control Linear Systems can be Hard"), the solution $P$ to the Riccati equation has norm ${\| P\|}_{2}$ that scales at most exponentially with the index $\kappa$ in the case of robustly-coupled systems. This result combined with the regret upper bounds of Simchowitz and Foster, give us the following result.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We prove that learning to control linear systems can be hard for non-trivial system classes. The problem of stabilization might require sample complexity which scales exponentially with the system dimension $n$. Similarly, online LQR might exhibit regret which scales exponentially with $n$. This difficulty arises in the case of underactuated systems. Such systems are structurally difficult to control; they can be very sensitive to inputs/noise or very hard to excite. If the system is robustly coupled and has a mild degree of underactuation (small controllability index), then we can guarantee that learning will be easy.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We stress that system theoretic quantities might not be dimensionless. On the contrary, they might grow very large with the dimension and dominate any poly$(n)$ terms. Hence, going forward, an important direction of future work is to find policies with optimal dependence on such system theoretic quantities. Although the optimal dependence is known for the problem of system identification, it is still not clear what is the optimal dependence in the case of control. For example, an interesting open problem is to find the optimal dependence of the regret $R_{T}$ on the Riccati equation solution $P$. For the problem of stabilization, it is open to find how sample complexity optimally scales with the least singular value of the controllability Gramian.
