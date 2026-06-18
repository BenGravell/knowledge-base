## Introduction

In this paper we study the problem of designing control laws for an unknown dynamical system using noisy data. This general problem exists for a long time, but has seen a renewed surge of interest over the last few years. The problem can be approached via different angles, for example using combined system identification and model-based control, or by computing control laws from data without the intermediate modeling step. We will contribute to the second category of methods, aiming at control design directly from noisy data.

One of the main challenges in this area is to come up with robust control laws that guarantee stability and performance of the unknown system despite the inherent uncertainty caused by noisy data. Even though there are several recent contributions addressing this issue, there are multiple open questions. In fact, one of the unsolved problems is to come up with *non-conservative* control design strategies using only a finite number of data samples.

We will tackle this problem by providing necessary and sufficient conditions on noisy data under which controllers can be obtained. As a consequence, our ensuing control technique is non-conservative, and also shown to be tractable from a computational point of view. The technical ingredient that enables our design is a new generalization of the classical S-lemma, which will be proven in this paper. We will formulate our control problems using the general data informativity framework as introduced in. As such, the results developed in this paper can be seen as a natural extension of those in to noisy data.

### Literature on data-driven control

The literature on data-driven control is expanding rapidly. Our account of previous work is therefore not exhaustive, but we note that additional references can be found in the survey. We mention contributions to data-driven optimal control, PID control, predictive control, and nonlinear control. Some of these techniques are iterative in nature: the controller is updated online when new data are presented. Examples of this include policy iteration methods and iterative feedback tuning. Other methods are one-shot in the sense that the controller is constructed offline from a batch of data. We mention, for instance, virtual reference feedback tuning and methods based on Willems' fundamental lemma (see also ). The latter line of work has been quite fruitful, with contributions ranging from output matching and control by interconnection, to data-enabled predictive control and a data-based closed-loop system parameterization. This parameterization has been used for stabilizing and optimal control design using data-based linear matrix inequalities. We also mention the extension studying LQR using noisy data, and the paper for a closed-loop parameterization using noisy data. Additional recent research directions include data-driven control of networks and the interplay between data-guided control and model reduction.

### Review of the S-lemma

First proven by Yakubovich, the *S-lemma* is a classical result in control theory and optimization. The result revolves around the question when the non-negativity of one quadratic function implies that of another. The crux of the S-lemma is that this seemingly difficult implication is equivalent to the feasibility of a linear matrix inequality (LMI) in a scalar variable, called a *multiplier*. The act of replacing the implication by a linear matrix inequality is often referred to as the *S-procedure*. The S-procedure is more generally applicable in situations where one quadratic inequality is implied by *multiple* quadratic inequalities. In this case, multiple scalar multipliers are used. It is well-known, however, that the S-procedure is conservative in general, although there exist special cases in which losslessness (a là S-lemma) can be shown \[2, Sec. 3\]. A generalized S-lemma involving more general types of multipliers was considered in, and was shown to be non-conservative under extra assumptions.

The classical S-lemma, as well as the contributions mentioned above, all deal with vector variables. However, for reasons that will become clear in Section II, we need a type of S-lemma that is applicable to quadratic functions of *matrix* variables. Such a result has been reported for specific quadratic functions in \[46, Thm. 3.3\]. In the special case that variables are *bounded*, an S-lemma for matrix variables can also be derived by combining the so-called *full block S-procedure* with results from the literature on LMI relaxations. These specific results are, however, less suited for the application of data-driven control that we have in mind. Therefore, in this paper we derive general matrix S-lemmas for both strict and non-strict inequalities. Our matrix S-lemma for non-strict inequalities is a direct generalization of the classical S-lemma. It also recovers the result from as a special case. As a corollary of our matrix S-lemma for a strict inequality, we recover the S-lemma derived from the general theory on LMI relaxations.

### Our contributions

The core of our approach is to formulate data-driven control as the problem of deciding whether one quadratic matrix inequality is implied by another one. Our first contribution is to extend the classical S-lemma to quadratic matrix inequalities. Our second contribution is to apply these results to data-driven control. In particular, we come up with design procedures for quadratic stabilization, $\mathcal{H}_{2}$ control and $\mathcal{H}_{\infty}$ control.

Throughout the paper we will assume no statistics on the noise, but we will work with general bounded disturbances. We are thereby inspired by recent papers that formalize the assumption of bounded disturbances in terms of quadratic matrix inequalities. In fact, we will work with an assumption on the noise that is closely related to that of, and is more general than the assumption in. In terms of control design, our approach completely differs from the above papers. In fact, instead of working with data-based parameterizations of closed-loop systems, we will work with a representation of all *open-loop* systems explaining the data, akin to the framework of. We believe that our approach is attractive for the following reasons:

We provide robust guarantees on the stability and performance of the unknown data-generating system. The design involves data-guided LMI's that are tractable from a computational point of view and are easy to implement.

By virtue of our matrix S-lemma, the design method is *non-conservative*. This is in contrast with previous LMI formulations in that provide sufficient conditions for controller design.

Last but not least, the variables involved in our method are independent of the time horizon of the experiment. Our approach is thus applicable to large data sets. This is an advantage over closed-loop system parameterizations, that become computationally intractable when applied to big data.

### Outline of the paper

In Section II we will formulate the problem. Section III contains our results on the matrix S-lemma. These results are then applied to data-driven stabilization in Section IV, and to data-driven $\mathcal{H}_{2}$ control and $\mathcal{H}_{\infty}$ control in Section V. In Section VI we provide simulation examples. Finally, our conclusions are provided in Section VII.

## The problem of data-driven stabilization

Consider the linear time-invariant system

where ${\mathbf{x}} \in {\mathbb{R}}^{n}$ denotes the state, ${\mathbf{u}} \in {\mathbb{R}}^{m}$ is the input and ${\mathbf{w}} \in {\mathbb{R}}^{n}$ is an unknown noise term. The matrices $A_{s} \in {\mathbb{R}}^{n \times n}$ and $B_{s} \in {\mathbb{R}}^{n \times m}$ denote the unknown state and input matrices. Our goal is to design stabilizing controllers for on the basis of a finite number of measurements of the state and input of the system. To this end, suppose that we measure state and input data on a time interval^11^1All our results are still true for data collected on multiple intervals, see \[3, Ex. 2\] for more details on how to arrange the data matrices in this case., and collect these samples in the matrices

By defining the matrices

We emphasize that the system matrices $A_{s}$ and $B_{s}$ as well as the noise term $W_{-}$ are *unknown*, while $X$ and $U_{-}$ are measured. Before we introduce the problem we will explain our assumption on the noise $W_{-}$.

### II-A Assumption on the noise

We will formalize our assumption on the noise in terms of a quadratic matrix inequality.

### Assumption 1

The noise samples ${w{}},{w{}},\ldots,{w{({T - 1})}}$, collected in the matrix $W_{-}$, satisfy the bound

for known matrices $\Phi_{11} = \Phi_{11}^{\top}$, $\Phi_{12}$ and $\Phi_{22} = \Phi_{22}^{\top} < 0$.

Note that the negative definiteness of $\Phi_{22}$ ensures that the set of noise matrices $W_{-}$ satisfying is bounded. In the special case $\Phi_{12} = 0$ and $\Phi_{22} = {- I}$, reduces to

The inequality has the interpretation that the energy of $\mathbf{w}$ is bounded on the finite time interval $\lbrack 0,{T - 1}\rbrack$. If $\mathbf{w}$ is a random variable, its *sample covariance matrix* is given by

where $J$ is the matrix of ones. Thus, can also capture known bounds on the sample covariance by the choices $\Phi_{12} = 0$ and $\Phi_{22} = {- {\frac{1}{T - 1}{({I - {\frac{1}{T}J}})}}}$. We emphasize, however, that we do not make any assumptions on the statistics of $\mathbf{w}$ and work with the general bound instead. Note that \[37, Asm. 5\] is a special case of Assumption 1 for the choices $\Phi_{11} = {\gammaX_{+}X_{+}^{\top}}$ with $\gamma > 0$, $\Phi_{12} = 0$ and $\Phi_{22} = {- I}$. We remark that norm bounds on the individual noise samples $w{(t)}$ also give rise to bounds of the form, although this may lead to some conservatism. Indeed, note that $\left. \parallel{w{(t)}}\parallel \right._{2}^{2} \leqslant \epsilon$ implies that ${w{(t)}w{(t)}^{\top}} \leqslant {\epsilonI}$ for all $t$. As such, the bound is satisfied for $\Phi_{11} = {T\epsilonI}$.

