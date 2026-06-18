<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Regret Bounds for Robust Adaptive Control of the Linear Quadratic Regulator

Topics include Regret bounds, Robustness, Control, Linear quadratic regulator, Adaptive control, Robust control, Linear systems.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider adaptive control of the Linear Quadratic Regulator (LQR), where an unknown linear system is controlled subject to quadratic costs. Leveraging recent developments in the estimation of linear systems and in robust controller synthesis, we present the first provably polynomial time algorithm that provides high probability guarantees of sub-linear regret on this problem. We further study the interplay between regret minimization and parameter estimation by proving a lower bound on the expected regret in terms of the exploration schedule used by any algorithm. Finally, we conduct a numerical study comparing our robust adaptive algorithm to other methods from the adaptive LQR literature, and demonstrate the flexibility of our proposed method by extending it to a demand forecasting problem subject to state constraints.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The problem of adaptively controlling an unknown dynamical system has a rich history, with classical asymptotic results of convergence and stability dating back decades. Of late, there has been a renewed interest in the study of a particular instance of such problems, namely the adaptive Linear Quadratic Regulator (LQR), with an emphasis on *non-asymptotic* guarantees of stability and performance. Initiated by Abbasi-Yadkori and Szepesvári, there have since been several works analyzing the regret suffered by various adaptive algorithms on LQR-- here the regret incurred by an algorithm is thought of as a measure of deviations in performance from optimality over time. These results can be broadly divided into two categories: those providing high-probability guarantees for a single execution of the algorithm, and those providing bounds on the expected *Bayesian* regret incurred over a family of possible systems. As we discuss in more detail, these methods all suffer from one or several of the following limitations: restrictive and unverifiable assumptions, limited applicability, and computationally intractable subroutines.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we provide, to the best of our knowledge, the first polynomial-time algorithm for the adaptive LQR problem that provides high probability guarantees of sub-linear regret, and that does not require unverifiable or unrealistic assumptions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Contributions", "weight": 1.0} -->

To develop the first polynomial-time algorithm that provides high probability guarantees of sub-linear regret, we leverage recent results from the estimation of linear systems, robust controller synthesis, and coarse-ID control. We show that our robust adaptive control algorithm: (i) guarantees stability and near-optimal performance at all times; (ii) achieves a regret up to time $T$ bounded by $\overset{\sim}{\mathcal{O}}{(T^{2/3})}$; and (iii) is based on finite-dimensional semidefinite programs of size logarithmic in $T$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Contributions", "weight": 1.0} -->

Furthermore, our method estimates the system parameters at $\overset{\sim}{\mathcal{O}}{(T^{- {1/3}})}$ rate in operator norm. Although system parameter identification is not necessary for optimal control performance, an accurate system model is often desirable in practice. Motivated by this, we study the interplay between regret minimization and parameter estimation, and identify fundamental limits connecting the two. We show that the expected regret of our algorithm is lower bounded by $\Omega{(T^{2/3})}$, proving that our analysis is sharp up to logarithmic factors. Moreover, our lower bound suggests that the estimation rate achievable by any algorithm with $\mathcal{O}{(T^{\alpha})}$ regret is $\Omega{(T^{- {\alpha/2}})}$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Contributions", "weight": 1.0} -->

Finally, we conduct a numerical study of the adaptive LQR problem, in which we implement our algorithm, and compare its performance to heuristic implementations of OFU and TS based methods. We show on several examples that the regret incurred by our algorithm is comparable to that of the OFU and TS based methods. Furthermore, the infinite horizon cost achieved by our algorithm at any given time on the true system is consistently lower than that attained by OFU and TS based algorithms. Finally, we use a demand forecasting example to show how our algorithm naturally generalizes to incorporate environmental uncertainty and safety constraints.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem Statement and Preliminaries", "weight": 1.0} -->

In this work we consider adaptive control of the following discrete-time linear system

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Statement and Preliminaries", "weight": 1.0} -->

where $x_{k} \in {\mathbb{R}}^{n}$ is the state, $u_{k} \in {\mathbb{R}}^{p}$ is the control input, and $w_{k} \in {\mathbb{R}}^{n}$ is the process noise. We assume that the state variables are observed exactly and, for simplicity, that $x_{0} = 0$. We consider the *Linear Quadratic Regulator* optimal control problem, given by cost matrices $Q \succeq 0$ and $R \succ 0$,

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Statement and Preliminaries", "weight": 1.0} -->

