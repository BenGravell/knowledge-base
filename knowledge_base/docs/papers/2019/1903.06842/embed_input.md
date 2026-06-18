<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Formulas for Data-Driven Control: Stabilization, Optimality, and Robustness

Topics include Data-driven control, Willems' fundamental lemma, Linear matrix inequalities, Stabilization, Linear quadratic regulation, Robust control, Output feedback, Nonlinear equilibria.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Turns the fundamental lemma into explicit LMI-based formulas for direct stabilization, LQR, output feedback, and noisy-data robustness. The paper is a core reference for direct data-driven control as a convex controller-synthesis problem rather than an identification-then-control pipeline.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In a paper by Willems and coauthors it was shown that persistently exciting data can be used to represent the input-output behavior of a linear system. Based on this fundamental result, we derive a parametrization of linear feedback systems that paves the way to solve important control problems using data-dependent Linear Matrix Inequalities only. The result is remarkable in that no explicit system's matrices identification is required. The examples of control problems we solve include the state and output feedback stabilization, and the linear quadratic regulation problem. We also discuss robustness to noise-corrupted measurements and show how the approach can be used to stabilize unstable equilibria of nonlinear systems.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Learning from data is essential to every area of science. It is the core of statistics and artificial intelligence, and is becoming ever more prevalent also in the engineering domain. Control engineering is one of the domains where learning from data is now considered as a prime issue.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Learning from data is actually not novel in control theory. System identification is one of the major developments of this paradigm, where modeling based on first principles is replaced by data-driven learning algorithms. Prediction error, maximum likelihood as well as subspace methods are all data-driven techniques which can be now regarded as standard for what concerns modeling. The learning-from-data paradigm has been widely pursued also for control design purposes. A main question is how to design control systems directly from process data with no intermediate system identification step. Besides their theoretical value, answers to this question could have a major practical impact especially in those situations where identifying a process model can be difficult and time consuming, for instance when data are affected by noise or in the presence of nonlinear dynamics. Despite many developments in this area, data-driven control is not yet well understood even if we restrict the attention to linear dynamics, which contrasts the achievements obtained in system identification. A major challenge is how to incorporate data-dependent stability and performance requirements in the control design procedure.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions to data-driven control can be traced back to the pioneering work by Ziegler and Nichols, direct adaptive control and neural networks theories. Since then, many techniques have been developed under the heading *data-driven* and *model-free* control. We mention unfalsified control theory, iterative feedback tuning, and virtual reference feedback tuning. This topic is now attracting more and more researchers, with problems ranging from PID-like control to model reference control and output tracking, predictive, robust and optimal control, the latter being one of the most frequently considered problems. The corresponding techniques are also quite varied, ranging from dynamics programming to optimization techniques and algebraic methods. These contributions also differ with respect to how learning is approached. Some methods only use a batch of process data meaning that learning is performed off-line, while other methods are iterative and require multiple on-line experiments. We refer the reader to for more references on data-driven control methods.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Willems *et al.*'s fundamental lemma and paper contribution*

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A central question in data-driven control is how to replace process models with data. For linear systems, there is actually a fundamental result which answers this question, proposed by Willems *et al.*. Roughly, this result stipulates that the whole set of trajectories that a linear system can generate can be represented by a finite set of system trajectories provided that such trajectories come from sufficiently excited dynamics. While this result has been (more or less explicitly) used for data-driven control design, certain implications of the so-called *Willems *et al.*'s fundamental lemma* seems not fully exploited.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we first revisit Willems *et al.*'s fundamental lemma, originally cast in the behavioral framework, through classic state-space descriptions (Lemma 2). Next, we show that this result can be used to get a data-dependent representation of the open-loop and closed-loop dynamics under a feedback interconnection. The first result (Theorem 1) indicates that the parametrization that emerges from the fundamental lemma is in fact the solution to a classic least-squares problem, and has clear connections with the so-called Dynamic Mode Decomposition. The second result (Theorem 2) is even more interesting as it provides a data-based representation of the closed-loop system transition matrix, where the controller is itself parametrized through data.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Theorem 2 turns out to have surprisingly straightforward, yet profound, implications for control design. We discuss this fact in Section IV. The main point is that the parametrization provided in Theorem 2 can be naturally related to the classic Lyapunov stability inequalities. This makes it possible to cast the problem of designing state-feedback controllers in terms of a simple Linear Matrix Inequality (LMI) (Theorem 3). In Theorem 4, the same arguments are used to solve a linear quadratic regulation problem through convex optimization. A remarkable feature of these results is that: (i) no parametric model of system is identified; (ii) stability guarantees come with a finite (computable) number of data points. Theorems 3 and 4 should be understood as *examples* of how the parametrization given in Theorem 2 can be used to approach the direct design of control laws from data. In fact, LMIs have proven their effectiveness in a variety of control design problems, and we are confident that the same arguments can be used for approaching other, more complex, design problems such as $H_{\infty}$ control and quadratic stabilization.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section V, we further exemplify the merits of the proposed approach by considering the problem of designing stabilizing controllers when data are corrupted by noise (Theorem 5), as well as the problem of stabilizing an unstable equilibrium of a nonlinear system (Theorem 6), both situations where identification can be challenging. The main derivations are given for state feedback. The case of output feedback (Theorem 8) is discussed in Section VI. Concluding remarks are given in Section VII.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-A Notation", "weight": 1.0} -->

