<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Revisiting the Asymptotic Optimality of RRT*

Topics include Motion planning, Asymptotically optimal, Probabilistically complete, Rapidly-exploring random tree star.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

This paper, from the original authors and friends, corrects some small mistakes in the theory of the asymptotic optimality results and offers new proof techniques.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

RRT* is one of the most widely used sampling-based algorithms for asymptotically-optimal motion planning. RRT* laid the foundations for optimality in motion planning as a whole, and inspired the development of numerous new algorithms in the field, many of which build upon RRT* itself. In this paper, we first identify a logical gap in the optimality proof of RRT*, which was developed by Karaman and Frazzoli. Then, we present an alternative and mathematically-rigorous proof for asymptotic optimality. Our proof suggests that the connection radius used by RRT* should be increased from γ (log n/n)1/d to γ' (log n/n)1/(d+1) in order to account n n for the additional dimension of time that dictates the samples' ordering. Here γ, γ' are constants, and n, d are the number of samples and the dimension of the problem, respectively.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

For many robot motion-planning applications, feasibility is not enough---we further desire path plans that are of high quality, reflecting a need for robots that can achieve their goals with efficiency, alacrity, and economy of motion. To this end we seek planning algorithms that can be trusted, whatever obstacle environment a robot faces, to produce optimal or near-optimal plans with minimal scenario-specific tuning. The advent of the asymptotically-optimal rapidly-exploring random tree (RRT^∗^) algorithm has ushered in a decade of theoretical and practical successes in the development of optimal sampling-based motion-planning algorithms.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although proposed in its initial form for the case of minimum-length path planning for robots without dynamic constraints, RRT^∗^ has been extended to handle kinodynamic planning problems including robotic systems governed by non-holonomic constraints, more expressive costs accounting for robot energy expenditure, and even to plan paths that minimize violation of safety rules or that otherwise balance performance considerations with safety constraints. Heuristic modifications to the core algorithm have also been demonstrated that improve practical RRT^∗^ implementations.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Each of these extensions leverages the simple yet powerful iterative local graph-rewiring technique introduced by RRT^∗^ to enable convergence to the optimal solution (as computation budget increases), provided an appropriate choice for the scaling of the rewiring radius as a function of sample count. Moreover, each of these extensions draws upon the original analysis presented in for the fundamental asymptotic scaling of this algorithm parameter; this analysis is therefore core to each of their optimality guarantees.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Contribution.* The primary contribution of this paper is an in-depth study of the theoretical analysis underpinning the asymptotic-optimality criterion for the RRT^∗^ algorithm. In revisiting this analysis, we identify a logical gap in the original proof and provide an amended proof suggesting a larger radius scaling exponent to ensure asymptotic optimality. The impact of this paper is potentially far-reaching in the large number of works that currently appeal to RRT^∗^ optimality to make their theoretical guarantees.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The paper is organized as follows. Section II provides preliminaries and a description of RRT^∗^. In Section III we review the original optimality proof of RRT^∗^ and identify a logical gap within it. In Section IV we provide the main contribution of this paper, which is an alternative proof that circumvents this logical gap. We conclude the paper in Section V.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-A Motion planning", "weight": 1.0} -->

Denote by $\mathcal{C}$ the robot's configuration space, and by $\mathcal{F} \subseteq \mathcal{C}$ the free space, i.e., the set of all collision free configurations. We assume that $\mathcal{C}$ is a subset of the Euclidean space. For simplicity, let $\mathcal{C} = {\lbrack 0,1\rbrack}^{d} \subset {\mathbb{R}}^{d}$ for some fixed $d \geq 2$. Given start and target configurations ${s,t} \in \mathcal{F}$, the *motion-planning* problem consists of finding a continuous path (curve) $\sigma:{{\lbrack 0,1\rbrack}\rightarrow\mathcal{F}}$ such that ${\sigma{}} = s$ and ${\sigma{}} = t$. That is, the robot starts its motion along $\sigma$ at $s$, and ends at $t$, while avoiding collisions.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Motion planning", "weight": 1.0} -->

An instance of the problem is defined by $(\mathcal{F},s,t)$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-B Algorithms", "weight": 1.0} -->

While our main focus in this paper is the RRT^∗^ algorithm, we also rely on the properties of the RRT algorithm, which is described first. The following description of the (geometric) RRT algorithm is based on and.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Algorithms", "weight": 1.0} -->

