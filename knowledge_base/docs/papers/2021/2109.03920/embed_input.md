<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Inverse Optimization: Theory and Applications

Topics include Optimization, Mathematical optimization.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Inverse optimization describes a process that is the "reverse" of traditional mathematical optimization. Unlike traditional optimization, which seeks to compute optimal decisions given an objective and constraints, inverse optimization takes decisions as input and determines an objective and/or constraints that render these decisions approximately or exactly optimal. In recent years, there has been an explosion of interest in the mathematics and applications of inverse optimization. This paper provides a comprehensive review of both the methodological and application-oriented literature in inverse optimization.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In traditional mathematical optimization, one takes as input an objective and a set of constraints to generate an optimal decision. In inverse optimization, decisions are given as input and an objective and/or constraints is the output. Specifically, the goal of inverse optimization is to determine parameters of an optimization model the forward modelthat render a set of decisions approximately or exactly optimal with respect to this forward model. Solving for this set of parameters is itself an optimization model, known as the inversemodel.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent years, there has been an explosion of interest in the mathematics and applications of inverse optimization. For example, it has found diverse applications in areas such as transportation, healthcare, and power systems, where we can use an observed data set of decisions to estimate a decision-making model that best reproduces these observations. Decision data can include individual routing choices, electricity consumption patterns or medical treatments, and the inverse optimization model can be used to estimate route-choice preferences, utility functions or clinical treatment objectives that are most consistent with the observed decisions. In these examples, inverse optimization provides a mathematical framework for estimating latent parameters and subjective preferences within decision-making problems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The tractability of an inverse optimization problem depends on the complexity of the forward model and the desired properties sought in the inverse model. Different applications require different modeling assumptions, leading to many different inverse models and corresponding solution methods. Nonetheless, all models can broadly be characterized as a combination of elements along the following three major dimensions (see Figure

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

- Forward problem structure:This dimension describes the structure of the forward model. Possibilities include linear, conic, convex, or discrete optimization models. Sequential decision-making models (e.g., Markov decision processes) are also possible. - Parameter type:The parameters to be estimated may reside in the objective, constraints, or both. The structure and tractability of the inverse optimization problem depend heavily on which parameters are estimated and the forward problem structure. Depending on the application, it may be necessary to achieve a perfect fitbetween the estimated parameters of the forward model and the decisions, i.e., finding parameters such that the decisions are optimal. In problems where this is unnecessary or impossible, the inverse problem may instead aim to maximize a suitable measure of fitness.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since the treatment of the first two dimensions is relatively similar across the third dimension, we specifically assign the labels of Classical Inverse Optimization and Data-Driven Inverse Optimizationto distinguish between the models that assume perfect model-data fit and those that do not. Classical problems, which dominate the early literature on inverse optimization, are often used to introduce new reformulation techniques of the inverse problem. As we will discuss in later sections, the models are also relevant in applications where it is necessary to find parameters in the forward model that render the decisions optimal. On the other hand, data-driven models draw upon the techniques and methods employed in classical models but also consider an additional layer of complexity arising from the possibility of imperfect model-data fit. Such models are relevant when there is model mis-specification or noisy observations in the decision data. This literature is distinguished by loss functions that correspond to various sub-optimality measures.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

every picture/.style=line width=0.75pt confidence=None created_by=None text='\\begin{tikzpicture}[font=\\sffamily]\n%uncomment if require: \\path; %set diagram left start at 0, and has height of 300\n\n \\node(FPS) [process, minimum width=3cm] {Forward Problem \\\\ Structure};\n %\\node(FPSprob) [noBox, below of = FPS, yshift=-0.5cm] {Linear \\\\ Convex \\\\ Integer \\\\ Sequential};\n \\node(FPSprob) [noBox, below of = FPS, yshift=-0.5cm] {\\\\[2em] Linear \\\\ Convex \\\\ Integer \\\\ Sequential};\n \n \\node(PT) [process, right of = FPS, xshift=3.5cm, minimum width=3cm] {Parameter \\\\ Type};\n

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

%\\node(PTprob) [noBox, below of = PT, yshift=-0.5cm] {\\\\[0.6em] Objective \\\\[0.2em] Constraints \\\\ ~};\n \\node(PTprob) [noBox, below of = PT, yshift=-0.5cm] {\\\\[2.2em] Objective \\\\[0.2em] Constraints \\\\[1.2em] ~};\n \n \\node(Ass) [process, right of = PT, xshift=3.5cm, minimum width=3cm] {Model-Data \\\\ Fit};\n %\\node(Assprob) [noBox, below of = Ass, yshift=-0.5cm] {Perfect \\\\ Imperfect \\\\ ~ \\\\ ~};\n %\\node(Assprob) [noBox, below of = Ass, yshift=-0.5cm]

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

{\\\\[0.6em] Perfect \\\\[0.2em] Imperfect \\\\ ~ };\n \\node(Assprob) [noBox, below of = Ass, yshift=-0.5cm] {\\\\[2.2em] Perfect \\\\[0.2em] Imperfect \\\\[1.2em] ~ };\n \n \\node [dashedBorder, fit=(FPS)(FPSprob)] (FPSborder) {};\n \\node [dashedBorder, fit=(PT)(PTprob)] (PTborder) {};\n \\node [dashedBorder, fit=(Ass)(Assprob)] (Assborder) {};\n \n \n \\draw[arrow, double, ->] (FPSborder) to (PTborder);\n \\draw[arrow, double, ->] (PTborder) to (Assborder);\n \n \\node[box, minimum

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

width=3cm, text width=3cm, right of = Assprob, xshift=3cm, yshift=0.7cm] (CIO) {Classical IO};\n \\node[box, minimum width=3cm, text width=3cm, right of = Assprob, xshift=3cm, yshift=-0.7cm] (DDIO) {Data-driven IO};\n \n \\draw[arrow, double, out=20, in=180] (Assprob) to (CIO);\n \\draw[arrow, double, out=-20, in=180] (Assprob) to (DDIO);\n\n\n %\\node(FO) [process, text width=4.1cm] {Forward model and $\\bTheta$};\n \n %\\node(Ass) [process, below of = FO, yshift=-1cm, text width=5.5cm] {Is Assumption~\ass:observed_decision_optimal satisfiable?};\n

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

\n \n %\\node(CIO) [process, below of = Ass, xshift=-4.5cm, yshift=-1.5cm, text width=4.5cm] {Classical Inverse \\\\ Optimization (Section~\sec:classic_IO)};\n %\\node(DDIO) [process, below of = Ass, xshift=4.5cm, yshift=-1.5cm, text width=4.5cm] {Data-driven Inverse \\\\ Optimization (Section~\sec:data-driven_IO)};\n \n \n %\\node(prior) [noBox, below of = CIO, yshift=-0.35cm, text width=4.8cm, minimum height=0.5cm, align=justify] {Propose prior estimate $\\hat\\btheta$};\n %\\node(formcio) [noBox, below of = prior, yshift=-0.5cm, text width=4.8cm, minimum height=0.5cm,

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

align=justify] {Solve inverse problem by reformulating $\\Xopt(\\btheta)$ using the structure of the forward model};\n \n \n %\\node(loss) [noBox, below of = DDIO, yshift=-0.35cm, text width=4.8cm, minimum height=0.5cm, align=justify] {Propose loss $\\ell(\\bhx, \\Xopt(\\btheta))$};\n %\\node(formddio) [noBox, below of = loss, yshift=-0.5cm, text width=4.8cm, minimum height=0.5cm, align=justify] {Solve inverse problem by additionally considering the empirical risk of the loss};\n \n \n %\\draw[arrow, double] (FO) to (Ass);\n %\\draw[arrow, double, out=180, in=90] (Ass) to (CIO);\n %\\draw[arrow, double, out=0, in=90]

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

(Ass) to (DDIO);\n \n %\\draw[arrow] (CIO) to (prior);\n %\\draw[arrow] (prior) to (formcio);\n \n %\\draw[arrow] (DDIO) to (loss);\n %\\draw[arrow] (loss) to (formddio);\n \n \n %\\node[draw, dashed, thick, rounded corners, fit=(CIO)(prior)(formcio)] {};\n \n %\\node[draw, dashed, thick, rounded corners, fit=(DDIO)(loss)(formddio)] {};\n\n\n\\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> A taxonomy of inverse optimization models.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

The arrows correspond to the sequence of steps used to build an inverse model. Specifically, a forward model is proposed, a subset of parameters are identified, and the properties that the parameters must satisfy are selected.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we provide (i) a systematic framework for describing and categorizing inverse optimization models, and (ii) a comprehensive review of both methodological and application-oriented literature. We first review different techniques, solution methods, and model properties of all existing inverse models using the above taxonomy. We then consolidate the extensive list of application areas in which inverse optimization is increasingly applied. To our knowledge, there is only one prior survey on inverse optimization [heuberger2004inverse]. That paper provides a theoretical review of select classical inverse models over particular 0-1 combinatorial forward problems, which was the focus of much early research in inverse optimization. Since then, we have observed a breadth of new models, methods, and applications, many specific to the data-driven literature. Our review thus covers techniques applicable to broad classes of problem structures, considers new developments specific to data-driven models, and examines the extensive list of modern applications.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, we briefly remark that inverse optimization falls under the umbrella of inverse problems, in which observational data on the effects of a process are used to estimate unobservable causes generating outcomes[tarantola2005inverse, kaipio2006statistical]. Inverse optimization is distinguished from other inverse problems by the fact that the process is a decision-making problem modeled via mathematical programming, while the data consists of solutions to these problems; thus, the methods and applications of inverse optimization differ from the broader literature.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Fundamentals of Inverse Optimization: A Road Map of This Paper", "weight": 1.0} -->

Inverse optimization modeling begins by defining a parametric forward optimization model that represents the decision-generating process of one or more agents. Then, given a set of target or observed decisions, the inverse optimization model determines parameters of this forward model that render the decisions approximately or exactly optimal. Figure[fig:io\_pipeline]illustrates these relationships.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Fundamentals of Inverse Optimization: A Road Map of This Paper", "weight": 1.0} -->

confidence=None created_by=None text='\\begin{tikzpicture}[font=\\sffamily]\n \\node[cloud, cloud puffs=15.7, cloud ignores aspect, minimum width=4cm, minimum height=2cm, align=center, draw] (fwd) at {Decision-generating \\\\ process(es)};\n\n \\draw (-3,0) node[anchor=east, minimum width=2cm, text width=1cm, align=center] (agentIn) {Agent(s)};\n \\draw [arrow] (agentIn) -- (fwd);\n %\\draw [arrow] (fwd) -- (agentOut);\n \n \\draw (-3,-3.5) node[anchor=east, text width=2cm, align=center] (modelOut) {Estimated \\\\ parameters};\n \\draw (0,-3.5) node[box, minimum width=4cm, text width=4cm, minimum

<!-- chunk {"id": "body-0020", "role": "body", "section": "Fundamentals of Inverse Optimization: A Road Map of This Paper", "weight": 1.0} -->

height=1.25cm] (inv) {Inverse optimization \\\\ model};\n %\\draw (0,-2.2) node[minimum width=4cm, align=center, text width=6cm] (fwdmodel) {Parametric forward model(s)};\n \\draw (0,-2) node[minimum width=4cm, align=center, text width=6cm] (fwdmodel) {Parametric forward model};\n\n %\\draw node[anchor=west, text width=2cm, align=center] (agentOut) {Decisions};\n %\\draw (3,-3.5) node[anchor=west, text width=2cm, align=center] (obsIn) {Observed decisions};\n \\draw (3,-2) node[anchor=west, text width=2cm, align=center] (obsIn) {Decisions};\n\n \\draw [arrow, dashed] (fwd) -- (fwdmodel);\n \\draw [arrow]

<!-- chunk {"id": "body-0021", "role": "body", "section": "Fundamentals of Inverse Optimization: A Road Map of This Paper", "weight": 1.0} -->

(fwdmodel) -- (inv);\n \\draw [arrow] (inv) -- (modelOut);\n\n %\\draw [arrow] (agentOut) -- (obsIn);\n %\\draw [arrow] (obsIn) -- (inv);\n \\draw [arrow] (obsIn) |- (inv);\n \\draw [arrow] (fwd) -| (obsIn);\n\n\\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> In an inverse optimization problem, agents generate decisions that the inverse optimizer observes. The inverse optimizer proposes a forward model of agent behavior and estimates the parameters under which the forward model best supports the decisions.

<!-- chunk {"id": "body-0022", "role": "body", "section": "The forward problem", "weight": 1.0} -->

Mathematically, let the forward optimization model be \prob{FOP}(\btheta):= \min_{\bx} \;\left\{ f(\bx, \btheta) \;|\; \bx \in \set{X}(\btheta) \right\}.

<!-- chunk {"id": "body-0023", "role": "body", "section": "The forward problem", "weight": 1.0} -->

This model is characterized by a parameter $\btheta$ from a parameter class $\bTheta$ that controls the objective $f(\bx, \btheta)$, feasible set $\set{X}(\btheta)$, or both. The objective $f(\bx, \btheta)$ is typically assumed to be a convex and differentiable parametric function in both $\bx$ and $\btheta$. Unless otherwise stated, we assume that $\bTheta$ is a polyhedron. For problems where $\btheta$ parameterizes only the objective function, i.e.,

<!-- chunk {"id": "body-0024", "role": "body", "section": "The forward problem", "weight": 1.0} -->

The feasible set is assumed to have the form $\set{X}(\btheta):= \{ \bx \in \field{R}^q \times \field{Z}^{n-q} \;|\; \bg(\bx, \btheta) \leq \bzero \}$, where $q \in \{0, 1, \ldots, n\}$ and $\bg(\bx, \btheta) = (g_1(\bx, \btheta), \cdots, g_m(\bx, \btheta))$ is composed of $m$ convex functions.

<!-- chunk {"id": "body-0025", "role": "body", "section": "The forward problem", "weight": 1.0} -->

Finally, let \set{X}^{\mathrm{opt}}(\btheta):= \argmin_{\bx} \;\left\{ f(\bx, \btheta) \;|\; \bx \in \set{X}(\btheta) \right\}, denote the optimal solution set, the set of points in $\mX(\btheta)$ that are optimal under $\btheta$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "The inverse problem", "weight": 1.0} -->

Consider a data set $\{\bhx_i\}_{i=1}^N$ of $N \geq 1$ decisions. These decisions may arrive from different versions of the forward model $\prob{FOP}_i(\btheta):= \min \{ f_i(\bx, \btheta) \;|\; \bx \in \set{X}_i(\btheta) \}$, for example via an agent who solves the same decision-generating process several times under different conditions. We also index the corresponding optimal sets $\set{X}^{\mathrm{opt}}_i(\btheta)$. Given this data set, inverse optimization estimates a parameter vector $\btheta^*$ such that the aggregate fit of the corresponding forward models $\prob{FOP}_i(\btheta^*)$ to $\bhx_i$ is optimized.

<!-- chunk {"id": "body-0027", "role": "body", "section": "The inverse problem", "weight": 1.0} -->

An estimate $\btheta^*$ is considered a perfect fit for $\bhx_i$ if $\bhx_i \in \set{X}^{\mathrm{opt}}_i(\btheta^*)$. We formally define the set of perfect fit estimates as the inverse-feasible set \boldsymbol{\Theta}^{\mathrm{inv}}_i(\bhx_i):= \left\{ \btheta \;\Big|\; \bhx_i \in \set{X}^{\mathrm{opt}}_i(\btheta) \right\}.

<!-- chunk {"id": "body-0028", "role": "body", "section": "The inverse problem", "weight": 1.0} -->

Given an input decision $\bhx \in \mathbb{R}^n$, inverse optimization estimates a parameter value $\btheta^*$ such that the corresponding forward optimization model $\prob{FOP}(\btheta^*)$ best fits $\hat\bx$. An estimate $\btheta^*$ is considered a perfect fit" for $\bhx$ if $\bhx \in \set{X}^{\mathrm{opt}}(\btheta^*)$. Such parameters are formally defined to belong to the inverse-feasible set \boldsymbol{\Theta}^{\mathrm{inv}}(\bhx):= \left\{ \btheta \;\Big|\; \bhx \in \set{X}^{\mathrm{opt}}(\btheta) \right\}.

<!-- chunk {"id": "body-0029", "role": "body", "section": "The inverse problem", "weight": 1.0} -->

More generally, we consider a data set $\{\bhx_i\}_{i=1}^N$ of $N \geq 1$ decisions. Note that these decisions may arrive from different versions of a forward model. For example, an agent may solve the same decision-generating process several times but under slightly different conditions, leading to a set of different instances of the forward optimization model, optimal solution set, and inverse-feasible set.

<!-- chunk {"id": "body-0030", "role": "body", "section": "The inverse problem", "weight": 1.0} -->

& A fundamental question in the design of an inverse optimization problem is whether inverse-feasibility must be strictly enforced. This leads to what we call the classical versus data-driven formulations (see Figure [fig:summary\_of\_io\_methods]).

<!-- chunk {"id": "body-0031", "role": "body", "section": "The inverse problem", "weight": 1.0} -->

confidence=None created_by=None text='\\begin{tikzpicture}[font=\\sffamily]\n \n \\node(FO) [process, text width=4.1cm] {Forward model and $\\bTheta$};\n \n \\node(Ass) [process, below of = FO, yshift=-0.5cm, text width=6.8cm] {Must inverse-feasibility be satisfied?}; \n \n %\\node(Ass) [process, below of = FO, yshift=-1cm, text width=5.5cm] {Must inverse-feasibility be satisfied?}; \n \n \n \\node(CIO) [process, below of = Ass, xshift=-4.5cm, yshift=-1.1cm, text width=7cm] {Classical Inverse Optimization \\\\ (Section~\sec:classic_IO)};\n \\node(DDIO) [process, below of = Ass, xshift=4.5cm,

<!-- chunk {"id": "body-0032", "role": "body", "section": "The inverse problem", "weight": 1.0} -->

yshift=-1.1cm, text width=7cm] {Data-driven Inverse Optimization \\\\ (Section~\sec:data-driven_IO)};\n \n \n \\node(prior) [noBox, below of = CIO, yshift=-0.35cm, text width=5.3cm, minimum height=0.5cm] {Add constraints $\\bhx_i \\in \\Xopt_i(\\btheta)$};\n \\node(formcio) [noBox, below of = prior, yshift=-0.35cm, text width=7.1cm, minimum height=0.5cm] {Solve inverse problem by reformulating $\\Xopt_i(\\btheta)$ using the forward model structure};\n \n \n \\node(loss) [noBox, below of = DDIO, yshift=-0.35cm, text width=5.3cm, minimum height=0.5cm, align=justify] {Add loss functions

<!-- chunk {"id": "body-0033", "role": "body", "section": "The inverse problem", "weight": 1.0} -->

$\\ell(\\bhx_i, \\Xopt_i(\\btheta))$};\n \\node(formddio) [noBox, below of = loss, yshift=-0.35cm, text width=7.1cm, minimum height=0.5cm] {Solve inverse problem by additionally considering the empirical risk of the loss};\n %\\node(formddio) [noBox, below of = loss, yshift=-0.5cm, text width=5cm, minimum height=0.5cm, align=justify] {Solve inverse problem by additionally considering the empirical risk of the loss};\n \n \n \\draw[arrow, double] (FO) to (Ass);\n \\draw[arrow, double, out=180, in=90] (Ass) to (CIO) node[above left, yshift=0.7cm] {Yes};\n \\draw[arrow, double, out=0, in=90] (Ass) to (DDIO) node[above right,

<!-- chunk {"id": "body-0034", "role": "body", "section": "The inverse problem", "weight": 1.0} -->

yshift=0.7cm] {No};\n %\\draw[conceptarrow, double] (LPFO) to [out=120, in=60] node[above] {\\footnotesize duality vs KKT} (CPFO);\n \n \\draw[arrow] (CIO) to (prior);\n \\draw[arrow] (prior) to (formcio);\n \n \\draw[arrow] (DDIO) to (loss);\n \\draw[arrow] (loss) to (formddio);\n \n \n \\node[dashedBorder, fit=(CIO)(prior)(formcio)] {};\n \\node[dashedBorder, fit=(DDIO)(loss)(formddio)] {};\n \n \\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> Classical and data-driven inverse optimization methods are differentiated by whether inverse feasibility must be satisfied.

<!-- chunk {"id": "body-0035", "role": "body", "section": "The inverse problem", "weight": 1.0} -->

From there, classical and data-driven techniques follow their respective steps.

<!-- chunk {"id": "body-0036", "role": "body", "section": "The inverse problem", "weight": 1.0} -->

Classical inverse optimization (Sectionsec:classic\_IO). These inverse optimization problems solve for a parameter $\btheta \in \bTheta$ that is inverse-feasible and minimizes an application-specific objective $h(\btheta)$:%\prob{IOP}\text{--}\prob{C}(\bhx):= \min_{\btheta} \;\left\{ h(\btheta) \;\Big|\; \btheta \in \boldsymbol{\Theta}^{\mathrm{inv}}_i(\bhx_i) \; \forall i \in \{1, \ldots, N\},\; \btheta \in \bTheta \right\}.

<!-- chunk {"id": "body-0037", "role": "body", "section": "The inverse problem", "weight": 1.0} -->

The inverse-feasibility constraints make[eq:classical\_io\_highlevel] a bilevel program. Many techniques have been developed to reformulate it into a single-level form.

<!-- chunk {"id": "body-0038", "role": "body", "section": "The inverse problem", "weight": 1.0} -->

Data-driven inverse optimization (Sectionsec:data-driven\_IO). Instead of enforcing inverse-feasibility, loss functions $\ell(\bx_i, \set{X}^{\mathrm{opt}}_i(\btheta))$ are used to penalize the extent to which inverse-feasibility is violated:%\prob{IOP}\text{--}\prob{DD}\left(\{(\bhx_i, \set{X}^{\mathrm{opt}}_i(\btheta))\}_{i=1}^N \right):= \min_{\btheta} \;\bigg\{ \kappa h(\btheta) + \frac{1}{N} \sum_{i=1}^N \ell\left(\bhx_i, \set{X}^{\mathrm{opt}}_i(\btheta) \right) \; \Big| \; \btheta \in \bTheta \bigg\}.

<!-- chunk {"id": "body-0039", "role": "body", "section": "The inverse problem", "weight": 1.0} -->

Here, $\kappa \geq 0$ describes a trade-off between an application-specific objective $h(\btheta)$ and the loss.

<!-- chunk {"id": "body-0040", "role": "body", "section": "The inverse problem", "weight": 1.0} -->

Alternative learning paradigms (Sectionsec:related\_model\_paradigms).The above problems become computationally challenging with large forward models or data sets, necessitating other approaches that permit fast algorithms. We discuss Inverse Online Learning (IOL), which considers input data sequentially, and Inverse Reinforcement Learning (IRL), which addresses large sequential decision-making models.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Choosing an inverse model", "weight": 1.0} -->

The choice of which inverse optimization model to use depends on the application. Most applications in the literature can be described as either Design applications (Section sec:classic\_IO\_apps). Inverse optimization can be used to design prices, incentives, or mechanisms $\btheta \in \bTheta$ to induce particular agent decisions $\{\bhx_i\}_{i = 1}^N$ by making them optimal under the computed parameters. These problems assume that the agents' decision-generating processes are known and focus on classical inverse optimization techniques.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Choosing an inverse model", "weight": 1.0} -->

