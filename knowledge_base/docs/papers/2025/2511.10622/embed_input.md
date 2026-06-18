<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Verification of Sequential Convex Programming for Parametric Non-convex Optimization

Topics include Convex optimization, Optimization, Control, Sequential convex programming, Optimization problem.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce a verification framework to exactly verify the worst-case performance of sequential convex programming (SCP) algorithms for parametric non-convex optimization. The verification problem is formulated as an optimization problem that maximizes a performance metric (e.g., the suboptimality after a given number of iterations) over parameters constrained to be in a parameter set and iterate sequences consistent with the SCP update rules. Our framework is general, extending the notion of SCP to include both conventional variants such as trust-region, convex-concave, and prox-linear methods, and algorithms that combine convex subproblems with rounding steps, as in relaxing and rounding schemes. Unlike existing analyses that may only provide local guarantees under limited conditions, our framework delivers global worst-case guarantees - quantifying how well an SCP algorithm performs across all problem instances in the specified family. Applications in control, signal processing, and operations research demonstrate that our framework provides, for the first time, global worst-case guarantees for SCP algorithms in the parametric setting.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we are interested in solving the parametric non-convex optimization problem

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $z \in \text{R}^{n}$ is the decision variable, $x \in \mathcal{X} \subseteq \text{R}^{d}$ is the *problem parameter*, $\mathcal{X}$ is a known set, ${\Omega{(x)}} \subseteq \text{R}^{n}$ is the possibly non-convex feasible region, and $f:{{\text{R}^{n} \times \text{R}^{d}}\rightarrow\text{R}}$ is the possibly non-convex objective with respect to $z$. In many settings, we must repeatedly solve problem \\tagform@1 with a varying problem parameter $x$. For instance, in model predictive control Borrelli et al.; Chen et al., we repeatedly solve optimal control problems with varying initial states. In energy systems, we repeatedly solve optimal power flow problems with varying loads and renewable generation Hentenryck; Baker. In signal processing, we repeatedly solve sparse coding problems with varying noisy measurements Gregor and LeCun; Liu et al..

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In operations research, such parametric structure arises in optimization problems over networks (e.g., traffic assignment, routing, or graph-based flow problems) where the underlying topology remains fixed but demands or costs vary across instances Still.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Global approaches such as branch-and-bound Lawler and Wood; Belotti et al. and branch-and-cut Padberg and Rinaldi; Stubbs and Mehrotra can, in principle, provide globally optimal solutions to problem \\tagform@1. However, these methods scale poorly with problem size and are often not practical in time-sensitive settings where real-time optimization is required Bertsimas and Stellato; Bengio et al.. Instead, it is common to rely on faster, heuristic approaches such as *sequential convex programming* Gill et al.; Dinh and Diehl; Nocedal and Wright; Boyd et al. in which a sequence of convex problems is solved. Convex optimization enjoys both a rich theoretical foundation, with strong guarantees of global optimality Boyd and Vandenberghe, and a mature ecosystem of efficient algorithms Boyd et al.; Parikh and Boyd; Ryu and Boyd; Ryu and Yin and solvers Goulart and Chen; Stellato et al.; O'Donoghue that make it practical for applications where real-time optimization is required.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many methods fall under this broad category of sequential convex programming. One widely used approach is the trust-region method Nocedal and Wright; Byrd et al., where at each iteration a local convex model is optimized within a bounded region around the current iterate. Another example is the convex-concave procedure (CCP) for difference-of-convex (DC) programming problems Lipp and Boyd; Yuille and Rangarajan; Shen et al., where the concave part of the objective or constraints is linearized to yield a convex subproblem. For composite optimization, the prox-linear method Drusvyatskiy and Paquette; Drusvyatskiy is a popular approach. At each iteration, it replaces the smooth inner map with its linearization and evaluates the convex (possibly non-smooth) outer function on this approximation, thereby reducing each step to a convex subproblem. It is common to use variants of these approaches, for example, by using penalized procedures or hyperparameters (e.g., the trust-region size) that vary over the iterations Lipp and Boyd.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Relaxing and rounding schemes are another popular way to solve problems of the form \\tagform@1 when the feasible set includes discrete constraints. A common example is to relax a non-convex constraint to obtain a convex problem and then round the resulting solution Goemans and Williamson; Ageev and Sviridenko. The work of Diamond et al. systematizes this approach with the relax-round-polish method: first, a relaxation of the non-convex problem is solved, then the discrete variables are rounded, and finally the remaining continuous variables are re-optimized by solving a convex problem. Like SCP, these methods rely on solving a sequence of convex optimization problems, but they differ in that they include explicit non-convex projection steps.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

While both conventional SCP methods and related heuristic methods that combine convex subproblems with rounding steps are widely used in practice, they lack guarantees on their global worst-case performance Diamond et al.; Boyd et al.; Lipp and Boyd. Such limitations can be unacceptable in systems where it is essential to *verify* the global quality of the candidate solution of these algorithms over all admissible parameters in the set $\mathcal{X}$. At the same time, existing analyses typically do not take advantage of the parametric structure of problem \\tagform@1. Exploiting this structure creates an opportunity to construct global guarantees in cases where none are otherwise available.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contributions", "weight": 1.0} -->

In this paper, we develop a framework to verify the global worst-case performance of sequential convex programming methods for parametric non-convex optimization. While SCP is traditionally understood to involve only convex subproblems, we adopt a broader definition that also encompasses algorithms combining convex subproblems with simple non-convex projection steps (e.g., in rounding schemes). Our verification method is meant to be solved offline (i.e., in a time-insensitive setting), so that the algorithm can then be used online when the problem parameter is seen (i.e., in a time-sensitive setting) with certified worst-case guarantees. In this work, we focus on the setting of non-convex quadratically-constrained quadratic programs with potentially additional discrete constraints (i.e., binary or sparsity constraints).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contributions", "weight": 1.0} -->

Verification framework for global performance guarantees. We introduce a verification framework to certify the global worst-case performance of SCP methods for parametric non-convex optimization. In this framework, verification is posed as an optimization problem that maximizes a performance metric over problem parameters constrained to a specified set and iterate sequences consistent with the SCP update rules for a given number of iterations. We focus on three complementary aspects of performance: (i) suboptimality with respect to the optimal value of problem \\tagform@1 in cases where feasibility of the candidate solution can be guaranteed, (ii) the worst-case level of constraint violation of the candidate solution when feasibility cannot be guaranteed, and (iii) feasibility of downstream convex subproblems which contain only linear constraints.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Contributions", "weight": 1.0} -->

Applicability across sequential convex programming algorithms. Our framework can be applied across a range of SCP algorithms including conventional variants such as trust-region, convex-concave, and prox-linear methods, and algorithms that combine convex subproblems with rounding steps such as relax-round-polish. The key idea to our approach is to encode the algorithm's steps---both convex quadratic programs (QPs) and rounding operations---as constraints in the verification problem through their optimality conditions. In the most general case, this yields a verification problem that is a mixed-integer quadratically-constrained quadratic program that can be solved using modern solvers.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Contributions", "weight": 1.0} -->

