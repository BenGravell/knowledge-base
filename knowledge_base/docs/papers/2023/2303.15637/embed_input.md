<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Fundamental Limitations of Learning Linear-Quadratic Regulators

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a local minimax lower bound on the excess cost of designing a linear-quadratic controller from offline data. The bound is valid for any offline exploration policy that consists of a stabilizing controller and an energy bounded exploratory input. The derivation leverages a relaxation of the minimax estimation problem to Bayesian estimation, and an application of Van Trees' inequality. We show that the bound aligns with system-theoretic intuition. In particular, we demonstrate that the lower bound increases when the optimal control objective value increases. We also show that the lower bound increases when the system is poorly excitable, as characterized by the spectrum of the controllability gramian of the system mapping the noise to the state and the H_infinity norm of the system mapping the input to the state. We further show that for some classes of systems, the lower bound may be exponential in the state dimension, demonstrating exponential sample complexity for learning the linear-quadratic regulator offline.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement Learning (RL) has demonstrated success in a variety of domains, including robotics and games. However, it is known to be very data intensive, making it challenging to apply to complex control tasks. This has motivated efforts by both the machine learning and control communities to understand the statistical hardness of RL in analytically tractable settings, such as the tabular setting and the linear-quadratic control setting. Such studies provide insights into the fundamental limitations of RL, and the efficiency of particular algorithms.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

There are two common problems of interest for understanding the statistical hardness of RL from the perspective of learning a linear-quadratic regulator (LQR): online LQR, and offline LQR. Online LQR models an interactive problem in which the learning agent attempts to minimize a regret-based objective, while simultaneously learning the dynamics. Offline LQR models a two-step pipeline, where data from the system is collected, and then used to design a controller. Guarantees in the online setting are in the form of regret bounds, whereas the offline setting focuses on Probably Approximately Correct (PAC) guarantees. The high data requirements of RL often render offline approaches the only feasible option for physical systems Levine et al.. Despite this fact, recent years have seen greater efforts to provide lower bounds for the online LQR problem. Meanwhile, lower bounds in the offline LQR setting are conspicuously absent. Motivated by this fact, we derive lower bounds for designing a linear-quadratic controller from offline data.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notation: The Euclidean norm of a vector $x$ is denoted by $\left\| x \right\|$. The quadratic norm of a vector $x$ with respect to a matrix $P$ is denoted $\left\| x \right\|_{P} = \sqrt{x^{\top}Px}$. For a matrix $A$, the spectral norm is denoted $\left\| A \right\|$ and the Frobenius norm is denoted $\left\| A \right\|_{F}$. The spectral radius of a square matrix $A$ is denoted $\rho{(A)}$. A symmetric, positive semidefinite matrix $A = A^{\top}$ is denoted $A \succeq 0$, and a symmetric, positive definite matrix is denoted $A \succ 0$. Similarly, $A \succeq B$ denotes that $A - B$ is positive semidefinite.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The eigenvalues of a symmetric positive definite matrix $A \in {\mathbb{R}}^{n \times n}$ are denoted ${\lambda_{1}{(A)}},\ldots,{\lambda_{n}{(A)}}$, and are sorted in non-ascending order. We also denote ${\lambda_{1}{(A)}} = {\lambda_{\max}{(A)}}$, and ${\lambda_{n}{(A)}} = {\lambda_{\min}{(A)}}$. For a matrix $A$, the vectorization operator ${\mathsf{v}\mathsf{e}\mathsf{c}}A$ maps $A$ to a column vector by stacking the columns of $A$. The kronecker product of $A$ with $B$ is denoted $A \otimes B$. Expectation and probability with respect to all the randomness of the underlying probability space are denoted $\text{E}$ and $\mathbf{P}$, respectively.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Let $\theta \in {\mathbb{R}}^{d_{\Theta}}$ be an unknown parameter. We study the fundamental limitations to learning to control the following parametric system model: The noise process $W_{t}$ is assumed to be iid mean zero Gaussian with fixed covariance matrices $\Sigma_{W} \succ 0$. The matrices ${A{(\theta)}} \in {\mathbb{R}}^{d_{\mathsf{X}} \times d_{\mathsf{X}}}$ and ${B{(\theta)}} \in {\mathbb{R}}^{d_{\mathsf{X}} \times d_{\mathsf{U}}}$ are known continuously differentiable functions of the unknown parameter. The system $({A{(\theta)}},{B{(\theta)}})$ is assumed to be stabilizable.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We assume that the learner is given access to $N \in {\mathbb{N}}$ experiments ${{(X_{0,n},\ldots,X_{{T - 1},n})},n} \in {\lbrack N\rbrack}$ from of length $T \in {\mathbb{N}}$. The input signal during these experiments is where $F$ renders the system stable^11^1Access to a stabilizing controller is often assumed unstable system identification Ljung. Open-loop unstable identification leads to poor conditioning., i.e. ${\rho{({{A{(\theta)}} + {B{(\theta)}F}})}} < 1$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Meanwhile, ${\overset{\sim}{U}}_{t,n}$ is an exploration component with energy budget $\sigma_{\overset{\sim}{u}}^{2}NT$,^22^2The choice to place a budget on the exploratory input ${\overset{\sim}{U}}_{t,n}$ rather than the total input $U_{t,n}$ is for ease of exposition. The energy of the exploratory input is bounded by the total budget, which is sufficient for our bounds. where $\sigma_{\overset{\sim}{u}} \in {\mathbb{R}}_{+}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

