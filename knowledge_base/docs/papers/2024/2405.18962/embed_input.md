<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Beyond the Fundamental Lemma: From Finite Time Series to Linear System

Topics include Behavioral systems, System identification, Fundamental lemma, Linear systems, Finite time series, Minimal realization, Lag bounds, Input-output data.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Revisits what can be identified from finite input-output time series beyond the trajectory-spanning statement of the fundamental lemma. The paper gives exact identifiability conditions and dimension/lag bounds, making it a more system-identification-oriented complement to direct control results.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We state necessary and sufficient conditions to uniquely identify (modulo state isomorphism) a linear time-invariant minimal input-state-output system from finite input-output data and upper- and lower bounds on lag and state space dimension.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Background. J.C. Willems' trilogy is one of broader, deeper, and more influential studies about mathematical modelling of dynamical systems from time series. The second part concerns the problem of obtaining a mathematical model for a linear system from a given (infinite) trajectory. It significantly influenced subspace identification methods, that compute a state sequence from finite-length data by adapting Willems' state construction from infinite- to finite-length data. Two assumptions are crucial: the state space dimension of the system is known; and a rank condition holds for a Hankel matrix constructed from the data. Although not formally proven at the time, it was believed that such rank condition is satisfied if the input data are sufficiently persistently exciting. This conjecture was formally proven in Willems et. al.'s *fundamental lemma* which allows the application of subspace identification even when only an upper bound on the state dimension is known.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The fundamental lemma parameterizes all trajectories of a system from a single sufficiently informative one. This parameterization was applied in linear quadratic control, simulation, model reduction of dissipative systems, and predictive control. More recently, this approach has gained significant momentum, initiated by papers such as and followed by many contributions addressing a variety of data-driven analysis and control problems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The recent surge in popularity of this parameterization has also revived the interest in the fundamental lemma itself. Its original proof was presented in the language of behavioral systems; an alternative proof for state space systems was provided. The original proof and that are by contradiction; a direct proof was presented for single-input systems. Generalizations to uncontrollable systems are in and extensions to continuous-time systems. Quantitative/robust variations are explored, frequency domain formulations, and online experiment design. Furthermore, the fundamental lemma has been generalized beyond linear systems to include various other model classes: descriptor systems, flat nonlinear systems, linear parameter-varying systems, and stochastic ones.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions. The fundamental lemma gives a *sufficient* condition for identifiability (in the sense of ); in this paper we investigate necessary and sufficient conditions on finite input-output data for identifiability of an unknown minimal input-state-output (ISO) system whose lag and state space dimension lie between given lower and upper bounds.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Using the concept of *data informativity* (see ), we develop a framework for ISO system identification from finite input-output data, incorporating a priori knowledge or assumptions. While currently limited to exact (deterministic) identification problems, such framework is of broader potential interest, for example in approximate modelling and for noisy data.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We characterize the shortest lag $\ell_{\min}$ and the minimum number of states $n_{\min}$, that an ISO system capable of generating the data must have. These integers can be computed *directly from the data*.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We compute an ISO system whose lag and state dimension are exactly $\ell_{\min}$ and $n_{\min}$ using a novel construction of a state trajectory from data that does not rely on assumptions on the length of the data set.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We establish an inequality (see ) relating the lag and state dimension of any data-generating system to $\ell_{\min}$ and $n_{\min}$. With such inequality we compute a sharper upper bound on the lag than the one given a priori.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Assuming a priori knowledge about minimality and lower and upper bounds on lag and state dimension, we state *necessary and sufficient* conditions on finite input-output data to guarantee unique identification modulo state isomorphism. Such conditions are formulated in terms of the rank of a Hankel matrix constructed from the input-output data, whose depth is determined by the input-output data themselves.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Relation with previous results. As in deterministic subspace identification methods (see ), our approach is also based on directly computing a state trajectory from input-output data. Our procedure is also related to the intersection of "past" and "future" crucial in subspace identification. The issues arising when working with *finite-length* data, however, seem to have been only touched upon in the subspace literature (see \[, p. 34\] and before the statement \[, Thm. 2\]). It is assumed that the data length is "sufficiently large" to guarantee that the data Hankel matrix contains enough information on the dynamics of an explaining model, but a *complete* characterization of such property such as given in the present paper is absent.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our approach is conceptually and methodologically closest to the behavioral one (see ). Instrumental to our results is the definition of a number of integer invariants computed directly from the data and associated with explaining models. Such integers are the finite data counterparts of those introduced in \[, Sect. 7\] for infinite time series. Moreover, the fundamental lemma is a *special case* of our results (see Proposition, Theorem, and Section 9.2), and we show that one can identify the unknown system under weaker conditions. Finally, we essentially improve the fundamental lemma as follows. Identification based on the fundamental lemma is offline: a sufficiently rich input signal is applied, the corresponding output response is measured, and then identification or trajectory-parametrization is performed. Such offline method does not exploit in *real-time* information from the output samples. In we use our approach to devise a shortest online experiment for linear system identification. Input values are chosen depending on the past input-output data and are applied *step-by-step*. Such online method requires less data points than the offline one, and it could pave the way to design plug-and-play data-driven controllers.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

