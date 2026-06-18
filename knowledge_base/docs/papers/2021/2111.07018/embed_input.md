<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Identification and Adaptive Control of Markov Jump Systems: Sample Complexity and Regret Bounds

Topics include Markov jump systems, System identification, Adaptive control, Regret bounds, Sample complexity, Certainty equivalence.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Combines identification of Markov jump linear dynamics with episodic certainty-equivalent control and regret analysis. The paper is valuable because it handles both mode-dependent dynamics and transition learning from a single trajectory, then translates estimation rates into adaptive-control guarantees.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Learning how to effectively control unknown dynamical systems is crucial for intelligent autonomous systems. This task becomes a significant challenge when the underlying dynamics are changing with time. Motivated by this challenge, this paper considers the problem of controlling an unknown Markov jump linear system (MJS) to optimize a quadratic objective. By taking a model-based perspective, we consider identification-based adaptive control of MJSs. We first provide a system identification algorithm for MJS to learn the dynamics in each mode as well as the Markov transition matrix, underlying the evolution of the mode switches, from a single trajectory of the system states, inputs, and modes. Through martingale-based arguments, sample complexity of this algorithm is shown to be O(1/sqrt(T)). We then propose an adaptive control scheme that performs system identification together with certainty equivalent control to adapt the controllers in an episodic fashion. Combining our sample complexity results with recent perturbation results for certainty equivalent control, we prove that when the episode lengths are appropriately chosen, the proposed adaptive control scheme achieves O(sqrt(T)) regret, which can be improved to O(polylog(T)) with partial knowledge of the system.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our proof strategy introduces innovations to handle Markovian jumps and a weaker notion of stability common in MJSs. Our analysis provides insights into system theoretic quantities that affect learning accuracy and control performance. Numerical simulations are presented to further reinforce these insights.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A canonical problem at the intersection of machine learning and control is that of adaptive control of an unknown dynamical system. An intelligent autonomous system is likely to encounter such a task; from an observation of the inputs and outputs, it needs to both learn and effectively control the dynamics. A commonly used control paradigm is the Linear Quadratic Regulator (LQR), which is theoretically well understood when system dynamics are linear and known. LQR also provides an interesting benchmark, when system dynamics are unknown, for reinforcement learning (RL) with continuous state and action spaces and for adaptive control.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A generalization of linear dynamical systems called Markov jump linear systems (MJSs) models dynamics that switch between multiple linear systems, called modes, according to an underlying finite Markov chain. MJS allows for modeling a richer set of problems where the underlying dynamics can abruptly change over time. One can, similarly, generalize the LQR paradigm to MJS by using mode-dependent cost matrices, which allow different control goals under different modes. While the MJS-LQR problem is also well understood when one has perfect knowledge of the system dynamics, in practice, it is not always possible to have a perfect knowledge of the system dynamics and the Markov transition matrix. For instance, a Mars rover optimally exploring an unknown heterogeneous terrain, optimal solar power generation on a cloudy day, or controlling investments in financial markets may be modeled as MJS-LQR problems with unknown system dynamics.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Earlier works have aimed at analyzing the asymptotic properties (i.e., stability) of adaptive controllers for unknown MJSs both in continuous-time and discrete-time settings, however, despite the practical importance of MJSs, non-asymptotic sample complexity results and regret analysis for MJSs are lacking. The high-level challenge here is the hybrid nature of the problem that requires consideration of both the system dynamics and the underlying Markov transition matrix. A related challenge is that, typically, the stability of MJS is understood only in the *mean-square sense*. This is in stark contrast to the deterministic stability (e.g., as in LQR), where the system is guaranteed to converge towards an equilibrium point in the absence of noise. In contrast, the convergence of MJS trajectories towards an equilibrium depends heavily on how the switching between modes occurs. Figure 1 shows an example (adapted from ) of an MJS that is stable in the mean-square sense despite having an unstable mode. Clearly, under an unfavorable mode switching sequence, the system trajectory can still blow up.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