When the signal is not restricted to an interval then it is simply denoted by its symbol, say $z$. To avoid notational burden, we use $z_{\lbrack k,{k + T}\rbrack}$ also to denote the sequence $\{{z{(k)}},\ldots,{z{({k + T})}}\}$. For the same reason, we simply write $\lbrack k,{k + T}\rbrack$ to denote the discrete interval ${\lbrack k,{k + T}\rbrack} \cap {\mathbb{Z}}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-A Notation", "weight": 1.0} -->

We denote the Hankel matrix associated to $z$ as

<!-- chunk {"id": "body-0014", "role": "body", "section": "I-A Notation", "weight": 1.0} -->

where $i \in {\mathbb{Z}}$ and ${t,N} \in {\mathbb{N}}$. The first subscript denotes the time at which the first sample of the signal is taken, the second one the number of samples per each column, and the last one the number of signal samples per each row. Sometimes, if $t = 1$, noting that the matrix $Z_{i,t,N}$ has only one block row, we simply write

<!-- chunk {"id": "body-0015", "role": "body", "section": "Persistence of excitation and Willems *et al.*'s fundamental lemma", "weight": 1.0} -->

In this section, we revisit the main result in and state a few auxiliary results inspired by subspace identification, which will be useful throughout the paper.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Persistence of excitation and Willems *et al.*'s fundamental lemma", "weight": 1.0} -->

For the sake of simplicity, throughout the paper we consider a controllable and observable discrete-time linear system

<!-- chunk {"id": "body-0017", "role": "body", "section": "Persistence of excitation and Willems *et al.*'s fundamental lemma", "weight": 1.0} -->

where $x_{0}$ is the system initial state, and where

<!-- chunk {"id": "body-0018", "role": "body", "section": "Persistence of excitation and Willems *et al.*'s fundamental lemma", "weight": 1.0} -->

are the Toeplitz and observability matrices of order $t$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Persistence of excitation and Willems *et al.*'s fundamental lemma", "weight": 1.0} -->

Let now $u_{d,{\lbrack 0,{T - 1}\rbrack}}$ and $y_{d,{\lbrack 0,{T - 1}\rbrack}}$ be the input-output data of the system collected during an experiment, and let

<!-- chunk {"id": "body-0020", "role": "body", "section": "Persistence of excitation and Willems *et al.*'s fundamental lemma", "weight": 1.0} -->

be the corresponding Hankel matrix. Similarly to, we can write

<!-- chunk {"id": "body-0021", "role": "body", "section": "Persistence of excitation and Willems *et al.*'s fundamental lemma", "weight": 1.0} -->

and $x_{d}{(i)}$ are the state samples. For $u_{d}$, $y_{d}$, and $x_{d}$, we use the subscript $d$ so as to emphasize that these are the sample data collected from the system during some experiment.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-A Persistently exciting data and the fundamental lemma", "weight": 1.0} -->

Throughout the paper, having the rank condition

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-A Persistently exciting data and the fundamental lemma", "weight": 1.0} -->

satisfied plays an important role. As we will see, a condition of this type in fact ensures that the data encode all the information for the direct design of control laws. A fundamental property established in is that it is possible to guarantee when the input is sufficient exciting. We first recall the notion of persistency of excitation.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Data-based system representations", "weight": 1.0} -->

Lemma 2 allows us to get a data-dependent representation of the open-loop and closed-loop dynamics of system (1a). The first result (Theorem 1) is a covert system identification result where, however, the role of Lemma 2 is emphasized, and which draws connections with the so-called Dynamic Mode Decomposition. Theorem 2 shows instead how one can parametrize feedback interconnections just by using data. This result will be key later on for deriving control design methods that avoid the need to identify a parametric model of the system to be controlled.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Data-based system representations", "weight": 1.0} -->

