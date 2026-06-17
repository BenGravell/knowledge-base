# Revisiting the Asymptotic Optimality of RRT*

- arXiv ID: [1909.09688](https://arxiv.org/abs/1909.09688)
- HTML source: [ar5iv](https://ar5iv.labs.arxiv.org/html/1909.09688)

# Revisiting the Asymptotic Optimality of RRT\* 

Kiril Solovey^1^, Lucas Janson^2^, Edward Schmerling^3^, Emilio Frazzoli^4^, and Marco Pavone^1^ ^1^ Department of Aeronautics and Astronautics, Stanford University, CA, USA.^2^ Department of Statistics, Harvard University, MA, USA.^3^ Waymo Research, CA, USA.^4^ Institute for Dynamic Systems and Control, ETH Zurich, Switzerland.

###### Abstract 

RRT^∗^ is one of the most widely used sampling-based algorithms for asymptotically-optimal motion planning. RRT^∗^ laid the foundations for optimality in motion planning as a whole, and inspired the development of numerous new algorithms in the field, many of which build upon RRT^∗^ itself. In this paper, we first identify a logical gap in the optimality proof of RRT^∗^, which was developed by Karaman and Frazzoli (2011). Then, we present an alternative and mathematically-rigorous proof for asymptotic optimality. Our proof suggests that the connection radius used by RRT^∗^ should be increased from ${\mathbf{γ}}\hspace{0pt}\left( \frac{{\mathbf{l}\mathbf{o}\mathbf{g}}{\mathbf{n}}}{\mathbf{n}} \right)^{\mathbf{1}/{\mathbf{d}}}$ to ${\mathbf{γ}}^{\prime}\hspace{0pt}\left( \frac{{\mathbf{l}\mathbf{o}\mathbf{g}}{\mathbf{n}}}{\mathbf{n}} \right)^{\mathbf{1}/{({{\mathbf{d}} + \mathbf{1}})}}$ in order to account for the additional dimension of time that dictates the samples' ordering. Here ${\mathbf{γ}},{\mathbf{γ}}^{\prime}$ are constants, and ${\mathbf{n}},{\mathbf{d}}$ are the number of samples and the dimension of the problem, respectively.

## I Introduction 

For many robot motion-planning applications, feasibility is not enough---we further desire path plans that are of high quality, reflecting a need for robots that can achieve their goals with efficiency, alacrity, and economy of motion. To this end we seek planning algorithms that can be trusted, whatever obstacle environment a robot faces, to produce optimal or near-optimal plans with minimal scenario-specific tuning. The advent of the asymptotically-optimal rapidly-exploring random tree (RRT^∗^) algorithm \[1\] has ushered in a decade of theoretical and practical successes in the development of optimal sampling-based motion-planning algorithms.

Although proposed in its initial form for the case of minimum-length path planning for robots without dynamic constraints, RRT^∗^ has been extended to handle kinodynamic planning problems \[2\] including robotic systems governed by non-holonomic constraints \[3\], more expressive costs accounting for robot energy expenditure \[4, 5\], and even to plan paths that minimize violation of safety rules \[6\] or that otherwise balance performance considerations with safety constraints \[7\]. Heuristic modifications to the core algorithm have also been demonstrated that improve practical RRT^∗^ implementations \[8, 9\].

Each of these extensions leverages the simple yet powerful iterative local graph-rewiring technique introduced by RRT^∗^ to enable convergence to the optimal solution (as computation budget increases), provided an appropriate choice for the scaling of the rewiring radius as a function of sample count. Moreover, each of these extensions draws upon the original analysis presented in \[1\] for the fundamental asymptotic scaling of this algorithm parameter; this analysis is therefore core to each of their optimality guarantees.

*Contribution.* The primary contribution of this paper is an in-depth study of the theoretical analysis underpinning the asymptotic-optimality criterion for the RRT^∗^ algorithm. In revisiting this analysis, we identify a logical gap in the original proof and provide an amended proof suggesting a larger radius scaling exponent to ensure asymptotic optimality. The impact of this paper is potentially far-reaching in the large number of works that currently appeal to RRT^∗^ optimality to make their theoretical guarantees.

The paper is organized as follows. Section II provides preliminaries and a description of RRT^∗^. In Section III we review the original optimality proof of RRT^∗^ and identify a logical gap within it. In Section IV we provide the main contribution of this paper, which is an alternative proof that circumvents this logical gap. We conclude the paper in Section V.

## II Preliminaries 

We provide several basic definitions that will be used throughout the paper. Given two points ${x,y} \in {\mathbb{R}}^{d}$, denote by $\|{x - y}\|$ the standard Euclidean distance. Denote by $\mathcal{B}_{r}\hspace{0pt}{(x)}$ the $d$-dimensional ball of radius $r > 0$ centered at $x \in {\mathbb{R}}^{d}$. Define ${\mathcal{B}_{r}\hspace{0pt}{(\Gamma)}}:={\bigcup_{x \in \Gamma}{\mathcal{B}_{r}\hspace{0pt}{(x)}}}$ for any $\Gamma \subseteq {\mathbb{R}}^{d}$. Similarly, given a curve $\sigma:{{\lbrack 0,1\rbrack}\rightarrow{\mathbb{R}}^{d}}$, define ${\mathcal{B}_{r}\hspace{0pt}{(\sigma)}} = {\bigcup_{\tau \in {\lbrack 0,1\rbrack}}{\mathcal{B}_{r}\hspace{0pt}{({\sigma\hspace{0pt}{(\tau)}})}}}$. For a subset $D \subset {\mathbb{R}}^{d}$, $|D|$ denotes its Lebesgue measure. All logarithms used herein are to base $e$.

### II-A Motion planning 

Denote by $\mathcal{C}$ the robot's configuration space, and by $\mathcal{F} \subseteq \mathcal{C}$ the free space, i.e., the set of all collision free configurations. We assume that $\mathcal{C}$ is a subset of the Euclidean space. For simplicity, let $\mathcal{C} = {\lbrack 0,1\rbrack}^{d} \subset {\mathbb{R}}^{d}$ for some fixed $d \geq 2$. Given start and target configurations ${s,t} \in \mathcal{F}$, the *motion-planning* problem consists of finding a continuous path (curve) $\sigma:{{\lbrack 0,1\rbrack}\rightarrow\mathcal{F}}$ such that ${\sigma\hspace{0pt}{(0)}} = s$ and ${\sigma\hspace{0pt}{(1)}} = t$. That is, the robot starts its motion along $\sigma$ at $s$, and ends at $t$, while avoiding collisions. An instance of the problem is defined by $(\mathcal{F},s,t)$. We consider the standard path length as a measure of quality:

###### Definition 1. 

Given a path $\sigma$, its *length* (cost), which corresponds to its Hausdorff measure, is represented by

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{c\hspace{0pt}{(\sigma)}} = {\sup\limits_{{n \in {\mathbb{N}}_{+}},{0 = \tau_{1} \leq \ldots \leq \tau_{n} = 1}}{\sum\limits_{i = 2}^{n}{\|{{\sigma\hspace{0pt}{(\tau_{i})}} - {\sigma\hspace{0pt}{(\tau_{i - 1})}}}\|}}}}.$$   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

We proceed to describe the notion of *robustness*, which is essential when discussing theoretical properties of sampling-based planners. Given a subset $\Gamma \subset \mathcal{C}$ and two configurations ${x,y} \in \Gamma$, denote by $\Sigma_{x,y}^{\Gamma}$ the set of all continuous paths, whose image is in $\Gamma$, that start in $x$ and end in $y$, i.e., if $\sigma \in \Sigma_{x,y}^{\Gamma}$ then $\sigma:{{\lbrack 0,1\rbrack}\rightarrow\Gamma}$ and ${{\sigma\hspace{0pt}{(0)}} = x},{{\sigma\hspace{0pt}{(1)}} = y}$. We mention that the following definition is slightly different than the one used in \[1, 10\].

###### Definition 2. 

Let $(\mathcal{F},s,t)$ be a motion-planning problem. A path $\sigma \in \Sigma_{s,t}^{\mathcal{F}}$ is *robust* if there exists $\delta > 0$ such that ${\mathcal{B}_{\delta}\hspace{0pt}{(\sigma)}} \subset \mathcal{F}$. We also say that $(\mathcal{F},s,t)$ is *robustly feasible* if there exists such a robust path.

###### Definition 3. 

The *robust optimum* is defined as

  -- ---------------------------------------------------------------------------------------------------------------------------- --
     $${c^{\ast} = {\inf\left\{ {c\hspace{0pt}{(\sigma)}} \middle| {\sigma \in {\Sigma_{s,t}^{\mathcal{F}}\hspace{0pt}\text{~is   
     robust}}} \right\}}}.$$                                                                                                      
  -- ---------------------------------------------------------------------------------------------------------------------------- --

### II-B Algorithms 

While our main focus in this paper is the RRT^∗^ algorithm, we also rely on the properties of the RRT algorithm, which is described first. The following description of the (geometric) RRT algorithm is based on \[11\] and \[1\].

1:V = {xinit}
2:for j = 1  to  n do
3:   xrand ← sample-free ()
4:   xnear ← nearest (xrand,V)
5:   xnew← steer(xnear, xrand, η)
6:   if collision-free(xnear, xnew) then
7:      V = V ∪ {xnew}; E = E ∪ {(xnear,xnew)}    
8:return G = (V,E)
Algorithm 1 RRT(xinit := s, xgoal := t, n, η)

The input for RRT (Algorithm 1) is an initial and goal configurations $x_{\text{init}},x_{\text{goal}}$, number of iterations $n$, and a steering parameter $\eta > 0$. RRT constructs a tree $G = {(V,E)}$ by performing $n$ iterations. In each iteration, a new sample $x_{\text{rand}}$ is returned from $\mathcal{F}$ uniformly at random by calling sample-free. Then, the vertex $x_{\text{near}} \in V$ that is nearest (according to $\parallel \cdot \parallel$) to $x_{\text{rand}}$ is found using nearest. A new configuration $x_{\text{new}} \in \mathcal{X}$ is then returned by steer, such that $x_{\text{new}}$ is on the line segment between $x_{\text{near}}$ and $x_{\text{rand}}$, and the distance $\|{x_{\text{near}} - x_{\text{new}}}\|$ is at most $\eta$. Finally, collision-free($x_{\text{near}},x_{\text{new}}$) checks whether the straight-line path from $x_{\text{near}}$ to $x_{\text{new}}$ is collision free. If so, $x_{\text{new}}$ is added as a vertex to $G$ and is connected by an edge from $x_{\text{near}}$.

We proceed to describe RRT^∗^ \[1\] in Algorithm 2. Every RRT^∗^ iteration begins with an RRT-style extension. The difference lies in the subsequent lines. First, RRT^∗^ attempts to connect the tree to $x_{\text{new}}$ from all its neighbors in $V$ within a $\min{\{{r\hspace{0pt}{({|V|})}},\eta\}}$ vicinity (lines 7-15). Notice that the expression $r\hspace{0pt}{({|V|})}$ determines the radius based on the current number of vertices in $V$. (The operation $\text{near}\hspace{0pt}{(x_{\text{new}},V,{\min{\{{r\hspace{0pt}{({|V|})}},\eta\}}})}$ returns the subset $V \cap {\mathcal{B}_{\min{\{{r\hspace{0pt}{({|V|})}},\eta\}}}\hspace{0pt}{(x_{\text{new}})}}$, i.e., the vertices that are within a distance of $\min{\{{r\hspace{0pt}{({|V|})}},\eta\}}$ from $x_{\text{new}}$.) However, it only adds a single edge to $x_{\text{new}}$ from the neighbor $x_{\text{min}} \in X_{\text{near}}$ such that $\text{cost}\hspace{0pt}{(x_{\text{new}})}$ is minimized (line 16). In the next step, RRT^∗^ attempts to perform rewires (lines 17-21): with the addition of $x_{\text{new}}$, it may be beneficial to reroute the existing path of $x_{\text{near}}$ to use $x_{\text{new}}$. RRT^∗^ checks whether changing the parent of $x_{\text{near}}$ to be $x_{\text{new}}$ reduces $\text{cost}\hspace{0pt}{(x_{\text{near}})}$. ($\text{parent}\hspace{0pt}{(x_{\text{near}})}$ returns the immediate predecessor of $x_{\text{near}}$ in $G$. $\text{cost}\hspace{0pt}{(x)}$ for $x \in V$ returns the cost of the path leading from $x_{\text{init}}$ to $x$ in $G$.)

1:V = {xinit}
2:for j = 1  to  n do
3:   xrand ← sample-free ()
4:   xnear ← nearest (xrand,V)
5:   xnew← steer(xnear, xrand, η)
6:   if collision-free(xnear, xnew) then
7:      Xnear = near (xnew,V,min {r (|V|),η})
8:      V = V ∪ {xnew}
9:      xmin = xnear
10:      cmin = cost (xnear) + ∥xnew−xnear∥
11:      for xnear ∈ Xnear do
12:         if collision-free (xnear,xnew) then
13:           if cost (xnear) + ∥xnew−xnear∥ &lt; cmin then
14:              xmin = xnear
15:              cmin = cost (xnear) + ∥xnew−xnear∥                           
16:      E = E ∪ {(xmin,xnew)}
17:      for xnear ∈ Xnear do
18:         if collision-free (xnew,xnear) then
19:           if cost (xnew) + ∥xnear−xnew∥ &lt; cost (xnear) then
20:              xparent = parent (xnear)
21:              E = E ∪ {(xnew,xnear)} ∖ {(xparent,xnear)}                              
22:return G = (V,E)
Algorithm 2 RRT∗(xinit := s, xgoal := t, n, r, η)

###### Remark 1. 

As mentioned above, RRT^∗^ performs extensions of the tree in a manner similar to RRT. That is, steer generates $x_{\text{new}}$, which lies on the straight line connecting $x_{\text{near}},x_{\text{rand}}$, such that ${\|{x_{\text{new}} - x_{\text{near}}}\|} \leq \eta$. Note that initially $x_{\text{new}} \neq x_{\text{rand}}$, but once the space is sufficiently covered by $G$, i.e., when $\mathcal{F} \subset {\bigcup_{v \in V}{\mathcal{B}_{\eta}\hspace{0pt}{(v)}}}$, then in all the following iterations it will hold that $x_{\text{new}} = x_{\text{rand}}$. This property will be important in the analysis of RRT^∗^, as it indicates that $x_{\text{new}}$ is uniformly sampled from $\mathcal{F}$. This notion will be formalized below. For now, it is useful to note that given the same sequence of samples, RRT and RRT^∗^ will generate two (possibly distinct) graphs that have a common vertex set.

## III Original optimality proof 

In this section we review the original proof \[1\] for asymptotic optimality of RRT^∗^, and point out a logical gap. Specifically, Theorem 38 in \[1\] states that if the connection radius used by RRT^∗^ is of the form

  -- --------------------------------------------------------------------------------------------------------------- -- -------
     ${{r^{\text{KF}}\hspace{0pt}{(n)}} = {\gamma^{\text{KF}}\hspace{0pt}\left( \frac{\log n}{n} \right)^{1/d}}},$      \(1\)
  -- --------------------------------------------------------------------------------------------------------------- -- -------

where $n \in {\mathbb{N}}_{+}$, and for some constant $\gamma^{\text{KF}} > 0$, the cost of the solution obtained by RRT^∗^ converges to the robust optimum $c^{\ast}$ as $n\rightarrow\infty$, almost surely.

Figure 1: Illustration of the components in the original proof [1]. (a) The robustly-optimal path σε is drawn as a black curve. (b) Discs represent the balls Bn, 1, …, Bn, Mn, whose centers are denoted as red bullets along σε. The path σn connecting samples between adjacent balls in an increasing order is illustrated as a blue curve. (c) A problematic scenario (Section III-B), where the RRT∗ tree G yields a suboptimal solution, is depicted in green.

### III-A Review of previous proof 

We provide a sketch of the original proof and identify a logical gap. We mention that our definitions of robustness (Definition 2) and robust optimum (Definition 3) are simplified versions of the ones used originally in \[1\], where the latter are slightly less convenient to work with (especially in correction of the proof which we give in Section IV). We thus adapt the original proof details presented in this section to our setting. We emphasize that the logical gap is unrelated to those definitions, and our argument presented below can be easily remapped to the original formulation.

Recall that the sample set of RRT^∗^ consists of $n$ time-labeled configurations. Denote by $\{ X_{1},\ldots,X_{n}\}$ the sample set, where indices denote the order in which the samples are drawn. Fix $\varepsilon > 0$ and let $\sigma_{\varepsilon}$ be a robust solution path such that ${c\hspace{0pt}{(\sigma_{\varepsilon})}} \leq {{({1 + \varepsilon})}\hspace{0pt}c^{\ast}}$. The proof constructs a sequence of $M_{n} \leq n$ identical balls $B_{n,1},\ldots,B_{n,M_{n}}$ that are centered on some equally-spaced points along $\sigma_{\varepsilon}$. The size and spacing of balls is set so that (a) $\sigma_{\varepsilon}$ is completely covered by them, (b) ${\bigcup_{i = 1}^{M_{n}}B_{n,i}} \subseteq \mathcal{F}$, and (c) for every ${1 \leq i \leq M_{n}},{{x \in B_{n,i}},{x^{\prime} \in B_{n,{i + 1}}}}$ it holds that ${\|{x - x^{\prime}}\|} \leq {r^{\text{KF}}\hspace{0pt}{(n)}} \leq {r^{\text{KF}}\hspace{0pt}{({|V|})}}$. Furthermore, it is shown in \[1\] that given $x_{i} \in B_{n,i}$ for every $1 \leq i \leq M_{n}$, the length of the path $\sigma$ connecting each $x_{i}$ to the point in the next ball with a straight line converges (as $n\rightarrow\infty$) to the length of $\sigma_{\varepsilon}$ (see Figure 1).

The proof establishes that if for every $1 \leq i < M_{n}$ there exist $X_{j_{i}},X_{j_{i + 1}}$ such that (i) ${X_{j_{i}} \in B_{n,i}},{X_{j_{i + 1}} \in B_{n,{i + 1}}}$ and (ii) $j_{i} < j_{i + 1}$, then RRT^∗^ is asymptotically optimal (see Section G.3 in \[1\]). The rationale behind these conditions is as follows. Condition (i) makes sure that the optimal path is approximated by samples drawn by RRT^∗^, i.e., for every point along $\sigma_{\varepsilon}$ there is a sample point in its vicinity. Condition (ii) ensures that RRT^∗^ will have the opportunity to add a directed edge from $X_{j_{i}}$ to $X_{j_{i + 1}}$: as $X_{j_{i + 1}}$ is sampled after $X_{j_{i}}$ then RRT^∗^ would consider drawing a directed edge from the latter to the former, considering the fact that $X_{j_{i}} \in {\text{near}\hspace{0pt}{(X_{j_{i + 1}},V,{\min{\{{r\hspace{0pt}{(n)}},\eta\}}})}}$ (this is formalized in Claim 1 below). Observe that $r\hspace{0pt}{(n)}$ is used as a conservative lower-bound for $r\hspace{0pt}{({|V|})}$ throughout \[1\], as we do too.

Consequently, the proof deduces that if these conditions are met RRT^∗^ is guaranteed to find a solution with cost at most $c^{\ast}\hspace{0pt}{({1 + \varepsilon})}$ with probability that converges to $1$ as $n\rightarrow\infty$. In particular, denote by $X_{j_{1}},\ldots,X_{j_{M_{n}}}$ the sequence of samples satisfying the conditions above, and let $\sigma_{n}$ be a path that is induced by those $M_{n}$ samples in the prescribed order. Then the claim is that the solution returned by RRT^∗^ is of length $c\hspace{0pt}{(\sigma_{n})}$, if not shorter.

### III-B A logical gap 

We identify an issue with the proof technique described above, and in particular with the conditions (i) and (ii). We assert that the line of reasoning mentioned above overlooks the fact that the existence of pairwise sequential samples does not directly imply the existence of a whole chain of samples with a proper ordering such that a path in $G$ traces through all the balls in sequence. That is, the fact that for every $1 \leq i < M_{n}$ (i) there exist $X_{j_{i}},X_{j_{i + 1}}$ such that ${X_{j_{i}} \in B_{n,i}},{X_{j_{i + 1}} \in B_{n,{i + 1}}}$ and (ii) $j_{i} < j_{i + 1}$, does not necessarily mean that (iii) there exists a sequence $j_{1} \leq j_{2} \leq \ldots \leq j_{M_{n}}$ such that $X_{j_{i}} \in B_{n,i}$ for every $1 \leq i < M_{n}$; (iii) is a sufficient (but not necessary) condition for recovering a path that is at least as good as $\sigma_{n}$.

Consider for instance the case where ${X_{j_{i}} \in B_{n,i}},{{X_{j_{i + 1}} \in B_{n,{i + 1}}},{{X_{j_{i + 1}^{\prime}} \in B_{n,{i + 1}}},{X_{j_{i + 2}^{\prime}} \in B_{n,{i + 2}}}}}$ and ${j_{i} < j_{i + 1}},{j_{i + 1}^{\prime} < j_{i + 2}^{\prime}}$, but $j_{i + 2}^{\prime} < j_{i}$, where there are two points $X_{j_{i + 1}},X_{j_{i + 1}^{\prime}}$ that fall into the same ball $B_{n,{i + 1}}$ (see Figure 1 (c)). Define ${X_{1}^{j_{i} - 1} = {\{ X_{1},\ldots,X_{j_{i} - 1}\}}},{B_{1}^{i - 1} = {\bigcup_{k = 1}^{i - 1}B_{n,k}}}$, and let $X^{B} = {X_{1}^{j_{i} - 1} \cap B_{1}^{i - 1} \cap {\mathcal{B}_{r\hspace{0pt}{(j_{i})}^{\text{KF}}}\hspace{0pt}{(X_{j_{i}})}}}$. Namely, $X^{B}$ contains all the sampled points that were drawn before $X_{j_{i}}$, which lie in previous balls along $\sigma_{\varepsilon}$, and whose distance from $X_{j_{i}}$ is at most $r\hspace{0pt}{(j_{i})}^{\text{KF}}$.

Now assume that $X^{B} = \varnothing$. We can choose the current structure of $G$ and the locations of $X_{j_{i}},X_{j_{i + 1}^{\prime}}$ such that the only directed edge that is added in iteration $j_{i}$ is $(X_{j_{i + 1}^{\prime}},X_{j_{i}})$, i.e., from $X_{j_{i + 1}^{\prime}}$ to $X_{j_{i}}$ (rather than the other way around). Note that in iteration $j_{i + 1}$ the addition of sample $X_{j_{i + 1}}$ would not resolve this problematic wiring since the latter sample will be connected by a directed edge either from $X_{j_{i}}$ or $X_{j_{i + 1}^{\prime}}$. Moreover, we can repeat this argument for preceding balls to yield a long chain of samples that are connected in the opposite direction.

In this discussion it is important to keep in mind that RRT^∗^ performs rewiring (i.e., changing the predecessor of a given vertex) only locally (lines 17-21 of Algorithm 2). That is, in order to force a rewiring of a given vertex $X_{j}$ RRT^∗^ must sample a vertex $x_{\text{new}}$ in the vicinity of $X_{j}$, and this rewiring would not cause a chain of rewires for $X_{j}$s predecessors or successors in $G$. Consequently, in order to reverse the direction of the aforementioned chain from $X_{j_{i + 1}^{\prime}}$, RRT^∗^ would need to sample new vertices along the chain in the correct order. For a more detailed example see the appendix.

As we show in our proof in the next section, condition (iii) is in fact sufficient to guarantee asymptotic optimality, and we prove that it indeed holds with high probability when we slightly increase the connection radius from Equation (1), and modify the constant $\gamma^{\text{KF}}$.

## IV Alternative proof 

In order to account for the additional dimension of time, we set the connection radius to be ${r\hspace{0pt}{(n)}} = {\gamma\hspace{0pt}\left( \frac{\log n}{n} \right)^{\frac{1}{d + 1}}}$, where $\gamma$ is a constant that will be determined below. We state our main theorem and provide an overview of the proof. The full proof is presented later on. Note that our result suggests that the exponent should be decreased from $1/d$ to $1/{({d + 1})}$, which yields a larger radius overall. Denote by $\sigma_{n}$ the path connecting $s$ to $t$ returned by RRT^∗^ after $n$ iterations. Recall that $c\hspace{0pt}{(\sigma_{n})}$ denotes its length (in case that no solution is found, the length of $\sigma_{n}$ is assumed to be $\infty$). Our main theorem, which appears below, states that if $\gamma$ is set correctly, then the cost of the solution returned by RRT^∗^ is upper-bounded asymptotically by ${({1 + \varepsilon})}\hspace{0pt}c^{\ast}$, where $c^{\ast}$ is the robust optimum, and $\varepsilon$ is a tuning parameter. Additional tuning parameters that appear in the theorem are as follows: $\eta$ is the steering size of RRT^∗^ (Algorithm 2, line 5), while $\mu$ and $\theta$ are constants whose purpose will become clear in the proof of the theorem.

###### Theorem 1. 

Suppose that $(\mathcal{F},s,t)$ is robustly feasible and fix $\eta > 0$, $\varepsilon \in {(0,1)}$,^11^1For simplicity, we upper-bound $\varepsilon$ with $1$ although the proof can be adapted to accommodate larger stretch factors. $\theta \in {(0,{1/4})}$, and $\mu \in {(0,1)}$. Define the radius of RRT^∗^ to be

  -- ---------------------- ------------------------------------------------------------------------------ -- -------
     $r\hspace{0pt}{(n)}$   ${= {\gamma\hspace{0pt}\left( \frac{\log n}{n} \right)^{\frac{1}{d + 1}}}},$      \(2\)
  -- ---------------------- ------------------------------------------------------------------------------ -- -------

such that

  -- ---------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------
     $\gamma$   ${\geq {{({2 + \theta})}\hspace{0pt}\left( {\frac{{({1 + {\varepsilon/4}})}\hspace{0pt}c^{\ast}}{{({d + 1})}\hspace{0pt}\theta\hspace{0pt}{({1 - \mu})}} \cdot \frac{|\mathcal{F}|}{\zeta_{d}}} \right)^{\frac{1}{d + 1}}}},$      \(3\)
  -- ---------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------

where $\zeta_{d}$ is the volume of a unit $d$-dimensional hypersphere. Then

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\lim\limits_{n\rightarrow\infty}{\Pr{\lbrack{{c\hspace{0pt}{(\sigma_{n})}} \leq {{({1 + \varepsilon})}\hspace{0pt}c^{\ast}}}\rbrack}}} = 1}.$$   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------- --