Estimation applications (Section sec:modern\_applications). These problems learn a decision-making model using decision inputs representing observed agent behavior. Here, data-driven inverse optimization models can generate parameter estimates $\btheta \in \bTheta$ even if it is infeasible to render all observed decisions $\{\bhx_i\}_{i = 1}^N$ optimal. This property is important in applications with large decision data sets obtained from noisy measurements, inconsistent behavior, or unobserved contextual factors.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Classical Inverse Optimization", "weight": 1.0} -->

In this section, we overview reformulation techniques for the inverse-feasibility constraint in Problem [eq:classical\_io\_highlevel]. We present different techniques for linear, conic, discrete, and sequential forward optimization models that each reformulate the corresponding inverse model into a tractable optimization problem. We also present variations where the input is only given in a partial form.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Classical Inverse Optimization", "weight": 1.0} -->

Although the reformulation techniques presented in this section can be used to solve any instance of Problem [eq:classical\_io\_highlevel], we consider the most common objective function found in the literature, i.e., $h(\btheta) = \| \btheta - \hat\btheta \|_p$, where $\bhtheta$ is a fixed value, interpreted as an a priori belief or estimate: \prob{IOP}\text{--}\prob{C}(\bhx, \bhtheta):= \min_{\btheta} \;\left\{ \norm{\btheta - \bhtheta}_p \;\bigg|\; \btheta \in \boldsymbol{\Theta}^{\mathrm{inv}}(\bhx), \; \btheta \in \bTheta \right\}.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Classical Inverse Optimization", "weight": 1.0} -->

For ease of exposition, we also assume a single decision input ($N=1$).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Classical Inverse Optimization", "weight": 1.0} -->

The earliest paradigms in classical inverse optimization used the following characterization of the inverse-feasible set (see [heuberger2004inverse] for a review): \boldsymbol{\Theta}^{\mathrm{inv}}(\bhx) = \left\{ \btheta \;|\; f(\bhx, \btheta) \leq f(\bx, \btheta), \; \forall \bx \in \set{X}(\btheta) \right\}.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Classical Inverse Optimization", "weight": 1.0} -->

For $\bhx$ to be optimal, it must have an objective value that is at least as good as any other feasible solution. However,[eq:xinv\_fundamental] requires enumerating every feasible solution. Consequently, early literature focuses on integer and network flow forward models where this enumeration can be finite. For example,[burton1992instance, burton1994use] use[eq:xinv\_fundamental] to estimate arc costs in shortest path forward models,[zhang1996inverse] explore spanning tree models, and[guler2010capacity] estimate the capacity constraints of minimum cost flow models. Since enumerating all feasible solutions is impractical in general, alternative and tractable characterizations of $\boldsymbol{\Theta}^{\mathrm{inv}}(\bhx)$ were developed.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Linear models", "weight": 1.0} -->

Linear models are among the most well-studied in inverse optimization, with efficient techniques to estimate both objectives and constraints. Consider the Linear Forward Model \prob{FOP}\text{--}\prob{L}((\btheta, \bPhi, \bpsi)):= \min \{ \btheta^\tpose \bx \;|\; \bPhi \bx \geq \bpsi \} where $\btheta \in \field{R}^n$, $\bPhi \in \field{R}^{m \times n }$, and $\bpsi \in \field{R}^m$ are the objective vector, constraint matrix, and right-hand-side constraint vector, respectively. The inverse optimization literature for linear forward models generally considers the estimation of either the objective or the constraint parameters independently, i.e.,

<!-- chunk {"id": "body-0049", "role": "body", "section": "Linear models", "weight": 1.0} -->

- Estimating the objective: Let $\bPhi = \bA$ and $\bpsi = \bb$ where $\bA \in \field{R}^{m \times n}$ and $\bb \in \field{R}^m$ are known constraint parameters, and estimate an objective vector $\btheta$ of a minimum distance from $\bhtheta$. - Estimating the constraints: Let $\btheta = \bc$ where $\bc \in \field{R}^n$ is a known objective vector and estimate $(\bPhi, \bpsi)$ of minimum distance from $(\hat\bPhi, \hat\bpsi)$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Linear models", "weight": 1.0} -->

Note that this generalizes special cases of estimating only the constraint matrix (i.e., $\bTheta:= \{ (\bPhi, \bpsi) \;|\; \bpsi = \bb \}$) or estimating the only the right-hand-side vector (i.e, $\bTheta:= \{ (\bPhi, \bpsi) \;|\; \bPhi = \bA \}$).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Linear models", "weight": 1.0} -->

When estimating only objective parameters, we assume $\bhx$ is feasible for the given constraint parameters, i.e., that $\bA \bhx \geq \bb$. When it is obvious from context, we simplify the notation of $\prob{FOP}\text{--}\prob{L}((\btheta, \bPhi, \bpsi))$ to omit known parameters (e.g., let $\prob{FOP}\text{--}\prob{L}(\btheta):= \min \{ \btheta^\tpose \bx \;|\; \bA \bx \geq \bb \}$).

<!-- chunk {"id": "body-0052", "role": "body", "section": "Estimating the objective", "weight": 1.0} -->

[ahuja2001inverse] propose one of the earliest inverse optimization frameworks for estimating the objective of general bounded linear forward models $\prob{FOP}\text{--}\prob{L}(\bhtheta)$. They show that the inverse optimization problem of a linear program can itself be a linear program by characterizing $\boldsymbol{\Theta}^{\mathrm{inv}}(\bhx)$ using the complementary slackness conditions in linear programming. Equivalently, strong duality conditions can also be used [chan2018inverse, shahmoradi2021quantile, ghobadi2021inferring].

<!-- chunk {"id": "body-0053", "role": "body", "section": "Estimating the objective", "weight": 1.0} -->

If $\bhx$ is an optimal solution for $\prob{FOP}\text{--}\prob{L}(\btheta)$, then there exists a dual vector $\blambda$ that satisfies (i) dual feasibility $\bA^\tpose \blambda = \btheta, \; \blambda \geq \bzero$ and (ii) complementary slackness $(\bA \bhx - \bb)^\tpose \blambda = 0$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Estimating the objective", "weight": 1.0} -->

From Property [prop:comp\_slack], the inverse-feasible set of $\prob{FOP}\text{--}\prob{L}(\btheta)$ has a convenient linear representation $\boldsymbol{\Theta}^{\mathrm{inv}}(\bhx) = \{ \btheta \;|\; \exists \blambda \geq \bzero: \bA^\tpose \blambda = \btheta \ \; (\bA \bhx - \bb)^\tpose \blambda = 0 \}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Estimating the objective", "weight": 1.0} -->

The inverse optimization problem then becomes \min_{\btheta, \blambda} \quad & \norm{\btheta - \bhtheta}_p \\\st \quad & \bA^\tpose \blambda = \btheta \\& \left(\bA \bhx - \bb \right)^\tpose \blambda = 0 \\& \btheta \in \bTheta, \quad \blambda \geq \bzero.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Estimating the objective", "weight": 1.0} -->

If $p=1$ or $p=\infty$, then problem[eq:ahuja\_ilo]becomes a linear program.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Estimating the objective", "weight": 1.0} -->

We next highlight the strong duality approach, which leads to an equivalent formulation.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Estimating the objective", "weight": 1.0} -->

If $\bhx$ is an optimal solution for $\prob{FOP}\text{--}\prob{L}(\btheta)$, then there exists a dual vector $\blambda$ that satisfies (i) dual feasibility $\bA^\tpose \blambda = \btheta, \; \blambda \geq \bzero$ and (ii) strong duality $\btheta^\tpose \bhx = \blambda^\tpose \bb$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Estimating the objective", "weight": 1.0} -->

Property [prop:strong\_duality] implies that we can replace the constraint $\left(\bA \bhx - \bb \right)^\tpose \blambda = 0$ in Problem [eq:ahuja\_ilo] with $\btheta^\tpose \bhx = \blambda^\tpose \bb$ via the following transformation \left(\bA \bhx - \bb \right)^\tpose \blambda = \blambda^\tpose \bA \bhx - \bb^\tpose \blambda = \btheta^\tpose \bhx - \bb^\tpose \blambda.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Estimating the objective", "weight": 1.0} -->

This observation underscores that there are often multiple equivalent formulations of an inverse problem for the same forward model, based on the choice of optimality condition that is used to develop the inverse problem. For many classical inverse problems, where inverse-feasibility is a constraint, these alternatives may often be considered equivalent. On the other hand, the specific choice of optimality condition can motivate different loss functions and lead to different model formulations in data-driven inverse optimization, as will be discussed in Section [sec:data-driven\_IO].

<!-- chunk {"id": "body-0061", "role": "body", "section": "Estimating the objective", "weight": 1.0} -->

As an extension, it has been shown that the inverse problem of an infinite-dimensional linear forward model is an infinite-dimensional convex program. [ghate2015inverse] study linear forward problems with a countably infinite number of variables and constraints, where under a sufficiency condition for strong duality, they construct $\boldsymbol{\Theta}^{\mathrm{inv}}(\bhx)$ as an infinite number of dual feasibility constraints and propose a convergent solution algorithm for the resulting infinite-dimensional inverse problem. [nourollahi2019inverse] extend these results to minimum cost flow problems on infinite dimensional networks and [ghate2020inverse]considers semi-infinite linear forward models that feature a finite dimensional decision vector but an uncountably infinite constraint set.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Estimating constraint parameters", "weight": 1.0} -->

[chan2020inverse] consider $\prob{FOP}\text{--}\prob{L}(\bPhi)$ where the right-hand-side constraint vector $\bpsi = \bb$ is known and only $\bPhi$ must be estimated. Given an observed $\bhx$, the inverse-feasible set is \boldsymbol{\Theta}^{\mathrm{inv}}(\bhx) = \{ \bPhi \;|\; \exists \blambda \geq \bzero: \bPhi^\tpose \blambda = \bc, \; \bc^\tpose \bhx = \blambda^\tpose \bb \}.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Estimating constraint parameters", "weight": 1.0} -->

Although $\boldsymbol{\Theta}^{\mathrm{inv}}(\bhx)$ contains bilinear constraints $\bPhi^\tpose \blambda = \bc$,[chan2020inverse] propose a solution method by observing that for $\bhx$ to be optimal, it must satisfy at least one constraint with equality. Specifically, an optimal solution of the inverse problem can be obtained by perturbing the nearest facet $\{ \bx \;|\; \hat{\bphi}_j^\tpose \bx \geq b_j \}$ from $\bhx$ until the corresponding constraint is satisfied. [ghobadi2021inferring] consider the general problem of estimating both $\bPhi$ and $\bpsi$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Estimating constraint parameters", "weight": 1.0} -->

Here, the inverse-feasible set $\boldsymbol{\Theta}^{\mathrm{inv}}(\bhx) = \{ (\bPhi, \bpsi) \;|\; \exists \blambda \geq \bzero: \bPhi^\tpose \blambda = \bc, \; \bc^\tpose \bhx = \blambda^\tpose \bpsi \}$ is now bilinear in two constraints. They derive a simple convex formulation of the inverse optimization problem by noting that the optimality of $\bhx$ means that $\bc^\tpose \bx \geq \bc^\tpose \bhx$ is an implicit constraint.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Estimating constraint parameters", "weight": 1.0} -->

Since for a linear optimization problem, all optimal solutions must lie on at least one of the facets of the feasible set, they select the implicit constraint as the supporting facet and reduce the inverse problem to estimating parameters $(\bPhi, \bpsi)$ such that the observed decision $\bhx$ is feasible: \min_{\bPhi, \bpsi} \quad & \norm{ \left(\bPhi, \bpsi) - (\hat\bPhi, \hat\bpsi\right) }_p \\\st \quad & \bPhi^\tpose \bhx \geq \bpsi \\& \left(\bPhi, \bpsi\right) \in \bTheta.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Estimating constraint parameters", "weight": 1.0} -->

The above approaches are also useful in robust optimization. For instance,[chan2020inverse] estimate parameters in an uncertainty set for robust linear optimization models of the form \min_{\bx} \max_{\bA \in \set{U}(\btheta)} \left\{ \bc^\tpose \bx \;\Big|\; \bA \bx \geq \bb \right\}, where the uncertainty set depends on the parameter to be estimated. Since robust linear optimization problems with polyhedral uncertainty sets can be reformulated into single-level linear optimization problems of the structure in $\prob{FOP}\text{--}\prob{L}(\bPhi)$ with the uncertainty set parameters in the constraints of the linear program, the above approaches apply.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Jointly estimating objective and constraint parameters", "weight": 1.0} -->

In some special cases, it is possible to jointly estimate parameters from both the objective and constraints. Consider the forward model $\prob{FOP}\text{--}\prob{L}((\btheta, \bpsi))$ where the constraint matrix $\bPhi = \bA$ is given, but the objective vector and right-hand-side vector need to be estimated. To solve this problem, we can leverage the complementary slackness formulation[eq:ahuja\_ilo]. Note here that if $\bb$ in problem[eq:ahuja\_ilo] is a decision variable (now denoted as $\bpsi$), the complementary slackness equation becomes bilinear, which can be reformulated into linear constraints using an additional set of auxiliary binary variables $\bz$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Jointly estimating objective and constraint parameters", "weight": 1.0} -->

This implies that the inverse optimization problem can be solved as the mixed integer linear program \min_{\btheta, \blambda, \bpsi, \bz} \quad & \norm{ \left(\btheta, \bpsi\right) - \left(\hat\btheta, \hat\bpsi\right) }_p \\\st \quad\; & \bA \bhx - \bpsi \geq \bzero \\& \bA\bhx - \bpsi \leq M\bz \\& \blambda \leq M(\mathbf{1}-\bz) \\& \bA^\top \blambda = \btheta \\& (\btheta, \bpsi) \in \bTheta, \quad \blambda \geq \bzero, \quad \bz \in \{0,1\}^m where $M > 0$is a sufficiently large constant.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Conic and convex models", "weight": 1.0} -->

$m \geq 2$, let $\set{C} \subset \field{R}^m$ be a proper cone, meaning it is convex and closed, it has a non-empty interior, and $\{\bx, -\bx\} \in \set{C} \Rightarrow \bx = \bzero$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Conic and convex models", "weight": 1.0} -->

Consider the Conic Forward Model \prob{FOP}\text{--}\prob{CON}(\btheta):= \min_{\bx} \; \left\{ f(\bx, \btheta) \;|\; -\bg(\bx, \btheta) \in \set{C} \right\} where $f(\bx, \btheta)$ is a convex function in $\bx$ and $\bg(\bx, \btheta) = \big(g_1(\bx, \btheta), \dots, g_m(\bx, \btheta) \big)$ is a vector-valued function whose elements are each differentiable and convex.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Conic and convex models", "weight": 1.0} -->

Note that setting $\set{C} = \field{R}^m_+$ reduces the forward model to a classical convex optimization problem, where the constraint $-\bg(\bx, \btheta) \in \mC$ in model [eq:fop\_conic] can be equivalently written as $\bg(\bx, \btheta) \leq \mathbf{0}$. [iyengar2005inverse] derive a tractable reformulation of $\prob{IOP}\text{--}\prob{C}(\bhx, \bhtheta)$ using the Karush-Kuhn-Tucker (KKT) conditions.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Conic and convex models", "weight": 1.0} -->

A decision $\bhx$ is optimal for $\prob{FOP}\text{--}\prob{CON}(\btheta)$ if (i) there exists $\bx \in \set{C}$ for which $-\bg(\bx, \btheta) \in \interior(\set{C})$, and (ii) there exists $\blambda \in \set{C}$ for which \nabla_{\bx} f(\bhx, \btheta) + \sum_{j=1}^m \lambda_j \nabla_{\bx} g_j(\bhx, \btheta) = 0 & \textrm{ and } \lambda_j g_j(\bhx, \btheta) = 0, \quad \forall j \in \{1, \dots, m\}.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Conic and convex models", "weight": 1.0} -->

Let the inverse-feasible set $\boldsymbol{\Theta}^{\mathrm{inv}}(\bhx)$ be the set of $\btheta$ that satisfy the KKT conditions above. For a general $\prob{FOP}\text{--}\prob{CON}(\btheta)$, this set features bilinear equations in $\lambda_j$ and $g_j(\bhx, \btheta)$, meaning that the general inverse problem is not easily solvable. However, in the case where $\btheta$ lies only in the objective, the corresponding inverse problem is a conic program.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Conic and convex models", "weight": 1.0} -->

Furthermore if $\nabla_{\bx} f(\bhx, \btheta)$ is an affine function of $\btheta$, then the above problem is convex. $\prob{FOP}\text{--}\prob{CON}(\btheta)$ can incur very efficient algorithms. For example,[zhang2010augmented] consider quadratic forward optimization models where $f(\bx, \btheta) = \bx^\tpose \bPhi \bx + \bpsi^\tpose \bx$ for $\bTheta = \{ (\bPhi, \bpsi) \;|\; \bPhi \in \field{S}^{n \times n}, \; \bpsi \in \set{R}^n \}$. Using Lemma[lem:iyengar\_inverse\_conic], the inverse conic problem is a semi-definite program (SDP).

<!-- chunk {"id": "body-0075", "role": "body", "section": "Conic and convex models", "weight": 1.0} -->

Here,[zhang2010augmented] propose a more efficient algorithm by first writing the dual of this program as a semi-smooth, differentiable convex program that can be solved by a Newton method. Further,[zhang2010inverse] consider convex forward models with separable basis objective functions $f(\bx,\btheta) = \sum_{b=1}^B \theta_b f^{(b)}(\bx)$and known linear equality constraints. In this case, the inverse problem is a linear program.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Markov decision processes", "weight": 1.0} -->

