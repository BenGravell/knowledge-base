<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty

Topics include Robustness, Uncertainty, Sample complexity.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper studies the sample complexity of the stochastic Linear Quadratic Regulator when applied to systems with multiplicative noise. We assume that the covariance of the noise is unknown and estimate it using the sample covariance, which results in suboptimal behaviour. The main contribution of this paper is then to bound the suboptimality of the methodology and prove that it decreases with 1/N, where N denotes the amount of samples. The methodology easily generalizes to the case where the mean is unknown and to the distributionally robust case studied in a previous work of the authors. The analysis is mostly based on results from matrix function perturbation analysis.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The field of learning control has recently seen explosive growth, which can be attributed to the availability of large amounts of data, creating an incentive for controllers that use the available information optimally. A significant amount of this research effort is being directed towards the familiar Linear Quadratic Regulation (LQR) problem where the transition matrices are unknown. Most of these developments however are related to deterministic systems.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Instead this paper takes a different approach, considering systems that intrinsically include the uncertainty in the dynamics through stochastic disturbances. More specifically we study systems with a time-varying multiplicative disturbance. These may cover a wide range of system classes like Linear Parameter Varying (LPV) systems and Linear Difference Inclusions (LDI) or in our case, when the disturbance varies stochastically, systems with multiplicative noise. Such systems have already been studied in the context of learning control by using policy iteration and intrinsically introduce robustness in the controller design.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The authors previously developed a control synthesis procedure using the *distributionally robust approach* that guarantees stability with high probability, when the true distribution of the system is not known. This paper is related to that result and provides a methodology to evaluate the performance of the *empirical approach*, where the sample mean and covariance are used to produce a controller making it similar to the *certainty equivanlent approach* for deterministic LQR. Therefore the proofs are similar to the result of Mania et. al., where the sample complexity of this certainty equivalent approach is studied.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The main result is then a suboptimality guarantee for the empirical controller. To produce such a result we make use of Riccati perturbation analysis. This paper is, to the authors' knowledge, the first instance of such a perturbation analysis being applied to discrete time systems with multiplicative noise. A Riccati perturbation bound for continuous time systems was already produced.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The remainder of this paper is then structured as follows. Section 2 presents the problem statement and the assumptions used throughout the paper. The main result is then presented in Section 3 in the form of three theorems that show how the uncertainty on the covariance propagates throughout the controller synthesis. The proof of these three components are then given in the following sections. Section 4 lists some results that are required for the remainder of the derivations as well as a way of deriving confidence bounds for the sample covariance. Section 5 then extends upon the results of Konstantinov et. al. to study the perturbed Riccati equation. Section 6 uses a result from convex analysis to derive a bound for the perturbation of the controller. Then Section 7 proofs the main suboptimality bound, from which a sufficient condition for mean square stability (*m.s.s.*) of the true system under the empirical controller also follows. Finally Section 8 provides a conclusion and suggestions for further work.

<!-- chunk {"id": "body-0008", "role": "body", "section": "PROBLEM STATEMENT", "weight": 1.0} -->

In this section, we describe the problem statement and state the main result.

<!-- chunk {"id": "body-0009", "role": "body", "section": "LQR for systems with multiplicative noise", "weight": 1.0} -->

where we assume that $Q \succ 0$ and $R \succ 0$.^11^1This assumption is not strictly necessary, see for some discussion. The solution of will yield a controller that renders the closed-loop system exponentially mean square stable (*e.m.s.s.*) \[1, Definition 1\]. Note that for the dynamics in *m.s.s.* is equivalent to *e.m.s.s.* \[1, Theorem 2\]. Therefore we will say a system is *m.s.s.* throughout the paper, thereby also implying it is *e.m.s.s.*.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Assumption 2.2", "weight": 1.0} -->

This assumption is valid with high probability when ${\hat{\Sigma}}_{0} = \begin{bmatrix}
\end{bmatrix}$ where $\hat{\Sigma} = {\sum_{i = 1}^{N}{w_{i}w_{i}^{\top}}}$ and under some additional assumptions on $w$, which are stated in Section 4. It is also applicable for the case where the mean is also unknown and estimated as the sample mean. The constants ${\underset{¯}{\mathbf{α}}}_{\mathbf{\Sigma}}$ and ${\overline{\mathbf{α}}}_{\mathbf{\Sigma}}$ depend on $N$, which is made explicit by using bold symbols.

<!-- chunk {"id": "body-0011", "role": "body", "section": "MAIN RESULT", "weight": 1.0} -->

Starting from this assumption we will study the optimal controller produced by applying Proposition 2.1. ‣ 2.1 LQR for systems with multiplicative noise ‣ 2 PROBLEM STATEMENT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty") for $\Sigma_{0}$ and ${\hat{\Sigma}}_{0}$ which we will denote as $K^{\ast}$ (*nominal controller*) and $\hat{K}$ (*empirical controller*) respectively. The goal is then to quantify the difference between $J_{K^{\star}}{(x_{0})}$ and $J_{\hat{K}}{(x_{0})}$. To do so we study how the perturbation on $\Sigma_{0}$ propagates through the controller synthesis in three stages. The first stage is how the solution of the Riccati equation is perturbed, which is quantified in Theorem 3.1. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty").

<!-- chunk {"id": "body-0012", "role": "body", "section": "MAIN RESULT", "weight": 1.0} -->

The second stage is the perturbation of the control gain, quantified in Theorem 3.2. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty"). The final stage is then the suboptimality, quantified in Theorem 3.3. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty").

<!-- chunk {"id": "body-0013", "role": "body", "section": "MAIN RESULT", "weight": 1.0} -->