High-probability light tail bounds are therefore not applicable without very strong assumptions on the joint spectral radius of different modes (cf. ). Perhaps more surprisingly, there are examples of MJS with all modes individually stable, however due to switching, the system exhibits an unstable behavior on average, and the MJS is not mean-square stable (see Example 3.17 of ). Therefore, finding controllers to individually stabilize the mode dynamics does not guarantee that overall system will be stable when mode switches over time. This more relaxed notion of *mean-square stability* presents major challenges in learning, controlling, and statistical analysis.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we provide the first comprehensive system identification and regret guarantees for learning and controlling Markov jump linear systems using a single trajectory while assuming only mean-square stability (see Def. 3.1 ‣ 3.1 Markov Jump Linear Systems ‣ 3 Preliminaries and Problem Setup ‣ Identification and Adaptive Control of Markov Jump Systems: Sample Complexity and Regret Bounds")). Importantly, our guarantees are optimal in the trajectory length $T$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

System identification: For an MJS with $s$ modes, the system dynamics involve a Markov transition matrix $\mathbf{T} \in {\mathbb{R}}^{s \times s}$ and $s$ state-input matrix pairs ${(\mathbf{A}_{i},\mathbf{B}_{i})}_{i = 1}^{s}$. We provide an algorithm (Alg. 1) to estimate these dynamics with an error rate of $\mathcal{O}{({{({n + p})}{\log{(T)}}\sqrt{s/T}})}$, where $n$ and $p$ are the state and input dimensions respectively, and the $\mathcal{O}{({1/\sqrt{T}})}$ dependence on the trajectory length $T$ is optimal.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

$\mathcal{O}{(\sqrt{T})}$-regret bound: We employ our system identification guarantees for the MJS-LQR. When the system dynamics are unknown, we show that the certainty-equivalent adaptive MJS-LQR Algorithm (Alg. 2) achieves a regret bound of $\mathcal{O}{(\sqrt{T})}$. Remarkably, this coincides with the optimal regret bound for the standard LQR problem obtained via certainty equivalence.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

$\mathcal{O}{({\text{polylog}{(T)}})}$-regret with partial knowledge: We also consider the practically relevant setting where the state matrices are unknown but the input matrices are known. We show that the regret bound can be significantly improved to $\mathcal{O}{({\text{polylog}{(T)}})}$. This bound also coincides with the polylogarithmic regret bound for the standard LQR with the knowledge of the input matrix $\mathbf{B}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Technical tools: Besides these key contributions to MJS control, our proof strategy introduces multiple innovations. To address Markovian mode transitions, we introduce a mixing-time argument to jointly track the approximate-dependence across the states and the modes. This in turn helps ensure each mode has sufficient samples and these samples are sufficiently informative. Secondly, as clarified further below, due to mean-square stability and mode transitions, it becomes non-trivial to determine whether the states have a light-tailed distribution (e.g., sub-gaussian or sub-exponential). To circumvent this, we develop intricate system identification arguments that allow for heavy-tailed states. Such arguments can potentially benefit other RL problems with heavy-tailed data.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Markov Jump Linear Systems", "weight": 1.0} -->

In this paper we consider the identification and adaptive control of MJSs which are governed by the following state equation,

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The MJS in (3.1) has ergodic Markov chain and is stabilizable.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Ergodicity guarantees that the distribution of $\omega{(t)}$ converges to a unique strictly positive stationary distribution \[27, Theorem 4.3.5\]. Throughout, we let ${\mathbf{π}}_{\infty}$ denote the stationary distribution of $\mathbf{T}$ and $\pi_{\min}:={{\min_{i}{\mathbf{π}}_{\infty}}{(i)}}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

In our analysis, ergodicity and $t_{MC}$ ensures that the MJS trajectory could have enough "visits" to every mode $i \in {\lbrack s\rbrack}$ thus providing us enough data to learn ${\lbrack\mathbf{T}\rbrack}_{i,:}$, $\mathbf{A}_{i}$ and $\mathbf{B}_{i}$. On the other hand, stability (or stabilizability) characterized by the spectral radius of $\overset{\sim}{\mathbf{L}}$ guarantees the convergence/mixing of $\mathbf{x}_{t}$, which allows us to obtain weakly dependent sub-trajectories from a single trajectory of MJS, upon which the sample complexity of learning the matrices $\mathbf{A}_{1:s}$ and $\mathbf{B}_{1:s}$ can be established.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

In this work we consider two major problems under the MJS setting: System identification and adaptive control, with identification being the core part of adaptive control.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

\(A\) System Identification. This problem seeks to estimate unknown system dynamics from data, i.e. from input-output trajectory(ies), when one has the flexibility to design the inputs so that the collected data has nice statistical properties. In the MJS setting, one needs to estimate both the state/input matrices $\mathbf{A}_{1:s},\mathbf{B}_{1:s}$ for every mode $i \in {\lbrack s\rbrack}$ as well as the Markov transition matrix $\mathbf{T}$. In this work, we seek to estimate the MJS dynamics from a single trajectory of states, inputs and mode observations ${\{\mathbf{x}_{t},\mathbf{u}_{t},{\omega{(t)}}\}}_{t = 0}^{T}$ and provide finite sample guarantees. As mentioned earlier, MJS presents unique statistical analysis challenges due to Markovian jumps and a weaker notion of stability. Section 4 presents our system identification guarantees overcoming these challenges.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

These guarantees are further integrated into model-based control for MJS-LQR in Section 5.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Here, the goal is to design control inputs to minimize the expected quadratic cost function composed of positive semi-definite cost matrices $\mathbf{Q}_{1:s}$ and $\mathbf{R}_{1:s}$ under the MJS dynamics (3.1). The quadratic cost incurred by the state $\mathbf{x}_{t}$ represents the deviation from target values, e.g. desired velocity, position, angle, etc., whereas, the quadratic term in $\mathbf{u}_{t}$ represents the control effort, e.g. energy consumption. The flexibility of having mode-dependent cost matrices allows one to design different control requirements or trade-offs under different circumstances. For the MJS-LQR problem (3.3), we assume the following.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Assumptions 1 and 2 together guarantee the solvability of MJS-LQR when the dynamics are known \[14, Corollary A.21\]. In the remaining of the paper, we use MJS-LQR$(\mathbf{A}_{1:s},\mathbf{B}_{1:s},\mathbf{T},\mathbf{Q}_{1:s},\mathbf{R}_{1:s})$ to denote MJS-LQR problem (3.3) composed of MJS($\mathbf{A}_{1:s},\mathbf{B}_{1:s},\mathbf{T}$) and cost matrices $\mathbf{Q}_{1:s},\mathbf{R}_{1:s}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Recall our assumption that the states $\mathbf{x}_{t}$ and the modes $\omega{(t)}$ can be observed at time $t \geq 0$. With these observations, instead of a fixed and open-loop input sequence, one can design closed-loop policies that generate real-time control inputs based on the current observations, e.g. mode-dependent state-feedback controllers. When the dynamics $\mathbf{A}_{1:s},\mathbf{B}_{1:s},\mathbf{T}$ of the MJS are known, one can solve for the optimal controllers recursively via coupled discrete-time algebraic Riccati equations. In this work, we assume the dynamics are unknown, and only the design parameters $\mathbf{Q}_{1:s}$ and $\mathbf{R}_{1:s}$ are known. Control schemes in this scenario are typically referred to as adaptive control, which usually involves procedures of learning, either the dynamics or directly the controllers.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Adaptive control suffers additional costs as (i) the lack of the exact knowledge of the system and (ii) the exploration-exploitation trade-off -- the necessity to sacrifice short-term input optimality to boost learning, so that overall long-term optimality can be improved.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Because of this, to evaluate the performance of an adaptive scheme, one is interested in the notion of regret -- how much more cost it will incur if one could have applied the optimal controllers? In our setting, we compare the resulting cost against the optimal cost $T \cdot J^{\star}$ where $J^{\ast}$ is the optimal infinite-horizon average cost

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

i.e., if one applies the optimal controller for infinitely long, how much cost one would get on average for each single time step. Compared to the regret analysis of standard adaptive LQR problem, in MJS-LQR setting, the cost analysis requires additional consideration of Markov chain mixing, which is addressed in this paper.

<!-- chunk {"id": "body-0027", "role": "body", "section": "System Identification for MJS", "weight": 1.0} -->

Our MJS identification procedure is given in Algorithm 1. We assume one has access to an initial stabilizing controller $\mathbf{K}_{1:s}$, which is a standard assumption in data-driven control for LTI systems. For MJSs, a thorough discussion on the validity of this assumption is provided in Section 6.1. Note that, if the open-loop MJS is already MSS, then one can simply set $\mathbf{K}_{1:s} = 0$ and carry out MJS identification.

<!-- chunk {"id": "body-0028", "role": "body", "section": "System Identification for MJS", "weight": 1.0} -->

This sub-sampling is required because of the mean-square stability, which can at most guarantee that the states are bounded in expectation. As a result of sub-sampling only bounded states/excitations, we obtain samples with manageable distributional properties. After appropriate scaling, we regress over these samples to obtain the estimates ${\hat{\mathbf{A}}}_{i},{\hat{\mathbf{B}}}_{i}$ for each $i \in {\lbrack s\rbrack}$. Lastly, using the empirical frequency of observed modes, we obtain the estimate $\hat{\mathbf{T}}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "System Identification for MJS", "weight": 1.0} -->

