<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

From Noisy Data to Feedback Controllers: Nonconservative Design via a Matrix S-Lemma

Topics include Data-driven control, Matrix S-lemma, Noisy data, Linear matrix inequalities, Quadratic stabilization, H2 control, H-infinity control, Robust control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Uses a matrix S-lemma to derive exact, nonconservative LMI conditions for controller synthesis from noisy input-state data. The result is a central technical tool for the informativity framework because it converts sets of data-consistent systems into tractable robust-control inequalities.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a new method to obtain feedback controllers of an unknown dynamical system directly from noisy input/state data. The key ingredient of our design is a new matrix S-lemma that will be proven in this paper. We provide both strict and non-strict versions of this S-lemma, that are of interest in their own right. Thereafter, we will apply these results to data-driven control. In particular, we will derive non-conservative design methods for quadratic stabilization, H_2 and H_inf control, all in terms of data-based linear matrix inequalities. In contrast to previous work, the dimensions of our decision variables are independent of the time horizon of the experiment. Our approach thus enables control design from large data sets.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we study the problem of designing control laws for an unknown dynamical system using noisy data. This general problem exists for a long time, but has seen a renewed surge of interest over the last few years. The problem can be approached via different angles, for example using combined system identification and model-based control, or by computing control laws from data without the intermediate modeling step. We will contribute to the second category of methods, aiming at control design directly from noisy data.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

One of the main challenges in this area is to come up with robust control laws that guarantee stability and performance of the unknown system despite the inherent uncertainty caused by noisy data. Even though there are several recent contributions addressing this issue, there are multiple open questions. In fact, one of the unsolved problems is to come up with *non-conservative* control design strategies using only a finite number of data samples.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We will tackle this problem by providing necessary and sufficient conditions on noisy data under which controllers can be obtained. As a consequence, our ensuing control technique is non-conservative, and also shown to be tractable from a computational point of view. The technical ingredient that enables our design is a new generalization of the classical S-lemma, which will be proven in this paper. We will formulate our control problems using the general data informativity framework as introduced. As such, the results developed in this paper can be seen as a natural extension of those in to noisy data.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Literature on data-driven control", "weight": 1.0} -->

The literature on data-driven control is expanding rapidly. Our account of previous work is therefore not exhaustive, but we note that additional references can be found in the survey. We mention contributions to data-driven optimal control, PID control, predictive control, and nonlinear control. Some of these techniques are iterative in nature: the controller is updated online when new data are presented. Examples of this include policy iteration methods and iterative feedback tuning. Other methods are one-shot in the sense that the controller is constructed offline from a batch of data. We mention, for instance, virtual reference feedback tuning and methods based on Willems' fundamental lemma (see also ). The latter line of work has been quite fruitful, with contributions ranging from output matching and control by interconnection, to data-enabled predictive control and a data-based closed-loop system parameterization. This parameterization has been used for stabilizing and optimal control design using data-based linear matrix inequalities. We also mention the extension studying LQR using noisy data, and the paper for a closed-loop parameterization using noisy data.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Literature on data-driven control", "weight": 1.0} -->

Additional recent research directions include data-driven control of networks and the interplay between data-guided control and model reduction.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Review of the S-lemma", "weight": 1.0} -->

First proven by Yakubovich, the *S-lemma* is a classical result in control theory and optimization. The result revolves around the question when the non-negativity of one quadratic function implies that of another. The crux of the S-lemma is that this seemingly difficult implication is equivalent to the feasibility of a linear matrix inequality (LMI) in a scalar variable, called a *multiplier*. The act of replacing the implication by a linear matrix inequality is often referred to as the *S-procedure*. The S-procedure is more generally applicable in situations where one quadratic inequality is implied by *multiple* quadratic inequalities. In this case, multiple scalar multipliers are used. It is well-known, however, that the S-procedure is conservative in general, although there exist special cases in which losslessness (a là S-lemma) can be shown \[2, Sec. 3\]. A generalized S-lemma involving more general types of multipliers was considered, and was shown to be non-conservative under extra assumptions.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Review of the S-lemma", "weight": 1.0} -->

The classical S-lemma, as well as the contributions mentioned above, all deal with vector variables. However, for reasons that will become clear in Section II, we need a type of S-lemma that is applicable to quadratic functions of *matrix* variables. Such a result has been reported for specific quadratic functions in \[46, Thm. 3.3\]. In the special case that variables are *bounded*, an S-lemma for matrix variables can also be derived by combining the so-called *full block S-procedure* with results from the literature on LMI relaxations. These specific results are, however, less suited for the application of data-driven control that we have in mind. Therefore, in this paper we derive general matrix S-lemmas for both strict and non-strict inequalities. Our matrix S-lemma for non-strict inequalities is a direct generalization of the classical S-lemma. It also recovers the result from as a special case. As a corollary of our matrix S-lemma for a strict inequality, we recover the S-lemma derived from the general theory on LMI relaxations.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Our contributions", "weight": 1.0} -->

The core of our approach is to formulate data-driven control as the problem of deciding whether one quadratic matrix inequality is implied by another one. Our first contribution is to extend the classical S-lemma to quadratic matrix inequalities. Our second contribution is to apply these results to data-driven control. In particular, we come up with design procedures for quadratic stabilization, $\mathcal{H}_{2}$ control and $\mathcal{H}_{\infty}$ control.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Our contributions", "weight": 1.0} -->

