<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Trajectory Optimization on Manifolds: A Theoretically-Guaranteed Embedded Sequential Convex Programming Approach

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Sequential Convex Programming (SCP) has recently gained popularity as a tool for trajectory optimization due to its sound theoretical properties and practical performance. Yet, most SCP-based methods for trajectory optimization are restricted to Euclidean settings, which precludes their application to problem instances where one must reason about manifold-type constraints (that is, constraints, such as loop closure, which restrict the motion of a system to a subset of the ambient space). The aim of this paper is to fill this gap by extending SCP-based trajectory optimization methods to a manifold setting. The key insight is to leverage geometric embeddings to lift a manifold-constrained trajectory optimization problem into an equivalent problem defined over a space enjoying a Euclidean structure. This insight allows one to extend existing SCP methods to a manifold setting in a fairly natural way. In particular, we present a SCP algorithm for manifold problems with refined theoretical guarantees that resemble those derived for the Euclidean setting, and demonstrate its practical performance via numerical experiments.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Trajectory optimization is a key problem in robotics, and it has thus been studied extensively through a variety of mathematical frameworks. Examples include sampling-based motion planning techniques, variational approaches such as CHOMP and STOMP, sum-of-squares methods, and sequential convex programming (SCP) techniques such as TrajOpt and GuSTO. Most of these methods, however, are restricted to Euclidean settings, which precludes their application (at least directly) to problem instances where one needs to reason about manifold-type constraints. For example, such constraints arise when the motion of a robotic system is forced to evolve on subsets of the ambient space (e.g., due to the presence of closed kinematic chains giving rise to loop closure constraints ), which are mathematically modeled as manifolds. Systems having such constraints include quadrotors, robots with camera orientation constraints, manipulator systems and robotic spacecraft, to name a few. For such systems, trajectory optimization methods must ensure that the computed trajectories lie on the relevant manifolds, preventing the planning of infeasible motions.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, this is in general challenging, as manifold-type constraints are often defined only locally (i.e., through local charts) or as implicit constraints (i.e., constraints of the type ${E{(x)}} = 0$ where $E$ is a submersion and $x$ is the state vector). As a pedagogical example, consider a two-joint manipulator. Its motion is forced to evolve on the torus ${\mathbb{T}}^{2}$ (see Figure 2), which represents a two-dimensional submanifold of ${\mathbb{R}}^{3}$. Specifically, each joint variable ($\theta_{i}$, $i = {1,2}$) evolves on the unitary circle $S^{1}$, and thus the combined evolution is on the Cartesian product $S^{1} \times S^{1}$, which is diffeomorphic to ${\mathbb{T}}^{2}$ (as characterized by implicit and nonlinear equality constraints).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite the ubiquitous presence of manifold constraints in robotic applications, the set of trajectory optimization tools that handle such constraints is relatively limited. The most naïve technique consists of simply removing, without principled justification, all manifold-type constraints, and then solving a relaxed version of the original problem in the resulting Euclidean space. Since this approach cannot guarantee trajectory feasibility, one needs to resort to post-processing before trajectory execution, often using a heuristic correction step which may be unsuccessful. This has prompted the design of optimization approaches that explicitly account for the presence of manifold constraints, including sampling-based techniques leveraging local chart analysis methods employing global chart-gluing procedures, and methods exploiting properties of specific types of manifolds (in particular, Lie groups), such as invariant metrics and projection operators. These methods, while directly accounting for the presence of manifold constraints, do not in general enjoy theoretical guarantees, and they only consider a subset of the typical constraints arising in robotic applications (e.g., control or goal region constraints are generally not addressed).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Building on the recent success of SCP-based techniques for trajectory optimization, the aim of this paper is to provide an SCP-based framework for trajectory optimization on manifolds that enjoys theoretical guarantees in terms of convergence, is general, in that it accounts for a vast class of constraints arising in robotic applications (possibly implicitly defined), and provides effective and reliable practical performance. Specifically, SCP entails successively convexifying the cost function and constraints of a nonconvex optimal control problem, seeking a solution to the original problem through a sequence of convex problems. Its attractiveness is due to high computational speed, broad applicability, and (continuous-time) theoretical guarantees. Extending SCP-based methods, primarily developed for Euclidean settings, to manifold-constrained problems is, however, challenging. In particular, when dealing with manifolds, it is challenging to make linearizations (required by SCP schemes that operate on dynamics) well-posed. The key technical idea of this paper is to leverage geometric embeddings -- that is, mappings that allow one to recover manifolds as subsets of Euclidean spaces. Leveraging embeddings provides four main advantages.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