More precisely, ${\overset{\sim}{U}}_{t,n}$ may be selected as a function of past observations $(X_{0,n},\ldots,X_{t,n})$, past trajectories ${{(X_{0,m},\ldots,X_{{T - 1},m})},m} < n$ and possible auxiliary randomization, while being constrained to an energy budget This formulation allows both open- and closed-loop experiments, but normalizes the average exploratory input energy to $\sigma_{\overset{\sim}{u}}^{2}$. The subscript $\theta$ on the expectation denotes that the system is rolled out with parameter $\theta$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The learner deploys a policy $\pi$ which is a measureable function of the $N$ offline experiments and the current state. In particular, the learner maps the offline data and the current state to the control input, $U_{t} = {\pi{(X_{t};\mathcal{Z})}}$. This is the case if the learner outputs a non-adaptive state feedback controller designed with the offline data. The goal of the learner is to minimize the cost defined: The expectation is over both the offline experiments, and a new evaluation rollout. Single subscripts on the states and actions, $X_{t}$ and $U_{t}$, refer to the evaluation rollout at time $t$. The superscript on the expectation denotes that the inputs applied in the evaluation rollout follow the policy $U_{t} = {\pi{(X_{t};\mathcal{Z})}}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Note that due to the dependence of the terminal cost $Q_{T}{(\theta)}$ on the unknown parameter $\theta$, the learner does not explicitly know the cost function it is minimizing. This is not an issue: it simply means that the learner must infer the objective function from the collected data.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The following assumption guarantees the existence of a static state feedback controller that minimizes $V_{T}^{\pi}{(\theta)}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 1.1", "weight": 1.0} -->

Under this assumption, the optimal policy for the known system is $U_{t} = {K{(\theta)}X_{t}}$, where $K{(\theta)}$ is the LQR: In light of this, we focus on the case in which the search space of the learner is the class of linear time-invariant state feedback policies where the gain is a measurable function of the past $N$ experiments^33^3This assumption is not critical, and may be removed without significantly changing the result. See the proof of the main result in Ziemann and Sandberg for details on how to remove this assumption.. This set is denoted $\Pi_{\mathsf{l}\mathsf{i}\mathsf{n}}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 1.1", "weight": 1.0} -->

The stochastic LQR cost $V_{T}^{\pi}{(\theta)}$ may be represented in terms of the gap between the control actions taken by the policy $\pi$ and the optimal policy, as shown below.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Contributions", "weight": 1.0} -->

