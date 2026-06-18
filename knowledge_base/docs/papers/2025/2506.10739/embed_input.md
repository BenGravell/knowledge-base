<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sampling-Based Planning under STL Specifications: A Forward Invariance Approach

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a variant of the Rapidly Exploring Random Tree Star (RRT^(star)) algorithm to synthesize trajectories satisfying a given spatio-temporal specification expressed in a fragment of Signal Temporal Logic (STL) for linear systems. Previous approaches for planning trajectories under STL specifications using sampling-based methods leverage either mixed-integer or non-smooth optimization techniques, with poor scalability in the horizon and complexity of the task. We adopt instead a control-theoretic perspective on the problem, based on the notion of set forward invariance. Specifically, from a given STL task defined over polyhedral predicates, we develop a novel algorithmic framework by which the task is efficiently encoded into a time-varying set via linear programming, such that trajectories evolving within the set also satisfy the task. Forward invariance properties of the resulting set with respect to the system dynamics and input limitations are then proved via non-smooth analysis.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We then present a modified RRT^(star) algorithm to synthesize asymptotically optimal and dynamically feasible trajectories satisfying a given STL specification, by sampling a tree of trajectories within the previously constructed time-varying set. We showcase two use cases of our approach involving an autonomous inspection of the International Space Station and room-servicing task requiring timed revisit of a charging station.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The application of sampling-based planners to plan kino-dynamically feasible trajectories in complex environments for systems subject to spatio-temporal constraints has been an active area of research during the past decades. Particularly, with the aim of deploying autonomous systems with verifiable performance guarantees, a growing body of literature has been devoted toward designing planning algorithms to synthesize trajectories satisfying tasks expressed as Linear Temporal Logic (LTL) formulas and, more recently, Signal Temporal Logic (STL) formulas.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The focus of this work is on trajectory planning for linear systems under STL specification, leveraging Rapidly Exploring Random Trees (RRT) and, in particular, its asymptotically optimal variant RRT^⋆^, with applications to real-time robot motion planning in complex environments.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Contributions", "weight": 1.0} -->

In this paper, we propose to adopt a novel approach to real-time sampling-based planning of trajectories for linear systems subject to STL constraints, leveraging the notion of forward invariance of time-varying sets. Namely, we formalize a simple, yet effective, approach to cast a STL specification, expressed over linear predicate functions, into a time-varying set, expressed as a time-varying polyhedron, which we design via linear programming. We show via a non-smooth analysis that the resulting set is forward invariant for the system dynamics, i.e., there exists a controller that maintains the system within the set under input constraints, given that the system starts within the set. While the problem of casting STL specifications into time-varying sets was previously considered, our contribution differs from these previous works in the following terms. While consider the entire STL fragment of specifications, their approach considers complex reachable set computations, which often can not be achieved in real-time. In this regard, we trade off a loss in expressivity, as we consider a subfragment of STL, for a reduction in computational complexity, for which we don't need to undertake complex reachable sets computations.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Contributions", "weight": 1.0} -->

On the other hand, compared to, we here consider a more expressive STL fragment that includes nested temporal operators, thus allowing for a richer set of specifications, e.g., recurring tasks.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contributions", "weight": 1.0} -->

Specifically, we encode an STL task $\phi$ into a time-varying polyhedron $\mathcal{B}^{\phi}{(t)}$, we provide a real-time implementation of RRT^⋆^ to synthesize dynamically feasible trajectories satisfying the task $\phi$. Namely, if we let $\zeta_{x}{(t)}$ represent a trajectory of a given linear system, we then propose to expand a tree of sampled trajectory that evolves within the time-varying set $\mathcal{B}^{\phi}{(t)}$ from which we obtain a minimum cost trajectory satisfying $\phi$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Organization", "weight": 1.0} -->

Sections II and III introduce preliminaries and problem formulation. In Sec. IV and V our first contribution is provided, developing an algorithmic approach to construct a time-varying polyhedral set from a given STL task $\phi$, with guaranteed forward invariance properties, such that trajectories evolving in this set also satisfy $\phi$. In Sec. VI an implementation of RRT^⋆^ leveraging such a time-varying set is shown, while simulations showcasing our algorithms are given in Sec. VII. Conclusions and future work are provided in Sec. VIII.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Signal Temporal Logic", "weight": 1.0} -->

