<!-- arxiv-full-text:v1 {"arxiv_id": "2609.23692", "source": "arxiv-html"} -->

## Introduction

Learning a stabilizing controller is a key step in many learning-based control tasks. Recent works have studied fundamental limits of learning to stabilize from a statistical perspective. In these works, the hardness of the problem is characterized by sample complexity, i.e., the number of samples required to achieve stabilization with high probability. Of particular relevance is, which shows that the hardness of learning to stabilize is governed by two key factors: distinguishability and co-stabilizability of the systems involved. While these principles appear broadly applicable, most existing sample complexity results focus on linear systems under full state observation with linear static state feedback controllers.^11^ 1 While dynamic controllers are used in some learning-based control approaches, the specific benefits of controller memory for stabilization have not been systematically investigated to the best of our knowledge.

Motivated by these observations, we focus on the *co-stabilization* problem, i.e., designing a single controller that stabilizes multiple systems. Co-stabilization is a fundamental structural property underlying robustness and learning-based control: the ability to stabilize a larger set of systems directly translates into increased tolerance to model uncertainty.

A key fact underlying our work is the following. While any stabilizable fully observed linear system admits a stabilizing linear static state feedback controller, this equivalence does not extend to co-stabilization. In particular, there exist pairs of systems that cannot be co-stabilized by any linear static state feedback controller but can be co-stabilized by a linear dynamic state feedback controller. This observation suggests that controller memory can fundamentally enlarge the class of systems that can be co-stabilized by a single policy. In this paper, we formalize this intuition and develop an algorithm to empirically demonstrate the benefits of dynamic state feedback for co-stabilization. Specifically, our contributions are summarized as follows: First, we prove that the linear dynamic state feedback is more expressive on the co-stabilization problem than the linear static state feedback for some typical examples from the literature. This is achieved by using results from strong stabilization and simultaneous stabilization in robust control.

Inspired by our theoretical results, we design a co-stabilization path integral algorithm, which iteratively updates linear dynamic state feedback policies, and empirically verify the advantage of linear dynamic state feedback on co-stabilization.

The rest of the paper is organized as follows. In Section II, we introduce the problem setup. In Section III, we present our main theoretical results. In Section IV, we develop a path-integral-based algorithm for computing co-stabilizing controllers. Section V provides numerical experiments. Finally, Section VI concludes the paper and discusses future directions. All proofs are deferred to the appendix.

## Problem Setup

We consider the following fully-observed discrete-time linear time-invariant (LTI) system: where $\mathbf{x}_{t}\in\mathbb{R}^{n}$, $\mathbf{u}_{t}\in\mathbb{R}^{m}$ are the state and input at time $t$. For simplicity, we assume $\mathbb{E}[\mathbf{x}_{0}\mathbf{x}_{0}^{\top}]=\mathbf{I}_{n}$. In the remainder of the paper, we denote a system in the form by the pair $(\mathbf{A},\mathbf{B})$.

We consider linear dynamic state feedback controllers, represented with a linear time-invariant system of the form: where the parameter matrices $\mathbf{K}\in\mathbb{R}^{m\times n}$, $\mathbf{H}\in\mathbb{R}^{m\times p}$, $\mathbf{G}\in\mathbb{R}^{p\times n}$, $\mathbf{F}\in\mathbb{R}^{p\times p}$, and the state of the controller $\mathbf{z}_{t}\in\mathbb{R}^{p}$, where $p$ is the memory of the controller. Then, the following augmented system represents the closed-loop:

### Remark 1

When $\mathbf{H}=\mathbf{0}_{m\times p},\mathbf{G}=\mathbf{0}_{p\times n},$ and $\mathbf{F}=\mathbf{0}_{p\times p}$, the linear dynamic state feedback controller is reduced to the linear static state feedback controller $\mathbf{u}_{t}=\mathbf{K}\mathbf{x}_{t}$. When $\mathbf{G}=[\mathbf{I}_{n}\;\mathbf{0}_{n\times(h-1)n}]^{\top}$, $\mathbf{F}=\begin{bmatrix}\mathbf{0}_{n\times(h-1)n}&\mathbf{0}_{n\times n}\\\mathbf{I}_{(h-1)n}&\mathbf{0}_{(h-1)n\times n}\end{bmatrix}$, and $\mathbf{H}=[\mathbf{K}_{1}\dots\mathbf{K}_{h-1}]$ with $\mathbf{K}_{i}\in\mathbb{R}^{m\times n}$ for $i\in[h-1]$, the linear dynamic state feedback controller is reduced to the linear state-history feedback controller $\mathbf{u}_{t}=\mathbf{K}\mathbf{x}_{t}+\sum_{i=1}^{h-1}\mathbf{K}_{i}\mathbf{x}_{t-i}$.

Since a linear static state feedback controller is a special case of a linear dynamic state feedback controller, any task that can be achieved by the former can also be achieved by the latter. On the other hand, when $(\mathbf{A},\mathbf{B})$ is given, it is well known that there exists a controller that stabilizes $(\mathbf{A},\mathbf{B})$ if and only if there exists a linear static state feedback controller that does so (see, e.g., \[9, Theorem 14.5\]). Next, we look at the problem of co-stabilization (also known as simultaneous stabilization ).

### Definition 1 (Co-stabilizability by a linear controller)

A pair of systems $S_{1}=(\mathbf{A}_{1},\mathbf{B}_{1})$ and $S_{2}=(\mathbf{A}_{2},\mathbf{B}_{2})$ is co-stabilizable by a linear controller $S_{c}$ if both the feedback interconnection of $S_{1}$ and $S_{c}$ and that of $S_{2}$ and $S_{c}$ are asymptotically stable.

