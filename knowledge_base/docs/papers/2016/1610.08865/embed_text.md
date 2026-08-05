<!-- arxiv-full-text:v1 {"arxiv_id": "1610.08865", "source": "ar5iv"} -->

## Introduction

Rapidly-Exploring Random Trees (RRT) is one of the most popular planning algorithms, especially when the search space is high-dimensional and finding the optimal path is computationally expensive. RRT performs well on many problems where classical dynamic programming based algorithms, such as A\*, perform poorly. RRT is essentially an exploration algorithm, and in the most basic implementation, the algorithm even ignores the goal information, which seems to be a major reason for its success. Planning problems, especially those in robotics, often feature narrow pathways connecting large explorable regions; combined with high dimensionality, this means that finding the optimal path is usually intractable. However, RRT often provides a feasible path quickly.

Although many attempts have been made to improve the basic algorithm, RRT has proven difficult to improve upon. In fact, given extra computation, repeatedly running RRT often produces competitive solutions. In this paper, we show that a simple alternative greatly improves upon RRT. We propose using the Hit-and-Run algorithm for feasible path search. Arguably simpler than RRT, the Hit-and-Run is a rapidly mixing MCMC sampling algorithm for producing a point uniformly at random from a convex space. color=blue!20!white,\]Victor: not that clear, you mean hnr is simpler that RRT? insist maybe more on what still need to be improved from RRT or say that you will detail later Not only Hit-and-Run finds a feasible path faster than RRT, it is also more robust with respect to the geometry of the space.

Before giving more details, we define the planning and sampling problems that we consider. Let $\Sigma$ be a bounded connected subset of ${\mathbb{R}}^{n}$. For points ${a,b} \in \Sigma$, we use $\lbrack a,b\rbrack$ to denote their (one-dimensional) convex hull. Given a starting point $a_{1}$ and a goal region $\mathcal{G} \subset \Sigma$, the planning problem is to find a sequence of points $\{ a_{1},a_{2},\ldots,a_{\tau}\}$ for $\tau \geq 1$ such that all points are in $\Sigma$, $a_{\tau}$ is in $\mathcal{G}$, and for $t = {2,\ldots,\tau}$, ${\lbrack a_{t - 1},a_{t}\rbrack} \subset \Sigma$.

The sampling problem is to generate points uniformly at random from $\Sigma$. Sampling is often difficult, but Markov Chain Monte Carlo (MCMC) algorithms have seen empirical and theoretical success. MCMC algorithms, such as Hit-and-Run and Ball-Walk, sample a Markov Chain on $\Sigma$ that has a stationary distribution equal to the uniform distribution on $\Sigma$; then, if we run the Markov Chain long enough, the marginal distribution of the sample is guaranteed to come from a distribution exponentially close to the target distribution. Solving the sampling problem yields a solution to the planning problem; one can generate samples and terminate when $a_{t}$ hits $\mathcal{G}$.

Figure 1: RRT (left) and Hit-and-Run (right) Let us define Hit-and-Run and the RRT algorithms (see also Figure 1 for an illustration). Hit-and-Run defines a Markov chain on $\Sigma$ where the transition dynamics are as follows. A direction is chosen uniformly at random, and $a_{t + 1}$ is chosen uniformly from the largest chord contained in $\Sigma$ in this direction passing through $a_{t}$. This Markov Chain has a uniform stationary distribution on $\Sigma$. As a planning algorithm, this chain continues until it hits the goal region. Let $\tau$ be the stopping time. The solution path is $\{ a_{1},a_{2},\ldots,a_{\tau}\}$.