Signal Temporal Logic (STL) is a predicate logic suitable to define spatial and temporal specification over state signals deriving from dynamical systems such as. Specifically, let a set of predicate functions $h:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$, with level set

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Signal Temporal Logic", "weight": 1.0} -->

where $U$ is the temporal until operator, with time interval ${\lbrack a,b\rbrack} \subset {\mathbb{R}}_{\geq 0}$, while $\neg$ and $\land$ represent logical negation and conjunction operators. The disjunction operator $\vee$ derives from these by De Morgans's laws. The temporal always and eventually operators derive from the until as ${G_{\lbrack a,b\rbrack}\phi} = {\neg{({\top{U_{\lbrack a,b\rbrack}{\neg\phi}}})}}$ and ${F_{\lbrack a,b\rbrack}\phi} = {\top{U_{\lbrack a,b\rbrack}\phi}}$, respectively. We here consider tasks $\phi$ with bounded time domain i.e. formulas whose temporal operators have a bounded domain, for which we define the time horizon of a task $\phi$ as

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Signal Temporal Logic", "weight": 1.0} -->

where De Morgan's laws can be used to infer the time horizon for other operators. A simple example provides some intuition.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Example 1", "weight": 1.0} -->

Dashed circles represent the level sets $\mathcal{H}^{i}$ and $\mathcal{H}^{c}$, where ${\mu^{h^{i}}{(\mathbf{x})}} = \top$ and ${\mu^{h^{c}}{(\mathbf{x})}} = \top$, respectively. A task for the black drone could be: "In the next 10 minutes, always visit the charging station with intervals of at most 2 minutes and eventually visit the region of interest and stay there for at least 1 minute".

<!-- chunk {"id": "body-0014", "role": "body", "section": "Example 1", "weight": 1.0} -->

In the STL formalism this can be written for example as $\phi = {{G_{\lbrack 0,10\rbrack}F_{\lbrack 0,2\rbrack}\mu^{h^{c}}{(\mathbf{x})}} \land {F_{\lbrack 0,10\rbrack}G_{\lbrack 0,1\rbrack}\mu^{h^{i}}{(\mathbf{x})}}}$. In this work, we aim at designing a time-varying set $\mathcal{B}^{\phi}{(t)}$ such that the evolution of the drone state within the set $\mathcal{B}^{\phi}{(t)}$ guarantees the satisfaction of the task $\phi$. $\square$

<!-- chunk {"id": "body-0015", "role": "body", "section": "Example 1", "weight": 1.0} -->

To characterize the satisfaction of a given STL task, we consider the STL quantitative semantics (see e.g. \[, Def. 10\] and \[, Sec. 2\]). Namely, let ${(\zeta_{x},t)} \vDash \phi$ denote that the signal $\zeta_{x}:{{\mathbb{R}}_{\geq 0}\rightarrow{\mathbb{X}}}$ satisfies $\phi$ starting from the reference time $t \in {\mathbb{R}}_{\geq 0}$ and let the function $\rho^{\phi}:{{{\mathcal{F}{({\mathbb{R}}_{\geq 0},{\mathbb{R}}^{n})}} \times {\mathbb{R}}_{\geq 0}}\rightarrow{\mathbb{R}}}$ be recursively defined over a trajectory $\zeta_{x}$ as

<!-- chunk {"id": "body-0016", "role": "body", "section": "Example 1", "weight": 1.0} -->

from which we know the semantic relation ${\rho^{\phi}{(\zeta_{x},t)}} > 0\Rightarrow{(\zeta_{x},t)} \vDash \phi$ \[, Prop. 16\]. Note that the selection of the start time is arbitrary, and $t = 0$ is selected as the convention hereafter without loss of generality. Differently from other semantics, quantitative semantics capture the degree of satisfaction of a specification $\phi$. Specifically, for a given margin $r > 0$, the signal $\zeta_{x}$ is said to robustly satisfy $\phi$ with degree $r$, if ${\rho^{\phi}{(\zeta_{x},0)}} \geq r > 0$, which we denote as ${(\zeta_{x},0)} \vDash_{r}\phi \equiv {\rho^{\phi}{(\zeta_{x},0)}} \geq r$ such that

