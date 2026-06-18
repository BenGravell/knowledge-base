## Introduction

Data-driven stabilization aims at designing a feedback law directly based on data collected from an *unknown system*, bypassing a system identification process (see \[4, Ch. 1.2\] for a historical background). Under suitable conditions on the data, such feedback laws can be obtained, and if implemented *exactly* as designed, they stabilize the unknown system. Nevertheless, data collected in an open-loop scenario do not contain information about perturbations arising from the feedback loop. As a result, a data-driven feedback that is unaware of such perturbations might be *fragile*. In this work, we study data-driven stabilization in the presence of perturbations on the controller parameters and the extent to which the stability of the unknown system is immune to such perturbations.

From design to real-world implementation, a feedback gain might undergo various perturbations due to, e.g., truncation errors in the numerical computations, limited word-length implementation, conversions from analog to digital and vice versa, and instrumental precision. Some feedback perturbations caused , e.g., faults in the sensors and actuators, can also be modeled by perturbations on the feedback gain. In addition, it is appealing for a designed feedback to provide room for future adjustments caused by a change in the design objectives. Hence, it is important to design a feedback that is not extremely sensitive to variations in the control parameters, and to that end, it is useful to know the tolerance towards feedback perturbations.

The problem of fragile controllers was raised in the paper by Keel and Bhattacharyya (see also and the references therein). They showed that a feedback gain obtained through $H_{\infty}$, $H_{2}$, $l_{1}$, or $\mu$ formulations can be fragile, which means that the stability of the closed-loop system is highly sensitive to variations in the control parameters. Since then, several design methods have been proposed to prevent fragile controllers, including the following works: Control fragility caused by fixed word-length implementations is studied , for which a loop-shaping method is introduced as a solution. Nonfragile controllers with linear-quadratic performance indices are studied , where it is observed that for some structured perturbations the problem can be tackled by convex optimization. The use of fixed-structure controllers to avoid fragility is considered . Nonfragile design through minimization of pole sensitivity is proposed in and the ellipsoidal sets of nonfragile feedback gains are studied . While most of the literature on nonfragile control is devoted to additive perturbations on the feedback gain, multiplicative perturbations are also studied, e.g, . Moreover, nonfragile filter design has also been a topic of research in the literature.

For unknown linear time-invariant (LTI) systems, a stabilizing state-feedback gain can be directly obtained from a collection of noisy input-state data. Given that the noise belongs to a known deterministic model, the data give rise to the set of *data-consistent systems*, which includes all systems that could have generated the available data for some noise sequence agreeing with the noise model. In this setting, since any data-consistent system can potentially be the unknown true system, one may seek a feedback gain to stabilize all data-consistent systems. This problem has already been studied within the framework of *data informativity*, for which solutions are presented , e.g.,. To the authors' knowledge, however, the fragility issues of such data-driven feedback design methods have not been addressed in the literature.

In this work, we answer the following question: *Given a state-feedback gain that stabilizes all data-consistent systems, to what extent such a guarantee is intact when the gain is perturbed?* We study the effect of additive perturbations on data-driven feedback gains. To that end, we parameterize all quadratically stabilizing feedback gains, for which we leverage the recently developed tools on quadratic matrix inequalities (QMIs) . We call a data-driven feedback gain extremely fragile if a variation in the feedback gain, no matter how small in magnitude, destabilizes a subset of the data-consistent systems. Two extreme cases where the data-driven feedback gain is extremely fragile or is completely immune to perturbations are isolated by necessary and sufficient conditions. Next, we study the general case where the data-driven feedback is neither fragile nor immune, for which we characterize the set of perturbations that leave the stability guarantee intact. For this, we introduce a measure that quantifies the fragility of a feedback gain. We show that one can compute this measure and find the least fragile feedback gain by solving a semi-definite program (SDP). For the sake of completeness and better understanding of the introduced concepts, we first study the underlying problems in the model-based setting, and then extend our study to the data-driven framework.

This note is organized as follows: Section 2 provides a recap of the data-driven stabilization theory. In Section 3, we present a parametrization for the set of data-driven stabilizing feedback gains. In Section 4, we study the fragility of feedback gains within model-based and data-driven settings. Finally, Section 5 concludes the paper.

### Notation

The set of $n \times n$ real symmetric matrices is denoted by ${\mathbb{S}}^{n}$. We say matrix $M$ is positive definite (resp., positive semi-definite), and we denote it by $M > 0$ (resp., $M \geq 0$), if $M \in {\mathbb{S}}^{n}$ and all its eigenvalues are positive (resp., nonnegative). We say matrix $M$ is negative definite (resp., negative semi-definite), and we denote it by $M < 0$ (resp., $M \leq 0$), if ${- M} > 0$ (resp., ${- M} \geq 0$). We denote the spectral norm of $M \in {\mathbb{C}}^{p \times q}$ by $\| M\|$. Given $C \in {\mathbb{R}}^{p \times q}$ and $\rho \geq 0$, let ${\mathcal{B}{(C,\rho)}} ≔ {\{ X:{{\|{X - C}\|} \leq \rho}\}}$ denote the ball centered around $C$ with radius $\rho$. For a matrix $M \in {\mathbb{R}}^{p \times q}$, its Moore--Penrose pseudoinverse is denoted by $M^{\dagger}$ and its kernel is denoted by ${\ker M} ≔ {\{{x \in {\mathbb{R}}^{q}}:{{Mx} = 0}\}}$. A square matrix is called *Schur* if all its eigenvalues lie inside the open unit disc in the complex plane. We define the set

where $\left. \Pi \middle| \Pi_{22} \right. ≔ {\Pi_{11} - {\Pi_{12}\Pi_{22}^{\dagger}\Pi_{21}}}$ is the generalized Schur complement of $\Pi$ with respect to $\Pi_{22}$. We also define the QMI-induced sets $\mathcal{Z}_{r}{(\Pi)}$ and $\mathcal{Z}_{r}^{+}{(\Pi)}$ as follows:

## Recap of Data-driven Stabilization

In this section, we briefly review data-driven stabilization results within the *data informativity* framework based on the existing literature.

Consider an LTI system of the form

where ${x{(t)}} \in {\mathbb{R}}^{n}$ is the state, ${u{(t)}} \in {\mathbb{R}}^{m}$ is the input, and ${w{(t)}} \in {\mathbb{R}}^{n}$ is the process noise. We assume that $A_{\text{true}}$ and $B_{\text{true}}$ are unknown, but we can access input-state data

collected from system. These data are influenced by the unknown process noise