Our main contribution is the following theorem. For the formal statements, see Theorem 2.2 and Corollary 2.1.

<!-- chunk {"id": "body-0017", "role": "body", "section": "System Identification", "weight": 1.0} -->

System identification is often a first step in designing a controller from experimental data, and has a longstanding history. The text Ljung covers classic asymptotic results. Control oriented identification was studied in Chen and Nett; Helmicki et al.. Recently, there has been interest in finite sample analysis for fully-observed linear systems, and partially-observed linear systems. Lower bounds for the sample complexity of system identification are presented in Jedra and Proutiere; Tsiamis and Pappas. For a more extensive discussion of prior work, we refer to the survey by Tsiamis et al..

<!-- chunk {"id": "body-0018", "role": "body", "section": "Learning Controllers Offline", "weight": 1.0} -->

Learning a controller from offline data is a familiar paradigm for control theorist and practitioners. It typically consists of system identification, followed by robust or certainty-equivalent control design, see Figure 2. Recent work provides finite sample guarantees for such methods. Upper and lower bounds on the sample complexity of stabilization from offline data are presented in Tsiamis et al.. The RL community has a similar paradigm, known as offline RL. Policy gradient approaches are a model-free algorithm suitable for offline RL, and are analyzed in Fazel et al.. Lower bounds on the variance of the gradient estimates in policy gradient approaches are supplied in Ziemann et al.. Lower bounds for offline linear control are also studied in Wagenmaker et al. with the objective of designing optimal experiments. We instead focus on the LQR setting to understand the dependence of the excess cost on interpretable system-theoretic quantities.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Online LQR", "weight": 1.0} -->

The problem of learning the optimal LQR controller online has a rich history beginning with Åström and Wittenmark. Regret minimization was introduced in Lai; Lai and Wei. The study of regret in online LQR was re-initiated by Abbasi-Yadkori and Szepesvári, inspired by works in the RL community. Many works followed to propose algorithms which were computationally tractable. Lower bounds on the regret of online LQR are presented in Simchowitz and Foster; Cassel et al.; Ziemann and Sandberg. The results in this paper follow a similar proof to Ziemann and Sandberg. The primary difference is that since our controller is designed via offline data, we may not make use of the exploration-exploitation tradeoff to upper bound the information available to the learner, as is done in Ziemann and Sandberg.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Excess Cost Lower Bound", "weight": 1.0} -->

We now proceed to establish our lower bound. As we are interested in the worst-case excess cost from any element of $\mathcal{B}{(\theta,\varepsilon)}$, we make the additional assumption that $F$ stabilizes $({A{(\theta')}},{B{(\theta')}})$ for all $\theta' \in {\mathcal{B}{(\theta,\varepsilon)}}$.^44^4We ultimately study the limit as $\varepsilon$ becomes small. Therefore, this is not significantly stronger than assuming that $F$ stabilizes (${A{(\theta)}},{B{(\theta)}}$). This also ensures that the optimal LQR controller exists for all points in the prior.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Excess Cost Lower Bound", "weight": 1.0} -->

To obtain a lower bound on the local minimax excess cost, we lower bound the maximization over $\theta' \in {\mathcal{B}{(\theta,\varepsilon)}}$ by an average over a distribution supported on $\mathcal{B}{(\theta,\varepsilon)}$. This reduces the problem to lower bounding a Bayesian complexity. Instead of fixing the parameter $\theta$, we let $\Theta$ be a random vector taking values in ${\mathbb{R}}^{d_{\Theta}}$ and suppose that it has prior density $\lambda$. Doing so enables the use of information theoretic tools to lower bound the complexity of estimating the parameter from data. The relaxation of the the maximization is shown in the following lemma.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

The prior $\lambda$ is smooth with compact support.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

The conditional density of $\mathcal{Z}$ given $\Theta$, $p{(\left. z \middle| \cdot \right.)}$, is continuously differentiable on the domain of $\lambda$ for almost every $z$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

