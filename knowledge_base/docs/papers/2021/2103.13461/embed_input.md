<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Matrix Finsler's Lemma with Applications to Data-Driven Control

Topics include Data-driven control, Matrix Finsler's lemma, Matrix S-lemma, Noisy data, Linear matrix inequalities, Lure systems, Robust control, Quadratic constraints.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Provides a matrix Finsler lemma that unifies exact-data and noisy-data direct control conditions under one quadratic-constraint view. It clarifies how several data-driven LMI synthesis results fit together and extends the machinery to Lur'e systems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In a recent paper it was shown how a matrix S-lemma can be applied to construct controllers from noisy data. The current paper complements these results by proving a matrix version of the classical Finsler's lemma. This matrix Finsler's lemma provides a tractable condition under which all matrix solutions to a quadratic equality also satisfy a quadratic inequality. We will apply this result to bridge known data-driven control design techniques for both exact and noisy data, thereby revealing a more general theory. The result is also applied to data-driven control of Lur'e systems.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Data-driven control refers to all approaches that use measured data as starting point in the control design. This design can be done either indirectly via model identification, or by directly mapping data to control policies. Both paradigms have a long history, but data-driven control has recently witnessed a renewed surge of interest, partly because of the widespread availability of data and the successes of machine learning algorithms. We mention contributions to data-driven optimal control, predictive control and robust tracking control, nonlinear control and system level synthesis.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Several recent papers aim at deriving tractable data-based linear matrix inequalities (LMI's) that enable direct data-driven control design. The paper proposes a semidefinite programming relaxation for the stabilization of switched systems. The authors of provide a data-based parameterization of controllers, which is applied to stabilization and optimal control problems. In, notions of informative data are defined, which leads to necessary and sufficient data-based conditions for different analysis and control problems. The paper considers a noise bound in terms of a quadratic matrix inequality and proposes LMI conditions for control with guaranteed stability and performance. Combining data with prior knowledge on the system dynamics has been studied. Also the problem of data-based verification of dissipativity properties has been cast as an LMI problem.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

An important question in this line of work regards the conservatism of the proposed LMI conditions. In this direction, a state-of-the-art result is the matrix generalization of the classical S-lemma. This result provides an LMI condition under which all matrix solutions to one quadratic matrix inequality (QMI) also satisfy another QMI. The first inequality is motivated by the data: a quadratic bound on the noise, used, has the consequence that all systems explaining the data satisfy a QMI. The second inequality captures design specifications such as stability or $\mathcal{H}_{2}$/$\mathcal{H}_{\infty}$ performance. Based on the matrix S-lemma, necessary and sufficient conditions could be provided for data-driven control with guaranteed quadratic stability and performance.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

A curious observation is that the stabilization result based on the S-lemma does not fully recover the stabilization result of for *noise-free* data. The reason is that in this case the Slater condition that is required for the matrix S-lemma does not hold. This fact is somewhat unsatisfactory because control using noise-free data should intuitively always be a special case of that for noisy data (with bound zero).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we resolve this issue by introducing a matrix version of Finsler's lemma. The classical Finsler's lemma provides an LMI condition under which a quadratic inequality is the consequence of a quadratic *equality*. We will explain the difficulties in generalizing this result to matrix variables. Then, as our main contribution we will provide a Finsler's lemma for matrix variables in case the involved matrices obey some special structure. This matrix Finsler's lemma is then applied to data-driven stabilization. Interestingly, we will see that the LMI condition of is also necessary and sufficient in the special case of noise-free data, a result that could not be concluded from the matrix S-lemma. We believe that the matrix Finsler's lemma will also find other applications in situations where a QMI is the consequence of a matrix equality. In this paper, we will study one more of such situations, namely the construction of absolutely stabilizing controllers of Lur'e systems.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Outline*: In Section II we recap data-driven stabilization results and state the problem. Section III contains our results on the matrix Finsler's lemma. In Section IV this result is applied to bridge the results for noiseless and noisy data. Finally, in Section V we consider control of Lur'e systems.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Recap of data-driven stabilization and problem formulation", "weight": 1.0} -->