We assume that the noise signal satisfies an energy bound of the form

where $\Phi \in \mathbf{\Pi}_{n,T}$ with $\Phi_{22} < 0$ is given.

Several noise models can be captured by this energy bound (see \[18, p. 4\] for a detailed account), among which the noise-free case corresponds to $\Phi_{11} = 0$, $\Phi_{12} = \Phi_{21}^{\top} = 0$, and $\Phi_{22} = {- I}$.

We define the data matrices

A pair of real matrices $(A,B)$ is called a *data-consistent system* if it satisfies

for some $W_{-}$ satisfying. We define the set of all data-consistent systems as

Clearly, ${(A_{\text{true}},B_{\text{true}})} \in \Sigma_{\mathcal{D}}$. One can verify that (see \[2, Lem. 4\])

${N_{11},N_{22}} \in {\mathbb{S}}^{n}$, and $N_{33} \in {\mathbb{S}}^{m}$. The following proposition summarizes some facts about $\Sigma_{\mathcal{D}}$.

### Proposition 1 (\[19, Prop. 14\])

Let $\Phi \in \mathbf{\Pi}_{n,T}$ with $\Phi_{22} < 0$. Then, the following statements hold:

$\Sigma_{\mathcal{D}}$ is bounded *if and only if* ${{rank}\begin{bmatrix}

Assume that $\Sigma_{\mathcal{D}}$ is bounded. Then, $\Sigma_{\mathcal{D}}$ is a singleton *if and only if*

In this case, $\Sigma_{\mathcal{D}} = {\{{(A_{\text{true}},B_{\text{true}})}\}}$ and

We consider the following notions of data informativity.

### Definition 2

The data $\mathcal{D}$ are called

*informative for stabilization* if there exists $K \in {\mathbb{R}}^{m \times n}$ such that $A + {BK}$ is Schur for all ${(A,B)} \in \Sigma_{\mathcal{D}}$.

*informative for quadratic stabilization* if there exist $K \in {\mathbb{R}}^{m \times n}$ and $P > 0$ such that

for all ${(A,B)} \in \Sigma_{\mathcal{D}}$.

Under suitable conditions, the two notions of data informativity in Definition 2 ‣ 2 Recap of Data-driven Stabilization ‣ Fragility Analysis of Data-Driven Feedback Gains") are equivalent. One such condition corresponds to the noise-free case.

### Proposition 3 (\[20, Thm. 1\])

Suppose that $\Phi_{11} = 0$, $\Phi_{22} = {- I}$, and $\Phi_{12} = \Phi_{21}^{\top} = 0$. Then, the data $\mathcal{D}$ are informative for stabilization *if and only if* they are so for quadratic stabilization.

The following proposition provides a necessary and sufficient LMI condition for the informativity of data $\mathcal{D}$ for quadratic stabilization.

### Proposition 4 (\[18, Thm. 5.1(b)\])

Suppose that $\begin{bmatrix}
\end{bmatrix}$ has full column rank. Then, the data $\mathcal{D}$ are informative for quadratic stabilization *if and only if* there exist $P > 0$, $\alpha \geq 0$, and $L$ such that

Moreover, $K = {LP^{- 1}}$ is a stabilizing feedback gain for all ${(A,B)} \in \Sigma_{\mathcal{D}}$ provided that (14]) ‣ 2 Recap of Data-driven Stabilization ‣ Fragility Analysis of Data-Driven Feedback Gains")) is feasible.

The LMI (14]) ‣ 2 Recap of Data-driven Stabilization ‣ Fragility Analysis of Data-Driven Feedback Gains")) contains $\frac{n{({n + 1})}}{2} + {mn} + 1$ unknowns. The computational complexity of this LMI can be reduced. To this end, we define

We partition matrix $M$ into four blocks, where the first block is denoted by $M_{11} \in {\mathbb{R}}^{m \times m}$, the second and third blocks are denoted by $M_{12} = M_{21}^{\top} \in {\mathbb{R}}^{m \times n}$, and the last block is denoted by $M_{22} \in {\mathbb{R}}^{n \times n}$. Now, the following proposition provides alternative LMI conditions to those in Proposition 4]) ‣ 2 Recap of Data-driven Stabilization ‣ Fragility Analysis of Data-Driven Feedback Gains"), reducing the number of unknowns to $\frac{n{({n + 1})}}{2} + 1$.

### Proposition 5 (\[18, Thm. 5.3(b)\])

Suppose that $\begin{bmatrix}
\end{bmatrix}$ has full column rank. Then, the data $\mathcal{D}$ are informative for quadratic stabilization *if and only if* there exist $P > 0$ and $\alpha \geq 0$ such that

Moreover, $K = {- {M_{12}M_{22}^{- 1}}}$ is a stabilizing feedback gain for all ${(A,B)} \in \Sigma_{\mathcal{D}}$ provided that (16]) ‣ 2 Recap of Data-driven Stabilization ‣ Fragility Analysis of Data-Driven Feedback Gains")) is feasible.

Propositions 4]) ‣ 2 Recap of Data-driven Stabilization ‣ Fragility Analysis of Data-Driven Feedback Gains") and 5]) ‣ 2 Recap of Data-driven Stabilization ‣ Fragility Analysis of Data-Driven Feedback Gains") can be used to obtain a stabilizing feedback gain for the unknown true system based on the collected data. However, the extent of the freedom over the choice of the feedback gain is not provided by these results. Such a description, which is instrumental in the fragility analysis of data-driven feedback gains, can be studied by the parameterization provided in the next section.

## Parametrization of Data-driven Feedback Gains

In this section, we will parameterize the set of quadratically stabilizing feedback gains that can be obtained from the collected input-state data. To that end, suppose that $\begin{bmatrix}
\end{bmatrix}$ has full column rank. For $P > 0$ and $\alpha \geq 0$, we define

The set of all quadratically stabilizing feedback gains that can be obtained from data $\mathcal{D}$ is the union of the sets $\mathcal{K}{(P,\alpha)}$ over all $P > 0$ and $\alpha \geq 0$, which is denoted by

The following theorem provides a parameterization for such sets.

### Theorem 6

Suppose that $\begin{bmatrix}
\end{bmatrix}$ has full column rank and data $\mathcal{D}$ are informative for quadratic stabilization. Let $P > 0$ and $\alpha \geq 0$ satisfy (16]) ‣ 2 Recap of Data-driven Stabilization ‣ Fragility Analysis of Data-Driven Feedback Gains")). Then, $K \in {\mathcal{K}{(P,\alpha)}}$ *if and only if* $K^{\top} \in {\mathcal{Z}_{n}^{+}{(M)}}$. Moreover, we have

