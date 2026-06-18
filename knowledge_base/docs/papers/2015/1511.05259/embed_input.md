<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Completeness of Randomized Kinodynamic Planners with State-based Steering

Topics include Kinodynamic planning, Probabilistic completeness, State-based steering, Steering function, Interpolation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proves probabilistic completeness for state-based (interpolating) kinodynamic planners under verifiable assumptions. Identifies second-order continuity as the key design requirement. Nice explanation of state-based steering and its beneficial properties as compraed with e.g. randomized action-propagation steering. Contains a great Section 2.3 on the differences between categories of steering functions.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Probabilistic completeness is an important property in motion planning. Although it has been established with clear assumptions for geometric planners, the panorama of completeness results for kinodynamic planners is still incomplete, as most existing proofs rely on strong assumptions that are difficult, if not impossible, to verify on practical systems. In this paper, we focus on an important class of kinodynamic planners, namely those that interpolate trajectories in the state space. We provide a proof of probabilistic completeness for such planners under assumptions that can be readily verified from the system's equations of motion and the user-defined interpolation function. Our proof relies crucially on a property of interpolated trajectories, termed second-order continuity (SOC), which we show is tightly related to the ability of a planner to benefit from denser sampling. We analyze the impact of this property in simulations on a low-torque pendulum. Our results show that a simple RRT using a second-order continuous interpolation swiftly finds solution, while it is impossible for the same planner using standard Bezier curves (which are not SOC) to find any solution.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A deterministic motion planner is said to be *complete* if it returns a solution whenever one exists. A *randomized* planner is said to be *probabilistically complete* if the probability of returning a solution, when there is one, tends to one as execution time goes to infinity. Theoretical as they may seem, these two notions are of notable practical interest, as proving completeness requires one to formalize the problem by hypotheses on the robot, the environment, etc. While experiments can show that a planner works for a given robot, in a given environment, for a given query, etc., a proof of completeness is a certificate that the planner works for a precise *set* of problems. The size of this set depends on how strong the assumptions required to make the proof are: the weaker the assumptions, the larger the set of solvable problems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Probabilistic completeness has been established for systems with *geometric* constraints such as *e.g.* obstacle avoidance. However, proofs for systems with *kinodynamic* constraints have yet to reach the same level of generality. Proofs available in the literature often rely on strong assumptions that are difficult to verify on practical systems (as a matter of fact, none of the previously mentioned works verified their hypotheses on non-trivial systems). In this paper, we establish probabilistic completeness (Section 3) for a large class of kinodynamic planners, namely those that interpolate trajectories in the state space. Unlike previous works, our assumptions can be readily verified from the system's equations of motion and the user-defined interpolation function.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The most important of these properties is *second-order continuity* (SOC), which states that the interpolation function varies smoothly and locally between states that are close. We evaluate the impact of this property in simulations (Section 4) on a low-torque pendulum. Experiments validate our completeness theorem, and suggest that SOC is an important design guideline for kinodynamic planners that interpolate in the state space.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Kinodynamic Constraints", "weight": 1.0} -->

Motion planning was first concerned only with *geometric* constraints such as obstacle avoidance or those imposed by the kinematic structures of manipulators. More recently, *kinodynamic* constraints, which stem from differential equations of dynamic systems, have also been taken into account.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Kinodynamic Constraints", "weight": 1.0} -->

Kinodynamic constraints are more difficult to deal with than geometric constraints because they cannot in general be expressed using only *configuration-space variables* -- such as the joint angles of a manipulator, the position and the orientation of a mobile robot, etc. Rather, they involve higher-order derivatives such as velocities and accelerations.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Kinodynamic Constraints", "weight": 1.0} -->

: non-integrable *equality* constraints on higher-order derivatives, such as found in wheeled vehicles, under-actuated manipulators or space robots.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Kinodynamic Constraints", "weight": 1.0} -->

: *inequality* constraints on higher-order derivatives such as torque bounds for manipulators, support areas or wrench cones for humanoid stability, etc.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Kinodynamic Constraints", "weight": 1.0} -->

Some authors have considered systems that are subject to both types of constraints, such as under-actuated manipulators with torque bounds.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Randomized Planners", "weight": 1.0} -->