Numerical examples. Through a broad variety of numerical examples from control, signal processing, and operations research, we demonstrate the utility of our framework in certifying worst-case guarantees on the performance of SCP algorithms. Our approach is able to provide exact numerical guarantees where no known analytic methods are able to. Our results reveal a broad spectrum of algorithmic behaviors, from certifiable convergence to optimality to cases where the worst-case guarantee plateaus short of global optimality, and even complete failure to make progress toward finding a feasible solution beyond the first iteration. These examples also show how the framework can provide further insights to design algorithms, such as hyperparameter selection and initialization choice.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Layout of the paper", "weight": 1.0} -->

In Section 2, we review related work. In Section 3, we introduce several SCP algorithms including the trust-region method, the CCP, the prox-linear method, and the relax-round-polish method. In Section 4, we present our verification framework to obtain global worst-case performance guarantees. In Section 5, we showcase the utility of this verification framework with many numerical examples. Finally, in Section 6, we conclude.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Conventional sequential convex programming", "weight": 1.0} -->

Sequential convex programming Gill et al.; Dinh and Diehl; Nocedal and Wright; Boyd et al.; Byrd et al.; Bonalli et al. conventionally refers to an algorithmic approach that solves non-convex problems by repeatedly constructing and solving convex approximations. Classical examples include the trust-region method Nocedal and Wright; Byrd et al.; Boyd et al., the CCP for DC programming Tao and An; Lipp and Boyd; Yuille and Rangarajan, and the prox-linear method for composite minimization Drusvyatskiy and Paquette; Lewis and Wright. In certain cases, some of these methods come with local guarantees Drusvyatskiy and Paquette; Bonalli et al., but in all cases, constructing tight global worst-case guarantees remains a challenge. Our framework can exactly certify the worst-case performance of such SCP methods in the parametric setting of \\tagform@1.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Relaxation and rounding methods", "weight": 1.0} -->

Relaxation and rounding schemes are widely used to tackle non-convex problems by replacing difficult discrete constraints with relaxed convex constraints, followed by either deterministic Ageev and Sviridenko; Nannicini and Belotti or randomized Goemans and Williamson; Raghavan and Tompson rounding to produce candidate solutions. A systematic formulation of this approach for deterministic rounding is the relax-round-polish framework Diamond et al., which combines a convex relaxation, a non-convex rounding step, and a subsequent polishing step that re-optimizes the continuous, convex variables. Such methods often yield strong empirical performance, but they lack worst-case guarantees on suboptimality and feasibility Diamond et al.. While SCP is traditionally understood to involve only convex subproblems, we adopt a broader definition that also encompasses algorithms combining convex subproblems with rounding steps (e.g., in relax-round-polish). Our framework also provides a way to exactly certify the worst-case performance of these methods.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Guarantees in parametric optimization", "weight": 1.0} -->

Recently, several works have studied tight performance bounds for algorithms that solve parametric optimization problems. The works of Ranjan et al.; Ranjan and Stellato are most similar to ours: they verify the worst-case performance of first-order methods for parametric convex optimization problems by encoding the algorithm steps as constraints in the verification problem. In contrast, our work verifies the performance of SCP algorithms for parametric non-convex optimization problems. Another key distinction is that in our setting, the algorithmic steps are defined *implicitly* through convex subproblems rather than through explicit update rules. Moreover, while global worst-case guarantees exist in convex optimization, no such guarantees are available in our non-convex setting.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Guarantees in parametric optimization", "weight": 1.0} -->

Other methods provide *probabilistic guarantees* on the performance of algorithms to solve parametric optimization problems Sambharya and Stellato; Huang et al.; however, these methods rely on the assumption that the problem parameters are independently and identically distributed (i.i.d.). This assumption is often hard to verify and may not be realistic in many scenarios (e.g., when problems are solved sequentially as in control applications Borrelli et al. ). Moreover, these guarantees only hold with high-probability---meaning that performance can still be arbitrarily poor even if it occurs rarely.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Finite-iteration guarantees in learning to optimize", "weight": 1.0} -->

An adjacent research area, learning to optimize (L2O) Chen et al.; Amos; Bengio et al., focuses on learning to accelerate algorithms for parametric optimization. L2O methods have been applied to a range of non-convex settings---for example, learning branching rules or the discrete variables for mixed-integer optimization Bengio et al.; Khalil et al.; Bertsimas and Stellato; Cauligi et al., and learning warm starts for SCP Banerjee et al. ---where they often deliver impressive empirical results. A central challenge in L2O, however, is guaranteeing performance after a finite number of iterations of an algorithm Chen et al.; Amos. One line of work addresses this gap with probabilistic generalization bounds, showing that a learned optimizer likely performs well on unseen problem instances Sambharya and Stellato; Sucker et al.; Sambharya et al.; Saravanos et al.; Sambharya and Stellato; Balcan et al..

<!-- chunk {"id": "body-0020", "role": "body", "section": "Finite-iteration guarantees in learning to optimize", "weight": 1.0} -->

Another line develops worst-case, finite-iteration guarantees, but these results hold only for convex problems Sambharya et al.; Banert et al.; Martin et al.. Although our work also considers the parametric setting, it differs fundamentally in that we do not learn an optimizer. Instead, we exactly verify the worst-case finite-iteration performance of SCP methods for parametric non-convex optimization---providing guarantees in a regime where existing L2O worst-case bounds do not apply.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Neural network verification", "weight": 1.0} -->

Our approach is closely related in spirit to neural network verification, which seeks to certify that for every admissible input (e.g., an image within a bounded perturbation set), the network's output satisfies a desired property (e.g., correct classification) Tjeng et al.; Ceccon et al.; Anderson et al.. The key similarity between the two lies in formulating verification as an optimization problem that searches for the most adversarial instance while encoding the computation steps (either the forward pass of a neural network or an SCP algorithm) as constraints.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Sequential convex programming algorithms", "weight": 1.0} -->

In this section, we introduce several SCP algorithms that fit within our verification framework. We focus on the trust-region method in Subsection 3.1, the penalized CCP in Subsection 3.2, the prox-linear method in Subsection 3.3, and the relax-round-polish method in Subsection 3.4. In each type of algorithm, we first write the non-convex optimization problem under consideration (which is a special case of problem \\tagform@1), and then present the algorithm steps. All methods can be described by the iterations $z^{k + 1} \in {s^{k}{(z^{k},x)}}$, where $z^{k}$ is the $k$-th iterate and $s^{k}:{{\text{R}^{n} \times \text{R}^{d}}\rightrightarrows\text{R}^{n}}$ is a (possibly multi-valued) operator.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Sequential convex programming algorithms", "weight": 1.0} -->

In this paper, we focus on the quite general case where the non-convex problems are mixed-integer quadratically-constrained quadratic programs. For the algorithms we consider^11^1except for the relax-round-polish method which has no initial point, the choice of initialization $z^{0}$ and hyperparameters can significantly influence the quality of the candidate solution produced by the algorithm.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Trust-region method", "weight": 1.0} -->

In this subsection, we consider the trust-region method to solve the problem

