<!-- arxiv-full-text:v1 {"arxiv_id": "1809.07051", "source": "ar5iv"} -->

## Introduction

Two decades ago LaValle and Kuffner presented the *Rapidly-exploring Random Tree* (RRT) method for sampling-based motion planning. Even though numerous alternatives for motion planning have been proposed since then, RRT remains one of the most widely used techniques today. This is due to its simplicity and practical efficiency, especially when combined with simple heuristics.

RRT is especially useful in single-query settings, as it focuses on finding a single trajectory moving a robot from an initial state to a goal state (or region), rather than exploring the full state space of the problem, as roadmap methods do, such as PRM. To achieve this objective, RRT grows a tree, rooted at an initial state, which is periodically extended towards random state samples until the goal is reached.

Notably, RRT is well suited to complex motion planning tasks and, in particular, problems involving kinodynamic constraints. This is due to the fact that RRT can be implemented without a steering function, which is difficult to obtain for many systems with complex dynamics. (This function returns a path between two states in the absence of obstacles. It corresponds to solving a two-point boundary value problem (BVP), which may be a difficult task for many dynamical systems.) Moreover, RRT has low dependence on parameters and is easily extendable to a variety of domains (e.g., graspRRT for integrated motion and grasp planning ).

Since its introduction, numerous variations and extensions of RRT have been proposed (see, e.g., ), to allow improved performance. While RRT is not asymptotically optimal (AO) and provably does not converge to the optimal solution, it forms the basis of many AO planners, including RRT^∗^ and RRG. In particular, the probabilistic completeness (PC) of most of the aforementioned RRT-based algorithms is derived from the PC properties of RRT.

Surprisingly, it is not completely obvious under what conditions RRT is probabilistically complete, especially when using forward propagation of controls for the kinodynamic case. Indeed there has been some debate on this issue in the literature. This paper aims to address this gap.

### I-A Contribution

We provide two new proofs of PC of RRT. The first one for the purely geometric setting, where we only require that the solution path has a certain clearance from the obstacles. For the kinodynamic case with forward propagation of random controls and duration, we add mild Lipschitz-continuity conditions. This line of work lays sound foundations for arguing the probabilistic completeness of the variety of methods whose PC relies on that of RRT.

Section II describes related work and Section III proceeds with the probabilistic completeness proof for the geometric case. Section IV gives a proof for the kinodynamic setting. A discussion on further research appears in Section V.

## Related work

Sampling-based algorithms are among the state-of-the-art alternatives for robot motion planning. Since their introduction in the mid 90's (e.g., PRM, EST and RRT), they have been used in numerous robotic tasks. Sampling-based motion planners are also widely used in various fields other than robotics, such as computational biology and digital animation. There are recent reviews that provide a comprehensive coverage of developments in sampling-based motion planning.

Sampling-based planners can potentially provide the following two desirable properties; (i) *probabilistic completeness (PC)* and (ii) *Asymptotic (near)-optimality (AO)*. The former implies that the probability that the planner will return a solution (if one exists) approaches one as the number of samples tends to infinity. AO is a stronger property, as it implies that the cost of the solution returned (if one exists) by the planning algorithm (nearly) approaches the cost of the optimal solution as the number of samples tends to infinity.

AO variants of RRT and PRM, i.e., the RRT^∗^ and PRM^∗^ methods, have been introduced more recently. The same line of work introduced another AO planning algorithm, RRG, which constructs a connected PRM-like roadmap in a single-query setting. Interestingly, the PC property of both RRT^∗^ and RRG relies entirely on the PC property of RRT. Since then, many variants of RRT^∗^ and RRG have been devised, most of which inherit their PC and AO properties from RRG and RRT^∗^. A different series of planners implicitly maintain a PRM structure to guarantee AO planning. A recent paper develops precise conditions for PRM-based planners (in terms of the connection radius used) to guarantee AO.

Although RRT^∗^, PRM^∗^, and their extensions, were initially developed to deal with geometric planning, they can be extended to kinodynamic planning. This requires proper adjustments to the algorithms and the proofs (see, e.g., ). Nevertheless, these approaches require the use of a steering function, which limits their application to systems for which such a function is readily available. Recent work proposes a different type of approach, called SST, that employs only forward propagation and achieves asymptotic near-optimality. Hauser and Zhou propose a simple yet effective approach termed AO-RRT, which employs a forward-propagating RRT as a black-box component, to achieve AO.

### II-A PC of Kinodynamic RRT