We will first recap two data-driven stabilization results, for noise-free and noisy data, which can be found in the references. Consider the system where $\mathbf{x} \in {\mathbb{R}}^{n}$ is the state, $\mathbf{u} \in {\mathbb{R}}^{m}$ is the control input and $\mathbf{w} \in {\mathbb{R}}^{n}$ denotes noise. The real matrices $A_{s}$ and $B_{s}$ are not assumed to be known. Instead of this, it is assumed that input/state data are obtained, which are collected in the matrices We will also make use of shifted versions of the state sequence which are denoted by

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Data-driven stabilization using exact data", "weight": 1.0} -->

In this section we focus on the noise-free situation in which $\mathbf{w} = 0$. The purpose is to use the input/state data $(U_{-},X)$ for the design of a stabilizing state feedback controller $\mathbf{u} = {K\mathbf{x}}$. Of course, this is only possible if the data contain sufficient information about the unknown system, i.e., if they are *informative* for control design.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Data-driven stabilization using noisy data", "weight": 1.0} -->

Next, we consider the system where $\mathbf{w}$ is not necessarily zero. The experimental input/state data are denoted by $(U_{-},X)$, as before. This time, we also denote the noise samples during an experiment by Of course, the matrix $W_{-}$ is not known, but is assumed to bounded as for known $\Phi_{11} = \Phi_{11}^{\top}$, $\Phi_{12}$ and $\Phi_{22} = \Phi_{22}^{\top} < 0$. This noise model was first introduced. It can be interpreted as the transposed (or dual) model as the one used. The inequality has the interpretation that the energy of $\mathbf{w}$ is bounded on the finite time interval $\lbrack 0,{T - 1}\rbrack$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-B Data-driven stabilization using noisy data", "weight": 1.0} -->

Given the noise model, the set of all systems explaining the data is given by all $(A,B)$ such that is satisfied for some realization $W_{-}$ of the noise, that is, With this in mind, we recall the following notion of informative data for stabilization using noisy data.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-C Problem formulation", "weight": 1.0} -->

To summarize, in the case of noise-free data, Proposition 1 gives a necessary and sufficient condition for informativity for stabilization. Moreover, in the case of noisy data, Proposition 4 provides a necessary and sufficient condition for informativity for quadratic stabilization.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-C Problem formulation", "weight": 1.0} -->

A natural question is now the following: what is the relation between these two propositions, and can the former be obtained as a special case from the latter?

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-C Problem formulation", "weight": 1.0} -->

Surprisingly, the answer to this question is far from trivial. To initiate our investigation, it is tempting to consider the noise model with Indeed, this noise model implies that ${W_{-}W_{-}^{\top}} \leq 0$, i.e., $W_{-} = 0$ which corresponds exactly to the case in which the data are noise-free.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-C Problem formulation", "weight": 1.0} -->

