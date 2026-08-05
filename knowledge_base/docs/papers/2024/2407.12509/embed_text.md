<!-- arxiv-full-text:v1 {"arxiv_id": "2407.12509", "source": "arxiv-html"} -->

## Introduction

*Background*: In the context of system identification, *experiment design* is concerned with the selection of inputs of a dynamical system in such a way that the resulting input-output data contain sufficient information about the system dynamics. Experiment design is a classical topic that has been investigated from different angles throughout the years.

An experiment design result that has recently been popularized is the so-called *fundamental lemma* by Willems and his coauthors. Roughly speaking, the result says that the dynamics of a linear time-invariant system can be uniquely identified from input-output data if the input data are chosen to be sufficiently persistently exciting. The fundamental lemma also provides a parameterization of all finite trajectories of the system, in terms of a data Hankel matrix. This parameterization has been applied in several recent data-driven analysis and control techniques ranging from simulation and linear quadratic regulation to predictive control, stabilization and dissipativity analysis.

The recent interest in data-driven control has also led to extensions of the fundamental lemma itself. Its original proof was presented in the language of behavioral theory; an alternative proof for state space systems was provided . Generalizations to uncontrollable systems are presented in and extensions to continuous-time systems . Robust/quantitative versions are explored in while frequency domain formulations have been considered . Furthermore, the fundamental lemma has been generalized to various other model classes such as descriptor systems, flat nonlinear systems, linear parameter-varying systems, and stochastic ones.

The assumption of persistency of excitation, central to the fundamental lemma, imposes a lower bound on the required number of data samples for system identification. This lower bound is conservative in the sense that system identification is possible using less data, as long as certain conditions are met. Until recently, the precise conditions enabling system identification were still missing from the literature. However, , necessary and sufficient conditions are provided under which the data contain sufficient information for system identification, assuming minimality of the data-generating system and upper (and lower) bounds on its lag and state-space dimension. As is quite reminiscent of the subspace identification literature, these conditions involve rank properties of data Hankel matrices. However, a truly remarkable feat of is that the *depth* of these Hankel matrices is not given a priori but is *determined from the data*.

In this paper, we will build on the framework of. However, unlike that focused on analyzing informativity of given data sets, the purpose of this paper is to *design* experiments that are informative for system identification. The main questions of this paper are therefore as follows: What is the shortest possible sequence of input-output data that enables linear system identification? And, if possible, how can we design the inputs of the system in order to generate such a shortest experiment?

Apart from being of theoretical interest, these questions are also highly relevant for control applications. In fact, the computation time of, for example, data-driven predictive control scales cubically with the data length. Working with shorter yet informative experiments reduces the computational burden of these methods.

*Contributions*: The main contributions of the paper are as follows: We assume that the unknown data-generating system is minimal and its lag and state-space dimension are upper bounded by $L$ and $N$. Then, based, we formulate a lower bound $T$ on the data length of any experiment that is informative for system identification (see).

We propose the experiment design method OnlineExperiment$(L,N)$. This procedure designs the inputs *online*, i.e., on the basis of past input-output samples. In Theorem 7 we prove that this method leads to informative experiments of length $T$.

A remarkable outcome of this paper is the fact that experiments can be designed of length *precisely equal to the lower bound $T$*. Interestingly, this number of samples $T$ depends on the unknown system and is thus not given a priori. It is revealed after the experiment design algorithm terminates.

*Relation to previous work*: The online experiment design method of this paper always requires less samples than the persistency of excitation requirement of the fundamental lemma. In many cases, there is a substantial difference in number of data samples. We provide an example of this in Section 8. The online experiment design method of keeps the depth of the data Hankel matrix *fixed* during the operation of the algorithm. In contrast to, our approach *adapts the depth* of the Hankel matrix during operation of the algorithm. The rationale is that the "correct" depth of the Hankel matrix for the necessary and sufficient conditions of is *a priori unknown*. We show in Section 8 that our method outperforms in some situations, depending on the given $L$ and $N$. In other cases, our results prove that the approach of leads to the shortest experiments for linear system identification.

*Outline*: In Section 2 we treat preliminaries. In Section 3 we recap the fundamental lemma. In Section 4 we recall the definition and characterization of *informativity for system identification*. Subsequently, in Section 5 we formalize the problem and in Section 6 we present our main results. In Section 7 we provide examples, while Section 8 contains a comparison to the state-of-the-art. Finally, in Section 9 we conclude the paper.

## Notation and preliminaries

We denote the $n \times n$ identity matrix by $I_{n}$ and the $m \times n$ zero matrix by $0_{m,n}$. The column vector containing $n$ zeros is denoted by $0_{n}$. For partitioned matrices containing zero and/or identity submatrices, we do not indicate the sizes of blocks that follow from their positions. The left kernel of a matrix $M \in {\mathbb{R}}^{m \times n}$ is defined as ${{lker}M}:={\{{x \in {\mathbb{R}}^{m}}\mid{{x^{\top}M} = 0}\}}$.

