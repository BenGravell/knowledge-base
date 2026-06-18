## INTRODUCTION

The field of learning control has recently seen explosive growth, which can be attributed to the availability of large amounts of data, creating an incentive for controllers that use the available information optimally. A significant amount of this research effort is being directed towards the familiar Linear Quadratic Regulation (LQR) problem where the transition matrices are unknown. Most of these developments however are related to deterministic systems.

Instead this paper takes a different approach, considering systems that intrinsically include the uncertainty in the dynamics through stochastic disturbances. More specifically we study systems with a time-varying multiplicative disturbance. These may cover a wide range of system classes like Linear Parameter Varying (LPV) systems and Linear Difference Inclusions (LDI) or in our case, when the disturbance varies stochastically, systems with multiplicative noise. Such systems have already been studied in the context of learning control by using policy iteration and intrinsically introduce robustness in the controller design.

The authors previously developed a control synthesis procedure using the *distributionally robust approach* that guarantees stability with high probability, when the true distribution of the system is not known. This paper is related to that result and provides a methodology to evaluate the performance of the *empirical approach*, where the sample mean and covariance are used to produce a controller making it similar to the *certainty equivanlent approach* for deterministic LQR. Therefore the proofs are similar to the result of Mania et. al., where the sample complexity of this certainty equivalent approach is studied.

The main result is then a suboptimality guarantee for the empirical controller. To produce such a result we make use of Riccati perturbation analysis. This paper is, to the authors' knowledge, the first instance of such a perturbation analysis being applied to discrete time systems with multiplicative noise. A Riccati perturbation bound for continuous time systems was already produced in.

The remainder of this paper is then structured as follows. Section 2 presents the problem statement and the assumptions used throughout the paper. The main result is then presented in Section 3 in the form of three theorems that show how the uncertainty on the covariance propagates throughout the controller synthesis. The proof of these three components are then given in the following sections. Section 4 lists some results that are required for the remainder of the derivations as well as a way of deriving confidence bounds for the sample covariance. Section 5 then extends upon the results of Konstantinov et. al. to study the perturbed Riccati equation. Section 6 uses a result from convex analysis to derive a bound for the perturbation of the controller. Then Section 7 proofs the main suboptimality bound, from which a sufficient condition for mean square stability (*m.s.s.*) of the true system under the empirical controller also follows. Finally Section 8 provides a conclusion and suggestions for further work.

### Notation

Let $IR$ denote the reals, $IN$ the naturals and ${IN_{+}} = {{IN} \smallsetminus {\{ 0\}}}$. We use ${\mathbb{S}}^{n}$ to denote the set of $n$-by-$n$ symmetric matrices. The set of positive (semi)definite matrices is then written as ${\mathbb{S}}_{+ +}^{n}$ $({\mathbb{S}}_{+}^{n}$). Then, for ${P,Q} \in {\mathbb{S}}^{n}$, we write $P \succ Q$ ($P \succeq Q$) to signify that ${P - Q} \in {\mathbb{S}}_{+ +}^{n}$ (${P - Q} \in {\mathbb{S}}_{+}^{n}$). We denote by $\otimes$ the Kronecker product, by $A^{\dagger}$ the pseudoinverse of some matrix $A$.. We assume that all random variables are defined on a probability space $(\Omega,\mathcal{F},{\mathbb{P}})$, with $\Omega$ the sample space, $\mathcal{F}$ its associated $\sigma$-algebra and $\mathbb{P}$ the probability measure. Let $y:{\Omega\rightarrow{IR^{n}}}$ be a random vector defined on $(\Omega,\mathcal{F},{\mathbb{P}})$. With some abuse of notation we will write $y \in {\mathbb{R}}^{n}$ to state the dimension of this random vector. Let ${\mathbb{P}}_{y}$ denote the distribution of $y$, *i.e.,* ${{\mathbb{P}}_{y}{(A)}} = {{\mathbb{P}}{\lbrack{y \in A}\rbrack}}$, then a trajectory ${\{ y_{i}\}}_{i = 1}^{N}$ of independent and identically distributed (*i.i.d.*) copies of $y$ is defined by the distribution it induces. That is, for any ${A_{0},\ldots,A_{N}} \in \mathcal{F}$ we define ${{\mathbb{P}}_{y}{({A_{0} \times \cdots \times A_{N}})}{{: =}{{\mathbb{P}}{\lbrack{y_{0} \in {A_{0} \land \cdots \land y_{N}} \in A_{N}}\rbrack}}}} = {\prod_{i = 0}^{N}{{\mathbb{P}}_{y}{(A_{i})}}}$. This definition can be extended to infinite trajectories ${\{ y_{i}\}}_{i \in {IN}}$ by Kolmogorov's existence theorem. We will write the expectation operator as $IE$. We denote by $IE\left\lbrack {y \mid z} \right\rbrack$ the conditional expectation with respect to $z$. For matrices we will use $\parallel \cdot \parallel$ to denote the spectral norm and ${\parallel \cdot \parallel}_{F}$ to denote the Frobenius norm. For a linear matrix operator $\mathcal{F}:{{IR^{n \times n}}\rightarrow{IR^{n \times n}}}$ we similarly use $\parallel\mathcal{F}\parallel$ to denote the operator-norm defined as ${\parallel\mathcal{F}\parallel}{{: =}{\max_{{\parallel X\parallel} \leq 1}{\parallel{\mathcal{F}{(X)}}\parallel}}}$.

## PROBLEM STATEMENT