### Proof 3.7

First, we prove that $K \in {\mathcal{K}{(P,\alpha)}}$ if and only if $K^{\top} \in {\mathcal{Z}_{n}^{+}{(M)}}$. For the "only if" part, let $K \in {\mathcal{K}{(P,\alpha)}}$. This implies that the LMI (14]) ‣ 2 Recap of Data-driven Stabilization ‣ Fragility Analysis of Data-Driven Feedback Gains")) is feasible with $L = {KP}$. Take the Schur complement of the matrix in (14]) ‣ 2 Recap of Data-driven Stabilization ‣ Fragility Analysis of Data-Driven Feedback Gains")) with respect to its lower block to have

Now, since we have $\Theta > 0$, take the Schur complement of with respect to the first ${{2n} \times 2}n$ block to have

Using $L = {KP}$ we observe that can be written as

Therefore, $K^{\top} \in {\mathcal{Z}_{n}^{+}{(M)}}$. To prove the "if" part, let $K^{\top} \in {\mathcal{Z}_{n}^{+}{(M)}}$, i.e., holds. Take $L = {KP}$. Observe that implies. Using a Schur complement argument, one can see that holds, and thus the LMI (14]) ‣ 2 Recap of Data-driven Stabilization ‣ Fragility Analysis of Data-Driven Feedback Gains")) is satisfied. Therefore, $LP^{- 1}$, and thus $K$, belongs to $\mathcal{K}{(P,\alpha)}$.

Next, we use \[18, Thm. 3.3\] to parameterize the set $\mathcal{Z}_{n}^{+}{(M)}$. Since $P > 0$ and $M_{22} \leq {- P}$, we have ${\ker M_{22}} = {\{ 0\}}$. This readily implies that ${\ker M_{22}} \subseteq {\ker M_{12}}$. In addition, by hypothesis, the inequality is feasible, which implies that ${\mathcal{Z}_{n}{(M)}} \neq \varnothing$. Thus, it follows from \[18, pp. 6,7\] that $\left. M \middle| M_{22} \right. \geq 0$. Therefore, we have $M \in \mathbf{\Pi}_{m,n}$. Now, in view of \[18, Thm. 3.3\], every $K = {LP^{- 1}}$ satisfies

for some $S$ with ${S^{\top}S} < I$.

## Fragility Analysis

In this section, we study the effect of *additive* perturbations on the stabilizing feedback gains (see Fig. 1) within both model-based and data-driven settings.

Figure 1: Additive feedback perturbations.

### Model-based analysis

For a stabilizable $(A,B)$, let $K$ be such that

is Schur. We define the radius of stabilizing gains centered around $K$ as

The value of $\mu_{(A,B)}^{\text{a}}{(K)}$ gives the largest bound for an additive feedback perturbation so that the closed-loop system remains stable. The following theorem characterizes the case where $\mu_{(A,B)}^{\text{a}}{(K)}$ is finite.

### Theorem 4.8

Suppose that $(A,B)$ is stabilizable. Let $K$ be such that $A_{K}$ is Schur. Then, ${\mu_{(A,B)}^{\text{a}}{(K)}} > 0$. Moreover, $\mu_{(A,B)}^{\text{a}}{(K)}$ is finite *if and only if* $B \neq 0$.

### Proof 4.9

Since $A_{K}$ is Schur, there exist $P > 0$ and $\beta > 0$ such that the Lyapunov inequality ${P - {A_{K}PA_{K}^{\top}}} \geq {\betaI}$ holds. Thus, there exists a sufficiently small $\rho > 0$ such that ${P - {{({A_{K} + {B\Delta}})}P{({A_{K} + {B\Delta}})}^{\top}}} > 0$ holds for all $\Delta \in {\mathcal{B}{(0,\rho)}}$. This implies that ${\mu_{(A,B)}^{\text{a}}{(K)}} > 0$. For the rest, first, suppose that $B = 0$. In this case, $\mu_{(A,B)}^{\text{a}}{(K)}$ is obviously not finite. Next, suppose that $B \neq 0$. Let $\rho > 0$ be such that $A_{K} + {B\Delta}$ is Schur for all $\Delta \in {\mathcal{B}{(0,\rho)}}$. Take $\Delta = {{({\rho/{\| B\|}})}B^{\top}}$. Since $A_{K} + {B\Delta}$ is Schur, we have ${|{{tr}{({A_{K} + {B\Delta}})}}|} < n$, thus, $\left| {{{tr}{(A_{K})}} + {{\rho{{tr}{({BB^{\top}})}}}/{\| B\|}}} \right| < n$. This shows that $\rho < {{{({n - {{tr}{(A_{K})}}})}{\| B\|}}/{{tr}{({BB^{\top}})}}}$, which proves that $\mu_{(A,B)}^{\text{a}}{(K)}$ is finite.

For SISO systems, the value of $\mu_{(A,B)}^{\text{a}}{(K)}$ may be obtained using discrete-time counterparts of the Kharitonov's theorem. However, for MIMO systems, computing $\mu_{(A,B)}^{\text{a}}{(K)}$ for given $(A,B)$ and $K$ is a hard problem in general (see, e.g., ). Therefore, we aim at developing numerically tractable algorithms to approximate $\mu_{(A,B)}^{\text{a}}{(K)}$ by computing a positive lower bound for it. To that end, given $K$ and $P > 0$ such that the Lyapunov inequality ${P - {A_{K}PA_{K}^{\top}}} > 0$ holds, we define

We also define the largest value of $\kappa_{(A,B)}^{\text{a}}{(P,K)}$ over $P > 0$ as

It is evident that ${\kappa_{(A,B)}^{\text{a}}{(P,K)}} \leq {\lambda_{(A,B)}^{\text{a}}{(K)}} \leq {\mu_{(A,B)}^{\text{a}}{(K)}}$. Now, we define the largest value of $\lambda_{(A,B)}^{\text{a}}{(K)}$ over $K$ as

For a given $(A,B)$, the value of $\lambda_{(A,B)}^{\text{a}}$ can be computed by solving an SDP provided by the following theorem.

### Theorem 4.10

Suppose that $(A,B)$ is stabilizable and $B \neq 0$. Then, $\lambda_{(A,B)}^{\text{a}} = \sqrt{1/\beta_{\ast}}$ where $\beta_{\ast}$ is the optimal value of the following SDP:

