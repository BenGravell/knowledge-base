<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Performance Bounds for the Scenario Approach and an Extension to a Class of Non-convex Programs

Topics include Scenario optimization, Chance constraints, Robust optimization, Nonconvex programs, Sample complexity, Fault detection, Uncertainty quantification.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Refines scenario-approach guarantees by bounding how the sampled scenario program relates to the robust and chance-constrained problem values over general uncertainty spaces. The paper also extends the framework to a class of nonconvex programs, including binary decisions, and resolves a measurability assumption that had often been left implicit in scenario-program analyses.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider the Scenario Convex Program (SCP) for two classes of optimization problems that are not tractable in general: Robust Convex Programs (RCPs) and Chance-Constrained Programs (CCPs). We establish a probabilistic bridge from the optimal value of SCP to the optimal values of RCP and CCP in which the uncertainty takes values in a general, possibly infinite dimensional, metric space. We then extend our results to a certain class of non-convex problems that includes, for example, binary decision variables. In the process, we also settle a measurability issue for a general class of scenario programs, which to date has been addressed by an assumption. Finally, we demonstrate the applicability of our results on a benchmark problem and a problem in fault detection and isolation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optimization problems under uncertainty have considerable applications in disciplines ranging from mathematical finance to control engineering. For example most control systems involve some level of uncertainty; the aim of a robust control design is to provide a guaranteed level of performance for all admissible values of the uncertain parameters. In the convex case, two well-known approaches for dealing with such uncertain programs are robust convex programs (RCPs) and chance-constrained programs (CCPs). RCPs consider constraint satisfaction for all, possibly infinitely many, realizations of the uncertainty. While it is known that certain classes of RCPs can be solved as effectively as their non-robust counterparts in other cases RCPs can be intractable. For example, the class of parametric linear matrix inequalities, which occur in many control problems, is NP-hard. CCPs, on the other hand, allow constraint violation with a low probability. The resulting optimization problem, however, is in general non-convex \[Pré95, \].

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Computationally tractable approximations to the aforesaid optimization problems can be obtained through the scenario convex programs (SCPs) in which only finitely many uncertainty samples are considered. A natural question in this case is how many samples would be "enough" to provide a good solution. To answer this question, one may view the problem from two perspectives: feasibility and objective performance. The literature mainly focuses on the first perspective. In this direction, the authors in initialized a feasibility theory for CCP refined subsequently. They established an explicit probabilistic lower bound for the sample size to guarantee the feasibility of the SCP solutions from a chance-constrained perspective. By contrast, the issue of performance bounds for both RCP and CCP via SCP has not been settled up to now. provides a novel perspective in this direction that leads to optimal performance bounds for CCPs. However, it involves the problem of optimal constraint removal, which in general is computationally intractable.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The first contribution of this article is to address the SCP Performance issue from the objective viewpoint. The key element of our analysis relies on the concept of the worst-case violation inspired by the recent work. The authors of derived an upper bound of the worst-case violation for the SCPs where the uncertainty takes values in a finite dimensional Euclidean space. This result leads to a performance bound for a particular class of $RCP$s where the uncertainly appears in the objective function, e.g., min-max optimization problems. Motivated by different applications such as control problems with saturation constraints, fault detection and isolation in dynamical systems, and approximate dynamic programming, in this article we first extend this result to infinite dimensional uncertainty spaces. In the sequel, we establish a theoretical bridge from the optimal values of SCP to the optimal values of both RCP and CCP. Along this direction, under mild assumptions on the constraint function (measurability with respect to the uncertainty and lower semicontinuity with respect to the decision variables), we shall also rigorously settle a measurability issue of the SCP optimizer, which to date has been addressed in the literature by an assumption, e.g..

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our second contribution is to extend these results to a class of non-convex programs that, in particular, allows for binary decision variables. In the context of mixed integer programs, the recent work investigates the feasibility perspective of CCPs, which leads to a bound of the required number of scenarios with exponential growth rate in the number of integer variables, whereas our proposed bound scales linearly.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The layout of this article is as follows: In Section 2 we formally introduce the optimization problems that will be addressed. Our results on probabilistic objective performance for both RCPs and CCPs based on SCPs are reported in Section 3. In Section 4 we extend our results to a class of non-convex programs, including mixed-integer programs with binary variables. To illustrate the proposed methodology, in Section 5 the theoretical results are applied to two examples: a benchmark problem whose solution can be computed explicitly, and a fault detection and isolation study with an application to the security of power networks. We conclude in Section 6 with a summary of our work and comment on possible subjects of further research. For better readability, some of the technical proofs and details are given in the appendices.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Let ${\mathbb{X}} \subset {\mathbb{R}}^{n}$ be a compact convex set and $c \in {\mathbb{R}}^{n}$ a constant vector. Let $\left(\mathcal{D},{{\mathfrak{B}}{(\mathcal{D})}},{\mathbb{P}} \right)$ be a probability space where $\mathcal{D}$ is a metric space with the respective Borel $\sigma$-algebra ${\mathfrak{B}}{(\mathcal{D})}$. Consider the measurable function $f:{{{\mathbb{X}} \times \mathcal{D}}\rightarrow{\mathbb{R}}}$, which is convex in the first argument for each $d \in \mathcal{D}$, and bounded in the second argument for each $x \in {\mathbb{X}}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