<!-- chunk {"id": "body-0017", "role": "body", "section": "Example 1", "weight": 1.0} -->

In this work, we consider predicate functions of the form

<!-- chunk {"id": "body-0018", "role": "body", "section": "Example 1", "weight": 1.0} -->

Linear predicates, as per, are commonly considered in the STL literature for their computational tractability while allowing for rich types of specifications (cf. ). Moreover, we consider STL tasks expressed in the fragment

<!-- chunk {"id": "body-0019", "role": "body", "section": "Example 1", "weight": 1.0} -->

where ${T,T^{\prime}} \in {\{ G,F\}}$. Formulas $\varphi$, as per (11a), represent temporally extended specifications over a single predicate based on the always or eventually operators, or a composition of these. Note that, formulas of type $\mu^{h_{1}}U_{\lbrack a,b\rbrack}\mu^{h_{2}}$ can be expressed in as ${G_{\lbrack a,\tau\rbrack}\mu^{h_{1}}} \land {F_{\lbrack\tau,\tau\rbrack}\mu^{h_{2}}}$ for some $\tau \in {\lbrack a,b\rbrack}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Example 1", "weight": 1.0} -->

Likewise, arbitrary nestings of the same temporal operator are part of (11a) since ${T_{\lbrack a_{1},b_{2}\rbrack}T_{\lbrack a_{2},b_{3}\rbrack}\ldots T_{\lbrack a_{N},b_{N}\rbrack}\mu^{h}} \equiv {T_{\lbrack{\sum_{n = 1}^{N}a_{n}},{\sum_{n = 1}^{N}b_{n}}\rbrack}\mu^{h}}$. Formulas $\phi$, as per (11b), represent conjunctions of formulas $\varphi$, as per (11b), to compose complex specifications, while formulas of type $\psi$, as per (11c), represent disjunctions of formulas $\phi$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Example 1", "weight": 1.0} -->

Informally speaking, the formula $\psi = {\vee_{k}\phi_{k}}$ is satisfied if at least one of the formulas $\phi_{k}$ is satisfied.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Example 1", "weight": 1.0} -->

While the fragment in does not capture the full expressivity of the STL fragment, we focus on for the following reasons. First, synthesizing trajectories that satisfy general STL specifications is an NP-hard problem, typically tackled using Mixed-Integer Linear Programming (MILP). Although MILP solvers are sound and complete, their computational demands are often prohibitive, even for formulas within the fragment, making real-time planning infeasible. Regarding the absence of the negation operator in --- which is commonly used to enforce safety properties (e.g., "always avoid region $\mathcal{H}$") --- this limitation does not significantly reduce expressivity in our settings since safety requirements will be handled at the sampling level by rejecting trajectories entering unsafe regions of the workspace, e.g. obstacles.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Example 1", "weight": 1.0} -->

At the same time, we admittedly can handle the $\vee$ operator only at a high level of the formula such that formulas of type $F_{\lbrack a,b\rbrack}G_{\lbrack a^{\prime},b^{\prime}\rbrack}{({\mu^{h_{1}} \vee \mu^{h_{2}}})}$ are not within fragment and we leave this extension as future work.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Example 1", "weight": 1.0} -->

To summarize, compared to planning via MILP solvers, we trade off a reduction in expressivity, for a simple and effective implementation that allows for real-time planning of trajectories satisfying STL tasks in the fragment, from which a rich set of behaviors of common interest (e.g. rescue, exploration, and patrolling) can be obtained.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-B Viability and forward invariance of set-valued maps", "weight": 1.0} -->

