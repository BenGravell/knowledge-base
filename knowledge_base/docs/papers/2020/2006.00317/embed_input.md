<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Control Design for Risk-Based Signal Temporal Logic Specifications

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a general framework for risk semantics on Signal Temporal Logic (STL) specifications for stochastic dynamical systems using axiomatic risk theory. We show that under our recursive risk semantics, risk constraints on STL formulas can be expressed in terms of risk constraints on atomic predicates. We then show how this allows a (stochastic) STL risk constraint to be transformed into a risk-tightened deterministic STL constraint on a related deterministic nominal system, enabling the application of existing STL methods. For affine predicate functions and a (coherent) Distributionally Robust Value at Risk measure, we show how risk constraints on atomic predicates can be reformulated as tightened deterministic affine constraints. We demonstrate the framework using a Model Predictive Control (MPC) design with an STL risk constraint.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

TEMPORAL logics allow to reason about temporal properties of systems and have traditionally been used in formal verification and model checking. More recently, temporal logics have also been used to impose highly expressive mission specifications on complex autonomous systems. For systems under linear temporal logic (LTL) and metric interval temporal logic (MITL) specifications, motion planning and control synthesis algorithms have been proposed.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Signal Temporal Logic (STL)* is a temporal logic interpreted over dense-time real-valued *(deterministic)* signals similar to MITL; it allows to additionally impose quantitative spatial properties by means of predicates that go beyond the abstract use of propositions in LTL and MITL. STL is hence more expressive and has been the focus of motion planning and control synthesis in areas such as robotics. In addition to the Boolean satisfaction relation given for LTL and MITL specifications, one can associate quantitative semantics with an STL specification that allow to reason about how robustly (severely) a specification is satisfied (violated). These quantitative semantics come in the form of the robustness degree and the robust semantics as well as space robustness, time robustness, and other variants.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Control of systems under STL specifications is inherently different compared to systems under LTL and MITL specifications, which is mainly based on abstractions and automata theory. For deterministic discrete-time systems, the authors in transform the STL specification into mixed-integer linear constraints and use Model Predictive Control (MPC) to deal with these constraints. Similarly, MPC has been employed by maximizing certain forms of the quantitative semantics associated with the STL specification at hand. These methods seem computationally more tractable than the approach presented in due to the use of smooth quantitative semantics. For deterministic continuous-time systems, uses timed-automata theory to decompose the STL specification into STL subspecifications that can be implemented by low-level feedback control laws, such as those. Learning-based methods for partially unknown systems have been presented.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A large fraction of the aforementioned research focuses on finite abstractions and/or *deterministic* systems. However, methodological advances are required to account for inherent uncertainties and high-dimensional continuous spaces in autonomous systems, especially due to *stochastic uncertainties* arising from the use of noisy data and learning components. Robust extensions of have been presented. Probabilistic notions of STL for stochastic systems have been presented. However, these formulations are either deterministic and based on a worst-case approach or utilize chance constraints, an incoherent measure of risk that can lead to undesirable decisions. Effective risk management in complex autonomous systems demands a more sophisticated approach to quantifying risks of specification violations. This motivates an axiomatic approach to risk, which has been advocated for in finance and more recently in robotics. Control under coherent risk measures has been considered. The extension to more complex and generic specifications, such as those captured by temporal logics, has however not been addressed.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions. 1) We present a general framework for defining risk semantics of STL specifications for *stochastic dynamical systems* using axiomatic risk theory. In particular, we compose risk metrics with predicate functions, which become stochastic in the considered setup. 2) We then recursively define risk semantics for Boolean and temporal STL operators. For a given STL specification, we show that these risk semantics can be expressed as risk constraints on predicate functions over certain time intervals. We then show how this allows such a risk constraint to be transformed into a risk-tightened deterministic STL constraint on a related deterministic nominal system. 3) For affine predicates and a coherent Distributionally Robust Value at Risk measure, we show how risk constraints on predicate functions can be explicitly reformulated as tightened deterministic affine constraints. 4) To demonstrate the framework, we use an MPC formulation to solve a risk-based STL control design problem, which we illustrate with numerical experiments.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Risk Measures and Axiomatic Risk Theory", "weight": 1.0} -->

