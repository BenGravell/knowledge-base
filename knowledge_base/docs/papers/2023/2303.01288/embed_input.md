<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Statistical Linearization for Robust Motion Planning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The goal of robust motion planning consists of designing open-loop controls which optimally steer a system to a specific target region while mitigating uncertainties and disturbances which affect the dynamics. Recently, stochastic optimal control has enabled particularly accurate formulations of the problem. Nevertheless, despite interesting progresses, these problem formulations still require expensive numerical computations. In this paper, we start bridging this gap by leveraging statistical linearization. Specifically, through statistical linearization we reformulate the robust motion planning problem as a simpler deterministic optimal control problem subject to additional constraints. We rigorously justify our method by providing estimates of the approximation error, as well as some controllability results for the new constrained deterministic formulation. Finally, we apply our method to the powered descent of a space vehicle, showcasing the consistency and efficiency of our approach through numerical experiments.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning is a powerful tool for motion design, with important applications in engineering and biology. Its main objective consists of computing an open-loop control which steers a given system to some desired target, while possibly optimizing performance criteria, e.g., minimizing effort. Specifically, motion planning becomes essential when no feedback-based control strategies are available, for instance because either no measurements are available or some states are not observable, as it happens in particular in the context of fast biological movements. In addition, motion planning is particularly beneficial to compute reference strategies low-level controllers track at online later stages, an approach which is of common use in robotics and aerospace. In all the aforementioned tasks, uncertainties ranging from measurement errors to unknown parameters or external perturbations may hinder the reliability of the computed control strategies. Methods taking these uncertainties into account are referred to as robust motion planning.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The existing robust motion planning methods can be categorized into three groups. In the first group, the so-called robust set methods tackle uncertainty by representing the states of the system through sets which contain all the possible outcomes. In particular, these paradigms build on interval analysis, and they have been successfully applied in both robotics and aerospace. Similarly, we find works which leverage positively invariant sets to generate safe trajectories. The common drawback of this class of methods is that they generally produce either conservative solutions or computationally expensive algorithms. The second group of works includes methods that reduce the sensitivity with respect to uncertain parameters of the computed control strategies for specific metrics. For instance, devise algorithms which minimize the sensitivity of the performance criteria which are to optimize. Alternatively, the algorithm in minimizes the sensitivity of the final state when controlling a robotic arm. Finally, models the dynamics of the sensitivity and minimizes the latter via an optimal control approach. Note that methods designed to treat uncertain parameters are surveyed. These first two classes of methods are well suited to handle parameter uncertainties, but random perturbations of the dynamics are better addressed by the third and last group of works which leverage the so called stochastic methods.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

