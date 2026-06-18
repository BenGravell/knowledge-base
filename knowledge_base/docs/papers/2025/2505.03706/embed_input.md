<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Policy Gradient Adaptive Control for the LQR: Indirect and Direct Approaches

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Motivated by recent advances of reinforcement learning and direct data-driven control, we propose policy gradient adaptive control (PGAC) for the linear quadratic regulator (LQR), which uses online closed-loop data to improve the control policy while maintaining stability. Our method adaptively updates the policy in feedback by descending the gradient of the LQR cost and is categorized as indirect, when gradients are computed via an estimated model, versus direct, when gradients are derived from data using sample covariance parameterization. Beyond the vanilla gradient, we also showcase the merits of the natural gradient and Gauss-Newton methods for the policy update. Notably, natural gradient descent bridges the indirect and direct PGAC, and the Gauss-Newton method of the indirect PGAC leads to an adaptive version of the celebrated Hewer's algorithm. To account for the uncertainty from noise, we propose a regularization method for both indirect and direct PGAC. For all the considered PGAC approaches, we show closed-loop stability and convergence of the policy to the optimal LQR gain. Simulations validate our theoretical findings and demonstrate the robustness and computational efficiency of PGAC.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The history of adaptive control is almost as long as the entire control field, and it is currently revived in the context of reinforcement learning (RL). A fundamental principle of an adaptive control system is its ability to monitor its own performance and adjust its parameters in the direction of better performance. Adaptive control for linear time-invariant systems with unknown parameters is widely studied, and the manifold approaches can be divided with three orthogonal classifications. A commonly adopted one is indirect (when a dynamical model is identified followed by model-based control), versus direct (when bypassing identification). Based on control objectives, approaches are categorized as seeking stability (i.e., convergence of signals) or optimality (i.e., convergence of a performance index). Another perspective considers the policy update rule: one-shot-based methods solve an online optimization problem to obtain the policy, whereas gradient-based methods update the policy iteratively using online gradient information.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Classical adaptive control methods mainly seek robust stability, including indirect and direct model-reference adaptive control (MRAC), self-tuning regulators, and model-free adaptive control. In particular, MRAC designs the control input based on Lyapunov theory to guarantee stability. In comparison, other approaches focus on optimality, aligning more closely with the Zames's definition of adaptive control, i.e., improve over the best performance with prior information. A widely adopted optimality criterion is the infinite-horizon linear quadratic regulator (LQR) cost, which quantifies the $\mathcal{H}_{2}$ norm of the closed-loop system. A representative instance is adaptive dynamical programming (ADP), a classical approach of reinforcement learning (RL). While it shows convergence to the optimal LQR gain, the stability of the closed-loop system remains unclear. An exception is the identification-based policy iteration method, which shows stability under sufficiently small identification error. Recently, there have been adaptive control methods showing both stability and convergence of the policy, based on the indirect certainty-equivalence LQR.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