### Remark 1

Note that the noise model in Assumption 1 is the "transposed" of the model in, in the sense that we penalize, e.g., the term $W_{-}\Phi_{22}W_{-}^{\top}$ instead of a term $W_{-}^{\top}Q_{w}W_{-}$. In some cases, these two different noise models are actually equivalent. For example, if $\Phi_{11} > 0$ and $\Phi_{12} = 0$ then can be written via a Schur complement argument as

In turn, this is equivalent to ${{- \Phi_{22}^{- 1}} - {W_{-}^{\top}\Phi_{11}^{- 1}W_{-}}} \geqslant 0$, which is of the same form as.

### Remark 2

In some cases, we may know a priori that the noise $\mathbf{w}$ does not directly affect the entire state-space, but is contained in a subspace. This prior knowledge can be captured by the noise model in Assumption 1. Indeed, $W_{-}$ is of the form $W_{-} = {E{\hat{W}}_{-}}$ for some ${\hat{W}}_{-} \in {\mathbb{R}}^{r \times T}$ satisfying

Thus, the conclusion is that we can incorporate the knowledge that $W_{-} \in {{im}E}$ by appropriate choices of the $\Phi$-matrices in. Showing the above claim is straightforward: note that the "only if" statement follows by pre- and post-multiplication with $E$ and $E^{\top}$, respectively. The "if" part follows by noting that $x \in {\ker E^{\top}}$ implies ${x^{\top}W_{-}{\hat{\Phi}}_{22}W_{-}^{\top}x} \geqslant 0$, thus ${W_{-}^{\top}x} = 0$. Hence, ${\ker E^{\top}} \subseteq {\ker W_{-}^{\top}}$, equivalently, ${{im}W_{-}} \subseteq {{im}E}$.

### II-B Problem formulation

We will follow the general framework for data-driven analysis and control in. To this end, we define the set of all systems $(A,B)$ explaining the data $(U_{-},X)$, i.e., all $(A,B)$ satisfying

for some $W_{-}$ satisfying. We denote this set by $\Sigma$:

We can only guarantee that a state feedback ${\mathbf{u}} = {K{\mathbf{x}}}$ stabilizes the true system $(A_{s},B_{s})$ if it stabilizes *all* systems in $\Sigma$. This motivates the following definition of *informative* data. Loosely speaking, data are called informative if they enable the design of a controller that stabilizes all systems in $\Sigma$ (and thus, the unknown $(A_{s},B_{s})$).

### Definition 3

Assume that $(U_{-},X)$ satisfies for some $W_{-}$ satisfying Assumption 1. The data $(U_{-},X)$ are called *informative for quadratic stabilization* if there exists a feedback gain $K$ and a matrix $P = P^{\top} > 0$ such that

for all ${(A,B)} \in \Sigma$.

Note that in particular, we are interested in *quadratic stabilization* and we ask for a *common* Lyapunov matrix $P$ for all ${(A,B)} \in \Sigma$. We will not treat $(A,B)$-dependent Lyapunov matrices in this paper, but consider this case for future work instead.

Definition 3 leads to two natural problems. First, we are interested in the question under which conditions the data are informative. We formalize this in the following problem.

### Problem 1 (Informativity)

Assume that $(U_{-},X)$ satisfies for some $W_{-}$ satisfying Assumption 1. Find necessary and sufficient conditions under which the data $(U_{-},X)$ are informative for quadratic stabilization.

The second problem is a design issue: we are interested in procedures to come up with a feedback that stabilizes all systems in $\Sigma$.

### Problem 2 (Control design)

Assume that $(U_{-},X)$ satisfies for some $W_{-}$ satisfying Assumption 1. If the data $(U_{-},X)$ are informative for quadratic stabilization, find a stabilizing feedback gain $K$ such that is satisfied for all ${(A,B)} \in \Sigma$.

In addition to data-driven stabilization, we are also interested in including performance specifications. Natural extensions to Problems 1. ‣ II-B Problem formulation ‣ II The problem of data-driven stabilization ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") and 2. ‣ II-B Problem formulation ‣ II The problem of data-driven stabilization ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") will be discussed in Section V.

### II-C Our approach

In what follows, we will outline our strategy for solving Problems 1. ‣ II-B Problem formulation ‣ II The problem of data-driven stabilization ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") and 2. ‣ II-B Problem formulation ‣ II The problem of data-driven stabilization ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma"). Let ${(A,B)} \in \Sigma$ and rewrite as

Recall that by Assumption 1, we have

By substitution of, this yields

This shows that $A$ and $B$ satisfy a *quadratic matrix inequality* (QMI) of the form ^22^2We note that quadratic uncertainty descriptions have also arisen in the papers studying data-driven control under the assumption that $\mathbf{w}$ is a normally distributed process noise.. In fact, the set $\Sigma$ of all systems explaining the data can be equivalently characterized in terms of, as asserted in the following lemma.

### Lemma 4

We have that $\Sigma = \left\{ {(A,B)}\mid{()\text{~is satisfied}} \right\}$.

### Proof

Suppose that ${(A,B)} \in \Sigma$. Then is satisfied for some $W_{-}$ satisfying. This means that holds. As such

To prove the reverse inclusion, let $(A,B)$ be such that is satisfied. Define $W_{-}:={X_{+} - {AX_{-}} - {BU_{-}}}$. By, $W_{-}$ satisfies the assumption. Since holds for $(A,B)$ by construction, we conclude that ${(A,B)} \in \Sigma$. ∎

By Lemma 4 the set $\Sigma$ of systems explaining the data is characterized by a quadratic matrix inequality in $(A,B)$. Next, we turn our attention to the design condition. Suppose that we fix^33^3We make this hypothesis purely to explain the ideas behind our approach. In fact, in Section IV we show how $P$ and $K$ can be computed from data. a Lyapunov matrix $P = P^{\top} > 0$ and a feedback gain $K$. Note that the inequality is equivalent to

which is yet another quadratic matrix inequality in $A$ and $B$. Therefore, Problem 1. ‣ II-B Problem formulation ‣ II The problem of data-driven stabilization ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") essentially boils down to understanding under which conditions the quadratic matrix inequality holds for all $(A,B)$ satisfying the quadratic matrix inequality. Data-driven stabilization thus naturally leads to the following fundamental question:

The familiar reader will immediately recognize the similarity between the above question and the statement of the so-called *S-lemma*. In fact, the S-lemma provides conditions under which the non-negativity of one quadratic function implies that of another one. This motivates the following section, in which we generalize the S-lemma to matrix variables.

## The matrix-valued S-lemma

In this section we present a new S-lemma with matrix variables. Before we do so, we provide a brief recap on the classical S-lemma.

### III-A Recap of the classical S-lemma

A function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is called *quadratic* if it can be written in the form

for some $M_{11} \in {\mathbb{R}}$, $M_{12} \in {\mathbb{R}}^{1 \times n}$ and $M_{22} = M_{22}^{\top} \in {\mathbb{R}}^{n \times n}$. A homogeneous quadratic function of the form ${f{(x)}} = {x^{\top}M_{22}x}$ is called a *quadratic form*. The following theorem describes the celebrated S-lemma, proven by Yakubovich in, see also \[2, Thm. 2.2\].

### Theorem 5 (S-lemma)

Let ${f,g}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ be quadratic functions. Suppose that there exists $\overline{x} \in {\mathbb{R}}^{n}$ such that ${g{(\overline{x})}} > 0$. Then ${f{(x)}} \geqslant 0$ for all $x \in {\mathbb{R}}^{n}$ such that ${g{(x)}} \geqslant 0$ if and only if there exists a scalar $\alpha \geqslant 0$ such that

We note that the functions $f$ and $g$ are not assumed to be convex. As such, it appears to be difficult to check the condition ${f{(x)}} \geqslant 0$ for all $x \in {\mathbb{R}}^{n}$ satisfying ${g{(x)}} \geqslant 0$. The importance of the S-lemma lies in the fact that the characterization (13. ‣ III-A Recap of the classical S-lemma ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) of this condition is equivalent to a *linear matrix inequality*