First, it allows one to lift a manifold-constrained problem into an equivalent problem defined over a space enjoying Euclidean structure, where linearizations can be easily computed. Second, embedded problems are often easier to address than their counterparts in local coordinates since, for example, linearity can be partially maintained. Third, embeddings provide a pathway to address implicitly-defined manifolds, as the equality constraints defining them are automatically satisfied in the lifted Euclidean space without the need for explicit enforcement. Fourth, and crucially, for dynamical systems evolving on Lie groups (as it is the case for virtually all robotic systems), there is always a "natural" embedding that can, at least in principle, be leveraged. Indeed, any mechanical system can always be identified with a subgroup $G \subseteq {\mathbb{R}}^{n \times n}$ of a Cartesian product of Lie groups of matrices.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Then, the first-order equation that governs the dynamical evolution of the system is where $\Gamma$ is the geodesic spray induced by the kinetic energy and $\text{vlft}{(F_{i})}$ is the vertical lift of the generalized force $F_{i}$. This can be reinterpreted as a first-order, control-affine equation with a drift term on the space $G \times {\mathfrak{g}}$ via the identification ${TG} \cong {G \times {\mathfrak{g}}}$, where $\mathfrak{g}$ denotes the Lie algebra of $G$. A natural embedding is then the inclusion ${G \times {\mathfrak{g}}} \subseteq {\mathbb{R}}^{2n^{2}}$ (we provide explicit examples in the rest of the paper).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Statement of Contributions: In this paper, we leverage geometric embeddings to extend SCP-based methods for trajectory optimization to manifold-constrained problems. Specifically, the contribution of this paper is fourfold. First, we introduce the notion of embedded SCP, a trajectory optimization method that exploits geometric embeddings to recast optimization on manifolds as a sequence of convex optimal control problems within Euclidean spaces. Importantly, a large number of trajectory optimization problems can be "naturally" (in the sense above) embedded in Euclidean spaces, which makes this step generally straightforward. Second, leveraging such a reformulation and extending recent results on theoretical guarantees for SCP-based methods in Euclidean spaces, we provide convergence guarantees for embedded SCP in the sense of the geometric Pontryagin Maximum Principle (PMP), i.e., in the sense of convergence of both the solution and corresponding Lagrange multipliers to stationary points satisfying necessary conditions for optimality and complying with the structure of the manifold characterizing the problem.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, a key aspect of our theoretical analysis entails showing how one can avoid manifold-type constraints in the optimization process, and yet can still guarantee that the computed solution lies on the manifold -- thus providing a computationally efficient pathway to deal with implicit manifold constraints. Third, by merging techniques from indirect optimal control and differential geometry, we extend the theoretical results to a large variety of settings, e.g., goal region constraints and pointwise state constraints arising in multitask scenarios. Fourth, again inspired by analogue results in the Euclidean setting, we harness the insights gained through our theoretical analysis to develop a convergence acceleration scheme for trajectory optimization on manifolds based on shooting methods.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

One must note that while geometric embeddings allow a principled and systematic development of SCP methods for manifold-constrained problems, they come with two key drawbacks. First, embedding the manifold into an Euclidean space requires solving an optimization problem on a space having a higher dimension than the original manifold (albeit of simpler structure). Nevertheless, SCP-based algorithms scale rather well with problem dimensionality, and thus this drawback is offset by the simplification in the problem structure. Second, a straightforward and simple leveraging of embeddings is possible only if globally defined dynamical equations are at our disposal, i.e., it is easy to write for some $N \in {\mathbb{N}}$, where $M$ is a $n$-dimensional manifold. Indeed, though recovering the expression above is always theoretically possible thanks to, it could be hard to practically describe complex dynamics as in (for example, for second-order dynamics that are defined only by local coordinates). Still, most of the systems commonly used in robotics are in the form provided, which makes possible to efficiently put in practice the method developed in this paper.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Structure of the Paper: In Section II, we define the problem of trajectory optimization on manifolds and introduce the tool of embeddings that allows us to reformulate the problem in a standard Euclidean space on which we can proceed by linearization. In Section III, we introduce the embedding trajectory optimization algorithm and the primary theoretical contributions that are geometrically consistent with the structure of the manifold. Finally, Sections V and VI present experiments, conclusions and future extensions for this work.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notation: We denote by $M$ an $n$-dimensional manifold with tangent bundle $TM$ and cotangent bundle $T^{\ast}M$ (both manifolds of dimension $2n$). The tangent space of $M$ at $x \in M$ will be denoted by $T_{x}M$. Moreover, we recall that a smooth vector field on $M$ is a mapping $f:{M\rightarrow{TM}}$ such that ${f{(x)}} \in {T_{x}M}$, for every $x \in M$. The interested reader is referred to for related concepts in differential geometry.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Formulation and Sequential Convex Programming on Manifolds", "weight": 1.0} -->

We begin in Section II-A by formulating trajectory optimization for dynamical systems as an optimal control problem on manifolds. Then, in Section II-B, we introduce a procedure for appropriately embedding the original problem on manifolds into an Euclidean space. This allows us to exploit classical SCP frameworks for trajectory optimization in Euclidean spaces to solve the problem in Section II-C via SCP in Euclidean Space ‣ II Problem Formulation and Sequential Convex Programming on Manifolds ‣ Trajectory Optimization on Manifolds: A Theoretically-Guaranteed Embedded Sequential Convex Programming Approach").

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Trajectory Optimization on Generic Manifolds", "weight": 1.0} -->

In this paper we consider a continuous-time formulation to ensure that the theoretical guarantees we derive are independent of the discretization scheme that is employed. A discussion about the impact of discretization schemes on the proposed methodology will be discussed in Section III-D.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Trajectory Optimization on Generic Manifolds", "weight": 1.0} -->

