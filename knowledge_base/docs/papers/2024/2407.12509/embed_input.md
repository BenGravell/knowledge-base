<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Shortest Experiment for Linear System Identification

Topics include System identification, Experiment design, Behavioral systems, Linear systems, Persistency of excitation, Online experiment design, Sample complexity, Input-output data.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Designs adaptive inputs that recover an unknown LTI system with the shortest possible experiment length under dimension and lag bounds. It is closely related to the informativity perspective because it asks how little data can be made informative for identification.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper is concerned with the following problem: given an upper bound of the state-space dimension and lag of a linear time-invariant system, design a sequence of inputs so that the system dynamics can be recovered from the resulting input-output data. As our main result we propose a new online experiment design method, meaning that the selection of the inputs is iterative and guided by data samples collected in the past. We show that this approach leads to the shortest possible experiments for linear system identification. In terms of sample complexity, the proposed method outperforms offline methods based on persistency of excitation as well as existing online experiment design methods.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Background*: In the context of system identification, *experiment design* is concerned with the selection of inputs of a dynamical system in such a way that the resulting input-output data contain sufficient information about the system dynamics. Experiment design is a classical topic that has been investigated from different angles throughout the years.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

An experiment design result that has recently been popularized is the so-called *fundamental lemma* by Willems and his coauthors. Roughly speaking, the result says that the dynamics of a linear time-invariant system can be uniquely identified from input-output data if the input data are chosen to be sufficiently persistently exciting. The fundamental lemma also provides a parameterization of all finite trajectories of the system, in terms of a data Hankel matrix. This parameterization has been applied in several recent data-driven analysis and control techniques ranging from simulation and linear quadratic regulation to predictive control, stabilization and dissipativity analysis.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The recent interest in data-driven control has also led to extensions of the fundamental lemma itself. Its original proof was presented in the language of behavioral theory; an alternative proof for state space systems was provided. Generalizations to uncontrollable systems are presented in and extensions to continuous-time systems. Robust/quantitative versions are explored in while frequency domain formulations have been considered. Furthermore, the fundamental lemma has been generalized to various other model classes such as descriptor systems, flat nonlinear systems, linear parameter-varying systems, and stochastic ones.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The assumption of persistency of excitation, central to the fundamental lemma, imposes a lower bound on the required number of data samples for system identification. This lower bound is conservative in the sense that system identification is possible using less data, as long as certain conditions are met. Until recently, the precise conditions enabling system identification were still missing from the literature. However necessary and sufficient conditions are provided under which the data contain sufficient information for system identification, assuming minimality of the data-generating system and upper (and lower) bounds on its lag and state-space dimension. As is quite reminiscent of the subspace identification literature, these conditions involve rank properties of data Hankel matrices. However, a truly remarkable feat of is that the *depth* of these Hankel matrices is not given a priori but is *determined from the data*.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we will build on the framework of. However, unlike that focused on analyzing informativity of given data sets, the purpose of this paper is to *design* experiments that are informative for system identification.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

What is the shortest possible sequence of input-output data that enables linear system identification? And, if possible, how can we design the inputs of the system in order to generate such a shortest experiment?

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Apart from being of theoretical interest, these questions are also highly relevant for control applications. In fact, the computation time of, for example, data-driven predictive control scales cubically with the data length. Working with shorter yet informative experiments reduces the computational burden of these methods.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We assume that the unknown data-generating system is minimal and its lag and state-space dimension are upper bounded by $L$ and $N$. Then, based, we formulate a lower bound $T$ on the data length of any experiment that is informative for system identification (see ).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose the experiment design method OnlineExperiment$(L,N)$. This procedure designs the inputs *online*, i.e., on the basis of past input-output samples. In Theorem we prove that this method leads to informative experiments of length $T$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