The following theorem gives our main results on learning the dynamics of an unknown MJS from finite samples obtained from a single trajectory. One can refer to Theorems B.1 and B.17 ‣ B.2.4 Finalizing the SYSID: Proof of Theorem 4.1 ‣ B.2 Estimation of 𝐀_{1:𝑠} and 𝐁_{1:𝑠} from a Single Trajectory (Main SYSID Analysis) ‣ Appendix B Sys ID Analysis ‣ Identification and Adaptive Control of Markov Jump Systems: Sample Complexity and Regret Bounds") in Appendix 4 for the detailed theorem statements and proofs.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Adaptive Control for MJS-LQR", "weight": 1.0} -->

Our adaptive MJS-LQR control scheme is given in Algorithm 2. It is performed on an epoch-by-epoch basis; a fixed controller is used for each epoch, and from epoch to epoch, the controller is updated using a newly collected MJS trajectory. Note that a new epoch is just a continuation of previous epochs instead of restarting the MJS. Similar to the discussion in Section 4, we assume, at the beginning of epoch $0$, that one has access to a stabilizing controller $\mathbf{K}_{1:s}^{}$. During epoch $i$, the controller $\mathbf{K}_{1:s}^{(i)}$ is used together with additive exploration noise $\mathbf{z}_{t}^{(i)}\overset{\text{i.i.d.}}{\sim}\mathcal{N}{(0,{\sigma_{\mathbf{z},i}^{2}\mathbf{I}_{p}})}$ to boost learning.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Adaptive Control for MJS-LQR", "weight": 1.0} -->