A risk measure is a function that assigns a real number to a random variable, quantifying its size, typically related to one of its tails. More formally, let $(\Omega,\mathcal{F},{\mathbb{P}})$ be a probability space, where $\Omega$ is the sample space, $\mathcal{F}$ is a $\sigma$-algebra of subsets of $\Omega$, and $\mathbb{P}$ is a probability measure on $\mathcal{F}$. Let $\mathbf{X}$ denote a set of real-valued random variables on $\Omega$ (i.e., $X \in \mathbf{X}$ is a Borel measurable function $X:{\Omega\rightarrow{\mathbb{R}}}$). A risk measure is a function $\rho:{\mathbf{X}\rightarrow{{\mathbb{R}} \cup {\{{\pm \infty}\}}}}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Risk Measures and Axiomatic Risk Theory", "weight": 1.0} -->

In finance, elements of $\mathbf{X}$ represent the value of a financial position, and a risk measure quantifies the probability and severity of a financial loss. Here, elements of $\mathbf{X}$ will represent states of a stochastic system, and a *risk measure quantifies the probability and severity of violating a signal temporal logic specification*.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Risk Measures and Axiomatic Risk Theory", "weight": 1.0} -->

Risk Axioms. Effective quantitative risk management in emerging complex autonomous systems is a major challenge, which motivates an axiomatic approach to risk measures.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Risk Measures and Axiomatic Risk Theory", "weight": 1.0} -->

${{{\forall X},X_{1},X_{2}} \in \mathbf{X}},$ and ${{c,\beta} \in {\mathbb{R}}},{\beta \geq 0}$. A risk measure is called *coherent* if it satisfies all four of these axioms. It has been argued that these axioms constitute natural desirable properties for risk measures in complex systems. *Spectral* or *distortion risk measures* also satisfy

<!-- chunk {"id": "body-0012", "role": "body", "section": "Risk Measures and Axiomatic Risk Theory", "weight": 1.0} -->

and can be viewed as refinements of coherent risk measures.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Risk Measures and Axiomatic Risk Theory", "weight": 1.0} -->

Unfortunately, many widely used risk measures in robotics and engineering are not coherent, and can lead to serious miscalculations of risk, e.g., mean-variance and mean-standard-deviation fail to be monotone, and VaR lacks subadditivity. The widely used chance constraint in optimization models is closely related to VaR and has been used for notions of STL robustness for stochastic systems. We advocate for axiomatic risk theory with coherent risk as a more systematic and sophisticated approach to risk management for STL specifications in emerging safety-critical autonomous systems.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Risk Measures and Axiomatic Risk Theory", "weight": 1.0} -->

Distributional Robustness. Evaluating any of the above risk measures requires knowledge of the probability distribution of the associated random variable. In practice however, we are never given the probability distribution, only noisy data. Instead, we must estimate properties of the distribution from the noisy data, or make assumptions about the distribution. In the emerging area of distributionally robust optimization, this uncertainty in our knowledge of the probability distribution itself is explicitly accounted. Rather than assuming a single probability distribution, we instead work with *ambiguity sets* of distributions.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Risk Measures and Axiomatic Risk Theory", "weight": 1.0} -->

A risk measure and an ambiguity set can be combined to obtain distributionally robust (DR) risk measures: $\rho_{\text{DR}} = {\sup_{{\mathbb{P}} \in \mathcal{P}}{\rho{(X)}}}$. For example, DR-VaR, $\sup_{{\mathbb{P}} \in \mathcal{P}}{\text{VaR}_{\delta}{(X)}}$, with various moment-based ambiguity sets is a coherent risk measure.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Risk-Based Signal Temporal Logic", "weight": 1.0} -->

Traditionally, STL constraints are specified for *deterministic* dynamical systems. STL formulas are based on predicates $\pi \in {\{\top,\bot\}}$ where $\top$ and $\bot$ denote true and false, respectively, and are obtained from evaluating a predicate function $\alpha:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ such that $\pi = {\{{{\alpha{(x)}} \geq 0}\}}$, i.e., $\pi = \top$ if and only if ${\alpha{(x)}} \geq 0$ where $x \in {\mathbb{R}}$. A typical STL formula $\varphi$ is composed from logical and bounded-time temporal operators and can always be rewritten in *negation normal form* (also referred to as positive normal form in), where the negation operator appears only at the atomic predicate level.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Risk-Based Signal Temporal Logic", "weight": 1.0} -->

