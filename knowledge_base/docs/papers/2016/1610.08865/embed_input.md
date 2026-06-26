<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Hit-and-Run for Sampling and Planning in Non-Convex Spaces

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose the Hit-and-Run algorithm for planning and sampling problems in non-convex spaces. For sampling, we show the first analysis of the Hit-and-Run algorithm in non-convex spaces and show that it mixes fast as long as certain smoothness conditions are satisfied. In particular, our analysis reveals an intriguing connection between fast mixing and the existence of smooth measure-preserving mappings from a convex space to the non-convex space. For planning, we show advantages of Hit-and-Run compared to state-of-the-art planning methods such as Rapidly-Exploring Random Trees.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Rapidly-Exploring Random Trees (RRT) is one of the most popular planning algorithms, especially when the search space is high-dimensional and finding the optimal path is computationally expensive. RRT performs well on many problems where classical dynamic programming based algorithms, such as A\*, perform poorly. RRT is essentially an exploration algorithm, and in the most basic implementation, the algorithm even ignores the goal information, which seems to be a major reason for its success. Planning problems, especially those in robotics, often feature narrow pathways connecting large explorable regions; combined with high dimensionality, this means that finding the optimal path is usually intractable. However, RRT often provides a feasible path quickly.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although many attempts have been made to improve the basic algorithm, RRT has proven difficult to improve upon. In fact, given extra computation, repeatedly running RRT often produces competitive solutions. In this paper, we show that a simple alternative greatly improves upon RRT. We propose using the Hit-and-Run algorithm for feasible path search. Arguably simpler than RRT, the Hit-and-Run is a rapidly mixing MCMC sampling algorithm for producing a point uniformly at random from a convex space. color=blue!20!white,\]Victor: not that clear, you mean hnr is simpler that RRT? insist maybe more on what still need to be improved from RRT or say that you will detail later Not only Hit-and-Run finds a feasible path faster than RRT, it is also more robust with respect to the geometry of the space.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Before giving more details, we define the planning and sampling problems that we consider. Let $\Sigma$ be a bounded connected subset of ${\mathbb{R}}^{n}$. For points ${a,b} \in \Sigma$, we use $\lbrack a,b\rbrack$ to denote their (one-dimensional) convex hull. Given a starting point $a_{1}$ and a goal region $\mathcal{G} \subset \Sigma$, the planning problem is to find a sequence of points $\{ a_{1},a_{2},\ldots,a_{\tau}\}$ for $\tau \geq 1$ such that all points are in $\Sigma$, $a_{\tau}$ is in $\mathcal{G}$, and for $t = {2,\ldots,\tau}$, ${\lbrack a_{t - 1},a_{t}\rbrack} \subset \Sigma$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The sampling problem is to generate points uniformly at random from $\Sigma$. Sampling is often difficult, but Markov Chain Monte Carlo (MCMC) algorithms have seen empirical and theoretical success. MCMC algorithms, such as Hit-and-Run and Ball-Walk, sample a Markov Chain on $\Sigma$ that has a stationary distribution equal to the uniform distribution on $\Sigma$; then, if we run the Markov Chain long enough, the marginal distribution of the sample is guaranteed to come from a distribution exponentially close to the target distribution. Solving the sampling problem yields a solution to the planning problem; one can generate samples and terminate when $a_{t}$ hits $\mathcal{G}$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

On the other hand, the RRT algorithm iteratively builds a tree $T$ with $a_{1}$ as a root and nodes labeled as $a^{n} \in \Sigma$ and edges $\{ a^{m},a^{n}\}$ that satisfy ${\lbrack a^{m},a^{n}\rbrack} \subseteq \Sigma$. To add a point to the tree, $a^{r}$ is uniformly sampled from $\Sigma$ and its nearest neighbor $a^{n} \in T$ is computed. If ${\lbrack a^{n},a^{r}\rbrack} \subset \Sigma$, then node $a^{r}$ and edge $\lbrack a^{n},a^{r}\rbrack$ are added to $T$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Otherwise, we search for the point $a^{e} \in {\lbrack a^{n},a^{r}\rbrack}$ farthest from $a^{n}$ such that ${\lbrack a^{n},a^{e}\rbrack} \subseteq \Sigma$. Then $a^{e}$ and $\lbrack a^{n},a^{e}\rbrack$ are added to the tree. This process is continued until we add an edge terminating in $\mathcal{G}$ and the sequence of points on that branch is returned as the solution path. In the presence of dynamic constraints, a different version of RRT that makes only small local steps is used. These versions will be discussed in the experiments section.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

There are two main contributions on this paper. First, we analyze the Hit-and-Run algorithm in a non-convex space and show that the mixing time is polynomial in dimensionality as long as certain smoothness conditions are satisfied. The mixing time of Hit-and-Run for convex spaces is known to be polynomial. However, to accommodate planning problems, we focus on non-convex spaces. Our analysis reveals an intriguing connection between fast mixing and the existence of smooth measure-preserving mappings. The only existing analysis of random walk algorithms in non-convex spaces is due to Chandrasekaran et al. who analyzed Ball-Walk in star-shaped bodies.^11^1We say $S$ is star-shaped if the kernel of $S$, define by $K_{S} = {\{{x \in S}:{{\forall y} \in {S{\lbrack x,y\rbrack}} \subset S}\}}$, is nonempty. Second, we propose Hit-and-Run for planning problems as an alternative to RRT and show that it finds a feasible path quickly.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