On the other hand, the RRT algorithm iteratively builds a tree $T$ with $a_{1}$ as a root and nodes labeled as $a^{n} \in \Sigma$ and edges $\{ a^{m},a^{n}\}$ that satisfy ${\lbrack a^{m},a^{n}\rbrack} \subseteq \Sigma$. To add a point to the tree, $a^{r}$ is uniformly sampled from $\Sigma$ and its nearest neighbor $a^{n} \in T$ is computed. If ${\lbrack a^{n},a^{r}\rbrack} \subset \Sigma$, then node $a^{r}$ and edge $\lbrack a^{n},a^{r}\rbrack$ are added to $T$. Otherwise, we search for the point $a^{e} \in {\lbrack a^{n},a^{r}\rbrack}$ farthest from $a^{n}$ such that ${\lbrack a^{n},a^{e}\rbrack} \subseteq \Sigma$. Then $a^{e}$ and $\lbrack a^{n},a^{e}\rbrack$ are added to the tree. This process is continued until we add an edge terminating in $\mathcal{G}$ and the sequence of points on that branch is returned as the solution path. In the presence of dynamic constraints, a different version of RRT that makes only small local steps is used. These versions will be discussed in the experiments section.

There are two main contributions on this paper. First, we analyze the Hit-and-Run algorithm in a non-convex space and show that the mixing time is polynomial in dimensionality as long as certain smoothness conditions are satisfied. The mixing time of Hit-and-Run for convex spaces is known to be polynomial. However, to accommodate planning problems, we focus on non-convex spaces. Our analysis reveals an intriguing connection between fast mixing and the existence of smooth measure-preserving mappings. The only existing analysis of random walk algorithms in non-convex spaces is due to Chandrasekaran et al. who analyzed Ball-Walk in star-shaped bodies.^11^1We say $S$ is star-shaped if the kernel of $S$, define by $K_{S} = {\{{x \in S}:{{\forall y} \in {S{\lbrack x,y\rbrack}} \subset S}\}}$, is nonempty. Second, we propose Hit-and-Run for planning problems as an alternative to RRT and show that it finds a feasible path quickly. From the mixing rate, we obtain a bound on the expected length of the solution path in the planning problem. Such performance guarantees are not available for RRT.

The current proof techniques in the analysis of Hit-and-Run heavily rely on the convexity of the space. It turns out that non-convexity is specially troubling when points are close to the boundary. We overcome these difficulties as follows. First, Lovász and Vempala show a tight isoperimetic inequality in terms of average distances instead of minimum distances. This enables us to ignore points that are sufficiently close to the boundary. Next we show that as long as points are sufficiently far from the boundary, the cross-ratio distances in the convex and non-convex spaces are closely related. Finally we show that, given a curvature assumption, if two points are close geometrically and are sufficiently far from the boundary, then their proposal distributions must be close as well. color=blue!20!white,\]Victor: what is a proposal distribution? color=blue!20!white,\]Victor: theoretical results for RRT in the litterature?

Hit-and-Run has a number of advantages compared to RRT; it does not require random points sampled from the space (which is itself a hard problem), and it is guaranteed to reach the goal region with high probability in a polynomial number of rounds. In contrast, there are cases where RRT growth can be very slow (see the experiments sections for a discussion). Moreover, Hit-and-Run provides safer solutions, as its paths are more likely to stay away from the boundary. In contrast, a common issue with RRT solutions is that they tend to be close to the boundary. Because of this, further post-processing steps are needed to smooth the path. color=blue!20!white,\]Victor: insist more on the fact that you do not change hitand run or propose a new version just show that the original algo is the solution and you provide the analysis which is cool

### Notation