$\min\limits_{Q,L}\beta$ (29a)
Q & {{QA^{\top}} + {L^{\top}B^{\top}}} & Q \\
\end{bmatrix} \geq 0}.$

Moreover, provided that $L_{\ast}$ and $Q_{\ast}$ are optimizers of the SDP, $A + {B{({K_{\ast} + \Delta})}}$ with $K_{\ast} = {L_{\ast}Q_{\ast}^{\dagger}}$ is Schur for all ${\|\Delta\|} < \lambda_{(A,B)}^{\text{a}}$.

To prove this theorem, we need an auxiliary result presented in the following lemma.

### Lemma 4.11

Suppose that $(A,B)$ is stabilizable. Let $K$ and $P > 0$ be such that ${P - {A_{K}PA_{K}^{\top}}} > 0$. Then, we have $\rho < {\kappa_{(A,B)}^{\text{a}}{(P,K)}}$ *if and only if* there exists $\gamma \geq 0$ such that the following LMI is satisfied:

### Proof 4.12

Observe that $\Delta$ satisfies ${P - {{({A_{K} + {B\Delta}})}^{\top}P{({A_{K} + {B\Delta}})}}} > 0$ for some $P > 0$ if and only if $\Delta \in {\mathcal{Z}_{m}^{+}{(M_{L})}}$. We also observe that ${\mathcal{B}{(0,\rho)}} = {\mathcal{Z}_{m}{(M_{\rho})}}$. One can verify that $M_{\rho} \in \mathbf{\Pi}_{n,m}$ and the second diagonal block of $M_{\rho}$ is negative definite. Therefore, it follows from the matrix S-lemma \[18, Thm. 4.10\] that ${\mathcal{Z}_{m}{(M_{\rho})}} \subseteq {\mathcal{Z}_{m}^{+}{(M_{L})}}$ if and only if ${M_{L} - {\gammaM_{\rho}}} > 0$ for some $\gamma \geq 0$. This is equivalent to.

The proof of Theorem 4.10 now follows from Lemma 4.11.

Proof of Theorem 4.10: We first show that LMI (29b) is feasible. For this, let $\nu > 0$, $K$ and $P > 0$ be such that

Take $Q = {\frac{\|{BB^{\top}}\|}{\nu}P}$ and $L = {KQ}$. Observe that

This implies that

Thus, there exists a sufficiently large $\overline{\beta} \geq 0$ such that (29b) is feasible for all $\beta \geq \overline{\beta}$. Now, we show that the SDP is attained. It follows from that any feasible solution satisfies $\beta \geq 0$. Let $\beta_{\ast}$ be the infimum value of $\beta$ such that (29b) holds for some $Q$ and $L$. We have $\beta_{\ast} \leq \overline{\beta}$. Let $(\beta_{i},Q_{i},L_{i})$ be a sequence satisfying such that ${\lim_{i\rightarrow\infty}\beta_{i}} = \beta_{\ast}$. Note that this sequence satisfies $Q_{i} \leq {\beta_{i}I}$. Hence, we have ${\lim_{i\rightarrow\infty}Q_{i}} \leq {\beta_{\ast}I}$. One can also verify that there exists $\eta > 0$ such that ${\lim_{i\rightarrow\infty}{\|{BL_{i}}\|}} \leq \eta$. Therefore, $\beta_{i}$, $Q_{i}$, and $BL_{i}$ are all bounded sequences. Let ${\overline{L}}_{i} = {B^{\top}{({BB^{\top}})}^{\dagger}BL_{i}}$. Since $BL_{i}$ is a bounded sequence, ${\overline{L}}_{i}$ is a bounded sequence with the property that ${BL_{i}} = {B{\overline{L}}_{i}}$. Thus, $(\beta_{i},Q_{i},{\overline{L}}_{i})$ is a bounded sequence that satisfies ${\lim_{i\rightarrow\infty}\beta_{i}} = \beta_{\ast}$. Now, it follows from the Bolzano-Weierstrass theorem that the optimal value is attained on a convergent subsequence.

Next, we prove that $\lambda_{(A,B)}^{\text{a}} = \sqrt{1/\beta_{\ast}}$. For this, we denote

To prove this claim, observe from Lemma 4.11 and that $\lambda_{(A,B)}^{\text{a}}$ is equal to the supremum value of $\rho$ such that holds for some $P$, $K$ and $\gamma \geq 0$. Note that $\gamma = 0$ is not a feasible solution. We introduce the new variable $\overline{P} = {P/\gamma}$. We also note that $\rho$ can always be taken to be positive, thus, we suppose that $\rho > 0$. Using a Schur complement argument for the matrix , we have

We multiply from left and right by a block diagonal matrix with the diagonal blocks ${\overline{P}}^{- 1}$ and $I$ to have

By a change of variables $Q = {\overline{P}}^{- 1}$, $L = {KQ}$, and $\beta = {1/\rho^{2}}$, we have

We take the Schur complement of the matrix in with respect to its second diagonal block to see that holds. Now, we use to show that $\lambda_{(A,B)}^{\text{a}} = \sqrt{1/\beta_{\ast}}$. To this end, let $Q_{\ast}$ and $L_{\ast}$ be the optimal solution of with the optimal value $\beta_{\ast}$. We claim that for any $\beta > \beta_{\ast}$, there exist $\hat{Q}$ and $\hat{L}$ such that ${\mathcal{L}{(\hat{Q},\hat{L},\beta)}} > 0$. To show this, note that since $(A,B)$ is stabilizable, there exist $\overline{Q}$, $\overline{L}$ and $r$ such that

Let $\beta > \beta_{\ast}$ and $\epsilon = {r/{({\beta - \beta_{\ast}})}}$. We take $\hat{Q} = {Q_{\ast} + {\overline{Q}/\epsilon}}$ and $\hat{L} = {L_{\ast} + {\overline{L}/\epsilon}}$. It follows from ${\mathcal{L}{(Q_{\ast},L_{\ast},\beta_{\ast})}} \geq 0$ that

This proves the claim, and, in turn, it shows that $\lambda_{(A,B)}^{\text{a}} = \sqrt{1/\beta_{\ast}}$.

