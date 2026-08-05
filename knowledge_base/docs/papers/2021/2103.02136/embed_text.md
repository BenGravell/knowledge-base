<!-- arxiv-full-text:v1 {"arxiv_id": "2103.02136", "source": "ar5iv"} -->

## Introduction

The standard approach to stochastic optimal control is to evaluate a random cumulative cost in expectation. However, this approach is not designed to protect against worst-case circumstances. This limitation motivates robust optimal control and related methods, such as minimax model predictive control and mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control.

Robust methods typically assume bounded disturbances, which excludes certain common noise models, such as Gaussian noise. A technique to alleviate this restriction is to use a *risk-averse* formulation, in which a random cost is assessed via *exponential utility*. Here, the objective takes the form ${\mathcal{J}_{\gamma}{(x,\pi)}}:={\frac{1}{\gamma}{\log\left( {E_{x}^{\pi}{(e^{{\gammaZ}/2})}} \right)}}$, where $Z \geq 0$ is a random cumulative cost, $\pi$ is a control policy, $x$ is an initial condition, and $\gamma > 0$ is a risk-aversion parameter.^11^1One may consider $\gamma < 0$, which corresponds to a *risk-seeking* perspective. We focus on the *risk-averse* perspective here, which assumes that noise leads to harm rather than benefit. This problem has been studied in increasing levels of generality from the 1970s to the 2010s, e.g., see. As $\gamma$ increases, the criterion $\mathcal{J}_{\gamma}{(x,\pi)}$ represents a more risk-averse perspective, while as $\gamma$ approaches zero, $\mathcal{J}_{\gamma}{(x,\pi)}$ tends to the usual expected cost.

In the case of linear dynamics with Gaussian noise and quadratic costs, the problem of optimizing $\mathcal{J}_{\gamma}{(x,\pi)}$ is commonly called LEQR control. For a fixed $\gamma > 0$, a Riccati recursion is used to derive the optimal value functions and the optimal control law, which is linear state-feedback. At each step $t$ of the recursion, it must be the case that the matrix $\Sigma^{- 1} - {\gamma{\overline{P}}_{t + 1}}$ is positive definite, where $\Sigma$ is the covariance of the process noise, and ${\overline{P}}_{t + 1}$ is the matrix obtained from step $t + 1$. If $\gamma$ is chosen too large, then the above condition may be violated, and the controller synthesis procedure breaks down. While it is known that $\mathcal{J}_{\gamma}{(x,\pi)}$ approximates a weighted sum of the expectation $E_{x}^{\pi}{(Z)}$ and the variance $\text{var}_{x}^{\pi}{(Z)}$ if $\gamma\text{var}_{x}^{\pi}{(Z)}$ is "small", a more precise interpretation of $\mathcal{J}_{\gamma}{(x,\pi)}$ has not been established.

The *Conditional Value-at-Risk* (CVaR) functional, which was invented in the early 2000s by the financial engineering community, has potential to alleviate the above issues. The CVaR of $Z$ at level $\alpha \in {(0,1\rbrack}$ represents the expectation of the $\alpha \cdot {100\%}$ largest values of $Z$. The intuitive interpretation of CVaR and its quantitative characterization of risk aversion (in terms of a *fraction* of worst-case outcomes) are two reasons for its popularity in financial engineering (see and the references therein) and its emerging popularity in control (e.g., see ). In addition to financial applications, CVaR may be a useful tool for the design of stormwater systems, which are required to satisfy precise regulatory specifications, and for the operation of robotic systems.

However, the optimization of CVaR is computationally expensive in general. Unlike the expectation of a random (cumulative) cost, the CVaR of a random cost, subject to the dynamics of a Markov decision process, does *not* satisfy a dynamic programming (DP) recursion on the state space. One way to resolve this issue and make DP valid is via a suitable state augmentation.

Here, we study a linear-quadratic optimal control problem with *distributional ambiguity*, where the cost is assessed via CVaR. Our first step is to derive an upper bound to the optimal value of this problem. This derivation (Theorem 3.2). ‣ 3 Upper Bound for CVaR-LQ Problem ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")) and additional analysis (Theorem 4.8. ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")) motivate the formulation of an interesting dynamic programming algorithm (Theorem 5.15). While the associated value functions are defined on an augmented state space, they are computed in a *scalable* fashion since their parameters come from a Riccati-like recursion. Moreover, our algorithm provides a risk-averse controller, in which a risk-aversion level is parameterized in a novel way through a positive definite matrix. While our controller synthesis procedure is more computationally complex than LEQR, it does not involve a condition that is analogous to the positive definiteness of $\Sigma^{- 1} - {\gamma{\overline{P}}_{t + 1}}$ for all $t$.

## CVaR-Linear-Quadratic Problem

### Notation

If $M \in {\mathbb{R}}^{n \times n}$, then $M \geq 0$ ($M > 0$) means that $M$ is symmetric and positive semi-definite (positive definite). Upper-case letters denote random objects (e.g., $X_{t}$), and lower-case letters denote values of random objects (e.g., $x_{t}$). If $\mathcal{E}$ is a separable metrizable space, $\mathcal{B}{(\mathcal{E})}$ is the Borel sigma algebra on $\mathcal{E}$, and $\mathcal{P}{(\mathcal{E})}$ is the space of probability measures on $(\mathcal{E},{\mathcal{B}{(\mathcal{E})}})$ with the weak topology. We define $\overline{\mathbb{R}}:={{\mathbb{R}} \cup {\{{- \infty},{+ \infty}\}}}$, ${\mathbb{R}}_{+}:={\lbrack 0,{+ \infty})}$, and ${\mathbb{R}}_{+}^{n}:={\{{z \in {\mathbb{R}}^{n}}:{{z_{i} \in {\mathbb{R}}_{+}},{i = {1,\ldots,n}}}\}}$. $0_{n \times m}$ is the $n \times m$ zero matrix. $I_{n}$ is the $n \times n$ identity matrix. The trace of a matrix $M \in {\mathbb{R}}^{n \times n}$ is $\text{tr}{(M)}$.