For a set $K$, we will denote the $n$-dimensional volume by $\text{vol}{(K)}$, the $({n - 1})$-dimensional surface volume by $S_{K} = {\text{vol}_{n - 1}{({\partial K})}}$, and the boundary by $\partial K$. The diameter of $K$ is $D_{K} = {\max_{{x,x'} \in K}\left| {x - x'} \right|}$, where $| \cdot |$ will be used for absolute value and Euclidean norm, and the distance between sets $K_{1}$ and $K_{2}$ is defined as ${d{(K_{1},K_{2})}} = {\min_{{x \in K_{1}},{y \in K_{2}}}\left| {x - y} \right|}$. Similarly, ${d{(x,K)}} = {d{({\{ x\}},K)}}$. For a set $K$, we use $K^{\epsilon}$ to denote $\{{x \in K}:{{d{(x,{\partial K})}} \geq \epsilon}\}$. Finally, for distributions $P$ and $Q$, we use $d_{tv}{(P,Q)}$ to denote the total variation distance between $P$ and $Q$.

We will also need some geometric quantities. We will denote lines (i.e., 1-dimensional affine spaces) by $\ell$. For ${x,y} \in K$, we denote their convex hull, that is, the line segment between them, by $\lbrack x,y\rbrack$ and $\ell{(x,y)}$ the line that passes through $x$ and $y$ (which contains $\lbrack x,y\rbrack$). We also write $\lbrack x_{1},\ldots,x_{k}\rbrack$ to denote that $x_{1},\ldots,x_{k}$ are collinear.

We also use $\ell_{K}{(x,y)}$ to denote the longest connected chord through $x \in K$ and $y \in K$ contained in $K$ and $|{\ell_{K}{(x,y)}}|$ its length. We use $a{(x,y)}$ and $b{(x,y)}$ to denote the endpoints of $\ell_{K}{(x,y)}$ that are closer to $x$ and $y$, respectively, so that ${\ell_{K}{(x,y)}} = {\lbrack{a{(x,y)}},{b{(x,y)}}\rbrack} = {\lbrack{b{(y,x)}},{a{(y,x)}}\rbrack}$. The Euclidean ball of unit radius centered at the origin, ${B_{n}{}} \subset {\mathbb{R}}^{n}$, has volume $\pi_{n}$. We use $x_{1:m}$ to denote the sequence $x_{1},\ldots,x_{m}$. Finally we use $a \land b$ to denote $\min{(a,b)}$.

## Sampling from Non-Convex Spaces

Most of the known results for the sampling times of the Hit-and-Run exist for convex sets only. We will think of $\Sigma$ as the image of some convex set $\Omega$ under a measure preserving, bilipschitz function $g$. The goal is to understand the relevant geometric quantities of $\Sigma$ through properties of $g$ and geometric properties of $\Omega$. We emphasize that the existence of the map $g$ and its properties are necessary for the analysis, but the actual algorithm does not need to know $g$. We formalize this assumption below as well as describe how we interact with $\Sigma$ and present a few more technical assumptions required for our analysis. We then present our main result, and follow that with some conductance results before moving on to the proof of the theorem in the next section.

### Assumption 1 (Oracle Access)

Given a point $u$ and a line $\ell$ that passes through $u$, the oracle returns whether $u \in \Sigma$, and, if so, the largest connected interval in $\ell \cap \Sigma$ containing $u$.

### Assumption 2 (Bilipschitz Measure-Preserving Embeddings)

There exist a convex set $\Omega \subset {\mathbb{R}}^{n}$ and a bilipschitz, measure-preserving map $g$ such that $\Sigma$ is the image of $\Omega$ under $g$. That is, there exists a function $g$ with $\left| {D_{g}{(x)}} \right| = 1$ (i.e. the Jacobian has unit determinant) with constants $L_{\Sigma}$ and $L_{\Omega}$ such that, for any ${x,y} \in \Omega$, In words, $g$ is measure-preserving, $g$ is $L_{\Sigma}$-Lipschitz, and $g^{- 1}$ is $L_{\Omega}$-Lipschitz.

As an example, Fonseca and Parry shows that for any star-shaped space, a smooth measure-preserving embedding exists. One interesting consequence of Assumption 2. ‣ 2 Sampling from Non-Convex Spaces ‣ Hit-and-Run for Sampling and Planning in Non-Convex Spaces") is that because the mapping is measure-preserving, there must exist a pair ${x,y} \in \Omega$ such that $\left| {{g{(x)}} - {g{(y)}}} \right| \geq \left| {x - y} \right|$. Otherwise, ${\int_{\Omega}g} \leq 1$, a contradiction. Similarly, there must exist a pair ${u,v} \in \Sigma$ such that $\left| {{g^{- 1}{(u)}} - {g^{- 1}{(v)}}} \right| \geq \left| {u - v} \right|$. Thus, To simplify the analysis, we will assume that $\Omega$ is a ball with radius $r$. In what follows, we use $x,y,z$ to denote points in $\Omega$, and $u,v,w$ to denote points in $\Sigma$. We will also assume that $\Sigma$ has no sharp corners and has a smooth boundary:

### Assumption 3 (Low Curvature)

For any two dimensional plane $\mathcal{H} \subset {\mathbb{R}}^{n}$, let $\kappa_{\mathcal{H}}$ be the curvature of ${\partial\Sigma} \cap \mathcal{H}$ and $\mathcal{R}_{\mathcal{H}}$ be the perimeter of ${\partial\Sigma} \cap \mathcal{H}$. We assume that $\Sigma$ has low curvature, i.e. that $\kappa = {\sup_{\mathcal{H}}{\kappa_{\mathcal{H}}\mathcal{R}_{\mathcal{H}}}}$ is finite.

Assumption 2. ‣ 2 Sampling from Non-Convex Spaces ‣ Hit-and-Run for Sampling and Planning in Non-Convex Spaces") does not imply low curvature, as there exist smooth measure-preserving mappings from the unit ball to a cube.

### Assumption 4

We assume that the volume of $\Sigma$ is equal to one. We also assume that $\Sigma$ contains a Euclidean ball of radius one.

Note that the unit ball has volume less than 1 for $n > 12$, so for small dimensional problems, we will need to relax this assumption.

We motivate the forthcoming technical machinery by demonstrating what it can accomplish. The following theorem is the main result of the paper, and the proof makes up most of Section 3.

### Theorem 5

Consider the Hit-and-Run algorithm. Let $\sigma_{0}$ be the distribution of the initial point given to Hit-and-Run, $\sigma_{t}$ be the distribution after $t$ steps of Hit-and-Run, and $\sigma$ be the stationary distribution (which is uniform). Let $M = {\sup_{A}{{{\sigma_{0}{(A)}}/\sigma}{(A)}}}$. Let $\epsilon$ be a positive scalar. After steps, we have ${d_{tv}{(\sigma_{t},\sigma)}} \leq \epsilon$. Here $C'$ is a low order polynomial of $L_{\Omega},L_{\Sigma},\kappa$.

## Analysis

This section proves Theorem 5. We begin by stating a number of useful geometrical results, which allow us to prove the two main components: an isoperimetric inequality in Section 3.2 and a total variation inequality in Section 3.3. We then combine everything in Section 3.4.

### Fast Mixing Markov Chains

We rely on the notion of conductance color=blue!20!white,\]Victor: reference? as our main technical tool. This section recalls the relevant results.