in the scalar variable $\alpha \geqslant 0$. Here the matrices $N_{11} \in {\mathbb{R}}$, $N_{12} \in {\mathbb{R}}^{1 \times n}$ and $N_{22} \in {\mathbb{R}}^{n \times n}$ define the quadratic function $g$ analogous to.

The scalar $\alpha$ is called a *multiplier* and the assumption ${g{(\overline{x})}} > 0$ for some $\overline{x} \in {\mathbb{R}}^{n}$ is often referred to as the *Slater condition*. This assumption is necessary in the sense that Theorem 5. ‣ III-A Recap of the classical S-lemma ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") is false without it. To show this by means of an example, one can take, e.g., ${f{(x)}} = {x^{\top}Ax}$ and ${g{(x)}} = {- {x^{\top}Bx}}$ with $A$ and $B$ as in the example of \[57, Page 4476\]. A version of the S-lemma where $g$ satisfies a strict inequality has been presented in \[2, Thm. 7.8\]. We will reformulate the result in the following theorem.

### Theorem 6 (Strict S-lemma)

Let ${f,g}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ be quadratic forms. Suppose that there exists an $\overline{x} \in {\mathbb{R}}^{n}$ such that ${g{(\overline{x})}} > 0$. Then ${f{(x)}} \geqslant 0$ for all $x \in {\mathbb{R}}^{n}$ such that ${g{(x)}} > 0$ if and only if there exists a scalar $\alpha \geqslant 0$ such that

Note that Theorem 6. ‣ III-A Recap of the classical S-lemma ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") is stated with two multipliers in \[2, Thm. 7.8\]. However, the inclusion of the Slater condition allows us to state Theorem 6. ‣ III-A Recap of the classical S-lemma ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") with a single multiplier $\alpha$.

### III-B S-lemma with matrix variables

Next, we aim at generalizing Theorems 5. ‣ III-A Recap of the classical S-lemma ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") and 6. ‣ III-A Recap of the classical S-lemma ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") to quadratic functions of the form

where $X \in {\mathbb{R}}^{n \times k}$ is a *matrix variable*, and the partitioned matrices ${M,N} \in {\mathbb{R}}^{{({k + n})} \times {({k + n})}}$ are real and symmetric. As our first step, the following theorem provides an S-lemma for homogeneous quadratic functions of the form $X^{\top}MX$ and $X^{\top}NX$. Naturally, instead of the non-negativity of functions in the classical S-lemma, we now consider the positive (semi)definiteness of quadratic functions of matrix variables.

### Theorem 7 (Homogeneous matrix S-lemma)

Let ${M,N} \in {\mathbb{R}}^{n \times n}$ be symmetric matrices and assume that ${{\overline{X}}^{\top}N\overline{X}} > 0$ for some $\overline{X} \in {\mathbb{R}}^{n \times k}$. The following statements are equivalent:

${X^{\top}MX} \geqslant 0$ for all $X \in {\mathbb{R}}^{n \times k}$ such that ${X^{\top}NX} \geqslant 0$.

${X^{\top}MX} \geqslant 0$ for all $X \in {\mathbb{R}}^{n \times k}$ such that ${X^{\top}NX} > 0$.

There exists a scalar $\alpha \geqslant 0$ such that ${M - {\alphaN}} \geqslant 0$.

### Remark 8

The assumption on the existence of $\overline{X}$ such that ${{\overline{X}}^{\top}N\overline{X}} > 0$ is a natural generalization of the Slater condition in Theorems 5. ‣ III-A Recap of the classical S-lemma ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") and 6. ‣ III-A Recap of the classical S-lemma ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma"). The assumption is again necessary in the sense that Theorem 7. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") is false without it. Nonetheless, it can be shown that the assumption can be weakened if one is interested only in the equivalence of (i. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) and (iii. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")). In fact, one can show using similar arguments as in the proof of Theorem 7. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") that (i. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) $\Leftrightarrow$ (iii. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) under the assumption that ${\exists\overline{x}} \in {\mathbb{R}}^{n}$ such that ${{\overline{x}}^{\top}N\overline{x}} > 0$, i.e., under the "standard" Slater condition.

### Proof of Theorem 7. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")

It is clear that (i. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) $\Longrightarrow$ (ii. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) and (iii. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) $\Longrightarrow$ (i. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")). As such, it suffices to prove the implication (ii. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) $\Longrightarrow$ (iii. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")). To this end, suppose that (ii. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) holds. Let $x \in {\mathbb{R}}^{n}$ be such that ${x^{\top}Nx} > 0$. We want to prove that ${x^{\top}Mx} \geqslant 0$ so that we can apply Theorem 6. ‣ III-A Recap of the classical S-lemma ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma"). Choose a vector $v \in {\mathbb{R}}^{k}$ such that $\left. \parallel v\parallel \right. = 1$. Next, we define the matrix $X \in {\mathbb{R}}^{n \times k}$ as $X:={{\epsilon\overline{X}} + {xv^{\top}}}$ for $\epsilon \neq 0$. Clearly, $X^{\top}NX$ is equal to

We claim that $X^{\top}NX$ is positive definite for $\epsilon$ sufficiently small. To prove this claim, first suppose that $y \in {\mathbb{R}}^{k}$ is nonzero and ${v^{\top}y} = 0$. Then we obtain

Secondly, suppose that $y \in {\mathbb{R}}^{k}$ is nonzero and $v^{\top}y =:\beta \neq 0$. Then $y^{\top}X^{\top}NXy$ is equal to

which is positive for $\epsilon$ sufficiently small since $\beta \neq 0$ and ${x^{\top}Nx} > 0$. We conclude that ${X^{\top}NX} > 0$ for $\epsilon$ sufficiently small. Now, by (ii. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) we conclude that ${X^{\top}MX} \geqslant 0$. Multiplication of the latter inequality from left by $v^{\top}$ and right by $v$ yields the inequality

This implies that ${x^{\top}Mx} \geqslant 0$. Indeed, if ${x^{\top}Mx} < 0$ then there exists a sufficiently small $\epsilon \neq 0$ such that

which contradicts. To conclude, we have shown that ${x^{\top}Mx} \geqslant 0$ for all $x \in {\mathbb{R}}^{n}$ such that ${x^{\top}Nx} > 0$. By Theorem 6. ‣ III-A Recap of the classical S-lemma ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma"), the condition (iii. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) is satisfied. This proves the theorem. ∎

Next, we build on Theorem 7. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") by introducing a general (inhomogeneous) S-lemma with matrix variables. The following theorem is one of the main results of this section.

### Theorem 9 (Matrix S-lemma)

Let ${M,N} \in {\mathbb{R}}^{{({k + n})} \times {({k + n})}}$ be symmetric matrices and assume that there exists some matrix $\overline{Z} \in {\mathbb{R}}^{n \times k}$ such that

Then the following statements are equivalent:

\end{bmatrix}^{\top}M\begin{bmatrix}
\end{bmatrix}} \geqslant {0{\forall Z}} \in {{\mathbb{R}}^{n \times k}\text{~with}\begin{bmatrix}
\end{bmatrix}^{\top}N\begin{bmatrix}
\end{bmatrix}} \geqslant 0}.$

\end{bmatrix}^{\top}M\begin{bmatrix}
\end{bmatrix}} \geqslant {0{\forall Z}} \in {{\mathbb{R}}^{n \times k}\text{~with}\begin{bmatrix}
\end{bmatrix}^{\top}N\begin{bmatrix}

There exists a scalar $\alpha \geqslant 0$ such that ${M - {\alphaN}} \geqslant 0$.

Note that for $k = 1$, the assumption (16. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) reduces to the standard Slater condition. In this case, Theorem 9. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") recovers Theorems 5. ‣ III-A Recap of the classical S-lemma ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") and 6. ‣ III-A Recap of the classical S-lemma ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") in the following sense: the equivalence of (I. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) and (III. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) is the statement of Theorem 5. ‣ III-A Recap of the classical S-lemma ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma"). The equivalence of (II. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) and (III. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) generalizes Theorem 6. ‣ III-A Recap of the classical S-lemma ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") for quadratic forms to general quadratic functions.

### Proof of Theorem 9. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")

Clearly, (I. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) $\Longrightarrow$ (II. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) and (III. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) $\Longrightarrow$ (I. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")). Thus, it suffices to prove that (II. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) $\Longrightarrow$ (III. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")). Our strategy will be to show that (II. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) implies statement (ii. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) of Theorem 7. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma"). To this end, suppose that (II. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) holds and let $X \in {\mathbb{R}}^{{({k + n})} \times k}$ be such that ${X^{\top}NX} > 0$. Partition $X$ as

