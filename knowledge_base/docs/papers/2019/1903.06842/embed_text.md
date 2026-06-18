## Introduction

Learning from data is essential to every area of science. It is the core of statistics and artificial intelligence, and is becoming ever more prevalent also in the engineering domain. Control engineering is one of the domains where learning from data is now considered as a prime issue.

Learning from data is actually not novel in control theory. System identification is one of the major developments of this paradigm, where modeling based on first principles is replaced by data-driven learning algorithms. Prediction error, maximum likelihood as well as subspace methods are all data-driven techniques which can be now regarded as standard for what concerns modeling. The learning-from-data paradigm has been widely pursued also for control design purposes. A main question is how to design control systems directly from process data with no intermediate system identification step. Besides their theoretical value, answers to this question could have a major practical impact especially in those situations where identifying a process model can be difficult and time consuming, for instance when data are affected by noise or in the presence of nonlinear dynamics. Despite many developments in this area, data-driven control is not yet well understood even if we restrict the attention to linear dynamics, which contrasts the achievements obtained in system identification. A major challenge is how to incorporate data-dependent stability and performance requirements in the control design procedure.

Contributions to data-driven control can be traced back to the pioneering work by Ziegler and Nichols, direct adaptive control and neural networks theories. Since then, many techniques have been developed under the heading *data-driven* and *model-free* control. We mention unfalsified control theory, iterative feedback tuning, and virtual reference feedback tuning. This topic is now attracting more and more researchers, with problems ranging from PID-like control to model reference control and output tracking, predictive, robust and optimal control, the latter being one of the most frequently considered problems. The corresponding techniques are also quite varied, ranging from dynamics programming to optimization techniques and algebraic methods. These contributions also differ with respect to how learning is approached. Some methods only use a batch of process data meaning that learning is performed off-line, while other methods are iterative and require multiple on-line experiments. We refer the reader to for more references on data-driven control methods.

*Willems *et al.*'s fundamental lemma and paper contribution*

A central question in data-driven control is how to replace process models with data. For linear systems, there is actually a fundamental result which answers this question, proposed by Willems *et al.*. Roughly, this result stipulates that the whole set of trajectories that a linear system can generate can be represented by a finite set of system trajectories provided that such trajectories come from sufficiently excited dynamics. While this result has been (more or less explicitly) used for data-driven control design, certain implications of the so-called *Willems *et al.*'s fundamental lemma* seems not fully exploited.

In this paper, we first revisit Willems *et al.*'s fundamental lemma, originally cast in the behavioral framework, through classic state-space descriptions (Lemma 2). Next, we show that this result can be used to get a data-dependent representation of the open-loop and closed-loop dynamics under a feedback interconnection. The first result (Theorem 1) indicates that the parametrization that emerges from the fundamental lemma is in fact the solution to a classic least-squares problem, and has clear connections with the so-called Dynamic Mode Decomposition. The second result (Theorem 2) is even more interesting as it provides a data-based representation of the closed-loop system transition matrix, where the controller is itself parametrized through data.

Theorem 2 turns out to have surprisingly straightforward, yet profound, implications for control design. We discuss this fact in Section IV. The main point is that the parametrization provided in Theorem 2 can be naturally related to the classic Lyapunov stability inequalities. This makes it possible to cast the problem of designing state-feedback controllers in terms of a simple Linear Matrix Inequality (LMI) (Theorem 3). In Theorem 4, the same arguments are used to solve a linear quadratic regulation problem through convex optimization. A remarkable feature of these results is that: (i) no parametric model of system is identified; (ii) stability guarantees come with a finite (computable) number of data points. Theorems 3 and 4 should be understood as *examples* of how the parametrization given in Theorem 2 can be used to approach the direct design of control laws from data. In fact, LMIs have proven their effectiveness in a variety of control design problems, and we are confident that the same arguments can be used for approaching other, more complex, design problems such as $H_{\infty}$ control and quadratic stabilization. In Section V, we further exemplify the merits of the proposed approach by considering the problem of designing stabilizing controllers when data are corrupted by noise (Theorem 5), as well as the problem of stabilizing an unstable equilibrium of a nonlinear system (Theorem 6), both situations where identification can be challenging. The main derivations are given for state feedback. The case of output feedback (Theorem 8) is discussed in Section VI. Concluding remarks are given in Section VII.

### I-A Notation

Given a signal $z:{{\mathbb{Z}}\rightarrow{\mathbb{R}}^{\sigma}}$, we denote by $z_{\lbrack k,{k + T}\rbrack}$, where $k \in {\mathbb{Z}}$, $T \in {\mathbb{N}}$, the restriction in vectorized form of $z$ to the interval ${\lbrack k,{k + T}\rbrack} \cap {\mathbb{Z}}$, namely

When the signal is not restricted to an interval then it is simply denoted by its symbol, say $z$. To avoid notational burden, we use $z_{\lbrack k,{k + T}\rbrack}$ also to denote the sequence $\{{z{(k)}},\ldots,{z{({k + T})}}\}$. For the same reason, we simply write $\lbrack k,{k + T}\rbrack$ to denote the discrete interval ${\lbrack k,{k + T}\rbrack} \cap {\mathbb{Z}}$.

We denote the Hankel matrix associated to $z$ as

where $i \in {\mathbb{Z}}$ and ${t,N} \in {\mathbb{N}}$. The first subscript denotes the time at which the first sample of the signal is taken, the second one the number of samples per each column, and the last one the number of signal samples per each row. Sometimes, if $t = 1$, noting that the matrix $Z_{i,t,N}$ has only one block row, we simply write

## Persistence of excitation and Willems *et al.*'s fundamental lemma

In this section, we revisit the main result in and state a few auxiliary results inspired by subspace identification, which will be useful throughout the paper.

For the sake of simplicity, throughout the paper we consider a controllable and observable discrete-time linear system

where ${x \in {\mathbb{R}}^{n}},{u \in {\mathbb{R}}^{m}}$ and $y \in {\mathbb{R}}^{p}$. The system input-output response of a over $\lbrack 0,{t - 1}\rbrack$ can be expressed as

where $x_{0}$ is the system initial state, and where

are the Toeplitz and observability matrices of order $t$.

Let now $u_{d,{\lbrack 0,{T - 1}\rbrack}}$ and $y_{d,{\lbrack 0,{T - 1}\rbrack}}$ be the input-output data of the system collected during an experiment, and let

be the corresponding Hankel matrix. Similarly to, we can write

and $x_{d}{(i)}$ are the state samples. For $u_{d}$, $y_{d}$, and $x_{d}$, we use the subscript $d$ so as to emphasize that these are the sample data collected from the system during some experiment.

### II-A Persistently exciting data and the fundamental lemma

Throughout the paper, having the rank condition

satisfied plays an important role. As we will see, a condition of this type in fact ensures that the data encode all the information for the direct design of control laws. A fundamental property established in is that it is possible to guarantee when the input is sufficient exciting. We first recall the notion of persistency of excitation.

### Definition 1

The signal $z_{\lbrack 0,{T - 1}\rbrack} \in {\mathbb{R}}^{\sigma}$ is persistently exciting of order $L$ if the matrix

has full rank $\sigmaL$. $\blacksquare$

For a signal $z$ to be persistently exciting of order $L$, it must be sufficiently long, namely $T \geq {{{({\sigma + 1})}L} - 1}$. We now state two results which are key for the developments of the paper.

### Lemma 1

\[27, Corollary 2\] Consider system (1a). If the input $u_{d,{\lbrack 0,{T - 1}\rbrack}}$ is persistently exciting of order $n + t$, then condition holds. $\blacksquare$

### Lemma 2

\[27, Theorem 1\] Consider system. Then the following holds:

If $u_{d,{\lbrack 0,{T - 1}\rbrack}}$ is persistently exciting of order $n + t$, then any $t$-long input/output trajectory of system can be expressed as

Any linear combination of the columns of the matrix in, that is

is a $t$-long input/output trajectory of.