The authors of study identifiability from multiple finite-length trajectories without assumptions on the input-output structure. The first similarity with our approach lies in the adoption of the "model class" concept; such class is associated with the *complexity* of a model. A second similarity lies in the sequential construction of left-annihilators of finite Hankel data matrices, although an autoregressive model is computed and we compute an ISO one instead. A fundamental difference is that to compute such annihilators only data Hankel matrices with at least as many columns as rows are used (see the definition of $L_{\max}$ on p. 3 therein); our informativity point of view instead allows us to exploit Hankel matrices of *full depth* in constructing a state sequence compatible with the data. Moreover, the identifiability characterization in \[, Theorem 17\] is based on a priori knowledge of lag and state dimension (see also Note 18 *ibid.*); ours depends on integers computed *only* and *directly* from the data.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Structure of the paper. In Section, we introduce notation, preliminary concepts and definitions. In Section we formalize the problem. Section contains a summary of our most relevant results and an outline of the logical links among them. In Section we illustrate such results on an example.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our main result is Theorem to whose proof, based on some intermediate results of independent interest, we devote the rest of the manuscript. In Section we introduce and study lag structures of explaning systems. Section contains a new iterative state construction from input-output data, from which an explaining system is straightforwardly derived. State-input data Hankel matrices and their properties are studied in Section. In Section we present two ways of constructing an explaining system from a given one. We discuss future work in Section.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Vectors and matrices", "weight": 1.0} -->

The space of $n$-dimensional real vectors is denoted by ${\mathbb{R}}^{n}$; the space of $n \times m$ matrices with real entries by ${\mathbb{R}}^{n \times m}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Vectors and matrices", "weight": 1.0} -->

We denote the $n \times n$ identity matrix by $I_{n}$ and the $m \times n$ zero matrix by $0_{m,n}$ whereas $0_{n}$ denotes the $n$-vector of zeros. For partitioned matrices containing zero and/or identity submatrices, we do not explicitly indicate the sizes of blocks that can be deduced from the matrix structure.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Void matrices", "weight": 1.0} -->

A void matrix is a matrix with zero rows and/or zero columns. We denote by $0_{n,0}$ and $0_{0,m}$ respectively the $n \times 0$ and $0 \times m$ void matrices. If $M$ and $N$ are, respectively $p \times q$ and $q \times r$ matrices, $MN$ is a $p \times r$ void matrix if $p = 0$ or $r = 0$ and ${MN} = 0_{p,r}$ if ${p,r} \geqslant 1$ and $q = 0$. The rank of a void matrix is defined to be zero.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Integer intervals and Hankel matrices", "weight": 1.0} -->

The set of integers is denoted by $\mathbb{Z}$ and the set of nonnegative integers by $\mathbb{N}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Integer intervals and Hankel matrices", "weight": 1.0} -->

Given ${i,j} \in {\mathbb{Z}}$ with $i \leqslant j$, we write $\lbrack i,j\rbrack$ to denote the ordered set of all integers between $i$ and $j$ both included. By convention, ${\lbrack i,j\rbrack} = \varnothing$ if $i > j$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Input-state-output systems", "weight": 1.0} -->

We work with linear discrete-time ISO systems

<!-- chunk {"id": "body-0024", "role": "body", "section": "Input-state-output systems", "weight": 1.0} -->

