## Introduction

Data-driven control refers to all approaches that use measured data as starting point in the control design. This design can be done either indirectly via model identification, or by directly mapping data to control policies. Both paradigms have a long history, but data-driven control has recently witnessed a renewed surge of interest, partly because of the widespread availability of data and the successes of machine learning algorithms. We mention contributions to data-driven optimal control, predictive control and robust tracking control, nonlinear control and system level synthesis.

Several recent papers aim at deriving tractable data-based linear matrix inequalities (LMI's) that enable direct data-driven control design. The paper proposes a semidefinite programming relaxation for the stabilization of switched systems. The authors of provide a data-based parameterization of controllers, which is applied to stabilization and optimal control problems. In, notions of informative data are defined, which leads to necessary and sufficient data-based conditions for different analysis and control problems. The paper considers a noise bound in terms of a quadratic matrix inequality and proposes LMI conditions for control with guaranteed stability and performance. Combining data with prior knowledge on the system dynamics has been studied . Also the problem of data-based verification of dissipativity properties has been cast as an LMI problem .

An important question in this line of work regards the conservatism of the proposed LMI conditions. In this direction, a state-of-the-art result is the matrix generalization of the classical S-lemma. This result provides an LMI condition under which all matrix solutions to one quadratic matrix inequality (QMI) also satisfy another QMI. The first inequality is motivated by the data: a quadratic bound on the noise, used , has the consequence that all systems explaining the data satisfy a QMI. The second inequality captures design specifications such as stability or $\mathcal{H}_{2}$/$\mathcal{H}_{\infty}$ performance. Based on the matrix S-lemma, necessary and sufficient conditions could be provided for data-driven control with guaranteed quadratic stability and performance.

A curious observation is that the stabilization result based on the S-lemma does not fully recover the stabilization result of for *noise-free* data. The reason is that in this case the Slater condition that is required for the matrix S-lemma does not hold. This fact is somewhat unsatisfactory because control using noise-free data should intuitively always be a special case of that for noisy data (with bound zero).

In this paper we resolve this issue by introducing a matrix version of Finsler's lemma. The classical Finsler's lemma provides an LMI condition under which a quadratic inequality is the consequence of a quadratic *equality*. We will explain the difficulties in generalizing this result to matrix variables. Then, as our main contribution we will provide a Finsler's lemma for matrix variables in case the involved matrices obey some special structure. This matrix Finsler's lemma is then applied to data-driven stabilization. Interestingly, we will see that the LMI condition of is also necessary and sufficient in the special case of noise-free data, a result that could not be concluded from the matrix S-lemma. We believe that the matrix Finsler's lemma will also find other applications in situations where a QMI is the consequence of a matrix equality. In this paper, we will study one more of such situations, namely the construction of absolutely stabilizing controllers of Lur'e systems.

*Outline*: In Section II we recap data-driven stabilization results and state the problem. Section III contains our results on the matrix Finsler's lemma. In Section IV this result is applied to bridge the results for noiseless and noisy data. Finally, in Section V we consider control of Lur'e systems.

## Recap of data-driven stabilization and problem formulation

We will first recap two data-driven stabilization results, for noise-free and noisy data, which can be found in the references. Consider the system where $\mathbf{x} \in {\mathbb{R}}^{n}$ is the state, $\mathbf{u} \in {\mathbb{R}}^{m}$ is the control input and $\mathbf{w} \in {\mathbb{R}}^{n}$ denotes noise. The real matrices $A_{s}$ and $B_{s}$ are not assumed to be known. Instead of this, it is assumed that input/state data are obtained, which are collected in the matrices We will also make use of shifted versions of the state sequence which are denoted by

### II-A Data-driven stabilization using exact data

In this section we focus on the noise-free situation in which $\mathbf{w} = 0$. The purpose is to use the input/state data $(U_{-},X)$ for the design of a stabilizing state feedback controller $\mathbf{u} = {K\mathbf{x}}$. Of course, this is only possible if the data contain sufficient information about the unknown system, i.e., if they are *informative* for control design.

### Definition 1

Suppose that the data $(U_{-},X)$ are generated by for $\mathbf{w} = 0$. Then $(U_{-},X)$ are *informative for stabilization by state feedback* if there exists a $K$ such that $A + {BK}$ is Schur stable for all ${(A,B)} \in \Sigma$, where The data are thus informative if there exists a single controller $K$ that stabilizes all systems explaining the data, i.e., all systems in $\Sigma$.

Informativity for stabilization can be checked by solving a data-based linear matrix inequality (LMI), given . This LMI condition was proposed , and in it was shown that it is *necessary and sufficient* for informativity for stabilization. We state the result as follows.

### Proposition 1

The data $(U_{-},X)$ are informative for stabilization by state feedback if and only if there exists a matrix $\Theta \in {\mathbb{R}}^{T \times n}$ such that ${X_{-}\Theta} = {({X_{-}\Theta})}^{\top}$ and Moreover, $K$ is such that $A + {BK}$ is stable for all ${(A,B)} \in \Sigma$ if and only if $K = {U_{-}\Theta{({X_{-}\Theta})}^{- 1}}$ for a $\Theta$ satisfying.

### II-B Data-driven stabilization using noisy data

Next, we consider the system where $\mathbf{w}$ is not necessarily zero. The experimental input/state data are denoted by $(U_{-},X)$, as before. This time, we also denote the noise samples during an experiment by Of course, the matrix $W_{-}$ is not known, but is assumed to bounded as for known $\Phi_{11} = \Phi_{11}^{\top}$, $\Phi_{12}$ and $\Phi_{22} = \Phi_{22}^{\top} < 0$. This noise model was first introduced. It can be interpreted as the transposed (or dual) model as the one used. The inequality has the interpretation that the energy of $\mathbf{w}$ is bounded on the finite time interval $\lbrack 0,{T - 1}\rbrack$.

Given the noise model, the set of all systems explaining the data is given by all $(A,B)$ such that is satisfied for some realization $W_{-}$ of the noise, that is, With this in mind, we recall the following notion of informative data for stabilization using noisy data.

### Definition 2

Suppose that the data $(U_{-},X)$ are generated by for some noise sequence $W_{-}$ satisfying. Then $(U_{-},X)$ are called *informative for quadratic stabilization* if there exists a feedback gain $K$ and a matrix $P = P^{\top} > 0$ such that for all ${(A,B)} \in \Sigma_{\Phi}$.

Note that we focus on stabilization with a *common* Lyapunov matrix $P$.

A necessary and sufficient condition for informativity for quadratic stabilization was given . The main concept that was used in that paper was a matrix version of the classical S-lemma. In fact, introduced both a non-strict and a strict version of this matrix S-lemma, both of which we recall in the following propositions.

\end{bmatrix} - {\begin{bmatrix} \end{bmatrix}\begin{bmatrix} \Phi_{12}^{\top} & \Phi_{22} \end{bmatrix}\begin{bmatrix} \end{bmatrix}^{\top}}} \geq 0}.$$

