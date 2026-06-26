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

Specifically, we encode an STL task $\phi$ into a time-varying polyhedron $\mathcal{B}^{\phi}{(t)}$ (see. Fig 1), we provide a real-time implementation of RRT^⋆^ to synthesize dynamically feasible trajectories satisfying the task $\phi$. Namely, if we let $\zeta_{x}{(t)}$ represent a trajectory of a given linear system, we then propose to expand a tree of sampled trajectory that evolves within the time-varying set $\mathcal{B}^{\phi}{(t)}$ from which we obtain a minimum cost trajectory satisfying $\phi$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Organization", "weight": 1.0} -->

Sections II and III introduce preliminaries and problem formulation. In Sec. IV and V our first contribution is provided, developing an algorithmic approach to construct a time-varying polyhedral set from a given STL task $\phi$, with guaranteed forward invariance properties, such that trajectories evolving in this set also satisfy $\phi$. In Sec. VI an implementation of RRT^⋆^ leveraging such a time-varying set is shown, while simulations showcasing our algorithms are given in Sec. VII. Conclusions and future work are provided in Sec. VIII.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Signal Temporal Logic", "weight": 1.0} -->

Signal Temporal Logic (STL) is a predicate logic suitable to define spatial and temporal specification over state signals deriving from dynamical systems such as.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Signal Temporal Logic", "weight": 1.0} -->

Using Backus--Naur notation, STL formulas are then recursively defined over a set of predicates according to the grammar: where $U$ is the temporal until operator, with time interval ${\lbrack a,b\rbrack} \subset {\mathbb{R}}_{\geq 0}$, while $\neg$ and $\land$ represent logical negation and conjunction operators. The disjunction operator $\vee$ derives from these by De Morgans's laws. The temporal always and eventually operators derive from the until as ${G_{\lbrack a,b\rbrack}\phi} = {\neg{({\top{U_{\lbrack a,b\rbrack}{\neg\phi}}})}}$ and ${F_{\lbrack a,b\rbrack}\phi} = {\top{U_{\lbrack a,b\rbrack}\phi}}$, respectively.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Signal Temporal Logic", "weight": 1.0} -->

We here consider tasks $\phi$ with bounded time domain i.e. formulas whose temporal operators have a bounded domain, for which we define the time horizon of a task $\phi$ as where De Morgan's laws can be used to infer the time horizon for other operators. A simple example provides some intuition.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Example 1", "weight": 1.0} -->

Consider Fig. 1. The predicate functions ${h^{c}{(\mathbf{x})}}:={\epsilon_{r} - {\|{\mathbf{x}_{c} - \mathbf{x}}\|}}$ and ${h^{i}{(\mathbf{x})}}:={\epsilon_{r} - {\|{\mathbf{x}_{i} - \mathbf{x}}\|}}$ represent a charging area (black battery in Fig. 1) and a region of interest (warning sign in Fig. 1), respectively. The term $\epsilon_{r} > 0$ is a positive radius, while $\mathbf{x}_{c}$ and $\mathbf{x}_{i}$ denote the position of the charging area and interest region in the workspace, respectively.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Example 1", "weight": 1.0} -->

Dashed circles represent the level sets $\mathcal{H}^{i}$ and $\mathcal{H}^{c}$, where ${\mu^{h^{i}}{(\mathbf{x})}} = \top$ and ${\mu^{h^{c}}{(\mathbf{x})}} = \top$, respectively. A task for the black drone (lower right in Fig. 1) could be: "In the next 10 minutes, always visit the charging station with intervals of at most 2 minutes and eventually visit the region of interest and stay there for at least 1 minute".

<!-- chunk {"id": "body-0015", "role": "body", "section": "Example 1", "weight": 1.0} -->