For $k \geqslant {- 1}$, we define the *$k$-th observability matrix* by

<!-- chunk {"id": "body-0025", "role": "body", "section": "Input-state-output systems", "weight": 1.0} -->

We denote the smallest integer $k \geqslant 0$ such that ${{rank}\Omega_{k}} = {{rank}\Omega_{k - 1}}$ by $\ell{(C,A)}$. Note that $0 \leqslant {\ell{(C,A)}} \leqslant n$; if $n = 0$, then ${\ell{(C,A)}} = 0$. If $(C,A)$ is observable, then $\ell{(C,A)}$ is the observability index. We call $\ell{(C,A)}$ the *lag* of the system; on this terminology, see statement (vii) of \[, Thm. 6\].

<!-- chunk {"id": "body-0026", "role": "body", "section": "Systems with $m$ inputs and $p$ outputs", "weight": 1.0} -->

We associate with the matrix $\begin{bmatrix}
\end{bmatrix}$. Given $m \geqslant 1$ and $p \geqslant 1$, we denote the set of all systems with lag $\ell$ and $n$ state variables by

<!-- chunk {"id": "body-0027", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Consider a linear discrete-time input-state-output system

<!-- chunk {"id": "body-0028", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

A fundamental problem in system identification is under what conditions and how the system can be uniquely determined from $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ (up to state isomorphisms). In this paper we examine such questions assuming prior knowledge about the unknown system. To formalize such problem we need to introduce some terminology and notation.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Explaining systems", "weight": 1.0} -->

The set of all systems that explain the data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ is denoted by $\mathcal{E}$ and is called the set of explaining systems. The subsets of $\mathcal{E}$ consisting of systems with a given lag and state space dimension are denoted by

<!-- chunk {"id": "body-0030", "role": "body", "section": "Explaining systems", "weight": 1.0} -->

It is straightforward to verify that $\mathcal{E}{(\ell,n)}$ and $\mathcal{E}{(n)}$ are invariant under state space transformations. In addition, it follows from that $\begin{bmatrix}
\end{bmatrix} \in {\mathcal{E}{(\ell_{true},n_{true})}} \subseteq {\mathcal{E}{(n_{true})}}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Informativity for system identification", "weight": 1.0} -->

The available prior knowledge is formalized through a subclass of systems $\mathcal{S}_{pk} \subseteq \mathcal{S}$ (with $\begin{bmatrix}
\end{bmatrix} \in \mathcal{S}_{pk}$), that encapsulates what is known a priori about the true system.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Problem 3", "weight": 1.0} -->

Given $T > 0$; $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ generated by a system; ${L_{-},L_{+},N_{-},N_{+}} \in {\mathbb{N}}$ satisfying; the model class $\mathcal{S}_{pk}$, establish necessary and sufficient conditions for informativity for system identification within $\mathcal{S}_{pk}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Main results", "weight": 1.0} -->

Informativity for system identification within is related to the rank of a Hankel matrix constructed from the data. We show that the depth of such Hankel matrix is determined by the data and by the bounds $L_{+}$ and $N_{+}$. To state such condition we need to introduce some more notation and terminology.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Data Hankel matrices", "weight": 1.0} -->

Throughout the paper, we assume that

<!-- chunk {"id": "body-0035", "role": "body", "section": "Lags and state dimensions of explaining systems", "weight": 1.0} -->

Note that $q$ is well-defined due to. In our first intermediate result we establish bounds on the lag and state dimension of any explaining system in terms of the $\delta_{k}$'s.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Constructing an explaining system", "weight": 1.0} -->

Our second intermediate result concerns whether one explaining system can be computed from the data. To answer such question, we introduce the notion of state for data.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Constructing an explaining system", "weight": 1.0} -->

From, it follows that $x_{\lbrack 0,T\rbrack}$ is a state for the data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ if and only if

<!-- chunk {"id": "body-0038", "role": "body", "section": "Constructing an explaining system", "weight": 1.0} -->

Consequently if one state sequence satisfying is available, one explaining system can be computed by solving. In the next result we show that for any data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ there always exists an explaining system with state dimension $\sum_{i = 0}^{q}\delta_{i}$, and that *all* such systems have lag $q$ (see ).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Sharpening the upper bound on the true lag", "weight": 1.0} -->

Assume that ${\mathcal{E}{(\ell,n)}} \neq \varnothing$; from Theorems.(b) ‣ Theorem 6. ‣ 4.2 Lags and state dimensions of explaining systems ‣ 4 Main results ‣ Beyond the fundamental lemma: from finite time series to linear system") and we obtain the immediate but crucial inequality

<!-- chunk {"id": "body-0040", "role": "body", "section": "Sharpening the upper bound on the true lag", "weight": 1.0} -->

Such inequality implies that the integer $L_{+}^{d}$ defined by

<!-- chunk {"id": "body-0041", "role": "body", "section": "Sharpening the upper bound on the true lag", "weight": 1.0} -->

is an upper bound, purely determined by the data and $N_{+}$, for the lag of every explaining system with at most $N_{+}$ states. Such upper bound yields a sharper upper bound on the lag than $L_{+}$; we can replace the latter by the actual upper bound

<!-- chunk {"id": "body-0042", "role": "body", "section": "Data informativity for system identification", "weight": 1.0} -->

The following is the main result of this paper; sufficiency is proved in Section 8.2 and necessity in Section 9.1.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 10", "weight": 1.0} -->

It is not surprising that informativity for system identification involves a rank condition on some Hankel matrix of the data. Theorem makes explicit that the depth of such Hankel matrix depends not only on the prior knowledge of the system but also on the given data. ∎

<!-- chunk {"id": "body-0044", "role": "body", "section": "Remark 11", "weight": 1.0} -->

Theorem is applicable even if one of the upper bounds is unknown. Indeed, if only the upper bound $L_{+}$ on the lag is known, but an upper bound $N_{+}$ on the state dimension is not, one can fix $N_{+} = {pL_{+}}$ since $n \leqslant {p\ell}$ for any observable system in $\mathcal{S}{(\ell,n)}$. For such choice it holds that

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 11", "weight": 1.0} -->

Conversely, if an upper bound $N_{+}$ on the state dimension is known but an upper bound $L_{+}$ on the lag is not, one can fix $L_{+} = N_{+}$ since the lag of a system cannot exceed its state dimension. For such choice of $L_{+}$ it holds that

<!-- chunk {"id": "body-0046", "role": "body", "section": "Remark 12", "weight": 1.0} -->

If $L_{-} = L_{+} = \ell_{true}$ and $L_{+} = N_{+} = n_{true}$ then it is straightforward to see that Proposition is a special case of Theorem (see Section 3.3). It is less straightforward to prove that the rank condition in Proposition implies the conditions in Theorem; we do this in Section 9.2. ∎

<!-- chunk {"id": "body-0047", "role": "body", "section": "Remark 13", "weight": 1.0} -->

Proposition can be applied only if the data length is at least ${L_{+} + N_{+} + {{({L_{+} + N_{+}})}m}} - 1$ whereas Theorem can be applied if the data length is at least $L_{+}^{a} + {{({L_{+}^{a} + 1})}m} + n_{true}$. As illustrated in Section, the difference between these lengths can be significantly large. ∎

<!-- chunk {"id": "body-0048", "role": "body", "section": "Remark 14", "weight": 1.0} -->

Theorem is important for online experiment design. Assume that $\ell_{true} \geqslant 1$ and that only an upper bound $L_{+}$ is known; the procedure in \[, Thm. 3\] constructs a sequence $u_{\lbrack 0,{T - 1}\rbrack}$ with $T = {{{({L_{+} + 1})}m} + L_{+} + n_{true}}$ such that the data $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ generated by the true system are informative for system identification in $\mathcal{S}_{{\lbrack 1,L_{+}\rbrack},{\lbrack 1,{pL_{+}}\rbrack}} \cap \mathcal{M}$. Surprisingly, the procedure does not require knowledge of $n_{true}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Remark 14", "weight": 1.0} -->

For this case $L_{+}^{a} = L_{+}$. If $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ are informative for system identification in $\mathcal{S}_{{\lbrack 1,L_{+}\rbrack},{\lbrack 1,{pL_{+}}\rbrack}} \cap \mathcal{M}$, then from (19d) and (20b) that $T \geqslant {{{({L_{+} + 1})}m} + L_{+} + n_{true}}$. Thus the experiment design procedure in \[, Thm. 3\] is minimal in the number of samples required. ∎

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 15", "weight": 1.0} -->

The constructive proof of Theorem and (20c) can be used to compute from informative data an explaining system isomorphic to the true system. We show this in Example. ‣ 7.2 Proof of Theorem 7 ‣ 7 State construction ‣ Beyond the fundamental lemma: from finite time series to linear system") after the proof of Theorem. ∎

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 16", "weight": 1.0} -->

Before proving Theorems, and we illustrate them with an example.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

Consider a system where $n_{true} = 3$, $m = 2$, $p = 2$, and

<!-- chunk {"id": "body-0053", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

Note that $\ell_{true} = 2$. Consider the input-output data

<!-- chunk {"id": "body-0054", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

One can verify that is satisfied with the state data

<!-- chunk {"id": "body-0055", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

Table presents the values of $\delta_{k}$ integers, $\ell_{\min}$, and $n_{\min}$ for different choices of $T$. The values of $\delta_{k}$ not explicitly indicated are zero: $\delta_{k} = 0$ for every $T \in {\lbrack 4,14\rbrack}$ and $k \in {\lbrack 3,{T - 1}\rbrack}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

If $L_{+} = \ell_{true}$ and $N_{+} = n_{true}$, a necessary condition for informativity is that $T \geqslant {{{({\ell_{true} + 1})}m} + \ell_{true} + n_{true}}$ (see (19c)). It follows that if $T < 11$ then $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ is not informative for every $L_{+}$ and $N_{+}$. The symbol '✓' in Table denotes data informativity for different values of $L_{+}$, $N_{+}$, and $T$, as inferred from the fundamental lemma and Theorem.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

Proposition requires significantly more samples than Theorem: the data $(u_{\lbrack 0,13\rbrack},y_{\lbrack 0,13\rbrack})$ are informative for the case $L_{+} = N_{+} = 4$. To infer informativity via the fundamental lemma, one would need at least ${{L_{+} + N_{+} + {{({L_{+} + N_{+}})}m}} - 1} = 23$ samples.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Lag structures of explaining systems", "weight": 1.0} -->

To prove Theorem, we first define the lag structure and relate it to the integers $\delta_{k}$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "The lag structure of a system", "weight": 1.0} -->

We refer to the sequence ${(\rho_{k})}_{k \in {\mathbb{N}}}$ as the lag structure of the system $\begin{bmatrix}
\end{bmatrix}$. The $\rho_{k}$'s are related to a *specific* system; if necessary to resolve ambiguities, we use the notation $\rho_{k}{(C,A)}$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Lag structures and $\\delta_{k}$ integers", "weight": 1.0} -->

Let $\begin{bmatrix}
\end{bmatrix} \in {\mathcal{S}{(n)}}$. For $k \geqslant {- 1}$, define the *$k$-th controllability matrix*, and the *$k$-th system matrix*, respectively, by

<!-- chunk {"id": "body-0061", "role": "body", "section": "Lag structures and $\\delta_{k}$ integers", "weight": 1.0} -->

$\Theta_{k}$ is the Toeplitz matrix of the first $k + 1$ Markov parameters of.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Lag structures and $\\delta_{k}$ integers", "weight": 1.0} -->

We now relate the integers $\delta_{k}$ (defined in terms of the *data matrices* $H_{k}$ and $G_{k}$ only) and the integers $\rho_{k}$ (defined by the matrices $C$ and $A$ of a *specific explaining system*).

<!-- chunk {"id": "body-0063", "role": "body", "section": "State construction", "weight": 1.0} -->

In this section, we present a new iterative state construction procedure from data instrumental in proving Theorem.

<!-- chunk {"id": "body-0064", "role": "body", "section": "On the left kernels of data Hankel matrices", "weight": 1.0} -->

for all $k \in {\lbrack 0,{T - 1}\rbrack}$. From the definition of $\sigma$ and the Hankel structure it follows that if $T \geqslant 2$, then for all $k \in {\lbrack 0,{T - 2}\rbrack}$

<!-- chunk {"id": "body-0065", "role": "body", "section": "On the left kernels of data Hankel matrices", "weight": 1.0} -->

The following result shows that ${lker}H_{k}$ can be written into a direct sum of ${{lker}G_{k}} \times {\{ 0\}}^{p}$ and shifts of certain subspaces.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Example 20 (State construction)", "weight": 1.0} -->

We compute a state for the data in Section and the values $T = 5$ and $T = 14$ following the procedure in the proof of Theorem.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Example 20 (State construction)", "weight": 1.0} -->

In view of -, these choices yield the state

<!-- chunk {"id": "body-0068", "role": "body", "section": "Example 20 (State construction)", "weight": 1.0} -->

Evidently $(u_{\lbrack 0,4\rbrack},y_{\lbrack 0,4\rbrack})$ are not informative for system identification: they are explained by a minimal system with 2 states.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Example 20 (State construction)", "weight": 1.0} -->

For $T = 14$, $\delta_{- 1} = \delta_{0} = 2$, $\delta_{1} = 1$, and $\delta_{k} = 0$ for $k \in {\lbrack 2,13\rbrack}$ (see Table in Section ). Moreover, $(u_{\lbrack 0,13\rbrack},y_{\lbrack 0,13\rbrack})$ are informative for system identification for all values of $L_{+}$ and $N_{+}$ in Table. As such, we can use Theorem to identify an isomorphic system to the true one. We first apply Lemma and conclude that ${\dim\mathcal{S}_{0}} = 0$, ${\dim\mathcal{S}_{1}} = 1$, and ${\dim\mathcal{S}_{2}} = 1$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Example 20 (State construction)", "weight": 1.0} -->

In view of -, these choices yield the state

<!-- chunk {"id": "body-0071", "role": "body", "section": "Example 20 (State construction)", "weight": 1.0} -->

Solving we obtain the explaining system

<!-- chunk {"id": "body-0072", "role": "body", "section": "Example 20 (State construction)", "weight": 1.0} -->

that is isomorphic to the true system.

<!-- chunk {"id": "body-0073", "role": "body", "section": "State-input data Hankel matrices", "weight": 1.0} -->

To prove the sufficiency part of Theorem we need auxiliary results on the ranks of state-input data Hankel matrices.

<!-- chunk {"id": "body-0074", "role": "body", "section": "On the ranks of state-input data Hankel matrices", "weight": 1.0} -->

for $k \in {\lbrack 0,{T - 1}\rbrack}$. Given the structure of $J_{k}$ we conclude that

<!-- chunk {"id": "body-0075", "role": "body", "section": "From one explaining system to another", "weight": 1.0} -->

To prove necessity in Theorem, we present two ways of computing explaining systems. The first one constructs an explaining system with $n$ states from a given one with $n$ states.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Example 25", "weight": 1.0} -->

We illustrate Lemma with the data in Section. Consider the explaining system ) for $(u_{\lbrack 0,4\rbrack},y_{\lbrack 0,4\rbrack})$. Note that is satisfied with $\xi = \begin{bmatrix}
\end{bmatrix}$, $\eta_{0} = \begin{bmatrix}
\end{bmatrix}$, and $\eta_{1} = \begin{bmatrix}
\end{bmatrix}$. Since $\ell = 1$ for ), $\zeta = {{col}{}}$ satisfies. Applying Lemma, we obtain the explaining system

<!-- chunk {"id": "body-0077", "role": "body", "section": "Example 25", "weight": 1.0} -->

with state $x_{\lbrack 0,5\rbrack} = \left. \lbrack\begin{array}{rrrrrr}
\end{array} \right\rbrack$. ∎

<!-- chunk {"id": "body-0078", "role": "body", "section": "Example 25", "weight": 1.0} -->

Using Lemma, we state a necessary condition for the isomorphism property.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We stated necessary and sufficient conditions for informativity for system identification in the class of minimal ISO systems whose lag and state dimension lie between given lower/upper bounds. To establish such result we obtained some intermediate ones of independent interest, most prominently the iterative construction of a state sequence and a corresponding ISO model in the proof of Theorem.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We aim to apply the concept of informativity for system identification in a model class to other classes than minimal systems, e.g. to dissipative systems. We also plan to work on the application of the informativity concept to identification in the behavioral framework, where interesting results have recently appeared.