LaValle and Kuffner discuss completeness of RRT in kinodynamic setting in one of the early works on the subject. While this work provides strong evidence for the PC of RRT, it only derives a proof sketch that does not fully addresses many of the complications that arise in analyzing sampling-based planners, be it a geometric or kinodynamic setting. For instance, the proofs in that paper assume the existence of "attraction sequences" and "basin regions", whose purpose is to lead the growth of the RRT tree toward the goal. It is not clear, however, whether such regions exist at all and for what types of robotic systems. It is also not clear whether the number of such regions is finite, and whether it is possible to produce samples in such regions with positive probability. Similar concerns were expressed by Caron et al..

Indeed, in 2014, Kunz and Stilman showed that one of the variants of RRT mentioned in the original RRT paper is in fact not PC. In particular, they consider RRT which employs a fixed time step (rather than random propagation time which we use here) and a best-control input strategy, which picks the control input that yields the nearest state to the random sample. For this setting they describe a counterexample consisting of a specific robotic system for which RRT will have a success rate of $0$. The reason being that the state space reachable by this type of RRT is a strict subset of the actual reachable space of the robotic system. Completeness of the other variants was left as an open question.

PC proofs of RRT under different steering functions and robot systems were presented in and. Specifically, Caron et al. consider state-based steering, which is different than forward propagation of random controls that we consider here. A setting similar to ours of random forward propagation was considered in and. It should be noted, however, that both papers consider a random-tree planner (and its extensions), which selects the next vertex to expand in a uniform and random manner among all its vertices, unlike RRT which expands the nearest neighbor toward a random sample point. Interestingly, the random tree is AO, in contrast to RRT which is not AO. Nevertheless, the selection process employed by RRT allows it to quickly explore the underlying state space when endowed with an appropriate metric.

## Probabilistic completeness of RRT: The geometric case

We start by defining useful notation in Subsection III-A and then proceed to describe RRT for the geometric case. Then, in Subsection III-B, we provide the PC proof. We call the algorithm in this section GEOM-RRT to distinguish from the kinodynamic version. The geometric case, where a steering function exists and the dimension of the control space is identical to the dimension of the state space, can be considered as a special case of the kinodynamic setting. Thus, this section can be viewed as an introduction to the more involved kinodynamic setting, which is analyzed in the following section.

### III-A Preliminaries

Let $\mathcal{X}$ be the state space, which is assumed to be ${\lbrack 0,1\rbrack}^{d}$ (a $d$-dimensional Euclidean hypercube), equipped with the standard Euclidean distance metric, whose norm we denote by $\parallel \cdot \parallel$. The free space is denoted by $\mathcal{F} \subseteq \mathcal{X}$. Given a subset $D \subseteq \mathcal{X}$ we denote by $|D|$ its Lebesgue measure. We will use $\mathcal{B}_{r}{(x)}$ to denote the ball of radius $r$ centered at $x \in {\mathbb{R}}^{d}$. Let $x_{\text{init}} \in \mathcal{F}$ denote the start state, and let $\mathcal{X}_{\text{goal}}$ be an open subset of $\mathcal{F}$ denoting the goal region. For simplicity, we assume that there exist ${\delta_{\text{goal}} > 0},{x_{\text{goal}} \in \mathcal{X}_{\text{goal}}}$, such that $\mathcal{X}_{\text{goal}} = {\mathcal{B}_{\delta_{\text{goal}}}{(x_{\text{goal}})}}$.

A motion-planning problem is implicitly defined by the triplet $(\mathcal{F},x_{\text{init}},\mathcal{X}_{\text{goal}})$. A solution to such a problem is a trajectory that moves the robot from the initial state to the goal region while avoiding collisions with obstacles. More formally, a valid trajectory is a continuous map $\pi:{{\lbrack 0,t_{\pi}\rbrack}\rightarrow\mathcal{F}}$, such that ${\pi{}} = x_{\text{init}}$ and ${\pi{(t_{\pi})}} \in \mathcal{X}_{\text{goal}}$. The clearance of $\pi$ is the maximal $\delta_{\text{clear}}$, such that ${\mathcal{B}_{\delta_{\text{clear}}}{({\pi{(t)}})}} \subseteq \mathcal{F}$ for all $t \in {\lbrack 0,t_{\pi}\rbrack}$. We require that $\delta_{\text{clear}} > 0$.