We say that points ${u,v} \in \Sigma$ see each other if ${\lbrack u,v\rbrack} \subseteq \Sigma$. We use $\text{view}{(u)}$ to denote all points in $\Sigma$ visible from $u$. Let $\ell_{\Sigma}{(u,v)}$ denote the chord through $u$ and $v$ inside $\Sigma$ and $\left| {\ell_{\Sigma}{(u,v)}} \right|$ its length. Let $P_{u}{(A)}$ be the probability of being in set $A \subset \Sigma$ after one step of Hit-and-Run from $u$ and $f_{u}$ its density function. By an argument similar to the argument in Lemma 3 of Lovász, we can show that The conductance of the Markov process is defined as We begin with a useful conductance result that applies to general Markov Chains.

### Lemma 6 (Corollary 1.5 of Lovász and Simonovits )

Let $M = {\sup_{A}{{{\sigma_{0}{(A)}}/\sigma}{(A)}}}$. Then for every $A \subset \Sigma$, Proving a lower bound on the conductance is therefore a key step in the mixing time analysis. Previous literature has shown such lower bounds for convex spaces. Our objective in the following is to obtain such bounds for more general non-convex spaces that satisfy bilipschtiz measure-preserving embedding and low curvature assumptions. color=blue!20!white,\]Alan: Maybe Add a comment about how this part of the paper applies for general Markov chains even though they are studying random walks on a convex body.

As in previous literature, we shall find that the following *cross-ratio distance* is very useful in deriving an isoperimetric inequality and a total variation inequality.

### Definition 1

Let $\lbrack a,u,v,b\rbrack$ be collinear and inside $\Sigma$, such that ${a,b} \in {\partial\Sigma}$. Define It is easy to see that ${d_{\Sigma}{(u,v)}} \geq {{4\left| {u - v} \right|}/D_{\Sigma}}$. We define the following distance measure for non-convex spaces.