Our proof of Theorem 1 proceeds similarly to the proof of the asymptotic optimality of FMT^∗^ \[10\] (which is in turn based on \[1\]), but with additional complications due to the time dimension and the coupling with the RRT algorithm. We proceed to describe the main ingredients of the proof.

Fix the parameters ${\varepsilon \in {(0,1)}},{{\theta \in {(0,{1/4})}},{{\mu \in {(0,1)}},{\eta > 0}}}$. Due to the fact that $(\mathcal{F},s,t)$ is robustly feasible, there exists a robust path $\sigma_{\varepsilon} \in \Sigma_{s,t}^{\mathcal{F}}$ and $\delta > 0$ such that ${c\hspace{0pt}{(\sigma_{\varepsilon})}} \leq {{({1 + {\varepsilon/4}})}\hspace{0pt}c^{\ast}}$ and ${\mathcal{B}_{\delta}\hspace{0pt}{(\sigma_{\varepsilon})}} \subset \mathcal{F}$. We will show that the RRT^∗^ graph $G$ contains a path that is in the vicinity of $\sigma_{\varepsilon}$, which implies that the solution returned by RRT^∗^ is of cost at most ${({1 + \varepsilon})}\hspace{0pt}c^{\ast}$ (which is slightly larger than ${({1 + {\varepsilon/4}})}\hspace{0pt}c^{\ast}$ due to the fact that this is still an approximation of the path $\sigma_{\varepsilon}$).