In the STL formalism this can be written for example as $\phi = {{G_{\lbrack 0,10\rbrack}F_{\lbrack 0,2\rbrack}\mu^{h^{c}}{(\mathbf{x})}} \land {F_{\lbrack 0,10\rbrack}G_{\lbrack 0,1\rbrack}\mu^{h^{i}}{(\mathbf{x})}}}$. In this work, we aim at designing a time-varying set $\mathcal{B}^{\phi}{(t)}$ (blue sets in Fig. 1) such that the evolution of the drone state within the set $\mathcal{B}^{\phi}{(t)}$ guarantees the satisfaction of the task $\phi$. $\square$ To characterize the satisfaction of a given STL task, we consider the STL quantitative semantics (see e.g. \[23, Def.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Example 1", "weight": 1.0} -->

16\]. Note that the selection of the start time is arbitrary, and $t = 0$ is selected as the convention hereafter without loss of generality. Differently from other semantics, quantitative semantics capture the degree of satisfaction of a specification $\phi$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Example 1", "weight": 1.0} -->

Thus, the set $\mathcal{H}$ in is a polyhedron since ${{h{({\mathbf{x}})}} \geq 0}\Leftrightarrow{{{D{\mathbf{x}}} + {\mathbf{c}}} \geq 0}$ where Linear predicates, as per, are commonly considered in the STL literature for their computational tractability while allowing for rich types of specifications (cf.). Moreover, we consider STL tasks expressed in the fragment where ${T,T'} \in {\{ G,F\}}$. Formulas $\varphi$, as per (11a), represent temporally extended specifications over a single predicate based on the always or eventually operators, or a composition of these.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Example 1", "weight": 1.0} -->

Likewise, arbitrary nestings of the same temporal operator are part of (11a) since ${T_{\lbrack a_{1},b_{2}\rbrack}T_{\lbrack a_{2},b_{3}\rbrack}\ldots T_{\lbrack a_{N},b_{N}\rbrack}\mu^{h}} \equiv {T_{\lbrack{\sum_{n = 1}^{N}a_{n}},{\sum_{n = 1}^{N}b_{n}}\rbrack}\mu^{h}}$. Formulas $\phi$, as per (11b), represent conjunctions of formulas $\varphi$, as per (11b), to compose complex specifications (e.g. Example 1), while formulas of type $\psi$, as per (11c), represent disjunctions of formulas $\phi$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Example 1", "weight": 1.0} -->

Informally speaking, the formula $\psi = {\vee_{k}\phi_{k}}$ is satisfied if at least one of the formulas $\phi_{k}$ is satisfied.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Example 1", "weight": 1.0} -->

While the fragment in does not capture the full expressivity of the STL fragment, we focus on for the following reasons. First, synthesizing trajectories that satisfy general STL specifications is an NP-hard problem, typically tackled using Mixed-Integer Linear Programming (MILP). Although MILP solvers are sound and complete, their computational demands are often prohibitive, even for formulas within the fragment, making real-time planning infeasible. Regarding the absence of the negation operator in --- which is commonly used to enforce safety properties (e.g., "always avoid region $\mathcal{H}$") --- this limitation does not significantly reduce expressivity in our settings since safety requirements will be handled at the sampling level by rejecting trajectories entering unsafe regions of the workspace, e.g. obstacles.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Example 1", "weight": 1.0} -->

At the same time, we admittedly can handle the $\vee$ operator only at a high level of the formula such that formulas of type $F_{\lbrack a,b\rbrack}G_{\lbrack a',b'\rbrack}{({\mu^{h_{1}} \vee \mu^{h_{2}}})}$ are not within fragment and we leave this extension as future work.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Example 1", "weight": 1.0} -->

To summarize, compared to planning via MILP solvers (e.g. ), we trade off a reduction in expressivity, for a simple and effective implementation that allows for real-time planning of trajectories satisfying STL tasks in the fragment, from which a rich set of behaviors of common interest (e.g. rescue, exploration, and patrolling) can be obtained.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-B Viability and forward invariance of set-valued maps", "weight": 1.0} -->

As pointed out in the introduction, we propose to adopt a forward invariance perspective over the satisfaction of STL specifications from fragment on the same line of.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-B Viability and forward invariance of set-valued maps", "weight": 1.0} -->

Specifically, we consider encoding STL tasks from the fragment into a time-varying set derived as the level set of a non-smooth Control Barrier Function (CBF) of the form ${\mathfrak{b}}:{{{\mathbb{R}}^{n} \times {\lbrack t_{0},t_{1}\rbrack}}\rightarrow{\mathbb{R}}}$, for some interval ${\lbrack t_{0},t_{1}\rbrack} \subset {\mathbb{R}}_{\geq 0}$, with level set $\mathcal{B}:{{\lbrack t_{0},t_{1}\rbrack}\rightarrow 2^{\mathbb{X}}}$ defined as We consider the function $\mathfrak{b}$ to be Lipschitz continuous and concave on ${\mathbb{R}}^{n}$, while it is piece-wise linear on $\lbrack

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-B Viability and forward invariance of set-valued maps", "weight": 1.0} -->

We provide an analytical form of $\mathfrak{b}$ later in Section IV, from which these assumptions will be clarified.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-B Viability and forward invariance of set-valued maps", "weight": 1.0} -->

A pivotal aspect in our planning framework is the ability to synthesize dynamically feasible trajectories that evolve within a time-varying set of the form, which we ought to design in order to satisfy a given STL task. The notion of forward-invariance of set-valued maps is thus introduced.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Problem 1", "weight": 1.0} -->

Consider the dynamical system and an STL task $\phi$ as per (11b) with maximum horizon $t_{hr}{(\phi)}$. Design an algorithm that returns a trajectory $\zeta_{x}:{{\lbrack 0,{t_{hr}{(\phi)}}\rbrack}\rightarrow{\mathbb{X}}}$ such that $\zeta_{x}$ is safe and ${(\zeta_{x},0)} \models_{r}\phi$ with robustness degree $r > 0$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Problem 1", "weight": 1.0} -->

To approach Problem 1, we develop the following steps. In the next Sections IV-V, an algorithmic approach is defined to design a time-varying set $\mathcal{B}^{\phi}{(t)}$, in the form of, from a given task $\phi$, as per (11b), such that 1) the set $\mathcal{B}^{\phi}{(t)}$ is forward invariant as per Def. 1, (i.e., we show the existence of a control law that maintains systems within the set $\mathcal{B}^{\phi}{(t)}$ at every time) 2) any trajectory of system evolving in $\mathcal{B}^{\phi}{(t)}$ also satisfies $\phi$ with a given robustness $r > 0$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Problem 1", "weight": 1.0} -->