Consider a persistently exciting input sequence $u_{d,{\lbrack 0,{T - 1}\rbrack}}$ of order $t + n$ with $t = 1$. Notice that the only requirement on $T$ is that $T \geq {{{({m + 1})}n} + m}$, which is necessary for the persistence of excitation condition to hold. By Lemma 1,

<!-- chunk {"id": "body-0026", "role": "body", "section": "Data-based system representations", "weight": 1.0} -->

From now, we will directly refer to condition, bearing in mind that this condition requires persistently exciting inputs of order $n + 1$. Before proceeding, we point out that condition can always be directly assessed when the state of the system is accessible. When instead only input/output data are accessible, condition cannot be directly assessed. Nonetheless, thanks to Lemma 1 this condition can always be enforced by applying an exciting input signal of a sufficiently high order -- for a discussion on the types of persistently exciting signals the reader is referred to \[2, Section 10\]. We will further elaborate on this point in Section VI where we also give an alternative explicitly verifiable condition for the case where only input/output data of the system are accessible.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A Data-based open-loop representation", "weight": 1.0} -->

The next result gives a data-based representation of a linear system and emphasizes the key role of Lemma 2.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B Data-based closed-loop representation", "weight": 1.0} -->

We now exploit Lemma 2 to derive a parametrization of system (1a) in closed-loop with a state-feedback law $u = {Kx}$. We give here a proof of this result since the arguments we use will often recur in the next sections.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-C From indirect to direct data-driven control", "weight": 1.0} -->

Obviously, Theorem 1 already provides a way for designing controllers from data, at least when the state of the system to be controlled is fully accessible. However, this approach is basically equivalent to a model-based approach where the system matrices $A$ and $B$ are first reconstructed using a collection of sample trajectories. A crucial observation that emerges from Theorem 2 is that also the controller $K$ can be parametrized through data via. Thus for design purposes one can regard $G_{K}$ as a *decision variable*, and search for the matrix $G_{K}$ that guarantees stability and performance specifications. In fact, as long as $G_{K}$ satisfies the condition ${X_{0,T}G_{K}} = I_{n}$ in we are ensured that $X_{1,T}G_{K}$ provides an equivalent representation of the closed-loop matrix $A + {BK}$ with feedback matrix $K = {U_{0,1,T}G_{K}}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-C From indirect to direct data-driven control", "weight": 1.0} -->

As shown in the next section, this enable design procedures that avoid the need to identify a parametric model of the system.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-C From indirect to direct data-driven control", "weight": 1.0} -->

We point out that Theorem 2 already gives an identification-free method for *checking* whether a candidate controller $K$ is stabilizing or not. In fact, given $K$, any solution $G_{K}$ to is such that ${X_{1,T}G_{K}} = {A + {BK}}$. One can therefore compute the eigenvalues of $X_{1,T}G_{K}$ to check whether $K$ is stabilizing or not. This method does not require to place $K$ into feedback, in the spirit of unfalsified control theory.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Data-driven control design: stabilization and optimal control", "weight": 1.0} -->

In this section, we discuss how Theorem 2 can be used to get identification-free design algorithms. Although the problems considered hereafter are all of practical relevance, we would like to regard them as application *examples* of Theorem 2. In fact, we are confident that Theorem 2 can be used to approach other, more complex, design problems such as $H_{\infty}$ control and quadratic stabilization.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A State feedback design and data-based parametrization of all stabilizing controllers", "weight": 1.0} -->

By Theorem 2, the closed-loop system under state-feedback $u = {Kx}$ is such that

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A State feedback design and data-based parametrization of all stabilizing controllers", "weight": 1.0} -->

where $G_{K}$ satisfies. One can therefore search for a matrix $G_{K}$ such that $X_{1,T}G_{K}$ satisfies the classic Lyapunov stability condition. As the next result shows, it turns out that this problem can be actually cast in terms of a simple Linear Matrix Inequality (LMI).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 1", "weight": 1.0} -->

*(Numerical implementation)* There are other ways to implement. One of these alternatives is obtained, considering the first inequality, the third equality and condition $P \succ 0$, and rewriting them as

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 1", "weight": 1.0} -->

In this case the resulting stabilizing state feedback-gain takes the expression $K = {U_{0,1,T}QP^{- 1}}$. In the previous numerical example but also in those that follow we observed that a formulation like the one above is more stable numerically. The reason is that CVX cannot directly interpret as a symmetric matrix (the upper-left block is given by $X_{0,T}Q$ with non-symmetric decision variable $Q$), and returns a warning regarding the expected outcome. $\blacksquare$

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 2", "weight": 1.0} -->