The first part of the proof deals with the technicality involved with the samples produced by the algorithm. Denote by $V = {\{{X_{1}\hspace{0pt}\ldots},X_{n}\}}$ the sequence of vertices produced by RRT^∗^, where $X_{j}$ is equal to $x_{\text{new}}$ generated in iteration $j$. Due to the fact that RRT^∗^ (and RRT) perform steering (line 5), samples are not distributed in a uniform manner, as $x_{\text{rand}}$ is not necessarily identical to $x_{\text{new}}$ (see Remark 1). However, we do show that most of the vertices in $V$ that are in the vicinity of $\sigma_{\varepsilon}$ are distributed uniformly at random, with probability approaching $1$ (see Lemma 1). This event is denoted by ${\mathfrak{E}}^{1}$ (see Definition 4).

Next, we proceed in a manner similar to other proofs of asymptotic optimality (see, \[1, 10, 13\]), by defining a sequence of points $x_{1},\ldots,x_{M_{n}}$ along the path $\sigma_{\varepsilon}$ and specifying a sequence of balls $B_{n,1},\ldots,B_{n,M_{n}}$ that are centered on those points respectively, and whose radius is proportional to $r\hspace{0pt}{(n)}$. More formally, define $M_{n} = \left\lceil {{c\hspace{0pt}{(\sigma_{\varepsilon})}} \cdot \left( \frac{r\hspace{0pt}{(n)}}{2 + \theta} \right)^{- 1}} \right\rceil$, and let $x_{1},\ldots,x_{M_{n}}$ be a sequence of points along $\sigma_{\varepsilon}$ such that ${\|{x_{i} - x_{i - 1}}\|} \leq \frac{\theta\hspace{0pt}r\hspace{0pt}{(n)}}{2 + \theta}$, ${x_{1} = s},{x_{M_{n}} = t}$. For every $1 \leq i \leq M_{n}$ define $B_{n,i}:={\mathcal{B}_{\frac{r\hspace{0pt}{(n)}}{2 + \theta}}\hspace{0pt}{(x_{i})}}$.