Throughout the paper we will assume no statistics on the noise, but we will work with general bounded disturbances. We are thereby inspired by recent papers that formalize the assumption of bounded disturbances in terms of quadratic matrix inequalities. In fact, we will work with an assumption on the noise that is closely related to that of, and is more general than the assumption. In terms of control design, our approach completely differs from the above papers. In fact, instead of working with data-based parameterizations of closed-loop systems, we will work with a representation of all *open-loop* systems explaining the data, akin to the framework of.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Our contributions", "weight": 1.0} -->

We provide robust guarantees on the stability and performance of the unknown data-generating system. The design involves data-guided LMI's that are tractable from a computational point of view and are easy to implement.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Our contributions", "weight": 1.0} -->

By virtue of our matrix S-lemma, the design method is *non-conservative*. This is in contrast with previous LMI formulations in that provide sufficient conditions for controller design.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Our contributions", "weight": 1.0} -->

Last but not least, the variables involved in our method are independent of the time horizon of the experiment. Our approach is thus applicable to large data sets. This is an advantage over closed-loop system parameterizations, that become computationally intractable when applied to big data.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Outline of the paper", "weight": 1.0} -->

In Section II we will formulate the problem. Section III contains our results on the matrix S-lemma. These results are then applied to data-driven stabilization in Section IV, and to data-driven $\mathcal{H}_{2}$ control and $\mathcal{H}_{\infty}$ control in Section V. In Section VI we provide simulation examples. Finally, our conclusions are provided in Section VII.

<!-- chunk {"id": "body-0017", "role": "body", "section": "The problem of data-driven stabilization", "weight": 1.0} -->

Consider the linear time-invariant system

<!-- chunk {"id": "body-0018", "role": "body", "section": "The problem of data-driven stabilization", "weight": 1.0} -->

where ${\mathbf{x}} \in {\mathbb{R}}^{n}$ denotes the state, ${\mathbf{u}} \in {\mathbb{R}}^{m}$ is the input and ${\mathbf{w}} \in {\mathbb{R}}^{n}$ is an unknown noise term. The matrices $A_{s} \in {\mathbb{R}}^{n \times n}$ and $B_{s} \in {\mathbb{R}}^{n \times m}$ denote the unknown state and input matrices. Our goal is to design stabilizing controllers for on the basis of a finite number of measurements of the state and input of the system. To this end, suppose that we measure state and input data on a time interval^11^1All our results are still true for data collected on multiple intervals, see \[3, Ex. 2\] for more details on how to arrange the data matrices in this case., and collect these samples in the matrices

<!-- chunk {"id": "body-0019", "role": "body", "section": "The problem of data-driven stabilization", "weight": 1.0} -->

We emphasize that the system matrices $A_{s}$ and $B_{s}$ as well as the noise term $W_{-}$ are *unknown*, while $X$ and $U_{-}$ are measured. Before we introduce the problem we will explain our assumption on the noise $W_{-}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-A Assumption on the noise", "weight": 1.0} -->

We will formalize our assumption on the noise in terms of a quadratic matrix inequality.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Note that the negative definiteness of $\Phi_{22}$ ensures that the set of noise matrices $W_{-}$ satisfying is bounded. In the special case $\Phi_{12} = 0$ and $\Phi_{22} = {- I}$, reduces to

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The inequality has the interpretation that the energy of $\mathbf{w}$ is bounded on the finite time interval $\lbrack 0,{T - 1}\rbrack$. If $\mathbf{w}$ is a random variable, its *sample covariance matrix* is given by

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

where $J$ is the matrix of ones. Thus, can also capture known bounds on the sample covariance by the choices $\Phi_{12} = 0$ and $\Phi_{22} = {- {\frac{1}{T - 1}{({I - {\frac{1}{T}J}})}}}$. We emphasize, however, that we do not make any assumptions on the statistics of $\mathbf{w}$ and work with the general bound instead. Note that \[37, Asm. 5\] is a special case of Assumption 1 for the choices $\Phi_{11} = {\gammaX_{+}X_{+}^{\top}}$ with $\gamma > 0$, $\Phi_{12} = 0$ and $\Phi_{22} = {- I}$. We remark that norm bounds on the individual noise samples $w{(t)}$ also give rise to bounds of the form, although this may lead to some conservatism. Indeed, note that $\left.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Note that the noise model in Assumption 1 is the "transposed" of the model, in the sense that we penalize, e.g., the term $W_{-}\Phi_{22}W_{-}^{\top}$ instead of a term $W_{-}^{\top}Q_{w}W_{-}$. In some cases, these two different noise models are actually equivalent. For example, if $\Phi_{11} > 0$ and $\Phi_{12} = 0$ then can be written via a Schur complement argument as

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 2", "weight": 1.0} -->