[erkin2010eliciting] use inverse optimization to estimate the reward function in a finite-state finite-action Markov decision process (MDP). Consider an MDP defined by the tuple $(\set{S}, \set{A}, p, \btheta, \gamma)$, where $s \in \set{S}$ and $a \in \set{A}$ are states and actions in their respective sets, $p(s'|a, s) \in $ is the state transition probability for any state-action pair, $\btheta: \set{S} \times \set{A} \to \field{R}$ is a reward function, and $\gamma \in $ is a discount factor. In a finite-state finite-action MDP, we can characterize the reward function as a matrix $\btheta \in \field{R}^{|\set{S}| \times |\set{A}|}$ for which $\theta_{s, a}$ denotes the reward for a state-action pair.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Markov decision processes", "weight": 1.0} -->

A (forward) MDP determines an optimal value function $\bv^*$ using the Bellman equations v_s = \max_{a \in \set{A}} \left\{ \theta_{s, a} + \gamma \sum_{s' \in \set{S}} p(s'|a, s) v_{s'} \right\}, \quad \forall s \in \set{S}.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Markov decision processes", "weight": 1.0} -->

In an inverse MDP, rather than observing $\hat{\bv}$, we observe a policy $\hat\bpi: \set{S} \rightarrow \set{A}$ where $\hat\bpi(s) \in \argmax_{a \in \set{A}} \{ \theta_{s, a} + \gamma \sum_{s' \in \set{S}} p(s'|a, s) v_{s'} \}$. Since an optimal policy can be derived by solving the dual of the above linear program[puterman1990markov], it also satisfies complementary slackness.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Markov decision processes", "weight": 1.0} -->

[Complementary Slackness for MDPs] The policy $\bhpi$ is optimal for $\prob{FOP}\text{--}\prob{MDP}(\btheta)$ if and only if \bhpi(s) = a' \; \Longrightarrow \; v_s = \theta_{s, a'} + \gamma \sum_{s' \in \set{S}} p(s'|a', s) v_{s'}, \quad \forall s \in \set{S}.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Markov decision processes", "weight": 1.0} -->

$\prob{FOP}\text{--}\prob{MDP}(\btheta)$ is an infinite-dimensional linear program and we can use infinite-dimensional inverse linear optimization[ghate2015inverse, ghate2020inverse].

<!-- chunk {"id": "body-0081", "role": "body", "section": "Markov decision processes", "weight": 1.0} -->

Large scale MDPs are often solved with approximate dynamic programming (ADP) or reinforcement learning. Inverse methods for ADP forward models remain an unexplored research area. The inverse reinforcement learning literature has developed in parallel with inverse optimization with limited cross-pollination[abbeel2004apprenticeship].

<!-- chunk {"id": "body-0082", "role": "body", "section": "Discrete models", "weight": 1.0} -->

We next consider forward models that are mixed integer linear programs (MILPs), which do not possess optimality certificates that can be conveniently represented in a small number of equations (e.g., the KKT conditions). Consider the Mixed Integer Forward Model \prob{FOP}\text{--}\prob{MI}(\btheta):= \max_{\bx} \left\{ \btheta^\tpose \bx \;\Big|\; \bA \bx \leq \bb, \; \bx \in \field{R}^{n-q} \times \field{Z}^{q} \right\}.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Discrete models", "weight": 1.0} -->

Note that we use a maximization problem to remain consistent with the original literature. Inverse optimization methods for $\prob{FOP}\text{--}\prob{MI}(\btheta)$ either use certificates of strong duality for integer programming, analogous to inverse linear optimization techniqueshere, it leads to inverse problems with an exponential number of variables and constraintsor use cutting plane algorithms.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Duality via sub-additive functions", "weight": 1.0} -->

[schaefer2009inverse] generalizes the previous strong duality approach to inverse integer linear optimization where $q=n$ in $\prob{FOP}\text{--}\prob{MI}(\btheta)$. [lamperski2015polyhedral] further explore MILPs where $q < n$. We highlight the strictly integer case below.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Duality via sub-additive functions", "weight": 1.0} -->

While the dual vector of a linear program is a non-negative vector, the dual variable of an integer program $\prob{FOP}\text{--}\prob{MI}(\btheta)$ is a non-decreasing and super-additive function $F:\field{Z}^m \rightarrow \field{R}$[lasserre2009linear]. An optimal dual function must be dual feasible and achieve the primal optimal value. [Strong Duality for MIPs] Let $\bA_i\in \field{R}^n$ be the $i$-th column of $\bA$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Duality via sub-additive functions", "weight": 1.0} -->

Then, $\bhx$ is optimal for $\prob{FOP}\text{--}\prob{MI}(\btheta)$ if there exists a non-decreasing super-additive function $F: \field{R}^m \rightarrow \field{R}$ where F(\bzero) = 0, \quad F(\bb) = \btheta^\tpose \bhx, \quad F(\bA_i) \leq \theta_i \qquad \forall i \in \{1, \dots, n\}.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Duality via sub-additive functions", "weight": 1.0} -->

To characterize the inverse-feasible set, we represent the dual function as a vector whose elements represent the function output for points in $\field{Z}^m$, similar to describing policy functions in MDPs. Although $\field{Z}^m$ is infinite,[schaefer2009inverse] shows that we only need to consider a sufficiently large finite subset $\set{B} \subset \field{Z}^m$ as the domain of the dual function.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Duality via sub-additive functions", "weight": 1.0} -->

Given $\set{B}$, the inverse-feasible set is \boldsymbol{\Theta}^{\mathrm{inv}}(\bhx) = \left\{ \btheta \;\bBigg@{4}|\; \exists F \in \field{R}^{|\set{B}|} \geq \bzero \,: \, \begin{array}{l} \displaystyle \text{Constraints eq:duality_mips} \\ %eq:duality_mips1--eq:duality_mips3} \\F(\bbeta) \leq F(\bbeta'), \quad \forall \bbeta \leq \bbeta' \in \set{B} \\F(\bbeta) + F(\bbeta') \leq F(\bbeta + \bbeta'), \quad \forall \bbeta, \bbeta' \in \set{B} where the last two sets of inequalities enforce super-additivity.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Duality via sub-additive functions", "weight": 1.0} -->

[schaefer2009inverse] then develops sufficient conditions on $\set{B}$ such that this $\boldsymbol{\Theta}^{\mathrm{inv}}(\bhx)$ fully describes inverse-feasibility.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Duality via sub-additive functions", "weight": 1.0} -->

Then, $\prob{IOP}\text{--}\prob{C}(\bhx, \bhtheta)$ is equivalent to the following (exponentially sized) convex optimization problem: \min_{\btheta, F} \quad & \norm{\btheta - \hat\btheta}_p \\\st \quad & F(\bA_i) \geq \theta_i, \quad \forall i \in \{1, \dots, n \} \\& F(\bb) = \btheta^\tpose \bhx, \quad F(\bzero) = 0 \\& F(\bbeta) \leq F(\bbeta'), \quad \forall \bbeta \leq \bbeta' \in \set{B} \\& F(\bbeta) + F(\bbeta') \leq F(\bbeta + \bbeta'), \quad \forall \bbeta, \bbeta' \in \set{B} \\& \btheta

<!-- chunk {"id": "body-0091", "role": "body", "section": "Duality via sub-additive functions", "weight": 1.0} -->

\in \bTheta, \quad F \geq \bzero The inverse problem to a mixed integer forward optimization model is a convex program whose non-linearities depend only on However, this program requires an exponential number of variables $F \in \field{R}^{|\set{B}|}$ and an exponential number of constraints.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Duality via sub-additive functions", "weight": 1.0} -->

If the dimension $n$ of the forward problem is large, then this super-additive duality-based approach is likely to be intractable. One approach is to approximate the class of super-additive functions $F(\bbeta)$. For example,[turner2013examining] use linear and quadratic approximations, often obtaining an optimal solution for small problems.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Cutting plane algorithms", "weight": 1.0} -->

Whereas[eq:xinv\_fundamental] was defined using the entire feasible set, i.e., $\btheta^\tpose \bhx \geq \btheta^\tpose \bx$ for all $\bx \in \set{X}$, with a mixed integer linear forward problem, we only need to consider this optimality condition over the set of extreme points of the forward feasible set [wang2009cutting]. Since this set is finite, the feasible set of Problem[eq:IOprior\_fullMIP]contains a finite but (generally) exponential number of constraints. [wang2009cutting] proposes a cutting plane algorithm that iteratively generates new extreme points and computes $\btheta$ to make $\bhx$ optimal over the growing set of previously generated points.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Cutting plane algorithms", "weight": 1.0} -->

1.2 A cutting plane algorithm for inverse mixed integer linear optimization Input: Forward optimization model $\prob{FOP}\text{--}\prob{MI}(\btheta), \btheta \in \bTheta$; Decision $\bhx$; Prior $\hat\btheta$ Output: Inverse optimization parameter estimate $\btheta^*$ Initialize $\tilde{\set{X}} = \emptyset$; $\tilde\btheta = \hat\btheta$ Solve $\prob{FOP}\text{--}\prob{MI}(\tilde\btheta)$ and let $\tilde\bx$ be an optimal solution $\tilde\btheta^\tpose \tilde\bx < \tilde\btheta^\tpose \bhx$ Update $\tilde{\set{X}} \gets \tilde{\set{X}} \cup \{ \tilde\bx \}$ \min_{\btheta} \left\{

<!-- chunk {"id": "body-0095", "role": "body", "section": "Cutting plane algorithms", "weight": 1.0} -->

\norm{\btheta - \bhtheta}_p \;\Big|\; \btheta^\tpose \bhx \geq \btheta^\tpose \tilde \bx, \; \forall \tilde\bx \in \tilde{\set{X}}, \; \btheta \in \bTheta \right\} and let $\tilde\btheta$ be an optimal solution Solve $\prob{FOP}\text{--}\prob{MI}(\tilde\btheta)$ and let $\tilde\bx$ be an optimal solution $\btheta^* = \tilde\btheta$ Since the feasible set of $\prob{FOP}\text{--}\prob{MI}(\btheta)$ may contain an exponential number of extreme points, each of being computationally demanding to compute, subsequent research focused on accelerating the cutting plane algorithm.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Cutting plane algorithms", "weight": 1.0} -->

[duan2011heuristic] describe a parallel computing approach where different extreme points are simultaneously computed and added. [bodur2022inverse] demonstrate that in many problem classes, generating extreme points or even interior points near $\bhx$ may be sufficient. This observation motivates the development of a trust-region based cutting plane algorithm where smaller, restricted forward problems are solved to generate both better and faster cuts.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Partially constrained inverse problems", "weight": 1.0} -->

Some studies assume that only a lower-dimensional function of a decision vector is given, such as a partial solution or the objective value of a solution.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Inverse optimization with a partial solution", "weight": 1.0} -->

Several papers have examined the problem of estimating model parameters when only a part" of a decision is observed. Examples appear in various network flow problems where we observe flows along only a subset of the arcs. For example, [yang2007partial] consider inverse assignment problems where only a subset of the assignments are identified, while[cai2008partial] explore minimum spanning trees where only a subset of disconnected arcs is given. The input to these inverse problems is no longer a point $\bhx \in \mX$, but rather a set $\hat \mX \subseteq \mX$ where a subset of variables denoted by $\mM$ are fixed to known values: \hat \mX = \left \{\bx \; | \; \bx \in \mX, \; x_i = \hat{x}_i \; \forall i \in \mM \right \}.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Inverse optimization with a partial solution", "weight": 1.0} -->

The Partial Inverse Optimization problem seeks a parameter $\btheta$ such that at least one $\bx \in \hat\mX$ is an optimal solution [zhang2016algorithms, li2018partial, tayyebi2020partial]: \min_{\btheta, \bx} \;\left\{ \norm{\btheta - \hat\btheta}_p \;\Big|\; \bx \in \hat\mX \ \; \btheta \in \boldsymbol{\Theta}^{\mathrm{inv}}(\bx) \ \; \btheta \in \bTheta \right\}.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Inverse optimization with a partial solution", "weight": 1.0} -->

For linear models $\prob{FOP}\text{--}\prob{L}(\btheta)$, problem[eq:partial\_IO] can be written as the following bilinear program using the complementary slackness property \min_{\btheta, \blambda, \bx} \quad & \norm{\btheta - \hat\btheta}_p \\& (\bA \bx - \bb)^\top \blambda = \bzero \\& \blambda^\top \bA = \btheta \\& \btheta \in \bTheta, \quad \bx \in \hat\mX, \quad \blambda \geq \bzero.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Inverse optimization with a partial solution", "weight": 1.0} -->

This model can be reformulated as a mixed integer linear program or solved using decomposition algorithms [hu2012linear]. [wang2013branch] develops a solution method to solve the Partial Inverse Optimization problem for mixed integer linear forward models $\prob{FOP}\text{--}\prob{MI}(\btheta)$. The solution method builds upon the cutting plane approach presented in Section [subsec:integer].

<!-- chunk {"id": "body-0102", "role": "body", "section": "Inverse optimal value", "weight": 1.0} -->

[ahmed2005inverse], [mostafaee2016inverse] and [vcerny2016inverse] consider the Inverse Optimal Value problem. Rather than observing a decision $\bhx$, the input is the objective function value $\hat{z}$. This leads to the problem \min_{\btheta} \left\{ \norm{\btheta - \hat\btheta}_p \;\Big|\; \min_{\bx} \{ \btheta^\tpose \bx \;|\; \bA \bx \geq \bb \} =\hat{z}, \; \btheta \in \bTheta \right\}.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Inverse optimal value", "weight": 1.0} -->

Under a few mild assumptions on the forward model including a bounded feasible region, [ahmed2005inverse] show that the inverse problem can be reformulated into \min_{\btheta, \blambda} \quad & \norm{\btheta - \hat\btheta}_p \\\st \quad & \blambda^\tpose \bb = \hat{z} \\& \bA^\tpose \blambda = \btheta \\& \btheta \in \bTheta, \quad \blambda \geq \bzero.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Inverse optimal value", "weight": 1.0} -->

The literature referenced in the previous paragraph also considers cases where there does not exist a $\btheta \in \bTheta$ such that $\btheta^\top \bhx = \hat{z}$, and methods are proposed to minimize this gap.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Inverse optimal value", "weight": 1.0} -->

confidence=None created_by=None text='\\begin{tikzpicture}[font=\\sffamily]\n \n \\node(LPFO) [process, text width=4.1cm] {Linear Forward Models};\n \n \\node(LPObj) [noBox, below of = LPFO, yshift=-1cm, xshift=-1.6cm, text width=3.0cm] {Estimating objectives \\\\ \n \\footnotesize\};\n \\node(LPCon) [noBox, below of = LPFO, yshift=-1cm, xshift=1.6cm, text width=4.0cm] {Estimating constraints \\\\ \\footnotesize \};\n \n \\node(CPFO) [process, left of = LPFO, xshift=-7cm, text width=4.1cm] {Conic Forward Models};\n \\node(CPFOprop) [noBox, below of = CPFO, text

<!-- chunk {"id": "body-0106", "role": "body", "section": "Inverse optimal value", "weight": 1.0} -->

width=4cm] {\\footnotesize \};\n %\\node(CPFOprop) [noBox, below of = CPFO, yshift=-1cm, text width=4cm] {Estimating differentiable objectives \\\\ \};\n \n \n \\node(IPFO) [process, right of = LPFO, xshift=7cm, text width=3.6cm] {Integer Forward \\\\ Models};\n \n \\node(IPDual) [noBox, below of = IPFO, yshift=-1cm, xshift=-1.8cm, text width=3.5cm] {Duality \\\\ \\footnotesize \ };\n \\node(IPCP) [noBox, below of = IPFO, yshift=-1cm, xshift=1.8cm, text width=3.5cm] {Cutting planes \\\\ \\footnotesize \ };\n \n \n \\node(INFLPFO) [process, below of =

<!-- chunk {"id": "body-0107", "role": "body", "section": "Inverse optimal value", "weight": 1.0} -->

LPObj, text width=4.6cm, yshift=-4cm] {Infinite-dimension \\\\ Linear Forward Models};\n \\node(INFprop) [noBox, below of = INFLPFO, text width=4.2cm] {\\footnotesize \ };\n \n \n \\node(NFFO) [process, above of = LPFO, xshift=5cm, yshift=4cm, text width=3.5cm] {Network Flow \\\\ Forward Models};\n \\node(NFFOcite) [noBox, below of = NFFO, yshift=-0.8cm, text width=7.5cm] {\\footnotesize \ \\\\\n (Surveyed in~\)};\n \n \n \\node(MDPFO) [process, below of = CPFO, yshift=-3.25cm, text width=3.8cm] {MDP Forward \\\\ Models};\n \\node(MDPFOcite)

<!-- chunk {"id": "body-0108", "role": "body", "section": "Inverse optimal value", "weight": 1.0} -->

[noBox, below of = MDPFO] {\\footnotesize \};\n \n \n \\node[dashedBorder, fit=(LPFO)(LPObj)(LPCon)] {};\n \\node[dashedBorder, fit=(IPFO)(IPDual)(IPCP)] {};\n \n \\draw (LPFO) to (LPObj);\n \\draw (LPFO) to (LPCon);\n \\draw (IPFO) to (IPDual);\n \\draw (IPFO) to (IPCP);\n \n \\draw[conceptarrow, double] (LPFO) to [out=120, in=60] node[above] {\\footnotesize KKT vs duality} (CPFO);\n \\draw[arrow, double] (LPObj) to [out=-60, in=240] node[below] {\\footnotesize via superadditive functions} (IPDual);\n \\draw[arrow, double]

<!-- chunk {"id": "body-0109", "role": "body", "section": "Inverse optimal value", "weight": 1.0} -->

(LPObj) to node[left, text width=2cm, text centered, align=center, xshift=0.05cm] {\\footnotesize via semi-infinite duality} (INFLPFO);\n \\draw[arrow, double] (NFFO) to [out=190, in=90] node[left, align=right, text centered, text width=2.8cm, yshift=0.5cm, xshift=0.75cm] {\\footnotesize LP optimality certificates} (LPFO);\n \\draw[conceptarrow, double] (NFFO) to [out=-10, in=60] node[right, align=left, text width=2.8cm, text centered] {\\footnotesize \eq:xinv_fundamental definition of optimality} (IPCP);\n \n \\draw[conceptarrow, double] (LPObj) to [out=180, in=90] node[left, text width=2.5cm, yshift=-0.6cm,

<!-- chunk {"id": "body-0110", "role": "body", "section": "Inverse optimal value", "weight": 1.0} -->

xshift=2cm, align=center, text centered] {\\footnotesize complementary slackness} (MDPFO);\n \n \\draw[arrow, double] ([yshift=-0.75cm]MDPFO.south) to [out=270, in=180] node[left, text width=2.5cm, yshift=-0.15cm, align=center, text centered] {\\footnotesize infinite states/actions} (INFLPFO);\n \n\n %\\node[draw, dashed, thick, fit=(ch3)(thm1)] {};\n %\\node[draw, dashed, thick, fit=(ch4)(lem1)(thm2)] {};\n %\\node[draw, dashed, thick, fit=(ch5)(prop1)] {};\n %\\node[draw, dashed, thick, fit=(ch6)(thm3)] {};\n \n %\\draw[arrow] (thm1)

<!-- chunk {"id": "body-0111", "role": "body", "section": "Inverse optimal value", "weight": 1.0} -->

-- (lem1);\n %\\draw[arrow] (thm1) -- (thm2);\n %\\draw[arrow] (lem1) -- (prop1);\n %\\draw[arrow] (thm2) -- (thm3);\n \n \\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> A roadmap of the main branches of classical inverse optimization. Bold arrows denote extensions and generalizations and dashed arrows denote conceptual similarities.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Summary", "weight": 1.0} -->

In this section, we examine classical inverse models for a variety of forward optimization structures. For each forward problem, we show that the inverse models can be formulated and solved by characterizing the optimality conditions using either forward optimality (i.e., via equation [eq:xinv\_fundamental]) or a form of duality (i.e., complementary slackness, strong duality, KKT, or superadditive duality). Figure[fig:summary\_of\_section3]summarizes these results and highlights the relationship between the forward problem structure and the optimality conditions that are leveraged to solve the inverse problem.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Data-Driven Inverse Optimization", "weight": 1.0} -->

In this section, we survey different loss functions and solution algorithms in data-driven inverse optimization. Most of this literature explores convex forward models whose instances are associated with observed input parameters $\bu \in \set{U}$. For a given input $\bhu_i$, consider the convex forward model \prob{FOP}\text{--}\prob{CVX}_i(\btheta):= \min_{\bx} \left\{ f(\bx, \bhu_i, \btheta) \;|\; \bg(\bx, \bhu_i, \btheta) \leq \bzero \right\}.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Data-Driven Inverse Optimization", "weight": 1.0} -->

We can also define $f_i(\bx, \btheta) \equiv f(\bx, \bu_i, \btheta)$ and $\bg_i(\bx, \btheta) \equiv \bg(\bx, \bu_i, \btheta)$, meaning that introducing $\bu_i$ does not lose any generality. In practice, $\bu_i$ captures observable changes between different instances.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Data-Driven Inverse Optimization", "weight": 1.0} -->

In the data-driven problem, we observe a data set of decisions and optimal solution sets $\set{D}:= \{ (\bhx_i, \set{X}^{\mathrm{opt}}_i(\btheta)) \}_{i=1}^N$, drawn i.i.d.from a probability distribution $(\bx, \set{X}^{\mathrm{opt}}(\btheta)) \sim \field{P}$.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Data-Driven Inverse Optimization", "weight": 1.0} -->

Note that the following statements are equivalent: (i) we observe $\set{D}:= \{ (\bhx_i, \set{X}^{\mathrm{opt}}_i(\btheta)) \}_{i=1}^N$; (ii) we observe a data set of decisions and forward models $\set{D}:= \{ (\bhx_i, \prob{FOP}\text{--}\prob{CVX}_i(\btheta)) \}_{i=1}^N$; (iii) we observe a data set of decisions and forward model inputs $\set{D}:= \{(\bhx_i, \bhu_i) \}_{i=1}^N$. At times, it is advantageous to specifically assume the data is obtained a specific format, so we interchange these statements as necessary.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Data-Driven Inverse Optimization", "weight": 1.0} -->

$\field{P}_N:= \sum_{i=1}^N \delta_{(\bhx_i, \set{X}^{\mathrm{opt}}_i(\btheta))}$ be the empirical distribution corresponding to the data set, let $\ell(\cdot, \cdot)$ be a loss function penalizing the violation of inverse-feasibility, and consider the inverse problem \prob{IOP}\text{--}\prob{DD}(\ell, \field{P}_N):= \min_{\btheta \in \bTheta} \;\; \frac{1}{N} \sum_{i=1}^N \ell\left(\bhx_i, \set{X}^{\mathrm{opt}}_i(\btheta) \right).

<!-- chunk {"id": "body-0118", "role": "body", "section": "Data-Driven Inverse Optimization", "weight": 1.0} -->

This problem is equivalent to Problem[eq:data-driven\_io\_highlevel] introduced in Section[subsec:problem\_def\_inverse], but without the second objective term $h(\btheta)$. While the literature in data-driven inverse optimization typically considers only the inverse-feasibility loss function, the solution algorithms easily adapt when $h(\btheta)$ is introduced. Finally, we note that most of this literature focuses on estimating objective function parameters.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Data-Driven Inverse Optimization", "weight": 1.0} -->

In this literature, we observe $N$ decisions, $\bhx_i$ for $i = 1, \dots, N$, which come from $N$ forward models $\prob{FOP}\text{--}\prob{CVX}_i(\btheta)$.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Data-Driven Inverse Optimization", "weight": 1.0} -->

It is at times advantageous to assume that the data is obtained specifically via one of the above statements, so we interchange the use of these statements in this section as necessary. Finally, we assume that the data set is drawn from i.i.d. samples from a probability distribution $(\bx, \set{X}^{\mathrm{opt}}(\btheta)) \sim \field{P}$ (or analogously $(\bx, \bu) \sim \field{P}$).

<!-- chunk {"id": "body-0121", "role": "body", "section": "Data-Driven Inverse Optimization", "weight": 1.0} -->

Given access to the data generating distribution, we may consider a loss function $\ell(\bx, \set{X}^{\mathrm{opt}}(\btheta))$ and minimize the expected risk \prob{IOP}\text{--}\prob{DD}(\ell, \field{P}):= \min_{\btheta \in \bTheta} \;\; \field{E}_\field{P} \left[\ell\left(\bx, \set{X}^{\mathrm{opt}}(\btheta) \right) \right] Since we do not have access to $\field{P}$, let $\field{P}_N = \sum_{i=1}^N \delta_{\bhx_i, \set{X}^{\mathrm{opt}}_i(\btheta)}$ be the empirical distribution corresponding to our data set and consider the Data-Driven Inverse Optimization Problem minimizing the empirical risk

<!-- chunk {"id": "body-0122", "role": "body", "section": "Data-Driven Inverse Optimization", "weight": 1.0} -->

The goal of most data-driven inverse optimization methods is to balance two, sometimes competing, priorities: proposing efficient solution algorithms to $\prob{IOP}\text{--}\prob{DD}(\ell, \field{P}_N)$ versus ensuring that data-driven inverse optimization yields statistically sound estimates of the expected risk.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

An intuitive measure of the error of a forward model with respect to an observed decision $\bhx$ is the distance of $\bhx$ from $\set{X}^{\mathrm{opt}}(\btheta)$. We define the Minimum Distance loss function \ell_{\mathrm{D}}\left(\bhx, \set{X}^{\mathrm{opt}}(\btheta) \right):= \min_{\bx \in \set{X}^{\mathrm{opt}}(\btheta)} \;\; \norm{\bx -\bhx}_2, which measures the $2$-norm distance from the optimal set. The data-driven inverse optimization problem $\prob{IOP}\text{--}\prob{DD}(\ell_{\mathrm{D}}, \field{P}_N)$using the above loss is referred to as the Inverse Distance problem.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

[aswani2018inverse] consider convex forward models $\prob{FOP}\text{--}\prob{CVX}_i(\btheta)$ parametrized by $\bhu_i$ in[eq:fop\_cvx\_u]. They show that for these models, $\prob{IOP}\text{--}\prob{DD}(\ell_\mathrm{D}, \field{P}_N)$ is a statistically consistent estimator of $\btheta$. That is, when the data set consists of i.i.d. samples from $\field{P}$, the empirical risk minimization problem $\prob{IOP}\text{--}\prob{DD}(\ell_\mathrm{D}, \field{P}_N)$converges in probability to the expected risk.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

Consider $\prob{FOP}\text{--}\prob{CVX}_i(\btheta)$ and suppose that

<!-- chunk {"id": "body-0126", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

- The feasible sets of $\prob{FOP}\text{--}\prob{CVX}_i(\btheta)$ are closed, absolutely bounded, and have non-empty interiors for all $\bu \in \set{U}$ and $\btheta \in \bTheta$. - $f_i(\bx, \bu, \btheta)$ and $\bg_i(\bx, \bu, \btheta)$ are continuous in $\bx, \bu, \btheta$, $f(\bx, \bu, \btheta)$ is strictly convex in $\bx$ for fixed $\bu, \btheta$, and $\bg_i(\bx, \bu, \btheta)$ is convex in $\bx$ for fixed $\bu\in\set{U}$ and $\btheta\in\bTheta$. - The set $\bTheta$ is closed, bounded, and convex.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

- The data distribution has finite variance $\field{E}_\field{P} [\bx \bx^\tpose] < \boldsymbol{\infty}_{n\times n}$.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

Theorem[thm:distance\_is\_consistent] states that solving $\prob{IOP}\text{--}\prob{DD}(\ell_{\mathrm{D}}, \field{P}_N)$ yields an estimate $\btheta_N$ that converges to the best estimate $\btheta^*$ that could be obtained with full knowledge of the data distribution $\field{P}$, i.e., the minimizer of $\prob{IOP}\text{--}\prob{DD}(\ell_\mathrm{D}, \field{P})$. This property is known as Risk Consistency.[aswani2018inverse] also prove a stronger consistency result, Parameter Consistency, where $\btheta_N \overset{p}{\to} \btheta^*$; this property requires additional identifiability assumptions such as a strictly convex forward objective function.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

$\prob{IOP}\text{--}\prob{DD}(\ell_{\mathrm{D}}, \field{P}_N)$ is an NP-hard problem for general convex forward models, certain cases permit convex approximations by reformulating $\set{X}^{\mathrm{opt}}(\btheta)$ via KKT conditions (see Section[sec:classical\_IO\_convex]) or strong duality[aswani2018inverse, chan2018inverse, chan2018multiple]. [Strong Duality for Convex Optimization] Assume that $\prob{FOP}\text{--}\prob{CVX}_i(\btheta)$ has a non-empty interior.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

Let $h_i(\blambda, \btheta)$ denote the Lagrangian dual function h_i(\blambda, \btheta):= \inf_{\bx} \left\{ f_i(\bx, \btheta) + \blambda^\tpose \bg_{i} (\bx, \btheta) \;\Big|\; \bg_i(\bx, \btheta) \leq \bzero \right\}.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

Then, $\bx \in \set{X}^{\mathrm{opt}}_i(\btheta)$ if and only if there exists $\blambda \geq \bzero$ for which $f_i(\bx, \btheta) = h_i(\blambda, \btheta)$.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

confidence=None created_by=None text='\\begin{tikzpicture}[font=\\sffamily]\n \n \\draw[step=1cm,gray!10,very thin] (-0.7,1.3) grid (5.7,5.7);\n \\draw[ultra thick] -- -- -- --;\n \\draw[fill=black] (5.5, 4) circle (0.05) node[above right] {$\\bhx$};\n \\draw[fill=black] circle (0.05) node[above] {$\\bx_1$};\n \\draw[fill=black] circle (0.05) node[above] {$\\bx_2$};\n \n %\\draw [thick, ->, color=red] (3, 2.5) -- node[right]{$\\btheta_1$} (3, 3.5);\n \\draw [thick, ->,

<!-- chunk {"id": "body-0133", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

The forward model $\prob{FOP}\text{--}\prob{L}(\btheta)$ is a linear program and $\bhx$ is an infeasible point. For $\btheta_1$, the nearest optimal solution to $\bhx$ is $\bx_1$. However, an infinitesimal rotation of the estimated cost vector to the left in $\btheta_2$ forces the nearest solution to be $\bx_2$.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

For most forward models, $\ell_\mathrm{D}(\bx, \set{X}^{\mathrm{opt}}(\btheta))$ is discontinuous in $\btheta$. Figure[fig:decision\_space\_is\_discontinuous] highlights an example.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

\geq \bzero, \quad \forall i \in \{1, \dots, N\} \\Rather than strictly enforcing primal feasibility and strong duality, problem[eq:inverse\_risk\_minimization\_epsilon] permits these two constraints to be slightly violated.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

The resulting program is convex in $\btheta$ for fixed $\bx_i, \blambda_i$, and in $\bx_i, \blambda_i$ for fixed $\btheta$. Further,[aswani2018inverse] develop an enumeration solution algorithm that solves for $\btheta$ and $\bx_i, \blambda_i$ separately. While this approach works for any convex forward model, the authors also show that for strictly convex forward models, there exists an efficient decomposition algorithm that parametrizes $\bx_i$with Nadaraya-Watson Kernel Regression using the observed decisions.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

Enumerative algorithm for $\prob{IOP}\text{--}\prob{DD}(\ell_\mathrm{D}, \set{D})$ when $f(\bx, \btheta)$ is not strictly continuous Input: Forward model $\prob{FOP}(\btheta), \btheta \in \bTheta$; Data set $\{(\bhx_i, \prob{FOP}_i(\btheta))\}_{i=1}^N$; Resolution $\delta > 0$ Output: Inverse optimization parameter estimate $\btheta^*$ Initialize $\delta$-net $\set{N}(\delta) \subset \bTheta$ that satisfies $\max_{\btheta \in \bTheta} \min_{\bhtheta \in \set{N}(\delta)} \| \btheta - \bhtheta \| \leq \delta$ $\bhtheta \in

<!-- chunk {"id": "body-0138", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

\set{N}(\delta)$ Compute $L_{\mathrm{D}, \epsilon}(\bhtheta):= $ the optimal value for problem[eq:inverse\_risk\_minimization\_epsilon] for fixed $\btheta=\bhtheta$.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

$\btheta^* \gets \argmin_{\bhtheta \in \set{N}(\delta)} L_{\mathrm{D}, \epsilon}(\bhtheta)$ We present the special case of the enumeration algorithm for $\prob{FOP}\text{--}\prob{L}(\btheta)$ where we can rewrite $h(\blambda)$ using strong duality.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

\in \{1, \dots, N\} \\Analogous to[eq:inverse\_risk\_minimization\_epsilon], the relaxed version of problem[eq:inverse\_risk\_minimization\_lp] replaces constraints[eq:inverse\_risk\_minimization\_lp3] and[eq:inverse\_risk\_minimization\_lp4] with $\btheta^\tpose \bx_i \leq \bb_i^\tpose \blambda_i + \epsilon$ and $\bA_i \bx_i \geq \bb_i - \epsilon \bone$, respectively.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

In the enumeration algorithm, we discretize $\bTheta$ by a $\delta$-net, i.e., a finite set $\set{N}(\delta) \subset \bTheta$ that satisfies $\max_{\btheta \in \bTheta} \min_{\bhtheta \in \set{N}(\delta)} \|\btheta - \bhtheta\| \leq \delta$. We then enumerate over $\hat\btheta \in \set{N}(\delta)$, solve the problem for each $\hat\btheta$, and select the best parameter.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

[chan2018inverse] and[chan2018multiple] explore a special case of $\prob{IOP}\text{--}\prob{DD}(\ell_{\mathrm{D}}, \field{P}_N)$ where all of the points in $\field{P}_N$ correspond to solutions for the same instance of the forward model, i.e., $\prob{FOP}\text{--}\prob{L}_i(\btheta) = \prob{FOP}\text{--}\prob{L}(\btheta)$ for all $i$. This enforces a single dual variable, i.e., $\blambda_i = \blambda$ for all $i$.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

Here, the dual feasibility constraint[eq:inverse\_risk\_minimization\_lp1] implies that the cost parameter lies in the row space of the constraint matrix $\btheta = \bA^\tpose \blambda$ where $\blambda \in \field{R}^m_+$. Assuming that $\bTheta$ is sufficiently large but excludes $\bzero$ (i.e., preventing trivial solutions), there must exist a $\blambda^*$ in the extreme rays of $\field{R}^m_+$ for which the corresponding $\btheta^*$ is optimal. This means that there exists $j$ where $\btheta^*$ is equal to $\ba_j$ multiplied by a normalization factor. Furthermore,[chan2018inverse] show that when $N=1$, the inverse optimization problem has a closed-form solution.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

In this special case of the forward model, the number of enumerations reduces from $|\set{N}(\delta)|$ (which depends on the size of $\bTheta$) to $m$. [chan2018inverse] and[chan2018multiple] explore a special case of $\prob{IOP}\text{--}\prob{DD}(\ell_{\mathrm{D}}, \field{P}_N)$ where all of the points in $\field{P}_N$ correspond to solutions for the same instance of the forward model, i.e., $\prob{FOP}\text{--}\prob{L}_i(\btheta) = \prob{FOP}\text{--}\prob{L}(\btheta)$ for all $i$. This enforces a single dual variable, i.e., $\blambda_i = \blambda$ for all $i$.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

Here,[chan2018multiple] show that $\prob{IOP}\text{--}\prob{DD}(\ell_\mathrm{D}, \field{P}_N)$ re-formulates to an enumerative search over the rows of $\bA$.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

Proposition[prop:iopd\_lp\_chan\_sol] intuits that since the dual feasibility constraint implies that the cost parameter lies in the row space of the constraint matrix $\btheta = \bA^\tpose \blambda$ where $\blambda \in \field{R}^m_+$, there must exist a $\blambda^*$ in the extreme rays of $\field{R}^m_+$ for which the corresponding $\btheta^*$ is optimal. We can normalize $\blambda^* = \bbe_j/\norm{\ba_j}_d$ to a unit vector. Then $\btheta^* = \ba_j/\norm{\ba_j}_d$. Furthermore,[chan2018inverse] show that when $N=1$, the above optimization problem has a closed-form solution.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

In this special case of the forward model, the number of enumerations reduces from $|\set{N}(\delta)|$ (which depends on the size of $\bTheta$) to $m$.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Distance from the optimal solution set", "weight": 1.0} -->

The geometric property equating optimal parameters to rows of the constraint matrix $\bA$ may lead to instability in estimates[shahmoradi2021quantile, gupta2022decomposition, ahmadi2020inverse]. For example if the rows of $\bA$ correspond to vectors that point in orthogonal directions and the estimated $\btheta$ must lie within this discrete set, then seemingly small variations in the data set may yield large changes in the estimate. Consequently,[gupta2022decomposition] propose restricting the distance minimization loss to only consider vertices of the feasible set. They propose the alternative loss function $\min_{\bx} \{ \norm{\bx -\bhx}_2 \;|\; \bx \in \set{X}^{\mathrm{opt}}(\btheta) \cap \extreme(\{\bx \;|\; \bA \bx \geq \bb \}) \}$and develop a two-phase mixed integer linear programming reformulation for the corresponding inverse problem.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Sub-optimality in the objective function value", "weight": 1.0} -->

Another intuitive and popular loss function to minimize when estimating $\btheta$ is the degree of sub-optimality of the observed decisions $\bhx_i$ under the estimated models $\prob{FOP}_i(\btheta)$. We can evaluate sub-optimality with two potential loss functions.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Sub-optimality in the objective function value", "weight": 1.0} -->

- Absolute Sub-optimality: This loss function measures the difference in the objective function values of the observed decisions with respect to the estimated optimal values, i.e., \ell_\mathrm{ASO}\left(\bhx, \set{X}^{\mathrm{opt}}(\btheta)\right):= \left| f(\bhx, \btheta) - \min_{\bx \in \set{X}(\btheta)} f(\bx, \btheta) \right|.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Sub-optimality in the objective function value", "weight": 1.0} -->

- Relative Sub-optimality: This loss function measures the competitive ratio of the objective function values of the observed decisions with respect to the estimated optimal values, i.e., \ell_\mathrm{RSO}\left(\bhx, \set{X}^{\mathrm{opt}}(\btheta)\right):= \left| \frac{f(\bhx, \btheta)}{\min_{\bx \in \set{X}(\btheta)} f(\bx, \btheta)} - 1 \right|. $\prob{IOP}\text{--}\prob{DD}(\ell_\mathrm{ASO}, \field{P}_N)$ and $\prob{IOP}\text{--}\prob{DD}(\ell_\mathrm{RSO}, \field{P}_N)$ denote the Inverse Absolute Sub-optimality and Inverse Relative Sub-optimality problems, respectively.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Sub-optimality in the objective function value", "weight": 1.0} -->

While these inverse problems do not possess statistical properties, they often lead to tractable optimization problems, especially for linear forward models. Moreover, $\prob{IOP}\text{--}\prob{DD}(\ell_\mathrm{ASO}, \field{P}_N)$ yields generalization bounds (see Section[sec:datadriven\_vi]).

<!-- chunk {"id": "body-0153", "role": "body", "section": "Absolute sub-optimality loss", "weight": 1.0} -->

We first consider a special case where the observed decisions are known to be feasible, i.e., $\bhx_i \in \set{X}_i(\btheta)$ for all $(\bhx_i, \prob{FOP}_i(\btheta)) \in \set{D}$ and $\btheta \in \bTheta$. Here, we can remove the absolute values in the loss function, reformulating the inverse problem to \min_{\btheta, \bx_i} \quad & \frac{1}{N} \sum_{i=1}^N (f_i(\bhx_i, \btheta) - f_i(\bx_i, \btheta)) \\\st \quad & \bx_i \in \set{X}^{\mathrm{opt}}_{i}(\btheta), \quad \forall i \in \{1, \dots, N\} \\This problem can be solved using difference of convex programming techniques.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Absolute sub-optimality loss", "weight": 1.0} -->

For linear forward models, the general (i.e., without assuming feasible observations) Inverse Absolute Sub-optimality problem can be reformulated and efficiently solved using strong duality. [chan2014generalized, chan2018inverse] explore this problem for a single observation.[chan2018multiple] extend these results to multiple observed decisions. We provide a slight generalization of their result below.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Absolute sub-optimality loss", "weight": 1.0} -->

Then, $\prob{IOP}\text{--}\prob{DD}(\ell_\mathrm{ASO}, \field{P}_N)$ is equivalent to the linear program \min_{\btheta, \blambda_i} \quad & \frac{1}{N} \sum_{i=1}^N | \btheta^\tpose \bhx_i - \bb_i^\tpose \blambda_i | \\\st \quad & \bA_i^\tpose \blambda_i = \btheta, \quad \blambda_i \geq \bzero, \quad \forall i \in \{1, \dots, N\} \\Problem[eq:aso\_lp\_form] generalizes the Inverse Linear Optimization problem of[ahuja2001inverse] from Section[subsec:linear].

<!-- chunk {"id": "body-0156", "role": "body", "section": "Absolute sub-optimality loss", "weight": 1.0} -->

If $\bhx_i$ are all optimal for some $\btheta$, then the optimal objective value will be 0 and we can replace the objective with constraints $\btheta^\tpose \bhx_i = \bb_i^\tpose \blambda$ for all $i$, recovering the original problem[eq:ahuja\_ilo].

<!-- chunk {"id": "body-0157", "role": "body", "section": "Absolute sub-optimality loss", "weight": 1.0} -->

The number of constraints and variables in problem [eq:aso\_lp\_form] scale with the number of data points. If the instances of the forward models are large optimization problems, then the inverse problem can quickly become difficult to solve.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Absolute sub-optimality loss", "weight": 1.0} -->

However, similar to the Minimum Distance loss setting,[chan2018multiple] show that when the forward model is the same for all of the observed decisions, i.e., $\prob{FOP}\text{--}\prob{L}_i(\btheta) = \prob{FOP}\text{--}\prob{L}(\btheta)$ for all $i$, then problem [eq:aso\_lp\_form] can be rewritten as a smaller linear program \min_{\btheta, \blambda} \quad & \frac{1}{N} \sum_{i=1}^N | \btheta^\tpose \bhx_i - \bb^\tpose \blambda | \\\st \quad & \bA^\tpose \blambda = \btheta, \quad \blambda \geq \bzero \\The key observation is that when the forward model is assumed to be the same across instances, we only need to control a

<!-- chunk {"id": "body-0159", "role": "body", "section": "Absolute sub-optimality loss", "weight": 1.0} -->

single dual variable rather than $N$ of them.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Absolute sub-optimality loss", "weight": 1.0} -->

The Absolute Sub-optimality loss can also be used to estimate parameters in the constraints of linear forward models. [chan2020inverse] and[ghobadi2021inferring] generalize their classical methods for constraint estimation (see Section[sec:classical\_io\_linear\_estimating\_constraints]) to the data-driven setting. Recall that[chan2020inverse] consider instances of forward optimization models $\prob{FOP}\text{--}\prob{L}_i(\bPhi)$ where the cost and right-hand-side constraint vectors $\bc_i$ and $\bb_i$, respectively, are given.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Absolute sub-optimality loss", "weight": 1.0} -->

In the data-driven setting, they formulate the problem \min_{\bPhi, \blambda_i} \quad & \frac{1}{N} \sum_{i=1}^N | \bc_i^\tpose \bhx_i - \bb_i^\tpose \blambda_i | \\\st \quad & \bPhi^\tpose \blambda_i = \btheta, \quad \blambda_i \geq \bzero, \quad\forall i \in \{1, \dots, N\} \\& \bPhi \bhx_i \geq \bb_i, \quad \forall i \in \{1, \dots, N\} \\This problem is a bilinear program, but[chan2020inverse] show that when the forward models are identical across instances, under a well-behaved $\bTheta$, the problem has an analytic solution.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Relative sub-optimality loss", "weight": 1.0} -->

Minimizing the Relative Sub-optimality loss function leads to a fractional programming problem, which are generally difficult to solve [frenk2005fractional]. However, this fractional component can be removed if the forward model satisfies a scaling invariance property. Specifically, if we can scale $\btheta$ while preserving the same optimal value and solution set, then the denominator in the loss function becomes irrelevant up to a scaling factor.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Relative sub-optimality loss", "weight": 1.0} -->

A forward model $\prob{FOP}(\btheta)$ is invariant to scaling if $\bx^* \in \set{X}^{\mathrm{opt}}(\btheta)$ implies that (i) $\bx^* \in \set{X}^{\mathrm{opt}}(\alpha \btheta)$ and (ii) $f(\bx^*, \alpha \btheta) = \alpha f(\bx^*, \btheta)$ for any $\alpha > 0$.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Relative sub-optimality loss", "weight": 1.0} -->

If the forward model satisfies this property and has a non-negative optimal value, then we can always scale the parameter while preserving the solution set.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Relative sub-optimality loss", "weight": 1.0} -->

Note that setting $f^{(b)} = x_b$ for all $b$ yields a linear objective, meaning $\prob{FOP}\text{--}\prob{L}_i(\btheta)$is also scaling invariant. [chan2014generalized, chan2018inverse] minimize the Relative Sub-optimality loss for a single decision $(\bhx, \prob{FOP}\text{--}\prob{L}(\btheta))$. [chan2018multiple] extend these results to the case of multiple observed decisions. In both cases, they characterize $\set{X}^{\mathrm{opt}}(\btheta)$ using strong duality. We provide below a revised version of their results for multiple decisions and instances.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Relative sub-optimality loss", "weight": 1.0} -->

Sub-optimality case, when the forward model is the same across instances, the inverse problem can be drastically reduced in size[chan2018multiple].

<!-- chunk {"id": "body-0167", "role": "body", "section": "Relative sub-optimality loss", "weight": 1.0} -->

Furthermore, the positivity assumption $\bb_i > \bzero$ is not necessary for solving $\prob{IOP}\text{--}\prob{DD}(\ell_{\mathrm{RSO}}, \field{P}_N)$; we refer to[chan2018multiple] for the generalization. [troutt2005linear, ref:troutt\_ejor08] explore the Relative Sub-optimality loss for the problem of jointly estimating the objective parameters and constraint matrix for $\prob{FOP}\text{--}\prob{L}((\btheta, \bPhi)):= \min \{ \btheta^\tpose \bx \;|\; \bPhi \bx \geq \bb \}$. Using scaling invariance, they reformulate their inverse problem to the one in Theorem[thm:io\_rdg], except now replacing $\bA_i$ with variables $\bPhi_i$.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Relative sub-optimality loss", "weight": 1.0} -->

The resulting inverse problem is non-convex, but[troutt2005linear, ref:troutt\_ejor08] propose an enumeration algorithm by discretizing the set of potential $\bPhi$.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Variational inequality loss", "weight": 1.0} -->

The first-order Variational Inequality (VI) is an optimality criterion for any general convex optimization problem with a differentiable objective function.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Variational inequality loss", "weight": 1.0} -->

The solution $\bhx_i$ is optimal for $\prob{FOP}\text{--}\prob{CVX}_i(\btheta)$ if and only if \nabla_{\bx} f_i(\bhx_i, \btheta)^\tpose \left(\bhx_i - \bx \right) \leq 0, \quad \forall \bx \in \set{X}_i(\btheta). [bertsimas2015data] use the violation of this variational inequality as a loss measure for data-driven inverse optimization.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Variational inequality loss", "weight": 1.0} -->

They propose the following Variational Inequality loss function: \ell_{\mathrm{VI}}\left(\bhx, \set{X}^{\mathrm{opt}}(\btheta) \right):= \max_{\bx \in \set{X}(\btheta)} \;\; \nabla_{\bx} f(\bhx, \btheta)^\tpose\left(\bhx - \bx \right).

<!-- chunk {"id": "body-0172", "role": "body", "section": "Variational inequality loss", "weight": 1.0} -->

Let $\prob{IOP}\text{--}\prob{DD}(\ell_\mathrm{VI}, \field{P}_N)$ denote the Inverse Variational Inequality problem. This problem is similar to the Sub-optimality problems in that it can usually be solved using convex programming. However, the inverse problem does not immediately yield statistical consistency, meaning there is no guarantee that the empirical risk problem $\prob{IOP}\text{--}\prob{DD}(\ell_\mathrm{VI}, \field{P}_N)$ converges in probability to the expected risk problem $\prob{IOP}\text{--}\prob{DD}(\ell_\mathrm{VI}, \field{P})$. Instead,[bertsimas2015data] develop a generalization bound, i.e., an upper bound on the expected risk as a function of the empirical risk. This bound holds specifically for when the forward models are conic optimization problems.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Variational inequality loss", "weight": 1.0} -->

- $\bA \bx = \bb, \bx \in \set{C}$ almost surely. - There exists $\btx \in \interior(\set{C})$ such that $\bA \btx = \bb$ almost surely. - The feasible sets are absolutely bounded in a ball of radius $R$.

<!-- chunk {"id": "body-0174", "role": "body", "section": "Variational inequality loss", "weight": 1.0} -->

Theorem[thm:ivi\_generalization] is a standard type of generalization bound used to evaluate machine learning models[bartlett2002rademacher]. For any estimated parameter, the theorem bounds the expected risk of variational inequality violation as a function of the empirical risk as observed by the data set and a constant factor that is a function of the number of points $N$ and the size of the feasible set $\bar{B}$. This constant factor scales as $O(1/\sqrt{N})$: with larger data sets of decisions, the empirical risk provides an increasingly accurate approximation of the expected risk.

<!-- chunk {"id": "body-0175", "role": "body", "section": "Variational inequality loss", "weight": 1.0} -->

We first remark that for linear forward models, the loss functions for Inverse Variational Inequality and Inverse Absolute Sub-optimality are equivalent: \ell_{\mathrm{VI}}\left(\bhx, \set{X}^{\mathrm{opt}}(\btheta) \right) &= \max_{\bx \in \set{X}} \; \btheta^\tpose\left(\bhx - \bx \right) % \\= \btheta^\tpose \bhx - \min_{\bx \in \set{X}} \btheta^\tpose \bx %\\= \left|\btheta^\tpose \bhx - \min_{\bx \in \set{X}} \btheta^\tpose \bx \right| = \ell_\mathrm{ASO}(\bhx, \set{X}^{\mathrm{opt}}(\btheta)) Recall that

<!-- chunk {"id": "body-0176", "role": "body", "section": "Variational inequality loss", "weight": 1.0} -->

Then, the generalization bound in Theorem[thm:ivi\_generalization] also applies for Inverse Absolute Sub-optimality with linear forward models. Furthermore, since the Inverse Absolute Sub-optimality problem possesses efficient solution algorithms, the Inverse Variational Inequality problem can be easily solved.

<!-- chunk {"id": "body-0177", "role": "body", "section": "Variational inequality loss", "weight": 1.0} -->

In general, computing $\ell_\mathrm{VI}(\bhx, \set{X}^{\mathrm{opt}}(\btheta))$ requires maximizing a convex optimization problem, and thus, minimizing $\prob{IOP}\text{--}\prob{DD}(\ell_\mathrm{VI}, \field{P}_N)$ outright requires solving a minimax optimization problem. However,[bertsimas2015data] observe that conic optimization problems admit a convenient dual form[aghassi2006solving]. This yields a convex reformulation.

<!-- chunk {"id": "body-0178", "role": "body", "section": "Variational inequality loss", "weight": 1.0} -->

f_i(\bhx_i, \btheta) - \bA_{i}^\tpose \blambda_i \in \set{C}_i \quad \forall i \in \{1, \dots, N\} \\Furthermore if $\nabla_{\bx} f_i(\bx, \btheta)$ is a linear function of $\btheta$, then the above problem is convex.

<!-- chunk {"id": "body-0179", "role": "body", "section": "Variational inequality loss", "weight": 1.0} -->

[thm:ivi\_duality\_solution] shows that the Inverse Variational Inequality problem can be solved via convex programming for forward optimization models with conic constraints. This theorem holds for any of the forward models introduced in Section[sec:problem\_def]. The Inverse Variational Inequality problem is attractive as it can be efficiently solved via convex programming for a large class of convex forward models, while also possessing theoretical guarantees on the quality of the inverse solution.

<!-- chunk {"id": "body-0180", "role": "body", "section": "Violating the KKT conditions", "weight": 1.0} -->

[keshavarz2011imputing] consider $\prob{FOP}\text{--}\prob{CVX}(\btheta)$ and propose loss functions that describe the degree to which each observed decision violates the KKT conditions. Recall that for a decision to be optimal for $\prob{FOP}\text{--}\prob{CVX}(\btheta)$ there must exist a dual variable such that the decision and dual satisfy a stationarity and a complementary slackness condition.

<!-- chunk {"id": "body-0181", "role": "body", "section": "Violating the KKT conditions", "weight": 1.0} -->

We define two loss terms below that measure the degree to which a primal and dual solution pair $(\bx, \blambda)$ violate these conditions: \ell_\mathrm{st}(\bx, \set{X}^{\mathrm{opt}}(\btheta), \blambda) &:= \left| \nabla_{\bx} f(\bx, \btheta) + \sum_{j=1}^m \lambda_{j} \nabla_{\bx} g_{j}(\bx, \btheta) \right| \\\ell_\mathrm{cs}(\bx, \set{X}^{\mathrm{opt}}(\btheta), \blambda) &:= \norm{ \left(\lambda_1 g_1(\bx, \btheta), \lambda_2 g_2(\bx, \btheta), \ldots, \lambda_m g_m(\bx,

<!-- chunk {"id": "body-0182", "role": "body", "section": "Violating the KKT conditions", "weight": 1.0} -->

$\prob{IOP}\text{--}\prob{DD}(\ell_\mathrm{KKT}, \field{P}_N)$ be the Inverse KKT problem. For a given $\bhx$, computing $\ell_\mathrm{KKT}(\bhx, \set{X}^{\mathrm{opt}}(\btheta))$ requires solving a convex optimization problem. Consequently, $\prob{IOP}\text{--}\prob{DD}(\ell_\mathrm{KKT}, \field{P}_N)$ becomes a non-convex problem in $(\btheta, \blambda)$ due to $\ell_\mathrm{cs}(\bhx, \set{X}^{\mathrm{opt}}(\btheta), \blambda)$. However, if the goal is to estimate only the parameters of the objective, then the inverse problem can be solved with convex programming.

<!-- chunk {"id": "body-0183", "role": "body", "section": "Alternatives to empirical risk minimization", "weight": 1.0} -->

So far, we have explored inverse optimization methods that minimize the expectation of a loss function over an empirical data distribution. We may also minimize alternative risk measures. For any probability distribution $\field{P}$, let $\rho^\field{P}(\cdot)$ denote a general risk measure[ruszczynski2006optimization, rockafellar2002conditional], and consider \prob{IOP}\text{--}\prob{DD}\text{--}\prob{R}(\ell, \field{P}, \rho):= \min_{\btheta \in \bTheta} \;\; \rho^\field{P}\left(\ell\left(\bx, \set{X}^{\mathrm{opt}}(\btheta) \right) \right).

<!-- chunk {"id": "body-0184", "role": "body", "section": "Alternatives to empirical risk minimization", "weight": 1.0} -->

Setting $\rho^\field{P}(\cdot) = \field{E}_\field{P}[\cdot]$recovers all of the previous models discussed in this section.

<!-- chunk {"id": "body-0185", "role": "body", "section": "Quantile inverse optimization", "weight": 1.0} -->

Empirical risk minimization yields estimators that may be sensitive to outliers Ideally, a small perturbation in $\field{P}_N$ should not result in a large perturbation of the estimated parameter $\btheta^*$. For example in linear regression, squared-error loss penalizes larger errors and invites sensitivity, motivating alternative approaches such as quantile regression [koenker2001quantile]. To reduce sensitivity in inverse optimization,[shahmoradi2021quantile] propose the Value-at-Risk (VaR) or $\chi$-quantile risk function \VaR_\chi(\ell, \field{P}) &:= \inf_{\tau \geq 0} \left\{ \tau \;\Big|\; \field{P}\left\{ \ell(\bx, \set{X}^{\mathrm{opt}}(\btheta)) \leq \tau \right\} \geq \chi \right\}, where $\chi \in $ is a percentile parameter that we choose.

<!-- chunk {"id": "body-0186", "role": "body", "section": "Quantile inverse optimization", "weight": 1.0} -->

Depending on the predetermined value of $\chi$, the Inverse VaR problem $\prob{IOP}\text{--}\prob{DD}\text{--}\prob{R}(\ell, \field{P}_N, \VaR)$ yields parameter estimates $\btheta^*$ for which the error has a bounded sensitivity with respect to perturbations in the data set.

<!-- chunk {"id": "body-0187", "role": "body", "section": "Quantile inverse optimization", "weight": 1.0} -->

Directly minimizing the $\chi$-quantile risk in $\prob{IOP}\text{--}\prob{DD}\text{--}\prob{R}(\ell, \field{P}_N, \VaR)$ is a challenging optimization problem since the Value-at-Risk is discrete. Given a data set, the Value-at-Risk is defined with indicator functions, $\inf_\tau \{ \tau \;|\; \sum_{i=1}^N \Ind \{ \ell(\bhx_i, \set{X}^{\mathrm{opt}}_i(\btheta)) \leq \tau \} \geq \chi \}$.

<!-- chunk {"id": "body-0188", "role": "body", "section": "Quantile inverse optimization", "weight": 1.0} -->

The difficulty in solving the Inverse VaR problem depends on the choice of $\ell(\bx, \set{X}^{\mathrm{opt}}(\btheta))$.[shahmoradi2021quantile] explore linear forward models $\prob{FOP}\text{--}\prob{L}(\btheta)$ and the Minimum Distance loss $\ell_\mathrm{D}(\bx, \set{X}^{\mathrm{opt}}(\btheta))$ for general $p$-norms.

<!-- chunk {"id": "body-0189", "role": "body", "section": "Quantile inverse optimization", "weight": 1.0} -->

Rather than directly solving Problem [eq:inverse\_quantile\_micp],[shahmoradi2021quantile] fix a target $\chi$-quantile loss $\tau = \hat\tau$ and search for a feasible $\btheta \in \bTheta$ that can achieve this target. Although the original Problem[eq:inverse\_quantile\_micp] is NP-hard, fixing $\tau$ can recast the problem to a bi-clique problem for which there exists effective solution algorithms and heuristics[dawande2001bipartite]. Second, fixing the Inverse VaR loss allows for introducing additional alternative objective functions for the inverse problem. In particular,[shahmoradi2021quantile] explore several statistical properties of forward model stability that they show can be satisfied by fixing $\tau$and minimizing an alternate objective.

<!-- chunk {"id": "body-0190", "role": "body", "section": "Distributionally robust inverse optimization", "weight": 1.0} -->

Generalizing $\prob{IOP}\text{--}\prob{DD}\text{--}\prob{R}(\ell, \field{P}, \rho)$, [esfahani2018data] propose a distributionally robust inverse optimization problem where the ambiguity set controls a worst-case data distribution from the empirical $\field{P}_N$.

<!-- chunk {"id": "body-0191", "role": "body", "section": "Distributionally robust inverse optimization", "weight": 1.0} -->

For any two distributions $\field{P}$ and $\field{Q}$, let W(\field{P}, \field{Q}):= \inf_{\bPi} \left\{ \field{E}_{\bPi} \left[\norm{\bx - \bx'}_2 \right] \;\Bigg|\; \begin{array}{ll} \displaystyle \text{$\bPi$ is a joint distribution of $\bx, \bx'$} \\\text{with marginals $\field{P}$ and $\field{Q}$, respectively} be the Wasserstein distance between them. This distance is well-defined for both continuous and discrete distributions, meaning we can compute Wasserstein distances with respect to $\field{P}_N$.

<!-- chunk {"id": "body-0192", "role": "body", "section": "Distributionally robust inverse optimization", "weight": 1.0} -->

Consider a ball-uncertainty set $\set{B}(\field{P}_N, \epsilon):= \{ \field{Q} \;|\; W(\field{Q}, \field{P}_N) \leq \epsilon \}$ of size $\epsilon > 0$ around the empirical distribution and define the Distributionally Robust Inverse problem \prob{IOP}\text{--}\prob{DD}\text{--}\prob{DRO}(\ell, \field{P}_N, \rho, \epsilon):= \min_{\btheta} \sup_{\field{Q}} \quad & \rho^\field{Q}\left(\ell\left(\bx, \set{X}^{\mathrm{opt}}(\btheta)\right)\right) \\\st \quad & \field{Q} \in \set{B}(\field{P}_N, \epsilon) \\This problem naturally provides an out-of-sample guarantee on the true

<!-- chunk {"id": "body-0193", "role": "body", "section": "Distributionally robust inverse optimization", "weight": 1.0} -->

Consider $\prob{FOP}\text{--}\prob{CVX}_i(\btheta)$ instances that are defined by known input parameters $\bhu_i$. Assume that there exists $\alpha > 1$ for which $A_\alpha:= \field{E}_\field{P}[\exp(\norm{(\bx, \bu)}^\alpha)] < \infty$. Let $\btheta^*$ be an optimal parameter estimate obtained by solving $\prob{IOP}\text{--}\prob{DD}\text{--}\prob{DRO}(\ell, \field{P}_N, \rho, \epsilon)$ and let $z^*_\mathrm{DRO}$ be the optimal value.

<!-- chunk {"id": "body-0194", "role": "body", "section": "Distributionally robust inverse optimization", "weight": 1.0} -->

We refer to[esfahani2018data] for details on computing $\beta$. Note that when $\rho^\field{P}(\cdot) = \field{E}_\field{P}[\cdot]$, the out-of-sample guarantee is similar to a generalization bound (see Theorem[thm:ivi\_generalization]) in terms of bounding the true risk. However, Proposition[propn:dro\_io\_generalization]holds independent of the risk measure or the loss function used to evaluate the inverse problem, meaning that the distributionally robust framework applies to any of the inverse optimization variants that were previously introduced. Furthermore, this guarantee directly compares the empirical and true risk with no additional terms.

<!-- chunk {"id": "body-0195", "role": "body", "section": "Distributionally robust inverse optimization", "weight": 1.0} -->

[esfahani2018data] explore the Conditional-Value-at-Risk (CVaR) at level $\alpha > 0$ as their risk measure for distributionally robust inverse optimization \CVaR(\ell, \alpha, \field{P}) &:= \inf_\tau \tau + \frac{1}{\alpha} \field{E}_\field{P} \left[\max\left\{ \ell(\bx, \set{X}^{\mathrm{opt}}(\btheta)) - \tau, \; 0 \right\} \right].

<!-- chunk {"id": "body-0196", "role": "body", "section": "Distributionally robust inverse optimization", "weight": 1.0} -->

%\\%\CVaR(\ell, \alpha, \field{P}) &:= \inf_\tau \tau + \frac{1}{\alpha} \sum_{i=1}^N \field{E}_\field{P} \left[\max\left\{ \ell(\bhx_i, \set{X}^{\mathrm{opt}}_i(\btheta)) - \tau, \; 0 \right\} \right]. %\\CVaR generalizes the empirical risk as a special case when $\alpha = 1$ and further generalizes the essential supremum risk measure for $\alpha \downarrow 0$. However, the distributionally robust inverse problem $\prob{IOP}\text{--}\prob{DD}\text{--}\prob{DRO}(\ell, \field{P}_N, \CVaR, \epsilon)$ is NP-hard for many forward model classes.

<!-- chunk {"id": "body-0197", "role": "body", "section": "Distributionally robust inverse optimization", "weight": 1.0} -->

For linear forward models $\prob{FOP}\text{--}\prob{L}_i(\btheta)$ and the sub-optimality loss function $\ell_\mathrm{ASO}(\bx, \set{X}^{\mathrm{opt}}(\btheta))$, [esfahani2018data] use techniques from distributionally robust optimization[esfahani2018dro] to show that $\prob{IOP}\text{--}\prob{DD}\text{--}\prob{DRO}(\ell_\mathrm{ASO}, \field{P}_N, \text{CVaR}, \epsilon)$can be re-formulated as a large conic optimization problem.

<!-- chunk {"id": "body-0198", "role": "body", "section": "Distributionally robust inverse optimization", "weight": 1.0} -->

[dong2020wasserstein] build on the distributionally robust framework of[esfahani2018data] for multi-objective forward optimization models \prob{FOP}\text{--}\prob{CVX}\text{--}\prob{MO}((\btheta, \bphi)):= \min_{\bx} \left\{ \sum_{b=1}^{B} \phi_b f^{(b)}(\bx, \btheta) \;\Bigg|\; \bg(\bx, \btheta) \leq \bzero \right\}. $\prob{FOP}\text{--}\prob{CVX}\text{--}\prob{MO}((\btheta, \bphi))$ reduces to the conventional convex forward model $\prob{FOP}\text{--}\prob{CVX}(\btheta, \bphi)$ when considering only a single objective.

<!-- chunk {"id": "body-0199", "role": "body", "section": "Distributionally robust inverse optimization", "weight": 1.0} -->

[dong2020wasserstein] use the expected value risk function $\rho^\field{P}(\cdot) = \field{E}_\field{P}[\cdot]$ and distance minimization loss $\ell_\mathrm{D}$, meaning that their inverse problem is a multi-objective distributionally robust generalization of the Inverse Distance problem of[aswani2018inverse]. Since the inverse problem of[aswani2018inverse] itself is NP-hard, the distributionally robust formulation is even more difficult to solve. Using duality,[dong2020wasserstein]show that the distributionally robust problem can be re-formulated into a semi-infinite optimization problem under certain conditions, which can be solved using constraint generation.

<!-- chunk {"id": "body-0200", "role": "body", "section": "Inverse optimization with non-parametric forward models", "weight": 1.0} -->

[bertsimas2015data] consider non-parametric kernel functions to model a forward optimization objective. A kernel $K: \field{R}^n \times \field{R}^n \rightarrow \field{R}$ is a similarity function that can compare a given point $\bx$ with another $\bhx_i$ in the data set (see[scholkopf2001learning] and[hastie2009elements] for reviews from a machine learning perspective).

<!-- chunk {"id": "body-0201", "role": "body", "section": "Inverse optimization with non-parametric forward models", "weight": 1.0} -->

In inverse optimization, a non-parametric objective can be modeled indirectly by representing the gradient $\nabla_{\bx} f(\bx)$ as a linear combination of kernels with respect to the observed decisions: \theta_{1,1} & \theta_{1, 2} & \cdots & \theta_{1, N} \\\theta_{2,1} & \theta_{2, 2} & \cdots & \theta_{2, N} \\\vdots & \vdots & \ddots & \vdots \\\theta_{n,1} & \theta_{n, 2} & \cdots & \theta_{n, N} Non-parametric representations do not permit a closed form of objective $f(\bx)$ from[eq:kernel\_forward\_objective] and can reduce forward model interpretability at the trade-off of flexibility by being able to characterize the gradient of an arbitrary convex function. Thus, kernel-based forward models are valuable when we do not have a clear structural understanding of an agent's decision-making process.

<!-- chunk {"id": "body-0202", "role": "body", "section": "Inverse optimization with non-parametric forward models", "weight": 1.0} -->

While the inverse optimization literature has primarily explored kernel representations of forward optimization objectives for Inverse Variational Inequality problems, kernel representations can be used in conjunction with any loss functions that depend on computing gradients of a forward objective. Furthermore, note that the kernel representation is linear in the kernel weights, meaning that the use of a kernel function typically will not increase the computational complexity of the inverse optimization problem. Finally, inverse optimization problems for estimating constraints often require gradient representations of the constraint functions (e.g., Inverse KKT). Consequently, non-parametric techniques can also be used to model constraints in such settings.

<!-- chunk {"id": "body-0203", "role": "body", "section": "Inverse optimization with non-parametric forward models", "weight": 1.0} -->

Depending on the choice of kernel function, $\btheta \bK(\bx)$ can represent function spaces that are arbitrarily complex[hastie2009elements], meaning that this non-parametric technique may overfit to the training decision data.[bertsimas2015data] recommend including a regularization penalty in the inverse optimization objective.

<!-- chunk {"id": "body-0204", "role": "body", "section": "Inverse optimization with non-parametric forward models", "weight": 1.0} -->

This regularization term on model complexity is weighted by a parameter $\kappa > 0$ and can be interpreted as a penalty on the smoothness of the kernel representation [girosi1993priors].

<!-- chunk {"id": "body-0205", "role": "body", "section": "Inverse optimization with non-parametric forward models", "weight": 1.0} -->

| Risk measure | Summary | Different risk measures that can be minimized in data-driven inverse optimization. Each risk measure is accompanied by the formula, the forward model classes where it can be easily minimized, statistical properties that it satisfies, and the general solution method.

<!-- chunk {"id": "body-0206", "role": "body", "section": "Inverse optimization with non-parametric forward models", "weight": 1.0} -->

| Risk measure | Summary | Different loss functions that can be minimized in data-driven inverse optimization. Each loss function is accompanied by the formula, the forward model classes where the empirical risk measure can be easily minimized, statistical properties that it satisfies, and the general solution method.

<!-- chunk {"id": "body-0207", "role": "body", "section": "Summary", "weight": 1.0} -->

The data-driven inverse literature proposes risk measures and loss functions that are applicable for any convex forward optimization model. We summarize advantages of the different methods and discuss general rules-of-thumb to consider when selecting a model. The different methods contrast along two dimensions: (i) whether they provide useful statistical properties as an estimator of forward agent behavior and (ii) whether they admit efficient solution algorithms. [tab:summary\_of\_dd\_risks]summarizes common risk measures in the literature and highlights appropriate use cases. While the empirical expected risk includes methods with statistical properties and fast solution algorithms, the quantile (VaR) and CVaR risk measures provide additional stability and generalization properties. These may be useful when the inverse optimizer has limited data sets but must generate estimates that generalize to new instance or are robust to decision data sensitivity. [tab:summary\_of\_dd\_losses] summarizes the different loss functions under the empirical expected risk. All of these losses can be easily minimized for linear forward optimization models, with the Inverse Distance, KKT, and Variational Inequality losses being also efficient for conic models.

<!-- chunk {"id": "body-0208", "role": "body", "section": "Summary", "weight": 1.0} -->

Inverse Distance further guarantees a statistically consistent estimator, while Inverse Absolute Sub-optimality and Inverse Variational Inequality have generalization bounds; the former guarantees convergence to a trueparameter given large data sets, while the latter bounds error when given finite data sets.

<!-- chunk {"id": "body-0209", "role": "body", "section": "Summary", "weight": 1.0} -->

The empirical expected risk is the most well-studied as it provides multiple methods with statistical properties and solution algorithms. However, the quantile (VaR) and CVaR risk measures provide a stability property and out-of-sample bound, respectively, independent of which loss function is used. The out-of-sample guarantee (Proposition[propn:dro\_io\_generalization]) is useful in applications where the inverse optimizer must use a fixed finite data set to estimate parameters that will be used to explain new instances of agent behavior. The stability property of[shahmoradi2021quantile]is useful when the inverse optimizer requires parameters that are robust to decision sensitivity, i.e., they will hold under small perturbations of the observed decisions. Note that efficient solution methods for these two risk measures have only been developed for specific loss functions and forward models. [tab:summary\_of\_dd\_losses] summarizes the different loss functions under the empirical expected risk. Each loss function can be easily minimized for linear forward optimization models. The Inverse Distance, KKT, and Variational Inequality losses further provide efficient algorithms for convex and conic forward models, respectively.

<!-- chunk {"id": "body-0210", "role": "body", "section": "Summary", "weight": 1.0} -->

The statistical properties of these methods fall under one of two categories: consistency (Inverse Distance) versus generalization (Inverse Absolute Sub-optimality, Inverse Variational Inequality). Consistency is useful when using large data sets of decisions because we can guarantee that a consistent estimator will converge to the best possible estimator with more data. On the other hand, generalization, similar to out-of-sample error (Proposition[propn:dro\_io\_generalization]) is important when we must estimate parameters with a finite data set that will hold for future observed decisions.

<!-- chunk {"id": "body-0211", "role": "body", "section": "Related Learning Paradigms", "weight": 1.0} -->

In this section, we overview two related streams to the inverse optimization literature. The first considers the situation where the decision data arrives sequentially in an online manner. This topic is relatively nascent but growing. The second is inverse reinforcement learning, which has evolved in parallel with inverse optimization into a divergent class of methods and applications.

<!-- chunk {"id": "body-0212", "role": "body", "section": "Inverse optimization through online learning", "weight": 1.0} -->

Rather than using a fixed set of decisions to estimate a parameter in one shot, Inverse Online Learning (IOL) operates over multiple rounds where in each round $t \in \{1, 2, \dots, T\}$, the inverse optimizer observes a new decision $\bhx_t \in \set{X}_t$ and then constructs a parameter estimate $\btheta_{t}$ by updating an existing estimate $\btheta_{t-1}$. Algorithm [algo:Online\_learning]outlines the general structure of an IOL problem.

<!-- chunk {"id": "body-0213", "role": "body", "section": "Inverse optimization through online learning", "weight": 1.0} -->

General inverse online learning framework Input: Data set $\{ \bhx_t, \set{X}_t(\btheta) \}_{t = 1}^T$ arriving sequentially; Initial learning rate $\eta_1$; Initial estimate $\btheta_0$ Output: Set of parameter estimates $\{\btheta_t\}_{t = 1}^T$ estimated sequentially Update estimate $\btheta_{t}$ using $(\bhx_t, \set{X}_t(\btheta_{t-1}), \eta_{t-1})$ Update learning rate $\eta_{t}$ The core requirement of IOL algorithms is a computationally efficient update rule. Note that even if observing a sequential stream of decision data, we could still use traditional inverse optimization methods which we refer to here as offline or batch modethat use the entire data set to estimate a parameter. However, these approaches would require solving increasingly larger inverse problems from scratch in each round. In contrast, update rules improve the previous estimate by using only the most recent observed decision.

<!-- chunk {"id": "body-0214", "role": "body", "section": "Inverse optimization through online learning", "weight": 1.0} -->

In fact, the computational efficiency of the IOL algorithms make them efficient heuristics even for offline inverse optimization.

<!-- chunk {"id": "body-0215", "role": "body", "section": "Inverse optimization through online learning", "weight": 1.0} -->

The computational efficiency of the update rules comes at a cost of the learning efficiency (i.e., estimation error) of the overall parameter. Thus, IOL methods require performance guarantees on this learning efficiency, represented by a regret function, which measures the difference in the cumulative loss from online learning versus the loss from a batch-level approach over the time horizon.

<!-- chunk {"id": "body-0216", "role": "body", "section": "Inverse optimization through online learning", "weight": 1.0} -->

\set{X}^{\mathrm{opt}}(\btheta))$ can be any of the loss functions considered in Section [sec:data-driven\_IO].

<!-- chunk {"id": "body-0217", "role": "body", "section": "Inverse optimization through online learning", "weight": 1.0} -->

Then, the performance guarantee is derived as an upper bound of the rate of decrease of $R(\{\btheta\}_{t=1}^T, \{\bhx_t\}_{t=1}^T)$ as a function of the data sequence $\{\bhx_t\}_{t=1}^T$. This bound depends on the loss function and the update rule used.

<!-- chunk {"id": "body-0218", "role": "body", "section": "Updates using a forward optimization oracle", "weight": 1.0} -->

[barmann2020online] explore IOL by minimizing the Absolute Sub-optimality loss (see Section[subsec:suboptimality]). Consider the forward model \min_{\bx} \; \left\{\btheta^\top \bx \; \Big | \; \bx \in \mX_t \right\} where the objective function is linear and unknown and the feasible set is an arbitrary bounded set. Furthermore, the authors assume access to a forward oracle, such that whenever a new data point $(\bhx_{t}, \set{X}_t)$ becomes available, an inverse optimizer can efficiently solve model [eq:forward\_model\_online] using the incumbent estimate $\btheta_{t-1}$ to generate an optimal solution $\bx^*_t \in \mX_t$.

<!-- chunk {"id": "body-0219", "role": "body", "section": "Updates using a forward optimization oracle", "weight": 1.0} -->

Then, the next estimate $\btheta_{t}$ is obtained with either of the two rules below, which are based on multiplicative weights update (MWU) [arora2012multiplicative] and online gradient descent (OGD) [zinkevich2003online] algorithms, respectively: \prob{MWU}(\btheta_{t-1}, \bhx_t): \quad & \btheta_{t} = \btheta_{t-1} - \eta_{t} \, (\btheta_{t-1} \odot (\bx^*_t - \bhx_t))\\ %\quad \quad \prob{OGD}(\btheta_{t-1}, \bhx_t): \quad & \btheta_{t} = \btheta_{t-1} - \eta_{t} \; (\bx^*_t - \bhx_t) Here, the symbol $\odot$ denotes element-wise vector

<!-- chunk {"id": "body-0220", "role": "body", "section": "Updates using a forward optimization oracle", "weight": 1.0} -->

The specifics of the learning rate parameter $\eta_t$ can be found in [barmann2020online]. The two update rules lead to slightly different performance guarantees, but both result in average regret converging at a rate of $\mO(1/\sqrt{T})$. However, the guarantees hold only under the assumption that the data is noise-free, i.e., all data points are generated exactly using a fixed $\btheta^*$ such that $\ell(\bhx_t, \set{X}^{\mathrm{opt}}_t(\btheta^*)) = 0$ for all $t$. This approach is extended by [xinying2020online]with similar convergence results for certain classes of forward problems with non-linear objectives.

<!-- chunk {"id": "body-0221", "role": "body", "section": "Updates using an inverse optimization oracle", "weight": 1.0} -->

[dong2018generalized] propose an update rule using Minimum Distance loss (see Section[sec:datadriven\_distance]) for problems with convex bounded feasible regions and strictly convex objective functions. Their update rule requires the solution of a single-point inverse optimization problem to directly update their parameter estimates, i.e., \btheta_{t} \in \argmin_{\btheta \in \Theta} \left\{ \norm{\btheta - \btheta_{t-1}}^2_2 + \eta_t \ell_\mathrm{D}(\bhx_t, \set{X}_t(\btheta)) \right\}.

<!-- chunk {"id": "body-0222", "role": "body", "section": "Updates using an inverse optimization oracle", "weight": 1.0} -->

The authors also show that average regret converges at a rate of $\mO(1/\sqrt{T})$, but that this convergence rate holds even under noisy data, as long as some assumptions on the distribution of noise is met.

<!-- chunk {"id": "body-0223", "role": "body", "section": "Inverse reinforcement learning", "weight": 1.0} -->

Inverse Reinforcement Learning (IRL) is the problem of estimating the reward function of a reinforcement learning problem[russell1998learning, ng2000algorithms]. Since reinforcement learning can be used for large-scale MDPs, the early IRL literature shares fundamental similarities to Inverse MDPs (see Section[subsec:MDP]). However, modern IRL methods draw from the machine learning literature (e.g., maximum likelihood estimation, gradient descent algorithms) more than inverse optimization[sutton2018reinforcement]. Nonetheless, the similarity of problems suggest that new data-driven inverse optimization methods may be obtained by adapting IRL techniques. We briefly highlight the relationship between IRL and inverse MDPs, summarize early techniques, and sketch current directions; we refer to[arora2018survey]for a detailed survey.

<!-- chunk {"id": "body-0224", "role": "body", "section": "Inverse reinforcement learning", "weight": 1.0} -->

A reinforcement learning problem is defined by the tuple $(\set{S}, \set{A}, p, \btheta, \gamma)$ comprising a state space, action set, transition probabilities, reward function, and discount factor. We deviate slightly from the notation of Section[subsec:MDP] and refer to specific rewards and value functions as $\theta(s, a)$ and $v(s)$, respectively. We assume without loss of generality that there is an initial state $s_0$ from which all trajectories begin. In IRL, we may observe a policy $\hat\bpi(s)$ from an agent, or instead only observe a data set of length $T$ state-action trajectories $\set{D} = \{ \tau_i \}_{i=1}^N$ where $\tau_i:= \langle (s_0, a^i_0), (s^i_1, a^i_1), \dots, (s^i_T, a^i_T) \rangle$.

<!-- chunk {"id": "body-0225", "role": "body", "section": "Inverse reinforcement learning", "weight": 1.0} -->

The goal is to estimate a reward vector $\btheta$for which the observed policy or trajectories are optimal.

<!-- chunk {"id": "body-0226", "role": "body", "section": "Inverse reinforcement learning", "weight": 1.0} -->

Early IRL methods observe a policy $\bhpi$ and solve an inverse problem with convex programming. For instance, Max-Margin methods estimate a reward function such that the actions taken by $\bhpi$ achieve higher expected rewards than any other actions[russell1998learning, ng2000algorithms, abbeel2004apprenticeship, ratliff2006maximum]. q(s, a):= \theta(s, a) + \gamma \sum_{s' \in \set{S}} p(s' | s, a) v(s') denote the state-action $q$-function. Then, given a policy $\bhpi$, the Max-Margin loss function is \ell_\mathrm{MM}(\bhpi):= \sum_{s \in \set{S}} \left(q(s, \bhpi(s)) - \max_{a \in \set{A} \setminus \{\bhpi(s)\}} q(s, a) \right).

<!-- chunk {"id": "body-0227", "role": "body", "section": "Inverse reinforcement learning", "weight": 1.0} -->

The above loss computes the difference in $q$-values between the actions from an observed policy and the next best action. For MDPs where the reward only depends on the state, i.e., $\theta(s, a) = \theta(s)$ for all $a \in \set{A}$,[ng2000algorithms] note that this loss is a convex function of $\btheta$. They formulate a convex program where the estimated reward is constrained to ensure that the observed policy satisfies an optimality condition for the MDP.

<!-- chunk {"id": "body-0228", "role": "body", "section": "Inverse reinforcement learning", "weight": 1.0} -->

Below, we present a variant of the original formulation:%\max_{\btheta} \quad & \sum_{s \in \set{S}} \left(q(s, \bhpi(s)) - \max_{a \in \set{A} \setminus \{\bhpi(s)\}} q(s, a) \right) - \kappa \norm{\btheta}_1 \\\max_{\btheta, v, q} \quad & \ell_\mathrm{MM}(\bhpi) - \kappa \norm{\btheta}_1 \\\st \quad & q(s, a) = \theta(s) + \gamma \sum_{s' \in \set{S}} p(s' | s, a) v(s'), \quad \forall s \in \set{S}, \forall a \in \set{A} \\& v(s) \geq q(s, a), \quad \forall s \in \set{S},

<!-- chunk {"id": "body-0229", "role": "body", "section": "Inverse reinforcement learning", "weight": 1.0} -->

\; a \in \set{A} \\& v(s) = q(s, a'), \quad \forall s \in \set{S}, \; a' = \bhpi(s) \\The constraints of Problem[eq:irl\_max\_margin] are equivalent to[eq:inverse\_mdp2][eq:inverse\_mdp4] except here written with the $q$-function.

<!-- chunk {"id": "body-0230", "role": "body", "section": "Inverse reinforcement learning", "weight": 1.0} -->

Furthermore in addition to the Max-Margin loss,[ng2000algorithms] include a regularization term $-\kappa \norm{\btheta}_1$ that encourages simpler small-magnitude estimated rewards. [eq:irl\_max\_margin] can be typically too difficult to solve for practical applications where the state and action spaces are large and we only observe trajectories rather than policies and state transition probabilities. The Max-Margin literature proposes two resolutions to address these concerns. First, we may model the reward as a linear combination of fixed basis functions $\theta(s) = \sum_{b=1}^B \theta_b f^{(b)}(s)$; this can reduce the number of variables to estimate and further ensure linearity in the parameters identical to convex-separable bases in the inverse optimization literature.

<!-- chunk {"id": "body-0231", "role": "body", "section": "Inverse reinforcement learning", "weight": 1.0} -->

Second, we may eschew designing a reward function itself and instead minimize the margin between the value function of the optimal policy $\bpi(\btheta)$ and the empirical expected state-action $q$-function value, i.e., \min_{\btheta \in \bTheta} \quad & \ell \left(v^{\bpi(\btheta)}\left(s_0 \right), \; \frac{1}{N} \sum_{i=1}^N \left(\theta\left(s_0\right) + \sum_{t=1}^T \gamma^t \theta\left(s_t^{(i)}\right) \right) \right) where $\{\langle (s_0, a^i_0), (s_1^i, a_1^i), \dots, s_T^i, a_T^i) \rangle \}_{i=1}^N$ is the data set of observed trajectories and

<!-- chunk {"id": "body-0232", "role": "body", "section": "Inverse reinforcement learning", "weight": 1.0} -->

$\ell(v_1, v_2)$ is a penalty function on the difference of values.

<!-- chunk {"id": "body-0233", "role": "body", "section": "Inverse reinforcement learning", "weight": 1.0} -->

The above problem is typically solved using iterative heuristics that compute the margin with respect to a set of candidate policies $\tilde\bpi$ in place of the optimal policy. Algorithm[algo:inverse\_reinforcement\_learning]highlights the general steps of a Max-Margin method.

<!-- chunk {"id": "body-0234", "role": "body", "section": "Inverse reinforcement learning", "weight": 1.0} -->

General max-margin inverse reinforcement learning framework Input: Data set of trajectories $\{\tau_i\}_{i=1}^N$ Output: Reward function estimate $\hat\theta(s, a) = \sum_{b=1}^B \hat\theta_b f^{(b)}(s, a)$ Initialize a reward estimate $\tilde\btheta$; Memory of rewards $\set{P} = \emptyset$ Convergence criteria not met Solve the reinforcement learning problem with $\tilde\btheta$ to obtain a candidate policy \tilde\bpi \gets \text{RL}(\set{S}, \set{A}, p, \tilde\btheta, \gamma) Update $\set{P} \gets \set{P} \cup \{ \tilde\bpi \}$ and solve an approximate Max-Margin IRL problem, e.g., \tilde\btheta \gets \argmin_{\btheta \in \bTheta} \quad &

<!-- chunk {"id": "body-0235", "role": "body", "section": "Inverse reinforcement learning", "weight": 1.0} -->

\sum_{\tilde\bpi \in \set{P}} \ell \left(v^{\tilde\bpi}\left(s_0 \right), \; \frac{1}{N} \sum_{i=1}^N \left(\theta\left(s_0\right) + \sum_{t=1}^T \gamma^t \theta\left(s_t^{(i)}\right) \right) \right) Final reward estimate $\tilde\btheta$ Note that the problem formulation of large-scale Max-Margin methods parallel the formulation of data-driven inverse optimization.

<!-- chunk {"id": "body-0236", "role": "body", "section": "Inverse reinforcement learning", "weight": 1.0} -->

In inverse optimization, inverse-feasibility becomes hard to satisfy with large decision data sets, necessitating data-driven loss functions that penalize the violation of optimality conditions. On the other hand, classical IRL is too large to model using optimality criteria, leading to loss functions that penalize the sub-optimality of the trajectories.

<!-- chunk {"id": "body-0237", "role": "body", "section": "Inverse reinforcement learning", "weight": 1.0} -->

Recent IRL methods relate more closely with modern machine learning, e.g., Maximum Entropy [ziebart2008maximum, boularias2011relative], Bayesian IRL[ramachandran2007bayesian, lopes2009active, levine2011nonlinear], or supervised learning of $q$-values[taskar2005learning]. For example, the Maximum Entropy literature posits that in an MDP with stochastic state dynamics, the observed trajectories $\tau$ are drawn from an optimal policy and must have the highest likelihood over all other trajectories.

<!-- chunk {"id": "body-0238", "role": "body", "section": "Inverse reinforcement learning", "weight": 1.0} -->

We conclude this section by highlighting a common weakness of both inverse optimization and IRL. Both problems face the risk of obtaining uninformative degenerate estimates. Note that for any MDP, the all-zero reward function $\theta(s, a) = 0$ will ensure that every policy (including an observed one) is optimal. In IRL, this necessitates well-designed objectives such as the Max-Margin. However,[ng1999policyinvariance] further show that the optimal policy for an MDP with reward function $\theta(s, a, s')$ is invariant to the transformation $\theta(s, a, s') + \gamma \Phi(s') - \Phi(s)$ for any arbitrary function $\Phi: \set{S} \rightarrow \field{R}$. Effectively, if a policy is optimal, there are an infinite number of reward functions for which it is so. To mitigate this problem,[fu2017learning] propose an adversarial IRL framework that estimates `disentangled' rewards.

<!-- chunk {"id": "body-0239", "role": "body", "section": "Inverse reinforcement learning", "weight": 1.0} -->

Although not to the same extent, the scaling invariance property (see Section[subsubsec:data-driven\_IO\_rdg]) is a similar characteristic in inverse optimization. However, scaling invariance is often easily mitigated by a normalization constraint in inverse optimization.

<!-- chunk {"id": "body-0240", "role": "body", "section": "Applications in Design Problems", "weight": 1.0} -->

We review the application of classical inverse optimization for the design of price incentives in bilevel games (Section [subsec:incentive\_design]) and price mechanisms in cooperative games (Section[subsec:mechanism\_design]). These two problems encompass many application areas and share a common theme of using prices to inducebehavioral change, under the assumption that the original decision-generating processes are known.

<!-- chunk {"id": "body-0241", "role": "body", "section": "Incentive design and pricing in bilevel games", "weight": 1.0} -->

Bilevel games represent hierarchical decision-making problems in which a leader makes the first decision and then a follower responds with their own decision [colson2007overview]. The leader may represent a policy-maker that generates incentives $\btheta \in \bTheta$ to encourage specific follower decisions that, for example, may be environmentally friendly or socially responsible. When the incentives are monetary, they appear as perturbations to the objective of the follower's decision-making process \min_{\bx} \; \left \{ g(\bx, \btheta) \; | \; \bx \in \mX \right \}.

<!-- chunk {"id": "body-0242", "role": "body", "section": "Incentive design and pricing in bilevel games", "weight": 1.0} -->

Assuming that the follower's problem is fully observable to the leader, the leader's problem is \min_{\bx, \btheta} \; \left \{ f(\bx) \; \bigg | \; \bx \in \argmin_{\bx \in \mX} g(\bx, \btheta), \, \btheta \in \bTheta \right \}, %[0.2cm] where $f(\bx)$ may, for example, represent the environmental cost of follower decision $\bx$.

<!-- chunk {"id": "body-0243", "role": "body", "section": "Incentive design and pricing in bilevel games", "weight": 1.0} -->

While the leader's problem can sometimes be reformulated as a single, large monolothic formulation, a more efficient approach is to decouple the computation of follower target" decisions and incentives, i.e., as a master problem and an inverse optimization subproblem. This process is depicted in Figure [fig:app\_classical\_IO]. In the master problem, the leader solves a variant of problem[eq:leader] where they minimize their own objective assuming control of the follower's decision. This generates a target" decision $\bhx$. To compute incentives $\btheta \in \bTheta$ that render $\bhx$ an optimal solution to the follower's problem, the inverse optimization subproblem is solved for forward problem[eq:follower]. We describe several examples of applications where this decomposition approach is used.

<!-- chunk {"id": "body-0244", "role": "body", "section": "Incentive design and pricing in bilevel games", "weight": 1.0} -->

every picture/.style=line width=0.75pt confidence=None created_by=None text='\\begin{tikzpicture}[font=\\sffamily]\n \\draw node[box, minimum height=1.7cm, minimum width=3cm, text width=3.0cm] (mp) {Master \\\\ problem};\n \\draw node[text width=2cm, align=center] (targets) {Target decision(s)};\n \\draw (4, -3) node[minimum height=1.7cm, minimum width=3cm, text width=3.0cm, align=center] (known) {Follower \\\\ decision-making \\\\ model(s)};\n %\\draw (3, -4) node[box, minimum width=3cm, text width=3.7cm] (known) {Known \\\\ decision-making \\\\ model};\n \\draw (8, -1.5) node[box, minimum height=1.7cm, minimum

<!-- chunk {"id": "body-0245", "role": "body", "section": "Incentive design and pricing in bilevel games", "weight": 1.0} -->

width=3cm, text width=3.0cm] (io) {Inverse \\\\ optimization \\\\ sub-problem};\n \n \\draw (13, -1.5) node[text width=3.5cm, align=center] (incentives) {Incentives and price mechanisms};\n \n \\draw[arrow] (mp) -- (targets);\n \\draw[arrow] (targets) -- (io);\n \\draw[arrow] (known) -- (io);\n \\draw[arrow] (io) -- (incentives);\n\\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> The solution process of many bilevel optimization problems.

<!-- chunk {"id": "body-0246", "role": "body", "section": "Incentive design and pricing in bilevel games", "weight": 1.0} -->

In this pipeline, classical inverse optimization is used to compute incentives that can induce followers to generate decisions that are optimal for the leader. These decisions are referred to as target decisions. [marcotte2009toll] study the toll design problem for diverting the transportation of hazardous materials away from high-risk and high-population areas. The leader is a local government imposing tolls while the follower is the carrier that is solving a linear optimization routing problem. The authors show that while the leader's problem can be solved as a large mixed integer program, the master-subproblem decomposition is more efficient and has the added benefit of computing tolls that optimize for another criteria in addition to making a low-risk route optimal. Details of this formulation can found in Section [ECsubsec:toll\_design]. [esfandeh2016regulating] and [bianco2016game]consider extensions of this toll design problem by accounting for network congestion effects and interactions between competing carriers, respectively. The Variational Inequality and KKT optimality conditions are leveraged to solve the corresponding inverse problems.

<!-- chunk {"id": "body-0247", "role": "body", "section": "Incentive design and pricing in bilevel games", "weight": 1.0} -->

Similar decomposition approaches have been examined for bilevel games aimed at mitigating carbon emissions For example, [zhou2011designing] consider a setting where the follower is an electricity generator that is planning to expand the generation capacity of different resources. A Partial Inverse Optimization problem (see Section [subsubsec:Partial\_IO]) is used to compute carbon tax and subsidy schemes to incentivize greater investment into renewable generation methods. Finally, the classical inverse optimization problem is also found in bilevel revenue maximization problems. Here, the leader aims to maximize total revenue collected from followers. [brotcorne2008joint], [brotcorne2011exact], and [afcsar2021revenue]show that leader's problem can be solved by decomposing it into a series of inverse optimization problems where each problem computes the maximum amount of profit that can be achieved for a given follower decision.

<!-- chunk {"id": "body-0248", "role": "body", "section": "Mechanism design in cooperative games", "weight": 1.0} -->

Consider a transportation market with $N$ carriers, each facing demand to transport people or goods across a network $\mG(\mV, \mA)$ with nodes $\mV$ and directed arcs $\mA$. Each carrier $i \in \{1, \ldots, N\}$ uses a set of capacitated transportation resources to obtain profits $r_{(v_1,v_2),i}$ for each unit of demand satisfied between node pairs $v_1,v_2 \in \mV$, up to a certain limit. Examples of carriers include freight transportation companies [agarwal2010network] or airlines [houghtalen2011designing]. While carriers can operate independently, the demand for each carrier may not match their resource capacity constraints. Thus, the total profits gained from behaving cooperatively, i.e., as an alliance, is greater than if carriers behave independently.

<!-- chunk {"id": "body-0249", "role": "body", "section": "Mechanism design in cooperative games", "weight": 1.0} -->

Inverse optimization can be used to compute profit-sharing mechanisms that incentivize carriers to make decisions that collectively lead to a cooperatively optimal solution [agarwal2008mechanism,agarwal2010network, houghtalen2011designing, zheng2015network, zheng2015empty]. For clarity, we consider a simplified model from this literature by assuming that $\mG$ is a fully connected network, so that we may simplify the reference of each pair of nodes $v_1, v_2 \in \mV $ to arc notation $a \in \mA$. We also assume zero operating costs for each carrier. Suppose that there is a centralized operator who can assume control over all resources from each carrier $i$. This operator can generate any decision $\bx \in \set{X}$ where each variable $x_a$ denotes the flow on arc $a$ and $\set{X}$ denotes flows that do not exceed collective carrier demands and resource constraints.

<!-- chunk {"id": "body-0250", "role": "body", "section": "Mechanism design in cooperative games", "weight": 1.0} -->

A cooperatively optimal solution $\bhx \in \mX$ can be generated by solving the following master problem, which maximizes the collective profit obtained over the entire network: \max_{\bx} \; \left \{ \sum_{i = 1}^N \, \sum_{a \in \mA} r_{a, i} x_{a}\; \bigg | \; \bx \in \mX \; \right \}.

<!-- chunk {"id": "body-0251", "role": "body", "section": "Mechanism design in cooperative games", "weight": 1.0} -->

A subsequent assignment problem decomposes $\bhx$ into flows for each carrier $\bhx_i$ such that $\bhx = \sum_{i = 1}^N \bhx_i$, where each $\bhx_i \in \mX_i$ represents a target decision for carrier $i$.

<!-- chunk {"id": "body-0252", "role": "body", "section": "Mechanism design in cooperative games", "weight": 1.0} -->

In an alliance, each carrier has full control over their resources and can make any decision $\bx_i \in \mX_i$. One way to incentivize the target decisions is through a cost-per-arc $\theta_a$ agreement. This mechanism rewards carriers for sharing resource capacity along arcs $a \in \mA$, and penalizes them for using their resources to satisfy individual own demand.

<!-- chunk {"id": "body-0253", "role": "body", "section": "Mechanism design in cooperative games", "weight": 1.0} -->

Carrier $i$'s problem under this mechanism is \max_{\bx_i^i, \bx^{-i}_i} \; \left \{ \sum_{a \in \mA} r_{a,i} x^i_{a,i} + \sum_{a \in \mA} \Big (\gamma_{a,i} \: x^{-i}_{a, i} - (1-\gamma_{a,i}) x^i_{a, i} \Big) \theta_{a} \; \bigg | \; \bx_i \in \mX_i \; \right \}, where the parameter $\gamma_{a,i}$ denotes a pre-defined fraction of the arc cost $\theta_a$ that must be paid by carrier $i$ to use arc $a$, and similarly, the fraction of arc cost $\theta_a$ that is received if $i$ shares its resources along arc $a$ [agarwal2010network].

<!-- chunk {"id": "body-0254", "role": "body", "section": "Mechanism design in cooperative games", "weight": 1.0} -->

The variables $x^i_{a,i}$ and $x^{-i}_{a,i}$, where $x_{a,i} = x^i_{a,i} + x^{-i}_{a,i}$, denote the subset of resources that are used to satisfy $i$'s demand and the demand of all other carriers, respectively.

<!-- chunk {"id": "body-0255", "role": "body", "section": "Mechanism design in cooperative games", "weight": 1.0} -->

To compute a single vector $\btheta = (\theta_1, \ldots, \theta_{|\mA|})$ for which every $\bhx_i$ is inverse-feasible, we solve the inverse optimization problem $$\min_{\btheta} \; \left \{ 0 \; \Big| \; \bhx_i \in \set{X}^{\mathrm{opt}}_i(\btheta) \ \forall i \in \{1,\ldots,N\}, \; \btheta \in \bTheta \; \right \}.$$ An important feature of this inverse model is that $\btheta$ must satisfy a large number of other constraints, denoted by set $\bTheta$, which include budget-balancing and stability constraints. The latter ensures that all carrier decisions are in the core of the cooperative game [lucas1971some], i.e., that no subset of carriers finds it more profitable to form a subcoalition [agarwal2010network].

<!-- chunk {"id": "body-0256", "role": "body", "section": "Mechanism design in cooperative games", "weight": 1.0} -->

This inverse problem is solved by reformulating the carriers' forward problems using complementary slackness or KKT conditions [agarwal2008mechanism,agarwal2010network, houghtalen2011designing, zheng2015network, zheng2015empty].

<!-- chunk {"id": "body-0257", "role": "body", "section": "Applications in Estimation Problems", "weight": 1.0} -->

Next, we discuss applications in transportation (Section [subsec:transportation]), power systems (Section [subsec:markets]), and healthcare (Section [subsec:healthcare]). In Section [subsec:other\_apps], we briefly highlight additional application areas.

<!-- chunk {"id": "body-0258", "role": "body", "section": "Transportation system modeling", "weight": 1.0} -->

Equilibrium models have a rich history of modeling congestion in road networks [patriksson2015traffic]. In these models, the travel time on each link in the network is described using a cost function that depends on volume of traffic flow on the link, and overall traffic in the network is assumed to satisfy a set of equilibrium conditions defined by these cost functions. However, finding the right" cost functions to describe a specific network is challenging. [bertsimas2015data] apply the non-parametric Inverse Variational Inequality model (see Section [subsec:non-param]) to estimate these cost functions using data of historical traffic flows in a given geographical region. Under the computed cost functions, the observed traffic flow data approximately satisfy the equilibrium conditions, which are in fact the optimality conditions of a convex forward problem. We leave the mathematical details to Section[subEC:traffic\_VI].

<!-- chunk {"id": "body-0259", "role": "body", "section": "Transportation system modeling", "weight": 1.0} -->

The models that are estimated using the inverse optimization approach have been shown to produce high-quality forecasts of traffic flow across a number of different real-world benchmarks [bertsimas2015data, zhang2016price, zhang2018price]. Aside from prediction, the estimated cost functions provide insight into network inefficiency and the value of smart traffic control [zhang2018price]. Furthermore, they can also be used to guide infrastructural investment and policy decisions, for example, by estimating the effects of new bike lanes on existing road networks [liu2022planning]. In this context, inverse formulations can be developed for richer equilibrium models. For example, [zhang2017data]consider inverse problems for multi-class transportation models where different vehicle types contribute differently to congestion levels.

<!-- chunk {"id": "body-0260", "role": "body", "section": "Personalized agent models", "weight": 1.0} -->

Prescriptive models for routing and scheduling in the transportation literature typically assume that the objective function describing the costs" of every decision is given. In practice, these costs may be unknown, vaguely defined or difficult to characterize. For instance, even under the exact same conditions, two individuals may prefer different decisions due to nonidentical, subjective preferences over various factors. The costs" in these models thus require estimation. [ronnqvist2017calibrated] describe a widely-used route recommendation system for long haul truck drivers in the Swedish forest industry. The recommendation system (i.e., the forward problem) is a multi-objective minimum cost routing problem where the feasible set $\mX = \{\bx \; | \; \bA\bx = \bb\}$ is defined by node-arc incidence matrix $\bA$ and vector $\bb$ capturing the origin and destination node.

<!-- chunk {"id": "body-0261", "role": "body", "section": "Personalized agent models", "weight": 1.0} -->

The cost" for any feasible path $\bx \in \mX$ is a weighted sum of $B$ different objective functions $f(\bx) = \sum_{b=1}^B \theta_b f^{(b)}(\bx)$, where each objective $f^{(b)}(\bx) = \bu_b^\top \bx$ represents a linear penalty such as fuel costs, road quality, speed limits and driver safety. To calibrate weights associated with each objective function, a sample of preferred routes between various origin and destination nodes are collected from the drivers.

<!-- chunk {"id": "body-0262", "role": "body", "section": "Personalized agent models", "weight": 1.0} -->

Given these routes $\bhx_i$ for $i \in \{1,\ldots, N\}$, an inverse optimization model that minimizes the Absolute Sub-optimality loss (Section [subsubsec:abs\_suboptimality]) is solved: \min_{\btheta, \blambda_i} \quad & \frac{1}{N} \sum_{i=1}^N w_i \bigg | \, \Big(\sum_{b=1}^B \theta_b \bu_b^\tpose \Big)\, \bhx_i - \bb_i^\tpose \blambda_i \, \bigg | \\\st \quad & \bA^\tpose \blambda_i = \sum_{b = 1}^B \theta_b \bu_b, \quad \blambda_i \geq \bzero, \quad \forall i \in \{1, \dots, N\} \\The weights $w_i$

<!-- chunk {"id": "body-0263", "role": "body", "section": "Personalized agent models", "weight": 1.0} -->

associated with each data point $i$prioritize different preferred paths, for example, by giving a higher value to paths between nodes that are farther apart.

<!-- chunk {"id": "body-0264", "role": "body", "section": "Personalized agent models", "weight": 1.0} -->

[chen2021inverse] consider inverse optimization for capacitated vehicle routing models, where routes chosen by long-term expert" drivers are used to refine travel time estimates in a network. Given a network with $m$ nodes and $n$ arcs, the routing problem seeks to find a minimum cost route that satisfies all demand for a homogeneous good at every node using a capacitated truck that replenishes inventory by revisiting depots. Let $Q$ denote the capacity of vehicle. Let $\bx$ represent arc choices and $\by \in \mathbb{R}^m_+$ represent the amount of a good in the vehicle at each node on the route.

<!-- chunk {"id": "body-0265", "role": "body", "section": "Personalized agent models", "weight": 1.0} -->

Then, given a demand vector $\bpi \in \mathbb{R}^m_+$, the forward routing problem can be formulated as the following mixed integer linear optimization model \min_{\bx, \by} \left \{\btheta^\top \bx \; \Big | \; \bA\bx + \bB\by \geq \bd, \; \bpi \leq \by \leq Q\mathbf{1}, \; \bx \in \{0,1\}^n \right \}.

<!-- chunk {"id": "body-0266", "role": "body", "section": "Personalized agent models", "weight": 1.0} -->

Given a dataset $\{(\bhx_i, \bhy_i), \bpi_i\}_{i=1}^N$,[chen2021inverse] estimate $\btheta$ using Inverse Online Learning with the Multiplicative Weights Update rule (see Section [subsec:online\_learning]). The authors show in a case study with an online retailer that the calibrated model can reproduce many expert" decisions.

<!-- chunk {"id": "body-0267", "role": "body", "section": "Personalized agent models", "weight": 1.0} -->

Agent modeling and policy-making. Third party decision-makers such as urban planners or public agencies can also use calibrate agent models to help guide policy decisions. [ref:chow\_12], [kang2013location] and [chow2015activity] use inverse optimization to calibrate household activity" models, which are mixed integer programming problems that model individual spatiotemporal travel patterns. The authors use real household survey data from cities across North America to calibrate these models, which can then be used to evaluate the effects of new investments in transit. Alternatively, [you2016inverse] use GPS data to calibrate vehicle routing models describing the freight activity of trucking companies. These models help urban planners better predict potential changes in trucking activity when introducing new parking, delivery or distribution regulations. [wei2018modeling] calibrate airline crew scheduling models using real data of crew schedules from a regional carrier in the U.S.. The calibrated models provide insights into how different airlines handle scheduling delays and how air traffic controllers can better manage centralized operations.

<!-- chunk {"id": "body-0268", "role": "body", "section": "Personalized agent models", "weight": 1.0} -->

With the exception of [wei2018modeling], where the authors develop their own local search heuristic to solve the inverse mixed integer optimization model, the rest of this agent modeling literature employs an algorithm that closely resembles Inverse Online Learning with an inverse optimization oracle (see Section [subsec:online\_learning]). The cutting plane algorithm, discussed in Section [subsec:integer], is used to solve the oracle.

<!-- chunk {"id": "body-0269", "role": "body", "section": "Market-clearing models", "weight": 1.0} -->

In North America, electricity markets are typically supported by a market operator, whose role includes scheduling production and power flow by matching supply offers with demand bids for future dates subject to certain institutional constraints. This market-clearing process is generally formulated as a linear optimization model and is solved at regular intervals every day. Furthermore, the final allocations (solutions), prices (shadow prices), and bid functions are published to maintain transparency in the market-clearing process. [birge2017inverse] describe an inverse optimization model that uses this public information to infer unobservable model parameters reflecting institutional constraints. Learning about these constraints can provide market participants and policy-makers with a better understanding of transmission capacities, which can inform bidding strategies or infrastructural investment decisions. The inverse model assumes a noise-free environment in which the constraint matrix to be estimated must make the data feasible and satisfy complementary slackness. Details of this estimation procedure are provided in Section [subEC:market\_clearing].

<!-- chunk {"id": "body-0270", "role": "body", "section": "Market-clearing models", "weight": 1.0} -->

This application also demonstrates how optimal dual variables of the forward problem can be both meaningful and directly accessible as data. These values can help restrict the parameter search space and may allow for more precise parameter estimation using fewer data points.

<!-- chunk {"id": "body-0271", "role": "body", "section": "Agent demand models", "weight": 1.0} -->

Price-responsive consumers of electricity include smart buildings, electric vehicles and data centers. Accurate demand models of these consumers can help operators, service providers and retailers make better planning, pricing and bidding decisions. We describe the use of inverse optimization to estimate utility functions of consumer demand models, which can then be used to generate demand predictions.

<!-- chunk {"id": "body-0272", "role": "body", "section": "Agent demand models", "weight": 1.0} -->

Let $y$ be a variable describing the amount of electricity consumption. Given a price $p_t$ at time period $t$, we assume that an agent's electricity consumption behaviour is the solution to an unobserved constrained utility maximization problem, $$\max_{y} \; \left \{ u_t(y) - p_ty \; | \; l_t \leq y \leq r_t \right \}.$$ where $u_t(y)$ is the agent's utility function and $(l_t, r_t)$ represent known upper and lower bounds on consumption. Given $N$ observations of consumption-price data pairs $\{(\hat y_i, p_i)\}_{i=1}^N$, the inverse optimization problem estimates a utility function that best fits the given data and accurately predicts future demand on out-of-sample data.

<!-- chunk {"id": "body-0273", "role": "body", "section": "Agent demand models", "weight": 1.0} -->

This requires us to first rewrite model [model:elec\_cons\_init]. $y$ be a variable representing a level of electricity consumption. Given a price $p_t$ at time period $t$, we assume that an agent's electricity consumption behaviour is the solution to an unobserved constrained utility maximization problem $$\max_{y} \; \left \{ u_t(y) - p_ty \; | \; l_t \leq y \leq r_t \right \},$$ where $u_t(y)$ is the agent's utility function and $(l_t, r_t)$ represent known lower and upper bounds on consumption defined by physical properties such as building thermal dynamics [fernandez2021forecasting], or operational constraints such as building temperature settings [saez2016data] and electric vehicle charging levels [fernandez2019ev].

<!-- chunk {"id": "body-0274", "role": "body", "section": "Agent demand models", "weight": 1.0} -->

We assume that the utility function is a stepwise function c_{1,t}s_{1} + \ldots + c_{i,t}(y - (i-1)s) \quad & \text{if $(i-1)s \leq y \leq is, \ i \geq 2$,} where each step" has equal width $s$ for a total of $I$ steps. Furthermore, we assume that $c_{i}^t \geq c^t_{j}$ for all $i < j$, which implies that the marginal utility is non-increasing in the consumption amount.

<!-- chunk {"id": "body-0275", "role": "body", "section": "Agent demand models", "weight": 1.0} -->

With this function, model[model:elec\_cons\_init] can be rewritten as a linear program \max_{\bx} \; \left \{ \left(\, \sum_{i = 1}^I c_{i,t} x_i \,\right) - p_t\mathbf{1}^\top \bx \; \Bigg | \; l_t \leq \mathbf{1}^\top \bx \leq r_t \right \} %y_t \in \mY_t, \; \forall t \in \mT \right \}. with decision vector $\bx$representing the amount consumed in each step.

<!-- chunk {"id": "body-0276", "role": "body", "section": "Agent demand models", "weight": 1.0} -->

The inverse optimization model estimates the components $c_{i,t}$ of the utility function for all $i$. Let the vector $\bpi_t = (\pi_{t,1}, \ldots, \pi_{t,m})$ describe a set of $m$ features at period $t$. Features can include recent consumption behavior or descriptions of weather conditions. Consider a data set of $N$ observations of consumption-features-price tuples $\{(\hat y_t, p_t, \bpi_t)\}_{t=1}^N$. We first transform each $\hat y_t$ into a vector $\bhx_t$ by setting the first $\lfloor y_t/s \rfloor$ elements of the vector as $s$, the $\lceil y_t/s \rceil$-th element as $\lfloor y_t/s \rfloor -s$, and the last $I-\lceil y_t/s \rceil$ elements as zero.

<!-- chunk {"id": "body-0277", "role": "body", "section": "Agent demand models", "weight": 1.0} -->

We then define the utility function components as a linear regression of the features c_{i,t} = \theta_{i,0} + \theta_{i,1}\pi_{t,1} + \ldots + \theta_{i,m}\pi_{t, m}, \quad \forall i \in \{1, \dots, I\}.

<!-- chunk {"id": "body-0278", "role": "body", "section": "Agent demand models", "weight": 1.0} -->

Let $\kappa >0$ be a regularization parameter. The regularized inverse optimization problem is \min_{\btheta \in \bTheta} \; \frac{1}{N} \sum_{t = 1}^N \ell \left (\bhx_t, \set{X}^{\mathrm{opt}}_t(\btheta) \right) + \kappa \norm{\btheta}_p, which estimates the regression parameters of the utility function subject to the utility taking the shape of a stepwise non-increasing linear function.

<!-- chunk {"id": "body-0279", "role": "body", "section": "Agent demand models", "weight": 1.0} -->

Both the Minimum Distance loss function $\ell_{\mathrm{D}}(\bhx_t, \set{X}^{\mathrm{opt}}_t(\btheta))$ (Section [sec:datadriven\_distance]) and the Absolute Sub-optimality loss function $\ell_{\mathrm{ASO}}(\bhx_t, \set{X}^{\mathrm{opt}}_t(\btheta))$ (Section [subsec:suboptimality]) have been examined in the literature [saez2016data,saez2017short,fernandez2019ev,fernandez2021forecasting,lu2018data]. The regularization hyperparameter $\kappa$ can be tuned using cross-validation. Since model [model:elec\_cons\_init]is a linear optimization model, strong duality can be used to formulate and solve the inverse problem.

<!-- chunk {"id": "body-0280", "role": "body", "section": "Agent demand models", "weight": 1.0} -->

The calibrated forward models are shown to outperform both classical and black-box time series forecasting methods over synthetic and real data.

<!-- chunk {"id": "body-0281", "role": "body", "section": "Agent demand models", "weight": 1.0} -->

The estimated utility function also possesses the same stepwise linear shape as the demand bids that must be submitted to market-clearing operators, meaning that the estimated functions can be directly submitted as a bid by a retailer. This latter observation reveals another benefit of using such a structured" estimation framework.

<!-- chunk {"id": "body-0282", "role": "body", "section": "Healthcare systems", "weight": 1.0} -->

Clinical pathways specify standardized processes in healthcare delivery for a specific group of patients. Patient journeys through the healthcare system that follow these pathways are considered concordant, whereas alternate pathways that ignore certain steps or include extraneous steps are deemed discordant. [chan2022inverse] use inverse optimization to develop a quantitative metric that measures the concordance of patient-traverse pathways against the recommended clinical pathways. Patient pathways are modeled as a walk on a graph representing the healthcare system. Clinical pathways are shortest paths on this graph. The following model represents an inverse shortest path problem, where the goal is to find arc costs $\btheta$ that make the clinical pathways shortest paths.

<!-- chunk {"id": "body-0283", "role": "body", "section": "Healthcare systems", "weight": 1.0} -->

\min_{\btheta, \blambda,\boldsymbol{\epsilon}} \quad & \sum_{i=1}^{N}(\epsilon^{r}_{i})^2\\\st \quad & \bA^\tpose \blambda \le \btheta\\& \btheta^\tpose \hat\bx^{r}_{i}=\bb^\tpose \blambda+\epsilon^{r}_{i}, \quad \forall i \in \{1, \ldots, N \} \\In this model, $\bA$ and $\bb$ encode the flow balance constraints in a shortest path problem with one source and one sink. We assume there are $N$ clinical pathways given, $\hat\bx^r_1, \ldots, \hat\bx^r_N$, between the source and sink.

<!-- chunk {"id": "body-0284", "role": "body", "section": "Healthcare systems", "weight": 1.0} -->

This model is a slight variation of the Absolute Sub-optimality model[eq:aso\_lp\_form\_one\_feas\_region], where: (i) the objective is the sum of squared duality gaps instead of sum of absolute duality gaps, and (ii) the duality constraints are modified, since the shortest path forward problem is a standard form linear program. The normalization constraint $\|\btheta\|_\infty = 1$ prevents $\btheta = \bzero$ from being optimal. The constraint $\bA\btheta = \bzero$ deals with the lower dimensionality of the forward feasible region (due to flow balance equality constraints) and ensures the cost vector does not point orthogonal to the entire feasible region. These constraints form $\bTheta$. Additional details are given in Section[sec:DPMEC].

<!-- chunk {"id": "body-0285", "role": "body", "section": "Healthcare systems", "weight": 1.0} -->

This work has been extended to the more complex clinical pathways associated with breast cancer diagnosis and treatment, modeled using hierarchical networks [chan2021inverse\_hier].

<!-- chunk {"id": "body-0286", "role": "body", "section": "Healthcare systems", "weight": 1.0} -->

The United States Medicare Shared Savings Program (MSSP) offers providers of medical care, known as Accountable Care Organizations (ACOs), bonus payments if they can reduce the cost of providing care for Medicare patients, as long as certain quality constraints are maintained. [aswani2019data] propose a modified MSSP contract with a performance-based subsidy for an ACO's upfront investment, to make participation in the MSSP more attractive. They use a principal-agent framework, where Medicare is the principal (aiming to maximize savings) and an ACO is the agent (aiming to maximize expected payoff). The resulting problem is bilevel since the solution to the ACO's problem, its optimal savings, is embedded in the constraints of Medicare's contract design problem. The key parameter to be estimated is an ACO's type, which is unobservable to Medicare and represents the ACO's ability to generate savings. Using a public data set that includes data on ACO spending and savings,[aswani2019data]solves a data-driven inverse optimization model to estimate the distribution of ACO types from the data.

<!-- chunk {"id": "body-0287", "role": "body", "section": "Healthcare systems", "weight": 1.0} -->

They use this distribution to construct optimal subsidy-based contracts that can simultaneously increase Medicare savings and ACO payments.

<!-- chunk {"id": "body-0288", "role": "body", "section": "Healthcare systems", "weight": 1.0} -->

Breast cancer screening. Disease screening strategies depend on the sensitivity and specificity of the test.[ayer2015inverse] estimates the range of sensitivity and specificity values of a hypothetical test that would make a given screening policy optimal. Disease progression under a given screening policy is modeled as a partially observable Markov chain. The resulting inverse optimization problem becomes a nonlinear problem and a complete solution method is proposed.

<!-- chunk {"id": "body-0289", "role": "body", "section": "Personalized decision making", "weight": 1.0} -->

Radiation therapy (RT) is one of the main ways to treat cancer.

<!-- chunk {"id": "body-0290", "role": "body", "section": "Personalized decision making", "weight": 1.0} -->

Treatment design the angles from which the radiation is delivered, the shape of the radiation beam from each angle, and the distribution of intensity over the beam's shape (divided into small beamlets) is performed by solving a large optimization model with an objective that is a weighted sum of multiple sub-objectives. Inverse optimization learns these weights from historical treatments. Using real data from previously treated prostate cancer patients,[chan2014generalized] show that simple linear models with inversely optimized objective function weights for a small number of objectives could recreate treatments that were designed using complex, non-convex treatment planning models with many objectives. Section[sec:RTEC]provides more details.

<!-- chunk {"id": "body-0291", "role": "body", "section": "Personalized decision making", "weight": 1.0} -->

Extensions from a modeling perspective include using convex objective functions [chan2018trade, sayre2014automatic], learning objective functions rather than the weights[ajayi2022objective], and using input data that represents partial dose distributions [babier2018knowledge]. Another direction of research includes combining inverse optimization with machine learning methods to generate personalized weights for each patient based on patient-specific anatomy, and to automate the treatment planning process for prospective patients[lee2013predicting,boutilier2015models,babier2018knowledge,babier2020knowledge,babier2020importance,goli2018small]. Finally,[ghate2020imputing]uses inverse optimization to estimate unobservable parameters of a non-convex quadratically constrained quadratic problem that finds optimal dosing schedules given observed schedules from clinical studies.

<!-- chunk {"id": "body-0292", "role": "body", "section": "Personalized decision making", "weight": 1.0} -->

Several papers have formulated Markov decision process models to determine when a patient should accept a living-donor transplant [alagoz2004optimal, alagoz2007choosing, alagoz2007determining]. In[erkin2010eliciting], the authors propose the inverse problem. By assuming a control-limit policy over ordered health states describing when a patient switches from waiting to accepting an offered liver, inverse optimization can determine patient preferences over the health states that make the observed policy optimal. Their paper applied formulation [eq:inverse\_mdp]with a weighted 1-norm in the objective and polyhedral constraints on the cost vector to generate a linear inverse problem.

<!-- chunk {"id": "body-0293", "role": "body", "section": "Additional applications", "weight": 1.0} -->

- Finance: Inverse optimization can be used to learn risk preferences of investors by using data on investment strategies. Consider the Markowitz mean-variance portfolio optimization problem \max_{\bx} \quad & \bx^\top \bQ \bx + \kappa \br^\top \bx\\- where $\bQ$ represents the covariance of stock returns, $\br$ is the vector of mean returns, and $\kappa$ is the preferred risk tolerance of the portfolio. Here, the linear constraints $\bA\bx \geq \bb$ denote any additional restrictions that may be imposed on investments. If we assume that observed investment decisions approximately reflect solutions to the Markowitz model, and that we have observed data $\{(\bhx_i, \br_i, \bQ_i, \bA_i, \bb_i)\}_{i=1}^N$, then we can use inverse optimization to infer the value of $\kappa$.

<!-- chunk {"id": "body-0294", "role": "body", "section": "Additional applications", "weight": 1.0} -->

Risk preference learning in Markowitz models is studied in [yu2021learning] using Inverse Online Learning with Minimum Distance loss (see Section [subsubsec:IOL\_inverseoracle]). The inverse model uses the optimality conditions \set{X}^{\mathrm{opt}}(\kappa) = \left \{ \bx \; \bigg | \; \bA\bx \geq \bb, \; \by^\top(\bA\bx - \bb) = 0, \; \bQ\bx - \kappa \br - \bA^\top \by = \bzero, \; \by \geq \mathbf{0} \right \}. - [li2021inverse] establish a more general framework for risk preference inference by developing inverse models for general, convex risk functions. Learned preferences can be used by financial planners and new automated robo-advising systems to provide investment support that is tailored to individual tastes [alsabah2019robo]. They can also be used to assess additional properties of existing portfolios.

<!-- chunk {"id": "body-0295", "role": "body", "section": "Additional applications", "weight": 1.0} -->

For example, [utz2014tri] uses a variant of the inverse Markowitz model to assess the level of environmental and social consideration that is given to socially-responsible mutual fund products when designed by different fund managers. - Economics: Inverse models have developed for multi-player Nash games, which are well-studied and appear in different application domains. In these games, each player $i \in \{1, \dots, N\} $ is assumed to simultaneously solve the following optimization problem, where $\bx^i$ denotes player $i$'s decision and $\bx^{-i}$ denotes the decisions of all other players: \max_{\bx^i} \left \{ f(\bx^i, \bx^{-i}, \btheta^i) \; \bigg | \; \bx^i \in \mX^i \right \} \quad \forall i \in \{1, \dots, N\}. - The objective function is typically assumed to be linear or quadratic in $\bx^i$ and $\bx^{-i}$.

<!-- chunk {"id": "body-0296", "role": "body", "section": "Additional applications", "weight": 1.0} -->

These games are often used to model decentralized markets where market participants compete by deciding on production quantity. Under mild assumptions, the equilibria of these multi-player games can be described using variational inequalities and KKT conditions. To infer the $\{\btheta_i\}_{i=1}^N$ terms, [bertsimas2015data] consider a data-driven inverse VI approach while [ratliff2014social] and [risanger2020inverse] apply a data-driven inverse KKT approach. [allen2021using] extends the inverse KKT approach to generalized Nash equilibria, where player decisions not only affect each other's objectives but also each other's feasible regions, for example, through a joint capacity constraint. - Biology: Optimization models are used to model certain cellular processes. For example, linear optimization can be used to model the metabolism of a cell [orth2010flux]. [ref:zhao\_cdc15] and [zhao2016mapping]apply data-driven inverse linear models with sub-optimality loss to infer objective functions that best explain and predict cellular metabolism behavior.

<!-- chunk {"id": "body-0297", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper reviews the extensive literature on inverse optimization.

<!-- chunk {"id": "body-0298", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We conclude with what we believe are two fruitful directions for future research.

<!-- chunk {"id": "body-0299", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The first direction is to develop more efficient solution methods. As we have pointed out in this review, many inverse models do not scale well with data. For example, when decision data points are drawn from different feasible regions, each data point requires the introduction of a new set of variables and constraints into the inverse model. Future work could aim to improve the solvability of large-scale inverse models, for example through novel decomposition or approximation methods.

<!-- chunk {"id": "body-0300", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The second direction is to develop inverse models that can better incorporate distributional information. The literature to date has little to no distributional assumptions about the input data, model parameters, or the degree of model mis-specification. This is in direct contrast with other models in statistics or econometrics, which rely heavily on distributional information. Incorporating such information may improve the estimation or prediction quality of the models.

<!-- chunk {"id": "body-0301", "role": "body", "section": "Additional Details for Select Applications", "weight": 1.0} -->

In this section we provide additional mathematical details of some applications that are discussed in the main body of the paper.

<!-- chunk {"id": "body-0302", "role": "body", "section": "Toll design for risk mitigation", "weight": 1.0} -->

$\mG(\mV, \mA)$ denote a network with nodes $\mV$ and arcs $\mA$. Assume the carrier's problem is a multi-commodity flow problem over $\mG$ minimizing the cost of transporting $S$ types of hazardous materials between a set of source-sink pairs. For each material type $s \in \{1, \dots, S\}$, let $c_a^s$ denote the cost of transporting the material $s$ on arc $a \in \set{A}$ and let $x_a^s \in \{0, 1\}$ be a binary variable that equals one if material $s$ is transported on arc $a$. Given resource and flow balance constraints in the form of $\set{X}$, the carrier's multi-commodity flow problem is \min_{\bx} \; \left \{ \sum_{s = 1}^S \sum_{a \in \mA} c_{a}^s x_{a}^s \; \bigg | \; \bx \in \mX \right \}.

<!-- chunk {"id": "body-0303", "role": "body", "section": "Toll design for risk mitigation", "weight": 1.0} -->

To solve this problem, we can use the master-subproblem technique, described in Section [sec:classic\_IO\_apps], which decouples the computation of the lowest-risk solution and the corresponding tolls into two sequential linear programs. Specifically, we first solve the master problem \min_{\bx} \; \left \{ \sum_{s=1}^S \, \sum_{a \in\mA} \rho_{a}^s x_{a}^s \; \bigg | \; \bx \in \mX \right \},%\text{MP:} \ \underset{\bx}{\min} \left \{ \sum_{s=1}^S \, \sum_{a \in\mA} \eta^s \rho_{a}^s x_{a}^s \; \bigg | \; \bx \in \mX \right \}, to yield a feasible flow $\bhx$ that minimizes the risk.

<!-- chunk {"id": "body-0304", "role": "body", "section": "Toll design for risk mitigation", "weight": 1.0} -->

Then we solve an inverse optimization subproblem to obtain the tolls for which $\bhx$ is now also optimal for the carrier, i.e., \min_{\btheta} \; \left \{ \sum_{s=1}^S \, \sum_{a\in\mA} \theta_{a}^s \hat x_{a}^s \; \bigg | \; \bhx \in \set{X}^{\mathrm{opt}}(\bc + \btheta), \; \btheta \geq \mathbf{0} \right \}.

<!-- chunk {"id": "body-0305", "role": "body", "section": "Toll design for risk mitigation", "weight": 1.0} -->

Note that this inverse problem computes the minimumamount of tolls that must be collected from the carrier to induce the minimum-risk solution.

<!-- chunk {"id": "body-0306", "role": "body", "section": "Estimating traffic equilibrium models", "weight": 1.0} -->

We first describe the traffic assignment model (i.e., the forward problem which produces equilibrium conditions), then provide details on inverse optimization framework used to estimate this model.

<!-- chunk {"id": "body-0307", "role": "body", "section": "Estimating traffic equilibrium models", "weight": 1.0} -->

The forward problem. Let $\mG = (\mV, \mA)$ define a road network consisting of a set of $m$ nodes $\mV$ and a set of $n$ directed arcs $\mA$, and let $\mP = \mV \times \mV$ denote the set of all node pairs in the network. Let $\bA \in \{0,1,-1\}^{m \times n}$ denote the node-arc incidence matrix. The value $d_{i,j}$ denotes the demand between each pair of nodes $(i,j) \in \mP$, and we define a corresponding vector $\bb^{i,j} \in \mathbb{R}^m$ where $\bb^{i,j}$ is a vector of all zeros except for elements $i$ and $j$ where $b^{i,j}_i = d_{i,j}$ and $b^{i,j}_j = - d_{i,j}$.

<!-- chunk {"id": "body-0308", "role": "body", "section": "Estimating traffic equilibrium models", "weight": 1.0} -->

Let $\bx^{i,j} = (x^{i,j}_1, \ldots, x^{i,j}_{n})$ denote a vector of flows on each arc corresponding to demand between node $i$ and $j$. Finally, let $\mX$ be the set of aggregate flows satisfying all pairwise demand, i.e., \bx \; \Bigg| \ \bx = \sum_{(i,j) \in \mP} \bx^{i,j}, \; \bA \bx^{i,j} = \bb^{i,j}, \; \bx^{i,j} \geq \mathbf{0}, \ \ \forall (i,j) \in \mP \right\}.

<!-- chunk {"id": "body-0309", "role": "body", "section": "Estimating traffic equilibrium models", "weight": 1.0} -->

For a given flow $\bx \in \mX$, let $\bff(\bx) = (f_1(x_1), \ldots, f_{n}(x_n))$ be the vector of marginal travel time costs on each arc under $\bx$. In the transportation literature, these costs are commonly modeled as f_a(x_a) = c_a \, g\left(\frac{x_a}{m_a}\right), where $c_a$ is a parameter measuring the uncongested travel time of arc $a$, $m_a$ is a parameter corresponding to the capacity" of an arc (e.g., the number of lanes and the speed limit) and $g(x)$ is a monotonically increasing function modeling congestion effects. Thus, arc costs are differentiated only by $c_a$ and $m_a$, where they increase when $c_a$ or $x_a$ increase, or when $m_a$ decreases.

<!-- chunk {"id": "body-0310", "role": "body", "section": "Estimating traffic equilibrium models", "weight": 1.0} -->

Given a demand matrix and known cost functions, different flow solutions can be computed using various transportation models which differ by the underlying assumptions made. A widely studied model is the traffic assignment problem [dafermos1969traffic, patriksson2015traffic], which produces solutions describing decentralized traffic flow, where every driver has complete information on costs and makes their routing decisions independent of decisions made by other drivers. This defines the forward model \min_{\bx} \left\{ \sum_{a = 1}^n \int_0^{x_a} f_a(s) \; ds \; \Bigg | \; \bx \in \mX\right\}.

<!-- chunk {"id": "body-0311", "role": "body", "section": "Estimating traffic equilibrium models", "weight": 1.0} -->

Since $\bff(\bx)$ represents the marginal travel time cost, it is the gradient of the objective function in the forward model. This model is considered to be a good approximation for describing real-world traffic movement. However, for this model to be of practical use, $\bff(\bx)$, and more specifically the $g(.)$ function, must be known. The standard approach in transportation modeling is to assume a specific $g(.)$ function, a common choice being $g(\frac{x_a}{m_a}) = (1 + 1.15(\frac{x_a}{m_a})^4)$, as well as a specific value of $m_a$[chow2014nonlinear, bertsimas2015data]. However, assuming such functions, rather than deriving from data, can result in poor modeling and out-of-sample performance.

<!-- chunk {"id": "body-0312", "role": "body", "section": "Estimating traffic equilibrium models", "weight": 1.0} -->

Suppose we observe spatiotemporal data of transportation flows and demands over $T$ periods, denoted by $\{(\bhx_t,\mX_t)\}_{t=1}^T$ with $\bhx_t \in \mX_t$ for all $t$. In the inverse problem, we estimate the marginal travel time cost functions $\bff(\bx, \btheta)$ where $f_a(x_a, \btheta) = c_a g(\frac{x_a}{m_a}, \btheta)$ are now parametrized by $\btheta$.

<!-- chunk {"id": "body-0313", "role": "body", "section": "Estimating traffic equilibrium models", "weight": 1.0} -->

Following [bertsimas2015data] and [zhang2018price], we model $g(\frac{x_a}{m_a}, \btheta)$ using polynomial kernels g\left(\frac{x_{a}}{m_a}, \btheta \right) = 1 + \theta_1 \left(\frac{x_a}{m_a}\right) + \ldots + \theta_n \left(\frac{x_a}{m_a}\right)^n.

<!-- chunk {"id": "body-0314", "role": "body", "section": "Estimating traffic equilibrium models", "weight": 1.0} -->

In order to estimate $\btheta$ using the data set $\{(\bhx_t,\mX_t)\}_{t=1}^T$, [bertsimas2015data] leverage an important property from the transportation literature, that when $\bff(\bx, \btheta)$ is strongly monotonic and continuously differentiable, the optimal traffic flows satisfy a Wardrop equilibrium[dafermos1969traffic, patriksson2015traffic]. That is, the unique optimal solution $\bx^*$ to $eq:TAP$ is also the unique solution to the following set of variational inequalities \bff(\bx^*, \btheta)^\top (\bx - \bx^*) \geq 0, \quad \forall \bx \in \mX.

<!-- chunk {"id": "body-0315", "role": "body", "section": "Estimating traffic equilibrium models", "weight": 1.0} -->

The Wardrop equilibrium ensures that for every $(i,j) \in \mP$, and for any route between the pair with positive flow in $\bx^*$, the cost of traveling along that route is no greater than the cost of traveling along any other feasible routes between $i$ and $j$ [patriksson2015traffic]. Practically, this implies that every driver acts selfishly and takes the lowest cost route.

<!-- chunk {"id": "body-0316", "role": "body", "section": "Estimating traffic equilibrium models", "weight": 1.0} -->

The parameters $\delta_i$ define a penalization term for polynomial kernels [bertsimas2015data, zhang2018price]. The set $\bTheta$ includes constraints that impose monotonicity on $\bff(\cdot)$ over the observed flow ranges, either in the form of a general constraint $\btheta \geq \mathbf{0}$ or as a set of individual constraints on each arc in the form of $f_a(x_a) \geq f_a(\tilde{x}_a)$ for all observed arc flows $x_a$ and $\tilde{x}_a$ where $x_a \geq \tilde{x}_a$. Note that because $g(\frac{x_a}{m_a}, \mathbf{0}) = 1$ in equation [app:poly\_kernel], we avoid inferring the trivial" objective vector $g(\cdot) = 0$ that would render all observed solutions equivalent and optimal.

<!-- chunk {"id": "body-0317", "role": "body", "section": "Estimating traffic equilibrium models", "weight": 1.0} -->

Finally, the regularization term $\kappa$in the inverse problem can be tuned using cross-validation. [zhang2016price] and [zhang2018price] show that the estimated cost functions can be used in a different model to measure network efficiency. Specifically, we can use $\{f_a(\cdot)\}_{a \in \mA}$ to solve a system-optimal routing model, which minimizes the total cumulative cost of travel for all drivers: $$\min_{\bx} \left\{ \sum_{a \in \mA} x_a f_a(x_a) \; \Big | \; \bx \in \mX \right\}.$$ Unlike solutions from model [eq:TAP], solutions from model [eq:SOP] are Pareto efficient. The ratio of the total travel time between system-optimal and user-optimal solutions, known as the price of anarchy", provides a measure of the efficiency of the system. While the ratio has been studied extensively as a theoretical concept, the inverse optimization approach enable the authors to provide one of the first empirical estimates of this ratio.

<!-- chunk {"id": "body-0318", "role": "body", "section": "Inferring constraints of market-clearing models", "weight": 1.0} -->

Consider a market with $J$ participants situated across $I$ different nodes. Let $v_j$ denote the total amount of electricity consumed ($v_j < 0$) or produced ($v_j > 0$) by participant $j \in \{1,\ldots,J\}$ who is situated at node $n(j)$. Let $S_j(v_j)$ describe an offer or bid function submitted by participant $j$, i.e., $S_j(v_j)$ (or $-S_j(v_j)$) denotes the price that a consumer (or producer) $j$ is willing to pay (or be paid) for $v_j$. We assume $S_j(v_j)$ is stepwise linear. Finally, let $x_i$ represent the total amount of electricity consumed or produced at node $i \in \{1, \ldots, I\}$.

<!-- chunk {"id": "body-0319", "role": "body", "section": "Inferring constraints of market-clearing models", "weight": 1.0} -->

The market clearing model as defined in [birge2017inverse] maximizes social welfare subject to constraints on $M$ different transmission links as well as constraints $\bv \in \mV$ defining individual production and consumption, i.e., \max_{\bx, \bv} \quad & \sum_{j=1}^J S_j(v_j)\\\text{s.t.} \quad & \sum_{j: n(j) = i} v_j = x_i, \quad \forall i \in \{1, \dots, I\}, \\%& \bll \leq \bv \leq \bu,\\The matrix $\bA \in \mathbb{R}^{M \times I}$ and vector $\bb \in \mathbb{R}^{M}$ define the grid and the transmission capacities (based on DC power flow).

<!-- chunk {"id": "body-0320", "role": "body", "section": "Inferring constraints of market-clearing models", "weight": 1.0} -->

The vector of optimal dual variables $\hat \bpi \in \mathbb{R}^I$ and $\hat \blambda \in \mathbb{R}^M$ corresponding to constraints [cons:ece\_nodes] and [cons:ece\_links]represent the prices of electricity at every node and the shadow prices of various capacity constraints, respectively; these are used to decide payments.

<!-- chunk {"id": "body-0321", "role": "body", "section": "Inferring constraints of market-clearing models", "weight": 1.0} -->

To recover the matrix $\bA$, [birge2017inverse] assume a noise-free environment and use a publicly available data set $\{(\bhx_i, \hat \blambda_i, \hat \bpi_i)\}_{i=1}^N$ where $N \geq M$ to find a matrix $\bA$ and vectors $\bb_i$ that satisfy the following set of optimality conditions ([birge2017inverse] include other constraints related to the physical transmission of electricity, which we omit here for simplicity): \bpi_i = \hat\blambda_i \bA, \ \bA \bhx_i \leq \bb_i, \ \hat\blambda_i \odot (\bA\bhx_i - \bb_i) = \mathbf{0}, \quad \forall i \in \{1, \ldots, N\}.

<!-- chunk {"id": "body-0322", "role": "body", "section": "Inferring constraints of market-clearing models", "weight": 1.0} -->

Finally, we note that the operations of electricity markets vary significantly across geographic regions, and these distinctions offer new research opportunities. For example, [ruiz2013revealing]examine a market where the model constraints are published rather than the bids. The authors describe a duality-based inverse optimization model to infer stepwise bid functions of producers.

<!-- chunk {"id": "body-0323", "role": "body", "section": "Clinical pathway concordance measurement", "weight": 1.0} -->

$\mathcal{G}$ denote a graph with nodes $\mathcal{N}$ and arcs $\mathcal{A}$. The nodes describe the set of activities patients can undertake, including concordant activities like medical imaging and treatment, and discordant activities like emergency department visits and extra consultations. A walk through the graph accumulates costs along the arcs it traverses. Clinical pathways developed by experts are assumed to be shortest paths through $\mathcal{G}$. Implicit costs of arcs between activities can then be estimated with model[model:IOclinpathway], which identifies a single set of arc costs $\btheta$that minimizes the aggregate sub-optimality of clinical pathways with respect to the difference between their costs and the shortest path cost. [model:IOclinpathway] considers the expert-defined clinical pathways as input, it does not consider actual patient data from either successful or unsuccessful clinical workflows. Consequently,[chan2022inverse] employ a second stage inverse problem to refine the cost vector $\btheta^*$ from model[model:IOclinpathway] with real patient pathways.

<!-- chunk {"id": "body-0324", "role": "body", "section": "Clinical pathway concordance measurement", "weight": 1.0} -->

Consider a set of patient-traversed pathways from patients who survived their cancer, $\hat\bx^s_1, \ldots, \hat\bx^s_S$ and a set of patient-traverse pathways from patients who died, $\hat\bx^d_1, \ldots, \hat\bx^d_D$. The refined problem penalizes the duality gaps with respect to patients who survived and encourages higher duality gaps for patients who died, while fixing the optimal duality gaps $\epsilon^{r*}_i$ from problem [model:IOclinpathway].

<!-- chunk {"id": "body-0325", "role": "body", "section": "Clinical pathway concordance measurement", "weight": 1.0} -->

The objective minimizes (maximizes) the aggregate sub-optimality with respect to the patients who survived (died). Because $\epsilon^{r*}_q$ is fixed, this model chooses among the optimal cost vectors from model[model:IOclinpathway] to find one that maximizes the separation between the pathway costs of patients who survived from those who died.

<!-- chunk {"id": "body-0326", "role": "body", "section": "Clinical pathway concordance measurement", "weight": 1.0} -->

Finally, using the optimal cost vector $\btheta^*$ from problem[model:patientref],[chan2022inverse] construct a concordance metric $\omega \in $ as follows: \omega(\hat\bx) = 1 - \frac{\btheta^{*\top}\hat\bx - \btheta^{*\top}\bx^*}{M(\hat\bx) - \btheta^{*\top}\hat\bx}.

<!-- chunk {"id": "body-0327", "role": "body", "section": "Clinical pathway concordance measurement", "weight": 1.0} -->

This metric measures the cost difference between a patient pathway $\hat\bx$ and a shortest path $\bx^*$, and normalizes it based on the cost difference between the longest walk with the same number steps as $\hat\bx$ (denoted $M(\hat\bx)$) and a shortest path. Using $\omega$, it becomes possible to rigorously score any patient pathway $\bhx$against the clinical pathways. Using a real dataset of colon cancer patients, the authors establish a statistically significant association between concordance and mortality, even after adjusting for patient covariates, which supports the clinical meaningfulness of the metric.

<!-- chunk {"id": "body-0328", "role": "body", "section": "Clinical pathway concordance measurement", "weight": 1.0} -->

An extension that has not been considered yet is the incorporate of cost of care into the concordance measurement. This can be done by modifying formulation [model:patientref]to favor patient pathways that are lower cost (in terms of real dollar amounts of imaging, treatment, diagnostic tests, etc.), rather than separating patients by their survival outcome.

<!-- chunk {"id": "body-0329", "role": "body", "section": "Radiation therapy treatment planning", "weight": 1.0} -->

The optimization problem contains multiple objectives used to balance multiple (potentially dozens) conflicting objectives, such as escalating dose to the tumor while minimizing dose to the healthy organs. The overall objective is formed by taking a weighted combination of the various objectives $f(\bx) = \sum_{k=1}^K \theta_k f_k(\bx)$ where $\theta_k$ is the weight of the $k$-th objective $f_k(\bx)$ for $k \in \{1, \dots, K\}$. Assuming linear objectives (i.e., $f_j(\bx) = \bc^{j\top}\bx$), the objective function can be rewritten as $\btheta^\top \bC \bx$, where the $j$-th row of $\bC$ is $\bc^j$.

<!-- chunk {"id": "body-0330", "role": "body", "section": "Radiation therapy treatment planning", "weight": 1.0} -->

The traditional clinical procedure of designing treatments involves manually selecting the objective function weights, solving the optimization problem, evaluating the treatment using several quantitative and qualitative metrics, and then iterating, if needed. As an alternative, inverse optimization can infer appropriate weights from historical treatments [chan2014generalized]. We present a simplified version of this model below. $\mathcal{B}$ be the sent of beamlets and $x_b$ be the intensity of beamlet $b$. Let $\mathcal{T}$ be the set of voxels (volumetric pixels) in the tumor and $\mathcal{V}$ be the set of all voxels. Let $\mathcal{O}_k$ be the set of healthy voxels corresponding to the $k$-th objective.

<!-- chunk {"id": "body-0331", "role": "body", "section": "Radiation therapy treatment planning", "weight": 1.0} -->

Each objective $f_k(\bx)$ penalizes the total dose delivered above a threshold $\tau^k_v$ for each voxel $v$, i.e., f_k(\bx):= \sum_{v \in \mathcal{O}_k}\max\left\{0, \sum_{b \in \mathcal{B}} D_{v,b}x_b - \tau^k_v\right\}, where $D_{v,b}$ is the dose deposited to voxel $v$ by unit intensity of beamlet $b$.

<!-- chunk {"id": "body-0332", "role": "body", "section": "Radiation therapy treatment planning", "weight": 1.0} -->

The complete formulation of the forward problem is \underset{\bx}{\text{min}} & \quad \sum_{k=1}^K \theta_k \sum_{v \in \mathcal{O}_k}\max\left\{0, \sum_{b \in \mathcal{B}} D_{v,b}x_b - \tau^k_v\right\} \\\textrm{s.t.} & \quad \sum_{b \in \mathcal{B}} D_{v,b}x_b \ge l_v, \quad \forall v \in \mathcal{T}, \\& \quad \sum_{b \in \mathcal{B}} D_{v,b} x_b \le u_v, \quad \forall v \in \mathcal{V}, \\where $l_v$ and $u_v$ denote lower and upper bound constraints on the tumor and healthy voxels, respectively, and $\mX$describes a set of linear constraints on the intensity values including

<!-- chunk {"id": "body-0333", "role": "body", "section": "Radiation therapy treatment planning", "weight": 1.0} -->

Both the Absolute and Relative Sub-optimality loss functions (see Sections [subsubsec:abs\_suboptimality] and [subsubsec:data-driven\_IO\_rdg]) have been used in the literature in the inverse formulation for the above forward problem.