Proof. See the Appendix. $\blacksquare$

Lemma 1 shows that if $T$ is taken sufficiently large then turns out to be satisfied, and this makes it possible to represent any input/output trajectory of the system as a linear combination of collected input/output data. This is the key property that enables one to replace a parametric description of the system with data. Lemma 2 has been originally proven in \[27, Theorem 1\] using the behavioral language, and it was later referred to in as the *fundamental lemma* to describe a linear system through a finite collection of its input/output data. Here, for making the paper as self-contained as possible, we gave a proof of this result using state-space descriptions, as they will recur often in the reminder of this paper.

## Data-based system representations

Lemma 2 allows us to get a data-dependent representation of the open-loop and closed-loop dynamics of system (1a). The first result (Theorem 1) is a covert system identification result where, however, the role of Lemma 2 is emphasized, and which draws connections with the so-called Dynamic Mode Decomposition. Theorem 2 shows instead how one can parametrize feedback interconnections just by using data. This result will be key later on for deriving control design methods that avoid the need to identify a parametric model of the system to be controlled.

Consider a persistently exciting input sequence $u_{d,{\lbrack 0,{T - 1}\rbrack}}$ of order $t + n$ with $t = 1$. Notice that the only requirement on $T$ is that $T \geq {{{({m + 1})}n} + m}$, which is necessary for the persistence of excitation condition to hold. By Lemma 1,

From now on, we will directly refer to condition, bearing in mind that this condition requires persistently exciting inputs of order $n + 1$. Before proceeding, we point out that condition can always be directly assessed when the state of the system is accessible. When instead only input/output data are accessible, condition cannot be directly assessed. Nonetheless, thanks to Lemma 1 this condition can always be enforced by applying an exciting input signal of a sufficiently high order -- for a discussion on the types of persistently exciting signals the reader is referred to \[2, Section 10\]. We will further elaborate on this point in Section VI where we also give an alternative explicitly verifiable condition for the case where only input/output data of the system are accessible.

### III-A Data-based open-loop representation

The next result gives a data-based representation of a linear system and emphasizes the key role of Lemma 2.

### Theorem 1

Let condition hold. Then system (1a) has the following equivalent representation

and $\dagger$ denotes the right inverse.

*Proof.* See the Appendix. $\blacksquare$

Theorem 1 is an identification type of result where the role of Lemma 2 is made explicit. In fact, noting that

it follows immediately that

In particular, the right-hand side of the above identity is simply the minimizer of the least-square problem \[2, Exercise 9.5\]

where $\parallel \cdot \parallel_{F}$ is the Frobenius norm. The representation given in Theorem 1 can be thus interpreted as the solution of a least-square problem.

It is also interesting to observe that Theorem 1 shows clear connections between Willems *et al.*'s fundamental lemma and the Dynamic Mode Decomposition, a numerical procedure for recovering state and control matrices of a linear system from its trajectories. In fact, by performing a singular value decomposition

it readily follows that can be rewritten as $X_{1,T}V_{1}\Sigma^{- 1}U_{1}^{\top}$ \[2, Section 2.6\], which is the basic solution described in \[31, Section III-B\] for recovering the matrices $A$ and $B$ of a linear system from its trajectories.

### III-B Data-based closed-loop representation

We now exploit Lemma 2 to derive a parametrization of system (1a) in closed-loop with a state-feedback law $u = {Kx}$. We give here a proof of this result since the arguments we use will often recur in the next sections.

### Theorem 2

Let condition hold. Then system (1a) in closed-loop with a state feedback $u = {Kx}$ has the following equivalent representation

where $G_{K}$ is a $T \times n$ matrix satisfying

Proof. By the Rouché-Capelli theorem, there exists a $T \times n$ matrix $G_{K}$ such that holds. Hence,

In particular, the first identity in gives. $\blacksquare$

### III-C From indirect to direct data-driven control

Obviously, Theorem 1 already provides a way for designing controllers from data, at least when the state of the system to be controlled is fully accessible. However, this approach is basically equivalent to a model-based approach where the system matrices $A$ and $B$ are first reconstructed using a collection of sample trajectories. A crucial observation that emerges from Theorem 2 is that also the controller $K$ can be parametrized through data via. Thus for design purposes one can regard $G_{K}$ as a *decision variable*, and search for the matrix $G_{K}$ that guarantees stability and performance specifications. In fact, as long as $G_{K}$ satisfies the condition ${X_{0,T}G_{K}} = I_{n}$ in we are ensured that $X_{1,T}G_{K}$ provides an equivalent representation of the closed-loop matrix $A + {BK}$ with feedback matrix $K = {U_{0,1,T}G_{K}}$. As shown in the next section, this enable design procedures that avoid the need to identify a parametric model of the system.

We point out that Theorem 2 already gives an identification-free method for *checking* whether a candidate controller $K$ is stabilizing or not. In fact, given $K$, any solution $G_{K}$ to is such that ${X_{1,T}G_{K}} = {A + {BK}}$. One can therefore compute the eigenvalues of $X_{1,T}G_{K}$ to check whether $K$ is stabilizing or not. This method does not require to place $K$ into feedback, in the spirit of unfalsified control theory.

## Data-driven control design: stabilization and optimal control

In this section, we discuss how Theorem 2 can be used to get identification-free design algorithms. Although the problems considered hereafter are all of practical relevance, we would like to regard them as application *examples* of Theorem 2. In fact, we are confident that Theorem 2 can be used to approach other, more complex, design problems such as $H_{\infty}$ control and quadratic stabilization.

### IV-A State feedback design and data-based parametrization of all stabilizing controllers

By Theorem 2, the closed-loop system under state-feedback $u = {Kx}$ is such that

where $G_{K}$ satisfies. One can therefore search for a matrix $G_{K}$ such that $X_{1,T}G_{K}$ satisfies the classic Lyapunov stability condition. As the next result shows, it turns out that this problem can be actually cast in terms of a simple Linear Matrix Inequality (LMI).

### Theorem 3

Let condition hold. Then, any matrix $Q$ satisfying

stabilizes system (1a). Conversely, if $K$ is a stabilizing state-feedback gain for system (1a) then it can be written as in, with $Q$ solution of.

Proof. By Theorem 2, is an equivalent representation of the closed-loop system. Hence, for any given $K$ the closed-loop system with $u = {Kx}$ is asymptotically stable if and only if there exists $P \succ 0$ such that

Let $Q:={G_{K}P}$. Stability is thus equivalent to the existence of two matrices $Q$ and $P \succ 0$ such that

where the two equality constraints are obtained from. By exploiting the constraint ${X_{0,T}Q} = P$, stability is equivalent to the existence of a matrix $Q$ such that

From the viewpoint of design, one can thus focus on the two inequality constraints which correspond to, while the equality constraint is satisfied a posteriori with the choice $K = {U_{0,1,T}Q{({X_{0,T}Q})}^{- 1}}$. $\blacksquare$

Note that in the formulation the parametrization of the closed-loop matrix $A + {BK}$ is given by $X_{1,T}Q{({X_{0,T}Q})}^{- 1}$, that is with $G_{K} = {Q{({X_{0,T}Q})}^{- 1}}$ which satisfies ${X_{0,T}G_{K}} = I$ corresponding to the second identity in. On the other hand, the constraint corresponding to the first identity in is guaranteed by the choice $K = {U_{0,1,T}Q{({X_{0,T}Q})}^{- 1}}$. This is the reason why is representative of closed-loop stability even if no constraint like appears in the formulation. We point out that Theorem 3 characterizes the whole set of stabilizing state-feedback gains in the sense that any stabilizing feedback gain $K$ can be expressed as in for some matrix $Q$ satisfying.

*Illustrative example*. As an illustrative example, consider the discretized version of a batch reactor system using a sampling time of $0.1s$,

The system to be controlled is open-loop unstable. The control design procedure is implemented in MATLAB. We generate the data with random initial conditions and by applying to each input channel a random input sequence of length $T = 15$ by using the MATLAB command rand. To solve we used CVX, obtaining