We then consider the following optimization problems: where $\varepsilon \in {\lbrack 0,1\rbrack}$ is the constraint violation level for the chance-constrained program. We denote the optimal value of the program $RCP$ (resp. ${CCP}_{\varepsilon}$) by $J_{RCP}^{\star}$ (resp. $J_{{CCP}_{\varepsilon}}^{\star}$). Suppose ${(d_{i})}_{i = 1}^{N}$ are $N$ independent and identically distributed (i.i.d.) samples drawn according to the probability measure $\mathbb{P}$. The centerpiece of this study is the scenario program where the optimal solution and optimal value of $SCP$ are denoted, respectively, by $x_{N}^{\star}$ and $J_{N}^{\star}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Notice that $SCP$ is naturally random as it depends on the random samples ${(d_{i})}_{i = 1}^{N}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

We assume throughout our subsequent analysis that the following measurability assumption holds, though we shall show in Subsection 3.3 how one may rigorously address this issue without any assumption for a large class of optimization programs (not necessarily convex).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

The optimization program $SCP$ in is convex and hence tractable even for cases where the problems are NP-hard. Motivated by this, a natural question is whether there exist theoretical links from $SCP$ to $RCP$ and ${CCP}_{\varepsilon}$. As mentioned in the introduction, this question can be addressed from two different perspectives: feasibility and objective performance.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Confidence interval for the objective functions", "weight": 1.0} -->

The following definition inspired by the recent work is the key object for our analysis.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 3.3 (Slater Point)", "weight": 1.0} -->

Under Assumption 3.3. ‣ 3.1. Confidence interval for the objective functions ‣ 3. Probabilistic Objective Performance ‣ Performance Bounds for the Scenario Approach and an Extension to a Class of Non-convex Programs"), we define the constant The following lemma is a classical result in perturbation theory of convex programs, which is a significant ingredient for the first result of this article.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Remark 3.5 ($L_{\\text{SP}}$ for Min-Max Problems)", "weight": 1.0} -->

In min-max problems, one may inspect that there always exists a Slater point (in the sense of Assumption 3.3. ‣ 3.1. Confidence interval for the objective functions ‣ 3. Probabilistic Objective Performance ‣ Performance Bounds for the Scenario Approach and an Extension to a Class of Non-convex Programs")) with the corresponding constant $L_{\text{SP}}$ arbitrarily close to $1$. In fact, it is straightforward to observe that for min-max problems $J_{{RCP}_{\gamma}}^{\star} = {J_{RCP}^{\star} - \gamma}$, which readily implies that the Lipschitz constant of Lemma 3.4 is $1$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Remark 3.5 ($L_{\\text{SP}}$ for Min-Max Problems)", "weight": 1.0} -->