In some cases, we may know a priori that the noise $\mathbf{w}$ does not directly affect the entire state-space, but is contained in a subspace. This prior knowledge can be captured by the noise model in Assumption 1. Indeed, $W_{-}$ is of the form $W_{-} = {E{\hat{W}}_{-}}$ for some ${\hat{W}}_{-} \in {\mathbb{R}}^{r \times T}$ satisfying

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Thus, the conclusion is that we can incorporate the knowledge that $W_{-} \in {{im}E}$ by appropriate choices of the $\Phi$-matrices. Showing the above claim is straightforward: note that the "only if" statement follows by pre- and post-multiplication with $E$ and $E^{\top}$, respectively. The "if" part follows by noting that $x \in {\ker E^{\top}}$ implies ${x^{\top}W_{-}{\hat{\Phi}}_{22}W_{-}^{\top}x} \geqslant 0$, thus ${W_{-}^{\top}x} = 0$. Hence, ${\ker E^{\top}} \subseteq {\ker W_{-}^{\top}}$, equivalently, ${{im}W_{-}} \subseteq {{im}E}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-B Problem formulation", "weight": 1.0} -->

We will follow the general framework for data-driven analysis and control. To this end, we define the set of all systems $(A,B)$ explaining the data $(U_{-},X)$, i.e., all $(A,B)$ satisfying

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-B Problem formulation", "weight": 1.0} -->

We can only guarantee that a state feedback ${\mathbf{u}} = {K{\mathbf{x}}}$ stabilizes the true system $(A_{s},B_{s})$ if it stabilizes *all* systems in $\Sigma$. This motivates the following definition of *informative* data. Loosely speaking, data are called informative if they enable the design of a controller that stabilizes all systems in $\Sigma$ (and thus, the unknown $(A_{s},B_{s})$).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Problem 1 (Informativity)", "weight": 1.0} -->

Assume that $(U_{-},X)$ satisfies for some $W_{-}$ satisfying Assumption 1. Find necessary and sufficient conditions under which the data $(U_{-},X)$ are informative for quadratic stabilization.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Problem 1 (Informativity)", "weight": 1.0} -->

The second problem is a design issue: we are interested in procedures to come up with a feedback that stabilizes all systems in $\Sigma$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Problem 2 (Control design)", "weight": 1.0} -->

Assume that $(U_{-},X)$ satisfies for some $W_{-}$ satisfying Assumption 1. If the data $(U_{-},X)$ are informative for quadratic stabilization, find a stabilizing feedback gain $K$ such that is satisfied for all ${(A,B)} \in \Sigma$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Problem 2 (Control design)", "weight": 1.0} -->

In addition to data-driven stabilization, we are also interested in including performance specifications. Natural extensions to Problems 1. ‣ II-B Problem formulation ‣ II The problem of data-driven stabilization ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") and 2. ‣ II-B Problem formulation ‣ II The problem of data-driven stabilization ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") will be discussed in Section V.

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-C Our approach", "weight": 1.0} -->

In what follows, we will outline our strategy for solving Problems 1. ‣ II-B Problem formulation ‣ II The problem of data-driven stabilization ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") and 2. ‣ II-B Problem formulation ‣ II The problem of data-driven stabilization ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma"). Let ${(A,B)} \in \Sigma$ and rewrite as

<!-- chunk {"id": "body-0034", "role": "body", "section": "II-C Our approach", "weight": 1.0} -->

This shows that $A$ and $B$ satisfy a *quadratic matrix inequality* (QMI) of the form ^22^2We note that quadratic uncertainty descriptions have also arisen in the papers studying data-driven control under the assumption that $\mathbf{w}$ is a normally distributed process noise.. In fact, the set $\Sigma$ of all systems explaining the data can be equivalently characterized in terms of, as asserted in the following lemma.

<!-- chunk {"id": "body-0035", "role": "body", "section": "The matrix-valued S-lemma", "weight": 1.0} -->

In this section we present a new S-lemma with matrix variables. Before we do so, we provide a brief recap on the classical S-lemma.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-A Recap of the classical S-lemma", "weight": 1.0} -->

A function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is called *quadratic* if it can be written in the form

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-A Recap of the classical S-lemma", "weight": 1.0} -->

for some $M_{11} \in {\mathbb{R}}$, $M_{12} \in {\mathbb{R}}^{1 \times n}$ and $M_{22} = M_{22}^{\top} \in {\mathbb{R}}^{n \times n}$. A homogeneous quadratic function of the form ${f{(x)}} = {x^{\top}M_{22}x}$ is called a *quadratic form*. The following theorem describes the celebrated S-lemma, proven by Yakubovich, see also \[2, Thm. 2.2\].

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-B S-lemma with matrix variables", "weight": 1.0} -->

Next, we aim at generalizing Theorems 5. ‣ III-A Recap of the classical S-lemma ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") and 6. ‣ III-A Recap of the classical S-lemma ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") to quadratic functions of the form

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-B S-lemma with matrix variables", "weight": 1.0} -->

where $X \in {\mathbb{R}}^{n \times k}$ is a *matrix variable*, and the partitioned matrices ${M,N} \in {\mathbb{R}}^{{({k + n})} \times {({k + n})}}$ are real and symmetric. As our first step, the following theorem provides an S-lemma for homogeneous quadratic functions of the form $X^{\top}MX$ and $X^{\top}NX$. Naturally, instead of the non-negativity of functions in the classical S-lemma, we now consider the positive (semi)definiteness of quadratic functions of matrix variables.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 8", "weight": 1.0} -->

