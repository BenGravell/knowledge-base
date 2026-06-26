<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sub-optimality of the Separation Principle for Quadratic Control from Bilinear Observations

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider the problem of controlling a linear dynamical system from bilinear observations with minimal quadratic cost. Despite the similarity of this problem to standard linear quadratic Gaussian (LQG) control, we show that when the observation model is bilinear, neither does the Separation Principle hold, nor is the optimal controller affine in the estimated state. Moreover, the cost-to-go is non-convex in the control input. Hence, finding an analytical expression for the optimal feedback controller is difficult in general. Under certain settings, we show that the standard LQG controller locally maximizes the cost instead of minimizing it. Furthermore, the optimal controllers (derived analytically) are not unique and are nonlinear in the estimated state. We also introduce a notion of input-dependent observability and derive conditions under which the Kalman filter covariance remains bounded. We illustrate our theoretical results through numerical experiments in multiple synthetic settings.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In many engineering settings, measurements result from the interaction between a measurement device and an unknown quantity. Traditionally, the unknown quantity is assumed to be independent of the measurement process; however, in general it may be influenced by being measured. This "observer effect" is present in examples ranging from electronic circuits, where measurement devices can alter resistance or impedance, to robotics, where active perception requires interaction, and quantum systems, where measurement induces wavefunction collapse. Perhaps the simplest model which captures such interaction is a *bilinear* observation model, in which the output is a bilinear function of the control input and the unknown state. Recent works propose a dynamical system model with linear transitions and bilinear measurements, and study the system identification problem.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In such settings, control inputs both change the state and affect observation of it. How should controllers be designed to account for these dual roles? In this paper, we address this question for optimal control of a linear dynamical system with bilinear observations and quadratic costs. The bilinearity is a small departure from the standard partially observed linear quadratic problem (LQG), in which the optimal controller is known to obey the *Separation Principle*: it suffices to independently consider state estimation and a state feedback controller. Separation principle has also been shown to holds in several variants of LQG, e.g., when measurement and control are performed over a packet-dropping link. Separating estimation from control is practically convenient, and it is a commonly used paradigm in practice, even when it is not guaranteed to be optimal.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We seek to develop a fundamental understanding of the trade-offs which arise when applying the separation principle to nonlinear and partially observed settings. We show that in the presence of bilinear observations, the optimal control law does not obey the separation principle, nor is it linear. Our results highlight the potential for tension between control and measurement, especially when the observations are less noisy than the state evolution. In particular, we show that the minimum of the LQG cost may maximize the state estimation error by causing a loss of observability. Such input-dependent observability is a key challenge which arises in nonlinear and partially observed settings.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Classic optimal control problems for linear dynamics and measurements are well studied. Perhaps the most well known is the $\mathcal{H}_{2}$ criterion, which results in a linear controller that satisfies the separation principle. The robust $\mathcal{H}_{\infty}$ criterion also leads to a linear controller, and it asymptotically follows the separation principle. Linear controllers are optimal in other settings, such as the state feedback min/max problem proposed. Even when not optimal, linear controllers are widely used. Modern approaches based on online learning and system level synthesis restrict controllers to be linear, mainly out of convenience, but do not enforce or utilize the separation principle.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Bilinear optimal control is generally intractable, thus a natural focus for control synthesis is stabilization. To achieve stabilization, performing state estimation is a key step. For fixed input sequences, optimal state estimation for bilinear systems follows the same principles as linear time varying systems. As a result, when the noise is Gaussian, Kalman filtering is statistically optimal. However, due to the input-dependent dynamics matrices, the Kalman filter is *nonlinear* in the input and output variables. In fact, unlike for linear systems, different choices of inputs may lead to better or worse filter performance. The problem of selecting inputs to minimize estimation error is traditionally studied in active learning or experiment design; however these settings treat the underlying state as static. Considering how best to measure the state of a dynamical systems is also studied in sensor design. However, work in this area often focuses on discrete and combinatorial decision spaces, and do not model the "observer effect" of measurement on the state.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The relationship between estimation and control also plays an important role in optimal decentralized control. The famous Witsenhausen counterexample constructed a simple two-stage LQG system where two (scalar valued) control decisions are made given decentralized information, and showed that for this system, linear controllers are not optimal. This simple counterexample has played a crucial role in understanding the challenges of decentralized control.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Contributions:* We make the following contributions towards addressing the problem of optimal control from bilinear observations: (i) we show that the separation principle does not hold when the observation model is bilinear, and (ii) provide a negative result, stating that the optimal controller is not affine in the estimated state. (iii) Under certain settings, we show that the optimal LQG controller can result in significantly worse performance, as it locally maximizes the cost function instead of minimizing. (iv) We then derive an analytical expression for the optimal nonlinear controller in these settings. (v) We also introduce a notion of input dependent observability and derive conditions under which the Kalman filtering covariance remains bounded.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Note that Assumption 1 is standard in the Linear Quadratic Gaussian (LQG) control problem, which is a special case of (2.2) with $\{{\bm{C}}_{k}\}_{k=1}^{p}=\mathbf{0}_{mn}$. Since we don't have access to the state vector ${\bm{x}}_{t}$ at any time $t$, our control policy will be a function of all the information available at time $t$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Input-Dependent State Estimation", "weight": 1.0} -->