### Definition 2

A set $\Sigma$ will be called $\tau$-best if, for any ${u,v} \in \Sigma$, there exist points $z_{1},\ldots,z_{\tau - 1}$ such that ${\lbrack u,z_{1}\rbrack},{\lbrack z_{\tau - 1},v\rbrack}$, and $\lbrack z_{i},z_{i + 1}\rbrack$ for $i = {1,\ldots,{\tau - 2}}$ are all in $\Sigma$; i.e., any two points in $\Sigma$ can be connected by $\tau$ line segments that are all inside $\Sigma$. We define the distance and, by extension, the distance between two subsets ${\Sigma_{1},\Sigma_{2}} \subset \Sigma$ as ${{\overset{\sim}{d}}_{\Sigma}{(\Sigma_{1},\Sigma_{2})}} = {\inf_{{u \in \Sigma_{1}},{v \in \Sigma_{2}}}{{\overset{\sim}{d}}_{\Sigma}{(u,v)}}}$.

The analysis of the conductance is often derived via an isoperimetric inequality.

### Theorem 7 (Theorem 4.5 of Vempala )

Let $\Omega$ be a convex body in ${\mathbb{R}}^{n}$. Let $h:{\Omega\rightarrow{\mathbb{R}}^{+}}$ be an arbitrary function. Let $(\Omega_{1},\Omega_{2},\Omega_{3})$ be any partition of $\Omega$ into measurable sets. Suppose that for any pair of points $x \in \Omega_{1}$ and $y \in \Omega_{2}$ and any point $z$ on the chord of $\Omega$ through $x$ and $y$, ${h{(z)}} \leq {{({1/3})}{\min{(1,{d_{\Omega}{(x,y)}})}}}$. Then where the expectation is defined with respect to the uniform distribution on $\Omega$.

Given an isoperimetric inequality, a total variation inequality is typically used in a mixing time analysis to lower bound cross-ratio distances and then lower bound the conductance. Our approach is similar. We use the embedding assumption to derive an isoperimetric inequality in the non-convex space $\Sigma$. Then we relate cross-ratio distance $d_{\Omega}$ to distance ${\overset{\sim}{d}}_{\Sigma}$. This approximation is good when the points are sufficiently far from the boundary. We incur a small error in the mixing bound by ignoring points that are too close to the boundary. Finally we use the curvature condition to derive a total variation inequality and to lower bound the conductance.

### Cross-Ratio Distances

The first step is to show the relationship between cross-ratio distances in the convex and non-convex spaces. We show that these distances are close as long as points are far from the boundary. These results will be used in the proof of the main theorem in Section 3.4 to obtain an isoperimetric inequality in the non-convex space. First we define a useful quantity.

### Definition 3