The assumption on the existence of $\overline{X}$ such that ${{\overline{X}}^{\top}N\overline{X}} > 0$ is a natural generalization of the Slater condition in Theorems 5. ‣ III-A Recap of the classical S-lemma ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") and 6. ‣ III-A Recap of the classical S-lemma ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma"). The assumption is again necessary in the sense that Theorem 7. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") is false without it. Nonetheless, it can be shown that the assumption can be weakened if one is interested only in the equivalence of (i.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 8", "weight": 1.0} -->

‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) and (iii. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")). In fact, one can show using similar arguments as in the proof of Theorem 7. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") that (i. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) $\Leftrightarrow$ (iii.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 8", "weight": 1.0} -->

‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) under the assumption that ${\exists\overline{x}} \in {\mathbb{R}}^{n}$ such that ${{\overline{x}}^{\top}N\overline{x}} > 0$, i.e., under the "standard" Slater condition.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Data-driven stabilization revisited", "weight": 1.0} -->

In this section, we apply the theory from Section III to data-driven stabilization, i.e., to Problems 1. ‣ II-B Problem formulation ‣ II The problem of data-driven stabilization ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") and 2. ‣ II-B Problem formulation ‣ II The problem of data-driven stabilization ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma") defined in Section II. To this end, for given $P = P^{\top} > 0$ and $K$ we define the partitioned matrices

<!-- chunk {"id": "body-0044", "role": "body", "section": "Data-driven stabilization revisited", "weight": 1.0} -->

Recall from Section II that data-driven stabilization entails deciding whether holds for all $(A,B)$ satisfying. In terms of the matrices $M$ and $N$ as defined above, we thus have to decide whether

<!-- chunk {"id": "body-0045", "role": "body", "section": "Data-driven stabilization revisited", "weight": 1.0} -->

The idea is now to apply Theorem 13. To this end, we have to verify its assumptions. In particular, we will check that $M_{22} \leqslant 0$, $N_{22} \leqslant 0$ and ${\ker N_{22}} \subseteq {\ker N_{12}}$. Note that

<!-- chunk {"id": "body-0046", "role": "body", "section": "Data-driven stabilization revisited", "weight": 1.0} -->

because $P > 0$ and $\Phi_{22} < 0$. Since $\Phi_{22}$ is nonsingular, we also see that

<!-- chunk {"id": "body-0047", "role": "body", "section": "Data-driven stabilization revisited", "weight": 1.0} -->

and thus ${\ker N_{22}} \subseteq {\ker N_{12}}$. We conclude that the assumptions of Theorem 13 are satisfied. We assume that the generalized Slater condition (16. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) holds for $N$ in (IV). Then, Theorem 13 asserts that holds if and only if there exist scalars $\alpha \geqslant 0$ and $\beta > 0$ such that

<!-- chunk {"id": "body-0048", "role": "body", "section": "Data-driven stabilization revisited", "weight": 1.0} -->

From a design point of view, the matrices $P$ and $K$ that appear in $M$ are not given. However, the idea is now to *compute* matrices $P$, $K$ and scalars $\alpha$ and $\beta$ such that holds. In fact, by the above discussion, the data $(U_{-},X)$ are informative for quadratic stabilization *if and only if* there exists an $n \times n$ matrix $P = P^{\top} > 0$, a $K \in {\mathbb{R}}^{m \times n}$ and two scalars $\alpha \geqslant 0$ and $\beta > 0$ such that holds. We note that (in particular, $M$) is not linear in $P$ and $K$. Nonetheless, by a rather standard change of variables and a Schur complement argument, we can transform into a linear matrix inequality. We summarize our progress in the following theorem, which is the main result of this section.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Remark 15", "weight": 1.0} -->

We note that under the extra assumption

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 15", "weight": 1.0} -->

it is possible to prove a variant Theorem 14 in which the non-strict inequality is replaced by a strict inequality, and the term $- {\betaI}$ is removed. This can be done by invoking Theorem 11. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma"), which is possible since implies that the set $\Sigma$ is bounded. The reason is that the coefficient matrix $N_{22}$ defining the quadratic term in is negative definite if holds.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 15", "weight": 1.0} -->

Here we chose to state and prove Theorem 14 in the slightly more general setting without assuming. In the discussion preceding Theorem 14 we have verified the assumptions of Theorem 13 for $M$ and $N$ in (LABEL:Mstab), (IV). In particular, this implies that the subspace inclusions hold and thus ${\ker\begin{bmatrix}
\end{bmatrix}} \subseteq {\ker\begin{bmatrix}
\end{bmatrix}}$, equivalently

<!-- chunk {"id": "body-0052", "role": "body", "section": "Remark 15", "weight": 1.0} -->

Therefore, any controller $K$ that stabilizes the systems in $\Sigma$ is necessarily of the form. This generalizes \[3, Lem. 15\] to the case of noisy data.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Inclusion of performance specifications", "weight": 1.0} -->

