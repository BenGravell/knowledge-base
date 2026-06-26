<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Finite-time Analysis of Approximate Policy Iteration for the Linear Quadratic Regulator

Topics include Reinforcement learning, Policy iteration, Regret bounds, Sample complexity, Control, Learning, PI, Linear quadratic regulator.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the sample complexity of approximate policy iteration (PI) for the Linear Quadratic Regulator (LQR), building on a recent line of work using LQR as a testbed to understand the limits of reinforcement learning (RL) algorithms on continuous control tasks. Our analysis quantifies the tension between policy improvement and policy evaluation, and suggests that policy evaluation is the dominant factor in terms of sample complexity. Specifically, we show that to obtain a controller that is within epsilon of the optimal LQR controller, each step of policy evaluation requires at most (n+d)^/epsilon^ samples, where n is the dimension of the state vector and d is the dimension of the input vector. On the other hand, only log(1/epsilon) policy improvement steps suffice, resulting in an overall sample complexity of (n+d)^ epsilon^(-2) log(1/epsilon). We furthermore build on our analysis and construct a simple adaptive procedure based on epsilon-greedy exploration which relies on approximate PI as a sub-routine and obtains T^(2/3) regret, improving upon a recent result of Abbasi-Yadkori et al.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

With the recent successes of reinforcement learning (RL) on continuous control tasks, there has been a renewed interest in understanding the sample complexity of RL methods. A recent line of work has focused on the Linear Quadratic Regulator (LQR) as a testbed to understand the behavior and trade-offs of various RL algorithms in the continuous state and action space setting. These results can be broadly grouped into two categories: the study of *model-based* methods which use data to build an estimate of the transition dynamics, and *model-free* methods which directly estimate the optimal feedback controller from data without building a dynamics model as an intermediate step. Much of the recent progress in LQR has focused on the model-based side, with an analysis of robust control from Dean et al. and certainty equivalence control by Fiechter and Mania et al.. These techniques have also been extended to the online, adaptive setting. On the other hand, for classic model-free RL algorithms such as Q-learning, SARSA, and approximate policy iteration (PI), our understanding is much less complete despite the fact that these algorithms are well understood in the tabular (finite state and action space) setting.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Indeed, most of the model-free analysis for LQR has focused exclusively on derivative-free random search methods.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we extend our understanding of model-free algorithms for LQR by studying the performance of approximate PI on LQR, which is a classic approximate dynamic programming algorithm. Approximate PI is a model-free algorithm which iteratively uses trajectory data to estimate the state-value function associated to the current policy (via e.g. temporal difference learning), and then uses this estimate to greedily improve the policy. A key issue in analyzing approximate PI is to understand the trade-off between the number of policy improvement iterations, and the amount of data to collect for each policy evaluation phase.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our analysis quantifies this trade-off, showing that if least-squares temporal difference learning (LSTD-Q) is used for policy evaluation, then a trajectory of length $\overset{\sim}{O}{({{({n + d})}^{3}/\varepsilon^{2}})}$ for each inner step of policy evaluation combined with $\mathcal{O}{({\log{({1/\varepsilon})}})}$ outer steps of policy improvement suffices to learn a controller that has $\varepsilon$-error from the optimal controller. This yields an overall sample complexity of $\mathcal{O}{({{({n + d})}^{3}\varepsilon^{- 2}{\log{({1/\varepsilon})}}})}$. Prior to our work, the only known guarantee for approximate PI on LQR was the asymptotic consistency result of Bradtke in the setting of no process noise.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We also extend our analysis of approximate PI to the online, adaptive LQR setting popularized by Abbasi-Yadkori and Szepesvári. By using a greedy exploration scheme similar to Dean et al. and Mania et al., we prove a $\overset{\sim}{O}{(T^{2/3})}$ regret bound for a simple adaptive policy improvement algorithm. While the $T^{2/3}$ rate is sub-optimal compared to the $T^{1/2}$ regret from model-based methods, our analysis improves the $\overset{\sim}{O}{(T^{{2/3} + \varepsilon})}$ regret (for $T \geq C^{1/\varepsilon}$) from the model-free Follow the Leader (FTL) algorithm of Abbasi-Yadkori et al.. To the best of our knowledge, we give the best regret guarantee known for a model-free algorithm. We leave open the question of whether or not a model-free algorithm can achieve optimal $T^{1/2}$ regret.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Main Results", "weight": 1.0} -->