As pointed out in the introduction, we propose to adopt a forward invariance perspective over the satisfaction of STL specifications from fragment on the same line of. Specifically, we consider encoding STL tasks from the fragment into a time-varying set derived as the level set of a non-smooth Control Barrier Function (CBF) of the form ${\mathfrak{b}}:{{{\mathbb{R}}^{n} \times {\lbrack t_{0},t_{1}\rbrack}}\rightarrow{\mathbb{R}}}$, for some interval ${\lbrack t_{0},t_{1}\rbrack} \subset {\mathbb{R}}_{\geq 0}$, with level set $\mathcal{B}:{{\lbrack t_{0},t_{1}\rbrack}\rightarrow 2^{\mathbb{X}}}$ defined as

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-B Viability and forward invariance of set-valued maps", "weight": 1.0} -->

A pivotal aspect in our planning framework is the ability to synthesize dynamically feasible trajectories that evolve within a time-varying set of the form, which we ought to design in order to satisfy a given STL task. The notion of forward-invariance of set-valued maps is thus introduced.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Problem 1", "weight": 1.0} -->

Consider the dynamical system and an STL task $\phi$ as per (11b) with maximum horizon $t_{hr}{(\phi)}$. Design an algorithm that returns a trajectory $\zeta_{x}:{{\lbrack 0,{t_{hr}{(\phi)}}\rbrack}\rightarrow{\mathbb{X}}}$ such that $\zeta_{x}$ is safe and ${(\zeta_{x},0)} \models_{r}\phi$ with robustness degree $r > 0$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Problem 1", "weight": 1.0} -->

To approach Problem, we develop the following steps. In the next Sections IV-V, an algorithmic approach is defined to design a time-varying set $\mathcal{B}^{\phi}{(t)}$, in the form of, from a given task $\phi$, as per (11b), such that 1) the set $\mathcal{B}^{\phi}{(t)}$ is forward invariant as per Def., (i.e., we show the existence of a control law that maintains systems within the set $\mathcal{B}^{\phi}{(t)}$ at every time) 2) any trajectory of system evolving in $\mathcal{B}^{\phi}{(t)}$ also satisfies $\phi$ with a given robustness $r > 0$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Problem 1", "weight": 1.0} -->

When considering the task disjunction $\psi = {\vee_{k}\phi_{k}}$, as per (11c), it is sufficient to only satisfy one of the tasks $\phi_{k}$ in order to satisfy $\psi$. Thus, we design a set $\mathcal{B}_{k}^{\phi}{(t)}$ for each $\phi_{k}$ in parallel, and the task achievable with highest robustness is selected to satisfy $\psi$, such that Problem naturally genealizes to the satisfaction of tasks of type $\psi$ as per (11c).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Problem 1", "weight": 1.0} -->

Eventually, in Section VI, we generate trajectories that satisfy Problem via a modified implementation of RRT^⋆^. Namely, we enforce the STL task satisfaction by generating a tree of sampled trajectories that evolves within the previously designed time-varying sets, while safety is enforced by rejecting trajectories intersecting the obstacles ${\mathcal{O}_{k} \subset {\mathbb{X}}},{k \in {\lbrack{\lbrack n_{o}\rbrack}\rbrack}}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "From STL tasks to time-varying sets: Viability", "weight": 1.0} -->

Leveraging the notion of parametric Control Barrier Functions (CBF), in this section we propose an algorithmic approach to design a viable time-varying set $\mathcal{B}^{\phi}{(t)}$, encoding an STL task $\phi$, as per, as the level set of a parametric CBF. We start first by considering the construction approach for a single task $\varphi$, as per (11a), to then generalize to the conjunction $\phi$, as per (11b). When considering a task $\psi = {\vee_{k}\phi_{k}}$, obtained as the disjunction of multiple tasks $\phi_{k}$, we apply the same construction approach separately for each $\phi_{k}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A Parametric Control Barrier Functions", "weight": 1.0} -->

where $h$ is the predicate associated to $\varphi$, as per, and the function $\gamma^{\varphi}:{{{\lbrack 0,\beta\rbrack} \times \Theta}\rightarrow{\mathbb{R}}}$ is a continuous piece-wise linear function over the sequence of switches ${(s_{i})}_{i = 1}^{3} = {(0,\alpha,\beta)}$ with $\beta \geq \alpha \geq 0$ such that for $i \in {\{ 1,2\}}$ we have

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A Parametric Control Barrier Functions", "weight": 1.0} -->

