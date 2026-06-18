<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Linear Systems Can Be Hard to Learn

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we investigate when system identification is statistically easy or hard, in the finite sample regime. Statistically easy to learn linear system classes have sample complexity that is polynomial with the system dimension. Most prior research in the finite sample regime falls in this category, focusing on systems that are directly excited by process noise. Statistically hard to learn linear system classes have worst-case sample complexity that is at least exponential with the system dimension, regardless of the identification algorithm. Using tools from minimax theory, we show that classes of linear systems can be hard to learn. Such classes include, for example, under-actuated or under-excited systems with weak coupling among the states. Having classified some systems as easy or hard to learn, a natural question arises as to what system properties fundamentally affect the hardness of system identifiability. Towards this direction, we characterize how the controllability index of linear systems affects the sample complexity of identification. More specifically, we show that the sample complexity of robustly controllable linear systems is upper bounded by an exponential function of the controllability index. This implies that identification is easy for classes of linear systems with small controllability index and potentially hard if the controllability index is large.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our analysis is based on recent statistical tools for finite sample analysis of system identification as well as a novel lower bound that relates controllability index with the least singular value of the controllability Gramian.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $x_{k}$ represents the state, $u_{k}$ represents the control signal, and $w_{k}$ is the process noise. The statistical analysis of system identification algorithms has a long history. Until recently, the main focus was providing guarantees for the convergence of system identification in the *asymptotic regime*, when the number of collected samples $N$ tends to infinity. Under sufficient persistency of excitation, system identification algorithms converge and the asymptotic bounds capture very well how the identification error decays with $N$ qualitatively.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, our standard asymptotic tools (e.g. the Central Limit Theorem), do not always capture all finite-sample phenomena \[6, Ch 2\]. Moreover, the identification error depends on various system theoretic constants, like the state space dimension $n$, which might be hidden under the big-$O$ notation in the asymptotic bounds. As a result, system identification limitations, like the curse of dimensionality, although known to practitioners, are not always reflected in the theoretical asymptotic bounds.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

With the advances in high-dimensional statistics, there has been a recent shift from asymptotic analysis with infinite data to statistical analysis of system identification with finite samples. Over the past two years there have been significant advances in understanding finite sample system identification for both fully-observed systems as well as partially-observed systems. A tutorial can be found. The above approaches offer mainly *data-independent* bounds which reveal how the state dimension $n$ and other system theoretic parameters affect the sample complexity of system identification *qualitatively*. This is different from finite sample data-dependent bounds-see for example bootstrapping or, which might be more tight and more suitable for applications but do not necessarily reveal this dependence.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite these advances, we still do not fully understand the fundamental limits of when identification is easy or hard. In this paper, we define as statistically easy, classes of systems whose finite-sample complexity is polynomial with the system dimension. Most prior research in the finite-sample analysis of fully observed systems falls in this category by assuming system is fully excited by the process noise $w_{k}$. We define as statistically hard, classes of linear systems whose worst-case sample complexity is at least exponential with the system dimension, regardless of the learning algorithm. Using recent tools from minimax theory, we show that classes of linear systems which are statistically hard to learn do indeed exist. Such system classes include, for example, under-actuated systems with weak state coupling. The fact that linear systems may contain exponentially hard classes has implications for broader classes of systems, such as nonlinear systems, as well as control algorithms, such as the linear quadratic regulator and reinforcement learning.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

By examining classes of linear systems that are statistically easy or hard, we quickly arrive at the conclusion that system theoretic properties, such as controllability, fundamentally affect the hardness of identification. In fact, as we show in the paper, structural properties like the controllability index can crucially affect learnability, determining whether a problem is hard or not.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

--Learnability of dynamical systems. We define two novel notions of learnability for classes of dynamical systems. A class of systems is easy to learn if it exhibits polynomial sample complexity with respect the state dimension $n$. It is hard to learn if for any possible learning algorithm it has exponential worst-case complexity.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

--Exponential sample complexity is possible. We identify classes of under-actuated linear systems whose worst-case sample complexity increases exponentially with the state dimension $n$ regardless of learning algorithm. These hardness results hold even for robustly controllable systems.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

--Controllability index affects sample complexity. We prove that under the least squares algorithm, the sample complexity is upper-bounded by an exponential function of the system's controllability index. This implies that if the controllability index is small $O{}$ (with respect to the dimension $n$), the sample complexity is guaranteed to be polynomial generalizing previous cases. If, however, the index grows linearly $\Omega{(n)}$, then there exist non-trivial linear systems which are exponentially hard to identify.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