In this section we extend our data-driven stabilization result by including different performance specifications. In particular, we will treat the $\mathcal{H}_{2}$ and $\mathcal{H}_{\infty}$ control problems, thereby illustrating the general applicability of the theory in Section III.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-A $\\mathcal{H}_{2}$ control", "weight": 1.0} -->

As before, consider the the unknown system. We associate to a performance output

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-A $\\mathcal{H}_{2}$ control", "weight": 1.0} -->

where ${\mathbf{z}} \in {\mathbb{R}}^{p}$, and $C$ and $D$ are known matrices that specify the performance. For any ${(A,B)} \in \Sigma$ explaining the data, the feedback law ${\mathbf{u}} = {K{\mathbf{x}}}$ yields the closed-loop system

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-A $\\mathcal{H}_{2}$ control", "weight": 1.0} -->

The transfer matrix from $\mathbf{w}$ to $\mathbf{z}$ of is given by

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-A $\\mathcal{H}_{2}$ control", "weight": 1.0} -->

where $tr$ denotes trace. The data-driven $\mathcal{H}_{2}$ problem entails the computation of a feedback gain $K$ from data such that $\left. \parallel{G{(z)}}\parallel \right._{\mathcal{H}_{2}} < \gamma$ *for all* ${(A,B)} \in \Sigma$. Similar to our results for quadratic stabilization, we restrict the attention to a matrix $P$ that is common for all $(A,B)$. This leads to the following natural definition.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Remark 18", "weight": 1.0} -->

If we know a priori that the noise $\mathbf{w}$ is contained in a subspace, say ${im}E$, then this information can easily be exploited in the $\mathcal{H}_{2}$ controller design. In fact, we only need to replace the LMI involving $Z$ by

<!-- chunk {"id": "body-0059", "role": "body", "section": "Remark 18", "weight": 1.0} -->

We recall that prior knowledge of ${\mathbf{w}} \in {{im}E}$, if available, can also be captured by our noise model, see Remark 2. A natural choice is thus to use $E$ both in the noise model as well as in the LMI ($\mathcal{H}_{2}$). However, we remark that this is not necessary: the noise in the experiment may come from a different subspace than the disturbances that are attenuated by the $\mathcal{H}_{2}$ controller.

<!-- chunk {"id": "body-0060", "role": "body", "section": "V-B $\\mathcal{H}_{\\infty}$ control", "weight": 1.0} -->

In this section we will turn our attention to the $\mathcal{H}_{\infty}$ control problem. As before, consider system with performance output. For any ${(A,B)} \in \Sigma$, the feedback ${\mathbf{u}} = {K{\mathbf{x}}}$ yields the system with transfer matrix from $\mathbf{w}$ to $\mathbf{z}$ given by $G{(z)}$. We will denote the $\mathcal{H}_{\infty}$ norm of $G{(z)}$ by $\left. \parallel{G{(z)}}\parallel \right._{\mathcal{H}_{\infty}}$. Let $\gamma > 0$. By \[59, Thm. 4.6.6(iii)\], the matrix $A + {BK}$ is stable and $\left.

<!-- chunk {"id": "body-0061", "role": "body", "section": "V-B $\\mathcal{H}_{\\infty}$ control", "weight": 1.0} -->

where we have defined $A_{K}:={A + {BK}}$ and $C_{K}:={C + {DK}}$. We now have the following definition of informativity for $\mathcal{H}_{\infty}$ control.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Examples", "weight": 1.0} -->

In this section we illustrate our theoretical results by examples and numerical simulations.

<!-- chunk {"id": "body-0063", "role": "body", "section": "VI-A Stabilization using bounds on the noise samples", "weight": 1.0} -->

Consider an unstable system of the form with $A_{s}$ and $B_{s}$ given by

<!-- chunk {"id": "body-0064", "role": "body", "section": "VI-A Stabilization using bounds on the noise samples", "weight": 1.0} -->

In this example, we assume that the noise samples $w{(t)}$ are bounded in norm as $\left. \parallel{w{(t)}}\parallel \right._{2}^{2} \leqslant \epsilon$ for all $t$. As explained in Section II, we can capture this prior knowledge using the noise model with $\Phi_{11} = {T\epsilonI}$, $\Phi_{12} = 0$ and $\Phi_{22} - I$. We pick a time horizon of $T = 20$ and draw the entries of the inputs and initial state randomly from a Gaussian distribution with zero mean and unit variance. The noise samples are drawn uniformly at random from the ball $\{{w \in {\mathbb{R}}^{3}}\mid{\left. \parallel w\parallel \right._{2}^{2} \leqslant \epsilon}\}$. We aim at constructing stabilizing controllers from the input/state data for various values of $\epsilon$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "VI-A Stabilization using bounds on the noise samples", "weight": 1.0} -->

In particular, we investigate six different noise levels: $\epsilon \in {\{ 0.5,1,1.5,2,2.2,2.4\}}$. For each noise level, we generate $100$ data sets using the method described above. We check the generalized Slater condition (16. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) by verifying that $N$ in (IV) has $3$ positive eigenvalues; this turns out to be true for all $600$ data sets. For each noise level, we record the percentage of data sets from which a stabilizing controller was found for $(A_{s},B_{s})$ using the formulation (FS). We display the results in the following table.