At the end of epoch $i$, the trajectory during that epoch is used to obtain a new MJS dynamics estimate $\mathbf{A}_{1:s}^{(i)},\mathbf{B}_{1:s}^{(i)},\mathbf{T}^{(i)}$ using Algorithm 1.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Adaptive Control for MJS-LQR", "weight": 1.0} -->

For a generic infinite-horizon MJS-LQR($\mathbf{A}_{1:s},\mathbf{B}_{1:s},\mathbf{T},\mathbf{Q}_{1:s},\mathbf{R}_{1:s}$), its optimal controller is given by $\mathbf{K}_{1:s}$ such that for all $j \in {\lbrack s\rbrack}$,

<!-- chunk {"id": "body-0033", "role": "body", "section": "Adaptive Control for MJS-LQR", "weight": 1.0} -->

for all $j \in {\lbrack s\rbrack}$. In practice, cDARE can be solved efficiently via value iteration or LMIs. Note that cDARE may not be solvable for arbitrary parameters, but our theory guarantees that when epoch lengths are appropriately chosen, cDARE parameterized by $\mathbf{A}_{1:s}^{(i)},\mathbf{B}_{1:s}^{(i)},\mathbf{T}^{(i)},\mathbf{Q}_{1:s},\mathbf{R}_{1:s}$ is solvable for every epoch $i$. This control design based on the estimated dynamics is also referred to as certainty equivalent control.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Adaptive Control for MJS-LQR", "weight": 1.0} -->

To achieve theoretically guaranteed performance, i.e., sub-linear regret, the key is to have a subtle scheduling of epoch lengths $T_{i}$ and exploration noise variance $\sigma_{\mathbf{z},i}^{2}$. We choose $T_{i}$ to increase exponentially with rate $\gamma > 1$, and set $\sigma_{\mathbf{z},i}^{2} = {\sigma_{\mathbf{w}}^{2}/\sqrt{T_{i}}}$, which collectively guarantee $\overset{\sim}{\mathcal{O}}{(\sqrt{T})}$ regret when combined with the system identification result from Theorem 4.1 ‣ 4 System Identification for MJS ‣ Identification and Adaptive Control of Markov Jump Systems: Sample Complexity and Regret Bounds").

<!-- chunk {"id": "body-0035", "role": "body", "section": "Adaptive Control for MJS-LQR", "weight": 1.0} -->

Intuitively, this scheduling can be interpreted as follows: (i) the increase of epoch lengths guarantees we have more accurate MJS estimates thus more optimal controllers; (ii) as the controller becomes more optimal we can gradually decrease the exploration noise and deploy (exploit) the controller for a longer time. Note that the scheduling rate $\gamma$ has a similar role to the discount factor in reinforcement learning: smaller $\gamma$ aims to reduce short-term cost while larger $\gamma$ aims to reduce long-term cost.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Adaptive Control for MJS-LQR", "weight": 1.0} -->

Input: Initial epoch length T0; initial stabilizing controller K1: s; epoch incremental ratio γ &gt; 1; and data clipping thresholds cx, cz
2 Set epoch length Ti = ⌊T0 γi⌋. 3 Set exploration noise variance $\sigma_{\mathbf{z},i}^{2} = \frac{\sigma_{\mathbf{w}}^{2}}{\sqrt{T_{i}}}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Adaptive Control for MJS-LQR", "weight": 1.0} -->

