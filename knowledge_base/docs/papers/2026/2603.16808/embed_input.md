<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Exponential Stability of Data-driven Nonlinear MPC Based on Input/output Models

Topics include Model predictive control, Predictive control, Stability analysis, Online algorithms, Optimization, Control, Nonlinear systems, Exponential stability.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider nonlinear model predictive control (MPC) schemes using surrogate models in the optimization step based on input-output data only. We establish exponential stability for sufficiently long prediction horizons assuming exponential stabilizability and a proportional error bound. Moreover, we verify the imposed condition on the approximation using kernel interpolation and demonstrate the practical applicability to nonlinear systems with a numerical example.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model predictive control (MPC) is nowadays a well-established advanced control technique, where the input is determined by solving a finite-horizon constrained optimal control problem. For the stability analysis, terminal conditions are often utilized, see and the references therein. Alternatively, stability can be established using a sufficiently long prediction horizon and some stabilizability condition related to the stage cost, see for an overview. These results rely on positive-definite stage cost penalizing the deviation from the desired set point. However, in practice, output weighting is often preferred since state measurements might not be available neccessitating the use of input/output models. Moreover, output weighting is closely related to closed-loop performance. Then, the resulting stage cost is only positive semi-definite in the system state, and the stability analysis requires more general tools, based on detectability conditions on the stage cost.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

MPC relies on a reliable and accurate model, which explains the recent research interest in data-driven approaches. To this end, a plethora of modeling techniques has been employed in MPC. For linear system, an effective method is based on the use of Willems' fundamental lemma, which allows to directly solve the optimization problem in MPC based on non-parametric models using input/output data only. For nonlinear systems, the explored approaches include Gaussian processes, Koopman operator theory, neural networks, and many more. Despite the availability of many different modeling techniques, data-driven models come with the presence of model-plant mismatch, which may impact the stability properties of the MPC scheme. To fill this gap, recent works have derived conditions, in which data-driven MPC preserves stability and closed-loop performance. Considering MPC without terminal conditions, shows that asymptotic stability can be obtained in presence of proportional bounds on the modeling error, and proposes a framework based on Koopman operator theory to generate data-driven models satisfying the required bounds. Similar results have been derived for MPC with terminal conditions, considering models with parametric uncertainty.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, exponential stability of Koopman MPC with terminal conditions has been studied, where the latter also introduces a constraint-tightening approach to guarantee robust constraint satisfaction despite model-plant mismatch.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

These existing stability results rely on state-space models and, thus, require state measurements. However, in many practical applications, only the system outputs are measurable, and, thus, MPC is designed on the base of input/output models. The goal of this paper, is to extend the results of asymptotic stability of MPC in presence of approximation errors to models in input/output form. In particular, we consider an MPC formulation with output-weighting stage cost, but without terminal conditions, in which stability is studied relying on a sufficiently long optimization horizon and a cost detectability property. We show that exponential stability of the data-driven MPC closed loop can be achieved if the surrogate model satisfies proportional error bounds and the system is exponential stabilizable. Further, we show that kernel interpolation is a suitable learning technique to provide data-driven surrogate models satisfying our requirements. Finally, we demonstrate our findings in numerical simulations.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The paper is organized as follows. Section II introduces the considered control problem and the MPC algorithm. Stability properties of the closed loop system are analyzed in Section III. In Section IV, we show how models satisfying the required conditions can be learned using kernel interpolation. Finally, numerical experiments are reported in Section V and conclusions are drawn in Section VI.\

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem formulation and MPC algorithm", "weight": 1.0} -->

The aim of the paper is to control a nonlinear system using a surrogate model inferred from input/output data. The considered system is described by

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem formulation and MPC algorithm", "weight": 1.0} -->

where ${y{(k)}} \in {\mathbb{R}}^{p}$ is the system output and ${u{(k)}} \in {\mathbb{U}}$ is its control input. ${\mathbb{U}} \subset {\mathbb{R}}^{m}$ is a compact set containing the origin in its interior, and ${x{(k)}} \in {\mathbb{R}}^{n}$ for $n = {{\nup} + {{({\nu - 1})}m}}$ is a vector consisting of inputs and outputs from the last $\nu$ steps. The parameter $\nu \in {\mathbb{N}}$ defines how many of the past observations are required to characterize the dynamics, and corresponds to the lag of the system.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem formulation and MPC algorithm", "weight": 1.0} -->