<!-- chunk {"id": "body-0025", "role": "body", "section": "Trust-region method", "weight": 1.0} -->

where $z \in \text{R}^{n}$ is the decision variable, $x \in \text{R}^{d}$ is the problem parameter, the functions $f:{{\text{R}^{n} \times \text{R}^{d}}\rightarrow\text{R}}$ and $g:{{\text{R}^{n} \times \text{R}^{d}}\rightarrow\text{R}^{m}}$ may be non-convex in $z$, and $h:{{\text{R}^{n} \times \text{R}^{d}}\rightarrow\text{R}^{p}}$ may be non-affine in $z$. The trust-region method iteratively builds local convex approximations around the current iterate and solves the resulting subproblems subject to a trust-region constraint Boyd et al.. Formally, given a current iterate $z^{k}$, we construct the trust-region subproblem

<!-- chunk {"id": "body-0026", "role": "body", "section": "Trust-region method", "weight": 1.0} -->

where $\hat{f}{(z,x,z^{k})}$ and $\hat{g}{(z,x,z^{k})}$ are convex approximations of $f$ and $g$ around $z^{k}$, $\hat{h}{(z,x,z^{k})}$ is an affine approximation of $h$ around $z^{k}$, and $\rho_{k} > 0$ is the trust-region radius at the $k$-th iteration. The trust-region constraint prevents the next iterate from moving too far from the current iterate, ensuring that the convexified problem is a meaningful local model of the non-convex problem.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Penalized convex-concave procedure", "weight": 1.0} -->

In this subsection, we consider the penalized CCP to solve the DC program

<!-- chunk {"id": "body-0028", "role": "body", "section": "Penalized convex-concave procedure", "weight": 1.0} -->

where $z \in \text{R}^{n}$ is the decision variable and $f_{i}:{{\text{R}^{n} \times \text{R}^{d}}\rightarrow\text{R}}$ and $g_{i}:{{\text{R}^{n} \times \text{R}^{d}}\rightarrow\text{R}}$ are convex functions in $z$ for $i = {0,\ldots,m}$. Problem \\tagform@4 is convex only if the $g_{i}$ functions are *affine* in $z$. The penalized CCP involves solving a series of optimization subproblems of the form

<!-- chunk {"id": "body-0029", "role": "body", "section": "Penalized convex-concave procedure", "weight": 1.0} -->

where $z \in \text{R}^{n}$ (the original decision variable) and $s \in \text{R}^{m}$ (introduced slack variables) are the decision variables, and $\tau_{k} > 0$ is a hyperparameter that weights the constraint violations at the $k$-th iteration. At each iterate $z^{k}$, the non-affine functions are replaced with their local affine approximations ${{\hat{g}}_{i}{(z,x,z^{k})}} = {{g_{i}{(z,x)}} + {{\nabla_{z}g_{i}}{(z^{k},x)}^{T}{({z - z^{k}})}}}$ for $i = {0,\ldots,m}$. By introducing slacks and penalizing their violation in the objective, the penalized CCP ensures that each subproblem remains feasible while still driving the iterates toward satisfaction of the original non-convex constraints.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Prox-linear method", "weight": 1.0} -->

In this subsection, we focus on the prox-linear method, an algorithm that is specialized to minimize composite functions of the form

<!-- chunk {"id": "body-0031", "role": "body", "section": "Prox-linear method", "weight": 1.0} -->

where $z$ is the decision variable and $\rho > 0$ is a regularization hyperparameter. Problem \\tagform@7 is convex in $z$ since convex functions composed with affine mappings are convex. We focus on the case where $h$ is the absolute value function and $c$ is a non-convex quadratic function---a case which has many applications Drusvyatskiy. Under certain assumptions, the iterates of the prox-linear method are known to converge to a point that is nearly stationary Drusvyatskiy and Paquette.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Relax-round-polish method", "weight": 1.0} -->

We now turn to an algorithm that is not typically viewed as an SCP method, due to the presence of a non-convex projection step: the relax-round-polish algorithm Diamond et al.. We apply it to the non-convex problem

<!-- chunk {"id": "body-0033", "role": "body", "section": "Relax-round-polish method", "weight": 1.0} -->

where the decision variable is $z = {(w,v)}$ with $w \in \text{R}^{n_{w}}$ and $v \in \text{R}^{n_{v}}$. The problem parameter is given by all of the problem data: i.e., $x = {(P_{w},c_{w},P_{v},c_{v},A,B,d)}$. Moreover, $P_{w} \succeq 0$ and $P_{v} \succeq 0$, so problem \\tagform@8 is a convex problem except for the non-convex constraint $v \in \mathcal{Z}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Relax-round-polish method", "weight": 1.0} -->

The relax-round-polish method consists of the following three steps.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Relax-round-polish method", "weight": 1.0} -->

Relax: Solve a convex relaxation of problem \\tagform@8. For binary constraints, we replace $v \in {\{ 0,1\}}^{n_{v}}$ with $v \in {\lbrack 0,1\rbrack}^{n_{v}}$. For sparsity constraints, we soften the condition by solving problem \\tagform@8 without the non-convex constraint but with an added penalty of $\lambda{\| v\|}_{1}$ for a chosen hyperparameter $\lambda > 0$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Relax-round-polish method", "weight": 1.0} -->

Round: Take the solution of the relaxed problem and project the variable $v$ to the non-convex set. For binary variables, this means rounding each entry of $v$ to either $0$ or $1$. For sparsity constraints, this means keeping the $k$ entries of largest magnitude and setting the other entries to $0$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Relax-round-polish method", "weight": 1.0} -->

Polish: With the discrete variables $v$ fixed, solve the resulting convex subproblem in the decision variable $w$. This step sharpens the continuous variables $w$ while enforcing consistency with the discrete variables $v$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Relax-round-polish method", "weight": 1.0} -->

Each of these three steps can be written in the form of the iterations $z^{k + 1} \in {s^{k}{(z^{k},x)}}$, where each operator $s^{k}$ is different. In this case of relax-round-polish, there is no need for an initialization $z^{0}$. While the relax and round steps are feasible optimization problems, there is no guarantee that the polish convex subproblem is feasible Diamond et al..

<!-- chunk {"id": "body-0039", "role": "body", "section": "Verification framework", "weight": 1.0} -->

In this section, we introduce our verification framework for certifying the global worst-case performance of SCP methods for parametric non-convex optimization. In Subsection 4.1, we formulate the verification problem as an optimization problem that maximizes a performance metric subject to constraints that i) encode the SCP steps, ii) enforce the parameter is in a set $\mathcal{X}$, iii) enforce that the initial point is in a set $S$, and iv) impose optimality on the true solution to problem \\tagform@1. In Subsection 4.2, we show how to encode the algorithm steps (the convex QPs and rounding steps) as constraints in the verification problem. Then in the next three subsections, we focus on three specific cases: verifying suboptimality when feasibility of the final iterate can be guaranteed in Subsection 4.3, verifying the level of constraint violation when feasibility cannot be guaranteed in Subsection 4.4, and verifying the feasibility of convex subproblems with linear constraints in Subsection 4.5.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Verification framework", "weight": 1.0} -->