As suggested in Section III, we need to reason both about the existence of samples inside those balls, and the order of those samples. We assign to every ball $B_{n,i}$ a specific time window $T_{i}$, corresponding to allowed timestamps of samples, and partition the sample set $V = {\{ X_{1},\ldots,X_{n}\}}$ into the subsets $V_{0},V_{1},\ldots,V_{M_{n}}$, where $X_{j} \in V_{i}$ if $j \in T_{i}$. In particular, $T_{0}$ consists of the first $n^{\prime}$ indices, where $n^{\prime} = {\mu\hspace{0pt}n}$, and every $T_{i}$, where $i > 1$ consists of ${({n - n^{\prime}})}/M_{n}$ indices, and $\mu \in {(0,1)}$ is a constant:

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${T_{i \neq 0} = \left\{ {n^{\prime} + {{({i - 1})} \cdot \left\lfloor \frac{n - n^{\prime}}{M_{n}} \right\rfloor} + 1},\ldots,{n^{\prime} + {i \cdot \left\lfloor \frac{n - n^{\prime}}{M_{n}} \right\rfloor}} \right\}}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

We show that the event ${\mathfrak{E}}^{2}$ (Definition 5) indicating that every $B_{n,i}$ contains a vertex from $V_{i}$ occurs with probability approaching $1$ as well (Lemma 2). The motivation for this event is the following claim, which indicates that edges between points in consecutive balls are added if deemed beneficial.

###### Claim 1. 

There exists $n \in {\mathbb{N}}_{+}$ large enough such that the following holds with respect to $G_{j_{i + 1}} = {(V_{j_{i + 1}},E_{j_{i + 1}})}$: Suppose that there exist ${X_{j_{i}} \in {V_{i} \cap B_{n,i}}},{X_{j_{i + 1}} \in {V_{i + 1} \cap B_{n,{i + 1}}}}$ and denote by $G_{j_{i + 1}}$ the RRT^∗^ graph at the end of iteration $j_{i + 1}$. Then in $G_{j_{i} + 1}$ it follows that ${\text{cost}\hspace{0pt}{(X_{j_{i + 1}})}} \leq {{\text{cost}\hspace{0pt}{(X_{j_{i}})}} + {\|{X_{j_{i}} - X_{j_{i + 1}}}\|}}$.

###### Proof. 

Recall that $B_{n,i} = {\mathcal{B}_{\frac{r\hspace{0pt}{(n)}}{2 + \theta}}\hspace{0pt}{(x_{i})}}$ and ${\|{x_{i} - x_{i + 1}}\|} \leq \frac{\theta\hspace{0pt}r\hspace{0pt}{(n)}}{2 + \theta}$. For any ${x \in B_{n,i}},{x^{\prime} \in B_{n,{i + 1}}}$ it follows that

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\|{x - x^{\prime}}\|} \leq {\frac{r\hspace{0pt}{(n)}}{2 + \theta} + \frac{\theta\hspace{0pt}r\hspace{0pt}{(n)}}{2 + \theta} + \frac{r\hspace{0pt}{(n)}}{2 + \theta}} = {r\hspace{0pt}{(n)}}}.$$   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

This implies that $X_{j_{i}} \in X_{\text{near}} = {\text{near}\hspace{0pt}{(X_{j_{i + 1}},V_{j_{i}},{r\hspace{0pt}{(n)}})}}$, which will cause the execution of the test $\text{collision-free}\hspace{0pt}{(X_{j_{i}},X_{j_{i + 1}})}$ (line 12 of RRT^∗^). The latter will be evaluated to be true since ${\mathcal{B}_{\delta}\hspace{0pt}{(\sigma_{\varepsilon})}} \subseteq \mathcal{F}$ and ${r\hspace{0pt}{(n)}} \ll \delta$ (for $n$ large enough). Thus, in line 13 the edge $(X_{j_{i}},X_{j_{i + 1}})$ will be added to the graph, unless there is a lower-cost alternative for connection. ∎

Thus, ${\mathfrak{E}}^{2}$ guarantees that the RRT^∗^ tree $G$ contains a path $\sigma_{n}^{\prime}$ connecting $s$ to $t$ that follows $\sigma_{\varepsilon}$ closely. In order to ensure that ${c\hspace{0pt}{(\sigma_{n}^{\prime})}} \leq {{({1 + \varepsilon})}\hspace{0pt}c^{\ast}}$ we need one more step, since $\sigma_{n}^{\prime}$ could stay close to $\sigma_{\varepsilon}$ but zig-zag around it, resulting in a high-cost solution.

Define the constants ${\alpha \in {(0,{{\theta\hspace{0pt}\varepsilon}/16})}},{\beta \in {(0,{{\theta\hspace{0pt}\varepsilon}/16})}}$. Additionally, define for every $1 \leq i \leq M_{n}$ the ball $B_{n,i}^{\beta}:={\mathcal{B}_{\frac{\beta\hspace{0pt}r\hspace{0pt}{(n)}}{2 + \theta}}\hspace{0pt}{(x_{i})}}$. The event ${\mathfrak{E}}^{3}$ (Definition 6) indicates that a fraction of at most $\alpha$ of the smaller balls $B_{n,i}^{\beta}$ does not contain samples from $V_{i}$. We show that ${\mathfrak{E}}^{3}$ occurs with probability approaching $1$ (Lemma 3). We then proceed to show that if ${\mathfrak{E}}^{2},{\mathfrak{E}}^{3}$ occur simultaneously then RRT^∗^ is guaranteed to return a solution with cost at most ${({1 + \varepsilon})}\hspace{0pt}c^{\ast}$ (Lemma 4).

### IV-A Proof of Theorem 1 

We start with a formal definition of ${\mathfrak{E}}^{1}$:

###### Definition 4. 

For every $1 \leq j \leq n$ denote by $x_{\text{rand}}^{j},x_{\text{new}}^{j}$ the random and new samples of RRT^∗^ in iteration $j$ (line 3 and line 5 in Algorithm 2, respectively). Define $n^{\prime}:={\mu\hspace{0pt}n}$ and

  -- ------------------------------ ------------------------------------------------------------------------------------------------------ --
     ${\mathfrak{E}}_{n}^{1}:=\{$   $\forall 1 \leq i \leq M_{n},n^{\prime} \leq j \leq n:$                                                
                                    $\text{~if~}x_{\text{rand}}^{j} \in B_{n,i}\text{~then~}x_{\text{rand}}^{j} = x_{\text{new}}^{j}\}.$   
  -- ------------------------------ ------------------------------------------------------------------------------------------------------ --