${\mathsf{v}\mathsf{e}\mathsf{c}}K$ is differentiable on the domain of $\lambda$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

The following theorem is a less general adaption from Bobrovsky et al. which suffices for our needs.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Consequences of the Lower Bound", "weight": 1.0} -->

In this section, we examine cases where the bound in Corollary 2.1 has interpretable dependence upon system properties. To do so, we restrict attention to the setting where all system parameters are unknown, i.e. ${{\mathsf{v}\mathsf{e}\mathsf{c}}\begin{bmatrix} \end{bmatrix}} = \theta$. In this setting, the quantity $\mathsf{D}_{\theta}{{\mathsf{v}\mathsf{e}\mathsf{c}}\begin{bmatrix} \end{bmatrix}}$ arising in the bounds from the previous section is the identity matrix.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Consequences of the Lower Bound", "weight": 1.0} -->

The derivative of the controller multiplied by a matrix with orthonormal columns, ${\mathsf{D}_{\theta}{{\mathsf{v}\mathsf{e}\mathsf{c}}K}}{(\theta)}V$, arises in the bounds from the previous section. In this section, this quantity is expressed in terms of the directional derivative of the controller in some direction $v$, denoted $d_{v}K{(\theta)}$. In particular, we represent the columns of $V$ as $v = {{\mathsf{v}\mathsf{e}\mathsf{c}}\begin{bmatrix} \end{bmatrix}}$ for arbitrary perturbations $\Delta_{A}$ of $A$ and $\Delta_{B}$ of $B$ which satisfy $\left\| \begin{bmatrix} \end{bmatrix} \right\|_{F} = 1$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Consequences of the Lower Bound", "weight": 1.0} -->

The corresponding change in the closed-loop state matrix is denoted $\Delta_{A_{cl}} = {\Delta_{A} + {\Delta_{B}K}}$. Then the directional derivative of the controller is shown in Lemma B.1 of Simchowitz and Foster to be where $P' = {\text{dlyap}{(A_{cl},{{A_{cl}^{\top}P\Delta_{A_{cl}}} + {\Delta_{A_{cl}}^{\top}PA_{cl}}})}}$. The subsequent sections study the bound from Corollary 2.1 under various perturbations $\begin{bmatrix} \end{bmatrix}$. Proofs are deferred to Appendix B.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Dimensional dependence", "weight": 1.0} -->

In the setting of online LQR for an unknown system, recent works obtaining lower bounds on the regret have used perturbation directions which cause tension between identification and control. In particular, they considered the set of perturbation directions For all such perturbations, $\Delta_{A_{cl}} = 0$, making it impossible to distinguish between the true parameters and the perturbed parameters online without sufficient exploratory input noise.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Dimensional dependence", "weight": 1.0} -->

While the tension between identification and control is no longer present in the offline setting, this set of perturbation directions retains the benefit that the directional derivative in is easy to work. In particular for any $v = {{\mathsf{v}\mathsf{e}\mathsf{c}}\begin{bmatrix} \end{bmatrix}} \in \mathbf{\Delta}$, As the matrices $\Delta$ parametrizing the set $\mathbf{\Delta}$ are $d_{\mathsf{X}} \times d_{\mathsf{U}}$ dimensional, we may stack $d_{\mathsf{X}}d_{\mathsf{U}}$ orthogonal vectors $v_{i}$ belonging $\mathbf{\Delta}$ into a matrix $V = \begin{bmatrix} v_{1} & \ldots & v_{d_{\mathsf{X}}d_{\mathsf{U}}} \end{bmatrix}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Dimensional dependence", "weight": 1.0} -->

This allows us to present a lower bound which demonstrates the dependence of the offline LQR problem upon the system dimensions $d_{\mathsf{X}}$ and $d_{\mathsf{U}}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 3.1", "weight": 1.0} -->