Consider a convex set $\Omega$ with some subset $\Omega'$ and collinear points $\{ a,x,b\}$ with ${a,b} \in {\partial\Omega}$, $x \in \Omega'$, and $\left| {x - b} \right| \leq \left| {x - a} \right|$. Let $c$ be a point on $\partial\Omega$. Let ${R{(a,x,b,c)}} = {\left| {x - b} \right|/\left| {x - c} \right|}$. We use $R{(\Omega,\Omega')}$ to denote the maximum of $R{(a,x,b,c)}$ over all such points. We use $R_{\epsilon}$ to denote $R{(\Omega,\Omega^{\epsilon})}$.

The following lemma is the main technical lemma, and we use it to express ${\overset{\sim}{d}}_{\Sigma}$ in terms of $d_{\Omega}$.

### Lemma 8

Let $\epsilon$ be a positive scalar such that ${R_{\epsilon}{({1 + {8R_{\epsilon}}})}} \geq {2/3}$. Let $\{ a,x_{1},x_{2},b\}$ be collinear such that $a$ and $b$ are on the boundary of $\Omega$, ${x_{1},x_{2}} \in \Omega^{\epsilon}$, and $\left| {x_{1} - a} \right| < \left| {x_{2} - a} \right|$. Let $c$ and $d$ be two points on the boundary of $\Omega$. Then

### Proof

We prove the claim by proving that ${A/B} \geq {1/{({4R_{\epsilon}{({1 + {2R_{\epsilon}}})}})}}$.\Case 1, $\left| {x_{1} - b} \right| \leq \left| {x_{1} - a} \right|$: In this case, $x_{1}$ and $x_{2}$ are both on the line segment $\lbrack{{({a + b})}/2},b\rbrack$. We consider two cases.\Case 1.1, $\left| {x_{2} - d} \right| \leq \left| {x_{2} - b} \right|$: We have that Because $\left| {x_{1} - a} \right| < \left| {x_{2} - a} \right|$ by the assumption of the lemma, we have $\left| {x_{2} - b} \right| < \left| {x_{1} - b} \right|$. Also because $\left| {x_{1} - b} \right| \leq \left| {x_{1} - a} \right|$ in Case 1, we have ${\left| {x_{1} - b} \right|/\left| {c - x_{1}} \right|} \leq R_{\epsilon}$. Thus We use also that by definition of $R_{\epsilon}$ $\left| {x_{2} - b} \right| \leq {R_{\epsilon}\left| {x_{2} - d} \right|}$. This and the previous result lets us bound Case 1.2, $\left| {x_{2} - d} \right| > \left| {x_{2} - b} \right|$:\Case 1.2.1, $\left| {c - x_{1}} \right| \leq \left| {x_{2} - d} \right|$: We have that $\left| {x_{2} - b} \right| < \left| {x_{1} - b} \right| \leq {R_{\epsilon}\left| {x_{1} - c} \right|}$. Thus, Case 1.2.2, $\left| {c - x_{1}} \right| > \left| {x_{2} - d} \right|$: As before, we bound $A$ and $B$ separately: Putting these together, where the second inequality holds because ${R_{\epsilon}{({1 + {8R_{\epsilon}}})}} \geq {2/3}$.\Case 2, $\left| {x_{1} - b} \right| > \left| {x_{1} - a} \right|$ and $\left| {x_{2} - b} \right| < \left| {x_{2} - a} \right|$: In this case, $x_{1}$ and $x_{2}$ are on opposite sides of the point ${({a + b})}/2$. Let $M$ be a positive constant. We will choose $M = 4$ later.\Case 2.1, $\left| {c - d} \right| \leq {M\left| {c - x_{1}} \right|}$: We bound Case 2.2, $\left| {c - d} \right| > {M\left| {c - x_{1}} \right|}$:\Case 2.2.1, $\left| {c - d} \right| \leq {M\left| {a - b} \right|}$: We have that Case 2.2.2, $\left| {c - d} \right| > {M\left| {a - b} \right|}$: Let $x_{0}$ be a point on the line segment $\lbrack x_{1},x_{2}\rbrack$. Let $\beta_{1}$ be the angle between line segments $\lbrack c,x_{1}\rbrack$ and $\lbrack x_{1},x_{0}\rbrack$. We write By the triangle inequality, Let $\beta_{2}$ be the angle between line segments $\lbrack d,x_{2}\rbrack$ and $\lbrack x_{2},x_{0}\rbrack$. Let $w = {1 - {2/M}}$. We write which is a quadratic inequality in $\left| {x_{2} - d} \right|$. Thus it holds that If we choose $M = 4$, then $\left| {x_{2} - d} \right| \geq {0.25\left| {c - d} \right|}$ and Finally, observe that Case 3 follows by symmetry from Case 1. ∎ The following lemma states that the distance $d_{\Omega}$ does not increase by adding more steps.

### Lemma 9

Let $a,y_{1},y_{2},\ldots,y_{m},b$ be in the convex body $\Omega$ such that the points $\{ a,y_{1},y_{2},\ldots,y_{m},b\}$ are collinear. Further assume that ${a,b} \in {\partial\Omega}$. We have that

### Proof

The next lemma upper bounds ${\overset{\sim}{d}}_{\Sigma}$ in terms of $d_{\Omega}$.

### Lemma 10

Let ${x_{1},x_{2}} \in \Omega^{\epsilon}$. We have that

### Proof

First we prove the inequality for the case that ${g{(x_{1})}} \in {\text{view}{({g{(x_{2})}})}}$. Let ${a,b} \in {\partial\Omega}$ be such that the points $\{ a,x_{1},x_{2},b\}$ are collinear. Let ${c,d} \in \Omega$ be points such that the points $\{{g{(c)}},{g{(x_{1})}},{g{(x_{2})}},{g{(d)}}\}$ are collinear and the line connecting $g{(c)}$ and $g{(d)}$ is inside $\Sigma$. By the Lipschitzity of $g$ and $g^{- 1}$ and Lemma 8, Now consider the more general case where ${g{(x_{1})}} \notin {\text{view}{({g{(x_{2})}})}}$. Find a set of points $y_{1},\ldots,y_{\tau}$ such that the line segments ${\lbrack{g{(x_{1})}},{g{(y_{1})}}\rbrack},{\lbrack{g{(y_{1})}},{g{(y_{2})}}\rbrack},\ldots,{\lbrack{g{(y_{\tau})}},{g{(x_{2})}}\rbrack}$ are all inside $\Sigma$. By definition of ${\overset{\sim}{d}}_{\Sigma}$ and Lemma 9, ${\overset{\sim}{d}}_{\Sigma}{({g{(x_{1})}},{g{(x_{2})}})}$ can be upper bounded by

### Total Variation Inequality

In this section, we show that if two points ${u,v} \in \Sigma$ are close to each other, then $P_{u}$ and $P_{v}$ are also close. First we show that if the two points are close to each other, then they have similar views.

### Lemma 11 (Overlapping Views)

Given the curvature $\kappa$ defined in Assumption 3. ‣ 2 Sampling from Non-Convex Spaces ‣ Hit-and-Run for Sampling and Planning in Non-Convex Spaces"), for any ${u,v} \in \Sigma^{\epsilon}$ such that $\left| {u - v} \right| \leq \epsilon' \leq \epsilon$, The proof is in Appendix A. Next we define some notation and show some useful inequalities. For $u \in \Sigma$, let $w$ be a random point obtained by making one step of Hit-and-Run from $u$. Define $F{(u)}$ by ${{\mathbb{P}}\left({\left| {w - u} \right| \leq {F{(u)}}} \right)} = {1/8}$. If ${d{(u,{\partial\Sigma})}} \geq h$, less than $1/8$ of any chord passing through $u$ is inside $B{(u,{h/16})}$. Thus ${{\mathbb{P}}\left({\left| {u - w} \right| \leq {h/16}} \right)} \leq {1/8}$, which implies Intuitively, the total variation inequality implies that if $u$ and $v$ are close geometrically, then their proposal distributions must be close as well.

### Lemma 12

Let ${u,v} \in \Sigma^{\epsilon}$ be two points that see each other. Let $\epsilon' = {\frac{\epsilon}{6}{\min\left(\frac{\pi}{4},\frac{\sin{({\pi/8})}}{\kappa} \right)}}$. Suppose that The proof is in Appendix A. The proof uses ideas from proof of Lemma 9 of Lovász. The proof of Lovász heavily relies on the convexity of the space, which does not hold in our case. We overcome the difficulties using the low curvature assumption and the fact that $u$ and $v$ are sufficiently far from the boundary.

### Putting Everything Together

Next we bound the conductance of Hit-and-Run.

### Lemma 13

where $r$ is the radius of ball $\Omega$ (so ${r^{n}\pi_{n}} = 1$). The conductance $\Phi$ of Hit-and-Run is at least The proof is in Appendix A. In proving this lemma, the non-convexity of $\Sigma$ is specially troubling when points are close to the boundary. We overcome this difficulty by using the isoperimetric inequality shown in Theorem 7). ‣ 3.1 Fast Mixing Markov Chains ‣ 3 Analysis ‣ Hit-and-Run for Sampling and Planning in Non-Convex Spaces"), which is in terms of average distances instead of minimum distances. This enables us to ignore points that are very close to the boundary.

If we treat $L_{\Sigma},L_{\Omega},\kappa$ as constants and collect all constants in $C$, we have a $\Phi \geq {C/n^{3}}$ lower bound for the conductance. Now we are ready to prove the main theorem.

### Proof of Theorem 5

Using Lemma 6). ‣ 3.1 Fast Mixing Markov Chains ‣ 3 Analysis ‣ Hit-and-Run for Sampling and Planning in Non-Convex Spaces") and Lemma 13, ${d_{tv}{(\sigma_{t},\sigma)}} \leq {\sqrt{M}{({1 - {C^{2}/{({2n^{6}})}}})}^{t}}$, which gives the final bound after rearrangement. ∎