The following results are the main contributions of the first part of the article.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Remark 3.9", "weight": 1.0} -->

Two remarks regarding the function $g$ in Proposition 3.8 are in order: Explicit expression: Under the hypotheses of Proposition 3.8, Theorem 3.6. ‣ 3.1. Confidence interval for the objective functions ‣ 3. Probabilistic Objective Performance ‣ Performance Bounds for the Scenario Approach and an Extension to a Class of Non-convex Programs") can be expressed in more explicit form. Let $\varepsilon$ and $\beta$ be in $\lbrack 0,1\rbrack$, $L_{d}$ be the Lipschitz constant of the constraint function $f$ in $d$, $L_{\text{SP}}$ be the constant, and $N{(\cdot, \cdot)}$ be as defined in (12. ‣ 2. Problem Statement ‣ Performance Bounds for the Scenario Approach and an Extension to a Class of Non-convex Programs")).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 3.9", "weight": 1.0} -->

Then, for any $N \geq {N\left({g{(\frac{\varepsilon}{L_{\text{SP}}L_{d}})}},\beta \right)}$ we have Curse of dimensionality: For an $n_{d}$-dimensional uncertainty set $\mathcal{D}$, the number of disjoint balls in $\mathcal{D}$ with radius $r$ grows proportional to $r^{- n_{d}}$ as $r$ decreases. Thus, the assumptions of Proposition 3.8 imply that $g{(r)}$ is of the order of $r^{n_{d}}$. Therefore, for the desired precision $\varepsilon$, as detailed in the preceding remark, the required number of samples $N$ grows exponentially as $\varepsilon^{- n_{d}}$. This appears to be an inherent feature when one seeks to bound the optimal value via scenario programs; see for similar observations.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Feasibility of RCP via SCP", "weight": 1.0} -->

In this subsection we provide an example to show the inherent difficulty of the feasibility connection from $SCP$ to the original problem $RCP$. Consider the following $RCP$ with its $SCP$ counterpart in which both decision and uncertainty space are compact subsets of $\mathbb{R}$: It is not difficult to see that the feasible set of the robust program is $\lbrack{- 1},0\rbrack$ with the optimizer $x^{\star} = 0$, whereas the optimizer of its scenario program is $x_{N}^{\star} = {\min_{i \leq N}d_{i}}$. If the probability measure $\mathbb{P}$ does not have atoms (point measure), we have ${{\mathbb{P}}^{N}\left\lbrack {{\min_{i \leq N}d_{i}} > 0} \right\rbrack} = 1$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Feasibility of RCP via SCP", "weight": 1.0} -->

Thus, one can deduce that where $\mathcal{P}$ is the family of all nonatomic measures on $\left(\mathcal{D},{{\mathfrak{B}}{(\mathcal{D})}} \right)$. More generally, if the set ${\arg{\max_{d \in \mathcal{D}}f}}{(x,d)}$ has measure zero for any $x \models {RCP}$ (e.g., when $f$ is convex in $d$ and the boundary of $\mathcal{D}$ has zero measure), then the program $SCP$ will almost surely return infeasible solutions to the program $RCP$, as the worst-case scenarios are almost surely neglected.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Measurability of the SCP optimizer", "weight": 1.0} -->

The objective of this subsection is to address the standing Assumption 2.1. The measurability of the optimizer $x_{N}^{\star}$ for the scenario program $SCP$ is a rather involved technical issue. In fact, to the best of our knowledge, in the literature this issue is always resolved by introducing an assumption. Let us highlight that the measurability of optimal values and the set of optimizers as well as the existence of a measurable selection are classical results in this context, see for instance \[, Theorem 14.37, p. 664\]. However, there is no a priori guarantee that the obtained optimizer of the program $SCP$ can be viewed as a measurable mapping from $\mathcal{D}^{N}$ to $\mathbb{X}$. Toward this issue, we propose a "two-stage" optimization program, in the *lexicographic* sense in the context of multi-objective optimization problems, in which the measurability of this mapping is ensured for a large class of programs (not necessarily convex).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Measurability of the SCP optimizer", "weight": 1.0} -->

