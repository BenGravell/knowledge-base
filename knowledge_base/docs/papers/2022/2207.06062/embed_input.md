<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Provably Stable Learning Control of Linear Dynamics with Multiplicative Noise

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Control of linear dynamics with multiplicative noise naturally introduces robustness against dynamical uncertainty. Moreover, many physical systems are subject to multiplicative disturbances. In this work we show how these dynamics can be identified from state trajectories. The least-squares scheme enables exploitation of prior information and comes with practical data-driven confidence bounds and sample complexity guarantees. We complement this scheme with an associated control synthesis procedure for LQR which robustifies against distributional uncertainty, guaranteeing stability with high probability and converging to the true optimum at a rate inversely proportional with the sample count. Throughout we exploit the underlying multi-linear problem structure through tensor algebra and completely positive operators. The scheme is validated through numerical experiments.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently the control community has gained renewed interest in learning control [Recht2018]. This can be viewed as a reaction to the practical success of machine learning specifically Reinforcement Learning (RL) when applied to control dynamical systems. An opportunity arises there in the lack of theoretical guarantees, particularly related to reliability and safety. On that regard, control theory has much to offer [Recht2018, Hewing2020d]. *This work focuses on stability specifically.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

One approach towards learning with guarantees *is to focus on specific classes of dynamics. The Linear Quadratic Regulator (LQR) [Bertsekas2005V1] has proven a valuable subject for such investigations. We categorize two approaches: *the model-free approach takes a RL algorithm and applies it to LQR, proving convergence, stability, etc. [Fazel2018, Bradtke1994, Lewis2009]; *and the model-based approach develops learning control schemes specialized to LQR with guarantees [Dean2019,Mania2019,Abeille2020].

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

*The latter, model-based approach [Astrom2008], [Ljung1999], [Bertsekas2005V1], *involves first identifying the dynamics before synthesizing a controller. As suggested in [Recht2018] under the term coarse-id learning, *integrating model-based approaches with statistical learning theory yields verifiably safe controllers [Dean2019]. We also present such a coarse-id method here.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

*we present a distributionally robust (DR) generalization of this coarse-id framework for deterministic LQR, tailored to linear dynamics with multiplicative noise. It incorporates a least-squares estimator of the dynamics paired with tight error bounds and accompanied by a control synthesis scheme. *In this manner, we expand upon our prior work [Coppens2019]and interpolate between robust and stochastic control, becoming less conservative as data is gathered while guaranteeing stability with high probability.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

LQR under multiplicative noise was first considered by Wonham [Wonham1967], who developed a generalized Riccati equation. Similarly many recent developments in learning LQR are generalizable to multiplicative noise [Wang2018,Gravell2019,Pang2021,Coppens2019]. This is interesting for two reasons.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

*multiplicative noise affects numerous real-world systems. These models occur frequently when disturbances enter a model through the parameters (e.g. through vibrations, nonlinear effects in spring systems, thermal and aerodynamic influences, etc.). A list of examples with references is provided in [Damm2004] with concrete applications in aerospace and vehicle control. Multiplicative noise has also been observed in biological applications like sensorimotor control [Todorov2002,Todorov2005], cell populations [Russo2018, Mohler1980a], population migration [Mohler1980a] and immune systems [Mohler1980b]. Other applications include nuclear fission [Mohler1980a], power grids [Afshari2020], communication channels [Wang2002], *electrical networks, sampled data feedback and climate models [Sura2005].

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second, the use of multiplicative noise induces robustness against parametric uncertainty. In this is motivated by the lack of stability margins in output-feedback LQG [Doyle1978]. This same fact was argued in a historical review by J. Doyle [Doyle1996] to have motivated the development of $\set{H}_{\infty}$ methods. In fact, as we formalize later, there is a strong relation between mean square stability (MSS) for multiplicative noise systems and robust stability [Bernstein1987,Gravell2020,Pascoe2019].

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Next, we provide a detailed overview of related work.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contributions", "weight": 1.0} -->

The main contributions of this work are as follows.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Contributions", "weight": 1.0} -->

- We show how linear quadratic (LQ) control of multiplicative noise is equivalent to LQ control of CP dynamics; - We consider an identification procedure that can both include prior knowledge about the dynamics and also performs well in the model-free setting. The optimal estimate is accompanied with a tight confidence set; - We introduce a synthesis procedure for DR LQR; - We analyze the sample complexity of the scheme.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Contributions", "weight": 1.0} -->

As mentioned above, CP operators have been applied in multiplicative noise before [Damm2003]. A formal equivalence of LQ control has not been shown however. The other results all strongly rely on this equivalence.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Contributions", "weight": 1.0} -->

*The system identification problem solved in item:id was previously considered. However, their confidence bound is too conservative for practical purposes and there is no possibility to include prior information about how the uncertainty enters into the dynamics. Particularly, when using longer trajectories in the data, their bound grows when more data is gathered, which is opposite to the behavior observed in experiments (cf. fig:toy-rollout and). Furthermore, unlike our bound in thm:error-bound-full, their bound is not data-driven. It instead depends on unknown system constants." ambiguity set is derived, but the full system dynamics are never identified. We consider item:idas the most We also generalize our previous work to the model-free setting: item:l4dc extends upon [Coppens2019] and item:cdc extends upon [Coppens2020], and applies the result to the DR control synthesis procedure.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Contributions", "weight": 1.0} -->

*Numerical experiments demonstrate practical applicability.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Contributions", "weight": 1.0} -->

The remainder of this paper describes the construction, solution and analysis of DR control for LQR under multiplicative noise. We provide a problem statement in sec:problem and preliminary results in sec:preliminary. We then consider the nominal case for LQR under multiplicative noise, when the dynamics are known. Next, in sec:construction, we describe an ambiguity set based on state measurements; in sec:synthesis we solve the resulting DR problem; and in sec:analysis we study convergence of the solution to the nominal controller as more data is gathered. Then we show how to add more prior information to the model related to a deterministic term in sec:structural. We end the paper with numerical results in sec:numerical and a conclusion in sec:conclusion.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Contributions", "weight": 1.0} -->

This paper is accompanied by a technical report including more detailed proofs, experiments and a section on including a deterministic term in the prior model structure.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem statement", "weight": 1.0} -->

In this work we consider linear systems with input- and state-multiplicative noise given for all $t \in \N$ as where $x_t \in \Re^{n_x}$ is the state, $u_t \in \Re^{n_u}$ the input and $v_t \in \Re^{n_v}$ is the disturbance, which follows an i.i.d. random process. The matrices are given by $A(v) \dfn \sum_{i=1}^{n_v} [v]_i A_i$ and $B(v) \dfn \sum_{i=1}^{n_v} [v]_i B_i$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem statement", "weight": 1.0} -->

The primary goal is to study solutions of the following stochastic LQR problem: &\minimize_{u_0, u_1, \dots} && \E\left[\sum_{t=0}^\infty \trans{x}_t Q x_t + \trans{u}_t R u_t \right], \end{aligned} \tag{$\mathcal{LQR}_\star$}$$ subject to [eq:dyn], for given $x_0$ and $Q \sgt 0$ and $R \sgt 0$ These assumptions are not necessary for solvability, yet are added here for convenience.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem statement", "weight": 1.0} -->

In practical applications the dynamics [eq:dyn] are often unknown. Hence we introduce a system identification scheme to estimate [eq:dyn], supporting both the setting where the modes $A_i$, $B_i$ are unknown and the setting where they are (partially) known. This information will be encoded through the use of a model tensor $\ten{M}$ described in sec:multiplicative.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem statement", "weight": 1.0} -->

Besides the modes, characterizing the distribution of $v_t$ is a more considerable challenge. We however are aided by the following fact. By linearity, the cost of [eq:slqr] only involves second moments of the states $X_t = \E[x_t \trans{x_t}]$ and the inputs $U_t = \E[u_t \trans{u_t}]$. In this work we thus tackle LQR in terms of the moment dynamics: $$X_{t+1} = \op{E}(Z_t), \quad \text{with } Z_t = \E[z_t \trans{z_t}],$$ for augmented state $z_t = (x_t, u_t) \in \Re^{n_z}$. These dynamics are easier to estimate, compared to [eq:dyn], yet contain all information required to solve the stochastic LQR problem.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem statement", "weight": 1.0} -->

We view [eq:dynsm] as an implicit definition for the operator $\op{E}$ *the explicit definition being eq:dynsm\_ and argue in sec:multiplicative how the fundamental operator $\op{E}$ (i) is linear in $Z_t$, characterizing its matrix $\opm{E}$ in terms of the quantities [eq:dyn], (ii) is completely positive (CP) *(cf. def:cpop and lem:tencp), (iii) has a bilinear structure since $\opm{E}$ depends linearly on $V = \E[v_t \trans{v_t}]$. These properties serve as a central theme of this work.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Problem statement", "weight": 1.0} -->

Since we will never get a completely accurate estimate of the distribution it makes sense in safety critical scenarios to use data to construct a set of likely distributions $\amb$ containing the true distribution with high probability (see the formal setup in [Coppens2021]). Given $\amb$ we then solve the DR LQR problem: &\minimize_{u_0, u_1, \dots} &\, & \maximize_{\nu \in \amb} &\,\,& \E_{\nu}\left[\sum_{t=0}^\infty \trans{x}_t Q x_t + \trans{u}_t R u_t \right], \end{alignedat} \tag{$\bar{\mathcal{LQR}}$}$$ which upper bounds the cost of [eq:slqr] with high probability. In this work, only the second moment $V = \E[v_t \trans{v_t}]$affects the problem. So we formulate the ambiguity set over moments.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Preliminary results", "weight": 1.0} -->

We introduce the main tools used throughout our work here. Specifically this section presents operators over the space of symmetric matrices in sec:operators and tensor algebra

<!-- chunk {"id": "body-0025", "role": "body", "section": "Operators over symmetric matrices", "weight": 1.0} -->

As argued later, the second moment of the disturbance $v$is identified by solving a linear system of equations, where the variable of interest is a symmetric matrix.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Operators over symmetric matrices", "weight": 1.0} -->

Useful tools when dealing with such problems are the Kronecker product $\otimes$ [Horn1991], the vector operator $\vec(\cdot)$ [Horn1991] and its inverse $\unvec(\cdot)$. These are connected through the fundamental property [Horn1991] $$\vec(U X \trans{V}) = (V \otimes U) \vec(X),$$ for any $U \in \Re^{m \times n}, V \in \Re^{\ell \times k}$ and $X \in \Re^{n \times k}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Operators over symmetric matrices", "weight": 1.0} -->

This property is often used to rewrite linear equations over matrices in terms of vectors. When $X \in \sym{d}$ however, we often run into non-invertible systems since $\vec(X) \in \Re^{d^2}$ has unnecessary degrees of freedom. After all, a symmetric matrix is uniquely determined by $\sd{d} \dfn d(d+1)/2$values.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Operators over symmetric matrices", "weight": 1.0} -->

It is easy to verify that $Q_d$ is a unique matrix for which $Q_d \trans{Q_d} = I_{\sd{d}}$ [DeKlerk2002].

<!-- chunk {"id": "body-0029", "role": "body", "section": "Operators over symmetric matrices", "weight": 1.0} -->

We can then introduce the symmetrized Kronecker product [DeKlerk2002], For any $U, V \in \Re^{m \times n}$, let $$V \skron U = \frac{1}{2} Q_{m} (U \kron V + V \kron U) \trans{Q}_n.$$ By definition, we have a generalization of [eq:kronfund] [DeKlerk2002] $$\svec(Z X \trans{Z}) = (Z \skron Z) \svec(X).$$ We will also consider more general linear operators on symmetric matrices, $\op{S} \colon \sym{n} \to \sym{m}$, which can be expressed for any $X \in \sym{n}$ as $$\op{S}(X) = \unsvec(\opm{S} \svec(X)),$$ for *a unique $\opm{S} \in \Re^{\sd{m} \times

<!-- chunk {"id": "body-0030", "role": "body", "section": "Operators over symmetric matrices", "weight": 1.0} -->

The set of such operators is denoted $\slop{n}{m}$. The adjoint $\adj{\op{S}}$, defined to satisfy $\tr[\op{S}(X) Y] = \tr[X \adj{\op{S}}(Y)]$, has matrix $\trans{\opm{S}}$. Similar to [Coppens2020] we will often need to bound the spectral norm of the image of such matrix operators.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Operators over symmetric matrices", "weight": 1.0} -->

We are especially interested in linear operators that preserve positive semidefiniteness of the argument. That is, a map $\op{S} \colon \sym{n} \to \sym{m}$ is positive iff $\op{S}(X) \sgeq 0$ for all $X \sgeq 0$. More specifically we consider a specific type of positive map: A $\op{S} \in \slop{n}{m}$ is completely positive (CP) [Choi1975] if, for some $A_i \in \Re^{m \times n}$ with $i \in \N_{1:r}$, The matrix of $\op{S}$ is $\opm{S} = \ssum_{i=1}^r (A_i \skron A_i)$. We write $\op{S} \in \cpop{n}{m}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Operators over symmetric matrices", "weight": 1.0} -->

Like for linear dynamics, stability of CP operators can be defined in terms of the spectral radius.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Operators over symmetric matrices", "weight": 1.0} -->

The specific norm is left unspecified since the convergence would remain the same by equivalence of matrix norms.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Operators over symmetric matrices", "weight": 1.0} -->

Then $$\hat{\rho}(A_1, \dots, A_r)/\sqrt{r} \leq \rho(A_1, \dots, A_r) \leq \hat{\rho}(A_1, \dots, A_r).$$ Note that the joint spectral radius describes stability the dynamics of switched linear system. That is, dynamics $x_{t+1} = A_t x_t$ are stable for any sequence of matrices $A_t$ from $\{A_i\}_{i=1}^r$ iff $\rho < 1$ [Jungers2009]. Therefore thm:stab-eq gives a strong relation between stability of such systems and stability of $\op{S}$(and as we will see later mean square stability of linear dynamics with multiplicative noise).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Operators over symmetric matrices", "weight": 1.0} -->

We finally consider a Lyapunov criterion for stability: Let $\op{S} \in \cpop{d}{d}$. Then

<!-- chunk {"id": "body-0036", "role": "body", "section": "Operators over symmetric matrices", "weight": 1.0} -->

- If $\rho(\op{S}) < 1$, then $\forall H \sgt 0$ $$\exists P \sgeq 0 \colon P - \adj{\op{S}}(P) = H.$$ - Moreover, $P$ is unique, positive definite and $\tr[PX] = \tr[H \sum_{t=0}^\infty \op{S}^t(X)]$, $\forall X \sgeq 0$. - If [eq:cp-lyap] for some $H \sgt 0$, then $\rho(\op{S}) < 1$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Operators over symmetric matrices", "weight": 1.0} -->

For linear systems with multiplicative noise this statement was shown in [Kubrusly1985]. The proof for CP operators is similar.and is included.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Operators over symmetric matrices", "weight": 1.0} -->

By $H \sgt 0$ and lem:trivialinequality this implies $X_t \to 0$. Thus $\rho(\op{S}) < 1$ by lem:stabcp.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Tensor algebra", "weight": 1.0} -->

The dynamics in [eq:dyn]inherently have bilinear structure. This warrants the use of multi-linear structures and specifically third order tensors. In this section we introduce tensors and show how they are used to model CP operators. $\ten{T} \in \Re^{q_1 \times q_2 \times q_3}$ denote a generic third order tensor. A good introduction is given in [Kolda2006], [Golub2013]. We restate some parts here for completeness.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Tensor algebra", "weight": 1.0} -->

We can extend the single mode- $n$ product to the multi-linear one, similarly to [eq:modendef].

<!-- chunk {"id": "body-0041", "role": "body", "section": "Tensor algebra", "weight": 1.0} -->

That is, $\ttimes{n}$ is replaced by $\btimes{n}$. As common in literature we omit the transposes in this case writing $\tucker{\ten{T}; x_1, x_2, x_3}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Tensor algebra", "weight": 1.0} -->

The order of operations in [eq:multimodendef] is important when acting on vectors. After all since $\ten{T} \btimes{2} x_2 \in \Re^{q_1 \times q_3}$ writing $(\ten{T} \btimes{2} x_2) \btimes{3} x_3$ is not defined. *Instead we would need to write $(\ten{T} \btimes{2} x_2) \btimes{2} x_3 = (\ten{T} \btimes{2} x_2) x_3$. The Tucker operator helps to avoid such complexities, since we assume the order is reduced after all mode-$n$ products have been completed.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Tensor algebra", "weight": 1.0} -->

We frequently use a generalization of For $\ten{Y} \in \Re^{p_1 \times p_2 \times p_3}$ as in def:tucker: $$\ten{Y}_{(n)} = X_n \ten{T}_{(n)} \trans{(X_j \kron X_i)},$$ for $n, i, j \in \{1, 2, 3\}$ with $j > i$ and $n \neq i \neq j$. [eq:unfoldtucker] is given in fig:unfoldtucker. Note how the values along the third axis are split up both by the matricization and the Kronecker product.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Tensor algebra", "weight": 1.0} -->

Dependency of $\op{S}$ on $W$ in eq:cp-tensor-def can be made explicit by writing $\op{S}(W; X)$. That is $\op{S}(W; \cdot) \in \slop{n}{m}$. We distinguish the parameters of the map from its arguments using a semicolon. So $\adj{\op{S}}(W; P)$ denotes the adjoint w.r.t. the argument, not the parameter $W$. $\op{S}(W; X)$ is also CP in its parameter $W$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Tensor algebra", "weight": 1.0} -->

We will see later in the setting of multiplicative noise dynamics that cor:cpmon:bis useful for finding sufficient conditions for stability. Specifically, it allows constructing dynamics whose second moments dominate those of the true dynamics in the psd. sense.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Tensor algebra", "weight": 1.0} -->

There is a bilinear structure present in [eq:cp-tensor-def]. This becomes clear when considering $\tr[P \op{S}(W; X)]$, which is linear in $P$, $X$ and $W$. Hence, there is a version of prop:kronunfold for CP maps (cf. prop:cpunfold), which allows different characterizations of $\op{S}$ and $\adj{\op{S}}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Tensor algebra", "weight": 1.0} -->

Next we state a generalization of a property for the Kronecker product between matrices, which is used to rewrite CP operators.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Known distribution", "weight": 1.0} -->

We consider the nominal setting for multiplicative noise, where the distribution is known. The (CP) operator $\op{E}$ from eq:dynsm, which fully describes the second moment dynamics of eq:dyn, is examined. We prove that it is (i) linear in $Z_t$; (ii) completely positive; and (iii) is linear in $\E[v_t\trans{v_t}]$. Moreover, we argue how identifying $\op{E}$is sufficient to describe both stability and quadratically optimal control.

<!-- chunk {"id": "body-0049", "role": "body", "section": "The model tensor", "weight": 1.0} -->

We first illustrate how the previous tools interface with multiplicative noise. Consider the true model tensor $\ten{V} \in \Re^{n_x \times n_z \times n_v}$, which is populated as $[\ten{V}]_{::i} = [A_i, B_i]$ for $i \in \N_{1:n_v}$ using the modes in [eq:dyn]. This splits up the dynamics into two unknowns: the tensor $\ten{V}$ and the distribution of $v_t$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "The model tensor", "weight": 1.0} -->