where $X_{1} \in {\mathbb{R}}^{k \times k}$ and $X_{2} \in {\mathbb{R}}^{n \times k}$. Clearly, for all sufficiently small $\epsilon > 0$ we have

Also note that $X_{1} + {\epsilonI}$ is nonsingular for all sufficiently small $\epsilon > 0$. This implies that

By (II. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")), we have

for all $\epsilon > 0$ sufficiently small. By taking the limit $\epsilon \downarrow 0$ we conclude that ${X^{\top}MX} \geqslant 0$. Therefore, statement (ii. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) (equivalently, statement (iii. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma"))) of Theorem 7. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") is satisfied. This means that (III. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) holds, which proves the theorem. ∎

As a special case of Theorem 9. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") we recover Theorem 3.3 of.

### Corollary 10

The quadratic matrix inequality ${M_{11} + {M_{12}Z} + {Z^{\top}M_{12}^{\top}} + {Z^{\top}M_{22}Z}} \geqslant 0$ holds for all $Z \in {\mathbb{R}}^{n \times k}$ satisfying ${I - {Z^{\top}DZ}} \geqslant 0$ if and only if there exists a scalar $\alpha \geqslant 0$ such that

### Proof

Note that the generalized Slater condition (16. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) is satisfied (one can choose e.g., $\overline{Z} = 0$). Thus, the statement follows from Theorem 9. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma"). ∎

Theorem 9. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") provides a natural generalization of the S-lemma to matrix variables. However, note that for the application that we have in mind, we need a slightly different version of the theorem. Indeed, note that in the data-driven context of Section II, a *strict* inequality must hold for all $(A,B)$ satisfying a non-strict inequality. As such, we need to extend Theorem 9. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") to the case when the inequality involving $M$ is *strict*. Before we do so we introduce the shorthand notation

### Theorem 11 (Strict matrix S-lemma)

Let $M$ and $N$ by symmetric matrices in ${\mathbb{R}}^{{({k + n})} \times {({k + n})}}$. Assume that $\mathcal{S}_{N}$ is bounded and that there exists some matrix $\overline{Z} \in {\mathbb{R}}^{n \times k}$ satisfying (16. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")). Then we have that

if and only if there exists $\alpha \geqslant 0$ such that ${M - {\alphaN}} > 0$.

### Proof

The "if" part is clear, so we focus on proving the "only if" part. Suppose that (17. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) holds. We claim that there exists an $\epsilon > 0$ such that

Suppose that this is not the case. Then there exists a sequence $\{\epsilon_{i}\}$ with $\epsilon_{i}\rightarrow 0$ as $i\rightarrow\infty$ with the property that for each $i$ there exists $Z_{i} \in \mathcal{S}_{N}$ such that

Since $\mathcal{S}_{N}$ is bounded, the sequence $\{ Z_{i}\}$ is bounded. As such, by the Bolzano-Weierstrass theorem, it contains a converging subsequence with limit, say, $Z^{\ast}$. We conclude that

Note that $\mathcal{S}_{N}$ is closed and thus $Z^{\ast} \in \mathcal{S}_{N}$. Since (17. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) holds we arrive at a contradiction. Therefore, we conclude that there exists an $\epsilon > 0$ such that holds. In particular, this implies the existence of $\epsilon > 0$ such that

Now, by Theorem 9. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") there exists an $\alpha \geqslant 0$ such that

We conclude that ${M - {\alphaN}} > 0$ which proves the theorem. ∎

At this point, it is worthwhile to point out a relation between Theorem 11. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") and the literature on LMI relaxations in robust control, see. In fact, we can derive a type of matrix S-lemma from the general theory in. As it turns out, this matrix S-lemma is also a corollary of Theorem 11. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma"). To obtain the result, we substitute $A = 0$, $B = I$, ${W{(x)}} = {- M}$ and

into Equation 1.2 of. Then, we combine the full block S-procedure (c.f.,\[51, page 367\]) with the fact that the LMI relaxation of is exact for a single full block \[51, Thm. 5.3\]. This yields the following result.

### Corollary 12

Let ${M,N} \in {\mathbb{R}}^{{({k + n})} \times {({k + n})}}$ be symmetric matrices, partitioned as in. Assume that $N$ is nonsingular, $N_{11} \geqslant 0$ and $N_{22} < 0$. Then we have that

if and only if there exists $\alpha \geqslant 0$ such that ${M - {\alphaN}} > 0$.

### Proof

We will show that the assumptions on $N$ imply the assumptions of Theorem 11. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma"). First of all, $N_{22} < 0$ implies that $\mathcal{S}_{N}$ is bounded. Secondly, the nonsingularity of $N$ and $N_{22}$ imply that the Schur complement $N_{11} - {N_{12}N_{22}^{- 1}N_{12}^{\top}}$ is nonsingular, and since $N_{11} \geqslant 0$ and $N_{22} < 0$ we have ${N_{11} - {N_{12}N_{22}^{- 1}N_{12}^{\top}}} > 0$. Thus, the matrix $\overline{Z}:={- {N_{22}^{- 1}N_{12}^{\top}}}$ satisfies the Slater condition (16. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")). The result now follows from Theorem 11. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma"). ∎

It turns out that we can even state Theorem 11. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") without the boundedness assumption if some more structure on the matrices $M$ and $N$ is given. In fact, we have the following result.

### Theorem 13

Let ${M,N} \in {\mathbb{R}}^{{({k + n})} \times {({k + n})}}$ be symmetric matrices, partitioned as in. Assume that $M_{22} \leqslant 0$, $N_{22} \leqslant 0$ and ${\ker N_{22}} \subseteq {\ker N_{12}}$. Suppose that there exists some matrix $\overline{Z} \in {\mathbb{R}}^{n \times k}$ satisfying (16. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")). Then we have that

if and only if there exist $\alpha \geqslant 0$ and $\beta > 0$ such that

### Proof

The "if" part is clear so we focus on proving the "only if" statement. Suppose that holds. We will first prove that ${\ker N_{22}} \subseteq {\ker M_{22}}$ and ${\ker N_{22}} \subseteq {\ker M_{12}}$. Let $Z \in \mathcal{S}_{N}$ and $\hat{Z} \in {\mathbb{R}}^{n \times k}$ be such that ${N_{22}\hat{Z}} = 0$. By the hypothesis ${\ker N_{22}} \subseteq {\ker N_{12}}$ we have ${Z + {\gamma\hat{Z}}} \in \mathcal{S}_{N}$ for any $\gamma \in {\mathbb{R}}$. Thus, we obtain

This implies that ${M_{22}\hat{Z}} = 0$. Indeed, recall that $M_{22} \leqslant 0$. Thus, if ${M_{22}\hat{Z}} \neq 0$ then there exists a sufficiently large $\gamma$ such that is violated. Similarly, we conclude that ${M_{12}\hat{Z}} = 0$. Therefore, we have shown that

Subsequently, we claim that there exists a $\beta > 0$ such that

If this claim is not true, then there exists a sequence $\{\beta_{i}\}$ such that $\beta_{i}\rightarrow 0$ and for all $i$ there exists $Z_{i} \in \mathcal{S}_{N}$ such that

{P - {\betaI}} &amp; 0 &amp; 0 &amp; 0 \\
0 &amp; {- P} &amp; {- L^{\top}} &amp; 0 \\
0 &amp; {- L} &amp; 0 &amp; L \\
0 &amp; 0 &amp; L^{\top} &amp; P
\end{bmatrix} - {\alpha\begin{bmatrix}
\end{bmatrix}\begin{bmatrix}
\Phi_{11} &amp; \Phi_{12} \\
\Phi_{12}^{\top} &amp; \Phi_{22}
\end{bmatrix}\begin{bmatrix}
\end{bmatrix}^{\top}}} \geqslant 0}.$$

Define $\mathcal{V}:={\{{Z \in {\mathbb{R}}^{n \times k}}\mid{{N_{22}Z} = 0}\}}$. Write $Z_{i}$ as $Z_{i} = {Z_{i}^{1} + Z_{i}^{2}}$, where $Z_{i}^{1} \in \mathcal{V}^{\perp}$ and $Z_{i}^{2} \in \mathcal{V}$. By the hypothesis ${\ker N_{22}} \subseteq {\ker N_{12}}$ we see that $Z_{i}^{1} \in \mathcal{S}_{N}$. Next, we claim that the sequence $\{ Z_{i}^{1}\}$ is bounded. We will prove this claim by contradiction. Thus, suppose that $\{ Z_{i}^{1}\}$ is unbounded. Clearly, the sequence