which stabilizes the closed-loop dynamics in agreement with Theorem 2. $\blacksquare$

### Remark 1

*(Numerical implementation)* There are other ways to implement. One of these alternatives is obtained from, considering the first inequality, the third equality and condition $P \succ 0$, and rewriting them as

In this case the resulting stabilizing state feedback-gain takes the expression $K = {U_{0,1,T}QP^{- 1}}$. In the previous numerical example but also in those that follow we observed that a formulation like the one above is more stable numerically. The reason is that CVX cannot directly interpret as a symmetric matrix (the upper-left block is given by $X_{0,T}Q$ with non-symmetric decision variable $Q$), and returns a warning regarding the expected outcome. $\blacksquare$

### Remark 2

*(Design for continuous-time systems)* Similar arguments can be used to deal with continuous-time systems. Given a sampling time $\Delta > 0$, let

be input and state sampled trajectories. Under condition (note that, if the sequence ${u_{d}{}},{u_{d}{(\Delta)}},\ldots$ is persistently exciting of order $n + 1$, then the application of the zero-order hold signal obtained from the input samples above ensures condition for the sampled-data system for generic choices of $\Delta$) we have ${A + {BK}} = {X_{1,T}G_{K}}$ where

Hence, for any given $K$, the closed-loop system with $u = {Kx}$ is asymptotically stable if and only if there exists $P \succ 0$ such that

where $G_{K}$ satisfies. In full analogy with the discrete-time case, it follows that any matrix $Q$ satisfying

is such that $K = {U_{0,1,T}Q{({X_{0,T}Q})}^{- 1}}$ is a stabilizing feedback gain. The main difference with respect to the case of discrete-time systems is the presence of the matrix $X_{1,T}$ that contains the derivatives of the state at the sampling times, which are usually not available as measurements. The use of these methods in the context of continuous-time systems might require the use of filters for the approximation of derivatives. This is left for future research. We stress that even though the matrix is built starting from input and state samples, the feedback gain $K = {U_{0,1,T}Q{({X_{0,T}Q})}^{- 1}}$, where $Q$ is the solution of, stabilizes the continuous-time system, not its sampled-data model. $\blacksquare$

### IV-B Linear quadratic regulation

Matrix (in)equalities similar to the one in are recurrent in control design, with the major difference that in only information collected from data appears, rather than the system matrices. Yet, these matrix inequalities can inspire the data-driven solution of other control problems. Important examples are optimal control problems.

Consider the system

where $\xi$ is an external input to the system, and where $z$ is a performance signal of interest; $Q_{x} \succeq 0$, $R \succ 0$ are weighting matrices with $(Q_{x},A)$ observable. The objective is to design a state-feedback law $u = {Kx}$ which renders $A + {BK}$ stable and minimizes the $H_{2}$ norm of the transfer function $h:{\xi\rightarrow z}$ \[39, Section 4\],

This corresponds in the time domain to the $2$-norm of the output $z$ when impulses are applied to the input channels, and it can also be interpreted as the mean-square deviation of $z$ when $\xi$ is a white process with unit covariance. It is kwown \[39, Section 6.4\] that the solution to this problem is given by the controller

where $X$ is the unique positive definite solution to the discrete-time algebraic Riccati (DARE) equation

This problem of finding $K$ can be equivalently formulated as a convex program. To see this, notice that the closed-loop system is given by

with corresponding $H_{2}$ norm

where $W_{c}$ denotes the controllability Gramian of the closed-loop system, which satisfies

where $W_{c} \succeq I$. The second term appearing in the trace function is equivalent to ${trace}{({R^{1/2}KW_{c}K^{\top}R^{1/2}})}$. As a natural counterpart of the continuous-time formulation in, the optimal controller $K$ can be found by solving the optimization problem

This can be cast as a convex optimization problem by means of suitable change of variables. Based on this formulation, it is straightforward to derive a data-dependent formulation of this optimization problem.

### Theorem 4

Let condition hold. Then, the optimal $H_{2}$ state-feedback controller $K$ for system can be computed as $K = {U_{0,1,T}Q{({X_{0,T}Q})}^{- 1}}$ where $Q$ optimizes

Proof. In view of and the parametrization, the optimal solution to can be computed as $K = {U_{0,1,T}G_{K}}$, where $G_{K}$ optimizes

To see this, let $(K_{\ast},W_{\ast},X_{\ast})$ be the optimal solution to with cost $J_{\ast}$. We show that the optimal solution $({\overline{G}}_{K},\overline{W},\overline{X})$ to is such that ${(K,W,X)} = {({U_{0,1,T}{\overline{G}}_{K}},\overline{W},\overline{X})}$ is feasible for and has cost $J_{\ast}$, which implies $K_{\ast} = {U_{0,1,T}{\overline{G}}_{K}}$ as the optimal controller is unique. Feasibility simply follows from the fact that $K = {U_{0,1,T}{\overline{G}}_{K}}$ along with ${X_{0,T}{\overline{G}}_{K}} = I_{n}$ implies that ${X_{1,T}{\overline{G}}_{K}} = {A + {BK}}$. In turn, this implies that ${(K,W,X)} = {({U_{0,1,T}{\overline{G}}_{K}},\overline{W},\overline{X})}$ satisfies all the constraints in. As a final step, let $\overline{J}$ be the cost associated with the solution ${(K,W,X)} = {({U_{0,1,T}{\overline{G}}_{K}},\overline{W},\overline{X})}$. Since the latter is a feasible solution to, we must have $\overline{J} \geq J_{\ast}$. Notice now that $\overline{J}$ is also the optimal cost of associated with the solution $({\overline{G}}_{K},\overline{W},\overline{X})$. Accordingly, let $G_{K_{\ast}}$ be a solution to computed with respect to $K = K_{\ast}$. Thus ${(G_{K},W,X)} = {(G_{K_{\ast}},W_{\ast},X_{\ast})}$ is a feasible solution to with cost $J_{\ast}$. This implies that $\overline{J} \leq J_{\ast}$ and thus $\overline{J} = J_{\ast}$. This shows that $K_{\ast} = {U_{0,1,T}{\overline{G}}_{K}}$.

The formulation follows directly from by defining $Q = {G_{K}W}$ and exploiting the relation ${X_{0,T}Q} = W$. $\blacksquare$

*Illustrative example*. We consider the batch reactor system of the previous subsection. As before, we generate the data with random initial conditions and by applying to each input channel a random input sequence of length $T = 15$ by using the MATLAB command rand. We let $Q_{x} = I_{n}$ and $R = I_{m}$. To solve we used CVX, obtaining

This controller coincides with the controller $\overline{K}$ obtained with the MATLAB command dare which solves the classic DARE equation. In particular, ${\|{K - \overline{K}}\|} \approx 10^{- 7}$. $\blacksquare$

### Remark 3

*(Numerical issues for unstable systems)* The above results are implicitly based on open-loop data. When dealing with unstable systems numerical instability problems may arise. Nonetheless, by Lemma 1 a persistently exciting input of order $n + 1$ suffices to ensure. In turn (see the discussion in Section III), this ensures that we "only" need $T = {{{({m + 1})}n} + m}$ samples in order to compute the controller. This guarantees that one can compute *a priori* for how long a system should run in open loop. In practice, this result also guarantees practical applicability for systems of moderate size that are not strongly unstable.

When dealing with large scale and highly unstable systems the situation is inevitably more complex, and other solutions might be needed. For instance, if a stabilising controller $\hat{K}$ (not necessarily performing) is known, then one can think of running *closed-loop* experiments during which a persistently exciting signal is superimposed to the control signal given by $\hat{K}$, making sure that all the previous results continue to follow without any modification. Measures of this type are widely adopted in adaptive control to overcome issues of loss of stabilisability due to the lack of excitation caused by feedback \[42, Section 7.6\]. $\blacksquare$