To encode known information about we introduce the model tensor $\ten{M} \in \Re^{n_x \times n_z \times n_w}$ and the auxiliary random vector $w_t \in \Re^{n_w}$. When the modes are known, we can simply pick $\ten{M} = \ten{V}$ and $w_t = v_t$. However, when $\ten{V}$ is only partially known we can still select a $\ten{M}$ that has sufficient modeling capacity. Specifically we would like that for any realization of the disturbance $v_t$ and hence of the random matrices $A(v_t)$ and $B(v_t)$, there exists a realization of $w_t$ producing the same matrices by the modes A sufficient assumption for this property is: Consider $\ten{V} \in \Re^{n_x \times n_z \times n_v}$ with $n_z \dfn n_x + n_u$ s.t.

<!-- chunk {"id": "body-0051", "role": "body", "section": "The model tensor", "weight": 1.0} -->

asm:model and this partitioning, we can show that x_{t+1} &= \tucker{\ten{A}; I_{n_x}, x_t, {w}_t} + \tucker{\ten{B}; I_{n_x}, u_t, {w}_t} \nonumber \\describes the same dynamics as [eq:dyn], given a suitable choice of $w_t$. We formalize equivalence of [eq:dynten] and [eq:dyn]below.

<!-- chunk {"id": "body-0052", "role": "body", "section": "The model tensor", "weight": 1.0} -->

When asm:model holds and $w_t = \pinv{(\trans{\ten{M}_{}})} \trans{\ten{V}_{}} v_t$, $\forall t \in \N$, then [eq:dynten] produces the same trajectories as [eq:dyn].

<!-- chunk {"id": "body-0053", "role": "body", "section": "The model tensor", "weight": 1.0} -->

We illustrate the need for asm:model. Assume $n_x = 2$, $n_u = 1$ and $n_v = 3$ with true modes: and $B_1 = B_2 = 0$. In this case $\ten{V}_{}$ is given as \begin{smallarray}{cccc|cc} \trans{\vec(A_1)} & \trans{\vec(B_1)} \\\trans{\vec(A_2)} & \trans{\vec(B_2)} \\\trans{\vec(A_3)} & \trans{\vec(B_3)} \\Say a designer, through some erroneous prior analysis, assumed that the top-left component in $A_1$ was equal to zero instead of two. This corresponds to the following model tensor: \begin{smallarray}{cccc|cc} for this choice asm:model fails and so will lem:model-eq. To see this, take $v_t = $.

<!-- chunk {"id": "body-0054", "role": "body", "section": "The model tensor", "weight": 1.0} -->

Then $\vec([A(v), B(v)]) = $. Observe that such a vector cannot be constructed by any linear combination of the rows of $\ten{M}_{}$. So there is no distribution for $w_t$ that reproduces the true dynamics. asm:model requires that the span of $\trans{\ten{M}_{}}$ should be sufficiently large to model the outputs of $A(v)$ and $B(v)$ given by realizations of $v \in \Re^{n_v}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "The model tensor", "weight": 1.0} -->

Note that this is always possible, by taking $\ten{M}_{} = I_{n_w}$. We refer to this as the model-free basis, since no prior structural assumptions are imposed on the dynamics. If we know the true modes $A_i$ and $B_i$, we can simply select $\ten{M} = \ten{V}$. As such, $\ten{M}$is used to introduce prior information into the dynamics.

<!-- chunk {"id": "body-0056", "role": "body", "section": "The model tensor", "weight": 1.0} -->

Since the sequence $v_t$ is i.i.d., the sequence $w_t$ as defined in lem:model-eq is i.i.d. too. We thus omit $t$ as the distribution remains constant. We can then use the transformation in lem:model-eq to find the true $W = \E[w \trans{w}]$ in terms of $V = \E[v \trans{v}]$: $$W = \pinv{(\trans{\ten{M}_{}})} \trans{\ten{V}_{}} V \ten{V}_{} \pinv{\ten{M}_{}}.$$ This allows translating the ground truth dynamics to another model tensor and will aid in validation of our method during the experiments in sec:numerical.

<!-- chunk {"id": "body-0057", "role": "body", "section": "The model tensor", "weight": 1.0} -->

We next illustrate the connection with CP operators by considering the dynamics of By prop:kronunfold, $\tucker{\ten{M}; I, z_t, {w}_t} = \ten{M}_{} ({w}_t \kron z_t)$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "The model tensor", "weight": 1.0} -->

The operator $\op{E} \colon \sym{n_z} \to \sym{n_x}$ is clearly CP by lem:tencp. It is linear with its matrix characterized by cor:cpadj. Moreover it has a bilinear structure, depending linearly on $W$ (and by [eq:true\_moment] on $V$). So we confirmed the claims from the problem statement. We provide a brief illustration of how $\op{E}$ encodes the dynamics and thenWe nextdiscuss nominal stability and LQR, before introducing the system identification scheme.

<!-- chunk {"id": "body-0059", "role": "body", "section": "The model tensor", "weight": 1.0} -->

The matrix associated with $\op{E}$ as described in cor:cpadj is given as follows: $$\opm{E} = Q_2 \begin{bmatrix} \end{bmatrix} \trans{Q_2}.$$ which is added as prescribed in the definition of $\skron$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Stability", "weight": 1.0} -->

We consider stability of the autonomous case of [eq:dynten]: Stability of stochastic systems is intimately related to convergence of random variables, which can be defined in several ways [Grimmett2001d]. We specifically consider convergence to zero of the second moment [Grimmett2001d], Consider the autonomous system [eq:aut-dyn]. It is considered mean-square stable (MSS) if $$\E[x_t \trans{x_t}] \to 0 \quad \text{as} \quad t \to \infty.$$ From the definition, MSS is equivalent to the stability of $$X_{t+1} = \op{F}(X_t) \dfn \ten{A}_{} (W \kron X_t) \trans{\ten{A}_{}},$$ where $X_t = \E[x_t \trans{x_t}]$ as before and $\op{F}$ is the autonomous version of $\op{E}$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Stability", "weight": 1.0} -->

Clearly this system is stable for all $X_0 \sgeq 0$ iff $\rho(\op{F}) < 1$ by lem:stabcp. Therefore: The system [eq:aut-dyn] is MSS iff $\rho(\op{F}) < 1$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Stability", "weight": 1.0} -->

We can verify stability with the Lyapunov condition prop:lyapcp and, as mentioned earlier, stability of [eq:aut-dyn] is *related with robust stability of the switching system with modes $\{A_i\}_{i=1}^{n_w}$ in the sense of thm:stab-eq. This *relation was observed before in [Gravell2020] and [Bernstein1987], yet not fully characterized.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

The goal of this section is twofold (i) we argue how LQ control of CP dynamics is equivalent to eq:slqr; and (ii) we show how the optimal policy is determined by solving a SDP, generalizing the result of [Balakrishnan2003].