is bounded. By the Bolzano-Weierstrass theorem it thus has a convergent subsequence with limit, say $Z_{\ast}$. Note that

By taking the limit along the subsequence as $i\rightarrow\infty$, we get ${Z_{\ast}^{\top}N_{22}Z_{\ast}} \geqslant 0$. Using the fact that $N_{22} \leqslant 0$ we conclude that $Z_{\ast} \in \mathcal{V}$. Since $Z_{i}^{1} \in \mathcal{V}^{\perp}$ for all $i$, also $\frac{Z_{i}^{1}}{\left. \parallel Z_{i}^{1}\parallel \right.} \in \mathcal{V}^{\perp}$ and thus $Z_{\ast} \in \mathcal{V}^{\perp}$. Therefore, we conclude that both $Z_{\ast} \in \mathcal{V}$ and $Z_{\ast} \in \mathcal{V}^{\perp}$, i.e., $Z_{\ast} = 0$. This is a contradiction since $\frac{Z_{i}^{1}}{\left. \parallel Z_{i}^{1}\parallel \right.}$ has norm 1 for all $i$. We conclude that the sequence $\{ Z_{i}^{1}\}$ is bounded. It thus contains a convergent subsequence with limit, say $Z_{\infty}$. Note that $\mathcal{S}_{N}$ is closed and thus $Z_{\infty} \in \mathcal{S}_{N}$. By and we conclude that

for all $i$. We take the limit as $i\rightarrow\infty$, which yields

As $Z_{\infty} \in \mathcal{S}_{N}$ this contradicts. As such, we conclude that there exists $\beta > 0$ such that holds. In particular, there exists $\beta > 0$ such that

The theorem now follows by application of Theorem 9. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma"). ∎

## Data-driven stabilization revisited

In this section, we apply the theory from Section III to data-driven stabilization, i.e., to Problems 1. ‣ II-B Problem formulation ‣ II The problem of data-driven stabilization ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") and 2. ‣ II-B Problem formulation ‣ II The problem of data-driven stabilization ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") defined in Section II. To this end, for given $P = P^{\top} > 0$ and $K$ we define the partitioned matrices

Recall from Section II that data-driven stabilization entails deciding whether holds for all $(A,B)$ satisfying. In terms of the matrices $M$ and $N$ as defined above, we thus have to decide whether

The idea is now to apply Theorem 13. To this end, we have to verify its assumptions. In particular, we will check that $M_{22} \leqslant 0$, $N_{22} \leqslant 0$ and ${\ker N_{22}} \subseteq {\ker N_{12}}$. Note that

because $P > 0$ and $\Phi_{22} < 0$. Since $\Phi_{22}$ is nonsingular, we also see that

and thus ${\ker N_{22}} \subseteq {\ker N_{12}}$. We conclude that the assumptions of Theorem 13 are satisfied. We assume that the generalized Slater condition (16. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) holds for $N$ in (IV). Then, Theorem 13 asserts that holds if and only if there exist scalars $\alpha \geqslant 0$ and $\beta > 0$ such that

From a design point of view, the matrices $P$ and $K$ that appear in $M$ are not given. However, the idea is now to *compute* matrices $P$, $K$ and scalars $\alpha$ and $\beta$ such that holds. In fact, by the above discussion, the data $(U_{-},X)$ are informative for quadratic stabilization *if and only if* there exists an $n \times n$ matrix $P = P^{\top} > 0$, a $K \in {\mathbb{R}}^{m \times n}$ and two scalars $\alpha \geqslant 0$ and $\beta > 0$ such that holds. We note that (in particular, $M$) is not linear in $P$ and $K$. Nonetheless, by a rather standard change of variables and a Schur complement argument, we can transform into a linear matrix inequality. We summarize our progress in the following theorem, which is the main result of this section.

### Theorem 14

Assume that the generalized Slater condition (16. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) holds for $N$ in (IV) and some $\overline{Z} \in {\mathbb{R}}^{{({n + m})} \times n}$. Then the data $(U_{-},X)$ are informative for quadratic stabilization if and only if there exists an $n \times n$ matrix $P = P^{\top} > 0$, an $L \in {\mathbb{R}}^{m \times n}$ and scalars $\alpha \geqslant 0$ and $\beta > 0$ satisfying (FS).

Moreover, if $P$ and $L$ satisfy (FS) then $K:={LP^{- 1}}$ is a stabilizing feedback gain for all ${(A,B)} \in \Sigma$.

### Proof

To prove the "if" statement, suppose that there exist $P$, $L$, $\alpha$ and $\beta$ satisfying (FS). Define $K:={LP^{- 1}}$. By computing the Schur complement of (FS) with respect to its fourth diagonal block, we obtain. As such, holds. We conclude that the data $(U_{-},X)$ are informative for quadratic stabilization and $K = {LP^{- 1}}$ is indeed a stabilizing controller for all ${(A,B)} \in \Sigma$.

Conversely, to prove the "only if" statement, suppose that the data $(U_{-},X)$ are informative for quadratic stabilization. This means that there exist $P = P^{\top} > 0$ and $K$ such that holds. By Theorem 13 there exist $\alpha \geqslant 0$ and $\beta > 0$ satisfying. Finally, by defining $L:={KP}$ and using a Schur complement argument, we conclude that (FS) is feasible. ∎

Theorem 14 provides a powerful necessary *and* sufficient condition under which quadratically stabilizing controllers can be obtained from noisy data. The assumption (16. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) puts a mild condition on the data matrices appearing in (IV). It is satisfied whenever $N$ has at least $n$ positive eigenvalues, a condition that is simple to verify from given data. So far, this condition was satisfied in all of our numerical experiments, see Section VI for more details^44^4In addition, we remark that even if the generalized Slater condition does not hold, the 'if' statement of Theorem 14 remains true.. Theorem 14 leads to an effective design procedure for obtaining stabilizing controllers directly from data. Indeed, the approach entails solving the linear matrix inequality (FS) for $P,L,\alpha$ and $\beta$ and computing a controller as $K = {LP^{- 1}}$. We now discuss some of the features of our control design procedure.

First of all, we note that the procedure is *non-conservative* since Theorem 14 provides a necessary and sufficient condition for obtaining quadratically stabilizing controllers from data.

We believe that our approach based on the set $\Sigma$ of *open-loop* systems provides a valuable alternative to the data-based closed-loop system parameterizations of \[37, Thm. 2\] and \[39, Thm. 4\]. Indeed, in the case of noisy data, it was recognized that certain linear constraints \[39, Eq. \] defining these closed-loop systems were difficult to incorporate in the control design^55^5In fact, it was mentioned in that involving the condition \[39, Eq. \] in design procedures is still an open problem.. Our design procedure does not suffer from the above problem. In fact, the constraint \[39, Eq. \] is *automatically incorporated* in our control design approach.

The variables $P,L,\alpha$ and $\beta$ are *independent* of the time horizon $T$ of the experiment. In fact, note that $P \in {\mathbb{R}}^{n \times n}$, $L \in {\mathbb{R}}^{m \times n}$ and ${\alpha,\beta} \in {\mathbb{R}}$. Also, the LMI (FS) is of dimension ${({{3n} + m})} \times {({{3n} + m})}$ and thus independent of $T$. As such, our approach fundamentally differs from the design methods in where certain decision variables have dimension $T \times n$, c.f. \[37, Thm. 6\] and \[39, Cor. 6\]. We believe that our $T$-independent design method will play a crucial role in control design from larger data sets. We note that the collection of big data sets is often unavoidable, for example because the signal-to-noise ratio is small, or because the data-generating system is large-scale.

### Remark 15

We note that under the extra assumption

it is possible to prove a variant Theorem 14 in which the non-strict inequality is replaced by a strict inequality, and the term $- {\betaI}$ is removed. This can be done by invoking Theorem 11. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma"), which is possible since implies that the set $\Sigma$ is bounded. The reason is that the coefficient matrix $N_{22}$ defining the quadratic term in is negative definite if holds.