More specifically, stochastic methods ensure robustness with respect to uncertain outcomes by reducing the corresponding covariance. Notably, has first provided the theoretical solution to the problem of minimizing the variance of the cost of an LQ problem under disturbances on the inputs. On the other hand, and propose analysis for exact covariance steering. Finally, achieves covariance minimization through penalization of the covariance of the final state within the cost, with the help of information matrices. Nevertheless, despite their accuracy, stochastic methods generally suffer from expensive numerical computations (except maybe for the linear quadratic case). Moreover, most of the existing methods have been tailored to specific applications, therefore we may claim there is no systematic methodology for robust motion planning using the stochastic modeling.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose a paradigm for robust motion planning which methodologically belongs to the aforementioned third group of works, and which in particular leverages stochastic differential equations to model uncertainty essentially along two main steps. First, as presented, we model the motion planning problem through a stochastic open-loop optimal control problem where the state covariance is penalized in the cost to ensure robustness. Then, we approximate this latter stochastic formulation through an appropriate deterministic optimal control problem whose state variables are the first two moments of the original stochastic state, i.e., its mean and covariance. These mean and covariance are efficiently computed thanks to statistical linearization, which essentially boils down to approximating the distribution of the original stochastic state through a Gaussian distribution. Statistical linearization methods have been successfully used for decades, especially for applications in mechanical. In addition, recently showed statistical linearization may be beneficially leveraged for variational inference. Despite its sound numerical performance, the theoretical well-posedness of statistical linearization still remains an open question.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Specifically, although accessibility properties of statistical linearization have already been preliminary studied, thus motivating its use for approximate covariance steering, the fidelity of approximations stemming from statistical linearization still requires investigation. In this paper, we start bridging this gap by computing estimates of the approximation error which is generated by statistical linearization. We additionally study the controllability of statistical linearization when accuracy constraints are imposed.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To showcase the validity of our theoretical findings, we solve a robust motion planning problem for the powered descent of a space vehicle. In the recent literature, the resulting optimal control problem has almost exclusively been studied in deterministic settings, i.e., uncertainties have not so far been considered. For this deterministic setting, theoretical analysis shows that the optimal control has generally a Max-Min-Max form, a control law which has been shown to suffer from lack of robustness with respect to uncertainties and disturbances. Therefore, infusing robustness with respect to uncertainty in the aforementioned optimal control problem formulation is crucial to ensure reliability in applications which are subject to high performance criteria. To the best of our knowledge, one of the first work addressing uncertainty for the powered descent of a space vehicle is, in which the authors make use of multi-objective optimization to minimize fuel consumption and state sensitivities at the same time. This strategy unfortunately increases the number of state variables by the square of the dimension of the state, therefore hindering computational performance. To reduce computational burden, in the more recent work the first two moments of the state variables are controlled via two separated deterministic problems: a mean steering problem and a covariance steering problem.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Nevertheless, the aforementioned robust motion planning methods lack justification of well-posedness, as well as analysis of the accuracy of the corresponding approximations. We fill this gap by applying our robust motion planning method for the powered descent of a space vehicle which explicitly includes modeling of environmental and system uncertainties, such as aerodynamic effects, parameter uncertainties, and measurement errors. We study the accessibility of the statistically linearized dynamics under both open-loop and partial feedback control laws, and we propose modelization for actuator limits in a stochastic setting. Finally, numerical results are provided to illustrate the consistency of the approach.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper is organized as follows. In Section 2, we formulate the robust motion planning problem and propose an approach which leverage statistical linearization to simplify it. Then, in Section 3 we compute estimates for the error induced by statistical linearization and we study the controllability of the approximated robust motion planning problem under new feasibility constraints which make statistical linearization well-posed. Finally, in Section 4 we apply our method to the powered descent of a space vehicle, providing numerical results which sustain our theoretical findings.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Modelling robustness via stochastic open-loop optimal control", "weight": 1.0} -->

As we mentioned in the introduction, we start by modeling a motion planning problem via a deterministic control system

<!-- chunk {"id": "body-0012", "role": "body", "section": "Modelling robustness via stochastic open-loop optimal control", "weight": 1.0} -->

where $x \in {\mathbb{R}}^{n}$ is the state variable and $u \in \mathcal{U} \subset {\mathbb{R}}^{k}$ is the control variable. We aim finding an open-loop control law $u{(t)}$, $t \in {\lbrack 0,t_{f}\rbrack}$, which steers the system from an initial state $x^{0}$ to a target set $\mathcal{S} \subset {\mathbb{R}}^{n}$, while minimizing a certain cost. The motion planning problem then amounts to the following optimal control problem (note that the final time $t_{f}$ below may be free or fixed depending on the considered problem).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem 1 (Deterministic motion planning)", "weight": 1.0} -->

At this step, let us further assume that the system is affected by uncertain perturbations. We consider two kind of perturbations here: 1) uncertainties on the initial state and 2) noise on the dynamics. We model the first uncertainties by taking a random variable $x^{0}$ as initial state; the second ones are modelled by replacing the initial control system with an Itô-type stochastic control system

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem 1 (Deterministic motion planning)", "weight": 1.0} -->

where $W_{t}$ is a $d$-dimensional Wiener process and $g{(x,u)}$ is a dispersion matrix. The quantities $x{(t_{f})}$ and $C{(u)}$ are now random variables, and hence the corresponding terminal conditions and cost should be expressed via appropriate expectations.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem 1 (Deterministic motion planning)", "weight": 1.0} -->

In this setting the sample trajectories are dispersed around the mean trajectory, and the dispersion may increase along these trajectories. Consequently the final states of sample trajectories may lie far from the target set $\mathcal{S}$. It is then natural to seek robustness by penalizing the norm of the covariance ${\mathbf{P}}{(t)}$ of the state $x_{t}$ in the cost. For this, let us introduce two non-negative symmetric matrices ${\overline{Q}}_{f}$ and $\overline{Q}$ which quantify penalization of the final covariance and of the covariance along trajectories, respectively. We thus obtain a first way of constructing a robust open-loop control strategy as solution to the following stochastic open-loop optimal control problem.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem 2 (Robust motion planning by stochastic optimal control)", "weight": 1.0} -->