The dimensional dependence $d_{\mathsf{X}}d_{\mathsf{U}}$ in the above bound is optimal up to constant factors when $d_{\mathsf{U}} \leq d_{\mathsf{X}}$. To see that this is so, observe that Theorem 2 of Mania et al. demonstrates an upper bound on the excess cost that scales as $d_{\mathsf{U}}\varepsilon^{2}$, where $\varepsilon^{2}$ bounds the system identification error, $\max\left\{ \left\| {\hat{A} - A} \right\|^{2},\left\| {\hat{B} - B} \right\|^{2} \right\}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 3.1", "weight": 1.0} -->

A consequence of Theorem 5.4 in Tu et al. is that if we apply exploratory inputs which are generated from a Gaussian distribution with mean zero and covariance $\sigma_{\overset{\sim}{u}}^{2}I$, then the upper bound on the system identification error scales as $\frac{d_{\mathsf{X}} + d_{\mathsf{U}}}{NT}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 3.1", "weight": 1.0} -->

Consequently, the upper bound on the excess cost scales with $\frac{d_{\mathsf{U}}{({d_{\mathsf{X}} + d_{\mathsf{U}}})}}{NT} \lesssim \frac{d_{\mathsf{X}}d_{\mathsf{U}}}{NT}$ in the underactuated setting. Therefore, for classes of systems where the remaining system-theoretic quantities are constant with respect to system dimension, the bound is optimal in the dimension.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Exponential Lower Bounds", "weight": 1.0} -->

The previous section demonstrated a lower bound that scales linearly with $d_{\mathsf{X}}d_{\mathsf{U}}$. Prior work has shown that in the setting of online LQR, there exist classes of systems where the lower bounds on the regret may scale exponentially with the state dimension. This is shown by demonstrating that particular system-theoretic terms, which are often treated as constant with respect to dimension, may actually grow exponentially with the state dimension. We demonstrate that in the setting of offline LQR, such systems still cause exponential dependence on dimension. Furthermore, because there are fewer restrictions upon the perturbation directions in the lower bound for the offline setting, we construct a simpler class of a systems which exhibits this behavior. In particular, consider the system with $0 < \rho < 1$, $F = 0$, $Q = I$, $R = 1$, and $\Sigma_{W} = I$. Let $V = {{\mathsf{v}\mathsf{e}\mathsf{c}}\begin{bmatrix} \end{bmatrix}}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Exponential Lower Bounds", "weight": 1.0} -->

Then the quantity $L{(\theta)}$ in Corollary 2.1 becomes $8\sigma_{\overset{\sim}{u}}^{2}$, as ${\nu_{1}{(V)}} = 0$. Meanwhile, (using the option $\Gamma = \Sigma_{W} = I$), the quantity $G$ becomes Using this insight, we may show that the lower bound grows exponentially with the system dimension.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Interesting System-Theoretic Quantities", "weight": 1.0} -->

A consequence of the result in Section 3.2 is that treating system-theoretic quantities as constant with respect to dimension, as is done in Remark 3.1, may fail to capture the difficulty of the problem. This leads to unfavorable aspects of the lower bound in Remark 3.1, such as the dependence of the denominator on $\left\| K \right\|$. Such an appearance indicates that for systems where the optimal LQR has a large gain, the lower bound becomes small. This is in contrast to our expectations, as a large optimal gain is often indicative of poor controllability (consider a scalar system, with $B\rightarrow 0$).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented lower bounds for offline linear-quadratic control problems. The focus was to understand the fundamental limitations of learning controllers from offline data in terms of system-theoretic properties. Several interesting consequences arose, such as the fact that our lower bound achieves the optimal dimensional dependence $d_{\mathsf{X}}d_{\mathsf{U}}$ for underactuated systems. We also showed that there exist classes of systems where the sample complexity is exponential with the system dimension, $d_{\mathsf{X}}$. We finally demonstrated that the lower bound scales in a natural way with familiar system-theoretic constants including the eigenvalues of the Riccati solution. An avenue for future work is extension of the lower bounds to the partially observed setting.