Finally, in Subsection 4.6, we show how to incorporate inexact solves to the convex subproblems into our framework.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Formulating the verification problem", "weight": 1.0} -->

Before presenting the verification formulations, we detail the algorithmic updates, initialization sets, and performance metrics that together specify how the algorithms are run and evaluated.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Algorithm steps", "weight": 1.0} -->

All of the algorithms outlined in Section 3 can be represented by the iterations

<!-- chunk {"id": "body-0043", "role": "body", "section": "Algorithm steps", "weight": 1.0} -->

where $s^{k}:{{\text{R}^{n} \times \text{R}^{d}}\rightrightarrows\text{R}^{n}}$ is a (possibly multi-valued) operator and $K$ is the number of iterations. The number of steps $K$ is either dictated by i) the prescribed number of steps within an algorithm (e.g., exactly three in relax-round-polish) or ii) the number of iterations one has time to run (e.g., in the case of trust-region and prox-linear methods). The operators $s^{k}$ need not be identical across iterations: different steps in an algorithm may correspond to solving different convex subproblems or applying different rounding rules. Moreover, we model each $s^{k}$ as a multi-valued operator since all of the algorithm steps we consider may have more than one solutions. Throughout, we assume that each subproblem admits at least one solution; issues of subproblem infeasibility are treated separately later in Subsection 4.5.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Initial points", "weight": 1.0} -->

Most of the algorithms we consider require an initial point $z^{0}$ which can significantly affect the quality of the resulting candidate solution Boyd et al.. We model the initialization by assuming that $z^{0}$ belongs to some known non-empty set $S$. For cold-started algorithms, the set of initial points is $S = {\{\mathbf{0}_{n}\}}$. When a heuristic warm start $z^{ws} \in \text{R}^{n}$ is available, we simply take $S = {\{ z^{ws}\}}$. For algorithms whose first step does not depend on $z^{0}$ (e.g., relax-round-polish), the specification of $S$ is omitted.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Performance metrics", "weight": 1.0} -->

We are interested in analyzing the worst-case performance in terms of some performance metric $\phi{(z^{K},z^{\star},x)}$ where $z^{K}$ is a candidate solution and $z^{\star}$ is the optimal solution to the original non-convex problem. We focus on three key aspects of performance in our verification framework: suboptimality, the level constraint violation, and subproblem feasibility.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Performance metrics", "weight": 1.0} -->

Suboptimality. To provide guarantees on suboptimality, we let

<!-- chunk {"id": "body-0047", "role": "body", "section": "Performance metrics", "weight": 1.0} -->

where $f{(z,x)}$ is the objective function of the original non-convex problem \\tagform@1, and $z^{\star}$ is the solution parametrized by parameter $x$. In this case, it is necessary that the final iterate $z^{K}$ be feasible, which is the case in many scenarios (see Subsection 4.3 for details).

<!-- chunk {"id": "body-0048", "role": "body", "section": "Performance metrics", "weight": 1.0} -->

Level of constraint violation. Given constraints of the form ${\Omega{(x)}} = {\{ z\mid{{g{(z,x)}} \leq 0}\}}$, the square of the $\ell_{2}$-norm of violations is quantified as

<!-- chunk {"id": "body-0049", "role": "body", "section": "Performance metrics", "weight": 1.0} -->

We could easily adapt this metric to other norms, such as the $\ell_{1}$-norm or the $\ell_{\infty}$-norm of violations. Moreover, the metric \\tagform@10 could be adapted to handle equality constraints.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Performance metrics", "weight": 1.0} -->

Subproblem feasibility. Sometimes, we cannot guarantee that the convex subproblems are feasible. For example, in the relax-round-polish method, once the discrete variables are fixed, there is no guarantee that there exists continuous variables that can satisfy the constraints. We show how to use the Farkas Lemma in Subsection 4.5 to check feasibility of downstream convex QPs.

<!-- chunk {"id": "body-0051", "role": "body", "section": "The verification problem", "weight": 1.0} -->

Using the algorithm steps, initial points, and performance metrics from above, we formulate the verification problem as

<!-- chunk {"id": "body-0052", "role": "body", "section": "The verification problem", "weight": 1.0} -->

We let $\delta$ denote the optimal value of problem \\tagform@11. In order for verification problem \\tagform@11 to be well-posed, we rely on the following three assumptions.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Assumption 1 (Existence of optimal solution)", "weight": 1.0} -->

For all parameters $x \in \mathcal{X}$, there exists a minimizer $z^{\star}{(x)}$ for problem \\tagform@1.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Assumption 2 (Non-empty sets)", "weight": 1.0} -->

The parameter set $\mathcal{X}$ and initial point set $S$ are both non-empty.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Assumption 3 (Well-posed subproblems)", "weight": 1.0} -->

For every parameter $x \in \mathcal{X}$ and initialization $z^{0} \in S$, each update subproblem that defines $z^{k + 1}$ is well-posed. That is, whenever the algorithm reaches iteration $k$ with iterate $z^{k}$, the corresponding update operator satisfies ${{s^{k}{(z^{k},x)}} \neq {\varnothing\text{for all~}k} = 0},{\ldots,{K - 1}}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Assumption 3 (Well-posed subproblems)", "weight": 1.0} -->

Assumption 1. ‣ The verification problem. ‣ 4.1 Formulating the verification problem ‣ 4 Verification framework ‣ Verification of Sequential Convex Programming for Parametric Non-convex OptimizationSubmitted to the editors 11/26/2025.") is mild and amounts to requiring that the parametric problem \\tagform@1 always admits at least one minimizer. Assumption 2. ‣ The verification problem. ‣ 4.1 Formulating the verification problem ‣ 4 Verification framework ‣ Verification of Sequential Convex Programming for Parametric Non-convex OptimizationSubmitted to the editors 11/26/2025.") is also mild, requiring that there is at least one feasible parameter and initial point. Throughout the paper, we assume that these two assumptions hold.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Assumption 3 (Well-posed subproblems)", "weight": 1.0} -->

Assumption 3. ‣ The verification problem. ‣ 4.1 Formulating the verification problem ‣ 4 Verification framework ‣ Verification of Sequential Convex Programming for Parametric Non-convex OptimizationSubmitted to the editors 11/26/2025.") requires more care. In many algorithmic settings this condition is natural---e.g., in the trust-region method where the constraints are convex and every admissible initial point is feasible for all parameters $x \in \mathcal{X}$. However, there are also important situations in which the assumption may fail, such as when downstream convex subproblems become infeasible (e.g., the final polish step in relax-round-polish). We remark that this assumption concerns only iterates generated by the algorithm; it does not impose feasibility of the $k$-th subproblem (corresponding to $s^{k}{(z^{k},x)}$) for arbitrary $z^{k}$, but only for those $z^{k}$ that arise during a valid run of the method.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Assumption 3 (Well-posed subproblems)", "weight": 1.0} -->