When considering the task disjunction $\psi = {\vee_{k}\phi_{k}}$, as per (11c), it is sufficient to only satisfy one of the tasks $\phi_{k}$ in order to satisfy $\psi$. Thus, we design a set $\mathcal{B}_{k}^{\phi}{(t)}$ for each $\phi_{k}$ in parallel, and the task achievable with highest robustness is selected to satisfy $\psi$, such that Problem 1 naturally genealizes to the satisfaction of tasks of type $\psi$ as per (11c).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Problem 1", "weight": 1.0} -->

Eventually, in Section VI, we generate trajectories that satisfy Problem 1 via a modified implementation of RRT^⋆^. Namely, we enforce the STL task satisfaction by generating a tree of sampled trajectories that evolves within the previously designed time-varying sets, while safety is enforced by rejecting trajectories intersecting the obstacles ${\mathcal{O}_{k} \subset {\mathbb{X}}},{k \in {\lbrack{\lbrack n_{o}\rbrack}\rbrack}}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "From STL tasks to time-varying sets: Viability", "weight": 1.0} -->

Leveraging the notion of parametric Control Barrier Functions (CBF), in this section we propose an algorithmic approach to design a viable time-varying set $\mathcal{B}^{\phi}{(t)}$, encoding an STL task $\phi$, as per, as the level set of a parametric CBF. We start first by considering the construction approach for a single task $\varphi$, as per (11a), to then generalize to the conjunction $\phi$, as per (11b). When considering a task $\psi = {\vee_{k}\phi_{k}}$, obtained as the disjunction of multiple tasks $\phi_{k}$, we apply the same construction approach separately for each $\phi_{k}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A Parametric Control Barrier Functions", "weight": 1.0} -->

where $h$ is the predicate associated to $\varphi$, as per, and the function $\gamma^{\varphi}:{{{\lbrack 0,\beta\rbrack} \times \Theta}\rightarrow{\mathbb{R}}}$ is a continuous piece-wise linear function over the sequence of switches ${(s_{i})}_{i = 1}^{3} = {(0,\alpha,\beta)}$ with $\beta \geq \alpha \geq 0$ such that for $i \in {\{ 1,2\}}$ we have An example of $\gamma^{\varphi}$ is given in Fig. 2, where $\gamma^{\varphi}$ intuitively represents a functional encoding of the temporal operators $G_{\lbrack a,b\rbrack}$ and $F_{\lbrack a,b\rbrack}$, such that the reader should associate the interval $\lbrack\alpha,\beta\rbrack$ with the interval $\lbrack

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A Parametric Control Barrier Functions", "weight": 1.0} -->