Note that in the case of linear static state feedback controllers, this definition simplifies to existence of $\mathbf{K}$ such that $\max_{i\in\{1,2\}}\{\rho(\mathbf{A}_{i}+\mathbf{B}_{i}\mathbf{K})\}<1$, where $\rho(\cdot)$ denotes the spectral radius of a square matrix. Similarly, the pair is said to be co-stabilizable by a linear dynamic state feedback if there exist a dimension $p\in\mathbb{Z}_{\geq 0}$ and feedback gains $(\mathbf{K},\mathbf{H},\mathbf{G},\mathbf{F})$ such that $\max_{i\in\{1,2\}}\{\rho(\mathbf{D}_{\mathbf{A}_{i},\mathbf{B}_{i}})\}<1$.

## Linear Static State Feedback vs. Linear Dynamic State Feedback

Pair with $a_{1}=a_{2}=a,\tfrac{b_{1}}{b_{2}}>\tfrac{a+1}{a-1}$ exp (n)-hard pair from exp (n)-hard pair from TABLE I: Co-Stabilizability Summary (|a1|,|a2| > 1, b > 0) In this section, we compare the co-stabilization capabilities of linear static state feedback and linear dynamic state feedback controllers on scalar systems and $\exp(n)$-hard systems. We show that linear dynamic state feedback controllers are strictly more expressive in certain settings than linear static state feedback controllers.

### III-A Scalar Systems

We first consider a class of discrete-time scalar systems. Let where $i\in\{1,2\}$, $x_{t},u_{t}\in\mathbb{R}$, and $b_{i}\neq 0$ for $i=1,2$.

The following theorem shows that linear dynamic state feedback can strictly enlarge the class of co-stabilizable system pairs compared to linear static state feedback.

### Theorem 1

The following two scalar pairs cannot be co-stabilized by any linear static state feedback controller, but can be co-stabilized by a linear dynamic state feedback controller: Systems in with $|a_{1}|,|a_{2}|>1$, $|a_{1}-a_{2}|>2$, and $b_{1}=b_{2}$; Systems in with $a_{1}=a_{2}=a>1$ and $\frac{b_{1}}{b_{2}}>\frac{a+1}{a-1}.$ Note that this result is existential and not constructive. In general, we do not know how much memory the dynamic state feedback controller would require. On the other hand, for some fixed small values of the memory, we can further quantify the advantage of dynamic controllers by characterizing the co-stabilization gap, i.e., the maximum distance in the parameter space that still allows co-stabilization.

### Proposition 1

Consider $S_{1}$ and $S_{2}$ in with $a_{1}\neq a_{2}$, $|a_{1}|,|a_{2}|>1$, and $b_{1}=b_{2}=b\neq 0$. Then: a co-stabilizing linear static state feedback controller exists if and only if $|a_{1}-a_{2}|<2$; a co-stabilizing linear state-history feedback controller of the form $u_{t}=k_{0}x_{t}+k_{1}x_{t-1}$ exists if and only if $|a_{1}-a_{2}|<4$.

Proposition 1 shows that even a finite-memory dynamic controller significantly enlarges the admissible co-stabilization region compared to static feedback. However, as Proposition 1 illustrates, finite controller memory may still lead to a bounded co-stabilization gap. The general quantitative relationship between controller memory and achievable co-stabilization gap remains open.

We next present a pair of systems that cannot be co-stabilized even by linear dynamic state feedback.

### Theorem 2

Consider $S_{1}$ and $S_{2}$ in with $a_{1}=a_{2}=a$, $|a|\geq 1$, and $b_{1}=-b_{2}=b>0$. Then no linear static or linear dynamic state feedback controller can co-stabilize this pair.

This result shows that dynamic state feedback does not universally overcome structural obstructions to co-stabilization.

### III-B $\exp(n)$-Hard Systems

This naturally raises the question of whether dynamic state feedback can remove the $\exp(n)$ hardness of learning to stabilize, which was established for static state feedback. Consider the parametrized pair: where $i\in\{3,4\}$ and $n\geq 2$.

In the construction of $\exp(n)$-hard systems , co-stabilization by a linear static state feedback controller requires the system parameters to be exponentially close in the state dimension $n$.

### Theorem 3