In this paper, we consider the following linear dynamical system: We let $n$ denote the dimension of the state $x_{t}$ and $d$ denote the dimension of the input $u_{t}$. For simplicity we assume that $d \leq n$, e.g. the system is under-actuated. We fix two positive definite cost matrices $(S,R)$, and consider the infinite horizon average-cost Linear Quadratic Regulator (LQR): We assume the dynamics matrices $(A,B)$ are unknown to us, and our method of interaction with (2.1) is to choose an input sequence $\{ u_{t}\}$ and observe the resulting states $\{ x_{t}\}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Main Results", "weight": 1.0} -->

We study the solution to (2.2) using *least-squares policy iteration (LSPI)*, a well-known approximate dynamic programming method in RL introduced by Lagoudakis and Parr. The study of approximate PI on LQR dates back to the Ph.D. thesis of Bradtke, where he showed that for *noiseless* LQR (when $w_{t} = 0$ for all $t$), the approximate PI algorithm is asymptotically consistent. In this paper we expand on this result and quantify non-asymptotic rates for approximate PI on LQR.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Least-Squares Temporal Difference Learning (LSTD-Q)", "weight": 1.0} -->

The first component towards an understanding of approximate PI is to understand least-squares temporal difference learning (LSTD-Q) for $Q$-functions, which is the fundamental building block of LSPI. Given a policy $K_{eval}$ which stabilizes $(A,B)$, the goal of LSTD-Q is to estimate the parameters of the $Q$-function associated to $K_{eval}$. Bellman's equation for infinite-horizon average cost MDPs (c.f. Bertsekas) states that the (relative) $Q$-function associated to a policy $\pi$ satisfies the following fixed-point equation: Here, $\lambda \in {\mathbb{R}}$ is a free parameter chosen so that the fixed-point equation holds.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Least-Squares Temporal Difference Learning (LSTD-Q)", "weight": 1.0} -->

LSTD-Q operates under the *linear architecture* assumption, which states that the $Q$-function can be described as ${Q{(x,u)}} = {q^{\mathsf{T}}\phi{(x,u)}}$, for a known (possibly non-linear) feature map $\phi{(x,u)}$. It is well known that LQR satisfies the linear architecture assumption, since we have: Here, we slightly abuse notation and let $Q$ denote the $Q$-function and also the matrix parameterizing the $Q$-function. Now suppose that a trajectory ${\{{(x_{t},u_{t},x_{t + 1})}\}}_{t = 1}^{T}$ is collected. Note that LSTD-Q is an *off-policy* method (unlike the closely related LSTD estimator for value functions), and therefore the inputs $u_{t}$ can come from any sequence that provides sufficient excitation for learning.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Least-Squares Temporal Difference Learning (LSTD-Q)", "weight": 1.0} -->

In particular, it does *not* have to come from the policy $K_{eval}$. In this paper, we will consider inputs of the form: where $K_{play}$ is a stabilizing controller for $(A,B)$. Once again we emphasize that $K_{play} \neq K_{eval}$ in general. The injected noise $\eta_{t}$ is needed in order to provide sufficient excitation for learning. In order to describe the LSTD-Q estimator, we define the following quantities which play a key role throughout the paper: The LSTD-Q estimator estimates $q$ via: Here, ${(\cdot)}^{\dagger}$ denotes the Moore-Penrose pseudo-inverse. Our first result establishes a non-asymptotic bound on the quality of the estimator $\hat{q}$, measured in terms of $\parallel{\hat{q} - q}\parallel$. Before we state our result, we introduce a key definition that we will use extensively.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Least-Squares Policy Iteration (LSPI)", "weight": 1.0} -->

With Theorem 2.1 ‣ 2 Main Results ‣ Finite-time Analysis of Approximate Policy Iteration for the Linear Quadratic Regulator") in place, we are ready to present the main results for LSPI. We describe two versions of LSPI in Algorithm 1 ‣ 2 Main Results ‣ Finite-time Analysis of Approximate Policy Iteration for the Linear Quadratic Regulator") and Algorithm 2 ‣ 2 Main Results ‣ Finite-time Analysis of Approximate Policy Iteration for the Linear Quadratic Regulator").

<!-- chunk {"id": "body-0014", "role": "body", "section": "Least-Squares Policy Iteration (LSPI)", "weight": 1.0} -->