Solving such a stochastic optimal control problem is computationally difficult and few theoretical and numerical methods exist. However since mean and covariance play a major role in the above problem, we can adopt the approach presented, which is based on statistical linearization.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem 2 (Robust motion planning by stochastic optimal control)", "weight": 1.0} -->

Importantly, the method requires that the deterministic cost $C$ in Problem 1. ‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning") has a quadratic dependence with respect to the state variables, so from now on we assume that the following property holds.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem 2 (Robust motion planning by stochastic optimal control)", "weight": 1.0} -->

The terminal cost $\psi$ and the infinitesimal cost $L$ in Problem 1. ‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning") are quadratic functions (non necessarily homogeneous) of $x$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem 2 (Robust motion planning by stochastic optimal control)", "weight": 1.0} -->

Assumption (H) guarantees that the expectation of the cost $C$ in Problem 1. ‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning") depends on $\mathbf{m}$ and $\mathbf{P}$ uniquely. Indeed, by denoting with $Q_{\psi}$ and $Q_{L}{(u)}$ the symmetric matrices which represent the homogeneous quadratic parts of $\psi$ and $L$ respectively, there holds

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem 2 (Robust motion planning by stochastic optimal control)", "weight": 1.0} -->

Therefore, we propose to compute an open-loop control for the robust motion planning Problem 2. ‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning") by rather solving the following deterministic optimal control problem (below, ${\mathbf{m}}^{0}$ and ${\mathbf{P}}^{0}$ denote the mean and covariance of the random variable $x^{0}$, respectively).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 1", "weight": 1.0} -->

the mean variable (equation in $m$) and the covariance variable (equation in $P$), which measures the dispersion of the process $x_{t}$, are decoupled;

<!-- chunk {"id": "body-0022", "role": "body", "section": "Remark 1", "weight": 1.0} -->

the resulting trajectory of the mean $m$ corresponds to the planned trajectory for the deterministic system.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Despite its simplicity, the formulation in Problem 3. ‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning") raises several questions, both from theoretical and practical point of view. First, in which sense is the solution to Problem 3. ‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning") an approximation of the solution to Problem 2. ‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning")? We answer this question in Section 3.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Second, is this approach relevant for robustness, in particular is the use of statistical linearization sufficient to reduce the covariance? The latter question boils down to study the controllability properties of the statistical linearization, i.e., the subject of our paper. From a practical point of view, we show the efficiency which is offered by solving Problem 3. ‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning") by studying the example of the landing of a reusable launcher in Section 4.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Justification of statistical linearization", "weight": 1.0} -->

In this section, our objective consists of endowing statistical linearization with guarantees of well-posedness, and for this we aim at showing two important properties under mild assumptions. First, we compute estimates which quantify constraints for the approximation error between the trajectories of the stochastic control system and those of its statistical linearization (11. ‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning")). In short, this property ensures statistical linearization represents a well-posed approximation of mean and covariance of a stochastic control system as soon as the variance is forced to take small values. As a second result, we show that statistical linearization (11. ‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning")) is controllable when the aforementioned approximation constraints are considered, in the specific case of control-linear systems, a fairly general class of control systems widely used in application. This latter result ensures that, under additional approximation constraints, Problem 3.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Justification of statistical linearization", "weight": 1.0} -->

‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning") is feasible, justifying the search of an optimal solution, and their solution trajectories are close to the trajectories of the original stochastic control system.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Estimates for statistical linearization", "weight": 1.0} -->

In this section, we leverage the following arguably mild assumption.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

the dispersion matrix does not depend on the state variable, i.e., it holds that ${g{(x,u)}} = {g{(u)}}$, for every ${(x,u)} \in {{\mathbb{R}}^{n} \times \mathcal{U}}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Note that, on the one hand the first condition in Assumption 1 is standard, in that it is generally required, among other conditions, to ensure existence and uniqueness for solutions to. Also, this condition trivially holds for vector field $f$ with compact support (in which case the function $\varphi$ is just a constant), a property often implicitly assumed in the models. On the other hand, the second condition in Assumption 1 is for instance satisfied as soon as uncertainty (specifically, $g{(x_{t},{u{(t)}})}dW_{t}$ in ) originates from some uniformly recurrent noise, such as system measurement errors, uncertain weather conditions, etc.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Before establishing estimates of the error between the trajectories of the stochastic control system and those of its statistical linearization, we note that under Assumption 1 the original stochastic control system takes the form

