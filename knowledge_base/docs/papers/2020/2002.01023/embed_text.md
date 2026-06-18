## Introduction

In the seminal work by Willems and coauthors, it was shown that a single, sufficiently exciting trajectory of a linear system can be used to parameterize *all* trajectories that the system can produce. This result has later been named the *fundamental lemma*, and plays an important role in the learning and control of dynamical systems on the basis of measured data.

An immediate consequence of the fundamental lemma is that a persistently exciting trajectory captures the entire behavior of the data-generating system, thus allowing successful identification of a system model using subspace methods. The lemma also enables data-driven simulation, which involves the computation of the system's response to a given reference input. In addition, Willems' lemma is instrumental in the design of controllers from data. The result has been applied to tackle several control problems, ranging from output matching to control by interconnection, predictive control, optimal and robust control, linear quadratic regulation as well as set-invariance control.

All of the above examples show the value of the fundamental lemma in modeling, simulation and control using a *single* measured system trajectory. Nonetheless, there are many scenarios in which *multiple* system trajectories are measured instead of a single one. For example, performing multiple short experiments becomes desirable when the data-generating system has unstable dynamics. Also, as pointed out in, a single system trajectory collected during normal operations may be too poorly excited to reveal the system dynamics. In contrast, multiple archival data may *collectively* provide a well-excited experiment. Another situation is when a single trajectory is measured but some of the samples are corrupted or missing. In this case, we have access to multiple system trajectories consisting of the remaining, uncorrupted, data samples. System identification from multiple experiments and from data with missing samples has been studied. However, a proof of Willems' lemma for multiple trajectories is still missing. Therefore, in this paper we aim at extending Willems' fundamental lemma to the case where multiple trajectories, possibly of different lengths, are given instead of a single one.

Originally, the fundamental lemma was formulated and proven in a behavioral context. The starting point in this paper, however, is a reformulation of the lemma in terms of state-space systems. Such a version of Willems' fundamental lemma has appeared before in \[9, Lem. 2\] and \[18, Thm. 3\] but no proof of the statement was given in this context. Our first contribution is to provide a complete and self-contained proof of the lemma for state-space systems. Strictly speaking, such an alternative proof is not necessary since the original proof of applies to state-space systems as a special case. Nonetheless, we believe that our proof can be of interest to researchers who want to apply Willems' lemma to state-space systems. In fact, the proof is *elementary* in the sense that it only makes use of basic concepts such as the Cayley-Hamilton theorem and Kalman controllability test. The proof is also direct, and in contrast to does not rely on a contradiction argument.

Our second contribution involves the extension of the fundamental lemma to the case of multiple trajectories. To this end, we first introduce a notion of *collective* persistency of excitation. Then, analogous to Willems' lemma, we show that a finite number of given trajectories can be used to parameterize all trajectories of the system, assuming that collective persistency of excitation holds. We will illustrate this result by two examples. First, we will show that the extended fundamental lemma enables the identification of linear systems from data sets with missing samples. Next, we will show how the result can be used to compute controllers of unstable systems from multiple short system trajectories, even when this is problematic from a single long trajectory.

The paper is organized as follows: in Section II we formulate and prove Willems' fundamental lemma. Section III extends the lemma to multiple trajectories. In Section IV we provide applications of this result. Finally, Section V contains our conclusions.

### I-A Notation

The *left kernel* of a real matrix $M$ is the space of all real row vectors $v$ such that ${vM} = 0$. The zero vector of dimension $n$ is denoted by $0_{n}$. Consider a signal $f:{{\mathbb{Z}}\rightarrow{\mathbb{R}}^{\bullet}}$ and let ${i,j} \in {\mathbb{Z}}$ be integers such that $i \leq j$. We denote by $f_{\lbrack i,j\rbrack}$ the restriction of $f$ to the interval $\lbrack i,j\rbrack$, that is,