Please refer to \[4, Eqs. (E.39) -- (E.42)\] for the derivation of Kalman filtering equations above. Importantly, unlike Kalman filtering from linear measurements, both the Kalman gain ${\bm{L}}({\bm{u}}_{t})$, and the error covariance ${\bm{\Sigma}}_{t+1|t}$ depend on the control inputs up to time $t$. Hence, the separation principle (Def. 2. ‣ 3 Main Results ‣ Sub-optimality of the Separation Principle for Quadratic Control from Bilinear Observations")) is not valid when controlling the partially observed LDS from bilinear observations (2.1). However, it is easy to show that, the Kalman filtering gives the optimal state estimation of (2.1), under Assumption 1.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Main Results", "weight": 1.0} -->

In this section we present our main results on the sub-optimality of the separation principle and linear controllers, and then derive the optimal nonlinear controller in a simple setting. First we present a formal definition of the separation principle, adapted.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Sufficient Conditions for Uniformly Bounded Cost", "weight": 1.0} -->

In this section, we derive conditions under which the estimation error covariance stays bounded. Since our observation matrices are input dependent, we first introduce the notion of uniform observability for bilinear observation systems 2.1.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Experimental Setups", "weight": 1.0} -->

We consider one scalar and two vector experimental setups: a system following (2.1) with $n=m=p=1$, and $T=2$, double integrator style dynamics, and a system with observation following the "orthogonal" condition in Proposition 1. ‣ 3.2 Sufficient Conditions for Uniformly Bounded Cost ‣ 3 Main Results ‣ Sub-optimality of the Separation Principle for Quadratic Control from Bilinear Observations"). For the vector systems, we consider fixed trajectory length of $T=100$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Double Integrator Style Dynamics", "weight": 1.0} -->

In this experiment, the dynamics are governed by the following state-space equations: where ${\bm{w}}_{t}{\overset{\text{i.i.d.}}{\sim}}\mathcal{N}(0,0.01{\bm{I}}_{2})$, $z_{t}{\overset{\text{i.i.d.}}{\sim}}\mathcal{N}(0,0.01)$, and we use $h=0.3$. For quadratic cost, we use ${\bm{Q}}={\bm{Q}}_{T}={\bm{I}}_{2}$, and ${\bm{R}}=1000$. The initial state distribution is $\mathcal{N}(0,{\bm{I}}_{2})$. These dynamics approximate a double integrator with discretization step $h$. For example, if the state contains position and velocity, then the input is a force.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Double Integrator Style Dynamics", "weight": 1.0} -->

The bilinear observation model posits that the signal-to-noise ratio of the position sensor scales with the input force. Put differently, the position measurement results in the application of a force.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Double Integrator Style Dynamics", "weight": 1.0} -->

(c) KF state estimation error Figure 2: Double Integrator. Bilinear observations (C1 = 1) incur more cost (a) than LQG due to the negative effects of small input (b) on state estimation (c,d).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Orthogonal observations", "weight": 1.0} -->

We consider the system (2.1) with $n=6$, and $p=m=3$. The dynamics matrix ${\bm{A}}$ is generated with i.i.d. $\mathcal{N}$ entries, and scaled to have its large eigenvalue $\rho({\bm{A}})=1.1$. The matrix ${\bm{B}}$ is generated with i.i.d. $\mathcal{N}(0,1/n)$ entries, whereas the matrices ${\bm{C}}_{1},\dots,{\bm{C}}_{p}$ are generated with i.i.d. $\mathcal{N}(0,1/m)$ entries. The matrix ${\bm{C}}_{0}$ is chosen in the orthogonal complement of the span of ${\bm{C}}_{1},\dots,{\bm{C}}_{p}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Orthogonal observations", "weight": 1.0} -->