where the minimum is taken over measurable functions $u = {\{{u_{k}{( \cdot )}}\}}_{k \geq 1}$, with each $u_{k}$ adapted to the history $x_{k}$, $x_{k - 1}$,..., $x_{1}$, and possibe additional randomness independent of future states. Given knowledge of $(A_{\star},B_{\star})$, the optimal policy is a static state-feedback law $u_{k} = {K_{\star}x_{k}}$, where $K_{\star}$ is derived from the solution to a discrete algebraic Riccati equation.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Statement and Preliminaries", "weight": 1.0} -->

We are interested in algorithms which operate without knowledge of the true system transition matrices $(A_{\star},B_{\star})$. We measure the performance of such algorithms via their regret, defined as

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Statement and Preliminaries", "weight": 1.0} -->

The regret of any algorithm is lower-bounded by $\Omega{(\sqrt{T})}$, a bound matched by OFU up to logarithmic factors. However, after each epoch, OFU requires optimizing a non-convex objective to $\mathcal{O}{(T^{- {1/2}})}$ precision. Instead, our method uses a subroutine based on convex optimization and robust control.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Algorithm and Guarantees", "weight": 1.0} -->

Our proposed robust adaptive control algorithm for LQR is shown in Algorithm 1. We note that while Line 9 of Algorithm 1 is written as an infinite-dimensional optimization problem, because of the FIR nature of the decision variables, it can be equivalently written as a finite-dimensional semidefinite program. We describe this transformation in Section G.3 of the Appendix.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Algorithm and Guarantees", "weight": 1.0} -->

Algorithm 1 Robust Adaptive Control Algorithm

<!-- chunk {"id": "body-0015", "role": "body", "section": "Algorithm and Guarantees", "weight": 1.0} -->