For the rest of this section we assume that ${\mathbb{X}} \subset {\mathbb{R}}^{n}$ is closed and the mapping $x\mapsto{f{(x,d)}}$ is lower semicontinuous. Consider the scenario program $SCP$ as defined in with the corresponding optimal value $J_{N}^{\star}$; $SCP$ is assumed to be feasible with probability one. Given the same uncertainty samples ${(d_{i})}_{i = 1}^{N}$ as in $SCP$, we introduce the second program where $\phi:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is a strictly convex function. Let us denote the optimizer of the above program by ${\overset{\sim}{x}}_{N}^{\star}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Measurability of the SCP optimizer", "weight": 1.0} -->

It is straightforward to observe that ${\overset{\sim}{x}}_{N}^{\star}$ is indeed an optimizer of the program $SCP$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 3.11 (Measurability of the Feasible Set)", "weight": 1.0} -->

The measurability of the feasibility event ${\overset{\sim}{x}}_{N}^{\star} \models {CCP}_{\varepsilon}$ (equivalently the measurability of the mapping $x\mapsto{{\mathbb{P}}{\lbrack{{f{(x,d)}} \leq 0}\rbrack}}$) is a straightforward consequence of Proposition 3.10. ‣ 3.3. Measurability of the SCP optimizer ‣ 3. Probabilistic Objective Performance ‣ Performance Bounds for the Scenario Approach and an Extension to a Class of Non-convex Programs") and Fubini's Theorem \[, Thm. 18.3, p. 234\].

<!-- chunk {"id": "body-0026", "role": "body", "section": "Extension to a Class of Non-Convex Programs", "weight": 1.0} -->

This section extends the results developed in Section 3.1 to a class of non-convex problems. Consider a family of programs introduced in in which the program data are indexed by $k$, i.e., ${({\mathbb{X}}_{k},f_{k},\varepsilon_{k})}_{k = 1}^{m}$. We assume that each tuple $({\mathbb{X}}_{k},f_{k},\varepsilon_{k})$ satisfies the required conditions in Section 2 (i.e., ${\mathbb{X}}_{k}$ is a compact convex set and the mapping $x\mapsto{f_{k}{(x,d)}}$ is convex for every $d \in \mathcal{D}$), and the corresponding programs are denoted by ${RCP}^{(k)}$ and ${CCP}_{\varepsilon_{k}}^{(k)}$ as defined.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Extension to a Class of Non-Convex Programs", "weight": 1.0} -->

Consider the following (non-convex) optimization problems: where $x \models {\bigcup_{k = 1}^{m}{RCP}^{(k)}}$ (resp. $x \models {\bigcup_{k = 1}^{m}{CCP}_{\varepsilon_{k}}^{(k)}}$) indicates that there exists $k \in {\{ 1,\cdots,m\}}$ such that $x \models {RCP}^{(k)}$ (resp. $x \models {CCP}_{\varepsilon_{k}}^{(k)}$). In other words, the programs seek an optimal solution which is feasible for at least one of the subprograms indexed by $k$, while the uncertainty space $\mathcal{D}$ as well as the associated measure $\mathbb{P}$ is shared between all the subprograms. Similarly, given i.i.d.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Extension to a Class of Non-Convex Programs", "weight": 1.0} -->

samples ${(d_{i})}_{i = 1}^{N} \subset \mathcal{D}$ with respect to the probability measure $\mathbb{P}$, consider the scenario (non-convex) program Each subprogram ${SCP}^{(k)}$ is defined according to the scenario convex program associated with the program data $({\mathbb{X}}_{k},f_{k})$ while the uncertainty samples ${(d_{i})}_{i = 1}^{N}$ are the same for all $k \in {\{ 1,\cdots,m\}}$. Before proceeding with the main result of this section, let us point out that the programs contain, for example, a class of mixed integer programs. Let $f:{{{\mathbb{R}}^{n} \times {\{ 0,1\}}^{\ell} \times \mathcal{D}}\rightarrow{\mathbb{R}}}$ be the constraint function.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Extension to a Class of Non-Convex Programs", "weight": 1.0} -->