For the pair in (5-Hard Systems ‣ III Linear Static State Feedback vs. Linear Dynamic State Feedback ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization")) with $r>1$, $\alpha_{3}=\alpha_{4}=1$, $0<v<\frac{r-1}{2}$, $b^{}=0$, $b^{}=\bar{b}$, and $\bar{b}>\left(\frac{2v}{r-1}\right)^{n}$, no linear static state feedback controller can co-stabilize the systems, whereas a linear dynamic state feedback controller can.

Theorem 1, together with Theorem 3-Hard Systems ‣ III Linear Static State Feedback vs. Linear Dynamic State Feedback ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization"), demonstrates that linear dynamic state feedback is strictly more expressive than linear static state feedback in the co-stabilization problem. However, this phenomenon does not extend to all $\exp(n)$-hard instances. In particular, combining Theorem 2 with the construction of $\exp(n)$-hard systems , we obtain the following.

### Theorem 4

For the pair in (5-Hard Systems ‣ III Linear Static State Feedback vs. Linear Dynamic State Feedback ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization")) with $r>1$, $\alpha_{3}=1$, $\alpha_{4}=-1$, $0<v<1$, and $b^{}=b^{}=0$, no linear dynamic state feedback controller can co-stabilize the systems.

Therefore, linear dynamic state feedback might not eliminate the $\exp(n)$ hardness of learning to stabilize established .

## Co-Stabilization by Path Integral with State-History Feedback

In the previous section, we established that linear dynamic state feedback is strictly more expressive than static feedback for co-stabilization. We now turn to the algorithmic problem of computing such controllers.

Finding a co-stabilizing controller for a given set of systems is, in general, hard. Existing work based on linear matrix inequalities (LMIs) provides sufficient conditions by requiring a shared Lyapunov function (see, e.g., Section 7.2.3 in ). Policy gradient methods have recently emerged as an alternative to LMIs, sometimes with global or local convergence guarantees. In this section, inspired by the path-integral policy search framework developed , and the stabilization strategy proposed , we propose a path integral algorithm for computing co-stabilizing controllers for a finite set of linear systems.

We first present our algorithm for linear static state feedback controllers. Then we will show that based on the reparametrizations, the same algorithm can be used to search for dynamic controllers.

### Remark 2

The previous section focuses on the theoretical characterization of co-stabilization of two systems, reflecting the inherent limitations of existing analytical tools in robust control. In contrast, the algorithm developed here is applicable to co-stabilize multiple systems.

Consider a finite collection $\left\{(\mathbf{A}_{i},\mathbf{B}_{i})\right\}_{i\in[M]}$ of linear systems. For a fixed feedback gain $\mathbf{K}$ and discount factor $\gamma\in$, define the infinite-horizon discounted federated LQR cost $J_{\mathrm{Co}}(\gamma,\mathbf{K}):=\frac{1}{M}\sum_{i=1}^{M}J(\gamma,\mathbf{K},\mathbf{A}_{i},\mathbf{B}_{i}),$ where with $\mathbb{E}[\mathbf{x}_{0}\mathbf{x}_{0}^{\top}]=\mathbf{I}_{n}$, $\mathbf{Q}\succeq 0$, and $\mathbf{R}\succ 0$. For later use, define For each system and fixed gain $\mathbf{K}$, define $\mathbf{P}^{i,\gamma}_{\mathbf{K}}$ and $\boldsymbol{\Sigma}^{i,\gamma}_{\mathbf{K}}$ as the unique positive semidefinite solutions of the discrete Lyapunov equations Under the assumption $\mathbb{E}[\mathbf{x}_{0}\mathbf{x}_{0}^{\top}]=\mathbf{I}_{n}$, Lemma 1 of implies $J(\gamma,\mathbf{K},\mathbf{A}_{i},\mathbf{B}_{i})=\operatorname{trace}\left(\mathbf{P}^{i,\gamma}_{\mathbf{K}}\right).$ Hence, the federated objective in can be evaluated by solving $M$ Lyapunov equations.

We now present the co-stabilization path-integral algorithm, summarized in Alg. 1, where $\underline{\sigma}$ denotes the least singular value of a matrix. The inner loop performs a zeroth-order stochastic descent via exponential reweighting of sampled perturbations, which follows the path integral idea . The update of $\alpha_{j}$ follows the stabilization idea . Unstable candidate gains are penalized by assigning a large cost $J_{\max}$.

Systems {(Ai, Bi)}i = 1M; Q ≽ 0, R ≻ 0; initial gain K0; γ0 ∈; λ > 0; r > 0; T; N; ξ ∈; $\underline{\alpha}$; Jmax > 0. Returns the feasibility flag and gain. $\widehat{\mathbf{K}}^{(j)}_{0}\leftarrow\mathbf{K}_{j}$ $\mathbf{K}_{n}\leftarrow\widehat{\mathbf{K}}^{(j)}_{t}+\Delta_{\mathbf{K},n}$ if $\rho(\sqrt{\gamma_{j}}(\mathbf{A}_{i}+\mathbf{B}_{i}\mathbf{K}_{n}))\geq 1$ for some i then $w_{n}\leftarrow\exp\!\left(-\frac{J_{n}-J_{\min}}{\lambda}\right)$, $v_{n}\leftarrow\frac{w_{n}}{\sum_{k}w_{k}}$ $\widehat{\mathbf{K}}^{(j)}_{t+1}\leftarrow\widehat{\mathbf{K}}^{(j)}_{t}+\sum_{n=1}^{N}v_{n}\Delta_{\mathbf{K},n}$ $\mathbf{K}_{j+1}\leftarrow\widehat{\mathbf{K}}^{(j)}_{T}$ $\alpha_{j}\leftarrow\frac{\underline{\sigma}(\mathbf{Q}+\mathbf{K}_{j+1}^{\top}\mathbf{R}\mathbf{K}_{j+1})}{\overline{J}(\gamma_{j},\mathbf{K}_{j+1})-\underline{\sigma}(\mathbf{Q}+\mathbf{K}_{j+1}^{\top}\mathbf{R}\mathbf{K}_{j+1})}$ if $\underset{i\in[M]}{\max}\rho(\mathbf{A}_{i}+\mathbf{B}_{i}\mathbf{K}_{j+1})<1$ then if γj + 1 ≥ 1 or $\alpha_{j}\leq\underline{\alpha}$ then Algorithm 1 Co-Stabilization by Path Integral Next, we show how to use Alg. 1 to get a co-stabilizing linear state-history feedback controller. For any $h\geq 1$, define the history-augmented state Then we have the lifted dynamics Then, by the reparametrizations for linear state-history feedback controllers, co-stabilization of linear state-history feedback reduces to linear static state feedback co-stabilization of the augmented systems, to which Alg. 1 applies directly.

### Remark 3 (Limits of LMI-based Co-Stabilization with Memory)

Although linear dynamic state feedback and state-history feedback can strictly enlarge the set of co-stabilizable systems, this advantage is not captured by standard LMI-based approaches based on a common quadratic Lyapunov function . In particular, it can be proved that augmenting the system with linear dynamic state feedback or state-history feedback does not enlarge the feasibility region of the corresponding co-stabilization LMI. This highlights a fundamental limitation of LMI-based methods: while dynamic controllers provide additional expressive power for co-stabilization, convex formulations based on common Lyapunov functions fail to exploit this benefit.

## Experiments

We conduct three numerical experiments to validate the theoretical results developed in the previous sections. The first two experiments are to check how Alg. 1 with linear state-history feedback^22^ 2 Empirically, we have not observed a substantial performance difference when using linear dynamic feedback versus linear state-history feedback with our algorithm. Hence, we restrict our experiments to the latter. is affected the controller memory and the original state dimension. The third experiment is to compare Alg. 1 with a co-stabilization policy gradient method from the literature.

### V-A Horizon vs. Co-Stabilization Gap

We first investigate how increasing the horizon of a linear state-history controller enlarges the co-stabilization region. Consider the scalar pair in with $a_{1}=a_{2}=1.2$, $b_{1}=1$, and $b_{2}>0$. We apply Alg. 1 to compute a co-stabilizing linear state-history feedback controller for $\{(a_{i},b_{i})\}_{i=1,2}$. For horizon $h$, the systems are lifted according to.

The hyperparameters of Alg. 1 are: $\mathbf{K}_{0}=\mathbf{0}$, $\mathbf{Q}^{\mathrm{his}}=\mathbf{I}_{h},\quad\mathbf{R}^{\mathrm{his}}=1$, $\xi=0.99$, $\lambda=10^{-4},\quad r=1\times 10^{-1}$, $T=20$, $N=20$, $J_{\max}=10^{12}$, and $\gamma_{0}=1/{\left(1+\max\{1,\max_{i\in\{1,2\}}\rho(\mathbf{A}^{\mathrm{his}}_{i}+\mathbf{B}^{\mathrm{his}}_{i}\widehat{\mathbf{K}}^{\mathrm{his}}_{0})\}^{2}\right)}.$

### Feasibility criterion

We declare Alg. 1 feasible for $\{(\mathbf{A}_{i},\mathbf{B}_{i})\}_{i=1,2}$ if, upon termination (i.e., $\gamma_{j+1}\geq 1$ or $\alpha_{j}\leq\underline{\alpha}=10^{-6}$), the returned gain $\widehat{\mathbf{K}}^{\mathrm{his}}_{j+1}$ satisfies Otherwise, the algorithm is declared infeasible.

### Largest admissible gap

For each horizon $h$, we apply a bisection procedure to determine the largest $\bar{b}_{2}$ such that Alg. 1 remains feasible. Fig. 1 plots $\bar{b}_{2}$ as a function of $h$.

The results in Fig. 1 show that in our experiments, the estimated feasible region increases monotonically with horizon. In particular, state-history feedback ($h>1$) achieves a strictly larger $\bar{b}_{2}$ than static state feedback ($h=1$), empirically supporting Theorem 1.

Fig. 1: Largest feasible b2 versus horizon h. In addition, the largest feasible b2 by solving LMI with a common quadratic Lyapunov function is 10.99.

### V-B Exponential Hardness in System Dimension

We next examine how the co-stabilization gap scales with system dimension. Consider the system in (5-Hard Systems ‣ III Linear Static State Feedback vs. Linear Dynamic State Feedback ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization")) with parameters $r=1.2$, $v=0.5$, $b^{}=0$, and $b^{}=\bar{b}>0$. We vary the state dimension $n\in\{2,3,4,5\}$.

We compare three approaches: i) LMI-based common quadratic Lyapunov method, which is also employed , ii) linear static state-feedback co-stabilization using Alg. 1 ($h=1$); and iii) linear state-history feedback co-stabilization using Alg. 1 ($h=3$). The hyperparameters of Alg. 1 follow the setup in Section V-A.