From the mixing rate, we obtain a bound on the expected length of the solution path in the planning problem. Such performance guarantees are not available for RRT.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The current proof techniques in the analysis of Hit-and-Run heavily rely on the convexity of the space. It turns out that non-convexity is specially troubling when points are close to the boundary. We overcome these difficulties as follows. First, Lovász and Vempala show a tight isoperimetic inequality in terms of average distances instead of minimum distances. This enables us to ignore points that are sufficiently close to the boundary. Next we show that as long as points are sufficiently far from the boundary, the cross-ratio distances in the convex and non-convex spaces are closely related. Finally we show that, given a curvature assumption, if two points are close geometrically and are sufficiently far from the boundary, then their proposal distributions must be close as well. color=blue!20!white,\]Victor: what is a proposal distribution? color=blue!20!white,\]Victor: theoretical results for RRT in the litterature?

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Hit-and-Run has a number of advantages compared to RRT; it does not require random points sampled from the space (which is itself a hard problem), and it is guaranteed to reach the goal region with high probability in a polynomial number of rounds. In contrast, there are cases where RRT growth can be very slow (see the experiments sections for a discussion). Moreover, Hit-and-Run provides safer solutions, as its paths are more likely to stay away from the boundary. In contrast, a common issue with RRT solutions is that they tend to be close to the boundary. Because of this, further post-processing steps are needed to smooth the path. color=blue!20!white,\]Victor: insist more on the fact that you do not change hitand run or propose a new version just show that the original algo is the solution and you provide the analysis which is cool

<!-- chunk {"id": "body-0013", "role": "body", "section": "Sampling from Non-Convex Spaces", "weight": 1.0} -->

Most of the known results for the sampling times of the Hit-and-Run exist for convex sets only. We will think of $\Sigma$ as the image of some convex set $\Omega$ under a measure preserving, bilipschitz function $g$. The goal is to understand the relevant geometric quantities of $\Sigma$ through properties of $g$ and geometric properties of $\Omega$. We emphasize that the existence of the map $g$ and its properties are necessary for the analysis, but the actual algorithm does not need to know $g$. We formalize this assumption below as well as describe how we interact with $\Sigma$ and present a few more technical assumptions required for our analysis. We then present our main result, and follow that with some conductance results before moving on to the proof of the theorem in the next section.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 1 (Oracle Access)", "weight": 1.0} -->

Given a point $u$ and a line $\ell$ that passes through $u$, the oracle returns whether $u \in \Sigma$, and, if so, the largest connected interval in $\ell \cap \Sigma$ containing $u$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 2 (Bilipschitz Measure-Preserving Embeddings)", "weight": 1.0} -->

There exist a convex set $\Omega \subset {\mathbb{R}}^{n}$ and a bilipschitz, measure-preserving map $g$ such that $\Sigma$ is the image of $\Omega$ under $g$. That is, there exists a function $g$ with $\left| {D_{g}{(x)}} \right| = 1$ (i.e. the Jacobian has unit determinant) with constants $L_{\Sigma}$ and $L_{\Omega}$ such that, for any ${x,y} \in \Omega$, In words, $g$ is measure-preserving, $g$ is $L_{\Sigma}$-Lipschitz, and $g^{- 1}$ is $L_{\Omega}$-Lipschitz.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 2 (Bilipschitz Measure-Preserving Embeddings)", "weight": 1.0} -->

As an example, Fonseca and Parry shows that for any star-shaped space, a smooth measure-preserving embedding exists. One interesting consequence of Assumption 2. ‣ 2 Sampling from Non-Convex Spaces ‣ Hit-and-Run for Sampling and Planning in Non-Convex Spaces") is that because the mapping is measure-preserving, there must exist a pair ${x,y} \in \Omega$ such that $\left| {{g{(x)}} - {g{(y)}}} \right| \geq \left| {x - y} \right|$. Otherwise, ${\int_{\Omega}g} \leq 1$, a contradiction. Similarly, there must exist a pair ${u,v} \in \Sigma$ such that $\left| {{g^{- 1}{(u)}} - {g^{- 1}{(v)}}} \right| \geq \left| {u - v} \right|$. Thus, To simplify the analysis, we will assume that $\Omega$ is a ball with radius $r$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 2 (Bilipschitz Measure-Preserving Embeddings)", "weight": 1.0} -->

In what follows, we use $x,y,z$ to denote points in $\Omega$, and $u,v,w$ to denote points in $\Sigma$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 3 (Low Curvature)", "weight": 1.0} -->

Assumption 2. ‣ 2 Sampling from Non-Convex Spaces ‣ Hit-and-Run for Sampling and Planning in Non-Convex Spaces") does not imply low curvature, as there exist smooth measure-preserving mappings from the unit ball to a cube.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