Specifically, consider an initial point ${\overline{x}}_{0} \in M$ and smooth mappings $g^{i}:{M\rightarrow{\mathbb{R}}^{r_{i}}}$, $i = {1,\ldots,\ell}$, which are submersions at 0. Here, $g^{i}$ represent pointwise state constraints that are used to mathematically model multitask scenarios; in particular, $g^{\ell}$ represents goal region constraints. Without loss of generality, we require ${\text{dist}{({\overline{x}}_{0},{{(g^{\ell})}^{- 1}{}})}} > 0$, where dist is a point-set distance evaluated w.r.t. some Riemannian metric on $M$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A Trajectory Optimization on Generic Manifolds", "weight": 1.0} -->

For times $0 < t_{1} < \cdots < t_{\ell}$, we model the dynamical evolution of the system by the following drift control-affine system in $M$ where $f_{j}:{M\rightarrow{TM}}$, $j = {0,\ldots,m}$ are $C^{1}$ vector fields. The pointwise state constraints ${g^{i}{({x{(t_{i})}})}} = 0$ are useful in multitask scenarios where one seeks to jointly optimize subtrajectories connecting different waypoints. We emphasize that, as previously mentioned, the dynamics of every mechanical system can be written as in Eq. by substituting the manifold $M$ with its tangent bundle $TM$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A Trajectory Optimization on Generic Manifolds", "weight": 1.0} -->

We pose trajectory optimization as an optimal control problem with penalized state constraints. Specifically, we define the Optimal Control Problem (OCP) as minimizing the integral cost under dynamics and pointwise constraints, among all control trajectories $u \in {L^{\infty}{({\lbrack 0,t_{\ell}\rbrack},{\mathbb{R}}^{m})}}$ satisfying ${u{(t)}} \in U$ almost everywhere in $\lbrack 0,t_{\ell}\rbrack$, where the measurable set $U \subseteq {\mathbb{R}}^{m}$ represents control constraints.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-A Trajectory Optimization on Generic Manifolds", "weight": 1.0} -->

Here, $f_{u}^{0}:{M\rightarrow{\mathbb{R}}^{m}}$, $g:{M\rightarrow{\mathbb{R}}}$ are $C^{1}$, $\parallel \cdot \parallel_{R}$ is the weighted norm defined by a constant positive-definite matrix $R \in {\mathbb{R}}^{m \times m}$, and times $t_{i}$, $i = {1,\ldots,\ell}$ are fixed. We remark that hard enforcement of dynamical and intermediate/final goal set constraints is naturally imposed. The function $g = {g_{a} + {\omegag_{b}}}$ accumulates contributions from a purely state-dependant cost $g_{a}$ and state constraint penalty function $g_{b}$ (e.g., stemming from collision-avoidance constraints), weighted by $\omega \geq 1$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-A Trajectory Optimization on Generic Manifolds", "weight": 1.0} -->

Penalizing state constraints (e.g., collision avoidance) provides both theoretical and numerical benefits: it allows us to obtain theoretical guarantees in the sense of the Pontryagin Maximum Principle, necessary conditions for optimality that are stronger than standard Lagrange multiplier rules (see also Theorem 3. ‣ III-C Convergence with Geometric Consistency ‣ III Algorithm Overview and Theoretical Guarantees ‣ Trajectory Optimization on Manifolds: A Theoretically-Guaranteed Embedded Sequential Convex Programming Approach") below), and it provides numerical flexibility by often allowing simple trajectories that violate constraints such as obstacle avoidance to be exploited for initialization. Indeed, given correct design of an SCP algorithm, we can still guarantee that returned solutions satisfy state constraints up to a user-defined tolerance.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-A Trajectory Optimization on Generic Manifolds", "weight": 1.0} -->

A representative example (that will serve as running example) of a trajectory optimization problem evolving on manifolds is the minimum-energy optimal control of a spacecraft avoiding collisions in a microgravity environment, which can be stated as (under the previous formalism, $g$ provides state constraints): where $r$ is the position of the vehicle, $v$ its tangential velocity, $q$ its orientation (expressed via quaternions), $w$ its angular velocity ($\Omega{(w)}$ is the usual skew-symmetric matrix depending on $w$) and the manifold $S^{3} \subseteq {\mathbb{R}}^{4}$ characterizes quaternions. Controls are represented by the thrust $u_{1}$ and the torque $u_{2}$. A naïve way to approach our running example (Ex) would entail removing, without principled justification, the constraint $q \in S^{3}$, and then solving the relaxed problem in the resulting Euclidean space -- this could result, however, in computation of infeasible trajectories.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-A Trajectory Optimization on Generic Manifolds", "weight": 1.0} -->

Better justified approaches could exploit local charts or Lie group properties, as mentioned in Section I. However, in what follows, we demonstrate another method to tackle the implicit manifold constraint $q \in S^{3}$, that hinges on embeddings and provides a way to lift SCP methods to manifold-constrained problems.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-B Embedding the Problem into the Euclidean Space", "weight": 1.0} -->

We would like to solve (OCP) via SCP, i.e., by an iterative procedure based on the linearization of all nonlinear mappings around the solution at the previous iteration. This requires us to compose a notion of linearized vector fields of $M$ around curves. In, the authors adapt such a definition on manifolds by recasting differential equations as algebraic equations of operators in $TM$. However, in many applications concerning dynamical systems, $M$ naturally appears as subset of the Euclidean space, in which case the most intuitive linearization is the one operating in the ambient Euclidean space. This insight motivates our approach: to recast (OCP) into an appropriate Euclidean space via geometric embeddings, i.e., mappings $e:{M\rightarrow{\mathbb{R}}^{N}}$ for $N \in {\mathbb{N}}$, and then to linearize in the ambient space.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-B Embedding the Problem into the Euclidean Space", "weight": 1.0} -->