An example of $\gamma^{\varphi}$ is given in Fig., where $\gamma^{\varphi}$ intuitively represents a functional encoding of the temporal operators $G_{\lbrack a,b\rbrack}$ and $F_{\lbrack a,b\rbrack}$, such that the reader should associate the interval $\lbrack\alpha,\beta\rbrack$ with the interval $\lbrack a,b\rbrack$ of the corresponding temporal operator. The parameters of $\gamma^{\varphi}$ (and thus ${\mathfrak{b}}^{\varphi}$) are stacked in the vector $\mathbf{\vartheta} = {\lbrack\overline{\gamma},r\rbrack}^{T} \in \Theta \subset {\mathbb{R}}^{2}$. By letting the robust level set of $h$ be defined as

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A Parametric Control Barrier Functions", "weight": 1.0} -->

from which we derive $\mathcal{H}^{r} \subset \mathcal{H}$, since $r > 0$. Since $\gamma^{\varphi}$ is defined by two piece-wise linear sections, it will be useful to introduce the index map $\Upsilon:{{\lbrack 0,\beta\rbrack}\rightarrow{\{ 1,2\}}}$ as

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-A Parametric Control Barrier Functions", "weight": 1.0} -->

with index $i \in {\{ 1,2\}}$ indicating either of the two linear sections of $\gamma^{\varphi}$. As the next proposition shows, the set $\mathcal{B}^{\varphi}{(\left. t \middle| \mathbf{\vartheta} \right.)}$ is viable, by construction, for any $\mathbf{\vartheta} \in \Theta$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B Time-varying set encoding: single operator case", "weight": 1.0} -->

First, the construction rules for formulas of type $\varphi = {G_{\lbrack a,b\rbrack}\mu^{h}}$ and $\varphi = {F_{\lbrack a,b\rbrack}\mu^{h}}$ are presented.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-D Time-varying set encoding: the conjunction case", "weight": 1.0} -->

and corresponding time-varying level set

<!-- chunk {"id": "body-0038", "role": "body", "section": "From STL tasks to time-varying sets: Forward Invariance", "weight": 1.0} -->

Now that we have analyzed the viability properties of the set $\mathcal{B}^{\phi}{(\left. t \middle| {\mathbf{θ}} \right.)}$, we want to focus on forward invariance. Namely, let the set $\mathcal{B}^{\phi}{(\left. t \middle| {\mathbf{θ}} \right.)}$ be defined by an appropriate selection of the switching times from Rules -. We want to find an optimal assignment of the parameters ${\mathbf{θ}} = {\lbrack{\mathbf{\vartheta}_{1}^{T}\ldots\mathbf{\vartheta}_{n_{\phi}}^{T}}\rbrack}^{T} \in \overline{\Theta}$, such that $\mathcal{B}^{\phi}{(\left.

<!-- chunk {"id": "body-0039", "role": "body", "section": "From STL tasks to time-varying sets: Forward Invariance", "weight": 1.0} -->

t \middle| {\mathbf{θ}} \right.)}$ is forward invariant and the robustness of satisfaction of the task $\phi = {\land_{l = 1}^{n_{\phi}}\varphi_{l}}$ is maximized, by considering the general optimization problem

<!-- chunk {"id": "body-0040", "role": "body", "section": "From STL tasks to time-varying sets: Forward Invariance", "weight": 1.0} -->

where ${\mathfrak{g}}:{\overline{\Theta}\rightarrow{\mathbb{R}}^{n_{g}}}$ is a set of constraints on $\mathbf{θ}$ such that the optimal set of parameters ${\mathbf{θ}}^{\ast}$ solving guarantees $\mathcal{B}^{\phi}{(\left. t \middle| {\mathbf{θ}}^{\ast} \right.)}$ is viable and forward invariant while maximizing the robustness of satisfaction for $\phi$. In this section, we clarify how the constraints in $\mathfrak{g}$ are defined starting first by showing constraints under which a single set $\mathcal{B}^{\varphi}{(\left. t \middle| \mathbf{\vartheta} \right.)}$ can be made forward invariant, to then generalize to the conjunction set $\mathcal{B}^{\phi}{(\left.

<!-- chunk {"id": "body-0041", "role": "body", "section": "From STL tasks to time-varying sets: Forward Invariance", "weight": 1.0} -->

t \middle| {\mathbf{θ}} \right.)}$, based on the result of Theorem.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-A Enforcing forward invariance: single task case", "weight": 1.0} -->