*Stochastic* systems require an alternative quantitative semantics. We denote a discrete-time finite-horizon *stochastic process* starting at time $t$ as ($\Xi_{N},t) = X_{t}X_{t + 1}\ldots X_{t + N}$ where $X_{i}$ is an ${\mathbb{R}}^{n}$-valued random variable from a set $\mathbf{X}$ of random variables that represents the *stochastic* system state at time $i$. Since the system state is stochastic, the question of $\Xi_{N}$ satisfying an STL formula is ill-posed, and the aforementioned Boolean semantics do not apply (notice that $\alpha{(X)}$ is a random variable). Instead, we quantify the risk of *violating* a specification by introducing a risk measure into STL formulas.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Risk-Based Signal Temporal Logic", "weight": 1.0} -->

(This contrasts with STL robustness measures, which quantify the *satisfaction* of a formula; it is more natural to consider the risk of violating a formula.) While there are several ways to define the risk of *violating* a formula $\mathcal{R}$, we choose to define the risk of violating an atomic predicate using the risk measures $\rho$ discussed in Section II and build up the STL risk-of-violation semantics recursively.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Control Design for Risk-Constrained STL", "weight": 1.0} -->

where $\Phi{(.,.)}$ is the state transition matrix defined as

<!-- chunk {"id": "body-0020", "role": "body", "section": "Control Design for Risk-Constrained STL", "weight": 1.0} -->

We consider a finite-horizon control design problem where the goal is to determine a state feedback control policy for $$ that satisfies a risk constraint associated with an STL formula $\varphi$. Specifically, we consider

<!-- chunk {"id": "body-0021", "role": "body", "section": "Control Design for Risk-Constrained STL", "weight": 1.0} -->

1}^{T},\ldots,W_{N - 1}^{T}\rbrack}^{T}$, $N$ is the time horizon, $J$ is a stage cost function with expectation taken with respect to the disturbance sequence $\{ W_{t}\}$, $\delta \in {\mathbb{R}}$ is a user-defined risk bound, and $U \subset {\mathbb{R}}^{Nm}$ is an input constraint set.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Control Design for Risk-Constrained STL", "weight": 1.0} -->

The challenge lies in the uncertainty in the system model and its appearance in the STL risk constraint. We approach this using Model Predictive Control (MPC) and a reformulation of the STL risk constraint into a tightened deterministic STL constraint so that existing control approaches for deterministic STL constraints can be used such as summarized in Section I.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Control Design for Risk-Constrained STL", "weight": 1.0} -->

Using MPC to (approximately) solve reduces the problem to a sequence of open-loop optimization problems. For an STL problem with formula $\varphi$, a natural choice for the prediction horizon is $N \geq {\text{len}{(\varphi)}}$ with a system run of $N_{s} > N$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Control Design for Risk-Constrained STL", "weight": 1.0} -->

where the decision variable is the open-loop control sequence $u_{t:{{t + N} - 1}}$, expectation is with respect to $W_{t:{{t + N} - 1}}$. Solving the optimization problem yields the future optimal control sequence $u_{t:{{t + N} - 1}}^{\ast} = {\lbrack u_{t}^{\ast},\ldots,u_{{t + N} - 1}^{\ast}\rbrack}$. Only the first component $u_{t}^{\ast}$ of this plan is implemented, and the problem is solved again after the next state realization is observed. Thus, the MPC policy is ${\mu_{\text{MPC}}{(x_{t})}} = u_{t}^{\ast}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Control Design for Risk-Constrained STL", "weight": 1.0} -->

We assume that ${\mathbb{E}}{\lbrack{J{(X_{t:{t + N}},u_{t:{{t + N} - 1}})}}\rbrack}$ in can be evaluated analytically, which is the case for quadratic $J$, allowing us to focus solely on challenges in accounting for the STL risk constraint.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Reformulation of STL Risk Constraints", "weight": 1.0} -->

In this section, we demonstrate how the optimization problem can be reformulated into an optimization problem with *deterministic*, tightened STL constraints on the nominal system dynamics. We also show how to explicitly write the tightened constraints on atomic predicates for one specific coherent risk measure, Distributionally Robust Value at Risk.