--New controllability Gramian bound Our sample complexity upper bound is a consequence of a new result that is of independent, system theoretic interest. We prove that for robustly controllable systems, the least singular value of the controllability Gramian can grow at most exponentially with the controllability index. Although it has been observed empirically that the Gramian might be affected by the curse of dimensionality, to the best of our knowledge this theoretical bound is new and has implications beyond system identification.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notation: The transpose operation is denoted by ${( \cdot )}^{\prime}$ and the complex conjugate by $\ast$. By $e_{i} \in {\mathbb{R}}^{n}$ we denote the $i -$th canonical vector. By $\sigma_{\min}$ we denote the least singular value. $\succeq$ denotes comparison in the positive semidefinite cone. The identity matrix of dimension $n$ is denoted by $I_{n}$. The spectral norm of a matrix $A$ is denoted by ${\| A\|}_{2}$. The notion of controllability and other related concepts are reviewed in the Appendix.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Learnability of System Classes", "weight": 1.0} -->

Consider system, where $x_{k} \in {\mathbb{R}}^{n}$ is the state and $u_{k} \in {\mathbb{R}}^{p}$ is the input. By $w_{k} \in {\mathbb{R}}^{r}$ we denote the process noise which is assumed to be Gaussian, i.i.d. with covariance $I_{r}$. Without loss of generality the initial state is assumed to be zero $x_{0} = 0$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

All state parameters are bounded: ${{\| A\|}_{2},{\| B\|}_{2},{\| H\|}_{2}} \leq M$, for some positive constant $M > 0$. The noise has unknown dimension $r$ and can be degenerate $r \leq n$. All parameters $A,B,H,r$ are considered unknown. Matrices $B,H$ have full column rank ${{rank}{(B)}} = p \leq n$, ${{rank}{(H)}} = r \leq n$. We also assume that the system is non-explosive ${\rho{(A)}} \leq 1$. Finally, we assume that the control inputs have bounded energy ${{\mathbb{E}}u_{t}^{\prime}u_{t}} \leq M$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

This setting is rich enough to provide insights about the difficulty of the general learning problem. To simplify the setting we assume that the system is non-explosive. The analysis of unstable systems is left for future research.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

A system identification (SI) algorithm $\mathcal{A}$ receives a finite number $N$ of input-state data ${(x_{0},u_{0})},\ldots,{(x_{N},u_{N})}$ generated by system, and returns an estimate of the unknown system's parameters ${\hat{A}}_{N},{\hat{B}}_{N},{\hat{H}}_{N}$. We denote by $N$ the number of collected input-state samples, which are generated during a single roll-out of the system, that is a single trajectory of length $N$. For simplicity, we focus only on the estimation of matrix $A$ in this paper.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Our goal is to study when the problem of system identification is fundamentally easy or hard. The difficulty is captured by the sample complexity, i.e. how many data $N$ do we need to achieve small identification error with high probability. Formally, let $\epsilon > 0$, $0 < \delta < 1$ be the accuracy and confidence parameters respectively. Then, the sample complexity is the smallest possible number of samples $N$ such that with probability at least $1 - \delta$ we can estimate $A$ with small error ${\|{A - {\hat{A}}_{N}}\|} \leq \epsilon$. Naturally, the sample complexity increases as the accuracy/confidence parameters $\epsilon,\delta$ decrease. The sample complexity also increases in general with the state-space dimension $n$ and the bound $M$ on the state space parameters.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Ideally, the sample complexity should grow slowly with $n,M,\epsilon^{- 1},\delta^{- 1}$. Inspired by Provably Approximately Correct (PAC) learning, we classify an identification problem as easy when the sample complexity depends polynomially on $n,M,\epsilon^{- 1},\delta^{- 1}$. For brevity we will use the symbol $S$ to denote the tuple $S = {(A,B,H)}$. Let ${\mathbb{P}}_{S}$ denote the probability distribution of the input-state data when the true parameters of the system are equal to $S$ and we apply a control law $u_{t} \in \mathcal{F}_{t}$, where $\mathcal{F}_{t} \triangleq {\sigma{(x_{0},u_{0},\ldots,u_{t - 1},x_{t})}}$ is the sigma algebra generated by the previous outputs and inputs.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

By $\mathcal{C}_{n}$ we will denote a class of systems with dimension $n$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Question 1", "weight": 1.0} -->

Do there exist classes of linear systems which are hard to learn, meaning not $poly$-learnable by any system identification algorithm? Furthermore, can the sample complexity for a class of linear systems be exponential with state dimension $n$?