For convenience, we temporarily omit the dependence from the parameters $\mathbf{\vartheta}$ and drop the index $l$ of each cCBF ${\mathfrak{b}}^{\varphi}$ in the derivations. We reintroduce full notation in the presentation of the main results.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-A Enforcing forward invariance: single task case", "weight": 1.0} -->

To enforce the forward invariance of the set $\mathcal{B}^{\varphi}{(t)}$ over the interval $\lbrack 0,\beta\rbrack$ we leverage the result of Theorem for which we show the existence of a control input $\zeta_{u}:{{\lbrack 0,\beta\rbrack}\rightarrow{\mathbb{U}}}$ satisfying the condition

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-A Enforcing forward invariance: single task case", "weight": 1.0} -->

In the presentation, we assume that the control input is measurable, which is a standard assumption when working with non-smooth dynamical systems (see e.g. \[, Sec. III(B)\]), as the measurability assumption is violated only in pathological cases, which rarely occur in practice.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Example 2", "weight": 1.0} -->

Leveraging this finite dimensional representation, Lemma shows that the feasibility of over the continuum of points in ${{{\mathbb{X}} \times {(s_{i},s_{i + 1})}},i} \in {\{ 1,2\}}$, can be verified by checking a set of linear inequalities over the set of vertices ${V_{\mathbb{Z}}^{i},i} \in {\{ 1,2\}}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-B Enforcing forward invariance: the conjunction case", "weight": 1.0} -->

Similarly to the single task case, we need to find a control input such that the condition

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-B Enforcing forward invariance: the conjunction case", "weight": 1.0} -->

is satisfied from every ${\mathbf{x}}_{0} \in {\mathcal{B}^{\phi}{}}$, from which forward invariance can be proved leveraging Thm.. With this goal, we select the control input given by

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-C Final optimization program", "weight": 1.0} -->

where constraint (53b) enforces each parameters $\mathbf{\vartheta}_{l}$ and state variables ${\mathbf{ξ}}_{l}$ in their respective sets $\Theta_{l}$ and $\mathbb{X}$, constraint (53c) enforces each input vector ${\mathbf{u}}_{q}^{j}$ in the sets $V_{\mathbb{U}}^{j}$ to be within the input bounds, constraint (53e) enforces ${\mathbf{x}}_{0} \in {\mathcal{B}^{\phi}{(\left. 0 \middle| {\mathbf{θ}} \right.)}}$, constraint (53f) enforces viability of the set $\mathcal{B}^{\phi}{(\left.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-C Final optimization program", "weight": 1.0} -->

t \middle| {\mathbf{θ}} \right.)}$ as per Proposition and finally (53g) enforces the forward invariance properties of the set $\mathcal{B}^{\phi}{(\left. t \middle| {\mathbf{θ}} \right.)}$ as per Lemma. Note that is a linear program which can be solved efficiently using standard off-the-shelf solvers for very high-dimensional problems.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Trajectory planning via RRT^⋆^", "weight": 1.0} -->

Given an STL task $\phi$, this section provides a detailed explanation of how Problem is approached leveraging the RRT^⋆^ planning algorithm. Loosely speaking, the approach taken consists on computing the time-varying set $\mathcal{B}^{\phi}{(t)}$, obtained as the solution to the parameters optimization problem (dropping $\mathbf{θ}$), and iteratively construct a tree of trajectories that evolves within the set $\mathcal{B}^{\phi}{(t)}$. It follows from the result of Lemma, that every such trajectory robustly satisfies $\phi$. The reason why an RRT^⋆^ planning approach is relevant to solve Problem is that it allows to generate safe trajectories that satisfy a task $\phi$, by rejecting trajectories that can potentially hit obstacles in the environment.

<!-- chunk {"id": "body-0051", "role": "body", "section": "VI-A The algorithm", "weight": 1.0} -->