### Proposition 2 (Matrix S-lemma)

Consider the symmetric matrices ${M,N} \in {\mathbb{R}}^{{({k + \ell})} \times {({k + \ell})}}$ and assume that there exists some matrix $\overline{Z} \in {\mathbb{R}}^{\ell \times k}$ such that Then we have that if and only if there exists a scalar $\alpha \geq 0$ such that ${M - {\alphaN}} \geq 0$.

### Proposition 3 (Strict matrix S-lemma)

Consider symmetric matrices ${M,N} \in {\mathbb{R}}^{{({k + \ell})} \times {({k + \ell})}}$, partitioned as Assume that $M_{22} \leq 0$, $N_{22} \leq 0$ and ${\ker N_{22}} \subseteq {\ker N_{12}}$. Suppose that there exists some matrix $\overline{Z} \in {\mathbb{R}}^{\ell \times k}$ satisfying (9 ‣ II-B Data-driven stabilization using noisy data ‣ II Recap of data-driven stabilization and problem formulation ‣ A Matrix Finsler’s Lemma with Applications to Data-Driven Control")). Then we have that if and only if there exist $\alpha \geq 0$ and $\beta > 0$ such that Based on the strict matrix S-lemma, the following characterization of informativity for quadratic stabilization can be established. For this, we define $N$ as

### Proposition 4

Assume that Slater condition (9 ‣ II-B Data-driven stabilization using noisy data ‣ II Recap of data-driven stabilization and problem formulation ‣ A Matrix Finsler’s Lemma with Applications to Data-Driven Control")) holds for $N$ in and some $\overline{Z} \in {\mathbb{R}}^{{({n + m})} \times n}$. Then the data $(U_{-},X)$ are informative for quadratic stabilization if and only if there exists an $n \times n$ matrix $P = P^{\top} > 0$, an $L \in {\mathbb{R}}^{m \times n}$ and a scalar $\beta > 0$ satisfying (FS).

Moreover, if $P$ and $L$ satisfy (FS) then $K:={LP^{- 1}}$ is a stabilizing feedback gain for all ${(A,B)} \in \Sigma_{\Phi}$.

We note that the original formulation in involved an additional scalar variable $\alpha$. However, in the stabilization problem in Proposition 4 this variable can be absorbed in $P,L$ and $\beta$.

### II-C Problem formulation

To summarize, in the case of noise-free data, Proposition 1 gives a necessary and sufficient condition for informativity for stabilization. Moreover, in the case of noisy data, Proposition 4 provides a necessary and sufficient condition for informativity for quadratic stabilization.

A natural question is now the following: what is the relation between these two propositions, and can the former be obtained as a special case from the latter?

Surprisingly, the answer to this question is far from trivial. To initiate our investigation, it is tempting to consider the noise model with Indeed, this noise model implies that ${W_{-}W_{-}^{\top}} \leq 0$, i.e., $W_{-} = 0$ which corresponds exactly to the case in which the data are noise-free.

Now, a problem arises when applying Proposition 4 to noise models of the form. The reason is that for $\Phi$ , the matrix $N$ in is negative semidefinite. In turn, this implies that the Slater condition (9 ‣ II-B Data-driven stabilization using noisy data ‣ II Recap of data-driven stabilization and problem formulation ‣ A Matrix Finsler’s Lemma with Applications to Data-Driven Control")) is *not satisfied*. The conclusion is that Proposition 4 does not yield a necessary and sufficient condition for quadratic stabilization in the noise-free case (note that *sufficiency* of (FS) does hold, regardless of the Slater condition).

Despite this potential shortcoming of Proposition 4, it turns out to be possible to bridge the results for exact and noisy data in Propositions 1 and 4. In order to understand this relation we need a new result, namely a matrix version of *Finsler's lemma*.

## The matrix Finsler's lemma

Essentially, informativity for stabilization (Definition 1) asks for the existence of $P$ and $K$ such that a quadratic *inequality* holds for all $(A,B)$ satisfying the *equality* defined . This is more than reminiscent of the classical Finsler's lemma, named after Paul Finsler who proved the result in 1936. Two versions of Finsler's lemma are known, for both strict and non-strict inequalities. We will recall both results in the following two propositions that can be found .

### Proposition 5 (Strict Finsler's lemma)

Let ${M,N} \in {\mathbb{R}}^{\ell \times \ell}$ be symmetric. Then ${x^{\top}Mx} > 0$ for all nonzero $x \in {\mathbb{R}}^{\ell}$ satisfying ${x^{\top}Nx} = 0$ if and only if there exists an $\alpha \in {\mathbb{R}}$ such that ${M - {\alphaN}} > 0$.

### Proposition 6 (Non-strict Finsler's lemma)

Let ${M,N} \in {\mathbb{R}}^{\ell \times \ell}$ be symmetric and assume that $N$ is indefinite. Then ${x^{\top}Mx} \geq 0$ for all $x \in {\mathbb{R}}^{\ell}$ satisfying ${x^{\top}Nx} = 0$ if and only if there exists an $\alpha \in {\mathbb{R}}$ such that ${M - {\alphaN}} \geq 0$.

In the spirit of Finsler's lemma, we would like to find a tractable characterization of a statement of the form where the inequality involving $M$ is either non-strict or strict. Note that, in contrast to Finsler's lemma, this statement involves *inhomogeneous* functions of *matrix variables*.

To motivate our main result, we first point out some difficulties that arise when attempting to generalize Propositions 5 ‣ III The matrix Finsler’s lemma ‣ A Matrix Finsler’s Lemma with Applications to Data-Driven Control") and 6 ‣ III The matrix Finsler’s lemma ‣ A Matrix Finsler’s Lemma with Applications to Data-Driven Control") to the matrix case. First, the strict Finsler's lemma does not directly generalize to inhomogeneous quadratic functions, even in the vector-valued case. To convince oneself of this fact, it is sufficient to realize that while the matrix clearly cannot be positive definite. Secondly, in the non-strict case, we note that Proposition 6 ‣ III The matrix Finsler’s lemma ‣ A Matrix Finsler’s Lemma with Applications to Data-Driven Control") requires a Slater condition as $N$ is assumed to be indefinite. This Slater condition is problematic for data-driven control since we already know that in the noise-free setting the matrix $N$ in is negative semidefinite. A generalization of Proposition 6 ‣ III The matrix Finsler’s lemma ‣ A Matrix Finsler’s Lemma with Applications to Data-Driven Control"), even if possible, thus appears to be of lesser interest.

Our solution to this is the following: we will develop a matrix Finsler's lemma for matrices $M$ and $N$ with *specific structure*, and without assuming any type of Slater condition. Our main result can be formulated as follows. We will use $X^{+}$ to denote the Moore-Penrose pseudo-inverse of $X$.

### Theorem 1 (Matrix Finsler's lemma)

Consider symmetric matrices ${M,N} \in {\mathbb{R}}^{{({k + \ell})} \times {({k + \ell})}}$ partitioned as in (10 ‣ II-B Data-driven stabilization using noisy data ‣ II Recap of data-driven stabilization and problem formulation ‣ A Matrix Finsler’s Lemma with Applications to Data-Driven Control")). Assume that $N_{22} \leq 0$ and ${N_{11} - {N_{12}N_{22}^{+}N_{12}^{\top}}} = 0$.

Then we have that if and only if there exists $\alpha \in {\mathbb{R}}$ such that ${M - {\alphaN}} \geq 0$.

### Proof

The "if" part is obvious. We thus focus on proving the "only if" part. By Assumption 2 ‣ III The matrix Finsler’s lemma ‣ A Matrix Finsler’s Lemma with Applications to Data-Driven Control"), the matrix $\overline{Z}:={- {N_{22}^{+}N_{12}^{\top}}}$ satisfies Now, let $\hat{Z}:={\xi\eta^{\top}}$ where $\xi \in {\ker N_{22}}$ and $\eta$ is a nonzero vector. By hypothesis, we have for all $\gamma \in {\mathbb{R}}$. Recall that by Assumption 1 ‣ III The matrix Finsler’s lemma ‣ A Matrix Finsler’s Lemma with Applications to Data-Driven Control"), $M_{22} \leq 0$. This implies that ${M_{22}\hat{Z}} = 0$, for otherwise there exists a sufficiently large $\gamma \in {\mathbb{R}}$ violating. We have thus proven that ${\ker N_{22}} \subseteq {\ker M_{22}}$, equivalently, ${{im}M_{22}} \subseteq {{im}N_{22}}$.

Next, define the matrix where for the last equality we have used Assumption 3 ‣ III The matrix Finsler’s lemma ‣ A Matrix Finsler’s Lemma with Applications to Data-Driven Control") as follows: since $N_{12} = {G^{\top}N_{22}}$ and ${{im}M_{22}} \subseteq {{im}N_{22}}$ we have ${N_{12}N_{22}^{+}M_{22}} = {G^{\top}M_{22}}$. Similarly, we conclude that ${N_{12}N_{22}^{+}M_{22}N_{22}^{+}N_{12}^{\top}} = {G^{\top}M_{22}G}$. These computations reveal that Finally, by Assumption 3 ‣ III The matrix Finsler’s lemma ‣ A Matrix Finsler’s Lemma with Applications to Data-Driven Control"), ${M_{11} + {G^{\top}M_{22}G}} > 0$ and thus it holds that ${T^{\top}{({M - {\alphaN}})}T} \geq 0$ if and only if By Assumption 2 ‣ III The matrix Finsler’s lemma ‣ A Matrix Finsler’s Lemma with Applications to Data-Driven Control"), $N_{22} \leq 0$ and since ${\ker N_{22}} \subseteq {\ker M_{22}}$, we conclude that there exists a sufficiently large $\alpha \in {\mathbb{R}}$ such that holds. This implies that there exists an $\alpha \in {\mathbb{R}}$ such that ${M - {\alphaN}} \geq 0$, proving the theorem. ∎

## Bridging the exact and noisy cases

In this section, we will apply the matrix Finsler's lemma to find a new characterization of informativity for stabilization in the exact data case, thereby bridging the exact and noisy formulations. The result can be formulated as follows.

### Theorem 2

Let the data $(U_{-},X)$ be generated by with $\mathbf{w} = 0$. Then $(U_{-},X)$ are informative for stabilization by state feedback if and only if there exist $P = P^{\top} > 0$ and $L$, and a scalar $\beta > 0$ satisfying Moreover, if $P$ and $L$ satisfy then $K:={LP^{- 1}}$ is a stabilizing feedback gain for all ${(A,B)} \in \Sigma$.

### Proof

To prove the "if" part, suppose that is feasible and define $K:={LP^{- 1}}$. Compute the Schur complement of with respect to the fourth row and column block, which yields Finally, for any ${(A,B)} \in \Sigma$, multiply from the left by $\begin{bmatrix} \end{bmatrix}$ and from right by its transposed. This results in proving that $A + {BK}$ is Schur stable. Thus, the data $(U_{-},X)$ are informative for stabilization by state feedback and $K = {LP^{- 1}}$ is a stabilizing controller for all ${(A,B)} \in \Sigma$.

Next, to prove the "only if" part, suppose that the data $(U_{-},X)$ are informative for stabilization by state feedback. Then there exists a controller $K$ such that $A + {BK}$ is Schur for all ${(A,B)} \in \Sigma$. By \[17, Lem. 15\] there exist $P = P^{\top} > 0$ and $\beta > 0$ such that holds for all ${(A,B)} \in \Sigma$. Define the partitioned matrices For these matrices, the statement in (13 ‣ III The matrix Finsler’s lemma ‣ A Matrix Finsler’s Lemma with Applications to Data-Driven Control")) holds. In addition, note that $M_{12} = 0$ and $M_{22} \leq 0$, thus Assumption 1) of Theorem 1 ‣ III The matrix Finsler’s lemma ‣ A Matrix Finsler’s Lemma with Applications to Data-Driven Control") holds. Similarly, $N_{22} \leq 0$, and $N_{11} - {N_{12}N_{22}^{+}N_{12}^{\top}}$ equals which is zero since ${{im}X_{+}^{\top}} \subseteq {{im}\begin{bmatrix} \end{bmatrix}}$ by hypothesis. Therefore, Assumption 2) of Theorem 1 ‣ III The matrix Finsler’s lemma ‣ A Matrix Finsler’s Lemma with Applications to Data-Driven Control") is also satisfied. Finally, note that $G:=\begin{bmatrix} \end{bmatrix}^{\top}$ satisfies Assumption 3). We conclude by Theorem 1 ‣ III The matrix Finsler’s lemma ‣ A Matrix Finsler’s Lemma with Applications to Data-Driven Control") that there exists $\alpha \in {\mathbb{R}}$ such that ${M - {\alphaN}} \geq 0$. In fact, we necessarily have $\alpha > 0$ since ${- P} < 0$. We can thus assume without loss that $\alpha = 1$ (as $P$ and $\beta$ can be scaled by $1/\alpha$). Finally, by defining $L = {KP}$ and using a Schur complement argument we conclude that is feasible. ∎ Theorem 2 bridges the exact and noisy case in the following sense. Note that the matrix on the right of equals which is nothing but a special case of the matrix on the right of (FS) for the choices $\Phi_{11} = 0$, $\Phi_{12} = 0$ and $\Phi_{22} = {- I}$. This means that feasibility of the LMI (FS) (with specific $\Phi$) is also necessary and sufficient for informativity for stabilization in the case of exact data. In this case, we even know that the assumption of a common Lyapunov function is not restrictive, i.e., informativity for stabilization is equivalent for informativity for quadratic stabilization if $\mathbf{w} = 0$. This follows directly from \[17, Lem. 15\].