Following the previous discussion, we assume that $M$ is a closed submanifold of ${\mathbb{R}}^{N}$, for some $N \in {\mathbb{N}}$. This means that we fix a particular embedding, which is given by the canonical inclusion $e:{M\rightarrow{\mathbb{R}}^{N}}:{x\mapsto x}$. This choice is made without loss of generality because, due to Whitney-type theorems, such a mapping always exists.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-B Embedding the Problem into the Euclidean Space", "weight": 1.0} -->

This setup allows us to transform the dynamics into the following drift control-affine system in ${\mathbb{R}}^{N}$: Therefore, (OCP) can be embedded in ${\mathbb{R}}^{N}$ by considering the following Embedded Optimal Control Problem (EOCP), which consists of minimizing the integral cost under dynamics, among all control trajectories $u \in {L^{\infty}{({\lbrack 0,t_{\ell}\rbrack},{\mathbb{R}}^{m})}}$ satisfying ${u{(t)}} \in U$ almost everywhere in $\lbrack 0,t_{\ell}\rbrack$. At this step, it is worth noting that this embedding approach is justified only if solving (EOCP) is equivalent to solve (OCP). Fortunately, this is actually the case: every couple $(x,u)$ is optimal for (OCP) if and only if it is optimal for the embedded problem (EOCP).

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-B Embedding the Problem into the Euclidean Space", "weight": 1.0} -->

The validity of the whole scheme hinges on this crucial remark, which is summarized in the statement below,

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Crucially, from Lemma 1. ‣ II-B Embedding the Problem into the Euclidean Space ‣ II Problem Formulation and Sequential Convex Programming on Manifolds ‣ Trajectory Optimization on Manifolds: A Theoretically-Guaranteed Embedded Sequential Convex Programming Approach"), we see that the satisfaction of implicit manifold-type constraints for (EOCP) is induced by hard enforcement of dynamical constraints. Therefore, any numerical strategy used to solve (EOCP) must provide hard enforcement of dynamics -- otherwise, the solution trajectory is not guaranteed to lie on the manifold!

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Let us show how this embedding framework applies to our running example (Ex). It is sufficient to note that the only components of the dynamics evolving on a manifold are given by the mapping and that this mapping is also defined when ${(q,w)} \in {\mathbb{R}}^{7}$. In other words, the original dynamics is equivalent to $\left({\frac{1}{2}\Omega{(w)}q},{J^{- 1}{({u_{2} - {{w \times J}w}})}} \right)$ restricted to the subset $S^{3} \times {\mathbb{R}}^{3}$. Therefore, the embedded dynamics related to this mapping are exactly the same but extended on ${\mathbb{R}}^{7}$, which shows that the embedded version of our example problem coincides with the original (OCP). Luckily, for many robotics applications which include trajectory optimization on manifolds, (EOCP) is equivalent to (OCP), which is also the case when formulation is met.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 1", "weight": 1.0} -->

This is among the main motivations for developing such an embedded framework (see also our discussion at the end of Section II-A).

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-C Reformulating Problem (OCP) via SCP in Euclidean Space", "weight": 1.0} -->

Given that (EOCP) evolves in the Euclidean space, we may solve it using SCP. Below, we describe a particular SCP formulation that enjoys geometrically consistent theoretical convergence guarantees.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-C Reformulating Problem (OCP) via SCP in Euclidean Space", "weight": 1.0} -->

Under the assumption that $U$ is convex, we iteratively linearize the nonlinear contributions of (EOCP) around local solutions, thus recursively defining a sequence of simplified problems. Specifically, at the end of iteration $k$, assume we have some continuous curves $x_{k}:{{\lbrack 0,t_{\ell}\rbrack}\rightarrow{\mathbb{R}}^{N}}$ and $u_{k}:{{\lbrack 0,t_{\ell}\rbrack}\rightarrow{\mathbb{R}}^{m}}$, continuously extended in the interval $(0,{+ \infty})$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-C Reformulating Problem (OCP) via SCP in Euclidean Space", "weight": 1.0} -->

Then, at iteration $k + 1$, the Linearized Embedded Optimal Control Problem (LEOCP)~k+1~ consists of minimizing the new cost where, consistent with the notation of Section II-B, $G_{k} = {G_{a} + {\omega_{k}G_{b}}}$ and $h_{k}{(s)}$ is any smooth approximation of $\max{\{ 0,s\}}$ \[24, Chapter 10\]. Function $h_{k}$ provides trust-region guarantees on the updates in the state trajectories and constraints via the bounds $0 \leq \Delta_{k} \leq \Delta_{0}$ and weights $1 \leq \omega_{0} \leq \omega_{k} \leq \omega_{\max}$. The dynamical constraint for (LEOCP)~k+1~ is obtained from the linearized expansion of all nonlinear mappings.

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-C Reformulating Problem (OCP) via SCP in Euclidean Space", "weight": 1.0} -->

Ideally, SCP algorithms may vary $\Delta_{k}$ and $\omega_{k}$ at each iteration to smoothen the process towards convergence, for example as.

<!-- chunk {"id": "body-0034", "role": "body", "section": "II-C Reformulating Problem (OCP) via SCP in Euclidean Space", "weight": 1.0} -->