which intuitively represents the total length of the trajectory from the root node $({\mathbf{x}}_{0},0)$ to $({\mathbf{x}}_{i},t_{i})$ obtained by concatenating the edge trajectories $\zeta_{x}^{\sigma_{k},\sigma_{k + 1}}$. The objective is to construct a tree of trajectories with minimum cost, with respect to, that satisfy $\phi$. This is done in two main phases: an expansion phase and a rewiring phase, which we detail next.

<!-- chunk {"id": "body-0052", "role": "body", "section": "VI-A1 Initialization", "weight": 1.0} -->

At initialization (lines - in Alg. ) the root node $({\mathbf{x}}_{0},0)$ and a desired STL task $\psi = {\vee_{k}\phi_{k}}$ is provided, encoding a set of possible tasks to be achieved. Based on this information, the time-varying sets $\mathcal{B}_{k}^{\phi}{(t)}$ are computed by solving the parameter optimization for each $\phi_{k}$. The task $\phi$ with the highest robustness is then selected for execution with the corresponding time-varying set $\mathcal{B}^{\phi}{(t)}$. Moreover, the tree $\mathcal{T}$ is initialized with $\mathcal{V} = {\{{({\mathbf{x}}_{0},0)}\}}$ and edge set $\mathcal{E} = \varnothing$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "VI-A2 Expansion phase", "weight": 1.0} -->

After initialization, the main iteration of the algorithm starts (lines - in Alg. ).

<!-- chunk {"id": "body-0054", "role": "body", "section": "VI-A2 Expansion phase", "weight": 1.0} -->

We choose samples with maximum time $t_{hr}{(\phi)}$ as the task satisfaction is determined within this maximum time. Since $\mathcal{B}^{\phi}{(t)}$ is defined up to the time $\beta_{\phi} \leq {t_{hr}{(\phi)}}$ as per, we consider the convention ${\mathcal{B}^{\phi}{(t)}} = {\mathbb{X}}$ for all $t \in {\lbrack\beta_{\phi},{t_{hr}{(\phi)}}\rbrack}$, which is without loss of generality since the satisfaction of $\phi$ is determined within the time $\beta_{\phi}$ as per Lemma.

<!-- chunk {"id": "body-0055", "role": "body", "section": "VI-A2 Expansion phase", "weight": 1.0} -->

Intuitively, the optimal trajectory $\zeta_{x}^{ij}$ obtained by solving is such that it starts from $({\mathbf{x}}_{i},t_{i})$ and it moves toward the node $(\overset{\sim}{\mathbf{x}},\overset{\sim}{t})$ for a time interval $\Delta$ until the node $({\mathbf{x}}_{j},t_{j})$ with $t_{j} = {t_{i} + \Delta}$ and ${\mathbf{x}}_{j} = {\zeta_{x}^{ij}{(t_{j})}}$, as depicted in Fig. -(left). Note constraint (58d) is a set of time-varying linear constraints with the form, such that is a quadratic program (quadratic cost and linear constraints), which can be solved efficiently.

<!-- chunk {"id": "body-0056", "role": "body", "section": "VI-A2 Expansion phase", "weight": 1.0} -->

An important fact is that, thanks to the construction approach taken for $\mathcal{B}^{\phi}{(t)}$, the control input signal $\zeta_{u}^{ij}:{{\lbrack t_{i},t_{j}\rbrack}\rightarrow{\mathbb{U}}}$ generated by applying from the initial state ${\mathbf{x}}_{i}$ (with resulting state signal $\zeta_{x}^{ij}:{{\lbrack t_{i},t_{j}\rbrack}\rightarrow{\mathbb{U}}}$) always represents a feasible solution to as per Lemma, from which the following proposition is derived.

<!-- chunk {"id": "body-0057", "role": "body", "section": "VI-A3 Rewiring phase", "weight": 1.0} -->

which is similar to, with the additional constraint (60e) that enforces the terminal value constraint ${\zeta_{x}^{ir}{(t_{r})}} = {\mathbf{x}}_{r}$. In principle, is computationally harder compared to, due to the double boundary value constraint. Moreover, different, the feasibility of (60e) can not be guaranteed due to the boundary value constraint. At this point, a trajectory is considered for rewiring if 1) a solution to exists, 2) such solution is not in collision and 3) the cost-to-go for node $({\mathbf{x}}_{r},t_{r})$ is reduced by the rewiring through node $({\mathbf{x}}_{j},t_{j})$ as