4 Evolve the MJS for Ti steps with ut(i) = Kω (t)(i)(i) xt(i) + zt(i) with $\mathbf{z}_{t}^{(i)}\overset{\text{i.i.d.}}{\sim}\mathcal{N}{(0,{\sigma_{\mathbf{z},i}^{2}\mathbf{I}_{p}})}$ and record the trajectory {xt(i), zt(i), ω(i) (t)}t = 0Ti. 6 Set the controller K1: s(i+1) for the next epoch to be the optimal controller for the infinite-horizon MJS-LQR(A1: s(i), B1: s(i), T(i), Q1: s, R1: s). Algorithm 2 Adaptive MJS-LQR

<!-- chunk {"id": "body-0038", "role": "body", "section": "Regret Analysis", "weight": 1.0} -->

and cumulative cost as $J_{T} = {\sum_{t = 1}^{T}c_{t}}$. We define the total regret and epoch-$i$ regret as

<!-- chunk {"id": "body-0039", "role": "body", "section": "Regret Analysis", "weight": 1.0} -->

Please refer to Theorem C.11 ‣ C.3.1 Proof for Theorem 5.1 ‣ C.3 Stitching Every Epoch ‣ Appendix C MJS Regret Analysis ‣ Identification and Adaptive Control of Markov Jump Systems: Sample Complexity and Regret Bounds") in the appendix for the complete version and proof.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Tighter probability bound under uniform stability", "weight": 1.0} -->

Note that the regret upper bound (5.5 ‣ 5.1 Regret Analysis ‣ 5 Adaptive Control for MJS-LQR ‣ Identification and Adaptive Control of Markov Jump Systems: Sample Complexity and Regret Bounds")) in Theorem 5.1 ‣ 5.1 Regret Analysis ‣ 5 Adaptive Control for MJS-LQR ‣ Identification and Adaptive Control of Markov Jump Systems: Sample Complexity and Regret Bounds") has the second term depending on the failure probability $\delta$ through $\frac{1}{\delta}$. Though this term has a much milder dependency on the time horizon $T$, when setting $\delta$ to be small, it can still easily outweigh the other $\overset{\sim}{\mathcal{O}}{( \cdot )}$ term in (5.5 ‣ 5.1 Regret Analysis ‣ 5 Adaptive Control for MJS-LQR ‣ Identification and Adaptive Control of Markov Jump Systems: Sample Complexity and Regret Bounds")), which only has $\log{(\frac{1}{\delta})}$ dependency, and can result in overly pessimistic regret bounds.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Tighter probability bound under uniform stability", "weight": 1.0} -->

Furthermore, in Appendix C.4, we construct an MJS example that is MSS but no dependencies better than $\frac{1}{\delta}$ can be established. Fortunately, there exists an easy workaround to get rid of this $\frac{1}{\delta}$ dependency if the MJS is uniformly stable, which enforces stability under arbitrary switching sequences thus is stronger than MSS. It allows us to bound $\mathbf{x}_{0}^{(i)}$ using tail inequalities much tighter than the Markov inequality and obtain ${\|\mathbf{x}_{0}^{(i)}\|}^{2} \leq {\mathcal{O}{({\log{(\frac{1}{\delta})}})}}$. In the end, in the regret bound, $\frac{1}{\delta}$ can be improved to $\log{(\frac{1}{\delta})}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Tighter probability bound under uniform stability", "weight": 1.0} -->

One type of uniform stability assumption that can help us in this case is regarding the closed-loop MJS under the optimal controllers. We let $\mathbf{K}_{1:s}^{\star}$ denote the optimal controller for the infinite-horizon MJS-LQR($\mathbf{A}_{1:s},\mathbf{B}_{1:s},\mathbf{T},\mathbf{Q}_{1:s},\mathbf{R}_{1:s}$) and define closed-loop state matrices $\mathbf{L}_{i}^{\star} = {\mathbf{A}_{i} + {\mathbf{B}_{i}\mathbf{K}_{i}^{\star}}}$ for all $i \in {\lbrack s\rbrack}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Tighter probability bound under uniform stability", "weight": 1.0} -->

The resulting regret bound is outlined in the following theorem, with its complete version and proof provided in Theorem C.12 ‣ C.4.1 Proof for Theorem 5.2 ‣ C.4 Regret Under Uniform Stability — Proof for Theorem 5.2 ‣ Appendix C MJS Regret Analysis ‣ Identification and Adaptive Control of Markov Jump Systems: Sample Complexity and Regret Bounds") of Appendix C.4.1.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Partial knowledge of dynamics", "weight": 1.0} -->