These optimality-seeking methods commonly require persistently exciting (PE) inputs, without which the bursting phenomenon may happen due to insufficient excitation.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A representative example of one-shot-based methods is indirect adaptive LQR, where the state-feedback policy is determined as the Riccati or semi-definite programming (SDP) solution of a certainty-equivalence LQR problem. However, one-shot-based methods are sensitive to uncertainty, as the policy may significantly vary with large noise. Gradient-based methods are widely adopted in classical adaptive control, which uses different objectives for online gradient computation. For example, the well-known MIT-rule optimizes the squared one-step prediction error, and MRAC includes an additional objective that reflects dynamics of the system. Compared with one-shot-based methods, gradient-based methods are computationally more efficient, as only a single gradient must be computed instead of a complete optimization problem. Moreover, they are robust to noise due to smooth and incremental policy updates. However, the existing gradient-based approaches mainly focus on stability, and it remains unclear if the LQR objective can be adopted to ensure optimality in adaptive control. A major challenge is the non-convexity of the LQR cost in the state-feedback gain, hindering proving convergence of gradient-based methods.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Theoretical studies of the policy gradient method, a foundational cornerstone of modern RL, have shed a light on the non-convex optimization landscape of the LQR. Specifically, the LQR cost is known to be gradient dominated in the state-feedback gain, leading to global linear convergence for policy gradient methods. However, computing the policy gradient requires an exact dynamical model. While zeroth-order methods can be used for gradient estimates in the absence of the model, they are intrinsically unsuitable for adaptive control, as the gradient can be estimated only after observing multiple long trajectories. Even with an exact policy gradient, the sequential stability of the closed-loop system under switching policies remains unclear. In fact, proving the stability of control systems based on RL (e.g., ADP and policy gradient methods) is a difficult task, and the intersection of RL and adaptive control continues to be a compelling and largely unexplored direction.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, there has been a growing interest in direct data-driven control inspired by subspace methods and behavioral system theory. With a data-based system parameterization, direct methods obtain the LQR gain directly from a single batch of PE data. Regularization methods are introduced to promote certainty-equivalence or robustness for direct LQR design or to harness the uncertainty for the separation principle of predictive control. Despite these advances, the adaptation of direct methods is acknowledged as a fundamental open problem in the comprehensive surveys. By proposing a sample covariance parameterization for the LQR and developing a projected gradient dominance property, our previous works attack the direct adaptive control problem with a gradient-based method called data-enabled policy optimization (DeePO), which has seen successful applications in power converter systems, aerospace control, and autonomous bicycle control. However, the closed-loop stability of DeePO remains unclear.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this article, we propose policy gradient adaptive control (PGAC) for the LQR, which is a unified gradient-based framework touching upon both indirect and direct approaches and seeking both stability and optimality. Starting from a batch of offline data and an initial stabilizing gain, it alternates between control, where the input signifies a state-feedback term plus probing noise ensuring persistency of excitation, and gradient-based policy update, where the policy gradient of the LQR cost is approximately computed with online closed-loop data. Our prior DeePO method is a special instance: namely, direct PGAC, using the vanilla gradient of the certainty-equivalent covariance-parameterized LQR for policy update. For indirect PGAC, we use the certainty-equivalence LQR cost with ordinary least-squares identification to compute the policy gradient. Beyond the vanilla policy gradient, we develop natural gradient and Gauss-Newton methods for PGAC. Notably, natural gradient descent bridges indirect and direct PGAC, and the Gauss-Newton method yields an adaptive variant of the celebrated Hewer's algorithm, an iterative method to solve the Riccati equation and a cornerstone of ADP.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our adaptive Hewer's algorithm coincides with the online identification-based policy iteration algorithm. Since the certainty-equivalence LQR formulation disregards uncertainty in the estimated model and may lead to an unstable closed-loop system, we propose a variance-based regularization method for both indirect and direct PGAC to account for the uncertainty. The classification of our certified PGAC methods is shown in Fig. A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)").

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivated by Zames's perspective that adaptation and learning involve the acquisition of information about the plant, we adopt the signal-to-noise ratio (SNR) of the collected data as a quantitative information metric, reflecting the uncertainty in the identified dynamics. This notion satisfies Zames's first monotonicity principle, as the SNR typically increases monotonically over time. For all the aforementioned PGAC approaches, we show that the optimality gap of the LQR gain is upper bounded by two terms signifying an exponential decrease in the initial optimality gap plus a bias scaling linearly with inverse of the SNR. This aligns with Zames's second monotonicity principle of adaptive control, i.e., the performance improves with increasing information. Our results capture the convergence rate of the policy as a function of the SNR, improving upon the rate established in DeePO.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

For example, the optimality gap decreases with time $t$ as $\mathcal{O}{({1/\sqrt{t}})}$ for $\text{SNR}_{t} \sim {\mathcal{O}{(\sqrt{t})}}$, which corresponds to the case of Gaussian noise and a constant excitation level.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Apart from non-asymptotic policy convergence certificates, we provide closed-loop stability guarantees of PGAC by leveraging a favorable feature of gradient-based methods, i.e., the update rate can be easily controlled via the stepsize. Specifically, we show that under a sufficiently small stepsize, the closed-loop system is sequentially stable under switching polices, and the state is upper-bounded by two terms, i.e., an exponential decrease in the initial state plus an upper bound of probing and process noise. While the one-shot-based adaptive control methods also ensure stability, they require a dwell time to mitigate the burn-in effect of switching policies and a safety mechanism in case of divergence. We believe that our analysis techniques provide a viable solution to proving closed-loop stability in RL algorithms.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

We perform simulations on a benchmark problem to validate our theoretical findings and demonstrate favorable computational efficiency and robustness of PGAC.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this article is organized as follows. Section IIA. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") recapitulates data-driven formulations of the LQR. Section IIIA. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") formulates the adaptive control problem and proposes PGAC. Section IVA. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") proposes two variants of gradient descent for PGAC. Section VA. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

(e-mail: alessandro.chiuso@unipd.it)") develops a regularization method for PGAC. Section VIA. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") uses simulations to validate our theoretical results. Concluding remarks are made in Section VIIA. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"). All proofs are provided in the Appendix.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Data-driven formulations of the LQR", "weight": 1.0} -->

This section recapitulates indirect certainty-equivalence LQR with least-squares identification and direct certainty-equivalence LQR with covariance parameterization.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A Model-based LQR", "weight": 1.0} -->

where $t \in {\mathbb{N}}$, $x_{t} \in {\mathbb{R}}^{n}$ is the state, $u_{t} \in {\mathbb{R}}^{m}$ is the control input, $w_{t} \in {\mathbb{R}}^{n}$ is the noise, and $z_{t}$ is the performance signal of interest. We assume that $(A,B)$ are controllable and the weighting matrices $(Q,R)$ are positive definite.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-A Model-based LQR", "weight": 1.0} -->

The LQR problem is phrased as finding a state-feedback gain $K \in {\mathbb{R}}^{m \times n}$ that minimizes the $\mathcal{H}_{2}$-norm of the transfer function ${\mathcal{T}{(K)}}:{w\rightarrow z}$ of the closed-loop system

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-A Model-based LQR", "weight": 1.0} -->

where $\Sigma$ is the closed-loop state covariance matrix obtained as the positive definite solution to the Lyapunov equation

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-A Model-based LQR", "weight": 1.0} -->