## Planning

This section makes an empirical argument for use of the Hit-and-Run in trajectory planning. In the first of two experiments, the state space is a position vector constrained to some map illustrated by the bottom plots of Figure 2. The second experiment also includes two dimensions of velocity in the state and limits state transitions to those that respect the map as well as kinematics and requires the planning to control the system explicitly (by specifying an acceleration vector for every time step). We will show that Hit-and-Run outperforms RRT in both cases by requiring fewer transitions to reach the goal state across a wide variety of map difficulties.

### Position only

The state starts at the bottom left of the spiral and the goal is the top right. Both algorithms are implemented as described in the introduction. The number of tranitions needed to reach the goal of both algorithms is plotted as a function of the width of the spiral arms; the larger the width, the easier the problem.

The results are presented in Figure 2. The top plot show the number of transitions needed by both algorithms as the width of the arms changes, averaged over 500 independent runs. We see that the Hit-and-Run outperforms RRT for all but the hardest problems, usually by a large margin. The two lower plots show the sample points produced from one run with width equal to 1.2; we see that RRT has more uniform coverage, but that Hit-and-Run has a large speedup over linear sections, therefore justifying its faster exploration.

Figure 2: Position only planning example RRT is slow in this problem because in many rounds the tree does not grow in the right direction. For example at the beginning the tree needs to grow upwards, but most random samples will bias the growth to right. As Hit-and-Run only considers the space that is visible to the current point, it is less sensitive to the geometry of the free space. We can make this problem arbitrarily hard for RRT by making the middle part of the spiral fatter. Hit-and-Run, on the other hand, is insensitive to such changes. Additionally, the growth of the RRT tree can become very slow towards the end. This is because the rest of the tree absorbs most samples, and the tree grows only if the random point falls in the vicinity of the goal.