Fig. 2 shows $\bar{m}$ versus $n$. While the chosen $v$ does not satisfy the conditions in Theorem 3-Hard Systems ‣ III Linear Static State Feedback vs. Linear Dynamic State Feedback ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization"), all methods exhibit exponential decay of the feasible co-stabilization gap as $n$ increases, suggesting fixed-horizon linear state-history feedback may not remove the $\exp(n)$ hardness identified .

Fig. 2: Largest feasible b̄ versus system dimension n.

### V-C Path Integral vs. Policy Gradient

In this part, we compare our Alg. 1 with the co-stabilization policy gradient algorithm given in for linear static state feedback ($h=1$) and linear state-history feedback with $h=3$. We implement the comparison experiment on the co-stabilization of two scalar systems and two single-input order-$2$ systems. The first one is the scalar pair in with $a_{1}=a_{2}=1.2$ and $b_{1},b_{2}$ are uniformly sampled from $$. The second one is the discretized and linearized inverted pendulum system: with known $dt=1e-4$ and $g=10$. For unknown $l$ and $m$, we independently sample two values from uniform distributions. Specifically, for each sample $i=1,2$, we draw $m_{i}\sim\mathcal{U}[0.75,1.25]$ and $\ell_{i}\sim\mathcal{U}[0.75,1.25]$, and define the corresponding linearized inverted pendulum system $(\mathbf{A}_{i},\mathbf{B}_{i})$. The hyperparameters of Alg. 1 follow the setup in Section V-A. The co-stabilization policy gradient algorithm uses the original implementation in the GitHub repository of. For each case, we run $20$ experiments independently to compute the co-stabilization success rates, which are summarized in Table II. Based on the table, we can see that the path-integral method in Alg. 1 is better than the co-stabilization policy gradient, and the controller memory increases the performance of Alg. 1 for the two implemented cases. A limitation of our Alg. 1 is that it is more time-expensive than the co-stabilization policy gradient.