With slight abuse of notation, we will also use the notation $f_{\lbrack i,j\rbrack}$ to refer to the sequence ${f{(i)}},{f{({i + 1})}},\ldots,{f{(j)}}$. Let $k$ be a positive integer such that $k \leq {{j - i} + 1}$ and define the *Hankel matrix* of depth $k$, associated with $f_{\lbrack i,j\rbrack}$, as

Note that the subscript $k$ refers to the number of block rows of the Hankel matrix.

### Definition 1

The sequence $f_{\lbrack i,j\rbrack}$ is said to be *persistently exciting of order $k$* if $\mathcal{H}_{k}{(f_{\lbrack i,j\rbrack})}$ has full row rank.

## Willems *et al.*'s fundamental lemma in the context of state-space systems

In this section we explain the fundamental lemma in a state-space setting. Our goal is to provide a simple and self-contained proof of the result within this context. Consider the linear time-invariant (LTI) system

$\mathbf{x}{({t + 1})}$ $= {{A\mathbf{x}{(t)}} + {B\mathbf{u}{(t)}}}$ (1a)
$\mathbf{y}{(t)}$ ${= {{C\mathbf{x}{(t)}} + {D\mathbf{u}{(t)}}}},$ (1b)

where $\mathbf{x} \in {\mathbb{R}}^{n}$ denotes the state, $\mathbf{u} \in {\mathbb{R}}^{m}$ is the input and $\mathbf{y} \in {\mathbb{R}}^{p}$ is the output. Let $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ be a given input/output trajectory^11^1Throughout this paper, we denote variables such as $\mathbf{u}$ and $\mathbf{y}$ by bold font characters, and specific instances of such variables in normal font, e.g., ${u{}},{u{}},\ldots$ and ${y{}},{y{}},\ldots$. of. We consider the Hankel matrices of these inputs and outputs, given by:

where $L \geq 1$. Clearly, each column of contains a length $L$ input/output trajectory of. By linearity of the system, every linear combination of the columns of is also a trajectory of. In other words,

is an input/output trajectory of for any real vector $g$.

The powerful crux of Willems *et al.*'s fundamental lemma is that *every* length $L$ input/output trajectory of can be expressed in terms of $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ as in, assuming that $u_{\lbrack 0,{T - 1}\rbrack}$ is persistently exciting. The result has appeared first in a behavioral context in \[1, Thm. 1\]. In Theorem 1, we will formulate the fundamental lemma for systems of the form. The theorem consists of two statements. First, under controllability and excitation assumptions, a rank condition on the state and input Hankel matrices (4 ‣ Theorem 1 ‣ II Willems et al.’s fundamental lemma in the context of state-space systems ‣ Willems’ Fundamental Lemma for State-space Systems and its Extension to Multiple Datasets")) is satisfied. Second, under the same conditions, all length $L$ input/output trajectories of can be written as a linear combination of the columns of the matrix.

### Theorem 1

Consider the system and assume that the pair $(A,B)$ is controllable. Let $(u_{\lbrack 0,{T - 1}\rbrack},x_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ be an input/state/output trajectory of. Assume that the input $u_{\lbrack 0,{T - 1}\rbrack}$ is persistently exciting of order $n + L$. Then the following statements hold:

has full row rank.

Every length $L$ input/output trajectory of can be expressed in terms of $u_{\lbrack 0,{T - 1}\rbrack}$ and $y_{\lbrack 0,{T - 1}\rbrack}$ as follows: $({\overline{u}}_{\lbrack 0,{L - 1}\rbrack},{\overline{y}}_{\lbrack 0,{L - 1}\rbrack})$ is an input/output trajectory of if and only if

for some real vector $g$.

Statement (i) ‣ Theorem 1 ‣ II Willems et al.’s fundamental lemma in the context of state-space systems ‣ Willems’ Fundamental Lemma for State-space Systems and its Extension to Multiple Datasets") has appeared first in the original paper by Willems and coworkers, c.f. \[1, Cor. 2(iii)\]. The result is intriguing since a rank condition on *both* input and state matrices can be inposed by injecting a sufficiently exciting input sequence. This rank condition is important from a design perspective and plays a fundamental role in MOESP type subspace algorithms, c.f. \[4, Sec. 3.3\]. Also, in the case that $L = 1$, full row rank of (4 ‣ Theorem 1 ‣ II Willems et al.’s fundamental lemma in the context of state-space systems ‣ Willems’ Fundamental Lemma for State-space Systems and its Extension to Multiple Datasets")) has been shown to be instrumental for the construction of state feedback controllers from data. In our work, statement (i) ‣ Theorem 1 ‣ II Willems et al.’s fundamental lemma in the context of state-space systems ‣ Willems’ Fundamental Lemma for State-space Systems and its Extension to Multiple Datasets") is used to prove the second statement of Theorem 1. Statement (ii) ‣ Theorem 1 ‣ II Willems et al.’s fundamental lemma in the context of state-space systems ‣ Willems’ Fundamental Lemma for State-space Systems and its Extension to Multiple Datasets") is a reformulation of \[1, Thm. 1\]. In what follows, we provide a self-contained and elementary proof of the fundamental lemma in a state-space context.