We refer to $C{(K)}$ as the LQR cost and to (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"))-(A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) as a policy parameterization of the LQR.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-A Model-based LQR", "weight": 1.0} -->

For known $(A,B)$, there are alternative formulations to find the optimal LQR gain $K^{\ast}:={{\arg{\min_{K}C}}{(K)}}$ of (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"))-(A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), e.g., via the celebrated Riccati equation. We recall a well-known iterative algorithm to solve the Riccati equation, called Hewer's algorithm (also known as policy iteration in reinforcement learning (RL) ), which starts from an initial stabilizing policy $K_{0}$ and alternates between

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-A Model-based LQR", "weight": 1.0} -->

where (5aA. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) is the policy evaluation, and (5bA. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) is the policy improvement. The Hewer's algorithm has asymptotic convergence guarantees to the solution of the Riccati equation and the optimal policy $K^{\ast}$, which are fixed points of (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")).

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-A Model-based LQR", "weight": 1.0} -->

For unknown $(A,B)$, there is a plethora of data-driven methods to find $K^{\ast}$, some of which we recapitulate below.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-B Indirect certainty-equivalence LQR with ordinary least-square identification", "weight": 1.0} -->

The conventional approach to data-driven LQR design follows the certainty-equivalence principle: it first identifies nominal system matrices $(A,B)$ from data, and then solves the LQR problem regarding the identified model as the ground-truth. The identification step is based on subspace relations among the state-space data. Consider a $t$-long time series of states, inputs, unknown noises, and successor states

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-B Indirect certainty-equivalence LQR with ordinary least-square identification", "weight": 1.0} -->

which satisfy the system dynamics

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-B Indirect certainty-equivalence LQR with ordinary least-square identification", "weight": 1.0} -->

We assume that the data is persistently exciting (PE), i.e., the block matrix of input and state data

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-B Indirect certainty-equivalence LQR with ordinary least-square identification", "weight": 1.0} -->

which is necessary for data-driven LQR design.

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-B Indirect certainty-equivalence LQR with ordinary least-square identification", "weight": 1.0} -->

Based on the subspace relations (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) and the rank condition (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), an estimated model $(\hat{A},\hat{B})$ can be obtained as the unique solution to the ordinary least-squares problem

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-B Indirect certainty-equivalence LQR with ordinary least-square identification", "weight": 1.0} -->

Following the certainty-equivalence principle, the system $(A,B)$ is replaced with its estimate $(\hat{A},\hat{B})$ in (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"))-(A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), and the LQR problem can be reformulated as

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-B Indirect certainty-equivalence LQR with ordinary least-square identification", "weight": 1.0} -->

where $\Sigma$ is the positive definite solution to

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-B Indirect certainty-equivalence LQR with ordinary least-square identification", "weight": 1.0} -->

The problem formulation (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"))-(A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) is termed indirect certainty-equivalence LQR design.

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-C Direct certainty-equivalence LQR with covariance parameterization", "weight": 1.0} -->

Instead of estimating a dynamical model (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), the direct data-driven LQR design aims to find $K^{\ast}$ directly from a batch of PE data. For this purpose, our previous work proposes a policy parameterization based on the sample covariance of input-state data

<!-- chunk {"id": "body-0034", "role": "body", "section": "II-C Direct certainty-equivalence LQR with covariance parameterization", "weight": 1.0} -->

Under the PE rank condition (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), the sample covariance $\Phi$ is positive definite, and there exists a unique solution $V \in {\mathbb{R}}^{{({n + m})} \times n}$ to

<!-- chunk {"id": "body-0035", "role": "body", "section": "II-C Direct certainty-equivalence LQR with covariance parameterization", "weight": 1.0} -->

for any given $K$. We refer to (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) as the covariance parameterization of the policy. Note that the dimension of the parameterized policy $V$ does not scale with data length $t$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "II-C Direct certainty-equivalence LQR with covariance parameterization", "weight": 1.0} -->

Following the certainty-equivalence principle, we disregard the uncertainty ${\overline{W}}_{0}$ in (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")). Substituting $A + {BK}$ with ${\overline{X}}_{1}V$ in (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"))-(A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) and together with (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0037", "role": "body", "section": "II-C Direct certainty-equivalence LQR with covariance parameterization", "weight": 1.0} -->

(e-mail: alessandro.chiuso@unipd.it)")), the LQR problem becomes

<!-- chunk {"id": "body-0038", "role": "body", "section": "II-C Direct certainty-equivalence LQR with covariance parameterization", "weight": 1.0} -->

with the gain matrix $K = {{\overline{U}}_{0}V}$, where $\Sigma$ is the positive definite solution to the Lyapunov equation

<!-- chunk {"id": "body-0039", "role": "body", "section": "II-C Direct certainty-equivalence LQR with covariance parameterization", "weight": 1.0} -->

The problem formulation (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"))-(A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) is termed direct certainty-equivalence LQR design, and its solution coincides with that of the indirect design (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"))-(A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Policy gradient adaptive control", "weight": 1.0} -->

In this section, we formulate the adaptive control problem and propose policy gradient adaptive control with convergence and stability guarantees.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-A Problem statement", "weight": 1.0} -->

We focus on the following adaptive control problem.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Problem 1", "weight": 1.0} -->

design a gradient-based method leveraging online closed-loop data such that the control policy converges to the optimal LQR gain, while ensuring the stability of the closed-loop system.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Problem 1", "weight": 1.0} -->

Problem A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") concerns both stability and optimality, which is in line with the definition of adaptive control by Zames, i.e., improve over the best with prior information. Throughout the article, we make the following assumption.^11^1From Section IIIA. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"), we use $X_{0,t},U_{0,t},W_{0,t},X_{1,t}$ to denote the data series of length $t$ in (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Problem 1", "weight": 1.0} -->

We also add a subscript $t$ to other notations to highlight the time dependence..

<!-- chunk {"id": "body-0045", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Assumption A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") is a quantitative condition of persistency of excitation and implies the rank condition (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")). It can be satisfied by adding probing noise to the control input and holds under another PE definition \[, Definition 2\], which can be verified by examining solely the inputs. Notice again that the PE assumption is universal in adaptive control.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

By Zames, adaptive control involves the acquisition of information about the plant. To specify the information metric, let

<!-- chunk {"id": "body-0047", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

denote the bound of the covariance between the process noise and input-state data. This quantity reflects not only the amount of noise but also its correlation with the input-state data, which can capture particular statistics (e.g., i.i.d. noise). Note that we do not assume statistics of noise for the seek of generality. Define the signal-to-noise ratio (SNR) of data at time $t$ as

<!-- chunk {"id": "body-0048", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

which describes the ratio between the useful and useless information. We adopt the SNR as an information metric, as the model uncertainty scales inversely with $\text{SNR}_{t}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-B The policy gradient adaptive control framework", "weight": 1.0} -->

To solve Problem A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"), we propose a policy gradient adaptive control (PGAC) framework alternating between control and gradient-based policy update. Specifically, the control input is in the form of $u_{t} = {{K_{t}x_{t}} + e_{t}}$, where the state-feedback gain $K_{t}$ is the parameterized policy at time $t$, and $e_{t}$ is a probing noise ensuring the PE condition. We assume that the initial gain $K_{t_{0}}$ is stabilizing, which is common in adaptive control. Define $\mathcal{S}:=\left.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The initial gain is stabilizing, i.e., $K_{t_{0}} \in \mathcal{S}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

We let Assumption A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") hold in the rest of the article. The policy $K_{t}$ is updated over time with gradient methods of the LQR cost. When $(A,B)$ are known, the policy iterates as

<!-- chunk {"id": "body-0052", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

where ${\nabla C}{(K_{t})}$ is the exact policy gradient. Then, the closed-form expression of ${\nabla C}{(K)}$ is given below.

<!-- chunk {"id": "body-0053", "role": "body", "section": "III-C Indirect policy gradient adaptive control", "weight": 1.0} -->

1:Offline data (X0, t0,U0, t0,X1, t0), an initial stabilizing policy Kt0, and a stepsize η.
3: Apply ut = Ktxt + et and observe xt + 1.
4: Estimate the model via recursive least-squares.
5: Perform one-step policy gradient descent

<!-- chunk {"id": "body-0054", "role": "body", "section": "III-C Indirect policy gradient adaptive control", "weight": 1.0} -->

where ∇Ĉt + 1(Kt) is the policy gradient with the estimated model (Ât + 1,B̂t + 1).
Algorithm 1 Indirect Policy Gradient Adaptive Control

<!-- chunk {"id": "body-0055", "role": "body", "section": "III-C Indirect policy gradient adaptive control", "weight": 1.0} -->

Indirect PGAC uses the least-squares estimates $(\hat{A},\hat{B})$ in (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) to approximately compute the policy gradient. The details are presented in Algorithm A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"). We require an initial stabilizing gain and a batch of offline PE data. In the online stage, the control input contains a probing noise $e_{t}$ to ensure Assumption A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"). After observing the new state, we use recursive least-squares to identify an updated model estimate.

<!-- chunk {"id": "body-0056", "role": "body", "section": "III-C Indirect policy gradient adaptive control", "weight": 1.0} -->

which is an efficient rank-one update. Then, we perform one-step policy gradient descent with stepsize $\eta$, where the gradient is computed with the estimated model.

<!-- chunk {"id": "body-0057", "role": "body", "section": "III-C Indirect policy gradient adaptive control", "weight": 1.0} -->

Lemma A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") will play an important role in quantifying the effects of replacing the exact policy gradient with the approximated policy gradient in (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")). Together with Lemmas ‣ III-B The policy gradient adaptive control framework ‣ III Policy gradient adaptive control ‣ Policy Gradient Adaptive Control for the LQR: Indirect and Direct Approaches This work was supported by ETH Zurich and the SNF through the NCCR Automation. F. Zhao and F. Dörfler are with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland.

<!-- chunk {"id": "body-0058", "role": "body", "section": "III-C Indirect policy gradient adaptive control", "weight": 1.0} -->

(e-mail: zhaofe@control.ee.ethz.ch; dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") and ‣ III-B The policy gradient adaptive control framework ‣ III Policy gradient adaptive control ‣ Policy Gradient Adaptive Control for the LQR: Indirect and Direct Approaches This work was supported by ETH Zurich and the SNF through the NCCR Automation. F. Zhao and F. Dörfler are with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: zhaofe@control.ee.ethz.ch; dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0059", "role": "body", "section": "III-C Indirect policy gradient adaptive control", "weight": 1.0} -->

(e-mail: alessandro.chiuso@unipd.it)"), we can show the convergence of $K_{t}$ in Algorithm A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)").