4: xnear ← nearest (xrand,V)
5: xnew← steer(xnear, xrand, η)
6: if collision-free(xnear, xnew) then
7: V = V ∪ {xnew}; E = E ∪ {(xnear,xnew)}
Algorithm 1 RRT(xinit:= s, xgoal:= t, n, η)

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-B Algorithms", "weight": 1.0} -->

The input for RRT (Algorithm 1) is an initial and goal configurations $x_{\text{init}},x_{\text{goal}}$, number of iterations $n$, and a steering parameter $\eta > 0$. RRT constructs a tree $G = {(V,E)}$ by performing $n$ iterations. In each iteration, a new sample $x_{\text{rand}}$ is returned from $\mathcal{F}$ uniformly at random by calling sample-free. Then, the vertex $x_{\text{near}} \in V$ that is nearest (according to $\parallel \cdot \parallel$) to $x_{\text{rand}}$ is found using nearest.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Algorithms", "weight": 1.0} -->

We proceed to describe RRT^∗^ in Algorithm 2. Every RRT^∗^ iteration begins with an RRT-style extension. The difference lies in the subsequent lines. First, RRT^∗^ attempts to connect the tree to $x_{\text{new}}$ from all its neighbors in $V$ within a $\min{\{{r{({|V|})}},\eta\}}$ vicinity (lines 7-15). Notice that the expression $r{({|V|})}$ determines the radius based on the current number of vertices in $V$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B Algorithms", "weight": 1.0} -->

In the next step, RRT^∗^ attempts to perform rewires (lines 17-21): with the addition of $x_{\text{new}}$, it may be beneficial to reroute the existing path of $x_{\text{near}}$ to use $x_{\text{new}}$. RRT^∗^ checks whether changing the parent of $x_{\text{near}}$ to be $x_{\text{new}}$ reduces $\text{cost}{(x_{\text{near}})}$. ($\text{parent}{(x_{\text{near}})}$ returns the immediate predecessor of $x_{\text{near}}$ in $G$. $\text{cost}{(x)}$ for $x \in V$ returns the cost of the path leading from $x_{\text{init}}$ to $x$ in $G$.)

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B Algorithms", "weight": 1.0} -->