Some remarks on practice are in order. First, in Line [7, only the trajectory data collected during the $i$-th epoch is used for the least squares estimate. Second, the epoch lengths we use grow exponentially in the epoch index. These settings are chosen primarily to simplify the analysis; in practice all the data collected should be used, and it may be preferable to use a slower growing epoch schedule (such as $T_{i} = {C_{T}{({i + 1})}}$). Finally, for storage considerations, instead of performing a batch least squares update of the model, a recursive least squares (RLS) estimator rule can be used to update the parameters in an online manner.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Regret Upper Bounds", "weight": 1.0} -->

Our guarantees for Algorithm 1 are stated in terms of certain system specific constants, which we define here. We let $K_{\star}$ denote the static feedback solution to the LQR problem for $(A_{\star},B_{\star},Q,R)$. Next, we define $(C_{\star},\rho_{\star})$ such that the closed loop system $A_{\star} + {B_{\star}K_{\star}}$ belongs to $\mathcal{S}{(C_{\star},\rho_{\star})}$. Our main assumption is stated as follows.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

The requirement of an initial stabilizing controller $\mathbf{K}^{}$ is not restrictive; Dean et al. provide an offline strategy for finding such a controller. Furthermore, in practice Algorithm 1 can be initialized with no controller, with random inputs applied instead to the system in the first epoch to estimate $(A_{\star},B_{\star})$ within an initial confidence set for which the synthesis problem becomes feasible.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

Our first guarantee is on the rate of estimation of $(A_{\star},B_{\star})$ as the algorithm progresses through time. This result builds on recent progress for estimation along trajectories of a linear dynamical system. For what follows, the notation $\overset{\sim}{\mathcal{O}}{( \cdot )}$ hides absolute constants and ${polylog}\left( T,\frac{1}{\delta},C_{\star},\frac{1}{1 - \rho_{\star}},n,p,{\parallel B_{\star}\parallel},{\parallel K_{\star}\parallel} \right)$ factors.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Regret Lower Bounds and Parameter Estimation Rates", "weight": 1.0} -->

We saw that Algorithm 1 achieves $\overset{\sim}{\mathcal{O}}{(T^{2/3})}$ regret with high probability. Now we provide a matching algorithmic lower bound on the expected regret, showing that the analysis presented in Section 3.1 is sharp as a function of $T$. Moreover, our lower bound characterizes how much regret must be accrued in order to achieve a specified estimation rate for the system parameters $(A_{\star},B_{\star})$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Regret Comparison", "weight": 1.0} -->

We illustrate the performance of several adaptive schemes empirically. We compare the proposed robust adaptive method with non-Bayesian Thompson sampling (TS) as in Abeille and Lazaric and a heuristic projected gradient descent (PGD) implementation of OFU. As a simple baseline, we use the nominal control method, which synthesizes the optimal infinite-horizon LQR controller for the estimated system and injects noise with the same schedule as the robust approach. Implementation details and computational considerations for all adaptive methods are in Appendix G.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Regret Comparison", "weight": 1.0} -->

This system corresponds to a marginally unstable Laplacian system where adjacent nodes are weakly connected; these dynamics were also studied. The cost is such that input size is penalized relatively less than state. This problem setting is amenable to robust methods due to both the cost ratio and the marginal instability, which are factors that may hurt optimistic methods. In Appendix H.1, we show similar results for an unstable system with large transients.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Regret Comparison", "weight": 1.0} -->

To standardize the initialization of the various adaptive methods, we use a rollout of length $T_{0} = 100$ where the input is a stabilizing controller plus Gaussian noise with fixed variance $\sigma_{u} = 1$. This trajectory is not counted towards the regret, but the recorded states and inputs are used to initialize parameter estimates. In each experiment, the system starts from $x_{0} = 0$ to reduce variance over runs. For all methods, the actual errors ${\hat{A}}_{t} - A_{\star}$ and ${\hat{B}}_{t} - B_{\star}$ are used rather than bounds or bootstrapped estimates. The effect of this choice on regret is small, as examined empirically in Appendix H.2.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Regret Comparison", "weight": 1.0} -->

The performance of the various adaptive methods is compared in Figure 1. The median and 90th percentile regret over 500 instances is displayed in Figure 1a, which gives an idea of both typical and worst-case behavior. The regret of the optimal LQR controller for the true system is displayed as a baseline. Overall, the methods have very similar performance. One benefit of robustness is the guaranteed stability and bounded infinite-horizon cost at every point during operation. In Figure 1b, this infinite-horizon LQR cost is plotted for the controllers played during each epoch. This value measures the cost of using each epoch's controller indefinitely, rather than continuing to update its parameters. The robust adaptive method performs relatively better than other adaptive algorithms, indicating that it is more amenable to early stopping, i.e., to turning off the adaptive component of the algorithm and playing the current controller indefinitely.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Extension to Uncertain Environment with State Constraints", "weight": 1.0} -->

The proposed robust adaptive method naturally generalizes beyond the standard LQR problem. We consider a disturbance forecasting example which incorporates environmental uncertainty and safety constraints. Consider a system with known dynamics driven by stochastic disturbances that are now correlated in time. We model the disturbance process as the output of an unknown autonomous LTI system, as illustrated in Figure 2(a). This setting can be interpreted as a demand forecasting problem, where, for example, the system is a server farm and the disturbances represent changes in the amount of incoming jobs. If the dynamics of the correlated disturbance process are known, this knowledge can be used for more cost-effective temperature control.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Extension to Uncertain Environment with State Constraints", "weight": 1.0} -->

We let the system $(A_{\star},B_{\star})$ with known dynamics be described by the graph Laplacian dynamics as in Eq. (4.1).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Extension to Uncertain Environment with State Constraints", "weight": 1.0} -->

The costs are set to model expensive inputs, with $Q = I$ and $R = {{1 \times 10^{3}}I}$. The controller synthesis problem in Line 9 of Algorithm 1 is modified to reflect the problem structure, and crucially, we add a constraint on the system response $\mathbf{\Phi}_{x}$. Further details of the formulation are explained in Appendix H.3. Figure 2(b) illustrates the effect. While the unconstrained synthesis results in trajectories with large state values, the constrained synthesis results in much more moderate behavior.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

We presented a polynomial-time algorithm for the adaptive LQR problem that provides high probability guarantees of sub-linear regret. In contrast to other approaches to this problem, our robust adaptive method guarantees stability, robust performance, and parameter estimation. We also explored the interplay between regret minimization and parameter estimation, identifying fundamental limits connecting the two.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

Several questions remain to be answered. It is an open question whether a polynomial-time algorithm can achieve a regret of $\overset{\sim}{\mathcal{O}}{(\sqrt{T})}$. In our implementation of OFU, we observed that PGD performed quite effectively. Interesting future work is to see if the techniques of Fazel et al. for policy gradient optimization on LQR can be applied to prove convergence of PGD on the OFU subroutine, which would provide an optimal polynomial-time algorithm. Moreover, we observed that OFU and TS methods in practice gave estimates of system parameters that were comparable with our method which explicitly adds excitation noise. It seems that the switching of control policies at epoch boundaries provides more excitation for system identification than is currently understood by the theory. Furthermore, practical issues that remain to be addressed include satisfying safety constraints and dealing with nonlinear dynamics; in both settings, finite-sample parameter estimation/system identification and adaptive control remain an open problem.