We describe in Algorithm 1 the (geometric) RRT algorithm, GEOM-RRT, based . The input for GEOM-RRT consists of an initial configuration $x_{\text{init}}$, goal region $\mathcal{X}_{\text{goal}}$, number of iterations $k$, and a steering parameter $\eta > 0$ used by the algorithm. GEOM-RRT constructs a tree $\mathcal{T}$ by preforming $k$ iterations of the following form. In each iteration, a new random sample $x_{\text{rand}}$ is returned from $\mathcal{X}$ uniformly by calling RANDOM_STATE. Then, the vertex $x_{\text{near}} \in \mathcal{T}$ that is nearest (according to $\parallel \cdot \parallel$) to $x_{\text{rand}}$ is found using NEAREST_NEIGHBOR. A new configuration $x_{\text{new}} \in \mathcal{X}$ is then returned by NEW_STATE, such that $x_{\text{new}}$ is on the line segment between $x_{\text{near}}$ and $x_{\text{rand}}$ and the distance $\|{x_{\text{near}} - x_{\text{new}}}\|$ is at most $\eta$. Finally, COLLISION_FREE($x_{\text{near}},x_{\text{new}}$) checks whether the path from $x_{\text{near}}$ to $x_{\text{new}}$ is collision free. If so, $x_{\text{new}}$ is added as a vertex to $\mathcal{T}$ and is connected by an edge from $x_{\text{near}}$.

3: xrand← RANDOM_STATE 4: xnear ← NEAREST_NEIGHBOR (xrand, 𝒯) 5: xnew← NEW_STATE(xrand, xnear, η) 6: if COLLISION_FREE(xnear, xnew) then 7: 𝒯.add_vertex(xnew) 8: 𝒯.add_edge(xnear, xnew) Algorithm 1 GEOM-RRT(xinit, 𝒳goal, k, η) To retrieve a trajectory for the robot, the single path in $\mathcal{T}$ from the root state $x_{\text{init}}$ to the goal is found. It can then be translated to a feasible, collision-free trajectory for the robot by tracing the configurations along this path.

### III-B Probabilistic completeness proof

Next we devise a PC proof for GEOM-RRT. Throughout this section we will assume that there exists a valid trajectory $\pi:{{\lbrack 0,t_{\pi}\rbrack}\rightarrow\mathcal{F}}$ with clearance $\delta_{\text{clear}} > 0$. Without loss of generality, assume that ${\pi{(t_{\pi})}} = x_{\text{goal}}$, i.e., the trajectory terminates at the center of the goal region. Denote by $L$ the (Euclidean) length of $\pi$. Also, let $\delta:={\min{\{\delta_{\text{clear}},\delta_{\text{goal}}\}}}$.

Let $m = \frac{5L}{\nu}$, where $\nu = {\min{(\delta,\eta)}}$, and $\eta$ is the steering parameter of GEOM-RRT. Then, define a sequence of $m + 1$ points ${x_{0} = {x_{\text{init}},\ldots}},{x_{m} = x_{\text{goal}}}$ along $\pi$, such that the length of the sub-path between every two consecutive points is $\nu/5$. Therefore, ${\|{x_{i} - x_{i + 1}}\|} \leqslant {\nu/5}$ for every $0 \leqslant i < m$. Next, we define a set of $m + 1$ balls of radius $\nu/5$, centered at these points, and prove that with high probability GEOM-RRT will generate a path that goes through these balls.

We start by proving Lemma 1, which will be used in the proof of Theorem 1 and specifies a condition for successfully extending the tree to the goal.

Figure 1: Illustration of the proof of Lemma 1.

### Lemma 1

Suppose that GEOM-RRT has reached $\mathcal{B}_{\nu/5}{(x_{i})}$, that is, $\mathcal{T}$ contains a vertex $x_{i}'$ such that $x_{i}' \in {\mathcal{B}_{\nu/5}{(x_{i})}}$. If a new sample $x_{\text{rand}}$ is drawn such that $x_{\text{rand}} \in {\mathcal{B}_{\nu/5}{(x_{i + 1})}}$, then the straight line segment between $x_{\text{rand}}$ and its nearest neighbor $x_{\text{near}}$ in $\mathcal{T}$ lies entirely in $\mathcal{F}$.

### Proof