a,b\rbrack$ of the corresponding temporal operator.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A Parametric Control Barrier Functions", "weight": 1.0} -->

Since $\gamma^{\varphi}$ is defined by two piece-wise linear sections, it will be useful to introduce the index map $\Upsilon:{{\lbrack 0,\beta\rbrack}\rightarrow{\{ 1,2\}}}$ as defining which of the two linear sections of $\gamma^{\varphi}$, a given time instant $t$ lies in (see right panel in Fig. 2). At time instant $s_{2}$, we use the convention ${\Upsilon{(t)}} = 2$ without loss of generality since $\gamma^{\varphi}$ is continuous at $s_{2}$. By the form of the predicate functions, each ${\mathfrak{b}}^{\varphi}$ in is explicitly written as ${{\mathfrak{b}}^{\varphi}{({\mathbf{x}},\left.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-B Time-varying set encoding: single operator case", "weight": 1.0} -->

First, the construction rules for formulas of type $\varphi = {G_{\lbrack a,b\rbrack}\mu^{h}}$ and $\varphi = {F_{\lbrack a,b\rbrack}\mu^{h}}$ are presented.

<!-- chunk {"id": "body-0036", "role": "body", "section": "From STL tasks to time-varying sets: Forward Invariance", "weight": 1.0} -->

Now that we have analyzed the viability properties of the set $\mathcal{B}^{\phi}{(\left. t \middle| {\mathbf{θ}} \right.)}$, we want to focus on forward invariance. Namely, let the set $\mathcal{B}^{\phi}{(\left. t \middle| {\mathbf{θ}} \right.)}$ be defined by an appropriate selection of the switching times from Rules 1-4. We want to find an optimal assignment of the parameters ${\mathbf{θ}} = {\lbrack{\mathbf{\vartheta}_{1}^{T}\ldots\mathbf{\vartheta}_{n_{\phi}}^{T}}\rbrack}^{T} \in \overline{\Theta}$, such that $\mathcal{B}^{\phi}{(\left.

<!-- chunk {"id": "body-0037", "role": "body", "section": "From STL tasks to time-varying sets: Forward Invariance", "weight": 1.0} -->

t \middle| {\mathbf{θ}} \right.)}$ is forward invariant and the robustness of satisfaction of the task $\phi = {\land_{l = 1}^{n_{\phi}}\varphi_{l}}$ is maximized, by considering the general optimization problem where ${\mathfrak{g}}:{\overline{\Theta}\rightarrow{\mathbb{R}}^{n_{g}}}$ is a set of constraints on $\mathbf{θ}$ such that the optimal set of parameters ${\mathbf{θ}}^{\ast}$ solving guarantees $\mathcal{B}^{\phi}{(\left. t \middle| {\mathbf{θ}}^{\ast} \right.)}$ is viable and forward invariant while maximizing the robustness of satisfaction for $\phi$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "From STL tasks to time-varying sets: Forward Invariance", "weight": 1.0} -->

In this section, we clarify how the constraints in $\mathfrak{g}$ are defined starting first by showing constraints under which a single set $\mathcal{B}^{\varphi}{(\left. t \middle| \mathbf{\vartheta} \right.)}$ can be made forward invariant, to then generalize to the conjunction set $\mathcal{B}^{\phi}{(\left. t \middle| {\mathbf{θ}} \right.)}$, based on the result of Theorem 1.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-A Enforcing forward invariance: single task case", "weight": 1.0} -->

For convenience, we temporarily omit the dependence from the parameters $\mathbf{\vartheta}$ and drop the index $l$ of each cCBF ${\mathfrak{b}}^{\varphi}$ in the derivations. We reintroduce full notation in the presentation of the main results.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-A Enforcing forward invariance: single task case", "weight": 1.0} -->

To enforce the forward invariance of the set $\mathcal{B}^{\varphi}{(t)}$ over the interval $\lbrack 0,\beta\rbrack$ we leverage the result of Theorem 1 for which we show the existence of a control input $\zeta_{u}:{{\lbrack 0,\beta\rbrack}\rightarrow{\mathbb{U}}}$ satisfying the condition for both intervals ${{(s_{i},s_{i + 1})},i} \in {\{ 1,2\}}$ and for every initial condition ${\mathbf{x}}_{0} \in {\mathcal{B}^{\varphi}{}}$, with $\zeta_{x}:{{\lbrack 0,\beta\rbrack}\rightarrow{\mathbb{X}}}$ being the solution to under $\zeta_{u}$ such that ${\zeta_{x}{}} =

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-A Enforcing forward invariance: single task case", "weight": 1.0} -->

To this purpose, we further analyze the value of the Lie derivative over each interval $(s_{i},s_{i + 1})$. Particularly, since for all $t \in {(s_{i},s_{i + 1})}$ the function $\gamma^{\varphi}$ is differentiable, the generalized gradient of ${\mathfrak{b}}^{\varphi}$ over $(s_{i},s_{i + 1})$, $i \in {\{ 1,2\}}$ can be computed applying \[28, Prop. 6(iii), Prop. 7(iii)\] as is the set of active components of ${\mathfrak{b}}^{\varphi}{({\mathbf{x}},t)}$ defining the components exactly equal to the minimum in the definition of ${\mathfrak{b}}^{\varphi}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-A Enforcing forward invariance: single task case", "weight": 1.0} -->

In the presentation, we assume that the control input is measurable, which is a standard assumption when working with non-smooth dynamical systems (see e.g. \[33, Sec. III(B)\]), as the measurability assumption is violated only in pathological cases, which rarely occur in practice.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Example 2", "weight": 1.0} -->

The vertices of the intervals ${{{\mathbb{X}} \times {(s_{i},s_{i + 1})}},i} \in {\{ 1,2\}}$ are given by the Cartesian product of the vertices $V_{\mathbb{X}}$ (black dots) and the intervals $(s_{i},s_{i + 1})$ for a total of 8 vertices for each set $V_{\mathbb{Z}}^{i}$. $\square$ Leveraging this finite dimensional representation, Lemma 2 shows that the feasibility of over the continuum of points in ${{{\mathbb{X}} \times {(s_{i},s_{i + 1})}},i} \in {\{ 1,2\}}$, can be verified by checking a set of linear inequalities over the set of vertices ${V_{\mathbb{Z}}^{i},i} \in {\{ 1,2\}}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Trajectory planning via RRT^⋆^", "weight": 1.0} -->

Given an STL task $\phi$, this section provides a detailed explanation of how Problem 1 is approached leveraging the RRT^⋆^ planning algorithm. Loosely speaking, the approach taken consists on computing the time-varying set $\mathcal{B}^{\phi}{(t)}$, obtained as the solution to the parameters optimization problem (dropping $\mathbf{θ}$), and iteratively construct a tree of trajectories that evolves within the set $\mathcal{B}^{\phi}{(t)}$. It follows from the result of Lemma 1, that every such trajectory robustly satisfies $\phi$. The reason why an RRT^⋆^ planning approach is relevant to solve Problem 1 is that it allows to generate safe trajectories that satisfy a task $\phi$, by rejecting trajectories that can potentially hit obstacles in the environment.

<!-- chunk {"id": "body-0045", "role": "body", "section": "VI-A The algorithm", "weight": 1.0} -->

RRT^⋆^ is a planning algorithm based on the iterative construction of a tree graph $\mathcal{T}{(\mathcal{V},\mathcal{E})}$ of trajectories exploring the state space $\mathbb{X}$ (see Fig 5).

<!-- chunk {"id": "body-0046", "role": "body", "section": "VI-A The algorithm", "weight": 1.0} -->

Let ${\mathcal{O}_{k},k} \in {\lbrack{\lbrack n_{o}\rbrack}\rbrack}$, for some $n_{o} \geq 0$, represent a set of obstacles in $\mathbb{X}$ within which no valid trajectory should enter.

<!-- chunk {"id": "body-0047", "role": "body", "section": "VI-A The algorithm", "weight": 1.0} -->

Additionally, consider the root node $({\mathbf{x}}_{0},0)$ which defines the initial state from which the planning task is undertaken, and for each node index $i \in {\lbrack{\lbrack{|\mathcal{V}|}\rbrack}\rbrack}$, let the set-valued map that returns the sequence of index pairs ${(\sigma_{k},\sigma_{k + 1})} \in {{\mathbb{N}} \times {\mathbb{N}}}$ defining the unique path of length $l \geq 1$ from the root node $({\mathbf{x}}_{0},0)$ to ${({\mathbf{x}}_{i},t_{i})} \in \mathcal{V}$. For example in Fig 5-(left) we have that ${\Pi{}} = {\{{},{}\}}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "VI-A The algorithm", "weight": 1.0} -->

Based the path defined by the map $\Pi$, the cost-to-go from the root node $({\mathbf{x}}_{0},0)$ to $({\mathbf{x}}_{i},t_{i})$ is then computed by the function $\text{c2g}:{{\mathbb{N}}\rightarrow{\mathbb{R}}_{\geq 0}}$ as which intuitively represents the total length of the trajectory from the root node $({\mathbf{x}}_{0},0)$ to $({\mathbf{x}}_{i},t_{i})$ obtained by concatenating the edge trajectories $\zeta_{x}^{\sigma_{k},\sigma_{k + 1}}$. The objective is to construct a tree of trajectories with minimum cost, with respect to, that satisfy $\phi$. This is done in two main phases: an expansion phase and a rewiring phase, which we detail next.

<!-- chunk {"id": "body-0049", "role": "body", "section": "VI-A1 Initialization", "weight": 1.0} -->

At initialization (lines 2-4 in Alg. 1) the root node $({\mathbf{x}}_{0},0)$ and a desired STL task $\psi = {\vee_{k}\phi_{k}}$ is provided, encoding a set of possible tasks to be achieved. Based on this information, the time-varying sets $\mathcal{B}_{k}^{\phi}{(t)}$ are computed by solving the parameter optimization for each $\phi_{k}$. The task $\phi$ with the highest robustness is then selected for execution with the corresponding time-varying set $\mathcal{B}^{\phi}{(t)}$. Moreover, the tree $\mathcal{T}$ is initialized with $\mathcal{V} = {\{{({\mathbf{x}}_{0},0)}\}}$ and edge set $\mathcal{E} = \varnothing$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "VI-A2 Expansion phase", "weight": 1.0} -->

