<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sample Complexity of Kalman Filtering for Unknown Systems

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we consider the task of designing a Kalman Filter (KF) for an unknown and partially observed autonomous linear time invariant system driven by process and sensor noise. To do so, we propose studying the following two step process: first, using system identification tools rooted in subspace methods, we obtain coarse finite-data estimates of the state-space parameters and Kalman gain describing the autonomous system; and second, we use these approximate parameters to design a filter which produces estimates of the system state. We show that when the system identification step produces sufficiently accurate estimates, or when the underlying true KF is sufficiently robust, that a Certainty Equivalent (CE) KF, i.e., one designed using the estimated parameters directly, enjoys provable sub-optimality guarantees. We further show that when these conditions fail, and in particular, when the CE KF is marginally stable (i.e., has eigenvalues very close to the unit circle), that imposing additional robustness constraints on the filter leads to similar sub-optimality guarantees.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We further show that with high probability, both the CE and robust filters have mean prediction error bounded by tilde O(1/sqrt(N)), where N is the number of data points collected in the system identification step. To the best of our knowledge, these are the first end-to-end sample complexity bounds for the Kalman Filtering of an unknown system.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Time series prediction is a fundamental problem across control theory, economics and machine learning.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

the celebrated Kalman Filter (KF) has been the standard method for prediction. When model is known, the KF minimizes the mean square prediction error. However, in many practical cases of interest (e.g., tracking moving objects, stock price forecasting), the state-space parameters are not known and must be learned from time-series data. This system identification step, based on a finite amount of data, inevitably introduces parametric errors in model, which leads to a KF with suboptimal prediction performance.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we study this scenario, and provide finite-data estimation guarantees for the Kalman Filtering of an unknown autonomous LTI system. We consider a simple two step procedure. In the first step, using system identification tools rooted in subspace methods, we obtain finite-data estimates of the state-space parameters, and Kalman gain describing system. Then, in the second step, we use these approximate parameters to design a filter which predicts the system state. We provide an end-to-end analysis of this two-step procedure, and characterize the sub-optimality of the resulting filter in terms of the number of samples used during the system identification step, where the sub-optimality is measured in terms of the mean square prediction error of the filter. A key insight that emerges from our analysis is that using a Certainty Equivalent (CE) Kalman Filter, i.e., using a KF computed directly from estimated parameters, can yield poor estimation performance if the resulting CE KF has eigenvalues close to the unit circle. To address this issue, we propose a Robust Kalman Filter that mitigates these effects and that still enjoys provable sub-optimality guarantees.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our main contributions are that: i) we show that if the system identification step produces sufficiently accurate estimates, or if the underlying true KF is sufficiently robust, then the CE KF has near optimal mean square prediction error, ii) we show when the CE KF is marginally stable, i.e., when it has eigenvalues close to the unit circle, that a Robust KF synthesized by explicitly imposing bounds on the magnitude of certain closed loop maps of the system enjoys similar mean square prediction error bounds as the CE KF, while demonstrating improved stability properties, and iii) we integrate the above results with the finite-data system identification guarantees of Tsiamis and Pappas, to provide, to the best of our knowledge, the first end-to-end sample complexity bounds for the Kalman Filtering of an unknown system. In particular, we show that the mean square estimation error of both the Certainty Equivalent and Robust Kalman filter produced by the two step procedure described above is, with high probability, bounded by $\overset{\sim}{O}{({1/\sqrt{N}})}$, where $N$ is the number of samples collected in the system identification step.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Related work. A similar two step process was studied for the Linear Quadratic (LQ) control of an unknown system in Dean et al.; Mania et al.. While LQ optimal control and Kalman Filtering are known to be dual problems, this duality breaks down when the state-space parameters describing the system dynamics are not known. In particular, the LQ optimal control problem assumes full state information, making the system identification step much simpler -- in particular, it reduces to a simple least-squares problem. In contrast, in the KF setting, as only partial observations are available, the additional challenge of finding an appropriate system order and state-space realization must be addressed. On the other hand, in the KF problem one can directly estimate the KF gain from data, which makes analyzing performance of the CE KF simpler than the performance of the CE LQ optimal controller.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