What remains to be proven is that $A + {B{({K_{\ast} + \Delta})}}$ with $K_{\ast} = {L_{\ast}Q_{\ast}^{\dagger}}$ is Schur for all ${\|\Delta\|} < \lambda_{(A,B)}^{\text{a}}$. To show this, let $\Delta \in {\mathbb{R}}^{m \times n}$ satisfy ${\|\Delta\|} < \sqrt{1/\beta_{\ast}}$. We observe from the first $n$ columns of the matrix in that ${\ker Q_{\ast}} \subseteq {\ker{BL_{\ast}}}$. By the definition of the Moore-Penrose pseudoinverse, we have $Q_{\ast} = {Q_{\ast}Q_{\ast}^{\dagger}Q_{\ast}}$. This implies that ${{im}{({I - {Q_{\ast}^{\dagger}Q_{\ast}}})}} \subseteq {\ker Q_{\ast}} \subseteq {\ker{BL_{\ast}}}$, and thus, ${BL_{\ast}Q_{\ast}^{\dagger}Q_{\ast}} = {BL_{\ast}}$. Hence, we have ${BL_{\ast}} = {BK_{\ast}Q_{\ast}}$. By substituting ${BL_{\ast}} = {BK_{\ast}Q_{\ast}}$ into (29b), we have

By taking the Schur complement of this with respect to its first diagonal block, we have

We multiply from left and right, respectively, by $\begin{bmatrix}
\end{bmatrix}$ and $\begin{bmatrix}
\end{bmatrix}^{\top}$ to have

Since ${\|\Delta\|} < \sqrt{1/\beta_{\ast}}$, we have ${I - {\beta_{\ast}\Delta\Delta^{\top}}} > 0$. Let $\sigma > 0$ be such that ${I - {\beta_{\ast}\Delta\Delta^{\top}}} \geq {\sigmaI}$. Therefore, we have

Let $v \in {\mathbb{C}}^{n}$ and $\eta \in {\mathbb{C}}$ be such that ${{({A + {BK_{\ast}} + {B\Delta}})}^{\top}v} = {\etav}$. We multiply from left and right, respectively, by $v^{\ast}$ and $v$ to have

In case ${B^{\top}v} = 0$, we have ${{({A + {BK_{\ast}} + {B\Delta}})}^{\top}v} = {A^{\top}v} = {\etav}$. Since $(A,B)$ is stabilizable, it follows from the Hautus test that ${|\eta|} < 1$. In case ${B^{\top}v} \neq 0$, it follows from that ${|\eta|} < 1$. Therefore, $A + {BK_{\ast}} + {B\Delta}$ is Schur, which completes the proof. \\QED

Theorem 4.10 can be used to compute the optimal feedback gain $K_{\ast}$ that provides the least amount of fragility in the sense of the measure. Nevertheless, if the feedback gain $K$ is given, one can also compute $\lambda_{(A,B)}^{\text{a}}{(K)}$ by solving an SDP discussed in the following remark.

### Remark 4.13

Suppose that $(A,B)$ is stabilizable and $B \neq 0$. Let $K$ be such that $A_{K}$ is Schur. Then, ${\lambda_{(A,B)}^{\text{a}}{(K)}} = \sqrt{1/\beta_{\ast}}$ where $\beta_{\ast}$ is the optimal value of the following SDP:

The following example illustrates the results of Theorems 4.10 and Remark 4.13.

### Example 4.14

Consider $A = \begin{bmatrix}
\end{bmatrix}$ and $B = \begin{bmatrix}
\end{bmatrix}$. The set of all stabilizing feedback gains is shown by the triangle area in Fig. 2. In particular, for $K = {- \begin{bmatrix}
\end{bmatrix}}$ we have ${\mu_{(A,B)}^{\text{a}}{(K)}} = 0.447$, and Remark 4.13 yields ${\lambda_{(A,B)}^{\text{a}}{(K)}} = 0.333$. According to Theorem 4.10, we have $\lambda_{(A,B)}^{\text{a}} = 0.667$ that is attained by $K_{\ast} = {- \begin{bmatrix}
\end{bmatrix}}$. Fig. 3 provides a contour plot illustrating the level sets of stabilizing feedback gains with constant $\lambda_{(A,B)}^{\text{a}}{(K)}$.

Figure 2: A visualization of the values of μ(A,B)a (K) and λ(A,B)a (K) for a certain K, and the value of λ(A,B)a with the optimal K* for Example 4.14.

Figure 3: Contours of constant λ(A,B)a (K) over all stabilizing feedback gains for Example 4.14.

### Data-driven analysis

In this section, we turn our attention to the data-driven setting. Assume that the data $\mathcal{D}$ are informative for stabilization. Let $K$ be such that $A + {BK}$ is Schur for all ${(A,B)} \in \Sigma_{\mathcal{D}}$. Analogous to, we define

The value of $\mu_{\mathcal{D}}^{\text{a}}{(K)}$ gives the largest bound for an additive feedback perturbation so that the closed-loop remains stable for all systems within $\Sigma_{\mathcal{D}}$. The two extreme cases where $\mu_{\mathcal{D}}^{\text{a}}{(K)}$ is zero or not finite are fully characterized by the following theorem.

### Theorem 4.15

Suppose that the data $\mathcal{D}$ are informative for stabilization. Let $K$ be such that $A + {BK}$ is Schur for all ${(A,B)} \in \Sigma_{\mathcal{D}}$. Then, the following statements hold:

${\mu_{\mathcal{D}}^{\text{a}}{(K)}} = 0$ *if and only if* ${{rank}\begin{bmatrix}

$\mu_{\mathcal{D}}^{\text{a}}{(K)}$ is not finite *if and only if* $\Sigma_{\mathcal{D}} = {\{{(A_{\text{true}},B_{\text{true}})}\}}$ such that $B_{\text{true}} = 0$.

### Proof 4.16

\(a\) To prove the "if" part, suppose that ${{rank}\begin{bmatrix}
\end{bmatrix}} < {n + m}$. Let nonzero $(A_{0},B_{0})$ be such that ${{A_{0}X_{-}} + {B_{0}U_{-}}} = 0$. Also, let $\rho = {\mu_{\mathcal{D}}^{\text{a}}{(K)}}$. By the definition, every $\overset{\sim}{K} \in {\mathcal{B}{(K,\rho)}}$ has the property that $A + {B\overset{\sim}{K}}$ is Schur for all ${(A,B)} \in \Sigma_{\mathcal{D}}$. Based on \[1, Lem. 15\], every such $\overset{\sim}{K}$ satisfies ${A_{0} + {B_{0}\overset{\sim}{K}}} = 0$. Thus, we have ${A_{0} + {B_{0}K}} = 0$. Since the data are informative for stabilization, we have ${{rank}X_{-}} = n$ (see \[1, Thm. 16\]). This implies that $B_{0} \neq 0$. Take $\Delta = {{({\rho/{\| B_{0}\|}})}B_{0}^{\top}}$ and observe that ${A_{0} + {B_{0}K} + {B_{0}\Delta}} = 0$ implies that ${\rhoB_{0}B_{0}^{\top}} = 0$. Since $B_{0} \neq 0$, we have $\rho = 0$. We prove the "only if" part by contraposition. Suppose that $\begin{bmatrix}
\end{bmatrix}$ has full column rank. This implies that $\Sigma_{\mathcal{D}}$ is bounded. In this case, there exist $K$ and $\beta > 0$ such that for every ${(A,B)} \in \Sigma_{\mathcal{D}}$ the Lyapunov inequality ${P - {{({A + {BK}})}P{({A + {BK}})}^{\top}}} \geq {\betaI}$ holds for some $P > 0$. Since $\beta > 0$, there exists a small enough $\rho > 0$ such that for every ${(A,B)} \in \Sigma_{\mathcal{D}}$, the Lyapunov inequality ${P - {{({A + {B\overset{\sim}{K}}})}P{({A + {B\overset{\sim}{K}}})}^{\top}}} > 0$ holds for all $\overset{\sim}{K} \in {\mathcal{B}{(K,\rho)}}$. This implies that ${\mu_{\mathcal{D}}^{\text{a}}{(K)}} > 0$.

\(b\) The "if" part is obvious. For the "only if" part, suppose that $\mu_{\mathcal{D}}^{\text{a}}{(K)}$ is not finite. In view of part (a), this implies that ${{rank}\begin{bmatrix}
\end{bmatrix}} = {n + m}$. Let ${(A,B)} \in \Sigma_{\mathcal{D}}$. Since $\mu_{\mathcal{D}}^{\text{a}}{(K)}$ is not finite, we have that $\mu_{(A,B)}^{\text{a}}{(K)}$ is also not finite. Due to Theorem 4.8, this implies that $B = 0$. This shows that every ${(A,B)} \in \Sigma_{\mathcal{D}}$ satisfies $B = B_{\text{true}} = 0$. What remains to be proven is that $\Sigma_{\mathcal{D}}$ is a singleton. To this end, define

According to the parametrization provided in \[18, Thm. 3.3\], one can verify that we have

Let $R_{A} \in {\mathbb{R}}^{{({n + m})} \times n}$ and $R_{B} \in {\mathbb{R}}^{{({n + m})} \times m}$ be such that $\begin{bmatrix}
\end{bmatrix} = R$. Note that $R > 0$, thus, $R_{B} \neq 0$. Now, since every data-consistent system $(A,B)$ satisfies $B = 0$, we have ${LSR_{B}} = 0$ for all ${SS^{\top}} \leq I$. This, together with $R_{B} \neq 0$, implies that $L = 0$. Therefore, the set $\Sigma_{\mathcal{D}}$ is a singleton due to.

### Remark 4.17

In case ${\mu_{\mathcal{D}}^{\text{a}}{(K)}} = 0$, a small additive perturbation on the feedback gain, no matter how small, destabilizes a nonempty subset of $\Sigma_{\mathcal{D}}$. Therefore, a small additive perturbation may also destabilize the true system. We refer to this case as *extreme fragility*. Theorem 4.15 shows that if $\begin{bmatrix}
\end{bmatrix}$ does not have full column rank, then any data-driven stabilizing feedback gain is extremely fragile. This condition is equivalent to the case where the set of data-consistent systems is unbounded. Therefore, in the noise-free case, the data-driven feedback gain is extremely fragile *if and only if* the system cannot be uniquely identified, see \[1, Prop. 6\].

Now, we aim at developing numerically tractable methods to approximate $\mu_{\mathcal{D}}^{\text{a}}{(K)}$. Suppose that the data $\mathcal{D}$ are informative for quadratic stabilization. Let $K$, $P > 0$, and $\alpha \geq 0$ be such that $K \in {\mathcal{K}{(P,\alpha)}}$. We define

One can also define the largest value of $\kappa_{\mathcal{D}}^{\text{a}}{(P,\alpha,K)}$ over all $P > 0$ and $\alpha \geq 0$ as

Now, we define the largest value $\lambda_{\mathcal{D}}^{\text{a}}{(K)}$ over all $K \in \mathcal{K}$ as

The value of $\lambda_{\mathcal{D}}^{\text{a}}$ can be obtained by solving an SDP as stated next.

### Theorem 4.18

Suppose that ${{rank}\begin{bmatrix}
\end{bmatrix}} = {n + m}$, the data $\mathcal{D}$ are informative for quadratic stabilization, and (11 ‣ Proposition 1 ([19, Prop. 14]) ‣ 2 Recap of Data-driven Stabilization ‣ Fragility Analysis of Data-Driven Feedback Gains")) does not hold. Then, $\lambda_{\mathcal{D}}^{\text{a}} = \sqrt{\beta_{\ast}}$ where $\beta_{\ast}$ is the optimal value of the following SDP:

$\max\limits_{Q,L,\zeta}\beta$ (55a)
\end{bmatrix} - {\zeta\begin{bmatrix}
\end{bmatrix}}} \geq 0}.$

Moreover, provided $L_{\ast}$ and $Q_{\ast}$ are optimizers of, $A + {B{({K_{\ast} + \Delta})}}$ with $K_{\ast} = {L_{\ast}Q_{\ast}^{\dagger}}$ is Schur for all ${\|\Delta\|} < \lambda_{\mathcal{D}}^{\text{a}}$ and all ${(A,B)} \in \Sigma_{\mathcal{D}}$.

To prove this theorem, we need an auxiliary result presented in the following Lemma.

### Lemma 4.19

Suppose that ${{rank}\begin{bmatrix}
\end{bmatrix}} = {n + m}$, the data $\mathcal{D}$ are informative for quadratic stabilization. Let $P > 0$, $K$ and $\alpha \geq 0$ be such that $K \in {\mathcal{K}{(P,\alpha)}}$. Then, we have $\rho < {\kappa_{\mathcal{D}}^{\text{a}}{(P,\alpha,K)}}$ *if and only if* there exists $\gamma > 0$ such that the following LMI is satisfied:

### Proof 4.20

We define ${\overline{M}}_{\rho} ≔ \begin{bmatrix}
\end{bmatrix}$ and

We observe from Theorem 6 that ${K + \Delta} \in {\mathcal{K}{(P,\alpha)}}$ if and only if ${K^{\top} + \Delta^{\top}} \in {\mathcal{Z}_{n}^{+}{(M)}}$, i.e.,