A remarkable outcome of this paper is the fact that experiments can be designed of length *precisely equal to the lower bound $T$*. Interestingly, this number of samples $T$ depends on the unknown system and is thus not given a priori. It is revealed after the experiment design algorithm terminates.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Relation to previous work*: The online experiment design method of this paper always requires less samples than the persistency of excitation requirement of the fundamental lemma. In many cases, there is a substantial difference in number of data samples. We provide an example of this in Section. The online experiment design method of keeps the depth of the data Hankel matrix *fixed* during the operation of the algorithm. In contrast to, our approach *adapts the depth* of the Hankel matrix during operation of the algorithm. The rationale is that the "correct" depth of the Hankel matrix for the necessary and sufficient conditions of is *a priori unknown*. We show in Section that our method outperforms in some situations, depending on the given $L$ and $N$. In other cases, our results prove that the approach of leads to the shortest experiments for linear system identification.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Outline*: In Section we treat preliminaries. In Section we recap the fundamental lemma. In Section we recall the definition and characterization of *informativity for system identification*. Subsequently, in Section we formalize the problem and in Section we present our main results. In Section we provide examples, while Section contains a comparison to the state-of-the-art. Finally, in Section we conclude the paper.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Void matrices", "weight": 1.0} -->

A void matrix is a matrix with zero rows and/or zero columns. We will use the notation $0_{n,0}$ and $0_{0,m}$ to denote, respectively, $n \times 0$ and $0 \times m$ void matrices. All matrix operations extend to void matrices in a natural manner. In particular, if $M$ and $N$ are, respectively $p \times q$ and $q \times r$ matrices, $MN$ is a $p \times r$ void matrix if $p = 0$ or $r = 0$ and ${MN} = 0_{p,r}$ if ${p,r} \geqslant 1$ and $q = 0$. In addition, the rank of a void matrix is zero.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Integer intervals and Hankel matrices", "weight": 1.0} -->

Given ${i,j} \in {\mathbb{Z}}$ with $i \leqslant j$, we write $\lbrack i,j\rbrack$ to denote the ordered set of all integers between $i$ and $j$, including both $i$ and $j$. By convention, ${\lbrack i,j\rbrack} = \varnothing$ if $i > j$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Integer intervals and Hankel matrices", "weight": 1.0} -->

We say that $f_{\lbrack i,j\rbrack}$ is *persistently exciting of order $k + 1$* if $H_{k}{(f_{\lbrack i,j\rbrack})}$ has full row rank. We stress that $H_{k}$ has $k + 1$ block rows, which is slightly different from the notation in most of the literature, but adopted here to be consistent with the paper.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Input-state-output systems", "weight": 1.0} -->

Throughout the paper, we work with linear discrete-time input-state-output systems of the form

<!-- chunk {"id": "body-0020", "role": "body", "section": "Input-state-output systems", "weight": 1.0} -->

For $k \geqslant {- 1}$, we define the *$k$-th observability matrix* by

<!-- chunk {"id": "body-0021", "role": "body", "section": "Input-state-output systems", "weight": 1.0} -->

and the *$k$-th Toeplitz matrix of Markov parameters* by

<!-- chunk {"id": "body-0022", "role": "body", "section": "Input-state-output systems", "weight": 1.0} -->

We denote the smallest integer $k \geqslant 0$ such that ${{rank}\Omega_{k}} = {{rank}\Omega_{k - 1}}$ by $\ell{(C,A)}$. Note that $0 \leqslant {\ell{(C,A)}} \leqslant n$ and if $n = 0$ then ${\ell{(C,A)}} = 0$. Moreover, if $(C,A)$ is observable, then $\ell{(C,A)}$ is the observability index of the pair. In the following we call $\ell{(C,A)}$ the *lag* of the system; for a justification of this terminology, see statements (iv) and (vii) of \[, Thm. 6\].

<!-- chunk {"id": "body-0023", "role": "body", "section": "Systems with $m$ inputs and $p$ outputs", "weight": 1.0} -->

We identify the system with the matrix $\begin{bmatrix}
\end{bmatrix}$. Given $m \geqslant 1$ and $p \geqslant 1$, we define the set of all systems with lag $\ell$ and $n$ states by

<!-- chunk {"id": "body-0024", "role": "body", "section": "Isomorphic systems", "weight": 1.0} -->

Two systems $\begin{bmatrix}
\end{bmatrix} \in {\mathcal{S}{(n)}}$ with $i \in {\lbrack 1,2\rbrack}$ are said to be isomorphic if $D_{1} = D_{2}$ and there exists a nonsingular matrix $S \in {\mathbb{R}}^{n \times n}$ such that $A_{1} = {S^{- 1}A_{2}S}$, $B_{1} = {S^{- 1}B_{2}}$, and $C_{1} = {C_{2}S}$. By extending this notion to a set of systems, we say that $\mathcal{S}^{\prime} \subseteq {\mathcal{S}{(n)}}$ has the isomorphism property if any pair of systems in $\mathcal{S}^{\prime}$ is isomorphic. By convention, the empty set has the isomorphism property.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Recap of the fundamental lemma and the high-level problem", "weight": 1.0} -->