From Corollary 4.2, we know that when input matrices $\mathbf{B}_{1:s}$ are known, no further exploration noise is needed to identify the state matrices $\mathbf{A}_{1:s}$ or Markov matrix $\mathbf{T}$. This can also be applied to the adaptive MJS-LQR setting, and the resulting regret bound can improve (from $\mathcal{O}{({{\log^{2}{(T)}}\sqrt{T}})}$ to $\mathcal{O}{({\log^{3}{(T)}})}$) since exploration noise incurs additional costs.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Partial knowledge of dynamics", "weight": 1.0} -->

The result is given by the following corollary, and we omit the proof due to its similarity to the proofs of Theorems 5.1 ‣ 5.1 Regret Analysis ‣ 5 Adaptive Control for MJS-LQR ‣ Identification and Adaptive Control of Markov Jump Systems: Sample Complexity and Regret Bounds") and 5.2 ‣ 5.2.1 Tighter probability bound under uniform stability ‣ 5.2 Two Special Cases ‣ 5 Adaptive Control for MJS-LQR ‣ Identification and Adaptive Control of Markov Jump Systems: Sample Complexity and Regret Bounds").

<!-- chunk {"id": "body-0046", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this section, we discuss how one may obtain the initial stabilizing controller for MJS as required in the input to Algorithms 1 and 2 and the application of our results to offline data-driven control.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Initial Stabilizing Controllers", "weight": 1.0} -->

Having access to an initial stabilizing controller has become a very common assumption in system identification (see for instance and references therein) and adaptive control for LTI systems. On the other hand, for work where no initial stabilizing controller is required, there is usually a separate warm-up phase at the beginning, where coarse dynamics is learned, upon which a stabilizing controller is computed. Recent non-asymptotic system identification results on potentially unstable LTI systems can be used to obtain coarse dynamics without stabilizing controller. One can use random linear feedback to construct a confidence set of the dynamics such that any point in this set can produce a stabilizing controller by solving Riccati equations. In the model-free setting, provides asymptotic results and relies on persistent excitation assumption. designs subtle scaled one-hot vector input and collects the trajectory to estimate the dynamics, then a stabilizing controller can be solved via semi-definite programming. For MJS or general switched systems, to the best of our knowledge, there is no work on stabilizing unknown dynamics using single trajectory with guarantees.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Initial Stabilizing Controllers", "weight": 1.0} -->

One challenge is, as we discussed in Section 1, the individual mode stability and overall stability does not imply each other due to mode switching. However, as outlined below, we can approach this problem leveraging what is recently done for the LTI case in the aforementioned literature (modulo some additional assumptions).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Initial Stabilizing Controllers", "weight": 1.0} -->

To investigate when ${\hat{\mathbf{K}}}_{1:s}$ can stabilize the MJS, the key is to obtain sample complexity guarantees for this coarse dynamics, i.e. dependence of estimation error $\|{{\hat{\mathbf{A}}}_{i} - \mathbf{A}_{i}}\|$, $\|{{\hat{\mathbf{B}}}_{i} - \mathbf{B}}\|$, and $\|{\hat{\mathbf{T}} - \mathbf{T}}\|$ on sample size. Fortunately provides the required estimation accuracy under which ${\hat{\mathbf{K}}}_{1:s}$ is guaranteed to be stabilizing. Thus, combining with the estimation error bounds (in terms of sample size), the required accuracy can be translated to the required number of samples.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Initial Stabilizing Controllers", "weight": 1.0} -->

Note that learning $\mathbf{T}$ is the same as learning a Markov chain, thus using the mode transition pair frequencies in an arbitrary single MJS trajectory, we can obtain an estimate $\hat{\mathbf{T}}$ as in Algorithm 1, and its sample complexity is given in Lemma B.1 in Appendix 4. The more challenging part is the identification scheme and corresponding sample complexity for ${\hat{\mathbf{A}}}_{1:s}$ and ${\hat{\mathbf{B}}}_{1:s}$. Here, we outline two potential schemes.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Initial Stabilizing Controllers", "weight": 1.0} -->

Suppose we could generate $N$ i.i.d. MJS rollout trajectories, each with length $T$ (small $T$, e.g. $T = 1$, is preferred to avoid potential unstable behavior and for the ease of the implementation). We can obtain least squares estimates ${\hat{\mathbf{A}}}_{1:s},{\hat{\mathbf{B}}}_{1:s}$ using only $\{\mathbf{x}_{T},\mathbf{x}_{T - 1},\mathbf{u}_{T - 1},{\omega{({T - 1})}}\}$ from each trajectory, which is similar to the scheme in for LTI systems. Since only i.i.d. data is used in the computation, one can easily obtain the sample complexity in terms of $N$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Initial Stabilizing Controllers", "weight": 1.0} -->

If each mode in the MJS can run in isolation (i.e. for any $i \in {\lbrack s\rbrack}$, ${\omega{(t)}} = i$ for all $t$) so that it acts as an LTI system, we could use recent advances on single-trajectory open-loop LTI system identification to obtain coarse estimates together with sample complexity for ${\hat{\mathbf{A}}}_{i}$ and ${\hat{\mathbf{B}}}_{i}$ for every mode $i$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Initial Stabilizing Controllers", "weight": 1.0} -->

We also note that while finding an initial stabilizing controller is theoretically very interesting and challenging, most results we know of are limited to simulated or numerical examples (see for instance and references therein). This is because, from a practical standpoint, an initial stabilizing controller is almost required in model-based approaches since running experiments with open-loop unstable plants can be very dangerous as the state could explode quickly.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Offline Data-Driven Control", "weight": 1.0} -->

In many scenarios, we may not be able to perform learning and control in real time due to limited onboard computing resources or measurement sensors. In this case, the dynamics is usually learned in a one-shot way at the beginning, and the resulting controller will be deployed forever without any further update. The controller suboptimality in this non-adaptive setting does not improve over time, thus the regret will increase linearly over time rather than sublinearly as in our work. The natural performance metric in this case is the time-averaged regret, which can also be viewed as the slope of the cumulative regret with respect to time. The system identification scheme and corresponding sample complexity developed in this paper can also help address this problem.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Offline Data-Driven Control", "weight": 1.0} -->

Combining our identification sample complexity result in Theorem 4.1 ‣ 4 System Identification for MJS ‣ Identification and Adaptive Control of Markov Jump Systems: Sample Complexity and Regret Bounds") with the infinite-horizon MJS-LQR perturbation result, we can easily obtain an upper bound on the suboptimality, ${\hat{J} - J^{\star}} \leq {\overset{\sim}{\mathcal{O}}\left( {{\log^{2}{(T_{0})}}/T_{0}} \right)}$, which provides the required rollout trajectory length $T_{0}$ if certain suboptimality is desired.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We provide experiments to investigate the efficiency and verify the theory of the proposed algorithms on synthetic datasets. Throughout, we show results from a synthetic experiment where entries of the true system matrices $({\mathbf{A}}_{1:s},{\mathbf{B}}_{1:s})$ were generated randomly from a standard normal distribution. We further scale each $\mathbf{A}_{i}$ to have ${\|\mathbf{A}_{i}\|} \leq 0.5$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The Markov matrix ${\mathbf{T}} \in {\mathbb{R}}_{+}^{s \times s}$ was sampled from a Dirichlet distribution $\text{Dir}{({{{({s - 1})} \cdot {\mathbf{I}}_{s}} + 1})}$, where ${\mathbf{I}}_{s}$ denotes the identity matrix. We assume that we had equal probability of starting in any initial mode.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We use ${{\|{\hat{\Psi} - \Psi}\|}/{\|\Psi\|}}:={\max_{j \in {\lbrack s\rbrack}}{{\|{{\hat{\Psi}}_{j} - \Psi_{j}}\|}/{\|\Psi_{j}\|}}}$ to investigate the convergence behaviour of MJS-SYSID Algorithm 1. The clipping constants in this algorithm, i.e., $C_{\text{sub}}$, $c_{\mathbf{x}}$, and $c_{\mathbf{z}}$ are chosen based on their lower bounds provided in Theorem 5.1 ‣ 5.1 Regret Analysis ‣ 5 Adaptive Control for MJS-LQR ‣ Identification and Adaptive Control of Markov Jump Systems: Sample Complexity and Regret Bounds"). In all the aforementioned algorithms, the depicted results are averaged over 10 independent replications.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Performance of MJS-SYSID", "weight": 1.0} -->