Efficiently encoding the algorithms steps and optimality conditions in problem \\tagform@11 is a challenge since the steps are *implicitly* defined by optimization subproblems. Moreover, the presence of tie-breakers introduces pessimism: the verification framework must account for the worst-case outcome of any tie when representing the algorithm's behavior. In Subsection 4.2 we show how to encode algorithm steps via their optimality conditions. To verify suboptimality, we show how to handle the optimality condition in problem \\tagform@11 in Subsection 4.3.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Encoding algorithm steps", "weight": 1.0} -->

In this subsection, we show how to encode the algorithm steps in SCP methods as constraints in the verification problem \\tagform@11. These building blocks are the components that we use to construct the verification problem for various algorithms. We show how to encode convex QPs in Subsection 4.2.1 and projections onto some non-convex sets in Subsection 4.2.2.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Convex quadratic problems", "weight": 1.0} -->

The main SCP steps we consider are convex QPs that take the primal and dual formulations of the form

<!-- chunk {"id": "body-0061", "role": "body", "section": "Convex quadratic problems", "weight": 1.0} -->

where the primal variables are $u \in \text{R}^{n_{u}}$ and $s \in \text{R}^{n_{s}}$ and the dual variable is $y \in \text{R}^{n_{y}}$. The Karush-Kuhn-Tucker (KKT) conditions of problem \\tagform@12 are O'Donoghue

<!-- chunk {"id": "body-0062", "role": "body", "section": "Convex quadratic problems", "weight": 1.0} -->

Since problem \\tagform@12 is convex, the KKT conditions are always sufficient for optimality, and are necessary if Slater's condition holds. Since we assume that each QP is feasible (under Assumption 3. ‣ The verification problem. ‣ 4.1 Formulating the verification problem ‣ 4 Verification framework ‣ Verification of Sequential Convex Programming for Parametric Non-convex OptimizationSubmitted to the editors 11/26/2025.")) and the feasible region is polyhedral, Slater's condition is always satisfied. Hence, the KKT conditions are necessary and sufficient for optimality.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Convex quadratic problems", "weight": 1.0} -->

As is standard in the bilevel programming literature Sinha et al., we avoid writing nested optimization problems in the verification problem \\tagform@11 explicitly by reformulating the QPs through their KKT conditions. In the most general case of the verification problem, the iterates ${\{ z^{k}\}}_{k = 0}^{K - 1}$, problem parameter $x$, and the problem data of each QP $(P,A,c,b)$ (which depends on the parameter $x$ and the iterate $z^{k}$) all serve as decision variables. The resulting KKT constraints introduce non-convexities (e.g., the complementarity constraint ${s^{T}y} = 0$ is a non-convex bilinear constraint).

<!-- chunk {"id": "body-0064", "role": "body", "section": "Projections onto non-convex sets", "weight": 1.0} -->

We now consider the case where the algorithm step is a projection onto a non-convex set $\mathcal{Z} \subseteq \text{R}^{n}$ for rounding steps outlined in Subsection 3.4. We denote this projection with the operator $\Pi$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Binary variables", "weight": 1.0} -->

To formalize how the projection step onto the set ${\{ 0,1\}}^{n}$ can be enforced within our framework, we state the following proposition.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Sparsity constraints", "weight": 1.0} -->

To formalize how the projection step onto the set $\{{z \in \text{R}^{n}}\mid{{\| z\|}_{0} \leq k}\}$ can be enforced within our framework, we state the following proposition.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Verifying suboptimality", "weight": 1.0} -->

In this subsection, we show how to verify the suboptimality of the candidate solution in cases where feasibility of the final iterate can be guaranteed. In this subsection, we assume that the following assumption holds.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Assumption 4.6 (Feasibility of final iterate)", "weight": 1.0} -->

For every problem parameter $x \in \mathcal{X}$, the SCP algorithm produces a final iterate $z^{K}$ that lies in the feasible set $\Omega{(x)}$.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Assumption 4.6 (Feasibility of final iterate)", "weight": 1.0} -->

There are many settings where Assumption 4.6. ‣ 4.3 Verifying suboptimality ‣ 4 Verification framework ‣ Verification of Sequential Convex Programming for Parametric Non-convex OptimizationSubmitted to the editors 11/26/2025.") is satisfied.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Assumption 4.6 (Feasibility of final iterate)", "weight": 1.0} -->

Unconstrained settings: ${\Omega{(x)}} = \text{R}^{n}$, so feasibility holds automatically.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Assumption 4.6 (Feasibility of final iterate)", "weight": 1.0} -->

Convex feasible regions with feasibility-preserving steps: If $\Omega{(x)}$ is convex for all $x \in \mathcal{X}$, the initial point is feasible for all parameters $x \in \mathcal{X}$, and each step preserves feasibility, then the final iterate remains feasible.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Assumption 4.6 (Feasibility of final iterate)", "weight": 1.0} -->

Non-convex feasible regions with explicit enforcement: In some cases of simpler non-convex feasible regions, feasibility is ensured by the algorithm itself---for example, when ${\Omega{(x)}} = {\{ 0,1\}}^{n}$ and the final step is a rounding operation.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Assumption 4.6 (Feasibility of final iterate)", "weight": 1.0} -->

Verified feasibility with our constraint satisfaction framework: In some cases, none of the above three conditions may hold. However, we can use the framework from Subsection 4.4 to first verify that the final iterate is always feasible after a given number of iterations. If feasibility can be verified, we can then solve a second verification problem for the worst-case suboptimality.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Assumption 4.6 (Feasibility of final iterate)", "weight": 1.0} -->

The primary difficulty in solving problem \\tagform@11 for worst-case suboptimality lies in enforcing the optimality condition. In Subsection 4.2.1 we showed how to encode the minimizer of a convex QP into the verification problem by directly writing the KKT conditions as constraints. However, we cannot rely on this reformulation for the optimality condition in problem \\tagform@11 since problem \\tagform@1 is non-convex. This means that i) the KKT conditions only encode stationary points for non-convex problems and ii) in order for the KKT conditions to be necessary for even a stationary point, additional constraint qualifications (like the linear independent constraint qualification) must be satisfied.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Assumption 4.6 (Feasibility of final iterate)", "weight": 1.0} -->

It turns out that in this case where the performance metric is the suboptimality, *we do not need to encode the optimality constraint*. Instead, we relax it to a feasible constraint and formulate the problem

<!-- chunk {"id": "body-0076", "role": "body", "section": "Assumption 4.6 (Feasibility of final iterate)", "weight": 1.0} -->

Let $\overline{\delta}$ denote the optimal value of problem \\tagform@13. Observe that problem \\tagform@11 with objective ${\phi{(z^{K},z^{\star},x)}} = {{f{(z^{K},x)}} - {f{(z^{\star},x)}}}$ and problem \\tagform@13 are the same except that the optimality constraint in \\tagform@11 is replaced with a feasibility constraint in \\tagform@13. The following theorem shows that *the relaxation from problem \\tagform@11 to problem \\tagform@13 is in fact tight*.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Verifying the level of constraint violation", "weight": 1.0} -->