TABLE II: Success rates comparison.

## Conclusion and Future Work

In this paper, we study the role of controller memory in co-stabilization. We show that linear dynamic state feedback strictly enlarges the class of co-stabilizable systems compared to static feedback, while fundamental limitations remain. On the algorithmic side, we develop a path-integral method for computing co-stabilizing controllers. Future work includes understanding how the controller memory affects the sample complexity of learning-to-stabilize problems. We are also interested in investigating the convergence properties of the proposed path integral algorithm for co-stabilization.

Acknowledgments: This work is supported in part by ONR grant N00014-21-1-2431 (CLEVR-AI). NO would like to thank Constantino Lagoa for some inspiring discussions on co-stabilization.

### A Some Frequency Domain Preliminary Results

In this section, we introduce some continuous-time frequency domain tools from the book. First, we need to introduce coprime factorization, which plays a critical role in feedback and robust control, followed by two useful lemmas.

### Definition 2 (Coprime Factorization)

Consider a continuous-time transfer function $P^{c}(s)$. A set of four stable, proper^33^ 3 A continuous-time transfer function is stable if its poles are all in the left-half complex plane and is proper if the degree of the numerator does not exceed the degree of the denominator. transfer functions $N(s)$, $M(s)$, $X(s)$ and $Y(s)$ is called a coprime factorization of $P^{c}(s)$ if $P^{c}(s)=N(s)/M(s)$ and $N(s)X(s)+M(s)Y(s)=1,$.

### Lemma 1 (\[7, Theorem 3 of Chapter 5\])

A continuous-time transfer function $P^{c}(s)$ is strongly stabilizable if and only if it has an even number of real poles between every pair of non-negative real zeros.

### Lemma 2 (\[7, Theorem 4 of Chapter 5\])

Consider the continuous-time transfer functions $P^{c}_{1}(s)$ and $P^{c}_{2}(s)$. There exists a proper continuous-time transfer function $C^{c}(s)$ such that both $\frac{1}{1+C^{c}(s)P^{c}_{1}(s)}$ and $\frac{1}{1+C^{c}(s)P^{c}_{2}(s)}$ are stable transfer functions if and only if there exist coprime factorizations $(N_{1}(s),M_{1}(s),X_{1}(s),Y_{1}(s))$ and $(N_{2}(s),M_{2}(s),X_{2}(s),Y_{2}(s))$ of $P^{c}_{1}(s)$ and $P^{c}_{2}(s)$, respectively, such that Consider two fully-observed LTI systems $(\mathbf{A}_{1},\mathbf{B}_{1})$ and $(\mathbf{A}_{2},\mathbf{B}_{2})$ defined, for which the output matrix is $\mathbf{I}_{n}$. The open-loop discrete-time transfer functions from input to state for these two systems are $P^{d}_{i}(z)=(z\mathbf{I}_{n}-\mathbf{A}_{i})^{-1}\mathbf{B}_{i}.$ The discrete-time transfer function from state to input for the linear dynamic state feedback controller defined in is $C^{d}(z)=\mathbf{K}+\mathbf{H}(z\mathbf{I}_{p}-\mathbf{F})^{-1}\mathbf{G}.$ In particular, in the following analysis, we restrict attention to scalar (SISO) transfer functions obtained from the systems under consideration via appropriate reductions. With the bilinear transformation $z=\frac{s+1}{s-1}$, we can transfer the discrete-time transfer functions into continuous-time transfer functions $P^{c}_{i}(s)=P^{d}_{i}\left(\frac{s+1}{s-1}\right)$ with $i=1,2$ and $C^{c}(s)=C^{d}\left(\frac{s+1}{s-1}\right)$. Then, the co-stabilization of $(\mathbf{A}_{1},\mathbf{B}_{1})$ and $(\mathbf{A}_{2},\mathbf{B}_{2})$ by linear dynamic state feedback controller defined in is equivalent to finding a proper $C^{c}(s)$ such that both $\frac{1}{1+C^{c}(s)P^{c}_{1}(s)}$ and $\frac{1}{1+C^{c}(s)P^{c}_{2}(s)}$ are stable transfer functions (More details can be found in Chapter 5 of.). This allows us to use Lemma 2. ‣ -A Some Frequency Domain Preliminary Results ‣ VI Conclusion and Future Work ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization") to prove our main results.

### B Proof of Theorem 1

### Proof of Theorem 1