<!-- chunk {"id": "body-0064", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

We start by stating the CP equivalent of &\minimize_{Z_t} &\quad& \sum_{t=0}^\infty \tr[Z_t H] \\&\stt && Z_t = \begin{bmatrix} \end{bmatrix} \sgeq 0, \\&&&X_{t+1} = \op{E}(Z_t), \quad \forall t \in \N, \end{alignedat} \tag{$\mathcal{LQR}_{\mathrm{cp}}$}$$ with $H \dfn \blkdiag(Q, R) \sgt 0$. The psd. constraint on $Z_t$ensures that it acts like the second moment of a random vector.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

We show that [eq:slqr] is equivalent to [eq:lqrcp] Let $\mathrm{Val}(\cdot)$ denote the optimal value. Then $$\mathrm{Val}eq:slqr = \mathrm{Val}eq:lqrcp,$$ given asm:model. Moreover sequence $(Z_t)_{t \in \N}$ is feasible for [eq:lqrcp] iff there is a feasible sequence and $\delta_t \in \Re^{n_u}$ is a random vector $\forall t \in \N$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

In the deterministic setting with $n_w = 1$ and $w_t = 1$ (so $\E[W] = 1$), we have $\adj{\op{F}}(P) = \trans{A}_1 P A_1$, $\adj{\op{H}}(P) = \trans{B}_1 P A_1$ and $\adj{G}(P) = \trans{B}_1 P B_1$. Hence we recover the classical Riccati operator as a special case.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

$$\Pi_K(X) \dfn [I; K] X [I, \trans{K}], \, \op{E}_K(X) \dfn \op{E}(\Pi_K(X)),$$ The policy $Z_t = \Pi_K(X_t)$ is recovered when taking $u_t = Kx_t$ in the equivalent [eq:slqr] (cf. thm:cpmulteq).

<!-- chunk {"id": "body-0068", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

We can then state the following theorem.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

- $\mathrm{Val}eq:lqrcp = \tr[P_{\star} X_0]$; See Appendixapp:lqr for the full proof.This result was shown for multiplicative noise in and generalized to the CP setting by thm:cpmulteq. Nonetheless, a full proof is included in the technical report.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

Here the existence of a $K$ such that $\rho(\op{E}_K(\cdot)) < 1$ is referred to as stabilizability. Among other things it implies the system being below the uncertainty threshold [Athans1977].

<!-- chunk {"id": "body-0071", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

Let us consider a deterministic system with $n_w = 1$ and \end{bmatrix}, \, B_1 = \begin{bmatrix} This will help us understand how eq:lqrcp generalizes the usual notions of LQR. We pick $H = \diag(1, 1, 0.1)$. Then the solution described by thm:cplqr is approximately: One can easily verify that this is the usual LQR solution in the deterministic setting. Let's spend some time noting what happens when we set $X_0 = x_0 \trans{x_0}$. In that case, for some $u_0$, let $Z_0 = (x_0, u_0) \trans{(x_0, u_0)}$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

It is not difficult to verify that this equals $x_1 \trans{x_1}$ for $x_1 = A_1 x_0 + B_1 u_0$. We could repeat this for each time step noting that $X_t = x_t \trans{x_t}$ and $Z_t = (x_t, u_t) \trans{(x_t, u_t)}$ in eq:lqrcp. Trivially we have $Z_t \sgeq 0$, so the trajectory is feasible. Moreover the cost becomes $\tr[Z_t H] = \trans{x_t} I x_t + 0.1 \trans{u_t} I u_t$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

So we can see that the classical LQR controller is at least a feasible solution to eq:lqrcp where we then have x_t \trans{x_t} & x_t \trans{x}_t \trans{K} \\ K x_t \trans{x_t} & K x_t \trans{x}_t \trans{K} \end{bmatrix} \\ &= (x_t, Kx_t) \trans{(x_t, Kx_t)}.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

Note that we have shown in thm:cplqr that such policies are in fact optimal. In terms of [eq:slqr] this implies that, a random policy $u_t = Kx_t + \delta_t$ for some random $\delta_t$ will not improve performance.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

Even though we directly tackled second moment dynamics in the optimal policy $Z_t = \Pi_{K_{\star}}(X_t)$ is realizable for multiplicative noise dynamics using $u_t = K_{\star} x_t$. So this controller is also optimal for [eq:slqr] as is well known (cf. [Coppens2019]) and achieves the equality in thm:cpmulteq.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

Thus we can conclude that LQR of CP dynamics is (i) identical to LQR of multiplicative noise dynamics; (ii) a natural generalization of classical LQR; and (iii) a relaxation for LQR of switching systems in the sense of The final question is how to find a $P_\star$ satisfying [eq:ric-def]. Numerical solution of such equations is considered in detail in [Damm2003]. We consider a reformulation as a SDP, akin to [Balakrishnan2003].

<!-- chunk {"id": "body-0077", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

- eq:ric-sdp-primal is bounded iff $\exists K \colon \rho(\op{E}_K) < 1$; - For bounded eq:ric-sdp-primal, the $P_\star$ that solves eq:ric-def is an optimizer. Moreover, for $X_0 \sgt 0$, $P_\star$ is the unique solution.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

The proof is analogous to the one in [Balakrishnan2003] and [Coppens2019]. The full proof is deferred to Appendixapp:lqr.A full proof in the CP case is deferred to.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

*So the SDP in thm:ric-sdp-primal both provides a way of solving the Riccati equation and a way to verify stabilizability.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Identifying the second moment", "weight": 1.0} -->

Our goal in this work is to generalize thm:cplqr to the data-driven DR setting [eq:drlqr], while retaining stability for a linear controller. This problem was considered in [Coppens2019], for sub-Gaussian normalized disturbance $\xi$ (i.e. $\xi \dfn \V[w]^{-1/2}(w - \E[w])$). Therefore [Coppens2019] supports among others Gaussian $w$ or bounded $\xi$. This setup had two main limitations: (i) bounded $w$ does not imply bounded $\xi$, so the link with classical robust control (as exploited for additive noise in [Coppens2021]) is lost; (ii)the setup is inapplicable when only state measurements are available. This section resolves we first formalize the concept of an ambiguity set.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Identifying the second moment", "weight": 1.0} -->

We operate in a setting similar to that of [Coppens2021]. Specifically consider a probability space $(\Omega, \F, \prob)$ and the problem \min_{u \in \set{U}} \quad \E[\ell(u, w)], with $u \in \Re^{n_u}$ some decision variable, $\ell \colon \Re^{n_u} \times \Re^{n_w} \to \eRe$ some loss function and $w \colon \Omega \to \set{W}$ a vector with $\set{W} \subset \Re^{n_w}$ the (compact) support of $w$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Identifying the second moment", "weight": 1.0} -->

$\Pf(\set{W})$ denote the space of probability measures on the measurable space $(\set{W}, \B)$ with $\B$ the Borel $\sigma$-algebra associated with $\set{W}$, the main difficulty in solving [eq:sopt] is the push-forward measure $\nu_{\star} \in \Pf(\set{W})$, defined as $\nu_{\star}(O) - \prob[w^{-1}(O)]$ for all $O \in \B$. In practice $\nu_{\star}$ is often unknown, hence $\E[\ell(u, w)] = \E_{\nu_{\star}}[\ell(u, w)]$cannot be evaluated.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Identifying the second moment", "weight": 1.0} -->

Instead DRO considers an ambiguity set $\amb \subseteq \Pf(\set{W})$, which contains $\nu_{\star}$ with high confidence.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Identifying the second moment", "weight": 1.0} -->

$$\prob[\nu_\star \in \amb] \geq 1 - \delta.$$ Usually this is guaranteed by imposing some structure on $\amb$ [Coppens2021]. Examples are moment-based ambiguity, which constrain the measures in terms of its moments, Wasserstein ambiguity [Kuhn2019] which is centered on the empirical measure and bounds the Wasserstein distance and $\phi$-divergence [Schuurmans2020] which bounds some divergence. The Wasserstein sets has the issue that the radius $\beta$ depends on unknown parameters of the distribution and the $\phi$-divergence sets often only support discrete distributions. The advantage of moment-based ambiguity as considered here and in [Coppens2021] is (i) it contains measures that are not only supported on the data; (ii) a fully data-driven estimate of $\beta$ is available; and (iii) problem complexity does not grow with the sample count. For more info see [Rahimian2019].

<!-- chunk {"id": "body-0085", "role": "body", "section": "Identifying the second moment", "weight": 1.0} -->

For a concrete example, a direct application of a matrix Hoeffding bound (cf. lem:mathfd) gives the following result when samples from the disturbance are available: Let $\set{W} = \left\{ w \in \Re^{n_w} \colon \nrm*{w}_2 \leq r_w \right\}$. Assume we have a set of i.i.d. samples $\{w_i\}_{i\in\N_{1:M}}$ of a random vector $w$ and let $\hat{\smoment} \dfn \ssum_{i=1}^{N} w_i \trans{w_i}/N$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Identifying the second moment", "weight": 1.0} -->

Given an ambiguity set $\amb$ we can then solve the following dro. problem, which is a conservative approximation of [eq:sopt], $$\min_{u \in \set{U}} \, \max_{\nu \in \amb} \, \E_{\nu}[\ell(u, w)].$$ These problems are related to risk measures by duality [Coppens2021].

<!-- chunk {"id": "body-0087", "role": "body", "section": "Identifying the second moment", "weight": 1.0} -->

The goal now is to generalize lem:dd-momentto the setting where only state measurements are available.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Measurement model", "weight": 1.0} -->

Considering the dynamics [eq:dynten], the goal is to estimate the denote the true values using a star subscript. $W_\star \dfn \E[w \trans{w}]$. *This should be accompanied by a similar concentration inequality as in lem:dd-moment without assuming direct access to samples $(w_i)_{i=1}^N$. Instead we measure a sequence of $N$ independent samples $(x_{i+1}, z_i)_{i=1}^N$, with $z_i = (x_i, u_i)$ the augmented state, satisfying the measurement model: where $(w_i)_{i=1}^N$denotes the noise sequence.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Measurement model", "weight": 1.0} -->

There are two important properties that [eq:measurement-model] should satisfy: (i) the `span' of the (mixed) model tensor $\ten{M}$ should describe the true dynamics (i.e. asm:model); and (ii) the data should be sufficiently rich to render *$W_\star$ observable. This final property is akin to persistency of excitation. We specifically assume that the support of $z_i$ is not degenerate as is formalized in the following assumption.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Measurement model", "weight": 1.0} -->

We assume that $\{z_i\}_{i\in\N_{1:N}}$ is a sequence of i.i.d. copies of a random vector $z$, with a distribution that is dominated by the Lebesgue measure.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Measurement model", "weight": 1.0} -->

A direct consequence of asm:data is that More details on asm:data are given., by lem:rank-condition, if $N \geq n_z$, Independence is guaranteed for each $i$ by either (i) taking a known random $z_i = (x_0, u_0)$, updating [eq:dyn] once and taking $x_{i+1} = x_1$; or (ii) taking a known $x_0$, updating [eq:dyn] $T$ times for random $u_t$ and taking $x_{i+1} = x_T$ and We refer to (i) as random initialization and to (ii) as rollout similar to [Xing2020, Dean2019].

<!-- chunk {"id": "body-0092", "role": "body", "section": "Measurement model", "weight": 1.0} -->

For rollout it is difficult to verify [eq:rank-condition]. Usually a notion of controllability and persistency of excitation is employed. Full generalizations of these concepts for multiplicative noise do not exist to our knowledge. Note however that the event in [eq:rank-condition] is related to the zeros of a polynomial. So an argument similar to the one in prop:obsv below is applicable. In practice one can sample $u_t$ from a distribution dominated by the Lebesgue measure and test whether [eq:rank-condition] holds *for $N = n_z$. *When taking more samples, the validity of eq:rank-condition will stay the same with probability one.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Noise observability", "weight": 1.0} -->

In some cases, the disturbances can be inferred exactly from state measurements. *Specifically in eq:measurement-model we can expand the definition of the Tucker product as in rem:tucker and plug in the definition of $\btimes{2}$ to get: $$x_{i+1} = (\ten{M} \btimes{2} z_i) \btimes{2} w_i = (\ssum_{j=1}^{n_z} [z_i]_j [\ten{M}]_{:j:}) w_i.$$ Thus if $(\ten{M} \btimes{2} z_i)$ is left invertible, we can uniquely identify $(w_i)_{i=1}^N$ from $(x_{i+1}, z_i)_{i=1}^N$.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Noise observability", "weight": 1.0} -->

Invertibility of $(\ten{M} \btimes{2} z_i)$ however is analogous to invertibility of a linear subspace of matrices (or linear forms), which is an unsolved problem in general (cf. [Testa2018] for $3 \times 3$ matrices). We have the following: Let $z$ denote a random vector with non-degenerate support (cf. asm:data) and $n_x \geq n_w$. Then, $(\ten{M} \btimes{2} z)$ is left invertible either with probability one or zero.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Noise observability", "weight": 1.0} -->

A high-level proof is given in [Lovasz1989] in the setting of invertibility of linear forms.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Noise observability", "weight": 1.0} -->

This suggests that it is often sufficient to sample $(\ten{M} \btimes{2} z)$ for a random $z$ and check its invertibility. *The conclusion will then generalize to other realizations, except for a set of measure zero. *When invertibility holds, eq:bilinear-form-alt can be solved for ${w}_i$ exactly. Then the following holds: Let $\set{W} = \left\{ w \in \Re^{n_w} \colon \nrm*{w}_2 \leq r_w \right\}$. Assume we have a set of i.i.d. samples $\{w_i\}_{i\in\N_{1:M}}$ of a random vector $w$ and let $\hat{\smoment} \dfn \ssum_{i=1}^{N} w_i \trans{w_i}/N$.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Noise observability", "weight": 1.0} -->

The result follows from a direct application of lem:mathfd by noting that the terms in the error satisfy $-r_w^2 I \sleq -w_i \trans{w_i} \sleq W_\star - w_i \trans{w_i} \sleq W_\star \sleq r_w^2I$.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Noise observability", "weight": 1.0} -->

We also want to estimate $W_\star$ in the other case (i.e., when $n_x < n_w$). For example, for a model-free basis we have $n_w = n_x n_z > n_x$. To do so we design least squares estimators.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Least squares estimator", "weight": 1.0} -->

To *design a least square (LS) estimator, we need to convert [eq:measurement-model] into an expression linear in $w_i \trans{w_i}$. We can do so by using lem:tensor-kron on eq:measurement-model *and use $I_{n_x} \skron I_{n_x} = I_{\sd{n_x}}$, which gives: $$x_{i+1} \skron x_{i+1} = \tucker{\ten{M} \skron \ten{M}; \update*{I_{\sd{n_x}},\,} z_i \skron z_i, w_i \skron w_i}.$$ Note $\E[w_i \skron w_i] = \E[\svec(w_i \trans{w_i})] \nfd \svec(W_\star)$.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Least squares estimator", "weight": 1.0} -->

We can write this in terms of linear equations by expanding the Tucker operator *(cf. def:tucker and rem:tucker): x_{i+1} \skron x_{i+1} &= (\ten{W} \btimes{2} (z_i \skron z_i)) \svec(W_\star) \\ &\qquad + (\ten{W} \btimes{2} (z_i \skron z_i)) \eta_i, with $\ten{W} = \ten{M} \skron \ten{M}$ and noise $\eta_i = w_i \skron w_i - \svec(W_\star)$.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Least squares estimator", "weight": 1.0} -->

$\E[\eta_i] = 0$ so $\E[E_N] = 0$, which suggests the LS estimate: $$\svec(\hat{\smoment}) = \pinv{\opm{Z}_N} Y_N.$$ A similar estimator to $\hat{\cmoment}$ is used in compressed covariance sensing [Romero2013], where it is observed that it acts as a good heuristic for the maximum likelihood estimator when $w$ is Gaussian. Noting that each element of the vector equation [eq:smoment-model] constitutes a bilinear form of $z_i$, reveals a connection with bilinear estimation [Kukush2003]. There, adjusted LS estimators exist that are consistent even when $z_i$is perturbed by random noise. For simplicity we consider exact state measurements here, which enables the use of ordinary LS, for which it is convenient to derive concentration inequalities.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Error analysis", "weight": 1.0} -->

We analyze the error of the LS estimator [eq:ls-estimator] under asm:model[asm:data]. The discussion *differs somewhat from the classical case *due to the biased estimate eq:ls-estimator. *However, this bias is inconsequential as our focus is on estimating the second moment dynamics. We demonstrate that the estimate $\op{E}(\hat{\smoment}; \cdot)$ *captures the second moment dynamics $\op{E}_\star \dfn \op{E}(W_\star; \cdot)$ without bias. This phenomenon is *commonly observed in system identification of multiplicative noise, *as noted. *Since this complicates the error analysis, we provide only the intuition here, with formal statements deferred to Appendixapp:identification.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Error analysis", "weight": 1.0} -->

The overall estimation error is given as $$\svec(\hat{\smoment} - W_\star) = (I - \pinv{\opm{Z}_N} \opm{Z}_N) \svec(W_\star) + \pinv{\opm{Z}}_N E_N.$$ We first discuss the nuances associated with the first term on a high level, before formally stating the error bound.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Error analysis", "weight": 1.0} -->

Noting that the second term is zero mean, the first term in eq:error-model-full constitutes the bias in the estimate. This bias is characterized exactly in lem:kernel-zn and is often non-zero. The reason for this can be given in terms of the matrix associated with $\op{E}(W; \cdot)$ denoted as $\opm{E} \in \Re^{\sd{n_x} \times \sd{n_z}}$, which uniquely determines the second moment dynamics. Our procedure parametrized $\opm{E}$ in terms of $W \in \sym{n_w}$. In other words, we use $\sd{n_w}$ parameters to describe $\sd{n_x} \sd{n_z}$ degrees of freedom. In the model-free case (i.e. when $n_w = n_z n_x$) we would always over parametrize $\opm{E}$ for $n_x > 1$.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Error analysis", "weight": 1.0} -->

One might therefore argue that $\opm{E}$ should be parametrized directly. We instead use $W$ for three reasons: (i) often a description like [eq:dyn] with a bound on $\nrm{w}_2$ is more natural in practical applications and such bounds do not translate well into bounds on $\opm{E}$; (ii) control synthesis using a confidence set over $W$ is more tractable; and (iii)the bias is inconsequential for the LQR cost and stability analysis.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Error analysis", "weight": 1.0} -->

(iii) is caused by the fact that the bias always lies in the kernel of the second moment dynamics (cf. [eq:dynsm\_]) $\op{E}(W; Z)$ w.r.t. $W$. This kernel in fact is also the cause of the bias in the first place as formalized in lem:kernel-sm.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Error analysis", "weight": 1.0} -->

We are now ready to state a data-driven bound, suitable for control synthesis. To do so we first consider some auxiliary operators. Letting $\ten{M}$ denote the model tensor (cf. asm:model) and $\ten{W} \dfn \ten{M} \skron \ten{M}$ as before, we introduce* \op{W}(z\trans{z}) &\dfn \trans{(\ten{W} \ttimes{2} (z \skron z))} (\ten{W} \ttimes{2} (z \skron z)) \\&= \ten{W}_{} ((z\trans{z} \skron z\trans{z}) \kron I_{\sd{n_x}}) \trans{\ten{W}_{}}, where the equality is shown in lem:wop:a.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Error analysis", "weight": 1.0} -->

Sample complexity Due to independence one may expect the matrices $\op{W}(z_i \trans{z_i})$ to behave similarly. Hence, one can expect $\nrm{\op{H}_i}_2$ to decrease with $1/N$. So $\zeta_W^2 = {\ssum_{i=1}^N \nrm{\op{H}_i}_2^2}$ would decrease with $1/N$ too. We formalize this intuition in a simplified setting below.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Error analysis", "weight": 1.0} -->

Details on bounding the tensor spectral norm $\nrm{\ten{W}}_2$ are given in [Chen2020a].

<!-- chunk {"id": "body-0110", "role": "body", "section": "Error analysis", "weight": 1.0} -->

Note that convergence of $\zeta_W$ depends on the kurtosis of $z$ (i.e. the fourth order moment) through $\gamma_W$, which can be difficult to quantify in practice. We observe that the value of $\gamma_W$ is invariant to scaling of $z$ and is larger when $z \skron z$ is spread out close to the boundary of its support, which will imply faster convergence.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Distributionally robust control synthesis", "weight": 1.0} -->

In this section we design approximate reformulations of [eq:drlqr]. The goal is to preserve the properties of thm:cplqr. Specifically we want to synthesize a distributionally robustly stabilizing controller, by solving a SDP as in thm:ric-sdp-primal. The synthesis procedure is described in sec:synthesis. We also *evaluate the sample complexity in sec:analysis.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Synthesis", "weight": 1.0} -->

In this section, we use our confidence bound in thm:error-bound-full to synthesize a controller that stabilizes the true system with high probability. Similarly, to sec:lqr we do so by investigating [eq:lqrcp]. Specifically consider the CP version of [eq:drlqr]: &\minimize_{Z_t \sgeq 0} \,\, \maximize_{\ubar{W} \sleq W \sleq \bar{W}} &\quad& \ssum_{t=0}^\infty \tr[Z_t H].

<!-- chunk {"id": "body-0113", "role": "body", "section": "Synthesis", "weight": 1.0} -->

\end{alignedat} \tag{$\bar{\mathcal{LQR}}_{\mathrm{cp}}$}$$ subject to $Z_t = [X_t, V_t; \trans{V_t}, U_t] \sgeq 0$, $X_{t+1} = {\op{E}}(W; Z_t)$ and with $\ubar{W}$ and $\bar{W}$ as in thm:error-bound-full. The constraints on $W$ define the equivalent of the ambiguity set in eq:drlqr. [eq:drlqr] by generalizing [thm:cplqr].

<!-- chunk {"id": "body-0114", "role": "body", "section": "Synthesis", "weight": 1.0} -->

We will use the closed-loop policy $\Pi_K$ as defined in eq:clops We have the following: Assume $H = \blkdiag(Q, R) \sgt 0$ and $$\exists K: \rho({\op{E}}_K(W; \cdot)) < 1, \,\forall W \colon \ubar{W} \sleq W \sleq \bar{W}.$$ Then the policy $Z_t = \Pi_{\bar{K}}(X_t)$ is optimal for [eq:drlqrcp], with $(\bar{P}, \bar{K})$ the optimal solution as described in thm:cplqr where we assume $\op{E} = \op{E}(\bar{W}, \cdot)$.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Synthesis", "weight": 1.0} -->

The proof is similar to that of [Coppens2019] for multiplicative noise, and is based on showing that the Bellman operator is of the same structure as in thm:cplqr by using cor:cpmon. A full proof for the CP case is given.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Synthesis", "weight": 1.0} -->

We do not repeat the full proof of thm:cplqr. Instead we consider only the Bellman operator and show that it has a similar structure to the one of [eq:lqrcp].

<!-- chunk {"id": "body-0117", "role": "body", "section": "Synthesis", "weight": 1.0} -->

The analogous Bellman operator to $$\minimize_{Z \sgeq 0} \, \maximize_{\ubar{W} \sleq W \sleq \bar{W}} \, \{ Observing that (cf. cor:cpmon) ${\op{E}}(Z) = \op{E}(W; Z) \sleq \op{E}(\bar{W}; Z)$ shows that $\op{E}(\bar{W}; Z)$ achieves the maximum in [eq:drbellman] $\forall Z$. Therefore, value iteration becomes: The proof is then completed by following the remainder of the proof of thm:cplqr, for $\op{E}(\bar{W}; \cdot)$ instead of $\op{E}(\cdot)$.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Synthesis", "weight": 1.0} -->

*Stabilizability is replaced by a robust equivalent. When violated, eq:drlqrcp is infeasible and the SDP in thm:ric-sdp-primal is unbounded. If this occurs the user should gather more data or verify if the nominal system is stabilizable using first principles (e.g. whether the uncertainty threshold is exceeded). When $\op{E}(\ubar{W}; \cdot)$ is not stabilizable (i.e. eq:ric-sdp-primal is unbounded), then the true system will not be either with high probability. In that case, not much can be done from a control perspective besides re-designing actuators. thm:error-bound-full implies the true $\op{E}_\star$ satisfies $\op{E}(\ubar{W}; \cdot) \sleq \op{E}_\star \sleq \op{E}(\bar{W}; \cdot)$ with probability at least $1 - \delta$.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Synthesis", "weight": 1.0} -->

So we have: Let $\bar{K}$ denote the DR policy as in thm:drlqrcp and assume the setup of thm:error-bound-full holds. Moreover, let $\op{E}_\star$ denote the true moment dynamics.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Synthesis", "weight": 1.0} -->

Then with probability at least $1-\delta$,

<!-- chunk {"id": "body-0121", "role": "body", "section": "Synthesis", "weight": 1.0} -->

By thm:error-bound-full, $\prob[\op{E}(\ubar{W}; \cdot) \sleq \op{E}_\star \sleq \op{E}(\bar{W}; \cdot)] \geq 1-\delta$. Thus, $\exists W \colon \ubar{W} \sleq W \sleq \bar{W}$ such that $\op{E}(W; \cdot) = \op{E}_\star(\cdot)$. So stability (i) follows from thm:drlqrcp:a and (ii) follows by maximization over $W$ in [eq:drlqrcp] for the inequality and thm:cpmulteq for the equality.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Synthesis", "weight": 1.0} -->

As in thm:cpmulteq, we have $\mathrm{Val}eq:drlqrcp = \mathrm{Val}eq:drlqr$. To save space we omit a proof and instead claim only $\mathrm{Val}eq:drlqrcp \geq \mathrm{Val}eq:slqr$. This is sufficient for safety critical applications where an upper bound is sufficient for stability. We show consistency of [eq:drlqrcp] later to further strengthen the result.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Sample complexity", "weight": 1.0} -->

As shown in the previous section, the solution of the DR problem sec:construction is described by a perturbed Riccati equation. As such, we use perturbation analysis to bound the sub-optimality of the DR controller when applied to the true dynamics. We leverage a previous result by the authors in [Coppens2020]to do so.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Sample complexity", "weight": 1.0} -->

The final complexity bound is as follows: *Assume asm:modelasm:data *(for $\nrm{z_i}_2$ bounded a.s.) and let $\bar{K}$ be the optimal controller in thm:drlqrcp. Then, for sufficient samples $N$ and with probability at least $1-\delta$, $$\tr\left[\sum_{t=0}^\infty Z_t H\right] - \mathrm{Val}eq:lqrcp = \op{O}\left(\frac{1}{N} \right),$$ where the first term is the cost of eq:lqrcp achieved for $Z_t = \Pi_{\bar{K}}(X_t)$ with true moment dynamics $X_{t+1} = \op{E}_\star(Z_t)$.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Sample complexity", "weight": 1.0} -->

Moreover by thm:cpmulteq, for sufficient samples $N$ and with probability at least $1-\delta$, $$\E\left[\sum_{t=0}^\infty \trans{x_t} Q x_t + u_t R u_t \right] - \mathrm{Val}eq:slqr = \op{O}\left(\frac{1}{N} \right),$$ where $x_{t+1} = A(v_t) x_t + B(v_t) u_t$ as in eq:dyn, $u_t = \bar{K} x_t$. So the first term is the cost achieved when applying $\bar{K}$ to the true multiplicative noise dynamics eq:dyn.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Sample complexity", "weight": 1.0} -->

We suggest some modifications of the proof of [Coppens2020] to show the second result. The first result then follows directly from thm:cpmulteq.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Sample complexity", "weight": 1.0} -->

Modifications are required as a relative bound like $\ubar{\alpha} W_\star \sleq \hat{W} - W_\star \sleq \bar{\alpha} W_\star$, with $\ubar{\alpha} \leq \bar{\alpha} = \mathcal{O}(1/\sqrt{N})$ with high probability, $W_\star$ the true value of $\E[w \trans{w}]$ and $\hat{W}$ some estimate. Instead we have $0 \sleq \bar{W} - W_\star \sleq 2\beta_W I$ with $\beta_W = \mathcal{O}(1/\sqrt{N})$ by thm:error-bound-full and lem:moment-sample-complexity (where we ignore the effect of the bias, without loss of generality due to lem:kernel-sm). So the proofs need to be modified.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Sample complexity", "weight": 1.0} -->

Specifically we replace [Coppens2020] with a bound like $$\nrm{\ten{A}_{} (\bar{W} - W_\star \kron P) \trans{\ten{A}_{}}}_2 \leq 2 \beta_W \nrm{\ten{A}_{} (I \kron P) \trans{\ten{A}_{}}}_2.$$ The proof is analogous and is based on cor:cpmon. Following the proof of [Coppens2020] and its dependencies, clearly only the constants in [Coppens2020] are affected. The rate shown in [Coppens2020] remains the same. *The full proof with explicit constants is given in app:sample-complexity.The full proof with explicit constants is given.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Sample complexity", "weight": 1.0} -->

Since the estimation error bounds are of the same order, we get the same sample complexity in the certainty equivalent setting [Astrom2008], where we use $\hat{W}$ instead of $\bar{W}$. The proof is analogous.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Sample complexity", "weight": 1.0} -->

*In both cases the rate in terms of $N$ is the same as in the additive noise case. This implies that, qualitatively in terms of samples, learning additive noise or multiplicative noise is similar. The dimensional dependency of the error however is $n_x^2 (n_x + n_u)$ for $n_x \geq n_u$ and omitting logarithmic terms. This is worse compared to additive noise, where a lower bound is established of $\sqrt{n_x^2 n_u}$. Note that our bound is not a lower bound, so further research might lead to a tighter dimensional dependency. Exploiting $\ubar{W}$ in thm:error-bound-full could be a first step.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Imposing prior structure", "weight": 1.0} -->

The tools we introduce for identification are also applicable when prior structure is imposed on the dynamics $$x_{t+1} = \left(\sum_{i=1}^{n_v} A_{i+1} [v_t]_i + A_1\right) x_t + \left(\sum_{i=1}^{n_v} B_{i+1} [v_t]_i + B_1\right) u_t,$$ where $A_i$ and $B_i$ are assumed known for $i\in\N_{1:n_v+1}$. We were able to handle the terms linear in $v_t$ in the previous sections by adequate selection of $\ten{M}$ in asm:model. However, the introduction of the known terms $A_1$ and $B_1$ are not supported They can be supported by assuming $A_1$ and $B_1$ are multiplied by an unknown random value. However, by doing so, structural information is lost.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Imposing prior structure", "weight": 1.0} -->

we illustrate how this prior information can be exploited in a DR control scheme.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Imposing prior structure", "weight": 1.0} -->

We can also partition $\ten{M}$ similarly as before in $\ten{A}$ and $\ten{B}$ and write the dynamics x_{t+1} &= \tucker{\ten{A}; x_t, w_t} + \tucker{\ten{B}; u_t, w_t} \nonumber \\lem:model-eq generalizes to When asm:model holds and $w_t = (1, \widetilde{w}_t)$ with $\widetilde{w}_t = \pinv{(\trans{\widetilde{\ten{M}}_{}})} \trans{\widetilde{\ten{V}}_{}} v_t$, $\forall t \in \N$. Then [eq:dynten-structured] produce the same trajectories as [eq:dyn-structured].

<!-- chunk {"id": "body-0134", "role": "body", "section": "Imposing prior structure", "weight": 1.0} -->

The proof is analogous to that of lem:model-eq.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Imposing prior structure", "weight": 1.0} -->

When estimating the second moment dynamics, estimating $\widetilde{W}$ is similar to before. However we now also estimate the mean of ${\mu}$. We provide details on estimation in sec:mean-id. Then we design a DR controller in sec:str-synthesis.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Mean identification", "weight": 1.0} -->

The measurement model [eq:measurement-model], under asm:model-structured is: $$x_{i+1} = \tucker{\ten{M}; z_i, (1, \widetilde{w}_i)}, \quad \forall i \in \N_{1:N}.$$ By expanding the Tucker product, [eq:measurement-model-structured] is equivalent to $y_{i+1} \dfn x_{i+1} - [A_1, B_1] z_i = \tucker{\widetilde{\ten{M}}; I_{n_x}, z_i, w_i}$. This is identical to the original measurement model [eq:measurement-model], but with a perturbed value of $x_{i+1}$ and truncated tensor $\widetilde{\ten{M}}$. Nonetheless, we can still identify $\widetilde{W}$ using [eq:ls-estimator].

<!-- chunk {"id": "body-0137", "role": "body", "section": "Mean identification", "weight": 1.0} -->

Moreover, identification of the mean is also possible: $$y_{i+1} = (\widetilde{\ten{M}} \btimes{2} z_i) ({\mu}_\star + \epsilon_i),$$ with $\epsilon_i = \widetilde{w}_i - {\mu}_\star$ a zero-mean error term and with ${\mu}_\star$ the true value of the mean ${\mu}$.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Mean identification", "weight": 1.0} -->

A more formal proof is provided in Appendix[app:identification].

<!-- chunk {"id": "body-0139", "role": "body", "section": "Mean identification", "weight": 1.0} -->

The ambiguity set is valid in the following sense: Let $\op{E}_\star$ denote the true moment dynamics and let asm:data[asm:model-structured] hold. Then with probability at least $1 - \delta_{\mu} - \delta_W$: $$\exists W \in \mmathcal{W} \colon \op{E}_{\star}(Z) = \op{E}(W; Z), \forall Z \in \sym{n_z}$$ with $\mmathcal{W}$ as in def:structured-ambiguity.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Mean identification", "weight": 1.0} -->

The full proof deferred to Appendix[app:identification]. It combines thm:error-bound-full and lem:mean-dd with some triangle inequalities.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Control synthesis", "weight": 1.0} -->

Using the learned ambiguity set we can then proceed with control synthesis. thm:drlqrcp we cannot find the exact solution. Instead we solve a relaxed SDP by leveraging a result from robust optimization [Ben-Tal2000].

<!-- chunk {"id": "body-0142", "role": "body", "section": "Control synthesis", "weight": 1.0} -->

In the non-structured setting, we used thm:ric-sdp-primalto synthesize a controller by solving a SDP. There is however no guarantee that a feasible solution to that SDP produces a stabilizing controller. This is only guaranteed for the optimum.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Control synthesis", "weight": 1.0} -->

So instead we will consider: &\stt && P \sgeq 0, \, P - \adj{\op{E}_{K}}(P) \sgeq Q + \trans{K} R K.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Control synthesis", "weight": 1.0} -->

The second constraint is a Lyapunov inequality for $\op{E}_{K}(P)$, which is defined as $\op{E}(\Pi_K(\cdot))$ as in eq:clops. Hence any feasible $K$ is stabilizing by lem:stabcp.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Control synthesis", "weight": 1.0} -->

- $\rho(\op{E}_{K}) < 1$ for any feasible $K$; - $(P_\star, K_\star)$ is optimal and uniquely so if $X_0 \sgt 0$.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Control synthesis", "weight": 1.0} -->

Here $P_\star$ and $K_\star$ those of thm:cplqr.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Control synthesis", "weight": 1.0} -->

We can now robustify eq:sdp-stab. Specifically, we introduce the robust constraint $$P - \adj{\op{E}_{K}}(W; P) \sgeq Q + \trans{K} R K, \quad \forall W \in \mmathcal{W}$$ with $\mmathcal{W}$ as in def:structured-ambiguity and $\adj{\op{E}}_K(W; P) = \adj{\Pi_K}(\adj{\op{E}}(W; P))$ (similar to lem:opadj). The non-linear SDP [eq:sdp-stab]with this robust constraint is relaxed as stated below.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Control synthesis", "weight": 1.0} -->

Let $X_0 = C_0 \trans{C_0}$ denote the Cholesky Consider the SDP: &\minimize_{\Theta, \Gamma, \Phi, \Psi, \Lambda}&\qquad& \tr[\Phi] \\&\stt&& \Theta \sgt 0, \Phi \sgt 0, \Psi \sgt 0, \Lambda \sgt 0, \\\Phi & \trans{U_0} \\ U_0 & \Theta \end{bmatrix} \sgeq 0, \, \begin{bmatrix} \Lambda & \beta_\mu \trans{\opm{F}} \\ \beta_\mu \opm{F} & I \kron \Psi \end{bmatrix} \sgeq 0, \\&&& T \sgeq \blkdiag(\Lambda, 0, \Psi, 0, 0), where we use the linear map: $$T \dfn \begin{bmatrix} \Theta & \trans{\opm{F}} &

<!-- chunk {"id": "body-0149", "role": "body", "section": "Control synthesis", "weight": 1.0} -->

\trans{\hat{F}} & \Theta & \trans{\Gamma} \\\opm{F} & \bar{\Sigma}^{-1} \kron \Theta \\asm:data[asm:model-structured], let $\op{E}_{\star}$ denote the true second moment dynamics as in eq:dynsm-structured and $\Pi_K$ the closed-loop policy as in eq:clops. Then, given a feasible $(\Theta, \Gamma)$, the pair $(P, K)$ with $P = \Theta^{-1}$ and $K = \Gamma \Theta^{-1}$ satisfies

<!-- chunk {"id": "body-0150", "role": "body", "section": "Control synthesis", "weight": 1.0} -->

- $\rho(\op{E}_{\star}(\Pi_K(\cdot))) < 1$; and - $\tr[\Phi] \geq \tr[P X_0] \geq \mathrm{val}eq:lqrcp = \mathrm{val}eq:slqr$first ineq. is eq., with probability at least $1 - \delta_W - \delta_\mu$.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Control synthesis", "weight": 1.0} -->

The proof is similar to that of [Coppens2019]. Note that $\adj{\op{E}}_K(P) = \adj{\Pi_K}(\adj{\op{E}}(P))$ by lem:opadj.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Control synthesis", "weight": 1.0} -->

$$P - \adj{\Pi_K}(\adj{\op{E}}(W; P)) \sgeq \adj{\Pi_K}(H),$$ with $H = \blkdiag(Q, R)$. We then plug in the specific form of $W$ as described in def:structured-ambiguity. That is $W = \blkdiag(0, \Sigma) + (1, \mu) \trans{(1, \mu)}$. Thus the left-hand side of [eq:rob-lmi-0] becomes $$P - \adj{\Pi_K}(\adj{\op{E}}(\blkdiag(0, \Sigma; P))) - \adj{\Pi_K}(\adj{\op{E}}(\mu_0 \trans{\mu_0}; P)),$$ where we introduced $\mu_0 = (1, \mu)$.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Control synthesis", "weight": 1.0} -->

Then, using these facts and the definition of $\opm{F}$ and $F_1$, after multiplying eq:rob-lmi-stab:b on the left and right side with $\Theta$ results: W &- \trans{[F_1; \opm{F}]}(\mu_0 \kron I) P (\trans{\mu_0} \kron I) [F_1; \opm{F}] \\&-\trans{\opm{F}} (\bar{\Sigma} \otimes I) \opm{F} \sgeq \Theta Q \Theta + \trans{\Gamma} R \Gamma, for all $(\mu \in \{\hat{\mu}\} + r_\mu \ball{n_w})$.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Control synthesis", "weight": 1.0} -->

Applying Schur complements and introducing $\theta = (\hat{\mu} - \mu)/r_\mu$, allows us to rewrite the final display as an inequality of the type $\mathcal{U}[\beta_\mu] \sgeq 0$ in lem:rob-sdp, with $T$as in the theorem above. Applying the Lemma gives the second and third LMI. lem:rob-sdp, a feasible pair $(\Theta, \Gamma)$ produces a pair $(P, K)$ that is feasible for the robust constraint [eq:rob-lmi-stab]. Since eq:rob-lmi-stab holds for all $W \in \mmathcal{W}$ it holds for $\op{E}_{\star}$ provided that $\exists W \in \mmathcal{W}$ such that $\op{E}_\star(Z) = \op{E}(W; Z)$ for all $Z$, which is true with probability at least $1 - \delta_\mu - \delta_W$.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Control synthesis", "weight": 1.0} -->

The first constraint in the final SDP $$\Phi \sgeq \trans{U_0} \Theta^{-1} \trans{U_0},$$ by a Schur complement. So $\tr[\Phi] \geq \tr[\trans{U_0} \Theta^{-1} \trans{U_0}]= \tr[X_0 P]$. Combined with the previous argument about feasibility and thm:sdp-stab:b, we prove (ii).

<!-- chunk {"id": "body-0156", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

In this section we numerically investigate the methods developed in this paper. We begin with the simple case of repeated *initialization (cf. rem:asm), comparing both the case where the modes are known and where they are not, i.e. the model-free setting. We show how, in the first setting, our bounds are sufficiently tight to enable control synthesis. Next we use data generated using rollout to produce similar estimates and we highlight the differences and challenges associated with doing so. We also show that experimentally our method also works when using only a single trajectory, although theoretical guarantees are not yet available in this setting. We also compared to the averaging rollout approach. Finally, we show how structural information can be exploited to get tighter estimates of the uncertainty.*In the technical report we compare with the averaging rollout approach in and show how structural information can be exploited to get tighter estimates of the uncertainty.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Accuracy of the estimate and bounds", "weight": 1.0} -->

We consider the case $n_x = 2$ and $n_u = 1$ with modes: \end{bmatrix}, \, A_2 = \begin{bmatrix} \end{bmatrix}, \, A_3 = \begin{bmatrix} \end{bmatrix}, \, B_3 = \begin{bmatrix} and $B_1 = B_2 = 0$. The disturbance is sampled uniformly from the ball $\{w \in \Re^3 \colon \nrm{w - \mu}_2 \leq 0.25\}$ To generate measurements we sample a $z_0 = (x_0, u_0)$ uniformly from an Euclidean ball of radius one and then propagate the dynamics by one step to get a measurement $x_1$, i.e. using repeated *initialization as in rem:asm. From this data, an estimate $\hat{W}$ and associated radius $\beta_W$ are determined as prescribed in thm:error-bound-full.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Accuracy of the estimate and bounds", "weight": 1.0} -->

To empirically quantify the accuracy of the scheme, the procedure above is repeated $M = 100$correct? times for each sample count $N$. For each estimate we compute $\nrm{\hat{W} - W_\star}_2$ and $\beta_W$. A confidence plot is provided in fig:toy. The middle plot depicts the result when $\ten{M}$ is selected, based on true mode info (i.e. $[\ten{M}]_{::i} = [A_i, B_i]$ for $i=1,2,3$); and the right-most plot uses the model-free case (i.e. $\ten{M}_{} = I$).

<!-- chunk {"id": "body-0159", "role": "body", "section": "Accuracy of the estimate and bounds", "weight": 1.0} -->

$W_\star$ in the first setting by noting that $\E[w\trans{w}] = r^2_w I_{n_w} / (n_w + 2)$ when $w$ is sampled uniformly from $\{w \in \Re^{n_w} \colon \nrm{w}_2 \leq r_w\}$ which can be verified by symmetry and solving a simple integral and applying the appropriate To shift the ball we shift $\widetilde{w} = w + \mu$. Hence $\E[\widetilde{w} \trans{\widetilde{w}}] = W_\star + \mu \trans{\mu}$.. Similarly, $W_\star$ for the model-free case is then recovered by applying the transformation in The left-most plot depicts the error when $\hat{W}$ is estimated directly from measurements of $w$ and the bound is as in lem:dd-moment. It is clear from the figure that the empirical error does not increase much when we do not directly observe the disturbance at least for this simple model.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Accuracy of the estimate and bounds", "weight": 1.0} -->

Instead the main loss is in the bound, which is about an order of magnitude looser than the direct sample case. This is to be expected however and, as we confirm later using DR synthesis, the bounds are still practical in low-dimensional settings.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Accuracy of the estimate and bounds", "weight": 1.0} -->

Error in moment estimation using repeated initialization: (left) when directly observing the disturbance; (mid) when using the true modes in $\ten{M}$; (right) when using no mode information, i.e. model-free. The dashed line depicts the radius predicted by thm:error-bound-full. Each colored area is a $0.1$ confidence interval surrounding the median.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Accuracy of the estimate and bounds", "weight": 1.0} -->

The middle and right-most plot depict the use of prior information and the model-free case respectively. The fact that $W_\star$ is not the same for both cases implies that the absolute errors are dissimilar. For a fair comparison, we additionally use the estimated second moment dynamics $\op{E}$ as in eq:dynsm\_. Specifically we plot $\nrm{\hat{\opm{E}} - \opm{E}_\star}_2/\nrm{\opm{E}_\star}_2$ where $\hat{\opm{E}}$ is the matrix associated with the estimated dynamics and $\opm{E}_\star$ its true value. These are computed using cor:cpadj. Note that $\opm{E}_{\star}$ is the same independent of the selected $\ten{M}$. fig:toy-operatorshows the result.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Accuracy of the estimate and bounds", "weight": 1.0} -->

Estimation accuracy of matrix of second order dynamics and comparison between model-free and true mode based estimation. Each colored area is a $0.1$ confidence interval surrounding the median.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Accuracy of the estimate and bounds", "weight": 1.0} -->

It is clear that, for the low-dimensional example considered here, exploiting prior mode information has no significant advantage when it comes to estimation accuracy. Instead the main advantage is a smaller ambiguity set. When using the model-free approach, the control synthesis problem remains infeasible for any tested sample count. That is, the ambiguity set exceeds the minimum size that can be stabilized by a single controller. When exploiting the prior information encapsulated in the modes, this is not the case.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Accuracy of the estimate and bounds", "weight": 1.0} -->

We can quantify the size of the ambiguity set through controller synthesis as in thm:drlqrcp. The performance of a gain $\hat{K}$ is measured through the infinite horizon cost achieved on the true system. This cost equals the optimum of the following SDP, by prop:lyapcp and lem:opadj, $$\min_{P} \, \{\tr[P X_0] \colon P - \adj{\Pi_{\hat{K}}}(\adj{\op{E}_{\star}}(P)) \sgeq \blkdiag(Q, R), \, P \sgeq 0 \}.$$ We select $X_0 = I$ here and in thm:ric-sdp-primal for control synthesis. Also let $Q = I$ and $R = 10$. The relative error with the true optimum of eq:slqr is then a metric for the accuracy of the ambiguity set. The result is depicted in fig:toy-cost.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Accuracy of the estimate and bounds", "weight": 1.0} -->

Note that the rate is as predicted in thm:sample-complexity.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Accuracy of the estimate and bounds", "weight": 1.0} -->

Evaluation of suboptimality of DR control synthesis. The colored area is a $0.1$ confidence interval surrounding the median.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Accuracy of the estimate and bounds", "weight": 1.0} -->

The dashed line in fig:toy-cost depicts the cost for the trivial ambiguity, which only uses $\nrm{w}_2 \leq r_w$ implying $\nrm{W_\star}_2 \leq r_w^2$. This constraint is also used to synthesize a controller with thm:drlqrcp. We say that the learned ambiguity set is informativewhen the performance of the associated controller improves upon the trivial one.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Accuracy of the estimate and bounds", "weight": 1.0} -->

Repeated initialization is not realistic in practice, since it assumes we can directly select all states of the system. Rollout instead initializes the system at some easily realizable initial state and then applies a sequence of control actions to excite the system. We use the state $x_0 = $ and use the control law $u_t = [-0.5, -0.2] x_t + \delta_t$ with $\delta_t$ sampled uniformly from a Euclidian ball of radius $35$ at each time step to integrate the dynamics for $T = 25$ time steps. Then $z_i = (x_{T-1}, u_{T-1})$ and $x_{i+1} = x_T$ are used as data points (cf. rem:asm) for $i=1, \dots, N$. Here $N$is the amount of rollouts, which we also refer to as the sample count.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Accuracy of the estimate and bounds", "weight": 1.0} -->

Similarly to before we can evaluate the accuracy of the estimate empirically, by resampling data sets and computing the errors. The result is depicted in fig:toy-rollout. Comparing with fig:toy we see, as expected, that estimation is more challenging when using rollout data. This is likely explained by the distribution of $z_i$ being less suitable for identification as discussed in rem:mixed Empirical result for toy problem using rollout data: (left) using the tail of $\#$nsamples rollouts of length $25$, with predicted radius as a dashed line; (right) using one rollout of length $\#$nsamples. Each colored area is a $0.1$ confidence interval surrounding the median.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Accuracy of the estimate and bounds", "weight": 1.0} -->

The right plot in fig:toy-rollout also depicts the empirical error when we simply use one rollout of length $T = N$. So the data is then $(x_i, u_i)$ and $x_{i+1}$ for $i\in\N_{0:N-1}$. It is clear that the estimate becomes more accurate when the trajectory length is increased, showing at least empirically that our approach can also work for single trajectory identification. This was also observed for a similar setup in [Di2021], yet a convergence proof and associated conditions on the exciting inputs are still unavailable (cf. rem:asm).

<!-- chunk {"id": "body-0172", "role": "body", "section": "Averaged rollouts approach", "weight": 1.0} -->

Comparison of three system identification approaches: (tail) using only the tail of each rollout; (full) using the full rollout; (averaging) when trajectories are averaged over rollouts. Each colored area is a $0.1$ confidence interval surrounding the median.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Averaged rollouts approach", "weight": 1.0} -->

In this part, we compare our approach with that of [Xing2020,Xing2021]. We will refer to this approach as the averaging rollout approach (contrasting our least-squares approach). In essence, this approach identifies the second moment dynamics [eq:dynsm\_] directly by using a sample average to construct a single moment trajectory $(Z_t, X_t)$. The second moment dynamics are then estimated using standard identification techniques from LTI identification.

<!-- chunk {"id": "body-0174", "role": "body", "section": "Averaged rollouts approach", "weight": 1.0} -->

We consider a dynamical system similar The dynamics in are defined differently. Constructing an exact equivalent that also satisfies asm:model is challenging. So instead the simpler system we consider is only approximately equivalent. to the one considered in [Xing2021]. Specifically \end{bmatrix}, A_2 = \begin{bmatrix} \end{bmatrix}, A_3 = \begin{bmatrix} \end{bmatrix}, \\ A_4 &= \begin{bmatrix} \end{bmatrix}, A_5 = \begin{bmatrix} \end{bmatrix}, \\ \trans{B_1} &= {\begin{bmatrix} \end{bmatrix}}, \, \trans{B_6} = {\begin{bmatrix} \end{bmatrix}}, \, \trans{B_7} = {\begin{bmatrix} The matrices $A_i$ and $B_i$ left unspecified are assumed zero.

<!-- chunk {"id": "body-0175", "role": "body", "section": "Averaged rollouts approach", "weight": 1.0} -->

We then sample the disturbance uniformly from a degenerate ellipse such that $W_\star = \diag(1, 0.15, 0.08, 0.02, 0.08, 0.05, 0.2)$ and $[w_t]_1 = 1$ for all $t \in \N$.

<!-- chunk {"id": "body-0176", "role": "body", "section": "Averaged rollouts approach", "weight": 1.0} -->

We then generate rollouts as in [Xing2021] and again evaluate the estimation accuracy in terms of $\opm{E}$. fig:tsummers shows the result. The rollout length was selected as $T = 12$and the horizontal axis tracks the amount of rollouts. In the averaging approach, the inputs should not only be random, but their distributions as well. This explains the high variance in the estimates.

<!-- chunk {"id": "body-0177", "role": "body", "section": "Averaged rollouts approach", "weight": 1.0} -->

The worst error is achieved when we use only the tail of each rollout in our least-squares scheme, which makes sure our convergence guarantees still hold. The averaging approach performs marginally better, and the asymptotic rates are the same (as confirmed by the theory in One can expect that accuracy improves further when the rollout length The analysis performed in however confirms an opposite result. This is likely due to conservativeness in their analysis.. Note however that the approach of [Xing2021]does not come with a tight error analysis. If theoretical guarantees are not critical, we can similarly to the single trajectory case considered above, also add other states in the rollout and use the full data set. The resulting estimate clearly outperforms the averaging result. Intuitively this is explained by the latter losing information by averaging.

<!-- chunk {"id": "body-0178", "role": "body", "section": "Averaged rollouts approach", "weight": 1.0} -->

It is also important to note that the scheme, as introduced in [Xing2021] does not support correlation between $A(w)$ and $B(w)$ (as in our first example). Extending the averaging scheme to support this is relatively trivial.

<!-- chunk {"id": "body-0179", "role": "body", "section": "Exploiting prior structure", "weight": 1.0} -->

We consider the structured dynamics [eq:dyn-structured] with \end{bmatrix}, \, B_1 = \begin{bmatrix} \end{bmatrix}, \, A_3 = \begin{bmatrix} \end{bmatrix}, \, B_4 = \begin{bmatrix} The matrices $A_i$ and $B_i$ left unspecified are assumed zero. The disturbance is distributed uniformly on $\{w \in \Re^3 \colon \nrm{w}_2 \leq 0.05\}$ and data is generated using repeated initialization, analogously to the procedure used in sec:toy. We then estimate $\hat{W}$ and $\hat{\mu}$ using the procedure in sec:structural. The empirical error and the predicted radii are then predicted in fig:struct-est.

<!-- chunk {"id": "body-0180", "role": "body", "section": "Exploiting prior structure", "weight": 1.0} -->

Error in moment estimation using repeated initialization and prior structure: (left) the second moment estimation error; (right) the mean estimation error. The dashed lines depict the predicted radius. Each colored area is a $0.1$ confidence interval surrounding the median.

<!-- chunk {"id": "body-0181", "role": "body", "section": "Exploiting prior structure", "weight": 1.0} -->

Finally, we also evaluate the size of the ambiguity set by using the control synthesis procedure of sec:str-synthesis. The LQR problem is tuned identically to before with $X_0 = I$, $Q = I$ and $R = 10$. We again compare with the true optimum and the trivial controller recovered when using only $\nrm{\mu}_2 \leq r_w$ and $\nrm{W_\star}_2 \leq r_w^2 I$ (the transformation to an ambiguity set like def:structured-ambiguity is analogous to the data-driven case). The resulting suboptimality plot is depicted in fig:struct-cost. Note that, the horizontal axis starts at $N = 20$. For fewer samples, the synthesis problem is infeasible. It is immediately clear how the structured prior information is exploited by our scheme by noting how little samples are required before the scheme improves upon the trivial controller. Also note that, even though we only proved the $1/N$ rate for the non-structured case, the same decrease is observed here.

<!-- chunk {"id": "body-0182", "role": "body", "section": "Exploiting prior structure", "weight": 1.0} -->

The same observation was made in [Coppens2019].

<!-- chunk {"id": "body-0183", "role": "body", "section": "Exploiting prior structure", "weight": 1.0} -->

Evaluation of suboptimality of DR control synthesis with structured prior information. The colored area is a $0.1$ confidence interval surrounding the median.

<!-- chunk {"id": "body-0184", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We developed a novel system identification scheme for linear dynamics with state- and input-multiplicative noise. The resulting estimators are shown to converge at a $1/\sqrt{N}$ rate, with $N$ the number of samples, when the data is generated either using rollout or through repeated initialization of the dynamics. We illustrated empirically that for simple dynamics the constants in our bounds are practical, i.e. they can be used for DR control synthesis. Moreover, the tightness of the bound is similar to that of a usual matrix Hoeffding bound. Also the DR control synthesis problem was shown to converge at a $1/N$rate to the true optimum.

<!-- chunk {"id": "body-0185", "role": "body", "section": "Conclusion", "weight": 1.5} -->

For more complex dynamics it is likely that the bounds are not sufficiently tight to enable DR control synthesis. In that case either bootstrapping can be exploited as in [Dean2019,Delage2010] or the DR scheme can be used to identify the robustness of the certainty equivalent controller as in [Gravell2020].

<!-- chunk {"id": "body-0186", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We additionally illustrated how knowledge about deterministic terms can be exploited to accelerate the identification process and tighten the associated bounds (referred to as structured information). An additional DR control synthesis scheme was also presented, which exploits the tighter bounds. The scheme was empirically shown to also converge to the true optimum at a $1/N$rate.

<!-- chunk {"id": "body-0187", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Moreover experiments illustrated that the identification scheme functions well when data is gathered from a single trajectory and compared the results with the averaging rollout identification scheme of From these tests it is clear that correlation between errors does not accumulate when using single trajectory data. A formal proof of this fact and a sample complexity analysis however proved challenging and is considered an open problem for future work.]Peter Coppensis a PhD researcher at the Department of Electrical Engineering (ESAT) of KU Leuven, Belgium and a recipient of a FWO fundamental research fellowship. He received his M.Eng. in Mathematical Engineering from the KU Leuven in 2019. His current research interests lie in learning control, enabled by distributionally robust optimization. Specifically its use in model predictive control an safety critical applications.]Panagiotis (Panos) Patrinosis associate professor at the Department of Electrical Engineering (ESAT) of KU Leuven, Belgium. In 2014 he was a visiting professor at Stanford University. He received his PhD in Control and Optimization, M.S. in Applied Mathematics and M.Eng. in Chemical Engineering from the National Technical University of Athens in 2010, 2005 and 2003, respectively.

<!-- chunk {"id": "body-0188", "role": "body", "section": "Conclusion", "weight": 1.5} -->

After his PhD he held postdoc positions at the University of Trento and IMT Lucca, Italy, where he became an assistant professor in 2012. His current research interests lie in the intersection of optimization, control and learning. In particular he is interested in the theory and algorithms for structured nonconvex optimization as well as learning-based, model predictive control with a wide range of applications including autonomous vehicles, machine learning and signal processing.

<!-- chunk {"id": "body-0189", "role": "body", "section": "Proofs for preliminaries", "weight": 1.0} -->

Thus we have shown the required result. lem:tensor-kron to show Let $\op{S}(W; X)$ be a CP operator parameterized as in eq:cp-tensor-def with some $\ten{V}$.

<!-- chunk {"id": "body-0190", "role": "body", "section": "Proofs for preliminaries", "weight": 1.0} -->

This, through reversal of the steps above enables proving the results. prop:kronunfold $(\trans{p} \ten{V}_{} (w \kron x))^2 = \tucker{\ten{V}; p, x, w}^2$. Unfolding along $n = 2$ and $3$ shows the other equalities in prop:cpunfold:a. Moreover since $\tucker{\ten{V}; p, x, w}^2 = \tucker{\ten{V}; p, x, w} \kron \tucker{\ten{V}; p, x, w}$ we can apply lem:tensor-kron to analogously get prop:cpunfold:b. Finally note that $\trans{Q}_{q_1} Q_{n_p} \vec{(P)} = \trans{Q}_{n_p} \svec{(P)}$ since $P \in \sym{n_p}$ and similarly for $X$ and $W$.

<!-- chunk {"id": "body-0191", "role": "body", "section": "Proofs for preliminaries", "weight": 1.0} -->

From [Kolda2009] $\ten{T} \btimes{1} \trans{Q} x = (\ten{T} \ttimes{1} Q) \btimes{1} x$, which combined with the definition of $\ten{V} \skron \ten{V}$ shows prop:cpunfold:c.

<!-- chunk {"id": "body-0192", "role": "body", "section": "Proofs for preliminaries", "weight": 1.0} -->

Proof of cor:cpadj We can directly apply prop:cpunfold:b to show the expression for $\adj{\op{S}}(W; X)$. For $\opm{S}$ note that $\tr[P \op{S}(W; X)] = \trans{\svec}(P) \opm{S} \svec(X)$.

<!-- chunk {"id": "body-0193", "role": "body", "section": "Proofs for preliminaries", "weight": 1.0} -->

We can rewrite the Tucker operator in prop:cpunfold:c as &\tucker{\ten{V} \skron \ten{V}; \svec(P), \svec(X), \svec(W)} \\&\qquad = (((\ten{V} \skron \ten{V}) \btimes{3} \svec(W)) \btimes{1} \svec(P)) \svec(X) \\&\qquad = \trans{\svec(P)} ((\ten{V} \skron \ten{V}) \btimes{3} \svec(W)) \svec(X).

<!-- chunk {"id": "body-0194", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

This section gives proofs related to LQR. We begin by introducing some auxiliary operators and their adjoints: Let $\op{E}$ be as in eq:dynsm\_, ${\Pi}_K(X) = [I; K] X [I, \trans{K}]$, Consider the Lyapunov operator $\op{L}(Z) = X - \op{E}(Z)$ and $\op{L}_K(X) = X - \op{E}_K(X)$. Here $X$ is the top-left $n_x \times n_x$ block of $Z$.

<!-- chunk {"id": "body-0195", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

Only elementary algebra, lem:tencp and cor:cpadj are used.

<!-- chunk {"id": "body-0196", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

Any $Z \sgeq 0$ can be partitioned as: X & X \trans{K} \\ K X & K X \trans{K} + \Delta for $\Delta \sgeq 0$ and $X \sgeq 0$.

<!-- chunk {"id": "body-0197", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

Let $Z = [X, V; \trans{V}, U]$. By [Boyd2004] $Z \sgeq 0$ iff $$X \sgeq 0, \quad \img{V} \subseteq \img{X}, \quad U - \trans{V} X^\dagger V \sgeq 0.$$ So there exists a $K$ s.t. $V = X \trans{K}$ and $\Delta = U - \trans{V} \pinv{X} V = U -\trans{K} X K \sgeq 0$ *Proof of thm:cpmulteq We use asm:model and lem:model-eq to consider [eq:dynten] instead of [eq:dyn] without loss of generality. We start with a feasible sequence for eq:slqr and construct an (equivalent) feasible sequence for eq:lqrcp.

<!-- chunk {"id": "body-0198", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

Let $H = \blkdiag(Q, R)$, $Z_t = \E[z_t \trans{z_t}] \sgeq 0$ with $z_t = (x_t, u_t)$ and $x_t, u_t$ satisfying [eq:dynten]. Note that, by eq:dynsm\_, any sequence $Z_t$ constructed as such satisfies the constraints of [eq:lqrcp].

<!-- chunk {"id": "body-0199", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

$$\E\left[\ssum_{t=0}^\infty \trans{x}_t Q x_t + \trans{u}_t R u_t \right] = \ssum_{t=0}^\infty \tr[H Z_t].$$ So the cost of $(x_t, u_t)$ for eq:slqr equals that of the constructed $Z_t$ in eq:lqrcp. So $\mathrm{val}eq:lqrcp \leq \mathrm{val}eq:slqr$.

<!-- chunk {"id": "body-0200", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

Next, we argue that for any sequence feasible for eq:lqrcp, we can construct a sequence $z_t = (x_t, u_t)$ feasible for eq:slqr. Note that for any $X \sgeq 0$ we can easily construct a random vector $x$ with $\E[x \trans{x}] = X$. So let $x_0$ be such a vector for $X_0$. Then, by lem:z-partition, $Z_0$ can be partitioned as $[X_0, X_0\trans{K}_0; K_0 X_0, K_0 X_0 \trans{K}_0 + \Delta_0]$ with $\Delta_0 \sgeq 0$ for which we pick a random vector $\delta_0$. So if we take $u_0 = K_0 x_0 + \delta_0$ and $z_0 = (x_0, u_0)$ then $\E[z_0 \trans{z_0}] = Z_0$.

<!-- chunk {"id": "body-0201", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

Repeating the same argument starting at $x_1$ and continuing for all time steps allows us to construct a feasible trajectory for eq:slqr. Again by $\E[z_t \trans{z_t}] = Z_t$ and eq:cost-eq-cp-slqr the cost for both trajectories is the same. Thus $\mathrm{val}eq:lqrcp \geq \mathrm{val}eq:slqr$.

<!-- chunk {"id": "body-0202", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

We continue with proving auxiliary results for thm:cplqr. We first consider the finite horizon version of eq:lqrcp: &\minimize_{Z_t} &\quad& \sum_{t=0}^{N-1} \tr[Z_t H] + \tr[P X_N] \\&\stt && Z_t = \begin{bmatrix} \end{bmatrix} \sgeq 0, \\&&&X_{t+1} = \op{E}(Z_t), \quad \forall t \in \N_{0:N-1}.

<!-- chunk {"id": "body-0203", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

We prove the fundamental property linking Consider $\op{J}^N$ and $\op{R}$ defined in sec:lqr. Let Then $Z_t = \Pi_{K_{N-t-1}}(X_t)$ for $t \in \N_{0:N-1}$ achieves the minimum: The result follows from dynamic programming (DP) [Bertsekas2005V1]. Starting from $\op{J}^0(P; X_0) = \tr[P_0X_0]$, with $P_0 = P$, Note that $\tr[P_{k} \op{E}(Z)] = \tr[\adj{\op{E}}(P_k) Z]$ by definition of the adjoint. We use lem:opadj to write $\adj{\op{E}}$ in terms of $\adj{\op{F}}$, $\adj{\op{G}}$ and $\adj{\op{H}}$.

<!-- chunk {"id": "body-0204", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

Introducing $X, K$ and $\Delta$ to partition $Z$ as in lem:z-partition allows rewriting the cost of [eq:bellman] (omitting constant terms) as: &\tr[\trans{(\adj{\op{H}}(P_{k}))} K X] + \tr[\adj{\op{H}}(P_k) X \trans{K}]\\&\quad + \tr[(R + \adj{\op{G}}(P_{k}))K X \trans{K}] + \tr[(R + \adj{\op{G}}(P_k)) \Delta], which is minimized uniquely at $\Delta = 0$, by noting that $R \sgt 0$ in conjunction with We can evaluate the gradient of the remaining terms with respect to $K$ using the identities in [Magnus2019]. This gives the following first-order optimality conditions: *This should hold for all $X \in \psd{n_x}$.

<!-- chunk {"id": "body-0205", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

Since $R \sgt 0$ this is the case iff For these values of $K$ and $\Delta$ we have $Z = \Pi_{K_k}(X)$, with $\Pi_{K_k}$ as in lem:opadj. Plugging into [eq:bellman]: &\quad = \tr[X \adj{\Pi}_{K_k}(H + \adj{\op{E}}(P_k))] = \tr[X \op{R}(P_k)], where the second equality follows from linearity and adjoints, while the third follows from lem:opadj and cancellation of the inverses in $K_k$. Iterating over $k$, repeatedly computing the optimal policy $K_k$ by the same procedure as usual in dynamic programming (cf. [Bertsekas2005V1]), completes the proof. Note that $k$ counts backwards in time, hence $K_{N-t-1}$ in $Z_t$.

<!-- chunk {"id": "body-0206", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

Result (i) is simply monotonicity of the Bellman operator [Bertsekas2005V2]. Specifically, by observing [eq:bellman] it is clear that the cost is larger for $P$ than for $P'$ since $\tr[P \op{E}(Z)] \geq \tr[P' \op{E}(Z)]$ for all $Z$. Hence the minimum is also larger. Moreover using eq:ric-alt gives $\tr[X \op{R}(P)] \geq \tr[X \op{R}(P')]$. Taking $X = x\trans{x}$ for any $x$ gives $\trans{x} \op{R}(P) x \geq \trans{x} \op{R}(P') x$ thus showing (i). Result (ii) follows from $H = \blkdiag(Q, R) \sgt 0$, causing the minimizer we computed for [eq:bellman] to be unique since it should satisfy eq:first-order.

<!-- chunk {"id": "body-0207", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

Next, we study the fixed point of the Riccati equation.

<!-- chunk {"id": "body-0208", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

Assume $H = \blkdiag(Q, R) \sgt 0$. Then, $\exists K \colon \rho(\op{E}_K) < 1$ implies

<!-- chunk {"id": "body-0209", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

The proof follows that of [Bertsekas2005V1].

<!-- chunk {"id": "body-0210", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

*(i) and $P = 0$ Let $K$ be a controller such that $\rho(\op{E}_K) < 1$. We will prove that $\lim_{k \to \infty} \op{R}^k(P) = P_{\star}$ is well defined by applying lem:monotone-convergence for which we should show for all $X$ that \tr[\op{R}^k X] &\leq \tr[\op{R}^{k+1} X], \, \forall k \in \N \text{ and } \\\lim_{k \to \infty} \tr[\op{R}^k X] &< +\infty.

<!-- chunk {"id": "body-0211", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

The first inequality follows by induction. To start the induction note that $\op{R} = \adj{\Pi}_{K_{0}}(H + \adj{\op{E}}) = \adj{\Pi}_{K_{0}}(H) \sgt 0$, where the first equality follows from eq:ric-alt. Then assume $\op{R}^{k+1} \sgeq \op{R}^{k}$. Taking $\op{R}$ on both sides and then using cor:ric-prop:a then proves the induction step.

<!-- chunk {"id": "body-0212", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

*(ii) Clearly $P_{\infty}$ derived in the previous step satisfies $\op{R}(P_{\infty}) = P_{\infty}$. This equality can be rewritten using eq:ric-alt as: $$P_\infty - \adj{\op{E}_{K_\star}}(P_{\infty}) = \adj{\op{E}_{K_\star}}(H) \sgt 0.$$ This is a Lyapunov equation. Therefore, by prop:lyapcp, $P_\infty$ is the unique solution to $\op{R}(P_{\infty}) = P_{\infty}$.

<!-- chunk {"id": "body-0213", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

*(iii) Stability follows directly from eq:ric-lyap and prop:lyapcp.

<!-- chunk {"id": "body-0214", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

The second inequality follows from the fact that $Z_t = \Pi_{K_{\star}}(X_t) = \Pi_{K_\star}(\op{E}_{K_\star}^t(X))$ is feasible for the problem in $\op{J}^N(P; X_0)$. From eq:ric-lyap and prop:lyapcp we get that the right-hand side of eq:squeezed-costs converges to $\tr[X_0 P_{\star}]$. This holds trivially for the sum. For the final term we use the fact that $\rho(\op{E}_{K_\star}) < 1$.

<!-- chunk {"id": "body-0215", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

We proceed by contradiction, assuming that $\op{R}^\infty(P) \nsgeq \op{R}^\infty$. Then, taking $X \sgt 0$, lem:trivialinequality implies $\tr[X (\op{R}^\infty(P) - \op{R}^\infty)] > 0$. This is a contradiction from what we showed earlier. Thus $\op{R}^\infty(P) = \op{R}^\infty$.

<!-- chunk {"id": "body-0216", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

We are now ready to prove the main LQR result: *Proof of thm:cplqr Stability follows directly from prop:lqr-infinite. Taking $N \to \infty$ in prop:lqr-finite shows (ii). Using [eq:ric-lyap] and prop:lyapcp gives $\tr[P_{\star} X_0] = \tr[H \ssum_{t=0}^{\infty} \op{E}^t_{K_{\star}}(X_0)]$. That is $Z_t = \Pi_{K_{\star}}(X_t)$ achieves the optimal cost.

<!-- chunk {"id": "body-0217", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

We conclude this section with the derivation of the SDP reformulations of the Riccati equation Proof of thm:ric-sdp-primal Introducing $\op{L}(Z) = X - \op{E}(Z)$ as in lem:opadj and its adjoint $\adj{\op{L}}$. It becomes clear from lem:opadj that the SDP in thm:ric-sdp-primal is equivalent to $$\minimize \, \{\tr[P (-X_0)] \colon \adj{\op{L}}(P) \sleq H, P \sgeq 0\}.$$ The Lagrangian dual of this SDP is [Balakrishnan2003] \end{bmatrix} \sgeq 0.

<!-- chunk {"id": "body-0218", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

The proof proceeds as follows: first strong duality is established; then feasibility is examined, proving (i); next optimality conditions are given for $X_0 \sgeq 0$; and finally the uniqueness of the solution is established for $X_0 \sgt 0$, proving (ii).

<!-- chunk {"id": "body-0219", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

*Strong duality Note that (i) $\exists Z \colon Z \nsgeq 0$, $Z_{22} - \op{L}(Z_11) = 0$ and $\tr[HZ_{11}] \sleq 0$, with $Z$ partitioned as in eq:dual; and (ii) $\exists P \colon P \sgt 0$ and $\adj{\op{L}}(P) \slt H$ are strong alternatives [Balakrishnan2003]. We can leverage lem:trivialinequality and $H \sgt 0$ to show that (i) holds only if $Z_{11} = 0$. Since $\op{L}$ is linear, this implies $Z_{22} = 0$. Therefore $Z = 0$ as well, which means that (i) can never hold. Therefore (ii) must hold and the primal problem is strictly feasible. Strong duality then follows by [Balakrishnan2003].

<!-- chunk {"id": "body-0220", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

*Feasibility Note that eq:dual is feasible iff there is some $Z_{11} \sgeq 0$ such that $\op{L}(Z_{11}) \sgeq X_0$. When the dynamics are stabilizable, then there is some $K$ such that $\rho(\op{E}_K) = \rho(\adj{\op{E}}_K) < 1$. Hence there exists an $X \sgt 0$ such that $\op{L}(\Pi_K(X)) = X - \op{E}_{K}(X) = X_0$ by prop:lyapcp, implying feasibility of $Z_{11} = \Pi_K(X)$. Therefore, by [Balakrishnan2003], the primal problem is bounded.

<!-- chunk {"id": "body-0221", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

prop:lyapcp, there is no $K, X$ such that $\op{L}(\Pi_K(X)) = X - \op{E}_{K}(X) = X_0 + Z_{22}$ for any $Z_{22} \sgeq 0$. Since, by lem:z-partition, any $Z_{11} \sgeq 0$ can be written as $Z_{11} = \Pi_K(X) + \blkdiag(\Delta, 0)$ for $\Delta \sgeq 0$ and $\op{L}(\Pi_K(X) + \blkdiag(\Delta, 0)) = \op{L}(\Pi_K(X)) - \op{E}(\blkdiag(0, \Delta)) \sleq \op{L}(\Pi_K(X))$.

<!-- chunk {"id": "body-0222", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

Thus there is no $Z_{11}$ such that $\op{L}(Z_{11}) = X_0 + Z_{22}$ and eq:dual is infeasible. This implies the primal problem is unbounded by [Balakrishnan2003].

<!-- chunk {"id": "body-0223", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

*Optimality From earlier, stabilizability results in feasibility of the dual. Note that $Z_{22} = \op{L}(Z_{11}) - X_0$ when $Z$ is feasible. So we only consider constraints on $Z_{11}$. By lem:z-partition, we can partition $Z_{11} \sgeq 0$ as with $X \sgeq 0$ and $\Delta \sgeq 0$. By complementary slack [Balakrishnan2003]: \end{bmatrix} X \begin{bmatrix} \end{bmatrix} \begin{bmatrix} Q - P + \adj{F}(P) & \trans{(\adj{\op{H}})}(P) \\ \adj{\op{H}}(P) & R + \adj{\op{G}}(P) & \quad + (R + \adj{\op{G}}(P)) \Delta = 0 for the optimum.

<!-- chunk {"id": "body-0224", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

Since $R \sgt 0$, the second term is zero iff $\Delta = 0$. Thus $Z_{11}$ solves the dual iff $Z_{11} = \Pi_K(X)$. $(Z_{11}, P) = (\Pi_K(X), P)$ with $X \sgt 0$ is then optimal iff \end{bmatrix} \begin{bmatrix} Q - P + \adj{F}(P) & \trans{(\adj{\op{H}})}(P) \\ \adj{\op{H}}(P) & R + \adj{\op{G}}(P) which holds iff $P = \op{R}(P)$ (i.e. $P = P_{\star}$) and $K = K_{\star}$. So $P_{\star}$is an optimal solution to the SDP, when it is bounded (i.e. the dual problem is feasible).

<!-- chunk {"id": "body-0225", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

*Uniqueness Assume $X_0 \sgt 0$. As shown before, $Z_{11} = \Pi_K(X)$ for some $X$. From feasibility we require that $X - \op{E}_K(X) \sgeq X_0 \sgt 0$. So $X \sgt 0$ holds. Therefore any pair of solutions $(Z_{11}, P)$ with $Z_{11} = \Pi_K(X)$ must satisfy eq:complementary-slack and, by earlier arguments $P = \op{R}(P)$ and $K = K_{\star}$.

<!-- chunk {"id": "body-0226", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

Next we prove the properties of *Proof of thm:sdp-stab Note that, by $H \sgt 0$, $\adj{\Pi}_K(H) = Q + \trans{K} R K \sgt 0$. Hence any feasible pair $(P, K)$ satisfies a Lyapunov equation for some $Q' \sgeq \adj{\Pi}_K(H)$. From lem:stabcp stability then follows and \forall X \colon \tr[PX] &= \tr[\ssum_{t=0}^{\infty} \op{E}^t_K(X) Q'] \\&\geq \tr[\ssum_{t=0}^{\infty} \op{E}^t_K(X) \adj{\Pi}_K(H)] \geq \op{J}^\star(X_0).

<!-- chunk {"id": "body-0227", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

[eq:ric-lyap], $(P_{\star}, K_{\star})$ are feasible for [eq:sdp-stab] and satisfy $\tr[P_{\star} X_0] = \op{J}^{\star}(X_0)$ by prop:lqr-infinite. Therefore this pair achieves the lower bound and is optimal. $X_0 \sgt 0$ and that there is a feasible $(P', K') \neq (P_{\star}, K_{\star}) \colon \tr[P' X_0] = \tr[P_{\star} X_0]$. By feasiblity and cor:ric-prop:b: $P' \sgeq \adj{\Pi}_{K'}(H + \adj{\op{E}}(P')) \sgeq \op{R}(P')$.

<!-- chunk {"id": "body-0228", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

So, by repeatedly applying cor:ric-prop:a we have $P' \sgeq \op{R}(P') \sgeq \op{R}^2(P) \sgeq \dots$. By induction we then have $P' \sgeq \lim_{k \to \infty} \op{R}^k(P') = P_{\star}$. Hence, by $X_0 \sgt 0$, $P' \neq P_{\star}$ and lem:trivialinequality we have $\tr[P' X_0] > \tr[P_{\star} X_0]$ which is a contradiction since we assumed $\tr[P'X_0] = \tr[P_\star X_0]$ before.

<!-- chunk {"id": "body-0229", "role": "body", "section": "Linear Quadratic Regulation", "weight": 1.0} -->

Thus $P' = \adj{\Pi}_{K'}(H + \adj{\op{E}}(P')) = \op{R}(P')$, which by cor:ric-prop:b and prop:lqr-infinite holds iff $(P', K') = (P_{\star}, K_{\star})$.

<!-- chunk {"id": "body-0230", "role": "body", "section": "Vector and matrix concentration", "weight": 1.0} -->

We extend the proof of [Coppens2021]. Let $X_i = V_i \Lambda_i \trans{V_i}$ be the eigenvalue decomposition.

<!-- chunk {"id": "body-0231", "role": "body", "section": "Vector and matrix concentration", "weight": 1.0} -->

Minimizing over $\theta$ gives the required result for $\lambda_1$ and $\lambda_d$. Taking a union bound gives the spectral norm bound.

<!-- chunk {"id": "body-0232", "role": "body", "section": "Vector and matrix concentration", "weight": 1.0} -->

Hence we have constructed a sequence of zero-mean, independent random variables $\{d_i\}_{i\in\N_{1:N}}$ that take their value a.s. in $[-[\gamma]_i + e_i, [\gamma]_i + e_i]$. Applying a classical Hoeffding bound [Boucheron2013] gives $$\prob[\ssum_{i=1}^{N} d_i \geq \beta] \leq \exp(-\beta^2/2\ssum_{i=1}^N \nrm{\gamma}_2^2),$$ where, as shown before, $\ssum_{i=1}^N d_i = \nrm{y}_2 - \E[\nrm{y}_2]$.

<!-- chunk {"id": "body-0233", "role": "body", "section": "Vector and matrix concentration", "weight": 1.0} -->

Plugging into [eq:meanbnd1] concludes the proof.

<!-- chunk {"id": "body-0234", "role": "body", "section": "Rank of random matrices", "weight": 1.0} -->

We introduce a fundamental lemma, regarding the span of random i.i.d. vectors [Eaton1973]: Given a sequence of i.i.d. copies $\{z_1, \dots, z_N\}$ of a random vector $z \colon \Omega \to \Re^d$ with $N \geq d$, the following statements are equivalent: $\forall w \in \Re^d$, $w \neq 0$, $\prob[\trans{w} z = 0] = 0$; Moreover if either (a) or (b) holds, then $\E[z \trans{z}] \sgt 0$.

<!-- chunk {"id": "body-0235", "role": "body", "section": "Rank of random matrices", "weight": 1.0} -->

The proof of [Eaton1973] stands in a more general setting then necessary. We provide a simplified proof for completeness. Without loss of generality we assume $N = d$. Let $Z_k \dfn [z_1, \dots, z_k]$ and $\set{B}[k]$ denote the We proceed by contradiction, so assume $\exists w \neq 0\colon \prob[\trans{w} z = 0] > 0$ and that (b) holds (i.e. $\prob[\set{B}[d]] = 1$). Note that $\prob[\neg \set{B}[d]]= \prob[\exists v \neq 0 \colon \trans{v} Z_d = 0]$ (i.e., the kernel of $\trans{Z_d}$ is nontrivial).

<!-- chunk {"id": "body-0236", "role": "body", "section": "Rank of random matrices", "weight": 1.0} -->

&\prob[\exists v \neq 0 \colon \trans{v} Z_d = 0] \\&\quad \geq \prob[\trans{w} Z_d = 0] = \Pi_{i=1}^d \prob[\trans{w}z_i = 0] > 0, where the first inequality follows by fixing $v = w$, the equality follows by independence and the final inequality follows by the assumption that (a) does not hold. So $\prob[\set{B}[d]] \neq 1$ and we have shown (a) $\Leftarrow$ (b) by contradiction.

<!-- chunk {"id": "body-0237", "role": "body", "section": "Rank of random matrices", "weight": 1.0} -->

We can decompose $\prob[\set{B}[d]]$ into \prob[z_d \notin \img(Z_{d-1}) \mid \set{B}[d-1]] \cdot \prob[\set{B}[d-1]] We know that $\exists w \in \ker(\trans{Z}_{d-1})/\{0\}$ since $Z_{d-1}$ is not full rank. Hence the first factor is equal to $\prob[\trans{w} z_d \neq 0 \mid \rk(Z_{d-1}) = d-1]$, where $w$ depends on $Z_{d-1}$. This factor equals $1$ since (a) holdsif this is iff. we can shorten the proof.

<!-- chunk {"id": "body-0238", "role": "body", "section": "Rank of random matrices", "weight": 1.0} -->

We can repeatedly apply the same decomposition to the second factor until we arrive at $\prob[\rk(z_1) = 1]$, which equals to $1$ since (a) also implies $\prob[z_1 = 0] = 0$. Hence $\prob[\rk(Z_d) = d] = 1$so (b) holds.

<!-- chunk {"id": "body-0239", "role": "body", "section": "Rank of random matrices", "weight": 1.0} -->

We can consider some examples of distributions satisfying (a). A clear sufficient condition is that the density of $z$is dominated by the Lebesgue measure. Another example are uniform distributions over spheres. Meanwhile, any atomic measure will not satisfy (a).

<!-- chunk {"id": "body-0240", "role": "body", "section": "Rank of random matrices", "weight": 1.0} -->

With the setup of lem:rank-condition, assume that $z$ is dominated by the Lebesgue measure. Then, if $N \geq \sd{d}$, $$\prob[\rk([z_1 \skron z_1, \dots, z_N \skron z_N]) = \sd{d}] = 1$$ and $\E[(z \trans{z}) \skron (z \trans{z})] \sgt 0$.

<!-- chunk {"id": "body-0241", "role": "body", "section": "Rank of random matrices", "weight": 1.0} -->

Applying lem:rank-condition to $z \kron z$ instead of $z$ gives: $$\prob[\trans{w}(z \skron z) = 0] = 0, \quad \forall w \in \Re^{\sd{d}}, w \neq 0.$$ The condition $\trans{w}(z \skron z) = 0 \Leftrightarrow \trans{z} W z$ describes the roots of a quadratic polynomial, with $W = \unsvec(w) \in \sym{d}$. It is well knowncite that such a set is of Lebesgue measure zero, if the polynomial is not identically zero. Since $W \in \sym{d}$, $\trans{z}W z = 0$ for all $z$ iff $W = 0$. Hence, by our domination assumption, $\prob[\trans{w}(z \skron z) = 0] = 0$ follows.

<!-- chunk {"id": "body-0242", "role": "body", "section": "Rank of random matrices", "weight": 1.0} -->

Applying lem:rank-condition and using $(z \kron z) \trans{(z \kron z)} = (z\trans{z}) \kron (z \trans{z})$ completes the proof. We can apply similar reasoning to prove the second result.

<!-- chunk {"id": "body-0243", "role": "body", "section": "Rank of random matrices", "weight": 1.0} -->

We could have directly used [eq:exact-kron-rank] as the assumption on $z$ to get a tight result. We avoided doing so, since [eq:exact-kron-rank] is more difficult to verify in practice.

<!-- chunk {"id": "body-0244", "role": "body", "section": "Identification model", "weight": 1.0} -->

We begin by showing some auxiliary results.

<!-- chunk {"id": "body-0245", "role": "body", "section": "Identification model", "weight": 1.0} -->

*For two matrices $U$, $V$ of conformable dimensions, with $\pinv{U} U = I$, we mimic \pinv{V} V &= \pinv{V} \pinv{U} U V \labelrel={step:moorp} \pinv{V} \pinv{U} (UV) \trans{(UV)} \pinv{(\trans{(UV)})} \\&= \pinv{V} V \trans{V} \trans{U} \pinv{(\trans{(UV)})} \\&\labelrel={step:moorpb} \trans{V} \trans{U} \pinv{(\trans{(UV)})} = \pinv{(UV)} (UV), where both [step:moorp] and [step:moorpb] use $\pinv{A} A \trans{A} = \trans{A}$ (cf. [Greville1966]). $\opm{Z}_N$ then gives the required result.

<!-- chunk {"id": "body-0246", "role": "body", "section": "Identification model", "weight": 1.0} -->

Next, we derive properties of $\op{W}$ and $\op{H}_i$ defined in [eq:hopmat].

<!-- chunk {"id": "body-0247", "role": "body", "section": "Identification model", "weight": 1.0} -->

The first result (i) follows by using prop:kronunfold to write &\trans{(\ten{W} \btimes{2} (z \skron z))} (\ten{W} \btimes{2} (z \skron z)) \\&\quad = \ten{W}_{} [(z \skron z) \kron I] [\trans{(z \skron z)} \kron I] \trans{\ten{W}}_{}.

<!-- chunk {"id": "body-0248", "role": "body", "section": "Identification model", "weight": 1.0} -->

Using $(A \kron X)(B \kron Y) = AB \kron XY$ [DeKlerk2002] and [DeKlerk2002] to argue $(z \skron z) \trans{(z \skron z)} = (z \trans{z} \skron z\trans{z})$, proves (i). We can show (ii) by using [eq:zmat-stacked] and applying similar tricks.

<!-- chunk {"id": "body-0249", "role": "body", "section": "Identification model", "weight": 1.0} -->

Finally (iii) is shown by using (i) to argue \nrm{\op{W}}_2 &= \sup_{z \in \ball{}} \{\nrm{(\ten{W} \btimes{2} (z \skron z))}_2^2\} \nonumber \\&= \sup_{x, w, z \in \ball{}} \{ (\trans{x} (\ten{W} \btimes{2} (z \skron z)) w)^2\}, where we used the variational representation of the spectral norm for the second equality and with $x \in \Re^{\sd{n_x}}$, $w \in \Re^{\sd{n_w}}$ and $\ball{}$ the unit Euclidean ball of generic dimension.

<!-- chunk {"id": "body-0250", "role": "body", "section": "Identification model", "weight": 1.0} -->

The squared quantity can be rewritten by noting \trans{x} (\ten{W} \btimes{2} (z \skron z)) w = \tucker{\ten{W}; x, z \skron z, w}.

<!-- chunk {"id": "body-0251", "role": "body", "section": "Identification model", "weight": 1.0} -->

Noting that $\trans{(z \skron z)} (z \skron z) = \nrm{z}_2^4$ implies that we can relax eq:vartnorm to take the supremum over $z' \in \ball{\sd{n_z}}$ instead of over $z \skron z$. So $$\nrm{\op{W}}_2 \leq \left(\sup_{x, w, z' \in \ball{}} \{ \tucker{\ten{W}; x, z', w}\}\right)^2,$$ which, plugging in the definition of the tensor spectral norm [Chen2020a], implies (iii). lem:wop is that Given $\opm{Z}_N$, $E_N$ as in eq:zmatdef and [eq:ematdef] respectively and $\op{W}$ as in lem:wop.

<!-- chunk {"id": "body-0252", "role": "body", "section": "Identification model", "weight": 1.0} -->

We are now ready to prove the data-driven bound.

<!-- chunk {"id": "body-0253", "role": "body", "section": "Identification model", "weight": 1.0} -->

Proof of thm:error-bound-full By the classical LS error equation eq:error-model-full: $$\svec(\hat{\smoment} - W) = (I - \pinv{\opm{Z}_N} \opm{Z}_N) \svec(W) + \pinv{\opm{Z}}_N E_N,$$ where we need asm:model to imply [eq:measurement-model] holds using lem:model-eq.

<!-- chunk {"id": "body-0254", "role": "body", "section": "Identification model", "weight": 1.0} -->

The matrices $X_i$ are therefore bounded and i.i.d. (by asm:data). Applying lem:mathfd and solving for $\beta$ shows $$\prob[\nrm{\ssum_{i=1}^N \op{H}_i(w_i \trans{w_i} - W)}_2 \leq \beta] \geq 1 - \delta.$$ asm:data and lem:kernel-zn that (I - \pinv{\opm{Z}_N} \opm{Z}_N) \svec(W) \nonumber = (I - \pinv{(\trans{\ten{W}_{}})} \trans{\ten{W}_{}}) \svec(W).

<!-- chunk {"id": "body-0255", "role": "body", "section": "Identification model", "weight": 1.0} -->

Applying lem:kernel-sm thus implies: \op{E}(\hat{\smoment} - W; Z) &= \op{E}(\unsvec(\pinv{\opm{Z}}_N E_N); Z).

<!-- chunk {"id": "body-0256", "role": "body", "section": "Identification model", "weight": 1.0} -->

We continue with the proofs of sec:mean-id.

<!-- chunk {"id": "body-0257", "role": "body", "section": "Identification model", "weight": 1.0} -->

*Proof of lem:mean-dd By the classical LS error equation: $${\mu}_\star - \hat{{\mu}} = (I - \pinv{(\opm{Z}_N^\mu)} \opm{Z}_N^\mu) {\mu}_\star + \pinv{(\opm{Z}_N^\mu)} E^\mu_N,$$ with $E^\mu_N = [\stucker{\widetilde{\ten{M}}; z_1, \epsilon_1}, \dots, \stucker{\widetilde{\ten{M}}; z_N, \epsilon_N}]$ and $\epsilon_i$ i.i.d. zero-mean random vectors. Equation eq:err-model-mean-full holds by asm:model-structured and lem:model-eq-structured.

<!-- chunk {"id": "body-0258", "role": "body", "section": "Identification model", "weight": 1.0} -->

Expanding the second term of eq:err-model-mean-full, inserting the definition of $G_i$ and $\op{M}$ gives [eq:error-model-mean]: $${\mu}_\star - \hat{{\mu}} = \ssum_{i=1}^N G_i \epsilon_i = \ssum_{i=1}^N \E[G_i \widetilde{w}_i] - G_i \widetilde{w}_i.$$ Note that $G_i \widetilde{w}_i$ is a sequence of i.i.d. random vectors with $\nrm{G_i \widetilde{w}_i}_2 \leq \nrm{G_i}_2 r_w$, by the definition of the spectral norm. Hence lem:vechfd is applicable. The final result is then recovered by solving for $\beta$.

<!-- chunk {"id": "body-0259", "role": "body", "section": "Identification model", "weight": 1.0} -->

The second bound follows directly by lem:mean-dd (which claims (i) $\prob[\nrm{\mu_\star - \hat{\mean}}_2 \leq \beta_\mu] \geq 1 - \delta_\mu$), while we have (ii) $\prob[\nrm{\Delta W_\eta}_2 \leq \beta_W] \geq 1 - \delta_W$ by eq:stoch-nrm-bnd in the proof of thm:error-bound-full. A union bound shows that both (i) and (ii) hold w.p. at least $ 1 - \delta_\mu - \delta_W$.

<!-- chunk {"id": "body-0260", "role": "body", "section": "Sample Complexity", "weight": 1.0} -->

We adjust the results of [Coppens2020-TR] to our setting, proving thm:sample-complexity. This analysis proceeds in three steps, the first two of which are related to thm:drlqrcp and the third evaluates the closed-loop cost of $\bar{K}$. To be more specific, thm:drlqrcp first finds $\bar{P}$ such that $\op{R}(\bar{W}; \bar{P}) = \bar{P}$ and then computes $\bar{K} = -(R + \adj{\op{G}}(\bar{P}))^{-1} \adj{\op{H}}(\bar{P})$. Here $(P_\star, K_{\star})$ are the solutions to the nominal problem in thm:cplqr.

<!-- chunk {"id": "body-0261", "role": "body", "section": "Sample Complexity", "weight": 1.0} -->

Throughout this section we heavily rely on the arguments in [Coppens2020-TR]. Whenever steps therein are repeated, more specific parts are referenced to aid the reader.

<!-- chunk {"id": "body-0262", "role": "body", "section": "Sample Complexity", "weight": 1.0} -->

*Riccati Perturbation Analysis To bound $\nrm{\bar{P} - P_{\star}}$ we need to evaluate the effect of a change in $W$ on the solution to the Riccati equation $\op{R}(P) = P$, with $\op{R}$ as in eq:ric-def. The dependency on $W$ is made explicit through rem:parameter.

<!-- chunk {"id": "body-0263", "role": "body", "section": "Sample Complexity", "weight": 1.0} -->

We then find $\Delta P$ such that $$\op{R}(W_\star + \Delta W; P_\star + \Delta P) = P_\star + \Delta P, \, \op{R}(W_\star; P_\star) = P_\star.$$ Here $W_{\star}$ is the true second moment $\E[w \trans{w}]$ as in sec:construction and $\Delta W$ is the difference between $W_{\star}$ and its data-driven estimate, i.e. $\bar{W}$ in [thm:error-bound-full] (or $\hat{W}$ in the certainty equivalent setting).

<!-- chunk {"id": "body-0264", "role": "body", "section": "Sample Complexity", "weight": 1.0} -->

We can then state the error bound.

<!-- chunk {"id": "body-0265", "role": "body", "section": "Sample Complexity", "weight": 1.0} -->

The perturbed Riccati equation eq:ric-perturbed can be written as a fixed-point equation whenever both the original system and the perturbed system are stabilizable: $$\Phi(\Delta P) \dfn - (\adj{\op{L}_\star})^{-1}\left(\op{R}_{0}(\Delta P) + \op{R}_{\Delta}(\Delta P) \right) = \Delta P,$$ with $\adj{\op{L}}_{K_{\star}}$ as in lem:opadj and its inverse existing due to the stabilizability assumption and thm:cplqr, $K_\star$ the optimal controller of thm:cplqr and \op{R}_0(\Delta P) &\dfn (P_\star + \Delta P) - \op{R}(W_{\star}; P_\star + \Delta P) -

<!-- chunk {"id": "body-0266", "role": "body", "section": "Sample Complexity", "weight": 1.0} -->

We next bound $\nrm{\bar{K} - K_\star}_2$ by following a procedure similar to the one of [Coppens2020-TR].

<!-- chunk {"id": "body-0267", "role": "body", "section": "Sample Complexity", "weight": 1.0} -->

Given the controller perturbation from the previous part, the sub-optimality of that controller follows directly from [Coppens2020-TR].

<!-- chunk {"id": "body-0268", "role": "body", "section": "Sample Complexity", "weight": 1.0} -->

In the modelfree setting when no knowledge is available on the modes the value of $n_w = n_x (n_x + n_u)$. Thus, the overall dimensional dependency $$\min(n_x, n_u) n_x (n_x + n_u) \log(n_x (n_x + n_u)) \approx n_x^2 (n_x + n_u),$$ for the usual setting where $n_x \geq n_u$. In the additive noise, certainty equivalent setting [Mania2019] establish a bound in the certainty equivalent with $\sqrt{(n_x + n_u)^3}$. This dimensional dependency is further improved to $\sqrt{n_u n_x^2}$ by [Simchowitz2020], which also establishes a lower bound with matching dimensional dependency. Our analysis therefore implies that learning multiplicative noise is more difficult to learn with respect to the dimensions. However a lower bound is needed to confirm this with certainty.

<!-- chunk {"id": "body-0269", "role": "body", "section": "Semidefinite programming", "weight": 1.0} -->

We will require the following technical lemmas: For some $P \in \sym{d}$ then $$\tr[P X] > 0, \, \forall X \nsgeq 0 \quad \Leftrightarrow \quad P \sgt 0.$$ ($\Rightarrow$) Assume $P$ is not positive definite, which implies $\exists x \colon \trans{x} P x \leq 0$. So $X = x \trans{x} \nsgeq 0$ gives a contradiction.

<!-- chunk {"id": "body-0270", "role": "body", "section": "Semidefinite programming", "weight": 1.0} -->

($\Leftarrow$) Any $X \nsgeq 0$ can be written as $\sum_{i=1}^r x_i \trans{x_i}$ for some $r > 0$ and nonzero $x_i$. Then by the cyclic property of the trace $\tr[P X] = \sum_{i=1}^r \trans{x_i} P x_i > 0$ by $P \sgt 0$.

<!-- chunk {"id": "body-0271", "role": "body", "section": "Semidefinite programming", "weight": 1.0} -->

This lemma is used in the proof of [Bertsekas2005V1]. Consider an orthonormal basis $\{X_i\}_{i=1}^{\sd{d}}$ for $\sym{d}$. Then $$\lim_{t \to \infty} \tr[X_i P_t] = \tr[X_i \lim_{t \to \infty} P_t] = \tr[X_i P_{\infty}]$$ is well defined by the monotone convergence theorem (since $\tr[X_i P_t] \leq \tr[X_i P_{t+1}]$ and $\tr[X_i P_t] < +\infty$ for all $t \in \N$). Completing the same argument for every $i$ gives us a linear system of equations with $P_{\infty}$ the unique solution.

<!-- chunk {"id": "body-0272", "role": "body", "section": "Semidefinite programming", "weight": 1.0} -->

We extend the result of This result was previously integrated in [Coppens2019].

<!-- chunk {"id": "body-0273", "role": "body", "section": "Semidefinite programming", "weight": 1.0} -->

Then we have the following implication:rank assumption on $R$ and $L$?

<!-- chunk {"id": "body-0274", "role": "body", "section": "Semidefinite programming", "weight": 1.0} -->

Here [eq:pred-second:a] used the triangle inequality and [eq:pred-second:b] used $\trans{|\theta|} \beta \geq -\nrm{|\theta|}_2 \nrm{\beta}_2 = -\nrm{\beta}_2$ for $[\beta]_i = \nrm{\Gamma^{-1/2} F_i \Lambda^{-1/2} u}_2$. [eq:pred:b] implies $\rho^2 \ssum_{i=1}^d\Lambda^{-1/2} \trans{H_i} \Gamma^{-1} F_i \Lambda^{-1/2} \sleq I$, by invertibility of $\Lambda, \Gamma$ and a Schur complement.

<!-- chunk {"id": "body-0275", "role": "body", "section": "Semidefinite programming", "weight": 1.0} -->

By the inequality of arithmetic and geometric means (i.e., $(\alpha + \beta)/2 \geq \sqrt{\alpha \beta}$) we have the final sufficient condition for $\set{U}[\rho] \sgeq 0$: $$\trans{x} T x \geq (\nrm{v}_2^2 + \nrm{u}_2^2)/2 = \trans{x} (\trans{L} \Gamma L + \trans{R} \Lambda R) x,$$ which holds $\forall x \in \Re^{\ell}$ by [eq:pred:a].