1:K0: initial stabilizing controller, 2: N: number of policy iterations, 5: μ: lower eigenvalue bound. 6:Collect 𝒟 = {(xk, uk, xk + 1)}k = 1T with input uk = K0 xk + ηk, ηk ∼ 𝒩 (0, ση2 I). Algorithm 1 LSPIv1 for LQR 1:K0: initial stabilizing controller, 2: N: number of policy iterations, 5: μ: lower eigenvalue bound.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Least-Squares Policy Iteration (LSPI)", "weight": 1.0} -->

Algorithm 2 LSPIv2 for LQR In Algorithms 1 ‣ 2 Main Results ‣ Finite-time Analysis of Approximate Policy Iteration for the Linear Quadratic Regulator") and 2 ‣ 2 Main Results ‣ Finite-time Analysis of Approximate Policy Iteration for the Linear Quadratic Regulator"), ${\mathsf{P}\mathsf{r}\mathsf{o}\mathsf{j}}_{\mu}{(\cdot)} = \arg\min_{{X = X^{\mathsf{T}}}:{X \succeq {\mu \cdot I}}}{\parallel X - \cdot \parallel}_{F}$ is the Euclidean projection onto the set of symmetric matrices lower bounded by $\mu \cdot I$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Least-Squares Policy Iteration (LSPI)", "weight": 1.0} -->

Furthermore, the map $G{(\cdot)}$ takes an ${({n + d})} \times {({n + d})}$ positive definite matrix and returns a $d \times n$ matrix: Algorithm 1 ‣ 2 Main Results ‣ Finite-time Analysis of Approximate Policy Iteration for the Linear Quadratic Regulator") corresponds to the version presented in Lagoudakis and Parr, where all the data $\mathcal{D}$ is collected up front and is re-used in every iteration of LSTD-Q. Algorithm 2 ‣ 2 Main Results ‣ Finite-time Analysis of Approximate Policy Iteration for the Linear Quadratic Regulator") is the one we will analyze in this paper, where new data is collected for every iteration of LSTD-Q. The modification made in Algorithm 2 ‣ 2 Main Results ‣ Finite-time Analysis of Approximate Policy Iteration for the Linear Quadratic Regulator") simplifies the analysis by allowing the controller $K_{t}$ to be independent of the data $\mathcal{D}_{t}$ in LSTD-Q. We remark that this does *not* require the system to be reset after every iteration of

<!-- chunk {"id": "body-0017", "role": "body", "section": "Least-Squares Policy Iteration (LSPI)", "weight": 1.0} -->

LSTD-Q. We leave analyzing Algorithm 1 ‣ 2 Main Results ‣ Finite-time Analysis of Approximate Policy Iteration for the Linear Quadratic Regulator") to future work.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Least-Squares Policy Iteration (LSPI)", "weight": 1.0} -->

Before we state our main finite-sample guarantee for Algorithm 2 ‣ 2 Main Results ‣ Finite-time Analysis of Approximate Policy Iteration for the Linear Quadratic Regulator"), we review the notion of a (relative) value-function. Similarly to (relative) $Q$-functions, the infinite horizon average-cost Bellman equation states that the (relative) value function $V$ associated to a policy $\pi$ satisfies the fixed-point equation: For a stabilizing policy $K$, it is well known that for LQR the value function ${V{(x)}} = {x^{\mathsf{T}}Vx}$ with Once again as we did for $Q$-functions, we slightly abuse notation and let $V$ denote the value function and the matrix that parameterizes the value function. Our main result for Algorithm 2 ‣ 2 Main Results ‣ Finite-time Analysis of Approximate Policy Iteration for the Linear Quadratic Regulator") appears in the following theorem. For simplicity, we will assume that ${\parallel S\parallel} \geq 1$ and ${\parallel R\parallel} \geq 1$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "LSPI for Adaptive LQR", "weight": 1.0} -->

We now turn our attention to the online, adaptive LQR problem as studied in Abbasi-Yadkori and Szepesvári. In the adaptive LQR problem, the quantity of interest is the *regret*, defined as: Here, the algorithm is penalized for the cost incurred from learning the optimal policy $K_{\star}$, and must balance exploration (to better learn the optimal policy) versus exploitation (to reduce cost). As mentioned previously, there are several known algorithms which achieve $\overset{\sim}{O}{(\sqrt{T})}$ regret. However, these algorithms operate in a *model-based* manner, using the collected data to build a confidence interval around the true dynamics $(A,B)$. On the other hand, the performance of adaptive algorithms which are *model-free* is less well understood.

<!-- chunk {"id": "body-0020", "role": "body", "section": "LSPI for Adaptive LQR", "weight": 1.0} -->