### Kinematic Planning

In this set of simulations, we constrain the state transitions to adhere to the laws of physics: the state propagates forward under kinematics until it exits the permissible map, in which case it stops inelastically at the boundary. The position map is the two-turn corridor, illustrated in the bottom plots of Figure 3. Both algorithms propose points to in the analogous manner to the previous section (where a desired speed is sampled in addition to a desired position); then, the best acceleration vector in the unit ball is calculated and the sample is propagated forward by the kinematics. If the sample point encounters the boundary, the velocity is zeroed. Both RRT and Hit-and-Run are constrained to use the same controller and the only difference is what points are proposed.

Figure 3: Performance under kinematic constraints We see that Hit-and-Run again outperforms RRT across a large gamut of path widths by as much as a factor of three. The bottom two plots are of a typical sample path, and we see that Hit-and-Run has two advantages: it accelerates down straight hallways, and it samples more uniformly from the state space. In contrast, RRT wastes many more samples along the boundaries.

## Conclusions and Future Work

This paper has two main contributions. First, we use a measure-preserving bilipschitz map to extend the analysis of the Hit-and-Run random walk to non-convex sets. Mixing time bounds for non-convex sets open up many applications, for example non-convex optimization via simulated annealing and similar methods. The second contribution of this paper has been to study one such application: the planning problem.

In contrast to RRT, using Hit-and-Run for planning has stronger guarantees on the number of samples needed and faster convergence in some cases. It also avoids the need for a sampling oracle for $\Sigma$, since it combines the search with an approximate sampling oracle. One drawback is that the sample paths for Hit-and-Run have no pruning and are therefore longer than the RRT paths. Hybrid approaches that yield short paths but also explore quickly are a promising future direction.