The proof for the linear static state feedback controller follows easily by checking the sign of $a_{1}+b_{1}k$ and $a_{2}+b_{2}k$. Next, we prove the result for the linear dynamic state feedback controller. The discrete-time transfer functions of $S_{1}$ and $S_{2}$ in are $P^{d}_{i}(z)=\frac{b_{i}}{z-a_{i}},$ with $i=1,2$. Mapping the discrete-time transfer functions $P^{d}_{1}(z)$ and $P^{d}_{2}(z)$ into continuous-time transfer functions via the one-to-one bilinear transformation, we get $P^{c}_{i}(s)=\frac{b_{i}(s-1)}{(1-a_{i})s+a_{i}+1},$ with $|a_{i}|\neq 1$ and $b_{i}\neq 0$, for $i=1,2$. We can then construct a coprime factorization of $P_{i}(s)$ for $i=1,2$ as follows: | | $\displaystyle N_{i}(s)$ | $\displaystyle=\frac{b_{i}(s-1)}{s+1},M_{i}(s)=\frac{(1-a_{i})s+(a_{i}+1)}{s+1},$ | | \(16\) | | | $\displaystyle X_{i}(s)$ | $\displaystyle=\frac{\frac{2a_{i}-1}{b_{i}}s-\frac{1}{b_{i}}}{s+1},Y_{i}(s)=\frac{2s}{s+1}.$ | | | Based on (15. ‣ -A Some Frequency Domain Preliminary Results ‣ VI Conclusion and Future Work ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization")) and, noting that $b_{1}=b_{2}\neq 0$, we obtain: Next, we need to determine if the above continuous-time transfer function $\hat{P}(s)$ is strongly stabilizable. The above continuous-time transfer function $\hat{P}(s)$ has two repeated unstable real zeros at $1$, and $1$ is not a pole of $\hat{P}(s)$. Therefore, $\hat{P}(s)$ does not have real poles between its unstable zeros, which, based on Lemma 1. ‣ -A Some Frequency Domain Preliminary Results ‣ VI Conclusion and Future Work ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization"), implies that $\hat{P}(s)$ is strongly stabilizable for all $b_{1}=b_{2}\neq 0$. Then by Lemma 2. ‣ -A Some Frequency Domain Preliminary Results ‣ VI Conclusion and Future Work ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization"), we complete the proof.

As before, the proof for the linear static state feedback controller can be done by checking the stability of $a_{1}+b_{1}k$ and $a_{2}+b_{2}k$. Next, we focus on the proof for linear dynamic state feedback controllers. Based on (15. ‣ -A Some Frequency Domain Preliminary Results ‣ VI Conclusion and Future Work ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization")) and, for $a_{1}=a_{2}=a>1$ and $\frac{b_{1}}{b_{2}}>\frac{a+1}{a-1}$, we have | | | $\displaystyle\frac{\left(b_{2}-b_{1}\right)(s-1)((1-a)s+(a+1))}{\left[\frac{b_{2}}{b_{1}}(2a-1)+2(1-a)\right]s^{2}+\left[2a\left(1-\frac{b_{2}}{b_{1}}\right)+2\right]s+\frac{b_{2}}{b_{1}}}.$ | | | Next, we need to determine if the above continuous-time transfer function $\hat{P}(s)$ is strongly stabilizable. Firstly, the above continuous-time transfer function $\hat{P}(s)$ has two independent unstable real zeros at $1$ and $\frac{a+1}{a-1}$ respectively. Noting that the denominator of $\hat{P}(s)$ is a quadratic and it is greater than zero when evaluated at $1$ and $\frac{a+1}{a-1}$, we conclude that there are either no poles or two real poles between the zeros. Hence, invoking Lemmas 1. ‣ -A Some Frequency Domain Preliminary Results ‣ VI Conclusion and Future Work ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization") and 2. ‣ -A Some Frequency Domain Preliminary Results ‣ VI Conclusion and Future Work ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization") concludes the proof. ∎

### C Proof of Proposition 1

Before proving Proposition 1, we present the Jury test for discrete-time stability of order-$2$ polynomials.

### Lemma 3 (Jury stability test for order-$2$ polynomial, Theorem 4.6 in )

Consider an order-$2$ polynomial $z^{2}+q_{1}z+q_{0}$. All roots of this polynomial are inside the unit circle if and only if $-(1+q_{0})<q_{1}<1+q_{0}$ and $|q_{0}|<1$.

### Proof of Proposition 1

The case of linear static state feedback controller follows as before from checking the stability of $a_{1}+b_{1}k$ and $a_{2}+b_{2}k$ with $k\in\mathbb{R}$. For the memory-2 linear state-history feedback, the augmented closed-loops for $i=1,2$ take the form The characteristic polynomial of $\mathbf{D}_{a_{i},b_{i}}$ is given: Let $k_{0},k_{1}$ stabilize $\mathbf{D}_{a_{1},b_{1}}$ so that the eigenvalues of $\mathbf{D}_{a_{1},b_{1}}$ satisfy $|p_{1}^{cl}|<1$ and $|p_{2}^{cl}|<1$. Then, Based on and, we can use $p_{1}^{cl}$ and $p_{2}^{cl}$ to express all stabilizing $(k_{0},k_{1})$ for $\mathbf{D}_{a_{1},b_{1}}$, Substituting $k_{0}$ and $k_{1}$ from into $\Delta_{2}(z)$, we have Based on the conditions of Jury stability test in Lemma 3. ‣ -C Proof of Proposition ‣ VI Conclusion and Future Work ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization"), $q_{0}$ of $\Delta_{i}(z)$ are the same for $i=1,2$. We just need to check the following condition on $q_{1}$ for $\Delta_{2}(z)$: The result follows by simplifying as:

### D Proof of Theorem 2

### Proof of Theorem 2