That is, ${\mathfrak{E}}_{n}^{1}$ is the event that all $x_{\text{rand}}^{j} \in B_{n,i}$ for $j$ between $n^{\prime}$ and $n$ satisfy $x_{\text{rand}}^{j} = x_{\text{new}}^{j}$.

###### Remark 2. 

We wish to stress that the following lemma, which lower bounds the probability of ${\mathfrak{E}}_{n}^{1}$, is a key ingredient in our proof. As we shall see below, this would allow us to treat some of the vertices added by RRT^∗^ as uniformly sampled, which is not true for all samples, as some are perturbed by the steer operation. We mention that this issue was not addressed in the original proof in \[1\], where the RRT^∗^ nodes were assumed (incorrectly) to be uniformly distributed. Furthermore, setting the steering step $\eta = \infty$ does not resolve this issue.

###### Lemma 1. 

There exist two constants ${a,b} > 0$ such that ${\Pr{\lbrack{\mathfrak{E}}_{n}^{1}\rbrack}} \geq {1 - {a \cdot e^{- {b\hspace{0pt}n}}}}$.

###### Proof. 

A similar proof appears in \[13, Claim 6\], albeit for a different type of sampling scheme and in the context of an RRG analysis. The main challenge here is to show that while it is not true that all the new samples $x_{\text{new}}$ are distributed uniformly randomly (due to lines 4,5 in Algorithm 2), most of them are. Define $\kappa:={{\min{\{\eta,\delta\}}}/10}$ and set $z_{1},\ldots,z_{\ell}$ to be a sequence of points placed along $\sigma_{\varepsilon}$, such that $\ell = {{c\hspace{0pt}{(\sigma_{\varepsilon})}}/\kappa}$, and ${\|{z_{k} - z_{k + 1}}\|} \leq \kappa$. Observe that for $n$ large enough it holds that ${\bigcup_{i = 1}^{M_{n}}B_{n,i}} \subset {\bigcup_{k = 1}^{\ell}{\mathcal{B}_{\kappa}\hspace{0pt}{(z_{k})}}}$.

Denote by $V_{n^{\prime}}^{\text{RRT}}$ the vertex set of RRT after $n^{\prime}$ iterations. Theorem 1 in \[14\] states that there exist constants ${a,c} > 0$ such that the probability that for every $1 \leq k \leq \ell$ it holds that ${V_{n^{\prime}}^{\text{RRT}} \cap {\mathcal{B}_{\kappa}\hspace{0pt}{(z_{k})}}} \neq \varnothing$ is at least ${a \cdot e^{- {c\hspace{0pt}n^{\prime}}}} = {a \cdot e^{- {b\hspace{0pt}n}}}$, where $b:={c\hspace{0pt}\mu}$. Notice that this theorem requires $\eta$ to be fixed (i.e., independent of $n$) and strictly positive.

Denote the latter event to be ${}_{}^{}$. Next, we show that ${}_{}^{}$ implies ${\mathfrak{E}}_{n}^{1}$. First, observe that $V_{n^{\prime}}^{\text{RRT}} = V_{n^{\prime}}^{\text{RRT}^{\ast}}$, where the latter is the vertex set of RRT^∗^ after $n^{\prime}$ iterations, and assume that ${}_{}^{}$ holds . Fix an iteration $n^{\prime} < j < n$ and some $1 \leq k \leq \ell$. Due to the fact that $\eta > 0$ is fixed, by the proof of Lemma 1 in \[14\] it follows that if $x_{\text{rand}}^{j} \in {\mathcal{B}_{\kappa}\hspace{0pt}{(z_{j})}}$ then $x_{\text{near}}^{j} \in {\mathcal{B}_{5\hspace{0pt}\kappa}\hspace{0pt}{(z_{j})}}$, and consequently

  -- --------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------- --
     $\|{x_{\text{rand}}^{j} - x_{\text{near}}^{j}}\|$   $= {\|{{{x_{\text{rand}}^{j} - z_{j}} + z_{j}} - x_{\text{near}}^{j}}\|}$                                                               
                                                         ${\leq {{\|{x_{\text{rand}}^{j} - z_{j}}\|} + {\|{z_{j} - x_{\text{near}}^{j}}\|}} \leq {\kappa + {5\hspace{0pt}\kappa}} \leq \eta}.$   
  -- --------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------- --

This implies that $x_{\text{new}}^{j} = x_{\text{rand}}^{j}$. Additionally, observe that due to the fact that the straight-line path from $x_{\text{near}}^{j}$ to $x_{\text{rand}}^{j}$ is contained in $\mathcal{B}_{\kappa}\hspace{0pt}{(z_{j})}$, where $\kappa < {\delta/5}$, it is also collision free. Thus, at the end of iteration $j$, $x_{\text{rand}}$ will be added to the RRT^∗^ graph as a vertex. ∎

We will prove that the following event ${\mathfrak{E}}^{2}$ holds with probability approaching $1$ by conditioning on ${\mathfrak{E}}^{1}$.

###### Definition 5. 

${\mathfrak{E}}_{n}^{2}$ represents the event that every $B_{n,i}$ contains at least one vertex from $V_{i}$. That is,

  -- ---------------------------------------------------------------------------------------------------- --
     $${\mathfrak{E}}_{n}^{2}:={\{\forall 1 \leq i \leq M_{n},V_{i} \cap B_{n,i} \neq \varnothing\}}.$$   
  -- ---------------------------------------------------------------------------------------------------- --

###### Lemma 2. 

${\lim_{n\rightarrow\infty}{\Pr{\lbrack{\mathfrak{E}}_{n}^{2}\rbrack}}} = 1$.

###### Proof. 

Observe that

  -- --------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $\Pr{\lbrack{\mathfrak{E}}_{n}^{2}\rbrack}$   $= {{{\Pr{\lbrack\left. {\mathfrak{E}}_{n}^{2} \middle| {\mathfrak{E}}_{n}^{1} \right.\rbrack}} \cdot {\Pr{\lbrack{\mathfrak{E}}_{n}^{1}\rbrack}}} + {{\Pr{\lbrack\left. {\mathfrak{E}}_{n}^{2} \middle| \overline{{\mathfrak{E}}_{n}^{1}} \right.\rbrack}} \cdot {\Pr{\lbrack\overline{{\mathfrak{E}}_{n}^{1}}\rbrack}}}}$   
                                                   ${\geq {{\Pr{\lbrack\left. {\mathfrak{E}}_{n}^{2} \middle| {\mathfrak{E}}_{n}^{1} \right.\rbrack}} \cdot {\Pr{\lbrack{\mathfrak{E}}_{n}^{1}\rbrack}}}}.$                                                                                                                                                                      
  -- --------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

We shall lower-bound the expression $\Pr{\lbrack\left. {\mathfrak{E}}_{n}^{2} \middle| {\mathfrak{E}}_{n}^{1} \right.\rbrack}$. By definition of ${\mathfrak{E}}_{n}^{1}$, for every $n^{\prime} < j \leq n$, and $i$ such that $j \in T_{i}$, if $x_{\text{rand}}^{j} \in B_{n,i}$, then $x_{\text{new}}^{j} = x_{\text{rand}}^{j}$ is a valid vertex of the RRT^∗^ graph. Thus, by conditioning on ${\mathfrak{E}}_{n}^{1}$ we can treat $V \smallsetminus V_{0}$ as uniform random samples from $\mathcal{F}$. This will come in handy in bounding the probability of ${\mathfrak{E}}^{2}$:

  -- ------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------
     $\Pr$   $\left\lbrack \overline{{\mathfrak{E}}_{n}^{2}} \middle| {\mathfrak{E}}_{n}^{1} \right\rbrack = {\Pr\left\lbrack {{\exists 1} \leq i \leq M_{n}},{{V_{i} \cap B_{n,i}} = \varnothing} \right\rbrack}$                                                                                                                                                    
             $\leq {\sum\limits_{i = 1}^{M_{n}}{\Pr\left\lbrack {{V_{i} \cap B_{n,i}} = \varnothing} \right\rbrack}} = {\sum\limits_{i = 1}^{M_{n}}\left( {1 - \frac{\left| B_{n,i} \right|}{|\mathcal{F}|}} \right)^{|T_{i}|}}$                                                                                                                                      \(4\)
             $\leq {M_{n}\hspace{0pt}\left( {1 - \frac{\zeta_{d}\hspace{0pt}\left( \frac{r\hspace{0pt}(n)}{2 + \theta} \right)^{d}}{|\mathcal{F}|}} \right)^{{({n - n^{\prime}})}/M_{n}}}$                                                                                                                                                                            
             $\leq {M_{n}\hspace{0pt}{\exp\left\{ {- {\frac{n - n^{\prime}}{M_{n}} \cdot \frac{\zeta_{d}}{|\mathcal{F}|} \cdot \frac{r\hspace{0pt}(n)^{d}}{\left( {2 + \theta} \right)^{d}}}} \right\}}}$                                                                                                                                                             \(5\)
             $\leq {M_{n}\hspace{0pt}{\exp\left\{ {- {\frac{n\hspace{0pt}r\hspace{0pt}(n)\hspace{0pt}\theta\hspace{0pt}\left( {1 - \mu} \right)}{c\hspace{0pt}\left( \sigma_{\varepsilon} \right)\hspace{0pt}\left( {2 + \theta} \right)} \cdot \frac{\zeta_{d}}{|\mathcal{F}|} \cdot \frac{r\hspace{0pt}(n)^{d}}{\left( {2 + \theta} \right)^{d}}}} \right\}}}$      
             $= {M_{n}\hspace{0pt}{\exp\left\{ {- {{\frac{\theta\hspace{0pt}\zeta_{d}\hspace{0pt}\left( {1 - \mu} \right)}{c\hspace{0pt}\left( \sigma_{\varepsilon} \right)\hspace{0pt}\left( {2 + \theta} \right)^{d + 1}\hspace{0pt}|\mathcal{F}|} \cdot n \cdot r}\hspace{0pt}(n)^{d + 1}}} \right\}}}$                                                            
             $= :M_{n}\exp\left\{ - \xi \cdot n \cdot \gamma^{d + 1}\frac{\log n}{n} \right\}$                                                                                                                                                                                                                                                                        \(6\)
             $= {\left\lceil {{c\hspace{0pt}\left( \sigma_{\varepsilon} \right)} \cdot \left( \frac{r\hspace{0pt}(n)}{2 + \theta} \right)^{- 1}} \right\rceil\hspace{0pt}{\exp\left\{ {- {\xi\hspace{0pt}\gamma^{d + 1}\hspace{0pt}{\log n}}} \right\}}}$                                                                                                             
             $< {\left( {{{c\hspace{0pt}\left( \sigma_{\varepsilon} \right)} \cdot \left( \frac{r\hspace{0pt}(n)}{2 + \theta} \right)^{- 1}} + 1} \right)\hspace{0pt}{\exp\left\{ {- {\xi\hspace{0pt}\gamma^{d + 1}\hspace{0pt}{\log n}}} \right\}}}$                                                                                                                 
             $= {\frac{c\hspace{0pt}\left( \sigma_{\varepsilon} \right)\hspace{0pt}\left( {2 + \theta} \right)}{\theta\hspace{0pt}\gamma}\hspace{0pt}\left( {\log n} \right)^{- {1/{({d + 1})}}}\hspace{0pt}n^{{1/{({d + 1})}} - {\xi\hspace{0pt}\gamma^{d + 1}}}}$                                                                                                   
             ${+ {\exp\left\{ {- {\xi\hspace{0pt}\gamma^{d + 1}\hspace{0pt}{\log n}}} \right\}}},$                                                                                                                                                                                                                                                                    \(7\)
  -- ------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------