Randomized planners such as such as Probabilistic Roadmaps (PRM) or Rapidly-exploring Random Trees (RRT) build a roadmap on the state space. Both rely on repeated random sampling of the free state space, *i.e.* states with non-colliding configurations and velocities within the system bounds. New states are connected to the roadmap using a *steering* function, which is a method used to drive the system from an initial to a goal configuration. The steering method may be imperfect, *e.g.* it may not reach the goal exactly, not take environment collisions into account, only apply to states that are sufficiently close, etc. The objective of the motion planner is to overcome these limitations, turning a local steering function into a global planning method.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Randomized Planners", "weight": 1.0} -->

PRM builds a roadmap that is later used to generate motions between many initial and final states (many-to-many queries). When new samples are drawn, they are connected to *all* neighboring states in the roadmap using the steering function, resulting in a connected graph. Meanwhile, RRT focuses on driving the system from *one* initial state $x_{\text{init}}$ towards a goal area (one-to-one queries). It grows a tree by connecting new samples to *one* neighboring state, usually their closest neighbor.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Randomized Planners", "weight": 1.0} -->

Both PRM's and RRT's *extension* step are represented by Algorithm 1, which relies on the following sub-routines (see Fig.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Randomized Planners", "weight": 1.0} -->

$\text{SAMPLE}{(S)}$: randomly sample an element from a set $S$;

<!-- chunk {"id": "body-0016", "role": "body", "section": "Randomized Planners", "weight": 1.0} -->

$\text{PARENTS}{(x,V)}$: return a set of states in the roadmap $V$ from which steering towards $x$ will be attempted;

<!-- chunk {"id": "body-0017", "role": "body", "section": "Randomized Planners", "weight": 1.0} -->

$\text{STEER}{(x,x^{\prime})}$: generate a system trajectory from $x$ towards $x^{\prime}$. If successful, return a new node $x_{\text{steer}}$ ready to be added to the roadmap. Depending on the planner, the successfulness criterion may be "reach $x^{\prime}$ exactly" or "reach a vicinity of $x^{\prime}$".

<!-- chunk {"id": "body-0018", "role": "body", "section": "Randomized Planners", "weight": 1.0} -->

0: initial node xinit, number of iterations N
3: xrand ← SAMPLE (𝒳free)
4: Xparents ← PARENTS (xrand,V)
5: for xparent in Xparents do
6: xsteer ← STEER (xparent,xrand)
7: if xsteer is a valid state then
Algorithm 1 Extension step of randomized planners (PRM or RRT)

<!-- chunk {"id": "body-0019", "role": "body", "section": "Randomized Planners", "weight": 1.0} -->

The design of each sub-routine greatly impacts the quality and even the completeness of the resulting planner. In the literature, $\text{SAMPLE}{(S)}$ is usually implemented as uniform random sampling over $S$, but some authors have suggested adaptive sampling as a way to improve planner performance. In geometric planners, $\text{PARENTS}{(q,V)}$ is usually implemented from the Euclidean norm over $\mathcal{C}$ as

<!-- chunk {"id": "body-0020", "role": "body", "section": "Randomized Planners", "weight": 1.0} -->

This choice results in the so-called Voronoi bias of RRTs. Both experiments and theoretical analysis support this choice for geometric planning, however it becomes inefficient for kinodynamic planning, as was showed by Shkolnik et al. on systems as simple as the torque-limited pendulum.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Steering Methods", "weight": 1.0} -->

This paper focuses on steering functions. These can be classified into three categories: analytical, state-based and control-based steering.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Analytical steering", "weight": 1.0} -->

This category corresponds to the ideal case when one can compute analytical trajectories respecting the system's differential constraints, which are usually called (perfect) *steering functions* in the literature. Unfortunately, it only applies to a handful of systems. Reeds and Shepp curves for cars are a notorious example of this.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Control-based steering", "weight": 1.0} -->

Generate a control $u:{{\lbrack 0,{\Deltat}\rbrack}\rightarrow\mathcal{U}_{\text{adm}}}$, where $\mathcal{U}_{\text{adm}}$ denotes the set of *admissible* controls, and compute the corresponding trajectory by *forward dynamics*. This approach has been called *incremental simulation*, *control application* or *control-space sampling* in the literature. It is widely applicable, as it only requires forward-dynamic calculations, but usually results in weak steering functions as the user has no or limited control over the destination state. In works such as, random functions $u$ are sampled from a family of primitives (*e.g.* piecewise-constant functions), a number of them are tried and only the one bringing the system closest to the target is retained. Linear-Quadratic Regulation (LQR) also qualifies as control-based steering: in this case, $u$ is computed as the optimal policy for a linear approximation of the system given a quadratic cost function.

<!-- chunk {"id": "body-0024", "role": "body", "section": "State-based steering", "weight": 1.0} -->

Interpolate a trajectory $\gamma_{\text{int}}:{{\lbrack 0,{\Deltat}\rbrack}\rightarrow\mathcal{C}}$, for instance a Bezier curve matching the initial and target configurations and velocities, and compute a control that makes the system track that trajectory. For fully-actuated system, this is typically done using *inverse dynamics*. An interpolated trajectory is rejected if no suitable control can be found. Compared to control-based steering, this approach applies to a more limited range of systems, but delivers more control over the destination state. Algorithm 2 gives the prototype of state-based steering functions.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Previous works", "weight": 1.0} -->

Randomized planners such as RRT and PRM are both simple to implement^22^2 For instance, the RRT used in the simulations of this paper was implemented in less than a hunder lines of Python code. yet efficient for geometric planning. The completeness of these planners has been established for geometric planning. In their proof, Hsu et al. quantified the problem of narrow passages in configuration space with the notion of $(\alpha,\beta)$-expansiveness. The two constants $\alpha$ and $\beta$ express a geometric lower bound on the rate of expansion of reachability areas.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Previous works", "weight": 1.0} -->

There is, however, a gap between geometric and *kinodynamic* planning in terms of proving probabilistic completeness. When Hsu et al. extended their solution to kinodynamic planning, they applied the same notion of expansiveness, but this time in the $\mathcal{X} \times \mathcal{T}$ (state and time) space with control-based steering. Their proof states that, when $\alpha > 0$ and $\beta > 0$, their planner is probabilistically complete. However, whether $\alpha > 0$ or $\alpha = 0$ in the non-geometric space $\mathcal{X} \times \mathcal{T}$ remains an open question. As a matter of fact, the problem of evaluating $(\alpha,\beta)$ has been deemed as difficult as the initial planning problem.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Previous works", "weight": 1.0} -->

In a parallel line of work, LaValle et al. provided a completeness argument for kinodynamic planning, based on the hypothesis of an *attraction sequence*, *i.e.* a covering of the state space where two major problems of kinodynamic planning are already solved: steering and antecedent selection. Unfortunately, the existence of such a sequence was not established.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Previous works", "weight": 1.0} -->

In the two previous examples, completeness is established under assumptions whose verification is at least as difficult as the motion planning problem itself. Arguably, too much of the complexity of kinodynamic planning has been abstracted into hypotheses, and these results are not strong enough to hold the claim that their planners are probabilistically complete in general. This was exemplified recently when Kunz and Stilman showed that RRTs with control-based steering were *not* probabilistically complete for a family of control inputs (namely, those with fixed time step and best-input extension). At the same time, Papadopoulos et al. established probabilistic completeness for the same planner using a different family of control inputs (randomly sampled piecewise-constant functions). The picture of completeness for kinodynamic planners therefore seems to be a nuanced one.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Previous works", "weight": 1.0} -->

Karaman et al. introduced the RRT\* path planner an extended it to kinodynamic planning with differential constraints, providing a sketch of proof for the completeness of their solution. However, they assumed that their planner had access to the optimal cost metric and optimal local steering, which restricts their analysis to systems for which these ideal solutions are known. The same authors tackled the problem from a slightly different perspective in where they supposed that the PARENTS function had access to $w$-weighted boxes, an abstraction of the system's local controlability. However, they did not show how these boxes can be computed in practice^33^3 The definition of $w$-weighted boxes is quite involved: it depends on the joint flow of vector fields spanning the tangent space of the system's manifold. and did not prove their theorem, arguing that the reasoning was similar to the one in for kinematic systems.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Previous works", "weight": 1.0} -->

To the best of our knowledge, the present paper is the first to provide a proof of probabilistic completeness for kinodynamic planners using state-based steering.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Terminology", "weight": 1.0} -->

A function is *smooth* when all its derivatives exist and are continuous. Let $\parallel \cdot \parallel$ denote the Euclidean norm. A function $f:{A\rightarrow B}$ between metric spaces is Lipschitz when there exists a constant $K_{f}$ such that

<!-- chunk {"id": "body-0032", "role": "body", "section": "Terminology", "weight": 1.0} -->

The (smallest) constant $K_{f}$ is called the Lipschitz constant of the function $f$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Terminology", "weight": 1.0} -->

Let $\mathcal{C}$ denote $n$-dimensional configuration space, where $n$ is the number of degrees of freedom of the robot. The *state space* $\mathcal{X}$ is the $2n$-dimensional manifold of configuration and velocity coordinates $x = {(q,\overset{˙}{q})}$. A trajectory is a continuous function $\gamma:{{\lbrack 0,{\Deltat}\rbrack}\rightarrow\mathcal{C}}$, and the distance of a state $x \in \mathcal{X}$ to a trajectory $\gamma$ is

<!-- chunk {"id": "body-0034", "role": "body", "section": "Terminology", "weight": 1.0} -->

where $u \in \mathcal{U}$ denotes the control input and ${x{(t)}} \in \mathcal{X}$. Let $\mathcal{U}_{\text{adm}} \subset \mathcal{U}$ denote the subset of admissible controls.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Terminology", "weight": 1.0} -->

A trajectory $\gamma$ that is solution to the differential system using only controls ${u{(t)}} \in \mathcal{U}_{\text{adm}}$ is called an *admissible* trajectory. The kinodynamic motion planning problem is to find an admissible trajectory from $q_{init}$ to $q_{goal}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "System assumptions", "weight": 1.0} -->