### Linear-Quadratic System Model

Consider a fully observable, linear time-invariant system: where $X_{t}$ is a ${\mathbb{R}}^{n}$-valued random state, $U_{t}$ is a ${\mathbb{R}}^{m}$-valued random control, and $W_{t}$ is a ${\mathbb{R}}^{n}$-valued random disturbance at time $t$. The matrices $A \in {\mathbb{R}}^{n \times n}$ and $B \in {\mathbb{R}}^{n \times m}$ and the length of the time horizon $N \in {\mathbb{N}}$ are given. The initial state $X_{0}$ is fixed at an arbitrary $x \in {\mathbb{R}}^{n}$. For convenience, define ${f{(x_{t},u_{t},w_{t})}}:={{Ax_{t}} + {Bu_{t}} + w_{t}}$ for all $x_{t} \in {\mathbb{R}}^{n}$, $u_{t} \in {\mathbb{R}}^{m}$, and $w_{t} \in {\mathbb{R}}^{n}$.

We make the following assumptions about the ${\mathbb{R}}^{n}$-valued disturbance process $(W_{0},W_{1},\ldots,W_{N - 1})$. $W_{t}$ and $W_{s}$ are independent for all $t \neq s$, and $W_{t}$ is independent of the initial state $X_{0}$ for each $t$. For each $t$, the exact distribution of $W_{t}$ is not known. However, the first and maximal second moment of $W_{t}$ are known, which we specify below.

### Definition 1 (Ambiguity Set)

We define $\mathcal{P}_{W} \subseteq {\mathcal{P}{({\mathbb{R}}^{n})}}$ to be the set of probability measures with zero mean and covariance upper-bounded by $\Sigma > 0$. Each disturbance $W_{t}$ has a distribution $\nu_{t} \in \mathcal{P}_{W}$. In other words, $\nu_{t}$ satisfies ${\int_{{\mathbb{R}}^{n}}{w_{t}\nu_{t}{({dw_{t}})}}} = 0_{n \times 1}$ and ${\int_{{\mathbb{R}}^{n}}{w_{t}w_{t}^{T}\nu_{t}{({dw_{t}})}}} \leq \Sigma$.

As the system evolves, a random cumulative quadratic cost is incurred. The random cost-to-go for time $t \in {\{ 0,1,\ldots,{N - 1}\}}$ is defined as $c{(X_{j},U_{j})}$ is the random stage cost at time $j$. $Z_{N}$ is the random terminal cost. $Q \in {\mathbb{R}}^{n \times n}$, $R \in {\mathbb{R}}^{m \times m}$, and $Q_{f} \in {\mathbb{R}}^{n \times n}$ satisfy $Q > 0$, $R > 0$, and $Q_{f} > 0$, respectively. We define $Z:=Z_{0}$. With slight abuse of notation, we also use ${c{(x_{t},u_{t})}} = {{x_{t}^{T}Qx_{t}} + {u_{t}^{T}Ru_{t}}}$ for all $x_{t} \in {\mathbb{R}}^{n}$ and $u_{t} \in {\mathbb{R}}^{m}$.

### CVaR-Risk-Averse Optimal Control Problem

