## Introduction

Background. J.C. Willems' trilogy \[(https://arxiv.org/html/2405.18962v1#bib.bib1), (https://arxiv.org/html/2405.18962v1#bib.bib2), (https://arxiv.org/html/2405.18962v1#bib.bib3)\] is one of broader, deeper, and more influential studies about mathematical modelling of dynamical systems from time series. The second part \[(https://arxiv.org/html/2405.18962v1#bib.bib2)\] concerns the problem of obtaining a mathematical model for a linear system from a given (infinite) trajectory. It significantly influenced subspace identification methods \[(https://arxiv.org/html/2405.18962v1#bib.bib4)\], that compute a state sequence from finite-length data by adapting Willems' state construction from infinite- to finite-length data. Two assumptions are crucial in \[(https://arxiv.org/html/2405.18962v1#bib.bib4)\]: the state space dimension of the system is known; and a rank condition holds for a Hankel matrix constructed from the data. Although not formally proven at the time, it was believed that such rank condition is satisfied if the input data are sufficiently persistently exciting. This conjecture was formally proven in Willems et. al.'s *fundamental lemma* (\[(https://arxiv.org/html/2405.18962v1#bib.bib5), Thm. 1\]) which allows the application of subspace identification even when only an upper bound on the state dimension is known.

The fundamental lemma parameterizes all trajectories of a system from a single sufficiently informative one. This parameterization was applied in linear quadratic control \[(https://arxiv.org/html/2405.18962v1#bib.bib6)\], simulation \[(https://arxiv.org/html/2405.18962v1#bib.bib7)\], model reduction of dissipative systems \[(https://arxiv.org/html/2405.18962v1#bib.bib8)\], and predictive control \[(https://arxiv.org/html/2405.18962v1#bib.bib9)\]. More recently, this approach has gained significant momentum, initiated by papers such as \[(https://arxiv.org/html/2405.18962v1#bib.bib10), (https://arxiv.org/html/2405.18962v1#bib.bib11), (https://arxiv.org/html/2405.18962v1#bib.bib12), (https://arxiv.org/html/2405.18962v1#bib.bib13)\] and followed by many contributions addressing a variety of data-driven analysis and control problems.

The recent surge in popularity of this parameterization has also revived the interest in the fundamental lemma itself. Its original proof was presented in the language of behavioral systems; an alternative proof for state space systems was provided in \[(https://arxiv.org/html/2405.18962v1#bib.bib14)\]. The original proof and that in \[(https://arxiv.org/html/2405.18962v1#bib.bib14)\] are by contradiction; a direct proof was presented in \[(https://arxiv.org/html/2405.18962v1#bib.bib15)\] for single-input systems. Generalizations to uncontrollable systems are in \[(https://arxiv.org/html/2405.18962v1#bib.bib16), (https://arxiv.org/html/2405.18962v1#bib.bib17), (https://arxiv.org/html/2405.18962v1#bib.bib15)\] and extensions to continuous-time systems in \[(https://arxiv.org/html/2405.18962v1#bib.bib18), (https://arxiv.org/html/2405.18962v1#bib.bib19), (https://arxiv.org/html/2405.18962v1#bib.bib20), (https://arxiv.org/html/2405.18962v1#bib.bib21)\]. Quantitative/robust variations are explored in \[(https://arxiv.org/html/2405.18962v1#bib.bib22), (https://arxiv.org/html/2405.18962v1#bib.bib23)\], frequency domain formulations in \[(https://arxiv.org/html/2405.18962v1#bib.bib24), (https://arxiv.org/html/2405.18962v1#bib.bib25)\], and online experiment design in \[(https://arxiv.org/html/2405.18962v1#bib.bib26)\]. Furthermore, the fundamental lemma has been generalized beyond linear systems to include various other model classes: descriptor systems \[(https://arxiv.org/html/2405.18962v1#bib.bib27)\], flat nonlinear systems \[(https://arxiv.org/html/2405.18962v1#bib.bib28)\], linear parameter-varying systems \[(https://arxiv.org/html/2405.18962v1#bib.bib29)\], and stochastic ones \[(https://arxiv.org/html/2405.18962v1#bib.bib30)\].

Contributions. The fundamental lemma gives a *sufficient* condition for identifiability (in the sense of \[(https://arxiv.org/html/2405.18962v1#bib.bib5), (https://arxiv.org/html/2405.18962v1#bib.bib31)\]); in this paper we investigate necessary and sufficient conditions on finite input-output data for identifiability of an unknown minimal input-state-output (ISO) system whose lag and state space dimension lie between given lower and upper bounds. Our main contributions are:

Using the concept of *data informativity* (see \[(https://arxiv.org/html/2405.18962v1#bib.bib32), (https://arxiv.org/html/2405.18962v1#bib.bib33)\]), we develop a framework for ISO system identification from finite input-output data, incorporating a priori knowledge or assumptions (Section (https://arxiv.org/html/2405.18962v1#S3 "3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system")). While currently limited to exact (deterministic) identification problems, such framework is of broader potential interest, for example in approximate modelling and for noisy data.

We characterize (Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem8 "Theorem 8. ‣ 4.4 The shortest lag and the minimum number of states ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) the shortest lag $\ell_{\min}$ and the minimum number of states $n_{\min}$, that an ISO system capable of generating the data must have. These integers can be computed *directly from the data*.

We compute an ISO system whose lag and state dimension are exactly $\ell_{\min}$ and $n_{\min}$ using a novel construction of a state trajectory from data (Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem7 "Theorem 7. ‣ 4.3 Constructing an explaining system ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) that does not rely on assumptions on the length of the data set.

We establish an inequality (see ((https://arxiv.org/html/2405.18962v1#S4.E17 "In 4.5 Sharpening the upper bound on the true lag ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system"))) relating the lag and state dimension of any data-generating system to $\ell_{\min}$ and $n_{\min}$. With such inequality we compute a sharper upper bound on the lag than the one given a priori.

Assuming a priori knowledge about minimality and lower and upper bounds on lag and state dimension, we state *necessary and sufficient* conditions on finite input-output data to guarantee unique identification modulo state isomorphism (Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem9 "Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")). Such conditions are formulated in terms of the rank of a Hankel matrix constructed from the input-output data, whose depth is determined by the input-output data themselves.

Relation with previous results. As in deterministic subspace identification methods (see \[(https://arxiv.org/html/2405.18962v1#bib.bib4), (https://arxiv.org/html/2405.18962v1#bib.bib34), (https://arxiv.org/html/2405.18962v1#bib.bib35)\]), our approach is also based on directly computing a state trajectory from input-output data. Our procedure (see Section (https://arxiv.org/html/2405.18962v1#S7 "7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")) is also related to the intersection of "past" and "future" crucial in subspace identification (see \[(https://arxiv.org/html/2405.18962v1#bib.bib34), Sect. 2.3.1\]). The issues arising when working with *finite-length* data, however, seem to have been only touched upon in the subspace literature (see \[(https://arxiv.org/html/2405.18962v1#bib.bib34), p. 34\] and before the statement \[(https://arxiv.org/html/2405.18962v1#bib.bib4), Thm. 2\]). It is assumed that the data length is "sufficiently large" to guarantee that the data Hankel matrix contains enough information on the dynamics of an explaining model, but a *complete* characterization of such property such as given in the present paper is absent.

Our approach is conceptually and methodologically closest to the behavioral one (see \[(https://arxiv.org/html/2405.18962v1#bib.bib2), (https://arxiv.org/html/2405.18962v1#bib.bib5), (https://arxiv.org/html/2405.18962v1#bib.bib36)\]). Instrumental to our results is the definition of a number of integer invariants computed directly from the data and associated with explaining models. Such integers are the finite data counterparts of those introduced in \[(https://arxiv.org/html/2405.18962v1#bib.bib1), Sect. 7\] for infinite time series. Moreover, the fundamental lemma is a *special case* of our results (see Proposition (https://arxiv.org/html/2405.18962v1#Thmtheorem4 "Proposition 4. ‣ 3.3 Two relevant results ‣ 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system"), Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem9 "Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system"), and Section [9.2](https://arxiv.org/html/2405.18962v1#S9.SS2 "9.2 Proposition 4 vs. Theorem 9 ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")), and we show that one can identify the unknown system under weaker conditions. Finally, we essentially improve the fundamental lemma as follows. Identification based on the fundamental lemma is offline: a sufficiently rich input signal is applied, the corresponding output response is measured, and then identification or trajectory-parametrization is performed. Such offline method does not exploit in *real-time* information from the output samples. In \[(https://arxiv.org/html/2405.18962v1#bib.bib37)\] we use our approach to devise a shortest online experiment for linear system identification. Input values are chosen depending on the past input-output data and are applied *step-by-step*. Such online method requires less data points than the offline one, and it could pave the way to design plug-and-play data-driven controllers.

The authors of \[(https://arxiv.org/html/2405.18962v1#bib.bib36)\] study identifiability from multiple finite-length trajectories without assumptions on the input-output structure. The first similarity with our approach lies in the adoption of the "model class" concept; in \[(https://arxiv.org/html/2405.18962v1#bib.bib36)\] such class is associated with the *complexity* of a model (see \[(https://arxiv.org/html/2405.18962v1#bib.bib36), Section III.B\]). A second similarity lies in the sequential construction of left-annihilators of finite Hankel data matrices, although in \[(https://arxiv.org/html/2405.18962v1#bib.bib36)\] an autoregressive model is computed and we compute an ISO one instead. A fundamental difference is that to compute such annihilators only data Hankel matrices with at least as many columns as rows are used in \[(https://arxiv.org/html/2405.18962v1#bib.bib36)\] (see the definition of $L_{\max}$ on p. 3 therein); our informativity point of view instead allows us to exploit Hankel matrices of *full depth* in constructing a state sequence compatible with the data. Moreover, the identifiability characterization in \[(https://arxiv.org/html/2405.18962v1#bib.bib36), Theorem 17\] is based on a priori knowledge of lag and state dimension (see also Note 18 *ibid.*); ours depends on integers computed *only* and *directly* from the data.

Structure of the paper. In Section (https://arxiv.org/html/2405.18962v1#S2 "2 Notation and preliminaries ‣ Beyond the fundamental lemma: from finite time series to linear system"), we introduce notation, preliminary concepts and definitions. In Section (https://arxiv.org/html/2405.18962v1#S3 "3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system") we formalize the problem. Section (https://arxiv.org/html/2405.18962v1#S4 "4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") contains a summary of our most relevant results and an outline of the logical links among them. In Section (https://arxiv.org/html/2405.18962v1#S5 "5 Illustrative example ‣ Beyond the fundamental lemma: from finite time series to linear system") we illustrate such results on an example.

Our main result is Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem9 "Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") to whose proof, based on some intermediate results of independent interest, we devote the rest of the manuscript. In Section (https://arxiv.org/html/2405.18962v1#S6 "6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system") we introduce and study lag structures of explaning systems. Section (https://arxiv.org/html/2405.18962v1#S7 "7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system") contains a new iterative state construction from input-output data, from which an explaining system is straightforwardly derived. State-input data Hankel matrices and their properties are studied in Section (https://arxiv.org/html/2405.18962v1#S8 "8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system"). In Section (https://arxiv.org/html/2405.18962v1#S9 "9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system") we present two ways of constructing an explaining system from a given one. We discuss future work in Section (https://arxiv.org/html/2405.18962v1#S10 "10 Conclusions ‣ Beyond the fundamental lemma: from finite time series to linear system").

## Notation and preliminaries

### Vectors and matrices

The space of $n$-dimensional real vectors is denoted by ${\mathbb{R}}^{n}$; the space of $n \times m$ matrices with real entries by ${\mathbb{R}}^{n \times m}$.

We denote the $n \times n$ identity matrix by $I_{n}$ and the $m \times n$ zero matrix by $0_{m,n}$ whereas $0_{n}$ denotes the $n$-vector of zeros. For partitioned matrices containing zero and/or identity submatrices, we do not explicitly indicate the sizes of blocks that can be deduced from the matrix structure.

Given matrices $M_{i}$, $i = {1,2,\ldots,k}$ with the same number of columns, we denote $\begin{bmatrix}
\end{bmatrix}^{T}$ by ${col}\left( M_{1},M_{2},\ldots,M_{k} \right)$. Given $M \in {\mathbb{R}}^{m \times n}$, we denote its kernel by ${\ker M}:=\left\{ {x \in {\mathbb{R}}^{n}}:{{Mx} = 0_{m}} \right\}$, its *row space* by ${{rsp}M}:=\left\{ {vM}:{v \in {\mathbb{R}}^{1 \times m}} \right\}$ and its *left kernel* by ${{{lker}M}:=\left\{ {v \in {\mathbb{R}}^{1 \times m}}:{{vM} = 0_{1,n}} \right\}}.$

We denote the zero subspace of ${\mathbb{R}}^{1 \times n}$ by $\mathbf{0}_{n}$.

### Void matrices

A void matrix is a matrix with zero rows and/or zero columns. We denote by $0_{n,0}$ and $0_{0,m}$ respectively the $n \times 0$ and $0 \times m$ void matrices. If $M$ and $N$ are, respectively $p \times q$ and $q \times r$ matrices, $MN$ is a $p \times r$ void matrix if $p = 0$ or $r = 0$ and ${MN} = 0_{p,r}$ if ${p,r} \geqslant 1$ and $q = 0$. The rank of a void matrix is defined to be zero.

### Integer intervals and Hankel matrices

The set of integers is denoted by $\mathbb{Z}$ and the set of nonnegative integers by $\mathbb{N}$.

Given ${i,j} \in {\mathbb{Z}}$ with $i \leqslant j$, we write $\lbrack i,j\rbrack$ to denote the ordered set of all integers between $i$ and $j$ both included. By convention, ${\lbrack i,j\rbrack} = \varnothing$ if $i > j$.

Let ${i,j} \in {\mathbb{N}}$, $i \leqslant j$; let $f_{k} \in {\mathbb{R}}^{n}$ with $k \in {\lbrack i,j\rbrack}$. We define

For $k \in {\lbrack 0,{j - i}\rbrack}$, the *Hankel matrix with depth $k + 1$ associated with $f_{\lbrack i,j\rbrack}$* is defined by:

### Input-state-output systems

We work with linear discrete-time ISO systems

${\mathbf{x}}{({t + 1})}$ $= {{A{\mathbf{x}}{(t)}} + {B{\mathbf{u}}{(t)}}}$ (1a)
${\mathbf{y}}{(t)}$ $= {{C{\mathbf{x}}{(t)}} + {D{\mathbf{u}}{(t)}}}$ (1b)

where $n \geqslant 0$, ${m,p} \geqslant 1$, $A \in {\mathbb{R}}^{n \times n}$, $B \in {\mathbb{R}}^{n \times m}$, $C \in {\mathbb{R}}^{p \times n}$, and $D \in {\mathbb{R}}^{p \times m}$. If $n = 0$, we call the system memoryless.

For $k \geqslant {- 1}$, we define the *$k$-th observability matrix* by

We denote the smallest integer $k \geqslant 0$ such that ${{rank}\Omega_{k}} = {{rank}\Omega_{k - 1}}$ by $\ell{(C,A)}$. Note that $0 \leqslant {\ell{(C,A)}} \leqslant n$; if $n = 0$, then ${\ell{(C,A)}} = 0$. If $(C,A)$ is observable, then $\ell{(C,A)}$ is the observability index. We call $\ell{(C,A)}$ the *lag* of the system; on this terminology, see statement (vii) of \[(https://arxiv.org/html/2405.18962v1#bib.bib1), Thm. 6\].

### Systems with $m$ inputs and $p$ outputs

We associate with ((https://arxiv.org/html/2405.18962v1#S2.E1 "In 2.4 Input-state-output systems ‣ 2 Notation and preliminaries ‣ Beyond the fundamental lemma: from finite time series to linear system")) the matrix $\begin{bmatrix}
\end{bmatrix}$. Given $m \geqslant 1$ and $p \geqslant 1$, we denote the set of all systems with lag $\ell$ and $n$ state variables by

### Isomorphic systems

Two systems $\begin{bmatrix}
\end{bmatrix} \in {\mathcal{S}{(n)}}$, $i = {1,2}$ are isomorphic if $D_{1} = D_{2}$ and there exists a nonsingular matrix $S \in {\mathbb{R}}^{n \times n}$ such that $A_{1} = {S^{- 1}A_{2}S}$, $B_{1} = {S^{- 1}B_{2}}$, $C_{1} = {C_{2}S}$. We say that $\mathcal{S}^{\prime} \subseteq {\mathcal{S}{(n)}}$ has the isomorphism property if all systems belonging to $\mathcal{S}^{\prime}$ are isomorphic to each other. By convention, the empty set has the isomorphism property.

## Problem formulation

Consider a linear discrete-time input-state-output system

${\mathbf{x}}{({t + 1})}$ $= {{A_{true}{\mathbf{x}}{(t)}} + {B_{true}{\mathbf{u}}{(t)}}}$ (3a)
${\mathbf{y}}{(t)}$ $= {{C_{true}{\mathbf{x}}{(t)}} + {D_{true}{\mathbf{u}}{(t)}}}$ (3b)

where $n_{true} \geqslant 0$, $A_{true} \in {\mathbb{R}}^{n_{true} \times n_{true}}$, $B_{true} \in {\mathbb{R}}^{n_{true} \times m}$, $C_{true} \in {\mathbb{R}}^{p \times n_{true}}$, and $D_{true} \in {\mathbb{R}}^{p \times m}$. We refer to ((https://arxiv.org/html/2405.18962v1#S3.E3 "In 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system")) as the true system. We denote its lag by $\ell_{true}:={\ell{(C_{true},A_{true})}}$. Throughout the paper, we assume that the true system is minimal, i.e. both observable and controllable.

Let $T \geqslant 1$ and $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ be input-output data generated by ((https://arxiv.org/html/2405.18962v1#S3.E3 "In 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system")): there exists $x_{\lbrack 0,T\rbrack} \in {\mathbb{R}}^{n_{true} \times {({T + 1})}}$ such that

A fundamental problem in system identification is under what conditions and how the system ((https://arxiv.org/html/2405.18962v1#S3.E3 "In 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system")) can be uniquely determined from $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ (up to state isomorphisms). In this paper we examine such questions assuming prior knowledge about the unknown system ((https://arxiv.org/html/2405.18962v1#S3.E3 "In 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system")). To formalize such problem we need to introduce some terminology and notation.

### Explaining systems

A system $\begin{bmatrix}
\end{bmatrix} \in {\mathcal{S}{(n)}}$ explains $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ if there exists $x_{\lbrack 0,T\rbrack} \in {\mathbb{R}}^{n \times {({T + 1})}}$ such that

The set of all systems that explain the data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ is denoted by $\mathcal{E}$ and is called the set of explaining systems. The subsets of $\mathcal{E}$ consisting of systems with a given lag and state space dimension are denoted by

It is straightforward to verify that $\mathcal{E}{(\ell,n)}$ and $\mathcal{E}{(n)}$ are invariant under state space transformations. In addition, it follows from ((https://arxiv.org/html/2405.18962v1#S3.E4 "In 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system")) that $\begin{bmatrix}
\end{bmatrix} \in {\mathcal{E}{(\ell_{true},n_{true})}} \subseteq {\mathcal{E}{(n_{true})}}$.

### Informativity for system identification

The available prior knowledge is formalized through a subclass of systems $\mathcal{S}_{pk} \subseteq \mathcal{S}$ (with $\begin{bmatrix}
\end{bmatrix} \in \mathcal{S}_{pk}$), that encapsulates what is known a priori about the true system ((https://arxiv.org/html/2405.18962v1#S3.E3 "In 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system")).

### Definition 1

The data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ are informative for system identification within $\mathcal{S}_{pk}$ if

${\mathcal{E} \cap \mathcal{S}_{pk}} = {{\mathcal{E}{(n_{true})}} \cap \mathcal{S}_{pk}}$, and

$\mathcal{E} \cap \mathcal{S}_{pk}$ has isomorphism property.

Condition (i) states that all explaining systems in $\mathcal{S}_{pk}$ have $n_{true}$ states, and (ii) that they are isomorphic to each other.

In the rest of the paper, we assume that *lower* and *upper bounds* on the *true lag* and *state dimension* are given:

Of particular interest are those systems whose lags and state dimensions are within the given lower and upper bounds:

The main results of this paper concern the informativity of the data for system identification within the prior knowledge class

In this case Definition (https://arxiv.org/html/2405.18962v1#Thmtheorem1 "Definition 1. ‣ 3.2 Informativity for system identification ‣ 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system") can be streamlined. Define

the proof of the following result is straightforward.

### Proposition 2

The data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ are informative for system identification within $\mathcal{S}_{{\lbrack L_{-},L_{+}\rbrack},{\lbrack N_{-},N_{+}\rbrack}} \cap \mathcal{M}$ if and only if

${\mathcal{E}_{{\lbrack L_{-},L_{+}\rbrack},{\lbrack N_{-},N_{+}\rbrack}} \cap \mathcal{M}} = {{\mathcal{E}{(n_{true})}} \cap \mathcal{M}}$, and

${\mathcal{E}{(n_{true})}} \cap \mathcal{M}$ has isomorphism property.

### Problem 3

Given $T > 0$; $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ generated by a system ((https://arxiv.org/html/2405.18962v1#S3.E3 "In 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system")); ${L_{-},L_{+},N_{-},N_{+}} \in {\mathbb{N}}$ satisfying ((https://arxiv.org/html/2405.18962v1#S3.E6 "In 3.2 Informativity for system identification ‣ 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system")); the model class $\mathcal{S}_{pk}$ in ((https://arxiv.org/html/2405.18962v1#S3.E7 "In 3.2 Informativity for system identification ‣ 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system")), establish necessary and sufficient conditions for informativity for system identification within $\mathcal{S}_{pk}$.

### Two relevant results

We state \[(https://arxiv.org/html/2405.18962v1#bib.bib5), Thm. 1\] in our framework.

### Proposition 4

Suppose that $\ell_{true} \geqslant 1$ and

If $u_{\lbrack 0,{T - 1}\rbrack}$ is persistently exciting of order $L_{+} + N_{+}$, that is,

and the data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ are informative for system identification within $\mathcal{S}_{{\lbrack 1,L_{+}\rbrack},{\lbrack 1,N_{+}\rbrack}} \cap \mathcal{M}$.

We state \[(https://arxiv.org/html/2405.18962v1#bib.bib36), Th.m 17\] in our framework.

### Proposition 5

Suppose that $\ell_{true} \geqslant 1$ and

Then, the data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ are informative for system identification within ${\mathcal{S}{(\ell_{true},n_{true})}} \cap \mathcal{M}$ if and only if

## Main results

Informativity for system identification within ((https://arxiv.org/html/2405.18962v1#S3.E7 "In 3.2 Informativity for system identification ‣ 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system")) is related to the rank of a Hankel matrix constructed from the data. We show that the depth of such Hankel matrix is determined by the data and by the bounds $L_{+}$ and $N_{+}$. To state such condition we need to introduce some more notation and terminology.

### Data Hankel matrices

For $k \in {\lbrack 0,{T - 1}\rbrack}$, we denote the *Hankel matrix of depth $k$* constructed from the data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ by $H_{k}$ and the matrix obtained from $H_{k}$ by deletion of its last $p$ rows by $G_{k}$:

Note that $H_{k} \in {\mathbb{R}}^{{{({k + 1})}{({m + p})}} \times {({T - k})}}$ and that $G_{k}$ is a ${({{{({k + 1})}m} + {kp}})} \times {({T - k})}$ matrix. We use the following sequence of integers to state several intermediate results towards necessary and sufficient conditions for data informativity:

and note that

Throughout the paper, we assume that

then $1 = {{rank}H_{T - 1}} = {{rank}G_{T - 1}}$ and hence

### Lags and state dimensions of explaining systems

Let $q \in {\lbrack 0,{T - 1}\rbrack}$ be the smallest integer such that $\delta_{q} = 0$:

Note that $q$ is well-defined due to ((https://arxiv.org/html/2405.18962v1#S4.E12 "In 4.1 Data Hankel matrices ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")). In our first intermediate result we establish bounds on the lag and state dimension of any explaining system in terms of the $\delta_{k}$'s.

### Theorem 6

Suppose that ${\mathcal{E}{(\ell,n)}} \neq \varnothing$. The following statements hold:

If $T \geqslant {\ell + 1}$, then $\ell \geqslant q$.

If $\ell \geqslant q$, then ${n - {\sum_{i = 0}^{q}\delta_{i}}} \geqslant {\ell - q}$.

The proof of this theorem is given in Section [6.3](https://arxiv.org/html/2405.18962v1#S6.SS3 "6.3 Proof of Theorem 6 ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system").

### Constructing an explaining system

Our second intermediate result concerns whether one explaining system can be computed from the data. To answer such question, we introduce the notion of state for data.

Let $\begin{bmatrix}
\end{bmatrix} \in {\mathcal{E}{(n)}}$. We say that $x_{\lbrack 0,T\rbrack} \in {\mathbb{R}}^{n \times {({T + 1})}}$ is a state for $\begin{bmatrix}
\end{bmatrix}$ if ((https://arxiv.org/html/2405.18962v1#S3.E5 "In 3.1 Explaining systems ‣ 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system")) is satisfied. We say that $x_{\lbrack 0,T\rbrack}$ is a state for the data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ if it is a state for some $\begin{bmatrix}
\end{bmatrix} \in {\mathcal{E}{(n)}}$.

From ((https://arxiv.org/html/2405.18962v1#S3.E5 "In 3.1 Explaining systems ‣ 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system")), it follows that $x_{\lbrack 0,T\rbrack}$ is a state for the data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ if and only if

Consequently if one state sequence satisfying ((https://arxiv.org/html/2405.18962v1#S4.E14 "In 4.3 Constructing an explaining system ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) is available, one explaining system can be computed by solving ((https://arxiv.org/html/2405.18962v1#S3.E5 "In 3.1 Explaining systems ‣ 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system")). In the next result we show that for any data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ there always exists an explaining system with state dimension $\sum_{i = 0}^{q}\delta_{i}$, and that *all* such systems have lag $q$ (see ((https://arxiv.org/html/2405.18962v1#S4.E13 "In 4.2 Lags and state dimensions of explaining systems ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system"))).

### Theorem 7

$\varnothing \neq {\mathcal{E}{({\sum_{i = 0}^{q}\delta_{i}})}} = {\mathcal{E}{(q,{\sum_{i = 0}^{q}\delta_{i}})}}$.

The proof of Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem7 "Theorem 7. ‣ 4.3 Constructing an explaining system ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") in Section [7.2](https://arxiv.org/html/2405.18962v1#S7.SS2 "7.2 Proof of Theorem 7 ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system") relies on a new iterative state-computation scheme from input-output data.

### The shortest lag and the minimum number of states

We define the shortest lag $\ell_{\min}$ and the minimum number of states $n_{\min}$ required to explain the data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$:

$\ell_{\min}$ and $n_{\min}$ can be computed from the $\delta_{k}$'s and $q$ as follows.

### Theorem 8

Define $q$ by ((https://arxiv.org/html/2405.18962v1#S4.E13 "In 4.2 Lags and state dimensions of explaining systems ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")); then $\ell_{\min} = q$ and $n_{\min} = {\sum_{i = 0}^{\ell_{\min}}\delta_{i}}$. Moreover, ${\mathcal{E}{(n_{\min})}} = {\mathcal{E}{(\ell_{\min},n_{\min})}} \subset \mathcal{O}$.

### Proof

From Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem7 "Theorem 7. ‣ 4.3 Constructing an explaining system ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system"), we see that $q \geqslant \ell_{\min}$ and ${\sum_{i = 0}^{q}\delta_{i}} \geqslant n_{\min}$; to prove the first part of the theorem, it is enough to prove the reverse inequalities. The definition of $q$ implies that $T \geqslant {q + 1}$; consequently $T \geqslant {\ell_{\min} + 1}$. Since ${\mathcal{E}{(\ell_{\min},n)}} \neq \varnothing$ for some $n$ due to the definition of $\ell_{\min}$ in ((https://arxiv.org/html/2405.18962v1#S4.E15 "In 4.4 The shortest lag and the minimum number of states ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")), Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem6 "Theorem 6. ‣ 4.2 Lags and state dimensions of explaining systems ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system").[(a)](https://arxiv.org/html/2405.18962v1#S4.I1.i1 "item (a) ‣ Theorem 6. ‣ 4.2 Lags and state dimensions of explaining systems ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") yields $\ell_{\min} \geqslant q$ and hence $\ell_{\min} = q$. The definition of $n_{\min}$ in ((https://arxiv.org/html/2405.18962v1#S4.E16 "In 4.4 The shortest lag and the minimum number of states ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) implies that ${\mathcal{E}{(\ell,n_{\min})}} \neq \varnothing$ for some $\ell$. Then, Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem6 "Theorem 6. ‣ 4.2 Lags and state dimensions of explaining systems ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system").[(b)](https://arxiv.org/html/2405.18962v1#S4.I1.i2 "item (b) ‣ Theorem 6. ‣ 4.2 Lags and state dimensions of explaining systems ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") implies that ${n_{\min} - {\sum_{i = 0}^{\ell_{\min}}\delta_{i}}} \geqslant {\ell - \ell_{\min}} \geqslant 0$. This proves $n_{\min} \geqslant {\sum_{i = 0}^{\ell_{\min}}\delta_{i}}$ and hence $n_{\min} = {\sum_{i = 0}^{\ell_{\min}}\delta_{i}}$.

To prove the second part, use Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem7 "Theorem 7. ‣ 4.3 Constructing an explaining system ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") to conclude that ${\mathcal{E}{(n_{\min})}} = {\mathcal{E}{(\ell_{\min},n_{\min})}}$. It remains to prove that ${\mathcal{E}{(n_{\min})}} \subset \mathcal{O}$. Suppose on the contrary that $\mathcal{E}{(n_{\min})}$ contains an unobservable system; a Kalman decomposition yields an explaining system with strictly lower state dimension. This contradicts the definition of $n_{\min}$ in ((https://arxiv.org/html/2405.18962v1#S4.E16 "In 4.4 The shortest lag and the minimum number of states ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")). Consequently, all systems in $\mathcal{E}{(n_{\min})}$ are observable: ${\mathcal{E}{(n_{\min})}} \subset \mathcal{O}$.∎

### Sharpening the upper bound on the true lag

Assume that ${\mathcal{E}{(\ell,n)}} \neq \varnothing$; from Theorems (https://arxiv.org/html/2405.18962v1#Thmtheorem6 "Theorem 6. ‣ 4.2 Lags and state dimensions of explaining systems ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system").[(b)](https://arxiv.org/html/2405.18962v1#S4.I1.i2 "item (b) ‣ Theorem 6. ‣ 4.2 Lags and state dimensions of explaining systems ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") and (https://arxiv.org/html/2405.18962v1#Thmtheorem8 "Theorem 8. ‣ 4.4 The shortest lag and the minimum number of states ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") we obtain the immediate but crucial inequality

Such inequality implies that the integer $L_{+}^{d}$ defined by

is an upper bound, purely determined by the data and $N_{+}$, for the lag of every explaining system with at most $N_{+}$ states. Such upper bound yields a sharper upper bound on the lag than $L_{+}$; we can replace the latter by the actual upper bound

since it follows from ((https://arxiv.org/html/2405.18962v1#S4.E17 "In 4.5 Sharpening the upper bound on the true lag ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) that

### Data informativity for system identification

The following is the main result of this paper; sufficiency is proved in Section [8.2](https://arxiv.org/html/2405.18962v1#S8.SS2 "8.2 Proof of Theorem 9: sufficiency part ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system") and necessity in Section [9.1](https://arxiv.org/html/2405.18962v1#S9.SS1 "9.1 Proof of Theorem 9: necessity part ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system").

### Theorem 9

The data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ are informative for system identification within $\mathcal{S}_{{\lbrack L_{-},L_{+}\rbrack},{\lbrack N_{-},N_{+}\rbrack}} \cap \mathcal{M}$ if and only if the following conditions hold:

$$\ell_{\min} \geqslant L_{-}$$ (19a)

Moreover, if the conditions ((https://arxiv.org/html/2405.18962v1#S4.E19 "In Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) are satisfied then

$$\ell_{true} = \ell_{\min}$$ (20a)
$${{\mathcal{E} \cap \mathcal{S}_{{\lbrack L_{-},L_{+}\rbrack},{\lbrack N_{-},N_{+}\rbrack}} \cap \mathcal{M}} = {\mathcal{E}{(n_{\min})}}}.$$ (20c)

Equations ((https://arxiv.org/html/2405.18962v1#S4.E19 "In Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) are *truly data-based* necessary and sufficient condition for informativity for system identification: $\ell_{\min}$ and $n_{\min}$ are computed directly from the data via Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem8 "Theorem 8. ‣ 4.4 The shortest lag and the minimum number of states ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system").

We conclude this section with some remarks on the consequences of Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem9 "Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") and its relation to other results.

### Remark 10

It is not surprising that informativity for system identification involves a rank condition on some Hankel matrix of the data. Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem9 "Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") makes explicit that the depth of such Hankel matrix depends not only on the prior knowledge of the system but also on the given data. ∎

### Remark 11

Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem9 "Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") is applicable even if one of the upper bounds is unknown. Indeed, if only the upper bound $L_{+}$ on the lag is known, but an upper bound $N_{+}$ on the state dimension is not, one can fix $N_{+} = {pL_{+}}$ since $n \leqslant {p\ell}$ for any observable system in $\mathcal{S}{(\ell,n)}$. For such choice it holds that

the first inequality follows from the fact that $n_{\min} \leqslant {p\ell_{\min}}$ as ${\mathcal{E}{(\ell_{\min},n_{\min})}} \subset \mathcal{O}$ (see Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem8 "Theorem 8. ‣ 4.4 The shortest lag and the minimum number of states ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) and the second one from ${L_{+} \geqslant \ell_{true} \geqslant \ell_{\min}}.$ As such, if $N_{+} = {pL_{+}}$ then $L_{+}^{a} = L_{+}$.

Conversely, if an upper bound $N_{+}$ on the state dimension is known but an upper bound $L_{+}$ on the lag is not, one can fix $L_{+} = N_{+}$ since the lag of a system cannot exceed its state dimension. For such choice of $L_{+}$ it holds that

where the inequality follows from the fact that $n_{\min} \geqslant \ell_{\min}$. Therefore, if $L_{+} = N_{+}$ then $L_{+}^{a} = L_{+}^{d}$. ∎

### Remark 12

If $L_{-} = L_{+} = \ell_{true}$ and $L_{+} = N_{+} = n_{true}$ then it is straightforward to see that Proposition (https://arxiv.org/html/2405.18962v1#Thmtheorem5 "Proposition 5. ‣ 3.3 Two relevant results ‣ 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system") is a special case of Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem9 "Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") (see Section [3.3](https://arxiv.org/html/2405.18962v1#S3.SS3 "3.3 Two relevant results ‣ 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system")). It is less straightforward to prove that the rank condition ((https://arxiv.org/html/2405.18962v1#S3.E9 "In Proposition 4. ‣ 3.3 Two relevant results ‣ 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system")) in Proposition (https://arxiv.org/html/2405.18962v1#Thmtheorem4 "Proposition 4. ‣ 3.3 Two relevant results ‣ 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system") implies the conditions in Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem9 "Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system"); we do this in Section [9.2](https://arxiv.org/html/2405.18962v1#S9.SS2 "9.2 Proposition 4 vs. Theorem 9 ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system"). ∎

### Remark 13

Proposition (https://arxiv.org/html/2405.18962v1#Thmtheorem4 "Proposition 4. ‣ 3.3 Two relevant results ‣ 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system") can be applied only if the data length is at least ${L_{+} + N_{+} + {{({L_{+} + N_{+}})}m}} - 1$ whereas Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem9 "Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") can be applied if the data length is at least $L_{+}^{a} + {{({L_{+}^{a} + 1})}m} + n_{true}$. As illustrated in Section (https://arxiv.org/html/2405.18962v1#S5 "5 Illustrative example ‣ Beyond the fundamental lemma: from finite time series to linear system"), the difference between these lengths can be significantly large. ∎

### Remark 14

Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem9 "Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") is important for online experiment design. Assume that $\ell_{true} \geqslant 1$ and that only an upper bound $L_{+}$ is known; the procedure in \[(https://arxiv.org/html/2405.18962v1#bib.bib26), Thm. 3\] constructs a sequence $u_{\lbrack 0,{T - 1}\rbrack}$ with $T = {{{({L_{+} + 1})}m} + L_{+} + n_{true}}$ such that the data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ generated by the true system are informative for system identification in $\mathcal{S}_{{\lbrack 1,L_{+}\rbrack},{\lbrack 1,{pL_{+}}\rbrack}} \cap \mathcal{M}$. Surprisingly, the procedure does not require knowledge of $n_{true}$. For this case $L_{+}^{a} = L_{+}$ (see Remark (https://arxiv.org/html/2405.18962v1# "Remark 11. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")). If $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ are informative for system identification in $\mathcal{S}_{{\lbrack 1,L_{+}\rbrack},{\lbrack 1,{pL_{+}}\rbrack}} \cap \mathcal{M}$, then from ([19d](https://arxiv.org/html/2405.18962v1#S4.E19.4 "In 19 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) and ([20b](https://arxiv.org/html/2405.18962v1#S4.E20.2 "In 20 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) that $T \geqslant {{{({L_{+} + 1})}m} + L_{+} + n_{true}}$. Thus the experiment design procedure in \[(https://arxiv.org/html/2405.18962v1#bib.bib26), Thm. 3\] is minimal in the number of samples required. ∎

### Remark 15

The constructive proof of Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem7 "Theorem 7. ‣ 4.3 Constructing an explaining system ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") and ([20c](https://arxiv.org/html/2405.18962v1#S4.E20.3 "In 20 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) can be used to compute from informative data an explaining system isomorphic to the true system. We show this in Example (https://arxiv.org/html/2405.18962v1# "Example 20 (State construction). ‣ 7.2 Proof of Theorem 7 ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system") after the proof of Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem7 "Theorem 7. ‣ 4.3 Constructing an explaining system ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system"). ∎

### Remark 16

The lower bounds $L_{-}$, $N_{-}$ are inconsequential for data informativity: if the data are informative within $\mathcal{S}_{{\lbrack L_{-},L_{+}\rbrack},{\lbrack N_{-},N_{+}\rbrack}} \cap \mathcal{M}$ then necessarily $\ell_{true} = \ell_{\min}$ and $n_{true} = n_{\min}$ (see ([20a](https://arxiv.org/html/2405.18962v1#S4.E20.1 "In 20 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")), ([20b](https://arxiv.org/html/2405.18962v1#S4.E20.2 "In 20 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system"))) and consequently the data are also informative in $\mathcal{S}_{{\lbrack 0,L_{+}\rbrack},{\lbrack 0,N_{+}\rbrack}} \cap \mathcal{M}$. The converse holds since ${\mathcal{S}_{{\lbrack L_{-},L_{+}\rbrack},{\lbrack N_{-},N_{+}\rbrack}} \cap \mathcal{M}} \subseteq {\mathcal{S}_{{\lbrack 0,L_{+}\rbrack},{\lbrack 0,N_{+}\rbrack}} \cap \mathcal{M}}$. ∎

Before proving Theorems (https://arxiv.org/html/2405.18962v1#Thmtheorem6 "Theorem 6. ‣ 4.2 Lags and state dimensions of explaining systems ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system"), (https://arxiv.org/html/2405.18962v1#Thmtheorem7 "Theorem 7. ‣ 4.3 Constructing an explaining system ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") and (https://arxiv.org/html/2405.18962v1#Thmtheorem9 "Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") we illustrate them with an example.

## Illustrative example

Consider a system ((https://arxiv.org/html/2405.18962v1#S3.E3 "In 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system")) where $n_{true} = 3$, $m = 2$, $p = 2$, and

Note that $\ell_{true} = 2$. Consider the input-output data

One can verify that ((https://arxiv.org/html/2405.18962v1#S3.E4 "In 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system")) is satisfied with the state data

Table (https://arxiv.org/html/2405.18962v1#S5.T1 "Table 1 ‣ 5 Illustrative example ‣ Beyond the fundamental lemma: from finite time series to linear system") presents the values of $\delta_{k}$ integers, $\ell_{\min}$, and $n_{\min}$ for different choices of $T$. The values of $\delta_{k}$ not explicitly indicated are zero: $\delta_{k} = 0$ for every $T \in {\lbrack 4,14\rbrack}$ and $k \in {\lbrack 3,{T - 1}\rbrack}$.

Table 1: δk integers, ℓmin, and nmin for different choices of T

If $L_{+} = \ell_{true}$ and $N_{+} = n_{true}$, a necessary condition for informativity is that $T \geqslant {{{({\ell_{true} + 1})}m} + \ell_{true} + n_{true}}$ (see ([19c](https://arxiv.org/html/2405.18962v1#S4.E19.3 "In 19 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system"))). It follows that if $T < 11$ then $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ is not informative for every $L_{+}$ and $N_{+}$. The symbol '✓' in Table (https://arxiv.org/html/2405.18962v1#S5.T2 "Table 2 ‣ 5 Illustrative example ‣ Beyond the fundamental lemma: from finite time series to linear system") denotes data informativity for different values of $L_{+}$, $N_{+}$, and $T$, as inferred from the fundamental lemma (Proposition (https://arxiv.org/html/2405.18962v1#Thmtheorem4 "Proposition 4. ‣ 3.3 Two relevant results ‣ 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system")) and Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem9 "Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system"). Proposition (https://arxiv.org/html/2405.18962v1#Thmtheorem4 "Proposition 4. ‣ 3.3 Two relevant results ‣ 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system") requires significantly more samples than Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem9 "Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") (see Remark (https://arxiv.org/html/2405.18962v1# "Remark 13. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")): the data $(u_{\lbrack 0,13\rbrack},y_{\lbrack 0,13\rbrack})$ are informative for the case $L_{+} = N_{+} = 4$ (see Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem9 "Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")). To infer informativity via the fundamental lemma, one would need at least ${{L_{+} + N_{+} + {{({L_{+} + N_{+}})}m}} - 1} = 23$ samples.

Table 2: Informativity of the data for different bounds and T

## Lag structures of explaining systems

To prove Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem6 "Theorem 6. ‣ 4.2 Lags and state dimensions of explaining systems ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system"), we first define the lag structure and relate it to the integers $\delta_{k}$.

### The lag structure of a system

Let $\begin{bmatrix}
\end{bmatrix} \in {\mathcal{S}{(\ell,n)}}$. For $k \geqslant {- 1}$, define $\Omega_{k}$ by ((https://arxiv.org/html/2405.18962v1#S2.E2 "In 2.4 Input-state-output systems ‣ 2 Notation and preliminaries ‣ Beyond the fundamental lemma: from finite time series to linear system")) and

We refer to the sequence ${(\rho_{k})}_{k \in {\mathbb{N}}}$ as the lag structure of the system $\begin{bmatrix}
\end{bmatrix}$. The $\rho_{k}$'s are related to a *specific* system; if necessary to resolve ambiguities, we use the notation $\rho_{k}{(C,A)}$.

### Lemma 17

Let $\begin{bmatrix}
\end{bmatrix} \in {\mathcal{S}{(\ell,n)}}$ and ${(\rho_{k})}_{k \in {\mathbb{N}}}$ be its lag structure. The following statements hold:

$p \geqslant \rho_{k} \geqslant 0$ for all $k \geqslant {- 1}$

$\rho_{\ell - 1} \geqslant 1$ and $\rho_{k} = 0$ for all $k \geqslant \ell$,

$n \geqslant {\sum_{i = 0}^{\ell}\rho_{i}}$; if $(C,A)$ is observable then equality holds.

$\rho_{k} \geqslant \rho_{k + 1}$ for all $k \geqslant 0$.

### Proof

The statements [(a)](https://arxiv.org/html/2405.18962v1#S6.I1.i1 "item (a) ‣ Lemma 17. ‣ 6.1 The lag structure of a system ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system") and [(b)](https://arxiv.org/html/2405.18962v1#S6.I1.i2 "item (b) ‣ Lemma 17. ‣ 6.1 The lag structure of a system ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system") readily follow from the definitions of $\rho_{k}$ and the lag. To prove [(c)](https://arxiv.org/html/2405.18962v1#S6.I1.i3 "item (c) ‣ Lemma 17. ‣ 6.1 The lag structure of a system ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system"), note that ${{rank}\Omega_{\ell}} = {\sum_{i = 0}^{\ell}\rho_{i}}$. This proves [(c)](https://arxiv.org/html/2405.18962v1#S6.I1.i3 "item (c) ‣ Lemma 17. ‣ 6.1 The lag structure of a system ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system") since $n \geqslant {{rank}\Omega_{\ell}}$, and equality holds if $(C,A)$ is observable.

To prove [(d)](https://arxiv.org/html/2405.18962v1#S6.I1.i4 "item (d) ‣ Lemma 17. ‣ 6.1 The lag structure of a system ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system"), we first give an alternative characterization of the integers $\rho_{k}$. Let $k \geqslant 0$. Note that ${{rsp}\Omega_{k}} = {{{rsp}\Omega_{k - 1}} + {{rsp}{CA^{k}}}}$ since $\Omega_{k} = \begin{bmatrix}
\end{bmatrix}$. As such, we have ${{rank}\Omega_{k}} = {{{{rank}\Omega_{k - 1}} + {{rank}{CA^{k}}}} - {\dim V_{k}}}$ where $V_{k}:={{{rsp}\Omega_{k - 1}} \cap {{rsp}{CA^{k}}}}$. This leads to the following alternative characterization for $\rho_{k}$:

Now let $k \geqslant 0$ and observe that ${CA^{k + 1}} = {CA^{k}A}$. Apply the rank-nullity theorem and obtain

where $W_{k}:={{{rsp}{CA^{k}}} \cap {{lker}A}}$. By combining ((https://arxiv.org/html/2405.18962v1#S6.E21 "In Proof. ‣ 6.1 The lag structure of a system ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system")) and ((https://arxiv.org/html/2405.18962v1#S6.E22 "In Proof. ‣ 6.1 The lag structure of a system ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system")), we obtain ${\rho_{k} - \rho_{k + 1}} = {{{\dim W_{k}} + {\dim V_{k + 1}}} - {\dim V_{k}}}$. Let $Z_{k}$ be a subspace such that $V_{k} = {{({V_{k} \cap W_{k}})} \oplus Z_{k}}$. Then, we have

Let $d = {\dim Z_{k}}$ and $\eta_{i} \in {\mathbb{R}}^{1 \times n}$ with $i \in {\lbrack 1,d\rbrack}$ be a basis for $Z_{k}$. From the definition of $Z_{k}$, it readily follows that $\eta_{i}A$ are linearly independent and ${\eta_{i}A} \in {{{rsp}{\Omega_{k - 1}A}} \cap {{rsp}{CA^{k + 1}}}} \subseteq {{{rsp}\Omega_{k}} \cap {{rsp}{CA^{k + 1}}}} = V_{k + 1}$. Therefore, ${\dim Z_{k}} \leqslant {\dim V_{k + 1}}$. Hence, it follows from ((https://arxiv.org/html/2405.18962v1#S6.E23 "In Proof. ‣ 6.1 The lag structure of a system ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system")) that $\rho_{k} \geqslant \rho_{k + 1}$ for all $k \geqslant 0$.∎

### Lag structures and $\delta_{k}$ integers

Let $\begin{bmatrix}
\end{bmatrix} \in {\mathcal{S}{(n)}}$. For $k \geqslant {- 1}$, define the *$k$-th controllability matrix*, and the *$k$-th system matrix*, respectively, by

$\Theta_{k}$ is the Toeplitz matrix of the first $k + 1$ Markov parameters of ((https://arxiv.org/html/2405.18962v1#S2.E1 "In 2.4 Input-state-output systems ‣ 2 Notation and preliminaries ‣ Beyond the fundamental lemma: from finite time series to linear system")). Given a state sequence $x_{\lbrack 0,T\rbrack}$ for an explaining system $\begin{bmatrix}
\end{bmatrix} \in {\mathcal{E}{(n)}}$, the data Hankel matrices $H_{k}$ and $G_{k}$ are related to the observability and system matrices by:

\end{bmatrix} = {\Phi_{k}\begin{bmatrix}
\end{bmatrix} = {\Psi_{k}\begin{bmatrix}

We now relate the integers $\delta_{k}$ (defined in terms of the *data matrices* $H_{k}$ and $G_{k}$ only) and the integers $\rho_{k}$ (defined by the matrices $C$ and $A$ of a *specific explaining system*).

### Lemma 18

Let ${(\rho_{k})}_{k \in {\mathbb{N}}}$ be the lag structure of an explaining system. For every $k \in {\lbrack 0,{T - 1}\rbrack}$, $\rho_{k} \geqslant \delta_{k}$.

### Proof

Let $k \in {\lbrack 0,{T - 1}\rbrack}$. Define $J_{k}:=\begin{bmatrix}
{H_{k}\left( u_{\lbrack 0,{T - 1}\rbrack} \right)}
\end{bmatrix}$; by applying the rank-nullity theorem to ((https://arxiv.org/html/2405.18962v1#S6.E26 "In 6.2 Lag structures and 𝛿_𝑘 integers ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system")), we see that

Now ${{{rank}\Phi_{k}} - {{rank}\Psi_{k}}} = {{{rank}\Omega_{k}} - {{rank}\Omega_{k - 1}}}$ and ${{rsp}\Psi_{k}} \subseteq {{rsp}\Phi_{k}}$ from ((https://arxiv.org/html/2405.18962v1#S6.E27 "In 6.2 Lag structures and 𝛿_𝑘 integers ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system")); subtract ((https://arxiv.org/html/2405.18962v1#S6.E29 "In Proof. ‣ 6.2 Lag structures and 𝛿_𝑘 integers ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system")) from ((https://arxiv.org/html/2405.18962v1#S6.E28 "In Proof. ‣ 6.2 Lag structures and 𝛿_𝑘 integers ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system")) to obtain $\rho_{k} \geqslant \delta_{k}$. ∎

We are ready to prove Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem6 "Theorem 6. ‣ 4.2 Lags and state dimensions of explaining systems ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system").

### Proof of Theorem [6](https://arxiv.org/html/2405.18962v1#Thmtheorem6 "Theorem 6. ‣ 4.2 Lags and state dimensions of explaining systems ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")

Let $\begin{bmatrix}
\end{bmatrix} \in {\mathcal{E}{(\ell,n)}}$ and let ${(\rho_{k})}_{k \in {\mathbb{N}}}$ be the lag structure of the system $\begin{bmatrix}
\end{bmatrix}$. To prove [(a)](https://arxiv.org/html/2405.18962v1#S4.I1.i1 "item (a) ‣ Theorem 6. ‣ 4.2 Lags and state dimensions of explaining systems ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system"), note that $\rho_{\ell} = 0$ due to Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 17. ‣ 6.1 The lag structure of a system ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system").[(b)](https://arxiv.org/html/2405.18962v1#S6.I1.i2 "item (b) ‣ Lemma 17. ‣ 6.1 The lag structure of a system ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system"). Since ${T - 1} \geqslant \ell$ by hypothesis, Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 18. ‣ 6.2 Lag structures and 𝛿_𝑘 integers ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system") and ((https://arxiv.org/html/2405.18962v1#S4.E11 "In 4.1 Data Hankel matrices ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) imply that $\delta_{\ell} = 0$. Then $\ell \geqslant q$ from ((https://arxiv.org/html/2405.18962v1#S4.E13 "In 4.2 Lags and state dimensions of explaining systems ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")).

To prove [(b)](https://arxiv.org/html/2405.18962v1#S4.I1.i2 "item (b) ‣ Theorem 6. ‣ 4.2 Lags and state dimensions of explaining systems ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system"), note that

due to Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 17. ‣ 6.1 The lag structure of a system ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system").[(c)](https://arxiv.org/html/2405.18962v1#S6.I1.i3 "item (c) ‣ Lemma 17. ‣ 6.1 The lag structure of a system ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system"). Therefore, if $\ell = q$ then [(b)](https://arxiv.org/html/2405.18962v1#S4.I1.i2 "item (b) ‣ Theorem 6. ‣ 4.2 Lags and state dimensions of explaining systems ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") readily follows from Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 18. ‣ 6.2 Lag structures and 𝛿_𝑘 integers ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system"). Suppose that $\ell > q$. Note that

where the first inequality follows from Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 17. ‣ 6.1 The lag structure of a system ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system").[(b)](https://arxiv.org/html/2405.18962v1#S6.I1.i2 "item (b) ‣ Lemma 17. ‣ 6.1 The lag structure of a system ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system") and Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 18. ‣ 6.2 Lag structures and 𝛿_𝑘 integers ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system"), and the second from the statements [(b)](https://arxiv.org/html/2405.18962v1#S6.I1.i2 "item (b) ‣ Lemma 17. ‣ 6.1 The lag structure of a system ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system") and [(d)](https://arxiv.org/html/2405.18962v1#S6.I1.i4 "item (d) ‣ Lemma 17. ‣ 6.1 The lag structure of a system ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system") of Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 17. ‣ 6.1 The lag structure of a system ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system"). Consequently, [(b)](https://arxiv.org/html/2405.18962v1#S4.I1.i2 "item (b) ‣ Theorem 6. ‣ 4.2 Lags and state dimensions of explaining systems ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") follows from ((https://arxiv.org/html/2405.18962v1#S6.E30 "In 6.3 Proof of Theorem 6 ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system")). $\square$

## State construction

In this section, we present a new iterative state construction procedure from data instrumental in proving Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem7 "Theorem 7. ‣ 4.3 Constructing an explaining system ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system").

### On the left kernels of data Hankel matrices

The $\delta_{k}$'s defined by ((https://arxiv.org/html/2405.18962v1#S4.E10 "In 4.1 Data Hankel matrices ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) are strongly related to certain subspaces of the left kernels of data Hankel matrices. To show this, we first introduce a shift operator on subspaces. Let $\mathcal{V} \subseteq {\mathbb{R}}^{{1 \times \kappa}{({m + p})}}$ be a subspace where $\kappa \in {\mathbb{N}}$. Define $\sigma\mathcal{V}$ as the subspace of all vectors of the form $\begin{bmatrix}
\end{bmatrix}$ where $v_{1} \in {\mathbb{R}}^{{1 \times \kappa}m}$ and $v_{2} \in {\mathbb{R}}^{{1 \times \kappa}p}$ satisfy ${\begin{bmatrix}
\end{bmatrix} \in \mathcal{V}}.$ By convention, ${\sigma^{0}\mathcal{V}}:=\mathcal{V}$. Moreover, ${\sigma^{k}\mathcal{V}} = {\sigma{({\sigma^{k - 1}\mathcal{V}})}}$ for $k \geqslant 1$. The definitions of $H_{k}$ and $G_{k}$ imply that

for all $k \in {\lbrack 0,{T - 1}\rbrack}$. From the definition of $\sigma$ and the Hankel structure it follows that if $T \geqslant 2$, then for all $k \in {\lbrack 0,{T - 2}\rbrack}$

The following result shows that ${lker}H_{k}$ can be written into a direct sum of ${{lker}G_{k}} \times {\{ 0\}}^{p}$ and shifts of certain subspaces.

### Lemma 19

For $k \in {\lbrack 0,{T - 1}\rbrack}$, there exist subspaces $\mathcal{S}_{k} \subseteq {\mathbb{R}}^{{1 \times {({k + 1})}}{({m + p})}}$ satisfying

and ${\dim\mathcal{S}_{k}} = {\delta_{k - 1} - \delta_{k}}$.

### Proof

To prove the existence of subspaces satisfying ((https://arxiv.org/html/2405.18962v1#S7.E35 "In Lemma 19. ‣ 7.1 On the left kernels of data Hankel matrices ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")) we use induction on $k$. From ((https://arxiv.org/html/2405.18962v1#S7.E31 "In 7.1 On the left kernels of data Hankel matrices ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")) with $k = 0$, we see that there exists a subspace $\mathcal{S}_{0} \subseteq {\mathbb{R}}^{1 \times {({m + p})}}$ such that ${{lker}H_{0}} = {\mathcal{S}_{0} \oplus \left( {{lker}{G_{0} \times \mathbf{0}_{p}}} \right)}$. If $T = 1$, there is nothing more to prove. Suppose that $T \geqslant 2$. Let $k \in {\lbrack 0,{T - 2}\rbrack}$ and assume that there exist subspaces $\mathcal{S}_{i} \subseteq {\mathbb{R}}^{{1 \times {({i + 1})}}{({m + p})}}$ with $i \in {\lbrack 0,k\rbrack}$ satisfying

From ((https://arxiv.org/html/2405.18962v1#S7.E31 "In 7.1 On the left kernels of data Hankel matrices ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")), ((https://arxiv.org/html/2405.18962v1#S7.E32 "In 7.1 On the left kernels of data Hankel matrices ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")) conclude that ${{\sigma{{lker}H_{k}}} + {({{lker}{G_{k + 1} \times \mathbf{0}_{p}}})}} \subseteq {{lker}H_{k + 1}}$: there exists $\mathcal{S}_{k + 1} \subseteq {\mathbb{R}}^{{1 \times {({k + 2})}}{({m + p})}}$ such that

Given subspaces $\mathcal{V}_{1},\mathcal{V}_{2},\mathcal{V}_{3}$ with ${\mathcal{V}_{1} \cap \mathcal{V}_{2}} = {\{ 0\}}$ and ${{({\mathcal{V}_{1} + \mathcal{V}_{2}})} \cap \mathcal{V}_{3}} = \mathcal{V}_{2}$, it holds that ${\mathcal{V}_{1} + \mathcal{V}_{2} + \mathcal{V}_{3}} = {\mathcal{V}_{1} \oplus \mathcal{V}_{3}}$. Take $\mathcal{V}_{1} = {\sigma{({\bigoplus_{i = 0}^{k}{\sigma^{k - i}\mathcal{S}_{i}}})}}$, $\mathcal{V}_{2} = {\sigma{({{lker}{G_{k} \times \mathbf{0}_{p}}})}}$, and $\mathcal{V}_{3} = {{lker}{G_{k + 1} \times \mathbf{0}_{p}}}$. Note that ${\mathcal{V}_{1} \cap \mathcal{V}_{2}} = {\{ 0\}}$ due to ((https://arxiv.org/html/2405.18962v1#S7.E36 "In Proof. ‣ 7.1 On the left kernels of data Hankel matrices ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")) and ${{({\mathcal{V}_{1} + \mathcal{V}_{2}})} \cap \mathcal{V}_{3}} = \mathcal{V}_{2}$ due to ((https://arxiv.org/html/2405.18962v1#S7.E34 "In 7.1 On the left kernels of data Hankel matrices ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")). Therefore, we see from ((https://arxiv.org/html/2405.18962v1#S7.E36 "In Proof. ‣ 7.1 On the left kernels of data Hankel matrices ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")) and ((https://arxiv.org/html/2405.18962v1#S7.E37 "In Proof. ‣ 7.1 On the left kernels of data Hankel matrices ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")) that ${{{lker}H_{k + 1}} = {\left( {\bigoplus_{i = 0}^{k + 1}{\sigma^{{k + 1} - i}\mathcal{S}_{i}}} \right) \oplus \left( {{lker}{G_{k + 1} \times \mathbf{0}_{p}}} \right)}}.$ This proves that there exist subspaces $\mathcal{S}_{k}$ such that ((https://arxiv.org/html/2405.18962v1#S7.E35 "In Lemma 19. ‣ 7.1 On the left kernels of data Hankel matrices ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")) holds. To complete the proof, it remains to show that ${\dim\mathcal{S}_{k}} = {\delta_{k - 1} - \delta_{k}}$ for $k \in {\lbrack 0,{T - 1}\rbrack}$. Let $k \in {\lbrack 0,{T - 1}\rbrack}$ and observe that ((https://arxiv.org/html/2405.18962v1#S7.E35 "In Lemma 19. ‣ 7.1 On the left kernels of data Hankel matrices ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")) yields ${{\dim{{lker}H_{k}}} = {{\sum_{i = 0}^{k}{\dim\mathcal{S}_{i}}} + {\dim{{lker}G_{k}}}}}.$ From the rank-nullity theorem, we conclude that ${{\sum_{i = 0}^{k}{\dim\mathcal{S}_{i}}} = {\delta_{- 1} - \delta_{k}}}.$ Therefore, ${\dim\mathcal{S}_{0}} = {\delta_{- 1} - \delta_{0}}$ and ${\dim\mathcal{S}_{k}} = {{\sum_{i = 0}^{k}{\dim\mathcal{S}_{i}}} - {\sum_{i = 0}^{k - 1}{\dim\mathcal{S}_{i}}}} = {\delta_{k - 1} - \delta_{k}}$ for all $k \in {\lbrack 1,{T - 1}\rbrack}$. ∎

### Proof of Theorem [7](https://arxiv.org/html/2405.18962v1#Thmtheorem7 "Theorem 7. ‣ 4.3 Constructing an explaining system ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")

We first prove that ${\mathcal{E}{({\sum_{i = 0}^{q}\delta_{i}})}} \neq \varnothing$ by constructing a state $x \in {\mathbb{R}}^{\sum_{i = 0}^{q}{\delta_{i} \times {({T + 1})}}}$ for the data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$.

Let subspaces $\mathcal{S}_{k} \subseteq {\mathbb{R}}^{{1 \times {({k + 1})}}{({m + p})}}$ with $k \in {\lbrack 0,{T - 1}\rbrack}$ be as in Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 19. ‣ 7.1 On the left kernels of data Hankel matrices ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system"). Also, denote $s_{k}:={\dim\mathcal{S}_{k}}$. For $i \in {\lbrack 0,q\rbrack}$, let $Q_{i,j} \in {\mathbb{R}}^{s_{i} \times m}$ and $P_{i,j} \in {\mathbb{R}}^{s_{i} \times p}$ with $j \in {\lbrack 0,i\rbrack}$ be such that the rows of the matrix $R_{i}:=\begin{bmatrix}
\end{bmatrix}$ form a basis for $\mathcal{S}_{i}$. Note that $R_{i} \in {\mathbb{R}}^{{s_{i} \times {({i + 1})}}{({m + p})}}$.

Since $\mathcal{S}_{i} \subseteq {{lker}H_{i}}$ due to ((https://arxiv.org/html/2405.18962v1#S7.E35 "In Lemma 19. ‣ 7.1 On the left kernels of data Hankel matrices ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")), ${R_{i}H_{i}} = 0$ and hence

Due to Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 19. ‣ 7.1 On the left kernels of data Hankel matrices ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system"), ${\sum_{i = 0}^{q}s_{i}} = {\delta_{- 1} - \delta_{q}} = p$ since $\delta_{- 1} = p$ and $\delta_{q} = 0$ by definition. Therefore, the matrix $\Pi:={{col}{(P_{0,0},P_{1,1},\ldots,P_{q,q})}}$ is $p \times p$.

We claim that $\Pi$ is nonsingular. To see this, let $\eta \in {\mathbb{R}}^{1 \times p}$ be such that ${\eta\Pi} = 0$. Define

and observe that $\Pi$ is the last block-column of $R$.

From the definition of $Q_{i,j}$ and $P_{i,j}$, it is straightforward to verify that the rows of $R$ form a basis for the subspace $\bigoplus_{i = 0}^{q}{\sigma^{({q - i})}\mathcal{S}_{i}}$. Then, ${\eta R} \in {\bigoplus_{i = 0}^{q}{\sigma^{({q - i})}\mathcal{S}_{i}}}$. This means that ${RH_{q}} = 0$. Since ${\eta\Pi} = 0$, the last $p$ entries of $\eta R$ are zero. Therefore, ${\eta R} \in \left( {{lker}{G_{q} \times \mathbf{0}_{p}}} \right)$ and hence ${\eta R} \in {\left( {\bigoplus_{i = 0}^{q}{\sigma^{({q - i})}\mathcal{S}_{i}}} \right) \cap \left( {{lker}{G_{q} \times \mathbf{0}_{p}}} \right)}$. Since ${\left( {\bigoplus_{i = 0}^{q}{\sigma^{({q - i})}\mathcal{S}_{i}}} \right) \cap \left( {{lker}{G_{q} \times \mathbf{0}_{p}}} \right)} = {\{ 0\}}$ due to ((https://arxiv.org/html/2405.18962v1#S7.E35 "In Lemma 19. ‣ 7.1 On the left kernels of data Hankel matrices ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")), we conclude that ${\eta R} = 0$. Since the rows of $R$ are linearly independent, we see that $\eta = 0$ and thus $\Pi \in {\mathbb{R}}^{p \times p}$ is nonsingular.

We now distinguish two cases: $q = 0$ and $q \geqslant 1$.

For the case $q = 0$, we have $s_{0} = {\delta_{- 1} - \delta_{0}} = p$ and $\Pi = P_{0,0}$. It follows from ((https://arxiv.org/html/2405.18962v1#S7.E38 "In 7.2 Proof of Theorem 7 ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")) with $i = 0$ and the nonsingularity of $P_{0,0}$ that $y_{\lbrack 0,{T - 1}\rbrack} = {- {P_{0,0}^{- 1}Q_{0,0}u_{\lbrack 0,{T - 1}\rbrack}}}$. Consequently, the memoryless model associated with $- {P_{0,0}^{- 1}Q_{0,0}}$ explains the data: ${- {P_{0,0}^{- 1}Q_{0,0}}} \in {\mathcal{E}{}} \neq \varnothing$. Together with ${\sum_{i = 0}^{q}\delta_{i}} = 0$, this proves the claim for the case $q = 0$.

For the case $q \geqslant 1$, we first construct some auxiliary sequences from the data and then we show that such sequences can be used to compute a state for the data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$.

Let $i \in {\lbrack 1,q\rbrack}$ and for $k \in {\lbrack 1,i\rbrack}$ define $x_{0}^{i,k} \in {\mathbb{R}}^{s_{i}}$ by

Define $x_{\lbrack 1,T\rbrack}^{i,k} \in {\mathbb{R}}^{s_{i} \times T}$ by

for $k \in {\lbrack 2,i\rbrack}$. Finally, define $x_{\lbrack 0,T\rbrack}^{i}:={{col}{(x_{\lbrack 0,T\rbrack}^{i,1},x_{\lbrack 0,T\rbrack}^{i,2},\ldots,x_{\lbrack 0,T\rbrack}^{i,i})}} \in {\mathbb{R}}^{{is_{i}} \times {({T + 1})}}$ and ${x_{\lbrack 0,T\rbrack}:={{col}{(x_{\lbrack 0,T\rbrack}^{1},x_{\lbrack 0,T\rbrack}^{2},\ldots,x_{\lbrack 0,T\rbrack}^{q})}} \in {\mathbb{R}}^{{({\sum_{i = 1}^{q}{is_{i}}})} \times {({T + 1})}}}.$

To verify this, note first that due to ((https://arxiv.org/html/2405.18962v1#S7.E39 "In 7.2 Proof of Theorem 7 ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system"))

Consider the case $i = 1$; then ${{x_{\lbrack 1,{T - 1}\rbrack}^{1,1}\overset{(⁢⁢)}{=}} - {Q_{1,0}u_{\lbrack 0,{T - 2}\rbrack}} - {P_{1,0}y_{\lbrack 0,{T - 2}\rbrack}}}.$ Now ${x_{\lbrack 1,{T - 1}\rbrack}^{1,1}\overset{(⁢⁢)}{=}Q_{1,1}u_{\lbrack 1,{T - 1}\rbrack}} + {P_{1,1}y_{\lbrack 1,{T - 1}\rbrack}}$; using ((https://arxiv.org/html/2405.18962v1#S7.E43 "In 7.2 Proof of Theorem 7 ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")), we conclude that ((https://arxiv.org/html/2405.18962v1#S7.E42 "In 7.2 Proof of Theorem 7 ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")) holds for $i = 1$.

To prove ((https://arxiv.org/html/2405.18962v1#S7.E42 "In 7.2 Proof of Theorem 7 ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")) for the case $i > 1$, let $\alpha \in {\lbrack 1,{T - 1}\rbrack}$. We first consider the case $\alpha \in {\lbrack 1,{i - 1}\rbrack}$. Note that

Now ${x_{0}^{i,{i - \alpha}}\overset{(⁢⁢)}{=}{\sum_{j = {i - \alpha}}^{i}{Q_{i,j}u_{j - {({i - \alpha})}}}}} + {P_{i,j}y_{j - {({i - \alpha})}}}$; from ((https://arxiv.org/html/2405.18962v1#S7.E44 "In 7.2 Proof of Theorem 7 ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")) it follows that

Together with ((https://arxiv.org/html/2405.18962v1#S7.E43 "In 7.2 Proof of Theorem 7 ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")), this proves that

Now let $\alpha \in {\lbrack i,{T - 1}\rbrack}$, and note that ${{x_{\alpha}^{i,i} - x_{{\alpha - i} + 1}^{i,1}} = {{\sum_{k = 2}^{i}{{({x_{{\alpha - i} + k}^{i,k} - x_{{{\alpha - i} + k} - 1}^{i,{k - 1}}})}\overset{(⁢⁢)}{=}}} - {\sum_{k = 2}^{i}{({{Q_{i,{k - 1}}u_{{{\alpha - i} + k} - 1}} + {P_{i,{k - 1}}y_{{{\alpha - i} + k} - 1}}})}}}}.$ Use ((https://arxiv.org/html/2405.18962v1#S7.E40 "In 7.2 Proof of Theorem 7 ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")) to obtain ${x_{\alpha}^{i,i} = {- {\sum_{k = 1}^{i}{({{Q_{i,{k - 1}}u_{{{\alpha - i} + k} - 1}} + {P_{i,{k - 1}}y_{{{\alpha - i} + k} - 1}}})}}}},$ and use ((https://arxiv.org/html/2405.18962v1#S7.E38 "In 7.2 Proof of Theorem 7 ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")) to conclude that $x_{\alpha}^{i,i} = {{Q_{i,i}u_{\alpha}} + {P_{i,i}y_{\alpha}}}$. Conclude that ${x_{\lbrack i,{T - 1}\rbrack}^{i,i} = {{Q_{i,i}u_{\lbrack i,{T - 1}\rbrack}} + {P_{i,i}y_{\lbrack i,{T - 1}\rbrack}}}}.$ Together with ((https://arxiv.org/html/2405.18962v1#S7.E45 "In 7.2 Proof of Theorem 7 ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")), this proves that ((https://arxiv.org/html/2405.18962v1#S7.E42 "In 7.2 Proof of Theorem 7 ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")) holds.

Since $\Pi$ is nonsingular, $P_{i,i}$ has full row rank. Therefore, ((https://arxiv.org/html/2405.18962v1#S7.E42 "In 7.2 Proof of Theorem 7 ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")) implies that ${{{rsp}y_{\lbrack 0,{T - 1}\rbrack}} \subseteq {{rsp}\begin{bmatrix}
\end{bmatrix}}}.$ It follows from ((https://arxiv.org/html/2405.18962v1#S7.E40 "In 7.2 Proof of Theorem 7 ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")) and ((https://arxiv.org/html/2405.18962v1#S7.E41 "In 7.2 Proof of Theorem 7 ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")) that ${{{rsp}x_{\lbrack 1,T\rbrack}} \subseteq {{rsp}\begin{bmatrix}
\end{bmatrix}}}.$ From ((https://arxiv.org/html/2405.18962v1#S4.E14 "In 4.3 Constructing an explaining system ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) we conclude that $x_{\lbrack 0,T\rbrack}$ is a state for $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$. Note that the number of rows of $x_{\lbrack 0,T\rbrack}$ equals $\sum_{i = 0}^{q}{is_{i}}$. Since $s_{k} = {\delta_{k - 1} - \delta_{k}}$ due to Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 19. ‣ 7.1 On the left kernels of data Hankel matrices ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system") and since $\delta_{q} = 0$, ${\sum_{i = 0}^{q}{is_{i}}} = {\sum_{i = 0}^{q}\delta_{i}}$. We conclude that ${\mathcal{E}{({\sum_{i = 0}^{q}\delta_{i}})}} \neq \varnothing$.

To prove the second claim, note that ${\mathcal{E}{(q,{\sum_{i = 0}^{q}\delta_{i}})}} \subseteq {\mathcal{E}{({\sum_{i = 0}^{q}\delta_{i}})}}$ by definition: it is enough to show that the reverse inclusion holds. To do so, let $\begin{bmatrix}
\end{bmatrix} \in {\mathcal{E}{({\sum_{i = 0}^{q}\delta_{i}})}}$ and $\ell = {\ell{(C,A)}}$. Suppose that $\ell < q$. Since ${T - 1} \geqslant q$ by ((https://arxiv.org/html/2405.18962v1#S4.E13 "In 4.2 Lags and state dimensions of explaining systems ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")), we have $T > {\ell + 1}$. Then, Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem6 "Theorem 6. ‣ 4.2 Lags and state dimensions of explaining systems ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system").[(a)](https://arxiv.org/html/2405.18962v1#S4.I1.i1 "item (a) ‣ Theorem 6. ‣ 4.2 Lags and state dimensions of explaining systems ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") implies that $\ell \geqslant q$. This contradicts $\ell < q$. As such, we conclude that $\ell \geqslant q$. Then, Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem6 "Theorem 6. ‣ 4.2 Lags and state dimensions of explaining systems ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system").[(b)](https://arxiv.org/html/2405.18962v1#S4.I1.i2 "item (b) ‣ Theorem 6. ‣ 4.2 Lags and state dimensions of explaining systems ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") implies that $q \geqslant \ell$, and $\ell = q$. This means that ${\mathcal{E}{({\sum_{i = 0}^{q}\delta_{i}})}} \subseteq {\mathcal{E}{(q,{\sum_{i = 0}^{q}\delta_{i}})}}$. This completes the proof. $\square$

### Example 20 (State construction)

We compute a state for the data in Section (https://arxiv.org/html/2405.18962v1#S5 "5 Illustrative example ‣ Beyond the fundamental lemma: from finite time series to linear system") and the values $T = 5$ and $T = 14$ following the procedure in the proof of Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem7 "Theorem 7. ‣ 4.3 Constructing an explaining system ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system").

For $T = 5$, $\delta_{- 1} = \delta_{0} = 2$, and $\delta_{k} = 0$ for $k \in {\lbrack 1,4\rbrack}$ (see Table (https://arxiv.org/html/2405.18962v1#S5.T1 "Table 1 ‣ 5 Illustrative example ‣ Beyond the fundamental lemma: from finite time series to linear system") in Section (https://arxiv.org/html/2405.18962v1#S5 "5 Illustrative example ‣ Beyond the fundamental lemma: from finite time series to linear system")). Use Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 19. ‣ 7.1 On the left kernels of data Hankel matrices ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system") to conclude that ${\dim\mathcal{S}_{0}} = 0$ and ${\dim\mathcal{S}_{1}} = 2$. Therefore, $P_{0,j}$ and $Q_{0,j}$ for $j \in {\{ 0,1\}}$ are void matrices and one can choose the following basis matrix for $\mathcal{S}_{1}$

In view of ((https://arxiv.org/html/2405.18962v1#S7.E39 "In 7.2 Proof of Theorem 7 ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system"))-((https://arxiv.org/html/2405.18962v1#S7.E40 "In 7.2 Proof of Theorem 7 ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")), these choices yield the state

Solving ((https://arxiv.org/html/2405.18962v1#S3.E5 "In 3.1 Explaining systems ‣ 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system")), we obtain the following explaining system:

Evidently $(u_{\lbrack 0,4\rbrack},y_{\lbrack 0,4\rbrack})$ are not informative for system identification: they are explained by a minimal system with 2 states.

For $T = 14$, $\delta_{- 1} = \delta_{0} = 2$, $\delta_{1} = 1$, and $\delta_{k} = 0$ for $k \in {\lbrack 2,13\rbrack}$ (see Table (https://arxiv.org/html/2405.18962v1#S5.T1 "Table 1 ‣ 5 Illustrative example ‣ Beyond the fundamental lemma: from finite time series to linear system") in Section (https://arxiv.org/html/2405.18962v1#S5 "5 Illustrative example ‣ Beyond the fundamental lemma: from finite time series to linear system")). Moreover, $(u_{\lbrack 0,13\rbrack},y_{\lbrack 0,13\rbrack})$ are informative for system identification for all values of $L_{+}$ and $N_{+}$ in Table (https://arxiv.org/html/2405.18962v1#S5.T2 "Table 2 ‣ 5 Illustrative example ‣ Beyond the fundamental lemma: from finite time series to linear system"). As such, we can use Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem7 "Theorem 7. ‣ 4.3 Constructing an explaining system ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") to identify an isomorphic system to the true one. We first apply Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 19. ‣ 7.1 On the left kernels of data Hankel matrices ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system") and conclude that ${\dim\mathcal{S}_{0}} = 0$, ${\dim\mathcal{S}_{1}} = 1$, and ${\dim\mathcal{S}_{2}} = 1$. Therefore, $P_{0,j}$ and $Q_{0,j}$ for $j \in {\{ 0,1\}}$ are void matrices and one can choose the following bases matrices for $\mathcal{S}_{1}$ and $\mathcal{S}_{2}$

In view of ((https://arxiv.org/html/2405.18962v1#S7.E39 "In 7.2 Proof of Theorem 7 ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system"))-((https://arxiv.org/html/2405.18962v1#S7.E41 "In 7.2 Proof of Theorem 7 ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")), these choices yield the state

Solving ((https://arxiv.org/html/2405.18962v1#S3.E5 "In 3.1 Explaining systems ‣ 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system")) we obtain the explaining system

that is isomorphic to the true system.

## State-input data Hankel matrices

To prove the sufficiency part of Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem9 "Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") we need auxiliary results on the ranks of state-input data Hankel matrices.

### On the ranks of state-input data Hankel matrices

Let $\begin{bmatrix}
\end{bmatrix} \in {\mathcal{E}{(n)}}$ and $x_{\lbrack 0,T\rbrack}$ be a state for $\begin{bmatrix}
\end{bmatrix}$. Define

for $k \in {\lbrack 0,{T - 1}\rbrack}$. Given the structure of $J_{k}$ we conclude that

for every $k \in {\lbrack 1,{T - 1}\rbrack}$.

We now study the relation of ${rank}H_{k}$ and ${{rank}J_{k}}{(x)}$. Recall from ((https://arxiv.org/html/2405.18962v1#S6.E26 "In 6.2 Lag structures and 𝛿_𝑘 integers ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system")) that $H_{k} = {\Phi_{k}J_{k}{(x)}}$ and ${G_{k} = {\Psi_{k}J_{k}{(x)}}}.$

### Lemma 21

Assume that $T \geqslant {\ell + 1}$. Let $\begin{bmatrix}
\end{bmatrix} \in {\mathcal{E}{(\ell,n)}}$ and $x_{\lbrack 0,T\rbrack}$ be a state for $\begin{bmatrix}
\end{bmatrix}$, and define $d:={\max{({\ell - 1},0)}}$. The following statements hold:

If $(C,A)$ is observable, then ${{{rank}J_{k}}{(x)}} = {{rank}H_{k}}$ for all $k \in {\lbrack d,{T - 1}\rbrack}$.

If $J_{i}{(x)}$ has full row rank for some $i \in {\lbrack 0,{T - 1}\rbrack}$, then for each $k \in {\lbrack 0,i\rbrack}$ $J_{k}{(x)}$ has full row rank, ${{rank}H_{k}} = {{{({k + 1})}m} + {{rank}\Omega_{k}}}$, and ${{rank}G_{k}} = {{{({k + 1})}m} + {{rank}\Omega_{k - 1}}}$.

### Proof

If $(C,A)$ is observable, then $\Phi_{k}$ has full column rank for $k \geqslant d$; statement [(a)](https://arxiv.org/html/2405.18962v1#S8.I1.i1 "item (a) ‣ Lemma 21. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system") is proved. To prove [(b)](https://arxiv.org/html/2405.18962v1#S8.I1.i2 "item (b) ‣ Lemma 21. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system"), note first that $J_{k}{(x)}$ has full row rank whenever $k \in {\lbrack 0,i\rbrack}$ due to ((https://arxiv.org/html/2405.18962v1#S8.E47 "In 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")). For the rest, observe that ((https://arxiv.org/html/2405.18962v1#S6.E26 "In 6.2 Lag structures and 𝛿_𝑘 integers ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system")) implies ${{rank}H_{k}} = {{rank}\Phi_{k}}$ and ${{rank}G_{k}} = {{rank}\Psi_{k}}$ whenever $J_{k}{(x)}$ has full row rank. From the definitions, we have ${{rank}\Phi_{k}} = {{{({k + 1})}m} + {{rank}\Omega_{k}}}$ and ${{rank}\Psi_{k}} = {{{({k + 1})}m} + {{rank}\Omega_{k - 1}}}$; the claim is proved.∎

An interesting and useful consequence of Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 21. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system") is related to the isomorphism property.

### Lemma 22

Suppose that $T \geqslant {\ell + 1}$. Let $\begin{bmatrix}
\end{bmatrix} \in {{\mathcal{E}{(\ell,n)}} \cap \mathcal{O}}$ and $x_{\lbrack 0,T\rbrack}$ be a state for $\begin{bmatrix}
\end{bmatrix}$. If $J_{\ell}{(x)}$ has full row rank, then ${\mathcal{E}{(\ell,n)}} \cap \mathcal{O}$ has the isomorphism property.

### Proof

Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 21. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system").[(b)](https://arxiv.org/html/2405.18962v1#S8.I1.i2 "item (b) ‣ Lemma 21. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system") implies that ${{{rank}H_{\ell}} = {{{({\ell + 1})}m} + n}}.$ Let $i \in {\lbrack 1,2\rbrack}$, $\begin{bmatrix}
\end{bmatrix} \in {{\mathcal{E}{(\ell,n)}} \cap \mathcal{O}}$ and let $x_{\lbrack 0,T\rbrack}^{i}$ be a state for $\begin{bmatrix}
\end{bmatrix}$. Denote $J_{k}{(x^{i})}$ by $J_{k}^{i}$. Because of observability, Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 21. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system").[(a)](https://arxiv.org/html/2405.18962v1#S8.I1.i1 "item (a) ‣ Lemma 21. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system") implies that $J_{\ell}^{i}$ has full row rank and statement [(b)](https://arxiv.org/html/2405.18962v1#S8.I1.i2 "item (b) ‣ Lemma 21. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system") implies that $J_{k}^{i}$ has full row rank for all $k \in {\lbrack 0,\ell\rbrack}$. In particular, $J_{0}^{i}$ has full row rank: there exist $S \in {\mathbb{R}}^{n \times n}$, $R \in {\mathbb{R}}^{n \times m}$, $Q \in {\mathbb{R}}^{m \times n}$, and $P \in {\mathbb{R}}^{m \times m}$ such that

The last $m$ rows of the matrices $J_{0}^{i}$ are identical; conclude that ${\begin{bmatrix}
\end{bmatrix}J_{0}^{2}} = 0$. Now $J_{0}^{2}$ has full row rank; conclude that $Q = 0$ and $P = I$. Using the same argument, ((https://arxiv.org/html/2405.18962v1#S8.E48 "In Proof. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")) leads to

Since $J_{\ell}^{i}$ has full row rank, it follows from ((https://arxiv.org/html/2405.18962v1#S6.E26 "In 6.2 Lag structures and 𝛿_𝑘 integers ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system")) that

where $\Phi_{\ell}^{i}:={\Phi_{\ell}{(A_{i},B_{i},C_{i},D_{i})}}$. Using ((https://arxiv.org/html/2405.18962v1#S6.E27 "In 6.2 Lag structures and 𝛿_𝑘 integers ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system")), we see that

Equation ((https://arxiv.org/html/2405.18962v1#S8.E49 "In Proof. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")) implies that $S$ is nonsingular due to observability whereas ((https://arxiv.org/html/2405.18962v1#S8.E50 "In Proof. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")) implies that the last $\ell m$ columns of $\Theta_{\ell}^{1}$ and $\Theta_{\ell}^{2}$ are identical. Given their Toeplitz structure, we see that

and ${C_{1}A_{1}^{k}B_{1}} = {C_{2}A_{2}^{k}B_{2}}$ for $k \in {\lbrack 0,{\ell - 2}\rbrack}$. Consequently the entries corresponding to the first $\ell p$ rows and first $m$ columns of $\Theta_{\ell}^{1} - \Theta_{\ell}^{2}$ are all zero. Hence, ((https://arxiv.org/html/2405.18962v1#S8.E50 "In Proof. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")) implies ${\Omega_{\ell - 1}^{1}R} = 0$. Now $R = 0$ since $(C_{1},A_{1})$ is observable. Therefore, ((https://arxiv.org/html/2405.18962v1#S8.E50 "In Proof. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")) implies $\Theta_{\ell}^{2} = \Theta_{\ell}^{1}$. Comparing the first $p$ rows in ((https://arxiv.org/html/2405.18962v1#S8.E49 "In Proof. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")), we see that

From $\Theta_{\ell}^{2} = \Theta_{\ell}^{1}$, we have

for every $k \in {\lbrack 0,{\ell - 1}\rbrack}$. Note that $\Omega_{\ell - 1}^{1}SB_{2}\overset{(⁢⁢)}{=}\Omega_{\ell - 1}^{2}B_{2}\overset{(⁢⁢)}{=}\Omega_{\ell - 1}^{1}B_{1}$. From the observability of $(C_{1},A_{1})$ conclude that

Note that ${{\Omega_{\ell - 1}^{1}{({{SA_{2}} - {A_{1}S}})}\overset{(⁢⁢)}{=}\Omega_{\ell - 1}^{2}A_{2}} - {\Omega_{\ell - 1}^{1}A_{1}S\overset{(⁢⁢)}{=}0}}.$ As $(C_{1},A_{1})$ is observable, we see that ${{SA_{2}} - {A_{1}S}} = 0$; with ((https://arxiv.org/html/2405.18962v1#S8.E51 "In Proof. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")), ((https://arxiv.org/html/2405.18962v1#S8.E52 "In Proof. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")), and ((https://arxiv.org/html/2405.18962v1#S8.E54 "In Proof. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")), this proves that $\begin{bmatrix}
\end{bmatrix}$ are isomorphic. Hence ${\mathcal{E}{(\ell,n)}} \cap \mathcal{O}$ has the isomorphism property. ∎

Given ((https://arxiv.org/html/2405.18962v1#S8.E47 "In 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")) and the rank-nullity theorem, ${{{rank}J_{k - 1}} + m} \geqslant {{rank}J_{k}}$ for all $k \in {\lbrack 1,{T - 1}\rbrack}$. Such relation between the ranks of two consecutive $J_{k}$-matrices is related to the controllability of the corresponding explaining system.

### Lemma 23

Let $\begin{bmatrix}
\end{bmatrix} \in {\mathcal{E}{(\ell,n)}}$ and $x_{\lbrack 0,T\rbrack}$ be a state for $\begin{bmatrix}
\end{bmatrix}$. If for some $k \in {\lbrack 1,{T - 1}\rbrack}$ ${{{{rank}J_{k - 1}}{(x)}} + m} = {{{rank}J_{k}}{(x)}}$ and $J_{k}{(x)}$ does not have full row rank, then $(A,B)$ is not controllable.

### Proof

Let $k \in {\lbrack 1,{T - 1}\rbrack}$ be such that ${{{{rank}J_{k - 1}}{(x)}} + m} = {{{rank}J_{k}}{(x)}}$ and $J_{k}{(x)}$ does not have full row rank. From the rank-nullity theorem, we have ${{\dim{{{lker}J_{k - 1}}{(x)}}} = {\dim{{{lker}J_{k}}{(x)}}} > 0}.$ Then, we see from ((https://arxiv.org/html/2405.18962v1#S8.E47 "In 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")) that

Now, define $\mathcal{A}_{k} \in {\mathbb{R}}^{{({n + {{({k + 1})}m}})} \times {({n + {{({k + 1})}m}})}}$ by $\mathcal{A}_{k}:=\begin{bmatrix}
\end{bmatrix}$. The relation $x_{\lbrack 1,T\rbrack} = {{Ax_{\lbrack 0,T\rbrack}} + {Bu_{\lbrack 0,{T - 1}\rbrack}}}$ implies that ${\mathcal{A}_{k}J_{k}} = \begin{bmatrix}
{H_{k - 1}\left( u_{\lbrack 1,{T - 1}\rbrack} \right)} \\
\end{bmatrix}$ for every $k \in {\lbrack 0,{T - 1}\rbrack}$. Note that the matrix $\begin{bmatrix}
\end{bmatrix}$ can be obtained from $J_{k - 1}{(x)}$ by deleting its first column. Hence, we see that ${{({{{{lker}J_{k - 1}}{(x)}} \times \mathbf{0}_{m}})}\mathcal{A}_{k}} \subseteq {{{lker}J_{k}}{(x)}}$ for every $k \in {\lbrack 1,{T - 1}\rbrack}$. Together with ((https://arxiv.org/html/2405.18962v1#S8.E55 "In Proof. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")), this implies that ${\{ 0\}} \neq {{{{lker}J_{k - 1}}{(x)}} \times \mathbf{0}_{m}}$ is left-invariant under $\mathcal{A}_{k}$, that is ${{({{{{lker}J_{k - 1}}{(x)}} \times \mathbf{0}_{m}})}\mathcal{A}_{k}} \subseteq {{{{lker}J_{k - 1}}{(x)}} \times \mathbf{0}_{m}}$. Therefore, the subspace ${{{lker}J_{k - 1}}{(x)}} \times \mathbf{0}_{m}$ must contain a left-eigenvector of $\mathcal{A}_{k}$, say $\zeta \in {\mathbb{C}}^{1 \times {({n + {{({k + 1})}m}})}}$. Note that the last $m$ entries of $\zeta$ are zero. Together with the structure of $\mathcal{A}_{k}$, this implies that $\zeta = \begin{bmatrix}
\end{bmatrix}$ where $\xi$ is nonzero. Hence, we see that ${\xi\begin{bmatrix}
\end{bmatrix}} = 0$ for some $\lambda \in {\mathbb{C}}$. It, then, follows from the Hautus test that $(A,B)$ is uncontrollable. ∎

### Proof of Theorem [9](https://arxiv.org/html/2405.18962v1#Thmtheorem9 "Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system"): sufficiency part

In view of Proposition (https://arxiv.org/html/2405.18962v1#Thmtheorem2 "Proposition 2. ‣ 3.2 Informativity for system identification ‣ 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system") and ((https://arxiv.org/html/2405.18962v1#S4.E18 "In 4.5 Sharpening the upper bound on the true lag ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")), proving sufficiency of Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem9 "Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") requires showing that the conditions ((https://arxiv.org/html/2405.18962v1#S4.E19 "In Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) imply:

${\mathcal{E}_{{\lbrack L_{-},L_{+}^{a}\rbrack},{\lbrack N_{-},N_{+}\rbrack}} \cap \mathcal{M}} = {{\mathcal{E}{(n_{true})}} \cap \mathcal{M}}$, and

${\mathcal{E}{(n_{true})}} \cap \mathcal{M}$ has the isomorphism property.

To this end, we need some preparations.

To begin with, it is clear from the definitions of $\ell_{\min}$ and $n_{\min}$ that ${\mathcal{E} \cap {\mathcal{S}{(\ell,n)}}} = \varnothing$ whenever $\ell < \ell_{\min}$ or $n < n_{\min}$. Therefore, we see from ([19a](https://arxiv.org/html/2405.18962v1#S4.E19.1 "In 19 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) and ([19b](https://arxiv.org/html/2405.18962v1#S4.E19.2 "In 19 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) that

Next, we compute the ranks of the data Hankel matrices $H_{k}$. Let $\begin{bmatrix}
\end{bmatrix} \in {\mathcal{E}{(n_{\min})}}$ and let $x_{\lbrack 0,T\rbrack} \in {\mathbb{R}}^{n_{\min} \times {({T + 1})}}$ be a state for $\begin{bmatrix}
\end{bmatrix}$. Note that $\ell_{\min} \leqslant \ell_{true} \leqslant L_{+}$ and $\ell_{\min} \leqslant L_{+}^{d} = {{N_{+} - n_{\min}} + \ell_{\min}}$. As such, we have $\ell_{\min} \leqslant L_{+}^{a} = {\min{(L_{+},L_{+}^{d})}}$. Due to Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem8 "Theorem 8. ‣ 4.4 The shortest lag and the minimum number of states ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system"), $(C,A)$ is observable. Since $m \geqslant 1$, ([19c](https://arxiv.org/html/2405.18962v1#S4.E19.3 "In 19 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) implies that $T \geqslant {L_{+}^{a} + 1}$. Therefore, it follows from Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 21. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system").[(a)](https://arxiv.org/html/2405.18962v1#S8.I1.i1 "item (a) ‣ Lemma 21. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system") that ${{{rank}J_{k}}{(x)}} = {{rank}H_{k}}$ for every $k \in {\lbrack d,L_{+}^{a}\rbrack}$ where $d = {\max{({\ell_{\min} - 1},0)}}$. In particular, we see from ([19d](https://arxiv.org/html/2405.18962v1#S4.E19.4 "In 19 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) that ${{{rank}J_{L_{+}^{a}}}{(x)}} = {{{({L_{+}^{a} + 1})}m} + n_{\min}}$ and hence $J_{L_{+}^{a}}{(x)}$ has full row rank. It follows from Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 21. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system").[(b)](https://arxiv.org/html/2405.18962v1#S8.I1.i2 "item (b) ‣ Lemma 21. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system") that

for every $k \in {\lbrack d,L_{+}^{a}\rbrack}$. We claim that

Suppose first that $N_{+} = n_{\min}$. Then, ((https://arxiv.org/html/2405.18962v1#S8.E58 "In 8.2 Proof of Theorem 9: sufficiency part ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")) follows from $\mathcal{E}_{{\lbrack\ell_{\min},L_{+}^{a}\rbrack},{\lbrack n_{\min},n_{\min}\rbrack}} \subseteq {\mathcal{E}{(n_{\min})}}$. Suppose now that $N_{+} > n_{\min}$. Let $\ell \in {\lbrack\ell_{\min},L_{+}^{a}\rbrack}$, $n \in {\lbrack{n_{\min} + 1},N_{+}\rbrack}$, and $\begin{bmatrix}
\end{bmatrix} \in {{\mathcal{E}{(\ell,n)}} \cap \mathcal{O}}$. Also, let ${\hat{x}}_{\lbrack 0,T\rbrack}^{n \times {({T + 1})}}$ be a state for $\begin{bmatrix}
\end{bmatrix}$. $\ell \geqslant 1$ since $(C,A)$ is observable and $n \geqslant 1$. Since $\ell \geqslant \ell_{\min}$, we further see that ${\ell - 1} \geqslant d$. Then, Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 21. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system").[(a)](https://arxiv.org/html/2405.18962v1#S8.I1.i1 "item (a) ‣ Lemma 21. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system") and ((https://arxiv.org/html/2405.18962v1#S8.E57 "In 8.2 Proof of Theorem 9: sufficiency part ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")) imply that ${{{{{rank}J_{\ell - 1}}{(\hat{x})}} + m} = {{{rank}J_{\ell}}{(\hat{x})}} = {{{({\ell + 1})}m} + n_{\min}}}.$ Since $n > n_{\min}$, Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 23. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system") implies that $(\hat{A},\hat{B})$ is not controllable. Therefore, we see that ${{\mathcal{E}{(\ell,n)}} \cap \mathcal{M}} = \varnothing$ whenever $\ell \in {\lbrack\ell_{\min},L_{+}^{a}\rbrack}$ and $n \in {\lbrack{n_{\min} + 1},N_{+}\rbrack}$. Hence, ((https://arxiv.org/html/2405.18962v1#S8.E58 "In 8.2 Proof of Theorem 9: sufficiency part ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")) holds.

Note that ${{\mathcal{E}{(\ell_{true},n_{true})}} \subseteq \mathcal{E}_{{\lbrack\ell_{\min},L_{+}^{a}\rbrack},{\lbrack n_{\min},N_{+}\rbrack}}}.$ Then, it follows from ((https://arxiv.org/html/2405.18962v1#S8.E58 "In 8.2 Proof of Theorem 9: sufficiency part ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")) that

Therefore, we see that

proving ([20a](https://arxiv.org/html/2405.18962v1#S4.E20.1 "In 20 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) and ([20b](https://arxiv.org/html/2405.18962v1#S4.E20.2 "In 20 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")). We conclude from ((https://arxiv.org/html/2405.18962v1#S8.E59 "In 8.2 Proof of Theorem 9: sufficiency part ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")) and Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem8 "Theorem 8. ‣ 4.4 The shortest lag and the minimum number of states ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") that

Thus, condition [(a)](https://arxiv.org/html/2405.18962v1#S8.I2.i1 "item (a) ‣ 8.2 Proof of Theorem 9: sufficiency part ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system") follows from ((https://arxiv.org/html/2405.18962v1#S8.E56 "In 8.2 Proof of Theorem 9: sufficiency part ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")), ((https://arxiv.org/html/2405.18962v1#S8.E60 "In 8.2 Proof of Theorem 9: sufficiency part ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")), and ((https://arxiv.org/html/2405.18962v1#S8.E61 "In 8.2 Proof of Theorem 9: sufficiency part ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")).

To show [(b)](https://arxiv.org/html/2405.18962v1#S8.I2.i2 "item (b) ‣ 8.2 Proof of Theorem 9: sufficiency part ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system"), note first that ((https://arxiv.org/html/2405.18962v1#S8.E57 "In 8.2 Proof of Theorem 9: sufficiency part ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")) and Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 22. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system") imply that ${\mathcal{E}{(\ell_{\min},n_{\min})}} \cap \mathcal{O}$ has the isomorphism property. Since the true system is minimal, we see that

Then, it follows from ((https://arxiv.org/html/2405.18962v1#S8.E61 "In 8.2 Proof of Theorem 9: sufficiency part ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")) that [(b)](https://arxiv.org/html/2405.18962v1#S8.I2.i2 "item (b) ‣ 8.2 Proof of Theorem 9: sufficiency part ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system") holds. What remains to be proven is ([20c](https://arxiv.org/html/2405.18962v1#S4.E20.3 "In 20 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")). To do so, note first that Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem8 "Theorem 8. ‣ 4.4 The shortest lag and the minimum number of states ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") implies that ${\mathcal{E}{(n_{\min})}} = {{\mathcal{E}{(\ell_{\min},n_{\min})}} \cap \mathcal{O}}$. Then, we see from ((https://arxiv.org/html/2405.18962v1#S8.E61 "In 8.2 Proof of Theorem 9: sufficiency part ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")) and ((https://arxiv.org/html/2405.18962v1#S8.E62 "In 8.2 Proof of Theorem 9: sufficiency part ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")) that ${{\mathcal{E}{(n_{\min})}} = {\mathcal{E}_{{\lbrack\ell_{\min},L_{+}^{a}\rbrack},{\lbrack n_{\min},N_{+}\rbrack}} \cap \mathcal{M}}}.$ Therefore, ([20c](https://arxiv.org/html/2405.18962v1#S4.E20.3 "In 20 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) follows from ((https://arxiv.org/html/2405.18962v1#S3.E8 "In 3.2 Informativity for system identification ‣ 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system")), ((https://arxiv.org/html/2405.18962v1#S4.E18 "In 4.5 Sharpening the upper bound on the true lag ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")), and ((https://arxiv.org/html/2405.18962v1#S8.E56 "In 8.2 Proof of Theorem 9: sufficiency part ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system")). $\square$

## From one explaining system to another

To prove necessity in Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem9 "Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system"), we present two ways of computing explaining systems. The first one constructs an explaining system with $n$ states from a given one with $n$ states.

### Lemma 24

Suppose that $\begin{bmatrix}
\end{bmatrix} \in {{\mathcal{E}{(\ell,n)}} \cap \mathcal{O}}$ for some $n \geqslant \ell \geqslant 1$. Let $x_{\lbrack 0,T\rbrack} \in {\mathbb{R}}^{n \times {({T + 1})}}$ be a state for $\begin{bmatrix}
\end{bmatrix}$. Also, let $d = {\min{(\ell,{T - 1})}}$, $\xi \in {\mathbb{R}}^{1 \times n}$ and $\eta_{i} \in {\mathbb{R}}^{1 \times m}$ with $i \in {\lbrack 0,d\rbrack}$ be such that

Let $0 \neq \zeta \in {\mathbb{R}}^{n}$ be such that

where $E_{0}$ and $E_{- 1}$ are determined by the recursion

Then, the following statements hold:

\end{bmatrix} \in {{\mathcal{E}{(\ell,n)}} \cap \mathcal{O}}$.

\end{bmatrix}$ and $\begin{bmatrix}
\end{bmatrix}$ are isomorphic, then

$\eta_{i} = 0$ for every $i \in {\lbrack 0,d\rbrack}$.

${\xi A^{i}B} = 0$ for every $i \in {\lbrack 0,{n - 1}\rbrack}$,

### Proof

To prove [(a)](https://arxiv.org/html/2405.18962v1#S9.I1.i1 "item (a) ‣ Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system"), we first show that there exists ${\hat{x}}_{\lbrack 0,T\rbrack} \in {\mathbb{R}}^{n \times {({T + 1})}}$ satisfying

We claim that ${\hat{x}}_{\lbrack 0,T\rbrack} \in {\mathbb{R}}^{n \times {({T + 1})}}$ defined by

satisfies ((https://arxiv.org/html/2405.18962v1#S9.E68 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) and ((https://arxiv.org/html/2405.18962v1#S9.E69 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")).

To prove this claim, let $k \in {\lbrack 0,{T - d - 1}\rbrack}$. Note that ${{{\hat{x}}_{k + 1}\overset{(⁢⁢)}{=}x_{k + 1}} - {\sum_{i = 0}^{d - 1}{E_{i}u_{k + 1 + i}}}} = {{{Ax_{k}} + {Bu_{k}}} - {\sum_{i = 0}^{d - 1}{E_{i}u_{k + 1 + i}}}}$ and ${{\hat{A}{\hat{x}}_{k}} + {\hat{B}u_{k}\overset{(⁢⁢)}{=}\hat{A}x_{k}} + {\hat{B}u_{k}}} - {\sum_{i = 0}^{d - 1}{\hat{A}E_{i}u_{k + i}}}$. Using ((https://arxiv.org/html/2405.18962v1#S9.E65 "In Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) and ((https://arxiv.org/html/2405.18962v1#S9.E67 "In Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")), one can verify that the difference between these two expressions is ${\zeta\xi x_{k}} + {\sum_{i = 0}^{d}{\zeta\eta_{i}u_{k + i}}}$. Therefore, ((https://arxiv.org/html/2405.18962v1#S9.E63 "In Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) implies that ${{\hat{x}}_{\lbrack 1,{T - d}\rbrack} = {{\hat{A}{\hat{x}}_{\lbrack 0,{T - d - 1}\rbrack}} + {\hat{B}u_{\lbrack 0,{T - d - 1}\rbrack}}}}.$ Together with ((https://arxiv.org/html/2405.18962v1#S9.E71 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")), this proves ((https://arxiv.org/html/2405.18962v1#S9.E68 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")).

Therefore, it remains to prove ((https://arxiv.org/html/2405.18962v1#S9.E69 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")). First, we make a few crucial observations. To begin with, we have

since $(C,A)$ is observable and $\zeta \neq 0$. Also, it follows from ((https://arxiv.org/html/2405.18962v1#S9.E64 "In Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) and ((https://arxiv.org/html/2405.18962v1#S9.E65 "In Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) that

and ${{C{\hat{A}}^{\ell}} = {{CA^{\ell}} + {CA^{\ell - 1}\zeta\xi}}}.$ Further, observe that

for $i \in {\lbrack 0,{\ell - 2}\rbrack}$ due to ((https://arxiv.org/html/2405.18962v1#S9.E64 "In Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) and ((https://arxiv.org/html/2405.18962v1#S9.E73 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")). Finally, it follows from the recursion ((https://arxiv.org/html/2405.18962v1#S9.E67 "In Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) that

for $i \in {\lbrack{- 1},d\rbrack}$ and from ((https://arxiv.org/html/2405.18962v1#S9.E74 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) that

To show ((https://arxiv.org/html/2405.18962v1#S9.E69 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")), we first deal with the case $d = 0$. Since $d = {\min{(\ell,{T - 1})}}$ and $\ell \geqslant 1$, we see that $T = 1$ in this case. Then, it follows from ((https://arxiv.org/html/2405.18962v1#S9.E70 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) that ${\hat{x}}_{\lbrack 0,1\rbrack} = x_{\lbrack 0,1\rbrack}$ and from ((https://arxiv.org/html/2405.18962v1#S9.E66 "In Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system"))-((https://arxiv.org/html/2405.18962v1#S9.E67 "In Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) that $\hat{D} = D$. Since $\hat{C} = C$ due to ((https://arxiv.org/html/2405.18962v1#S9.E66 "In Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")), we see that ((https://arxiv.org/html/2405.18962v1#S9.E69 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) is readily satisfied if $d = 0$.

Suppose now that $d \geqslant 1$. Note that

where the last equality follows from the fact that $x$ is a state for the explaining system $\begin{bmatrix}
\end{bmatrix}$. Hence, we see that ((https://arxiv.org/html/2405.18962v1#S9.E69 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) is satisfied if $d = 1$.

Suppose that $d \geqslant 2$. In view of ((https://arxiv.org/html/2405.18962v1#S9.E77 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")), what remains to be proven is that

To do so, let $i \in {\lbrack 1,{d - 1}\rbrack}$. Define ${\hat{y}}_{{T - d} + i}:={{\hat{C}{\hat{x}}_{{T - d} + i}} + {\hat{D}u_{{T - d} + i}}}$ and ${\Delta_{{T - d} + i}:={{\hat{y}}_{{T - d} + i} - y_{{T - d} + i}}}.$ Note that

where the first equality follows from ((https://arxiv.org/html/2405.18962v1#S9.E71 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")), the second from the fact that $x$ is a state for the data, and the third from ((https://arxiv.org/html/2405.18962v1#S9.E70 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")). By using ((https://arxiv.org/html/2405.18962v1#S9.E65 "In Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")), ((https://arxiv.org/html/2405.18962v1#S9.E67 "In Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")), ((https://arxiv.org/html/2405.18962v1#S9.E73 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")), ((https://arxiv.org/html/2405.18962v1#S9.E74 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")), and the fact that $d \leqslant \ell$, we see that ${\Delta_{{T - d} + i} = {{\sum_{j = 0}^{i}{C{\hat{A}}^{i - j}E_{0}u_{{T - d} + j}}} - {\sum_{j = 0}^{d - 1}{C{\hat{A}}^{i}E_{j}u_{{T - d} + j}}}}}.$ By using ((https://arxiv.org/html/2405.18962v1#S9.E74 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) and ((https://arxiv.org/html/2405.18962v1#S9.E75 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")), one can prove by induction that

for all $j \in {\lbrack 0,{d - 1}\rbrack}$ and $i \in {\lbrack j,{d - 1}\rbrack}$ as well as that

for all $j \in {\lbrack 1,{d - 1}\rbrack}$ and $i \in {\lbrack 0,{j - 1}\rbrack}$. It follows from ((https://arxiv.org/html/2405.18962v1#S9.E79 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) that ${{\sum_{j = 0}^{i}{C{\hat{A}}^{i}E_{j}u_{{T - d} + j}}} = {\sum_{j = 0}^{i}{C{\hat{A}}^{i - j}E_{0}u_{{T - d} + j}}}}.$ Hence, we have ${\Delta_{{T - d} + i} = {- {\sum_{j = {i + 1}}^{d - 1}{C{\hat{A}}^{i}E_{j}u_{{T - d} + j}\overset{(⁢⁢)}{=}0}}}}.$ This proves ((https://arxiv.org/html/2405.18962v1#S9.E78 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) and hence ((https://arxiv.org/html/2405.18962v1#S9.E71 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) in view of ((https://arxiv.org/html/2405.18962v1#S9.E77 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")). Therefore, we proved that $\begin{bmatrix}
\end{bmatrix} \in {\mathcal{E}{(n)}}$. Further, it follows from ((https://arxiv.org/html/2405.18962v1#S9.E73 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) and observability of $(C,A)$ that $(\hat{C},\hat{A})$ is also observable and ${\ell{(\hat{C},\hat{A})}} = \ell$. Then, we have $\begin{bmatrix}
\end{bmatrix} \in {{\mathcal{E}{(\ell,n)}} \cap \mathcal{O}}$ which proves [(a)](https://arxiv.org/html/2405.18962v1#S9.I1.i1 "item (a) ‣ Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system").

To prove [(b)](https://arxiv.org/html/2405.18962v1#S9.I1.i2 "item (b) ‣ Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system"), note that

since the two systems are isomorphic. The latter, together with ((https://arxiv.org/html/2405.18962v1#S9.E73 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")), implies that ${CA^{i}E_{- 1}} = 0$ for all $i \in {\lbrack 0,{\ell - 1}\rbrack}$. As $(C,A)$ is observable and $\ell = {\ell{(C,A)}}$, we see that $E_{- 1} = 0$. Since $E_{- 1} = {{\hat{A}E_{0}} + {\zeta\eta_{0}}}$, ((https://arxiv.org/html/2405.18962v1#S9.E72 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) and ((https://arxiv.org/html/2405.18962v1#S9.E73 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) imply that

for all $i \in {\lbrack 0,{\ell - 2}\rbrack}$. As $(C,A)$ is observable and $\ell = {\ell{(C,A)}}$, ((https://arxiv.org/html/2405.18962v1#S9.E81 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) and ((https://arxiv.org/html/2405.18962v1#S9.E82 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) imply that $E_{0} = 0$. Therefore, we have ${\zeta\eta_{0}} = {E_{- 1} - {\hat{A}E_{0}}} = 0$. Since $\zeta \neq 0$, this yields $\eta_{0} = 0$. Note that $E_{0} = {\sum_{k = 0}^{\ell - 1}{{\hat{A}}^{k}\zeta\eta_{k + 1}}} = 0$ due to ((https://arxiv.org/html/2405.18962v1#S9.E75 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")). From ((https://arxiv.org/html/2405.18962v1#S9.E72 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) and ((https://arxiv.org/html/2405.18962v1#S9.E73 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")), we have ${C{\hat{A}}^{\ell - 1}\zeta} \neq 0$. As such, the vectors ${\hat{A}}^{i}\zeta$ with $i \in {\lbrack 0,{\ell - 1}\rbrack}$ are linearly independent. Then, it follows from ${\sum_{k = 0}^{\ell - 1}{{\hat{A}}^{k}\zeta\eta_{k + 1}}} = 0$ that $\eta_{i} = 0$ for every $i \in {\lbrack 1,{\ell - 1}\rbrack}$. Thus, we have proven [(b)(i)](https://arxiv.org/html/2405.18962v1#S9.I1.i2.I1.i1 "item (b)(i) ‣ item (b) ‣ Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system").

To prove [(b)(ii)](https://arxiv.org/html/2405.18962v1#S9.I1.i2.I1.i2 "item (b)(ii) ‣ item (b) ‣ Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system"), note first that $\hat{B} = B$ as $E_{- 1} = 0$. Then, we have $0 = {{C{({{sI} - \hat{A}})}^{- 1}B} - {C{({{sI} - A})}^{- 1}B}} = {C{({{sI} - \hat{A}})}^{- 1}\zeta\xi{({{sI} - A})}^{- 1}B}$ where the first equality follows from isomorphism, the second is evident. Since $C{({{sI} - \hat{A}})}^{- 1}\zeta$ is a nonzero column vector, we see that ${\xi{({{sI} - A})}^{- 1}B} = 0$. This proves [(b)(ii)](https://arxiv.org/html/2405.18962v1#S9.I1.i2.I1.i2 "item (b)(ii) ‣ item (b) ‣ Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system"). ∎

### Example 25

We illustrate Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system") with the data in Section (https://arxiv.org/html/2405.18962v1#S5 "5 Illustrative example ‣ Beyond the fundamental lemma: from finite time series to linear system"). Consider the explaining system ((https://arxiv.org/html/2405.18962v1#S7.E46 "In Example 20 (State construction). ‣ 7.2 Proof of Theorem 7 ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")) for $(u_{\lbrack 0,4\rbrack},y_{\lbrack 0,4\rbrack})$. Note that ((https://arxiv.org/html/2405.18962v1#S9.E63 "In Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) is satisfied with $\xi = \begin{bmatrix}
\end{bmatrix}$, $\eta_{0} = \begin{bmatrix}
\end{bmatrix}$, and $\eta_{1} = \begin{bmatrix}
\end{bmatrix}$. Since $\ell = 1$ for ((https://arxiv.org/html/2405.18962v1#S7.E46 "In Example 20 (State construction). ‣ 7.2 Proof of Theorem 7 ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system")), $\zeta = {{col}{}}$ satisfies ((https://arxiv.org/html/2405.18962v1#S9.E64 "In Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")). Applying Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system"), we obtain the explaining system

with state $x_{\lbrack 0,5\rbrack} = \left. \lbrack\begin{array}{rrrrrr}
\end{array} \right\rbrack$. ∎

Using Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system"), we state a necessary condition for the isomorphism property.

### Lemma 26

Suppose that $n \geqslant \ell \geqslant 0$ and $\begin{bmatrix}
\end{bmatrix} \in {{\mathcal{E}{(\ell,n)}} \cap \mathcal{M}}$. Let $x_{\lbrack 0,T\rbrack} \in {\mathbb{R}}^{n \times {({T + 1})}}$ be a state for $\begin{bmatrix}
\end{bmatrix}$. If ${\mathcal{E}{(\ell,n)}} \cap \mathcal{M}$ has the isomorphism property, then $T \geqslant {\ell + {{({\ell + 1})}m} + n}$ and $J_{\ell}{(x)}$ has full row rank.

### Proof

Suppose first that $\ell = n = 0$. Since ${\mathcal{E}{}} \cap \mathcal{M}$ has the isomorphism property, $u_{\lbrack 0,{T - 1}\rbrack} = {J_{0}{(x)}}$ must have full row rank and hence $T \geqslant m$.

Now, suppose that $n \geqslant \ell \geqslant 1$. Let $d = {\min{(\ell,{T - 1})}}$, $\xi \in {\mathbb{R}}^{1 \times n}$ and $\eta_{i} \in {\mathbb{R}}^{1 \times m}$ with $i \in {\lbrack 0,d\rbrack}$ be vectors such that $\begin{bmatrix}
\xi & \eta_{0} & \cdots & \eta_{d}
\end{bmatrix} \in {{{lker}J_{d}}{(x)}}$. Also, let $\zeta_{0}$ be a nonzero vector be such that ${CA^{i}\zeta_{0}} = 0$ for $i \in {\lbrack 0,{\ell - 2}\rbrack}$. For $\varepsilon > 0$, let $\begin{bmatrix}
{\hat{A}}_{\varepsilon} & {\hat{B}}_{\varepsilon} \\
{\hat{C}}_{\varepsilon} & {\hat{D}}_{\varepsilon}
\end{bmatrix}$ denote the explaining system obtained from Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system") by taking $\zeta = {\varepsilon\zeta_{0}}$. Since $(A,B)$ is controllable, so is $({\hat{A}}_{\varepsilon},{\hat{B}}_{\varepsilon})$ for all sufficiently small $\varepsilon$. Hence, we see that $\begin{bmatrix}
{\hat{A}}_{\varepsilon} & {\hat{B}}_{\varepsilon} \\
{\hat{C}}_{\varepsilon} & {\hat{D}}_{\varepsilon}
\end{bmatrix} \in {{\mathcal{E}{(\ell,n)}} \cap \mathcal{M}}$ for some $\epsilon > 0$. Since ${\mathcal{E}{(\ell,n)}} \cap \mathcal{M}$ has the isomorphism property and $(A,B)$ is controllable, Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system").[(b)](https://arxiv.org/html/2405.18962v1#S9.I1.i2 "item (b) ‣ Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system") implies that $\xi = 0$ and $\eta_{i} = 0$ for all $i \in {\lbrack 0,d\rbrack}$. This means that $J_{d}{(x)}$ has full row rank. Since $T \geqslant 1$, $m \geqslant 1$, and $n \geqslant 1$, $J_{T - 1}{(x)}$ has at least 2 rows and exactly 1 column. As such, it cannot have full row rank. Then, we see that $d = {\min{(\ell,{T - 1})}} \neq {T - 1}$. Therefore, ${T - 1} > \ell$, $d = \ell$, and $J_{\ell}{(x)}$ has full row rank. This implies that $T \geqslant {\ell + {{({\ell + 1})}m} + n}$.∎

We now show how to construct an explaining system from a given one by increasing the state dimension and the lag.

### Lemma 27

Suppose that $n \geqslant 1$, $A \in {\mathbb{R}}^{n \times n}$, and $C \in {\mathbb{R}}^{p \times n}$ are such that $(C,A)$ is observable. Denote $\ell = {\ell{(C,A)}}$. Let $\zeta \in {\mathbb{R}}^{n}$ be such that

Also, let $n^{\prime} \geqslant 1$, $A^{\prime} \in {\mathbb{R}}^{n^{\prime} \times n^{\prime}}$ and $C^{\prime} \in {\mathbb{R}}^{1 \times n^{\prime}}$ be such that $(C^{\prime},A^{\prime})$ is observable. Then, the pair

is observable and $\overline{\ell}:={\ell{(\overline{C},\overline{A})}} = {\ell + n^{\prime}}$. Moreover, if $\zeta^{\prime} \in {\mathbb{R}}^{n^{\prime}}$ satisfies

### Proof

By direct inspection, we see that ${\overline{C}{\overline{A}}^{k}} = \begin{bmatrix}
\end{bmatrix}$ where $\Xi_{0} = 0$, $\Xi_{k + 1} = {{CA^{k}\zeta C^{\prime}} + {\Xi_{k}A^{\prime}}}$ for all $k \geqslant 0$. By using ((https://arxiv.org/html/2405.18962v1#S9.E83 "In Lemma 27. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")), we further see that

$\Xi_{k} = 0$ for all $k \in {\lbrack 0,{\ell - 1}\rbrack}$, and

$\Xi_{\ell} = {CA^{\ell - 1}\zeta C^{\prime}}$.

Let ${\overline{\Omega}}_{k}$, $\Omega_{k}$, and $\Omega_{k}^{\prime}$ be the $k$-th observability matrices of the pairs $(\overline{C},\overline{A})$, $(C,A)$, and $(C^{\prime},A^{\prime})$, respectively. We claim that

for all $i \geqslant 0$. To show this, let $i \geqslant 0$. Note that ${\overline{\Omega}}_{\ell + i}$ is of the form

From [(ii)](https://arxiv.org/html/2405.18962v1#S9.I2.i2 "item (ii) ‣ Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system") and ((https://arxiv.org/html/2405.18962v1#S9.E83 "In Lemma 27. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")), it follows that

Since $(C,A)$ is observable and ${\ell{(C,A)}} = \ell$, ${{rank}\Omega_{\ell - 1}} = n$. Therefore, we see from ((https://arxiv.org/html/2405.18962v1#S9.E87 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) that ((https://arxiv.org/html/2405.18962v1#S9.E86 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) holds. Since $C^{\prime} \in {\mathbb{R}}^{1 \times n^{\prime}}$ and $(C^{\prime},A^{\prime})$ is observable, we have ${\ell{(C^{\prime},A^{\prime})}} = n^{\prime}$. Then, ((https://arxiv.org/html/2405.18962v1#S9.E86 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) implies that ${{rank}{\overline{\Omega}}_{{\ell + n^{\prime}} - 1}} = {n + n^{\prime}}$ and hence that $(\overline{C},\overline{A})$ is observable. It also follows from ((https://arxiv.org/html/2405.18962v1#S9.E86 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) that ${{rank}{\overline{\Omega}}_{{\ell + n^{\prime}} - 2}} < {n + n^{\prime}}$. This means that ${\ell{(\overline{C},\overline{A})}} = {\ell + n^{\prime}}$. Further, if $\zeta^{\prime}$ satisfies ((https://arxiv.org/html/2405.18962v1#S9.E84 "In Lemma 27. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) then $\zeta^{\prime} \in {\ker\Omega_{n^{\prime} - 2}^{\prime}}$ and $\zeta^{\prime} \notin {\ker\Omega_{n^{\prime} - 1}^{\prime}}$. From ((https://arxiv.org/html/2405.18962v1#S9.E87 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) and ((https://arxiv.org/html/2405.18962v1#S9.E88 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")), it follows that $\begin{bmatrix}
\end{bmatrix} \in {\ker{\overline{\Omega}}_{{\ell + n^{\prime}} - 2}}$ and $\begin{bmatrix}
\end{bmatrix} \notin {\ker{\overline{\Omega}}_{{\ell + n^{\prime}} - 1}}$. Hence, ((https://arxiv.org/html/2405.18962v1#S9.E85 "In Lemma 27. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) holds.∎

### Lemma 28

Suppose that $n \geqslant \ell \geqslant 0$ and $\begin{bmatrix}
\end{bmatrix} \in {{\mathcal{E}{(\ell,n)}} \cap \mathcal{M}}$. Let $x_{\lbrack 0,T\rbrack} \in {\mathbb{R}}^{n \times {({T + 1})}}$ be a state for $\begin{bmatrix}
\end{bmatrix}$. If $\mu \geqslant 1$ and ${{\mathcal{E}{({\ell + \mu},{n + \mu})}} \cap \mathcal{M}} = \varnothing$, then $T \geqslant {\ell + \mu + {{({\ell + \mu + 1})}m} + n}$ and $J_{\ell + \mu}{(x)}$ has full row rank.

### Proof

Let $\lambda \in {\mathbb{R}}$, $A_{\lambda}^{\prime} \in {\mathbb{R}}^{\mu \times \mu}$ be the Jordan block with the eigenvalue $\lambda$, $C^{\prime}:=e_{1}^{T}$, and $\zeta^{\prime}:=e_{\mu}$ where $e_{i}$ denotes the $i$th standard basis vector of ${\mathbb{R}}^{\mu}$. Clearly, $(C^{\prime},A_{\lambda}^{\prime})$ is observable and ${\ell{(C^{\prime},A_{\lambda}^{\prime})}} = \mu$. In addition, we have that ${{C^{\prime}{(A_{\lambda}^{\prime})}^{i}\zeta^{\prime}} = 0}\mspace{21mu}{{\forall i} \in {\lbrack 0,{\mu - 2}\rbrack}}$ and ${{C^{\prime}{(A_{\lambda}^{\prime})}^{\mu - 1}\zeta^{\prime}} = 1}.$

We claim that $J_{d}{(x)}$ has full row rank where $d = {\min{({\ell + \mu},{T - 1})}}$. To prove it we consider the cases $n = 0$ and $n \geqslant 1$.

For the case $n = 0$, we have that $\ell = 0$, $x$ is a void matrix, and $y_{\lbrack 0,{T - 1}\rbrack} = {Du_{\lbrack 0,{T - 1}\rbrack}}$ for some $D \in {\mathbb{R}}^{p \times m}$. Therefore, for every nonzero $\theta \in {\mathbb{R}}^{p}$, $z_{\lbrack 0,T\rbrack}:=0_{\mu \times {({T + 1})}}$ is a state for $\begin{bmatrix}
\end{bmatrix} \in {{\mathcal{E}{(\mu,\mu)}} \cap \mathcal{O}}$. Let $\eta_{i}$ with $i \in {\lbrack 0,d\rbrack}$ be such that $\begin{bmatrix}
\eta_{0} & \cdots & \eta_{d}
\end{bmatrix} \in {{{lker}J_{d}}{(x)}}$. Clearly, we have $\begin{bmatrix}
0_{1,\mu} & \eta_{0} & \cdots & \eta_{d}
\end{bmatrix} \in {{{lker}J_{d}}{(z)}}$. Define

where ${E_{d} = {0\text{and}E_{i - 1}} = {{{\hat{A}}_{\lambda}E_{i}} + {\zeta^{\prime}\eta_{i}\text{for}i}} \in {\lbrack 0,d\rbrack}}.$ Since $d = {\min{(\mu,{T - 1})}}$ for this case, it follows from Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system").[(a)](https://arxiv.org/html/2405.18962v1#S9.I1.i1 "item (a) ‣ Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system") that $\begin{bmatrix}
{\hat{A}}_{\lambda} & {\hat{B}}_{\lambda} \\
\end{bmatrix} \in {{\mathcal{E}{(\mu,\mu)}} \cap \mathcal{O}}$. Since ${{\mathcal{E}{(\mu,\mu)}} \cap \mathcal{M}} = \varnothing$ due to the hypothesis, $({\hat{A}}_{\lambda},{\hat{B}}_{\lambda})$ is uncontrollable. From the fact that ${\hat{A}}_{\lambda} = A_{\lambda}^{\prime}$ is a Jordan block, we see that ${{(\zeta^{\prime})}^{T}A_{\lambda}^{\prime}} = {\lambda{(\zeta^{\prime})}^{T}}$ and ${{(\zeta^{\prime})}^{T}E_{- 1}} = 0$. Since $E_{- 1} = {\sum_{k = 0}^{d}{{(A_{\lambda}^{\prime})}^{k}\zeta^{\prime}\eta_{k}}}$ due to ((https://arxiv.org/html/2405.18962v1#S9.E75 "In Proof. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")), we see that ${\sum_{k = 0}^{d}{\lambda^{k}\eta_{k}}} = 0$. As $\lambda$ is an arbitrary real number, we conclude that $\eta_{i} = 0$ for every $i \in {\lbrack 0,d\rbrack}$ and hence $J_{d}{(x)}$ has full row rank.

For the case $n \geqslant 1$, let $\zeta \in {\mathbb{R}}^{n}$ be as in ((https://arxiv.org/html/2405.18962v1#S9.E83 "In Lemma 27. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) and define $\overline{C}:=\begin{bmatrix}
\end{bmatrix}$, ${\overline{A}}_{\varepsilon,\lambda}:=\begin{bmatrix}
A & {\varepsilon\zeta C^{\prime}} \\
\end{bmatrix}$, $\overline{B}:=\begin{bmatrix}
\end{bmatrix}$ for $\varepsilon > 0$. Then, it follows from Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 27. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system") that $(\overline{C},{\overline{A}}_{\varepsilon,\lambda})$ is observable, $\ell{(\overline{C},{\overline{A}}_{\varepsilon,\lambda})} = \ell + \mu =:\overline{\ell}$,

Note that $\begin{bmatrix}
{\overline{A}}_{\varepsilon,\lambda} & \overline{B} \\
\end{bmatrix} \in {{\mathcal{E}{({\ell + \mu},{n + \mu})}} \cap \mathcal{O}}$ and $z_{\lbrack 0,T\rbrack}:=\begin{bmatrix}
\end{bmatrix}$ is a state for $\begin{bmatrix}
{\overline{A}}_{\varepsilon,\lambda} & \overline{B} \\
\end{bmatrix}$. Let $d = {\min{({\ell + \mu},{T - 1})}}$. Also, let $\xi \in {\mathbb{R}}^{1 \times n}$, $\eta_{i}$ with $i \in {\lbrack 0,d\rbrack}$ be such that $\begin{bmatrix}
\xi & \eta_{0} & \cdots & \eta_{d}
\end{bmatrix} \in {{{lker}J_{d}}{(x)}}$. Clearly, we have $\begin{bmatrix}
\xi & 0_{1,\mu} & \eta_{0} & \cdots & \eta_{d}
\end{bmatrix} \in {{{lker}J_{d}}{(z)}}$. Define

where ${E_{d} = {0\text{and}E_{i - 1}} = {{{\hat{A}}_{\varepsilon,\lambda}E_{i}} + {\begin{bmatrix}
\end{bmatrix}\eta_{i}\text{for}i}} \in {\lbrack 0,d\rbrack}}.$ Then, it follows from Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system").[(a)](https://arxiv.org/html/2405.18962v1#S9.I1.i1 "item (a) ‣ Lemma 24. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system") that $\begin{bmatrix}
{\hat{A}}_{\varepsilon,\lambda} & {\hat{B}}_{\varepsilon} \\
\overline{C} & {\hat{D}}_{\varepsilon}
\end{bmatrix} \in {{\mathcal{E}{({\ell + \mu},{n + \mu})}} \cap \mathcal{O}}$. From the hypothesis, we know that $({\hat{A}}_{\varepsilon,\lambda},{\hat{B}}_{\varepsilon,\lambda})$ is uncontrollable. By taking the limit as $\varepsilon$ tends to zero, we conclude that $({\hat{A}}_{0,\lambda},{\hat{B}}_{0,\lambda})$ is uncontrollable as well. Note that

where $F_{d} = 0$ and $F_{i - 1} = {{{\hat{A}}_{0,\lambda}F_{i}} + {\begin{bmatrix}
\end{bmatrix}\eta_{i}}}$ for $i \in {\lbrack 0,d\rbrack}$. Suppose that $\lambda$ is not an eigenvalue of $A$. Then, every left eigenvector of ${\hat{A}}_{0,\lambda}$ corresponding to an eigenvalue of $A$ must be of the form $\begin{bmatrix}
\end{bmatrix}$ where $v \in {\mathbb{C}}^{1 \times n}$. From ${{(\zeta^{\prime})}^{T}A_{\lambda}} = {\lambda{(\zeta^{\prime})}^{T}}$, we see that left eigenvectors of ${\hat{A}}_{0,\lambda}$ corresponding to the eigenvalue $\lambda$ are nonzero multiples of $\begin{bmatrix}
{\xi{({{\lambda I} - A})}^{- 1}} & {(\zeta^{\prime})}^{T}
\end{bmatrix}$. Since $(A,B)$ is controllable but $({\hat{A}}_{0,\lambda},{\hat{B}}_{0,\lambda})$ is uncontrollable, it follows from the Hautus test that ${\begin{bmatrix}
{\xi{({{\lambda I} - A})}^{- 1}} & {(\zeta^{\prime})}^{T}
\end{bmatrix}{\hat{B}}_{0,\lambda}} = 0$. Since $F_{- 1} = {\sum_{k = 0}^{d}{{\hat{A}}_{0,\lambda}^{k}\begin{bmatrix}
\end{bmatrix}\eta_{k}}}$, we see that ${{{\xi{({{\lambda I} - A})}^{- 1}B} + {\sum_{k = 0}^{d}{\lambda^{k}\eta_{k}}}} = 0}.$ Since this equality holds for all $\lambda \in {\mathbb{R}}$ that are not eigenvalues of $A$, we conclude that $\eta_{i} = 0$ for $i \in {\lbrack 0,d\rbrack}$ and ${\xi{({{\lambda I} - A})}^{- 1}B} = 0$. Since $(A,B)$ is controllable we conclude that $\xi = 0$ and that $J_{d}{(x)}$ has full row rank.

To prove that $J_{\ell + \mu}{(x)}$ has full row rank, note that $J_{T - 1}{(x)}$ has at least $2$ rows and exactly $1$ column since $T \geqslant 1$, $m \geqslant 1$, and $n \geqslant 1$. As such, it cannot have full row rank. Then, we see that $d = {\min{({\ell + \mu},{T - 1})}} \neq {T - 1}$. Therefore, ${T - 1} > {\ell + \mu}$, $d = {\ell + \mu}$, and $J_{\ell + \mu}{(x)}$ has full row rank. The latter implies that $T \geqslant {\ell + \mu + {{({\ell + \mu + 1})}m} + n}$.∎

### Proof of Theorem [9](https://arxiv.org/html/2405.18962v1#Thmtheorem9 "Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system"): necessity part

Assume that the data are informative for system identification in $\mathcal{S}_{{\lbrack L_{-},L_{+}\rbrack},{\lbrack N_{-},N_{+}\rbrack}} \cap \mathcal{M}$. Let $\begin{bmatrix}
\end{bmatrix} \in {{\mathcal{E}{(\ell_{true},n_{true})}} \cap \mathcal{M}}$ and let $x \in {\mathbb{R}}^{n \times {({T + 1})}}$ be a state for $\begin{bmatrix}
\end{bmatrix}$. Since ${\mathcal{E}{(n_{true})}} \cap \mathcal{M}$ has the isomorphism property, we have ${{\mathcal{E}{(n_{true})}} \cap \mathcal{M}} = {{\mathcal{E}{(\ell_{true},n_{true})}} \cap \mathcal{M}}$. Then, Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 26. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system") implies that

and $J_{\ell_{true}}{(x)}$ has full row rank whereas Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 21. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system").[(b)](https://arxiv.org/html/2405.18962v1#S8.I1.i2 "item (b) ‣ Lemma 21. ‣ 8.1 On the ranks of state-input data Hankel matrices ‣ 8 State-input data Hankel matrices ‣ Beyond the fundamental lemma: from finite time series to linear system") implies that $\delta_{k} = \rho_{k}$ for every $k \in {\lbrack 0,\ell_{true}\rbrack}$. As $\rho_{\ell_{true} - 1} \geqslant 1$ due to Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 17. ‣ 6.1 The lag structure of a system ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system").[(b)](https://arxiv.org/html/2405.18962v1#S6.I1.i2 "item (b) ‣ Lemma 17. ‣ 6.1 The lag structure of a system ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system"), we see that $q \geqslant \ell_{true}$. Then, Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem8 "Theorem 8. ‣ 4.4 The shortest lag and the minimum number of states ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") implies that $\ell_{\min} \geqslant \ell_{true}$. Since the reverse inequality readily follows from the definition of $\ell_{\min}$ in ((https://arxiv.org/html/2405.18962v1#S4.E15 "In 4.4 The shortest lag and the minimum number of states ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")), we have $\ell_{true} = \ell_{\min}$. Further, Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem8 "Theorem 8. ‣ 4.4 The shortest lag and the minimum number of states ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") and Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 17. ‣ 6.1 The lag structure of a system ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system").[(c)](https://arxiv.org/html/2405.18962v1#S6.I1.i3 "item (c) ‣ Lemma 17. ‣ 6.1 The lag structure of a system ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system") imply that $n_{true} = n_{\min}$. Then, ([19a](https://arxiv.org/html/2405.18962v1#S4.E19.1 "In 19 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) and ([19b](https://arxiv.org/html/2405.18962v1#S4.E19.2 "In 19 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) follow from ((https://arxiv.org/html/2405.18962v1#S3.E6 "In 3.2 Informativity for system identification ‣ 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system")).

If $L_{+}^{a} = \ell_{true}$, ([19c](https://arxiv.org/html/2405.18962v1#S4.E19.3 "In 19 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) readily follows from ((https://arxiv.org/html/2405.18962v1#S9.E90 "In 9.1 Proof of Theorem 9: necessity part ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) and ([19d](https://arxiv.org/html/2405.18962v1#S4.E19.4 "In 19 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) follows from ${{rank}H_{\ell_{true}}} = {{{rank}J_{\ell_{true}}}{(x)}}$ and $J_{\ell_{true}}{(x)}$ having full row rank. Suppose that $L_{+}^{a} > \ell_{true}$. Note that the informativity of the data for system identification within $\mathcal{S}_{{\lbrack L_{-},L_{+}\rbrack},{\lbrack N_{-},N_{+}\rbrack}} \cap \mathcal{M}$ implies that ${{\mathcal{E}{({\ell_{true} + \mu},{n_{true} + \mu})}} \cap \mathcal{M}} = \varnothing$ where $\mu = {L_{+}^{a} - \ell_{true}}$. Then, Lemma (https://arxiv.org/html/2405.18962v1# "Lemma 28. ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system") implies that ([19c](https://arxiv.org/html/2405.18962v1#S4.E19.3 "In 19 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) holds and $J_{L_{+}^{a}}{(x)}$ has full row rank. Since ${{rank}H_{L_{+}^{a}}} = {{{rank}J_{L_{+}^{a}}}{(x)}}$, we see that ([19d](https://arxiv.org/html/2405.18962v1#S4.E19.4 "In 19 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) holds. $\square$

### Proposition [4](https://arxiv.org/html/2405.18962v1#Thmtheorem4 "Proposition 4. ‣ 3.3 Two relevant results ‣ 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system") vs. Theorem [9](https://arxiv.org/html/2405.18962v1#Thmtheorem9 "Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")

We want to show that the condition

appearing in Proposition (https://arxiv.org/html/2405.18962v1#Thmtheorem4 "Proposition 4. ‣ 3.3 Two relevant results ‣ 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system") implies the conditions ([19a](https://arxiv.org/html/2405.18962v1#S4.E19.1 "In 19 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")), ([19b](https://arxiv.org/html/2405.18962v1#S4.E19.2 "In 19 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")), and ([19d](https://arxiv.org/html/2405.18962v1#S4.E19.4 "In 19 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) of Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem9 "Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system"). Let $\begin{bmatrix}
\end{bmatrix} \in {\mathcal{E}{(n_{\min})}}$ and let $x_{\lbrack 0,T\rbrack} \in {\mathbb{R}}^{n_{\min} \times {({T + 1})}}$ be a state for $\begin{bmatrix}
\end{bmatrix}$. Since ${{L_{+} + N_{+}} - 1} \geqslant \ell_{\min}$, we see from ((https://arxiv.org/html/2405.18962v1#S6.E26 "In 6.2 Lag structures and 𝛿_𝑘 integers ‣ 6 Lag structures of explaining systems ‣ Beyond the fundamental lemma: from finite time series to linear system")) and ((https://arxiv.org/html/2405.18962v1#S9.E91 "In 9.2 Proposition 4 vs. Theorem 9 ‣ 9 From one explaining system to another ‣ Beyond the fundamental lemma: from finite time series to linear system")) that ${{{rank}J_{{L_{+} + N_{+}} - 1}}{(x)}} = {{{({L_{+} + N_{+}})}m} + n_{true}}$. This implies that $n_{true} \leqslant n_{\min}$. Since the reverse inequality holds due to ((https://arxiv.org/html/2405.18962v1#S4.E16 "In 4.4 The shortest lag and the minimum number of states ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")), we see that $n_{\min} = n_{true}$. Then, it follows from Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem8 "Theorem 8. ‣ 4.4 The shortest lag and the minimum number of states ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") that $\ell_{\min} = \ell_{true}$. Therefore, ([19a](https://arxiv.org/html/2405.18962v1#S4.E19.1 "In 19 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")), ([19b](https://arxiv.org/html/2405.18962v1#S4.E19.2 "In 19 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")), and ([19d](https://arxiv.org/html/2405.18962v1#S4.E19.4 "In 19 ‣ Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")) are satisfied.

## Conclusions

We stated necessary and sufficient conditions for informativity for system identification in the class of minimal ISO systems whose lag and state dimension lie between given lower/upper bounds (see Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem9 "Theorem 9. ‣ 4.6 Data informativity for system identification ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system")). To establish such result we obtained some intermediate ones of independent interest, most prominently the iterative construction of a state sequence and a corresponding ISO model in the proof of Theorem (https://arxiv.org/html/2405.18962v1#Thmtheorem7 "Theorem 7. ‣ 4.3 Constructing an explaining system ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system").

We aim to apply the concept of informativity for system identification in a model class (see Definition (https://arxiv.org/html/2405.18962v1#Thmtheorem1 "Definition 1. ‣ 3.2 Informativity for system identification ‣ 3 Problem formulation ‣ Beyond the fundamental lemma: from finite time series to linear system")) to other classes than minimal systems, e.g. to dissipative systems. We also plan to work on the application of the informativity concept to identification in the behavioral framework, where interesting results (see \[(https://arxiv.org/html/2405.18962v1#bib.bib36)\]) have recently appeared.