A subset $\mathcal{A} \subseteq {\mathbb{R}}^{n}$ is called *affine* if it can be expressed as $\mathcal{A} = {{\{ x\}} + \mathcal{S}}$ where $x \in {\mathbb{R}}^{n}$ and $\mathcal{S} \subseteq {\mathbb{R}}^{n}$ is a subspace. The dimension of $\mathcal{A}$ is defined as the dimension of $\mathcal{S}$.

### Void matrices

A void matrix is a matrix with zero rows and/or zero columns. We will use the notation $0_{n,0}$ and $0_{0,m}$ to denote, respectively, $n \times 0$ and $0 \times m$ void matrices. All matrix operations extend to void matrices in a natural manner. In particular, if $M$ and $N$ are, respectively $p \times q$ and $q \times r$ matrices, $MN$ is a $p \times r$ void matrix if $p = 0$ or $r = 0$ and ${MN} = 0_{p,r}$ if ${p,r} \geqslant 1$ and $q = 0$. In addition, the rank of a void matrix is zero.

### Integer intervals and Hankel matrices

Given ${i,j} \in {\mathbb{Z}}$ with $i \leqslant j$, we write $\lbrack i,j\rbrack$ to denote the ordered set of all integers between $i$ and $j$, including both $i$ and $j$. By convention, ${\lbrack i,j\rbrack} = \varnothing$ if $i > j$.

Let ${i,j} \in {\mathbb{Z}}$ with $i \leqslant j$. Also, let ${{f{(i)}},{f{({i + 1})}},\ldots,{f{(j)}}} \in {\mathbb{R}}^{n}$ be a sequence of vectors. We define Also, for $0 \leqslant k \leqslant {j - i}$ the *Hankel matrix of $k + 1$ block rows associated with $f_{\lbrack i,j\rbrack}$* is defined: We say that $f_{\lbrack i,j\rbrack}$ is *persistently exciting of order $k + 1$* if $H_{k}{(f_{\lbrack i,j\rbrack})}$ has full row rank. We stress that $H_{k}$ has $k + 1$ block rows, which is slightly different from the notation in most of the literature, but adopted here to be consistent with the paper.

### Input-state-output systems

Throughout the paper, we work with linear discrete-time input-state-output systems of the form where $n \geqslant 0$, ${m,p} \geqslant 1$, $A \in {\mathbb{R}}^{n \times n}$, $B \in {\mathbb{R}}^{n \times m}$, $C \in {\mathbb{R}}^{p \times n}$, and $D \in {\mathbb{R}}^{p \times m}$.

For $k \geqslant {- 1}$, we define the *$k$-th observability matrix* by the *$k$-th controllability matrix* by and the *$k$-th Toeplitz matrix of Markov parameters* by We denote the smallest integer $k \geqslant 0$ such that ${{rank}\Omega_{k}} = {{rank}\Omega_{k - 1}}$ by $\ell{(C,A)}$. Note that $0 \leqslant {\ell{(C,A)}} \leqslant n$ and if $n = 0$ then ${\ell{(C,A)}} = 0$. Moreover, if $(C,A)$ is observable, then $\ell{(C,A)}$ is the observability index of the pair. In the following we call $\ell{(C,A)}$ the *lag* of the system; for a justification of this terminology, see statements (iv) and (vii) of \[33, Thm. 6\].

### Systems with $m$ inputs and $p$ outputs

We identify the system with the matrix $\begin{bmatrix} \end{bmatrix}$. Given $m \geqslant 1$ and $p \geqslant 1$, we define the set of all systems with lag $\ell$ and $n$ states by

### Isomorphic systems

Two systems $\begin{bmatrix} \end{bmatrix} \in {\mathcal{S}{(n)}}$ with $i \in {\lbrack 1,2\rbrack}$ are said to be isomorphic if $D_{1} = D_{2}$ and there exists a nonsingular matrix $S \in {\mathbb{R}}^{n \times n}$ such that $A_{1} = {S^{- 1}A_{2}S}$, $B_{1} = {S^{- 1}B_{2}}$, and $C_{1} = {C_{2}S}$. By extending this notion to a set of systems, we say that $\mathcal{S}' \subseteq {\mathcal{S}{(n)}}$ has the isomorphism property if any pair of systems in $\mathcal{S}'$ is isomorphic. By convention, the empty set has the isomorphism property.

## Recap of the fundamental lemma and the high-level problem

In this section we recap the fundamental lemma and we sketch the problem of this paper at a high level. Let $m \geqslant 1$ and $p \geqslant 1$. Consider the linear discrete-time input-state-output system where $n_{true} \geqslant 0$, $A_{true} \in {\mathbb{R}}^{n_{true} \times n_{true}}$, $B_{true} \in {\mathbb{R}}^{n_{true} \times m}$, $C_{true} \in {\mathbb{R}}^{p \times n_{true}}$, and $D_{true} \in {\mathbb{R}}^{p \times m}$. We refer to the system as the true system. Its lag will be denoted by $\ell_{true}:={\ell{(C_{true},A_{true})}}$.

Throughout the paper, we assume that the true system is *minimal*, i.e. both observable and controllable. We also assume to know upper bounds on the true lag and true state-space dimension. In other words, we have $L$ and $N$ such that: Let $t \geqslant 1$. Consider the input-output data $(u_{\lbrack 0,{t - 1}\rbrack},y_{\lbrack 0,{t - 1}\rbrack})$ generated by system during the time window $\lbrack 0,{t - 1}\rbrack$. In what follows, we state a reformulation of the fundamental lemma.