After initialization, the main iteration of the algorithm starts (lines 6-8 in Alg. 1).

<!-- chunk {"id": "body-0051", "role": "body", "section": "VI-A2 Expansion phase", "weight": 1.0} -->

We choose samples with maximum time $t_{hr}{(\phi)}$ as the task satisfaction is determined within this maximum time. Since $\mathcal{B}^{\phi}{(t)}$ is defined up to the time $\beta_{\phi} \leq {t_{hr}{(\phi)}}$ as per, we consider the convention ${\mathcal{B}^{\phi}{(t)}} = {\mathbb{X}}$ for all $t \in {\lbrack\beta_{\phi},{t_{hr}{(\phi)}}\rbrack}$, which is without loss of generality since the satisfaction of $\phi$ is determined within the time $\beta_{\phi}$ as per Lemma 3.

<!-- chunk {"id": "body-0052", "role": "body", "section": "VI-A2 Expansion phase", "weight": 1.0} -->

An important fact is that, thanks to the construction approach taken for $\mathcal{B}^{\phi}{(t)}$, the control input signal $\zeta_{u}^{ij}:{{\lbrack t_{i},t_{j}\rbrack}\rightarrow{\mathbb{U}}}$ generated by applying from the initial state ${\mathbf{x}}_{i}$ (with resulting state signal $\zeta_{x}^{ij}:{{\lbrack t_{i},t_{j}\rbrack}\rightarrow{\mathbb{U}}}$) always represents a feasible solution to as per Lemma 3, from which the following proposition is derived.