<!-- chunk {"id": "body-0031", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

and the statistical linearization of now writes

<!-- chunk {"id": "body-0032", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Error estimates between the trajectories of the stochastic control system and those of its statistical linearization are given below. Let us first fix some notation. Given a control law $u \in {L^{2}{({\lbrack 0,t_{f}\rbrack},\mathcal{U})}}$ and a random variable $x^{0}$ with mean and covariance $({\mathbf{m}}^{0},{\mathbf{P}}^{0})$, we denote by $({\mathbf{m}},{\mathbf{P}})$ the mean and covariance of the solutions to with initial condition $x^{0}$ and control $u$, whereas $(m,P)$ denotes the trajectories solutions to with initial condition $({\mathbf{m}}^{0},{\mathbf{P}}^{0})$ and control $u$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 2", "weight": 1.0} -->

The error on the mean has an exponent 2 for homogeneity reasons, the covariance being homogeneous to the square of the mean.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Controllability of Problem 3. ‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning\") under approximation constraints", "weight": 1.0} -->

Proposition 1 quantitatively estimates the well-posedness of statistical linearization: if one is capable of controlling in such a way that the left-hand side of takes small values, then the solutions to the statistical linearization well-approximate, i.e., with respect to second-order moments, the solutions to the original stochastic control system. These latter requirements represent new constraints to which Problem 3. ‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning") should be subject, to compute meaningful solutions to Problem 2. ‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning").

<!-- chunk {"id": "body-0035", "role": "body", "section": "Controllability of Problem 3. ‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning\") under approximation constraints", "weight": 1.0} -->

However the aforementioned constraints entail controllability issues. Indeed Problem 3. ‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning") consists of a minimization problem on the set of $L^{2}$ controls whose associated trajectory satisfies the terminal condition ${m{(t_{f})}} \in \mathcal{S}$. The fact that this set of controls is non-empty can be guaranteed by usual controllability conditions on the dynamics $f{(x,u)}$. The question is whether this set of admissible control remains non-empty when adding the new constraints we previously introduced. The aim of this section is to answer this question.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Controllability of Problem 3. ‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning\") under approximation constraints", "weight": 1.0} -->

Let us first formalize the setting properly. For this, fix $t_{f} > 0$, and choose a vector $m^{0} \in {\mathbb{R}}^{n}$ and a non-nnegative symmetric matrix $P^{0}$. Given a control $u \in {L^{2}{({\lbrack 0,t_{f}\rbrack},{\mathbb{R}}^{k})}}$, we denote by $(m_{u},P_{u})$ the solution to (11. ‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning")) with initial condition $(m^{0},P^{0})$ and control $u$. Assume Assumption 1 is satisfied and let $\alpha$ be the increasing function stemming from Proposition 1.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Controllability of Problem 3. ‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning\") under approximation constraints", "weight": 1.0} -->

As a direct corollary of Proposition 1, ${\mathbb{U}}{(\varepsilon,m^{0},P^{0})}$ is a class of control guaranteeing that the statistical linearization approximates to within $\varepsilon$ the solutions to the original stochastic control system.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

the vector fields satisfy the Lie bracket generating condition