We state these theorems for a system with dynamics, with ${IE{\lbrack w\rbrack}} = 0$ and ${IE{\lbrack{ww^{\top}}\rbrack}} = \Sigma$ and $K^{\star}$ the optimal controller and $P^{\star}$ the solution of (3. ‣ 2.1 LQR for systems with multiplicative noise ‣ 2 PROBLEM STATEMENT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty")). Then assume we have some ${\hat{\Sigma}}_{0} = {\Sigma_{0} + {\Delta\Sigma_{0}}}$ which satisfies Assumption 2.2 and denote by $\hat{K}$ the optimal controller for ${\hat{\Sigma}}_{0}$ and $\hat{P}$ the solution of (3. ‣ 2.1 LQR for systems with multiplicative noise ‣ 2 PROBLEM STATEMENT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty")).

<!-- chunk {"id": "body-0014", "role": "body", "section": "MAIN RESULT", "weight": 1.0} -->

The constants used in the theorems below are listed in Table 1.

<!-- chunk {"id": "body-0015", "role": "body", "section": "PRELIMINARY RESULTS", "weight": 1.0} -->

In this section we provide some results that will be used throughout the remainder of this paper. First we slightly alter a previous result from high-dimensional statistics that results in a condition on ${\hat{\Sigma}}_{0}$ as. Second we introduce three lemmas that are related to bounding the operator norms of versions of $\mathcal{F}$, $\mathcal{G}$ and $\mathcal{L}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 4.1", "weight": 1.0} -->

Here we follow the definition of a sub-Gaussian random vector (denoted by $subG$) given in \[1, Definition 5\]. Condition (iv) holds for example for gaussian $w$ ($\sigma = 1$) and for $w$ with bounded support (where $\sigma$ can be estimated from data ).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Norms of matrix operators", "weight": 1.0} -->

We will consider bounding norms associated with $\mathcal{F}$ and $\mathcal{G}$ in two circumstances. The first being where we have some $\Delta\Sigma_{0}$ that is constrained. The second being the case where we have some ${\parallel{\DeltaP}\parallel} \leq \epsilon$. To deal with these two cases we will use the lemmas given below.

<!-- chunk {"id": "body-0018", "role": "body", "section": "RICCATI PERTURBATION", "weight": 1.0} -->

In this section we study the stochastic Riccati equation with perturbed parameters. The goal is to bound how much such perturbations affect the solutions, thereby proving Theorem 3.1. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty"). To do so we will use the methodology applied, to the deterministic case. The main proof is stated at the end of the section, for which we state the main component first. This is a reformulation of the perturbed Riccati equation as a fixed-point equation.

<!-- chunk {"id": "body-0019", "role": "body", "section": "RICCATI PERTURBATION", "weight": 1.0} -->

with $\mathcal{L}_{\star}$ the Lyapunov operator for the optimal closed-loop system --- which is invertible since the closed-loop system is *m.s.s.* --- and where

<!-- chunk {"id": "body-0020", "role": "body", "section": "RICCATI PERTURBATION", "weight": 1.0} -->

Using the constants in Table 1, Lemma 5.1 then describes two essential properties of $\Phi$. The proof is deferred to Appendix.1.

<!-- chunk {"id": "body-0021", "role": "body", "section": "CONTROLLER PERTURBATION", "weight": 1.0} -->

In this section we derive a bound on $\parallel{K^{\star} - \hat{K}}\parallel$, thereby proving Theorem 3.2. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty"). We state the proof at the end of the section, but first introduce some of the components.

<!-- chunk {"id": "body-0022", "role": "body", "section": "SUBOPTIMALITY", "weight": 1.0} -->

This section is dedicated to the proof of the main result of this paper. More specifically we derive a bound for the suboptimality of the empirical controller compared to the nominal one, given in (8. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty")) as a part of Theorem 3.3. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty"). The proof of which is stated at the end of this section.

<!-- chunk {"id": "body-0023", "role": "body", "section": "SUBOPTIMALITY", "weight": 1.0} -->

We can then state the following lemma

<!-- chunk {"id": "body-0024", "role": "body", "section": "CONCLUSIONS AND FUTURE WORKS", "weight": 1.0} -->

This paper studied the sample complexity of LQR applied to systems with multiplicative noise. Overall we provided three types of sample complexities in Theorem 3.1. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty")-3.3. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty").

<!-- chunk {"id": "body-0025", "role": "body", "section": "CONCLUSIONS AND FUTURE WORKS", "weight": 1.0} -->

The first is given in Theorem 3.1. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty"), which produces a bound on the amount of samples required to make the resulting problem stabilizable and the Riccati perturbation finite.

<!-- chunk {"id": "body-0026", "role": "body", "section": "CONCLUSIONS AND FUTURE WORKS", "weight": 1.0} -->

The second sample-complexity is the one related to stability, given in Theorem 3.3. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty"). It gives a bound on the amount of samples required before the produced controller stabilizes the true system.

<!-- chunk {"id": "body-0027", "role": "body", "section": "CONCLUSIONS AND FUTURE WORKS", "weight": 1.0} -->

The final sample-complexity is then related to performance. It is given in Corollary 3.4. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty") and states that the suboptimality decreases with $1/N$. This is the same rate as was derived for determinstic certainty equivalent LQR.

<!-- chunk {"id": "body-0028", "role": "body", "section": "CONCLUSIONS AND FUTURE WORKS", "weight": 1.0} -->

In future work, we aim to extend the results to partially observed systems and to the distributionally robust approach, where the stability complexity is absent, since it is satisfied automatically.