In this section we recap the fundamental lemma and we sketch the problem of this paper at a high level. Let $m \geqslant 1$ and $p \geqslant 1$. Consider the linear discrete-time input-state-output system

<!-- chunk {"id": "body-0026", "role": "body", "section": "Recap of the fundamental lemma and the high-level problem", "weight": 1.0} -->

Throughout the paper, we assume that the true system is *minimal*, i.e. both observable and controllable. We also assume to know upper bounds on the true lag and true state-space dimension.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Recap of the fundamental lemma and the high-level problem", "weight": 1.0} -->

Let $t \geqslant 1$. Consider the input-output data $(u_{\lbrack 0,{t - 1}\rbrack},y_{\lbrack 0,{t - 1}\rbrack})$ generated by system during the time window $\lbrack 0,{t - 1}\rbrack$. In what follows, we state a reformulation of the fundamental lemma.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Informativity for system identification", "weight": 1.0} -->

In this section we recap the definition and characterization of informativity for system identification. Without making any a priori assumption on the input, let $(u_{\lbrack 0,{t - 1}\rbrack},y_{\lbrack 0,{t - 1}\rbrack})$ be data obtained. This means that there exists $x_{\lbrack 0,t\rbrack} \in {\mathbb{R}}^{n_{true} \times {({t + 1})}}$ such that

<!-- chunk {"id": "body-0029", "role": "body", "section": "Informativity for system identification", "weight": 1.0} -->

The set of all systems that explain the data $(u_{\lbrack 0,{t - 1}\rbrack},y_{\lbrack 0,{t - 1}\rbrack})$ is denoted by $\mathcal{E}_{t}$ and is referred to as the set of explaining systems. The subsets of $\mathcal{E}_{t}$ consisting of systems with a given lag and state space dimension are respectively defined as

<!-- chunk {"id": "body-0030", "role": "body", "section": "The shortest lag and minimum number of states", "weight": 1.0} -->

As proven, these integers admit a simple characterization in terms of the data. To explain this, let $k \in {\lbrack 0,{t - 1}\rbrack}$ and denote the Hankel matrix of $k + 1$ block rows constructed from the data $(u_{\lbrack 0,{t - 1}\rbrack},y_{\lbrack 0,{t - 1}\rbrack})$ by

<!-- chunk {"id": "body-0031", "role": "body", "section": "The shortest lag and minimum number of states", "weight": 1.0} -->

Note that $G_{k,t}$ may be obtained by removing the last row of outputs $y_{\lbrack k,{t - 1}\rbrack}$ from $H_{k,t}$. Now, define

<!-- chunk {"id": "body-0032", "role": "body", "section": "The shortest lag and minimum number of states", "weight": 1.0} -->

Throughout the paper, we assume that $u_{\lbrack 0,{t - 1}\rbrack} \neq 0_{m,t}$. From this blanket assumption, it follows that ${{rank}H_{{t - 1},t}} = {{rank}G_{{t - 1},t}} = 1$ and hence

<!-- chunk {"id": "body-0033", "role": "body", "section": "The shortest lag and minimum number of states", "weight": 1.0} -->

Let $q_{t} \in {\lbrack 0,{t - 1}\rbrack}$ be the smallest integer such that $\delta_{q_{t},t} = 0$. Note that $q_{t}$ is well-defined due to. The shortest lag and minimum number of states can be computed in terms of $\delta_{k,t}$ and $q_{t}$, as recalled next.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Necessary and sufficient conditions for informativity", "weight": 1.0} -->

We are now in a position to recall the conditions for informativity for system identification. Before we do so, we note that \[, Thms. 6(b) and 8\] shows that ${N - n_{\min,t}} + \ell_{\min,t}$ is an upper bound for the lag of any explaining system with at most $N$ states. This upper bound, which is determined by the data and $N$, is in some cases smaller than the given upper bound $L$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Necessary and sufficient conditions for informativity", "weight": 1.0} -->

The following theorem from \[, Thm. 9\] provides *necessary and sufficient* conditions for the data to be informative for system identification.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Formal problem statement", "weight": 1.0} -->

It follows from the lower bound (10a) that