A convexified formulation similar to (7 via SCP in Euclidean Space ‣ II Problem Formulation and Sequential Convex Programming on Manifolds ‣ Trajectory Optimization on Manifolds: A Theoretically-Guaranteed Embedded Sequential Convex Programming Approach"))-(8 via SCP in Euclidean Space ‣ II Problem Formulation and Sequential Convex Programming on Manifolds ‣ Trajectory Optimization on Manifolds: A Theoretically-Guaranteed Embedded Sequential Convex Programming Approach")) has already been introduced. However, we stress the fact that this new formulation deals with the presence of the manifold $M$ and of pointwise state constraints. The introduction of these two new features necessitates a considerable revision of the proof of theoretical guarantees (see the Appendix).

<!-- chunk {"id": "body-0035", "role": "body", "section": "II-C Reformulating Problem (OCP) via SCP in Euclidean Space", "weight": 1.0} -->

The sequence of problems (LEOCP)~k~ is well-posed if, for each iteration $k \geq 1$, an optimal solution for (LEOCP)~k~ exists. For this, we consider the following assumptions: The set $U$ is compact and convex. Moreover, the differentials of mappings $G^{i}$, $i = {1,\ldots,\ell}$, are of full rank.

<!-- chunk {"id": "body-0036", "role": "body", "section": "II-C Reformulating Problem (OCP) via SCP in Euclidean Space", "weight": 1.0} -->

At every iteration $k \geq 1$, problem (LEOCP)~k~ is feasible.

<!-- chunk {"id": "body-0037", "role": "body", "section": "II-C Reformulating Problem (OCP) via SCP in Euclidean Space", "weight": 1.0} -->

Under these assumptions, classical existence Filippov-type arguments (applied to the reduced form of (LEOCP)~k~, see also the Appendix) show that, at each iteration $k \geq 1$, the problem (LEOCP)~k~ has at least one optimal solution. We remark that similar assumptions have been considered; in the present contribution, $(A_{1})$-$(A_{3})$ gather the assumptions in and appropriately adapt them to the context of manifolds and pointwise state constraints. Comments on their validity for very general trajectory optimization problems are easily adapted from \[6, Section II.B\].

<!-- chunk {"id": "body-0038", "role": "body", "section": "II-C Reformulating Problem (OCP) via SCP in Euclidean Space", "weight": 1.0} -->

Coming back to our running example problem (Ex), since we have already proved that the embedded problem coincides with (Ex), the linearization technique above applies directly to (Ex) without any additional step. This is particularly useful and happens every time the embedded problem is equivalent to the original one, which is common in trajectory optimization as highlighted previously. We remark that in nearly all scenarios having natural control constraints $U$, Assumptions $(A_{1})$-$(A_{3})$ are easily satisfied by (Ex).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Algorithm Overview and Theoretical Guarantees", "weight": 1.0} -->

In Section III-A, we detail a general algorithm for the solution of (OCP) which combines SCP-based procedures with the embedded framework defined previously. Its convergence guarantees, in the sense of the Pontryagin Maximum Principle, are studied in Section III-B to III-D, where we show that these respect the original structure of the manifold in (OCP), despite solving a sequence of linearized versions of the embedded problem. Notably, this procedure allows one to solve (OCP) on manifolds defined implicitly via nonlinear equalities without explicit representation.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-A SCP-based Trajectory Optimization on Manifolds", "weight": 1.0} -->

1:Input: Trajectory x0 and control u0 defined in (0, ∞). 2:Output: Solution for (LEOCP)k at iteration k. 3:Data: Parameters for the used SCP procedure. 4:Transform (OCP) into problem (EOCP) in the Euclidean space, as in Section II-B; 5:Linearize (EOCP) by defining a sequence of convex problems (LEOCP)k (an example of such linearization is given in Section II-C); 6:Select a SCP procedure on Euclidean spaces to solve the sequence of problems (LEOCP)k for (xk, uk); 7:return (xk, uk) at the last iteration. Algorithm 1 Embedded SCP (E-SCP) The first two steps in the algorithm above consist of transforming (OCP) into the optimal control problem (EOCP) on the Euclidean space via embedding procedures and successively linearizing it as detailed in Section II-B. In the third step, one finally applies some SCP scheme on Euclidean spaces.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-A SCP-based Trajectory Optimization on Manifolds", "weight": 1.0} -->

It is important to remark that E-SCP provides the user with the freedom to choose any sequential convex procedure to solve the sequence of problems (LEOCP)~k~. However, we show in Section III-B that specific choices of SCP (e.g. using hard enforcement of dynamical constraints) provide theoretical guarantees for E-SCP which are also consistent with the presence of the manifold within the original problem (OCP).

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-A SCP-based Trajectory Optimization on Manifolds", "weight": 1.0} -->

Problem (LEOCP)~1~ is linearized around an initial curve tuple $(x_{0},u_{0})$, where these initialization curves should be as close as possible to a feasible or even optimal curve for (LEOCP)~1~, although we do not require that $(x_{0},u_{0})$ is feasible for the embedded problem (EOCP). This allows one to initialize E-SCP with simple, even infeasible, guesses for solutions of (EOCP), such as a straight line in the manifold, as detailed in \[6, Section III.A\].

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-B Necessary Conditions for Optimality", "weight": 1.0} -->