<!-- chunk {"id": "body-0022", "role": "body", "section": "Question 1", "weight": 1.0} -->

A class of linear systems $\mathcal{C}_{n}$ that is not $poly$-learnable will be viewed as hard. By negating Definition 1. ‣ 2 Learnability of System Classes ‣ Linear Systems can be Hard to Learn"), this notion of hardness means that given any system identification algorithm, there exist instances $S \in \mathcal{C}_{n}$ that cannot have polynomial sample complexity. In other words, a system class $\mathcal{C}_{n}$ is classified as hard when its impossible to find any system identification algorithm that achieve polynomial sample complexity for all $S \in \mathcal{C}_{n}$. This can be viewed as a fundamental statistical limitation for the chosen class of systems $\mathcal{C}_{n}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Question 1", "weight": 1.0} -->

Motivated by Figure 1, we define an important subclass of hard problems, namely linear system classes that have worst-case sample complexity that grows exponentially with the dimension $n$ regardless of identification algorithm choice.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Question 2", "weight": 1.0} -->

When is a class of linear systems $\mathcal{C}_{n}$ guaranteed to be $poly$-learnable?

<!-- chunk {"id": "body-0025", "role": "body", "section": "Question 2", "weight": 1.0} -->

Based on prior work, we already have partial answers to Question 2 as we know that linear systems with isotropic noise are $poly$-learnable. In Section 5, we seek to broaden the classes of $poly$-learnable systems and discover their relation to fundamental system theoretic properties such as controllability.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Question 2", "weight": 1.0} -->

While Definitions 1. ‣ 2 Learnability of System Classes ‣ Linear Systems can be Hard to Learn"), 2. ‣ 2 Learnability of System Classes ‣ Linear Systems can be Hard to Learn") are inspired by PAC learning, they have a different flavor. One of the differences is that the guarantees in Definitions 1. ‣ 2 Learnability of System Classes ‣ Linear Systems can be Hard to Learn"), 2. ‣ 2 Learnability of System Classes ‣ Linear Systems can be Hard to Learn") are stated in terms of recovering the state-space parameters, while in PAC learning, they would be stated in terms of the prediction error of the learned model or informally $\sum_{k = 0}^{N - 1}{{\mathbb{E}}{\|{x_{k} - {\hat{A}x_{k - 1}} - {\hat{B}u_{k - 1}}}\|}^{2}}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Directly-excited systems are poly-learnable", "weight": 1.0} -->

In this section, we revisit state-of-the-art results in finite-sample complexity for fully-observed linear systems and re-establish that they all lead to polynomial sample complexity. In prior work, the class of linear systems considered assumes that the stochastic process noise is isotropic, i.e. ${HH^{\prime}} = {\sigma_{w}^{2}I_{n}}$. Since all states are directly excited by the process noise, all modes of the system are captured sufficiently in the data. To obtain polynomial complexity, it suffices to use the least squares identification algorithm

<!-- chunk {"id": "body-0028", "role": "body", "section": "Directly-excited systems are poly-learnable", "weight": 1.0} -->

with white noise inputs $u_{t} \sim {\mathcal{N}{(0,{\sigma_{u}^{2}I})}}$. Based on the algorithm analysis, let $k$ be a fixed time index which is much smaller than the horizon $N$ (see Theorem 2.1 in for details). Let $0 < \delta < 1$ and $\epsilon$ be the confidence and accuracy parameters respectively.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Directly-excited systems are poly-learnable", "weight": 1.0} -->

In a slight departure, we can show that the determinant of the Gramian $\det{(\Gamma_{N})}$ can only increase at most polynomially with the number of samples $N$ and exponentially with state dimension $n$. This is a direct consequence of the following lemma, which is a new result.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Exp-hard system classes", "weight": 1.0} -->

In this section, we show that there exist common classes of linear systems which are impossible or hard to identify with a finite amount of samples. As we will see, this can happen when systems are under-actuated and under-excited. When only a limited number of system states is directly driven by inputs (or excited by noise) and the remaining states are only indirectly excited, then identification can be inhibited.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Controllable systems with infinite sample complexity", "weight": 1.0} -->