Our model for an $\mathcal{X}$-state randomized planner is given by Algorithm 1 using state-based steering.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

where $u \in \mathcal{U}_{\text{adm}}$ and we assume that the set of admissible controls $\mathcal{U}_{\text{adm}}$ is compact. Since torque constraints are our main concern, we will focus on

<!-- chunk {"id": "body-0038", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

which is indeed compact.^44^4 The application of our proof of completeness to an arbitrary compact set presents no technical difficulty: one can just replace ${|u|} \leq \tau_{\text{max}}$ with $d{(u,{\partial\mathcal{U}_{\text{adm}}})}$, with $\partial\mathcal{U}_{\text{adm}}$ the boundary of $\mathcal{U}_{\text{adm}}$. Using Equation avoids this level of verbosity. (Vector comparisons are component-wise.)

<!-- chunk {"id": "body-0039", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The forward dynamics function $f$ is Lipschitz continuous in both of its arguments, and its inverse $f^{- 1}$ (the inverse dynamics function $u = {f^{- 1}{(x,\overset{˙}{x})}}$) is Lipschitz in both of its arguments.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

These two assumptions are satisfied when $f$ is given by as long as the matrices $M{(q)}$ and $C{(q,\overset{˙}{q})}$ are bounded and the gravity term $g{(q)}$ is Lipschitz. Indeed, for a small displacement between $x$ and $x^{\prime}$,

<!-- chunk {"id": "body-0041", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Let us illustrate this on the double pendulum depicted in Figure 2. When both links have mass $m$ and length $l$, the gravity term

<!-- chunk {"id": "body-0042", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

is Lipschitz with constant $K_{g} = {2mgl}$, while the inertial term is bounded by $\left\| M \right\| \leq {3ml^{2}}$. When joint angular velocities are bounded by $\omega$, the norm of the Coriolis tensor is bounded by $2\omegaml^{2}$. Using, one can therefore derive the Lipschitz constant $K_{f^{- 1}}$ of the inverse dynamics function.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

Interpolated trajectories $\gamma_{\text{int}}$ are smooth Lipschitz functions, and their time-derivatives ${\overset{˙}{\gamma}}_{\text{int}}$ (*i.e.* interpolated velocities) are also Lipschitz.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Assumption 4 (Local boundedness)", "weight": 1.0} -->

Interpolated trajectories stay within a neighborhood of their start and end states, *i.e.* there exists a constant $\eta$ such that, for any ${(x,x^{\prime})} \in \mathcal{X}^{2}$, the interpolated trajectory $\gamma_{\text{int}}:{{\lbrack 0,{\Deltat}\rbrack}\rightarrow\mathcal{C}}$ resulting from $\text{INTERPOLATE}{(x,x^{\prime})}$ is included in a ball of center $x$ and radius $\eta\left\| {x^{\prime} - x} \right\|$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Assumption 5 (Discrete-acceleration convergence)", "weight": 1.0} -->

When start and end states become close, accelerations of interpolated trajectories uniformly converge to the discrete acceleration between them, *i.e.* there exists some $\nu > 0$ such that, if $\gamma_{\text{int}}:{{\lbrack 0,{\Deltat}\rbrack}\rightarrow\mathcal{C}}$ results from $\text{INTERPOLATE}{(x,x^{\prime})}$, then

<!-- chunk {"id": "body-0046", "role": "body", "section": "Assumption 5 (Discrete-acceleration convergence)", "weight": 1.0} -->

These three assumptions ensure that the planner interpolates trajectories locally and "continuously" when $x$ and $x^{\prime}$ are close. We will call them altogether *second-order continuity*, where "second-order" refers to the discrete acceleration encoded in small variations $({\Deltaq},{\Delta\overset{˙}{q}})$. This continuous behavior plays a key role in our proof of completeness, as it ensures that denser sampling will allow finding arbitrarily narrow state-space passages.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Assumption 5 (Discrete-acceleration convergence)", "weight": 1.0} -->

Let us consider again the example the double pendulum, for the interpolation function $\gamma = {\text{INTERPOLATE}{(x,x^{\prime})}}$ given by

<!-- chunk {"id": "body-0048", "role": "body", "section": "Assumption 5 (Discrete-acceleration convergence)", "weight": 1.0} -->

The duration $\Deltat$ is taken as $\Deltat_{\text{disc}}$, so that ${\gamma{}} = q$, ${\gamma{({\Deltat})}} = q^{\prime}$ and $\overset{¨}{\gamma}$ is the discrete acceleration. This interpolation, like any polynomial function, is Lipschitz smooth; Assumption 5. ‣ 3.2 Interpolation assumptions ‣ 3 Completeness Theorem ‣ Completeness of Randomized Kinodynamic Planners with State-based Steering") is verified by construction, and Assumption 4. ‣ 3.2

<!-- chunk {"id": "body-0049", "role": "body", "section": "Completeness theorem", "weight": 1.0} -->

In order to prove the theorem, we will use the following two lemmas, which are proved in A.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion of the Proof", "weight": 1.5} -->

We have effectively constructed the attraction sequence conjectured. We can now conclude the proof similarly to the strategy sketched in that paper. Let us denote by $\mathcal{B}_{t}:={\mathcal{B}{({{(\gamma,\overset{˙}{\gamma})}{(t)}},{\delta\rho})}}$, the ball of radius $\delta\rho$ centered on ${{(\gamma,\overset{˙}{\gamma})}{(t)}} \in \mathcal{X}$, where ${\delta\rho} = {O{({\deltat^{2}})}}$ as before. Suppose that the roadmap contains a state $x \in \mathcal{B}_{t}$, and let $t^{\prime}:={t + {\deltat}}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion of the Proof", "weight": 1.5} -->

If the planner samples a state $x^{\prime} \in \mathcal{B}_{t^{\prime}}$, the interpolation between $x$ and $x^{\prime}$ will be successful and $x^{\prime}$ will be added to the roadmap. Since the volume of $\mathcal{B}_{t^{\prime}}$ is non-zero, the event $\{{{\text{SAMPLE}{(\mathcal{X}_{\text{free}})}} \in \mathcal{B}_{t^{\prime}}}\}$ will happen with probability one as the number of extensions goes to infinity. At the initialization of the planner, the roadmap is reduced to $x_{\text{init}} = {({\gamma{}},{\overset{˙}{\gamma}{}})}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion of the Proof", "weight": 1.5} -->

Therefore, using the property above, by induction on the number of time steps $\deltat$, the last state $x_{\text{goal}} = {({\gamma{(T)}},{\overset{˙}{\gamma}{(T)}})}$ will be eventually added to the roadmap with probability one, and the planner will find an admissible trajectory connecting $x_{\text{init}}$ to $x_{\text{goal}}$. $\blacksquare$

<!-- chunk {"id": "body-0053", "role": "body", "section": "Completeness and state-based steering in practice", "weight": 1.0} -->

Shkolnik et al. showed how RRTs could not be directly applied to kinodynamic planning due to their poor expansion rate at the boundaries of the roadmap. They illustrated this phenomenon on the planning problem of swinging up a (single) pendulum vertically against gravity. Let us consider the same system, *i.e.* the 1-DOF single pendulum depicted in Figure 2 (A), with length $l = 20$ cm and mass $m = 8$ kg. It satisfies the system assumptions of Theorem 1 *a fortiori*, as we saw that they apply to the double pendulum.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Completeness and state-based steering in practice", "weight": 1.0} -->

We assume that the single actuator of the pendulum, corresponding to the joint angle $\theta$ in Figure 2, has limited actuation power: ${|\tau|} \leq \tau_{\max}$. The static equilibrium of the system requiring the most torque is given at $\theta = {\pm {\pi/2}}$ with $\tau = {\frac{1}{2}lmg} \approx 7.84$ Nm. Therefore, when $\tau_{\max} < 7.84$ Nm, it is impossible for the system to raise upright directly, and the pendulum rather needs to swing back and forth to accumulate kinetic energy before it can swing up. For any $\tau_{\max} > 0$, the pendulum can achieve the swingup in a finite number of swings $N$, with $N\rightarrow\infty$ as $\tau_{\max}\rightarrow 0$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Bezier interpolation", "weight": 1.0} -->

This interpolation is straightforward to implement, however it does not verify our Assumption 5. ‣ 3.2 Interpolation assumptions ‣ 3 Completeness Theorem ‣ Completeness of Randomized Kinodynamic Planners with State-based Steering"), as for instance

<!-- chunk {"id": "body-0056", "role": "body", "section": "Bezier interpolation", "weight": 1.0} -->

Our proof of completeness does not apply to such interpolators: even though a feasible trajectory is sampled as closely as possible $({{\Deltax}\rightarrow 0})$, the interpolated acceleration will *not* approximate the smooth acceleration underlying the feasible trajectory.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Second-order continuous interpolation", "weight": 1.0} -->

We call $C{(t)}$ the *second-order continuous 1-DOF* (SOC1) interpolation.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Second-order continuous interpolation", "weight": 1.0} -->

Note that this interpolation function only applies to single-DOF systems. For multi-DOF systems, the correct duration $\Deltat_{C}$ used to transfer from one state to another is different for each DOF, hence constant accelerations cannot be used. One can then apply optimization techniques or use a richer family of curves such as piecewise linear-quadratic segments.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Comparison in simulations", "weight": 1.0} -->

According to Theorem 1 and our previous discussion, a randomized planner based on Bezier interpolation is not expected to be probabilistically complete as $\tau_{\max}\rightarrow 0$, while the same planner using the SOC1 interpolation will be complete at any rate. We asserted this statement in simulations of the pendulum with RRT.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Comparison in simulations", "weight": 1.0} -->

Our implementation of RRT is that described in Algorithm 1, with the addition of the *steer-to-goal* heuristic: every $m = 100$ steps, the planner tries to steer to $x_{\text{goal}}$ rather than $x_{\text{rand}}$. This extra step speeds up convergence when the system reaches the vicinity of the goal area. We use uniform random sampling for $\text{SAMPLE}{(S)}$, while for $\text{PARENTS}{(x^{\prime},V)}$ returns the $k = 10$ nearest neighbors of $x^{\prime}$ in the roadmap $V$. All the source code used in these experiments can be accessed.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Comparison in simulations", "weight": 1.0} -->

We compared the performance of RRT with the Bezier and SOC1 interpolations, all other parameters being the same, on a single pendulum with $\tau_{\max} = 5$ Nm. The RRT-SOC1 combo found a four-swing solution after 26,300 RRT extensions, building a roadmap with 6434 nodes (Figure 3).

<!-- chunk {"id": "body-0062", "role": "body", "section": "Comparison in simulations", "weight": 1.0} -->

Meanwhile, even after one day of computations and more than 200,000 RRT extensions, the RRT-Bezier combo could not find any solution. Figure 4 shows the roadmap at 100,000 extensions (26,663 nodes). Interestingly, we can distinguish two zones in this roadmap. The first one is a dense, diamond-shape area near the downward equilibrium $\theta = 0$. It corresponds to states that are straightforward to connect by Bezier interpolation, and as expected from Proposition 1, velocities $\overset{˙}{\theta}$ in this area decrease sharply with $\theta$. The second one consists of two cones directed torwards the goal. Both areas exhibit a higher density near the axis $\overset{˙}{\theta} = 0$, which is also consistent with Proposition 1.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Comparison in simulations", "weight": 1.0} -->

The comparison of the two roadmaps is clear: with a second-order continuous interpolation, the RRT-SOC1 planner leverages additional sampling into exploration of the state space. Conversely, RRT-Bezier lacks this property (Proposition 1), and its roadmap stays confined to a subset of the pendulum's reachable space.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we provided the first "operational" proof of probabilistic completeness for a large class of randomized kinodynamic planners, namely those that interpolate state-space trajectories. We observed that an important ingredient for completeness is the "continuity" of the interpolation procedure, which we characterized by the *second-order continuity* (SOC) property. In particular, we found in simulation experiments that this property is critical to planner performances: a standard RRT with second-order continuous interpolation has no difficulty finding swingup trajectories for a low-torque pendulum, while the same RRT with Bezier interpolation (which are not SOC) could not find any solution. This experimentally confirms our completeness theorem and suggests that second-order continuity is an important design guideline for kinodynamic planners with state-based steering.