Although the strategy for solving problems (LEOCP)~k~ in E-SCP is up to the user, we show that specific choices of solvers allow one to recover important theoretical guarantees for the convergence of E-SCP to critical points for the original problem (OCP) on manifolds. Specifically, we can show the convergence of E-SCP towards a trajectory satisfying first-order necessary conditions for optimality under the Pontryagin Maximum Principle when the sequence of problems (LEOCP)~k~ is chosen as in Section II-C via SCP in Euclidean Space ‣ II Problem Formulation and Sequential Convex Programming on Manifolds ‣ Trajectory Optimization on Manifolds: A Theoretically-Guaranteed Embedded Sequential Convex Programming Approach"). However, we must adapt the proof for the classical Euclidean setting to take into account the presence of both manifold and pointwise state constraints. This will be done by leveraging fundamental results from differential geometry and optimal control, i.e., Hamiltonian systems and the Pontryagin Maximum Principle with pointwise state constraints. For self-containtment, we summarize some of these results in the following discussion (see, e.g., for an extended treatment).

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-B Necessary Conditions for Optimality", "weight": 1.0} -->

By standard identifications, we denote ${(p^{0},p)} \in {T^{\ast}{({{\mathbb{R}} \times M})}}$ and we define the Hamiltonian function related to as where $\pi:{{T^{\ast}M}\rightarrow M}$ is the canonical projection and $\langle \cdot, \cdot \rangle$ denotes the duality in $T^{\ast}M$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-B Necessary Conditions for Optimality", "weight": 1.0} -->

Combining the classical geometric Pontryagin Maximum Principle with the reduction scheme for pointwise state constraints developed in yields the following extended geometric Pontryagin Maximum Principle (see Appendix for a proof sketch).

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-C Convergence with Geometric Consistency", "weight": 1.0} -->

The convergence of E-SCP can be inferred by leveraging one further commonly adopted regularity assumption concerning optimal controls: At every iteration $k \geq 1$, the optimal control $u_{k}$ of (LEOCP)~k~ is piecewise continuous in every subinterval $\lbrack 0,t_{1}\rbrack$ and $\lbrack t_{i - 1},t_{i}\rbrack$ for $i = {2,\ldots,\ell}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-D Geometric Consistency and Discrete-Time Convergence", "weight": 1.0} -->

Despite the fact that E-SCP entails solving a sequence of linearized problems for the embedded reformulation (EOCP), i.e., without explicit representation of the manifold, Lemma 1. ‣ II-B Embedding the Problem into the Euclidean Space ‣ II Problem Formulation and Sequential Convex Programming on Manifolds ‣ Trajectory Optimization on Manifolds: A Theoretically-Guaranteed Embedded Sequential Convex Programming Approach") and Corollary 1. ‣ III-C Convergence with Geometric Consistency ‣ III Algorithm Overview and Theoretical Guarantees ‣ Trajectory Optimization on Manifolds: A Theoretically-Guaranteed Embedded Sequential Convex Programming Approach") ensure that the numerical solution converges to trajectories that satisfy the manifold constraints and also ensure that the limiting solution satisfies strong first-order necessary conditions for optimality that respect the geometric structure of the original manifold.

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-D Geometric Consistency and Discrete-Time Convergence", "weight": 1.0} -->

The additional advantage of working within a continuous-time setting is that the validity of the theoretical guarantees is independent of the time-discretization scheme used to solve the ODEs. For instance, choosing schemes such as Euler or Simpson's rule lead to well well-posed convex optimization problems when the dynamics are linearized within each SCP step. With a sufficiently small time-step, one can ensure that the discrete solution provided by SCP stays close to the solution of the continuous-time problem (EOCP). Finally, Corollary 1. ‣ III-C Convergence with Geometric Consistency ‣ III Algorithm Overview and Theoretical Guarantees ‣ Trajectory Optimization on Manifolds: A Theoretically-Guaranteed Embedded Sequential Convex Programming Approach") further implies that this discretized solution stays close to the solution for the original continuous-time (OCP).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Convergence Acceleration via Differential Shooting Method", "weight": 1.0} -->

An important result provided by Theorem 3. ‣ III-C Convergence with Geometric Consistency ‣ III Algorithm Overview and Theoretical Guarantees ‣ Trajectory Optimization on Manifolds: A Theoretically-Guaranteed Embedded Sequential Convex Programming Approach") is the convergence of Pontryagin extremals related to the sequence of solutions for problem (LEOCP)~k~ in the Euclidean space towards a Pontryagin extremal related to the solution for (OCP) in the manifold, found by E-SCP. As a consequence, we can extend the acceleration procedure proposed in to the manifold and pointwise state constraint case, i.e., warm-starting shooting methods with E-SCP.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Convergence Acceleration via Differential Shooting Method", "weight": 1.0} -->

The key idea is that since the convergence of the adjoint vectors is provided in ${\mathbb{R}}^{N}$, one can leverage them to re-state a shooting method on the manifold within ${\mathbb{R}}^{N}$. However, unlike the framework proposed, the main difficulty concerns the pointwise state constraints that introduce discontinuities for the multipliers. Fortunately, we can still use this hybrid method by leveraging the knowledge of adjoint vectors at intermediate times. Assuming SCP is converging, the Lagrange multipliers $\lambda_{k}^{i}$ related to the pointwise condition ${G_{k}^{i}{({x{(t_{i})}})}} = 0$ for the finite dimensional discretization of problems (LEOCP)~k~ approximate the values $\gamma_{k}{(t_{i})}$ of the adjoint vectors related to the continuous-time (LEOCP)~k~ (see and the problem reduction provided in the Appendix).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Convergence Acceleration via Differential Shooting Method", "weight": 1.0} -->