## Robustness: noise-corrupted data and nonlinear systems

In the previous subsections, we have considered data-driven design formulations based on LMIs. Besides their simplicity, one of the main reasons for resorting to such formulations is that LMIs have proven their effectiveness also in the presence of perturbations and/or uncertainties around the system to be controlled. In this subsection, we exemplify this point by considering stabilization with noisy data, as well as the problem of stabilizing an unstable equilibrium of a nonlinear system, which are both situations where identification can be challenging.

### V-A Stabilization with noisy data

Consider again system (1a), but suppose that one can only measure the signal

where $w$ is an unknown measurement noise. We will assume no particular statistics on the noise. The problem of interest is to design a stabilizing controller for system (1a) assuming that we measure $\zeta$. Let

where $w_{d}{(k)}$, $k = {0,1,\ldots,T}$ are noise samples associated to the experiment, and

The latter are the matrices containing the available information about the state of the system. Recall that in the noise-free case, a stabilizing controller can be found by searching for a solution $Q$ to the LMI. In the noisy case, it seems thus natural to replace with the design condition

This condition already gives a possible solution approach. In fact, since positive definiteness is preserved under sufficiently small perturbations, for every solution $Q$ to there exists a noise level such that $Q$ will remain solution to, and such that the controller $K = {U_{0,1,T}Q{({Z_{0,T}Q})}^{- 1}}$ obtained by replacing $X_{0,T}$ with $Z_{0,T}$ will remain stabilizing, where the latter property holds since the eigenvalues of $A + {BK}$ depend with continuity on $K$. This indicates that the considered LMI-based approach has some intrinsic degree of robustness to measurement noise.

We formalize these considerations by focusing the attention on a slightly different formulation, which consists in finding a matrix $Q$ and a scalar $\alpha > 0$ such that

It is easy to verify that in the noise-free case and with persistently exciting inputs also this formulation is always feasible and any solution $Q$ is such that $K = {U_{0,1,T}Q{({Z_{0,T}Q})}^{- 1}}$ gives a stabilizing controller. We show this fact in the next Remark 4. We consider the formulation (V-A) because it makes it possible to explicitly *quantify* noise levels for which a solution returns a stabilizing controller.

### Remark 4

*(Feasibility of (V-A) under noise-free data)* In the noise-free case, that is when $Z_{0,T} = X_{0,T}$ and $Z_{1,T} = X_{1,T}$, the formulations and coincide. Suppose then that is feasible and let $\overline{Q}$ be a solution. Since positive definiteness is preserved under small perturbations, ${(Q,\alpha)} = {(\overline{Q},\overline{\beta})}$ will be a solution to the first of (V-A) for a sufficiently small $\overline{\beta} > 0$. Hence ${(Q,\alpha)} = {({\delta\overline{Q}},{\delta\overline{\beta}})}$ will remain feasible for the first of (V-A) for all $\delta > 0$. We can thus pick $\delta$ small enough so that ${(Q,\alpha)}:={({\delta\overline{Q}},{\delta\overline{\beta}})}$ satisfies also the second of (V-A).

Conversely, consider any solution $(Q,\alpha)$ to (V-A) and let $K = {U_{0,1,T}Q{({Z_{0,T}Q})}^{- 1}}$. Since $\alpha > 0$, the first inequality in (V-A) implies that also holds, which, in view of the identities $Z_{0,T} = X_{0,T}$ and $Z_{1,T} = X_{1,T}$, is equivalent to have condition satisfied. Hence, the gain $K$ is stabilizing. $\blacksquare$

Consider the following assumptions.

### Assumption 1

have full row rank. $\blacksquare$

### Assumption 2

for some $\gamma > 0$, where $R_{0,T}:={{AW_{0,T}} - W_{1,T}}$. $\blacksquare$

Assumptions 1 and 2 both express the natural requirement that the loss of information caused by noise is not significant. In particular, Assumption 1 is the counterpart of condition for noise-free data, and is always satisfied when the input is persistently exciting and the noise is sufficiently small. This is because: (i) condition implies that $X_{0,T}$ has rank $n$; (ii) $X_{1,T} = {{AX_{0,T}} + {BU_{0,1,T}}}$ so that condition implies that ${{rank}X_{1,T}} = {{rank}\left\lbrack {BA} \right\rbrack} = n$ otherwise the system would not be controllable; and (iii) the rank of a matrix does not change under sufficiently small perturbations.

Intuitively, Assumption 1 alone is not sufficient to guarantee the existence of a solution returning a stabilizing controller since this assumption may also be verified by arbitrary noise, in which case the data need not contain any useful information. Assumption 2 takes into account this aspect, and plays the role of a "*signal-to-noise ratio*" (SNR) condition. Notice that when Assumption 1 holds then Assumption 2 is always satisfied for large enough $\gamma$. As next theorem shows, however, to get stability one needs to restrict the magnitude of $\gamma$, meaning that the SNR must be sufficiently large.

### Theorem 5

Suppose that Assumptions 1 and 2 hold. Then, any solution $(Q,\alpha)$ to (V-A) such that $\gamma < {\alpha^{2}/{({4 + {2\alpha}})}}$ returns a stabilizing controller $K = {U_{0,1,T}Q{({Z_{0,T}Q})}^{- 1}}$.

Proof. As a first step, we parametrize the closed-loop system as a function of $G_{K}$ and the noise,

which exists in view of Assumption 1.

By this parametrization, $A + {BK}$ is stable if and only if there exists $P \succ 0$ such that

where $G_{K}$ satisfies. Following the same analysis as in Section IV-A, introducing the change of variable $Q = {G_{K}P}$ and exploiting the relation ${Z_{0,T}Q} = P$, stability is equivalent to the existence of a matrix $Q$ such that

From the viewpoint of design, one can focus on the inequality constraints, since the equality constraint can be satisfied a posteriori with $K = {U_{0,1,T}Q{({Z_{0,T}Q})}^{- 1}}$.

We can now finalize the proof. First recall that for arbitrary matrices $X,Y,F$ with $F \succ 0$, and a scalar $\varepsilon > 0$, it holds that ${{XFY^{\top}} + {YFX^{\top}}} \preceq {{\varepsilonXFX^{\top}} + {\varepsilon^{- 1}YFY^{\top}}}$. By applying this property to the second inequality in with $F = {Z_{0,T}Q}$, $X = {Z_{1,T}Q{({Z_{0,T}Q})}^{- 1}}$, $Y = {R_{0,T}Q{({Z_{0,T}Q})}^{- 1}}$, a sufficient condition for stability is that

where $\varepsilon > 0$. By the Schur complement any solution $(Q,\alpha)$ gives ${{{Z_{1,T}Q{({Z_{0,T}Q})}^{- 1}Q^{\top}Z_{1,T}^{\top}} + {\alphaZ_{1,T}Z_{1,T}^{\top}}} - {Z_{0,T}Q}} \prec 0$ and ${Q{({Z_{0,T}Q})}^{- 1}Q^{\top}} \prec I_{T}$. Accordingly, any solution $(Q,\alpha)$ ensures that

This implies that any solution $(Q,\alpha)$ to (V-A) ensures stability if the right hand side of is negative definite. Pick $\varepsilon = {\alpha/2}$. The right hand side of is negative definite if

which is satisfied when $\gamma < {\alpha^{2}/{({4 + {2\alpha}})}}$. $\blacksquare$

*Illustrative example*. We consider the batch reactor system of the previous section. We generate the data with unit random initial conditions and by applying to each input channel a unit random input sequence of length $T = 15$. The noise is taken as a random sequence within $\lbrack{- 0.01},0.01\rbrack$. To solve (V-A) we used CVX, obtaining