where (4) is due to the union bound and the fact that $V_{i}$ is uniformly sampled at random from $\mathcal{F}$, (5) is due to the inequality ${1 - x} \leq e^{- x}$ for $x \in {(0,1)}$ which applies here for $n$ large enough, and (6) defines $\xi:=\frac{\theta\hspace{0pt}\zeta_{d}\hspace{0pt}{({1 - \mu})}}{c\hspace{0pt}{(\sigma_{\varepsilon})}\hspace{0pt}{({2 + \theta})}^{d + 1}\hspace{0pt}{|\mathcal{F}|}}$. If ${{({d + 1})}^{- 1} - {\xi\hspace{0pt}\gamma^{d + 1}}} \leq 0$ then the final expression tends to 0. Indeed,

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     ${{\frac{1}{d + 1} - {\frac{\theta\hspace{0pt}\zeta_{d}\hspace{0pt}\left( {1 - \mu} \right)}{c\hspace{0pt}\left( \sigma_{\varepsilon} \right)\hspace{0pt}\left( {2 + \theta} \right)^{d + 1}\hspace{0pt}|\mathcal{F}|} \cdot \gamma^{d + 1}}} \leq 0}\Leftrightarrow$                                                                                                                                                                                                                                                                                                    
     ${{\left( {2 + \theta} \right)\hspace{0pt}\left( \frac{c\hspace{0pt}\left( \sigma_{\varepsilon} \right)\hspace{0pt}|\mathcal{F}|}{\left( {d + 1} \right)\hspace{0pt}\theta\hspace{0pt}\zeta_{d}\hspace{0pt}\left( {1 - \mu} \right)} \right)^{\frac{1}{d + 1}}} \leq {\left( {2 + \theta} \right)\hspace{0pt}\left( \frac{c^{\ast}\hspace{0pt}\left( {1 + \left. \varepsilon/4 \right.} \right)\hspace{0pt}|\mathcal{F}|}{\left( {d + 1} \right)\hspace{0pt}\theta\hspace{0pt}\zeta_{d}\hspace{0pt}\left( {1 - \mu} \right)} \right)^{\frac{1}{d + 1}}} \leq \gamma}.$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

It remains to show that ${\lim_{n\rightarrow\infty}{{\Pr{\lbrack\left. {\mathfrak{E}}_{n}^{2} \middle| {\mathfrak{E}}_{n}^{1} \right.\rbrack}} \cdot {\Pr{\lbrack{\mathfrak{E}}_{n}^{1}\rbrack}}}} = 1$:

  -- -------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $\Pr{\lbrack\left. {\mathfrak{E}}_{n}^{2} \middle| {\mathfrak{E}}_{n}^{1} \right.\rbrack}$   $\cdot \Pr{\lbrack{\mathfrak{E}}_{n}^{1}\rbrack} = {(1 - \Pr{\lbrack\overline{{\mathfrak{E}}_{n}^{2}}|{\mathfrak{E}}_{n}^{1}\rbrack})}{(1 - \Pr{\lbrack\overline{{\mathfrak{E}}_{n}^{1}}\rbrack})}$                                                                                                                                                 
                                                                                                  $= {{1 + {{\Pr{\lbrack\left. \overline{{\mathfrak{E}}_{n}^{2}} \middle| {\mathfrak{E}}_{n}^{1} \right.\rbrack}} \cdot {\Pr{\lbrack\overline{{\mathfrak{E}}_{n}^{1}}\rbrack}}}} - {\Pr{\lbrack\left. \overline{{\mathfrak{E}}_{n}^{2}} \middle| {\mathfrak{E}}_{n}^{1} \right.\rbrack}} - {\Pr{\lbrack\overline{{\mathfrak{E}}_{n}^{1}}\rbrack}}}$   
                                                                                                  ${> {1 - {\Pr{\lbrack\left. \overline{{\mathfrak{E}}_{n}^{2}} \middle| {\mathfrak{E}}_{n}^{1} \right.\rbrack}} - {\Pr{\lbrack\overline{{\mathfrak{E}}_{n}^{1}}\rbrack}}}},$                                                                                                                                                                         
  -- -------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

where the final expression converges to $1$, according to Equation 7 and Lemma 1. ∎

Next we consider the existence of samples in a collection of smaller balls.

###### Definition 6. 

Let $K_{n}^{\beta}:=\left| \left\{ {i \in \left\{ 1,\ldots,M_{n} \right\}}:{{B_{n,i}^{\beta} \cap V_{i}} = \varnothing} \right\} \right|$. ${\mathfrak{E}}_{n}^{3}:={\{{K_{n}^{\beta} \leq {\alpha\hspace{0pt}M_{n}}}\}}$ is the event that at most $\alpha\hspace{0pt}M_{n}$ of the smaller balls $B_{n,i}^{\beta}$ do not contain any samples from $V_{i}$.

###### Lemma 3. 

${\lim_{n\rightarrow\infty}{\Pr{\lbrack{\mathfrak{E}}_{n}^{3}\rbrack}}} = 1$.

###### Proof. 

Similarly to Lemma 2, it is sufficient to show that ${\lim_{n\rightarrow\infty}{\Pr{\lbrack\left. \overline{{\mathfrak{E}}_{n}^{3}} \middle| {\mathfrak{E}}_{n}^{1} \right.\rbrack}}} = 0$. We shall upper bound the probability that $K_{n}^{\beta} > {\alpha\hspace{0pt}M_{n}}$ assuming that ${\mathfrak{E}}_{n}^{1}$ holds. To this end, we compute the expectation of $K_{n}^{\beta}$ and apply Markov's inequality.