4: xnear ← nearest (xrand,V) 5: xnew← steer(xnear, xrand, η) 6: if collision-free(xnear, xnew) then 7: Xnear = near (xnew,V,min {r (|V|),η}) 10: cmin = cost (xnear) + ∥xnew−xnear∥ 11: for xnear ∈ Xnear do 12: if collision-free (xnear,xnew) then 13: if cost (xnear) + ∥xnew−xnear∥ &lt; cmin then 15: cmin = cost (xnear) + ∥xnew−xnear∥ 17: for xnear ∈ Xnear do 18: if collision-free (xnew,xnear) then 19: if cost (xnew) + ∥xnear−xnew∥ &lt; cost (xnear) then 20: xparent = parent (xnear) 21: E = E ∪ {(xnew,xnear)} ∖ {(xparent,xnear)} Algorithm 2 RRT∗(xinit:= s, xgoal:= t, n,

<!-- chunk {"id": "body-0017", "role": "body", "section": "Remark 1", "weight": 1.0} -->

As mentioned above, RRT^∗^ performs extensions of the tree in a manner similar to RRT. That is, steer generates $x_{\text{new}}$, which lies on the straight line connecting $x_{\text{near}},x_{\text{rand}}$, such that ${\|{x_{\text{new}} - x_{\text{near}}}\|} \leq \eta$. Note that initially $x_{\text{new}} \neq x_{\text{rand}}$, but once the space is sufficiently covered by $G$, i.e., when $\mathcal{F} \subset {\bigcup_{v \in V}{\mathcal{B}_{\eta}{(v)}}}$, then in all the following iterations it will hold that $x_{\text{new}} = x_{\text{rand}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Remark 1", "weight": 1.0} -->

This property will be important in the analysis of RRT^∗^, as it indicates that $x_{\text{new}}$ is uniformly sampled from $\mathcal{F}$. This notion will be formalized below. For now, it is useful to note that given the same sequence of samples, RRT and RRT^∗^ will generate two (possibly distinct) graphs that have a common vertex set.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Original optimality proof", "weight": 1.0} -->

In this section we review the original proof for asymptotic optimality of RRT^∗^, and point out a logical gap. Specifically, Theorem 38 in states that if the connection radius used by RRT^∗^ is of the form

<!-- chunk {"id": "body-0020", "role": "body", "section": "Original optimality proof", "weight": 1.0} -->

where $n \in {\mathbb{N}}_{+}$, and for some constant $\gamma^{\text{KF}} > 0$, the cost of the solution obtained by RRT^∗^ converges to the robust optimum $c^{\ast}$ as $n\rightarrow\infty$, almost surely.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Review of previous proof", "weight": 1.0} -->

We provide a sketch of the original proof and identify a logical gap. We mention that our definitions of robustness (Definition 2) and robust optimum (Definition 3) are simplified versions of the ones used originally, where the latter are slightly less convenient to work with (especially in correction of the proof which we give in Section IV). We thus adapt the original proof details presented in this section to our setting. We emphasize that the logical gap is unrelated to those definitions, and our argument presented below can be easily remapped to the original formulation.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A Review of previous proof", "weight": 1.0} -->

Recall that the sample set of RRT^∗^ consists of $n$ time-labeled configurations. Denote by $\{ X_{1},\ldots,X_{n}\}$ the sample set, where indices denote the order in which the samples are drawn. Fix $\varepsilon > 0$ and let $\sigma_{\varepsilon}$ be a robust solution path such that ${c{(\sigma_{\varepsilon})}} \leq {{({1 + \varepsilon})}c^{\ast}}$. The proof constructs a sequence of $M_{n} \leq n$ identical balls $B_{n,1},\ldots,B_{n,M_{n}}$ that are centered on some equally-spaced points along $\sigma_{\varepsilon}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A Review of previous proof", "weight": 1.0} -->

Furthermore, it is shown in that given $x_{i} \in B_{n,i}$ for every $1 \leq i \leq M_{n}$, the length of the path $\sigma$ connecting each $x_{i}$ to the point in the next ball with a straight line converges (as $n\rightarrow\infty$) to the length of $\sigma_{\varepsilon}$ (see Figure 1).

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A Review of previous proof", "weight": 1.0} -->

The proof establishes that if for every $1 \leq i < M_{n}$ there exist $X_{j_{i}},X_{j_{i + 1}}$ such that (i) ${X_{j_{i}} \in B_{n,i}},{X_{j_{i + 1}} \in B_{n,{i + 1}}}$ and (ii) $j_{i} < j_{i + 1}$, then RRT^∗^ is asymptotically optimal (see Section G.3 in ). The rationale behind these conditions is as follows. Condition (i) makes sure that the optimal path is approximated by samples drawn by RRT^∗^, i.e., for every point along $\sigma_{\varepsilon}$ there is a sample point in its vicinity.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A Review of previous proof", "weight": 1.0} -->

Condition (ii) ensures that RRT^∗^ will have the opportunity to add a directed edge from $X_{j_{i}}$ to $X_{j_{i + 1}}$: as $X_{j_{i + 1}}$ is sampled after $X_{j_{i}}$ then RRT^∗^ would consider drawing a directed edge from the latter to the former, considering the fact that $X_{j_{i}} \in {\text{near}{(X_{j_{i + 1}},V,{\min{\{{r{(n)}},\eta\}}})}}$ (this is formalized in Claim 1 below). Observe that $r{(n)}$ is used as a conservative lower-bound for $r{({|V|})}$ throughout, as we do too.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A Review of previous proof", "weight": 1.0} -->

Consequently, the proof deduces that if these conditions are met RRT^∗^ is guaranteed to find a solution with cost at most $c^{\ast}{({1 + \varepsilon})}$ with probability that converges to $1$ as $n\rightarrow\infty$. In particular, denote by $X_{j_{1}},\ldots,X_{j_{M_{n}}}$ the sequence of samples satisfying the conditions above, and let $\sigma_{n}$ be a path that is induced by those $M_{n}$ samples in the prescribed order. Then the claim is that the solution returned by RRT^∗^ is of length $c{(\sigma_{n})}$, if not shorter.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B A logical gap", "weight": 1.0} -->

We identify an issue with the proof technique described above, and in particular with the conditions (i) and (ii). We assert that the line of reasoning mentioned above overlooks the fact that the existence of pairwise sequential samples does not directly imply the existence of a whole chain of samples with a proper ordering such that a path in $G$ traces through all the balls in sequence.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B A logical gap", "weight": 1.0} -->

Now assume that $X^{B} = \varnothing$. We can choose the current structure of $G$ and the locations of $X_{j_{i}},X_{j_{i + 1}^{\prime}}$ such that the only directed edge that is added in iteration $j_{i}$ is $(X_{j_{i + 1}^{\prime}},X_{j_{i}})$, i.e., from $X_{j_{i + 1}^{\prime}}$ to $X_{j_{i}}$ (rather than the other way around). Note that in iteration $j_{i + 1}$ the addition of sample $X_{j_{i + 1}}$ would not resolve this problematic wiring since the latter sample will be connected by a directed edge either from $X_{j_{i}}$ or $X_{j_{i + 1}^{\prime}}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B A logical gap", "weight": 1.0} -->

Moreover, we can repeat this argument for preceding balls to yield a long chain of samples that are connected in the opposite direction.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B A logical gap", "weight": 1.0} -->

In this discussion it is important to keep in mind that RRT^∗^ performs rewiring (i.e., changing the predecessor of a given vertex) only locally (lines 17-21 of Algorithm 2). That is, in order to force a rewiring of a given vertex $X_{j}$ RRT^∗^ must sample a vertex $x_{\text{new}}$ in the vicinity of $X_{j}$, and this rewiring would not cause a chain of rewires for $X_{j}$s predecessors or successors in $G$. Consequently, in order to reverse the direction of the aforementioned chain from $X_{j_{i + 1}^{\prime}}$, RRT^∗^ would need to sample new vertices along the chain in the correct order. For a more detailed example see the appendix.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B A logical gap", "weight": 1.0} -->

As we show in our proof in the next section, condition (iii) is in fact sufficient to guarantee asymptotic optimality, and we prove that it indeed holds with high probability when we slightly increase the connection radius from Equation, and modify the constant $\gamma^{\text{KF}}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Alternative proof", "weight": 1.0} -->

In order to account for the additional dimension of time, we set the connection radius to be ${r{(n)}} = {\gamma\left( \frac{\log n}{n} \right)^{\frac{1}{d + 1}}}$, where $\gamma$ is a constant that will be determined below. We state our main theorem and provide an overview of the proof. The full proof is presented later. Note that our result suggests that the exponent should be decreased from $1/d$ to $1/{({d + 1})}$, which yields a larger radius overall. Denote by $\sigma_{n}$ the path connecting $s$ to $t$ returned by RRT^∗^ after $n$ iterations. Recall that $c{(\sigma_{n})}$ denotes its length (in case that no solution is found, the length of $\sigma_{n}$ is assumed to be $\infty$).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Alternative proof", "weight": 1.0} -->

Our main theorem, which appears below, states that if $\gamma$ is set correctly, then the cost of the solution returned by RRT^∗^ is upper-bounded asymptotically by ${({1 + \varepsilon})}c^{\ast}$, where $c^{\ast}$ is the robust optimum, and $\varepsilon$ is a tuning parameter. Additional tuning parameters that appear in the theorem are as follows: $\eta$ is the steering size of RRT^∗^ (Algorithm 2, line 5), while $\mu$ and $\theta$ are constants whose purpose will become clear in the proof of the theorem.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 2", "weight": 1.0} -->

We wish to stress that the following lemma, which lower bounds the probability of ${\mathfrak{E}}_{n}^{1}$, is a key ingredient in our proof. As we shall see below, this would allow us to treat some of the vertices added by RRT^∗^ as uniformly sampled, which is not true for all samples, as some are perturbed by the steer operation. We mention that this issue was not addressed in the original proof, where the RRT^∗^ nodes were assumed (incorrectly) to be uniformly distributed. Furthermore, setting the steering step $\eta = \infty$ does not resolve this issue.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper we revisited the original asymptotic-optimality proof of RRT^∗^, and discussed an apparent logical gap within it. We then introduced an alternative proof that amends this logical gap. Our new proof suggests that the connection radius of RRT^∗^ should be slightly larger than the original bound on the radius that was developed. We leave the question of whether our bound is tight, i.e., whether the exponent of $1/{({d + 1})}$ in Equation can be lowered to $1/d$, to future research. The practical successes of the algorithm and its extensions, using the exponent $1/d$, provide some evidence that this might be the case.