We use the results of the previous section to give an adaptive model-free algorithm for LQR which achieves $\overset{\sim}{O}{(T^{2/3})}$ regret, which improves upon the $\overset{\sim}{O}{(T^{{2/3} + \varepsilon})}$ regret (for $T \geq C^{1/\varepsilon}$) achieved by the adaptive model-free algorithm of Abbasi-Yadkori et al.. Our adaptive algorithm based on LSPI is shown in Algorithm 3.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we evaluate LSPI in both the non-adaptive offline setting (Section 2.2 ‣ 2 Main Results ‣ Finite-time Analysis of Approximate Policy Iteration for the Linear Quadratic Regulator")) as well as the adaptive online setting (Section 2.3). Section G contains more details about both the algorithms we compare to as well as our experimental methodology.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Experiments", "weight": 1.0} -->

We first look at the performance of LSPI in the non-adaptive, offline setting. Here, we compare LSPI to other popular model-free methods, and the model-based certainty equivalence (nominal) controller (c.f.). For model-free, we look at policy gradients (REINFORCE) (c.f.) and derivative-free optimization (c.f.). We consider the LQR instance $(A,B,S,R)$ with We choose an LQR problem where the $A$ matrix is stable, since the model-free methods we consider need to be seeded with an initial stabilizing controller; using a stable $A$ allows us to start at $K_{0} = 0_{2 \times 3}$. We fix the process noise $\sigma_{w} = 1$. The model-based nominal method learns $(A,B)$ using least-squares, exciting the system with Gaussian inputs $u_{t}$ with variance $\sigma_{u} = 1$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Experiments", "weight": 1.0} -->

For policy gradients and derivative-free optimization, we use the projected stochastic gradient descent (SGD) method with a constant step size $\mu$ as the optimization procedure. For policy iteration, we evaluate both $\mathsf{L}\mathsf{S}\mathsf{P}\mathsf{I}\mathsf{v}\mathsf{1}$ (Algorithm 1 ‣ 2 Main Results ‣ Finite-time Analysis of Approximate Policy Iteration for the Linear Quadratic Regulator")) and $\mathsf{L}\mathsf{S}\mathsf{P}\mathsf{I}\mathsf{v}\mathsf{2}$ (Algorithm 2 ‣ 2 Main Results ‣ Finite-time Analysis of Approximate Policy Iteration for the Linear Quadratic Regulator")).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Experiments", "weight": 1.0} -->

For every iteration of LSTD-Q, we project the resulting $Q$-function parameter matrix onto the set $\{ Q:{Q \succeq {\gammaI}}\}$ with $\gamma = {\min{\{{\lambda_{\min}{(S)}},{\lambda_{\min}{(R)}}\}}}$. For $\mathsf{L}\mathsf{S}\mathsf{P}\mathsf{I}\mathsf{v}\mathsf{1}$, we choose $N = 15$ by picking the $N \in {\lbrack 5,10,15\rbrack}$ which results in the best performance after $T = 10^{6}$ timesteps.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Experiments", "weight": 1.0} -->

Next, we compare the performance of LSPI in the adaptive setting. We compare LSPI against the model-free linear quadratic control (MFLQ) algorithm of Abbasi-Yadkori et al., the certainty equivalence (nominal) controller (c.f.), and the optimal controller. We set the process noise $\sigma_{w} = 1$, and consider the example of Dean et al.: Figure 2: Plot of adaptive performance. The shaded regions represent the median to upper 90th percentile over 100 trials. Here, LSPI is Algorithm 3 using LSPIv1, MFLQ is from Abbasi-Yadkori et al., nominal is the ε-greedy adaptive certainty equivalent controller (c.f.), and optimal has access to the true dynamics. (a) Plot of regret versus time. (b) Plot of the cost sub-optimality versus time.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We studied the sample complexity of approximate PI on LQR, showing that order ${({n + d})}^{3}\varepsilon^{- 2}{\log{({1/\varepsilon})}}$ samples are sufficient to estimate a controller that is within $\varepsilon$ of the optimal. We also show how to turn this offline method into an adaptive LQR method with $T^{2/3}$ regret. Several questions remain open with our work. The first is if policy iteration is able to achieve $T^{1/2}$ regret, which is possible with other model-based methods. The second is whether or not model-free methods provide advantages in situations of partial observability for LQ control. Finally, an asymptotic analysis of LSPI, in the spirit of Tu and Recht, is of interest in order to clarify which parts of our analysis are sub-optimal due to the techniques we use versus are inherent in the algorithm.