It is straightforward to see that a chance-constrained mixed integer program can be formulated as where ${f_{k}{(x,d)}} ≔ {f{(x,y_{k},d)}}$ for each selection of the binary variables $y_{k} \in {\{ 0,1\}}^{\ell}$. Then, by setting $m ≔ 2^{\ell}$, ${\mathbb{X}}_{k} ≔ {\mathbb{X}}$, $\varepsilon_{k} ≔ \varepsilon$, the right-hand side of the above relation is readily in the framework of. A similar argument also holds for the robust mixed integer problems counterparts.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Extension to a Class of Non-Convex Programs", "weight": 1.0} -->

As a first step, we extend the feasibility result of Theorem 2.2. ‣ 2. Problem Statement ‣ Performance Bounds for the Scenario Approach and an Extension to a Class of Non-convex Programs") to the non-convex setting.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 4.2 (Growth rate)", "weight": 1.0} -->

Notice that the number of subprograms, $m$, contributes to the confidence level $\beta$ in a linear fashion. As an illustration, suppose $\varepsilon_{k} ≔ \varepsilon$. In this case, one can easily verify that the confidence level of the non-convex program $SP$ can be set equal to $\frac{\beta}{m}$, where $\beta$ is the confidence level of each of the subprograms ${SCP}^{(k)}$. From a computational perspective, one can follow the same calculation as, and deduce that the contribution of $m$ to the number of the required samples $\overset{\sim}{N}$ appears in a logarithm. Thus, in our example of mixed integer programming above, the required number of samples grows linearly in the number of binary variables, which for most of applications could be considered a reasonable growth rate.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 4.2 (Growth rate)", "weight": 1.0} -->

The literature on computational schemes on non-convex problems is mainly based on statistical learning methods. A recent example of this nature is, which considers a class of problems involving Boolean expressions of polynomial functions. Given the degree and number of polynomial functions ($\alpha$ and $k$, respectively), the explicit sample bounds of scale with $\varepsilon^{- 1}{\log{({\alphak\varepsilon^{- 1}})}}$ as opposed to our result in (36. ‣ 4. Extension to a Class of Non-Convex Programs ‣ Performance Bounds for the Scenario Approach and an Extension to a Class of Non-convex Programs")) which grows proportional to $\varepsilon^{- 1}{\log{(m)}}$. We now proceed to extend the main results of Subsection 3.1, i.e., Theorems 3.6. ‣ 3.1. Confidence interval for the objective functions ‣ 3. Probabilistic Objective Performance ‣ Performance Bounds for the Scenario Approach and an Extension to a Class of Non-convex Programs") and 3.7.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 4.2 (Growth rate)", "weight": 1.0} -->

‣ 3.1. Confidence interval for the objective functions ‣ 3. Probabilistic Objective Performance ‣ Performance Bounds for the Scenario Approach and an Extension to a Class of Non-convex Programs"), to the non-convex settings and at once.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Sketch of the proof", "weight": 1.0} -->

The proof effectively follows the same lines as in the proofs of Theorems 3.6. ‣ 3.1. Confidence interval for the objective functions ‣ 3. Probabilistic Objective Performance ‣ Performance Bounds for the Scenario Approach and an Extension to a Class of Non-convex Programs") and 3.7. ‣ 3.1. Confidence interval for the objective functions ‣ 3. Probabilistic Objective Performance ‣ Performance Bounds for the Scenario Approach and an Extension to a Class of Non-convex Programs"). To adapt the required preliminaries, let us recall again that the optimizer of the programs is one of the optimizers of the respective subprograms. The same assertion holds for the random program as well. Moreover, since each subprogram of fulfills the assumptions of Subsection 3.1, Lemmas 3.2 and 3.4 also hold for each subprogram with the corresponding data $({\mathbb{X}}_{k},f_{k})$. Therefore, in light of Theorem 4.1.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Sketch of the proof", "weight": 1.0} -->