Based on this inequality, one can verify that ${K^{\top} + \Delta^{\top}} \in {\mathcal{Z}_{n}^{+}{(M)}}$ is equivalent to $\Delta^{\top} \in {\mathcal{Z}_{n}^{+}{(M_{K})}}$. Observe that ${\mathcal{B}{(0,\rho)}} = {\mathcal{Z}_{n}{({\overline{M}}_{\rho})}}$. Also, observe that ${\overline{M}}_{\rho} \in \mathbf{\Pi}_{m,n}$ and the second diagonal block of ${\overline{M}}_{\rho}$ is negative definite. Therefore, it follows from the matrix S-lemma \[18, Thm. 4.10\] that ${\mathcal{Z}_{n}{({\overline{M}}_{\rho})}} \subseteq {\mathcal{Z}_{n}^{+}{(M_{K})}}$ if and only if ${M_{K} - {\gamma{\overline{M}}_{\rho}}} > 0$ for some $\gamma \geq 0$. Since $M_{K}$ is not positive definite, we see that $\gamma \neq 0$. Using a Schur complement argument, one can verify that ${M_{K} - {\gamma{\overline{M}}_{\rho}}} > 0$ is equivalent to.

Now, we use this lemma to prove Theorem 4.18.

Proof of Theorem 4.18: We first show that the LMI (55b) is feasible. For this, it follows from Theorem 6 that there exist $\overline{P} > 0$, $\overline{L}$, $\overline{\alpha} \geq 0$ and $\nu > 0$ such that

Thus, we observe that there exists a sufficiently large $\overline{\gamma} > 0$ such that (55b) holds with $Q = {\overline{P}/\overline{\gamma}}$, $L = {\overline{L}/\overline{\gamma}}$ and $\beta = {\nu/\overline{\gamma}}$. Now, we show that the SDP is attained. We observe from the last ${{2n} \times 2}n$ diagonal block of the matrix in (55b) that every feasible $Q$ satisfies $0 \leq Q \leq I$. This, in turn, implies that there exists a $\delta > 0$ such that every feasible $L$ satisfies ${\| L\|} \leq \delta$. Since (11 ‣ Proposition 1 ([19, Prop. 14]) ‣ 2 Recap of Data-driven Stabilization ‣ Fragility Analysis of Data-Driven Feedback Gains")) does not hold, $N$ has at least one positive eigenvalue. This implies that there exists a $\overline{\zeta} \geq 0$ such that every feasible $\zeta$ satisfies $0 \leq \zeta \leq \overline{\zeta}$. Now, it is evident from the third diagonal block that there exists a $\overline{\beta} \geq 0$ such that every feasible $\beta$ satisfies $\beta \leq \overline{\beta}$. Hence, the set of all feasible solutions is bounded. Therefore, the SDP is attained.

Next, we prove that $\lambda_{\mathcal{D}}^{\text{a}} = \sqrt{\beta_{\ast}}$. For this, define

To prove this claim, we observe from Lemma 4.19 that $\lambda_{\mathcal{D}}^{\text{d}}$ is equal to the supremum value of $\rho$ such that holds for some $P$, $K$, $\alpha \geq 0$, and $\gamma > 0$. Take $Q = {P/\gamma}$, $L = {KQ}$, and $\zeta = {\alpha/\gamma}$, one can verify that ${\mathcal{L}_{\mathcal{D}}{(Q,L,\zeta,\beta)}} > 0$ is equivalent to. Thus, the claim holds. This claim can be used to show that $\lambda_{\mathcal{D}}^{\text{a}} = \sqrt{\beta_{\ast}}$. To this end, we prove that there exist $\hat{Q}$, $\hat{L}$, and $\hat{\zeta}$ such that ${\mathcal{L}_{\mathcal{D}}{(\hat{Q},\hat{L},\hat{\zeta},\beta)}} > 0$ for any $\beta < \beta_{\ast}$. Since the data $\mathcal{D}$ are informative for quadratic stabilization, it follows from Lemma 4.19 that there exist $\overline{Q}$, $\overline{L}$, and $\overline{\zeta}$ such that ${\mathcal{L}_{\mathcal{D}}{(\overline{Q},\overline{L},\overline{\zeta},0)}} > 0$. Let $Q_{\ast}$, $L_{\ast}$ and $\zeta_{\ast}$ be optimal solutions for the SDP, i.e., ${\mathcal{L}_{\mathcal{D}}{(Q_{\ast},L_{\ast},\zeta_{\ast},\beta_{\ast})}} \geq 0$. Let $\epsilon = {\beta/\beta_{\ast}}$. We take $\hat{Q} = {{\epsilonQ_{\ast}} + {{({1 - \epsilon})}\overline{Q}}}$, $\hat{L} = {{\epsilonL_{\ast}} + {{({1 - \epsilon})}\overline{L}}}$ and $\hat{\zeta} = {{\epsilon\zeta_{\ast}} + {{({1 - \epsilon})}\overline{\zeta}}}$. We observe that

It follows from ${\mathcal{L}_{\mathcal{D}}{(Q_{\ast},L_{\ast},\zeta_{\ast},\beta_{\ast})}} \geq 0$ that ${\mathcal{L}_{\mathcal{D}}{(\hat{Q},\hat{L},\hat{\zeta},\beta)}} > 0$. This implies that $\beta^{\ast}$ is equal to the supremum value of $\beta$ such that ${\mathcal{L}_{\mathcal{D}}{(Q,L,\zeta,\beta)}} > 0$, i.e., $\lambda_{\mathcal{D}}^{\text{a}} = \sqrt{\beta_{\ast}}$.

What remains to be proven is that $A + {BK_{\ast}} + {B\Delta}$ is Schur with $K_{\ast} = {L_{\ast}Q_{\ast}^{\dagger}}$ for all ${\|\Delta\|} < \lambda_{\mathcal{D}}^{\text{a}}$ and all ${(A,B)} \in \Sigma_{\mathcal{D}}$. To show this, let $\Delta \in {\mathbb{R}}^{m \times n}$ satisfy ${\|\Delta\|} < \sqrt{\beta_{\ast}}$ and ${(A,B)} \in \Sigma_{\mathcal{D}}$. Observe from ${\mathcal{L}_{\mathcal{D}}{(Q_{\ast},L_{\ast},\zeta_{\ast},\beta_{\ast})}} \geq 0$ that we have ${\ker Q_{\ast}} \subseteq {\ker L_{\ast}}$. We also have ${Q_{\ast}Q_{\ast}^{\dagger}Q_{\ast}} = Q_{\ast}$, which implies that ${{im}{({I = {Q_{\ast}^{\dagger}Q_{\ast}}})}} \subseteq {\ker Q_{\ast}} \subseteq {\ker L_{\ast}}$. Hence, we have ${L_{\ast}Q_{\ast}^{\dagger}Q_{\ast}} = L_{\ast}$. This implies that $L_{\ast} = {KQ_{\ast}}$. Therefore,

Take the Schur complement of this with respect to the last $n \times n$ diagonal block to have

It follows from that ${\begin{bmatrix}
\end{bmatrix}N\begin{bmatrix}
\end{bmatrix}^{\top}} \geq 0$. Using this, we multiply from left and right, respectively, by $\begin{bmatrix}
\end{bmatrix}$ and its transpose to have

Since the data are informative for quadratic stabilization, the pair $(A,B)$ is stabilizable. Now, using the same argument as in the proof of Theorem 4.10, one can verify that since ${\|\Delta\|} < \sqrt{\beta_{\ast}}$, we have that $A + {BK_{\ast}} + {B\Delta}$ is Schur. This completes the proof. \\QED

Theorem 4.18 is the data-driven counterpart of Theorem 4.10, which provides the least fragile data-driven feedback gain in the sense of measure. To analyze the fragility of a given feedback gain in the data-driven setting, one can solve the SDP provided by the following remark.

### Remark 4.21

Suppose that ${{rank}\begin{bmatrix}
\end{bmatrix}} = {n + m}$, the data $\mathcal{D}$ are informative for quadratic stabilization, and (11 ‣ Proposition 1 ([19, Prop. 14]) ‣ 2 Recap of Data-driven Stabilization ‣ Fragility Analysis of Data-Driven Feedback Gains")) does not hold. Let $K \in {\mathcal{K}{(P,\alpha)}}$ for some $P > 0$ and $\alpha \geq 0$. Then, ${\lambda_{\mathcal{D}}^{\text{a}}{(K)}} = \sqrt{\beta_{\ast}}$ where $\beta_{\ast}$ is the optimal value of the following SDP:

The following example illustrates the results of Theorems 4.18 and Remark 4.21.

### Example 4.22

Consider the true system with

Assume that the noise sequence satisfies ${\| W_{-}\|} \leq 1$, which can be modeled by $\Phi_{11} = I$, $\Phi_{12} = \Phi_{21}^{\top} = 0$, and $\Phi_{22} = {- I}$. Consider the collected input-state data and the noise signal as follows:

The LMIs in (16]) ‣ 2 Recap of Data-driven Stabilization ‣ Fragility Analysis of Data-Driven Feedback Gains")) are feasible^11^1For the numerical examples of this paper, the LMIs and SDPs are solved using the YALMIP toolbox of MATLAB with the MOSEK solver., hence, the data are informative for quadratic stabilization. The set $\mathcal{K}$ is shown in Fig. 4. In particular, for $K = {- \begin{bmatrix}
\end{bmatrix}}$, according to Remark 4.21 we have ${\lambda_{\mathcal{D}}^{\text{a}}{(K)}} = 0.055$. Theorem 4.18 yields $\lambda_{\mathcal{D}}^{\text{a}} = 0.087$, which is attained by $K_{\ast} = {- \begin{bmatrix}
\end{bmatrix}}$. Fig. 5 provides a contour plot illustrating the level sets of stabilizing feedback gains with constant values of $\lambda_{\mathcal{D}}^{\text{a}}{(K)}$.