System identification of autonomous LTI systems is referred to as stochastic system identification. Classical results consider the asymptotic consistency of stochastic subspace system identification, as in Deistler et al.; Bauer et al., whereas contemporary results seek to provide finite data guarantees. Finite data guarantees for system identification of partially observed systems can also be found in Oymak and Ozay; Simchowitz et al.; Sarkar et al., but these results focus on learning the non-stochastic part of the system, assuming that a user specified input is used to persistently excite the dynamics.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Classical approaches to robust Kalman Filtering can be found in El Ghaoui and Calafiore; Sayed et al.; Levy and Nikoukhah, where parametric uncertainty is explicitly taken into account during the filter synthesis procedure. Although similar in spirit to our robust KF procedure, these approaches assume fixed parametric uncertainty, and do not characterize the effects of parametric uncertainty on estimation performance, with this latter step being key in providing end-to-end sample complexity bounds. We also note that although not directly comparable to our work, the filtering problem for an unknown LTI system was also recently studied in the adversarial noise setting in Hazan et al., where a spectral filtering technique is used to directly predict the output bypassing the system identification step. In the stochastic noise case, online-learning of the Kalman Filter was studied in Kozdoba et al., where the goal is to predict a scalar output. This is different from our paper, where the goal is to learn a state-space representation of the KF; our analysis holds for multi-output systems as well.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Paper structure. In Sec. 2, we formulate the problem, and in Sec. 3 and 4, we derive performance guarantees for the proposed CE and Robust Kalman filters. In Sec. 5, we provide end-to-end sample complexity bounds for our two step procedure, and demonstrate the effectiveness of our pipeline with a numerical example in Sec. 6. We end with a discussion of future work in Sec. 7. All proofs, missing details, and a summary of the system identification results from Tsiamis and Pappas can be found in the Appendix.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

where $x_{k} \in {\mathbb{R}}^{n}$ is the prediction (state), $y_{k} \in {\mathbb{R}}^{m}$ is the output, and $e_{k} \in {\mathbb{R}}^{n}$ is the innovation process. The innovations $e_{k}$ are assumed to be i.i.d. zero mean Gaussians, with positive definite covariance matrix $R$, and the initial state is assumed to be $x_{0} = 0$. In general, the system driven by i.i.d. zero mean Gaussian process and sensor noise is equivalent to system for a suitable gain matrix $K$, as both noise models produce outputs with identical statistical properties. We make the following assumption throughout the rest of the paper.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Matrices $A,C,K,R$ are unknown, and the pair $(A,C)$ is observable. Both the matrices $A$ and $A - {KC}$ have spectral radius less than $1$, i.e., ${\rho{(A)}} < 1$ and ${\rho{({A - {KC}})}} < 1$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The observability assumption is standard, and the stability of $A - {KC}$ follows from the properties of the Kalman filter. We note that the filter synthesis procedures we propose can be applied even if ${\rho{(A)}} \geq 1$ -- however, in this case, we are unable to guarantee bounded estimation error for the resulting CE and robust KFs (see Theorem 3.1. ‣ 3 Estimation Guarantees for Certainty Equivalent Kalman Filtering ‣ Sample Complexity of Kalman Filtering for Unknown Systems") and Lemma 4.1. ‣ 4 Estimation Guarantees for Robust Kalman Filtering ‣ Sample Complexity of Kalman Filtering for Unknown Systems")).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Our goal is to provide end-to-end sample complexity bounds for the two step pipeline illustrated in Fig. 1. First, we collect a trajectory ${\{ y_{t}\}}_{t = 0}^{N}$ of length $N$ from system, and use system identification tools with finite data guarantees to learn the parameters $\hat{A},\hat{C},\hat{K},\hat{R}$ and bound the corresponding parameter uncertainties by $(\epsilon_{A},\epsilon_{C},\epsilon_{K},\epsilon_{R})$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

where $\left\{ L_{t} \right\}_{t = 1}^{\infty}$ are to be designed and $\overset{\sim}{J}$ is the filter's mean square prediction error as defined with respect to the optimal KF. Note that the predictor class above includes the CE KF -- see Section 3 -- and that if the the true system parameters are known, i.e., if $\hat{A} = A$, $\hat{C} = C$, $\hat{K} = K$, then the optimal mean squared prediction error $\overset{\sim}{J} = 0$ is achieved.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem 1 (End-to-end Sample Complexity)", "weight": 1.0} -->