### Proposition 1

Consider the minimal system. Suppose that $\ell_{true} \geqslant 1$, and that $N$ and $L$ satisfy. Assume that $u_{\lbrack 0,{t - 1}\rbrack}$ is persistently exciting of order $N + L + 1$. Then The latter rank condition implies that all length $L + 1$ input-output trajectories of can be obtained as linear combinations of the columns of the data Hankel matrix. This fact has been used frequently in the recent data-driven control literature. In terms of system identification, Proposition 1 has the following two consequences: The state-space dimension of the true system can be obtained from data as The system matrices $A_{true},B_{true},C_{true}$ and $D_{true}$ can be identified up to an isomorphism from the data. That is, using $(u_{\lbrack 0,{t - 1}\rbrack},y_{\lbrack 0,{t - 1}\rbrack})$ we can find matrices $A,B,C$ and $D$ such that are isomorphic, using, for example, subspace identification.

Thus, the fundamental lemma can be interpreted as an experiment design result, that tells us that the system matrices can be uniquely identified (up to isomorphism) as long as the input is designed to be persistently exciting. This condition on the input, however, puts a bound on the required number of data samples. In fact, $u_{\lbrack 0,{t - 1}\rbrack}$ can only be persistently exciting of order $N + L + 1$ if In fact, by designing $u_{\lbrack 0,{t - 1}\rbrack}$ such that $H_{N + L}{(u_{\lbrack 0,{t - 1}\rbrack})}$ is square and nonsingular, the system matrices can be identified from an input-output experiment of length exactly $N + L + {m{({N + L + 1})}}$. However, as we will see in this paper it is not necessary to collect this many samples in order to identify the system. The main questions of this paper are thus the following: What is the shortest experiment for linear system identification? In other words, what is the smallest time $T$ for which there exists an "informative" experiment $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ from which the matrices $A_{true},B_{true},C_{true}$ and $D_{true}$ can be identified up to isomorphism?

If possible, how can we design precisely $T$ inputs such that the resulting data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ are informative for system identification?

In order to give a precise answer to these questions, we first recap the definition and characterization of informativity for system identification in Section 4. We then provide a formal mathematical problem statement in Section 5, and solve this problem in Section 6.

## Informativity for system identification

In this section we recap the definition and characterization of informativity for system identification. Without making any a priori assumption on the input, let $(u_{\lbrack 0,{t - 1}\rbrack},y_{\lbrack 0,{t - 1}\rbrack})$ be data obtained. This means that there exists $x_{\lbrack 0,t\rbrack} \in {\mathbb{R}}^{n_{true} \times {({t + 1})}}$ such that A system $\begin{bmatrix} \end{bmatrix} \in {\mathcal{S}{(n)}}$ explains the data $(u_{\lbrack 0,{t - 1}\rbrack},y_{\lbrack 0,{t - 1}\rbrack})$ if there exists $x_{\lbrack 0,t\rbrack} \in {\mathbb{R}}^{n \times {({t + 1})}}$ such that The set of all systems that explain the data $(u_{\lbrack 0,{t - 1}\rbrack},y_{\lbrack 0,{t - 1}\rbrack})$ is denoted by $\mathcal{E}_{t}$ and is referred to as the set of explaining systems. The subsets of $\mathcal{E}_{t}$ consisting of systems with a given lag and state space dimension are respectively defined as

### Definition of informativity for system identification

The set $\mathcal{S}_{L,N}$ consists of all systems with lag at most $L$ and state-space dimension at most $N$, i.e., In view of the bounds and the minimality of the true system, we have the following *prior knowledge*: With this in mind, we define the notion of informativity for system identification. We also refer the reader to for a general treatment of informativity for different analysis and control problems.

### Definition 2

We say that the data $(u_{\lbrack 0,{t - 1}\rbrack},y_{\lbrack 0,{t - 1}\rbrack})$ are informative for system identification if ${\mathcal{E}_{t} \cap \mathcal{M} \cap \mathcal{S}_{L,N}} = {{\mathcal{E}_{t}{(n_{true})}} \cap \mathcal{M} \cap \mathcal{S}_{L,N}}$, and $\mathcal{E}_{t} \cap \mathcal{M} \cap \mathcal{S}_{L,N}$ has the isomorphism property.

The first condition means that all explaining systems satisfying the prior knowledge have $n_{true}$ states, while the second one asserts that any pair of such systems is isomorphic. Definition 2 thus captures the important property that there is precisely one equivalence class of state-space systems explaining the input-output data. In, necessary and sufficient conditions are provided under which the data are informative for system identification. In order to recall these conditions, we first need to define two important integers, namely the shortest lag and minimum number of states.

### The shortest lag and minimum number of states