In the previous subsection, we assumed that the feasibility of the candidate solution $z^{K}$ could be guaranteed; yet in some cases this assumption is not realistic. In this subsection, we discuss how to measure the worst-case constraint violation (as measured by the square of the $\ell_{2}$-norm of the violations) in such cases. Assuming that the feasible region $\Omega{(x)}$ is defined by inequality constraints ${g_{i}{(z,x)}} \leq 0$, $i = {1,\ldots,m}$, we can verify the worst-case constraint violation of the candidate solution $z^{K}$ by solving the verification problem

<!-- chunk {"id": "body-0078", "role": "body", "section": "Verifying the level of constraint violation", "weight": 1.0} -->

If the optimal value of problem \\tagform@14 is zero, then the candidate solution $z^{K}$ is guaranteed to be feasible for any admissible parameter $x \in \mathcal{X}$. If the optimal value is positive, then there exists a parameter $x \in \mathcal{X}$ for which the candidate solution $z^{K}$ is infeasible, and the optimal value quantifies the corresponding level of constraint violation. In problem \\tagform@14 we penalize the square of the $\ell_{2}$-norm of violations, but we could easily adjust it to penalize other metrics (e.g., the $\ell_{\infty}$ or $\ell_{1}$ norms) of violations.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Verifying feasibility of subproblems with linear constraints", "weight": 1.0} -->

Convex subproblems arising within the SCP procedure may, in some cases, be infeasible. In this subsection, we show how our verification framework can certify whether feasibility of a convex QP at iteration $K - 1$ is guaranteed for all admissible parameters and iterates consistent with the SCP update rules. Suppose that the convex QP at the final iteration has constraints ${A^{K - 1}u} \leq b^{K - 1}$ where the problem data $A^{K - 1}$ and $b^{K - 1}$ are functions of the previous iterate $z^{K - 1}$ and parameter $x$: i.e., ${(A^{K - 1},b^{K - 1})} = {\psi^{K - 1}{(z^{K - 1},x)}}$. Feasibility of these linear constraints can be characterized using the Farkas Lemma.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Inexact solves", "weight": 1.0} -->

In practice, QPs are solved using iterative QP solvers Stellato et al.; O'Donoghue; Goulart and Chen, which are typically solved up to a given tolerance. In this subsection, we describe how to handle inexact solves to problem \\tagform@12 in our verification framework.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Inexact solves", "weight": 1.0} -->

Distance to optimality inexactness: A common modeling assumption is that the computed solution is within an $\epsilon$-distance of the true subproblem solution. In this case, we include variables for the QP's optimal solution $u^{exact}$ that exactly satisfies the KKT conditions and the inexact solution $u^{inexact}$ with the constraint ${\|{u^{exact} - u^{inexact}}\|}_{\infty} \leq \epsilon$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Inexact solves", "weight": 1.0} -->

KKT inexactness: Many QP solvers, such as SCS O'Donoghue and OSQP Stellato et al., report accuracy in terms of primal and dual residuals rather than distance to the exact solution. In this case, the iterates automatically satisfy some of the optimality conditions from Subsection 4.2 (see for example, ), but not the primal residuals ${\|{{{Au} + s} - b}\|}_{\infty} \leq \epsilon$ and dual residuals ${\|{{Pu} + {A^{T}y} + c}\|}_{\infty} \leq \epsilon$. In this case, we replace the exact optimality conditions with these constraints.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Inexact solves", "weight": 1.0} -->

We use the infinity norm since this is the standard convergence criterion in many QP solvers O'Donoghue; Stellato et al.; Ranjan and Stellato. These two models allow our framework to reliably capture the kinds of inexactness encountered in practice, ensuring that the resulting worst-case guarantees remain meaningful even when subproblems are not solved to full precision.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

In this section, we showcase the utility of our framework to verify the performance of SCP methods with numerical examples. We focus on the trust-region method in Subsection 5.1, the penalized CCP in Subsection 5.2, the prox-linear method in Subsection 5.3, and the relax-round-polish algorithm in Subsection 5.4. The code to reproduce our results is available at

<!-- chunk {"id": "body-0085", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

We solve the verification problems (which in the most general case are mixed-integer quadratically-constrained quadratic programs) to a $2\%$ optimality gap (unless otherwise indicated) using Gurobi 12.0 Gurobi Optimization. In some examples, we use scalability enhancements described in Appendix Subsection B based on optimization-based bound tightening and solving the verification problems *sequentially*. We include all of the timing results to solve the verification problems in Appendix Section C. Our results exhibit a wide range of algorithmic behaviors---from provable convergence to a globally optimal point, to scenarios where significant progress is made but plateaus short of optimality, and cases where the algorithm immediately stalls and fails to progress. In all examples, Assumptions 1. ‣ The verification problem. ‣ 4.1 Formulating the verification problem ‣ 4 Verification framework ‣ Verification of Sequential Convex Programming for Parametric Non-convex OptimizationSubmitted to the editors 11/26/2025."), 2. ‣ The verification problem.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

‣ 4.1 Formulating the verification problem ‣ 4 Verification framework ‣ Verification of Sequential Convex Programming for Parametric Non-convex OptimizationSubmitted to the editors 11/26/2025."), and 3. ‣ The verification problem. ‣ 4.1 Formulating the verification problem ‣ 4 Verification framework ‣ Verification of Sequential Convex Programming for Parametric Non-convex OptimizationSubmitted to the editors 11/26/2025.") which ensure the existence of an optimal solution for every admissible parameter, the parameter sets and initial point sets are non-empty, and the SCP update rules are well-posed, are satisfied.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Baselines", "weight": 1.0} -->

To the best of our knowledge, no general baseline methods exist to generate worst-case guarantees for these SCP algorithms. For validation, in all experiments we report the *sample maximum*, obtained by uniformly sampling $500$ parameter instances from the set $\mathcal{X}$ (unless stated otherwise) and taking the worst-case value. We formulate the convex QPs in CVXPY Diamond and Boyd; Agrawal et al. and solve them using OSQP Stellato et al..

<!-- chunk {"id": "body-0088", "role": "body", "section": "Trust-region method", "weight": 1.0} -->

In this subsection, we apply our verification framework to the trust-region method from Subsection 3.1, on box-constrained quadratic minimization in Subsection 5.1.1 and network utility maximization in Subsection 5.1.2.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Box-constrained quadratic minimization", "weight": 1.0} -->

We first consider the non-convex box-constrained quadratic optimization problem

<!-- chunk {"id": "body-0090", "role": "body", "section": "Box-constrained quadratic minimization", "weight": 1.0} -->

where $z \in \text{R}^{n}$ is the decision variable, $x \in \text{R}^{n}$ is the problem parameter, and the matrix $P \in \text{S}^{n}$ which has both positive and negative eigenvalues is shared across all problem instances.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We take $P = {\overline{P} + {\overline{P}}^{T}}$, where the entries of $\overline{P}$ are generated by sampling from a standard Gaussian distribution in an i.i.d. fashion. In this example, we compare against two different sets for the parameters: $\mathcal{X}_{1} = {\lbrack 2,4\rbrack}^{n}$ and $\mathcal{X}_{2} = {\lbrack 5,8\rbrack}^{n}$. We fix the trust-region size to be $\rho = 0.2$ and solve the verification problem with a cold start $S = {\{\mathbf{0}_{n}\}}$ and with a warm start $S = {\{ s^{ws}\}}$.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Numerical example", "weight": 1.0} -->