In this section, we investigate the performance of our MJS-SYSID method, i.e., Algorithm 1. We first empirically evaluate the effect of the noise variances $\sigma_{\mathbf{w}}$ and $\sigma_{\mathbf{z}}$. In particular, we study how the system errors vary with (i) ${\sigma_{\mathbf{w}} = 0.01},{\sigma_{\mathbf{z}} \in {\{ 0.01,0.02,0.1\}}}$ and (ii) ${\sigma_{\mathbf{z}} = 0.01},{\sigma_{\mathbf{w}} \in {\{ 0.01,0.02,0.1\}}}$. The number of states, inputs, and modes are set to $n = 5$, $p = 3$, and $s = 5$, respectively.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Performance of MJS-SYSID", "weight": 1.0} -->

Fig. 2 (a) and (b) demonstrate how the relative estimation error ${\|{\hat{\Psi} - \Psi}\|}/{\|\Psi\|}$ changes as $T$ increases. Each curve on the plot represents a fixed $\sigma_{\mathbf{w}}$ and $\sigma_{\mathbf{z}}$. These empirical results are all consistent with the theoretical bound of MJS-SYSID given in (4.1 ‣ 4 System Identification for MJS ‣ Identification and Adaptive Control of Markov Jump Systems: Sample Complexity and Regret Bounds")). In particular, the estimation errors degrade with increasing $\sigma_{\mathbf{w}}$ and decreasing $\sigma_{\mathbf{z}}$, respectively.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Performance of MJS-SYSID", "weight": 1.0} -->