For every $1 \leq i \leq M_{n}$, denote by $I_{i}$ the indicator variable for the event that ${B_{n,i}^{\beta} \cap V_{i}} = \varnothing$. Observe that $K_{n}^{\beta} = {\sum_{i = 1}^{M_{n}}I_{i}}$. For $n$ large enough we have that

  -- ------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $E\hspace{0pt}\left\lbrack I_{i} \right\rbrack$   $= {\Pr\left\lbrack {I_{i} = 1} \right\rbrack} = \left( {1 - \frac{\left| B_{n,i}^{\beta} \right|}{|\mathcal{F}|}} \right)^{|T_{i}|}$                                                                                                                                                                
                                                       $\leq \left( {1 - \frac{\beta^{d}\hspace{0pt}\zeta_{d}\hspace{0pt}\left( \frac{r\hspace{0pt}(n)}{2 + \theta} \right)^{d}}{|\mathcal{F}|}} \right)^{{n\hspace{0pt}{({1 - \mu})}}/M_{n}}$                                                                                                              
                                                       $\leq {\exp\left\{ {- {{\frac{\beta^{d}\hspace{0pt}\theta\hspace{0pt}\zeta_{d}\hspace{0pt}\left( {1 - \mu} \right)}{c\hspace{0pt}\left( \sigma_{\varepsilon} \right)\hspace{0pt}\left( {2 + \theta} \right)^{d + 1}\hspace{0pt}|\mathcal{F}|} \cdot n \cdot r}\hspace{0pt}(n)^{d + 1}}} \right\}}$   
                                                       $\leq {\exp\left\{ {- {\frac{\beta^{d}\hspace{0pt}\theta\hspace{0pt}\zeta_{d}\hspace{0pt}\left( {1 - \mu} \right)}{c\hspace{0pt}\left( \sigma_{\varepsilon} \right)\hspace{0pt}\left( {2 + \theta} \right)^{d + 1}\hspace{0pt}|\mathcal{F}|} \cdot \gamma^{d + 1} \cdot {\log n}}} \right\}}$        
                                                       ${= {\exp\left\{ {- {\frac{\beta^{d}}{d + 1}\hspace{0pt}{\log n}}} \right\}} = n^{- {\beta^{d}/{({d + 1})}}}}.$                                                                                                                                                                                      
  -- ------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Thus, ${E\hspace{0pt}{\lbrack K_{n}^{\beta}\rbrack}} = {\sum_{i = 1}^{M_{n}}{E\hspace{0pt}{\lbrack I_{i}\rbrack}}} \leq {M_{n}\hspace{0pt}n^{- {\beta^{d}/{({d + 1})}}}}$. By Markov's inequality, it follows that

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------
     ${{\Pr\left\lbrack {K_{n}^{\beta} > {\alpha\hspace{0pt}M_{n}}} \right\rbrack} \leq \frac{E\hspace{0pt}\left\lbrack K_{n}^{\beta} \right\rbrack}{\alpha\hspace{0pt}M_{n}} \leq \frac{M_{n}\hspace{0pt}n^{- {\beta^{d}/{({d + 1})}}}}{\alpha\hspace{0pt}M_{n}} = \frac{n^{- {\beta^{d}/{({d + 1})}}}}{\alpha}}.$      \(8\)
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------

As $\alpha$ is fixed, the last expression tends to $0$ as $n$ tends to $\infty$. While the upper bound obtained in (8) is sufficient for our purpose, we mention that a tighter bound can be derived by using a slightly more complex Poissonization argument similar to that used in \[10\]. ∎

Next, we show that if ${\mathfrak{E}}^{2},{\mathfrak{E}}^{3}$ occur simultaneously, then the cost of $c\hspace{0pt}{(\sigma_{n})}$ is bounded by ${({1 + \varepsilon})}\hspace{0pt}c^{\ast}$.

###### Lemma 4. 

For $n$ large enough, if the events ${\mathfrak{E}}_{n}^{2},{\mathfrak{E}}_{n}^{3}$ occur, then ${c\hspace{0pt}{(\sigma_{n})}} \leq {{({1 + \varepsilon})}\hspace{0pt}c^{\ast}}$.

###### Proof. 

As ${\mathfrak{E}}_{n}^{2} \land {\mathfrak{E}}_{n}^{3}$ we may define the sequence of vertices ${X_{j_{1}},\ldots,X_{j_{M_{n}}}} \in V$, such that ${X_{j_{1}} = s},{X_{j_{M_{n}}} = t}$, and for every $1 < i < M_{n}$, $X_{j_{i}} \in {V_{i} \cap B_{n,i}^{\beta}}$ if ${V_{i} \cap B_{n,i}^{\beta}} \neq \varnothing$, and $X_{j_{i}} \in {V_{i} \cap B_{n,i}}$ otherwise.

Denote by $\sigma_{n}^{\prime}$ the path induced by concatenating those points, and notice that it is collision free by definition of $B_{n,i}$ and $\sigma_{\varepsilon}$. Next, we claim that the cost of the path $\sigma_{n}$ obtained by RRT^∗^ is upper-bounded by the cost of $\sigma_{n}^{\prime}$, which is equal to $\sum_{i = 2}^{M_{n}}{\|{X_{j_{i}} - X_{j_{i - 1}}}\|}$. Consider iteration $j_{i}$ of RRT^∗^, for $1 < i \leq M_{n}$ and observe that (i) $x_{\text{new}}^{j_{i}} = X_{j_{i}}$, (ii) $X_{j_{i - 1}} \in X_{\text{near}}^{j_{i}}$. By Claim 1, it follows that ${\text{cost}\hspace{0pt}{(X_{j_{i}})}} \leq {\sum_{k = 2}^{i}{\|{X_{j\hspace{0pt}{(k)}} - X_{j\hspace{0pt}{({k - 1})}}}\|}}$, as desired. Thus, ${c\hspace{0pt}{(\sigma_{n})}} \leq {c\hspace{0pt}{(\sigma_{n}^{\prime})}}$.

We proceed to bound $c\hspace{0pt}{(\sigma_{n}^{\prime})}$. Observe that for any $1 < i \leq M_{n}$ it holds that $\|{X_{j_{i}} - X_{j_{i - 1}}}\|$ is at most

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $$\begin{cases}                                                                                                                                                                                                                                                                                                      
     {{\frac{\theta\hspace{0pt}r\hspace{0pt}(n)}{2 + \theta} + \frac{\beta\hspace{0pt}r\hspace{0pt}(n)}{2 + \theta} + \frac{\beta\hspace{0pt}r\hspace{0pt}(n)}{2 + \theta}},} & {{\text{if~}\hspace{0pt}X_{j_{i - 1}}} \in {B_{n,{i - 1}}^{\beta}\hspace{0pt}\text{~AND~}\hspace{0pt}X_{j_{i}}} \in B_{n,i}^{\beta}} \\   
     {{\frac{\theta\hspace{0pt}r\hspace{0pt}(n)}{2 + \theta} + \frac{\beta\hspace{0pt}r\hspace{0pt}(n)}{2 + \theta} + \frac{r\hspace{0pt}(n)}{2 + \theta}},} & {{\text{if~}\hspace{0pt}X_{j_{i - 1}}} \in {B_{n,{i - 1}}^{\beta}\hspace{0pt}\text{~XOR~}\hspace{0pt}X_{j_{i}}} \in B_{n,i}^{\beta}} \\                    
     {{\frac{\theta\hspace{0pt}r\hspace{0pt}(n)}{2 + \theta} + \frac{r\hspace{0pt}(n)}{2 + \theta} + \frac{r\hspace{0pt}(n)}{2 + \theta}},} & \text{otherwise}                                                                                                                                                            
     \end{cases}.$$                                                                                                                                                                                                                                                                                                       
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Thus,

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     ${c\hspace{0pt}\left( \sigma_{n}^{\prime} \right)} \leq {\sum\limits_{i = 2}^{M_{n}}\left\| {X_{j_{i}} - X_{j_{i - 1}}} \right\|}$                                                                                                                                                                                                                                                                               
     $\leq {{\left( {M_{n} - 1} \right)\hspace{0pt}\frac{\theta\hspace{0pt}r\hspace{0pt}(n)}{2 + \theta}} + {\left\lceil {\left( {1 - \alpha} \right)\hspace{0pt}\left( {M_{n} - 1} \right)} \right\rceil\hspace{0pt}\frac{2\hspace{0pt}\beta\hspace{0pt}r\hspace{0pt}(n)}{2 + \theta}}}$                                                                                                                             
     ${+ {\left\lfloor {\alpha\hspace{0pt}\left( {M_{n} - 1} \right)} \right\rfloor\hspace{0pt}\frac{2\hspace{0pt}r\hspace{0pt}(n)}{2 + \theta}}} \leq {\left( {M_{n} - 1} \right)\hspace{0pt}r\hspace{0pt}(n)\hspace{0pt}\frac{\theta + {2\hspace{0pt}\beta} + {2\hspace{0pt}\alpha}}{2 + \theta}}$                                                                                                                  
     $\leq {\frac{c\hspace{0pt}\left( \sigma_{\varepsilon} \right)\hspace{0pt}\left( {2 + \theta} \right)}{\theta\hspace{0pt}r\hspace{0pt}(n)}\hspace{0pt}r\hspace{0pt}(n)\hspace{0pt}\frac{\theta + {2\hspace{0pt}\beta} + {2\hspace{0pt}\alpha}}{2 + \theta}} \leq {{\left( {1 + \frac{\varepsilon}{4}} \right)\hspace{0pt}c^{\ast}} \cdot \frac{\theta + {2\hspace{0pt}\beta} + {2\hspace{0pt}\alpha}}{\theta}}$   
     $< {\left( {1 + \frac{\varepsilon}{4}} \right)\hspace{0pt}c^{\ast}\hspace{0pt}\frac{\theta + \frac{2\hspace{0pt}\theta\hspace{0pt}\varepsilon}{16} + \frac{2\hspace{0pt}\theta\hspace{0pt}\varepsilon}{16}}{\theta}} = {\left( {1 + \frac{\varepsilon}{4}} \right)^{2}\hspace{0pt}c^{\ast}}$                                                                                                                     
     ${= {\left( {1 + \frac{\varepsilon}{2} + \frac{\varepsilon^{2}}{16}} \right)\hspace{0pt}c^{\ast}} < {\left( {1 + \frac{\varepsilon}{2} + \frac{\varepsilon}{16}} \right)\hspace{0pt}c^{\ast}} < {\left( {1 + \varepsilon} \right)\hspace{0pt}c^{\ast}}}.\blacksquare$                                                                                                                                            
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