Consider $S_{1}$ and $S_{2}$ in with $a_{1}=a_{2}=a$, $|a|\geq 1$, and $b_{1}=-b_{2}=b>0$. Based on (15. ‣ -A Some Frequency Domain Preliminary Results ‣ VI Conclusion and Future Work ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization")) and, for this setting, we have Because $\left(4a+2\right)^{2}+4\left(3-4a\right)=16a^{2}+16=16\left(a^{2}+1\right)>0$, $\hat{P}(s)$ has two real poles.

In addition, it can be checked that the strong stabilizability of $\hat{P}(s)$ is invariant under different coprime factorizations of $P^{c}_{1}(s)$ and $P^{c}_{2}(s)$. Then, if there exists one group of coprime factorization of $P^{c}_{1}(s)$ and $P^{c}_{2}(s)$ such that $\hat{P}(s)$ is not strongly stabilizable, then for all other coprime factorizations, $\hat{P}(s)$ is also not strongly stabilizable.

Next, we discuss the cases $|a|=1$ and $|a|>1$ separately. When $a=1$, $\hat{P}(s)$ have two nonnegative real zeros at $1$ and $+\infty$ and the denominator is $-s^{2}+6s-1$. Since the denominator is a quadratic with a leading negative coefficient, evaluating to a positive number at $1$, there exists a real pole of the system between $1$ and $+\infty$. Combining with Lemma 1. ‣ -A Some Frequency Domain Preliminary Results ‣ VI Conclusion and Future Work ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization"), $\hat{P}(s)$ is not strongly stabilizable for $a=1$. With a similar reasoning, we can show $\hat{P}(s)$ is not strongly stabilizable for $a=-1$ either.

When $|a|>1$, $\hat{P}(s)$ has two independent unstable real zeros at $1$ and $\frac{a+1}{a-1}$ respectively. Next, we determine the positions of poles of $\hat{P}(s)$. First, recall that the denominator evaluates to a positive number at $1$, and it can be shown that it evaluates to $\frac{-4a^{2}}{(a-1)^{2}}<0$ at $\frac{a+1}{a-1}$. Therefore, it can be concluded that $\hat{P}(s)$ has a real pole less than $1$ and one between $1$ and $\frac{a_{1}+1}{a_{1}-1}$. Combining with Lemma 1. ‣ -A Some Frequency Domain Preliminary Results ‣ VI Conclusion and Future Work ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization"), we get that $\hat{P}(s)$ is not strongly stabilizable for all $|a|>1$. Then by Lemma 2. ‣ -A Some Frequency Domain Preliminary Results ‣ VI Conclusion and Future Work ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization"), there does not exist a co-stabilizing linear dynamic state feedback controller for this pair. As the linear static state feedback controller is a special case of the linear dynamic state feedback controller, we complete the proof. ∎

### E Proof of Theorem 3-Hard Systems ‣ III Linear Static State Feedback vs. Linear Dynamic State Feedback ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization")

### Proof of Theorem 3-Hard Systems ‣ III Linear Static State Feedback vs. Linear Dynamic State Feedback ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization")

The proof for linear static state feedback controllers is finished in Proposition 1. Next, let us finish the proof for the linear dynamic state feedback controllers of this case. For the pair in (5-Hard Systems ‣ III Linear Static State Feedback vs. Linear Dynamic State Feedback ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization")) with $r>1$, $\alpha_{3}=\alpha_{4}=1$, $0<v<\frac{r-1}{2}$, $b^{}=0$, $b^{}=\bar{b}$, $S_{3}$ and $S_{4}$ in (5-Hard Systems ‣ III Linear Static State Feedback vs. Linear Dynamic State Feedback ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization")) are able to be reduced to the following two scalar systems: $x_{t+1}^{}=rx_{t}^{}+v^{n}u_{t-n+1}$ and $x_{t+1}^{}=rx_{t}^{}+v^{n}u_{t-n+1}+\bar{b}u_{t}$. The discrete-time transfer functions for these two systems are: Similar to Theorem 1, we replace $z$ with $\frac{s+1}{s-1}$ in $P^{d}_{3}(z)$ and $P^{d}_{4}(z)$ to get their continuous-time transfer functions as follows: | | | $\displaystyle P^{c}_{4}(s)=\frac{v^{n}(s-1)^{n}+\bar{b}(s+1)^{n-1}(s-1)}{\left[(1+r)-(r-1)s\right](s+1)^{n-1}}.$ | | | For $P^{c}_{3}(s)$, a coprime factorization is the following: | | | $\displaystyle N_{3}(s)=\frac{v^{n}(s-1)^{n}}{(s+1)^{n}},$ | $\displaystyle M_{3}(s)=\frac{(1+r)-(r-1)s}{s+1},$ | | \(28\) | | | | $\displaystyle X_{3}(s)=\frac{a_{0}}{s+1},$ | $\displaystyle Y_{3}(s)=\frac{\sum_{k=0}^{n}b_{k}s^{k}}{(s+1)^{n}},$ | | | where $a_{0}=\frac{2\,r^{n+1}}{(r-1)\,v^{n}}$, $b_{n}=-\frac{1}{r-1}$, and | | | $\displaystyle\frac{1}{1+r}\sum_{j=0}^{k}\left(\frac{r-1}{\,1+r\,}\right)^{k-j}\left[\binom{n+1}{j}-\frac{2\,r^{n+1}}{\,r-1\,}\binom{n}{j}(-1)^{n-j}\right],$ | | | for $k=0,1,\dots,n-1.$ For $P^{c}_{4}(s)$, a coprime factorization has the following $N_{4}(s)$ and $M_{4}(s)$ Because $M_{4}(s)=M_{3}(s)$ and $N_{4}(s)=N_{3}+\bar{b}\frac{s-1}{s+1}$, we have Then, combining with (15. ‣ -A Some Frequency Domain Preliminary Results ‣ VI Conclusion and Future Work ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization")), we get | | $\displaystyle\hat{P}(s)$ | $\displaystyle=\frac{\bar{b}((1+r)-(r-1)s)\frac{s-1}{(s+1)^{2}}}{1+\bar{b}\frac{2r^{n+1}}{r-1}\frac{s-1}{(s+1)^{2}}}$ | | \(31\) | Firstly, the above continuous-time transfer function $\hat{P}(s)$ has two independent unstable real zeros at $1$ and $\frac{r+1}{r-1}$ respectively. Next, we determine the positions of the poles of $\hat{P}(s)$. Consider the denominator It can be checked that $Q=4>0$ and $Q((r+1)/(r-1))>0$ for $\bar{b}>0$ and $r>1$. Because $Q(s)$ is a quadratic function, $Q(s)$ always has $0$ or $2$ zeros between $1$ and $(r+1)/(r-1)$. Based on this fact and Lemma 1. ‣ -A Some Frequency Domain Preliminary Results ‣ VI Conclusion and Future Work ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization"), we get that $\hat{P}(s)$ is always strongly stabilizable for all $r>1$ and $\bar{b}>0$. Then by Lemma 2. ‣ -A Some Frequency Domain Preliminary Results ‣ VI Conclusion and Future Work ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization"), we complete the proof. ∎