with $\alpha \approx 10^{- 4}$. Condition $\gamma < {\alpha^{2}/{({4 + {2\alpha}})}}$ is not satisfied as the smallest value of $\gamma$ satisfying Assumption 2 is $\approx 10^{- 2}$. Nonetheless, $K$ stabilizes the closed-loop system. As pointed out, this simply reflects that the condition $\gamma < {\alpha^{2}/{({4 + {2\alpha}})}}$ can be theoretically conservative. In fact, numerical simulations indicate that condition $\gamma < {\alpha^{2}/{({4 + {2\alpha}})}}$ is satisfied for noise of order $10^{- 4}$, while in practice the algorithm systematically returns stabilizing controllers for noise of order $10^{- 2}$, and for noise of order $10^{- 1}$ (noise which can also alter the first digit of the noise-free trajectory) it returns stabilizing controllers in more than half of the cases. $\blacksquare$

In contrast with Assumption 1 which can be assessed from data only, checking whether Assumption 2 holds with a value $\gamma < {\alpha^{2}/{({4 + {2\alpha}})}}$ requires prior knowledge of an upper bound on $R_{0,T}$. In turn, this requires prior knowledge of an upper bound on the noise and on the largest singular value of $A$. If this information is available then Assumption 2 can be assessed from data. ^11^1 For instance, recalling that $W_{0,T}$ and $W_{1,T}$ are $n \times T$ matrices, it follows from the Gershgorin theorem that ${{W_{0,T}W_{0,T}^{\top}} \preceq {n\overline{w}TI_{n}}},{{W_{1,T}W_{1,T}^{\top}} \preceq {n\overline{w}TI_{n}}}$ where $\overline{w}$ denotes an upper bound on the noise, that is ${|{w_{i}{(k)}w_{j}{(k)}}|} \leq \overline{w}$ for all ${1 \leq i},{j \leq n}$ and for all $k = {0,1,\ldots,T}$. This implies that $R_{0,T}$ satisfies ${R_{0,T}R_{0,T}^{\top}} \preceq {2n\overline{w}TI_{n}{({1 + \sigma_{A}})}}$, where $\sigma_{A}$ denotes the the square of the largest singular value of the matrix $A$. One can replace Assumption 2 with a (more conservative) condition which can be assessed under the only assumption that an upper bound on the noise is available. Before stating this result, we nonetheless point out that there is a reason why $A$ appears in Assumption 2. In fact, the information loss caused by noise does not depend only on the magnitude of the noise but also on its "direction". For instance, in case the noise $w$ follows the equation ${w{({k + 1})}} = {Aw{(k)}}$ then $R_{0,T}$ becomes zero, meaning that Assumption 2 holds with an arbitrary $\gamma$ irrespective of the magnitude of $w$. In fact, in this case $w$ behaves as a genuine system trajectory (it evolves in the set of states that the system can generate), so it brings useful information on the system dynamics. This indicates that noise of large magnitude but "close" to the set of states where the system evolves can be less detrimental of noise with smaller magnitude but which completely alters the direction of the noise-free trajectory.

As anticipated, one can replace Assumption 2 with a (more conservative) condition verifiable under the only assumption that an upper bound on the noise is known.

### Assumption 3

for some $\gamma_{1} \in {(0,0.5)}$ and $\gamma_{2} > 0$. $\blacksquare$

### Corollary 1

Suppose that Assumptions 1 and 3 hold. Then, any solution $(Q,\alpha)$ to (V-A) such that

returns a stabilizing controller $K = {U_{0,1,T}Q{({Z_{0,T}Q})}^{- 1}}$.

*Proof.* See the Appendix. $\blacksquare$

In both Theorem 5 and Corollary 1, stability relies on the fulfilment of a condition like $\gamma < {\alpha^{2}/{({4 + {2\alpha}})}}$. This suggests that it might be convenient to reformulate the design problem by searching for the solution $(Q,\alpha)$ to (V-A) maximizing $\alpha$, which still results in a convex problem. Nonetheless, it is worth noting that both Theorem 5 and Corollary 1 only give *sufficient* conditions, meaning (as shown also in the previous numerical example) that one can find stabilizing controllers even when $\gamma \geq {\alpha^{2}/{({4 + {2\alpha}})}}$.

### V-B Stabilization of nonlinear systems

The previous result shows that a controller can be designed in the presence of noise provided that signal-to-noise ratio is sufficiently small. This hints at the possibility of designing also a stabilizing control for nonlinear systems based on data alone. As a matter of fact, around an equilibrium a nonlinear system can be expressed via its first order approximation plus a reminder. If we run our experiment in such a way that the input and the state remain sufficiently close to the equilibrium, then the reminder can be viewed as a process disturbance of small magnitude and there is a legitimate hope that the robust stabilization result also applies to this case. In the rest of this section we formalize this intuition.

Consider a smooth nonlinear system

and let $(\overline{x},\overline{u})$ be a *known* equilibrium pair, that is such that $\overline{x} = {f{(\overline{x},\overline{u})}}$. Let us rewrite the nonlinear system as

where ${\deltax}:={x - \overline{x}}$, ${\deltau}:={u - \overline{u}}$, and where

The quantity $d$ accounts for higher-order terms and it has the property that is goes to zero faster than $\deltax$ and $\deltau$, namely we have

with $R{({\deltax},{\deltau})}$ an $n \times {({n + m})}$ matrix of smooth functions with the property that

It is known that if the pair $(A,B)$ defining the linearized system is stabilizable then the controller $K$ rendering $A + {BK}$ stable also exponentially stabilizes the equilibrium $(\overline{x},\overline{u})$ for the original nonlinear system. The objective here is to provide sufficient conditions for the design of $K$ from data. To this end, we consider the following result which is an adaptation of Theorem 5. Let

be the data resulting from an experiment carried out on the nonlinear system. Note that the matrices $X_{0,T}$, $X_{1,T}$ and $U_{0,1,T}$ are known. Consider the following assumptions.

### Assumption 4

have full row rank. $\blacksquare$

### Assumption 5

for some $\gamma > 0$. $\blacksquare$

The following result holds.

### Theorem 6

Consider a nonlinear system as in, along with an equilibrium pair $(\overline{x},\overline{u})$. Suppose that Assumptions 4 and 5 hold. Then, any solution $(Q,\alpha)$ to

such that $\gamma < {\alpha^{2}/{({4 + {2\alpha}})}}$ returns a stabilizing state-feedback gain $K = {U_{0,1,T}Q{({X_{0,T}Q})}^{- 1}}$, which locally stabilizes the equilibrium pair $(\overline{x},\overline{u})$.

*Proof.* We only sketch the proof since essentially analogous to the proof of Theorem 5. Note that

which exists in view of Assumption 4. The rest of the proof follows exactly the same steps as the proof of Theorem 5 by replacing $Z_{0,T}$, $Z_{1,T}$ and $R_{0,T}$ by $X_{0,T}$, $X_{1,T}$ and $- D_{0,T}$, respectively. $\blacksquare$

Before illustrating the result with a numerical example, we make some observations.

Assumptions 4 and 5 parallel the assumptions considered for the case of noisy data. In particular, Assumptions 5 is the counterpart of Assumption 2 (or Assumption 3) and it amounts to requiring that the experiment is carried out sufficiently close to the system equilibrium so that the effect of the nonlinearities (namely the disturbance $d$) becomes small enough compared with $\deltax$ (*cf.* ).

At this moment, we do not have a method for designing the experiments in such a way that Assumptions 4 and 5 hold. This means that verifying Assumption 5 requires at this stage prior knowledge of an upper bound on $d$, that is on the type of nonlinearity (Assumption 4 can be anyway assessed from data only). Albeit in some cases this information can be inferred from physical considerations, in general this is an important aspect which deserves to be studied. Numerical simulations (including the example which follows) nonetheless indicate that at least in certain cases the "margin" is appreciable in the sense that one obtains stabilizing controllers even when the experiment leads the system sensibly far from its equilibrium.

*Illustrative example.* Consider the Euler discretization of an inverted pendulum