Given the data $(u_{\lbrack 0,{t - 1}\rbrack},y_{\lbrack 0,{t - 1}\rbrack})$, we define the following two integers that play a pivotal role in the characterization of informativity for system identification: As proven, these integers admit a simple characterization in terms of the data. To explain this, let $k \in {\lbrack 0,{t - 1}\rbrack}$ and denote the Hankel matrix of $k + 1$ block rows constructed from the data $(u_{\lbrack 0,{t - 1}\rbrack},y_{\lbrack 0,{t - 1}\rbrack})$ by Note that $G_{k,t}$ may be obtained by removing the last row of outputs $y_{\lbrack k,{t - 1}\rbrack}$ from $H_{k,t}$. Now, define Throughout the paper, we assume that $u_{\lbrack 0,{t - 1}\rbrack} \neq 0_{m,t}$. From this blanket assumption, it follows that ${{rank}H_{{t - 1},t}} = {{rank}G_{{t - 1},t}} = 1$ and hence Let $q_{t} \in {\lbrack 0,{t - 1}\rbrack}$ be the smallest integer such that $\delta_{q_{t},t} = 0$. Note that $q_{t}$ is well-defined due to. The shortest lag and minimum number of states can be computed in terms of $\delta_{k,t}$ and $q_{t}$, as recalled next (see \[5, Thm. 8\]).

### Proposition 3

$\ell_{\min,t} = q_{t}$ and $n_{\min,t} = {\sum_{i = 0}^{\ell_{\min,t}}\delta_{i,t}}$.

An important consequence of Proposition 3 is that the integers $\ell_{\min,t}$ and $n_{\min,t}$ can readily be computed using the data.

### Necessary and sufficient conditions for informativity

We are now in a position to recall the conditions for informativity for system identification. Before we do so, we note that \[5, Thms. 6(b) and 8\] shows that ${N - n_{\min,t}} + \ell_{\min,t}$ is an upper bound for the lag of any explaining system with at most $N$ states. This upper bound, which is determined by the data and $N$, is in some cases smaller than the given upper bound $L$. This means that we can replace $L$ by the actual upper bound on the lag: The following theorem from \[5, Thm. 9\] provides *necessary and sufficient* conditions for the data to be informative for system identification.

### Theorem 4

The data $(u_{\lbrack 0,{t - 1}\rbrack},y_{\lbrack 0,{t - 1}\rbrack})$ are informative for system identification if and only if the following two conditions hold: Moreover, if the conditions in are satisfied, then

## Formal problem statement

If the data $(u_{\lbrack 0,{t - 1}\rbrack},y_{\lbrack 0,{t - 1}\rbrack})$ are informative for system identification, then $\ell_{\min,t} = \ell_{true}$ and $n_{\min,t} = n_{true}$ by Theorem 4. In this case, $L_{t}^{a}$ is equal to It follows from the lower bound (10a) that that is, any set of informative input-output data contains at least $T$ samples.

The main question is now as follows: can we design a sequence of inputs $u_{\lbrack 0,{T - 1}\rbrack}$ of length *precisely* $T$ such that the resulting input-output data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ are informative for system identification? We will focus on an *online* design of the inputs, in the sense that the choice of $u{(t)}$ is guided by the data $(u_{\lbrack{t - 1}\rbrack},y_{\lbrack 0,{t - 1}\rbrack})$ collected at previous time steps. We formalize the problem as follows.

### Problem 1

Let $T$ be as . Consider the system with initial state ${x{}} = x_{0} \in {\mathbb{R}}^{n}$. Let ${y{(t)}} \in {\mathbb{R}}^{p}$ denote the output of at time $t$ resulting from $x_{0}$ and the control inputs ${{u{}},{u{}},\ldots,{u{(t)}}} \in {\mathbb{R}}^{m}$.

For each $t = {0,1,\ldots,{T - 1}}$, given $(u_{\lbrack 0,{t - 1}\rbrack},y_{\lbrack 0,{t - 1}\rbrack})$, design $u{(t)}$ such that the resulting data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ are informative for system identification.

We note that the initial state $x_{0}$ of the system is arbitrary and not assumed to be given. Our goal is thus to design inputs that lead to an informative experiment *irrespective of $x_{0}$*.

In addition, we emphasize that it is not straightforward to see that Problem 1 has a solution. In fact, even though $T$ is a lower bound on the number of data samples required for system identification, it is at this point unclear whether there *exists* an experiment of length exactly $T$. Also, even if such an experiment exists, it is far from obvious that there is a systematic way of *constructing* such an experiment without knowledge of the true system. An additional challenge is that the time $T$ itself depends on the true lag and true state-space dimension, which are *not a priori known*.

Remarkably, as we show in this paper, it turns out to be *always* possible to design an informative experiment of length precisely $T$, despite these challenges.

## Online experiment design

In this section we present our main results, building up to the online experiment design method. We start with the following auxiliary lemma that asserts that the rank of the Hankel matrix $H_{k,t}$ can be increased at time $t + 1$, assuming that certain conditions are met.

### Lemma 5

Let $t \geqslant 2$ and $k \geqslant 1$. If then there exists an $({m - 1})$-dimensional affine set $\mathcal{A}_{t} \subseteq {\mathbb{R}}^{m}$ such that whenever ${u{(t)}} \notin \mathcal{A}_{t}$.

### Proof