<!-- chunk {"id": "body-0053", "role": "body", "section": "VI-A3 Rewiring phase", "weight": 1.0} -->

Intuitively, the set $\mathcal{R} = {\text{future_nns}{({({\mathbf{x}}_{j},t_{j})})}}$ is the set of nodes within a ball of radius $\epsilon_{R} > 0$ from $({\mathbf{x}}_{j},t_{j})$ and with $t_{r} \geq t_{j}$ (see right panel in Fig. 5) and for which we want to reduce the current cost-to-go in the tree $\mathcal{T}$. The constraint $t_{r} \geq t_{j}$ serves to guarantee the time consistency in the expansion of the tree during the rewiring.

<!-- chunk {"id": "body-0054", "role": "body", "section": "VI-A3 Rewiring phase", "weight": 1.0} -->

In principle, is computationally harder compared to, due to the double boundary value constraint. Moreover, different, the feasibility of (60e) can not be guaranteed due to the boundary value constraint. At this point, a trajectory is considered for rewiring if 1) a solution to exists, 2) such solution is not in collision and 3) the cost-to-go for node $({\mathbf{x}}_{r},t_{r})$ is reduced by the rewiring through node $({\mathbf{x}}_{j},t_{j})$ as then the new trajectory $\zeta_{x}^{jr}$ is added to the tree and the old trajectory $\zeta_{x}^{pr}$ from the parent node $({\mathbf{x}}_{p},t_{p})$ of node $({\mathbf{x}}_{j},t_{j})$ in the tree $\mathcal{T}$ is removed. In any other case, the current rewiring failed, and the algorithm continues.