To calculate the warm start point $s^{ws}$, we solve the non-convex problem \\tagform@16 with $x$ fixed to the point at the center of the parameter set (e.g., for $\mathcal{X}_{2}$, we fix $x = {{(6.5)}\mathbf{1}_{n}}$). Assumption 4.6. ‣ 4.3 Verifying suboptimality ‣ 4 Verification framework ‣ Verification of Sequential Convex Programming for Parametric Non-convex OptimizationSubmitted to the editors 11/26/2025.") is satisfied since the initial point is always feasible and the SCP steps preserve feasibility. We take $n = 10$ in this example. We use only $10$ samples to compute the sample maximum, as using more samples causes the curves to overlap and become difficult to distinguish.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Results", "weight": 1.0} -->

We illustrate our results in Figure 1. In parameter set $\mathcal{X}_{1}$, the cold-started initialization is certifiably optimal, while the warm-started initialization is not; in parameter set $\mathcal{X}_{2}$, the reverse holds. This shows that guarantees are highly dependent on both the initialization and the parameter set.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Results", "weight": 1.0} -->

verified performance: warm-started sample maximum: warm-started
verified performance: cold-started sample maximum: cold-started

<!-- chunk {"id": "body-0095", "role": "body", "section": "Network utility maximization", "weight": 1.0} -->

We now turn to the resource allocation setting, modeled as a network utility maximization problem Mattingley and Boyd. We model a communication network comprising $d$ edges and $n$ flows. Each edge $i$ has capacity $d_{i}$, and each flow $j$ carries a non-negative rate $z_{j}$. The routing structure is encoded in a binary matrix $R \in {\{ 0,1\}}^{d \times n}$, where $R_{ij} = 1$ indicates that flow $j$ passes through edge $i$. The total load on edge $i$ is then given by the sum of the rates of all flows that traverse it, compactly expressed as $Rz$ which must satisfy the parametric capacity constraints ${Rz} \leq x$. We consider a variant with quadratic objective Fazel and Chiang; Guisewite and Pardalos

<!-- chunk {"id": "body-0096", "role": "body", "section": "Network utility maximization", "weight": 1.0} -->

where $z \in \text{R}^{n}$ is the decision variable, $x \in \text{R}^{d}$ is the problem parameter, and $R \in {\{ 0,1\}}^{d \times n}$, $D \in \text{S}_{+}^{n}$, and $d \in \text{R}^{n}$ are problem data fixed for all instances. Problem \\tagform@17 is non-convex since the objective function being maximized is convex.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We set the cost problem data to be $d = \mathbf{0}_{n}$ and $D = I_{n}$. We generate the routing matrix $R$ as in Ranjan and Stellato, where we select $1$ with $0$ for each entry i.i.d. with probability $0.5$. We let $\mathcal{X} = {\lbrack 7,8\rbrack}^{d}$. We use a cold start (initialized from a random point in ${\lbrack 0,1\rbrack}^{d}$)^33^3We cold start from a random point instead of the zero vector because the trust-region method gets stuck at the zero vector. This cold start is feasible for all problems with parameter $x \in \mathcal{X}$ which means that Assumption 4.6. ‣ 4.3 Verifying suboptimality ‣ 4 Verification framework ‣ Verification of Sequential Convex Programming for Parametric Non-convex OptimizationSubmitted to the editors 11/26/2025.") is met.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We take $d = 10$ and $n = 5$ as in Ranjan and Stellato.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Results", "weight": 1.0} -->

The results are illustrated in Figure 2, where we test different trust-region size values $\rho$. Our framework reveals that among the tested sizes $\{ 1,2,5\}$, the largest trust-region size $5$ provides the strongest worst-case guarantees. For all three cases, the worst-case guarantee plateaus within $5$ iterations.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Penalized convex-concave procedure", "weight": 1.0} -->

In this subsection, we apply our verification framework to the penalized CCP from Subsection 3.2, focusing on power converter control in Subsection 5.2.1 and the knapsack problem in Subsection 5.2.2.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Power converter control", "weight": 1.0} -->

We consider the following optimal control problem for power electronic converters, following a similar setup from Takapoui et al.:

<!-- chunk {"id": "body-0102", "role": "body", "section": "Power converter control", "weight": 1.0} -->

where the decision variable $u$ is the stacked controls over the time indices. The matrices $P \in \text{S}^{Tn_{u}}$ and $K \in \text{R}^{{Tn_{u}} \times n_{s}}$ and the vector $c_{0} \in \text{R}^{Tn_{u}}$ are derived from the problem data. At the end of the penalized CCP, we round the solution to the nearest vector in the discrete set ${\{{- 1},1\}}^{Tn_{u}}$ to obtain a feasible point, thus satisfying Assumption 4.6. ‣ 4.3 Verifying suboptimality ‣ 4 Verification framework ‣ Verification of Sequential Convex Programming for Parametric Non-convex OptimizationSubmitted to the editors 11/26/2025.") (see Subsection 4.2.2 for how to encode this step as constraints).