<!-- chunk {"id": "body-0037", "role": "body", "section": "Formal problem statement", "weight": 1.0} -->

that is, any set of informative input-output data contains at least $T$ samples.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Formal problem statement", "weight": 1.0} -->

The main question is now as follows: can we design a sequence of inputs $u_{\lbrack 0,{T - 1}\rbrack}$ of length *precisely* $T$ such that the resulting input-output data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ are informative for system identification? We will focus on an *online* design of the inputs, in the sense that the choice of $u{(t)}$ is guided by the data $(u_{\lbrack{t - 1}\rbrack},y_{\lbrack 0,{t - 1}\rbrack})$ collected at previous time steps. We formalize the problem as follows.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Problem 1", "weight": 1.0} -->

For each $t = {0,1,\ldots,{T - 1}}$, given $(u_{\lbrack 0,{t - 1}\rbrack},y_{\lbrack 0,{t - 1}\rbrack})$, design $u{(t)}$ such that the resulting data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ are informative for system identification.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Problem 1", "weight": 1.0} -->

We note that the initial state $x_{0}$ of the system is arbitrary and not assumed to be given. Our goal is thus to design inputs that lead to an informative experiment *irrespective of $x_{0}$*.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Problem 1", "weight": 1.0} -->

In addition, we emphasize that it is not straightforward to see that Problem has a solution. In fact, even though $T$ is a lower bound on the number of data samples required for system identification, it is at this point unclear whether there *exists* an experiment of length exactly $T$. Also, even if such an experiment exists, it is far from obvious that there is a systematic way of *constructing* such an experiment without knowledge of the true system. An additional challenge is that the time $T$ itself depends on the true lag and true state-space dimension, which are *not a priori known*.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Problem 1", "weight": 1.0} -->

Remarkably, as we show in this paper, it turns out to be *always* possible to design an informative experiment of length precisely $T$, despite these challenges.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Online experiment design", "weight": 1.0} -->

In this section we present our main results, building up to the online experiment design method. We start with the following auxiliary lemma that asserts that the rank of the Hankel matrix $H_{k,t}$ can be increased at time $t + 1$, assuming that certain conditions are met.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Remark 9", "weight": 1.0} -->

Without going into details, we mention that Theorem shows that "randomly" chosen inputs $u_{\lbrack 0,{T - 1}\rbrack}$ lead to informative experiments of length precisely $T$ with high probability. In fact, the only imposed constraints on the inputs are that $u_{\lbrack 0,{m - 1}\rbrack}$ is nonsingular, and that ${u{(t)}} \in {\mathbb{R}}^{m}$ is not a member of an $({m - 1})$-dimensional affine set. Regardless of how the inputs are chosen to satisfy these constraints, however, a crucial aspect of OnlineExperiment$(L,N)$ is its stopping criterion. Indeed, we emphasize that $T$ is not a priori known but has to be deduced from data.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

In this section we illustrate OnlineExperiment$(L,N)$ by means of an example. Consider the true system

<!-- chunk {"id": "body-0046", "role": "body", "section": "Online experiment", "weight": 1.0} -->

We now apply OnlineExperiment$(L,N)$. We start with $k = 0$. We choose $u_{\lbrack 0,1\rbrack} = I$, which is obviously nonsingular, and measure

<!-- chunk {"id": "body-0047", "role": "body", "section": "Online experiment", "weight": 1.0} -->

Using these data and Proposition, we compute

<!-- chunk {"id": "body-0048", "role": "body", "section": "Online experiment", "weight": 1.0} -->

It can be checked that we have increased the rank of the depth-$1$ Hankel matrix from ${{rank}H_{1,3}} = 2$ to ${{rank}H_{1,8}} = 7$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Online experiment", "weight": 1.0} -->

Since $k \neq L_{8}^{a}$, we set $k = 2$. Following the while loop in Line, we construct

<!-- chunk {"id": "body-0050", "role": "body", "section": "Online experiment", "weight": 1.0} -->

By doing so, we have increased the rank of the depth-$2$ Hankel matrix from ${{rank}H_{2,9}} = 7$ to ${{rank}H_{2,11}} = 9$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Online experiment", "weight": 1.0} -->

Since $k \neq L_{11}^{a}$ we set $k = 3$. This time, we apply the while loop in Line to obtain the data

<!-- chunk {"id": "body-0052", "role": "body", "section": "Online experiment", "weight": 1.0} -->