<!-- chunk {"id": "body-0066", "role": "body", "section": "VI-A Stabilization using bounds on the noise samples", "weight": 1.0} -->

For $\epsilon = 0.5$ we find a stabilizing controller in all $100$ cases. When the noise level increases, the percentage of data sets for which the LMI (FS) is feasible decreases. The interpretation is that by increasing the noise we enlarge the set of explaining systems $\Sigma$. It thus becomes harder to simultaneously stabilize the systems in $\Sigma$. Nonetheless, even for the larger noise level of $\epsilon = 2.4$ we find a stabilizing controller in $73$ out of the $100$ data sets.

<!-- chunk {"id": "body-0067", "role": "body", "section": "VI-B $\\mathcal{H}_{2}$ control of a fighter aircraft", "weight": 1.0} -->

We consider a state-space model of a fighter aircraft \[59, Ex. 10.1.2\]. In particular, we discretize the model of using a sampling time of $0.01$, which results in the (unstable) system of the form with $A_{s}$ and $B_{s}$ given by

<!-- chunk {"id": "body-0068", "role": "body", "section": "VI-B $\\mathcal{H}_{2}$ control of a fighter aircraft", "weight": 1.0} -->

respectively. We consider the performance output as in with

<!-- chunk {"id": "body-0069", "role": "body", "section": "VI-B $\\mathcal{H}_{2}$ control of a fighter aircraft", "weight": 1.0} -->

and $D = 0$. First, we look for the smallest $\gamma$ such that is feasible for $(A_{s},B_{s})$. This minimum value of $\gamma$ is $1.000$ and can be regarded as a benchmark: no data-driven method can perform better than the model-based solution using full knowledge of $(A_{s},B_{s})$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "VI-B $\\mathcal{H}_{2}$ control of a fighter aircraft", "weight": 1.0} -->

Of course, our goal is not to use the knowledge of $(A_{s},B_{s})$ but to seek a data-driven solution instead. Therefore, we collect $T = 750$ input and state samples of. The entries of the inputs and initial state were drawn randomly from a Gaussian distribution with zero mean and unit variance. Also the noise samples were drawn randomly from a Gaussian distribution, with zero mean and variance $\sigma^{2}$ with $\sigma = 0.005$. In this example, we assume knowledge of a bound on the energy of the noise as

<!-- chunk {"id": "body-0071", "role": "body", "section": "VI-B $\\mathcal{H}_{2}$ control of a fighter aircraft", "weight": 1.0} -->

We verified that this bound is satisfied for the generated noise sequence. In addition, we verified that the matrix $N$ in (IV) has $6$ positive eigenvalues, thus the generalized Slater condition (16. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) holds.

<!-- chunk {"id": "body-0072", "role": "body", "section": "VI-B $\\mathcal{H}_{2}$ control of a fighter aircraft", "weight": 1.0} -->

Next, we want to compute an $\mathcal{H}_{2}$ controller for the unknown system using the generated data. We do so by minimizing $\gamma$ subject to ($\mathcal{H}_{2}$). This is a semidefinite program that we solve in Matlab, using Yalmip with Mosek as an LMI solver. The obtained controller $K$ stabilizes the original system $(A_{s},B_{s})$. In addition, the system, in feedback with $K$, has an $\mathcal{H}_{2}$ norm of $\gamma_{s}$ where $\gamma_{s}^{2} = 1.007$. We note that this is almost identical to the smallest possible $\mathcal{H}_{2}$ norm of $1.000$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "VI-B $\\mathcal{H}_{2}$ control of a fighter aircraft", "weight": 1.0} -->

Subsequently, we repeat the above experiment using only a *part* of our data set. In particular, we compute an $\mathcal{H}_{2}$ controller via the semidefinite program as before, using only the first $i$ samples of $X_{+},X_{-}$ and $U_{-}$ for $i = {50,100,\ldots,750}$. We display the results in Figure 1.

<!-- chunk {"id": "body-0074", "role": "body", "section": "VI-B $\\mathcal{H}_{2}$ control of a fighter aircraft", "weight": 1.0} -->

In each of the cases a stabilizing controller was found from data. However, the performance of these controllers when applied to the true system varies, and is quite poor for $i < 500$. Starting from $i = 500$ and onward, the performance is close to the optimal performance of the true system.

<!-- chunk {"id": "body-0075", "role": "body", "section": "VI-B $\\mathcal{H}_{2}$ control of a fighter aircraft", "weight": 1.0} -->

Next, we investigate what happens when we increase the variance $\sigma^{2}$ of the noise. First, we take $\sigma = 0.05$. We again generate $750$ data samples, and assume the same bound on the noise. The $\mathcal{H}_{2}$ controller achieves a performance of $\gamma_{s}^{2} = 1.146$ when interconnected to the true system. Increasing the variance of the noise has the effect that the set $\Sigma$ of explaining systems becomes larger. As such, it is more difficult to control all systems in $\Sigma$ resulting in a slightly larger $\gamma_{s}$. This behavior becomes even more apparent when increasing the variance of the noise to $\sigma = 0.5$. In this case we obtain a controller that yields a performance of $\gamma_{s}^{2} = 3.579$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "VI-B $\\mathcal{H}_{2}$ control of a fighter aircraft", "weight": 1.0} -->