Then, up to some subsequence, for every small $\delta > 0$, there exists an iteration $k_{\delta} \geq 1$ for which, for every iteration $k \geq k_{\delta}$, one has ${\|{{\overset{\sim}{\gamma}{(t_{i})}} - \lambda_{k}^{i}}\|} < \delta$, $i = {1,\ldots,\ell}$, where $\overset{\sim}{\gamma}$ is an adjoint vector related to the solution of (OCP) found by SCP (see Theorem 3. ‣ III-C Convergence with Geometric Consistency ‣ III Algorithm Overview and Theoretical Guarantees ‣ Trajectory Optimization on Manifolds: A Theoretically-Guaranteed Embedded Sequential Convex Programming Approach")).

<!-- chunk {"id": "body-0052", "role": "body", "section": "Convergence Acceleration via Differential Shooting Method", "weight": 1.0} -->

This means that, starting from some iteration $k \geq k_{\delta}$, we can run a shooting method to solve (OCP), initializing using $\lambda_{k}^{i}$, $i = {1,\ldots,\ell}$. At each iteration of SCP, we use the values $\lambda_{k}^{i}$ provided by the solver to initialize the shooting method until convergence is achieved. This provides a theoretically guaranteed method to accelerate convergence for SCP towards a more accurate solution.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Numerical Experiments and Discussion", "weight": 1.0} -->

In this section, we provide implementation details and examples to demonstrate various facets of our approach. We focus on three important aspects: providing comparisons between E-SCP and standard SCP on Euclidean spaces, providing comparisons between E-SCP and state-of-the-art algorithms for trajectory optimization, and analyzing convergence acceleration for E-SCP via shooting methods.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Numerical Experiments and Discussion", "weight": 1.0} -->

Simulations are provided by considering two problems: our running example (Ex), defined in Section II-A, and a trajectory optimization problem for a 7 degree-of-freedom manipulator in a cluttered environment. Consistent with our embedding framework, rather than describing the manipulator via joint angle variables (i.e., local variables), the states are characterized by tuples ${(x_{i},y_{i})} \in {\mathbb{S}}^{1}$, $i = {1,\ldots,7}$ (one for each joint), so that the system evolves in the $7$-dimensional torus, i.e., ${(x_{1},y_{1},\ldots,x_{7},y_{7})} \in {\mathbb{T}}^{7}$, which is naturally embedded in ${\mathbb{R}}^{14}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Numerical Experiments and Discussion", "weight": 1.0} -->

The dynamics are given by the kinematic equations of a manipulator, that is, each joint $i$ satisfies: where each $u_{i} \in {\mathbb{R}}$ is a control variable. As for our running example (Ex), naturally represents a dynamical system in ${\mathbb{R}}^{2}$, so that, problem (EOCP) coincides with (OCP).

<!-- chunk {"id": "body-0056", "role": "body", "section": "Numerical Experiments and Discussion", "weight": 1.0} -->

The examples and algorithms presented in this work were implemented in the Julia programming language using the GuSTO.jl package located at with optimization problems solved using Gurobi. We chose GuSTO as the SCP procedure for E-SCP (line 4 of Algorithm 1), so that Corollary 1. ‣ III-C Convergence with Geometric Consistency ‣ III Algorithm Overview and Theoretical Guarantees ‣ Trajectory Optimization on Manifolds: A Theoretically-Guaranteed Embedded Sequential Convex Programming Approach") held. For each compared SCP method, the continuous-time optimal control problem was discretized using a trapezoidal approximation of the dynamics, assuming a zero-order hold for the control, and the discrete-time cost considered for each problem was the energy $\sum_{k = 1}^{d - 1}{{\| u_{k}\|}_{2}^{2}\Deltat}$, where $d$ is the number of discretization points for the trajectory. Additionally, obstacle avoidance constraints served as our non-convex state constraints. For each set of simulations presented, we report results for 50 experiments with different start and goal configurations.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Numerical Experiments and Discussion", "weight": 1.0} -->

A SCP trial is marked as successful if the algorithm converged and the resulting solution was collision-free. We used the Bullet Physics engine to calculate signed distances for obstacle avoidance constraints or penalties. For each experiment, the variables were initialized using straight-line initializations on the manifold.

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-A Comparison with State-of-the-Art", "weight": 1.0} -->

In this section, we demonstrate the benefits obtained when using E-SCP to solve trajectory optimization problems on manifolds, rather than standard SCP approaches. More specifically, the main advantage of E-SCP is that, when considering hard enforcement of dynamical constraints, the limiting numerical solution is guaranteed to lie on the manifold, even if such a constraint is not explicitly enforced. This approach is in contrast to enforcing the nonlinear manifold-type equality constraints that appear when using standard Euclidean-based SCP approaches. Since added equality constraints increase the complexity of the problem and may adversely affect efficiency, removing manifold-type constraints in SCP provides greater flexibility in solving the sequential problems, given that these constraints are implicitly satisfied.