Consider a CVaR optimal control problem on a discrete, finite time horizon with distributional ambiguity: subject to the linear dynamics, where $x \in {\mathbb{R}}^{n}$ is an initial condition and $\alpha \in {(0,1\rbrack}$ is a risk-aversion level. The objective $\text{CVaR}_{\alpha,x}^{\pi,\gamma}{(Z)}$ is the CVaR of $Z$ at level $\alpha$, when the system is initialized at $x$ and evolves according to a control policy $\pi \in \Pi$ and a disturbance strategy $\gamma \in \Gamma$. ($\gamma$ provides a distribution for $W_{t}$ for each $t$. $\Pi$ and $\Gamma$ will be defined in this section.) The CVaR of $Z$ represents the expectation of the $\alpha \cdot 100$% largest values of $Z$.

While the problem does not satisfy a dynamic programming (DP) recursion on ${\mathbb{R}}^{n}$, there is a useful DP recursion on ${\mathbb{R}}^{n} \times {\mathbb{R}}$ (Lemma 4.12. ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")). A CVaR optimal control problem *without* distributional ambiguity has been solved by defining an augmented state space. Taking inspiration, we use a ${\mathbb{R}}^{n} \times {\mathbb{R}}$-valued, random *augmented state* $(X_{t},S_{t})$. The dynamics of $X_{t}$ are given. $S_{t}$ is a $\mathbb{R}$-valued random variable, whose dynamics are given by $S_{t}$ keeps track of the random cumulative cost up to time $t$. The realizations of $(X_{0},S_{0})$ are concentrated at an arbitrary point ${(x,s)} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$. We use the *augmented state space* ${\mathbb{R}}^{n} \times {\mathbb{R}}$ to define $\Pi$, the class of history-dependent control policies that summarize the history through $(X_{t},S_{t})$.

### Definition 2 (Control Policies $\Pi$)

A control policy $\pi \in \Pi$ takes the form $\pi:={(\pi_{0},\pi_{1},\ldots,\pi_{N - 1})}$, such that for each $t$, $\pi_{t}$ is a (Borel-measurable) stochastic kernel on ${\mathbb{R}}^{m}$ given ${\mathbb{R}}^{n} \times {\mathbb{R}}$.

### Definition 3 (Disturbance Strategies $\Gamma$)

Every disturbance strategy $\gamma \in \Gamma$ takes the form $\gamma:={(\nu_{0},\nu_{1},\ldots,\nu_{N - 1})}$, such that $\nu_{t} \in \mathcal{P}_{W}$ is the unknown distribution of $W_{t}$ for each $t$.

### Probability Space for Random Cumulative Cost

For any ${(x,s)} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$, $\pi \in \Pi$, and $\gamma \in \Gamma$, the random cost $Z = Z_{0}$ is defined on a probability space $(\Omega,{\mathcal{B}{(\Omega)}},P_{x,s}^{\pi,\gamma})$, where the sample space is $\Omega:={{({{\mathbb{R}}^{n} \times {\mathbb{R}} \times {\mathbb{R}}^{m}})}^{N} \times {\mathbb{R}}^{n} \times {\mathbb{R}}}$. Every $\omega \in \Omega$ takes the form $\omega = {(x_{0},s_{0},u_{0},\ldots,x_{N - 1},s_{N - 1},u_{N - 1},x_{N},s_{N})}$, where ${(x_{t},s_{t})} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$ is the value of $(X_{t},S_{t})$ and $u_{t} \in {\mathbb{R}}^{m}$ is the value of $U_{t}$ in the trajectory $\omega$. We have specified implicitly that the coordinates of $\omega$ have causal dependencies via and Definition 2 ‣ 2.3 CVaR-Risk-Averse Optimal Control Problem ‣ 2 A CVaR-Linear-Quadratic Problem ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem"). The random state at time $t$ is a function $X_{t}:{\Omega\rightarrow{\mathbb{R}}^{n}}$, such that if $\omega \in \Omega$ is as above, then ${X_{t}{(\omega)}}:=x_{t}$, which is Borel measurable. $S_{t}$ and $U_{t}$ are defined analogously. The probability measure $P_{x,s}^{\pi,\gamma}$ is used to evaluate expectations, e.g., ${E_{x,s}^{\pi,\gamma}{(Z)}}:={\int_{\Omega}{Z{(\omega)}{dP_{x,s}^{\pi,\gamma}}{(\omega)}}}$. The form of $P_{x,s}^{\pi,\gamma}$ on measurable rectangles is known, and it depends on the dynamics of the augmented state, an initial augmented condition ${(x,s)} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$, a control policy $\pi \in \Pi$, and a disturbance strategy $\gamma \in \Gamma$ (Ionescu-Tulcea Theorem). For instance, see \[17, Prop. 7.28\] or \[18, Prop. C.10, Remark C.11\] for details.

### Defining CVaR of Random Cumulative Cost

The Conditional Value-at-Risk of $Z = Z_{0}$ at a risk-aversion level $\alpha \in {(0,1\rbrack}$ is defined as follows: where ${g_{\alpha,x}^{\pi,\gamma}{(s,Z)}}:={s + {\frac{1}{\alpha}E_{x,s}^{\pi,\gamma}{({\max{({Z - S_{0}},0)}})}}}$.

### Remark 1

where $Y$ is a random variable such that ${E{({|Y|})}} < {+ \infty}$. In, we use an *extended definition* for CVaR to permit a class of policies $\Pi$ that depends on the augmented state space and need not have a particular analytical form (e.g., linear).

## Upper Bound for CVaR-LQ Problem

We use the definition of $\text{CVaR}_{\alpha,x}^{\pi,\gamma}{(Z)}$ to re-express $J_{\alpha}^{\ast}{(x)}$. For any $x \in {\mathbb{R}}^{n}$ and $\alpha \in {(0,1\rbrack}$, it holds that In the current section, first we show that there is a policy $\pi \in \Pi$ such that $J_{\alpha,\pi}{(x)}$ is finite (Lemma 1 is finite for some 𝜋) ‣ 3 Upper Bound for CVaR-LQ Problem ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")), which guarantees that the problem is well-defined. Second, we derive an upper bound to $J_{\alpha}^{\ast}{(x)}$ (Theorem 3.2). ‣ 3 Upper Bound for CVaR-LQ Problem ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")): with ${V_{0}^{\ast}{(x,s)}}:={\inf_{\pi \in \Pi}{\sup_{\gamma \in \Gamma}{E_{x,s}^{\pi,\gamma}{({\max{({Z - S_{0}},0)}})}}}}$. Toward the goal of computing $V_{0}^{\ast}$ scalably, we will define a value iteration algorithm with value functions $V_{N},\ldots,V_{1},V_{0}$ (Section 4). We will analyze the algorithm in the setting of deterministic policies and finitely many disturbance values. We will show that, under a measurable selection assumption, ${\overline{V}}_{0}^{\ast} \leq {\overline{V}}_{0}$ (Theorem 4.8. ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")), where ${\overline{V}}_{0}^{\ast}$ and ${\overline{V}}_{0}$ are the versions of $V_{0}^{\ast}$ and $V_{0}$ in the simplified setting, respectively. In Section 5, we will prove that $V_{0} \leq {\hat{V}}_{0}$, where such that $a_{0} \in {\mathbb{R}}$ and $P_{0} > 0$ are obtained via a Riccati-like recursion (Theorem 5.15). We will explain how the proof of Theorem 5.15 provides an algorithm for a novel risk-averse controller. Also, the above analysis takes key steps toward deriving a *scalable* upper bound to a CVaR linear-quadratic optimal control problem with distributional ambiguity.

### Lemma 1 ($J_{\alpha,\pi}{(x)}$ is finite for some $\pi$)

For all $x \in {\mathbb{R}}^{n}$ and $\alpha \in {(0,1\rbrack}$, there is a $\pi \in \Pi$ such that ${J_{\alpha,\pi}{(x)}} \in {\mathbb{R}}$.

### Proof 3.1

Let $\pi \in \Pi$ be an open-loop deterministic policy such that $U_{t}$ takes the value $0_{m \times 1}$ for each $t$. By using the quadratic cost, linear dynamics, and the definition of the ambiguity set, it holds that where $H_{x}^{\pi,\Sigma}:={{x^{T}Qx} + {\text{tr}\left({Fxx^{T}F^{T}\overline{Q}} \right)} + {\text{tr}\left({G\overline{\Sigma}G^{T}\overline{Q}} \right)}}$. $\overline{\Sigma}$ is a block diagonal matrix containing $N$ copies of $\Sigma$. $\overline{Q}:={\text{diag}{(Q,\ldots,Q,Q_{f})}}$ is a block diagonal matrix with $N - 1$ copies of $Q$. $F \in {\mathbb{R}}^{{Nn} \times n}$ and $G \in {\mathbb{R}}^{{{Nn} \times N}n}$ depend on $A$ and $N$. The desired statement follows.

By the previous lemma and since $\{{J_{\alpha,\pi}{(x)}}:{\pi \in \Pi}\}$ is bounded below by 0, it holds that ${J_{\alpha}^{\ast}{(x)}} \in {\mathbb{R}}$.

### Theorem 3.2 (Upper bound to $J_{\alpha}^{\ast}{(x)}$)

| | $G_{\alpha}{(x)}$ | ${{:={\inf\limits_{\pi \in \Pi}{\inf\limits_{s \in {\mathbb{R}}}{\sup\limits_{\gamma \in \Gamma}{g_{\alpha,x}^{\pi,\gamma}{(s,Z)}{\forall x}}}}} \in {\mathbb{R}}^{n}},{{\forall\alpha} \in {(0,1\rbrack}}},$ | | \(7\) | | | $V_{0}^{\ast}{(x,s)}$ | ${{:={\inf\limits_{\pi \in \Pi}{\sup\limits_{\gamma \in \Gamma}{E_{x,s}^{\pi,\gamma}{({\max{({Z - S_{0}},0)}})}{\forall x}}}} \in {\mathbb{R}}^{n}},{{\forall s} \in {\mathbb{R}}}}.$ | | | For all $x \in {\mathbb{R}}^{n}$ and $\alpha \in {(0,1\rbrack}$, ${J_{\alpha}^{\ast}{(x)}} \leq {G_{\alpha}{(x)}}$, ${G_{\alpha}{(x)}} \in {\mathbb{R}}$, and ${G_{\alpha}{(x)}} = {\underset{s\in{\mathbb{R}}}{inf}{({s + {\frac{1}{\alpha}V_{0}^{\ast}{(x,s)}}})}}$. Moreover, $V_{0}^{\ast}$ is finite.

### Proof 3.3

We have ${J_{\alpha}^{\ast}{(x)}} \leq {G_{\alpha}{(x)}}$ because where $\Gamma_{x}^{\pi}:={\{{\gamma \in \Gamma}:{{E_{x,s}^{\pi,\gamma}{(Z)}} < {+ {\infty{\forall s}}} \in {\mathbb{R}}}\}}$, and since $\Gamma_{x}^{\pi} \subseteq \Gamma$. ${G_{\alpha}{(x)}} \in {\mathbb{R}}$ because $\{{\sup_{\gamma \in \Gamma}{g_{\alpha,x}^{\pi,\gamma}{(s,Z)}}}:{{\pi \in \Pi},{s \in {\mathbb{R}}}}\}$ is bounded below and there exist $s \in {\mathbb{R}}$ and $\pi \in \Pi$ such that ${\sup_{\gamma \in \Gamma}{g_{\alpha,x}^{\pi,\gamma}{(s,Z)}}} \in {\mathbb{R}}$. Indeed, let $s = 0$, and let $\pi$ assign the value $0_{m \times 1}$ to each $U_{t}$. Then, we have We have ${G_{\alpha}{(x)}} = {\inf_{s \in {\mathbb{R}}}{({s + {\frac{1}{\alpha}V_{0}^{\ast}{(x,s)}}})}}$ because one may exchange the order of infima. $V_{0}^{\ast}$ is finite because 1) for any ${(x,s)} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$, there is a $\pi \in \Pi$ such that ${\sup_{\gamma \in \Gamma}{E_{x,s}^{\pi,\gamma}{({\max{({Z - S_{0}},0)}})}}} \in {\mathbb{R}}$, and 2) $\{{\sup_{\gamma \in \Gamma}{E_{x,s}^{\pi,\gamma}{({\max{({Z - S_{0}},0)}})}}}:{\pi \in \Pi}\}$ is bounded below by 0. For the first property, one may choose the policy that assigns the value $0_{m \times 1}$ to each $U_{t}$.

## Analysis of a Value Iteration Algorithm

To estimate $V_{0}^{\ast}$. ‣ 3 Upper Bound for CVaR-LQ Problem ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")) in a scalable fashion, we propose a value iteration algorithm on ${\mathbb{R}}^{n} \times {\mathbb{R}}$.

### Algorithm 1 (Value Iteration for General Setting)

Let the functions $V_{N},V_{N - 1},\ldots,V_{0}$ be defined recursively as follows. For all ${(x,s)} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$ and for $t = {{N - 1},\ldots,1,0}$,

### Conjecture 4.4

The functions $V_{N - 1},\ldots,V_{1},V_{0}$ are Borel measurable and bounded below by 0.

We use the Conjecture in the proof of Theorem 5.15, which requires the Lebesgue integrals in Algorithm 1 ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem") to exist. The Conjecture will be proved formally in future work by using properties of convex functions.

In this work, we will analyze Algorithm 1 ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem") in the setting of finitely many disturbance values and deterministic policies.

### Definition 4.5 ($\overline{\Pi}$)

$\overline{\Pi}$ is the set of deterministic policies such that every $\pi \in \overline{\Pi}$ takes the form $\pi = {(\pi_{0},\pi_{1},\ldots,\pi_{N - 1})}$, where each $\pi_{t}:{{{\mathbb{R}}^{n} \times {\mathbb{R}}}\rightarrow{\mathbb{R}}^{m}}$ is Borel measurable.

### Definition 4.6 (${\overline{\mathcal{P}}}_{W}$)

Let $W_{t}$ be supported on the $N_{W} \in {\mathbb{N}}$ points ${\{ w^{1},w^{2},\ldots,w^{N_{W}}\}} \subseteq {\mathbb{R}}^{n}$, and let $p_{t}^{j} \in {\lbrack 0,1\rbrack}$ be the (unknown) probability that the value of $W_{t}$ is $w^{j}$. In this case, the ambiguity set of distributions is

### Definition 4.7 ($\overline{\Gamma}$)

The set of disturbance strategies in the setting of finitely many disturbance values is $\overline{\Gamma}:=\left\{ {\gamma = {(p_{0},p_{1},\ldots,p_{N - 1})}}:{p_{t} \in {{\overline{\mathcal{P}}}_{W}{\forall t}}} \right\}$.

The version of $V_{0}^{\ast}$. ‣ 3 Upper Bound for CVaR-LQ Problem ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")) in the setting of finitely many disturbance values and deterministic policies is for all ${(x,s)} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$. The version of Algorithm 1 ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem") in the setting of finitely many disturbance values follows.

### Algorithm 2 (Value Iteration in Finite Case)

Let the functions ${\overline{V}}_{N},{\overline{V}}_{N - 1},\ldots,{\overline{V}}_{0}$ be defined recursively as follows. For all ${(x,s)} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$ and for $t = {{N - 1},\ldots,1,0}$, The next theorem specifies properties of Algorithm 2 ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem").

### Theorem 4.8 (Analysis of Algorithm 2 ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem"))

For $t = {0,1,\ldots,N}$, the value function ${\overline{V}}_{t}:{{{\mathbb{R}}^{n} \times {\mathbb{R}}}\rightarrow{\mathbb{R}}}$ is convex and bounded below by 0, and ${\overline{V}}_{t}{(x_{t},s_{t})}$ is non-increasing in $s_{t}$ for each $x_{t}$. For $t = {0,1,\ldots,{N - 1}}$, for any ${(x_{t},s_{t})} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$, there is a $u_{x_{t},s_{t}}^{\ast} \in {\mathbb{R}}^{m}$ such that For $t = {0,1,\ldots,{N - 1}}$, suppose that ${\overline{V}}_{t}$ is Borel measurable and there is a Borel measurable function $\pi_{t}^{\ast}:{{{\mathbb{R}}^{n} \times {\mathbb{R}}}\rightarrow{\mathbb{R}}^{m}}$ such that for all ${(x_{t},s_{t})} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$, Define $\pi^{\ast}:={(\pi_{0}^{\ast},\pi_{1}^{\ast},\ldots,\pi_{N - 1}^{\ast})}$. Then, Algorithm 2 ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem") provides an upper bound to ${\overline{V}}_{0}^{\ast}$, specifically, ${\overline{V}}_{0}^{\ast} \leq {\overline{V}}_{0}$.

### Remark 4.9

Theorem 4.8. ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem") invokes a measurable selection assumption (see also \[18, Th. 3.2.1\]), which motivates future study of measurable selection theorems.

To prove Theorem 4.8. ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem"), we present two supporting results.

### Lemma 4.10 (Value Function Analysis)

Let $v:{{{\mathbb{R}}^{n} \times {\mathbb{R}}}\rightarrow{\mathbb{R}}}$ be convex and bounded below by 0. Also, let $v{(x,s)}$ be non-increasing in $s$ for each $x$. Define $v^{\ast}:{{{\mathbb{R}}^{n} \times {\mathbb{R}}}\rightarrow\overline{\mathbb{R}}}$ as ${v^{\ast}{(x,s)}}:={\inf_{u \in {\mathbb{R}}^{m}}{\sup_{p \in {\overline{\mathcal{P}}}_{W}}{\sum_{j = 1}^{N_{W}}{p^{j}v\left( {f{(x,u,w^{j})}},{s - {c{(x,u)}}} \right)}}}}$. Then, $v^{\ast}$ is finite, convex, and bounded below by 0, and $v^{\ast}{(x,s)}$ is non-increasing in $s$ for each $x$. Also, for all ${(x,s)} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$, there is a $u_{x,s}^{\ast} \in {\mathbb{R}}^{m}$ such that ${v^{\ast}{(x,s)}} = {\sup_{p \in {\overline{\mathcal{P}}}_{W}}{\sum_{j = 1}^{N_{W}}{p^{j}v\left( {f{(x,u_{x,s}^{\ast},w^{j})}},{s - {c{(x,u_{x,s}^{\ast})}}} \right)}}}$.

### Proof 4.11

Since $f{(x,u,w^{j})}$ is affine in $(x,u,s)$ for each $w^{j}$, $s - {c{(x,u)}}$ is concave in $(x,u,s)$, $v$ is convex, and $v{(x,s)}$ is non-increasing in $s$ for each $x$, ${(x,u,s)}\mapsto{v{({f{(x,u,w^{j})}},{s - {c{(x,u)}}})}}$ is convex in $(x,u,s)$ for each $w^{j}$. By proceeding step-by-step through the operations that lead to $v^{\ast}$ and by using knowledge of the operations that preserve convexity, the desired properties follow.

The next supporting result for Theorem 4.10. ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem") provides properties of conditional expectations and a DP recursion on ${\mathbb{R}}^{n} \times {\mathbb{R}}$. For $t = {0,1,\ldots,N}$, the function $\omega\mapsto{({X_{t}{(\omega)}},{S_{t}{(\omega)}})}$ is Borel measurable \[17, Prop. 7.14\]. Let $\pi \in \overline{\Pi}$ and $\gamma \in \overline{\Gamma}$ be given. For $t = {0,1,\ldots,N}$, denote the *$(\pi,\gamma)$-conditional expectation* of $\max{({Z_{t} - S_{t}},0)}$ as follows: ${\varphi_{t}^{\pi,\gamma}{(x_{t},s_{t})}}:={E^{\pi,\gamma}{({{\left. {\max{({Z_{t} - S_{t}},0)}} \middle| X_{t} \right. = x_{t}},{S_{t} = s_{t}}})}}$, where $Z_{t}$ is defined by and $Z = Z_{0}$. The function $\varphi_{t}^{\pi,\gamma}:{{{\mathbb{R}}^{n} \times {\mathbb{R}}}\rightarrow\overline{\mathbb{R}}}$ is Borel measurable, and $\varphi_{t}^{\pi,\gamma}$ is almost-everywhere unique with respect to $P_{t,x,s}^{\pi,\gamma} \in {\mathcal{P}{({{\mathbb{R}}^{n} \times {\mathbb{R}}})}}$, which is defined by for every $K \in {\mathcal{B}{({{\mathbb{R}}^{n} \times {\mathbb{R}}})}}$ \[19, Th. 6.3.3\].

### Lemma 4.12 (A DP Recursion)

Let $\pi \in \overline{\Pi}$, $\gamma \in \overline{\Gamma}$, and ${(x,s)} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$ be given. Then, we have for almost every ${(x_{N},s_{N})} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$ with respect to $P_{N,x,s}^{\pi,\gamma}$. Lastly, it holds that for almost every ${(x_{t},s_{t})} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$ with respect to $P_{t,x,s}^{\pi,\gamma}$ and for every $t \in {\{{N - 1},\ldots,1,0\}}$.

### Proof 4.13

The conclusions follow from the same arguments that are used to prove the DP recursion for expected cumulative costs (when one uses the probability measure $P_{x,s}^{\pi,\gamma}$ and the dynamics of the augmented state).

Next, we use Lemma 4.10. ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem") and Lemma 4.12. ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem") to prove Theorem 4.8. ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem").

### Proof 4.14 (Theorem 4.8. ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem"))

The properties of ${\overline{V}}_{t}$ hold by verifying the properties of ${\overline{V}}_{N}$ and by applying Lemma 4.10. ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem") inductively. Next, we show the last statement, i.e., ${\overline{V}}_{0}^{\ast} \leq {\overline{V}}_{0}$. By Lemma 4.12. ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem"), we have ${{\overline{V}}_{0}^{\ast}{(x,s)}} = {\inf_{\pi \in \overline{\Pi}}{\sup_{\gamma \in \overline{\Gamma}}{\varphi_{0}^{\pi,\gamma}{(x,s)}}}}$ for all ${(x,s)} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$. Let ${(x,s)} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$, $\gamma \in \overline{\Gamma}$, and $t \in {\{ 0,1,\ldots,N\}}$ be given. It suffices to show that $\varphi_{t}^{\pi^{\ast},\gamma} \leq {\overline{V}}_{t}$ almost everywhere with respect to $P_{t,x,s}^{\pi^{\ast},\gamma}$. Indeed, the above statement implies that $\varphi_{0}^{\pi^{\ast},\gamma} \leq {\overline{V}}_{0}$ almost everywhere with respect to $P_{0,x,s}^{\pi^{\ast},\gamma}$. It follows that Since $\gamma \in \overline{\Gamma}$ in (12. ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")) is arbitrary, we have Then, since $\pi^{\ast} \in \overline{\Pi}$ and by the definition of the infimum, Since ${(x,s)} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$ in (14. ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")) is arbitrary, the proof would be complete.