### Proof

Statement (ii) ‣ Theorem 1 ‣ II Willems et al.’s fundamental lemma in the context of state-space systems ‣ Willems’ Fundamental Lemma for State-space Systems and its Extension to Multiple Datasets") has been proven assuming statement (i) ‣ Theorem 1 ‣ II Willems et al.’s fundamental lemma in the context of state-space systems ‣ Willems’ Fundamental Lemma for State-space Systems and its Extension to Multiple Datasets") in \[9, Lemma 2\]. It therefore remains to be shown that (4 ‣ Theorem 1 ‣ II Willems et al.’s fundamental lemma in the context of state-space systems ‣ Willems’ Fundamental Lemma for State-space Systems and its Extension to Multiple Datasets")) has full row rank. Let $\begin{bmatrix}
\end{bmatrix}$ be a vector in the left kernel of (4 ‣ Theorem 1 ‣ II Willems et al.’s fundamental lemma in the context of state-space systems ‣ Willems’ Fundamental Lemma for State-space Systems and its Extension to Multiple Datasets")), where $\xi^{\top} \in {\mathbb{R}}^{n}$ and $\eta^{\top} \in {\mathbb{R}}^{mL}$. We will first show that $\xi$ and $\eta$ can be used to construct $n + 1$ vectors in the left kernel of the "deeper" Hankel matrix

First, by definition of $\xi$ and $\eta$, it is clear that

Next, by the laws of system (1a) we have

Using this fact, we see that

where the latter equality holds by definition of $\xi$ and $\eta$. Now, by repeatedly exploiting the laws of (1a) and using the same arguments we find that the $n + 1$ vectors

are all contained in the left kernel of the matrix. By persistency of excitation, $\mathcal{H}_{n + L}{(u_{\lbrack 0,{T - 1}\rbrack})}$ has full row rank, and hence the left kernel of has dimension at most $n$. Therefore, the $n + 1$ vectors in are linearly dependent. We claim that this implies $\eta = 0$. To prove this claim, partition $\eta = \begin{bmatrix}
\eta_{1} & \eta_{2} & \cdots & \eta_{L}
\end{bmatrix}$, where ${\eta_{1}^{\top},\eta_{2}^{\top},\ldots,\eta_{L}^{\top}} \in {\mathbb{R}}^{m}$. Since the last $m$ entries of the vectors $w_{0},w_{1},\ldots,w_{n - 1}$ are zero, the linear dependence of the vectors implies $\eta_{L} = 0$ by inspection of $w_{n}$. We substitute this equation in $\eta$ and conclude that the last $2m$ entries of $w_{0},w_{1},\ldots,w_{n - 1}$ are zero. As such, also $\eta_{L - 1} = 0$. We can proceed with these substitutions to show that $\eta_{1} = \eta_{2} = {\cdots\eta_{L}} = 0$, i.e., $\eta = 0$. Next, by Cayley-Hamilton theorem, ${\sum_{i = 0}^{n}{\alpha_{i}A^{i}}} = 0$ where $\alpha_{i} \in {\mathbb{R}}$ for all $i = {0,1,\ldots,n}$, and $\alpha_{n} = 1$. Define the linear combination $v:={\sum_{i = 0}^{n}{\alpha_{i}w_{i}}}$. By and by substitution of $\eta = 0$, the vector $v$ is equal to

This implies that the vector

is contained in the left kernel of $\mathcal{H}_{n}{(u_{\lbrack 0,{T - L - 1}\rbrack})}$, which is zero by persistency of excitation. In other words,

Since $\alpha_{n} = 1$ it follows from the last equation that ${\xiB} = 0$. Substitution in the second to last equation then results in ${\xiAB} = 0$. We continue by backward substitution to obtain ${\xiB} = {\xiAB} = \cdots = {\xiA^{n - 1}B} = 0$. Controllability of $(A,B)$ hence results in $\xi = 0$. We therefore conclude that (4 ‣ Theorem 1 ‣ II Willems et al.’s fundamental lemma in the context of state-space systems ‣ Willems’ Fundamental Lemma for State-space Systems and its Extension to Multiple Datasets")) has full row rank, which proves the theorem. ∎

## Extension of Willems *et al.*'s lemma to multiple trajectories

In this section we propose an extension of the fundamental lemma that is applicable to the case in which *multiple* system trajectories are given. Our approach will require the notion of *collective* persistency of excitation.

### Definition 2

Consider the input sequences $u_{\lbrack 0,{T_{i} - 1}\rbrack}^{i}$ for $i = {1,2,\ldots,q}$, where $q$ is the number of data sets. Let $k$ be a positive integer such that $k \leq T_{i}$ for all $i$. The input sequences $u_{\lbrack 0,{T_{i} - 1}\rbrack}^{i}$ for $i = {1,2,\ldots,q}$ are called *collectively persistently exciting* of order $k$ if the mosaic-Hankel matrix

has full row rank.

Collective persistency of excitation is more flexible than the persistency of excitation of a single input sequence. Indeed, for the input sequences $u_{\lbrack 0,T_{i}\rbrack}^{i}$ to be collectively persistently exciting, it is sufficient that at least one of them is persistently exciting. However, this is clearly not necessary: the sequences $u_{\lbrack 0,T_{i}\rbrack}^{i}$ may be collectively persistently exciting even when none of the individual input sequences is persistently exciting. The added flexibility of collective persistency of excitation is also apparent from the *length* of the input sequences. Indeed, a single $u_{\lbrack 0,{T - 1}\rbrack}$ can only be persistently exciting of order $k$ if $T \geq {{k{({m + 1})}} - 1}$. In comparison, for collective persistency of excitation of order $k$ it is necessary that ${\sum_{i = 1}^{q}T_{i}} \geq {{k{({m + q})}} - q}$. This means that collective persistency of excitation can be achieved by input sequences having length $T_{i}$ as short as $k$, assuming the number of data sets $q$ is sufficiently large. In the next theorem we extend the fundamental lemma to the case of multiple data sets.

### Theorem 2

Consider system and assume that the pair $(A,B)$ is controllable. Let $(u_{\lbrack 0,{T_{i} - 1}\rbrack}^{i},x_{\lbrack 0,{T_{i} - 1}\rbrack}^{i},y_{\lbrack 0,{T_{i} - 1}\rbrack}^{i})$ be an input/state/output trajectory of for $i = {1,2,\ldots,q}$. Assume that the inputs $u_{\lbrack 0,{T_{i} - 1}\rbrack}^{i}$ are collectively persistently exciting of order $n + L$. Then the following statements hold:

has full row rank.

Every length $L$ input/output trajectory of can be expressed in terms of $u_{\lbrack 0,{T_{i} - 1}\rbrack}^{i}$ and $y_{\lbrack 0,{T_{i} - 1}\rbrack}^{i}$ ($i = {1,2,\ldots,q}$) as follows: $({\overline{u}}_{\lbrack 0,{L - 1}\rbrack}$, ${\overline{y}}_{\lbrack 0,{L - 1}\rbrack})$ is an input/output trajectory of if and only if

for some real vector $g$.

Note that if $q = 1$ and $T_{1} = T$ we deal with a single experiment, and in this case Theorem 2 recovers Theorem 1.

### Proof

We first prove that (9 ‣ Theorem 2 ‣ III Extension of Willems et al.’s lemma to multiple trajectories ‣ Willems’ Fundamental Lemma for State-space Systems and its Extension to Multiple Datasets")) has full row rank. Let $\begin{bmatrix}
\end{bmatrix}$ be a vector in the left kernel of (9 ‣ Theorem 2 ‣ III Extension of Willems et al.’s lemma to multiple trajectories ‣ Willems’ Fundamental Lemma for State-space Systems and its Extension to Multiple Datasets")), where $\xi^{\top} \in {\mathbb{R}}^{n}$ and $\eta^{\top} \in {\mathbb{R}}^{mL}$. By exploiting the laws of the system (1a) we see that the vectors

are contained in the left kernel of the matrix

By the persistency of excitation assumption, the matrix

has full row rank, and hence the left kernel of has dimension at most $n$. Therefore, the $n + 1$ vectors in are linearly dependent. This yields $\eta = 0$ following the same argument as in the proof of Theorem 1. Next, by Cayley-Hamilton theorem, ${\sum_{i = 0}^{n}{\alpha_{i}A^{i}}} = 0$ where $\alpha_{i} \in {\mathbb{R}}$ for $i = {0,1,\ldots,n}$ and $\alpha_{n} = 1$. We define the linear combination $v:={\sum_{i = 0}^{n}{\alpha_{i}w_{i}}}$. Clearly, the vector $v$ is equal to

Hence, the vector

is contained in the left kernel of

which is zero by collective persistency of excitation. Following the same steps as in the proof of Theorem 1 we conclude by backward substitution that ${\xiB} = {\xiAB} = \cdots = {\xiA^{n - 1}B} = 0$. By controllability of $(A,B)$ we have $\xi = 0$, proving statement (i) ‣ Theorem 2 ‣ III Extension of Willems et al.’s lemma to multiple trajectories ‣ Willems’ Fundamental Lemma for State-space Systems and its Extension to Multiple Datasets").

Next, we prove statement (ii) ‣ Theorem 1 ‣ II Willems et al.’s fundamental lemma in the context of state-space systems ‣ Willems’ Fundamental Lemma for State-space Systems and its Extension to Multiple Datasets"). Let ${\overline{u}}_{\lbrack 0,{L - 1}\rbrack}$ and ${\overline{y}}_{\lbrack 0,{L - 1}\rbrack}$ be vectors such that (10 ‣ Theorem 2 ‣ III Extension of Willems et al.’s lemma to multiple trajectories ‣ Willems’ Fundamental Lemma for State-space Systems and its Extension to Multiple Datasets")) is satisfied for some $g$. Then

is a linear combination of length $L$ trajectories of and hence, by linearity, itself an input/output trajectory of. Conversely, let $({\overline{u}}_{\lbrack 0,{L - 1}\rbrack}$, ${\overline{y}}_{\lbrack 0,{L - 1}\rbrack})$ be an input/output trajectory of and denote by ${\overline{x}}_{0}$ a corresponding initial state at time $0$. We have the relation

where $\mathcal{T}_{L}$ and $\mathcal{O}_{L}$ are defined as

Since (9 ‣ Theorem 2 ‣ III Extension of Willems et al.’s lemma to multiple trajectories ‣ Willems’ Fundamental Lemma for State-space Systems and its Extension to Multiple Datasets")) has full row rank, there exists a vector $g$ such that

Substitution of the latter expression into and using the fact that

for all $i = {1,2,\ldots,q}$ yields (10 ‣ Theorem 2 ‣ III Extension of Willems et al.’s lemma to multiple trajectories ‣ Willems’ Fundamental Lemma for State-space Systems and its Extension to Multiple Datasets")), as desired. ∎

## Examples of application

### IV-A Identification with missing data samples

In this section we treat an example in which we want to identify a system model from a measured trajectory with missing data samples. System identification from trajectories with missing data has been studied in the papers. As we will see, it is also possible to apply Theorem 2(ii) ‣ Theorem 2 ‣ III Extension of Willems et al.’s lemma to multiple trajectories ‣ Willems’ Fundamental Lemma for State-space Systems and its Extension to Multiple Datasets") in this context.

Suppose that we have access to the following, partially corrupted, input/output trajectory of length $T = 20$:

The data are generated by a minimal LTI system of (unknown) state-space dimension $n = 2$. Note that some of the samples are *missing*, which we indicate by $\times$. Our goal is to identify an LTI system that is compatible with the observed data.

In this problem, we have access to three input/output system trajectories, namely $(u_{\lbrack 0,4\rbrack},y_{\lbrack 0,4\rbrack})$, $(u_{\lbrack 6,11\rbrack},y_{\lbrack 6,11\rbrack})$ and $(u_{\lbrack 13,18\rbrack},y_{\lbrack 13,18\rbrack})$. It is not difficult to verify that the input sequences $u_{\lbrack 0,4\rbrack}$, $u_{\lbrack 6,11\rbrack}$ and $u_{\lbrack 13,18\rbrack}$ are collectively persistently exciting of order $5$. It can be easily verified that no LTI system of dimension $1$ can explain the data. Thus we consider LTI systems of dimension $2$. Since the inputs are collectively persistently exciting of order $5$, and since the data-generating system has dimension $n = 2$, by Theorem 2(ii) ‣ Theorem 2 ‣ III Extension of Willems et al.’s lemma to multiple trajectories ‣ Willems’ Fundamental Lemma for State-space Systems and its Extension to Multiple Datasets") every length $L = 3$ input/output trajectory of the system can be written as linear combination of the columns of

We exploit this result by computing, as a function of $\mathcal{D}$, the length $7$ system trajectory

where question marks denote to-be-computed values. The idea is as follows: if the "past" inputs ${\overline{u}{({- 2})}},{\overline{u}{({- 1})}}$ and "past" outputs ${\overline{y}{({- 2})}},{\overline{y}{({- 1})}}$ are zero, the state ${\overline{x}{}} \in {\mathbb{R}}^{2}$ corresponding to $({\overline{u}}_{\lbrack{- 2},4\rbrack},{\overline{y}}_{\lbrack{- 2},4\rbrack})$ is unique, and equal to zero. This means that ${\overline{u}}_{\lbrack 0,4\rbrack}$ is an impulse, applied to a system of the form with zero initial state. Consequently, the output ${\overline{y}}_{\lbrack 0,4\rbrack}$ simply consists of the first Markov parameters of, that is, ${\overline{y}}_{\lbrack 0,4\rbrack} = \begin{bmatrix}
\end{bmatrix}$. From these Markov parameters it is straightforward to compute a state-space realization, e.g., using the Ho-Kalman algorithm \[19, Section 3.4.4\].

Therefore, our remaining task is to compute ${\overline{y}}_{\lbrack 0,4\rbrack}$. Inspired by, we will compute this trajectory iteratively by computing multiple length 3 trajectories as linear combinations of the columns of. To begin with, we compute the first unknown in, which is $\overline{y}{}$. To do so, we have to solve the system of linear equations^22^2 Note that the the solution $g$ is not unique in general, but $\overline{y}{}$ *is* unique. The reason is that the initial state ${\overline{x}{}} = 0$ is uniquely specified by the "past" inputs ${\overline{u}{({- 2})}},{\overline{u}{({- 1})}}$ and outputs ${\overline{y}{({- 2})}},{\overline{y}{({- 1})}}$. In turn, the initial state $\overline{x}{}$ and input $\overline{u}{}$ uniquely specify the output $\overline{y}{}$. Also see \[3, Prop. 1\].

in the unknowns $g$ and $\overline{y}{}$. One possible approach \[3, Alg. 1\] is to obtain a solution $\overline{g}$ to the first five linear equations in. Subsequently, $\overline{y}{}$ is obtained by multiplication of the last row of $\mathcal{D}$ with $\overline{g}$. We do this to find ${\overline{y}{}} = 1$. Next, to find $\overline{y}{}$ we complete the length 3 trajectory $({\overline{u}}_{\lbrack{- 1},1\rbrack},{\overline{y}}_{\lbrack{- 1},1\rbrack})$ by solving the system of equations

which results in ${\overline{y}{}} = 0$. Repeating this process, we obtain ${\overline{y}{}} = 1$, ${\overline{y}{}} = 2$ and ${\overline{y}{}} = 3$, meaning that

Finally, it is not difficult to obtain a state-space realization of these Markov parameters as

The approach outlined in this section is generally also applicable in the case that multiple consecutive data samples are missing. Even in the case that the number of consecutive missing samples is *unknown*, we can apply Theorem 2 to the partial trajectories. Note that we require a sufficient number of partial trajectories of length at least 5 to guarantee collective persistency of excitation of order $5$. In the case of missing data with larger frequency, it may still be possible to identify the system by computation of the left kernels of submatrices of the Hankel matrix.

### IV-B Data-driven LQR of an unstable system

Consider the unstable batch reactor system, which we have discretized using a sampling time of $0.5$s to obtain a system of the form (1a) with

The goal of this example is the data-based design of an optimal control input $u^{\ast}$ that minimizes the cost functional

under the zero endpoint constraint ${\lim_{t\rightarrow\infty}{x{(t)}}} = 0$. Here $Q$ and $R$ are state and input weight matrices, respectively. Under standard assumptions on $A$, $B$, $Q$ and $R$ \[22, Thm. 23\], the optimal input exists, is unique, and is generated by the feedback law $u^{\ast} = {Kx}$, where

and where $P^{+}$ is the largest real symmetric solution to the algebraic Riccati equation

In \[9, Thm. 4\] an attractive design procedure is introduced to obtain $K$ directly from input/state data. The idea is to inject an input sequence $u_{\lbrack 0,{T - 1}\rbrack}$ that is persistently exciting of order $n + 1$ such that the matrix^33^3Note that $X_{-}:={\mathcal{H}_{1}{(x_{\lbrack 0,{T - 1}\rbrack})}}$ and $U_{-}:={\mathcal{H}_{1}{(u_{\lbrack 0,{T - 1}\rbrack})}}$.

has full row rank by Theorem 1(i) ‣ Theorem 1 ‣ II Willems et al.’s fundamental lemma in the context of state-space systems ‣ Willems’ Fundamental Lemma for State-space Systems and its Extension to Multiple Datasets"). Subsequently, $K$ is found by solving a semidefinite program involving the data $x_{\lbrack 0,T\rbrack}$ and $u_{\lbrack 0,{T - 1}\rbrack}$ alone; see \[9, Eq. 27\]. Later on, it was shown \[22, Thm. 26\] that full row rank of is actually also *necessary* for obtaining $K$ from input/state data. In addition, another semidefinite program was introduced \[22, Thm. 29\] to obtain $P^{+}$ and $K$ from input/state data. Both semidefinite programs of and are applicable to this example, but we will follow the method of since it involves less decision variables, c.f. \[22, Remark 31\]. We will compare the approach based on a *single* measured trajectory of the system with the one based on *multiple* trajectories. In both the approaches, we take $Q$ and $R$ as the identity matrices of appropriate dimensions.

First, we compute $K$ on the basis of a *single* measured trajectory of (1a). We choose a random initial state and random input sequence of length $T = 20$, generated using the Matlab command rand. This input is persistently exciting of order $5$. Finally, we let $X_{-}$ and $U_{-}$ as in, and define $X_{+}:={\mathcal{H}_{1}{(x_{\lbrack 1,T\rbrack})}}$. By \[22, Thm. 29\], the largest solution $P^{+}$ to the algebraic Riccati equation is the unique solution to the optimization problem

where ${\mathcal{L}{(P)}}:={{X_{-}^{\top}PX_{-}} - {X_{+}^{\top}PX_{+}} - {X_{-}^{\top}QX_{-}} - {U_{-}^{\top}RU_{-}}}$. We use Yalmip with Sedumi 1.3 as LMI solver. Because of the large magnitude of the data samples (reaching ${\|{x{}}\|} = {1.049 \cdot 10^{8}}$), the solver runs into numerical problems and returns a matrix $P_{sing}$ that does not resemble $P^{+}$. In fact, comparing $P_{sing}$ with the "true" matrix $P^{+}$ obtained via the (model-based) Matlab command dare, we see

To overcome this problem, we next consider *multiple* short experiments, demonstrating the effectiveness of this second approach. We collect $q = 5$ data sets of length $T_{i} = 6$ for $i = {1,2,3,4,5}$. The input sequences $u_{\lbrack 0,{T_{i} - 1}\rbrack}^{i}$ of these sets are again chosen randomly, and are verified to be collectively persistently exciting of order $5$. Similar as before, we use the notation $X_{-}^{i}:={\mathcal{H}_{1}{(x_{\lbrack 0,{T_{i} - 1}\rbrack}^{i})}}$, $X_{+}^{i}:={\mathcal{H}_{1}{(x_{\lbrack 1,T_{i}\rbrack}^{i})}}$ and $U_{-}^{i}:={\mathcal{H}_{1}{(u_{\lbrack 0,{T_{i} - 1}\rbrack}^{i})}}$ for all $i$. In addition, we concatenate these data matrices and define

With these data matrices, we solve again. This result in the solution $P_{mult}$ with ${\|{P_{mult} - P^{+}}\|} = {7.849 \cdot 10^{- 10}}$. Next, we continue the design procedure of \[22, Thm. 29\] by computing a right inverse $X_{-}^{\dagger}$ of $X_{-}$ such that ${\mathcal{L}{(P_{mult})}X_{-}^{\dagger}} = 0$. The optimal control gain is then computed as

The error between between $K_{mult}$ and the true optimal gain $K$ obtained via the command dare is small. In fact, we have ${\|{K_{mult} - K}\|} = {7.083 \cdot 10^{- 11}}$. The closed-loop matrix $A + {BK_{mult}}$ is stable and its spectral radius is $0.188$.

The approach that uses multiple trajectories overall requires more samples than the one using a single trajectory. Indeed, as explained in Section III, a necessary condition for collective persistency of excitation of order $k$ is that

This means that ${\sum_{i = 1}^{5}T_{i}} \geq 30$ in our example. In comparison, a necessary condition for persistency of excitation of order $5$ of a single trajectory is $T \geq 14$. Nonetheless, as shown in this example, the use of multiple short trajectories enables the accurate computation of feedback gains even for unstable systems while this may be problematic when using a single long trajectory.

## Conclusions

Willems *et al.*'s fundamental lemma is a beautiful result that asserts that all trajectories of a linear system can be parameterized by a single, persistently exciting one. In this paper we have extended the fundamental lemma to the scenario where multiple trajectories are given instead of a single one. To this end, we have introduced a notion of collective persistency of excitation. Subsequently, we have shown that all trajectories of a linear system can be parameterized by a finite number of them, assuming these are collectively persistently exciting. We have shown that this result enables the identification of linear systems from data sets with missing data samples. We have also shown that the result can be used to construct controllers of unstable systems from multiple measured trajectories, even when this is not possible from a single trajectory.