Given the two equivalent conditions in Proposition 1 and Theorem 2 it is natural to question the relative merits of both approaches. First of all, we note that the LMI conditions in and are different in nature: the variable $\Theta$ in has dimension $T \times n$ which depends on the time horizon of the experiment, while the dimensions of the variables $P,L$ and $\beta$ in are independent of $T$. From a computational point of view, Theorem 2 may thus be preferred in cases where the inputs of the experiment are chosen to be *persistently exciting* since this puts a lower bound $T \geq {n + m + {nm}}$ on the required number of samples. On the other hand, it has recently been shown that for controllable pairs $(A_{s},B_{s})$, the data $(U_{-},X)$ can be made informative for stabilization with at most $T = {n + m}$ samples, using an online input design method. In this case, the LMI may be preferred since has dimension ${{2n} \times 2}n$ which is smaller than the dimension ${({{3n} + m})} \times {({{3n} + m})}$ of.

## Data-driven stabilization of Lur'e systems

In this section, we will apply the matrix Finsler's lemma to control Lur'e systems. First, we will explain the classical problem of absolute stability for such systems. Consider the Lur'e system where $\mathbf{x} \in {\mathbb{R}}^{n}$ is the state, $\mathbf{u} \in {\mathbb{R}}^{m}$ is the input and $\phi:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$ is a (nonlinear) function satisfying the sector condition The real matrices $A,B,E$ and $C$ are of appropriate dimensions. Suppose that we apply a state feedback controller $\mathbf{u} = {K\mathbf{x}}$ resulting in For systems of the form, a problem with a rich history is that of *absolute stability*, i.e. global asymptotic stability of $0$ *for all* sector-bounded nonlinearities, c.f. for references. We focus on proving absolute stability of by means of a quadratic Lyapunov function ${V{(z)}}:={z^{\top}Pz}$ where $P = P^{\top} > 0$. We thus want that ${V{({x{({t + 1})}})}} < {V{({x{(t)}})}}$ for all sector-bounded nonlinearities $\phi$ and all nonzero $x{(t)}$ and resulting $x{({t + 1})}$ satisfying. We will mimic the continuous-time setting of \[28, Ch. 5\]. Let $A_{K}:={A + {BK}}$. Then we require for all $w \in {\mathbb{R}}$ and nonzero $x \in {\mathbb{R}}^{n}$ satisfying ${w{({w - {Cx}})}} \leq 0$. Equivalently, for all $w \in {\mathbb{R}}$ and nonzero $x \in {\mathbb{R}}^{n}$ satisfying Since is not satisfied when $x = 0$ and $w \neq 0$, the latter statement is equivalent to being satisfied for all nonzero $(x,w)$ satisfying. Assuming $C \neq 0$, the inequality is strictly feasible. Thus, by the S-lemma \[28, p. 24\] we conclude that is satisfied for all nonzero $(x,w)$ satisfying if and only if for some scalar $\alpha \geq 0$. Proving absolute stability of by a quadratic Lyapunov function thus boils down to finding $P = P^{\top} > 0$ and $\alpha \geq 0$ such that holds. By homogeneity, we can even get rid of $\alpha$ and look for $P = P^{\top} > 0$ satisfying