<!-- chunk {"id": "body-0055", "role": "body", "section": "VI-A3 Rewiring phase", "weight": 1.0} -->

The rewiring phase terminates when all possible rewiring attempts have been made, and the whole iteration is restarted.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Simulations", "weight": 1.0} -->

* Sum of solver times of for tasks ϕ1 and ϕ2 Figure 6: Trajectories planned by Alg. 1 for the room servicing scenario (a) and ISS inspection (c). The color gradient denotes time progression. On panel (b), we show the performance summary table. First, the task optimization time required to compute the set ℬϕ(t) by solving (Alg. 1 line 2) is reported with the obtained robustness. Then, the average and standard deviation of the cost/time for the first/best solution found by our RRT⋆ algorithm for the two case studies (the time is computed based on the RRT⋆ iteration Alg. 1 from line 5 to5) is reported based on a batch of 100 simulations. Simulations where run on Intel Core i7-1265U with 32GB RAM.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Simulations", "weight": 1.0} -->

We present two use cases of our proposed RRT algorithm. One involves servicing some interest points while ensuring revisit of a charging station, and one involves inspecting the International Space Station (ISS) with a deputy spacecraft over a long-horizon mission. The open source software cvxpy was employed to solve the linear program for each STL task and to transcribe the continuous time optimization programs and necessary to run Alg. 1.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Case study", "weight": 1.0} -->

0,200\rbrack}F_{\lbrack 0,100\rbrack}\mu^{h_{c}}} \land {G_{\lbrack 255,265\rbrack}\mu^{h_{1}}}}$ where the predicate functions ${h_{i},i} \in {\{ 1,2,3\}}$ represent areas of interest, while $h_{c}$ represents the charging station which should be revisited (see purple boxes in Fig. 6(a)).

<!-- chunk {"id": "body-0059", "role": "body", "section": "Case study", "weight": 1.0} -->

The difference between $\phi_{1}$ and $\phi_{2}$ is only in the order in which the regions of interest are reached. The task $\phi_{2}$ was selected for the satisfaction of $\psi$ with maximum robustness $r = 0.12$, while the resulting robustness for $\phi_{1}$ was only $r = 0.06$. The best trajectory (in terms of the cost in) obtained by our algorithm is shown in Fig. 6(a), with the color gradient representing the time progression along the trajectory. The algorithm was run for a total of 500 iterations, over 100 experiments with running time and trajectory cost summarized in Tab. 6(b). Due to the sampling-based nature of the algorithm, the obtained trajectory is only piece-wise smooth. While we did not smooth the resulting trajectory, any smoothing algorithm could be applied to further improve the final result, e.g., using splines optimization.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Case study", "weight": 1.0} -->

We consider a deputy spacecraft inspecting the International Space Station (ISS) by visiting a set of pre-selected observation regions (purple boxes in Fig. 6(c)). The deputy is modelled as a double integrator governed by the standard Clohessy--Wiltshire model.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Case study", "weight": 1.0} -->

The deputy is required to visit four observation regions (purple boxes in Fig. 6(c)) and hold the position for a period of $400s$ ($\approx 6.7$ min).

<!-- chunk {"id": "body-0062", "role": "body", "section": "Case study", "weight": 1.0} -->

The algorithm was run for a total of 500 iterations, over 100 experiments with running time and trajectory cost summarized in Tab. 6(b).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduced a sampling-based planning framework, based on RRT^⋆^, to synthesize trajectories under STL specifications with real-time performance. Namely, our approach leverages suitably constructed time-varying sets, with provable forward invariance guarantees with respect to controllable and input limited linear dynamics, to synthesize trajectories robustly satisfying a given STL task. As a next step, we aim to further expand our framework to nonlinear systems, applying techniques from spline optimization, and to broaden the class of STL specifications that we can consider.