Here we chose to state and prove Theorem 14 in the slightly more general setting without assuming. In the discussion preceding Theorem 14 we have verified the assumptions of Theorem 13 for $M$ and $N$ in (LABEL:Mstab), (IV). In particular, this implies that the subspace inclusions hold and thus ${\ker\begin{bmatrix}
\end{bmatrix}} \subseteq {\ker\begin{bmatrix}
\end{bmatrix}}$, equivalently

Therefore, any controller $K$ that stabilizes the systems in $\Sigma$ is necessarily of the form. This generalizes \[3, Lem. 15\] to the case of noisy data.

## Inclusion of performance specifications

In this section we extend our data-driven stabilization result by including different performance specifications. In particular, we will treat the $\mathcal{H}_{2}$ and $\mathcal{H}_{\infty}$ control problems, thereby illustrating the general applicability of the theory in Section III.

### V-A $\mathcal{H}_{2}$ control

As before, consider the the unknown system. We associate to a performance output

where ${\mathbf{z}} \in {\mathbb{R}}^{p}$, and $C$ and $D$ are known matrices that specify the performance. For any ${(A,B)} \in \Sigma$ explaining the data, the feedback law ${\mathbf{u}} = {K{\mathbf{x}}}$ yields the closed-loop system

The transfer matrix from $\mathbf{w}$ to $\mathbf{z}$ of is given by

and its $\mathcal{H}_{2}$ norm is denoted by $\left. \parallel{G{(z)}}\parallel \right._{\mathcal{H}_{2}}$. Let $\gamma > 0$. It is well-known that $A + {BK}$ is stable and $\left. \parallel{G{(z)}}\parallel \right._{\mathcal{H}_{2}} < \gamma$ if and only if there exists a matrix $P = P^{\top} > 0$ such that

where $tr$ denotes trace. The data-driven $\mathcal{H}_{2}$ problem entails the computation of a feedback gain $K$ from data such that $\left. \parallel{G{(z)}}\parallel \right._{\mathcal{H}_{2}} < \gamma$ *for all* ${(A,B)} \in \Sigma$. Similar to our results for quadratic stabilization, we restrict the attention to a matrix $P$ that is common for all $(A,B)$. This leads to the following natural definition.

### Definition 16

Assume that $(U_{-},X)$ satisfies for some $W_{-}$ satisfying Assumption 1. The data $(U_{-},X)$ are *informative for $\mathcal{H}_{2}$ control* with performance $\gamma$ if there exist matrices $P = P^{\top} > 0$ and $K$ such that holds for all ${(A,B)} \in \Sigma$.

With the theory of Section III in place, characterizing informativity for $\mathcal{H}_{2}$ control essentially boils down to massaging the inequalities such that they are amenable to design. To this end, note that the first inequality of is equivalent to

where we defined $A_{Y,L}:={{AY} + {BL}}$ and $C_{Y,L}:={{CY} + {DL}}$ with $Y:=P^{- 1}$ and $L:={KY}$. Using a Schur complement argument, this is equivalent to

Now, holds if and only if

Note that is independent of $A$ and $B$. In turn, we can write as

Note that the inequality is of a form where $A$ and $B$ appear on the left and their transposes appear on the right, analogous to. As such, we are in a position to apply Theorem 13. In fact, we derive the following theorem.

### Theorem 17

Assume that the generalized Slater condition (16. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) holds for $N$ in (IV) and some $\overline{Z} \in {\mathbb{R}}^{{({n + m})} \times n}$. Then the data $(U_{-},X)$ are informative for $\mathcal{H}_{2}$ control with performance $\gamma$ if and only if there exist matrices $Y = Y^{\top} > 0$, $Z = Z^{\top}$ and $L$, and scalars $\alpha \geqslant 0$ and $\beta > 0$ satisfying ($\mathcal{H}_{2}$).

Moreover, if $Y$ and $L$ satisfy ($\mathcal{H}_{2}$) then $K:={LY^{- 1}}$ is such that $A + {BK}$ is stable and $\left. \parallel{G{(z)}}\parallel \right._{\mathcal{H}_{2}} < \gamma$ for all ${(A,B)} \in \Sigma$.

{Y - {\betaI}} &amp; 0 &amp; 0 &amp; 0 &amp; 0 \\
0 &amp; 0 &amp; 0 &amp; Y &amp; 0 \\
0 &amp; 0 &amp; 0 &amp; L &amp; 0 \\
0 &amp; Y &amp; L^{\top} &amp; Y &amp; C_{Y,L}^{\top} \\
0 &amp; 0 &amp; 0 &amp; C_{Y,L} &amp; I
\end{bmatrix} - {\alpha\begin{bmatrix}
\end{bmatrix}\begin{bmatrix}
\Phi_{11} &amp; \Phi_{12} \\
\Phi_{12}^{\top} &amp; \Phi_{22}
\end{bmatrix}\begin{bmatrix}
\end{bmatrix}^{\top}}} \geqslant 0},{\begin{bmatrix}
\end{bmatrix} &gt; {0,\begin{array}{r}
\end{bmatrix} \geqslant 0},} \\

### Proof

Suppose that ($\mathcal{H}_{2}$) is feasible and define $P:=Y^{- 1}$ and $K:={LP}$. The last two inequalities of ($\mathcal{H}_{2}$) imply that ${{tr}P} < \gamma^{2}$. We now compute the Schur complement of the first LMI in ($\mathcal{H}_{2}$) with respect to the diagonal block

We thereby make use of the fact that this block is nonsingular by the second LMI of ($\mathcal{H}_{2}$). The computation of the Schur complement results in

where $M$ is defined in and $N$ is defined in (IV). We thus conclude that the inequality is satisfied for all ${(A,B)} \in \Sigma$. As such, holds for all ${(A,B)} \in \Sigma$. Note that holds by the second LMI of ($\mathcal{H}_{2}$). Therefore, we conclude that holds for all ${(A,B)} \in \Sigma$. In other words, the data $(U_{-},X)$ are informative for $\mathcal{H}_{2}$ control with performance $\gamma$, and $K = {LY^{- 1}}$ is a suitable controller.

Conversely, suppose that the data $(U_{-},X)$ are informative for $\mathcal{H}_{2}$ control with performance $\gamma$. Then there exist matrices $P = P^{\top} > 0$ and $K$ such that holds for all ${(A,B)} \in \Sigma$. Define $Y:=P^{- 1}$, $L:={KY}$ and $Z:=P$. Clearly, the last two inequalities of ($\mathcal{H}_{2}$) are satisfied by definition of $Z$. In addition, we know that and hold for all ${(A,B)} \in \Sigma$. By, the second LMI of ($\mathcal{H}_{2}$) is satisfied. To prove that the first LMI of ($\mathcal{H}_{2}$) also holds, we want to apply Theorem 13. Note that we have already verified the assumptions of this theorem for the matrix $N$ in (IV), see the discussion preceding Theorem 14. In addition, we note that

since ${Y - {C_{Y,L}^{\top}C_{Y,L}}} > 0$. Hence, Theorem 13 is applicable. We conclude that there exist $\alpha \geqslant 0$ and $\beta > 0$ such that holds. Using a Schur complement argument, we see that $Y$, $L$, $\alpha$ and $\beta$ satisfy the first LMI of ($\mathcal{H}_{2}$). Thus, ($\mathcal{H}_{2}$) is feasible which proves the theorem. ∎

### Remark 18

If we know a priori that the noise $\mathbf{w}$ is contained in a subspace, say ${im}E$, then this information can easily be exploited in the $\mathcal{H}_{2}$ controller design. In fact, we only need to replace the LMI involving $Z$ by

We recall that prior knowledge of ${\mathbf{w}} \in {{im}E}$, if available, can also be captured by our noise model, see Remark 2. A natural choice is thus to use $E$ both in the noise model as well as in the LMI ($\mathcal{H}_{2}$). However, we remark that this is not necessary: the noise in the experiment may come from a different subspace than the disturbances that are attenuated by the $\mathcal{H}_{2}$ controller.

### V-B $\mathcal{H}_{\infty}$ control