<!-- chunk {"id": "body-0027", "role": "body", "section": "V-A From STL formula violation risk to atomic predicate violation risk", "weight": 1.0} -->

The semantics in Definition 1 are useful for two main reasons: 1) the risk metrics described in Section II appear only at the atomic predicate level and the risk of failing to satisfy an STL formula is defined recursively from there, 2) through the recursive STL risk semantics, all operators (except negation) are defined in terms of $\min$ and $\max$ operators over time intervals. These reasons allow transforming a risk-based STL constraint into similar risk constraints on atomic predicates. This is formalized in Theorem 1.

<!-- chunk {"id": "body-0028", "role": "body", "section": "V-B Risk-tightened predicates", "weight": 1.0} -->

Having found atomic predicate risk constraints and, we now turn to reformulating the stochastic STL problem into a deterministic one assuming affine predicates^11^1Note that the use of affine predicates only is not particularly restrictive since most Mixed-Integer Linear Programming (MILP) tools, widely used with STL, only allow affine predicates..

<!-- chunk {"id": "body-0029", "role": "body", "section": "V-C Explicit reformulation for affine predicates and Distributionally Robust Value at Risk", "weight": 1.0} -->

In Section V-A we obtained constraints on atomic predicates of the form: ${\rho{({- {\alpha{(X_{t})}}})}} \leq \delta$ or ${\rho{({\alpha{(X_{t})}})}} \leq \delta$. In Section V-B we reformulated the system, derived risk-tightened atomic predicate constraints with affine predicates (${\alpha{(x)}} = {{a^{T}x} + b}$), and presented the deterministic system. In this section we turn to evaluating the tightened constraints for a particular choice of the risk metric $\rho$: the Distributionally Robust Value at Risk (DR-VaR).

<!-- chunk {"id": "body-0030", "role": "body", "section": "V-C Explicit reformulation for affine predicates and Distributionally Robust Value at Risk", "weight": 1.0} -->

We now present Lemma 1 which explicitly presents the deterministic constraints equivalent to and.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We use the BluSTL package in its closed-loop deterministic setting for our results. The package uses YALMIP and reformulates an STL specification into a Mixed-Integer Linear Program (MILP), and then solves an MPC problem. Each agent is a double integrator with four states (position and velocity along two directions), two control inputs (along velocity directions), and four additive disturbances on the states. The disturbances are sampled from a 0-mean 3 degree of freedom t-distribution scaled to 0.005-variance and applied to velocity states only. BluSTL converts the continuous time system to discrete-time with 0.1sec system steps and 0.2sec controller steps. We perform two types of simulations. Type 1: The controller ignores the disturbance in the dynamics and uses deterministic MPC with the nominal model, but is evaluated with the disturbance in closed-loop. Type 2: We explicitly incorporate the uncertainty using our proposed STL risk analysis, transform the specification into a deterministic risk-tightened STL formula, compute the control, and then evaluate in closed-loop with the disturbance.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We use $\delta_{1} = 0.1$ risk bound for predicates involving the obstacle avoidance and $\delta_{2} = 0.5$ risk bound for predicates involving the goal region. This puts more emphasis on obstacle avoidance. We also saturate the tightening parameter $\Delta{\|{\Sigma_{W_{0:{t - 1}}}^{1/2}L_{t - 1}^{T}a}\|}_{2}$ after 1 second to limit the effect of increasing prediction uncertainty. In both cases the objective $J$ minimizes the sum of the 1-norm of the control inputs and the distance to the goal. We run 100 simulations for each type and present them in Fig. 1.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Type 1 trajectories (left) get very close and occasionally collide with the obstacle. The disturbance causes 84 of the 100 simulations to fail to reach the goal. Type 2 (right) trajectories, however, satisfy the risk bounds and remain sufficiently far from the obstacle, and 98 of the 100 reach the goal.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

We presented a general framework for risk-based STL specifications for stochastic systems using axiomatic risk theory. We are exploring several extensions and variations in ongoing and future work, including explicit reformulations for various risk measures and ambiguity sets, non-affine predicates, non-linear dynamics, infinite-horizon persistent tasks, and alternative risk semantics.