<!-- chunk {"id": "body-0060", "role": "body", "section": "III-C Indirect policy gradient adaptive control", "weight": 1.0} -->

Apart from the convergence, we need to show stability of the closed-loop system. Since $K_{t}$ is updated over time, we resort to stability analysis of switching or time-varying systems.

<!-- chunk {"id": "body-0061", "role": "body", "section": "III-D Direct policy gradient adaptive control", "weight": 1.0} -->

Instead of computing the policy gradient with an estimated model, direct PGAC updates the policy based on the sample covariance parameterization (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"))-(A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")). The details are presented in Algorithm A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"), which is also known as data-enabled policy optimization (DeePO). In the online stage, we use sample covariance to parameterize the policy (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0062", "role": "body", "section": "III-D Direct policy gradient adaptive control", "weight": 1.0} -->

(e-mail: alessandro.chiuso@unipd.it)")) and perform one-step projected gradient descent on the parameterized policy (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")). Define $\mathcal{V}:=\left. \{{V \in {\mathbb{R}}^{{({n + m})} \times n}} \middle| {{\rho{({{\overline{X}}_{1}V})}} < 1}\} \right.$ as the feasible set of the covariance-parameterized LQR (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")). The gradient and projection expressions are as below.

<!-- chunk {"id": "body-0063", "role": "body", "section": "PGAC with the natural gradient and Gauss-Newton methods", "weight": 1.0} -->

In the previous section, we have developed indirect and direct PGAC methods, where the vanilla gradient descent is used to update the policy. In this section, we demonstrate the merits of two variants of gradient descent: natural gradient and Gauss-Newton methods, for the policy update of PGAC. In particular, the natural gradient descent bridges indirect and direct PGAC, and the Gauss-Newton method of the indirect PGAC leads to an adaptive version of Hewer's algorithm (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")).

<!-- chunk {"id": "body-0064", "role": "body", "section": "IV-A Bridging indirect and direct PGAC via natural gradient", "weight": 1.0} -->

Let us vectorize $K$ as $\theta = {\text{vec}{(K^{\top})}}$. Then, the natural policy gradient update of the LQR cost $C{(\theta)}$ is given by^22^2With a slight abuse of notation, we use $C{(\theta)}$ and $C{(K)}$ interchangeably.

<!-- chunk {"id": "body-0065", "role": "body", "section": "IV-A Bridging indirect and direct PGAC via natural gradient", "weight": 1.0} -->

where ${\nabla C}{(\theta)}$ is the vanilla gradient, and $F_{\theta} \succ 0$ is the Fisher information matrix (FIM) that captures the curvature of the parameter space of $\theta$, which biases the gradient descent in the direction of large uncertainties. The corresponding update for $K$ takes the form

<!-- chunk {"id": "body-0066", "role": "body", "section": "IV-A Bridging indirect and direct PGAC via natural gradient", "weight": 1.0} -->

where $\Sigma$ satisfies (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), $P$ satisfies ( ‣ III-B The policy gradient adaptive control framework ‣ III Policy gradient adaptive control ‣ Policy Gradient Adaptive Control for the LQR: Indirect and Direct Approaches This work was supported by ETH Zurich and the SNF through the NCCR Automation. F. Zhao and F. Dörfler are with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: zhaofe@control.ee.ethz.ch; dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0067", "role": "body", "section": "IV-A Bridging indirect and direct PGAC via natural gradient", "weight": 1.0} -->

(e-mail: alessandro.chiuso@unipd.it)")), and the last equality follows from Lemma ‣ III-B The policy gradient adaptive control framework ‣ III Policy gradient adaptive control ‣ Policy Gradient Adaptive Control for the LQR: Indirect and Direct Approaches This work was supported by ETH Zurich and the SNF through the NCCR Automation. F. Zhao and F. Dörfler are with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: zhaofe@control.ee.ethz.ch; dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"). We briefly highlight the merits of natural gradient.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Compared with the vanilla gradient descent, the natural gradient descent (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) is computationally more efficient, as it can be computed with only one Lyapunov equation ( ‣ III-B The policy gradient adaptive control framework ‣ III Policy gradient adaptive control ‣ Policy Gradient Adaptive Control for the LQR: Indirect and Direct Approaches This work was supported by ETH Zurich and the SNF through the NCCR Automation. F. Zhao and F. Dörfler are with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: zhaofe@control.ee.ethz.ch; dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Remark 2", "weight": 1.0} -->

(e-mail: alessandro.chiuso@unipd.it)")) instead of two for the vanilla gradient in Lemma ‣ III-B The policy gradient adaptive control framework ‣ III Policy gradient adaptive control ‣ Policy Gradient Adaptive Control for the LQR: Indirect and Direct Approaches This work was supported by ETH Zurich and the SNF through the NCCR Automation. F. Zhao and F. Dörfler are with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: zhaofe@control.ee.ethz.ch; dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"). Moreover, the stepsize for natural gradient (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Remark 2", "weight": 1.0} -->

(e-mail: alessandro.chiuso@unipd.it)")) can be chosen more aggressively than that of the vanilla gradient, leading to an improved convergence rate.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Motivated by (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), for indirect PGAC with natural gradient, we substitute the policy update (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) in Algorithm A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") with

<!-- chunk {"id": "body-0072", "role": "body", "section": "Remark 2", "weight": 1.0} -->

where ${\hat{P}}_{t + 1}$ is the positive definite solution to Lyapunov equation ( ‣ III-B The policy gradient adaptive control framework ‣ III Policy gradient adaptive control ‣ Policy Gradient Adaptive Control for the LQR: Indirect and Direct Approaches This work was supported by ETH Zurich and the SNF through the NCCR Automation. F. Zhao and F. Dörfler are with the Department of Information Technology and Electrical Engineering, ETH Zürich, 8092 Zürich, Switzerland. (e-mail: zhaofe@control.ee.ethz.ch; dorfler@control.ee.ethz.ch)A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) with the estimated model $({\hat{A}}_{t + 1},{\hat{B}}_{t + 1})$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Remark 2", "weight": 1.0} -->

For direct PGAC with natural gradient, we notice that the covariance parameterization (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) defines a smooth bijection between the spaces of $K$ and $V$. By leveraging the fact that FIM captures the geometry of the paramterization space, we show that indirect and direct PGAC are bridged by adopting the natural gradient descent for the policy update.

<!-- chunk {"id": "body-0074", "role": "body", "section": "IV-B Indirect PGAC with Gauss-Newton method and its equivalence to an adaptive Hewer's algorithm", "weight": 1.0} -->

1:Offline data (X0, t0,U0, t0,X1, t0) and an initial stabilizing policy Kt0.
3: Apply ut = Ktxt + et and observe xt + 1.
4: Estimate the model via recursive least-squares.
5: Policy evaluation P̂t + 1 = Q + Kt⊤RKt + (Ât + 1+B̂t + 1Kt)⊤P̂t + 1(Ât + 1+B̂t + 1Kt).

<!-- chunk {"id": "body-0075", "role": "body", "section": "IV-B Indirect PGAC with Gauss-Newton method and its equivalence to an adaptive Hewer's algorithm", "weight": 1.0} -->

The Gauss-Newton method is a quasi-Newton method under a particular Riemannian metric. It iterates as

<!-- chunk {"id": "body-0076", "role": "body", "section": "IV-B Indirect PGAC with Gauss-Newton method and its equivalence to an adaptive Hewer's algorithm", "weight": 1.0} -->

with the constant stepsize $0 < \eta < 1$. The stepsize of the Gauss-Newton method can be chosen more aggressively than the vanilla and natural gradient, leading to a faster convergence rate. With a special choice of stepsize $\eta = {1/2}$, the Gauss-Newton update (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) is equivalent to

<!-- chunk {"id": "body-0077", "role": "body", "section": "IV-B Indirect PGAC with Gauss-Newton method and its equivalence to an adaptive Hewer's algorithm", "weight": 1.0} -->

This coincides with the Hewer's algorithm (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) and enjoys local quadratic convergence. However, the Gauss-Newton update is computationally less efficient than natural gradient, as computing (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) involves the inverse of a matrix.

<!-- chunk {"id": "body-0078", "role": "body", "section": "IV-B Indirect PGAC with Gauss-Newton method and its equivalence to an adaptive Hewer's algorithm", "weight": 1.0} -->

Inspired by (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), for indirect PGAC we substitute the policy update (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) in Algorithm A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") with

<!-- chunk {"id": "body-0079", "role": "body", "section": "IV-B Indirect PGAC with Gauss-Newton method and its equivalence to an adaptive Hewer's algorithm", "weight": 1.0} -->

Our theoretical guarantees of indirect PGAC with the Gauss-Newton update (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) are as below.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Boosting the performance of PGAC via regularization", "weight": 1.0} -->

So far, we have developed PGAC with variants of gradient descent of the certainty-equivalence LQR formulations (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) and (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")). However, the certainty-equivalence approach neglects the effect of noise in the data, leading to uncertainties in the closed-loop covariance matrix and the cost function. This section recalls a regularization method for PGAC to compensate the uncertainty. As a main contribution, we show that the theoretical guarantees of PGAC are preserved under proper choices of the regularization coefficient.

<!-- chunk {"id": "body-0081", "role": "body", "section": "V-A Indirect PGAC with regularization", "weight": 1.0} -->

For the indirect certainty-equivalence LQR (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)"))-(A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), the closed-loop covariance matrix $\Sigma$ satisfies the Lyapunov equation (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")). However, given $(A,B)$, the Lyapunov equation that should be met is (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0082", "role": "body", "section": "V-A Indirect PGAC with regularization", "weight": 1.0} -->

(e-mail: alessandro.chiuso@unipd.it)")). For brevity, define

<!-- chunk {"id": "body-0083", "role": "body", "section": "V-A Indirect PGAC with regularization", "weight": 1.0} -->

Then, the difference between the right-hand sides of (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) and (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) is

<!-- chunk {"id": "body-0084", "role": "body", "section": "V-A Indirect PGAC with regularization", "weight": 1.0} -->

For well-behaved noise statistics, $\|{\overline{W}}_{0}\|$ usually vanishes quickly with time \[, Lemma 1\], and the first two terms dominate the difference. To reduce the difference, we introduce the regularizer $\text{Tr}{({\Phi^{- 1}\Xi})}$ to the certainty-equivalence cost (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), leading to the regularized cost

<!-- chunk {"id": "body-0085", "role": "body", "section": "V-A Indirect PGAC with regularization", "weight": 1.0} -->

where $\Sigma$ satisfies (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), and $\lambda > 0$ is the regularization coefficient. The regularizer is a correction to the penalty matrices of the LQR problem. In line, the regularization also compensates the uncertainty in the cost function and promotes exploitation. We demonstrate these merits via simulations in Section VI-CA. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)").