<!-- chunk {"id": "body-0039", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Note that the above assumption implies that Assumption 1 is satisfied with ${\varphi{(r)}} = {Lr}$. Assumption 2 may seem rather restrictive, in particular for what concerns the hypothesis that the dynamics is control-linear and the dispersion is constant. However this setting is encountered in many control applications, often in the case of simplification of more complex problems. Also, the Lie bracket generating condition is generic, i.e., it is satisfied by almost every tuple of vector fields $(f_{1},\ldots,f_{k})$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Under this assumption we show that we have controllability for the variable $m$ in any class ${\mathbb{U}}{(\varepsilon,m^{0},P^{0})}$ provided $P^{0}$ is small enough.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Note that when the initial condition $x^{0}$ is deterministic, the initial covariance $P^{0}$ is zero. The proposition then implies that, for every $m^{0},m^{f}$ and $\varepsilon$, the corresponding set ${\mathbb{U}}{(\varepsilon,m^{0},0)}$ contains controls joining $m^{0}$ to $m^{f}$. This case is important for applications.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Application: motion planning of the powered descent of a space vehicle", "weight": 1.0} -->

In this section, we present an application of our method to the problem of the powered descent of a space vehicle. In particular, we show the interest of our robust motion planning approach to optimize landing trajectories under uncertainties. Landing trajectories are often performed by vertical landing, whose last stage, the powered descent, is particularly challenging and requires high accuracy. To achieve this, the usual strategy is to optimize a reference trajectory in the first place that will be tracked during the powered descent thanks to a feedback control. Up to now, the trajectory optimization has been done in general in a deterministic optimal control framework, without considering uncertainties. For instance, has first introduced the landing trajectory generation problem as a minimal-fuel optimal control problem, and since then, a wide literature has investigated landing problems. Existing results state that the optimal control has generally a Max-Min-Max form, meaning that its norm switches at most twice between its inferior and superior bounds. This control is particularly sensitive to uncertainties, hence the interest in developing robust methods for which are subject to high performance criteria.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Framework", "weight": 1.0} -->

For the sake of simplicity, we consider a two dimensional formulation only, we refer the reader to for a discussion on the complete three dimensional model. In this setting, the state $x = {(r,v,\mu)} \in {\mathbb{R}}^{5}$ is composed by the position $r = {(y,z)} \in {\mathbb{R}}^{2}$, the velocity $v = {(v_{y},v_{z})} \in {\mathbb{R}}^{2}$, and the mass $\mu \in {\mathbb{R}}$, while the control $u = {(u_{y},u_{z})}$ represents the two dimensional thrust.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Framework", "weight": 1.0} -->

Ignoring disturbances and uncertainties, the dynamics of the system, referred later as the *unperturbed dynamics*, is

<!-- chunk {"id": "body-0045", "role": "body", "section": "Framework", "weight": 1.0} -->

where the maximal thrust $T$, the mass flow rate $q$ of the engine, and the gravitational acceleration $g_{0}$ are positive constants. Moreover, the thrust is subject to the physical limits of the actuators, which can be modeled by upper and lower bounds on the control norm as follows

<!-- chunk {"id": "body-0046", "role": "body", "section": "Framework", "weight": 1.0} -->

The goal of the powered descent is to reach the target $\mathcal{S} = {\{{{r = 0},{v = 0}}\}}$ from the initial state $x{}$. To save the largest amount of fuel in the vehicle tanks, the motion planning problem takes the form of Problem 1.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Framework", "weight": 1.0} -->

In addition, the system is subject to at least two types of uncertainties. First, several effects such as aerodynamic forces are usually neglected from the dynamics model for convenience. Therefore, we propose to model these neglected quantities through an additive noise on the acceleration (i.e., the derivative of $v$). As a result, we write the dynamics as

<!-- chunk {"id": "body-0048", "role": "body", "section": "Framework", "weight": 1.0} -->

where $W_{t}$ is a one-dimensional Brownian motion and $g = {(0,0,\sigma_{y},\sigma_{z},0)}$ is a constant vector, $\sigma_{y},\sigma_{z}$ being nonnegative constants. Second, the initial state $x{}$ is known only up to measurement errors. We model these errors by considering $x{}$ as a random variable $x^{0}$ with normal density $\mathcal{N}{({\mathbf{m}}^{0},{\mathbf{P}}^{0})}$. Finally, we formulate the robust motion planning of the powered descent as a problem in the form of Problem 2. ‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning").

<!-- chunk {"id": "body-0049", "role": "body", "section": "Direct statistical linearization", "weight": 1.0} -->

Following the approach described in Section 2, we solve a problem in the form of Problem 3. ‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning") rather than one in the form of Problem 2. ‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning"). In particular, we look for a solution of the robust powered descent problem as a control law $u$ which minimizes the following problem (where we write $m$ as $m = {(m_{r},m_{v},m_{\mu})} \in {{\mathbb{R}}^{2} \times {\mathbb{R}}^{2} \times {\mathbb{R}}}$).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Problem 4", "weight": 1.0} -->

Unfortunately, this formulation can not be leveraged because the corresponding statistical linearization is not controllable, in the sense that it does not enjoy accessibility property. In particular, there is no reason for the solution of Problem 4 to perform the powered descent with a small final covariance.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Problem 4", "weight": 1.0} -->