Figure 4: A visualization of the value of λ𝒟a (K) for a certain K, and the value of λ𝒟a with the optimal K* for Example 4.22.

Figure 5: Contours of constant λ𝒟a (K) for Example 4.22.

The following example discusses a more realistic case study compared to that of Example 4.22.

### Example 4.23

Consider the state-space model of a fighter aircraft \[25, Ex. 10.1.2\] as a benchmark example^22^2The Matlab files for this example, including the data set, are available at We discretize the continuous-time model with a sample time of $0.01$ to have

We collect $T = 500$ input and state data samples from this system. The data are generated starting from

with the input drawn at random from a zero-mean Gaussian distribution with unit variance. During this process, the entries of the noise samples are also drawn at random but from a uniform distribution between $- {0.005/6}$ and $0.005/6$. This noise model can be captured by with $\Phi_{11} = {0.005^{2}TI_{n}}$, $\Phi_{12} = \Phi_{21}^{\top} = 0$, and $\Phi_{22} = {- I_{T}}$.

We first design a feedback gain, $K_{o}$, using the method provided . This can be done using Proposition 4]) ‣ 2 Recap of Data-driven Stabilization ‣ Fragility Analysis of Data-Driven Feedback Gains"), which yields

For this feedback gain, using Remark 4.21 we have ${\lambda_{\mathcal{D}}^{\text{a}}{(K_{o})}} = 0.026$. Now, we use Theorem 4.18 to compute the least fragile feedback gain in the sense of measure as

which corresponds to $\lambda_{\mathcal{D}}^{\text{a}} = {\lambda_{\mathcal{D}}^{\text{a}}{(K_{\ast})}} = 0.441$. Comparing the values of $\lambda_{\mathcal{D}}^{\text{a}}{(K_{o})}$ and $\lambda_{\mathcal{D}}^{\text{a}}$, we see that although $K_{o}$ and $K_{\ast}$ are both quadratically stabilizing gains for the true system, $K_{o}$ is more sensitive to additive perturbations. For instance, consider a perturbation as

which satisfies ${\lambda_{\mathcal{D}}^{\text{a}}{(K_{o})}} < {\|\Delta\|} = 0.353 < \lambda_{\mathcal{D}}^{\text{a}}$. One can verify that $A_{\text{true}} + {B_{\text{true}}{({K_{\ast} + \Delta})}}$ is Schur. However, $A_{\text{true}} + {B_{\text{true}}{({K_{o} + \Delta})}}$ is not Schur as it has an eigenvalue equal to $1.016$.

## Conclusions

It has been shown that the fragility of a data-driven feedback gain can be quantified by means of a measure, and the least fragile data-driven feedback gain can be computed by solving a data-based SDP. In addition, it has been shown that extreme fragility and complete immunity of a data-driven feedback gain towards feedback perturbations can be fully characterized by conditions that only depend on input-state data and the noise model. In this work, we only focused on *additive* perturbation on the control parameters. Another type of feedback perturbation that is relevant in practical applications of data-driven controllers is the *multiplicative* one, which can capture the effect of various faults and failures. The study of this and other types of feedback perturbations is left as future work.