For sake of simplicity, we assume ${x{(k)}} \in \Omega \subseteq {\mathbb{R}}^{n}$, where $\Omega$ contains the origin in its interior and is a positive invariant set w.r.t. system under inputs $u \in {\mathbb{U}}$.^11^1The case in which the invariance condition does not hold is studied, in which a uniform error bound is leveraged to tighten the constraints and, then, to determine a set in which stability holds.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem formulation and MPC algorithm", "weight": 1.0} -->

for all ${x,x^{\prime}} \in \Omega$. The system can also be written in an equivalent state-space form as

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem formulation and MPC algorithm", "weight": 1.0} -->

The MPC design is based on a data-driven surrogate model

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem formulation and MPC algorithm", "weight": 1.0} -->

with right-hand side approximation $F_{y}^{\varepsilon}$ of $F_{y}$, where the superscript $\varepsilon \in {(0,\overline{\varepsilon}\rbrack}$, $\overline{\varepsilon} > 0$, stands for the approximation accuracy and is used in the following to indicate a dependence on the surrogate dynamics. In Section IV we introduce kernel regression as a possible method to compute such a surrogate model in a data-driven fashion. The surrogate system also has an equivalent state dynamics given by $F_{x}^{\varepsilon}$, analogously defined to, which is also assumed to render the set $\Omega$ positive invariant to streamline the exposition.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem formulation and MPC algorithm", "weight": 1.0} -->

The goal of the paper is to show that in presence of suitable bounds on the modeling error, MPC using the surrogate model in the optimization step stabilizes the controlled system. The MPC is designed considering the quadratic input/output stage cost $\ell:{{{\mathbb{R}}^{p} \times {\mathbb{R}}^{m}}\rightarrow{\mathbb{R}}_{\geq 0}}$ given by

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem formulation and MPC algorithm", "weight": 1.0} -->

Finally, the MPC algorithm is reported in Algorithm 1.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem formulation and MPC algorithm", "weight": 1.0} -->

Input: Horizon N ∈ ℕ, surrogate Fxε, stage cost ℓ,
Input: input constraints 𝕌

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem formulation and MPC algorithm", "weight": 1.0} -->

Initialization: Set k = 0, and initialize the state as
If k &gt; 0, measure output y (k) and set
Solve the optimal control problem

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem formulation and MPC algorithm", "weight": 1.0} -->

to obtain optimal control sequence u⋆ = {u⋆ (i)}i = 0N − 1
Apply the MPC feedback law μNε (x̂) = u⋆ to the
plant to generate the closed loop

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem formulation and MPC algorithm", "weight": 1.0} -->

For the closed-loop analysis, we also introduce the nominal cost function $J_{N}$, and the nominal (optimal) value function $V_{N}$, that are defined analogously to $J_{N}^{\varepsilon}$ and $V_{N}^{\varepsilon}$, but using the actual system dynamics $F_{x}$ instead of the surrogate $F_{x}^{\varepsilon}$ in (6c). In case we have a linear surrogate model $F_{x}^{\varepsilon}$, (OCP) is a computationally efficient convex optimization problem, assuming also $\mathbb{U}$ is convex. In general, we consider a nonlinear true dynamics $F_{x}$ and hence a nonlinear surrogate dynamics $F_{x}^{\varepsilon}$ and hence (OCP) is a nonlinear program, as standard in nonlinear MPC.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Stability analysis", "weight": 1.0} -->

Our goal is to prove exponential stability of the data-driven MPC closed-loop system. To this end, we require the following properties of the model $F_{y}^{\varepsilon}$, see, e.g.,.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

For every $\varepsilon \in {(0,\overline{\varepsilon}\rbrack}$, $\overline{\varepsilon} > 0$, let the surrogate model satisfy

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

uniform Lipschitz continuity in the first argument on $\Omega$, i.e., there exists $\overline{L} > 0$ such that, for every $\varepsilon \in {(0,\overline{\varepsilon}\rbrack}$, there is a Lipschitz constant $L_{F_{y}^{\varepsilon}}$ with $L_{F_{y}^{\varepsilon}} \leq \overline{L}$ satisfying, for all ${x,x^{\prime}} \in \Omega$, $u \in {\mathbb{U}}$,

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Assumption 1 can be rigorously verified, e.g., kernel-based surrogate models as shown in Section IV.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

To derive the stability results, it is important to notice that the considered stage cost only penalizes the system output, and is therefore only positive semi-definite in the state $x$. Hence, the standard stability results for positive definite stage cost, cf., cannot be applied directly. Instead, the stability proof relies on cost detectability. In view of the NARX structure of the system and model, the following result, which is a straightforward adaptation of \[8, Remark 3\], establishes this detectability condition.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 2 (Cost controllability)", "weight": 1.0} -->

System is cost controllable with stage cost on the set $\Omega$, i.e., there exists a monotonically increasing bounded sequence ${(B_{N})}_{N \in {\mathbb{N}}_{0}}$ such that, for every $\hat{x} \in \Omega$ and every $N \in {\mathbb{N}}$, there exists a control sequence $\mathbf{u} \in {\mathbb{U}}^{N}$ satisfying the growth bound

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 2 (Cost controllability)", "weight": 1.0} -->

Cost controllability with a quadratic cost $\ell$ means that the system can be exponentially stabilized to the origin. Compared to the positive-definite-cost case, we cannot have only the stage cost $\ell$ on the right hand side, see for an in-depth discussion.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 2 (Cost controllability)", "weight": 1.0} -->

In the following, we show that, if the system under control is cost controllable, then the same property is preserved by the surrogate model, and vice versa. This proposition follows a similar reasoning like \[15, Proposition 1\]. However, since the stage cost is only semi-definite, it cannot be used to bound the state prediction error, and the cost detectability function $W$ has to be used instead.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Kernel interpolation: Data-driven models", "weight": 1.0} -->

In the following, we show how we can learn a function $F_{y}^{\varepsilon}$ satisfying Assumption 1 from input-output data using kernel interpolation.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Kernel interpolation: Data-driven models", "weight": 1.0} -->

Specifically, we have a data set $\mathcal{X}$ consisting of $\xi_{i} = {(x_{i},u_{i})} \in \Omega \times {\mathbb{U}} =:\Omega_{\xi} \subseteq {\mathbb{R}}^{n + m}$ and $y_{i} = {F_{y}{(\xi_{i})}}$, $i \in {\lbrack 1:D\rbrack}$. Since we can identify each component independently, we focus on estimating $F_{y}^{\varepsilon}$ for a scalar output ($p = 1$) to simplify the exposition. We denote the fill distance of this data by

<!-- chunk {"id": "body-0030", "role": "body", "section": "Kernel interpolation: Data-driven models", "weight": 1.0} -->

Suppose that this data set contains the origin, i.e., $0 \in \mathcal{X}$. Let $\mathsf{k}:{{\Omega_{\xi} \times \Omega_{\xi}}\rightarrow{\mathbb{R}}_{\geq 0}}$ be a symmetric, strictly positive kernel with corresponding reproducing kernel Hilbert space (RKHS) denoted by $\mathbb{H}$. Furthermore, suppose that $F_{y} \in {\mathbb{H}}$. Kernel interpolation yields the unique function that interpolates the data with the minimal RKHS norm, which is given by

<!-- chunk {"id": "body-0031", "role": "body", "section": "Kernel interpolation: Data-driven models", "weight": 1.0} -->

Suppose the RKHS is norm equivalent to the Sobolev space of order $s$, e.g., by choosing a corresponding Matern or Wendland kernel $\mathsf{k}$ of sufficient smoothness. Then, according to \[22, Thm. 5.4\], the power function satisfies

<!-- chunk {"id": "body-0032", "role": "body", "section": "Kernel interpolation: Data-driven models", "weight": 1.0} -->

for some constant $C > 0$, where we use the fact that $0 \in \mathcal{X}$, i.e., the origin is contained in the data set. By setting $s > {1 + {{({n + m})}/2}}$, we satisfy the proportional error bounds with $\varepsilon$ given by the fill distance $h_{\mathcal{X}}$. Furthermore, if kernel $\mathsf{k}$ is twice continuous differentiable with a bounded Hessian, then both functions ${F_{y}^{\varepsilon},F_{y}} \in {\mathbb{H}}$ are also Lipschitz continuous.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Kernel interpolation: Data-driven models", "weight": 1.0} -->

In conclusion, Assumption 1 holds by using kernel interpolation if: (i) the data has a small enough fill distance $h_{\mathcal{X}}\rightarrow 0$, (ii) the equilibrium at the origin is contained in the data set, and (iii) the unknown function $F_{y}$ lies in the RKHS $\mathbb{H}$ with a suitably chosen kernel $\mathsf{k}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Numerical example", "weight": 1.0} -->

The exponential stability of the data-driven MPC is illustrated in a two-tank example described by

<!-- chunk {"id": "body-0035", "role": "body", "section": "Numerical example", "weight": 1.0} -->

with constants ${A_{1} = 0.001},{{c_{1,2} = 0.0254},{c_{2} = 0.0261}}$. The system is integrated by using the classical fourth-order Runge--Kutta method (RK4) using a sampling time ${\Deltat} = 10$s. The output of the system is given by $y = h_{1}$, and the control objective is to steer the system to the equilibrium point $\overline{h} = {(0.0438,0.09)}^{\top}$, $\overline{u} = {5.461 \cdot 10^{- 6}}$, while respecting the input constraint $u \in {\mathbb{U}} ≔ {\lbrack{3.16 \cdot 10^{- 6}},{4.76 \cdot 10^{- 5}}\rbrack}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Numerical example", "weight": 1.0} -->

To ensure proportional error bounds, the first data point is in the reference equilibrium, i.e. $x_{1} = {\lbrack{\overline{h}}_{1},{\overline{h}}_{1},\overline{u}\rbrack}$, $u_{1} = \overline{u}$ and $y_{1} = {\overline{h}}_{1}$. For the simulations, we consider datasets with $D \in {\{ 100,500,2500\}}$ data points. In order to obtain models with an equilibrium point in the origin, the input and output data are shifted with respect to their reference and rescaled before the model identification.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Numerical example", "weight": 1.0} -->

For MPC, we consider a prediction horizon $N = 20$ as well as weights $Q = 1$ and $R = 10^{- 1}$. As comparison strategy, we consider the nominal MPC which uses the exact model for prediction. The nominal MPC is implemented with the same cost function and prediction horizon of the data-driven MPC.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Numerical example", "weight": 1.0} -->

The simulation results are reported in Figs. 1 and 2. Fig. 1 illustrates the tracking errors $\|{{h_{1}{(k)}} - {\overline{h}}_{1}}\|$ of the data-driven MPC closed-loop, comparing the models computed with different numbers of data points, and of the nominal MPC closed-loop. It can be observed that the convergence rate is faster with a larger dataset, even if it does not reach the convergence speed of the closed-loop obtained with perfect system knowledge. Moreover, Fig. 2 shows the corresponding trajectories of the optimal value function $V_{N}^{\varepsilon}$ and the Lyapunov function candidate $Y_{N}^{\varepsilon}$. It is evident that $V_{N}^{\varepsilon}$ fails to serve as a Lyapunov function for any of the surrogate models.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Numerical example", "weight": 1.0} -->

When considering $Y_{N}^{\varepsilon}$, we observe similar non-monotonic behaviour for $D = 100$ as seen with the optimal value function, however, with an increasing number of data points, i.e., $D \in {\{ 500,2500\}}$, $Y_{N}^{\varepsilon}$ is monotonically decreasing. This verifies the findings of Theorem 2, indicating that a sufficiently small modeling error ensures exponential stability.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In this paper, we have provided sufficient conditions such that data-driven MPC without terminal conditions ensures exponential stability for nonlinear input-output systems. The key requirement is the combination of cost detectability and a proportional error bound. The latter can be achieved using kernel interpolation. Future work could consider investigating other data-driven models for proportional error bounds. Moreover, an interesting open research direction is the inclusion of general noise in this framework using Gaussian process models.