Note that ${{{lker}H_{{k - 1},t}} \times {\{ 0_{m}\}}} \subseteq {{lker}G_{k,t}}$. Therefore, it holds that ${\dim{{lker}G_{k,t}}} \geqslant {\dim{{lker}H_{{k - 1},t}}}$. It follows from the rank-nullity theorem that ${{{kp} + {{({k + 1})}m}} - {{rank}G_{k,t}}} \geqslant {{k{({p + m})}} - {{rank}H_{{k - 1},t}}}$. As such, ${{rank}G_{k,t}} \leqslant {m + {{rank}H_{{k - 1},t}}}$. Moreover, note that ${{rank}G_{k,t}} = {m + {{rank}H_{{k - 1},t}}}$ if and only if ${{{lker}H_{{k - 1},t}} \times {\{ 0_{m}\}}} = {{lker}G_{k,t}}$. Therefore, implies that there exist $\xi_{i} \in {\mathbb{R}}^{p}$ and $\eta_{j} \in {\mathbb{R}}^{m}$ with $i \in {\lbrack 0,{k - 1}\rbrack}$ and $j \in {\lbrack 0,k\rbrack}$ such that $\eta_{k} \neq 0$ and Now, define the set If ${u{(t)}} \notin \mathcal{A}_{t}$ then Since ${{lker}G_{k,{t + 1}}} \subseteq {{lker}G_{k,t}}$, we conclude from the latter inequality that ${\dim{{lker}G_{k,{t + 1}}}} < {\dim{{lker}G_{k,t}}}$. Therefore, the last column of $G_{k,{t + 1}}$ is not a linear combination of the columns of $G_{k,t}$. Thus, the last column of $H_{k,{t + 1}}$ is also not a linear combination of the columns of $H_{k,t}$. We conclude that holds, which proves the lemma. ∎ As long as the inequality holds, Lemma 5 may be successively applied several times to increase the rank of the Hankel matrix. In the next lemma, we show how to deduce from the data whether $k = L^{a}$, as soon as the condition fails to hold. This lemma will be used as a stopping criterion for our online experiment design algorithm.

### Lemma 6

Let $t \geqslant 2$ and $k \geqslant 1$ and suppose that the data $(u_{\lbrack 0,{t - 1}\rbrack},y_{\lbrack 0,{t - 1}\rbrack})$ are such that $H_{k,t}$ has full column rank. Let $\tau \geqslant 0$ and assume that $u_{\lbrack t,{{t + \tau} - 1}\rbrack}$ satisfy for every $s \in {\lbrack t,{{t + \tau} - 1}\rbrack}$, ${{rank}G_{k,s}} < {m + {{rank}H_{{k - 1},s}}}$ and ${u{(s)}} \notin \mathcal{A}_{s}$, where $\mathcal{A}_{s}$ is as in Lemma 5. ${{rank}G_{k,{t + \tau}}} = {m + {{rank}H_{{k - 1},{t + \tau}}}}$.

Then the following statements hold: If $k \geqslant \ell_{true}$ then ${{rank}H_{k,{t + \tau}}} = {{{({k + 1})}m} + n_{true}}$, $\ell_{\min,{t + \tau}} = \ell_{true}$, and $n_{\min,{t + \tau}} = n_{true}$. $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ are informative for system identification.

### Proof

We first prove (a) ‣ Lemma 6. ‣ 6 Online experiment design ‣ The shortest experiment for linear system identification"). Assume that $k \geqslant \ell_{true}$. Hypothesis 1 and Lemma 5 imply that Let $x_{\lbrack 0,{{t + \tau} - 1}\rbrack} \in {\mathbb{R}}^{n_{true} \times {({t + \tau})}}$ be a state compatible with the input-output data $(u_{\lbrack 0,{{t + \tau} - 1}\rbrack},y_{\lbrack 0,{{t + \tau} - 1}\rbrack})$ and the true system, i.e., holds. Since $(C_{true},A_{true})$ is observable and $k \geqslant \ell_{true}$, the observability matrix $\Omega_{k - 1}$ of the true system has rank $n_{true}$. This implies that the matrices have full column rank, where we recall that $\Theta_{k - 1}$ is the Toeplitz matrix of Markov parameters of the true system, defined. Therefore, By hypothesis 2, we thus have By \[5, Lemma 23\] and the fact that $(A_{true},B_{true})$ is controllable, Therefore,, we conclude that proving the first item of (a) ‣ Lemma 6. ‣ 6 Online experiment design ‣ The shortest experiment for linear system identification"). The second item of (a) ‣ Lemma 6. ‣ 6 Online experiment design ‣ The shortest experiment for linear system identification") now follows immediately. Finally, to prove the third item, let Let $x_{\lbrack 0,{{t + \tau} - 1}\rbrack} \in {\mathbb{R}}^{n_{\min,{t + \tau}} \times {({t + \tau})}}$ be a state compatible with the input-output data and the above explaining system. Obviously, ${{rank}H_{k,{t + \tau}}} \leqslant {n_{\min,{t + \tau}} + {{({k + 1})}m}}$ and therefore $n_{\min,{t + \tau}} \geqslant n_{true}$. However, since also $n_{\min,{t + \tau}} \leqslant n_{true}$, we obtain $n_{true} = n_{\min,{t + \tau}}$. Finally, it follows from \[5, Equation \] that $\ell_{\min,{t + \tau}} \geqslant \ell_{true}$. Since obviously $\ell_{\min,{t + \tau}} \leqslant \ell_{true}$, we conclude that $\ell_{\min,{t + \tau}} = \ell_{true}$, proving the third item of (a) ‣ Lemma 6. ‣ 6 Online experiment design ‣ The shortest experiment for linear system identification").