We assume that the volume of $\Sigma$ is equal to one. We also assume that $\Sigma$ contains a Euclidean ball of radius one.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

Note that the unit ball has volume less than 1 for $n > 12$, so for small dimensional problems, we will need to relax this assumption.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

We motivate the forthcoming technical machinery by demonstrating what it can accomplish. The following theorem is the main result of the paper, and the proof makes up most of Section 3.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Analysis", "weight": 1.0} -->

This section proves Theorem 5. We begin by stating a number of useful geometrical results, which allow us to prove the two main components: an isoperimetric inequality in Section 3.2 and a total variation inequality in Section 3.3. We then combine everything in Section 3.4.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Fast Mixing Markov Chains", "weight": 1.0} -->

We rely on the notion of conductance color=blue!20!white,\]Victor: reference? as our main technical tool. This section recalls the relevant results.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Fast Mixing Markov Chains", "weight": 1.0} -->

We say that points ${u,v} \in \Sigma$ see each other if ${\lbrack u,v\rbrack} \subseteq \Sigma$. We use $\text{view}{(u)}$ to denote all points in $\Sigma$ visible from $u$. Let $\ell_{\Sigma}{(u,v)}$ denote the chord through $u$ and $v$ inside $\Sigma$ and $\left| {\ell_{\Sigma}{(u,v)}} \right|$ its length. Let $P_{u}{(A)}$ be the probability of being in set $A \subset \Sigma$ after one step of Hit-and-Run from $u$ and $f_{u}$ its density function. By an argument similar to the argument in Lemma 3 of Lovász, we can show that The conductance of the Markov process is defined as We begin with a useful conductance result that applies to general Markov Chains.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Cross-Ratio Distances", "weight": 1.0} -->

The first step is to show the relationship between cross-ratio distances in the convex and non-convex spaces. We show that these distances are close as long as points are far from the boundary. These results will be used in the proof of the main theorem in Section 3.4 to obtain an isoperimetric inequality in the non-convex space. First we define a useful quantity.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Total Variation Inequality", "weight": 1.0} -->

In this section, we show that if two points ${u,v} \in \Sigma$ are close to each other, then $P_{u}$ and $P_{v}$ are also close. First we show that if the two points are close to each other, then they have similar views.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Putting Everything Together", "weight": 1.0} -->

Next we bound the conductance of Hit-and-Run.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Planning", "weight": 1.0} -->

This section makes an empirical argument for use of the Hit-and-Run in trajectory planning. In the first of two experiments, the state space is a position vector constrained to some map illustrated by the bottom plots of Figure 2. The second experiment also includes two dimensions of velocity in the state and limits state transitions to those that respect the map as well as kinematics and requires the planning to control the system explicitly (by specifying an acceleration vector for every time step). We will show that Hit-and-Run outperforms RRT in both cases by requiring fewer transitions to reach the goal state across a wide variety of map difficulties.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Position only", "weight": 1.0} -->

The state starts at the bottom left of the spiral and the goal is the top right. Both algorithms are implemented as described in the introduction. The number of tranitions needed to reach the goal of both algorithms is plotted as a function of the width of the spiral arms; the larger the width, the easier the problem.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Position only", "weight": 1.0} -->

The results are presented in Figure 2. The top plot show the number of transitions needed by both algorithms as the width of the arms changes, averaged over 500 independent runs. We see that the Hit-and-Run outperforms RRT for all but the hardest problems, usually by a large margin. The two lower plots show the sample points produced from one run with width equal to 1.2; we see that RRT has more uniform coverage, but that Hit-and-Run has a large speedup over linear sections, therefore justifying its faster exploration.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Kinematic Planning", "weight": 1.0} -->

In this set of simulations, we constrain the state transitions to adhere to the laws of physics: the state propagates forward under kinematics until it exits the permissible map, in which case it stops inelastically at the boundary. The position map is the two-turn corridor, illustrated in the bottom plots of Figure 3. Both algorithms propose points to in the analogous manner to the previous section (where a desired speed is sampled in addition to a desired position); then, the best acceleration vector in the unit ball is calculated and the sample is propagated forward by the kinematics. If the sample point encounters the boundary, the velocity is zeroed. Both RRT and Hit-and-Run are constrained to use the same controller and the only difference is what points are proposed.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

This paper has two main contributions. First, we use a measure-preserving bilipschitz map to extend the analysis of the Hit-and-Run random walk to non-convex sets. Mixing time bounds for non-convex sets open up many applications, for example non-convex optimization via simulated annealing and similar methods. The second contribution of this paper has been to study one such application: the planning problem.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

In contrast to RRT, using Hit-and-Run for planning has stronger guarantees on the number of samples needed and faster convergence in some cases. It also avoids the need for a sampling oracle for $\Sigma$, since it combines the search with an approximate sampling oracle. One drawback is that the sample paths for Hit-and-Run have no pruning and are therefore longer than the RRT paths. Hybrid approaches that yield short paths but also explore quickly are a promising future direction.