Let us better elucidate this "non controllability" property. We introduce first some notations in a general setting. Given a dynamical system of the form on ${\mathbb{R}}^{n}$, denote by ${\mathcal{f}} = {\{{{\mathcal{f}}{({\mathcal{x}},{\mathcal{u}})}}:{{\mathcal{u}} \in \mathcal{U}}\}}$ the associated family of vector fields, and consider the following linear space of vector fields,

<!-- chunk {"id": "body-0052", "role": "body", "section": "Problem 4", "weight": 1.0} -->

then the statistical linearization (11. ‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning")) defined by $f{(x,u)}$ and any dispersion $g$ is accessible from any point in an open and dense subset of ${{\mathbb{R}}^{n} \times \text{Sym}_{+}}{({\mathbb{R}}^{n})}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Problem 4", "weight": 1.0} -->

Note that in the present application this condition is never satisfied.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Remark 4", "weight": 1.0} -->

The sufficient accessibility condition is not satisfied. This does not prove that the statistically linearized system (11. ‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning")) is not accessible, since the condition tested is only a sufficient one. However, the lack of accessibility is expected because here the vector fields in $\mathcal{f}$ are analytic vector fields, and in this case the Lie-based accessibility sufficient conditions are merely necessary (see ). In a more informal way, notice that the dynamics is almost linear and the statistical linearizations of linear systems are never accessible. Finally, our numerical solutions of the robust motion planning problem subject to dynamics (11. ‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning")) (such as those presented on Figure 2) do not succeed in reducing the covariance, which tends to confirm this non accessibility property.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Adding feedback into the model", "weight": 1.0} -->

We have seen in the previous subsection that our method fails to provide an open-loop control that is satisfactory in terms of robustness. Nevertheless, some measurements, such as for position $r$ and velocity $v$, are available during the powered descent, and we can include those into a feedback control. Note that, on the one hand, measurements of mass are generally not available and, on the other hand, this quantity is in general not observable, which in turn hinders the design of feedback controls that are also functions of the mass.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Adding feedback into the model", "weight": 1.0} -->

Therefore, we replace the control variable $u$ in by a function $u_{FB}$ of $\overline{x} = {(r,v)}$ which depends on some appropriate parameters $\nu$, and in turn we consider $\nu$ as the new control variable. When including this partial feedback controls, the launch vehicle unperturbed dynamics writes as

<!-- chunk {"id": "body-0057", "role": "body", "section": "Adding feedback into the model", "weight": 1.0} -->

Keeping the same dispersion term $g$ as, we obtain a new stochastic model for the dynamics,

<!-- chunk {"id": "body-0058", "role": "body", "section": "Adding feedback into the model", "weight": 1.0} -->

Returning to the physics of the problem, let us remark that the control $u$ is provided by two actuators, one for the norm of $u$, the other one for its direction, so that

<!-- chunk {"id": "body-0059", "role": "body", "section": "Adding feedback into the model", "weight": 1.0} -->

where $u_{\rho} = {\| u\|}$ and $u_{\theta} \in {\lbrack{- \pi},\pi)}$. Restricting ourselves to linear functions of $\overline{x}$, we write the feedback control as

<!-- chunk {"id": "body-0060", "role": "body", "section": "Adding feedback into the model", "weight": 1.0} -->

Note that the statistical linearization of the system defined by writes as

<!-- chunk {"id": "body-0061", "role": "body", "section": "Adding feedback into the model", "weight": 1.0} -->

and we checked with the help of a formal calculation software that, unlike in the case of the statistical linearization of, this new system satisfies the sufficient condition for accessibility, i.e. that, denoting by ${\mathcal{f}}_{\mathcal{F}\mathcal{B}}$ the family of all vector fields $f_{FB}{( \cdot,\nu)}$, there holds

<!-- chunk {"id": "body-0062", "role": "body", "section": "Adding actuator limits to the model", "weight": 1.0} -->

In the dynamics, the control of the actuators $u_{FB}{(x_{t},{\nu{(t)}})}$ becomes a stochastic process, therefore imposing $u_{min} \leq {\| u_{FB}\|} \leq u_{max}$ is not possible. In turn, the physical limit of the actuators have to be taken into account differently in the model, and we propose two independent ways to handle them.