*(Design for continuous-time systems)* Similar arguments can be used to deal with continuous-time systems. Given a sampling time $\Delta > 0$, let

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 2", "weight": 1.0} -->

be input and state sampled trajectories. Under condition (note that, if the sequence ${u_{d}{}},{u_{d}{(\Delta)}},\ldots$ is persistently exciting of order $n + 1$, then the application of the zero-order hold signal obtained from the input samples above ensures condition for the sampled-data system for generic choices of $\Delta$) we have ${A + {BK}} = {X_{1,T}G_{K}}$ where

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Hence, for any given $K$, the closed-loop system with $u = {Kx}$ is asymptotically stable if and only if there exists $P \succ 0$ such that

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 2", "weight": 1.0} -->

where $G_{K}$ satisfies. In full analogy with the discrete-time case, it follows that any matrix $Q$ satisfying

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 2", "weight": 1.0} -->

is such that $K = {U_{0,1,T}Q{({X_{0,T}Q})}^{- 1}}$ is a stabilizing feedback gain. The main difference with respect to the case of discrete-time systems is the presence of the matrix $X_{1,T}$ that contains the derivatives of the state at the sampling times, which are usually not available as measurements. The use of these methods in the context of continuous-time systems might require the use of filters for the approximation of derivatives. This is left for future research. We stress that even though the matrix is built starting from input and state samples, the feedback gain $K = {U_{0,1,T}Q{({X_{0,T}Q})}^{- 1}}$, where $Q$ is the solution of, stabilizes the continuous-time system, not its sampled-data model. $\blacksquare$

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-B Linear quadratic regulation", "weight": 1.0} -->

Matrix (in)equalities similar to the one in are recurrent in control design, with the major difference that in only information collected from data appears, rather than the system matrices. Yet, these matrix inequalities can inspire the data-driven solution of other control problems. Important examples are optimal control problems.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-B Linear quadratic regulation", "weight": 1.0} -->

where $\xi$ is an external input to the system, and where $z$ is a performance signal of interest; $Q_{x} \succeq 0$, $R \succ 0$ are weighting matrices with $(Q_{x},A)$ observable. The objective is to design a state-feedback law $u = {Kx}$ which renders $A + {BK}$ stable and minimizes the $H_{2}$ norm of the transfer function $h:{\xi\rightarrow z}$ \[39, Section 4\],

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-B Linear quadratic regulation", "weight": 1.0} -->

This corresponds in the time domain to the $2$-norm of the output $z$ when impulses are applied to the input channels, and it can also be interpreted as the mean-square deviation of $z$ when $\xi$ is a white process with unit covariance. It is kwown \[39, Section 6.4\] that the solution to this problem is given by the controller

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-B Linear quadratic regulation", "weight": 1.0} -->

where $X$ is the unique positive definite solution to the discrete-time algebraic Riccati (DARE) equation

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-B Linear quadratic regulation", "weight": 1.0} -->

This problem of finding $K$ can be equivalently formulated as a convex program. To see this, notice that the closed-loop system is given by

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-B Linear quadratic regulation", "weight": 1.0} -->

where $W_{c}$ denotes the controllability Gramian of the closed-loop system, which satisfies

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-B Linear quadratic regulation", "weight": 1.0} -->

where $W_{c} \succeq I$. The second term appearing in the trace function is equivalent to ${trace}{({R^{1/2}KW_{c}K^{\top}R^{1/2}})}$. As a natural counterpart of the continuous-time formulation, the optimal controller $K$ can be found by solving the optimization problem

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-B Linear quadratic regulation", "weight": 1.0} -->

This can be cast as a convex optimization problem by means of suitable change of variables. Based on this formulation, it is straightforward to derive a data-dependent formulation of this optimization problem.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 3", "weight": 1.0} -->

*(Numerical issues for unstable systems)* The above results are implicitly based on open-loop data. When dealing with unstable systems numerical instability problems may arise. Nonetheless, by Lemma 1 a persistently exciting input of order $n + 1$ suffices to ensure. In turn (see the discussion in Section III), this ensures that we "only" need $T = {{{({m + 1})}n} + m}$ samples in order to compute the controller. This guarantees that one can compute *a priori* for how long a system should run in open loop. In practice, this result also guarantees practical applicability for systems of moderate size that are not strongly unstable.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 3", "weight": 1.0} -->

When dealing with large scale and highly unstable systems the situation is inevitably more complex, and other solutions might be needed. For instance, if a stabilising controller $\hat{K}$ (not necessarily performing) is known, then one can think of running *closed-loop* experiments during which a persistently exciting signal is superimposed to the control signal given by $\hat{K}$, making sure that all the previous results continue to follow without any modification. Measures of this type are widely adopted in adaptive control to overcome issues of loss of stabilisability due to the lack of excitation caused by feedback \[42, Section 7.6\]. $\blacksquare$