In this section we will turn our attention to the $\mathcal{H}_{\infty}$ control problem. As before, consider system with performance output. For any ${(A,B)} \in \Sigma$, the feedback ${\mathbf{u}} = {K{\mathbf{x}}}$ yields the system with transfer matrix from $\mathbf{w}$ to $\mathbf{z}$ given by $G{(z)}$. We will denote the $\mathcal{H}_{\infty}$ norm of $G{(z)}$ by $\left. \parallel{G{(z)}}\parallel \right._{\mathcal{H}_{\infty}}$. Let $\gamma > 0$. By \[59, Thm. 4.6.6(iii)\], the matrix $A + {BK}$ is stable and $\left. \parallel{G{(z)}}\parallel \right._{\mathcal{H}_{\infty}} < \gamma$ if and only if there exists a matrix $P = P^{\top} > 0$ such that

where we have defined $A_{K}:={A + {BK}}$ and $C_{K}:={C + {DK}}$. We now have the following definition of informativity for $\mathcal{H}_{\infty}$ control.

### Definition 19

Assume that $(U_{-},X)$ satisfies for some $W_{-}$ satisfying Assumption 1. The data $(U_{-},X)$ are *informative for $\mathcal{H}_{\infty}$ control* with performance $\gamma$ if there exist matrices $P = P^{\top} > 0$ and $K$ such that and hold for all ${(A,B)} \in \Sigma$.

By pre- and postmultiplication of by $P^{- 1}$ we obtain

where the matrices $Y:=P^{- 1}$, $L:={KY}$, $A_{Y,L}:={{AY} + {BL}}$ and $C_{Y,L}:={{CY} + {DL}}$ are defined as in the $\mathcal{H}_{2}$ problem. Note that the first of these inequalities can again be written in the -by now familiar- form

where $Z:={({Y - {\frac{1}{\gamma^{2}}I}})}^{- 1}$. We thus have the following theorem.

{Y - {\betaI}} &amp; 0 &amp; 0 &amp; 0 &amp; C_{Y,L}^{\top} \\
0 &amp; 0 &amp; 0 &amp; Y &amp; 0 \\
0 &amp; 0 &amp; 0 &amp; L &amp; 0 \\
0 &amp; Y &amp; L^{\top} &amp; {Y - {\frac{1}{\gamma^{2}}I}} &amp; 0 \\
C_{Y,L} &amp; 0 &amp; 0 &amp; 0 &amp; I
\end{bmatrix} - {\alpha\begin{bmatrix}
\end{bmatrix}\begin{bmatrix}
\Phi_{11} &amp; \Phi_{12} \\
\Phi_{12}^{\top} &amp; \Phi_{22}
\end{bmatrix}\begin{bmatrix}
\end{bmatrix}^{\top}}} \geqslant 0},{{Y - {\frac{1}{\gamma^{2}}I}} &gt; 0}}.$$

### Theorem 20

Assume that the generalized Slater condition (16. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) holds for $N$ in (IV) and some $\overline{Z} \in {\mathbb{R}}^{{({n + m})} \times n}$. Then the data $(U_{-},X)$ are informative for $\mathcal{H}_{\infty}$ control with performance $\gamma$ if and only if there exist matrices $Y = Y^{\top} > 0$ and $L$, and scalars $\alpha \geqslant 0$ and $\beta > 0$ satisfying ($\mathcal{H}_{\infty}$).

Moreover, if $Y$ and $L$ satisfy ($\mathcal{H}_{\infty}$) then $K:={LY^{- 1}}$ is such that $A + {BK}$ is stable and $\left. \parallel{G{(z)}}\parallel \right._{\mathcal{H}_{\infty}} < \gamma$ for all ${(A,B)} \in \Sigma$.

The proof of Theorem 20 is based on Theorem 13. It follows similar steps as the proof of Theorem 17, and is therefore not reported here.

## Examples

In this section we illustrate our theoretical results by examples and numerical simulations.

### VI-A Stabilization using bounds on the noise samples

Consider an unstable system of the form with $A_{s}$ and $B_{s}$ given by

In this example, we assume that the noise samples $w{(t)}$ are bounded in norm as $\left. \parallel{w{(t)}}\parallel \right._{2}^{2} \leqslant \epsilon$ for all $t$. As explained in Section II, we can capture this prior knowledge using the noise model with $\Phi_{11} = {T\epsilonI}$, $\Phi_{12} = 0$ and $\Phi_{22} - I$. We pick a time horizon of $T = 20$ and draw the entries of the inputs and initial state randomly from a Gaussian distribution with zero mean and unit variance. The noise samples are drawn uniformly at random from the ball $\{{w \in {\mathbb{R}}^{3}}\mid{\left. \parallel w\parallel \right._{2}^{2} \leqslant \epsilon}\}$. We aim at constructing stabilizing controllers from the input/state data for various values of $\epsilon$. In particular, we investigate six different noise levels: $\epsilon \in {\{ 0.5,1,1.5,2,2.2,2.4\}}$. For each noise level, we generate $100$ data sets using the method described above. We check the generalized Slater condition (16. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) by verifying that $N$ in (IV) has $3$ positive eigenvalues; this turns out to be true for all $600$ data sets. For each noise level, we record the percentage of data sets from which a stabilizing controller was found for $(A_{s},B_{s})$ using the formulation (FS). We display the results in the following table.

For $\epsilon = 0.5$ we find a stabilizing controller in all $100$ cases. When the noise level increases, the percentage of data sets for which the LMI (FS) is feasible decreases. The interpretation is that by increasing the noise we enlarge the set of explaining systems $\Sigma$. It thus becomes harder to simultaneously stabilize the systems in $\Sigma$. Nonetheless, even for the larger noise level of $\epsilon = 2.4$ we find a stabilizing controller in $73$ out of the $100$ data sets.

### VI-B $\mathcal{H}_{2}$ control of a fighter aircraft

We consider a state-space model of a fighter aircraft \[59, Ex. 10.1.2\]. In particular, we discretize the model of using a sampling time of $0.01$, which results in the (unstable) system of the form with $A_{s}$ and $B_{s}$ given by

respectively. We consider the performance output as in with

and $D = 0$. First, we look for the smallest $\gamma$ such that is feasible for $(A_{s},B_{s})$. This minimum value of $\gamma$ is $1.000$ and can be regarded as a benchmark: no data-driven method can perform better than the model-based solution using full knowledge of $(A_{s},B_{s})$.

Of course, our goal is not to use the knowledge of $(A_{s},B_{s})$ but to seek a data-driven solution instead. Therefore, we collect $T = 750$ input and state samples of. The entries of the inputs and initial state were drawn randomly from a Gaussian distribution with zero mean and unit variance. Also the noise samples were drawn randomly from a Gaussian distribution, with zero mean and variance $\sigma^{2}$ with $\sigma = 0.005$. In this example, we assume knowledge of a bound on the energy of the noise as

We verified that this bound is satisfied for the generated noise sequence. In addition, we verified that the matrix $N$ in (IV) has $6$ positive eigenvalues, thus the generalized Slater condition (16. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) holds.

Next, we want to compute an $\mathcal{H}_{2}$ controller for the unknown system using the generated data. We do so by minimizing $\gamma$ subject to ($\mathcal{H}_{2}$). This is a semidefinite program that we solve in Matlab, using Yalmip with Mosek as an LMI solver. The obtained controller $K$ stabilizes the original system $(A_{s},B_{s})$. In addition, the system, in feedback with $K$, has an $\mathcal{H}_{2}$ norm of $\gamma_{s}$ where $\gamma_{s}^{2} = 1.007$. We note that this is almost identical to the smallest possible $\mathcal{H}_{2}$ norm of $1.000$.

Subsequently, we repeat the above experiment using only a *part* of our data set. In particular, we compute an $\mathcal{H}_{2}$ controller via the semidefinite program as before, using only the first $i$ samples of $X_{+},X_{-}$ and $U_{-}$ for $i = {50,100,\ldots,750}$. We display the results in Figure 1.

Figure 1: Achieved ℋ2 performance of the true system in feedback with a data-based controller (blue) and the optimal (model-based) performance of the true system (red).

In each of the cases a stabilizing controller was found from data. However, the performance of these controllers when applied to the true system varies, and is quite poor for $i < 500$. Starting from $i = 500$ and onward, the performance is close to the optimal performance of the true system.