<!-- chunk {"id": "body-0063", "role": "body", "section": "First approach: saturation modelling", "weight": 1.0} -->

The first approach consists in encoding the physical limits of the actuators directly in the dynamic model. This can be achieved by using a saturation function in the model, which can be given as follows: for real numbers $a < b$, consider a function ${sat}_{a}^{b}$ such that ${{sat}_{a}^{b}{(s)}} \in {\lbrack a,b\rbrack}$ for every $s \in {\mathbb{R}}$. Then, using the notation of the control introduced, we replace the original unperturbed dynamics $f{(x,u)}$ by

<!-- chunk {"id": "body-0064", "role": "body", "section": "First approach: saturation modelling", "weight": 1.0} -->

Assuming that ${sat}_{a}^{b}$ is a smooth function, we can compute the statistical linearization of the saturated feedback dynamics as

<!-- chunk {"id": "body-0065", "role": "body", "section": "First approach: saturation modelling", "weight": 1.0} -->

Following our previous discussion, we add the aforementioned control constraints to Problem 3. ‣ 2 Modelling robustness via stochastic open-loop optimal control ‣ Statistical Linearization for Robust Motion Planning"), obtaining the following robust motion planning problem.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Note that the smoothness of ${sat}_{a}^{b}$ is required in order to use statistical linearization. Different possibilities exist for the choice of a smooth saturation function, e.g., the hyperbolic tangent function or the exact (non smooth) saturation function defined by ${{\overline{sat}}_{a}^{b}{(s)}} = s$ if $s \in {\lbrack a,b\rbrack}$, $= a$ if $s \leq a$, and $= b$ if $s \geq b$ (we use this latter in our simulation). Note that this function can be written as

<!-- chunk {"id": "body-0067", "role": "body", "section": "Remark 5", "weight": 1.0} -->

We then choose a small parameter $\epsilon$ and define ${sat}_{a}^{b}$ by replacing the absolute values $|s|$ by $\sqrt{s^{2} + \epsilon^{2}}$ in the expression above. The smaller $\epsilon$ is, the closer the approximation to the exact saturation function is (see Figure 1).

<!-- chunk {"id": "body-0068", "role": "body", "section": "Second approach: chance constraints", "weight": 1.0} -->

The second approach consists in requiring that the inequality constraint be satisfied with a probability greater than a certain given threshold. Let us explain why such chance constraint is well-suited for the statistical linearization approach. Indeed, consider a chance constraint such as

<!-- chunk {"id": "body-0069", "role": "body", "section": "Second approach: chance constraints", "weight": 1.0} -->

where $a \in {\mathbb{R}}^{5}$, $c \in {\mathbb{R}}$, and $p \in {}$ is the chosen probability threshold. In this formula the probability $\Pr$ is supposed to be computed with respect to the probability distribution of the process $x_{t}$ solution of. Now, the main principle underneath the method of statistical linearization consists of approximating the distribution of $x_{t}$ by rather a normal distribution whose mean and covariance are the state variables $m{(t)}$ and $P{(t)}$ of the statistical linearization (see for explanations on this approximation). For such a distribution the chance constraint writes as

<!-- chunk {"id": "body-0070", "role": "body", "section": "Second approach: chance constraints", "weight": 1.0} -->

where $\Psi^{- 1}$ is the inverse cumulative distribution function of the normal distribution. Thus, the chance constraint on the stochastic process is transformed into a state constraint in the setting of the statistical linearization.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Second approach: chance constraints", "weight": 1.0} -->

Following this approach, we reformulate the norm constraint on $u_{FB}$ as the following chance constraint on the solutions of: for every $t \in {\lbrack 0,t_{f}\rbrack}$, there holds

<!-- chunk {"id": "body-0072", "role": "body", "section": "Second approach: chance constraints", "weight": 1.0} -->

where $p$ is the chosen threshold. By replacing these constraints by state constraints on the statistical linearization, we finally formulate the following robust motion planning problem.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Problem 6 (Chance constrained robust motion planning)", "weight": 1.0} -->

where $\overline{m}$ denotes the first four components of $m$ and $\overline{P}$ the matrix formed by the first four lines and columns of $P$;

<!-- chunk {"id": "body-0074", "role": "body", "section": "Problem 6 (Chance constrained robust motion planning)", "weight": 1.0} -->