It remains to show that ${\mathfrak{E}}^{2} \land {\mathfrak{E}}^{3}$ occurs with probability approaching $1$:

  -- ------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $\lim\limits_{n\rightarrow\infty}{\Pr{\lbrack{{\mathfrak{E}}^{2} \land {\mathfrak{E}}^{3}}\rbrack}}$   $= {1 - {\lim\limits_{n\rightarrow\infty}{\Pr{\lbrack{\overline{{\mathfrak{E}}^{2}} \vee \overline{{\mathfrak{E}}^{3}}}\rbrack}}}}$                                              
                                                                                                            ${\geq {1 - {\lim\limits_{n\rightarrow\infty}\left( {{\Pr{\lbrack\overline{{\mathfrak{E}}^{2}}\rbrack}} + {\Pr{\lbrack\overline{{\mathfrak{E}}^{3}}\rbrack}}} \right)}} = 1}.$   
  -- ------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

## V Conclusion 

In this paper we revisited the original asymptotic-optimality proof of RRT^∗^ in \[1\], and discussed an apparent logical gap within it. We then introduced an alternative proof that amends this logical gap. Our new proof suggests that the connection radius of RRT^∗^ should be slightly larger than the original bound on the radius that was developed in \[1\]. We leave the question of whether our bound is tight, i.e., whether the exponent of $1/{({d + 1})}$ in Equation (2) can be lowered to $1/d$, to future research. The practical successes of the algorithm and its extensions, using the exponent $1/d$, provide some evidence that this might be the case.

## Acknowledgments 

We thank Sertac Karaman for insightful discussions on his work \[1\]. We also thank Michal Kleinbort for feedback on the manuscript. This work was supported in part by NSF, Award Number: 1931815.

We provide a detailed counter example (Figures 2-12) illustrating our argument that the fact that for every $1 \leq i < M_{n}$ (i) there exist $X_{j_{i}},X_{j_{i + 1}}$ such that ${X_{j_{i}} \in B_{n,i}},{X_{j_{i + 1}} \in B_{n,{i + 1}}}$ and (ii) $j_{i} < j_{i + 1}$, does not necessarily mean that (iii) there exists a sequence $j_{1} \leq j_{2} \leq \ldots \leq j_{M_{n}}$ such that $X_{j_{i}} \in B_{n,i}$ for every $1 \leq i < M_{n}$ (see Section III-B).

Figure 2: The input scenario for the counter example. The goal is to find a path from configuration s on the left to t on the right, while avoiding the two gray obstacles. The path σε is drawn as a black curve.

Figure 3: The first three samples X1, X2, X3 are drawn by the algorithm, where X3 = t. The edge (s,X1) is added first through line 5 of Algorithm 2. The edges (X1,X2), (X2,X3) are added in a similar fashion. We assume that no rewiring occurs in those steps due to the smaller magnitude of r1 in comparison to ∥X1 − X3∥. We also mention that the length of the new path to t just discovered can be made arbitrarily long with respect to σε by moving X1, X2 further away from s and t respectively, and setting the steering parameter η to be large enough to support such long connections.

Figure 4: We construct a sequence of Mn balls Bn, 1, …, Bn, Mn, which we denote for simplicity by b1, …, bMn, and we fix n = 23. For simplicity, we set Mn = 12 in the illustration, to avoid unnecessarily complicating the visualization. Below we also assume that the connection radius r23 used by RRT∗ is equal to the diameter of any ball bi, although a similar out come will follow when r23 is much larger (as long as r23 &lt; ∥X2 − X3∥).

Figure 5: Next, we generate the sample X4 ∈ b11, which introduces the edge (X3,X4) and does not result in rewiring. As we mentioned earlier, we assume that rn &lt; ∥X2 − X3∥, which implies that the edge (X2,X4) will not be considered.

Figure 6: Next, we generate the sample X5 ∈ b12, which introduces the edge (X4,X5), since the cost-to-come via X3 is smaller than through a connection from X4. Clearly, the edge (X5,X4) cannot improve the cost-to-come of X4, and it is therefore not added in the rewiring stage. Observe that X4 ∈ b11, X5 ∈ b12, and X4 was sampled before X5, which implies that conditions (i), (ii) are satisfied locally for b11, b12.

Figure 7: Similarly to X4, the sample X6 is produced in b10, which yields the edge (X4,X6), and introduces no rewiring.

Figure 8: Similarly to X5, the sample X7 is produced in b11, and the edge (X4,X6) is left intact.

Figure 9: In a similar manner, we introduce incrementally the samples X8 ∈ b9, X9 ∈ b10. Notice that a path from t in the opposite direction of the balls towards s (currently till X8) is beginning to form.

Figure 10: This sample scheme can be repeated until the sample X22 ∈ b2 is produced, which is within r23 distance from s. This introduces the edge (s,X22), which minimizes the cost-to-come to X22.

Figure 11: The introduction of X22 forces a rewire of X20 and X18 within the same iteration: the edges (X22,X20), (X22,X18) are added, whereas (X18,X20) and (X16,X18) are removed. It is important to note that by definition of RRT∗, this rewire does not promote further rewiring to the predecessors of X18, X20 in G.

Figure 12: Finally, the sample X23 ∈ b3 is drawn, and the edge (s,X23) is added. This will promote additional rewires to X16, X19, X18, X21,in the vicinity of X23, although as earlier those rewires will not propagate to other vertices of G. It is clear that at this point for every 1 ≤ i &lt; Mn it holds that there exist (i) Xji ∈ bi, Xji + 1 ∈ bi + 1 and (ii) ji &lt; ji + 1. Unfortunately, the graph G does not contain a path starting at s and going sequentially through the balls b1, …, b12 until t is reached. To conclude, even though conditions (i), (ii) hold, RRT∗ will return the path consisting of the vertices s, X1, X2, t, which is substantially longer than σε.

## References 

-   [\[1\] S. Karaman and E. Frazzoli, "Sampling-based algorithms for optimal motion planning," *International Journal of Robotics Research*, vol. 30, no. 7, pp. 846--894, 2011.]
-   [\[2\] ------, "Optimal kinodynamic motion planning using incremental sampling-based methods," in *IEEE Conference on Decision and Control*, 2010, pp. 7681--7687.]
-   [\[3\] ------, "Sampling-based optimal motion planning for non-holonomic dynamical systems," in *IEEE International Conference on Robotics and Automation*, 2013, pp. 5041--5047.]
-   [\[4\] G. Goretkin, A. Perez, R. Platt, and G. Konidaris, "Optimal sampling-based planning for linear-quadratic kinodynamic systems," in *IEEE International Conference on Robotics and Automation*, 2013, pp. 2429--2436.]
-   [\[5\] D. J. Webb and J. van den Berg, "Kinodynamic RRT\*: Optimal motion planning for systems with linear differential constraints," in *IEEE International Conference on Robotics and Automation*, 2013, pp. 5054--5061.]
-   [\[6\] L. I. Reyes Castro, P. Chaudhari, J. Tumova, S. Karaman, E. Frazzoli, and D. Rus, "Incremental sampling-based algorithm for minimum-violation motion planning," in *IEEE Conference on Decision and Control*, 2013, pp. 3217--3224.]
-   [\[7\] W. Liu and M. H. Ang, Jr., "Incremental sampling-based algorithm for risk-aware planning under motion uncertainty," in *IEEE International Conference on Robotics and Automation*, 2014, pp. 2051--2058.]
-   [\[8\] B. Akgun and M. Stilman, "Sampling heuristics for optimal motion planning in high dimensions," in *IEEE/RSJ International Conference on Intelligent Robots and Systems*, 2011, pp. 2640--2645.]
-   [\[9\] J. D. Gammell, S. S. Srinivasa, and T. D. Barfoot, "Informed RRT\*: Optimal sampling-based path planning focused via direct sampling of an admissible ellipsoidal heuristic," in *IEEE/RSJ International Conference on Intelligent Robots and Systems*, 2014, pp. 2997--3004.]
-   [\[10\] L. Janson, E. Schmerling, A. A. Clark, and M. Pavone, "Fast marching tree: A fast marching sampling-based method for optimal motion planning in many dimensions," *International Journal of Robotics Research*, vol. 34, no. 7, pp. 883--921, 2015.]
-   [\[11\] J. J. Kuffner and S. M. LaValle, "RRT-Connect: An efficient approach to single-query path planning," in *IEEE International Conference on Robotics and Automation*, 2000, pp. 995--1001.]
-   [\[12\] K. Solovey, L. Janson, E. Schmerling, E. Frazzoli, and M. Pavone, "Revisiting the asymptotic optimality of RRT," *CoRR*, vol. abs/1909.09688, 2019.]
-   [\[13\] K. Solovey and M. Kleinbort, "The critical radius in sampling-based motion planning," *International Journal of Robotics Reseasrch*, 2019.]
-   [\[14\] M. Kleinbort, K. Solovey, Z. Littlefield, K. E. Bekris, and D. Halperin, "Probabilistic completeness of RRT for geometric and kinodynamic planning with forward propagation," *IEEE Robotics and Automation Letters*, 2019.]