In this section, we describe the problem statement and state the main result.

### LQR for systems with multiplicative noise

This paper considers linear systems with input- and state-multiplicative noise given by:

with ${A{(w)}{{: =}A_{0}}} + {\sum_{i = 1}^{n_{w}}{w^{(i)}A_{i}}}$ and ${B{(w)}{{: =}B_{0}}} + {\sum_{i = 1}^{n_{w}}{w^{(i)}B_{i}}}$, where at each time $k$, $x_{k} \in {IR^{n_{x}}}$ denotes the state, $u_{k} \in {IR^{n_{u}}}$ the input and $w_{k} \in {IR^{n_{w}}}$ an *i.i.d.* copy of a square integrable random vector $w$ distributed according to ${\mathbb{P}}_{w}$. We use $w^{(i)}$ to denote the $i$'th element of $w$. We introduce the following shorthands: $\mathbf{A}{{: =}\begin{bmatrix}
A_{0}^{\top} & A_{1}^{\top} & \ldots & A_{n_{w}}^{\top}
\end{bmatrix}^{\top}}$, $\mathbf{B}{{: =}\begin{bmatrix}
B_{0}^{\top} & B_{1}^{\top} & \ldots & B_{n_{w}}^{\top}
\end{bmatrix}^{\top}}$ and define $\Sigma_{0} = \begin{bmatrix}
\end{bmatrix}$, where we assume that ${IE{\lbrack w\rbrack}} = 0$ and ${IE{\lbrack{ww^{\top}}\rbrack}} = \Sigma$. The $\#$ operator, when applied to a matrix, then denotes the block transpose, *i.e.,* $\mathbf{A}^{\#}{{: =}\begin{bmatrix}
\end{bmatrix}^{\top}}$

The primary goal is to study solutions of the following stochastic LQR problem:

where we assume that $Q \succ 0$ and $R \succ 0$.^11^1This assumption is not strictly necessary, see for some discussion. The solution of will yield a controller that renders the closed-loop system exponentially mean square stable (*e.m.s.s.*) \[1, Definition 1\]. Note that for the dynamics in *m.s.s.* is equivalent to *e.m.s.s.* \[1, Theorem 2\]. Therefore we will say a system is *m.s.s.* throughout the paper, thereby also implying it is *e.m.s.s.*.

The solution of is then described by the following result \[1, Proposition 3\]:

### Proposition 2.1 (LQR control synthesis)

Consider a system with dynamics and the associated LQR problem. Assuming that is mean square stabilizable, *i.e.,* there exists a $K$, such that the closed-loop system $x_{k + 1} = {{({{A{(w_{k})}} + {B{(w_{k})}K}})}x_{k}}$ is *m.s.s.*, then the following statements holds.

The optimal solution of is given by $K^{\star} = {- {{({R + {\mathcal{G}{(P^{\star})}}})}^{- 1}\mathcal{H}{(P^{\star})}}}$, with $P^{\star}$ the solution of the following Riccati equation:

with the linear maps $\mathcal{F}{(P)}$, $\mathcal{G}{(P)}$, $\mathcal{H}{(P)}$ defined in Table 1.

The controller $K^{\star}$ renders *m.s.s.* in closed-loop.

The optimal cost is given by\
${J_{K^{\star}}{(x_{0})}} = {IE{\lbrack{\sum_{k = 0}^{\infty}{x_{k}^{\top}{({Q + {{}_{}^{}RK^{\star}}})}x_{k}}}\rbrack}} = {x_{0}^{\top}P^{\star}x_{0}}$.

The goal of this paper is then to consider the effect of misestimation of $\Sigma$ on the closed-loop cost. More specifically we will operate under the following assumption

### Assumption 2.2

Let ${\hat{\Sigma}}_{0} = {\Sigma_{0} + {\Delta\Sigma_{0}}}$ be some estimator of $\Sigma_{0}$, using $N$ samples of the random vector $w$. We will assume it satisfies the following:

where ${- 1} \leq {\underset{¯}{\mathbf{α}}}_{\mathbf{\Sigma}} \leq 0 \leq {\overline{\mathbf{α}}}_{\mathbf{\Sigma}} = {\mathcal{O}\left( {1/\sqrt{N}} \right)}$.

This assumption is valid with high probability when ${\hat{\Sigma}}_{0} = \begin{bmatrix}
\end{bmatrix}$ where $\hat{\Sigma} = {\sum_{i = 1}^{N}{w_{i}w_{i}^{\top}}}$ and under some additional assumptions on $w$, which are stated in Section 4. It is also applicable for the case where the mean is also unknown and estimated as the sample mean. The constants ${\underset{¯}{\mathbf{α}}}_{\mathbf{\Sigma}}$ and ${\overline{\mathbf{α}}}_{\mathbf{\Sigma}}$ depend on $N$, which is made explicit by using bold symbols.

## MAIN RESULT

Starting from this assumption we will study the optimal controller produced by applying Proposition 2.1. ‣ 2.1 LQR for systems with multiplicative noise ‣ 2 PROBLEM STATEMENT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty") for $\Sigma_{0}$ and ${\hat{\Sigma}}_{0}$ which we will denote as $K^{\ast}$ (*nominal controller*) and $\hat{K}$ (*empirical controller*) respectively. The goal is then to quantify the difference between $J_{K^{\star}}{(x_{0})}$ and $J_{\hat{K}}{(x_{0})}$. To do so we study how the perturbation on $\Sigma_{0}$ propagates through the controller synthesis in three stages. The first stage is how the solution of the Riccati equation is perturbed, which is quantified in Theorem 3.1. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty"). The second stage is the perturbation of the control gain, quantified in Theorem 3.2. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty"). The final stage is then the suboptimality, quantified in Theorem 3.3. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty").