Note that this formulation may be numerically expensive to handle because additional mixed constraints on both mean and covariance are considered.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Remark 6", "weight": 1.0} -->

The solution $\nu{( \cdot )}$ of the above problem guarantees that the constraint $u_{min} \leq {\| u_{FB}\|} \leq u_{max}$ is satisfied only in probability. Thus when using this control law $\nu{( \cdot )}$ for simulating the stochastic model, one has to model the system including saturation (such as the function $f_{FB}^{sat}$ defined in the first approach) to force the physical limits of the actuator.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Numerical results", "weight": 1.0} -->

This section presents some numerical results to illustrate solutions of Problems 4--6. ‣ Second approach: chance constraints ‣ 4.3.2 Adding actuator limits to the model ‣ 4.3 Statistical linearization through partial feedback ‣ 4 Application: motion planning of the powered descent of a space vehicle ‣ Statistical Linearization for Robust Motion Planning"). Calculations are based on a direct method which makes use of a time discretization of the considered optimal control problems, using a grid of $150$ nodes and the CasADi toolbox (combined with the IPOPT solver). The computed open-loop optimal control is then used as an input to simulate the stochastic dynamic model with random uncertainties. When performing the simulations, actuator limits are forced by applying a saturation on the input control following the exact expression.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Numerical results", "weight": 1.0} -->

The parameters in the dynamics and the simulation settings are specified in Table 1. The initial mean state is given by $(r^{0},v^{0},m^{0})$. We assume that measurements of the initial position and velocity are quite accurate, while the initial mass is imprecisely known, hence the setting of $P^{0}$. Along the trajectory, the dynamics is subject to perturbations due to aerodynamic effects, modeled by white noises of standard deviation depending on the mass $g = \frac{\sigma}{\mu}$. Moreover, the nonnegative symmetric matrices $Q$ and $Q_{f}$ are fixed to the same value for the three considered problems. We do not penalize the mass covariance, since position and velocity are the quantities of interest to attain precision landing and ensure security.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Numerical results", "weight": 1.0} -->

The shape of the control norm $\| u\|$ looks like a Max-Min-Max control to which margins would have been added with respect to the real actuator limits, $u_{min}$ and $u_{max}$. We observe that the dispersion is controlled all along the trajectory, as required. The final state standard deviation is $\overline{P}{(t_{f})} = {(5.2m,5.8m,0.5m/s,}$ $0.5m/s)$, which is smaller than the initial covariance. The final time is $34.4s$, which is much higher than the final time of the previous setting. This can be explained as follows. Without the accessibility property, reducing the final time represents the only way to minimize the final covariance. On the contrary, thanks to partial feedback the control may be kept closer to the fuel-optimal solution while providing robustness.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Numerical results", "weight": 1.0} -->

Finally, the fourth set of plots (Figure 5) shows the relative error stemming from statistical linearization. Those are obtained when simulating the saturated feedback linearized dynamics using the control solution of Problem 5. ‣ First approach: saturation modelling ‣ 4.3.2 Adding actuator limits to the model ‣ 4.3 Statistical linearization through partial feedback ‣ 4 Application: motion planning of the powered descent of a space vehicle ‣ Statistical Linearization for Robust Motion Planning"). Approximation of the true mean and covariance are obtained via Monte-Carlo estimates with $1000$ sample trajectories solutions to dynamics. Thus, since the errors on both mean and covariance remain bounded, we deduce that estimates of the statistical linearization are consistent.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Conclusion and perspectives", "weight": 1.5} -->

We presented a method for stochastic robust motion planning which leverages statistical linearization to approximate the original formulation with a deterministic optimal control problem on the mean and the covariance of the original state variables. We justify our work through appropriate theoretical bounds for the approximation error due to statistical linearization, and through numerical experiments on the powered descent of a space vehicle.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Conclusion and perspectives", "weight": 1.5} -->

We suggest three main future research directions. First, we will investigate extensions of our theoretical bounds for the approximation error due to statistical linearization to more general settings, e.g., to stochastic systems whose diffusion explicitly depends on the state variables. Second, we will consider extending our controllability results in Section 3.2 to settings which go beyond control-linear systems; one possible direct application of this latter result would encompass controllability of stochastic differential equations. Third, we will focus on applying our approach to other applications, such as stochastic robust motion planning of autonomous vehicles and space robots.