### F Proof of Theorem 4-Hard Systems ‣ III Linear Static State Feedback vs. Linear Dynamic State Feedback ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization")

### Proof of Theorem 4-Hard Systems ‣ III Linear Static State Feedback vs. Linear Dynamic State Feedback ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization")

For the pair in (5-Hard Systems ‣ III Linear Static State Feedback vs. Linear Dynamic State Feedback ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization")) with $r>1$, $\alpha_{3}=1$, $\alpha_{4}=-1$, $0<v<1$, and $b^{}=b^{}=0$, $S_{3}$ and $S_{4}$ can be reduced to the following two scalar time-delay systems: where $i\in\{5,6\}$, $\alpha_{5}=1$ and $\alpha_{6}=-1$. Therefore, the co-stabilization of $S_{3}$ and $S_{4}$ is equivalent to that of $S_{5}$ and $S_{6}$. When taking $a=r$ and $b=v^{n}$ in Theorem 2, we know that there does not exist a co-stabilizing linear dynamic state feedback controller: where $i\in\{7,8\}$, $\alpha_{7}=1$ and $\alpha_{8}=-1$. Next, we prove the conclusion by the contrapositive. Assume that there exists a linear dynamic state feedback controller that co-stabilizes the systems.

Introduce the delay-input-state Then the following dynamics always satisfy The delayed systems in can therefore be written as Interconnecting with the controller yields the following closed-loop autonomous LTI systems on the state $\tilde{\mathbf{z}}_{t}:=[x_{t}\;\boldsymbol{\eta}_{t}^{\top}\;\mathbf{z}_{t}^{\top}]^{\top}$ where the closed-loop matrix is By assumption, $\mathbf{A}_{\mathrm{cl},+}$ and $\mathbf{A}_{\mathrm{cl},-}$ are both stable.

Next, we consider the costabilization of the systems. Let $\boldsymbol{\delta}_{t}\in\mathbb{R}^{n-1}$ denote the controller-side delay state: where $u^{K}_{t}:=\mathbf{H}\mathbf{z}_{t}+\mathbf{K}x_{t}$. Then implies the realization | | | $\displaystyle\mathbf{z}_{t+1}=\mathbf{F}\mathbf{z}_{t}+\mathbf{G}x_{t},$ | $\displaystyle u^{K}_{t}=\mathbf{H}\mathbf{z}_{t}+\mathbf{K}x_{t},$ | | \(40\) | | | | $\displaystyle\boldsymbol{\delta}_{t+1}=\mathbf{S}\boldsymbol{\delta}_{t}+\mathbf{e}u^{K}_{t},$ | $\displaystyle u_{t}=\mathbf{c}^{\top}\boldsymbol{\delta}_{t}.$ | | | This is again a linear dynamic state feedback controller.

Combining the controller in and the non-delayed plant, the resulting closed-loop dynamics on $\hat{\mathbf{z}}_{t}:=[x_{t}\;\boldsymbol{\delta}_{t}^{\top}\;\mathbf{z}_{t}^{\top}]^{\top}$ are Comparing with the closed-loop dynamics, we see that the closed-loop matrices are identical up to relabeling $\boldsymbol{\eta}_{t}\leftrightarrow\boldsymbol{\delta}_{t}$. Hence, for each choice of sign $\pm$, the closed-loop matrix in is stable.

Therefore, the co-stabilization of the systems in implies the co-stabilization of the systems . In other words, if there does not exist a co-stabilizing linear dynamic state feedback controller , there also does not exist a co-stabilizing linear dynamic state feedback controller .

In conclusion, there does not exist a co-stabilizing linear dynamic state feedback controller for $S_{3}$ and $S_{4}$ when the conditions in Theorem 4-Hard Systems ‣ III Linear Static State Feedback vs. Linear Dynamic State Feedback ‣ Benefits of Linear Dynamic State Feedback in Co-stabilization") hold. ∎