Now, we fix $\sigma_{\mathbf{w}} = \sigma_{\mathbf{z}} = 0.01$ and investigate the performance of the MJS-SYSID with varying number of states, inputs, and modes. Fig. 2 (c) and (d) show how the estimation error ${\|{\hat{\Psi} - \Psi}\|}/{\|\Psi\|}$ changes with (left) $s = 5$, $n \in {\{ 5,10,20\}}$, $p = {n - 2}$ and (right) $n = 5$, $p = {n - 2}$, $s \in {\{ 5,10,20\}}$. As we can see, the MJS-SYSID has better performance with small $n$, $p$ and $s$ which is consistent with (4.1 ‣ 4 System Identification for MJS ‣ Identification and Adaptive Control of Markov Jump Systems: Sample Complexity and Regret Bounds")).

<!-- chunk {"id": "body-0062", "role": "body", "section": "Performance of Adaptive MJS-LQR", "weight": 1.0} -->

In our next series of experiments, we explore the sensitivity of the regret bounds to the system parameters. In these experiments, we set the initial epoch length $T_{0} = 2000$ and incremental ratio $\gamma = 2$. We select five epochs to run Algorithm 2. As an intermediate step for computing controller $\mathbf{K}_{1:s}^{({i + 1})}$ in Algorithm 2, the coupled Riccati equations (5.2) are solved via value iteration, and the iteration stops when the parameter variation between two iterations falls below $10^{- 6}$, or iteration number reaches $10^{4}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Performance of Adaptive MJS-LQR", "weight": 1.0} -->

Fig. 3 demonstrates how regret bounds vary with (a) $\sigma_{\mathbf{w}} \in {\{ 0.001,0.002,0.01,0.02\}}$, $n = 10$, $p = s = 5$; (b) $\sigma_{\mathbf{w}} = 0.01$, $n = 10$, $p = 5$, $s \in {\{ 4,6,8,10\}}$, and (c) $\sigma_{\mathbf{w}} = 0.01$, $s = 10$, $p = 5$, $n \in {\{ 4,6,8,10\}}$. We see that the regret degrades as $\sigma_{\mathbf{w}},n$, and $s$ increase. We also see that when $\sigma_{\mathbf{w}}$ is large ($T$ is small), the regret becomes worse quickly as $n$ and $s$ grow larger.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Performance of Adaptive MJS-LQR", "weight": 1.0} -->

These results are consistent with the theoretical bounds in Theorem 5.1 ‣ 5.1 Regret Analysis ‣ 5 Adaptive Control for MJS-LQR ‣ Identification and Adaptive Control of Markov Jump Systems: Sample Complexity and Regret Bounds").

<!-- chunk {"id": "body-0065", "role": "body", "section": "Conclusions and Discussion", "weight": 1.0} -->

Markov jump systems are fundamental to a rich class of control problems where the underlying dynamics are changing with time. Despite its importance, statistical understanding (system identification and regret bounds) of MJS have been lacking due to the technicalities such as Markovian transitions and weaker notion of mean-square stability. At a high-level, this work overcomes (much of) these challenges to provide finite sample system identification and model-based adaptive control guarantees for MJS. Notably, resulting estimation error and regret bounds are optimal in the trajectory length and coincide with the standard LQR up to polylogarithmic factors. As a future work, it would be interesting and of practical importance to investigate the case when mode is not observed, which makes both system identification and adaptive quadratic control problems non-trivial.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Conclusions and Discussion", "weight": 1.0} -->

We want to mention possible negative societal impacts. While our work is theoretical and has many potential positive impacts in reinforcement learning, robotics, and autonomous systems, there are also potential negative applications in the military (e.g. with drone control) and for malicious actors (e.g. computer network hackers), among others. Additionally, all our work was built on stochastic noise assumptions, whereas in reality intelligent autonomous systems may instead encounter adversarial behavior. There is potential here for future work to extend our approach to non-stochastic noise or even non-Markovian / non-random switching among states.