Denote by $x_{\text{near}}$ the nearest neighbor of $x_{\text{rand}}$ among the RRT vertices. See Figure 1 for an illustration. Then, from the definition of $x_{\text{near}}$, it follows that ${\|{x_{\text{near}} - x_{\text{rand}}}\|} \leqslant {\|{x_{i}' - x_{\text{rand}}}\|}$, where $x_{i}' \in {\mathcal{B}_{\nu/5}{(x_{i})}}$.

We show that $x_{\text{near}}$ must lie in $\mathcal{B}_{\nu}{(x_{i})}$, implying that $\overline{x_{\text{near}}x_{\text{rand}}} \subset \mathcal{F}$, as $x_{rand} \in {\mathcal{B}_{\nu/5}{(x_{i + 1})}} \subset {\mathcal{B}_{\nu}{(x_{i})}}$. From ${\|{x_{\text{near}} - x_{\text{rand}}}\|} \leqslant {\|{x_{i}' - x_{\text{rand}}}\|}$ and the triangle inequality, we have: From the triangle inequality, we have that Hence, $x_{\text{near}} \in {\mathcal{B}_{\nu}{(x_{i})}} \subseteq \mathcal{F}$ and thus $\overline{x_{\text{near}}x_{\text{rand}}} \subset \mathcal{F}$.

Note that ${\|{x_{\text{near}} - x_{\text{rand}}}\|} \leqslant \eta$, since: ${{\|{x_{\text{rand}} - x_{\text{near}}}\|} \leqslant {\|{x_{\text{rand}} - x_{i}'}\|} \leqslant {{\|{x_{i}' - x_{i}}\|} + {\|{x_{i} - x_{i + 1}}\|} + {\|{x_{i + 1} - x_{\text{rand}}}\|}} \leqslant {3 \cdot \frac{\nu}{5}} < \nu \leqslant \eta}.$ The fact that ${\|{x_{\text{near}} - x_{\text{rand}}}\|} \leqslant \eta$, means that $x_{\text{new}} = x_{\text{rand}}$.

We now prove our main theorem.

### Theorem 1

The probability that GEOM-RRT fails to reach $\mathcal{X}_{\text{goal}}$ from $x_{\text{init}}$ after $k$ iterations is at most $ae^{- {bk}}$, for some constants ${a,b} \in {\mathbb{R}}_{> 0}$.

### Proof

Assume that $\mathcal{B}_{\nu/5}{(x_{i})}$ already contains an RRT vertex. Let $p$ be the probability that in the next iteration an RRT vertex will be added to $\mathcal{B}_{\nu/5}{(x_{i + 1})}$. Recall that due to Lemma 1, $x_{\text{rand}} \in {\mathcal{B}_{\nu/5}{(x_{i + 1})}}$ ensures that RRT will reach $\mathcal{B}_{\nu/5}{(x_{i + 1})}$. Since at each iteration $i$ we draw $x_{\text{rand}}$ uniformly at random from ${\lbrack 0,1\rbrack}^{d}$, the probability $p$ that this sample falls inside $\mathcal{B}_{\nu/5}{(x_{i + 1})}$ is equal to ${{|\mathcal{B}_{\nu/5}|}/{|{\lbrack 0,1\rbrack}^{d}|}} = {|\mathcal{B}_{\nu/5}|}$.

Figure 2: A Markov chain where the success probability p = |ℬν/5| is the probability to uniformly sample from a specific ball of radius ν/5. State (m) is a terminal state. m successful outcomes imply that the algorithm finds a path from initial state to goal, where the ith successful outcome switches from state i to state i + 1.

In order for GEOM-RRT to reach $\mathcal{X}_{\text{goal}}$ from $x_{\text{init}}$ we need to repeat this step $m$ times from $x_{i}$ to $x_{i + 1}$ for $0 \leqslant i < m$. This stochastic process can be viewed as a Markov chain (see Figure 2). Alternatively, this process can be described as $k$ Bernoulli trials with success probability $p$. The planning problem can be solved after $m$ successful outcomes (the $i$th outcome adds an RRT vertex in $\mathcal{B}_{\nu/5}{(x_{i})}$). Note that it is possible that the process ends after less than $m$ successful outcomes, i.e., by defining success to be $m$ successful outcomes we obtain an upper bound on the probability of failure.

Next, we bound the probability of failure, that is, the probability that the process does not reach state $(m)$, after $k$ steps. Let $X_{k}$ denote the number of successes in $k$ trials, then where the transitions rely on (i) $m \ll k$, (ii) $p < \frac{1}{2}$, and (iii) ${({1 - p})} \leqslant e^{- p}$.

As $p,m$ are fixed and independent of $k$, the expression $\frac{1}{{({m - 1})}!}k^{m}me^{- {pk}}$ decays to zero exponentially with $k$. Therefore, GEOM-RRT with uniform samples is probabilistically complete. ∎

## Probabilistic completeness of RRT under differential constraints

We begin by formulating the kinodynamic problem. Our assumptions on the robotic system and the environment as well as the definitions appear in Subsection IV-A and are adapted from Li et al.. Next, we describe the modifications to RRT required for solving the kinodynamic problem. Finally, in Subsection IV-B, we devise a novel PC proof for the kinodynamic RRT.

### IV-A Preliminaries

We adapt the problem attributes introduced in the previous section to accommodate the more involved structure of the kinodynamic case. The state space $\mathcal{X} \subseteq {\mathbb{R}}^{d}$ is a smooth $d$-dimensional manifold. Let $\mathcal{F} \subset \mathcal{X}$ denote the free state space. As before, we assume that there exist ${x_{\text{goal}} \in \mathcal{X}},{\delta_{\text{goal}} > 0}$, such that $\mathcal{X}_{\text{goal}} = {\mathcal{B}_{\delta_{\text{goal}}}{(x_{\text{goal}})}}$.

Let ${\mathbb{U}} \subseteq {\mathbb{R}}^{D}$ denote the space of control vectors. The given system has differential constraints of the following form: Trajectories under differential constraints are defined as follows.

### Definition 1

A valid trajectory $\pi$ of duration $t_{\pi}$ is a continuous function $\pi:{{\lbrack 0,t_{\pi}\rbrack}\rightarrow\mathcal{F}}$. A trajectory $\pi$ is generated by starting at a given state $\pi{}$ and applying a control function $\Upsilon:{{\lbrack 0,t_{\pi}\rbrack}\rightarrow{\mathbb{U}}}$ by forward integrating Equation 1.

Similar to prior work, we consider control functions that are piecewise constant:

### Definition 2

A piecewise constant control function $\overline{\Upsilon}$ with resolution $\Deltat$ is the concatenation of constant control functions ${\overline{\Upsilon}}_{i}:{{\lbrack 0,{\Deltat}\rbrack}\rightarrow u_{i}}$, where $u_{i} \in {\mathbb{U}}$, and $1 \leqslant i \leqslant k$, for some $k \in {\mathbb{N}}_{> 0}$.

We assume that the system is Lipschitz continuous for both of its arguments. That is, ${{\exists K_{u}},K_{x}} > 0$ s.t. ${{{\forall x_{0}},x_{1}} \in \mathcal{X}},{{u_{0},u_{1}} \in {\mathbb{U}}}$: We describe here the (kinodynamic) RRT algorithm, based.

3: xrand← RANDOM_STATE 4: xnear ← NEAREST_NEIGHBOR (xrand, 𝒯) 5: t← SAMPLE_DURATION(0, Tprop) 6: u← SAMPLE_CONTROL_INPUT(𝕌) 7: xnew← PROPAGATE(xnear, u, t) 8: if COLLISION_FREE(xnear, xnew) then 9: 𝒯.add_vertex(xnew) 10: 𝒯.add_edge(xnear, xnew) Algorithm 2 RRT(xinit, 𝒳goal, k, Tprop, 𝕌) The RRT algorithm in dynamic settings with no BVP solver has the following inputs: start state $x_{\text{init}}$, goal region $\mathcal{X}_{\text{goal}}$, the number of iterations $k$, the maximal time duration for propagation $T_{\text{prop}}$, and the set of control inputs $\mathbb{U}$. Our proof below assumes that $T_{\text{prop}}$ is positive and independent of $k$.

Lines 5--7 in Algorithm 2 replace line 5 in Algorithm 1. Here, a random time duration $t$ is chosen between $0$ and $T_{\text{prop}}$ as well as a random control input $u \in {\mathbb{U}}$. The algorithm uses a forward propagation approach (function PROPAGATE) from $x_{\text{near}}$: control input $u$ is applied for time duration $t$, reaching a new state $x_{\text{new}}$. Finally, if the trajectory from $x_{\text{near}}$ to $x_{\text{new}}$ is collision-free, then $x_{\text{new}}$ is added to $\mathcal{T}$ together with a connecting edge to $x_{\text{near}}$.

### IV-B Probabilistic completeness proof

We prove that RRT for a system with dynamics satisfying the aforementioned characteristics is PC. To do so, we start by proving three lemmas. The following lemma, which is an extension of Theorem 15 , bounds the distance between the endpoints of two trajectories with similar control inputs and initial positions, for the same duration.

### Lemma 2

Let $\pi,\pi'$ be two trajectories, with the corresponding control functions ${\Upsilon{(t)}},{\Upsilon'{(t)}}$. Suppose that ${x_{0} = {\pi{}}},{x_{0}' = {\pi'{}}}$. Let $T > 0$ be a time duration such that for all $t \in {\lbrack 0,T\rbrack}$ it holds that ${{\Upsilon{(t)}} = u},{{\Upsilon'{(t)}} = u'}$. That is, $\Upsilon,\Upsilon'$ remain fixed throughout $\lbrack 0,T\rbrack$. Then where ${\Deltax} = {\|{x_{0} - x_{0}'}\|}$ and ${\Deltau} = {\|{u - u'}\|}$.

### Proof

From the Lipschitz continuity assumption and the triangle inequality, we have that As in the proof of Theorem 15, we will use the Euler integration method to approximate the value of the trajectory $\pi$ at duration $T$. We divide $\lbrack 0,T\rbrack$ into $\ell \in {\mathbb{N}}_{> 0}$ pieces, each of duration $h$, i.e., $T = {\ell \cdot h}$. Let $x_{i},x_{i}'$ denote the resulting approximations of the trajectories $\pi,\pi'$ at duration $i \cdot h$. From Euler's method we have that The proof in shows that Since ${({1 + {K_{x}h}})}^{\ell} = {({1 + {{K_{x}T}/\ell}})}^{\ell} < e^{K_{x}T}$ we have that From the Lipschitz continuity assumption we have that the Euler integration method converges to the solution of the *Initial value problem*. That is, ${\forall 0} < i \leqslant \ell$, Next, we give a lower bound on the probability of a successful forward propagation step of RRT (Algorithm 2), from a given tree node, using a random control $u \in {\mathbb{U}}$ and a random duration $t \in T_{\text{prop}}$. We note that our proof uses a construction similar to \[36, proof of Theorem 17\].

### Lemma 3

Let $\pi$ be a trajectory with clearance $\delta > 0$, and duration $\tau \leqslant T_{\text{prop}}$. Suppose that the control function $\Upsilon$ is fixed for all $t \in {\lbrack 0,\tau\rbrack}$, i.e., ${\Upsilon{(t)}} = u \in {\mathbb{U}}$. Denote by $x_{i},x_{i + 1}$ the states ${\pi{}},{\pi{(\tau)}}$, respectively. Let ${r_{i},r_{i + 1}} \in {\mathbb{R}}_{> 0}$, such that $r_{i + 1} = {{4e^{K_{x}\tau}} \cdot r_{i}}$ and $r_{i + 1} \leqslant \delta$.

Suppose that the propagation step begins at state $x_{i}' \in {\mathcal{B}_{r_{i}}{(x_{i})}}$ and ends in $x_{i + 1}'$. Then for any ${\kappa \in {(0,1\rbrack}},{\epsilon_{i} \in {(0,{\kappar_{i + 1}})}}$, we have that: where $\zeta_{D}$ is the Lebesgue measure of the unit ball in ${\mathbb{R}}^{D}$ and $0 < p_{t} \leqslant 1$ is some constant.

### Proof

Consider a sequence of balls of radius $r' = {{\kappar_{i + 1}} - \epsilon_{i}}$, such that (i) the center $c_{t}$ of each ball lies on $\pi$, that is, $c_{t} = {\pi{(t)}}$ for some duration $t \in {\lbrack 0,\tau\rbrack}$, and (ii) ${\mathcal{B}_{r'}{(c_{t})}} \subset {\mathcal{B}_{\kappar_{i + 1}}{(x_{i + 1})}}$. The centers of all such balls constitute a segment of the trajectory $\pi$ whose duration is $T_{\kappa}$. See Figure 3 for an illustration.

Fix $t \in {\lbrack 0,\tau\rbrack}$, such that ${\mathcal{B}_{r'}{(c_{t})}} \subset {\mathcal{B}_{\kappar_{i + 1}}{(x_{i + 1})}}$. Additionally denote by $u_{\text{rand}}$ the random control generated by RRT, and denote by $\pi_{t}$ the trajectory corresponding to the propagation step starting at $x_{i}'$, using the control $u_{\text{rand}}$ and duration $t$. By Lemma 2, we have that: where ${\Deltau} = {\|{u - u_{\text{rand}}}\|}$. Now, we wish to find the value $\Deltau$ such that ${\|{{\pi{(t)}} - {\pi_{t}{(t)}}}\|} < {{\kappar_{i + 1}} - \epsilon_{i}}$, which would imply that ${\pi_{t}{(t)}} = x_{i + 1}' \in {\mathcal{B}_{\kappar_{i + 1}}{(x_{i + 1})}}$. Thus, we require that As $r_{i + 1} = {{4e^{K_{x}\tau}} \cdot r_{i}}$ the above constraint yields the condition which implies that To ensure that the bound holds for all possible durations $t$ in the relevant range, we should consider $t = \tau$, which is the maximal duration there, as the above expression is decreasing with $t$. That is, we enforce the following bound To summarize, we have shown that for certain values of $t$ and $u_{\text{rand}}$ it is guaranteed to have $x_{i + 1}' \in {\mathcal{B}_{\kappar_{i + 1}}{(x_{i + 1})}}$. It remains to calculate the probability of randomly choosing such values. The probability for successful propagation is at least the (a) probability of choosing a proper $t$ such that $\pi{(t)}$ is a center $c_{t}$ of a small ball ${\mathcal{B}_{r'}{(c_{t})}} \subset {\mathcal{B}_{\kappar_{i + 1}}{(x_{i + 1})}}$ times the (b) probability for choosing a control input that will cause $\pi_{t}{(t)}$ to fall inside ${\mathcal{B}_{r'}{(c_{t})}} \subset {\mathcal{B}_{\kappar_{i + 1}}{(x_{i + 1})}}$.

Clearly, the probability to choose a proper duration for propagation is at least $p_{t} = {T_{\kappa}/T_{\text{prop}}} > 0$. The probability^11^1The maxima function guarantees that the probability will be valid, that is, at least 0. to choose a proper control input is at least: Therefore, the probability for successfully propagating is at least $\rho_{i} = {p_{t} \cdot p_{u}}$. ∎ Finally, we prove a lower bound on the probability to grow the tree from a vertex in a certain ball.

### Lemma 4

Let $x \in {\mathbb{R}}^{d}$ be such that ${\mathcal{B}_{r}{(x)}} \subset \mathcal{F}$. Suppose that there exists an RRT vertex $v \in {\mathcal{B}_{{2r}/5}{(x)}}$. Let $x_{\text{near}}$ denote the nearest neighbor of $x_{\text{rand}}$ among all RRT vertices (see Algorithm 2). The probability that $x_{\text{near}} \in {\mathcal{B}_{r}{(x)}}$ is at least ${|\mathcal{B}_{r/5}|}/{|\mathcal{X}|}$.

### Proof

Suppose that there exists an RRT vertex $z \notin {\mathcal{B}_{r}{(x)}}$, as otherwise it is immediate that $x_{\text{near}} \in {\mathcal{B}_{r}{(x)}}$. We show that if $x_{\text{rand}} \in {\mathcal{B}_{r/5}{(x)}}$ then $x_{\text{near}} \in {\mathcal{B}_{r}{(x)}}$. See Figure 4 for an illustration of the proof.

Figure 4: Illustration of the proof of Lemma 4. z, v are RRT vertices. xrand is the sampled state. Its nearest neighbor will be a vertex in ℬr (x).

Observe that ${\|{x_{\text{rand}} - v}\|} \leqslant {{3r}/5}$ and ${\|{x_{\text{rand}} - z}\|} > {{4r}/5}$. Thus, $v$ is closer to $x_{\text{rand}}$ than $z$ is, implying that $z$ will not be reported as the nearest neighbor of $x_{\text{rand}}$. If $x_{\text{near}} \neq v$, then there must be another RRT vertex $y \in {\mathcal{B}_{{3r}/5}{(x_{\text{rand}})}} \subset {\mathcal{B}_{r}{(x)}}$ such that $\|{y - x_{\text{rand}}}\|$ is minimal. Finally, the probability to choose $x_{\text{rand}} \in {\mathcal{B}_{r/5}{(x)}}$ is ${|\mathcal{B}_{r/5}|}/{|\mathcal{X}|}$. ∎ Now we are ready to prove our main theorem.

### Theorem 2

Suppose that there exists a valid trajectory $\pi$ from $x_{\text{init}}$ to $x_{\text{goal}}$ lying in $\mathcal{F}$, with clearance $\delta_{\text{clear}} > 0$. Suppose that the trajectory $\pi$ has a piecewise constant control function. Then the probability that RRT fails to reach $\mathcal{X}_{\text{goal}}$ from $x_{\text{init}}$ after $k$ iterations is at most $a'e^{- {b'k}}$, for some constants ${a',b'} \in {\mathbb{R}}_{> 0}$.

### Proof

Let $\tau \leqslant T_{\text{prop}}$ be a fixed duration for which there exists $\ell \in {\mathbb{N}}_{> 0}$ such that ${\ell \cdot \tau} = {\Deltat}$.

We choose a set of times ${t_{0} = {0,t_{1},t_{2},\ldots}},{t_{m} = t_{\pi}}$, such that the difference between every two consecutive ones is $\tau$, where $t_{\pi}$ is the duration of $\pi$. Let ${x_{0} = {\pi{(t_{0})}}},{{x_{1} = {{\pi{(t_{1})}},\ldots}},{x_{m} = {\pi{(t_{m})}}}}$ be states along the path $\pi$ that are obtained after duration $t_{0},t_{1},\ldots,t_{m}$, respectively. That is, $x_{i} = {\pi{(t_{i})}}$. Obviously, $m = {t_{\pi}/\tau}$ is some constant independent of the number of samples.

We now place a set of $m + 1$ balls centered at $x_{0},\ldots,x_{m}$ such that the radius of the $i$th ball is $r_{i} = {{({4e^{K_{x}\tau}})}^{i} \cdot r_{0}}$ for $0 \leqslant i \leqslant m$. Requiring that $r_{m} = {\min{\{\delta_{\text{goal}},\delta_{\text{clear}}\}}}$, we obtain a value for the smallest radius $r_{0}$. We show that given that an RRT vertex in the $i$th ball exists, the probability $p_{i}$ that in the next iteration RRT will generate a new vertex in the $({i + 1})$st ball when propagating from a vertex in the $i$th ball is bounded from below by a positive constant. More accurately, we show that $p_{i} \geqslant p_{0}$, where $p_{0}$ is the probability that RRT will generate a new vertex in $\mathcal{B}_{r_{1}}{(x_{1})}$ when propagating from $x_{0} = x_{\text{init}}$ and it is positive. The rest of the proof is the same as that of Theorem 1.

Recall that Lemma 3 shows a lower bound $\rho_{i}$ on the probability of a successful propagation between two consecutive balls of radii $r_{i},r_{i + 1}$ placed in ${x_{i} = {\pi{(t_{i})}}},{x_{i + 1} = {\pi{(t_{i + 1})}}}$, respectively, such that ${t_{i + 1} - t_{i}} = \tau$. Assign $\kappa$ from Lemma 3 the value $2/5$ and fix $\epsilon_{i} = {\kappar_{0}} = {{2r_{0}}/5}$ for all $0 \leqslant i \leqslant m$ (note that $\epsilon_{i} \in {(0,{\kappar_{i}})}$, as required). Then $\rho_{i} > 0$ for a duration $\tau$ if If the above expression is satisfied for $i = 0$ then it also must hold for $1 \leqslant i \leqslant m$ as $r_{i} > r_{0}$. Since $e^{K_{x}\tau} \geqslant 1$ for any $\tau \geqslant 0$ it must follow that Moreover, we may set $\tau \leqslant T_{\text{prop}}$ such that there exists $\ell \in {\mathbb{N}}_{> 0}$ for which ${\ell \cdot \tau} = {\Deltat}$ holds.

Suppose that there exists an RRT vertex $v \in {\mathcal{B}_{{2r_{i}}/5}{(x_{i})}} \subset {\mathcal{B}_{r_{i}}{(x_{i})}}$. We need to bound the probability $p_{i}$ that in the next iteration the RRT tree will grow from an RRT vertex in $\mathcal{B}_{r_{i}}{(x_{i})}$, given that an RRT vertex in $\mathcal{B}_{{2r_{i}}/5}{(x_{i})}$ exists, and that the propagation step will add a vertex to $\mathcal{B}_{{2r_{i + 1}}/5}{(x_{i + 1})}$. That is, $p_{i}$ is the probability that in the next iteration both $x_{\text{near}} \in {\mathcal{B}_{r_{i}}{(x_{i})}}$ and $x_{\text{new}} \in {\mathcal{B}_{{2r_{i + 1}}/5}{(x_{i + 1})}}$.

From Lemma 4, we have that the probability $q_{i}$ that $x_{\text{near}}$ lies in $\mathcal{B}_{r_{i}}{(x_{i})}$, given that there exists an RRT vertex in $\mathcal{B}_{{2r_{i}}/5}{(x_{i})}$, is at least ${|\mathcal{B}_{r_{i}/5}|}/{|\mathcal{X}|}$. Now, since $r_{i} \geqslant r_{0}$ for $0 \leqslant i \leqslant {m - 1}$, we have that $q_{i} \geqslant q_{0} > 0$. From Lemma 3 we have that the probability for $x_{\text{new}} \in {\mathcal{B}_{{2r_{i + 1}}/5}{(x_{i + 1})}}$ is at least some positive constant $\rho_{i} > 0$. Moreover, it holds that $\rho_{i} \geqslant \rho_{0}$ for $0 \leqslant i \leqslant {m - 1}$. Hence, for all $0 \leqslant i \leqslant {m - 1}$ it holds that $p_{i} \geqslant p_{0}$, where $p_{0} = {q_{0} \cdot \rho_{0}} > 0$. The rest of the proof is the same as that of Theorem 1. ∎

## Discussion

Although our proofs assume uniform samples, they can be easily extended to samples generated using a Poisson point process, which is preferable in certain settings. An immediate extension of this work is to verify whether our proofs hold when other sampling distributions are considered, e.g., Halton sequences (see ).

Another possible direction is to further relax some of the assumptions made for kinodynamic systems, such as Lipschitz continuity. Additionally, the work raises the following challenging research question: Is it possible to extend these proofs that have a reduced set of assumptions to other sampling-based planners, or informed variants of RRT.

Finally, we mention that the following variants of RRT are not addressed in the current paper, or in the work of Kunz and Stilman: (i) random time + best-control input; (ii) fixed time + random control; (iii) random time larger than a fixed threshold + random or best control. Whether these variants are indeed probabilistically complete remains as a question for future research.