Fix a failure probability $\delta > 0$. Given a single trajectory $y_{0},\ldots,y_{N}$ of system, compute system parameter estimates $\hat{A},\hat{C},\hat{K},\hat{R}$, and design a Kalman filter in class, defined by gains $\left\{ L_{t} \right\}_{t = 1}^{\infty}$, such that with probability at least $1 - \delta$, we have that $\overset{\sim}{J} \leq \epsilon_{J}$, so long as $N \geq {{poly}{({1/\epsilon_{J}},{\log{({1/\delta})}})}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem 1 (End-to-end Sample Complexity)", "weight": 1.0} -->

To address Problem 1 ‣ 2 Problem Formulation ‣ Sample Complexity of Kalman Filtering for Unknown Systems"), we will: i) leverage recent results regarding the the sample complexity of stochastic system identification, ii) provide estimation guarantees for certainty equivalent as well as robust Kalman filter designed using the identified system parameters (see Problem 2 ‣ 2 Problem Formulation ‣ Sample Complexity of Kalman Filtering for Unknown Systems") below), and (iii) provide end-to-end performance guarantees by integrating steps (i) and (ii) (see Problem 1 ‣ 2 Problem Formulation ‣ Sample Complexity of Kalman Filtering for Unknown Systems") above).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem 1 (End-to-end Sample Complexity)", "weight": 1.0} -->

Recently Tsiamis and Pappas provided a finite sample analysis for stochastic system identification which provides bounds on the identification error $\epsilon:={\max{(\epsilon_{A},\epsilon_{C},\epsilon_{K},\epsilon_{R})}}$. Leveraging these results, we focus next on solving the Filter Synthesis task described below using both a certainty equivalent Kalman filter as well as a robust Kalman filter.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem 2 (Near Optimal Kalman Filtering of an Uncertain System)", "weight": 1.0} -->

Consider system. Let $\hat{A},\hat{C},\hat{K},\hat{R}$ be estimates satisfying^11^1 In practice, estimating the parameters of a partially observed system is ill-posed, in that any similarity transformation $S$ can be applied to generate parameters $({S^{- 1}AS},{CS},{S^{- 1}K},R)$ describing the same system, and the bounds described hold for *some* similarity transformation $S$. All results in this paper apply nearly as is to the general case of $S \neq I$ under suitable assumptions -- more details can be found in the extended version.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Estimation Guarantees for Certainty Equivalent Kalman Filtering", "weight": 1.0} -->

For the certainty equivalent Kalman filter, we directly use the estimated state-space parameters from the system identification step.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Estimation Guarantees for Certainty Equivalent Kalman Filtering", "weight": 1.0} -->

Then, based on standard Kalman filter theory, we compute the stabilizing solution^22^2A stabilizing solution $P$ to the Riccati equation defines a Kalman gain $L_{CE}$ such that ${\rho{({\hat{A} - {L_{CE}\hat{C}}})}} < 1$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Estimation Guarantees for Certainty Equivalent Kalman Filtering", "weight": 1.0} -->

Then, the CE Kalman filter gain is static and takes the form

<!-- chunk {"id": "body-0024", "role": "body", "section": "Estimation Guarantees for Certainty Equivalent Kalman Filtering", "weight": 1.0} -->

Trivially, if ${\rho{({\hat{A} - {\hat{K}\hat{C}}})}} < 1$, then the stabilizing solution of the Riccati equation is $P = 0$ with $L_{CE} = \hat{K}$; the solution does not depend on $\hat{R}$. The next result shows that if the underlying true Kalman filter is sufficiently robust, as measured by a spectral decay rate, and that estimation parameter errors are sufficiently small, then the CE Kalman filter achieves near optimal performance.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Estimation Guarantees for Robust Kalman Filtering", "weight": 1.0} -->

To address the possible poor performance of the CE Kalman filter when model uncertainty is large, we propose to search over dynamic filters subject to additional robustness constraints on their transient response. Using the System Level Synthesis (SLS) framework for Kalman Filtering, we parameterize the class of dynamic filters subject to additional robustness constraints in a way that leads to convex optimization problems.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Estimation Guarantees for Robust Kalman Filtering", "weight": 1.0} -->