<!-- chunk {"id": "body-0103", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We generate the dynamics matrices $A$ and $B$ by discretizing the continuous dynamics as described. We have $n_{s} = 4$ and $n_{u} = 1$. We set $Q_{t}$ to be the all zeroes matrix except for the bottom right entry which is $1$. We set $R_{t} = 0$ and $s_{t}^{ref} = {}$ for $t = {0,\ldots,T}$. We discretize with ${\Deltat} = 10^{- 6}$ seconds and take $T = 10$ time steps. We set $\mathcal{X} = {\lbrack{- 2},2\rbrack}^{n_{s}}$ and use the hyperparameter $\tau_{k} = 0.2$ for the penalties in problem \\tagform@5. We compare the two different inexactness criteria for terminating the penalized CCP from Subsection 4.6 for different tolerances.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We use the same warm-start initialization heuristic as described in Subsection 5.1.1.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Results", "weight": 1.0} -->

We illustrate our guarantees in Figure 3. We observe a sizeable gap between the verified worst-case performance and the sample maximum for the KKT inexactness criteria, indicating that the verification framework finds particularly adversarial inexact solutions that do not naturally arise from the OSQP solver.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Knapsack", "weight": 1.0} -->

We now consider the knapsack problem formulated as

<!-- chunk {"id": "body-0107", "role": "body", "section": "Knapsack", "weight": 1.0} -->

where $z \in \text{R}^{n}$ is the decision variable, $x \in \text{R}^{n}$ is the problem parameter, and $a \in \text{R}_{+ +}^{n}$ and $b \in \text{R}_{+ +}$ are problem data that are fixed for all problem instances. The goal is to select a subset of items (given by binary variables $z$) that maximizes the total value $x^{T}z$ while ensuring the total occupied space $a^{T}z$ does not exceed capacity $b$.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We set $n = 10$, randomly sample the vector $a$ from a uniform distribution in $\lbrack 0,1\rbrack$ in an i.i.d. fashion, and set $b$ to be half the sum of the entries of $a$. We set the penalty hyperparameters with $\tau_{k} = {\tau_{0}\kappa^{k}}$ and test across $\tau_{0} \in {\{ 0.01,1,100\}}$ and $\kappa \in {\{ 1,2\}}$. We initialize from the vector ${(0.5)}\mathbf{1}_{n}$ (the middle of the set ${\{ 0,1\}}^{n}$) and take the parameter set $\mathcal{X} = {\lbrack 5,7\rbrack}^{n}$.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Results", "weight": 1.0} -->

We showcase our bounds on the level of constraint violation in Figure 4. Across all choices of hyperparameters $\tau_{0}$ and $\kappa$, the penalized CCP fails to make any progress beyond the first iteration, and no feasible solution can be verified in any case.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Prox-linear method", "weight": 1.0} -->

In this subsection, we apply our verification framework to the prox-linear method from Subsection 3.3 for phase retrieval in Subsection 5.3.1.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Phase retrieval", "weight": 1.0} -->

We consider the phase retrieval problem

<!-- chunk {"id": "body-0112", "role": "body", "section": "Phase retrieval", "weight": 1.0} -->

where $z \in \text{R}^{n}$ is the decision variable, $x \in \text{R}^{d}$ is the problem parameter, and the dictionary vectors ${\{ a_{i}\}}_{i = 1}^{d}$ (where $a_{i} \in \text{R}^{n}$) are fixed across all instances. Phase retrieval seeks to reconstruct a signal $z$ from quadratic measurements, which arises in applications such as optics, imaging, and crystallography Drusvyatskiy.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We consider a small phase retrieval problem where $d = 15$ and $n = 5$. We use hyperparameter $\rho = 1$ and compare against two different parameter sets: $\mathcal{X}_{1} = {\lbrack 6,7\rbrack}^{d}$ and $\mathcal{X}_{2} = {\lbrack 6.5,7\rbrack}^{d}$. We generate the entries of the $a_{i}$ vectors i.i.d. from a standard Gaussian distribution with probability $0.25$ and otherwise set it to $0$. We use the same warm-start initialization heuristic as described in Subsection 5.1.1. Since problem \\tagform@21 is unconstrained, Assumption 4.6. ‣ 4.3 Verifying suboptimality ‣ 4 Verification framework ‣ Verification of Sequential Convex Programming for Parametric Non-convex OptimizationSubmitted to the editors 11/26/2025.") is met.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Results", "weight": 1.0} -->

The results for this example are illustrated in Figure 5. For the smaller parameter set, we can obtain significantly stronger worst-case guarantees.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Results", "weight": 1.0} -->

verified performance: set 𝒳1 sample maximum: set 𝒳1
verified performance: set 𝒳2 sample maximum: set 𝒳2
Figure 5: Phase retrieval results. With the smaller parameter set 𝒳2, we can certify global optimality (up to tolerance 0.001) after 4 iterations. The worst-case guarantee for the larger parameter set 𝒳1 is significantly worse. For K = 4 and 𝒳2, Gurobi fails to reach a 2% optimality gap within the 2 hour time limit, so we report the best upper bound obtained.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Relax-round-polish", "weight": 1.0} -->

In this subsection, we apply our framework to verify the relax-round-polish method from Subsection 3.4 on sparse coding in Subsection 5.4.1 and hybrid vehicle control in Subsection 5.4.2.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Sparse coding", "weight": 1.0} -->

We consider the cardinality-constrained version of a sparse coding problem

<!-- chunk {"id": "body-0118", "role": "body", "section": "Sparse coding", "weight": 1.0} -->

where $z \in \text{R}^{n}$ is the decision variable, $x \in \text{R}^{d}$ is the problem parameter, and $A \in \text{R}^{d \times n}$ is problem data that is fixed for all instances. In the relax-round-polish method, recall that our relax step consists in solving the lasso problem ${{\min_{z}{({1/2})}}{\|{{Az} - x}\|}_{2}^{2}} + {\lambda{\| z\|}_{1}}$ with hyperparameter $\lambda$. The subsequent round step retains only the $k$ largest entries of $z$ in magnitude, setting all others to zero. Finally, the polish step fixes this support and solves a least-squares problem over the selected variables. We use our verification framework to upper bound the suboptimality.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We follow a similar setup from Ranjan et al. to generate a random $A$ matrix. With probability $0.2$, we sample the entries of $A \in \text{R}^{d \times n}$ i.i.d. from a standard normal distribution and otherwise set each entry to $0$. We then normalize the columns to have unit norm. We take the set $\mathcal{X} = {\lbrack 5,8\rbrack}^{d}$ and use $d = 20$, $n = 15$, and $k = 5$. We then solve the verification problem for a range of $\lambda$ values spaced evenly on a log-scale between $0.01$ and $100$.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Results", "weight": 1.0} -->

verified performance sample maximum
Figure 6: Sparse coding results. Among the set of hyperparameter options, λ = 3.16 yields the lowest worst-case suboptimality. We observe a sizeable gap between the verified bound and the sample maximum, which we attribute to the method’s combinatorial structure. By selecting an adversarial parameter, the verification procedure can (i) induce ties in the relaxation that make multiple rounding outcomes equally valid, and (ii) break those ties in the most adverse way to maximize suboptimality. In contrast, the sampling procedure breaks such ties at random, leading to milder observed outcomes.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Hybrid vehicle control", "weight": 1.0} -->

We study a hybrid vehicle control problem that captures the task of meeting a power demand while managing battery energy, limiting engine switching, and enforcing operational constraints. Formally, we consider

<!-- chunk {"id": "body-0122", "role": "body", "section": "Results", "weight": 1.0} -->

feasibility certificate found infeasibility certificate found
time limit reached, but feasibility verified from other verification problems
Figure 7: Hybrid vehicle results. Left: Δ E = 0.0. Middle: Δ E = 0.5. Right: Δ E = 1.0. As we go from i) right-to-left across the three plots, ii) right-to-left within any plot, or iii) down-to-up within any plot, the size of the parameter set 𝒳 strictly decreases, so it is strictly easier to find the feasibility certificate. We use this fact to verify feasibility in cases, where the time limit is reached.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduce a verification framework to certify the worst-case performance of sequential convex programming methods for parametric non-convex optimization. The verification problem is formulated as an optimization problem that maximizes a performance metric over a given parameter set subject to constraints representing the SCP steps. Our framework is general and applies to many SCP algorithms and extends naturally to inexact subproblem solves. Applications in control, signal processing, and operations research demonstrate that the framework provides worst-case guarantees in settings where they are otherwise unavailable.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Conclusion", "weight": 1.5} -->

There are several interesting directions for future work. First, it would be interesting to extend our framework to handle semidefinite program relaxations of non-convex optimization problems and low-rank rounding schemes (as done in Goemans and Williamson ). Second, adapting the framework to analyze randomized rounding schemes would enable certification of algorithms that incorporate stochastic elements. Third, improving the scalability of the approach remains an important challenge, for example through more efficient numerical implementations or problem-specific simplifications.
