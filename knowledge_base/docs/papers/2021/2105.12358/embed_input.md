<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Certainty Equivalent Quadratic Control for Markov Jump Systems

Topics include Markov jump systems, Certainty equivalence, Linear quadratic control, Riccati equation, Robustness, Perturbation bounds.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Develops perturbation bounds for certainty-equivalent quadratic control of Markov jump linear systems with errors in dynamics and transition probabilities. The paper isolates how uncertainty propagates through coupled Riccati equations and the optimal cost, supporting model-based control under estimated jump dynamics.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Real-world control applications often involve complex dynamics subject to abrupt changes or variations. Markov jump linear systems (MJS) provide a rich framework for modeling such dynamics. Despite an extensive history, theoretical understanding of parameter sensitivities of MJS control is somewhat lacking. Motivated by this, we investigate robustness aspects of certainty equivalent model-based optimal control for MJS with quadratic cost function. Given the uncertainty in the system matrices and in the Markov transition matrix is bounded by epsilon and eta respectively, robustness results are established for (i) the solution to coupled Riccati equations and (ii) the optimal cost, by providing explicit perturbation bounds which decay as O(epsilon+ eta) and O((epsilon+ eta)^) respectively.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The Linear Quadratic Regulator (LQR) is both theoretically well understood and commonly used in practice when the system dynamics are known. It also provides an interesting benchmark, when system dynamics are unknown, for reinforcement learning with continuous state and action spaces and for adaptive control.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A natural generalization of linear dynamical systems is Markov jump linear systems (MJS) that allow the dynamics of the underlying system to switch between multiple linear systems according to an underlying finite Markov chain. Similarly, a natural generalization of LQR problem to MJS is to use mode-dependent cost matrices, which allows to have different control goals under different modes. While the optimal control for MJS-LQR is well understood when one has perfect knowledge of the system dynamics, in practice it may not be optimal due to the imperfect knowledge of the system dynamics and the transition matrix. For instance, one might use system identification techniques to learn an approximate model for the system. Designing optimal controllers for MJS-LQR with this approximate system dynamics and transition matrix in place of the true ones leads to so-called certainty equivalent (CE) control which is used extensively in practice. However, a theoretical understanding of the suboptimality of the CE control for MJS-LQR is lacking. The main challenge here is the hybrid nature of the problem that requires consideration of both the system dynamics uncertainty $\epsilon$, and the underlying Markov transition matrix uncertainty $\eta$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The solution of infinite horizon MJS-LQR involves coupled algebraic Riccati equations. Our goal is to understand how sensitive the solution of these equations and the corresponding optimal cost are to the perturbations in system model. To this aim, we first develop explicit $\mathcal{O}{({\epsilon + \eta})}$ perturbation bound for the solution to coupled algebraic Riccati equations that arise in the context of MJS-LQR. This in turn is used to establish explicit $\mathcal{O}{({({\epsilon + \eta})}^{2})}$ suboptimality bound. Finally, numerical experiments are provided to support our theoretical claims. Our proof strategy requires nontrivial advances over those of. Specifically, the coupled nature of Riccati equations requires novel perturbation arguments as these coupled equations lack some of the nice properties of the standard Riccati equations, like uniqueness of solutions under certain conditions or being amenable to matrix factorization based approaches.

<!-- chunk {"id": "body-0007", "role": "body", "section": "III-B Linear Quadratic Regulator", "weight": 1.0} -->

Unlike classical LQR for LTI systems, where cost matrices are usually fixed throughout the time horizon, the mode-dependent cost matrices in MJS-LQR allows us to have different control goals under different modes. To guarantee MJS-LQR is solvable, we assume the MJS in and the cost matrices satisfy the following.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

The following lemma characterizes some properties of the minimizer of.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Perturbation Analysis for MJS-LQR", "weight": 1.0} -->

Before we formally state our results, we introduce a few more concepts and assumptions.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In this section, we present some numerical results to support our proposed theory. All of the synthesis and performance experiments are run in MATLAB.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We next study how the system errors vary with ${\epsilon_{\mathbf{A}},\epsilon_{\mathbf{B}},\eta_{\mathbf{T}}} \in {\{ 0.01,0.02,0.05,0.1,0.2,0.3\}}$, and the number of modes $s \in {\{ 10,20,30,40\}}$. We set the number of states and inputs to $n = 10$ and $p = 5$, respectively. For each choice of $\epsilon_{\mathbf{A}}$, $\epsilon_{\mathbf{B}}$, and $\eta_{\mathbf{T}}$, we run $100$ experiments, and record $(\mathbf{P}_{1:s}^{\star},{\hat{\mathbf{P}}}_{1:s})$ and the costs for these matrices.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In this work, we provide a perturbation analysis for cDARE, which arise in the solution of MJS-LQR, and an end-to-end suboptimality guarantee for certainty equivalence control for MJS-LQR. Our results show the robustness of the optimal policy to perturbations in system dynamics and establish the validity of the certainty equivalent control in a neighborhood of the original system. This work opens up multiple future directions. First, with proper system identification algorithms, we can analyze model-based online/adaptive algorithms where control policy is updated continuously over a single trajectory. Second, a natural extension would be to study MJS with output measurements where states are only partially observed, i.e., the LQG setting. This will require considering the dual coupled Riccati equations for filtering.