<!-- chunk {"id": "body-0059", "role": "body", "section": "V-A Comparison with State-of-the-Art", "weight": 1.0} -->

For this comparison, we considered the 7-DoF manipulator using 120 discretization points over a trajectory time of 30 seconds. The achieved results are shown in Table V-A. Here, comparisons are given between E-SCP with GuSTO as the internal solver, TrajOpt without any enforced manifold-type constraints, and versions of GuSTO and TrajOpt where the manifold-type constraints are penalized (denoted by SCP and TrajOpt-P, respectively, in Table V-A).

<!-- chunk {"id": "body-0060", "role": "body", "section": "V-A Comparison with State-of-the-Art", "weight": 1.0} -->

E-SCP has the best performance in reduction of dynamical constraint error (even if negligible). As can be expected, the methods that explicitly penalize the presence of the manifold achieve the highest precision for manifold-constraint satisfaction (even if also negligible). However, a keen analysis of Table V-A shows that this comes with the tradeoff that the additional state-constraint penalties produce a greater tendency to fall into high-cost local minima, since the penalization affects the way the internal convex optimization algorithm reduces the cost. Consequently, the resulting true cost of the non-penalizing algorithms is on average lower than their penalizing counterparts. In other words, E-SCP provides better optimal solutions than state-of-the-art penalization approaches.

<!-- chunk {"id": "body-0061", "role": "body", "section": "V-A Comparison with State-of-the-Art", "weight": 1.0} -->

In addition, we note that although unit-norm constraints like $x \in {\mathbb{T}}^{n}$ can be easily formulated as penalty expressions and satisfied through penalization, more complex manifold constraints (e.g., those associated with SO, closed-kinematic chains, etc.) are more difficult to formulate and satisfy in this way, and would be better handled using E-SCP. Indeed, from Theorem 3. ‣ III-C Convergence with Geometric Consistency ‣ III Algorithm Overview and Theoretical Guarantees ‣ Trajectory Optimization on Manifolds: A Theoretically-Guaranteed Embedded Sequential Convex Programming Approach") we see that manifold constraint error in E-SCP scales with the dynamical constraint error, which in turn depends only on the discretization scheme. Thus, we expect the negligible manifold constraint error for E-SCP in the previous example to carry over to more complex manifolds.

<!-- chunk {"id": "body-0062", "role": "body", "section": "V-A Comparison with State-of-the-Art", "weight": 1.0} -->

\addstackgap[4pt]\CenterstackDynamical constraint error \addstackgap[2pt]\Centerstack𝕋7 manifold constraint error \addstackgap[2pt]\CenterstackTrue cost \addstackgap[2pt]\CenterstackComputation time V-B Convergence Acceleration via Shooting Methods In this section, we provide numerical simulations that highlight convergence benefits that are obtained when E-SCP is combined with shooting methods. In particular, we consider trajectory optimization of a spacecraft having the dynamics and embedding given in (Ex) and navigating through a highly cluttered environment, using 100 discretization points over 50-second trajectories. As shown in Table II, the results are very promising: on average, the shooting method cuts significantly the number of SCP iterations required to converge to a trajectory, resulting in an overall 59.4% increase in speed. The difference in performance is made more stark by the fact that the shooting method can occasionally converge in cases where SCP is unable to converge at all due to the use of naive in-collision straight-line initialization.

<!-- chunk {"id": "body-0063", "role": "body", "section": "V-A Comparison with State-of-the-Art", "weight": 1.0} -->

Indeed, it is also interesting to note that in cases where the shooting method provides the final convergence, the final trajectory cost is always lower (if sometimes only slightly) than the cost returned by SCP alone, as the shooting method relies on the Newton method and thus tends to achieve a much higher proximity to the optimal on convergence than SCP.

<!-- chunk {"id": "body-0064", "role": "body", "section": "V-A Comparison with State-of-the-Art", "weight": 1.0} -->

\addstackgap[4pt]\CenterstackE-SCP Only \addstackgap[4pt]\CenterstackE-SCP + Shooting \addstackgap[2pt]SCP Iterations \addstackgap[2pt]Reported Cost TABLE II: Averaged results of experiments using a shooting method to accelerate the convergence of E-SCP, while resulting in lower trajectory cost than using E-SCP alone.

<!-- chunk {"id": "body-0065", "role": "body", "section": "V-A Comparison with State-of-the-Art", "weight": 1.0} -->

In this paper we provided an SCP-based method for trajectory optimization with manifold constraints. Our key insight was to leverage geometric embeddings to lift a manifold-constrained trajectory optimization problem into an equivalent problem defined over a space enjoying Euclidean structure, where SCP can be readily applied. We derived sound theoretical guarantees and validated the proposed methodology via numerical experiments. Among other benefits, our method can easily accommodate implicitly-defined manifold constraints. This work opens the field to many future avenues of research. First, we plan to study the setting with free final times ti, i = 1, …, ℓ, both from a theoretical and numerical standpoint. Second, related to the previous direction, it is of interest to design accurate numerical schemes that can handle multi-shooting methods and free final time settings. Third, we would like to leverage techniques from Lie group theory to improve performance when applying E-SCP to such specific class of submanifolds. Finally, we plan to evaluate our method on hardware platforms, such as robotic manipulators and test beds for free-flying robotic spacecraft.