As a result, the system satisfies the condition in Proposition 1. ‣ 3.2 Sufficient Conditions for Uniformly Bounded Cost ‣ 3 Main Results ‣ Sub-optimality of the Separation Principle for Quadratic Control from Bilinear Observations"). The process and observation noise follows $\mathcal{N}(0,0.01{\bm{I}}_{n})$ and $\mathcal{N}(0,0.01{\bm{I}}_{m})$, respectively. For quadratic cost, we choose ${\bm{Q}}={\bm{Q}}_{T}={\bm{I}}_{n}$, and ${\bm{R}}={\bm{I}}_{p}$. The initial state distribution is $\mathcal{N}(0,{\bm{I}}_{n})$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

For each vector system, we evaluate the performance of the separation principle controller for different observation models. We consider perfect state observation (LQR), linear state observation (LQG), and bilinear state observation. For the partially observed models, we use the Kalman filter to estimate the state. The initial state estimate is sampled at random from the initial distribution to avoid the degenerate case where $\hat{{\bm{x}}}_{t}=0$ for all $t\geq 0$ (see the discussion preceding Proposition 1. ‣ 3.2 Sufficient Conditions for Uniformly Bounded Cost ‣ 3 Main Results ‣ Sub-optimality of the Separation Principle for Quadratic Control from Bilinear Observations")). We simulate trajectories 50 times and plot the median quantities (solid line) and the 25th and 75th percentiles (shaded).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Double Integrator", "weight": 1.0} -->

In Figure 2(a), we plot the quadratic cost over time, which shows that the bilinear observation model generally incurs higher cost. Plotting the input over time in Figure 2(b) reveals that the input magnitude drops towards zero near the end of the trajectory, due to the optimal state feedback policy. Though this has no ill effect on LQG, it disrupts the state estimation accuracy for the bilinear model, as illustrated in Figure 2(c) and (d). The Kalman filter diverges because the small inputs lead to a loss of observability, highlighting the sub-optimality of the separation principle in this setting.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Double Integrator", "weight": 1.0} -->

(a) Linear and bilinear observations show different quadratic cost (b) Linear and bilinear observations show similar quadratic cost Figure 3: For fixed A, B, C1, …, Cp, two plots correspond to different C0.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Orthogonal Observations", "weight": 1.0} -->

Following Proposition 1. ‣ 3.2 Sufficient Conditions for Uniformly Bounded Cost ‣ 3 Main Results ‣ Sub-optimality of the Separation Principle for Quadratic Control from Bilinear Observations"), we consider scenarios where the observation model rules out a loss of observability by design. For fixed ${\bm{A}},{\bm{B}},{\bm{C}}_{1},\dots,{\bm{C}}_{p}$, we choose two different ${\bm{C}}_{0}$ in the orthogonal complement of the span of ${\bm{C}}_{1},\dots,{\bm{C}}_{p}$. In Figure 3, we can see that the choice of ${\bm{C}}_{0}$ can show different behavior. Figure 3(a) shows that the bilinear observations can actually improve the quadratic cost compared with LQG. On the other hand, Figure 3(b) shows that the performance can be similar for linear vs. bilinear observations.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

We study the problem of minimizing a quadratic cost of controlling linear dynamical systems from bilinear observations. Our results show that the separation principle does not hold in general for these problems. Moreover, the optimal controller is not affine in the estimated state, although the estimation problem itself remains straightforward, that is, the KF still gives the optimal state estimates, and the posterior distribution of the state. We find that the optimal control problem has a cost-to-go which is generally nonconvex, and the control inputs affect the estimated state and the estimation error covariance in non-trivial ways. We derive analytical expression for the optimal nonlinear control policy in a simple setting and find that the optimal controller is indeed nonlinear in the estimated state. We also derive conditions which guarantee uniform observability in the case of bilinear observations, and verify it through numerical experiments.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

There are several open questions leading to interesting directions for future work. First, deriving an optimal nonlinear control law for (2.2) when $T>2$ is still an open problem. An alternate approach to this will be direct policy optimization for (2.2). Second, when the dynamics matrices are unknown, it will be challenging to design an adaptive control scheme for the system (2.1). Lastly, extending this problem to study the optimal control of partially observed bilinear dynamical systems is also an important future direction.