<!-- chunk {"id": "body-0052", "role": "body", "section": "Robustness: noise-corrupted data and nonlinear systems", "weight": 1.0} -->

In the previous subsections, we have considered data-driven design formulations based on LMIs. Besides their simplicity, one of the main reasons for resorting to such formulations is that LMIs have proven their effectiveness also in the presence of perturbations and/or uncertainties around the system to be controlled. In this subsection, we exemplify this point by considering stabilization with noisy data, as well as the problem of stabilizing an unstable equilibrium of a nonlinear system, which are both situations where identification can be challenging.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-A Stabilization with noisy data", "weight": 1.0} -->

Consider again system (1a), but suppose that one can only measure the signal

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-A Stabilization with noisy data", "weight": 1.0} -->

where $w$ is an unknown measurement noise. We will assume no particular statistics on the noise. The problem of interest is to design a stabilizing controller for system (1a) assuming that we measure $\zeta$. Let

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-A Stabilization with noisy data", "weight": 1.0} -->

where $w_{d}{(k)}$, $k = {0,1,\ldots,T}$ are noise samples associated to the experiment, and

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-A Stabilization with noisy data", "weight": 1.0} -->

The latter are the matrices containing the available information about the state of the system. Recall that in the noise-free case, a stabilizing controller can be found by searching for a solution $Q$ to the LMI. In the noisy case, it seems thus natural to replace with the design condition

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-A Stabilization with noisy data", "weight": 1.0} -->

This condition already gives a possible solution approach. In fact, since positive definiteness is preserved under sufficiently small perturbations, for every solution $Q$ to there exists a noise level such that $Q$ will remain solution to, and such that the controller $K = {U_{0,1,T}Q{({Z_{0,T}Q})}^{- 1}}$ obtained by replacing $X_{0,T}$ with $Z_{0,T}$ will remain stabilizing, where the latter property holds since the eigenvalues of $A + {BK}$ depend with continuity on $K$. This indicates that the considered LMI-based approach has some intrinsic degree of robustness to measurement noise.

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-A Stabilization with noisy data", "weight": 1.0} -->

We formalize these considerations by focusing the attention on a slightly different formulation, which consists in finding a matrix $Q$ and a scalar $\alpha > 0$ such that

<!-- chunk {"id": "body-0059", "role": "body", "section": "V-A Stabilization with noisy data", "weight": 1.0} -->

It is easy to verify that in the noise-free case and with persistently exciting inputs also this formulation is always feasible and any solution $Q$ is such that $K = {U_{0,1,T}Q{({Z_{0,T}Q})}^{- 1}}$ gives a stabilizing controller. We show this fact in the next Remark 4. We consider the formulation (V-A) because it makes it possible to explicitly *quantify* noise levels for which a solution returns a stabilizing controller.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Remark 4", "weight": 1.0} -->

*(Feasibility of (V-A) under noise-free data)* In the noise-free case, that is when $Z_{0,T} = X_{0,T}$ and $Z_{1,T} = X_{1,T}$, the formulations and coincide. Suppose then that is feasible and let $\overline{Q}$ be a solution. Since positive definiteness is preserved under small perturbations, ${(Q,\alpha)} = {(\overline{Q},\overline{\beta})}$ will be a solution to the first of (V-A) for a sufficiently small $\overline{\beta} > 0$. Hence ${(Q,\alpha)} = {({\delta\overline{Q}},{\delta\overline{\beta}})}$ will remain feasible for the first of (V-A) for all $\delta > 0$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Remark 4", "weight": 1.0} -->

We can thus pick $\delta$ small enough so that ${(Q,\alpha)}:={({\delta\overline{Q}},{\delta\overline{\beta}})}$ satisfies also the second of (V-A).

<!-- chunk {"id": "body-0062", "role": "body", "section": "Remark 4", "weight": 1.0} -->

Conversely, consider any solution $(Q,\alpha)$ to (V-A) and let $K = {U_{0,1,T}Q{({Z_{0,T}Q})}^{- 1}}$. Since $\alpha > 0$, the first inequality in (V-A) implies that also holds, which, in view of the identities $Z_{0,T} = X_{0,T}$ and $Z_{1,T} = X_{1,T}$, is equivalent to have condition satisfied. Hence, the gain $K$ is stabilizing. $\blacksquare$