We will prove that $\varphi_{t}^{\pi^{\ast},\gamma} \leq {\overline{V}}_{t}$ almost everywhere with respect to $P_{t,x,s}^{\pi^{\ast},\gamma}$ by backwards induction on $t$. The base case ($t = N$) holds by Lemma 4.12. ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem") and the definition of ${\overline{V}}_{N}$. Now, assume (the induction hypothesis) that for some $t \in {\{{N - 1},\ldots,1,0\}}$ we have $\varphi_{t + 1}^{\pi^{\ast},\gamma} \leq {\overline{V}}_{t + 1}$ almost everywhere with respect to $P_{{t + 1},x,s}^{\pi^{\ast},\gamma}$. For brevity, we use the notation By applying Lemma 4.12. ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem"), ${\overline{V}}_{t + 1}$ being Borel measurable, and (10. ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")), it suffices to show that for almost every ${(x_{t},s_{t})} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$ with respect to $P_{t,x,s}^{\pi^{\ast},\gamma}$. This follows from the induction hypothesis, the Borel measurability of ${\overline{V}}_{t + 1}$, and a classic integration result \[19, Th. 1.6.6 (b)\]. This also involves expressing $P_{{t + 1},x,s}^{\pi^{\ast},\gamma}$ in terms of $P_{t,x,s}^{\pi^{\ast},\gamma}$; the reader may see \[17, p. 192, Eq. \] for a related derivation.

## Scalable Upper Bound

Here, we return to the setting where there may be uncountably many disturbance values. We will derive a scalable upper bound to $V_{0}$ (Alg. 1 ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")) of the form, ${{\hat{V}}_{0}{(x,s)}}:={a_{0} + {\max{({{x^{T}P_{0}x} - s},0)}}}$ for all ${(x,s)} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$, where $a_{0} \in {\mathbb{R}}$ and a positive definite symmetric matrix $P_{0} \in {\mathbb{R}}^{n \times n}$ are obtained through a Riccati-like recursion. The recursion is parameterized by a positive definite symmetric matrix $L$ and provides a risk-averse controller. After the proof of Theorem 5.15, we will describe the controller synthesis procedure.

### Theorem 5.15

Define $P_{N}:=Q_{f}$ and $a_{N}:=0$. Let $L \in {\mathbb{R}}^{n \times n}$ satisfy $L > 0$. For $t = {{N - 1},\ldots,1,0}$, define the matrices $P_{t} \in {\mathbb{R}}^{n \times n}$, such that $P_{t} > 0$, and the scalars $a_{t} \in {\mathbb{R}}$ recursively, For all $t \in {\{ N,\ldots,1,0\}}$, define ${{\hat{V}}_{t}{(x_{t},s_{t})}}:={a_{t} + {\max{({{x_{t}^{T}P_{t}x_{t}} - s_{t}},0)}}}$ for all ${(x_{t},s_{t})} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$. Then, for all $t \in {\{ N,\ldots,1,0\}}$, we have $V_{t} \leq {\hat{V}}_{t}$, provided that $V_{t}$ is Borel measurable and bounded below by 0.

### Remark 5.16 (About $L$, $P_{t}$, $a_{t}$)

$P_{t}$ and $a_{t}$ are parameterized by $L$. In the finite-time case above, $L \in {\mathbb{R}}^{n \times n}$ is only required to be symmetric and positive definite.

### Proof 5.17

We proceed by induction. The base case holds because $P_{N} = Q_{f}$ and $a_{N} = 0$. Now assume that for some $t \in {\{{N - 1},\ldots,1,0\}}$, for all ${(x_{t + 1},s_{t + 1})} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$, we have ${V_{t + 1}{(x_{t + 1},s_{t + 1})}} \leq {a_{t + 1} + {\max{({{x_{t + 1}^{T}P_{t + 1}x_{t + 1}} - s_{t + 1}},0)}}}$, where $P_{t + 1} \in {\mathbb{R}}^{n \times n}$ satisfies $P_{t + 1} > 0$ and $a_{t + 1}$ is a scalar. It suffices to show that ${{V_{t}{(x_{t},s_{t})}} \leq {a_{t} + {{\max{({{x_{t}^{T}P_{t}x_{t}} - s_{t}},0)}}{\forall{(x_{t},s_{t})}}}} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}},$ where $a_{t}$ and $P_{t}$ are defined. Let ${(x_{t},s_{t})} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$. Since ${\hat{V}}_{t + 1}$ and $V_{t + 1}$ are Borel measurable and $0 \leq V_{t + 1} \leq {\hat{V}}_{t + 1}$, it holds that ${V_{t}{(x_{t},s_{t})}} \leq {a_{t + 1} + {\inf_{u_{t} \in {\mathbb{R}}^{m}}{\sup_{\nu_{t} \in \mathcal{P}_{W}}{\int_{{\mathbb{R}}^{n}}{{\max{({\phi_{{t + 1},u_{t}}^{x_{t},s_{t}}{(w_{t})}},0)}}\nu_{t}{({dw_{t}})}}}}}}$, where ${\phi_{{t + 1},u_{t}}^{x_{t},s_{t}}{(w_{t})}}:={{{f{(x_{t},u_{t},w_{t})}^{T}P_{t + 1}f{(x_{t},u_{t},w_{t})}} + {c{(x_{t},u_{t})}}} - s_{t}}$. By weak duality (e.g., see \[20, Lem. A.1\]), where $\Delta:={\text{diag}{(\Sigma,1)}}$ and $\mathcal{M}_{{t + 1},u_{t}}^{x_{t},s_{t}}$ is the set of matrices $M = \begin{bmatrix} \end{bmatrix} > 0$ s.t. $M_{11} \in {\mathbb{R}}^{n \times n}$, $M_{22} \in {\mathbb{R}}$, and By matrix algebra, it follows that is equivalent to Here, $(\ast)$ denotes the appropriate terms for symmetry. By \[21, Lemma 3.1\], is solvable for $u_{t} \in {\mathbb{R}}^{m}$ if and only if ${W_{\overline{P}}^{T}\Phi_{x_{t},s_{t}}^{M}W_{\overline{P}}} > 0$ and ${W_{\overline{Q}}^{T}\Phi_{x_{t},s_{t}}^{M}W_{\overline{Q}}} > 0$, where the columns of $W_{\overline{P}}$ and $W_{\overline{Q}}$ form bases for the nullspaces of $\overline{P}$ and $\overline{Q}$, respectively. By matrix algebra, it holds that Therefore, $\psi{(x_{t},s_{t})}$ is equivalent to By and $\Delta = {\text{diag}{(\Sigma,1)}}$, it holds that By taking a Schur complement, $M > H_{x_{t},s_{t}}$ is equivalent to $M_{11} > \overset{\sim}{G}$ and $M_{22} > {h{(x_{t},s_{t},M)}}$, where We have $\overset{\sim}{G} \leq P_{t + 1}$, so $M_{11} > \overset{\sim}{G}$ is redundant: To bound the objective, we use the relaxation $M_{12} = 0_{n \times 1}$. Recall that $L > 0$ and define the set ${\hat{\mathcal{M}}}_{{t + 1},L}^{x_{t},s_{t}} \subseteq \mathcal{M}_{t + 1}^{x_{t},s_{t}}$ as: where we define ${\hat{h}{(x_{t},s_{t},M_{11})}}:=$ By substituting the definition of $M_{11}^{\ast}$, we have where $a_{t}$ is given. Since ${\hat{h}{(x_{t},s_{t},{P_{t + 1} + L})}} = {{x_{t}^{T}P_{t}x_{t}} - s_{t}}$, where $P_{t}$ is given, we are done.

### Remark 5.18 (Controller Synthesis)

Based on the proof of Theorem 5.15, we can derive a sub-optimal policy as follows. For a fixed $L > 0$, compute the matrices $P_{t}$ via the recursion. Let $x_{0} \in {\mathbb{R}}^{n}$ be an initial condition. Define $s_{0}:={x_{0}^{T}P_{0}x_{0}}$, which depends on $L$ through $P_{0}$. For $t = {0,1,\ldots,{N - 1}}$, proceed through the following steps: Compute $M_{x_{t},s_{t}}^{\ast}$ as per the proof of Theorem 5.15, $M_{x_{t},s_{t}}^{\ast}:={\text{diag}{(M_{11}^{\ast},M_{22}^{\ast})}}$, where $M_{11}^{\ast}:={P_{t + 1} + L}$, $M_{22}^{\ast}:={\max{({\hat{h}{(x_{t},s_{t},M_{11}^{\ast})}},0)}}$, and $\hat{h}$ is given.

Choose a $u_{t} \in {\mathbb{R}}^{m}$ that satisfies when $M = M_{x_{t},s_{t}}^{\ast}$. Such a $u_{t}$ is guaranteed to exist from the choice of $M = M_{x_{t},s_{t}}^{\ast}$ and by repeating several steps in the proof above. We note that the $u_{t}$ satisfying may not be unique.

Nature chooses a disturbance value $w_{t} \in {\mathbb{R}}^{n}$.

Calculate $x_{t + 1} = {{Ax_{t}} + {Bu_{t}} + w_{t}}$ and $s_{t + 1} = {s_{t} - {c{(x_{t},u_{t})}}}$. Update $t$ by 1. Go to step 1 if $t < N$.

We now identify some interesting similarities and differences between our approach and classical methods.

### Remark 5.19 (Relation to LEQR and LQ games)

The Riccati recursion for the LEQR problem in finite time takes the form: for $t = {{N - 1},\ldots,1,0}$, provided that $\gamma > 0$ is chosen so that $\Sigma^{- 1} - {\gamma{\overline{P}}_{t + 1}}$ is positive definite for each $t$. Similarly, the Riccati recursion for a soft-constrained LQ game takes the form \[1, Eq. 3.4a', p. 53\]: for $t = {{N - 1},\ldots,1,0}$, provided that ${\hat{P}}_{t}$ is invertible for each $t$, $R = I_{m}$, and $\lambda$ is a scalar parameter representing a disturbance-attenuation level. The key differences between, (33. ‣ 5 A Scalable Upper Bound ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")), and (34. ‣ 5 A Scalable Upper Bound ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")) appear in the terms $\gamma\Sigma$, $\frac{1}{\lambda^{2}}\Sigma$, and ${({P_{t + 1} + L})}^{- 1}$, respectively. Our recursion encodes a risk-aversion level through the matrix ${({P_{t + 1} + L})}^{- 1}$, whereas the classical recursions (33. ‣ 5 A Scalable Upper Bound ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")) (34. ‣ 5 A Scalable Upper Bound ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")) encode risk aversion by scaling the covariance $\Sigma$.

### Remark 5.20 (Relation to minimax MPC)

One may interpret an LEQR controller in a model-predictive-control (MPC) setting as an approximate solution to minimax MPC \[3, p. 99\]. In minimax MPC, a matrix $\mathcal{T} \geq 0$, which depends on a bounded region containing the process noise, appears in the algorithm that provides an optimal control \[3, Eq. 8.29, p. 99\]. Our recursion has a similar structure since it is parameterized by a matrix $L > 0$, and it is plausible that a preferable choice of $L$ depends on the maximal covariance $\Sigma$ (a topic for future investigation). A key distinction between minimax MPC and our approach is the uncertainty model of the process noise. Our approach permits process noise with an unbounded support and a spectrum of possibilities that occur with various probabilities. However, minimax MPC permits process noise that lives in a bounded region with known bounds \[3, p. 42\]. The "better" uncertainty model may be application-dependent.

## Numerical Simulation

Fig. 1 provides example trade-off curves comparing LEQR (as $\gamma$ varies) with our proposed approach from Section 5 (as $L$ varies). These results show that for a simple one-state system, our proposed approach (ACVaR) has comparable performance relative to LEQR. This finding is notable given the simplicity of our experiment and that our method avoids the case where $\gamma$ is too large and the LEQR cost becomes infinite. We also simulated the optimal CVaR controller , which is not distributionally robust. This controller assumes exact prior knowledge of the disturbance distribution, which explains its superior performance. However, this optimal CVaR controller is not scalable to higher-dimensional problem instances, since it requires discretizing the augmented state space.

Figure 1: Trade-offs between empirical mean, standard deviation, and CVaR0.05 of the LQR cost for (i) our controller (ACVaR) as L varies, (ii) the LEQR controller as γ varies (LEQR), (iii) the exact CVaRα controller with prior knowledge of the disturbance distribution as α varies (CVaR), and (iv) the LQR controller (LQR). We used the scalar dynamical system xt + 1 = xt + ut + wt with R = Qf = 1, Q = 10−3, x0 = 1, and N = 4. The disturbance wt is zero-mean Gaussian with unit variance. The parameter ranges were 0.2 ≤ L ≤ 100, $\frac{\gamma_{\text{c}}}{10} \leq \gamma \leq \gamma_{\text{c}}$, where γc is the critical γ value for LEQR. Each point is the mean of 50,000 trials, where the same schedule of pseudo-random seeds are used across policies. In the limits L → ∞, γ → 0, and α → 1 for ACVaR, LEQR, and CVARα, respectively, we recover the risk-neutral LQR policy.

## Concluding Remarks

We took steps toward deriving a scalable upper bound to a distributionally robust, CVaR optimal control problem for linear systems with quadratic costs. CVaR characterizes the (usually abstract) notion of risk as a fraction of worst-case outcomes, which is intuitive and precise. A result from our analysis is a risk-averse controller with intriguing similarities and differences relative to the state-of-the-art.

Potential areas for future work include studying the infinite-horizon case, characterizing the extent to which the upper bound approximation parameterized by $L$ is tight, and elucidating the connections between the choice of $L$ and the maximal covariance $\Sigma$.

Further numerical experiments, potentially with higher-dimensional or more realistic application-specific examples, are needed to ascertain whether the proposed approach may be a superior alternative to LEQR in certain application domains.