### V-A Data-driven stabilization

Next, we consider the system where $A_{s},B_{s}$ and $E_{s}$ are unknown but the matrix $C$ is known^11^1This assumption can be replaced by measurements of ${\mathbf{y}{(t)}}:={C\mathbf{x}{(t)}}$.. We aim at constructing an absolutely stabilizing controller $\mathbf{u} = {K\mathbf{x}}$ on the basis of measurements $X$ and $U_{-}$ as in and If we define $X_{+}$ and $X_{-}$ as in then all systems $(A,B,E)$ explaining the data are given by the set $\Sigma$ defined by

### Definition 3

Suppose that the data $(U_{-},W_{-},X)$ in and have been generated . Then $(U_{-},W_{-},X)$ are called *informative for absolute quadratic stabilization* if there exist $P = P^{\top} > 0$ and $K$ such that holds for all ${(A,B,E)} \in \Sigma$.

### Theorem 3

The data $(U_{-},W_{-},X)$ are informative for absolute quadratic stabilization if and only if there exist matrices $Q = Q^{\top} > 0$ and $L$ and scalars $\alpha \in {\mathbb{R}}$ and $\beta > 0$ such that ${CQC^{\top}} < 4$ and In this case, $K:={LQ^{- 1}}$ is such that is absolutely stable for all ${(A,B,E)} \in \Sigma$.