<!-- chunk {"id": "body-0063", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

have full row rank. $\blacksquare$

<!-- chunk {"id": "body-0064", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Assumptions 1 and 2 both express the natural requirement that the loss of information caused by noise is not significant. In particular, Assumption 1 is the counterpart of condition for noise-free data, and is always satisfied when the input is persistently exciting and the noise is sufficiently small. This is because: (i) condition implies that $X_{0,T}$ has rank $n$; (ii) $X_{1,T} = {{AX_{0,T}} + {BU_{0,1,T}}}$ so that condition implies that ${{rank}X_{1,T}} = {{rank}\left\lbrack {BA} \right\rbrack} = n$ otherwise the system would not be controllable; and (iii) the rank of a matrix does not change under sufficiently small perturbations.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Intuitively, Assumption 1 alone is not sufficient to guarantee the existence of a solution returning a stabilizing controller since this assumption may also be verified by arbitrary noise, in which case the data need not contain any useful information. Assumption 2 takes into account this aspect, and plays the role of a "*signal-to-noise ratio*" (SNR) condition. Notice that when Assumption 1 holds then Assumption 2 is always satisfied for large enough $\gamma$. As next theorem shows, however, to get stability one needs to restrict the magnitude of $\gamma$, meaning that the SNR must be sufficiently large.

<!-- chunk {"id": "body-0066", "role": "body", "section": "V-B Stabilization of nonlinear systems", "weight": 1.0} -->

The previous result shows that a controller can be designed in the presence of noise provided that signal-to-noise ratio is sufficiently small. This hints at the possibility of designing also a stabilizing control for nonlinear systems based on data alone. As a matter of fact, around an equilibrium a nonlinear system can be expressed via its first order approximation plus a reminder. If we run our experiment in such a way that the input and the state remain sufficiently close to the equilibrium, then the reminder can be viewed as a process disturbance of small magnitude and there is a legitimate hope that the robust stabilization result also applies to this case. In the rest of this section we formalize this intuition.

<!-- chunk {"id": "body-0067", "role": "body", "section": "V-B Stabilization of nonlinear systems", "weight": 1.0} -->

and let $(\overline{x},\overline{u})$ be a *known* equilibrium pair, that is such that $\overline{x} = {f{(\overline{x},\overline{u})}}$. Let us rewrite the nonlinear system as

<!-- chunk {"id": "body-0068", "role": "body", "section": "V-B Stabilization of nonlinear systems", "weight": 1.0} -->

The quantity $d$ accounts for higher-order terms and it has the property that is goes to zero faster than $\deltax$ and $\deltau$, namely we have

<!-- chunk {"id": "body-0069", "role": "body", "section": "V-B Stabilization of nonlinear systems", "weight": 1.0} -->

with $R{({\deltax},{\deltau})}$ an $n \times {({n + m})}$ matrix of smooth functions with the property that

<!-- chunk {"id": "body-0070", "role": "body", "section": "V-B Stabilization of nonlinear systems", "weight": 1.0} -->

It is known that if the pair $(A,B)$ defining the linearized system is stabilizable then the controller $K$ rendering $A + {BK}$ stable also exponentially stabilizes the equilibrium $(\overline{x},\overline{u})$ for the original nonlinear system. The objective here is to provide sufficient conditions for the design of $K$ from data. To this end, we consider the following result which is an adaptation of Theorem 5. Let

<!-- chunk {"id": "body-0071", "role": "body", "section": "V-B Stabilization of nonlinear systems", "weight": 1.0} -->

be the data resulting from an experiment carried out on the nonlinear system. Note that the matrices $X_{0,T}$, $X_{1,T}$ and $U_{0,1,T}$ are known. Consider the following assumptions.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

have full row rank. $\blacksquare$

<!-- chunk {"id": "body-0073", "role": "body", "section": "Input-output data: the case of SISO systems", "weight": 1.0} -->

In Section IV-A, the measured data are the inputs and the state, and the starting point is to express the trajectories of the system and the control gain in terms of the Hankel matrix of input-state data. Here we show how similar arguments can be used when only input/output data are accessible. The main derivations are given for single-input single-output (SISO) systems. A remark on multi-input multi-output (MIMO) systems is provided in Section VI-C.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Input-output data: the case of SISO systems", "weight": 1.0} -->

Consider a SISO systems as in in left difference operator representation \[43, Section 2.3.3\],

<!-- chunk {"id": "body-0075", "role": "body", "section": "Input-output data: the case of SISO systems", "weight": 1.0} -->

This representation corresponds to for $D = 0$. In this case, one can reduce the output measurement case to the state measurement case with minor effort. Let

<!-- chunk {"id": "body-0076", "role": "body", "section": "Input-output data: the case of SISO systems", "weight": 1.0} -->

from we obtain the state space system on the next page. Note that we turned our attention to a system of order $2n$, which is not minimal.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Input-output data: the case of SISO systems", "weight": 1.0} -->

{{\chi{({k + 1})}} =} &amp; {{\underset{\mathcal{A}}{\underbrace{\begin{bmatrix} 0 &amp; 1 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 \\ 0 &amp; 0 &amp; 1 &amp; \cdots &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 \\ \vdots &amp; \vdots &amp; \vdots &amp; \ddots &amp; \vdots &amp; \vdots &amp; \vdots &amp; \vdots &amp; \ddots &amp; \vdots \\ 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 1 &amp; 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 \\ {-a_{1}} &amp;

<!-- chunk {"id": "body-0078", "role": "body", "section": "Input-output data: the case of SISO systems", "weight": 1.0} -->

{-a_{2}} &amp; {-a_{3}} &amp; \cdots &amp; {-a_{n}} &amp; b_{1} &amp; b_{2} &amp; b_{3} &amp; \cdots &amp; b_{n} \\ &amp; &amp; &amp; &amp; &amp; &amp; &amp; &amp; &amp; \\ 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 &amp; 1 &amp; 0 &amp; \cdots &amp; 0 \\ 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 &amp; 0 &amp; 1 &amp; \cdots &amp; 0 \\ \vdots &amp; \vdots &amp; \vdots &amp; \ddots &amp; \vdots &amp; \vdots &amp; \vdots &amp; \vdots &amp; \ddots &amp;

<!-- chunk {"id": "body-0079", "role": "body", "section": "Input-output data: the case of SISO systems", "weight": 1.0} -->

\vdots \\ 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 1 \\ 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 \end{bmatrix}}}\chi{(k)}} + {\underset{\mathcal{B}}{\underbrace{\begin{bmatrix} {{y{(k)}} =} &amp; {\underset{\mathcal{C}}{\underbrace{\begin{bmatrix} {-a_{1}} &amp; {-a_{2}} &amp; {-a_{3}} &amp; \cdots &amp; {-a_{n}} &amp; b_{1} &amp; b_{2} &amp; b_{3} &amp; \cdots &amp;

<!-- chunk {"id": "body-0080", "role": "body", "section": "Input-output data: the case of SISO systems", "weight": 1.0} -->

Consider now the matrix in written for the system ${\chi{({k + 1})}} = {{\mathcal{A}\chi{(k)}} + {\mathcal{B}u{(k)}}}$, with $T$ satisfying $T \geq {{2n} + 1}$. If this matrix is full-row rank, then the analysis in the previous sections can be repeated also for system. For system the matrix in question takes the form

<!-- chunk {"id": "body-0081", "role": "body", "section": "VI-A Data-based open-loop representation", "weight": 1.0} -->

Similar to the case in which inputs and states are measured, the full rank property plays a crucial role in expressing the system via data. As a matter of fact, for any pair $(u,\chi)$ we have

<!-- chunk {"id": "body-0082", "role": "body", "section": "VI-A Data-based open-loop representation", "weight": 1.0} -->

As in the proof of Theorem 1 for the full state measurement case, we can thus solve for $g$, replace it, and obtain the following result.

<!-- chunk {"id": "body-0083", "role": "body", "section": "VI-B Design of output feedback controllers", "weight": 1.0} -->

Consider the left difference operator representation, its realization and the input/state pair $(u,\chi)$. We introduce a controller of the form

<!-- chunk {"id": "body-0084", "role": "body", "section": "VI-B Design of output feedback controllers", "weight": 1.0} -->

whose state space representation is given,

<!-- chunk {"id": "body-0085", "role": "body", "section": "VI-B Design of output feedback controllers", "weight": 1.0} -->

{{\chi^{c}{({k + 1})}} =} &amp; {{\underset{\mathcal{F}}{\underbrace{\begin{bmatrix} 0 &amp; 1 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 \\ 0 &amp; 0 &amp; 1 &amp; \cdots &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; \ldots &amp; 0 \\ \vdots &amp; \vdots &amp; \vdots &amp; \ddots &amp; \vdots &amp; \vdots &amp; \vdots &amp; \vdots &amp; \ddots &amp; \vdots \\ 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 1 &amp; 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 \\ {-c_{1}}

<!-- chunk {"id": "body-0086", "role": "body", "section": "VI-B Design of output feedback controllers", "weight": 1.0} -->

&amp; {-c_{2}} &amp; {-c_{3}} &amp; \cdots &amp; {-c_{n}} &amp; d_{1} &amp; d_{2} &amp; d_{3} &amp; \cdots &amp; d_{n} \\ &amp; &amp; &amp; &amp; &amp; &amp; &amp; &amp; &amp; \\ 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 &amp; 1 &amp; 0 &amp; \cdots &amp; 0 \\ 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 &amp; 0 &amp; 1 &amp; \cdots &amp; 0 \\ \vdots &amp; \vdots &amp; \vdots &amp; \ddots &amp; \vdots &amp; \vdots &amp; \vdots &amp; \vdots &amp; \ddots

<!-- chunk {"id": "body-0087", "role": "body", "section": "VI-B Design of output feedback controllers", "weight": 1.0} -->

&amp; \vdots \\ 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 1 \\ 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; \cdots &amp; 0 \end{bmatrix}}}\chi^{c}{(k)}} + {\underset{\mathcal{G}}{\underbrace{\begin{bmatrix} {{y^{c}{(k)}} =} &amp; {{\underset{\mathcal{H}}{\underbrace{\begin{bmatrix} {-c_{1}} &amp; {-c_{2}} &amp; {-c_{3}} &amp; \cdots &amp; {-c_{n}} &amp; d_{1} &amp; d_{2} &amp;

<!-- chunk {"id": "body-0088", "role": "body", "section": "VI-B Design of output feedback controllers", "weight": 1.0} -->

with state $\chi^{c}$ defined similar to. In the closed-loop system, we enforce the following interconnection conditions relating the process and the controller

<!-- chunk {"id": "body-0089", "role": "body", "section": "VI-B Design of output feedback controllers", "weight": 1.0} -->

Note in particular the identity, for $k \geq n$,

<!-- chunk {"id": "body-0090", "role": "body", "section": "VI-B Design of output feedback controllers", "weight": 1.0} -->

Hence, for $k \geq n$, there is no loss of generality in considering as the closed-loop system the system

<!-- chunk {"id": "body-0091", "role": "body", "section": "VI-B Design of output feedback controllers", "weight": 1.0} -->

In the following result we say that controller stabilizes system, meaning that the closed-loop system is asymptotically stable.

<!-- chunk {"id": "body-0092", "role": "body", "section": "VI-C A remark on the case of MIMO systems", "weight": 1.0} -->

An analysis similar to the one presented before can be repeated starting from the left-difference operator of a MIMO system,

<!-- chunk {"id": "body-0093", "role": "body", "section": "VI-C A remark on the case of MIMO systems", "weight": 1.0} -->

In case of MIMO systems, we assume that we collect data with an input $u_{d,{\lbrack 0,{T - 1}\rbrack}}$, $T \geq {{({{{({m + p})}n} + 1})}{({m + 1})}}$, persistently exciting of order ${{({m + p})}n} + 1$. Then, by Lemma 1 we obtain the fulfilment of the following condition

<!-- chunk {"id": "body-0094", "role": "body", "section": "Discussion and conclusions", "weight": 1.5} -->

Persistently exciting data enable the construction of data-dependent matrices that can replace systems models. Adopting this paradigm proposed by we have shown the existence of a parametrization of feedback control systems that allows us to reduce the stabilization problem to an equivalent data-dependent linear matrix inequality. Since LMIs are ubiquitous in systems and control we expect that our approach could lead to data-driven solutions to many other control problems. As an example we have considered an LQR problem. For several control problems, LMIs have proven their effectiveness in providing robustness to various sources of uncertainty. We have capitalized on this fact extending the analysis to the case of noise-corrupted data and showing how the approach can be used to stabilize unstable equilibria of nonlinear systems, which are both situations where identification can be challenging. A remarkable feature of all these results is that: (i) no parametric model of system is identified; (ii) stability guarantees come with a finite (computable) number of data points.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Discussion and conclusions", "weight": 1.5} -->

Studying how our approach can be used to systematically address control problems via data-dependent LMIs could be very rewarding, and lead to a methodical inclusion of data to analyze and design control systems. A great leap forward will come from systematically extending the methods of this paper to systems where identification is challenging, such as switched and nonlinear systems. The results of this paper show that our approach is concretely promising for nonlinear systems, but we have only touched the surface of this research area. Estimating the domain of attraction or considering other approaches such as *lifting* techniques are two simple examples of compelling research directions for nonlinear systems. Recent results have reignited the interest of the community on system identification for nonlinear systems, interestingly pointing out the importance of the concept of persistently exciting signals. We are confident that our approach will also play a fundamental role in developing a systematic methodology for the data-driven design of control laws for nonlinear systems.