‣ 4. Extension to a Class of Non-Convex Programs ‣ Performance Bounds for the Scenario Approach and an Extension to a Class of Non-convex Programs"), it only suffices to consider the worst-case possibility among all the subprograms. ∎

<!-- chunk {"id": "body-0036", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

This section presents two examples to illustrate the theoretical results developed in the preceding sections and their performance. We first apply the results to a simple example whose analytical solution is available.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Example 1: Quadratic Constraint via Infinite Hyperplanes", "weight": 1.0} -->

Let $x = {\lbrack x_{1},x_{2}\rbrack}^{\intercal}$ be the decision variables selected in the compact set ${\mathbb{X}} ≔ {\lbrack 0,1\rbrack}^{2} \subset {\mathbb{R}}^{2}$, the linear objective function defined by $c ≔ {\lbrack{- 1},{- 1}\rbrack}^{\intercal}$, and the constraint function ${f{(x,d)}} ≔ {{{x_{1}{\cos{(d)}}} + {x_{2}{\sin{(d)}}}} - 1}$ where the uncertainty $d$ comes from the set $\mathcal{D} ≔ {\lbrack 0,{2\pi}\rbrack}$. Consider the optimization problems introduced in where $\mathbb{P}$ is the uniform probability measure on $\mathcal{D}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Example 1: Quadratic Constraint via Infinite Hyperplanes", "weight": 1.0} -->

It is not difficult to infer that the infinitely many hyperplane constraints can be replaced by a simple quadratic constraint. That is, for any $\gamma \geq 0$ In the light of the above observation, we have the analytical solutions where $J_{{RCP}_{\gamma}}^{\star}$ and $J_{{CCP}_{\varepsilon}}^{\star}$ are the optimal values of the optimization problems ${RCP}_{\gamma}$ and ${CCP}_{\varepsilon}$ as defined in and, respectively. The pictorial representation of the solutions is in Figure 3.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Example 2: Fault Detection and Isolation", "weight": 1.0} -->

The task of fault detection and isolation (FDI) involves generating a diagnosis signal to detect the occurrence of a specific fault. This is typically accomplished by designing a filter with all available signals as inputs (e.g., control signals and given measurements) and a scalar output that implements a non-zero mapping from the fault to the residual while decoupling unknown disturbances. In, a scalable optimization based approach is proposed to design an FDI filter for a class of nonlinear differential algebraic equation (DAE) where the filter is trained for finite number of disturbance signatures. The class of disturbances is further extended to a probability space where the filter performance is quantified in a probabilistic fashion.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Example 2: Fault Detection and Isolation", "weight": 1.0} -->

As a particular subclass of DAEs, consider the nonlinear differential equation where the matrices $A,B_{d},B_{f},C$ and the function $E{(\cdot)}$ describe the linear and nonlinear dynamics of the model, respectively. Following, we restrict the class of filters to linear transfer functions whose residual consists of two terms: $r = {{G{\lbrack x\rbrack}{(f)}} + {r{\lbrack x\rbrack}{(d)}}}$ where $G{\lbrack x\rbrack}$ is a linear time invariant transfer function expressing the mapping from the fault $f{(\cdot)}$ to the residual, and $r{\lbrack x\rbrack}{(d)}$ is the contribution of the unknown disturbance $d{(\cdot)}$, and $x \in {\mathbb{R}}^{n}$ denotes the coefficients of the FDI filter to be designed.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Example 2: Fault Detection and Isolation", "weight": 1.0} -->

For linear systems (i.e., $E \equiv 0$) perfect decoupling between $d$ and $r$ may be possible (i.e., ${r{\lbrack x\rbrack}{(d)}} \equiv 0$ for all $d$). For nonlinear systems, however, may not be the case. In this light, to minimize the impact of nonlinearities and disturbances on the residual, an optimal FDI filter can be obtained by the min-max program where the quadratic term $x^{\intercal}Q_{d}x$ represents the $\mathcal{L}_{2}$-norm of $r{\lbrack x\rbrack}{(d)}$ over a given receding horizon, $\mathcal{D}$ is the space of possible disturbance patterns, and the last (non-convex) constraint is concerned with the norm of $G{\lbrack x\rbrack}$ as an operator.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Example 2: Fault Detection and Isolation", "weight": 1.0} -->

The matrices $H$ and $F$ are determined by the linear terms of the system dynamics, and the positive semidefinite matrix $Q_{d}$ reflects the nonlinearity signature of the system dynamics in the presence of a disturbance pattern $d$; it depends on $d$ and the nonlinear term $E{(\cdot)}$ of. We refer interested readers to for details of the derivation of the above program.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Example 2: Fault Detection and Isolation", "weight": 1.0} -->

For numerical case study, we consider an application of the above FDI design to detect a cyber intrusion in a two-area power network discussed. The setup in this example is a simplified version of \[, Section IV\] where each power area contains one generator.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Example 2: Fault Detection and Isolation", "weight": 1.0} -->

Thus, the state in comprises $X ≔ \left\lbrack {\Delta\phi},\left\{ {\Deltaf_{i}} \right\}_{1:2},\left\{ {\DeltaP_{m_{i}}} \right\}_{1:2},\left\{ {\DeltaP_{agc_{i}}} \right\}_{1:2} \right\rbrack^{\intercal}$ where $\Delta\phi$ is the voltage angle difference between the ends of the tie line, $\Deltaf_{i}$ the generator frequency, $\DeltaP_{m_{i}}$ the generated mechanical power, and $\DeltaP_{agc_{i}}$ the automatic generation control (AGC) signal in each area.^22^2The symbol $\Delta$ stands for the deviation from the nominal value..

<!-- chunk {"id": "body-0045", "role": "body", "section": "Example 2: Fault Detection and Isolation", "weight": 1.0} -->

The system dynamics is modeled in the framework of; the details are provided in Appendix B.1. The disturbance signal $d{(\cdot)}$ represents a load deviation that may occur in the first area. The signal $f$ models the intrusion signal in the AGC of the first area, and the measurement signals are the frequencies and output power of the turbines, i.e., $Y = \left\lbrack \left\{ {\Deltaf_{i}} \right\}_{1:2},\left\{ {\DeltaP_{m_{i}}} \right\}_{1:2} \right\rbrack^{\intercal}$. For a given horizon $T > 0$, we consider the class of disturbance signatures where $a_{k}{(\alpha)}$ are the constant coefficients parametrized by $\alpha$. The choice of $\mathcal{D}$ allows one to exploit available spectrum information of the disturbance signals.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Example 2: Fault Detection and Isolation", "weight": 1.0} -->

In this example, motivated by the emphasis on both low and high frequency regions, we assume ${a_{k}{(\alpha)}} ≔ {5\left({{\alpha0.5^{k}} + {{({1 - \alpha})}0.5^{|{10 - k}|}}} \right)}$, $p = 30$, and $T = {4\text{sec}}$. For scenario generation, we consider a uniform probability distribution for the parameter $\alpha \in {\lbrack 0,1\rbrack}$, which in fact induces the probability measure $\mathbb{P}$ on $\mathcal{D}$. Let $d_{0} \in \mathcal{D}$ be a disturbance signature with the corresponding parameter $\alpha_{0}$. It is straightforward to observe that where the function $g$, denoted in view of Proposition 3.8, is an invertible lower bound for the measure of open balls in $\mathcal{D}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Example 2: Fault Detection and Isolation", "weight": 1.0} -->

For the particular set of parameters in this example and specific operating region of interest, one can show that the mapping $d\mapsto Q_{d}$ is Lipschitz continuous with the constant $L_{d} = 0.02$; see Appendix B.2 for more details. By virtue of Proposition 3.8 and normalizing^33^3Due to the linearity of the filter operator, one can always normalize the filter coefficients with no performance deterioration. the optimizer of the $SCP$ counterpart of the program, we can introduce the ULB candidate Notice that the Infinite norm constraint in is in fact a non-convex constraint. However, one may view it as the union of a finite number of constraint sets, see \[, Remark 3.2\]. Therefore, the optimization problem is already in the framework of $RP$ as introduced in where $m$ is the number of rows in matrix $F$. It is remarkable that $m - 1$ equals the degree of the FDI filter chosen a priori.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Example 2: Fault Detection and Isolation", "weight": 1.0} -->

Thanks to the min-max structure of the robust program, the Lipschitz constant of Lemma 3.4 for each subprogram of is $L_{\text{SP}} = 1$, see Remark 3.5. ‣ 3.1. Confidence interval for the objective functions ‣ 3. Probabilistic Objective Performance ‣ Performance Bounds for the Scenario Approach and an Extension to a Class of Non-convex Programs").

<!-- chunk {"id": "body-0049", "role": "body", "section": "Example 2: Fault Detection and Isolation", "weight": 1.0} -->

In this example, the dimension of the decision variable $x$ is $n = 55$, the number of rows in $F$ is $m = 5$, and the confidence level is set to $\beta = 0.01$. Therefore, to achieve the confidence interval ${I{(\varepsilon)}} = {h{(\varepsilon)}} = {5 \times 10^{- 4}}$, we need to set $\varepsilon = {3.57 \times 10^{- 3}}$ which, due to Theorem 4.1.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Example 2: Fault Detection and Isolation", "weight": 1.0} -->

‣ 4. Extension to a Class of Non-Convex Programs ‣ Performance Bounds for the Scenario Approach and an Extension to a Class of Non-convex Programs"), requires to generate $N$ disturbance signatures $d \in \mathcal{D}$ so that (a) Scenarios of the disturbance signatures (solid), and intrusion signal (dash) (b) Energy of the filter residual (solid), and the threshold level (dash) (c) Residual response before the intrusion starts Figure 5. Numerical results for Example 2 Figures 5 demonstrate the numerical results of Example 2 over the course of $15$ seconds. In Figure 5(a), 30 different realizations of disturbance inputs as well as an intrusion signal starting from $t = 10$ are shown in solid and dash curves, respectively. Figure 5(b) depicts the energy of the filter residual for the last $T = 4$ seconds (solid), and the threshold level associated with confidence $\beta = 0.01$ (dash).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Example 2: Fault Detection and Isolation", "weight": 1.0} -->