where we simplified the sampled times $k\Delta$ in $k$, with $\Delta$ the sampling time. The states $x_{1},x_{2}$ are the angular position and velocity, respectively, $u$ is the applied torque. The system has an unstable equilibrium in ${(\overline{x},\overline{u})} = {}$ corresponding to the pendulum upright position and therefore ${\deltax} = x$ and ${\deltau} = u$. It is straightforward to verify that

Suppose that the parameters are $\Delta = 0.1$, $m = \ell = 1$, $g = 9.8$ and $\mu = 0.01$. The control design procedure is implemented in MATLAB. We generate the data with random initial conditions within $\lbrack{- 0.1},0.1\rbrack$, and by applying a random input sequence of length $T = 5$ within $\lbrack{- 0.1},0.1\rbrack$. To solve we used CVX, obtaining

which stabilizes the unstable equilibrium in agreement with Theorem 6 as the linearized system has matrices

In this example, $\alpha = 0.0422$ and condition $\gamma < {\alpha^{2}/{({4 + {2\alpha}})}}$ holds because $X_{1,T}$ is of order $0.01$ and $D_{0,T}$ is of order $10^{- 5}$ so that the smallest value of $\gamma$ for which Assumption 5 holds is $\approx 10^{- 6}$ while ${\alpha^{2}/{({4 + {2\alpha}})}} \approx 10^{- 4}$. We finally notice that the algorithm systematically returns stabilizing controllers also for initial conditions and inputs within the interval $\lbrack{- 0.5},0.5\rbrack$ which corresponds to an initial displacement of about $28$ degrees from the equilibrium, albeit in this case condition $\gamma < {\alpha^{2}/{({4 + {2\alpha}})}}$ not always holds. $\blacksquare$

## Input-output data: the case of SISO systems

In Section IV-A, the measured data are the inputs and the state, and the starting point is to express the trajectories of the system and the control gain in terms of the Hankel matrix of input-state data. Here we show how similar arguments can be used when only input/output data are accessible. The main derivations are given for single-input single-output (SISO) systems. A remark on multi-input multi-output (MIMO) systems is provided in Section VI-C.

Consider a SISO systems as in in left difference operator representation \[43, Section 2.3.3\],

This representation corresponds to for $D = 0$. In this case, one can reduce the output measurement case to the state measurement case with minor effort. Let

from we obtain the state space system on the next page. Note that we turned our attention to a system of order $2n$, which is not minimal.