Increasing $\sigma$ even more to $\sigma = 1$ results in infeasibility of the LMI's ($\mathcal{H}_{2}$) for any $\gamma$; the set of explaining systems has become too large for a quadratically stabilizing controller to exist.

<!-- chunk {"id": "body-0077", "role": "body", "section": "VI-B $\\mathcal{H}_{2}$ control of a fighter aircraft", "weight": 1.0} -->

We remark that the size of the set $\Sigma$ does not only depend on the variance of the noise, but also on the available bound on the noise. Throughout this example, we have used the bound. However, if we reconsider the case of $\sigma = 0.5$ with the tighter bound ${W_{-}W_{-}^{\top}} \leqslant {1.22T\sigma^{2}I}$ (which is also satisfied in this example) we obtain a controller with better performance $\gamma_{s}^{2} = 2.706$. This illustrates the simple fact that data-driven controllers not only depend on the particular design strategy, but also on the *prior knowledge* on the noise.

<!-- chunk {"id": "body-0078", "role": "body", "section": "VI-B $\\mathcal{H}_{2}$ control of a fighter aircraft", "weight": 1.0} -->

We conclude the example with a remark on the dimension of the variables involved in the formulation ($\mathcal{H}_{2}$). The symmetric matrices $Y$ and $Z$ both have $21$ free variables. The matrix $L$ contains $12$ variables, and $\alpha$ and $\beta$ are both scalar variables. Thus, the total number of variables is $56$. The size of the largest LMI in ($\mathcal{H}_{2}$) is $21 \times 21$. We emphasize that our approach is based directly on the set $\Sigma$ of open-loop systems and avoids the parameterization of closed-loop systems, as employed. Such parameterizations involve decision variables of dimension $T \times n$, which would result in at least $4500$ variables in this example.

<!-- chunk {"id": "body-0079", "role": "body", "section": "VI-C Comparison with related results", "weight": 1.0} -->

As we have mentioned before, one of the advantages of our approach compared to existing work is that our LMI condition provides necessary and sufficient conditions for data-driven quadratic stabilization. The purpose of this example is to demonstrate that our results can thus lead to stabilizing controllers even in situations where the results from cannot.

<!-- chunk {"id": "body-0080", "role": "body", "section": "VI-C Comparison with related results", "weight": 1.0} -->

Consider the system, where $A_{s} = 1$ and $B_{s} = 1$. Suppose that $T = 3$ and the noise matrix is given by

<!-- chunk {"id": "body-0081", "role": "body", "section": "VI-C Comparison with related results", "weight": 1.0} -->

Throughout the example, we assume that we have access to the noise bound ${W_{-}W_{-}^{\top}} \leqslant 1$. Note that this bound is indeed satisfied, and that it can be captured using Assumption 1 by the choices $\Phi_{11} = 1$, $\Phi_{12} = 0$ and $\Phi_{22} = {- I}$. We also note that by Remark 1, this noise bound can be captured by \[39, Asm. 3\] with the choices $Q_{w} = {- 1}$, $S_{w} = 0$ and $R_{w} = I$. Finally, we note that the noise bound can be captured by \[37, Asm. 5\] with the choice $\gamma = 1$. As such, we can compare the design methods reported in Theorem 14 of this paper with the approaches in \[39, Cor. 6, Rem. 7\] and \[37, Thm.

<!-- chunk {"id": "body-0082", "role": "body", "section": "VI-C Comparison with related results", "weight": 1.0} -->

6\]^66^6We note that studies stabilization in the setting that $\mathbf{w}$ represents a bounded nonlinearity. The interpretation of $\mathbf{w}$, however, is not important for this comparison. In fact, our results (as well as those in ) are applicable to general bounded disturbances, hence also to disturbances resulting from bounded nonlinearities..

<!-- chunk {"id": "body-0083", "role": "body", "section": "VI-C Comparison with related results", "weight": 1.0} -->

We start by applying Theorem 14 to the data in this example. Note that $X_{-} = \begin{bmatrix}
\end{bmatrix}$ and $X_{+} = \begin{bmatrix}
\end{bmatrix}$. It can be easily verified that ${(P,L,\alpha,\beta)} = {(0.9,{- 1.35},1.1,0.18)}$ is a solution to (FS). In addition, the Slater condition is satisfied in this example. As such, we conclude by Theorem 14 that the controller $K = {L/P} = {- 1.5}$ is stabilizing for all ${(A,B)} \in \Sigma$. In particular, we see that the true closed-loop system matrix $- 0.5$ is stable.

<!-- chunk {"id": "body-0084", "role": "body", "section": "VI-C Comparison with related results", "weight": 1.0} -->

We will now investigate the design method of \[37, Thm. 6\]. This approach involves finding a matrix $Q$ and a scalar $\alpha > 0$ such that $X_{-}Q$ is symmetric and

<!-- chunk {"id": "body-0085", "role": "body", "section": "VI-C Comparison with related results", "weight": 1.0} -->