<!-- chunk {"id": "body-0086", "role": "body", "section": "V-A Indirect PGAC with regularization", "weight": 1.0} -->

Next, we derive the gradient expression of the regularized cost (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")). Consider the following partition of $\Phi^{- 1}$

<!-- chunk {"id": "body-0087", "role": "body", "section": "V-B Direct PGAC with regularization", "weight": 1.0} -->

Leveraging the covariance parameterization in (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), the regularizer in (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) can be reformulated as $\text{Tr}{({V\Sigma V^{\top}\Phi})}$. Then, the direct LQR cost with regularization is

<!-- chunk {"id": "body-0088", "role": "body", "section": "V-B Direct PGAC with regularization", "weight": 1.0} -->

We derive the gradient expression of $J{(V;\lambda)}$, the proof of which follows the same vein as that of \[, Lemma 2\] and is omitted due to space limitation.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Numerical case studies", "weight": 1.0} -->

This section uses simulations to demonstrate the effectiveness of PGAC in terms of convergence, stability, and computational efficiency. Our simulations are based on the benchmark LQR problem with the model \[, Section 6\]

<!-- chunk {"id": "body-0090", "role": "body", "section": "Numerical case studies", "weight": 1.0} -->

which corresponds to a discrete-time marginally unstable Laplacian system, and $Q = I_{3}$ and $R = {10^{- 3} \times I_{3}}$. Note that the direct PGAC method has been validated in nonlinear power systems and real-world experiments of an autonomous bicycle. Our code is run in Matlab and provided in

<!-- chunk {"id": "body-0091", "role": "body", "section": "VI-A Convergence and closed-loop stability of PGAC", "weight": 1.0} -->

We compare the convergence and stability of the one-shot-based adaptive control, direct and indirect PGAC with the vanilla gradient, natural gradient, and Gauss-Newton methods. We set the number of offline data to $t_{0} = 20$ and let $x_{0} = 0$, $u_{t} \sim {\mathcal{N}{(0,I_{3})}}$ for $t < t_{0}$. For $t \geq t_{0}$, we set $u_{t} = {{K_{t}x_{t}} + e_{t}}$ with $e_{t} \sim {\mathcal{N}{(0,I_{3})}}$ to ensure persistency of excitation.

<!-- chunk {"id": "body-0092", "role": "body", "section": "VI-A Convergence and closed-loop stability of PGAC", "weight": 1.0} -->

The noise is drawn from $w_{t} \sim {\mathcal{N}{(0,I_{3})}}$, which corresponds to a poor $\text{SNR}_{t} \in {\lbrack{- 5},0\rbrack}$ dB. We set the stepsize to $\eta = 0.02$ for indirect PGAC with the vanilla gradient, $\eta = 0.2$ for natural gradient, $\eta = 0.5$ for the Gauss-Newton method (Algorithm A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")), and $\eta_{t} = {0.2/{\| M_{t}\|}}$ for direct PGAC.

<!-- chunk {"id": "body-0093", "role": "body", "section": "VI-A Convergence and closed-loop stability of PGAC", "weight": 1.0} -->

The one-shot-based method obtains $K_{t}$ from the Riccati equation with an estimated model (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) every time step. For all the methods, we set $K_{t_{0}}$ as the certainty-equivalence LQR (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) with offline data.

<!-- chunk {"id": "body-0094", "role": "body", "section": "VI-A Convergence and closed-loop stability of PGAC", "weight": 1.0} -->

Fig. A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") shows the optimality gap of the policy sequence for the one-shot-based method and direct and indirect PGAC with the vanilla gradient under the same randomness realization. For clarity of presentation, we omit the curves of indirect PGAC with natural gradient and Gauss-Newton, which lie between those of the one-shot-based method and indirect PGAC with the vanilla gradient. We make several key observations. First, all the methods improve the performance over the initial policy using online closed-loop data, and the optimality gap converges asymptotically at the rate $\mathcal{O}{({1/t})}$, which implies that our theoretically certified rate $\mathcal{O}{({1/\sqrt{t}})}$ is conservative. Second, the one-shot-based method diverges at the early stage due to unexpected large noise. In contrast, PGAC methods exhibit more stable convergence.

<!-- chunk {"id": "body-0095", "role": "body", "section": "VI-A Convergence and closed-loop stability of PGAC", "weight": 1.0} -->

This is expected in presence of noise, as the gradient is more robust than the minimizer.

<!-- chunk {"id": "body-0096", "role": "body", "section": "VI-A Convergence and closed-loop stability of PGAC", "weight": 1.0} -->

Fig. A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)") shows their average finite-horizon cost $\sum_{i = 0}^{t - 1}{{\| z_{i}\|}^{2}/t}$ as a function of time, where $z_{t}$ is the performance output in (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")). We observe that all methods exhibit highly similar average costs, which converge rapidly to a positive constant. This indicates that the closed-loop systems resulting from both PGAC and the one-shot-based method are stable. Furthermore, the convergence behavior aligns with our theoretical results, i.e., the state is bounded by the sum of an exponentially decaying term and a steady-state bias determined by the probing and process noise.