We state these theorems for a system with dynamics, with ${IE{\lbrack w\rbrack}} = 0$ and ${IE{\lbrack{ww^{\top}}\rbrack}} = \Sigma$ and $K^{\star}$ the optimal controller and $P^{\star}$ the solution of (3. ‣ 2.1 LQR for systems with multiplicative noise ‣ 2 PROBLEM STATEMENT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty")). Then assume we have some ${\hat{\Sigma}}_{0} = {\Sigma_{0} + {\Delta\Sigma_{0}}}$ which satisfies Assumption 2.2 and denote by $\hat{K}$ the optimal controller for ${\hat{\Sigma}}_{0}$ and $\hat{P}$ the solution of (3. ‣ 2.1 LQR for systems with multiplicative noise ‣ 2 PROBLEM STATEMENT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty")). The constants used in the theorems below are listed in Table 1.

${\overline{\eta}}_{\mathcal{G}}$

Table 1: Overview of system constants

### Theorem 3.1 (Riccati Perturbation)

The distance between the solutions of the Riccati equations $P^{\ast}$ and $\hat{P}$ for covariances $\Sigma_{0}$ and ${\hat{\Sigma}}_{0}$ respectively is bounded as follows:

with ${\mathbf{α}}_{\mathbf{\Sigma}} = {\max{\{{|{\underset{¯}{\mathbf{α}}}_{\mathbf{\Sigma}}|},{|{\overline{\mathbf{α}}}_{\mathbf{\Sigma}}|}\}}}$. This bound holds as long as the following conditions are satisfied:

and ${\mathbf{α}}_{\mathbf{\Sigma}}$ sufficiently small such that the right side of (5. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty")) is smaller than $\mu_{P}^{\star} = {{\min\sigma}{(P^{\star})}}$.

### Proof

See Section 5 for the proof. ∎

### Theorem 3.2 (Controller Perturbation)

The distance between the optimal controllers for $\Sigma_{0}$ and ${\hat{\Sigma}}_{0}$ is bounded as follows:

with $\mathbf{\epsilon}_{\mathbf{P}}$ the right-hand side of (5. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty")), $\kappa_{K} = {{\kappa_{\mathcal{G}}{\parallel K^{\star}\parallel}} + \kappa_{\mathcal{H}}}$, $\eta_{K} = {{\eta_{\mathcal{G}}{\parallel K^{\star}\parallel}} + \eta_{\mathcal{H}}}$ and $\mu_{R} = {{\min\sigma}{(R)}}$.

### Proof

See Section 6 for the proof. ∎

### Theorem 3.3 (Suboptimality)

The difference between the optimal cost $J_{K^{\star}}{(x_{0})}$ and the closed-loop cost achieved when applying $\hat{K}$ to the true system, denoted by $J_{\hat{K}}{(x_{0})}$, is bounded as follows:

where $\overline{n} = {\min{(n_{x},n_{u})}}$ and $\mathbf{\epsilon}_{\mathbf{K}}$ the right-side of (7. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty")). The bound in (8. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty")) is valid as long as:

### Proof

See Section 7 for the proof. ∎

The rate of decrease predicted by these theorems is then given in the Corollary below.

### Corollary 3.4 (Suboptimality bound)

Let ${\hat{\Sigma}}_{0}$ satisfy Assumption 2.2 and let $K^{\star}$ denote the nominal controller and $\hat{K}$ the emprical controller. Then

assuming that $N$ is sufficiently large.

### Proof

The proof is quite straightforward. Note that ${\mathbf{α}}_{\mathbf{\Sigma}} = {\mathcal{O}{({1/\sqrt{N}})}}$ by Assumption 2.2. Let $\mathbf{\epsilon}_{\mathbf{P}}$ denote the right-hand side of (5. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty")). Evaluating the limit $\lim_{N\rightarrow\infty}{\sqrt{N}\mathbf{\epsilon}_{\mathbf{P}}}$ results in

where the final equality follows from the fact that ${\lim_{N\rightarrow\infty}{\sqrt{N}{\mathbf{α}}_{\mathbf{\Sigma}}}} = c > 0$ (since ${\mathbf{α}}_{\mathbf{\Sigma}} = {\mathcal{O}{({1/\sqrt{N}})}}$ by assumption), which implies that the limit of the numerator is $4\eta_{\mathcal{F}}\kappa_{\mathcal{R}_{0}}c$. The limit of the denominator meanwhile is $4\kappa_{\mathcal{R}_{0}}\kappa_{\mathcal{L}}^{\star}$, since ${\lim_{N\rightarrow\infty}{\mathbf{α}}_{\mathbf{\Sigma}}} = 0$. The overall limit being some positive constant then directly implies that $\mathbf{\epsilon}_{\mathbf{P}} = {\mathcal{O}{({1/\sqrt{N}})}}$.

Let $\mathbf{\epsilon}_{\mathbf{K}}$ be the right-hand side of (7. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty")) then we can see that $\mathbf{\epsilon}_{\mathbf{K}} = {\mathcal{O}{({1/\sqrt{N}})}}$, since it depends linearly on ${{\mathbf{α}}_{\mathbf{\Sigma}}\mathbf{\epsilon}_{\mathbf{P}}} = {\mathcal{O}{({1/N})}}$ and ${\mathbf{α}}_{\mathbf{\Sigma}}$. Finally (8. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty")) implies the required result since the factor in square brackets is $\mathcal{O}{}$ -- which can be seen by noting that the limit for $N\rightarrow\infty$ is one -- and since $\mathbf{\epsilon}_{\mathbf{K}}^{2} = {\mathcal{O}{({1/N})}}$. ∎

Note that the rate predicted by Corollary 3.4. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty") is the same as the one achieved by the certainty equivalent controller for deterministic LQR.

## PRELIMINARY RESULTS

In this section we provide some results that will be used throughout the remainder of this paper. First we slightly alter a previous result from high-dimensional statistics that results in a condition on ${\hat{\Sigma}}_{0}$ as in. Second we introduce three lemmas that are related to bounding the operator norms of versions of $\mathcal{F}$, $\mathcal{G}$ and $\mathcal{L}$.

### Concentration inequalities for the sample covariance

When using the sample-covariance $\hat{\Sigma} = {\sum_{i = 0}^{M}{w_{i}w_{i}^{\top}}}$, with $\left\{ w_{i} \right\}_{i = 0}^{M}$ *i.i.d.* copies of $w$, we can find a high confidence bound of the parameters ${\underset{¯}{\mathbf{α}}}_{\mathbf{\Sigma}}$ and ${\overline{\mathbf{α}}}_{\mathbf{\Sigma}}$ under the following assumptions:

### Assumption 4.1

We assume that 1 $w$is square integrable, 2 $w_{k}$and $w_{\ell}$ are independent for all $k \neq \ell$, 3 ${IE{\lbrack w\rbrack}} = 0$ 4 ${IE{\lbrack{ww^{\top}}\rbrack}} = \Sigma \succ 0$and 5 ${\Sigma^{- {1/2}}w} \sim {{subG}_{n_{w}}{(\sigma^{2})}}$for some $\sigma \geq 1$.

Here we follow the definition of a sub-Gaussian random vector (denoted by $subG$) given in \[1, Definition 5\]. Condition (iv) holds for example for gaussian $w$ ($\sigma = 1$) and for $w$ with bounded support (where $\sigma$ can be estimated from data ). Under these assumptions we can prove a slightly altered version of \[1, Theorem 8\], which is stated as:

### Theorem 4.2

Let $w \in {IR^{n_{w}}}$ be a random vector satisfying Assumption 4.1 and $\hat{\Sigma}$ the sample covariance as defined above. Then with probability at least $1 - \beta$,

with $\mathbf{t}_{\mathbf{\Sigma}}{{: =}{\frac{\sigma^{2}}{1 - {2\epsilon}}\left( {\sqrt{\frac{32q{(\beta,\epsilon,n_{w})}}{M}} + \frac{2q{(\beta,\epsilon,n_{w})}}{M}} \right)}}$, $\epsilon \in {(0,{1/2})}$ chosen freely and ${q{(\beta,\epsilon,n_{w})}{{: =}{n_{w}{\log{({1 + {1/\epsilon}})}}}}} + {\log{({2/\beta})}}$.

### Proof

The proof is a specialised version of that of \[1, Theorem 8\] and combines \[15, Lemma A.1.\] with the methodology of. The major difference is that no uncertainty on the mean is considered and the difference $\hat{\Sigma} - \Sigma$ is bounded instead of simply finding an upper bound for $\hat{\Sigma}$. ∎

Note ${- {{\mathbf{t}}_{\mathbf{\Sigma}}\Sigma_{0}}} \preceq {\Delta\Sigma_{0}} \preceq {{\mathbf{t}}_{\mathbf{\Sigma}}\Sigma_{0}}$ follows directly from.

### Norms of matrix operators

We will consider bounding norms associated with $\mathcal{F}$ and $\mathcal{G}$ in two circumstances. The first being where we have some $\Delta\Sigma_{0}$ that is constrained by. The second being the case where we have some ${\parallel{\DeltaP}\parallel} \leq \epsilon$. To deal with these two cases we will use the lemmas given below.

### Lemma 4.3

Consider the matrices $\mathbf{A} \in {IR^{{n_{x}n_{w}} \times p}}$, $P \in {\mathbb{S}}_{+}^{n_{x}}$, $\Sigma_{0} \in {\mathbb{S}}_{+}^{n_{w}}$ and ${\Delta\Sigma_{0}} \in {\mathbb{S}}^{n_{w}}$, where ${{\underset{¯}{\mathbf{α}}}_{\mathbf{\Sigma}}\Sigma_{0}} \preceq {\Delta\Sigma_{0}} \preceq {{\overline{\mathbf{α}}}_{\mathbf{\Sigma}}\Sigma_{0}}$. Let ${\mathbf{α}}_{\mathbf{\Sigma}} = {\max{\{{|{\underset{¯}{\mathbf{α}}}_{\mathbf{\Sigma}}|},{|{\overline{\mathbf{α}}}_{\mathbf{\Sigma}}|}\}}}$ We can then state the following bound:

### Proof

From ${{\underset{¯}{\mathbf{α}}}_{\mathbf{\Sigma}}\Sigma_{0}} \preceq {\Delta\Sigma_{0}} \preceq {{\overline{\mathbf{α}}}_{\mathbf{\Sigma}}\Sigma_{0}}$, due to the fact that the eigenvalues of a kronecker product of two matrices are the products of the eigenvalues of the matrices, we have that ${{{\underset{¯}{\mathbf{α}}}_{\mathbf{\Sigma}}\Sigma_{0}} \otimes P} \preceq {{\Delta\Sigma_{0}} \otimes P} \preceq {{{\overline{\mathbf{α}}}_{\mathbf{\Sigma}}\Sigma_{0}} \otimes P}$, implying ${{\underset{¯}{\mathbf{α}}}_{\mathbf{\Sigma}}\mathbf{A}^{\top}{({\Sigma_{0} \otimes P})}\mathbf{A}} \preceq {\mathbf{A}^{\top}{({{\Delta\Sigma_{0}} \otimes P})}\mathbf{A}} \preceq {{\overline{\mathbf{α}}}_{\mathbf{\Sigma}}\mathbf{A}^{\top}{({\Sigma_{0} \otimes P})}\mathbf{A}}$, which implies the required result. ∎

### Lemma 4.4

Consider the matrices $\mathbf{A} \in {IR^{{n_{x}n_{w}} \times p}}$, $P \in {\mathbb{S}}_{+}^{n_{x}}$ and $\Sigma \in {\mathbb{S}}_{+}^{n_{w}}$. Suppose ${\parallel P\parallel} \leq \epsilon$ then:

### Proof

Note that ${\parallel P\parallel} \leq \epsilon$ implies $P \preceq {\epsilonI}$. Therefore we can prove the required result using the same arguments as for the proof of Lemma 4.3. ∎

Using Lemma 4.4 we can see that $\kappa_{\mathcal{F}} = {\parallel{\mathbf{A}^{\top}{({\Sigma_{0} \otimes I})}\mathbf{A}}\parallel}$, since ${\parallel\mathcal{F}\parallel}{{: =}{\max_{{\parallel P\parallel} \leq 1}{\parallel{\mathbf{A}^{\top}{({\Sigma_{0} \otimes P})}\mathbf{A}}\parallel}}}$. Analogously we can find $\kappa_{\mathcal{G}}$, $\kappa_{\mathcal{G}}^{\#}$ and $\kappa_{\mathcal{F}}^{\star}$. The lemma is however not applicable to $\kappa_{\mathcal{H}}$, which is why we define it as $\kappa_{\mathcal{H}} = {{\parallel\mathbf{A}\parallel}{\parallel\mathbf{B}\parallel}}$. The same is true for $\kappa_{\mathcal{H}}^{\star}$ and $\kappa_{\mathcal{H}}^{\#}$. The applicability of Lemma 4.3 is less direct and will be used in Section 5 and Section 7. To evaluate $\kappa_{\mathcal{L}}^{\star}$ and $\kappa_{\mathcal{L}}^{\#}$ we use Lemma 4.5, which is similar to a result for deterministic dynamics:

### Lemma 4.5

Let $\mathcal{L}_{\star}{(P)}$ be an invertible Lyapunov operator as defined in Table 1. Then,

### Proof

First note that ${\parallel I\parallel} = 1$. Therefore ${\parallel\mathcal{L}_{\star}^{- 1}\parallel} \geq {\parallel{\mathcal{L}_{\star}^{- 1}{(I)}}\parallel}$. To prove ${\parallel\mathcal{L}_{\star}^{- 1}\parallel} \leq {\parallel{\mathcal{L}_{\star}^{- 1}{(I)}}\parallel}$ note that ${x_{0}^{\top}\mathcal{L}_{\star}^{- 1}{(Q)}x_{0}} = {IE{\lbrack{\sum_{k = 0}^{\infty}{x_{k}^{\top}Qx_{k}}}\rbrack}}$, with $x_{k + 1} = {A{(w_{k})}x_{k}}$. We can write this as ${\operatorname{Tr}{({\sum_{k = 0}^{\infty}{IE{\lbrack{x_{k}x_{k}^{\top}}\rbrack}Q}})}} = {\operatorname{Tr}{HQ}}$, where $H = {{}_{}^{}{(I)}} \succeq 0$ and apply \[18, Proposition 2.1\] to show that $I = {{{\arg\max}_{{\parallel Q\parallel} \leq 1}\operatorname{Tr}}{HQ}}$. Therefore ${\parallel\mathcal{L}_{\star}^{- 1}\parallel} \leq {\parallel{\mathcal{L}_{\star}^{- 1}{(I)}}\parallel}$. ∎

## RICCATI PERTURBATION

In this section we study the stochastic Riccati equation with perturbed parameters. The goal is to bound how much such perturbations affect the solutions, thereby proving Theorem 3.1. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty"). To do so we will use the methodology applied in, to the deterministic case. The main proof is stated at the end of the section, for which we state the main component first. This is a reformulation of the perturbed Riccati equation as a fixed-point equation.

More specifically let $P^{\star}$ be the solution of ${\mathcal{R}{(P^{\star},\Sigma_{0})}} = 0$ and $\Delta\Sigma_{0}$ selected such that ${\Sigma_{0} + {\Delta\Sigma_{0}}} \in {\mathbb{S}}_{+}^{n_{w}}$. Then a ${\DeltaP} \in {\mathbb{S}}^{n_{x}}$ is a solution of ${\mathcal{R}{({P^{\star} + {\DeltaP}},{\Sigma_{0} + {\Delta\Sigma_{0}}})}} = 0$ iff it is a solution to the following fixed-point equation:

with $\mathcal{L}_{\star}$ the Lyapunov operator for the optimal closed-loop system --- which is invertible since the closed-loop system is *m.s.s.* --- and where

Using the constants in Table 1, Lemma 5.1 then describes two essential properties of $\Phi$. The proof is deferred to Appendix.1.

### Lemma 5.1

Let $\Phi$ be defined as in and $\mathcal{D}{{: =}\left\{ {{\DeltaP} \in {\mathbb{S}}^{n_{x}}} \middle| {{{\parallel{\DeltaP}\parallel} \leq \mathbf{\epsilon}_{\mathbf{P}} \leq \mu_{P}^{\star}},{{{\DeltaP} + P^{\star}} \succeq 0}} \right\}}$. For every ${\DeltaP} \in \mathcal{D}_{P}$

the spectral norm of $\Phi{({\DeltaP})}$ is bounded as:

the matrix $\Phi{({\DeltaP})}$ is symmetric.

### Proof of Theorem 3.1. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty")

We can now complete proof of Theorem 3.1. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty"). To do so first note that ${h{(\mathbf{\epsilon}_{\mathbf{P}},{\mathbf{α}}_{\mathbf{\Sigma}})}} = \mathbf{\epsilon}_{\mathbf{P}}$ is a quadratic equation. It is easy to check that (6. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty")) is a necessary and sufficient condition for the existence of a positive solution, which is given by (5. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty")). By assumption we then also have that $\mathbf{\epsilon}_{\mathbf{P}} \leq {\mu_{P}^{\star}{{: =}{{\min\sigma}{(P^{\star})}}}}$.

Under these conditions we can verify three properties of the mapping $\Phi$: 1 it preserves symmetry, 2 ${\parallel{\DeltaP}\parallel} \leq \mathbf{\epsilon}_{\mathbf{P}}$implies ${\parallel{\Phi{({\DeltaP})}}\parallel} \leq \mathbf{\epsilon}_{\mathbf{P}}$, 3 ${P^{\star} + {\DeltaP}} \succeq 0$implies ${P^{\star} + {\Phi{({\DeltaP})}}} \succeq 0$. Property (i) directly follows from Lemma 5.1. From we also know that for every ${\DeltaP} \in \mathcal{D}_{P}$ we have ${\parallel{\Phi{({\DeltaP})}}\parallel} \leq {h{(\mathbf{\epsilon}_{\mathbf{P}},{\mathbf{α}}_{\mathbf{\Sigma}})}} = \mathbf{\epsilon}_{\mathbf{P}}$, which implies property (ii). Since ${\parallel{\Phi{({\DeltaP})}}\parallel} \leq \mathbf{\epsilon}_{\mathbf{P}} \leq \mu_{P}^{\star}$ property (iii) holds as well. Therefore ${\Phi{(\mathcal{D}_{P})}} \subseteq \mathcal{D}_{P}$ and we can apply the Brouwer Fixed-Point Theorem \[20, Corollary 17.56\], which proves ${\DeltaP} \in \mathcal{D}_{P}$ and therefore Theorem 3.1. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty"). ∎

## CONTROLLER PERTURBATION

In this section we derive a bound on $\parallel{K^{\star} - \hat{K}}\parallel$, thereby proving Theorem 3.2. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty"). We state the proof at the end of the section, but first introduce some of the components.

We will use a result from convex optimization, \[4, Lemma 1\], which we can apply since both the nominal as well as the empirical controllers are optima of the following cost functions:

Both functions are strongly convex with $\mu_{R} = {{\min\sigma}{(R)}}$. We will then need a bound for $\parallel{{{\nabla f^{\star}}{(u)}} - {{\nabla\hat{f}}{(u)}}}\parallel$:

### Lemma 6.1

Let $f^{\star}{(u)}$ and $\hat{f}{(u)}$ defined respectively as in and. Then the difference between their gradients is bounded as:

### Proof

The gradients are given by ${{\nabla f^{\star}}{(u)}} = {{{({{\mathbf{B}^{\top}{({\Sigma_{0} \otimes P^{\star}})}\mathbf{B}} + R})}u} + {\mathbf{B}^{\top}{({\Sigma_{0} \otimes P^{\star}})}\mathbf{A}x}}$ and ${{\nabla\hat{f}}{(u)}} = {{{({{\mathbf{B}^{\top}{({{\hat{\Sigma}}_{0} \otimes \hat{P}})}\mathbf{B}} + R})}u} + {\mathbf{B}^{\top}{({{\hat{\Sigma}}_{0} \otimes \hat{P}})}\mathbf{A}x}}$. The difference between the first terms of the gradients can be bounded by using Lemma 4.3 and Lemma 4.4. More specifically we have

We can remove the dependency on $\Delta\Sigma_{0}$ and $\DeltaP$ by applying Lemma 4.3 and Lemma 4.4 respectively, resulting in:

Since Lemma 4.4 and Lemma 4.3 are not applicable for the difference between the second term of the gradients we instead produce the following bound:

where we used for ${\parallel{\Delta\Sigma_{0}}\parallel} \leq {{\mathbf{α}}_{\mathbf{\Sigma}}{\parallel\Sigma_{0}\parallel}}$. Using the definitions of $\kappa_{\mathcal{G}}$, $\kappa_{\mathcal{H}}$, $\eta_{\mathcal{G}}$ and $\eta_{\mathcal{H}}$ we get. ∎

We are now ready to bound $\parallel{\hat{K} - K^{\star}}\parallel$.

### Proof of Theorem 3.2. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty")

Let $x$ be any vector with ${\parallel x\parallel} = 1$. Then we have

where we used ${\hat{K}x} = \hat{u}$ and ${K^{\star}x} = u^{\star}$ for the first inequality and we combined \[4, Lemma 1\] and Lemma 6.1 for the second inequality. Let $x^{\star} = {{\arg\max}_{{\parallel x\parallel} = 1}{\parallel{{({\hat{K} - K^{\star}})}x}\parallel}}$, for which ${\parallel{{({\hat{K} - K^{\star}})}x^{\star}}\parallel} = {\parallel{\hat{K} - K^{\star}}\parallel}$. Then also holds for $x^{\star}$. If we also use ${\parallel{K^{\star}x^{\star}}\parallel} \leq {{\parallel K^{\star}\parallel}{\parallel x^{\star}\parallel}} = {\parallel K^{\star}\parallel}$, then we have proven Theorem 3.2. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty"). ∎

## SUBOPTIMALITY

This section is dedicated to the proof of the main result of this paper. More specifically we derive a bound for the suboptimality of the empirical controller compared to the nominal one, given in (8. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty")) as a part of Theorem 3.3. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty"). The proof of which is stated at the end of this section.

We first introduce the main component, which is a perturbation bound on a matrix operator, similar to the one derived in Section 5. More specifically we will study the adjoint Lyapunov operator $\mathcal{L}^{\#}:{{{{IR^{n_{x} \times n_{x}}} \times I}R^{n_{u} \times n_{x}}}\rightarrow{IR^{n_{x} \times n_{x}}}}$ for the closed-loop system $x_{k + 1} = {{({{A{(w)}} + {B{(w)}\hat{K}}})}x_{k}}$ given by ${\mathcal{L}^{\#}{(X,K)}{{: =}X}} - {{({\mathbf{A} + {\mathbf{B}K}})}_{}^{}{({\Sigma_{0} \otimes X})}{({\mathbf{A} + {\mathbf{B}K}})}^{\#}}$. In the remainder of this section we will omit the second argument of $\mathcal{L}^{\#}$ and use a subscript $\star$, when $K^{\star}$ is implied (*i.e.,* ${\mathcal{L}^{\#}{(X,K^{\star})}} = {\mathcal{L}_{\star}^{\#}{(X)}}$). This corresponds with the definition in Table 1.

We can then state the following lemma

### Lemma 7.1

Let $X_{\infty}^{\star}$ and ${\hat{X}}_{\infty} = {{\hat{X}}_{\infty} + {\DeltaX_{\infty}}}$ denote the solution to ${\mathcal{L}_{\star}^{\#}{(X_{\infty}^{\star})}} = {x_{0}x_{0}^{\top}}$ and ${\mathcal{L}^{\#}{({\hat{X}}_{\infty},\hat{K})}} = {x_{0}x_{0}^{\top}}$ respectively. Then $\DeltaX_{\infty}$ is also the solution of the following fixed-point equation:

with ${\DeltaK} = {\hat{K} - K^{\star}}$. The following bounds then hold

with $\kappa_{\mathcal{H}}^{\star}$, $\kappa_{\mathcal{G}}^{\#}$ and $\kappa_{\mathcal{L}}^{\#}$ defined as in Table 1.

### Proof

We can use basic algebra and ${\mathcal{L}_{\star}^{\#}{(X_{\infty}^{\star})}} = {x_{0}x_{0}^{\top}}$ to rewrite the perturbed Lyapunov equation ${\mathcal{L}^{\#}{({X_{\infty}^{\star} + {\DeltaX_{\infty}}},{K^{\star} + {\DeltaK}})}} = {x_{0}x_{0}^{\top}}$ as in. The bounds are then derived by noting that ${\parallel{{({\mathbf{B}\DeltaK})}_{}^{}{({\Sigma_{0} \otimes X_{\infty}^{\star}})}{({\mathbf{B}\DeltaK})}^{\#}}\parallel} = {\parallel{{}_{}^{}{({{\Sigma_{0} \otimes \Delta}KX_{\infty}^{\star}\DeltaK^{\top}})}\mathbf{B}^{\#}}\parallel} \leq {\kappa_{\mathcal{G}}^{\#}{\parallel{\DeltaK}\parallel}^{2}{\parallel X_{\infty}^{\star}\parallel}}$. We also know ${\parallel{{({\mathbf{B}\DeltaK})}_{}^{}{({\Sigma_{0} \otimes X_{\infty}^{\star}})}{}_{}^{}}\parallel} \leq {{\parallel\mathbf{A}_{\star}^{\#}\parallel}{\parallel\mathbf{B}^{\#}\parallel}{\parallel\Sigma_{0}\parallel}{\parallel{\DeltaK}\parallel}{\parallel X_{\infty}^{\star}\parallel}} = {\kappa_{\mathcal{H}}^{\#}{\parallel{\DeltaK}\parallel}{\parallel X_{\infty}^{\star}\parallel}}$. Using the same tricks for the final term in and the definition of $\kappa_{\mathcal{L}}^{\#}$ allows us to prove. The same tricks also produce where we use ${{A \otimes B} + {A \otimes C}} = {A \otimes {({B + C})}}$. ∎

Similarly to how Lemma 5.1 was used to bound the Riccati perturbation, we can bound $\parallel{\DeltaX_{\infty}}\parallel$.

### Lemma 7.2

Suppose ${{}_{}^{}{({{2\kappa_{\mathcal{H}}{\parallel{\DeltaK}\parallel}} + {\kappa_{\mathcal{G}}^{\#}{\parallel{\DeltaK}\parallel}^{2}}})}} < 1$ then we can bound $\parallel{\DeltaX_{\infty}}\parallel$ as

and $\hat{K}$ renders the true system *m.s.s.*.

### Proof

It is easy to verify that the solution to $\mathbf{\epsilon}_{\mathbf{X}} = {g{(\mathbf{\epsilon}_{\mathbf{X}})}}$ is given by the right-hand side of, with $g$ as defined in Lemma 7.1. Let $\mathcal{D}_{X} = \left\{ {{\DeltaX_{\infty}} \in {\mathbb{S}}^{n_{x}}}\mid{{{\parallel{\DeltaX_{\infty}}\parallel} \leq \mathbf{\epsilon}_{\mathbf{X}}},{{X_{\infty}^{\star} + {\DeltaX_{\infty}}} \succeq 0}} \right\}$. Then, due to ${{}_{}^{}{({{2\kappa_{\mathcal{H}}{\parallel{\DeltaK}\parallel}} + {\kappa_{\mathcal{G}}^{\#}{\parallel{\DeltaK}\parallel}^{2}}})}} < 1$ and Lemma 7.1, the operator $\Phi_{\mathcal{L}}$ is a contraction on $\mathcal{D}_{X}$. Invoking the Banach Fixed-Point Theorem \[20, Theorem 3.48\] then guarantees that $\mathcal{D}_{X}$ contains a fixed-point of $\Phi_{\mathcal{L}}$. Therefore $\hat{K}$ stabilizes the true system since ${\parallel{X_{\infty}^{\star} + {\DeltaX_{\infty}}}\parallel} \leq {{\parallel X_{\infty}^{\star}\parallel} + \mathbf{\epsilon}_{\mathbf{X}}}$ is finite, implying *m.s.s.* and we have ${\parallel{\DeltaX_{\infty}}\parallel} \leq \mathbf{\epsilon}_{\mathbf{X}}$. ∎

We are now ready to prove the suboptimality bound

### Proof of Theorem 3.3. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty")

We start by using \[9, Lemma 3.5\], which states:

where $\hat{K} = {K^{\star} + {\DeltaK}}$. Let ${\overline{\eta}}_{\mathcal{G}} = {\parallel{{\mathcal{G}{(P^{\star})}} + R}\parallel}$ and $\overline{n} = {\min{\{ n_{x},n_{u}\}}}$. Then consider two matrices ${A,B} \in {\mathbb{S}}_{x}^{n}$ and let $\sigma_{i}$ denote the $i$'th smallest eigenvalue of a matrix. Then we can show ${\operatorname{Tr}{\lbrack{AB}\rbrack}} \leq {\sum_{i = 1}^{n}{\sigma_{i}{(A)}\sigma_{i}{(B)}}} \leq {{\operatorname{Tr}{\lbrack A\rbrack}}{\parallel B\parallel}}$, where we used *von Neumann's trace theorem* \[21, Theorem 7.4.1.1\] for the first inequality and the definition of the spectral norm and ${\operatorname{Tr}{\lbrack A\rbrack}} = {\sum_{i = 1}^{n}{\sigma_{i}{(A)}}}$ for the second. By repeatedly applying this property, we can show ${\operatorname{Tr}\left\lbrack {\DeltaK^{\top}{({R + {\mathcal{G}{(P^{\star})}}})}\DeltaK{\hat{X}}_{\infty}} \right\rbrack} \leq {{{\operatorname{Tr}\left\lbrack {\DeltaK^{\top}\DeltaK} \right\rbrack}{\overline{\eta}}_{\mathcal{G}}}{\parallel{\hat{X}}_{\infty}\parallel}}$. Since ${\operatorname{Tr}\left\lbrack {\DeltaK^{\top}\DeltaK} \right\rbrack} = {\parallel{\DeltaK}\parallel}_{F}^{2} \leq {\overline{n}{\parallel{\DeltaK}\parallel}^{2}}$, we have:

The value of $\mathbf{\epsilon}_{\mathbf{K}}$ is given as the right-hand side of (7. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty")) in Theorem 3.3. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty"), leaving only the derivation of a bound for ${\hat{X}}_{\infty}$. Note that, by definition of $\kappa_{\mathcal{L}}^{\#}$ and since $X_{\infty}^{\star} = {{}_{}^{}{({x_{0}x_{0}^{\top}})}}$, we have ${\parallel X_{\infty}^{\star}\parallel} \leq {{}_{}^{}{\parallel x_{0}\parallel}^{2}}$. Hence using Lemma 7.2 --- which is applicable due to (9. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty")) in Theorem 3.3. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty") --- we can prove

Substituting this into results in (8. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty")). ∎

## CONCLUSIONS AND FUTURE WORKS

This paper studied the sample complexity of LQR applied to systems with multiplicative noise. Overall we provided three types of sample complexities in Theorem 3.1. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty")-3.3. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty").

The first is given in Theorem 3.1. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty"), which produces a bound on the amount of samples required to make the resulting problem stabilizable and the Riccati perturbation finite.

The second sample-complexity is the one related to stability, given in Theorem 3.3. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty"). It gives a bound on the amount of samples required before the produced controller stabilizes the true system.

The final sample-complexity is then related to performance. It is given in Corollary 3.4. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty") and states that the suboptimality decreases with $1/N$. This is the same rate as was derived for determinstic certainty equivalent LQR in.

In future work, we aim to extend the results to partially observed systems and to the distributionally robust approach, where the stability complexity is absent, since it is satisfied automatically.