In, it is shown that these responses are in fact the closed loop maps from process and sensor noise $({\mathbf{w}},{\mathbf{v}})$ to state estimation error, and that the filter gain achieving the desired behavior can be recovered via ${\mathbf{L}} = {- {\mathbf{\Phi}_{w}^{- 1}\mathbf{\Phi}_{v}}}$ so long as the responses $(\mathbf{\Phi}_{w},\mathbf{\Phi}_{v})$ are constrained to lie in an affine space defined by the system dynamics. By expressing the mean squared prediction error of the filters in terms of their system responses, we are able to clearly delineate the effects of parametric uncertainty from the cost of deviating from the CE Kalman filter.

<!-- chunk {"id": "body-0027", "role": "body", "section": "End-to-End Sample Complexity for the Kalman Filter", "weight": 1.0} -->

Theorems 3.1. ‣ 3 Estimation Guarantees for Certainty Equivalent Kalman Filtering ‣ Sample Complexity of Kalman Filtering for Unknown Systems") and 4.2. ‣ 4 Estimation Guarantees for Robust Kalman Filtering ‣ Sample Complexity of Kalman Filtering for Unknown Systems") provide two different solutions to Problem 2 ‣ 2 Problem Formulation ‣ Sample Complexity of Kalman Filtering for Unknown Systems"). Combining these theorems with the finite data system identification guarantees of Tsiamis and Pappas, we now derive, to the best of our knowledge, the first end-to-end sample complexity bounds for the Kalman filtering of an unknown system. For both the CE and robust Kalman filter, we show that the mean squared estimation error defined in decreases with rate $O{({1/\sqrt{N}})}$ up to logarithmic terms, where $N$ is the number of samples collected during the system identification step. The formal statement of the following theorem which addresses Problem 1 ‣ 2 Problem Formulation ‣ Sample Complexity of Kalman Filtering for Unknown Systems") can be found in Theorem E.1. ‣ Appendix E Formal end-to-end result ‣ Sample Complexity of Kalman Filtering for Unknown Systems").

<!-- chunk {"id": "body-0028", "role": "body", "section": "Simulations", "weight": 1.0} -->

We perform Monte Carlo simulations of the proposed pipeline for the system

<!-- chunk {"id": "body-0029", "role": "body", "section": "Simulations", "weight": 1.0} -->

for varying sample lengths $N$. We simulate both the CE and robust Kalman filters, and set the regularization parameter to $\mathcal{C} = 10$ in the robust SLS optimization problem. For each iteration, we first simulate system to obtain $N$ output samples. Then, we perform system identification to obtain the system parameters, after which we synthesize both CE and robust Kalman filters. Finally, we compute the mean prediction error of the designed filters.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Simulations", "weight": 1.0} -->

For the identification scheme, we used the variation of the MOESP algorithm Qin, which is more sample efficient in practice than the one analyzed in Tsiamis and Pappas --see Algorithm 1 and Section D.2. The basis of the state-space representation returned by the subspace algorithm is data-dependent and varies with each simulation. For this reason, to compare the performance across different simulations, we compute the mean square error in terms of the original state space basis. Note that the SLS optimization problem is semi-infinite since we optimize over the infinite variables $\left\{ \Phi_{w,t} \right\}_{t = 1}^{\infty}$ and $\left\{ \Phi_{v,t} \right\}_{t = 0}^{\infty}$. To deal with this issue, we optimize over a finite horizon $T$--see for example Dean et al., which makes the problem finite and tractable. Here, we selected $T = 30$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Simulations", "weight": 1.0} -->

[CE Kalman Filter] \subfigure[Robust Kalman Filter]
Figure 2: The 95% and 97.5% empirical percentiles for the mean squared prediction error $\overset{\sim}{J}$ of the CE and Robust Kalman filters. We run 1000 Monte Carlo simulations for different sample lengths N (x-axis, number of samples).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Conclusions & Future work", "weight": 1.0} -->

In this paper, we proposed and analyzed a system identification and filter synthesis pipeline. Leveraging contemporary finite data guarantees from system identification, as well as novel parameterizations of robust Kalman filters, we provided, to the best of our knowledge, the first end-to-end sample complexity bounds for the Kalman filtering of an unknown autonomous LTI system. Our analysis revealed that, depending on the spectral properties of the CE Kalman filter, a robust Kalman filter approach may lead to improved performance. In future work, we would like to explore how to improve robustness and performance by further exploiting information about system uncertainty, as well as how to integrate our results into an optimal control framework, such as Linear Quadratic Gaussian control.