For presentation simplicity, let us assume that there are no exogenous inputs $B = 0$. Similar results also hold when $B \neq 0$--see Remark 1. ‣ 4.2 Robustly controllable systems can be exp-hard ‣ 4 Exp-hard system classes ‣ Linear Systems can be Hard to Learn"). To fully identify the unknown matrix $A$, it is necessary that the pair $(A,H)$ is controllable. Furthermore, let's assume that the noise is meaningful, that is ${\sigma_{\min}{(H)}} \geq \sigma$ for some $\sigma > 0$. However, controllability of $(A,H)$ and ${\sigma_{\min}{(H)}} \geq \sigma$ are not sufficient to ensure system identification from a finite numer of samples. The following, perhaps unsurprising theorem, shows that for this class of linear systems, the worst-case sample complexity is infinite.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Robustly controllable systems can be exp-hard", "weight": 1.0} -->

Theorem 2. ‣ 4.1 Controllable systems with infinite sample complexity ‣ 4 Exp-hard system classes ‣ Linear Systems can be Hard to Learn") implies that we need to bound the system away from uncontrollability in order to obtain non-trivial sample complexity bounds. In order to formulate this, we review the notion of distance from uncontrollability, which is the norm of the smallest perturbation that makes $(A,H)$ uncontrollable.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Assumption 2 (Robust Controllability)", "weight": 1.0} -->

Assumption 2. ‣ 4.2 Robustly controllable systems can be exp-hard ‣ 4 Exp-hard system classes ‣ Linear Systems can be Hard to Learn") is not restrictive as long as we allow the bound to degrade with the dimension. Common systems like the $n -$th order integrator have distance that degrades linearly with $n$--see Lemmas B.1, B.2 in the Appendix. However, even for system classes that satisfy Assumption 2. ‣ 4.2 Robustly controllable systems can be exp-hard ‣ 4 Exp-hard system classes ‣ Linear Systems can be Hard to Learn"), the next theorem shows that system identification can be $\exp$-hard.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 1 (Exogenous inputs)", "weight": 1.0} -->

When $B \neq 0$ similar results hold but with an additional interpretation. Consider system but with $H = e_{1}$, $B = {\rhoe_{n}}$. Then, if we apply white-noise input signals we have two possibilities: i) the control inputs have bounded energy per Assumption 1 but we suffer from exponential sample complexity or ii) we obtain polynomial sample complexity but we allow the energy of the inputs to increase exponentially with the dimension. From this alternative viewpoint a system is hard to learn if it requires exponentially large control inputs.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 2", "weight": 1.0} -->

The constant $8$ in $8{({n + 1})}^{- 1}$ in the statement of Theorem 3-hard classes). ‣ 4.2 Robustly controllable systems can be exp-hard ‣ 4 Exp-hard system classes ‣ Linear Systems can be Hard to Learn") is not important in our analysis. We could modify Theorem 3-hard classes). ‣ 4.2 Robustly controllable systems can be exp-hard ‣ 4 Exp-hard system classes ‣ Linear Systems can be Hard to Learn") so that $8$ can be replaced by any smaller constant. In particular, we can decrease $8$ by considering systems with smaller chains, which still have exponential sample complexity. Instead of system, we can consider for example the following. Let $J_{\lfloor{n/m}\rfloor}{}$ be the Jordan block of size $\lfloor{n/m}\rfloor$, for some $m$, and eigenvalue 1 and define

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Notice that we reduced the size of the chain by $1/m$ and we added $n - {\lfloor{n/m}\rfloor}$ directly excited states. By increasing $m$, we can achieve a larger distance to uncontrollability (constant smaller than $8$). However, we will still have exponential sample complexity of the order of at least $\lfloor{n/m}\rfloor$, based on the length of the chain.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Controllability index affects learnability", "weight": 1.0} -->

Structural system properties of an underactuated system, such as the chained structure in the dynamics, can be critical in making system identification easy or hard. This poses novel questions about understanding how system theoretic properties affect system learnability as defined in Definitions 1. ‣ 2 Learnability of System Classes ‣ Linear Systems can be Hard to Learn") and 2. ‣ 2 Learnability of System Classes ‣ Linear Systems can be Hard to Learn"). We begin a new line of inquiry by characterizing how the controllability index $\kappa$, a critical structural system property, affects the statistical properties of system identification. A brief review of the concept of controllability index can be found in the Appendix. It can be viewed as a structural measure of whether a system is directly actuated or underactuated resulting in long chains. The following theorem, is the first result connecting the controllability index with sample complexity bounds.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Simulations", "weight": 1.0} -->