where we recall that $\gamma = 1$ in this example. We will now show that, do not have a solution $(Q,\alpha)$, and thus, the design procedure from \[37, Thm. 6\] cannot find a controller that is guaranteed to stabilize the true system. To see this, note that and $\alpha > 0$ imply $\alpha > {1 + \sqrt{5}}$. We write $Q = \begin{bmatrix}
\end{bmatrix}^{\top}$ and note that by the upper left block of the first matrix, we have $q_{3} > \alpha$, thus $q_{3} > 1$. Now, by taking the Schur complement of the second matrix in with respect to the upper left block, we obtain $q_{3} > {q_{1}^{2} + q_{2}^{2} + q_{3}^{2}}$. However, this inequality cannot be satisfied since $q_{3} > 1$. As such, we conclude that, do not have a solution.

<!-- chunk {"id": "body-0086", "role": "body", "section": "VI-C Comparison with related results", "weight": 1.0} -->

Next, we turn our attention to the design procedure of \[39, Rem. 7\]. For $S_{w} = 0$, this procedure boils down to finding a solution $(\mathcal{Y},M)$ to

<!-- chunk {"id": "body-0087", "role": "body", "section": "VI-C Comparison with related results", "weight": 1.0} -->

where we recall that $Q_{w} = {- 1}$ and $R_{w} = I$ in this example. We will now show that, do not have a solution $(\mathcal{Y},M)$. To see this, note that implies $M = \begin{bmatrix}
\end{bmatrix}^{\top}$ with ${m_{1},m_{2}} \in {\mathbb{R}}$. The negative definiteness of the submatrix of consisting of the second and third row and column imply $\mathcal{Y} > 1$. Moreover, by inspection of the first and fourth row and column block of we see that ${{- \mathcal{Y}} + {M^{\top}M}} < 0$ and thus, ${{- \mathcal{Y}} + m_{1}^{2} + m_{2}^{2} + \mathcal{Y}^{2}} < 0$. This inequality, however, cannot be satisfied as $\mathcal{Y} > 1$.

<!-- chunk {"id": "body-0088", "role": "body", "section": "VI-C Comparison with related results", "weight": 1.0} -->

As such, we see that and do not have a solution $(\mathcal{Y},M)$.

<!-- chunk {"id": "body-0089", "role": "body", "section": "VI-C Comparison with related results", "weight": 1.0} -->

We conclude that Theorem 14 can be successfully applied even in situations in which the design procedures of do not lead to controllers that are guaranteed to stabilize the true system.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Discussion and conclusions", "weight": 1.5} -->

We have studied the problem of obtaining feedback controllers from noisy data. The essence of our approach has been to formulate data-driven control as the problem of determining when one quadratic matrix inequality implies another one. To get a grip on this fundamental question, we have generalized the classical S-lemma to matrix variables. The implication involving quadratic matrix inequalities is thereby *equivalent* to a linear matrix inequality in a scalar variable. We have established several versions of the matrix S-lemma, for both strict and non-strict inequalities. These matrix S-lemmas are interesting in their own right, and generalize existing S-lemmas as well as a theorem involving quadratic matrix inequalities.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Discussion and conclusions", "weight": 1.5} -->

We have followed up by applying our matrix S-lemma to data-driven control. In particular, we have given necessary and sufficient conditions under which stabilizing, $\mathcal{H}_{2}$, and $\mathcal{H}_{\infty}$ controllers can be obtained from noisy data. Our control design revolves around data-guided linear matrix inequalities, which can be solved efficiently using modern LMI solvers. In addition to being non-conservative, an attractive feature of our design procedure is that decision variables are *independent* of the time horizon of the experiment.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Discussion and conclusions", "weight": 1.5} -->

So far, we have only applied the matrix S-lemma involving a strict inequality (Thms. 11. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma"), 13) to data-driven control. However, we are convinced that also the matrix S-lemma with *non-strict* inequalities (Thm. 9. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma")) will find applications, for example, in the verification of dissipativity properties from data.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Discussion and conclusions", "weight": 1.5} -->

The noise model that we have employed is flexible, and can describe, e.g., constant disturbances, energy bounded noise and norm bounds on noise samples. If one is only interested in the latter, however, we expect that more specific control techniques are possible. In fact, analogous to, we can write the inequality ${w{(t)}^{\top}w{(t)}} \leqslant \epsilon$ as

<!-- chunk {"id": "body-0094", "role": "body", "section": "Discussion and conclusions", "weight": 1.5} -->

In the spirit of the S-procedure, one could thus design a stabilizing controller by computing^77^7This procedure is likely to be conservative, however, since the classical S-lemma is in general conservative for more than two quadratic functions. matrices $P = P^{\top} > 0$ and $K$, and *multiple* non-negative scalars $\alpha_{0},\alpha_{1},\ldots,\alpha_{T - 1}$ such that

<!-- chunk {"id": "body-0095", "role": "body", "section": "Discussion and conclusions", "weight": 1.5} -->

with $M$ given by (LABEL:Mstab). We will consider norm bounded noise samples in more detail in future work.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Discussion and conclusions", "weight": 1.5} -->

Yet another idea for future work is to extend the current results for state-feedback design to data-driven dynamic output feedback design. Specifically, it would be interesting to see whether the matrix S-lemmas can be applied to obtain dynamic output feedback controllers from a finite set of noisy *input/output* samples.