Notice that the proposed threshold is $\gamma^{\star} + 0.0005$, where $\gamma^{\star}$ is the optimal solution of the random counterpart of the program with N = 22618 scenarios. Figure 5(c) presents the filter response which is the same figure as 5(b) but zoomed in on the period prior to the intrusion.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion and Future Direction", "weight": 1.5} -->

In this article we presented probabilistic performance bounds for both $RCP$ and ${CCP}_{\varepsilon}$ via $SCP$. The proposed bounds are based on considering the tail probability of the worst-case constraint violation of the $SCP$ solution as introduced together with some classical results from perturbation theory of convex optimization. In contrast to earlier approaches, this methodology is, to the best of our knowledge, the first confidence bounds for the objective performance of RCPs and CCPs based on scenario programs. Subsequently, we extended our results to a certain class of non-convex programs allowing for binary decision variables.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Conclusion and Future Direction", "weight": 1.5} -->

For future work, in light of Theorems 3.6. ‣ 3.1. Confidence interval for the objective functions ‣ 3. Probabilistic Objective Performance ‣ Performance Bounds for the Scenario Approach and an Extension to a Class of Non-convex Programs") and 3.7. ‣ 3.1. Confidence interval for the objective functions ‣ 3. Probabilistic Objective Performance ‣ Performance Bounds for the Scenario Approach and an Extension to a Class of Non-convex Programs"), we aim to study the derivation of ULBs as introduced in Definition 3.1. Meaningful ULBs may depend highly on the individual structure of the optimization problems, in particular the uncertainty set and the constraint functions. Another potential direction, as highlighted by Example 1 in Section 5.1, is to investigate the relation between the constant $L_{\text{SP}}$ in and the dual optimizers of the program $SCP$.