Now, a problem arises when applying Proposition 4 to noise models of the form. The reason is that for $\Phi$, the matrix $N$ in is negative semidefinite. In turn, this implies that the Slater condition (9 ‣ II-B Data-driven stabilization using noisy data ‣ II Recap of data-driven stabilization and problem formulation ‣ A Matrix Finsler’s Lemma with Applications to Data-Driven Control")) is *not satisfied*. The conclusion is that Proposition 4 does not yield a necessary and sufficient condition for quadratic stabilization in the noise-free case (note that *sufficiency* of (FS) does hold, regardless of the Slater condition).

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-C Problem formulation", "weight": 1.0} -->

Despite this potential shortcoming of Proposition 4, it turns out to be possible to bridge the results for exact and noisy data in Propositions 1 and 4. In order to understand this relation we need a new result, namely a matrix version of *Finsler's lemma*.

<!-- chunk {"id": "body-0019", "role": "body", "section": "The matrix Finsler's lemma", "weight": 1.0} -->

Essentially, informativity for stabilization (Definition 1) asks for the existence of $P$ and $K$ such that a quadratic *inequality* holds for all $(A,B)$ satisfying the *equality* defined. This is more than reminiscent of the classical Finsler's lemma, named after Paul Finsler who proved the result in 1936. Two versions of Finsler's lemma are known, for both strict and non-strict inequalities. We will recall both results in the following two propositions that can be found.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Bridging the exact and noisy cases", "weight": 1.0} -->

In this section, we will apply the matrix Finsler's lemma to find a new characterization of informativity for stabilization in the exact data case, thereby bridging the exact and noisy formulations. The result can be formulated as follows.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Data-driven stabilization of Lur'e systems", "weight": 1.0} -->

In this section, we will apply the matrix Finsler's lemma to control Lur'e systems. First, we will explain the classical problem of absolute stability for such systems. Consider the Lur'e system where $\mathbf{x} \in {\mathbb{R}}^{n}$ is the state, $\mathbf{u} \in {\mathbb{R}}^{m}$ is the input and $\phi:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$ is a (nonlinear) function satisfying the sector condition The real matrices $A,B,E$ and $C$ are of appropriate dimensions. Suppose that we apply a state feedback controller $\mathbf{u} = {K\mathbf{x}}$ resulting in For systems of the form, a problem with a rich history is that of *absolute stability*, i.e. global asymptotic stability of $0$ *for all* sector-bounded nonlinearities, c.f. for references.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Data-driven stabilization of Lur'e systems", "weight": 1.0} -->

We focus on proving absolute stability of by means of a quadratic Lyapunov function ${V{(z)}}:={z^{\top}Pz}$ where $P = P^{\top} > 0$. We thus want that ${V{({x{({t + 1})}})}} < {V{({x{(t)}})}}$ for all sector-bounded nonlinearities $\phi$ and all nonzero $x{(t)}$ and resulting $x{({t + 1})}$ satisfying. We will mimic the continuous-time setting of \[28, Ch. 5\]. Let $A_{K}:={A + {BK}}$. Then we require for all $w \in {\mathbb{R}}$ and nonzero $x \in {\mathbb{R}}^{n}$ satisfying ${w{({w - {Cx}})}} \leq 0$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Data-driven stabilization of Lur'e systems", "weight": 1.0} -->

Equivalently, for all $w \in {\mathbb{R}}$ and nonzero $x \in {\mathbb{R}}^{n}$ satisfying Since is not satisfied when $x = 0$ and $w \neq 0$, the latter statement is equivalent to being satisfied for all nonzero $(x,w)$ satisfying. Assuming $C \neq 0$, the inequality is strictly feasible. Thus, by the S-lemma \[28, p. 24\] we conclude that is satisfied for all nonzero $(x,w)$ satisfying if and only if for some scalar $\alpha \geq 0$. Proving absolute stability of by a quadratic Lyapunov function thus boils down to finding $P = P^{\top} > 0$ and $\alpha \geq 0$ such that holds. By homogeneity, we can even get rid of $\alpha$ and look for $P = P^{\top} > 0$ satisfying

<!-- chunk {"id": "body-0024", "role": "body", "section": "V-A Data-driven stabilization", "weight": 1.0} -->

Next, we consider the system where $A_{s},B_{s}$ and $E_{s}$ are unknown but the matrix $C$ is known^11^1This assumption can be replaced by measurements of ${\mathbf{y}{(t)}}:={C\mathbf{x}{(t)}}$.. We aim at constructing an absolutely stabilizing controller $\mathbf{u} = {K\mathbf{x}}$ on the basis of measurements $X$ and $U_{-}$ as in and If we define $X_{+}$ and $X_{-}$ as in then all systems $(A,B,E)$ explaining the data are given by the set $\Sigma$ defined by