Next, we will prove (b) ‣ Lemma 6. ‣ 6 Online experiment design ‣ The shortest experiment for linear system identification"). Assume that $k = L_{t + \tau}^{a}$. We have that where the last inequality follows from \[5, Equation \]. Combining this with $L \geqslant \ell_{true}$, we obtain $k = L_{t + \tau}^{a} \geqslant \ell_{true}$, by definition of $L_{t + \tau}^{a}$. Therefore, the three items listed under (a) ‣ Lemma 6. ‣ 6 Online experiment design ‣ The shortest experiment for linear system identification") hold. From the fact that $\ell_{\min,{t + \tau}} = \ell_{true}$ and $n_{\min,{t + \tau}} = n_{true}$, it follows that $L_{t + \tau}^{a} = L^{a}$, and therefore $k = L^{a}$. This proves the first item of (b) ‣ Lemma 6. ‣ 6 Online experiment design ‣ The shortest experiment for linear system identification"). Moreover, the second item of (a) ‣ Lemma 6. ‣ 6 Online experiment design ‣ The shortest experiment for linear system identification") implies that ${t + \tau} = {L^{a} + {{({L^{a} + 1})}m} + n_{true}}$, which shows that ${t + \tau} = T$, proving the second item of (b) ‣ Lemma 6. ‣ 6 Online experiment design ‣ The shortest experiment for linear system identification"). Finally, from the third item of (a) ‣ Lemma 6. ‣ 6 Online experiment design ‣ The shortest experiment for linear system identification"), we see that ${{rank}H_{L_{T}^{a},T}} = {{{({L_{T}^{a} + 1})}m} + n_{\min,T}}$. Therefore, it follows from Theorem 4 that the data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ are informative for system identification. Therefore, also the third item of (b) ‣ Lemma 6. ‣ 6 Online experiment design ‣ The shortest experiment for linear system identification") holds. This proves the lemma. ∎ The core idea of our approach is to adapt the depth $k$ of the Hankel matrix during the operation of the experiment design procedure. For a *fixed* depth $k$, Lemma 5 will be used for $s \in {\lbrack t,{{t + \tau} - 1}\rbrack}$ until the rank condition ${{rank}G_{k,{t + \tau}}} = {m + {{rank}H_{{k - 1},{t + \tau}}}}$ holds. Then, following Lemma 6, we check whether $k = L_{t + \tau}^{a}$. If $k = L_{t + \tau}^{a}$ then we are done because the data $(u_{\lbrack 0,{{t + \tau} - 1}\rbrack},y_{\lbrack 0,{{t + \tau} - 1}\rbrack})$ are informative for system identification. Otherwise, if $k \neq L_{t + \tau}^{a}$ we increase the depth of the Hankel matrix to $k + 1$ and repeat the process. This leads to the following algorithm.

2: choose $u_{\lbrack 0,{m - 1}\rbrack}$ to be nonsingular 3: measure outputs $y_{\lbrack 0,{m - 1}\rbrack}$ 5: while $k \neq L_{t}^{a}$ do$\rhd$ stopping criterion 12: while ${{rank}G_{k,t}} < {m + {{rank}H_{{k - 1},t}}}$ do 13: choose ${u{(t)}} \notin \mathcal{A}_{t}$ 14: measure output $y{(t)}$ $\rhd$ ${{rank}H_{k,{t + 1}}} = {{{rank}H_{k,t}} + 1}$ 18: return $(u_{\lbrack 0,{t - 1}\rbrack},y_{\lbrack 0,{t - 1}\rbrack})$ 19:$\rhd$ ${(k,t)} = {(L^{a},T)}$ and the data are informative The following theorem asserts that OnlineExperiment$(L,N)$ leads to informative data sets with the least possible number of samples. This is the main result of the paper.

### Theorem 7

The procedure OnlineExperiment$(L,N)$ returns input-output data $(u_{\lbrack 0,{t - 1}\rbrack},y_{\lbrack 0,{t - 1}\rbrack})$ that are informative for system identification. Moreover, $t = T$, where $T$ is defined .

Before we prove Theorem 7, we state the following auxiliary lemma.

### Lemma 8

Let $k \geqslant 0$ and $t \geqslant {k + 2}$. If the data $(u_{\lbrack 0,{t - 1}\rbrack},y_{\lbrack 0,{t - 1}\rbrack})$ are such that $H_{k,t}$ has full column rank then also $H_{{k + 1},t}$ has full column rank.

### Proof