{{\chi{({k + 1})}} =} &amp; {{\underset{\mathcal{A}}{\underbrace{\begin{bmatrix}
0 &amp; 1 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 \\
0 &amp; 0 &amp; 1 &amp; \cdots &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 \\
\vdots &amp; \vdots &amp; \vdots &amp; \ddots &amp; \vdots &amp; \vdots &amp; \vdots &amp; \vdots &amp; \ddots &amp; \vdots \\
0 &amp; 0 &amp; 0 &amp; \cdots &amp; 1 &amp; 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 \\
{-a_{1}} &amp; {-a_{2}} &amp; {-a_{3}} &amp; \cdots &amp; {-a_{n}} &amp; b_{1} &amp; b_{2} &amp; b_{3} &amp; \cdots &amp; b_{n} \\
&amp; &amp; &amp; &amp; &amp; &amp; &amp; &amp; &amp; \\
0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 &amp; 1 &amp; 0 &amp; \cdots &amp; 0 \\
0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 &amp; 0 &amp; 1 &amp; \cdots &amp; 0 \\
\vdots &amp; \vdots &amp; \vdots &amp; \ddots &amp; \vdots &amp; \vdots &amp; \vdots &amp; \vdots &amp; \ddots &amp; \vdots \\
0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 1 \\
0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0
\end{bmatrix}}}\chi{(k)}} + {\underset{\mathcal{B}}{\underbrace{\begin{bmatrix}
{{y{(k)}} =} &amp; {\underset{\mathcal{C}}{\underbrace{\begin{bmatrix}
{-a_{1}} &amp; {-a_{2}} &amp; {-a_{3}} &amp; \cdots &amp; {-a_{n}} &amp; b_{1} &amp; b_{2} &amp; b_{3} &amp; \cdots &amp; b_{n}
\end{bmatrix}}}\chi{(k)}}

Consider now the matrix in written for the system ${\chi{({k + 1})}} = {{\mathcal{A}\chi{(k)}} + {\mathcal{B}u{(k)}}}$ in, with $T$ satisfying $T \geq {{2n} + 1}$. If this matrix is full-row rank, then the analysis in the previous sections can be repeated also for system. For system the matrix in question takes the form

where ${\chi_{d}{({i + 1})}} = {{\mathcal{A}\chi_{d}{(i)}} + {\mathcal{B}u_{d}{(i)}}}$ for $i \geq 0$ and where $\chi_{d}{}$ is the initial condition in the experiment,

The following result holds.

### Lemma 3

holds. Moreover, if $u_{d,{\lbrack 0,{T - 1}\rbrack}}$ is persistently exciting of order ${2n} + 1$ then

Proof. The identity follows immediately from the definition of the state $\chi$ in and the definition ${\hat{X}}_{0,T}$ in. As for the second statement, by the Key Reachability Lemma \[43, Lemma 3.4.7\], it is known that the $2n$-dimensional state space model is controllable if and only if the polynomials $z^{n} + {a_{n}z^{n - 1}\ldots} + {a_{2}z} + a_{1}$, ${b_{n}z^{n - 1}} + \ldots + {b_{2}z} + b_{1}$ are coprime. Under this condition and persistency of excitation, Lemma 1 applied to immediately proves. $\blacksquare$

### VI-A Data-based open-loop representation

Similar to the case in which inputs and states are measured, the full rank property plays a crucial role in expressing the system via data. As a matter of fact, for any pair $(u,\chi)$ we have

for some $g$. Hence,

As in the proof of Theorem 1 for the full state measurement case, we can thus solve for $g$ in, replace it in, and obtain the following result.

### Theorem 7

Let condition hold. Then system has the following equivalent representation:

with $e_{n}$ the $n$-th versor of ${\mathbb{R}}^{2n}$.

Proof. The proof follows the same steps as the proof of Theorem 1 and is omitted. $\blacksquare$

A representation of order $n$ of the system can also be extracted from. The model, which only depends on measured input-output data, can be used for various analysis and design purposes. In the next subsection, we focus on the problem of designing an output feedback controller without going through the step of identifying a parametric model of the system.

### VI-B Design of output feedback controllers

Consider the left difference operator representation, its realization and the input/state pair $(u,\chi)$. We introduce a controller of the form

whose state space representation is given by,

{{\chi^{c}{({k + 1})}} =} &amp; {{\underset{\mathcal{F}}{\underbrace{\begin{bmatrix}
0 &amp; 1 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 \\
0 &amp; 0 &amp; 1 &amp; \cdots &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; \ldots &amp; 0 \\
\vdots &amp; \vdots &amp; \vdots &amp; \ddots &amp; \vdots &amp; \vdots &amp; \vdots &amp; \vdots &amp; \ddots &amp; \vdots \\
0 &amp; 0 &amp; 0 &amp; \cdots &amp; 1 &amp; 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 \\
{-c_{1}} &amp; {-c_{2}} &amp; {-c_{3}} &amp; \cdots &amp; {-c_{n}} &amp; d_{1} &amp; d_{2} &amp; d_{3} &amp; \cdots &amp; d_{n} \\
&amp; &amp; &amp; &amp; &amp; &amp; &amp; &amp; &amp; \\
0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 &amp; 1 &amp; 0 &amp; \cdots &amp; 0 \\
0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 &amp; 0 &amp; 1 &amp; \cdots &amp; 0 \\
\vdots &amp; \vdots &amp; \vdots &amp; \ddots &amp; \vdots &amp; \vdots &amp; \vdots &amp; \vdots &amp; \ddots &amp; \vdots \\
0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 1 \\
0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0
\end{bmatrix}}}\chi^{c}{(k)}} + {\underset{\mathcal{G}}{\underbrace{\begin{bmatrix}
{{y^{c}{(k)}} =} &amp; {{\underset{\mathcal{H}}{\underbrace{\begin{bmatrix}
{-c_{1}} &amp; {-c_{2}} &amp; {-c_{3}} &amp; \cdots &amp; {-c_{n}} &amp; d_{1} &amp; d_{2} &amp; d_{3} &amp; \cdots &amp; d_{n}
\end{bmatrix}}}\chi^{c}{(k)}},}

with state $\chi^{c}$ defined similar to. In the closed-loop system, we enforce the following interconnection conditions relating the process and the controller

Note in particular the identity, for $k \geq n$,

Hence, for $k \geq n$, there is no loss of generality in considering as the closed-loop system the system

In the following result we say that controller stabilizes system, meaning that the closed-loop system is asymptotically stable.

### Theorem 8

Let condition hold. Then the following properties hold:

The closed-loop system has the equivalent representation

where $G_{\mathcal{K}}$ is a ${T \times 2}n$ matrix such that

is the vector of coefficients of the controller.

Any matrix $\mathcal{Q}$ satisfying

is such that the controller with coefficients given by

stabilizes system. Conversely, any controller that stabilizes system must have coefficients $\mathcal{K}$ given by (128 ‣ Theorem 8 ‣ VI-B Design of output feedback controllers ‣ VI Input-output data: the case of SISO systems ‣ Formulas for Data-driven Control: Stabilization, Optimality and Robustness")), with $\mathcal{Q}$ a solution of (127 ‣ Theorem 8 ‣ VI-B Design of output feedback controllers ‣ VI Input-output data: the case of SISO systems ‣ Formulas for Data-driven Control: Stabilization, Optimality and Robustness")).

Proof. (i) In view of condition and by Rouché-Capelli theorem, a ${T \times 2}n$ matrix $G_{\mathcal{K}}$ exists such that (125 ‣ Theorem 8 ‣ VI-B Design of output feedback controllers ‣ VI Input-output data: the case of SISO systems ‣ Formulas for Data-driven Control: Stabilization, Optimality and Robustness")) holds. Hence,

from which we obtain (124 ‣ Theorem 8 ‣ VI-B Design of output feedback controllers ‣ VI Input-output data: the case of SISO systems ‣ Formulas for Data-driven Control: Stabilization, Optimality and Robustness")), which are the dynamics parametrized with respect to the matrix $G_{\mathcal{K}}$.

\(ii\) The parametrization (124 ‣ Theorem 8 ‣ VI-B Design of output feedback controllers ‣ VI Input-output data: the case of SISO systems ‣ Formulas for Data-driven Control: Stabilization, Optimality and Robustness")) of the closed-loop system is the output-feedback counterpart of the parametrization obtained for the case of full state measurements. We can then proceed analogously to the proof of Theorem 3 replacing $G_{K},X_{0,T},X_{1,T}$ with $G_{\mathcal{K}},{\hat{X}}_{0,T},{\hat{X}}_{1,T}$ and obtain the claimed result mutatis mutandis. $\blacksquare$

Note that given a solution $\mathcal{K}$ as in (128 ‣ Theorem 8 ‣ VI-B Design of output feedback controllers ‣ VI Input-output data: the case of SISO systems ‣ Formulas for Data-driven Control: Stabilization, Optimality and Robustness")) the resulting entries ordered as in (126 ‣ Theorem 8 ‣ VI-B Design of output feedback controllers ‣ VI Input-output data: the case of SISO systems ‣ Formulas for Data-driven Control: Stabilization, Optimality and Robustness")) lead to the following state-space realization of order $n$ for the controller

As a final point, we notice that Theorem 8 relies on the knowledge of the order $n$ of the system. In many cases, as for instance in the numerical example which follows, this information can result from *first principles* considerations. Otherwise, one can determine the model order from data, *e.g.* using subspace identification methods \[44, Theorem 2\]. In this regard, it is worth pointing out that determining the model order from data does not correspond to the whole algorithmic procedure needed to get a parametric model of the system. Note that this information is also sufficient to render condition verifiable from data, which circumvents the problem of assessing persistence of excitation conditions that depend on the state trajectory of the system.

*Illustrative example*. Consider a system made up by two carts. The two carts are mechanically coupled by a spring with uncertain stiffness $\gamma \in {\lbrack 0.25,1.5\rbrack}$. The aim is to control the position of one cart by applying a force to the other cart. The system state-space description is given by

Assume that $\gamma = 1$ (unknown). The system is controllable and observable. All the open-loop eigenvalues are on the imaginary axis. The input-output discretized version using a sampling time of $1s$ is as in with coefficients

We design a controller following the approach described in Theorem 8. We generate the data with random initial conditions and by applying a random input sequence of length $T = 9$. To solve (127 ‣ Theorem 8 ‣ VI-B Design of output feedback controllers ‣ VI Input-output data: the case of SISO systems ‣ Formulas for Data-driven Control: Stabilization, Optimality and Robustness")) we used CVX, obtaining from (128 ‣ Theorem 8 ‣ VI-B Design of output feedback controllers ‣ VI Input-output data: the case of SISO systems ‣ Formulas for Data-driven Control: Stabilization, Optimality and Robustness"))

which stabilizes the closed-loop dynamics in agreement with Theorem 8. In particular, a minimal state-space representation $(A_{c},B_{c},D_{c},D_{c})$ of this controller is given by (see )

### VI-C A remark on the case of MIMO systems

An analysis similar to the one presented before can be repeated starting from the left-difference operator of a MIMO system,

where $y \in {\mathbb{R}}^{p}$, $u \in {\mathbb{R}}^{m}$, with $A_{i}$ and $B_{i}$ matrices of suitable dimensions. We define the state vector $\chi \in {\mathbb{R}}^{{({m + p})}n}$ as before which yields the state representation.

{{\chi{({k + 1})}} =} &amp; {{\underset{\mathcal{A}}{\underbrace{\begin{bmatrix}
0 &amp; I_{p} &amp; 0 &amp; \cdots &amp; 0 &amp; \mathbb{0}_{p\times m} &amp; \mathbb{0}_{p\times m} &amp; \mathbb{0}_{p\times m} &amp; \cdots &amp; \mathbb{0}_{p\times m} \\
0 &amp; 0 &amp; I_{p} &amp; \cdots &amp; 0 &amp; \mathbb{0}_{p\times m} &amp; \mathbb{0}_{p\times m} &amp; \mathbb{0}_{p\times m} &amp; \cdots &amp; \mathbb{0}_{p\times m} \\
\vdots &amp; \vdots &amp; \vdots &amp; \ddots &amp; \vdots &amp; \vdots &amp; \vdots &amp; \vdots &amp; \ddots &amp; \vdots \\
0 &amp; 0 &amp; 0 &amp; \cdots &amp; I_{p} &amp; \mathbb{0}_{p\times m} &amp; \mathbb{0}_{p\times m} &amp; \mathbb{0}_{p\times m} &amp; \cdots &amp; \mathbb{0}_{p\times m} \\
{-A_{1}} &amp; {-A_{2}} &amp; {-A_{3}} &amp; \cdots &amp; {-A_{n}} &amp; B_{1} &amp; B_{2} &amp; B_{3} &amp; \cdots &amp; B_{n} \\
&amp; &amp; &amp; &amp; &amp; &amp; &amp; &amp; &amp; \\
\mathbb{0}_{m\times p} &amp; \mathbb{0}_{m\times p} &amp; \mathbb{0}_{m\times p} &amp; \cdots &amp; \mathbb{0}_{m\times p} &amp; \mathbb{0}_{m\times m} &amp; I_{m} &amp; \mathbb{0}_{m\times m} &amp; \ldots &amp; \mathbb{0}_{m\times m} \\
\mathbb{0}_{m\times p} &amp; \mathbb{0}_{m\times p} &amp; \mathbb{0}_{m\times p} &amp; \cdots &amp; \mathbb{0}_{m\times p} &amp; \mathbb{0}_{m\times m} &amp; \mathbb{0}_{m\times m} &amp; I_{m} &amp; \cdots &amp; \mathbb{0}_{m\times m} \\
\vdots &amp; \vdots &amp; \vdots &amp; \ddots &amp; \vdots &amp; \vdots &amp; \vdots &amp; \vdots &amp; \ddots &amp; \vdots \\
\mathbb{0}_{m\times p} &amp; \mathbb{0}_{m\times p} &amp; \mathbb{0}_{m\times p} &amp; \ldots &amp; \mathbb{0}_{m\times p} &amp; \mathbb{0}_{m\times m} &amp; \mathbb{0}_{m\times m} &amp; \mathbb{0}_{m\times m} &amp; \ldots &amp; I_{m} \\
\mathbb{0}_{m\times p} &amp; \mathbb{0}_{m\times p} &amp; \mathbb{0}_{m\times p} &amp; \ldots &amp; \mathbb{0}_{m\times p} &amp; \mathbb{0}_{m\times m} &amp; \mathbb{0}_{m\times m} &amp; \mathbb{0}_{m\times m} &amp; \ldots &amp; \mathbb{0}_{m\times m}
\end{bmatrix}}}\chi{(k)}} + {\underset{\mathcal{B}}{\underbrace{\begin{bmatrix}
\mathbb{0}_{p\times m} &amp; \\
\mathbb{0}_{p\times m} &amp; \\
\mathbb{0}_{p\times m} &amp; \\
\mathbb{0}_{p\times m} &amp; \\
\mathbb{0}_{m\times m} &amp; \\
\mathbb{0}_{m\times m} &amp; \\
\mathbb{0}_{m\times m} &amp; \\
{{y{(k)}} =} &amp; {\underset{\mathcal{C}}{\underbrace{\begin{bmatrix}
{-A_{1}} &amp; {-A_{2}} &amp; {-A_{3}} &amp; \cdots &amp; {-A_{n}} &amp; B_{1} &amp; B_{2} &amp; B_{3} &amp; \cdots &amp; B_{n}
\end{bmatrix}}}\chi{(k)}}

In case of MIMO systems, we assume that we collect data with an input $u_{d,{\lbrack 0,{T - 1}\rbrack}}$, $T \geq {{({{{({m + p})}n} + 1})}{({m + 1})}}$, persistently exciting of order ${{({m + p})}n} + 1$. Then, by Lemma 1 we obtain the fulfilment of the following condition

Under this condition, the same analysis of Section VI-B can be repeated to obtain the following:

### Corollary 2

Let condition hold. Then any matrix $\mathcal{Q}$ satisfying (127 ‣ Theorem 8 ‣ VI-B Design of output feedback controllers ‣ VI Input-output data: the case of SISO systems ‣ Formulas for Data-driven Control: Stabilization, Optimality and Robustness")) is such that the controller

with matrix coefficients given by

stabilizes system. Conversely, any controller as in that stabilizes can be expressed in terms of the coefficients $\begin{bmatrix}
\end{bmatrix}$ given by, with $\mathcal{Q}$ a solution to (127 ‣ Theorem 8 ‣ VI-B Design of output feedback controllers ‣ VI Input-output data: the case of SISO systems ‣ Formulas for Data-driven Control: Stabilization, Optimality and Robustness")).

## Discussion and conclusions

Persistently exciting data enable the construction of data-dependent matrices that can replace systems models. Adopting this paradigm proposed by we have shown the existence of a parametrization of feedback control systems that allows us to reduce the stabilization problem to an equivalent data-dependent linear matrix inequality. Since LMIs are ubiquitous in systems and control we expect that our approach could lead to data-driven solutions to many other control problems. As an example we have considered an LQR problem. For several control problems, LMIs have proven their effectiveness in providing robustness to various sources of uncertainty. We have capitalized on this fact extending the analysis to the case of noise-corrupted data and showing how the approach can be used to stabilize unstable equilibria of nonlinear systems, which are both situations where identification can be challenging. A remarkable feature of all these results is that: (i) no parametric model of system is identified; (ii) stability guarantees come with a finite (computable) number of data points.

Studying how our approach can be used to systematically address control problems via data-dependent LMIs could be very rewarding, and lead to a methodical inclusion of data to analyze and design control systems. A great leap forward will come from systematically extending the methods of this paper to systems where identification is challenging, such as switched and nonlinear systems. The results of this paper show that our approach is concretely promising for nonlinear systems, but we have only touched the surface of this research area. Estimating the domain of attraction or considering other approaches such as *lifting* techniques are two simple examples of compelling research directions for nonlinear systems. Recent results have reignited the interest of the community on system identification for nonlinear systems, interestingly pointing out the importance of the concept of persistently exciting signals. We are confident that our approach will also play a fundamental role in developing a systematic methodology for the data-driven design of control laws for nonlinear systems.

### A Proof of Lemma 2

\(i\) By the Rouché-Capelli theorem, the rank condition implies the existence of a vector $g \in {\mathbb{R}}^{T - t}$ such that

By replacing this expression in, we get

where the last identity holds because of. This concludes the proof of (i).

Thus $U_{0,t,{{T - t} + 1}}g$ represents a $t$-long input sequence $u_{\lbrack 0,{t - 1}\rbrack}$ of system, while ${Y_{0,t,{{T - t} + 1}}g} = {{\mathcal{O}_{t}x_{0}} + {\mathcal{T}_{t}u_{\lbrack 0,{t - 1}\rbrack}}}$ is the corresponding output obtained from initial conditions $x_{0}$. $\blacksquare$

### B Proof of Theorem 1

For compactness, let

By the Rouché-Capelli theorem, for any given $v$, the system of equations

admits infinite solutions $g$, given by

where $\Pi_{S}^{\perp}:=\left( {I - {S^{\dagger}S}} \right)$ is the orthogonal projector onto the kernel of $S$. Hence,

for some $g{(k)}$. As a final step, also note that ${\begin{bmatrix}
\end{bmatrix}S} = X_{1,T}$. Overall, we thus have

with ${X_{1,T}\Pi_{S}^{\perp}} = {\begin{bmatrix}
\end{bmatrix}S\Pi_{S}^{\perp}} = 0$ where the last identity holds by the properties of the projector. $\blacksquare$

### C Proof of Corollary 1

The idea for the proof is to show that Assumption 3 implies Assumption 2 with

meaning that the proof of Theorem 5 applies to Corollary 1.

Suppose that holds. By pre- and post-multiplying both terms of by $\lbrack{BA}\rbrack$ and ${\lbrack{BA}\rbrack}^{\top}$ we get

where we set $V_{0,T}:={{AZ_{0,T}} + {BU_{0,1,T}}}$ for compactness. Let us now write $\gamma_{1}$ as

Note that the above relation is well defined since $\gamma_{1} \in {(0,0.5)}$ by hypothesis. Also notice that for every $\gamma_{1} \in {(0,0.5)}$ there uniquely corresponds $\delta_{1} > 0$.

Hence, can be rewritten as

Recall now that for arbitrary matrices $X,Y,F$ with $F \succ 0$, and a scalar $\varepsilon > 0$, it holds that

By applying this property to the right hand side of with $\varepsilon = 0.5$, $X = V_{0,T}$, $F = I$ and $Y = {AW_{0,T}}$, we get

Consider now, and let us write $\gamma_{2}$ as

where $\delta_{1}$ has been defined in and $\delta_{2}$ is a constant. Condition thus reads

Combining and and using, we finally verify that Assumption 2 is satisfied with $\gamma$ as in. To see this, consider first the terms on the left hand side of and. By applying again wit $\varepsilon = 0.5$, $X = {AW_{0,T}}$, $F = I$ and $Y = {- W_{1,T}}$ we obtain

Consider next the terms on the right hand side of and. By applying again with $\varepsilon = 0.5$, $X = X_{1,T}$, $F = I$ and $Y = {- W_{1,T}}$, we obtain

This gives the claim. $\blacksquare$