Next, we investigate what happens when we increase the variance $\sigma^{2}$ of the noise. First, we take $\sigma = 0.05$. We again generate $750$ data samples, and assume the same bound on the noise. The $\mathcal{H}_{2}$ controller achieves a performance of $\gamma_{s}^{2} = 1.146$ when interconnected to the true system. Increasing the variance of the noise has the effect that the set $\Sigma$ of explaining systems becomes larger. As such, it is more difficult to control all systems in $\Sigma$ resulting in a slightly larger $\gamma_{s}$. This behavior becomes even more apparent when increasing the variance of the noise to $\sigma = 0.5$. In this case we obtain a controller that yields a performance of $\gamma_{s}^{2} = 3.579$. Increasing $\sigma$ even more to $\sigma = 1$ results in infeasibility of the LMI's ($\mathcal{H}_{2}$) for any $\gamma$; the set of explaining systems has become too large for a quadratically stabilizing controller to exist.

We remark that the size of the set $\Sigma$ does not only depend on the variance of the noise, but also on the available bound on the noise. Throughout this example, we have used the bound. However, if we reconsider the case of $\sigma = 0.5$ with the tighter bound ${W_{-}W_{-}^{\top}} \leqslant {1.22T\sigma^{2}I}$ (which is also satisfied in this example) we obtain a controller with better performance $\gamma_{s}^{2} = 2.706$. This illustrates the simple fact that data-driven controllers not only depend on the particular design strategy, but also on the *prior knowledge* on the noise.

We conclude the example with a remark on the dimension of the variables involved in the formulation ($\mathcal{H}_{2}$). The symmetric matrices $Y$ and $Z$ both have $21$ free variables. The matrix $L$ contains $12$ variables, and $\alpha$ and $\beta$ are both scalar variables. Thus, the total number of variables is $56$. The size of the largest LMI in ($\mathcal{H}_{2}$) is $21 \times 21$. We emphasize that our approach is based directly on the set $\Sigma$ of open-loop systems and avoids the parameterization of closed-loop systems, as employed in. Such parameterizations involve decision variables of dimension $T \times n$, which would result in at least $4500$ variables in this example.

### VI-C Comparison with related results

As we have mentioned before, one of the advantages of our approach compared to existing work is that our LMI condition provides necessary and sufficient conditions for data-driven quadratic stabilization. The purpose of this example is to demonstrate that our results can thus lead to stabilizing controllers even in situations where the results from cannot.

Consider the system, where $A_{s} = 1$ and $B_{s} = 1$. Suppose that $T = 3$ and the noise matrix is given by

We collect the data samples

Throughout the example, we assume that we have access to the noise bound ${W_{-}W_{-}^{\top}} \leqslant 1$. Note that this bound is indeed satisfied, and that it can be captured using Assumption 1 by the choices $\Phi_{11} = 1$, $\Phi_{12} = 0$ and $\Phi_{22} = {- I}$. We also note that by Remark 1, this noise bound can be captured by \[39, Asm. 3\] with the choices $Q_{w} = {- 1}$, $S_{w} = 0$ and $R_{w} = I$. Finally, we note that the noise bound can be captured by \[37, Asm. 5\] with the choice $\gamma = 1$. As such, we can compare the design methods reported in Theorem 14 of this paper with the approaches in \[39, Cor. 6, Rem. 7\] and \[37, Thm. 6\]^66^6We note that studies stabilization in the setting that $\mathbf{w}$ represents a bounded nonlinearity. The interpretation of $\mathbf{w}$, however, is not important for this comparison. In fact, our results (as well as those in ) are applicable to general bounded disturbances, hence also to disturbances resulting from bounded nonlinearities..

We start by applying Theorem 14 to the data in this example. Note that $X_{-} = \begin{bmatrix}
\end{bmatrix}$ and $X_{+} = \begin{bmatrix}
\end{bmatrix}$. It can be easily verified that ${(P,L,\alpha,\beta)} = {(0.9,{- 1.35},1.1,0.18)}$ is a solution to (FS). In addition, the Slater condition is satisfied in this example. As such, we conclude by Theorem 14 that the controller $K = {L/P} = {- 1.5}$ is stabilizing for all ${(A,B)} \in \Sigma$. In particular, we see that the true closed-loop system matrix $- 0.5$ is stable.

We will now investigate the design method of \[37, Thm. 6\]. This approach involves finding a matrix $Q$ and a scalar $\alpha > 0$ such that $X_{-}Q$ is symmetric and

where we recall that $\gamma = 1$ in this example. We will now show that, do not have a solution $(Q,\alpha)$, and thus, the design procedure from \[37, Thm. 6\] cannot find a controller that is guaranteed to stabilize the true system. To see this, note that and $\alpha > 0$ imply $\alpha > {1 + \sqrt{5}}$. We write $Q = \begin{bmatrix}
\end{bmatrix}^{\top}$ and note that by the upper left block of the first matrix in, we have $q_{3} > \alpha$, thus $q_{3} > 1$. Now, by taking the Schur complement of the second matrix in with respect to the upper left block, we obtain $q_{3} > {q_{1}^{2} + q_{2}^{2} + q_{3}^{2}}$. However, this inequality cannot be satisfied since $q_{3} > 1$. As such, we conclude that, do not have a solution.

Next, we turn our attention to the design procedure of \[39, Rem. 7\]. For $S_{w} = 0$, this procedure boils down to finding a solution $(\mathcal{Y},M)$ to

where we recall that $Q_{w} = {- 1}$ and $R_{w} = I$ in this example. We will now show that, do not have a solution $(\mathcal{Y},M)$. To see this, note that implies $M = \begin{bmatrix}
\end{bmatrix}^{\top}$ with ${m_{1},m_{2}} \in {\mathbb{R}}$. The negative definiteness of the submatrix of consisting of the second and third row and column imply $\mathcal{Y} > 1$. Moreover, by inspection of the first and fourth row and column block of we see that ${{- \mathcal{Y}} + {M^{\top}M}} < 0$ and thus, ${{- \mathcal{Y}} + m_{1}^{2} + m_{2}^{2} + \mathcal{Y}^{2}} < 0$. This inequality, however, cannot be satisfied as $\mathcal{Y} > 1$. As such, we see that and do not have a solution $(\mathcal{Y},M)$.

We conclude that Theorem 14 can be successfully applied even in situations in which the design procedures of do not lead to controllers that are guaranteed to stabilize the true system.

## Discussion and conclusions

We have studied the problem of obtaining feedback controllers from noisy data. The essence of our approach has been to formulate data-driven control as the problem of determining when one quadratic matrix inequality implies another one. To get a grip on this fundamental question, we have generalized the classical S-lemma to matrix variables. The implication involving quadratic matrix inequalities is thereby *equivalent* to a linear matrix inequality in a scalar variable. We have established several versions of the matrix S-lemma, for both strict and non-strict inequalities. These matrix S-lemmas are interesting in their own right, and generalize existing S-lemmas as well as a theorem involving quadratic matrix inequalities.

We have followed up by applying our matrix S-lemma to data-driven control. In particular, we have given necessary and sufficient conditions under which stabilizing, $\mathcal{H}_{2}$, and $\mathcal{H}_{\infty}$ controllers can be obtained from noisy data. Our control design revolves around data-guided linear matrix inequalities, which can be solved efficiently using modern LMI solvers. In addition to being non-conservative, an attractive feature of our design procedure is that decision variables are *independent* of the time horizon of the experiment.

So far, we have only applied the matrix S-lemma involving a strict inequality (Thms. 11. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma"), 13) to data-driven control. However, we are convinced that also the matrix S-lemma with *non-strict* inequalities (Thm. 9. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) will find applications, for example, in the verification of dissipativity properties from data.

The noise model that we have employed is flexible, and can describe, e.g., constant disturbances, energy bounded noise and norm bounds on noise samples. If one is only interested in the latter, however, we expect that more specific control techniques are possible. In fact, analogous to, we can write the inequality ${w{(t)}^{\top}w{(t)}} \leqslant \epsilon$ as

In the spirit of the S-procedure, one could thus design a stabilizing controller by computing^77^7This procedure is likely to be conservative, however, since the classical S-lemma is in general conservative for more than two quadratic functions. matrices $P = P^{\top} > 0$ and $K$, and *multiple* non-negative scalars $\alpha_{0},\alpha_{1},\ldots,\alpha_{T - 1}$ such that

with $M$ given by (LABEL:Mstab). We will consider norm bounded noise samples in more detail in future work.

Yet another idea for future work is to extend the current results for state-feedback design to data-driven dynamic output feedback design. Specifically, it would be interesting to see whether the matrix S-lemmas can be applied to obtain dynamic output feedback controllers from a finite set of noisy *input/output* samples.