Since $H_{k,t}$ has full column rank, the submatrix obtained from removing the first column of $H_{k,t}$, has full column rank as well. Since is also the submatrix of $H_{{k + 1},t}$ obtained by removing the row blocks $u_{\lbrack 0,{t - k - 2}\rbrack}$ and $y_{\lbrack 0,{t - k - 2}\rbrack}$, we conclude that $H_{{k + 1},t}$ has full column rank. This proves the lemma. ∎

### Proof of Theorem 7

The proof consists of the following three steps. First, we prove that the Hankel matrix $H_{k,t}$ always has full column rank at the start of the while loop in Line 12. Secondly, we prove that the procedure terminates within a finite number of steps. Finally, we show that the latter number is precisely equal to $T$, and the data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ are informative for system identification.

We begin with the first step. Consider the $k$-th iteration of the while loop in Lines 5-17. Let $t_{k}$ be the time instant at the start of the while loop in Line 12. We claim that $H_{k,t_{k}}$ has full column rank.

We first prove this claim for the first iteration of the while loop, i.e., consider $k = 1$. If $m \geqslant 2$ then the if statement in Lines 7-11 is ignored, and $t_{1} = m$. Note that the Hankel matrix $H_{0,m}$ has full column rank by the choice of the inputs $u_{\lbrack 0,{m - 1}\rbrack}$ in Line 2. It is then clear that $H_{1,t_{1}}$ has full column rank by Lemma 8. On the other hand, if $m = 1$, then $t_{1} = {m + 1}$. In this case, the Hankel matrix $H_{1,{m + 1}}$ has one column, which is nonzero due to line 2. Therefore, also in this case $H_{1,t_{1}}$ has full column rank.

Now consider any iteration $k \geqslant 1$ of the while loop in Lines 5-17. Assume that $H_{k,t_{k}}$ has full column rank. Our goal is to show that $H_{{k + 1},t_{k + 1}}$ has full column rank as well.

Consider the $k$-th iteration of the while loop in Lines 5-17. Since $H_{k,t_{k}}$ has full column rank by hypothesis, we can apply Lemma 5 to the while loop in Lines 12-16. In particular, this while loop is applied for a finite number of iterations, say $\tau \in {\mathbb{N}}$, which yields the Hankel matrix $H_{k,{t_{k} + \tau}}$. By repeated application of Lemma 5, $H_{k,{t_{k} + \tau}}$ has full column rank. This means, in particular, that ${t_{k} + \tau} \geqslant {k + 1}$.

Now, we turn our attention to the $({k + 1})$-th iteration of the while loop in Lines 5-17. If ${t_{k} + \tau} = {k + 1}$ then the if statement in Lines 7-11 generates an arbitrary input $u{({t_{k} + \tau})}$ and corresponding output $y{({t_{k} + \tau})}$. In this case, $t_{k + 1} = {t_{k} + \tau + 1}$ and the resulting Hankel matrix $H_{{k + 1},t_{k + 1}}$ is a column vector of rank one by Line 2. In the other case, if ${t_{k} + \tau} > {k + 1}$ then $t_{k + 1} = {t_{k} + \tau}$ and it follows that $H_{{k + 1},t_{k + 1}}$ has full column rank by Lemma 8.

Secondly, we prove that the procedure terminates in a finite number of steps. Now, let $t_{k} \in {\mathbb{N}}$ be the time instant, corresponding to the depth $k$, at which the stopping criterion in Line 5 is checked. We want to prove the existence of a depth $k \geqslant 0$ such that $k = L_{t_{k}}^{a}$. Clearly, since $L_{t_{k}}^{a} \geqslant \ell_{true}$, this cannot happen if $k < \ell_{true}$. For any $k \geqslant \ell_{true}$ we have that $\ell_{\min,t_{k}} = \ell_{true}$ and $n_{\min,t_{k}} = n_{true}$ by Lemma 6(a) ‣ Lemma 6. ‣ 6 Online experiment design ‣ The shortest experiment for linear system identification"), meaning that $L_{t_{k}}^{a} = L^{a}$. Since the depth $k$ is increased by one in every iteration of the while loop in Lines 5-17, this implies that there exists $k \geqslant \ell_{true}$ such that $k = L_{t_{k}}^{a}$.

Finally, we prove the last step. Let $k$ be such that $k = L_{t_{k}}^{a}$. It follows from Lemma 6(b) ‣ Lemma 6. ‣ 6 Online experiment design ‣ The shortest experiment for linear system identification") that $t_{k}$ is precisely equal to $T$, and the data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ are informative for system identification. This proves the theorem. ∎

### Remark 9

Without going into details, we mention that Theorem 7 shows that "randomly" chosen inputs $u_{\lbrack 0,{T - 1}\rbrack}$ lead to informative experiments of length precisely $T$ with high probability. In fact, the only imposed constraints on the inputs are that $u_{\lbrack 0,{m - 1}\rbrack}$ is nonsingular (Line 2 of the algorithm), and that ${u{(t)}} \in {\mathbb{R}}^{m}$ is not a member of an $({m - 1})$-dimensional affine set (Line 13). Regardless of how the inputs are chosen to satisfy these constraints, however, a crucial aspect of OnlineExperiment$(L,N)$ is its stopping criterion. Indeed, we emphasize that $T$ is not a priori known but has to be deduced from data.

## Illustrative example