The rank of the depth-$3$ Hankel matrix has increased from ${{rank}H_{3,12}} = 9$ to ${{rank}H_{3,14}} = 11$. Finally, we compute

<!-- chunk {"id": "body-0053", "role": "body", "section": "Online experiment", "weight": 1.0} -->

Since $k = L_{14}^{a}$, the procedure terminates. We conclude that $T = 14$ and the data $(u_{\lbrack 0,13\rbrack},y_{\lbrack 0,13\rbrack})$ are informative for system identification. For this example, we note that the required number of samples $T$ is less than the experiment design approach that works with the *fixed* depth $L = 4$ Hankel matrix. However, this is not always the case. For example, if we study the same example but with the given upper bounds $L = 3$ and $N = 6$, we can use OnlineExperiment$(L,N)$ to generate the same informative data, with the only difference that we now have $L_{2}^{a} = 3$. In this case, the number of $T = 14$ data samples is the same as.

<!-- chunk {"id": "body-0054", "role": "body", "section": "PE of order $L^{a} + 1$ is not sufficient for informativity", "weight": 1.0} -->

According to Theorem, an obvious necessary condition for informativity is that the inputs are *persistently exciting of order $L^{a} + 1$*. This condition, however, is not sufficient as demonstrated next. We use the same example as above, but just change $u{}$ from $\begin{bmatrix}
\end{bmatrix}$ to $\begin{bmatrix}
\end{bmatrix}$, i.e., we choose the inputs as

<!-- chunk {"id": "body-0055", "role": "body", "section": "PE of order $L^{a} + 1$ is not sufficient for informativity", "weight": 1.0} -->

The corresponding outputs are then given by

<!-- chunk {"id": "body-0056", "role": "body", "section": "PE of order $L^{a} + 1$ is not sufficient for informativity", "weight": 1.0} -->

In this case, ${{{rank}H_{3}}{(u_{\lbrack 0,13\rbrack})}} = 8$ so $u_{\lbrack 0,13\rbrack}$ is persistently exciting of order $L^{a} + 1$. However ${{rank}H_{3,14}} = 10 \neq 11$ so the conditions of Theorem are not satisfied.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Comparison to previous work", "weight": 1.0} -->

The proposed online experiment design method largely improves the (offline) persistency of excitation condition of the fundamental lemma. Indeed, recall that the input $u_{\lbrack 0,{t - 1}\rbrack}$ can only be *persistently exciting* of order $N + L + 1$ if $t \geqslant {N + L + {m{({N + L + 1})}}}$. In general, this lower bound on the number of data samples is much larger than $T$. For example, if $m = 80$, $p = 10$, $\ell_{true} = 20$, $n_{true} = 100$, $L = 100$ and $N = 150$, the online experiment design method requires $T = 5850$ samples whereas persistency of excitation requires $t \geqslant 20330$ samples.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Comparison to previous work", "weight": 1.0} -->

The proposed approach also improves the online experiment design of. In fact, in the latter paper a method was given to guarantee that the Hankel matrix $H_{L}$ of *fixed depth* $L$ has rank ${{({L + 1})}m} + n_{true}$. This was done in the least possible number of time steps, $t = {L + {{({L + 1})}m} + n_{true}}$. However, by Theorem, the condition ${{rank}H_{L}} = {{{({L + 1})}m} + n_{true}}$ is sufficient for informativity for system identification, but in general not necessary. In particular, if $L^{a} < L$ then the experiment design method of this paper leads to a shorter experiment for system identification than the one provided. If $L^{a} = L$, then the number of samples coincides.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In this paper we have proposed an experiment design method that leads to input-output data that are informative for system identification. The key features of the approach are i) it is *online*, meaning that the design of the inputs is guided by data collected at previous time steps, and ii) it *adapts the depth* of the input-output Hankel matrix during the operation of the algorithm. We have shown that this approach leads to informative sequences of input-output samples of the shortest possible length. Interestingly, the exact number of samples in such a shortest experiment cannot be determined a priori, but is only revealed after the termination of the procedure. The online experiment design method improves over methods based on persistent excitation by significantly reducing the required number of data samples for system identification. The results of this paper have also revealed that the online experiment design method of yields the shortest experiment for system identification only in *some* cases. In situations where the data-based bound on the lag of the system is smaller than the a priori given bound, the experiment design method of this paper outperforms.