<!-- chunk {"id": "body-0097", "role": "body", "section": "VI-A Convergence and closed-loop stability of PGAC", "weight": 1.0} -->

We note that the divergence at the early stage is due to abrupt large process noise.

<!-- chunk {"id": "body-0098", "role": "body", "section": "VI-B Computational efficiency of PGAC", "weight": 1.0} -->

We compare their efficiency in terms of the computation time. For indirect PGAC, we apply recursive least squares (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) for identification. For direct PGAC, we apply the rank-one update in \[, Section V-B\]. For the one-shot-based method, the certainty-equivalence LQR problem (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy. (e-mail: alessandro.chiuso@unipd.it)")) is solved using the dlqr function in MATLAB. We perform $20$ independent trials and record the mean of the computation time for running $t = 500$ time steps. The results are summarized in Table I. We observe that compared with the one-shot-based method, the PGAC approaches require significantly less computational time.

<!-- chunk {"id": "body-0099", "role": "body", "section": "VI-B Computational efficiency of PGAC", "weight": 1.0} -->

This gap is due to that PGAC performs only one or two Lyapunov equation solves per iteration for gradient descent, whereas the one-shot-based method involves solving a Riccati equation at each step. Among all the PGAC approaches, direct PGAC consumes highest computation time as the dimension of the optimization matrix $V \in {\mathbb{R}}^{{({n + m})} \times n}$ is higher than that of $K \in {\mathbb{R}}^{m \times n}$ in the indirect case. For indirect PGAC, the vanilla gradient method is slowest as it requires solving two Lyapunov equations per time step instead of one for natural gradient and Gauss-Newton methods. It is worth noting that while we demonstrate the results using a simple third-order system (A. Chiuso is with the Department of Information Engineering, University of Padova, Via Gradenigo 6/b, 35131 Padova, Italy.

<!-- chunk {"id": "body-0100", "role": "body", "section": "VI-B Computational efficiency of PGAC", "weight": 1.0} -->

(e-mail: alessandro.chiuso@unipd.it)")), the computational gap between PGAC and the one-shot-based method grows substantially with increasing system dimension; we refer the reader to our previous work \[, Section V\] for more comprehensive simulation results.

<!-- chunk {"id": "body-0101", "role": "body", "section": "VI-C The impact of regularization", "weight": 1.0} -->

We study the impact of regularization for both indirect and direct PGAC with the vanilla gradient. We set the stepsize to $\eta = 0.2$ for indirect PGAC and $\eta_{t} = {0.2/{\| M_{t}\|}}$ for direct PGAC. Consider $100$ independent trials. We denote by $\mathcal{P}$ the percentage the algorithm converges without any instability issue and by $\mathcal{M}$ the median of the optimality gap ${({{C{(K_{T})}} - C^{\ast}})}/C^{\ast}$ with $T = 1000$ through all trails where convergence is observed. The results are reported in Table II, where the one-shot-based method without regularization is for comparison. With regularization, both indirect and direct PGAC significantly outperform the one-shot-based method in terms of algorithm stability, i.e., the robustness of policy updates against noise. Furthermore, direct PGAC achieves a smaller optimality gap compared to the one-shot-based method.

<!-- chunk {"id": "body-0102", "role": "body", "section": "VI-C The impact of regularization", "weight": 1.0} -->

This is because our regularizer well compensates the uncertainty induced by noise in both the closed-loop covariance matrix and the cost function.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Concluding remarks", "weight": 1.0} -->

In this article, we proposed policy gradient adaptive control (PGAC) for the LQR, which touches upon both indirect and direct approaches and enables the use of variant gradient methods and regularization. For all approaches, we showed convergence of the policy and stability of the closed-loop system. Simulations validated the theoretical results and illustrated the robustness and computational efficiency of PGAC.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Concluding remarks", "weight": 1.0} -->

We believe that this article leads to fruitful future works. It would be interesting to see if the probing signal can be designed using the sample covariance to efficiently reduce the uncertainty. As observed in the simulation, our theoretical convergence rate may be conservative, and a sharper analysis might be possible. Our sequential stability analysis can be used for other RL-based adaptive control methods, e.g., adaptive dynamical programming, where the closed-loop stability is largely open. Our PGAC framework can be extended to other settings (e.g., output feedback control), performance indices (e.g., $\mathcal{H}_{\infty}$ norm), noise assumptions (e.g., stochastic noise), and system classes (e.g., time-varying systems).