In this section we illustrate OnlineExperiment$(L,N)$ by means of an example. Consider the true system so that $n_{true} = 3$, $m = 2$, $p = 2$, and $\ell_{true} = 2$. Let $x_{0} = \begin{bmatrix} \end{bmatrix}^{\top}$. Moreover, let $L = 4$ and $N = 4$ be the available upper bounds.

### Online experiment

We now apply OnlineExperiment$(L,N)$. We start with $k = 0$. We choose $u_{\lbrack 0,1\rbrack} = I$, which is obviously nonsingular, and measure Using these data and Proposition 3, we compute Since $k \neq L_{2}^{a}$, we increase $k$ to $k = 1$. The inputs are now designed according to the while loop in Line 12 as: resulting in the measured outputs It can be checked that we have increased the rank of the depth-$1$ Hankel matrix from ${{rank}H_{1,3}} = 2$ to ${{rank}H_{1,8}} = 7$. Based on the data thusfar, we use Proposition 3 to compute: Since $k \neq L_{8}^{a}$, we set $k = 2$. Following the while loop in Line 12, we construct By doing so, we have increased the rank of the depth-$2$ Hankel matrix from ${{rank}H_{2,9}} = 7$ to ${{rank}H_{2,11}} = 9$. Again, we compute: Since $k \neq L_{11}^{a}$ we set $k = 3$. This time, we apply the while loop in Line 12 to obtain the data The rank of the depth-$3$ Hankel matrix has increased from ${{rank}H_{3,12}} = 9$ to ${{rank}H_{3,14}} = 11$. Finally, we compute Since $k = L_{14}^{a}$, the procedure terminates. We conclude that $T = 14$ and the data $(u_{\lbrack 0,13\rbrack},y_{\lbrack 0,13\rbrack})$ are informative for system identification. For this example, we note that the required number of samples $T$ is less than the experiment design approach in that works with the *fixed* depth $L = 4$ Hankel matrix. However, this is not always the case. For example, if we study the same example but with the given upper bounds $L = 3$ and $N = 6$, we can use OnlineExperiment$(L,N)$ to generate the same informative data, with the only difference that we now have $L_{2}^{a} = 3$. In this case, the number of $T = 14$ data samples is the same as.

### PE of order $L^{a} + 1$ is not sufficient for informativity

According to Theorem 4, an obvious necessary condition for informativity is that the inputs are *persistently exciting of order $L^{a} + 1$*. This condition, however, is not sufficient as demonstrated next. We use the same example as above, but just change $u{}$ from $\begin{bmatrix} \end{bmatrix}$ to $\begin{bmatrix} \end{bmatrix}$, i.e., we choose the inputs as The corresponding outputs are then given by In this case, ${{{rank}H_{3}}{(u_{\lbrack 0,13\rbrack})}} = 8$ so $u_{\lbrack 0,13\rbrack}$ is persistently exciting of order $L^{a} + 1$. However ${{rank}H_{3,14}} = 10 \neq 11$ so the conditions of Theorem 4 are not satisfied.

## Comparison to previous work

The proposed online experiment design method largely improves the (offline) persistency of excitation condition of the fundamental lemma (see Proposition 1). Indeed, recall that the input $u_{\lbrack 0,{t - 1}\rbrack}$ can only be *persistently exciting* of order $N + L + 1$ if $t \geqslant {N + L + {m{({N + L + 1})}}}$. In general, this lower bound on the number of data samples is much larger than $T$ . For example, if $m = 80$, $p = 10$, $\ell_{true} = 20$, $n_{true} = 100$, $L = 100$ and $N = 150$, the online experiment design method requires $T = 5850$ samples whereas persistency of excitation requires $t \geqslant 20330$ samples.

The proposed approach also improves the online experiment design of. In fact, in the latter paper a method was given to guarantee that the Hankel matrix $H_{L}$ of *fixed depth* $L$ has rank ${{({L + 1})}m} + n_{true}$. This was done in the least possible number of time steps, $t = {L + {{({L + 1})}m} + n_{true}}$. However, by Theorem 4, the condition ${{rank}H_{L}} = {{{({L + 1})}m} + n_{true}}$ is sufficient for informativity for system identification, but in general not necessary. In particular, if $L^{a} < L$ then the experiment design method of this paper leads to a shorter experiment for system identification than the one provided . If $L^{a} = L$, then the number of samples coincides .

## Conclusions

In this paper we have proposed an experiment design method that leads to input-output data that are informative for system identification. The key features of the approach are i) it is *online*, meaning that the design of the inputs is guided by data collected at previous time steps, and ii) it *adapts the depth* of the input-output Hankel matrix during the operation of the algorithm. We have shown that this approach leads to informative sequences of input-output samples of the shortest possible length. Interestingly, the exact number of samples in such a shortest experiment cannot be determined a priori, but is only revealed after the termination of the procedure. The online experiment design method improves over methods based on persistent excitation by significantly reducing the required number of data samples for system identification. The results of this paper have also revealed that the online experiment design method of yields the shortest experiment for system identification only in *some* cases. In situations where the data-based bound on the lag of the system is smaller than the a priori given bound, the experiment design method of this paper outperforms.