<!-- chunk {"id": "body-0058", "role": "body", "section": "VI-A3 Rewiring phase", "weight": 1.0} -->

then the new trajectory $\zeta_{x}^{jr}$ is added to the tree and the old trajectory $\zeta_{x}^{pr}$ from the parent node $({\mathbf{x}}_{p},t_{p})$ of node $({\mathbf{x}}_{j},t_{j})$ in the tree $\mathcal{T}$ is removed. In any other case, the current rewiring failed, and the algorithm continues.

<!-- chunk {"id": "body-0059", "role": "body", "section": "VI-A3 Rewiring phase", "weight": 1.0} -->

The rewiring phase terminates when all possible rewiring attempts have been made, and the whole iteration is restarted.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Simulations", "weight": 1.0} -->

* Sum of solver times of for tasks ϕ1 and ϕ2

<!-- chunk {"id": "body-0061", "role": "body", "section": "Simulations", "weight": 1.0} -->

We present two use cases of our proposed RRT algorithm. One involves servicing some interest points while ensuring revisit of a charging station, and one involves inspecting the International Space Station (ISS) with a deputy spacecraft over a long-horizon mission. The open source software cvxpy was employed to solve the linear program for each STL task and to transcribe the continuous time optimization programs and necessary to run Alg..

<!-- chunk {"id": "body-0062", "role": "body", "section": "Case study", "weight": 1.0} -->

The dynamics represent a single integrator dynamics with a position-dependent velocity drift.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Case study", "weight": 1.0} -->

0,200\rbrack}F_{\lbrack 0,100\rbrack}\mu^{h_{c}}} \land {G_{\lbrack 255,265\rbrack}\mu^{h_{1}}}}$ where the predicate functions ${h_{i},i} \in {\{ 1,2,3\}}$ represent areas of interest, while $h_{c}$ represents the charging station which should be revisited (see purple boxes in Fig. 6(a)).

<!-- chunk {"id": "body-0064", "role": "body", "section": "Case study", "weight": 1.0} -->

The difference between $\phi_{1}$ and $\phi_{2}$ is only in the order in which the regions of interest are reached. The task $\phi_{2}$ was selected for the satisfaction of $\psi$ with maximum robustness $r = 0.12$, while the resulting robustness for $\phi_{1}$ was only $r = 0.06$. The best trajectory (in terms of the cost in ) obtained by our algorithm is shown in Fig. 6(a), with the color gradient representing the time progression along the trajectory. The algorithm was run for a total of 500 iterations, over 100 experiments with running time and trajectory cost summarized in Tab. 6(b). Due to the sampling-based nature of the algorithm, the obtained trajectory is only piece-wise smooth. While we did not smooth the resulting trajectory, any smoothing algorithm could be applied to further improve the final result, e.g., using splines optimization.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Case study", "weight": 1.0} -->

We consider a deputy spacecraft inspecting the International Space Station (ISS) by visiting a set of pre-selected observation regions (purple boxes in Fig. 6(c)). The deputy is modelled as a double integrator governed by the standard Clohessy--Wiltshire model. Namely, let the state ${\mathbf{x}} = {\lbrack{{\mathbf{p}}{\mathbf{v}}}\rbrack}^{T} \in {\mathbb{R}}^{6}$ represent the position and velocity of the deputy with dynamics $\overset{˙}{\mathbf{x}} = {{A{\mathbf{x}}} + {B{\mathbf{u}}}}$ as

<!-- chunk {"id": "body-0066", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduced a sampling-based planning framework, based on RRT^⋆^, to synthesize trajectories under STL specifications with real-time performance. Namely, our approach leverages suitably constructed time-varying sets, with provable forward invariance guarantees with respect to controllable and input limited linear dynamics, to synthesize trajectories robustly satisfying a given STL task. As a next step, we aim to further expand our framework to nonlinear systems, applying techniques from spline optimization, and to broaden the class of STL specifications that we can consider.