We study three simulation scenarios to illustrate the qualitative implications of our results. In the first two cases, we verify that the sample complexity of the least squares algorithm can indeed grow exponentially with the dimension. In the third case, we investigate how the controllability index affects the sample complexity. In all cases, we perform Monte Carlo simulations to compute the empirical mean error ${\|{A - {\hat{A}}_{N}}\|}_{2}$ and we count the number of samples required to have error less than $\epsilon$, for some $\epsilon > 0$. For numerical stability in the least squares estimator we used a regularization term (ridge regression) with coefficient $0.001$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Simulations", "weight": 1.0} -->

In the first example in Section 2, Figure 1, we used $1000$ Monte Carlo iterations to approximate the empirical average. We modeled the noise as gaussian with $w_{k} \sim {\mathcal{N}{(0,0.5)}}$ and used white noise inputs $u_{k} \sim {\mathcal{N}{}}$. The sample complexity of the least squares algorithm seems to be exponential with the dimension. In Section 4, we showed that such systems exhibit exponential sample complexity due to the weak coupling between the states.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Simulations", "weight": 1.0} -->

In the second example, we study the behavior of Jordan blocks actuated from the last state. Let $J_{n}{(\lambda)}$ be a Jordan block of dimension $n$ and eigenvalues all $\lambda$. We consider the system $A = {J_{n}{(\lambda)}}$, $H = {0.1e_{n}}$, $B = {5e_{n}}$, which means we excite directly only state $x_{t,n}$. We repeat the same experiment as before for $1000$ Monte Carlo simulations with ${w_{k},u_{k}} \sim {\mathcal{N}{}}$ and for $\epsilon = 0.005$. In Figure 2, it seems that the complexity of the least squares algorithm is also exponential when $0 < \lambda < 1$. In this case the coupling between the states is not weak. However, certain subspaces might still be hard to excite. As $\lambda$ approaches the unit circle eigenvalue $1$ the complexity improves.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Simulations", "weight": 1.0} -->

For $\lambda = 1$, after $n = 9$ Matlab returned inaccurate results as the condition number of the data becomes very large. Hence, we do not report any results beyond $n = 9$. However, based on simulations for small $n$ it might be possible that the system can be learned by only a polynomial number of samples. The intuition might be that in this case instability helps with excitation. It is an open problem to prove or disprove exponential lower bounds for the Jordan block when $0 < \lambda < 1$. Similarly, we leave it as an open problem to prove or disprove polynomial upper bounds for the Jordan block when $\lambda = 1$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Simulations", "weight": 1.0} -->

In the third example, we consider the Jordan block $A = {J_{n}{(0.5)}}$ with noise $H = {0.1e_{n}}$. We start from $B = {5e_{n}}$ and we gradually add more exogenous inputs to decrease the controllability index: we try $B = {5\begin{bmatrix}
\end{bmatrix}}$ and $B = {5\begin{bmatrix}
\end{bmatrix}}$ which correspond to indices $\kappa = {\lceil{n/2}\rceil}$ and $\kappa = 2$ respectively. We repeat the same experiment as before for $1000$ Monte Carlo simulations with ${w_{k},u_{k}} \sim {\mathcal{N}{}}$ and for $\epsilon = 0.005$. In Figure 3, it seems that the sample complexity remains exponential when $\kappa = {\lceil{n/2}\rceil}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Simulations", "weight": 1.0} -->

However, when $\kappa = 2$ there is a phase transition and the sample complexity becomes polynomial with the dimension.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The results of this paper paint a broader and more diverse landscape about the statistical complexity of learning linear systems, summarized in Figure 4 according to the controllability index $\kappa$ of the considered system class. While statistically easy cases that were previously known are captured by Theorem 1. ‣ 3 Directly-excited systems are poly-learnable ‣ Linear Systems can be Hard to Learn"), we also showed that hard system classes exist (Theorem 3-hard classes). ‣ 4.2 Robustly controllable systems can be exp-hard ‣ 4 Exp-hard system classes ‣ Linear Systems can be Hard to Learn")). By exploiting structural system theoretic properties, such as the controllability index, we broadened the class of easy to learn linear systems (Theorem 4. ‣ 5 Controllability index affects learnability ‣ Linear Systems can be Hard to Learn")).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our results pose numerous future questions for exploiting other system properties (e.g. observability) for efficiently learning classes of partially-observed linear systems or nonlinear systems. It remains an open problem to prove whether or not the $n -$th order integrator is poly-learnable as discussed in Section 6. Similarly, it is an open problem to prove whether or not the Jordan block of size $n$ and eigenvalues all $0 < \lambda < 1$ has exponential complexity. Finally, the results of this paper might have ramifications for control, for example learning the linear quadratic regulator, as well as reinforcement learning.