### Proof

We first prove the "if" part. Note that the lower right $2$ by $2$ block matrix of is positive definite since $Q > 0$ and ${CQC^{\top}} < 4$. Define $P:=Q^{- 1}$ and $K:={LQ^{- 1}}$, and let ${(A,B,E)} \in \Sigma$. Multiply from both sides by the block diagonal matrix with blocks $I,I,1,1,P$ and $1$. Then take the Schur complement of with respect to the lower right $2$ by $2$ block, and multiply with $\begin{bmatrix} \end{bmatrix}$ from left and its transposed from right to obtain Finally, by using a Schur complement argument twice, we see that implies. Therefore the data are informative for absolute quadratic stabilization and $K$ is a suitable controller with Lyapunov matrix $Q^{- 1}$.

To prove the "only if" part, suppose that there exist $P = P^{\top} > 0$ and $K$ such that holds for all ${(A,B,E)} \in \Sigma$. Using a Schur complement argument twice this implies holds. Analogous to \[17, Lem. 15\] it can be shown that $A + {BK}$ and $E$ are the same for all ${(A,B,E)} \in \Sigma$. This implies that still holds for all ${(A,B,E)} \in \Sigma$ if we replace the strict inequality by a non-strict inequality and $P^{- 1}$ by $P^{- 1} - {\betaI}$ for some sufficienctly small $\beta > 0$. Define By Theorem 1 ‣ III The matrix Finsler’s lemma ‣ A Matrix Finsler’s Lemma with Applications to Data-Driven Control"), we conclude that there exists an $\alpha \in {\mathbb{R}}$ such that ${M - {\alphaN}} \geq 0$. Finally, by defining the variables $Q:=P^{- 1}$ and $L:={KQ}$ and using a Schur complement argument, we see that ${CQC^{\top}} < 4$ and is feasible. ∎
