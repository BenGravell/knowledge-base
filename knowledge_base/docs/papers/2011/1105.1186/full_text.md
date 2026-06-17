# Sampling-based Algorithms for Optimal Motion Planning

- arXiv ID: [1105.1186](https://arxiv.org/abs/1105.1186)
- HTML source: [ar5iv](https://ar5iv.labs.arxiv.org/html/1105.1186)

Sertac Karaman       Emilio Frazzoli The authors are with the Laboratory for Information and Decision Systems, Massachusetts Institute of Technology, Cambridge, MA.

###### Abstract 

During the last decade, sampling-based path planning algorithms, such as Probabilistic RoadMaps (PRM) and Rapidly-exploring Random Trees (RRT), have been shown to work well in practice and possess theoretical guarantees such as probabilistic completeness. However, little effort has been devoted to the formal analysis of the quality of the solution returned by such algorithms, e.g., as a function of the number of samples. The purpose of this paper is to fill this gap, by rigorously analyzing the asymptotic behavior of the cost of the solution returned by stochastic sampling-based algorithms as the number of samples increases. A number of negative results are provided, characterizing existing algorithms, e.g., showing that, under mild technical conditions, the cost of the solution returned by broadly used sampling-based algorithms converges almost surely to a non-optimal value. The main contribution of the paper is the introduction of new algorithms, namely, PRM^∗^ and RRT^∗^, which are provably asymptotically optimal, i.e., such that the cost of the returned solution converges almost surely to the optimum. Moreover, it is shown that the computational complexity of the new algorithms is within a constant factor of that of their probabilistically complete (but not asymptotically optimal) counterparts. The analysis in this paper hinges on novel connections between stochastic sampling-based path planning algorithms and the theory of random geometric graphs.

Keywords: Motion planning, optimal path planning, sampling-based algorithms, random geometric graphs.

## 1 Introduction 

The robotic motion planning problem has received a considerable amount of attention, especially over the last decade, as robots started becoming a vital part of modern industry as well as our daily life (Latombe, 1991; LaValle, 2006; Choset et al., 2005). Even though modern robots may possess significant differences in sensing, actuation, size, workspace, application, etc., the problem of navigating through a complex environment is embedded and essential in almost all robotics applications. Moreover, this problem is relevant to other disciplines such as verification, computational biology, and computer animation (Latombe, 1999; Bhatia and Frazzoli, 2004; Branicky et al., 2006; Cortes et al., 2007; Liu and Badler, 2003; Finn and Kavraki, 1999).

Informally speaking, given a robot with a description of its dynamics, a description of the environment, an initial state, and a set of goal states, the motion planning problem is to find a sequence of control inputs so as the drive the robot from its initial state to one of the goal states while obeying the rules of the environment, e.g., not colliding with the surrounding obstacles. An algorithm to address this problem is said to be complete if it terminates in finite time, returning a valid solution if one exists, and failure otherwise.

Unfortunately, the problem is known to be very hard from the computational point of view. For example, a basic version of the motion planning problem, called the generalized piano movers problem, is PSPACE-hard (Reif, 1979). In fact, while complete planning algorithms exist (see, e.g., Lozano-Perez and Wesley, 1979; Schwartz and Sharir, 1983; Canny, 1988), their complexity makes them unsuitable for practical applications.

Practical planners came around with the development of cell decomposition methods (Brooks and Lozano-Perez, 1983) and potential fields (Khatib, 1986). These approaches, if properly implemented, relaxed the completeness requirement to, for instance, resolution completeness, i.e., the ability to return a valid solution, if one exists, if the resolution parameter of the algorithm is set fine enough. These planners demonstrated remarkable performance in accomplishing various tasks in complex environments within reasonable time bounds (Ge and Cui, 2002). However, their practical applications were mostly limited to state spaces with up to five dimensions, since decomposition-based methods suffered from large number of cells, and potential field methods from local minima (Koren and Borenstein, 1991). Important contributions towards broader applicability of these methods include navigation functions (Rimon and Koditschek, 1992) and randomization (Barraquand and Latombe, 1993).

The above methods rely on an explicit representation of the obstacles in the configuration space, which is used directly to construct a solution. This may result in an excessive computational burden in high dimensions, and in environments described by a large number of obstacles. Avoiding such a representation is the main underlying idea leading to the development of sampling-based algorithms (Kavraki and Latombe, 1994; Kavraki et al., 1996; LaValle and Kuffner, 2001). See  Lindemann and LaValle (2005) for a historical perspective. These algorithms proved to be very effective for motion planning in high-dimensional spaces, and attracted significant attention over the last decade, including very recent work  (see, e.g., Prentice and Roy, 2009; Tedrake et al., 2010; Luders et al., 2010; Berenson et al., 2008; Yershova and LaValle, 2008; Stilman et al., 2007; Koyuncu et al., 2010). Instead of using an explicit representation of the environment, sampling-based algorithms rely on a collision checking module, providing information about feasibility of candidate trajectories, and connect a set of points sampled from the obstacle-free space in order to build a graph (roadmap) of feasible trajectories. The roadmap is then used to construct the solution to the original motion-planning problem.

Informally speaking, sampling-based methods provide large amounts of computational savings by avoiding explicit construction of obstacles in the state space, as opposed to most complete motion planning algorithms. Even though these algorithms are not complete, they provide probabilistic completeness guarantees in the sense that the probability that the planner fails to return a solution, if one exists, decays to zero as the number of samples approaches infinity (Barraquand et al., 1997)  (see also Hsu et al., 1997; Kavraki et al., 1998; Ladd and Kavraki, 2004). Moreover, the rate of decay of the probability of failure is exponential, under the assumption that the environment has good "visibility" properties (Barraquand et al., 1997). More recently, the empirical success of sampling-based algorithms was argued to be strongly tied to the hypothesis that most practical robotic applications, even though involving robots with many degrees of freedom, feature environments with such good visibility properties (Hsu et al., 2006).

### 1.1 Sampling-Based Algorithms 

Arguably, the most influential sampling-based motion planning algorithms to date include Probabilistic RoadMaps (PRMs) (Kavraki et al., 1996, 1998) and Rapidly-exploring Random Trees (RRTs) (Kuffner and LaValle, 2000; LaValle and Kuffner, 2001; LaValle, 2006). Even though the idea of connecting points sampled randomly from the state space is essential in both approaches, these two algorithms differ in the way that they construct a graph connecting these points.

The PRM algorithm and its variants are multiple-query methods that first construct a graph (the roadmap), which represents a rich set of collision-free trajectories, and then answer queries by computing a shortest path that connects the initial state with a final state through the roadmap. The PRM algorithm has been reported to perform well in high-dimensional state spaces (Kavraki et al., 1996). Furthermore, the PRM algorithm is probabilistically complete, and such that the probability of failure decays to zero exponentially with the number of samples used in the construction of the roadmap (Kavraki et al., 1998). During the last two decades, the PRM algorithm has been a focus of robotics research: several improvements were suggested by many authors and the reasons to why it performs well in many practical cases were better understood (see, e.g., Branicky et al., 2001; Hsu et al., 2006; Ladd and Kavraki, 2004, for some examples).

Even though multiple-query methods are valuable in highly structured environments, such as factory floors, most online planning problems do not require multiple queries, since, for instance, the robot moves from one environment to another, or the environment is not known a priori. Moreover, in some applications, computing a roadmap a priori may be computationally challenging or even infeasible. Tailored mainly for these applications, incremental sampling-based planning algorithms such as RRTs have emerged as an online, single-query counterpart to PRMs (see, e.g., Kuffner and LaValle, 2000; Hsu et al., 2002). The incremental nature of these algorithms avoids the necessity to set the number of samples a priori, and returns a solution as soon as the set of trajectories built by the algorithm is rich enough, enabling on-line implementations. Moreover, tree-based planners do not require connecting two states exactly and more easily handle systems with differential constraints. The RRT algorithm has been shown to be probabilistically complete (Kuffner and LaValle, 2000), with an exponential rate of decay for the probability of failure (Frazzoli et al., 2002). The basic version of the RRT algorithm has been extended in several directions, and found many applications in the robotics domain and elsewhere (see, for instance, Frazzoli et al., 2002; Bhatia and Frazzoli, 2004; Cortes et al., 2007; Branicky et al., 2006, 2003; Zucker et al., 2007). In particular, RRTs have been shown to work effectively for systems with differential constraints and nonlinear dynamics (LaValle and Kuffner, 2001; Frazzoli et al., 2002) as well as purely discrete or hybrid systems (Branicky et al., 2003). Moreover, the RRT algorithm was demonstrated in major robotics events on various experimental robotic platforms (Bruce and Veloso, 2003; Kuwata et al., 2009; Teller et al., 2010; Shkolnik et al., 2011; Kuffner et al., 2002).

Other sampling-based planners of note include Expansive Space Trees (EST) (Hsu et al., 1997, 1999) and Sampling-based Roadmap of Trees (SRT) (Plaku et al., 2005). The latter combines the main features of multiple-query algorithms such as PRM with those of single-query algorithms such as RRT and EST.

### 1.2 Optimal Motion Planning 

In most applications, the quality of the solution returned by a motion planning algorithm is important. For example, one may be interested in solution paths of minimum cost, with respect to a given cost functional, such as the length of a path, or the time required to execute it. The problem of computing optimal motion plans has been proven in Canny and Reif (1987) to be very challenging even in basic cases.

In the context of sampling-based motion planning algorithms, the importance of computing optimal solutions has been pointed out in early seminal papers (LaValle and Kuffner, 2001). However, optimality properties of sampling-based motion planning algorithms have not been systematically investigated, and most of the relevant work relies on heuristics. For example, in many field implementations of sampling-based planning algorithms (see, e.g., Kuwata et al., 2009), it is often the case that since a feasible path is found quickly, additional available computation time is devoted to improving the solution with heuristics until the solution is executed. Urmson and Simmons (2003) proposed heuristics to bias the tree growth in RRT towards those regions that result in low-cost solutions. They have also shown experimental results evaluating the performance of different heuristics in terms of the quality of the solution returned. Ferguson and Stentz (2006) considered running the RRT algorithm multiple times in order to progressively improve the quality of the solution. They showed that each run of the algorithm results in a path with smaller cost, even though the procedure is not guaranteed to converge to an optimal solution. Criteria for restarting multiple RRT runs, in a different context, were also proposed in Wedge and Branicky (2008). A more recent approach is the transition-based RRT (T-RRT) designed to combine rapid exploration properties of the RRT with stochastic global optimization methods (Jaillet et al., 2010; Berenson et al., 2011).

A different approach that also offers optimality guarantees is based on graph search algorithms, such as A^∗^, applied over a finite discretization (based, e.g., on a grid, or a cell decomposition of the configuration space) that is generated offline. Recently, these algorithms received a large amount of attention. In particular, they were extended to run in an anytime fashion (Likhachev et al., 2004, 2008), deal with dynamic environments (Stentz, 1995; Likhachev et al., 2008), and handle systems with differential constraints (Likhachev and Ferguson, 2009). These have also been successfully demonstrated on various robotic platforms (Likhachev and Ferguson, 2009; Dolgov et al., 2009). However, optimality guarantees of these algorithms are only ensured up to the grid resolution. Moreover, since the number of grid points grows exponentially with the dimensionality of the state space, so does the (worst-case) running time of these algorithms.

### 1.3 Statement of Contributions 

To the best of the author's knowledge, this paper provides the first systematic and thorough analysis of optimality and complexity properties of the major paradigms for sampling-based path planning algorithms, for multiple- or single-query applications, and introduces the first algorithms that are both asymptotically optimal and computationally efficient, with respect to other algorithms in this class. A summary of the contributions can be found below, and is shown in Table 1.

As a first set of results, it is proven that the standard PRM and RRT algorithms are not asymptotically optimal, and that the "simplified" PRM algorithm is asymptotically optimal, but computationally expensive. Moreover, it is shown that the $k$-nearest variant of the (simplified) PRM algorithm is not necessarily probabilistically complete (e.g., it is not probabilistically complete for $k = 1$), and is not asymptotically optimal for any fixed $k$.

In order to address the limitations of sampling-based path planning algorithms available in the literature, new algorithms are proposed, i.e., PRM^∗^, RRG, and RRT^∗^, and proven to be probabilistically complete, asymptotically optimal, and computationally efficient. Of these, PRM^∗^ is a batch variable-radius PRM, applicable to multiple-query problems, in which the radius is scaled with the number of samples in a way that provably ensures both asymptotic optimality and computational efficiency. RRG is an incremental algorithm that builds a connected roadmap, providing similar performance to PRM^∗^ in a single-query setting, and in an anytime fashion (i.e., a first solution is provided quickly, and monotonically improved if more computation time is available). The RRT^∗^ algorithm is a variant of RRG that incrementally builds a tree, providing anytime solutions, provably converging to an optimal solution, with minimal computational and memory requirements.

Algorithm
Probabilistic Completeness
Asymptotic Optimality
Monotone Convergence
Time Complexity
Space Complexity

Processing
Query

Existing
Algorithms
PRM
Yes
No
Yes
O (n log n)
O (n log n)
O (n)

sPRM
Yes
Yes
Yes
O (n2)
O (n2)
O (n2)

k-sPRM
Conditional
No
No
O (n log n)
O (n log n)
O (n)

RRT
Yes
No
Yes
O (n log n)
O (n)
O (n)

Proposed
Algorithms
PRM∗
Yes
Yes
No
O (n log n)
O (n log n)
O (n log n)

k-PRM∗

RRG
Yes
Yes
Yes
O (n log n)
O (n log n)
O (n log n)

k-RRG

RRT∗
Yes
Yes
Yes
O (n log n)
O (n)
O (n)

k-RRT∗

Table 1: Summary of results. Time and space complexity are expressed as a function of the number of samples n, for a fixed environment.

In this paper, the problem of planning a path through a connected bounded subset of a $d$-dimensional Euclidean space is considered. As in the early seminal papers on incremental sampling-based motion planning algorithms such as Kuffner and LaValle (2000), no differential constraints are considered (i.e., the focus of the paper is on path planning problems), but our methods can be easily extended to planning in configuration spaces and applied to several practical problems of interest. The extension to systems with differential constraints is deferred to future work (see Karaman and Frazzoli (2010a) for preliminary results).

Finally, the results presented in this article, and the techniques used in the analysis of the algorithms, hinge on novel connections established between sampling-based path planning algorithms in robotics and the theory of random geometric graphs, which may be of independent interest.

A preliminary version of this article has appeared in Karaman and Frazzoli (2010b). Since then a variety of new algorithms based on the the ideas behind PRM^∗^, RRG, and RRT^∗^ have been proposed in the literature. For instance, a probabilistically complete and probabilistically sound algorithm for solving a class of differential games has appeared in Karaman and Frazzoli (2010c). Algorithms based on the RRG were used to solve belief-space planning problems in Bry and Roy (2011). The RRT^∗^ algorithm was used for anytime motion planning in Karaman et al. (2011), where it was also demonstrated experimentally on a full-size robotic fork truck. In Alterovitz et al. (2011), the analysis given in Karaman and Frazzoli (2010b) was used to guarantee computational efficiency and asymptotic optimality of a new algorithm that can trade off between exploration and optimality during planning.

A software library implementing the new algorithms introduced in this paper has been released as open-source software by the authors, and is currently available at [http://ares.lids.mit.edu/software/](http://ares.lids.mit.edu/software/)

### 1.4 Paper Organization 

This paper is organized as follows. Section 2 lays the ground in terms of notation and problem formulation. Section 3 is devoted to the discussion of the algorithms that are considered in the paper: first, the main paradigms for sampling-based motion planning algorithms available in the literature are presented, together with their main variants. Then, the new proposed algorithms are presented and motivated. In Section 4 the properties of these algorithms are rigorously analyzed, formally establishing their probabilistic completeness and asymptotically optimality (or lack thereof), as well as their computational complexity as a function of the number of samples and of the number of obstacles in the environment. Experimental results are presented in Section 5, to illustrate and validate the theoretical findings. Finally, Section 6 contains conclusions and perspectives for future work. In order not to excessively disrupt the flow of the presentation, a summary of notation used throughout the paper, as well as lengthy proofs of important results are presented in the Appendix.

## 2 Preliminary Material 

This section contains some preliminary material that will be necessary for the discussion in the remainder of the paper. Namely, the problems of feasible and optimal motion planning is introduced, and some important results from the theory of random geometric graphs are summarized. The notation used in the paper is summarized in Appendix A.

### 2.1 Problem Formulation 

In this section, the feasible and optimal path planning problems are formalized.

Let $\mathcal{X} = {(0,1)}^{d}$ be the *configuration space*, where $d \in {\mathbb{N}}$, $d \geq 2$. Let $\mathcal{X}_{obs}$ be the obstacle region, such that $\mathcal{X} \smallsetminus \mathcal{X}_{obs}$ is an open set, and denote the obstacle-free space as $\mathcal{X}_{free} = {{cl}\hspace{0pt}{({\mathcal{X} \smallsetminus \mathcal{X}_{obs}})}}$, where ${cl}\hspace{0pt}{( \cdot )}$ denotes the closure of a set. The initial condition $x_{init}$ is an element of $\mathcal{X}_{free}$, and the goal region $\mathcal{X}_{goal}$ is an open subset of $\mathcal{X}_{free}$. A path planning problem is defined by a triplet $(\mathcal{X}_{free},x_{init},\mathcal{X}_{goal})$.

Let $\sigma:{{\lbrack 0,1\rbrack}\rightarrow{\mathbb{R}}^{d}}$; the total variation of $\sigma$ is defined as

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     $${{{TV}\hspace{0pt}{(\sigma)}} = {\sup\limits_{\{{{n \in {\mathbb{N}}},{0 = \tau_{0} < \tau_{1} < \cdots < \tau_{n} = s}}\}}{\sum\limits_{i = 1}^{n}{|{{\sigma\hspace{0pt}{(\tau_{i})}} - {\sigma\hspace{0pt}{(\tau_{i - 1})}}}|}}}}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

A function $\sigma$ with ${{TV}\hspace{0pt}{(\sigma)}} < \infty$ is said to have bounded variation.

###### Definition 1 (Path) 

A function $\sigma:{{\lbrack 0,1\rbrack}\rightarrow{\mathbb{R}}^{d}}$ of bounded variation is called a

-   [•]

    Path, if it is continuous;

-   [•]

    *Collision-free path*, if it is a path, and ${\sigma\hspace{0pt}{(\tau)}} \in \mathcal{X}_{free}$, for all $\tau \in {\lbrack 0,1\rbrack}$;

-   [•]

    *Feasible path*, if it is a collision-free path, ${\sigma\hspace{0pt}{(0)}} = x_{init}$, and ${\sigma\hspace{0pt}{(1)}} \in {{cl}\hspace{0pt}{(\mathcal{X}_{goal})}}$.

The total variation of a path is essentially its length, i.e., the Euclidean distance traversed by the path in ${\mathbb{R}}^{d}$. The feasibility problem of path planning is to find a feasible path, if one exists, and report failure otherwise:

###### Problem 2 (Feasible path planning) 

Given a path planning problem $(\mathcal{X}_{free},x_{init},\mathcal{X}_{goal})$, find a feasible path $\sigma:{{\lbrack 0,1\rbrack}\rightarrow\mathcal{X}_{free}}$ such that ${\sigma\hspace{0pt}{(0)}} = x_{init}$ and ${\sigma\hspace{0pt}{(1)}} \in {{cl}\hspace{0pt}{(\mathcal{X}_{goal})}}$, if one exists. If no such path exists, report failure.

Let $\Sigma$ denote the set of all paths, and $\Sigma_{free}$ the set of all collision-free paths. Given two paths ${\sigma_{1},\sigma_{2}} \in \Sigma$, such that ${\sigma_{1}\hspace{0pt}{(1)}} = {\sigma_{2}\hspace{0pt}{(0)}}$, let $\left. \sigma_{1} \middle| \sigma_{2} \right. \in \Sigma$ denote their concatenation, i.e., ${{(\left. \sigma_{1} \middle| \sigma_{2} \right.)}\hspace{0pt}{(\tau)}}:={\sigma_{1}\hspace{0pt}{({2\hspace{0pt}\tau})}}$ for all $\tau \in {\lbrack 0,{1/2}\rbrack}$ and ${{(\left. \sigma_{1} \middle| \sigma_{2} \right.)}\hspace{0pt}{(\tau)}}:={\sigma_{2}\hspace{0pt}{({{2\hspace{0pt}\tau} - 1})}}$ for all $\tau \in {({1/2},1\rbrack}$. Both $\Sigma$ and $\Sigma_{free}$ are closed under concatenation. Let $c:{\Sigma\rightarrow R_{\geq 0}}$ be a function, called the cost function, which assigns a strictly positive cost to all non-trivial collision-free paths (i.e., ${c\hspace{0pt}{(\sigma)}} = 0$ if and only if ${{\sigma\hspace{0pt}{(\tau)}} = {\sigma\hspace{0pt}{(0)}}},{{\forall\tau} \in {\lbrack 0,1\rbrack}}$). The cost function is assumed to be monotonic, in the sense that for all ${\sigma_{1},\sigma_{2}} \in \Sigma$, ${c\hspace{0pt}{(\sigma_{1})}} \leq {c\hspace{0pt}{(\left. \sigma_{1} \middle| \sigma_{2} \right.)}}$, and bounded, in the sense that there exists $k_{c}$ such that ${c\hspace{0pt}{(\sigma)}} \leq {k_{c}\hspace{0pt}{TV}\hspace{0pt}{(\sigma)}}$, ${\forall\sigma} \in \Sigma$.

The optimality problem of path planning asks for finding a feasible path with minimum cost:

###### Problem 3 (Optimal path planning) 

Given a path planning problem $(\mathcal{X}_{free},x_{init},\mathcal{X}_{goal})$ and a cost function $c:{\Sigma\rightarrow{\mathbb{R}}_{\geq 0}}$, find a feasible path $\sigma^{\ast}$ such that ${c\hspace{0pt}{(\sigma^{\ast})}} = {\min{\{{{c\hspace{0pt}{(\sigma)}}:{\sigma\hspace{0pt}\text{~is feasible}}}\}}}$. If no such path exists, report failure.

### 2.2 Random Geometric Graphs 

The objective of this section is to summarize some of the results on random geometric graphs that are available in the literature, and are relevant to the analysis of sampling-based path planning algorithms. In the remainder of this article, several connections are made between the theory of random geometric graphs and path-planning algorithms in robotics, providing insight on a number of issues, including, e.g., probabilistic completeness and asymptotic optimality, as well as technical tools to analyze the algorithms and establish their properties. In fact, it turns out that the data structures constructed by most sampling-based motion planning algorithms in the literature coincide, in the absence of obstacles, with standard models of random geometric graphs.

Random geometric graphs are in general defined as stochastic collections of points in a metric space, connected pairwise by edges if certain conditions (e.g., on the distance between the points) are satisfied. Such objects have been studied since their introduction by Gilbert (1961); see, e.g., Penrose (2003) and  Balister et al. (2009a) for an overview of recent results. From the theoretical point of view, the study of random geometric graphs makes a connection between random graphs (Bollobás, 2001) and percolation theory (Bollobás and Riordan, 2006). On the application side, in recent years, random geometric graphs have attracted significant attention as models of ad hoc wireless networks (Gupta and Kumar, 1998, 2000).

Much of the literature on random geometric graphs deals with infinite graphs defined on unbounded domains, with vertices generated as a homogeneous Poisson point process. Recall that a Poisson random variable of parameter $\lambda \in {\mathbb{R}}_{> 0}$ is an integer-valued random variable ${{Poisson}\hspace{0pt}{(\lambda)}}:{\Omega\rightarrow{\mathbb{N}}_{0}}$ such that ${{\mathbb{P}}\hspace{0pt}{({{{Poisson}\hspace{0pt}{(\lambda)}} = k})}} = {{e^{- \lambda}\hspace{0pt}\lambda^{k}}/{k!}}$. A homogeneous Poisson point process of intensity $\lambda$ on ${\mathbb{R}}^{d}$ is a random countable set of points $\mathcal{P}_{\lambda}^{d} \subset {\mathbb{R}}^{d}$ such that, for any disjoint measurable sets ${\mathcal{S}_{1},\mathcal{S}_{2}} \subset {\mathbb{R}}^{d}$, ${\mathcal{S}_{1} \cap \mathcal{S}_{2}} = \varnothing$, the numbers of points of $\mathcal{P}_{\lambda}^{d}$ in each set are independent Poisson variables, i.e., ${{card}\left( {\mathcal{P}_{\lambda}^{d} \cap \mathcal{S}_{1}} \right)} = {{Poisson}\hspace{0pt}{({\mu\hspace{0pt}{(\mathcal{S}_{1})}\hspace{0pt}\lambda})}}$ and ${{card}\left( {\mathcal{P}_{\lambda}^{d} \cap \mathcal{S}_{2}} \right)} = {{Poisson}\hspace{0pt}{({\mu\hspace{0pt}{(\mathcal{S}_{2})}\hspace{0pt}\lambda})}}$. In particular, the intensity of a homogeneous Poisson point process can be interpreted as the expected number of points generated in the unit cube, i.e., ${{\mathbb{E}}\hspace{0pt}{({{card}\left( {\mathcal{P}_{\lambda}^{d} \cap {(0,1)}^{d}} \right)})}} = {{\mathbb{E}}\hspace{0pt}{({{Poisson}\hspace{0pt}{(\lambda)}})}} = \lambda$.

Perhaps the most studied model of infinite random geometric graph is the following, introduced in Gilbert (1961), and often called Gilbert's disc model, or Boolean model:

###### Definition 4 (Infinite random $r$-disc graph) 

Let ${\lambda,r} \in {\mathbb{R}}_{> 0}$, and $d \in {\mathbb{N}}$. An infinite random $r$-disc graph $G_{\infty}^{disc}\hspace{0pt}{(\lambda,r)}$ in $d$ dimensions is an infinite graph with vertices ${\{ X_{i}\}}_{i \in {\mathbb{N}}} = \mathcal{P}_{\lambda}^{d}$, and such that $(X_{i},X_{j})$, ${i,j} \in {\mathbb{N}}$, is an edge if and only if ${\|{X_{i} - X_{j}}\|} < r$.

A fundamental issue in infinite random graphs is whether the graph contains an infinite connected component, with non-zero probability. If it does, the random graph is said to percolate. Percolation is an important paradigm in statistical physics, with many applications in disparate fields such as material science, epidemiology, and microchip manufacturing, just to name a few (see, e.g., Sahimi, 1994).

Consider the infinite random $r$-disc graph, for $r = 1$, i.e., $G_{\infty}^{disc}\hspace{0pt}{(\lambda,1)}$, and assume, without loss of generality, that the origin is one of the vertices of this graph. Let $p_{k}\hspace{0pt}{(\lambda)}$ denote the probability that the connected component of $G_{\infty}^{disc}\hspace{0pt}{(\lambda,1)}$ containing the origin contains $k$ vertices, and define $p_{\infty}\hspace{0pt}{(\lambda)}$ as ${p_{\infty}\hspace{0pt}{(\lambda)}} = {1 - {\sum_{k = 1}^{\infty}{p_{k}\hspace{0pt}{(\lambda)}}}}$. The function $p_{\infty}:{\lambda\rightarrow{p_{\infty}\hspace{0pt}{(\lambda)}}}$ is monotone, and ${p_{\infty}\hspace{0pt}{(0)}} = 0$ and ${\lim_{\lambda\rightarrow\infty}{p_{\infty}\hspace{0pt}{(\lambda)}}} = 1$ (Penrose, 2003). A key result in percolation theory is that there exists a non-zero critical intensity $\lambda_{c}$ defined as $\lambda_{c}:={\sup{\{\lambda:{{p_{\infty}\hspace{0pt}{(\lambda)}} = 0}\}}}$. In other words, for all $\lambda > \lambda_{c}$, there is a non-zero probability that the origin is in an infinite connected component of $G_{\infty}^{disc}\hspace{0pt}{(\lambda,1)}$; moreover, under these conditions, the graph has precisely one infinite connected component, almost surely (Meester and Roy, 1996). The function $p_{\infty}$ is continuous for all $\lambda \neq \lambda_{c}$: in other words, the graph undergoes a phase transition at the critical density $\lambda_{c}$, often also called the continuum percolation threshold (Penrose, 2003). The exact value of $\lambda_{c}$ is not known; Meester and Roy provide $0.696 < \lambda_{c} < 3.372$ for $d = 2$ (Meester and Roy, 1996), and simulations suggest that $\lambda_{c} \approx 1.44$ (Quintanilla et al., 2000).

For many applications, including the ones in this article, models of finite graphs on a bounded domain are more relevant. Penrose introduced the following model (Penrose, 2003):

###### Definition 5 (Random $r$-disc graph) 

Let $r \in {\mathbb{R}}_{> 0}$, and ${n,d} \in {\mathbb{N}}$. A random $r$-disc graph $G^{disc}\hspace{0pt}{(n,r)}$ in $d$ dimensions is a graph whose $n$ vertices, $\{ X_{1},X_{2},\ldots,X_{n}\}$, are independent, uniformly distributed random variables in ${(0,1)}^{d}$, and such that $(X_{i},X_{j})$, ${i,j} \in {\{ 1,\ldots,n\}}$, $i \neq j$, is an edge if and only if ${\|{X_{i} - X_{j}}\|} < r$.

For finite random geometric graph models, one is typically interested in whether a random geometric graph possesses certain properties asymptotically as $n$ increases. Since the number of vertices is finite in random graphs, percolation can not be defined easily. In this case, percolation is studied in terms of the scaling of the number of vertices in the largest connected component with respect to the total number of vertices; in particular, a finite random geometric graph is said to percolate if it contains a "giant" connected component containing at least a constant fraction of all the nodes. As in the infinite case, percolation in finite random geometric graphs is often a phase transition phenomenon. In the case of random $r$-disc graphs,

###### Theorem 6 (Percolation of random $r$-disc graphs (Penrose, 2003)) 

Let $G^{disc}\hspace{0pt}{(n,r)}$ be a random $r$-disc graph in $d \geq 2$ dimensions, and let $N_{\max}\hspace{0pt}{({G^{disc}\hspace{0pt}{(n,r)}})}$ be the number of vertices in its largest connected component. Then, almost surely,

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\lim\limits_{n\rightarrow\infty}\frac{N_{\max}\hspace{0pt}{({G^{disc}\hspace{0pt}{(n,r_{n})}})}}{n}} = 0},{{\text{~if~}\hspace{0pt}r_{n}} < \left( {\lambda_{c}/n} \right)^{1/d}}},$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

and

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\lim\limits_{n\rightarrow\infty}\frac{N_{\max}\hspace{0pt}{({G^{disc}\hspace{0pt}{(n,r)}})}}{n}} > 0},{{\text{~if~}\hspace{0pt}r_{n}} > \left( {\lambda_{c}/n} \right)^{1/d}}},$$   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

where $\lambda_{c}$ is the continuum percolation threshold.

A random $r$-disc graph with ${\lim_{n\rightarrow\infty}{n\hspace{0pt}r_{n}^{d}}} = \lambda \in {(0,\infty)}$ is said to operate in the thermodynamic limit. It is said to be in subcritical regime when $\lambda < \lambda_{c}$ and supercritical regime when $\lambda > \lambda_{c}$.

Another property of interest is connectivity. Clearly, connectivity implies percolation. Interestingly, emergence of connectivity in random geometric graphs is a phase transition phenomenon, as percolation. The following result is available in the literature:

###### Theorem 7 (Connectivity of random $r$-disc graphs (Penrose, 2003)) 

Let $G^{disc}\hspace{0pt}{(n,r)}$ be a random $r$-disc graph in $d$ dimensions. Then,

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${\lim\limits_{n\rightarrow\infty}{{\mathbb{P}}\hspace{0pt}\left( {\{{G^{disc}\hspace{0pt}{(n,r)}\hspace{0pt}\text{~is connected~}}\}} \right)}} = \left\{ \begin{array}{ll}   
     {1,} & {{{\text{~if~}\hspace{0pt}\zeta_{d}\hspace{0pt}r^{d}} > {{\log{(n)}}/n}},} \\                                                                                            
     {0,} & {{{\text{~if~}\hspace{0pt}\zeta_{d}\hspace{0pt}r^{d}} < {{\log{(n)}}/n}},}                                                                                               
     \end{array} \right.$$                                                                                                                                                           
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

where $\zeta_{d}$ is the volume of the unit ball in $d$ dimensions.

Another model of random geometric graphs considers edges between $k$ nearest neighbors. (Note that there are no ties, almost surely.) Both infinite and finite models are considered, as follows.

###### Definition 8 (Infinite random $k$-nearest neighbor graph) 

Let $\lambda \in {\mathbb{R}}_{> 0}$, and ${d,k} \in {\mathbb{N}}$. An infinite random $k$-nearest neighbor graph $G_{\infty}^{near}\hspace{0pt}{(\lambda,k)}$ in $d$ dimensions is an infinite graph with vertices ${\{ X_{i}\}}_{i \in {\mathbb{N}}} = \mathcal{P}_{\lambda}^{d}$, and such that $(X_{i},X_{j})$, ${i,j} \in {\mathbb{N}}$, is an edge if $X_{j}$ is among the $k$ nearest neighbors of $X_{i}$, or if $X_{i}$ is among the $k$ nearest neighbors of $X_{j}$.

###### Definition 9 (Random $k$-nearest neighbor graph) 

Let ${d,k,n} \in {\mathbb{N}}$. A random $k$-nearest neighbor graph $G^{near}\hspace{0pt}{(n,k)}$ in $d$ dimensions is a graph whose $n$ vertices, $\{ X_{1},X_{2},\ldots,X_{n}\}$, are independent, uniformly distributed random variables in ${(0,1)}^{d}$, and such that $(X_{i},X_{j})$, ${i,j} \in {\{ 1,\ldots,n\}}$, $i \neq j$, is an edge if $X_{j}$ is among the $k$ nearest neighbors of $X_{i}$, or if $X_{i}$ is among the $k$ nearest neighbors of $X_{j}$.

Percolation and connectivity for random $k$-nearest neighbor graphs exhibit phase transition phenomena, as in the random $r$-disc case. However, the results available in the literature are more limited. Results on percolation are only available for infinite graphs:

###### Theorem 10 (Percolation in infinite random $k$-nearest graphs (Balister et al., 2009a)) 

Let $G_{\infty}^{near}\hspace{0pt}{(\lambda,k)}$ be an infinite random $k$-nearest neighbor graph in $d \geq 2$ dimensions. Then, there exists a constant $k_{d}^{p} > 0$ such that

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     $${{\mathbb{P}}\hspace{0pt}\left( \left\{ {G_{\infty}^{near}\hspace{0pt}{(1,k)}\hspace{0pt}\text{~has an infinite component~}} \right\} \right)} = \left\{ \begin{array}{ll}   
     {1,} & {{{\text{~if~}\hspace{0pt}k} \geq k_{d}^{p}},} \\                                                                                                                       
     {0,} & {{{\text{~if~}\hspace{0pt}k} < k_{d}^{p}}.}                                                                                                                             
     \end{array} \right.$$                                                                                                                                                          
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

The value of $k_{d}^{p}$ is not known. However, it is believed that $k_{2}^{p} = 3$, and $k_{d}^{p} = 2$ for all $d \geq 3$ (Balister et al., 2009a). It is known that percolation does not occur for $k = 1$ (Balister et al., 2009a).

Regarding connectivity of random $k$-nearest neighbor graphs, the only available results in the literature are not stated in terms of a given number of vertices: rather, the results are stated in terms of the restriction of a homogeneous Poisson point process to the unit cube. In other words, the vertices of the graph are obtained as ${\{ X_{1},X_{2},\ldots\}} = {\mathcal{P}_{\lambda}^{d} \cap {(0,1)}^{d}}$. This is equivalent to setting the number of vertices as a Poisson random variable of parameter $n$, and then sampling the ${Poisson}\hspace{0pt}{(n)}$ vertices independently and uniformly in ${(0,1)}^{d}$:

###### Lemma 11 (Stoyan et al. (1995)) 

Let ${\{ X_{i}\}}_{i \in {\mathbb{N}}}$ be a sequence of points drawn independently and uniformly from $\mathcal{S} \subseteq \mathcal{X}$. Let ${Poisson}\hspace{0pt}{(n)}$ be a Poisson random variable with parameter $n$. Then, $\{ X_{1},X_{2},\ldots,X_{{Poisson}\hspace{0pt}{(n)}}\}$ is the restriction to $\mathcal{S}$ of a homogeneous Poisson point process with intensity ${n/\mu}\hspace{0pt}{(\mathcal{S})}$.

The main advantage in using such a model to generate the vertices of a random geometric graph is independence: in the Poisson case, the numbers of points in any two disjoint measurable regions ${\mathcal{S}_{1},\mathcal{S}_{2}} \subset {\lbrack 0,1\rbrack}^{d}$, ${\mathcal{S}_{1} \cap \mathcal{S}_{2}} = \varnothing$, are independent Poisson random variables, with mean $\mu\hspace{0pt}{(\mathcal{S}_{1})}\hspace{0pt}\lambda$ and $\mu\hspace{0pt}{(\mathcal{S}_{2})}\hspace{0pt}\lambda$, respectively. These two random variables would not be independent if the total number of vertices were fixed a priori (also called a binomial point process). With some abuse of notation, such a random geometric graph model will be indicated as $G^{near}\hspace{0pt}{({{Poisson}\hspace{0pt}{(n)}},k)}$.

###### Theorem 12 (Connectivity of random $k$-nearest graphs (Balister et al., 2009b; Xue and Kumar, 2004)) 

Let $G^{near}\hspace{0pt}{({{Poisson}\hspace{0pt}{(n)}},k)}$ indicate a $k$-nearest neighbor graph model in $d = 2$ dimensions, such that its vertices are generated using a Poisson point process of intensity $n$. Then, there exists a constant $k_{2}^{c} > 0$ such that

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${\lim\limits_{n\rightarrow\infty}{{\mathbb{P}}\hspace{0pt}\left( \left\{ {G^{near}\hspace{0pt}{({{Poisson}\hspace{0pt}{(n)}},{\lfloor{k\hspace{0pt}{\log{(n)}}}\rfloor})}\hspace{0pt}\text{~is connected~}} \right\} \right)}} = \left\{ \begin{array}{ll}   
     {1,} & {{{\text{~if~}\hspace{0pt}k} \geq k_{2}^{c}},} \\                                                                                                                                                                                                       
     {0,} & {{{\text{~if~}\hspace{0pt}k} < k_{2}^{c}}.}                                                                                                                                                                                                             
     \end{array} \right.$$                                                                                                                                                                                                                                          
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

The value of $k_{2}^{c}$ is not known; the current best estimate is $0.3043 \leq k_{2}^{c} \leq 0.5139$ (Balister et al., 2005).

Finally, the last model of random geometric graph that will be relevant for the analysis of the algorithms in this paper is the following:

###### Definition 13 (Online nearest neighbor graph) 

Let ${d,n} \in {\mathbb{N}}$. An online nearest neighbor graph $G^{ONN}\hspace{0pt}{(n)}$ in $d$ dimensions is a graph whose $n$ vertices, $(X_{1},X_{2},\ldots,X_{n})$, are independent, uniformly distributed random variables in ${(0,1)}^{d}$, and such that $(X_{i},X_{j})$, ${i,j} \in {\{ 1,\ldots,n\}}$, $j > 1$, is an edge if and only if ${\|{X_{i} - X_{j}}\|} = {\min_{1 \leq k < j}{\|{X_{k} - X_{j}}\|}}$.

Clearly, the online nearest neighbor graph is connected by construction, and trivially percolates. Recent results for this random geometric graph model include estimates of the total power-weighted edge length and an analysis of the vertex degree distribution, see, e.g., Wade (2009).

## 3 Algorithms 

In this section, a number of sampling-based motion planning algorithms are introduced. First, some common primitive procedures are defined. Then, the PRM and the RRT algorithms are outlined, as they are representative of the major paradigms for sampling-based motion planning algorithms in the literature. Then, new algorithms, namely PRM^∗^ and RRT^∗^, are introduced, as asymptotically optimal and computationally efficient versions of their "standard" counterparts.

### 3.1 Primitive Procedures 

Before discussing the algorithms, it is convenient to introduce the primitive procedures that they rely on.

##### Sampling: 

Let ${\mathtt{S}\mathtt{a}\mathtt{m}\mathtt{p}\mathtt{l}\mathtt{e}}:{\omega\mapsto{\{{{\mathtt{S}\mathtt{a}\mathtt{m}\mathtt{p}\mathtt{l}\mathtt{e}}_{i}\hspace{0pt}{(\omega)}}\}}_{i \in {\mathbb{N}}_{0}} \subset \mathcal{X}}$ be a map from $\Omega$ to sequences of points in $\mathcal{X}$, such that the random variables ${\mathtt{S}\mathtt{a}\mathtt{m}\mathtt{p}\mathtt{l}\mathtt{e}}_{i}$, $i \in {\mathbb{N}}_{0}$, are independent and identically distributed (i.i.d.). For simplicity, the samples are assumed to be drawn from a uniform distribution, even though results extend naturally to any absolutely continuous distribution with density bounded away from zero on $\mathcal{X}$. It is convenient to consider another map, ${\mathtt{S}\mathtt{a}\mathtt{m}\mathtt{p}\mathtt{l}\mathtt{e}\mathtt{F}\mathtt{r}\mathtt{e}\mathtt{e}}:{\omega\mapsto{\{{{\mathtt{S}\mathtt{a}\mathtt{m}\mathtt{p}\mathtt{l}\mathtt{e}\mathtt{F}\mathtt{r}\mathtt{e}\mathtt{e}}_{i}\hspace{0pt}{(\omega)}}\}}_{i \in {\mathbb{N}}_{0}} \subset \mathcal{X}_{free}}$ that returns sequences of i.i.d. samples from $\mathcal{X}_{free}$. For each $\omega \in \Omega$, the sequence ${\{{{\mathtt{S}\mathtt{a}\mathtt{m}\mathtt{p}\mathtt{l}\mathtt{e}\mathtt{F}\mathtt{r}\mathtt{e}\mathtt{e}}_{i}\hspace{0pt}{(\omega)}}\}}_{i \in {\mathbb{N}}_{0}}$ is the subsequence of ${\{{{\mathtt{S}\mathtt{a}\mathtt{m}\mathtt{p}\mathtt{l}\mathtt{e}}_{i}\hspace{0pt}{(\omega)}}\}}_{i \in {\mathbb{N}}_{0}}$ containing only the samples in $\mathcal{X}_{free}$, i.e., ${\{{{\mathtt{S}\mathtt{a}\mathtt{m}\mathtt{p}\mathtt{l}\mathtt{e}\mathtt{F}\mathtt{r}\mathtt{e}\mathtt{e}}_{i}\hspace{0pt}{(\omega)}}\}}_{i \in {\mathbb{N}}_{0}} = {{\{{{\mathtt{S}\mathtt{a}\mathtt{m}\mathtt{p}\mathtt{l}\mathtt{e}}_{i}\hspace{0pt}{(\omega)}}\}}_{i \in {\mathbb{N}}_{0}} \cap \mathcal{X}_{free}}$.

##### Nearest Neighbor: 

Given a graph $G = {(V,E)}$, where $V \subset \mathcal{X}$, a point $x \in \mathcal{X}$ , the function ${\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}}:{{(G,x)}\mapsto v \in V}$ returns the vertex in $V$ that is "closest" to $x$ in terms of a given distance function. In this paper, the Euclidean distance is used (see, e.g., LaValle and Kuffner (2001) for alternative choices), and hence

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}}\hspace{0pt}{({G = {{(V,E)},x}})}}:={{argmin}_{v \in V}\hspace{0pt}{\|{x - v}\|}}}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

A set-valued version of this function is also considered, ${\mathtt{k}\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}}:{{(G,x,k)}\mapsto{\{ v_{1},v_{2},\ldots,v_{k}\}}}$, returning the $k$ vertices in $V$ that are nearest to $x$, according to the same distance function as above. (By convention, if the cardinality of $V$ is less than $k$, then the function returns $V$.)

##### Near Vertices: 

Given a graph $G = {(V,E)}$, where $V \subset \mathcal{X}$, a point $x \in \mathcal{X}$, and a positive real number $r \in {\mathbb{R}}_{> 0}$, the function ${\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}}:{{(G,x,r)}\mapsto V^{\prime} \subseteq V}$ returns the vertices in $V$ that are contained in a ball of radius $r$ centered at $x$, i.e.,

  -- ---------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}}\hspace{0pt}{({G = {{(V,E)},x,r}})}}:=\left\{ {v \in V}:{v \in \mathcal{B}_{x,r}} \right\}}.$$   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------- --

##### Steering: 

Given two points ${x,y} \in \mathcal{X}$, the function ${\mathtt{S}\mathtt{t}\mathtt{e}\mathtt{e}\mathtt{r}}:{{(x,y)}\mapsto z}$ returns a point $z \in \mathcal{X}$ such that $z$ is "closer" to $y$ than $x$ is. Throughout the paper, the point $z$ returned by the function $\mathtt{S}\mathtt{t}\mathtt{e}\mathtt{e}\mathtt{r}$ will be such that $z$ minimizes $\|{z - y}\|$ while at the same time maintaining ${\|{z - x}\|} \leq \eta$, for a prespecified $\eta > 0$,^11^1This steering procedure is used widely in the robotics literature, since its introduction in Kuffner and LaValle (2000). Our results also extend to the Rapidly-exploring Random Dense Trees (see, e.g., LaValle, 2006), which are slightly modified versions of the RRTs that do not require tuning any prespecified parameters such as $\eta$ in this case. i.e.,

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathtt{S}\mathtt{t}\mathtt{e}\mathtt{e}\mathtt{r}}\hspace{0pt}{(x,y)}}:={{argmin}_{z \in \mathcal{B}_{x,\eta}}\hspace{0pt}{\|{z - y}\|}}}.$$   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------- --

##### Collision Test: 

Given two points ${x,x^{\prime}} \in \mathcal{X}$, the Boolean function ${\mathtt{C}\mathtt{o}\mathtt{l}\mathtt{l}\mathtt{i}\mathtt{s}\mathtt{i}\mathtt{o}\mathtt{n}\mathtt{F}\mathtt{r}\mathtt{e}\mathtt{e}}\hspace{0pt}{(x,x^{\prime})}$ returns $\mathtt{T}\mathtt{r}\mathtt{u}\mathtt{e}$ if the line segment between $x$ and $x^{\prime}$ lies in $\mathcal{X}_{free}$, i.e., ${\lbrack x,x^{\prime}\rbrack} \subset \mathcal{X}_{free}$, and $\mathtt{F}\mathtt{a}\mathtt{l}\mathtt{s}\mathtt{e}$ otherwise.

### 3.2 Existing Algorithms 

Next, some of the sampling-based algorithms available in the literature are outlined. For convenience, inputs and outputs of the algorithms are not shown explicitly, but are as follows. All algorithms take as input a path planning problem $(\mathcal{X}_{free},x_{init},\mathcal{X}_{goal})$, an integer $n \in {\mathbb{N}}$, and a cost function $c:{\Sigma\rightarrow{\mathbb{R}}_{\geq 0}}$, if appropriate. These inputs are shared with functions and procedures called within the algorithms. All algorithms return a graph $G = {(V,E)}$, where $V \subset \mathcal{X}_{free}$, ${{card}(V)} \leq {n + 1}$, and $E \in {V \times V}$. The solution of the path planning problem can be easily computed from such a graph, e.g., using standard shortest-path algorithms.

##### Probabilistic RoadMaps (PRM): 

The Probabilistic RoadMaps algorithm is primarily aimed at multi-query applications. In its basic version, it consists of a pre-processing phase, in which a roadmap is constructed by attempting connections among $n$ randomly-sampled points in $\mathcal{X}_{free}$, and a query phase, in which paths connecting initial and final conditions through the roadmap are sought. "Expansion" heuristics for enhancing the roadmap's connectivity are available in the literature (Kavraki et al., 1996) but have no impact on the analysis in this paper, and will not be discussed.

The pre-processing phase, outlined in Algorithm 1: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning"), begins with an empty graph. At each iteration, a point $x_{rand} \in \mathcal{X}_{free}$ is sampled, and added to the vertex set $V$. Then, connections are attempted between $x_{rand}$ and other vertices in $V$ within a ball of radius $r$ centered at $x_{rand}$, in order of increasing distance from $x_{rand}$, using a simple local planner (e.g., straight-line connection). Successful (i.e., collision-free) connections result in the addition of a new edge to the edge set $E$. To avoid unnecessary computations (since the focus of the algorithm is establishing connectivity), connections between $x_{rand}$ and vertices in the same connected component are avoided. Hence, the roadmap constructed by PRM is a forest, i.e., a collection of trees.

1V ← ⌀; E ← ⌀;
2 for i = 0, …, n do
3       xrand ← SampleFreei;
4       U ← Near (G=(V,E), xrand, r) ;
5       V ← V ∪ {xrand};
6       foreach u ∈ U, in order of increasing ∥u − xrand∥, do
7             if xrand and u are not in the same connected component of G = (V,E) then
8                  if CollisionFree (xrand,u) then E ← E ∪ {(xrand,u), (u,xrand)};
9                  
10 return G = (V,E);
Algorithm 1 PRM (preprocessing phase)

Analysis results in the literature are only available for a "simplified" version of the PRM algorithm (Kavraki et al., 1998), referred to as sPRM in this paper. The simplified algorithm initializes the vertex set with the initial condition, samples $n$ points from $\mathcal{X}_{free}$, and then attempts to connect points within a distance $r$, i.e., using a similar logic as PRM, with the difference that connections between vertices in the same connected component are allowed. Notice that in the absence of obstacles, i.e., if $\mathcal{X}_{free} = \mathcal{X}$, the roadmap constructed in this way is a random $r$-disc graph.

1V ← {xinit} ∪ {SampleFreei}i = 1, …, n; E ← ⌀;
2 foreach v ∈ V do
3       U ← Near (G=(V,E), v, r) ∖ {v};
4       foreach u ∈ U do
5             if CollisionFree (v,u) then E ← E ∪ {(v,u), (u,v)}
6 return G = (V,E);
Algorithm 2 sPRM

Practical implementation of the (s)PRM algorithm have often considered different choices for the set $U$ of vertices to which connections are attempted (i.e., line 1: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning") in Algorithm 1: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning"), and line 2: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning") in Algorithm 2: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning")). In particular, the following criteria are of particular interest:

-   [•]

    $k$-Nearest (s)PRM: Choose the nearest $k$ neighbors to the vertex under consideration, for a given $k$ (a typical value is reported as $k = 15$ (LaValle, 2006)). In other words, $U\leftarrow{{\mathtt{k}\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}}\hspace{0pt}{({G = {{(V,E)},x_{rand},k}})}}$ in line 1: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning") of Algorithm 1: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning") and $U\leftarrow{{{\mathtt{k}\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}}\hspace{0pt}{({G = {{(V,E)},v,k}})}} \smallsetminus {\{ v\}}}$ in line 2: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning") of Algorithm 2: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning"). The roadmap constructed in this way in an obstacle-free environment is a random $k$-nearest graph.

-   [•]

    Bounded-degree (s)PRM: For any fixed $r$, the average number of connections attempted at each iteration is proportional to the number of vertices in $V$, and can result in an excessive computational burden for large $n$. To address this, an upper bound $k$ can be imposed on the cardinality of the set $U$ (a typical value is reported as $k = 20$ (LaValle, 2006)). In other words, $U\leftarrow{{{\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}}\hspace{0pt}{(G,x_{rand},r)}} \cap {{\mathtt{k}\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}}\hspace{0pt}{(G,x_{rand},k)}}}$ in line 1: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning") of Algorithm 1: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning"), and $U\leftarrow{{({{{\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}}\hspace{0pt}{(G,v,r)}} \cap {{\mathtt{k}\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}}\hspace{0pt}{(G,v,k)}}})} \smallsetminus {\{ v\}}}$ in line 2: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning") of Algorithm 2: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning").

-   [•]

    Variable-radius (s)PRM: Another option to maintain the degree of the vertices in the roadmap small is to make the connection radius $r$ a function of $n$, as opposed to a fixed parameter. However, there are no clear indications in the literature on the appropriate functional relationship between $r$ and $n$.

##### Rapidly-exploring Random Trees (RRT): 

The Rapidly-exploring Random Tree algorithm is primarily aimed at single-query applications. In its basic version, the algorithm incrementally builds a tree of feasible trajectories, rooted at the initial condition. An outline of the algorithm is given in Algorithm 3: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning"). The algorithm is initialized with a graph that includes the initial state as its single vertex, and no edges. At each iteration, a point $x_{rand} \in \mathcal{X}_{free}$ is sampled. An attempt is made to connect the nearest vertex $v \in V$ in the tree to the new sample. If such a connection is successful, $x_{rand}$ is added to the vertex set, and $(v,x_{rand})$ is added to the edge set. In the original version of this algorithm, the iteration is stopped as soon as the tree contains a node in the goal region. In this paper, for consistency with the other algorithms (e.g., PRM), the iteration is performed $n$ times. In the absence of obstacles, i.e., if $\mathcal{X}_{free} = \mathcal{X}$, the tree constructed in this way is an online nearest neighbor graph.

1V ← {xinit}; E ← ⌀;
2 for i = 1, …, n do
3       xrand ← SampleFreei;
4       xnearest ← Nearest (G=(V,E), xrand);
5       xnew ← Steer (xnearest,xrand) ;
6       if ObtacleFree (xnearest,xnew) then
7             V ← V ∪ {xnew}; E ← E ∪ {(xnearest,xnew)} ;
8            
9 return G = (V,E);
10
Algorithm 3 RRT

A variant of RRT consists of growing two trees, respectively rooted at the initial state, and at a state in the goal set. To highlight the fact that the sampling procedure must not necessarily be stochastic, the algorithm is also referred to as Rapidly-exploring Dense Trees (RDT) (LaValle, 2006).

### 3.3 Proposed algorithms 

In this section, the new algorithms considered in this paper are presented. These algorithms are proposed as asymptotically optimal and computationally efficient versions of their "standard" counterparts, as will be made clear through the analysis in the next section. Input and output data are the same as in the algorithms introduced in Section 3.2.

##### Optimal Probabilistic RoadMaps (PRM^∗^): 

In the standard PRM algorithm, as well as in its simplified "batch" version considered in this paper, connections are attempted between roadmap vertices that are within a fixed radius $r$ from one another. The constant $r$ is thus a parameter of PRM. The proposed algorithm---shown in Algorithm 4: ‣ 3.3 Proposed algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning")---is similar to sPRM, with the only difference being that the connection radius $r$ is chosen as a function of $n$, i.e., $r = {r\hspace{0pt}{(n)}}:={\gamma_{PRM}\hspace{0pt}{({{\log{(n)}}/n})}^{1/d}}$, where $\gamma_{PRM} > \gamma_{PRM}^{\ast} = {2\hspace{0pt}{({1 + {1/d}})}^{1/d}\hspace{0pt}\left( {{\mu\hspace{0pt}{(\mathcal{X}_{free})}}/\zeta_{d}} \right)^{1/d}}$, $d$ is the dimension of the space $\mathcal{X}$, $\mu\hspace{0pt}{(\mathcal{X}_{free})}$ denotes the Lebesgue measure (i.e., volume) of the obstacle-free space, and $\zeta_{d}$ is the volume of the unit ball in the $d$-dimensional Euclidean space. Clearly, the connection radius decreases with the number of samples. The rate of decay is such that the average number of connections attempted from a roadmap vertex is proportional to $\log{(n)}$.

Note that in the discussion of variable-radius PRM in LaValle (2006), it is suggested that the radius be chosen as a function of sample dispersion. (Recall that the dispersion of a point set contained in a bounded set $\mathcal{S} \subset {\mathbb{R}}^{d}$ is the radius of the largest empty ball centered in $\mathcal{S}$.) Indeed, the dispersion of a set of $n$ random points sampled uniformly and independently in a bounded set is $O\hspace{0pt}{({({{\log{(n)}}/n})}^{1/d})}$ (Niederreiter, 1992), which is precisely the rate at which the connection radius is scaled in the PRM^∗^ algorithm.

1V ← {xinit} ∪ {SampleFreei}i = 1, …, n; E ← ⌀;
2 foreach v ∈ V do
3       U ← Near (G=(V,E), v, γPRM (log (n)/n)1/d) ∖ {v};
4       foreach u ∈ U do
5             if CollisionFree (v,u) then E ← E ∪ {(v,u), (u,v)}
6 return G = (V,E);
Algorithm 4 PRM∗

Another version of the algorithm, called $k$-nearest PRM^∗^, can be considered, motivated by the $k$-nearest PRM implementation previously mentioned, whereby the number $k$ of nearest neighbors to be considered is not a constant, but is chosen as a function of the cardinality of the roadmap $n$. More precisely, ${k\hspace{0pt}{(n)}}:={k_{PRM}\hspace{0pt}{\log{(n)}}}$, where $k_{PRM} > k_{PRM}^{\ast} = {e\hspace{0pt}{({1 + {1/d}})}}$, and $U\leftarrow{{{\mathtt{k}\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}}\hspace{0pt}{({G = {{(V,E)},v,{k_{PRM}\hspace{0pt}{\log{(n)}}}}})}} \smallsetminus {\{ v\}}}$ in line 4: ‣ 3.3 Proposed algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning") of Algorithm 4: ‣ 3.3 Proposed algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning").

Note that $k_{PRM}^{\ast}$ is a constant that only depends on $d$, and does not otherwise depend on the problem instance, unlike $\gamma_{PRM}^{\ast}$. Moreover, $k_{PRM} = {2\hspace{0pt}e}$ is a valid choice for all problem instances.

##### Rapidly-exploring Random Graph (RRG): 

The Rapidly-exploring Random Graph algorithm was introduced as an incremental (as opposed to batch) algorithm to build a connected roadmap, possibly containing cycles. The RRG algorithm is similar to RRT in that it first attempts to connect the nearest node to the new sample. If the connection attempt is successful, the new node is added to the vertex set. However, RRG has the following difference. Every time a new point $x_{new}$ is added to the vertex set $V$, then connections are attempted from all other vertices in $V$ that are within a ball of radius ${r\hspace{0pt}{({{card}(V)})}} = {\min{\{{\gamma_{RRG}\hspace{0pt}{({{\log{({{card}(V)})}}/{{card}(V)}})}^{1/d}},\eta\}}}$, where $\eta$ is the constant appearing in the definition of the local steering function, and $\gamma_{RRG} > \gamma_{RRG}^{\ast} = {2\hspace{0pt}{({1 + {1/d}})}^{1/d}\hspace{0pt}\left( {{\mu\hspace{0pt}{(\mathcal{X}_{free})}}/\zeta_{d}} \right)^{1/d}}$. For each successful connection, a new edge is added to the edge set $E$. Hence, it is clear that, for the same sampling sequence, the RRT graph (a directed tree) is a subgraph of the RRG graph (an undirected graph, possibly containing cycles). In particular, the two graphs share the same vertex set, and the edge set of the RRT graph is a subset of that of the RRG graph.

1V ← {xinit}; E ← ⌀;
2 for i = 1, …, n do
3       xrand ← SampleFreei;
4       xnearest ← Nearest (G=(V,E), xrand);
5       xnew ← Steer (xnearest,xrand) ;
6       if ObtacleFree (xnearest,xnew) then
7             Xnear ← Near (G=(V,E), xnew, min {γRRG (log (card(V))/card(V))1/d, η}) ;
8             V ← V ∪ {xnew}; E ← E ∪ {(xnearest,xnew), (xnew,xnearest)} ;
9             foreach xnear ∈ Xnear do
10                   if CollisionFree (xnear,xnew) then E ← E ∪ {(xnear,xnew), (xnew,xnear)}
11            
12 return G = (V,E);
13
Algorithm 5 RRG

Another version of the algorithm, called $k$-nearest RRG, can be considered, in which connections are sought to $k$ nearest neighbors, with $k = {k\hspace{0pt}{({{card}(V)})}}:={k_{RRG}\hspace{0pt}{\log{({{card}(V)})}}}$, where $k_{RRG} > k_{RRG}^{\ast} = {e\hspace{0pt}{({1 + {1/d}})}}$, and $X_{near}\leftarrow{{\mathtt{k}\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}}\hspace{0pt}{({G = {{(V,E)},x_{new},{k_{RRG}\hspace{0pt}{\log{({{card}(V)})}}}}})}}$, in line 5: ‣ 3.3 Proposed algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning") of Algorithm 5: ‣ 3.3 Proposed algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning").

Note that $k_{RRG}^{\ast}$ is a constant that depends only on $d$, and does not depend otherwise on the problem instance, unlike $\gamma_{RRG}^{\ast}$. Moreover, $k_{RRG} = {2\hspace{0pt}e}$ is a valid choice for all problem instances.

##### Optimal RRT (RRT^∗^): 

Maintaining a tree structure rather than a graph is not only economical in terms of memory requirements, but may also be advantageous in some applications, due to, for instance, relatively easy extensions to motion planning problems with differential constraints, or to cope with modeling errors. The RRT^∗^ algorithm is obtained by modifying RRG in such a way that formation of cycles is avoided, by removing "redundant" edges, i.e., edges that are not part of a shortest path from the root of the tree (i.e., the initial state) to a vertex. Since the RRT and RRT^∗^ graphs are directed trees with the same root and vertex set, and edge sets that are subsets of that of RRG, this amounts to a "rewiring" of the RRT tree, ensuring that vertices are reached through a minimum-cost path.

Before discussing the algorithm, it is necessary to introduce a few new functions. Given two points ${x_{1},x_{2}} \in {\mathbb{R}}^{d}$, let ${{\mathtt{L}\mathtt{i}\mathtt{n}\mathtt{e}}\hspace{0pt}{(x_{1},x_{2})}}:{{\lbrack 0,s\rbrack}\rightarrow\mathcal{X}}$ denote the straight-line path from $x_{1}$ to $x_{2}$. Given a tree $G = {(V,E)}$, let ${\mathtt{P}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{n}\mathtt{t}}:{V\rightarrow V}$ be a function that maps a vertex $v \in V$ to the unique vertex $u \in V$ such that ${(u,v)} \in E$. By convention, if $v_{0} \in V$ is the root vertex of $G$, ${{\mathtt{P}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{n}\mathtt{t}}\hspace{0pt}{(v_{0})}} = v_{0}$. Finally, let ${\mathtt{C}\mathtt{o}\mathtt{s}\mathtt{t}}:{V\rightarrow{\mathbb{R}}_{\geq 0}}$ be a function that maps a vertex $v \in V$ to the cost of the unique path from the root of the tree to $v$. For simplicity, in stating the algorithm we will assume an additive cost function, so that ${{\mathtt{C}\mathtt{o}\mathtt{s}\mathtt{t}}\hspace{0pt}{(v)}} = {{{\mathtt{C}\mathtt{o}\mathtt{s}\mathtt{t}}\hspace{0pt}{({{\mathtt{P}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{n}\mathtt{t}}\hspace{0pt}{(v)}})}} + {c\hspace{0pt}{({{\mathtt{L}\mathtt{i}\mathtt{n}\mathtt{e}}\hspace{0pt}{({{\mathtt{P}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{n}\mathtt{t}}\hspace{0pt}{(v)}},v)}})}}}$, although this is not necessary for the analysis in the next section. By convention, if $v_{0} \in V$ is the root vertex of $G$, then ${{\mathtt{C}\mathtt{o}\mathtt{s}\mathtt{t}}\hspace{0pt}{(v_{0})}} = 0$.

1V ← {xinit}; E ← ⌀;
2 for i = 1, …, n do
3       xrand ← SampleFreei;
4       xnearest ← Nearest (G=(V,E), xrand);
5       xnew ← Steer (xnearest,xrand) ;
6       if ObtacleFree (xnearest,xnew) then
7             Xnear ← Near (G=(V,E), xnew, min {γRRT* (log (card(V))/card(V))1/d, η}) ;
8             V ← V ∪ {xnew};
9             xmin ← xnearest; cmin ← Cost (xnearest) + c (Line (xnearest,xnew));
10             foreach xnear ∈ Xnear do // Connect along a minimum-cost path
11                   if CollisionFree (xnear,xnew) ∧ Cost (xnear) + c (Line (xnear,xnew)) &lt; cmin then
12                         xmin ← xnear; cmin ← Cost (xnear) + c (Line (xnear,xnew))
13                  
14             E ← E ∪ {(xmin,xnew)};
15             foreach xnear ∈ Xnear do // Rewire the tree
16                   if CollisionFree (xnew,xnear) ∧ Cost (xnew) + c (Line (xnew,xnear)) &lt; Cost (xnear) then xparent ← Parent (xnear);
17                   E ← (E∖{(xparent,xnear)}) ∪ {(xnew,xnear)}
18            
19 return G = (V,E);
Algorithm 6 RRT∗

The RRT^∗^ algorithm, shown in Algorithm 6: ‣ 3.3 Proposed algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning"), adds points to the vertex set $V$ in the same way as RRT and RRG. It also considers connections from the new vertex $x_{new}$ to vertices in $X_{near}$, i.e., other vertices that are within distance ${r\hspace{0pt}{({{card}(V)})}} = {\min{\{{\gamma_{{RRT}^{\ast}}\hspace{0pt}{({{\log{({{card}(V)})}}/{{card}(V)}})}^{1/d}},\eta\}}}$ from $x_{new}$. However, not all feasible connections result in new edges being inserted in the edge set $E$. In particular, (i) an edge is created from the vertex in $X_{near}$ that can be connected to $x_{new}$ along a path with minimum cost, and (ii) new edges are created from $x_{new}$ to vertices in $X_{near}$, if the path through $x_{new}$ has lower cost than the path through the current parent; in this case, the edge linking the vertex to its current parent is deleted, to maintain the tree structure.

Another version of the algorithm, called $k$-nearest RRT^∗^, can be considered, in which connections are sought to $k$ nearest neighbors, with ${k\hspace{0pt}{({{card}(V)})}} = {k_{RRG}\hspace{0pt}{\log{({{card}(V)})}}}$, and $X_{near}\leftarrow{{\mathtt{k}\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}}\hspace{0pt}{({G = {{(V,E)},x_{new},{k_{RRG}\hspace{0pt}{\log{(i)}}}}})}}$, in line 6: ‣ 3.3 Proposed algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning") of Algorithm 6: ‣ 3.3 Proposed algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning").

## 4 Analysis 

In this section, a number of results concerning the probabilistic completeness, asymptotic optimality, and complexity of the algorithms in Section 3 are presented.

The return value of Algorithms 1: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning")-6: ‣ 3.3 Proposed algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning") is a graph. Since the sampling procedure $\mathtt{S}\mathtt{a}\mathtt{m}\mathtt{p}\mathtt{l}\mathtt{e}\mathtt{F}\mathtt{r}\mathtt{e}\mathtt{e}$ is stochastic, the returned graph is in fact a random variable.^22^2We will not address the case in which the sampling procedure is deterministic, but refer the reader to LaValle et al. (2004), which contains an in-depth discussion of the relative merits of randomness and determinism in sampling-based motion planning algorithms. Since the sampling procedure is modeled as a map from the sample space $\Omega$ to infinite sequences in $\mathcal{X}$, sets of vertices and edges of the graphs maintained by the algorithms can be defined as functions from the sample space $\Omega$ to appropriate sets. More precisely, let $ALG$ be a label indicating one of the algorithms in Section 3, and let ${\{{V_{i}^{ALG}\hspace{0pt}{(\omega)}}\}}_{i \in {\mathbb{N}}}$ and ${\{{E_{i}^{ALG}\hspace{0pt}{(\omega)}}\}}_{i \in {\mathbb{N}}}$ be, respectively, the sets of vertices and edges in the graph returned by algorithm $ALG$, indexed by the number of samples, for a particular realization of the sample sequence. (In other words, these are sequences of functions defined from $\Omega$ into finite subsets of $\mathcal{X}_{free}$ or $\mathcal{X}_{free} \times \mathcal{X}_{free}$.) Similarly, let $G_{i}^{ALG} = {(V_{i}^{ALG},E_{i}^{ALG})}$. (The label $ALG$ will be at times omitted when the algorithm being used is clear from the context.)

All algorithms considered in the paper are sound, in the sense that they only return graphs with vertices and edges representing points and paths in $\mathcal{X}_{free}$.This statement can be easily verified by inspection of the algorithms in Section 3.

### 4.1 Probabilistic Completeness 

In this section, the feasibility problem is considered, and the (probabilistic) completeness properties of the algorithms in Section 3 are analyzed. First, some preliminary definitions are given, followed by a definition of probabilistic completeness. Then, completeness properties of various sampling-based motion planning algorithms are stated.

Let $\delta > 0$ be a real number. A state $x \in \mathcal{X}_{free}$ is said to be a $\delta$-interior state of $\mathcal{X}_{free}$, if the closed ball of radius $\delta$ centered at $x$ lies entirely inside $\mathcal{X}_{free}$. The $\delta$-interior of $\mathcal{X}_{free}$, denoted as ${int}_{\delta}\hspace{0pt}{(\mathcal{X}_{free})}$, is defined as the collection of all $\delta$-interior states, i.e., ${{int}_{\delta}\hspace{0pt}{(\mathcal{X}_{free})}}:=\left. \{{x \in \mathcal{X}_{free}} \middle| {\mathcal{B}_{x,\delta} \subseteq \mathcal{X}_{free}}\} \right.$. In other words, the $\delta$-interior of $\mathcal{X}_{free}$ is the set of all states that are at least a distance $\delta$ away from any point in the obstacle set (see Figure 1). A collision-free path $\sigma:{{\lbrack 0,1\rbrack}\rightarrow\mathcal{X}_{free}}$ is said to have strong $\delta$-clearance, if $\sigma$ lies entirely inside the $\delta$-interior of $\mathcal{X}_{free}$, i.e., ${\sigma\hspace{0pt}{(\tau)}} \in {{int}_{\delta}\hspace{0pt}{(\mathcal{X}_{free})}}$ for all $\tau \in {\lbrack 0,1\rbrack}$. A path planning problem $(\mathcal{X}_{free},x_{init},\mathcal{X}_{goal})$ is said to be robustly feasible if there exists a path with strong $\delta$-clearance, for some $\delta > 0$, that solves it. In terms of the notation used in this paper, the notion of probabilistic completeness can be stated as follows.

###### Definition 14 (Probabilistic Completeness) 

An algorithm ALG is probabilistically complete, if, for any robustly feasible path planning problem $(\mathcal{X}_{free},x_{init},\mathcal{X}_{goal})$,

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\operatorname{lim\ inf}\limits_{n\rightarrow\infty}{{\mathbb{P}}\hspace{0pt}\left( {\{{{\exists x_{goal}} \in {V_{n}^{ALG} \cap {\mathcal{X}_{goal}\hspace{0pt}\text{~such that~}\hspace{0pt}x_{init}\hspace{0pt}\text{~is connected to~}\hspace{0pt}x_{goal}\hspace{0pt}\text{~in~}\hspace{0pt}G_{n}^{ALG}}}}\}} \right)}} = 1}.$$   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

If an algorithm is probabilistically complete, and the path planning problem is robustly feasible, the limit

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     $$\lim_{n\rightarrow\infty}{{\mathbb{P}}\hspace{0pt}\left( {\{{{\exists x_{goal}} \in {V_{n}^{ALG} \cap {\mathcal{X}_{goal}\hspace{0pt}\text{~such that~}\hspace{0pt}x_{init}\hspace{0pt}\text{~is connected to~}\hspace{0pt}x_{goal}\hspace{0pt}\text{~in~}\hspace{0pt}G_{n}^{ALG}}}}\}} \right)}$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

exists and is equal to 1. On the other hand, the same limit is equal to zero for any sampling-based algorithm (including probabilistically complete ones) if the problem is not robustly feasible, unless the samples are drawn from a singular distribution adapted to the problem.

Figure 1: An illustration of the δ-interior of 𝒳free. The obstacle region 𝒳obs is shown in dark grey and the δ-interior of 𝒳free is shown in light grey. The distance between the dashed boundary of intδ (𝒳free) and the solid boundary of 𝒳free is precisely δ.

It is known from the literature that the sPRM and RRT algorithms are probabilistically complete, and that the probability of finding a solution if one exists approaches one exponentially fast with the number of vertices in the graph returned by the algorithms. In other words,

###### Theorem 15 (Probabilistic completeness of sPRM (Kavraki et al., 1998)) 

Consider a robustly feasible path planning problem $(\mathcal{X}_{free},x_{init},\mathcal{X}_{goal})$. There exist constants $a > 0$ and $n_{0} \in {\mathbb{N}}$, dependent only on $\mathcal{X}_{free}$ and $\mathcal{X}_{goal}$, such that

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{{\mathbb{P}}\hspace{0pt}\left( \left\{ {{\exists x_{goal}} \in {V_{n}^{sPRM} \cap \mathcal{X}_{goal}}}:{x_{goal}\hspace{0pt}\text{~is connected to~}\hspace{0pt}x_{init}\hspace{0pt}\text{~in~}\hspace{0pt}G_{n}^{sPRM}} \right\} \right)} > {1 - e^{- {a\hspace{0pt}n}}}},{{\forall n} > n_{0}}}.$$   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

###### Theorem 16 (Probabilistic Completeness of RRT (LaValle and Kuffner, 2001)) 

Consider a robustly feasible path planning problem $(\mathcal{X}_{free}$, $x_{init},\mathcal{X}_{goal})$. There exist constants $a > 0$ and $n_{0} \in {\mathbb{N}}$, both dependent only on $\mathcal{X}_{free}$ and $\mathcal{X}_{goal}$, such that

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{{\mathbb{P}}\hspace{0pt}\left( \left\{ {{V_{n}^{RRT} \cap \mathcal{X}_{goal}} \neq \varnothing} \right\} \right)} > {1 - e^{- {a\hspace{0pt}n}}}},{{\forall n} > n_{0}}}.$$   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

On the other hand, the probabilistic completeness results do not necessarily extend to the heuristics used in practical implementations of the (s)PRM algorithm, as detailed in Section 3. For example, consider the $k$-nearest sPRM algorithm, where $k = 1$. That is, each vertex is connected to its nearest neighbor and the resulting undirected graph is returned as the output. This sPRM algorithm will be called the 1-nearest sPRM, and indicated with the label $1\hspace{0pt}P\hspace{0pt}R\hspace{0pt}M$. The RRT algorithm can be thought of as the incremental version of the 1-nearest sPRM algorithm: the RRT algorithm also connects each sample to its nearest neighbor, but forces connectivity of the graph by an incremental construction. The following theorem shows that the 1-nearest sPRM algorithm is not probabilistically complete, although the RRT is (see Theorem 16) ‣ 4.1 Probabilistic Completeness ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning")). Furthermore, the probability that it fails to find a path converges to one as the number of samples approaches infinity.

###### Theorem 17 (Incompleteness of $k$-nearest sPRM for $k = 1$) 

The $k$-nearest sPRM algorithm is not probabilistically complete for $k = 1$. Furthermore,

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\lim\limits_{n\rightarrow\infty}{{\mathbb{P}}\hspace{0pt}\left( {\{{{\exists x_{goal}} \in {V_{n}^{1\hspace{0pt}P\hspace{0pt}R\hspace{0pt}M} \cap {\mathcal{X}_{goal}\hspace{0pt}\text{~such that~}\hspace{0pt}x_{init}\hspace{0pt}\text{~is connected to~}\hspace{0pt}x_{goal}\hspace{0pt}\text{~in~}\hspace{0pt}G_{n}^{ALG}}}}\}} \right)}} = 0}.$$   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

The proof of this theorem requires two intermediate results that are provided below. For simplicity of presentation, consider the case when $\mathcal{X}_{free} = \mathcal{X}$. Let $G_{n}^{1\hspace{0pt}P\hspace{0pt}R\hspace{0pt}M} = {(V_{n}^{1\hspace{0pt}P\hspace{0pt}R\hspace{0pt}M},E_{n}^{1\hspace{0pt}P\hspace{0pt}R\hspace{0pt}M})}$ denote the graph returned by the 1-nearest sPRM algorithm, when the algorithm is run with $n$ samples. Let $L_{n}$ denote the total length of all the edges present in $G_{n}^{1\hspace{0pt}P\hspace{0pt}R\hspace{0pt}M}$. Recall that $\zeta_{d}$ denotes the volume of the unit ball in the $d$-dimensional Euclidean space. Let $\zeta_{d}^{\prime}$ denote the volume of the union of two unit balls whose centers are a unit distance apart.

###### Lemma 18 (Total length of the 1-nearest neighbor graph (Wade, 2007)) 

For all $d \geq 2$, $L_{n}/n^{1 - {1/d}}$ converges to a constant in mean square, i.e.,

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\lim\limits_{n\rightarrow\infty}{{\mathbb{E}}\hspace{0pt}\left\lbrack \left( {\frac{L_{n}}{n^{1 - {1/d}}} - {\left( {1 + \frac{1}{d}} \right)\hspace{0pt}\left( {\frac{1}{\zeta_{d}} - \frac{\zeta_{d}}{2\hspace{0pt}{(\zeta_{d}^{\prime})}^{1 + {1/d}}}} \right)}} \right)^{2} \right\rbrack}} = 0}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

###### Proof. 

This lemma is a direct consequence of Theorem 3 of Wade (2007). ∎∎

Let $N_{n}$ denote the number of connected components of $G_{n}^{1\hspace{0pt}P\hspace{0pt}R\hspace{0pt}M}$.

###### Lemma 19 (Number of connected components of the 1-nearest neighbor graph) 

For all $d \geq 2$, $N_{n}/n$ converges to a constant in mean square, i.e.,

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\lim\limits_{n\rightarrow\infty}{{\mathbb{E}}\hspace{0pt}\left\lbrack \left( {\frac{N_{n}}{n} - \frac{\zeta_{d}}{2\hspace{0pt}\zeta_{d}^{\prime}}} \right)^{2} \right\rbrack}} = 0}.$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

###### Proof. 

A reciprocal pair is a pair of vertices each of which is the other one's nearest neighbor. In a graph formed by connecting each vertex to its nearest neighbor, any connected component includes exactly one reciprocal pair whenever the number of vertices is greater than 2 (see, e.g., Eppstein et al., 1997). The number of reciprocal pairs in such a graph was shown to converge to $\zeta_{d}/{({2\hspace{0pt}\zeta_{d}^{\prime}})}$ in mean square in Henze (1987) (see also Remark 2 in Wade (2007)). ∎∎

###### Proof of Theorem 17 ‣ 4.1 Probabilistic Completeness ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning"). 

Let ${\overset{\sim}{L}}_{n}$ denote the average length of a connected component in $G_{n}^{1\hspace{0pt}P\hspace{0pt}R\hspace{0pt}M}$, i.e., ${\overset{\sim}{L}}_{n} = {L_{n}/N_{n}}$. Let $L_{n}^{\prime}$ denote the length of the connected component that includes $x_{init}$. Since the samples are drawn independently and uniformly, the random variables ${\overset{\sim}{L}}_{n}$ and $L_{n}^{\prime}$ have the same distribution (although they are clearly dependent). Let $\gamma_{L}$ denote the constant that $L_{n}/n^{1 - {1/d}}$ converges to (see Lemma 18) ‣ 4.1 Probabilistic Completeness ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning")). Similarly, let $\gamma_{N}$ denote the constant that $N_{n}/n$ converges to (see Lemma 19 ‣ 4.1 Probabilistic Completeness ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning")).

Recall that convergence in mean square implies convergence in probability and hence convergence in distribution (Grimmett and Stirzaker, 2001). Since both $L_{n}/n^{1 - {1/d}}$ and $N_{n}/n$ converge in mean square to constants and ${{\mathbb{P}}\hspace{0pt}{({\{{N_{n} = 0}\}})}} = 0$ for all $n \in {\mathbb{N}}$, by Slutsky's theorem (Resnick, 1999), ${n^{1/d}\hspace{0pt}{\overset{\sim}{L}}_{n}} = \frac{L_{n}/n^{1 - {1/d}}}{N_{n}/n}$ converges to $\gamma:={\gamma_{L}/\gamma_{N}}$ in distribution. In this case, it also converges in probability, since $\gamma$ is a constant (Grimmett and Stirzaker, 2001). Then, $n^{1/d}\hspace{0pt}L_{n}^{\prime}$ also converges to $\gamma$ in probability, since ${\overset{\sim}{L}}_{n}$ and $L_{n}^{\prime}$ are identically distributed for all $n \in {\mathbb{N}}$. Thus, $L_{n}^{\prime}$ converges to $0$ in probability, i.e., ${\lim_{n\rightarrow\infty}{{\mathbb{P}}\hspace{0pt}\left( \left\{ {L_{n}^{\prime} > \epsilon} \right\} \right)}} = 0$, for all $\epsilon > 0$.

Let $\epsilon > 0$ be such that $\epsilon < {\inf_{x \in \mathcal{X}_{goal}}{\|{x - x_{init}}\|}}$. Let $A_{n}$ denote the event that the graph returned by the 1-nearest sPRM algorithm contains a feasible path, i.e., one that starts from $x_{init}$ and reaches the goal region Clearly, the event $\{{L_{n}^{\prime} > \epsilon}\}$ occurs whenever $A_{n}$ does, i.e., $A_{n} \subseteq {\{{L_{n}^{\prime} > \epsilon}\}}$. Then, ${{\mathbb{P}}\hspace{0pt}{(A_{n})}} \leq {{\mathbb{P}}\hspace{0pt}{({\{{L_{n}^{\prime} > \epsilon}\}})}}$. Taking the limit superior of both sides

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\operatorname{lim\ inf}\limits_{n\rightarrow\infty}{{\mathbb{P}}\hspace{0pt}{(A_{n})}}} \leq {\operatorname{lim\ sup}\limits_{n\rightarrow\infty}{{\mathbb{P}}\hspace{0pt}{(A_{n})}}} \leq {\operatorname{lim\ sup}\limits_{n\rightarrow\infty}{{\mathbb{P}}\hspace{0pt}{({\{{L_{n}^{\prime} > \epsilon}\}})}}} = \,\, 0}.$$   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

In other words, the limit $\lim_{n\rightarrow\infty}{{\mathbb{P}}\hspace{0pt}{(A_{n})}}$ exists and is equal zero. ∎∎

Consider the variable-radius sPRM algorithm. The following theorem asserts that variable-radius sPRM algorithm is not probabilistically complete in the subcritical regime.

###### Theorem 20 (Incompleteness of variable-radius sPRM with ${r\hspace{0pt}{(n)}} = {\gamma\hspace{0pt}n^{- {1/d}}}$) 

There exists a constant $\gamma > 0$ such that the variable radius sPRM with connection radius ${r\hspace{0pt}{(n)}} = {\gamma\hspace{0pt}n^{- {1/d}}}$ is not probabilistically complete.

The proof of this result requires some intermediate results from random geometric graph theory. Recall that $\lambda_{c}$ is the critical density, or continuum percolation threshold (see Section 2.2). Given a Borel set $\Gamma \subseteq {\mathbb{R}}^{d}$, let $G_{\Gamma}^{disc}\hspace{0pt}{(n,r)}$ denote the random $r$-disc graph formed with vertices independent and uniformly sampled from $\Gamma$ and edges connecting two vertices, $v$ and $v^{\prime}$, whenever ${\|{v - v^{\prime}}\|} < r_{n}$.

###### Lemma 21 (Penrose (2003)) 

Let $\lambda \in {(0,\lambda_{c})}$ and $\Gamma \subset {\mathbb{R}}^{d}$ be a Borel set. Consider a sequence ${\{ r_{n}\}}_{n \in {\mathbb{N}}}$ that satisfies ${n\hspace{0pt}r_{n}^{d}} \leq \lambda$, ${\forall n} \in {\mathbb{N}}$. Let $N_{\max}\hspace{0pt}{({G_{\Gamma}^{disc}\hspace{0pt}{(n,r_{n})}})}$ denote the size of the largest component in $G_{\Gamma}^{disc}\hspace{0pt}{(n,r_{n})}$. Then, there exist constants ${a,b} > 0$ and $m_{0} \in {\mathbb{N}}$ such that for all $m \geq m_{0}$,

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( \left\{ {{N_{\max}\hspace{0pt}{({G_{\Gamma}^{disc}\hspace{0pt}{(n,r_{n})}})}} \geq m} \right\} \right)} \leq {n\hspace{0pt}\left( {e^{- {a\hspace{0pt}m}} + e^{- {b\hspace{0pt}n}}} \right)}}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

###### Proof of Theorem 20=𝛾⁢𝑛^{-1/𝑑}) ‣ 4.1 Probabilistic Completeness ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning"). 

Let $\epsilon > 0$ such that $\epsilon < {\inf_{x \in X_{goal}}{\|{x - x_{init}}\|}}$ and that the $2\hspace{0pt}\epsilon$-ball centered at $x_{init}$ lies entirely within the obstacle-free space. Let $G_{n}^{PRM} = {(V_{n}^{PRM},E_{n}^{PRM})}$ denote the graph returned by this variable radius sPRM algorithm, when the algorithm is run with $n$ samples. Let $G_{n} = {(V_{n},E_{n})}$ denote the the restriction of $G_{n}^{PRM}$ to the $2\hspace{0pt}\epsilon$-ball centered at $x_{init}$ defined as $V_{n} = {V_{n}^{PRM} \cap \mathcal{B}_{x_{init},{2\hspace{0pt}\epsilon}}}$ and $E_{n} = {{({V_{n} \times V_{n}})} \cap E_{n}^{PRM}}$.

Clearly, $G_{n}$ is equivalent to the random $r$-disc graph on $\Gamma = \mathcal{B}_{x_{init},{2\hspace{0pt}\epsilon}}$. Let $N_{\max}\hspace{0pt}{(G_{n})}$ denote the number of vertices in the largest connected component of $G_{n}$. By Lemma 21) ‣ 4.1 Probabilistic Completeness ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning"), there exists constants ${a,b} > 0$ and $m_{0} \in {\mathbb{N}}$ such that

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}{({\{{{N_{\max}\hspace{0pt}{(G_{n})}} \geq m}\}})}} \leq {n\hspace{0pt}\left( {e^{- {a\hspace{0pt}m}} + e^{- {b\hspace{0pt}n}}} \right)}},$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

for all $m \geq m_{0}$. Then, for all $m = {\lambda^{- {1/d}}\hspace{0pt}{({\epsilon/2})}\hspace{0pt}n^{1/d}} > m_{0}$,

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( \left\{ {{N_{\max}\hspace{0pt}{(G_{n})}} \geq {\lambda^{- {1/d}}\hspace{0pt}\frac{\epsilon}{2}\hspace{0pt}n^{1/d}}} \right\} \right)} \leq {n\hspace{0pt}\left( {e^{- {a\hspace{0pt}\lambda^{- {1/d}}\hspace{0pt}{({\epsilon/2})}\hspace{0pt}n^{1/d}}} + e^{- {b\hspace{0pt}n}}} \right)}}.$$   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Let $L_{n}$ denote the total length of all the edges in the connected component that includes $x_{init}$. Since $r_{n} = {\lambda^{1/d}\hspace{0pt}n^{- {1/d}}}$,

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     $${{{\mathbb{P}}\hspace{0pt}\left( \left\{ {L_{n} \geq \frac{\epsilon}{2}} \right\} \right)} \leq {n\hspace{0pt}\left( {e^{- {a\hspace{0pt}\lambda^{- {1/d}}\hspace{0pt}{({\epsilon/2})}\hspace{0pt}n^{1/d}}} + e^{- {b\hspace{0pt}n}}} \right)}}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

Since the right hand side is summable, by the Borel-Cantelli lemma the event $\left\{ {L_{n} \geq {\epsilon/2}} \right\}$ occurs infinitely often with probability zero, i.e., ${{\mathbb{P}}\hspace{0pt}{({\operatorname{lim\ sup}_{n\rightarrow\infty}{\{{L_{n} \geq {\epsilon/2}}\}}})}} = 0$.

Given a graph $G = {(V,E)}$ define the diameter of this graph as the distance between the farthest pair of vertices in $V$, i.e., $\max_{{v,v^{\prime}} \in V}{\|{v - v^{\prime}}\|}$. Let $D_{n}$ denote the diameter of the largest component in $G_{n}$. Clearly, $D_{n} \leq L_{n}$ holds surely. Thus, ${{\mathbb{P}}\hspace{0pt}\left( {\operatorname{lim\ sup}_{n\rightarrow\infty}\left\{ {D_{n} \geq {\epsilon/2}} \right\}} \right)} = 0$.

Let $I \in {\mathbb{N}}$ be the smallest number that satisfies $r_{I} \leq {\epsilon/2}$. Notice that the edges connected to the vertices $V_{n}^{PRM} \cap \mathcal{B}_{x_{init},\epsilon}$ coincide with those connected to $V_{n} \cap \mathcal{B}_{x_{init},\epsilon}$, for all $n \geq I$. Let $R_{n}$ denote distance of the farthest vertex $v \in V_{n}^{PRM}$ to $x_{init}$ in the component that contains $x_{init}$ in $G_{n}^{PRM}$. Notice also that $R_{n} \geq \epsilon$ only if $D_{n} \geq {\epsilon/2}$, for all $n \geq I$. That is, for all $n \geq I$, $\left\{ {R_{n} \geq \epsilon} \right\} \subseteq \left\{ {D_{n} \geq {\epsilon/2}} \right\}$, which implies ${{\mathbb{P}}\hspace{0pt}\left( {\operatorname{lim\ sup}_{n\rightarrow\infty}\left\{ {R_{n} \geq \epsilon} \right\}} \right)} = 0$.

Let $A_{n}$ denote the event that the graph returned by this variable radius sPRM algorithm includes a path that reaches the goal region. Clearly, $\{{R_{n} \geq \epsilon}\}$ holds, whenever $A_{n}$ holds. Hence, ${{\mathbb{P}}\hspace{0pt}{(A_{n})}} \leq {{\mathbb{P}}\hspace{0pt}{({\{{R_{n} \geq \epsilon}\}})}}$. Taking the limit superior of both sides yields

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\operatorname{lim\ inf}\limits_{n\rightarrow\infty}{{\mathbb{P}}\hspace{0pt}{(A_{n})}}} \leq {\operatorname{lim\ sup}\limits_{n\rightarrow\infty}{{\mathbb{P}}\hspace{0pt}{(A_{n})}}} \leq {\operatorname{lim\ sup}\limits_{n\rightarrow\infty}{{\mathbb{P}}\hspace{0pt}\left( \left\{ {R_{n} \geq \epsilon} \right\} \right)}} \leq {{\mathbb{P}}\hspace{0pt}\left( {\operatorname{lim\ sup}\limits_{n\rightarrow\infty}\left\{ {R_{n} \geq \epsilon} \right\}} \right)} = 0}.$$   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Hence, ${\lim_{n\rightarrow\infty}{{\mathbb{P}}\hspace{0pt}{(A_{n})}}} = 0$. ∎∎

Finally, the probabilistic completeness of the new algorithms proposed in Section 3 is established. Probabilistic completeness of PRM^∗^ is implied by its asymptotic optimality, proved in Section 4.2.

###### Theorem 22 (Completeness of PRM^∗^) 

The PRM^∗^ algorithm is probabilistically complete.

Probabilistic completeness of RRG and RRT^∗^ is a straightforward consequence of the probabilistic completeness of RRT:

###### Theorem 23 (Probabilistic completeness of RRG and RRT^∗^) 

The RRG and RRT^∗^ algorithms are probabilistically complete. Furthermore, for any robustly feasible path planning problem $(\mathcal{X}_{free},x_{init},\mathcal{X}_{goal})$, there exist constants $a > 0$ and $n_{0} \in {\mathbb{N}}$, both dependent only on $\mathcal{X}_{free}$ and $\mathcal{X}_{goal}$, such that

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{{\mathbb{P}}\hspace{0pt}\left( \left\{ {{V_{n}^{RRG} \cap \mathcal{X}_{goal}} \neq \varnothing} \right\} \right)} > {1 - e^{- {a\hspace{0pt}n}}}},{{\forall n} > n_{0}}},$$   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

and

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{{\mathbb{P}}\hspace{0pt}\left( \left\{ {{V_{n}^{{RRT}^{\ast}} \cap \mathcal{X}_{goal}} \neq \varnothing} \right\} \right)} > {1 - e^{- {a\hspace{0pt}n}}}},{{\forall n} > n_{0}}}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

###### Proof. 

By construction, ${V_{n}^{RRG}\hspace{0pt}{(\omega)}} = {V_{n}^{{RRT}^{\ast}}\hspace{0pt}{(\omega)}} = {V_{n}^{RRT}\hspace{0pt}{(\omega)}}$, for all $\omega \in \Omega$ and $n \in {\mathbb{N}}$. Moreover, the RRG and RRT^∗^ algorithms return connected graphs. Hence the result follows directly from the probabilistic completeness of RRT. ∎∎

In particular, note that if the RRT algorithm returns a feasible solution by iteration $n$, so will the RRG and RRT^∗^ algorithms, assuming the same sample sequence.

### 4.2 Asymptotic Optimality 

In this section, the optimality problem of path planning is considered. The algorithms presented in Section 3 are analyzed, in terms of their ability to return solutions whose cost converge to the global optimum. First, a definition of asymptotic optimality is provided as almost-sure convergence to optimal paths. Second, it is shown that the RRT algorithm lacks the asymptotic optimality property. Third, the PRM^∗^, RRG, and RRT^∗^ algorithms, as well as their $k$-nearest implementations, are shown to be asymptotically optimal.

Recall from Section 4.1 that an algorithm is probabilistically complete if the algorithm finds with high probability a solution to path planning problems that are robustly feasible, i.e., for which feasible path exists with strong $\delta$-clearance. A similar approach is used to define asymptotic optimality, relying on a notion of weak $\delta$-clearance and on a continuity property for the cost of paths, which will be introduced below.

Let ${\sigma_{1},\sigma_{2}} \in \Sigma_{free}$ be two collision-free paths with the same end points. A path $\sigma_{1}$ is said to be homotopic to $\sigma_{2}$, if there exists a continuous function $\psi:{{\lbrack 0,1\rbrack}\rightarrow\Sigma_{free}}$, called the homotopy, such that ${\psi\hspace{0pt}{(0)}} = \sigma_{1}$, ${\psi\hspace{0pt}{(1)}} = \sigma_{2}$, and $\psi\hspace{0pt}{(\tau)}$ is a collision-free path in for all $\tau \in {\lbrack 0,1\rbrack}$. Intuitively, a path that is homotopic to $\sigma$ can be continuously transformed to $\sigma$ through $\mathcal{X}_{free}$  (see Munkres, 2000). A collision-free path $\sigma:{{\lbrack 0,s\rbrack}\rightarrow\mathcal{X}_{free}}$ is said to have weak $\delta$-clearance, if there exists a path $\sigma^{\prime}$ that has strong $\delta$-clearance and there exist a homotopy $\psi$, with ${\psi\hspace{0pt}{(0)}} = \sigma$, ${\psi\hspace{0pt}{(1)}} = \sigma^{\prime}$, and for all $\alpha \in {(0,1\rbrack}$ there exists $\delta_{\alpha} > 0$ such that $\psi\hspace{0pt}{(\alpha)}$ has strong $\delta_{\alpha}$-clearance. See Figure 2 for an illustration of the weak $\delta$-clearance property. A path that violates the weak $\delta$-clearance property is shown in Figure 3. Weak $\delta$-clearance does not require points along a path to be at least a distance $\delta$ away from the obstacles (see Figure 4). In fact, a collision-free path with uncountably many points lying on the boundary of an obstacle can still have weak $\delta$-clearance.

Figure 2: An illustration of a path σ with weak δ-clearance. The path σ′ that lies inside intδ (𝒳free) and is in the same homotopy class as σ is also shown in the figure. Note that σ does not have strong δ-clearance.

Figure 3: An illustration of an example path σ that does not have weak δ-clearance. For any positive value of δ, there is no path in intδ (𝒳free) that is in the same homotopy class as σ.

  
Figure 4: An illustration of a path that has weak δ-clearance. The path passes through a point where two spheres representing the obstacle region are in contact. Clearly, the path does not have strong δ-clearance.

Next, the set of all paths with bounded length is introduced as a normed space, which allows taking the limit of a sequence of paths. Recall that $\Sigma$ is the set of all paths, and $T\hspace{0pt}V\hspace{0pt}{( \cdot )}$ denotes the total variation, i.e., the length, of a path (see Section 2.1). Given ${\sigma_{1},\sigma_{2}} \in \Sigma$ with $\sigma_{1}:{{\lbrack 0,1\rbrack}\rightarrow\mathcal{X}}$ and $\sigma_{2}:{{\lbrack 0,1\rbrack}\rightarrow\mathcal{X}}$, the addition operation is defined as ${{({\sigma_{1} + \sigma_{2}})}\hspace{0pt}{(\tau)}} = {{\sigma_{1}\hspace{0pt}{(\tau)}} + {\sigma_{2}\hspace{0pt}{(\tau)}}}$ for all $\tau \in {\lbrack 0,1\rbrack}$. The set of paths $\Sigma$ is closed under addition. Given a path $\sigma:{{\lbrack 0,1\rbrack}\rightarrow\mathcal{X}}$ and a scalar $\alpha \in {\mathbb{R}}$, the multiplication by a scalar operation is defined as ${{({\alpha\hspace{0pt}\sigma})}\hspace{0pt}{(\tau)}}:={\alpha\hspace{0pt}\sigma\hspace{0pt}{(\tau)}}$ for all $\tau \in {\lbrack 0,1\rbrack}$. With these addition and multiplication by a scalar operations, the function space $\Sigma$ is, in fact, a vector space. On the vector space $\Sigma$, define the norm ${\|\sigma\|}_{BV}:={{\int_{0}^{1}{{|{\sigma\hspace{0pt}{(\tau)}}|}\hspace{0pt}{d\tau}}} + {{TV}\hspace{0pt}{(\sigma)}}}$, and denote the function space $\Sigma$ endowed with the norm $\parallel \cdot \parallel_{BV}$ by ${BV}\hspace{0pt}{(\mathcal{X})}$. The norm $\parallel \cdot \parallel_{BV}$ induces the following distance function:

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{dist}\hspace{0pt}{(\sigma_{1},\sigma_{2})}} = {\|{\sigma_{1} - \sigma_{2}}\|}_{BV} = {{\int_{0}^{1}{\left\| {{({\sigma_{1} - \sigma_{2}})}\hspace{0pt}{(\tau)}} \right\|\hspace{0pt}{d\tau}}} + {{TV}\hspace{0pt}{({\sigma_{1} - \sigma_{2}})}}}$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

where $\parallel \cdot \parallel$ is the usual Euclidean norm. A sequence ${\{\sigma_{n}\}}_{n \in {\mathbb{N}}}$ of paths is said to converge to a path $\overline{\sigma}$, denoted as ${\lim_{n\rightarrow\infty}\sigma_{n}} = \overline{\sigma}$, if the norm of the difference between $\sigma_{n}$ and $\overline{\sigma}$ converges to zero, i.e., ${\lim_{n\rightarrow\infty}{\|{\sigma_{n} - \overline{\sigma}}\|}_{BV}} = 0$.

A feasible path $\sigma^{\ast} \in \mathcal{X}_{free}$ that solves the optimality problem (Problem 3 ‣ 2.1 Problem Formulation ‣ 2 Preliminary Material ‣ Sampling-based Algorithms for Optimal Motion Planning")) is said to be a robustly optimal solution if it has weak $\delta$-clearance and, for any sequence of collision-free paths ${\{\sigma_{n}\}}_{n \in {\mathbb{N}}}$, $\sigma_{n} \in \mathcal{X}_{free}$, ${\forall n} \in {\mathbb{N}}$, such that ${\lim_{n\rightarrow\infty}\sigma_{n}} = \sigma^{\ast}$, ${\lim_{n\rightarrow\infty}{c\hspace{0pt}{(\sigma_{n})}}} = {c\hspace{0pt}{(\sigma^{\ast})}}$. Clearly, a path planning problem that has a robustly optimal solution is necessarily robustly feasible. Let $c^{\ast} = {c\hspace{0pt}{(\sigma^{\ast})}}$ be the cost of an optimal path, and let $Y_{n}^{ALG}$ be the extended random variable corresponding to the cost of the minimum-cost solution included in the graph returned by $ALG$ at the end of iteration $n$.

###### Definition 24 (Asymptotic Optimality) 

An algorithm ALG is asymptotically optimal if, for any path planning problem $(\mathcal{X}_{free},x_{init},\mathcal{X}_{goal})$ and cost function $c:{\Sigma\rightarrow{\mathbb{R}}_{\geq 0}}$ that admit a robustly optimal solution with finite cost $c^{\ast}$,

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( \left\{ {{\operatorname{lim\ sup}\limits_{n\rightarrow\infty}Y_{n}^{ALG}} = c^{\ast}} \right\} \right)} = 1}.$$   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------- --

Note that, since $Y_{n}^{ALG} \geq c^{\ast}$, ${\forall n} \in {\mathbb{N}}$, asymptotic optimality of $ALG$ implies that the limit $\lim_{n\rightarrow\infty}Y_{n}^{ALG}$ exists, and is equal to $c^{\ast}$. Clearly, probabilistic completeness is necessary for asymptotic optimality. Moreover, the probability that a sampling-based algorithm converges to an optimal solution almost surely has probability either zero or one. That is, a sampling-based algorithm either converges to the optimal solution in almost all runs, or the convergence does not occur in almost all runs.

###### Lemma 25 

Given that ${\operatorname{lim\ sup}_{n\rightarrow\infty}Y_{n}^{ALG}} < \infty$, i.e., $ALG$ finds a feasible solution eventually, the probability that ${\operatorname{lim\ sup}_{n\rightarrow\infty}Y_{n}^{ALG}} = c^{\ast}$ is either zero or one.

###### Proof. 

Conditioning on the event $\{{{\operatorname{lim\ sup}_{n\rightarrow\infty}Y_{n}^{ALG}} < \infty}\}$ ensures that $Y_{n}^{ALG}$ is finite, thus a random variable, for all large $n$. Given a sequence ${\{ Y_{n}\}}_{n \in {\mathbb{N}}}$ of random variables, let $\mathcal{F}_{m}^{\prime}$ denote the $\sigma$-field generated by the sequence ${\{ Y_{n}\}}_{n = m}^{\infty}$ of random variables. The tail $\sigma$-field $\mathcal{T}$ is defined as $\mathcal{T} = {\bigcap_{n \in {\mathbb{N}}}\mathcal{F}_{n}^{\prime}}$. An event $A$ is said to be a tail event if $A \in \mathcal{T}$. Any tail event occurs with probability either zero or one by the Kolmogorov zero-one law (Resnick, 1999). Consider the sequence ${\{ Y_{n}^{ALG}\}}_{n \in {\mathbb{N}}}$ of random variables. Let $\mathcal{F}_{m}^{\prime}$ denote the $\sigma$-fields generated by ${\{ Y_{n}^{ALG}\}}_{n = m}^{\infty}$. Then, ${\left\{ {{\operatorname{lim\ sup}_{n\rightarrow\infty}Y_{n}^{ALG}} = c^{\ast}} \right\} = \left\{ {{\operatorname{lim\ sup}_{{n\rightarrow\infty},{n \geq m}}Y_{n}^{ALG}} = c^{\ast}} \right\} \in {\mathcal{F}_{m}^{\prime}\hspace{0pt}\text{~for all~}\hspace{0pt}n} \in {\mathbb{N}}}.$ Hence, $\left\{ {Y_{n}^{ALG} = c^{\ast}} \right\} \in {\bigcap_{n \in {\mathbb{N}}}\mathcal{F}_{m}^{\prime}}$ is a tail event. The result follows by the Kolmogorov zero-one law.∎∎

Among the first steps in assessing the asymptotic optimality properties of an algorithm $ALG$ is determining whether the limit $\lim_{n\rightarrow\infty}Y_{n}^{ALG}$ exists. It turns out that if the graphs returned by $ALG$ satisfy a monotonicity property, then the limit exists, and is in general a random variable, indicated with $Y_{\infty}^{ALG}$.

###### Lemma 26 

If ${G_{i}^{ALG}\hspace{0pt}{(\omega)}} \subseteq {G_{i + 1}^{ALG}\hspace{0pt}{(\omega)}}$, ${\forall\omega} \in \Omega$ and ${\forall i} \in {\mathbb{N}}$, then ${{\lim_{n\rightarrow\infty}{Y_{n}^{ALG}\hspace{0pt}{(\omega)}}} = {Y_{\infty}^{ALG}\hspace{0pt}{(\omega)}}}.$

###### Proof. 

Since ${G_{i}^{ALG}\hspace{0pt}{(\omega)}} \subseteq {G_{i + 1}^{ALG}\hspace{0pt}{(\omega)}}$, then ${Y_{i + 1}^{ALG}\hspace{0pt}{(\omega)}} \leq {Y_{i}^{ALG}\hspace{0pt}{(\omega)}}$, for all $\omega \in \Omega$. Since $Y_{i}^{ALG} \geq c^{\ast}$, then the sequence converges to some limiting value, dependent on $\omega$, i.e., $Y_{\infty}^{ALG}\hspace{0pt}{(\omega)}$.∎∎

Of the algorithms presented in Section 3, it is easy to check that PRM, sPRM, RRT, RRG, and RRT^∗^ satisfy the monotonicity property in Lemma 26. On the other hand, $k$-nearest sPRM and PRM^∗^ do not: in these cases, the random variable $Y_{i + 1}^{ALG}$ is not necessarily dominated by $Y_{i}^{ALG}$. This is evident in numerical experiments, e.g., see Figures 10 and 11 in Section 5.

In order to avoid trivial cases of asymptotic optimality, it is necessary to rule out problems in which optimal solutions can be computed after a finite number of samples. Let $\Sigma^{\ast}$ denote the set of all optimal paths, i.e., the set of all paths that solve the optimal planning problem (Problem 3 ‣ 2.1 Problem Formulation ‣ 2 Preliminary Material ‣ Sampling-based Algorithms for Optimal Motion Planning")), and $\mathcal{X}_{opt}$ denote the set of states that an optimal path in $\Sigma^{\ast}$ passes through, i.e.,

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${\mathcal{X}_{opt} = \left. \{{x \in X_{free}} \middle| {{{\exists\sigma^{\ast}} \in \Sigma^{\ast}},{\tau \in {{\lbrack 0,1\rbrack}\hspace{0pt}\text{~such that~}\hspace{0pt}x} = {\sigma^{\ast}\hspace{0pt}{(\tau)}}}}\} \right.}.$$   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

###### Assumption 27 (Zero-measure Optimal Paths) 

The set of all points traversed by an optimal trajectory has measure zero, i.e., ${\mu\hspace{0pt}\left( \mathcal{X}_{opt} \right)} = 0$.

Most cost functions and problem instances of interest satisfy this assumption, including, e.g., the Euclidean length of the path when the goal region is convex. This assumption does not imply that there is a single optimal path; indeed, there are problem instances with uncountably many optimal paths, for which Assumption 27 ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning") holds. (A simple example is the motion planning problem in three dimensional Euclidean space where a ball shaped obstacle is placed between the initial state and the goal region.) Assumption 27 ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning") implies that no sampling-based planning algorithm can find a solution to the optimality problem in a finite number of iterations.

###### Lemma 28 

If Assumption 27 ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning") holds, the probability that a sampling-based algorithm $ALG$ returns a graph containing an optimal path at a finite iteration $n \in {\mathbb{N}}$ is zero, i.e.,

  -- --------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( {\cup_{n \in {\mathbb{N}}}{\{{Y_{n}^{ALG} = c^{\ast}}\}}} \right)} = 0}.$$   
  -- --------------------------------------------------------------------------------------------------------------- --

###### Proof. 

Let $B_{n}$ denote the event that $ALG$ constructs a graph containing a path with cost exactly equal to $c^{\ast}$ at the end of iteration $i$, i.e., $B_{n} = {\{{Y_{n}^{ALG} = c^{\ast}}\}}$. Let $B$ denote the event that $ALG$ returns a graph containing a path that costs exactly $c^{\ast}$ at some finite iteration $i$. Then, $B$ can be written as $B = {\cup_{n \in {\mathbb{N}}}B_{n}}$. Since $B_{n} \subseteq B_{n + 1}$, by monotonocity of measures, ${\lim_{i\rightarrow\infty}{{\mathbb{P}}\hspace{0pt}{(B_{n})}}} = {{\mathbb{P}}\hspace{0pt}{(B)}}$. By Assumption 27 ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning") and the definition of the sampling procedure, ${{\mathbb{P}}\hspace{0pt}{(B_{n})}} = 0$ for all $n \in {\mathbb{N}}$, since the probability that the set $\bigcup_{i = 1}^{n}{\{{{\mathtt{S}\mathtt{a}\mathtt{m}\mathtt{p}\mathtt{l}\mathtt{e}\mathtt{F}\mathtt{r}\mathtt{e}\mathtt{e}}\hspace{0pt}{(i)}}\}}$ of points contains a point from a zero-measure set is zero. Hence, ${{\mathbb{P}}\hspace{0pt}{(B)}} = 0$. ∎∎

In the remainder of the paper, it will be tacitly assumed that Assumption 27 ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning"), and hence Lemma 28, hold.

#### 4.2.1 Existing algorithms 

The algorithms in Section 3.2 were originally introduced to efficiently solve the feasibility problem, relaxing the completeness requirement to probabilistic completeness. Nevertheless, it is of interest to establish whether these algorithms are asymptotically optimal in addition to being probabilistically complete. (The first two results in this section rely on results that will be proven in Section 4.2.2, i.e., the fact that the RRT algorithm is not asymptotically optimal, and the PRM^∗^ algorithm is asymptotically optimal)

First, consider the PRM algorithm and its variants. The PRM algorithm, in its original form, is not asymptotically optimal.

###### Theorem 29 (Non-optimality of PRM) 

The PRM algorithm is not asymptotically optimal.

###### Proof. 

The proof is based on a counterexample, establishing a form of equivalence between PRM and RRT, which in turn will be proven not to be asymptotically optimal in Theorem 33 ‣ Rapidly-exploring Random Trees ‣ 4.2.1 Existing algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning"). Consider a convex obstacle-free environment, e.g., $\mathcal{X}_{free} = \mathcal{X}$, and choose the connection radius for PRM and the steering parameter for RRT such that ${r,\eta} > {{diam}\hspace{0pt}{(\mathcal{X})}}$. At each iteration, exactly one vertex and one edge is added to the graph, since (i) all connection attempts using the local planner (e.g., straight line connections as considered in this paper) are collision-free, and (ii) at the end of each iteration, the graph is connected (i.e., it contains only one connected component). In particular, the graph returned by the PRM algorithm in this case is a tree, and the arborescence obtained by choosing as the root the first sample point, i.e., ${\mathtt{S}\mathtt{a}\mathtt{m}\mathtt{p}\mathtt{l}\mathtt{e}\mathtt{F}\mathtt{r}\mathtt{e}\mathtt{e}}_{0}$, is an online nearest-neighbor graph (see Section 2.2) coinciding with the graph returned by RRT with the random initial condition $x_{init} = {\mathtt{S}\mathtt{a}\mathtt{m}\mathtt{p}\mathtt{l}\mathtt{e}\mathtt{F}\mathtt{r}\mathtt{e}\mathtt{e}}_{0}$.

Recall that the PRM algorithm is applicable for multiple-query planning problems: in other words, the graph returned by the PRM algorithm is used to solve path planning problems from arbitrary $x_{init} \in \mathcal{X}_{free}$ and $\mathcal{X}_{goal} \subset \mathcal{X}_{free}$. (Note that all such problems admit robust optimal solutions.) In particular, for $x_{init} = {\mathtt{S}\mathtt{a}\mathtt{m}\mathtt{p}\mathtt{l}\mathtt{e}\mathtt{F}\mathtt{r}\mathtt{e}\mathtt{e}}_{0}$, and any $X_{goal}$, then ${Y_{n}^{PRM}\hspace{0pt}{(\omega)}} = {Y_{n}^{RRT}\hspace{0pt}{(\omega)}}$, for all $\omega \in \Omega$, $n \in {\mathbb{N}}$. In particular, since both PRM and RRT satisfy the monotonicity condition in Lemma 26, Theorem 33 ‣ Rapidly-exploring Random Trees ‣ 4.2.1 Existing algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning") implies that

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( \left\{ {{\operatorname{lim\ sup}\limits_{n\rightarrow\infty}Y_{n}^{PRM}} = c^{\ast}} \right\} \right)} = {{\mathbb{P}}\hspace{0pt}\left( \left\{ {{\lim\limits_{n\rightarrow\infty}Y_{n}^{PRM}} = c^{\ast}} \right\} \right)} = {{\mathbb{P}}\hspace{0pt}\left( \left\{ {{\lim\limits_{n\rightarrow\infty}Y_{n}^{RRT}} = c^{\ast}} \right\} \right)} = 0}.$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

∎∎

The lack of asymptotic optimality of PRM is due to its incremental construction, coupled with the constraint eliminating edges making unnecessary connections within a connected component. Such a constraint is not present in the batch construction of the sPRM algorithm, which is indeed asymptotically optimal (at the expense of computational complexity, see Section 4.3).

###### Theorem 30 (Asymptotic Optimality of sPRM) 

The sPRM algorithm is asymptotically optimal.

###### Proof. 

By construction, ${V_{n}^{sPRM}\hspace{0pt}{(\omega)}} = {V_{n}^{{PRM}^{\ast}}\hspace{0pt}{(\omega)}}$, and ${E_{n}^{sPRM}\hspace{0pt}{(\omega)}} \supseteq {E_{n}^{{PRM}^{\ast}}\hspace{0pt}{(\omega)}}$ for all $\omega \in \Omega$. Hence, the graph returned by sPRM includes all the paths that are present in the graph returned by PRM^∗^. Then, asymptotic optimality of sPRM follows from that of PRM^∗^, which will be proven in Theorem 34 ‣ 4.2.2 Proposed algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning"). ∎∎

On the other hand, as in the case of probabilistic completeness, the heuristics that are often used in the practical implementation of (s)PRM are not asymptotically optimal.

###### Theorem 31 (Non-optimality of $k$-nearest sPRM) 

The $k$-nearest sPRM algorithm is not asymptotically optimal, for any constant $k \in {\mathbb{N}}$.

This theorem will be proven under the assumption that the underlying point process is Poisson. More precisely, the algorithm is analyzed when it is run with ${Poisson}\hspace{0pt}{(n)}$ samples. That is, the realization of the random variable ${Poisson}\hspace{0pt}{(n)}$ determines the number of points sampled independently and uniformly in $\mathcal{X}_{free}$. Hence, the expected number of samples is equal to $n$, although its realization may slightly differ. However, since the Poisson random variable has exponentially-decaying tails, its large deviations from its mean is unlikely (see, e.g., Grimmett and Stirzaker (2001) for a more precise statement). With a slight abuse of notation, the cost of the best path in the graph returned by the $k$-nearest sPRM algorithm when the algorithm is run with ${Poisson}\hspace{0pt}{(n)}$ number of samples is denoted by $Y_{n}^{k\hspace{0pt}{PRM}}$, and it is shown that ${{\mathbb{P}}\hspace{0pt}{({\{{{\operatorname{lim\ sup}_{n\rightarrow\infty}Y_{n}^{k\hspace{0pt}{PRM}}} = c^{\ast}}\}})}} = 0$.

###### Proof of Theorem 31 ‣ 4.2.1 Existing algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning"). 

Let $\sigma^{\ast}$ denote an optimal path and $s^{\ast}$ denote its length, i.e., $s^{\ast} = {T\hspace{0pt}V\hspace{0pt}{(\sigma^{\ast})}}$. For each $n$, consider a tiling of $\sigma^{\ast}$ with disjoint open hypercubes, each with edge length $2\hspace{0pt}n^{- {1/d}}$, such that the center of each cube is a point on $\sigma^{\ast}$. See Figure 5. Let $M_{n}$ denote the maximum number of tiles that can be generated in this manner and note ${M_{n} \geq {\frac{s^{\ast}}{2}\hspace{0pt}n^{1/d}}}.$ Partition each tile into several open cubes as follows: place an inner cube with edge length $n^{- {1/d}}$ at the center of the tile and place several outer cubes each with edge length $\frac{1}{2}\hspace{0pt}n^{- {1/d}}$ around the cube at the center as shown in Figure 5. Let $F_{d}$ denote the number of outer cubes. The volumes of the inner cube and each of the outer cubes are $n^{- 1}$ and $2^{- d}\hspace{0pt}n^{- 1}$, respectively.

Figure 5: An illustration of the tiles mention in the proof of Theorem 31. A single tile is shown in the left; a tiling of the optimal trajectory σ* is shown on the right.

For $n \in {\mathbb{N}}$ and $m \in {\{ 1,2,\ldots,M_{n}\}}$, consider the tile $m$ when the algorithm is run with ${Poisson}\hspace{0pt}{(n)}$ samples. Let $I_{n,m}$ denote the indicator random variable for the event that the center cube of this tile contains no samples, whereas every outer cube contains at least $k + 1$ samples, in tile $m$.

The probability that the inner cube contains no samples is $e^{- {{1/\mu}\hspace{0pt}{(\mathcal{X}_{free})}}}$. The probability that an outer cube contains at least $k + 1$ samples is ${1 - {{\mathbb{P}}\hspace{0pt}\left( {\{{{{Poisson}\hspace{0pt}{({{2^{- d}/\mu}\hspace{0pt}{(\mathcal{X}_{free})}})}} \geq {k + 1}}\}} \right)}} = {1 - {{\mathbb{P}}\hspace{0pt}{({\{{{{Poisson}\hspace{0pt}{({{2^{- d}/\mu}\hspace{0pt}{(\mathcal{X}_{free})}})}} \leq k}\}})}}} = {1 - \frac{\Gamma\hspace{0pt}{({k + 1},{{2^{- d}/\mu}\hspace{0pt}{(\mathcal{X}_{free})}})}}{k!}}$, where $\Gamma\hspace{0pt}{( \cdot , \cdot )}$ is the incomplete gamma function (Abramowitz and Stegun, 1964). Then, noting that the cubes in a given tile are disjoint and using the independence property of the Poisson process (see Lemma 11) ‣ 2.2 Random Geometric Graphs ‣ 2 Preliminary Material ‣ Sampling-based Algorithms for Optimal Motion Planning")),

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{E}}\hspace{0pt}\left\lbrack I_{n,m} \right\rbrack} = {e^{- {{1/\mu}\hspace{0pt}{(\mathcal{X}_{free})}}}\hspace{0pt}\left( {1 - \frac{\Gamma\hspace{0pt}{({k + 1},{{2^{- d}/\mu}\hspace{0pt}{(\mathcal{X}_{free})}})}}{k!}} \right)^{F_{d}}} > \,\, 0},$$   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

which is a constant that is independent of $n$; denote this constant by $\alpha$.

Let $G_{n} = {(V_{n},E_{n})}$ denote the graph returned by the $k$-nearest PRM algorithm by the end of ${Poisson}\hspace{0pt}{(n)}$ iterations. Observe that if $I_{n,m} = 1$, then there is no edge of $G_{n}$ crossing the cube of side length $\frac{1}{2}\hspace{0pt}n^{- {1/d}}$ that is centered at the center of the inner cube in tile $m$ (shown as the white cube in Figure 6). To prove this claim, note the following two facts. First, no point that is outside of the cubes can have an edge that crosses the inner cube. Second, no point in one of the outer cubes has an edge that has length greater than $\frac{\sqrt{d}}{2}\hspace{0pt}i^{- {1/d}}$. Thus, no edge can cross the white cube illustrated in Figure 6.

Figure 6: The event that the inner cube contains no points and each outer cube contains at least k points of the point process is illustrated. The cube of side length $\frac{1}{2}\hspace{0pt}n^{- {1/d}}$ is shown in white.

Let $\sigma_{n}$ denote the path in $G_{n}$ that is closest to $\sigma^{\ast}$ in terms of the bounded variation norm. Let $U_{n}:={\|{\sigma_{n} - \sigma^{\ast}}\|}_{BV}$. Notice that $U_{n} \geq {\frac{1}{2}\hspace{0pt}n^{- {1/d}}\hspace{0pt}{\sum_{m = 1}^{M_{n}}I_{n,m}}} = {\frac{1}{2}\hspace{0pt}n^{- {1/d}}\hspace{0pt}M_{n}\hspace{0pt}I_{n,1}} = {\frac{s^{\ast}}{4}\hspace{0pt}I_{n,1}}$. Then,

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{E}}\hspace{0pt}\left\lbrack {\operatorname{lim\ sup}\limits_{n\rightarrow\infty}U_{n}} \right\rbrack} \geq {\operatorname{lim\ sup}\limits_{n\rightarrow\infty}{{\mathbb{E}}\hspace{0pt}\left\lbrack U_{n} \right\rbrack}} \geq {\operatorname{lim\ sup}\limits_{n\rightarrow\infty}{\frac{s^{\ast}}{4}\hspace{0pt}{\mathbb{E}}\hspace{0pt}\left\lbrack I_{n,m} \right\rbrack}} \geq \frac{\alpha\hspace{0pt}s^{\ast}}{4} > \,\, 0},$$   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

where the first inequality follows from Fatou's lemma (Resnick, 1999). This implies ${{\mathbb{P}}\hspace{0pt}{({\{{{\operatorname{lim\ sup}_{n\rightarrow\infty}U_{n}} > 0}\}})}} > 0$. Since $U_{i} > 0$ implies $Y_{n} > c^{\ast}$ surely,

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( \left\{ {{\operatorname{lim\ sup}_{n\rightarrow\infty}Y_{n}} > c^{\ast}} \right\} \right)} \geq {{\mathbb{P}}\hspace{0pt}\left( \left\{ {{\operatorname{lim\ sup}_{n\rightarrow\infty}U_{n}} > 0} \right\} \right)} > 0}.$$   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

That is, ${{\mathbb{P}}\hspace{0pt}\left( \left\{ {{\operatorname{lim\ sup}_{n\rightarrow\infty}Y_{n}} = c^{\ast}} \right\} \right)} < 1$. In fact, by Lemma 25, ${{\mathbb{P}}\hspace{0pt}\left( \left\{ {{\operatorname{lim\ sup}_{n\rightarrow\infty}Y_{n}} = c^{\ast}} \right\} \right)} = 0$.∎∎

Second, asymptotic optimality of a large class of variable radius sPRM algorithms is considered. Consider a variable radius sPRM in which connection radius satisfies ${r\hspace{0pt}{(n)}} \leq {\gamma\hspace{0pt}n^{- {1/d}}}$ for some $\gamma > 0$ and for all $n \in {\mathbb{N}}$. The next theorem shows that this algorithm lacks the asymptotic optimality property.

###### Theorem 32 (Non-optimality of variable radius sPRM with ${r\hspace{0pt}{(n)}} = {\gamma\hspace{0pt}n^{- {1/d}}}$) 

Consider a variable radius sPRM algorithm with connection radius ${{r\hspace{0pt}{(n)}} = {\gamma\hspace{0pt}n^{- {1/d}}}}.$ This sPRM algorithm is not asymptotic optimal for any $\gamma \in {\mathbb{R}}_{\geq 0}$.

###### Proof. 

Let $\sigma^{\ast}$ denote a path that is a robust solution to the optimality problem. Let $n$ denote the number of samples that the algorithm is run with. For all $n$, construct a set $B_{n} = {\{ B_{n,1},B_{n,2},\ldots,B_{n,M_{n}}\}}$ of openly disjoint balls as follows. Each ball in $B_{n}$ has radius $r_{n} = {\gamma\hspace{0pt}n^{- {1/d}}}$, and lies entirely inside $\mathcal{X}_{free}$. Furthermore, the balls in $B_{n}$ "tile" $\sigma^{\ast}$ such that the center of each ball lies on $\sigma^{\ast}$ (see Figure 7). Let $M_{n}$ denote the maximum number of balls, $\overline{s}$ denote the length of the portion of $\sigma^{\ast}$ that lies within the $\delta$-interior of $\mathcal{X}_{free}$, and $n_{0} \in {\mathbb{N}}$ denote the number for which $r_{n} \leq \delta$ for all $n \geq n_{0}$.

Then, for all $n \geq n_{0}$,

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     $${M_{n} \geq \frac{\overline{s}}{2\hspace{0pt}\gamma\hspace{0pt}\left( \frac{1}{n} \right)^{1/d}} = {\frac{\overline{s}}{2\hspace{0pt}\gamma}\hspace{0pt}n^{1/d}}}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

Figure 7: An illustration of the covering of the optimal path, σ*, with openly disjoint balls. The balls cover only a portion of σ* that lies within the δ-interior of 𝒳free.

Indicate the graph returned by this sPRM algorithm as $G_{n} = {(V_{n},E_{n})}$. Denote the event that the ball $B_{n,m}$ contains no vertex in $V_{n}$ by $A_{n,m}$. Denote the indicator random variable for the event $A_{n,m}$ by $I_{n,m}$, i.e., $I_{n,m} = 1$ when $A_{n,m}$ holds and $I_{n,m} = 0$ otherwise. Then, for all $n \geq n_{0}$,

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\mathbb{E}}\hspace{0pt}{\lbrack I_{n,m}\rbrack}} = {{\mathbb{P}}\hspace{0pt}{(A_{n,m})}} = \left( {1 - \frac{\mu\hspace{0pt}{(B_{n,m})}}{\mu\hspace{0pt}{(\mathcal{X}_{free})}}} \right)^{n} = \left( {1 - {\frac{\zeta_{d}\hspace{0pt}\gamma^{d}}{\mu\hspace{0pt}{(\mathcal{X}_{free})}}\hspace{0pt}\frac{1}{n}}} \right)^{n}$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Let $N_{n}$ be the random variable that denotes the total number of balls in $B_{n}$ that contain no vertex in $V_{n}$, i.e., $N_{n} = {\sum_{m = 1}^{M_{n}}I_{n,m}}$. Then, for all $n \geq n_{0}$,

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{E}}\hspace{0pt}{\lbrack N_{n}\rbrack}} = {{\mathbb{E}}\hspace{0pt}\left\lbrack {\sum_{m = 1}^{M_{n}}I_{n,m}} \right\rbrack} = {\sum\limits_{m = 1}^{M_{n}}{{\mathbb{E}}\hspace{0pt}{\lbrack I_{n,m}\rbrack}}} = {M_{n}\hspace{0pt}{\mathbb{E}}\hspace{0pt}{\lbrack I_{n,1}\rbrack}} \geq {\frac{\overline{s}}{2\hspace{0pt}\gamma}\hspace{0pt}n^{1/d}\hspace{0pt}\left( {1 - {\frac{\zeta_{d}\hspace{0pt}\gamma^{d}}{\mu\hspace{0pt}{(\mathcal{X}_{free})}}\hspace{0pt}\frac{1}{n}}} \right)^{n}}}.$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Consider a ball $B_{n,m}$ that contains no vertices of this sPRM algorithm. Then, no edges of the graph returned by this algorithm cross the ball of radius $\frac{\sqrt{3}}{2}\hspace{0pt}r_{n}$ centered at the center of $B_{n,m}$. See Figure 8.

Figure 8: If the outer ball does not contain vertices of the PRM graph, then no edge of the graph corresponds to a path crossing the inner ball.

Let $P_{n}$ denote the (finite) set of all acyclic paths that reach the goal region in the graph returned by this sPRM algorithm when the algorithm is run with $n$ samples. Let $U_{n}$ denote the total variation of the path that is closest to $\sigma^{\ast}$ among all paths in $P_{n}$, i.e., $U_{n}:={\min_{\sigma_{n} \in P_{n}}{\|{\sigma_{n} - \sigma^{\ast}}\|}_{BV}}$. Then,

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     $${{{\mathbb{E}}\hspace{0pt}{\lbrack U_{n}\rbrack}} \geq {{\mathbb{E}}\hspace{0pt}\left\lbrack {\gamma\hspace{0pt}\left( \frac{1}{n} \right)^{1/d}\hspace{0pt}N_{n}} \right\rbrack} \geq {\frac{\overline{s}}{2}\hspace{0pt}\left( {1 - {\frac{\zeta_{d}\hspace{0pt}\gamma^{d}}{\mu\hspace{0pt}{(\mathcal{X}_{free})}}\hspace{0pt}\frac{1}{n}}} \right)^{n}}}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

Taking the limit superior of both sides, the following inequality can be established:

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{E}}\hspace{0pt}\left\lbrack {\operatorname{lim\ sup}\limits_{n\rightarrow\infty}U_{n}} \right\rbrack} \geq {\operatorname{lim\ sup}\limits_{n\rightarrow\infty}{{\mathbb{E}}\hspace{0pt}\left\lbrack U_{n} \right\rbrack}} \geq {\operatorname{lim\ sup}\limits_{n\rightarrow\infty}{\frac{\overline{s}}{2}\hspace{0pt}\left( {1 - {\frac{\zeta_{d}\hspace{0pt}\gamma^{d}}{\mu\hspace{0pt}{(\mathcal{X}_{free})}}\hspace{0pt}\frac{1}{n}}} \right)^{n}}} = {\frac{\overline{s}}{2}\hspace{0pt}e^{- \frac{\zeta_{d}\hspace{0pt}\gamma^{d}}{\mu\hspace{0pt}{(\mathcal{X}_{free})}}}} > 0},$$   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

where the first inequality follows from Fatou's lemma (Resnick, 1999). Hence, ${{\mathbb{P}}\hspace{0pt}{({\{{{\operatorname{lim\ sup}_{n\rightarrow\infty}U_{n}} > 0}\}})}} > 0$, which implies that ${{\mathbb{P}}\hspace{0pt}\left( \left\{ {{\operatorname{lim\ sup}_{n\rightarrow\infty}Y_{n}^{ALG}} > c^{\ast}} \right\} \right)} > 0$. That is, ${{\mathbb{P}}\hspace{0pt}\left( \left\{ {{\operatorname{lim\ sup}_{n\rightarrow\infty}Y_{n}^{ALG}} = c^{\ast}} \right\} \right)} < 1$. In fact, ${{\mathbb{P}}\hspace{0pt}\left( \left\{ {{\operatorname{lim\ sup}_{n\rightarrow\infty}Y_{n}^{ALG}} = c^{\ast}} \right\} \right)} = 0$ by the Kolmogorov zero-one law (see Lemma 25). ∎∎

##### Rapidly-exploring Random Trees 

In this section, it is shown that the minimum-cost path in the RRT algorithm converges to a certain random variable, however, under mild technical assumptions, this random variable is not equal to the optimal cost, with probability one.

###### Theorem 33 (Non-optimality of RRT) 

The RRT algorithm is not asymptotically optimal.

The proof of this theorem can be found in Appendix B ‣ Sampling-based Algorithms for Optimal Motion Planning"). Note that, since at each iteration the RRT algorithm either adds a vertex and an edge, or leaves the graph unchanged, ${G_{i}^{RRT}\hspace{0pt}{(\omega)}} \subseteq {G_{i + 1}^{RRT}\hspace{0pt}{(\omega)}}$, for all $i \in {\mathbb{N}}$ and all $\omega \in \Omega$, and hence the limit $\lim_{n\rightarrow\infty}Y_{n}^{RRT}$ exists and is equal to the random variable $Y_{\infty}^{RRT}$. In conjunction with Lemma 25, Theorem 33 ‣ Rapidly-exploring Random Trees ‣ 4.2.1 Existing algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning") implies that this limit is strictly greater than $c^{\ast}$ almost surely, i.e., ${{\mathbb{P}}\hspace{0pt}\left( {\{{{\lim_{n\rightarrow\infty}Y_{n}^{RRT}} > c^{\ast}}\}} \right)} = 1$. In other words, the cost of the best solution returned by RRT converges to a suboptimal value, with probability one. In fact, it is possible to construct problem instances such that the probability that the first solution returned by the RRT algorithm has arbitrarily high cost is bounded away from zero (Nechushtan et al., 2010).

Since the cost of the best path returned by the RRT algorithm converges to a random variable, Theorem 33 ‣ Rapidly-exploring Random Trees ‣ 4.2.1 Existing algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning") provides new insight explaining the effectiveness of approaches as in Ferguson and Stentz (2006). In fact, running multiple instances of the RRT algorithm amounts to drawing multiple samples of $Y_{\infty}^{RRT}$.

#### 4.2.2 Proposed algorithms 

In this section, the proposed algorithms are analyzed for asymptotic optimality, i.e., almost sure convergence to optimal solutions. It is shown that the PRM^∗^, RRG, and RRT^∗^ algorithms, as well as their $k$-nearest implementations, are all asymptotically optimal. The proofs of the following theorems are quite lengthy, and will be provided in the appendix.

Recall that $d$ denotes the dimensionality of the configuration space, $\mu\hspace{0pt}{(\mathcal{X}_{free})}$ denotes the Lebesgue measure of the obstacle-free space, and $\zeta_{d}$ denotes the volume of the unit ball in the $d$-dimensional Euclidean space. Proofs of the following theorems can be found in Appendices C ‣ Sampling-based Algorithms for Optimal Motion Planning")--G ‣ Sampling-based Algorithms for Optimal Motion Planning").

###### Theorem 34 (Asymptotic optimality of PRM^∗^) 

If $\gamma_{PRM} > {2\hspace{0pt}{({1 + {1/d}})}^{1/d}\hspace{0pt}\left( \frac{\mu\hspace{0pt}{(X_{free})}}{\zeta_{d}} \right)^{1/d}}$, then the PRM^∗^ algorithm is asymptotically optimal.

###### Theorem 35 (Asymptotic optimality of $k$-nearest PRM^∗^) 

If $k_{PRM} > {e\hspace{0pt}{({1 + {1/d}})}}$, then the $k$-nearest implementation of the PRM^∗^ algorithm is asymptotically optimal.

###### Theorem 36 (Asymptotic optimality of RRG) 

If $\gamma_{PRM} > {2\hspace{0pt}{({1 + {1/d}})}^{1/d}\hspace{0pt}\left( \frac{\mu\hspace{0pt}{(X_{free})}}{\zeta_{d}} \right)^{1/d}}$, then the RRG algorithm is asymptotically optimal.

###### Theorem 37 (Asymptotic optimality of $k$-nearest RRG) 

If $k_{RRG} > {e\hspace{0pt}{({1 + {1/d}})}}$, then the $k$-nearest implementation of the RRG algorithm is asymptotically optimal.

###### Theorem 38 (Asymptotic optimality of RRT^∗^) 

If $\gamma_{{RRT}^{\ast}} > {{({2\hspace{0pt}{({1 + {1/d}})}})}^{1/d}\hspace{0pt}\left( \frac{\mu\hspace{0pt}{(X_{free})}}{\zeta_{d}} \right)^{1/d}}$, then the RRT^∗^ algorithm is asymptotically optimal.

###### Theorem 39 (Asymptotic optimality of $k$-nearest RRT^∗^) 

If $k_{{RRT}^{\ast}} > {2^{d + 1}\hspace{0pt}e\hspace{0pt}{({1 + {1/d}})}}$, then the $k$-nearest implementation of the RRT^∗^ algorithm is asymptotically optimal.

The proof of the latter theorem follows from those of Theorems 37 ‣ 4.2.2 Proposed algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning") and 38 ‣ 4.2.2 Proposed algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning").

### 4.3 Computational Complexity 

The objective of this section is to compare the computational complexity of the algorithms provided in Section 3. First, each algorithm is analyzed in terms of the number of calls to the $\mathtt{C}\mathtt{o}\mathtt{l}\mathtt{l}\mathtt{i}\mathtt{s}\mathtt{i}\mathtt{o}\mathtt{n}\mathtt{F}\mathtt{r}\mathtt{e}\mathtt{e}$ procedure. Second, the computational complexity of certain primitive procedures such as $\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}$ and $\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}$ (see Section 3.1) are analyzed. Using these results, a thorough analysis of the computational complexity of the all the algorithms is given in terms of the number of simple operations, such as comparisons, additions, multiplications. An analysis of the computational complexity of the query phase, i.e., the complexity of extracting the optimal solution from the graph returned by these algorithms, is also provided.

The following notation for asymptotic computational complexity will be used throughout this section. Let $W_{n}^{ALG}\hspace{0pt}{(P)}$ be a function of the graph returned by algorithm $ALG$ when $ALG$ is run with inputs $P = {(\mathcal{X}_{free},x_{init},\mathcal{X}_{goal})}$ and $n$. Clearly, $W_{n}^{ALG}\hspace{0pt}{(P)}$ is a random variable. Let $f:{{\mathbb{N}}\rightarrow{\mathbb{N}}}$ be an increasing function with ${\lim_{n\rightarrow\infty}{f\hspace{0pt}{(n)}}} = \infty$. The random variable $W_{n}^{ALG}$ is said belong to $\Omega\hspace{0pt}{({f\hspace{0pt}{(n)}})}$, denoted as $W_{n}^{ALG} \in {\Omega\hspace{0pt}{({f\hspace{0pt}{(n)}})}}$, if there exists a problem instance $P = {(\mathcal{X}_{free},x_{init},\mathcal{X}_{goal})}$ such that ${\operatorname{lim\ inf}_{n\rightarrow\infty}{{\mathbb{E}}\hspace{0pt}{\lbrack{{{W_{n}^{ALG}\hspace{0pt}{(P)}}/f}\hspace{0pt}{(n)}}\rbrack}}} > 0$. Similarly, $W_{n}^{ALG}$ is said to belong to $O\hspace{0pt}{({f\hspace{0pt}{(n)}})}$ if ${\operatorname{lim\ sup}_{n\rightarrow\infty}{{\mathbb{E}}\hspace{0pt}{\lbrack{{{W_{n}^{ALG}\hspace{0pt}{(P)}}/f}\hspace{0pt}{(n)}}\rbrack}}} < \infty$ for all problem instances $P = {(\mathcal{X}_{free},x_{init},\mathcal{X}_{goal})}$.

##### Number of calls to the $\mathtt{C}\mathtt{o}\mathtt{l}\mathtt{l}\mathtt{i}\mathtt{s}\mathtt{i}\mathtt{o}\mathtt{n}\mathtt{F}\mathtt{r}\mathtt{e}\mathtt{e}$ procedure 

Let $M_{n}^{ALG}$ denote the total number of calls to the $\mathtt{C}\mathtt{o}\mathtt{l}\mathtt{l}\mathtt{i}\mathtt{s}\mathtt{i}\mathtt{o}\mathtt{n}\mathtt{F}\mathtt{r}\mathtt{e}\mathtt{e}$ procedure by algorithm $ALG$ in iteration $n$.

First, lower-bounds are established for the PRM and sPRM algorithms.

###### Lemma 40 (PRM) 

$M_{n}^{PRM} \in {\Omega\hspace{0pt}{(n)}}$.

###### Proof. 

Consider the problem instance $(\mathcal{X}_{free},x_{init},\mathcal{X}_{goal})$, where $\mathcal{X}_{free}$ is composed of two openly-disjoint sets $\mathcal{X}_{1}$ and $\mathcal{X}_{2}$ (see Figure 9). The set $\mathcal{X}_{2}$ is designed to be a hyperrectangle shaped set with one side equal to $r/2$, where $r$ is the connection radius.

Figure 9: An illustration of 𝒳free = 𝒳1 ∪ 𝒳2.

Any $r$-ball centered at a point in $\mathcal{X}_{2}$ will certainly contain a nonzero measure part of $\mathcal{X}_{2}$. Define $\overline{\mu}$ as the volume of the smallest region in $\mathcal{X}_{2}$ that can be intersected by an $r$-ball centered at $\mathcal{X}_{2}$, i.e., $\overline{\mu}:={\inf_{x \in \mathcal{X}_{2}}{\mu\hspace{0pt}{({\mathcal{B}_{x,r} \cap \mathcal{X}_{1}})}}}$. Clearly, $\overline{\mu} > 0$.

Thus, for any sample $X_{n}$ that falls into $\mathcal{X}_{2}$, the PRM algorithm will attempt to connect $X_{n}$ to a certain number of vertices that lies in a subset $\mathcal{X}_{1}^{\prime}$ of $\mathcal{X}_{1}$ such that ${\mu\hspace{0pt}{(\mathcal{X}_{1}^{\prime})}} \geq \overline{\mu}$. The expected number of vertices in $\mathcal{X}_{1}^{\prime}$ is at least $\overline{\mu}\hspace{0pt}n$. Moreover, none of these vertices can be in the same connected component with $X_{n}$. Thus, ${{\mathbb{E}}\hspace{0pt}{\lbrack{M_{n}^{PRM}/n}\rbrack}} > \overline{\mu}$. The result is obtained by taking the limit inferior of both sides. ∎∎

###### Lemma 41 (sPRM) 

$M_{n}^{sPRM} \in {\Omega\hspace{0pt}{(n)}}$.

###### Proof. 

The proof of a stronger result is provided. It is shown that for all problem instances $P = {(\mathcal{X}_{free},x_{init},\mathcal{X}_{goal})}$, ${\operatorname{lim\ inf}_{n\rightarrow\infty}{{\mathbb{E}}\hspace{0pt}{\lbrack{M_{n}^{sPRM}/n}\rbrack}}} > 0$, which implies the lemma. Recall from Algorithm 2: ‣ 3.2 Existing Algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning") that $r$ denotes the connection radius. Let $\overline{\mu}$ denote the volume of the smallest region that can be formed by intersecting $\mathcal{X}_{free}$ with an $r$-ball centered at a point inside $\mathcal{X}_{free}$, i.e., ${\overline{\mu}:={\inf_{x \in \mathcal{X}_{free}}{\mu\hspace{0pt}{({\mathcal{B}_{x,r} \cap \mathcal{X}_{free}})}}}}.$ Recall that $\mathcal{X}_{free}$ is the closure of an open set. Hence, $\overline{\mu} > 0$.

Clearly, $M_{n}$, the number of calls to the $\mathtt{C}\mathtt{o}\mathtt{l}\mathtt{l}\mathtt{i}\mathtt{s}\mathtt{i}\mathtt{o}\mathtt{n}\mathtt{F}\mathtt{r}\mathtt{e}\mathtt{e}$ procedure in iteration $n$, is equal to the number of nodes inside the ball of radius $r$ centered at the last sample point $X_{n}$. Moreover, the volume of the $\mathcal{X}_{free}$ that lies inside this ball is at least $\overline{\mu}$. Then, the expected value of $M_{n}$ is lower bounded by the expected value of a binomial random variable with parameters ${\overline{\mu}/\mu}\hspace{0pt}{(\mathcal{X}_{free})}$ and $n$, since the underlying point process is binomial. Thus, ${{{\mathbb{E}}\hspace{0pt}{\lbrack M_{n}^{sPRM}\rbrack}} \geq {\frac{\overline{\mu}}{\mu\hspace{0pt}{(\mathcal{X}_{free})}}\hspace{0pt}n}}.$ Then, ${{\mathbb{E}}\hspace{0pt}{\lbrack{M_{n}/n}\rbrack}} \geq {\overline{\mu}/\mathcal{X}_{free}}$ for all $n \in {\mathbb{N}}$. Taking the limit inferior of both sides gives the result. ∎∎

Clearly, for $k$-nearest PRM, $M_{n}^{k\hspace{0pt}\text{-}\hspace{0pt}{sPRM}} = k$ for all $n \in {\mathbb{N}}$ with $n > k$. Similarly, for the RRT, $M_{n}^{RRT} = 1$ for all $n \in {\mathbb{N}}$.

The next lemma upper-bounds the number of calls to the $\mathtt{C}\mathtt{o}\mathtt{l}\mathtt{l}\mathtt{i}\mathtt{s}\mathtt{i}\mathtt{o}\mathtt{n}\mathtt{F}\mathtt{r}\mathtt{e}\mathtt{e}$ procedure in the proposed algorithms.

###### Lemma 42 (PRM^∗^, RRG, and RRT^∗^) 

${M_{n}^{{PRM}^{\ast}},M_{n}^{RRG},M_{n}^{{RRT}^{\ast}}} \in {O\hspace{0pt}{({\log n})}}$.

###### Proof. 

First, consider PRM^∗^. Recall that $r_{n}$ denotes the connection radius of the PRM^∗^ algorithm. Recall that the $r_{n}$ interior of $\mathcal{X}_{free}$, denoted by ${int}_{r_{n}}\hspace{0pt}{(\mathcal{X}_{free})}$, is defined as the set of all points $x$, for which the $r_{n}$-ball centered at $x$ lies entirely inside $\mathcal{X}_{free}$. Let $A$ denote the event that the sample $X_{n}$ drawn at the last iteration falls into the $r_{n}$ interior of $\mathcal{X}_{free}$. Then,

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     $${{{\mathbb{E}}\hspace{0pt}\left\lbrack M_{n}^{{PRM}^{\ast}} \right\rbrack} = {{{\mathbb{E}}\hspace{0pt}\left\lbrack M_{n}^{{PRM}^{\ast}} \middle| A \right\rbrack\hspace{0pt}{\mathbb{P}}\hspace{0pt}{(A)}} + {{\mathbb{E}}\hspace{0pt}\left\lbrack M_{n}^{{PRM}^{\ast}} \middle| A^{c} \right\rbrack\hspace{0pt}{\mathbb{P}}\hspace{0pt}{(A^{c})}}}}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

Let $n_{0} \in {\mathbb{N}}$ be the smallest number such that ${\mu\hspace{0pt}{({{int}_{r_{n}}\hspace{0pt}{(\mathcal{X}_{free})}})}} > 0$. Clearly, such $n_{0}$ exists, since ${\lim_{n\rightarrow\infty}r_{n}} = 0$ and $\mathcal{X}_{free}$ has non-empty interior. Recall that $\zeta_{d}$ is the volume of the unit ball in the $d$-dimensional Euclidean space and that the connection radius of the PRM^∗^ algorithm is $r_{n} = {\gamma_{PRM}\hspace{0pt}{({\log{n/n}})}^{1/d}}$. Then, for all $n \geq n_{0}$

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     $${{{\mathbb{E}}\hspace{0pt}\left\lbrack M_{n}^{{PRM}^{\ast}} \middle| A \right\rbrack} = {\frac{\zeta_{d}\hspace{0pt}\gamma_{PRM}}{\mu\hspace{0pt}{({{int}_{r_{n}}\hspace{0pt}{(\mathcal{X}_{free})}})}}\hspace{0pt}{\log n}}}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

On the other hand, given that $X_{n} \notin {{int}_{r_{n}}\hspace{0pt}{(\mathcal{X}_{free})}}$, the $r_{n}$-ball centered at $X_{n}$ intersects a fragment of $\mathcal{X}_{free}$ that has volume less than the volume of an $r_{n}$-ball in the $d$-dimensional Euclidean space. Then, for all $n > n_{0}$, ${{{\mathbb{E}}\hspace{0pt}\left\lbrack M_{n}^{{PRM}^{\ast}} \middle| A^{c} \right\rbrack} \leq {{\mathbb{E}}\hspace{0pt}\left\lbrack M_{n}^{{PRM}^{\ast}} \middle| A \right\rbrack}}.$

Hence, for all $n \geq n_{0}$,

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{E}}\hspace{0pt}\left\lbrack \frac{M_{n}^{{PRM}^{\ast}}}{\log n} \right\rbrack} \leq \frac{\zeta_{d}\hspace{0pt}\gamma_{PRM}}{\mu\hspace{0pt}{({{int}_{r_{n}}\hspace{0pt}{(\mathcal{X}_{free})}})}} \leq \frac{\zeta_{d}\hspace{0pt}\gamma_{PRM}}{\mu\hspace{0pt}{({{int}_{r_{n_{0}}}\hspace{0pt}{(\mathcal{X}_{free})}})}}}.$$   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Next, consider the RRG. Recall that $\eta$ is the parameter provided in the $\mathtt{S}\mathtt{t}\mathtt{e}\mathtt{e}\mathtt{r}$ procedure (see Section 3.1). Let $D$ denote the diameter of the set $\mathcal{X}_{free}$, i.e., $D:={\sup_{{x,x^{\prime}} \in \mathcal{X}_{free}}{\|{x - x^{\prime}}\|}}$. Clearly, whenever $\eta \geq D$, $V^{{PRM}^{\ast}} = V^{RRG} = V^{{RRT}^{\ast}}$ surely, and the claim holds.

To prove the claim when $\eta < D$, let $C_{n}$ denote the event that for any point $x \in \mathcal{X}_{free}$ the RRG algorithm has a vertex $x^{\prime} \in V_{n}^{RRG}$ such that ${\|{x - x^{\prime}}\|} \leq \eta$. As shown in the proof of Theorem 36 ‣ 4.2.2 Proposed algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning") (see Lemma 63 ‣ Sampling-based Algorithms for Optimal Motion Planning")), there exists ${a,b} > 0$ such that ${{\mathbb{P}}\hspace{0pt}{(C_{n}^{c})}} \leq {a\hspace{0pt}e^{- {b\hspace{0pt}n}}}$. Then,

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{E}}\hspace{0pt}\left\lbrack M_{n}^{RRG} \right\rbrack} = {{{\mathbb{E}}\hspace{0pt}\left\lbrack M_{n}^{RRG} \middle| C_{n} \right\rbrack\hspace{0pt}{\mathbb{P}}\hspace{0pt}{(C_{n})}} + {{\mathbb{E}}\hspace{0pt}\left\lbrack M_{n}^{RRG} \middle| C_{n}^{c} \right\rbrack\hspace{0pt}{\mathbb{P}}\hspace{0pt}{(C_{n}^{c})}}}},$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Clearly, ${{\mathbb{E}}\hspace{0pt}\left\lbrack M_{n}^{RRG} \middle| C_{n}^{c} \right\rbrack} \leq n$. Hence, the second term of the sum on the right hand side converges to zero as $n$ approaches infinity. On the other hand, given that $C_{n}$ holds, the new vertex that will be added to the graph at iteration $n$, if such a vertex is added at all, will be the same as the last sample, $X_{n}$. To complete the argument, given any set of $n$ points placed inside $\mu\hspace{0pt}{(X_{free})}$, let $N_{n}$ denote the number of points that are inside a ball of radius $r_{n}$ that is centered at a point $X_{n}$ sampled uniformly at random from $\mu\hspace{0pt}{(X_{free})}$. The expected number of points inside this ball is no more than ${\frac{\zeta_{d}\hspace{0pt}r_{n}^{d}}{\mu\hspace{0pt}{(X_{free})}}\hspace{0pt}n}.$ Hence, ${{\mathbb{E}}\hspace{0pt}{\lbrack\left. M_{n}^{RRG} \middle| C_{n} \right.\rbrack}} < {\frac{\zeta_{d}\hspace{0pt}\gamma_{PRM}}{\mu\hspace{0pt}{(X_{free})}}\hspace{0pt}{\log n}}$, which implies the existence of a constant $\phi_{1} \in {\mathbb{R}}_{\geq 0}$ such that ${\operatorname{lim\ sup}_{n\rightarrow\infty}{{\mathbb{E}}\hspace{0pt}{\lbrack{M_{n}^{RRG}/{({\log n})}}\rbrack}}} \leq \phi_{1}$.

Finally, since $M_{n}^{{RRT}^{\ast}} = M_{n}^{RRG}$ holds surely, ${\operatorname{lim\ sup}_{n\rightarrow\infty}{{\mathbb{E}}\hspace{0pt}{\lbrack{M_{n}^{RRG}/{({\log n})}}\rbrack}}} \leq \phi_{1}$ also. ∎∎

Trivially, $M_{n}^{k\hspace{0pt}\text{-}\hspace{0pt}{PRM}^{\ast}} = M_{n}^{k\hspace{0pt}\text{-}\hspace{0pt}{RRG}} = M_{n}^{k\hspace{0pt}\text{-}\hspace{0pt}{RRT}^{\ast}} = {k\hspace{0pt}{\log n}}$ for all $n$ with ${n/{\log n}} > k$.

##### Complexity of the $\mathtt{C}\mathtt{o}\mathtt{l}\mathtt{l}\mathtt{i}\mathtt{s}\mathtt{i}\mathtt{o}\mathtt{n}\mathtt{F}\mathtt{r}\mathtt{e}\mathtt{e}$ procedure 

In this section, complexity of the $\mathtt{C}\mathtt{o}\mathtt{l}\mathtt{l}\mathtt{i}\mathtt{s}\mathtt{i}\mathtt{o}\mathtt{n}\mathtt{F}\mathtt{r}\mathtt{e}\mathtt{e}$ procedure in terms of the number of obstacles in the environment is analyzed, which is a widely-studied problem in the literature (see, e.g., Lin and Manocha (2004) for a survey). The main result is based on Six and Wood (1982), which shows that checking collision with $m$ obstacles can be executed in $O\hspace{0pt}{({\log^{d}m})}$ time using data structures based on spatial trees (see also Edelsbrunner and Maurer, 1981; Hopcroft et al., 1983).

##### Complexity of the $\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}$ procedure 

The nearest neighbor search problem has been widely studied in the literature, since it has many applications in, e.g., computer graphics, database systems, image processing, data mining, pattern recognition, etc. (Samet, 1989b, a). Clearly, a brute-force algorithm that examines every vertex runs in $O\hspace{0pt}{(n)}$ time and requires $O\hspace{0pt}{(1)}$ space. However, in many online real-time applications such as robotics, it is highly desirable to reduce the computation time of each iteration under sublinear bounds, e.g., in $O\hspace{0pt}{({\log n})}$ time, especially for anytime algorithms that provide better solutions as the number of iterations increase.

Fortunately, existing algorithms for computing an "approximate" nearest neighbor, if not an exact one, are computationally very efficient. In the sequel, a vertex $y$ is said to be an $\varepsilon$-approximate nearest neighbor of a point $x$ if ${\|{y - x}\|} \leq {{({1 + \varepsilon})}\hspace{0pt}{\|{z - x}\|}}$, where $z$ is the true nearest neighbor of $x$. An approximate nearest neighbor can be computed using balanced-box decomposition (BBD) trees, which achieves $O\hspace{0pt}{({c_{d,\varepsilon}\hspace{0pt}{\log n}})}$ query time using $O\hspace{0pt}{({d\hspace{0pt}n})}$ space (Arya et al., 1999), where $c_{d,\varepsilon} \leq {d\hspace{0pt}{\lceil{1 + {{6\hspace{0pt}d}/\varepsilon}}\rceil}^{d}}$. This algorithm is computationally optimal in fixed dimensions, since it closely matches a lower bound for algorithms that use a tree structure stored in roughly linear space (Arya et al., 1999). Using approximate nearest neighbor computation in the context of both PRMs and RRTs was discussed very recently in Yershova and LaValle (2007); Plaku and Kavraki (2008).

Let $G = {(V,E)}$ be a graph with $V \subseteq \mathcal{X}$ and let $x \in \mathcal{X}$. The discussion above implies that the number of simple operations executed by the ${\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}}\hspace{0pt}{(G,x)}$ procedure is $\Theta\hspace{0pt}{({\log{|V|}})}$ in fixed dimensions, if the $\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}$ procedure is implemented using a tree structure that is stored in linear space.

##### Complexity of the $\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}$ procedure 

Problems similar to that solved by the $\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}$ procedure are also widely-studied in the literature, generally under the name of range search problems, as they have many applications in, for instance, computer graphics and spatial database systems (Samet, 1989a). In the worst case and in fixed dimensions, computing the exact set of vertices that reside in a ball of radius $r_{n}$ centered at a query point $x$ takes $O\hspace{0pt}{({n^{1 - {1/d}} + m})}$ time using $k$-d trees (Lee and Wong, 1977), where $m$ is the number of vertices returned by the search (see also Chanzy et al. (2001) for an analysis of the average case).

Similar to the nearest neighbor search, computing approximate solutions to the range search problem is computationally easier. A range search algorithm is said to be $\varepsilon$-approximate if it returns all vertices that reside in the ball of size $r_{n}$ and no vertices outside a ball of radius ${({1 + \varepsilon})}\hspace{0pt}r_{n}$, but may or may not return the vertices that lie outside the former ball and inside the latter ball. Computing $\varepsilon$-approximate solutions using BBD-trees requires $O\hspace{0pt}{({{2^{d}\hspace{0pt}{\log n}} + {d^{2}\hspace{0pt}{({{3\hspace{0pt}\sqrt{d}}/\varepsilon})}^{d - 1}}})}$ time when using $O\hspace{0pt}{({d\hspace{0pt}n})}$ space, in the worst case (Arya and Mount, 2000). Thus, in fixed dimensions, the complexity of this algorithm is $O\hspace{0pt}{({{\log n} + {({1/\varepsilon})}^{d - 1}})}$, which is known to be optimal, closely matching a lower bound (Arya and Mount, 2000). More recently, algorithms that can provide trade-offs between time and space were also proposed (Arya et al., 2005).

Note that the $\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}$ procedure can be implemented as an approximate range search while maintaining the asymptotic optimality guarantee. Notice that the expected number of vertices returned by the $\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}$ procedure also does not change, except by a constant factor. Hence, the $\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}$ procedure can be implemented to run in order $\log n$ expected time in the limit and linear space in fixed dimensions.

##### Time complexity of the processing phase 

The following results characterize the asymptotic computational complexity of various sampling-based algorithms in terms of the number of simple operations such as comparisons, additions, and multiplications.

Let $n$ denote the total number of iterations (or, alternatively, the number of samples), and $m$ denote the number of obstacles in the environment. Then, by Lemmas 40 ‣ Number of calls to the 𝙲𝚘𝚕𝚕𝚒𝚜𝚒𝚘𝚗𝙵𝚛𝚎𝚎 procedure ‣ 4.3 Computational Complexity ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning") and 41 ‣ Number of calls to the 𝙲𝚘𝚕𝚕𝚒𝚜𝚒𝚘𝚗𝙵𝚛𝚎𝚎 procedure ‣ 4.3 Computational Complexity ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning"), ${N_{n}^{PRM},N_{n}^{sPRM}} \in {\Omega\hspace{0pt}{({n^{2}\hspace{0pt}{\log^{d}m}})}}$. In the $k$-nearest sPRM and RRT algorithms, $\Omega\hspace{0pt}{({\log n})}$ time is spent on finding the ($k$-)nearest neighbor(s) and $\Omega\hspace{0pt}{({\log^{d}m})}$ time is spent on collision checking at each iteration. Hence, ${N_{n}^{k\hspace{0pt}\text{-}\hspace{0pt}{sPRM}},N_{n}^{RRT}} \in {\Omega\hspace{0pt}{({{n\hspace{0pt}{\log n}} + {n\hspace{0pt}{\log^{d}m}}})}}$.

In all the proposed algorithms, $O\hspace{0pt}{({\log n})}$ time is spent on finding the near neighbors, and $\log{n\hspace{0pt}{\log^{d}m}}$ time is spent on collision checking. Thus, $N_{n}^{ALG} \in {O\hspace{0pt}{({n\hspace{0pt}{\log{n\hspace{0pt}{\log^{d}m}}}})}}$ for $ALG \in {\{{PRM}^{\ast},k\text{-}{PRM}^{\ast},}$ ${RRG},k\text{-}{RRG},{RRT}^{\ast},k\text{-}{RRT}^{\ast}\}$.

##### Time complexity of the query phase 

After algorithm $ALG$ returns the graph $G_{n}^{ALG}$, the optimal path must be extracted from this graph using, e.g., Dijkstra's shortest path algorithm (Schrijver, 2003). In this section, the complexity of this operation, called the query phase, is discussed.

The following lemma yields the asymptotic computational complexity of computing shortest paths. Let $G = {(V,E)}$ be a graph. A length function $l:{E\rightarrow{\mathbb{R}}_{> 0}}$ is a function that assigns each edge in $E$ a positive length. Given a vertex $v \in V$, the shortest paths tree for $G$, $l$, and $v$ is a graph $G^{\prime} = {(V,E^{\prime})}$, where $E^{\prime} \subseteq E$ such that for any $v^{\prime} \in {V \smallsetminus {\{ v\}}}$, there exists a unique path in $G$ that starts from $v$ and reaches $v^{\prime}$, moreover, this path is the optimal such path in $G$.

###### Lemma 43 (Complexity of shortest paths (Schrijver, 2003)) 

Given a graph $G = {(V,E)}$, a length function $l:{E\rightarrow{\mathbb{R}}_{> 0}}$, and a vertex $v \in V$, the shortest path tree for $G$, $l$, and $v$ can be found in time $O\hspace{0pt}{({{{|V|}\hspace{0pt}{\log{({|V|})}}} + {|E|}})}$.

It remains to determine the number of vertices and edges in $G_{n}^{ALG} = {(V_{n}^{ALG},E_{n}^{ALG})}$, for each algorithm $ALG$.

Trivially, ${|E_{n}^{ALG}|} \in {\Omega\hspace{0pt}{(n)}}$ holds for all the algorithms discussed in this paper, in particular, for ${A\hspace{0pt}L\hspace{0pt}G} \in {\{{PRM},{k\hspace{0pt}\text{-}\hspace{0pt}{sPRM}},{RRT}\}}$. For the sPRM algorithm, a stronger bound can be provided: ${|E_{n}^{sPRM}|} \in {\Omega\hspace{0pt}{(n^{2})}}$. To prove this claim, consider the problem instance $(\mathcal{X}_{free},x_{init},\mathcal{X}_{goal})$, where $\mathcal{X}_{free} = \mathcal{X} = {(0,1)}^{d}$. Then, the straight path between any two vertices will be collision-free. Thus, the number of edges is exactly equal to the number of calls to the CollisionFree procedure. Then, the result follows from Lemma 41 ‣ Number of calls to the 𝙲𝚘𝚕𝚕𝚒𝚜𝚒𝚘𝚗𝙵𝚛𝚎𝚎 procedure ‣ 4.3 Computational Complexity ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning").

For the proposed algorithms, ${{|E_{n}^{{PRM}^{\ast}}|},{|E_{n}^{RRG}|}} \in {O\hspace{0pt}{({n\hspace{0pt}{\log n}})}}$. Since the number of edges is always less than or equal to the total number of calls to the $\mathtt{C}\mathtt{o}\mathtt{l}\mathtt{l}\mathtt{i}\mathtt{s}\mathtt{i}\mathtt{o}\mathtt{n}\mathtt{F}\mathtt{r}\mathtt{e}\mathtt{e}$ procedure, this claim follows directly from Lemma 42 ‣ Number of calls to the 𝙲𝚘𝚕𝚕𝚒𝚜𝚒𝚘𝚗𝙵𝚛𝚎𝚎 procedure ‣ 4.3 Computational Complexity ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning"). Finally, ${{|E_{n}^{k\hspace{0pt}\text{-}\hspace{0pt}{PRM}^{\ast}}|},{|E_{n}^{k\hspace{0pt}\text{-}\hspace{0pt}{RRG}}|}} \in {O\hspace{0pt}{({n\hspace{0pt}{\log n}})}}$ and ${{|E_{n}^{{RRT}^{\ast}}|},{|E_{n}^{k\hspace{0pt}\text{-}\hspace{0pt}{RRT}^{\ast}}|}} \in {O\hspace{0pt}{(n)}}$ all hold trivially.

##### Space complexity 

Space complexity of an algorithm $ALG$ is defined as the amount of memory that is used by $ALG$ to compute the graph $G_{n}^{ALG} = {(V_{n}^{ALG},E_{n}^{ALG})}$. Clearly, in all algorithms discussed in this paper, the space complexity is the size of $G_{n}^{ALG}$, i.e., ${|V_{n}^{ALG}|} + {|E_{n}^{ALG}|}$. Since the number of edges is at least as much as the number of vertices in $G_{n}^{ALG}$ for all algorithms discussed in this paper, the space complexity of an algorithm, in this context, is the number edges in the graph that it returns, which was determined in the previous section.

## 5 Numerical Experiments 

This section is devoted to an experimental study of the algorithms considered in the paper. All algorithms were implemented in C and run on a computer with 2.66 GHz processor and 4GB RAM running the Linux operating system. Unless otherwise noted, total variation of a path is its cost.

A first set of experiments were run to illustrate the different performance of $k$-nearest PRM and of PRM^∗^. The $k$-nearest PRM and the PRM^∗^ algorithms were run alongside in two dimensional configuration-space and the cost of the best path in both algorithms is plotted versus the number of iterations in Figure 10. The $k$-nearest PRM does not converge to optimal solutions, unlike PRM^∗^. The performance of the PRM^∗^ algorithm is also shown in configuration spaces of dimensions up to five in Figure 11.

The main bulk of the experiments were aimed at demonstrating the performance of the RRT^∗^ algorithm, especially in comparison with its "standard" counterpart, i.e., RRT. Three problem instances were considered. In the first two, the cost function is the Euclidean path length.

The first scenario includes no obstacles. Both algorithms are run in a square environment. The trees maintained by the algorithms are shown in Figure 12 at several stages. The figure illustrates that, in this case, the RRT algorithm does not improve the feasible solution to converge to an optimum solution. On the other hand, running the RRT^∗^ algorithm further improves the paths in the tree to lower cost ones. The convergence properties of the two algorithms are also investigated in Monte-Carlo runs. Both algorithms were run for 20,000 iterations 500 times and the cost of the best path in the trees were averaged for each iteration. The results are shown in Figure 13, which shows that in the limit the RRT algorithm has cost very close to a $\sqrt{2}$ factor the optimal solution (see LaValle and Kuffner (2009) for a similar result in a deterministic setting), whereas the RRT^∗^ converges to the optimal solution. Moreover, the variance over different RRT runs approaches 2.5, while that of the RRT^∗^ approaches zero. Hence, almost all RRT^∗^ runs have the property of convergence to an optimal solution, as expected.

In the second scenario, both algorithms are run in an environment in presence of obstacles. In Figure 14, the trees maintained by the algorithms are shown after 20,000 iterations. The tree maintained by the RRT^∗^ algorithm is also shown in Figure 15 in different stages. It can be observed that the RRT^∗^ first rapidly explores the state space just like the RRT. Moreover, as the number of samples increase, the RRT^∗^ improves its tree to include paths with smaller cost and eventually discovers a path in a different homotopy class, which reduces the cost of reaching the target considerably. Results of a Monte-Carlo study for this scenario is presented in Figure 16. Both algorithms were run alongside up until 20,000 iterations 500 times and cost of the best path in the trees were averaged for each iteration. The figures illustrate that all runs of the RRT^∗^ algorithm converges to the optimum, whereas the RRT algorithm is about 1.5 of the optimal solution on average. The high variance in solutions returned by the RRT algorithm stems from the fact that there are two different homotopy classes of paths that reach the goal. If the RRT luckily converges to a path of the homotopy class that contains an optimum solution, then the resulting path is relatively closer to the optimum than it is on average. If, on the other hand, the RRT first explores a path of the second homotopy class, which is often the case for this particular scenario, then the solution that RRT converges to is generally around twice the optimum.

Finally, in the third scenario, where no obstacles are present, the cost function is selected to be the line integral of a function, which evaluates to 2 in the high cost region, 1/2 in the low cost region, and 1 everywhere else. The tree maintained by the RRT^∗^ algorithm is shown after 20,000 iterations in Figure 17. Notice that the tree either avoids the high cost region or crosses it quickly, and vice-versa for the low-cost region. (Incidentally, this behavior corresponds to the well known Snell-Descartes law for refraction of light, see Rowe and Alexander (2000) for a path-planning application.)

To compare the running time, both algorithms were run alongside in an environment with no obstacles for up to one million iterations. Figure 18, shows the ratio of the running time of RRT^∗^ and that of RRT versus the number of iterations averaged over 50 runs. As expected from the complexity analysis of Section 4.3, this ratio converges to a constant value. A similar figure is produced for the second scenario and provided in Figure 19.

The RRT^∗^ algorithm was also run in a 5-dimensional state space. The number of iterations versus the cost of the best path averaged over 100 trials is shown in Figure 20. A comparison with the RRT algorithm is provided in the same figure. The ratio of the running times of the RRT^∗^ and the RRT algorithms is provided in Figure 21. The same experiment is carried out for a 10-dimensional configuration space. The results are shown in Figure 22.

Figure 10: The cost of the best path in the k-nearest sPRM algorithm, and that in the PRM∗ algorithm are shown versus the number of iterations in simulation examples with no obstacles. The k-nearest sPRM algorithm was run for k = 5, 7, 10, 13, 15, each of which is shown separately in blue, and the PRM∗ algorithm is shown in red. The values are normalized so that the cost of the optimal path is equal to one. The iterations were stopped when the query phase of the algorithms exceeded the memory limit (approximately 4GB).

Figure 11: Cost of the best path in the PRM∗ algorithm is shown in up to 2, 3, 4, and 5 dimensional configuration spaces, in Figures (a), (b), (c), and (d), respectively. The initial condition and goal region are on opposite vertices of the unit cube (0,1)d. The obstacle region is a cube centered at (0.5,0.5,…,0.5) and has volume 0.5 in all cases.

(a)

(b)

(c)

(d)

(e)

(f)

(g)

Figure 12: A Comparison of the RRT∗ and RRT algorithms on a simulation example with no obstacles. Both algorithms were run with the same sample sequence. Consequently, in this case, the vertices of the trees at a given iteration number are the same for both of the algorithms; only the edges differ. The edges formed by the RRT algorithm are shown in (a)-(d) and (i), whereas those formed by the RRT∗ algorithm are shown in (e)-(h) and (j). The tree snapshots (a), (e) contain 250 vertices, (b), (f) 500 vertices, (c), (g) 2500 vertices, (d), (h) 10,000 vertices and (i), (j) 20,000 vertices. The goal regions are shown in magenta (in upper right). The best paths that reach the target in all the trees are highlighted with red.

(a)

Figure 13: The cost of the best paths in the RRT (shown in red) and the RRT∗ (shown in blue) plotted against iterations averaged over 500 trials in (a). The optimal cost is shown in black. The variance of the trials is shown in (b).

(a)

Figure 14: A Comparison of the RRT (shown in (a)) and RRT∗ (shown in (b)) algorithms on a simulation example with obstacles. Both algorithms were run with the same sample sequence for 20,000 samples. The cost of best path in the RRT and the RRG were 21.02 and 14.51, respectively.

(a)

(b)

(c)

Figure 15: RRT∗ algorithm shown after 500 (a), 1,500 (b), 2,500 (c), 5,000 (d), 10,000 (e), 15,000 (f) iterations.

Figure 16: An environment cluttered with obstacles is considered. The cost of the best paths in the RRT (shown in red) and the RRT∗ (shown in blue) plotted against iterations averaged over 500 trials in (a). The optimal cost is shown in black. The variance of the trials is shown in (b).

Figure 17: RRT∗ algorithm at the end of iteration 20,000 in an environment with no obstacles. The upper yellow region is the high-cost region, whereas the lower yellow region is low-cost.

Figure 18: A comparison of the running time of the RRT∗ and the RRT algorithms. The ratio of the running time of the RRT∗ over that of the RRT up until each iteration is plotted versus the number of iterations.

Figure 19: A comparison of the running time of the RRT∗ and the RRT algorithms in an environment with obstacles. The ratio of the running time of the RRT∗ over that of the RRT up until each iteration is plotted versus the number of iterations.

(a)

Figure 20: The cost of the best paths in the RRT (shown in red) and the RRT∗ (shown in blue) run in a 5 dimensional obstacle-free configuration space plotted against iterations averaged over 100 trials in (a). The optimal cost is shown in black. The variance of the trials is shown in (b).

(a)

Figure 21: The ratio of the running time of the RRT and the RRT∗ algorithms is shown versus the number of iterations.

(a)

Figure 22: The cost of the best paths in the RRT (shown in red) and the RRT∗ (shown in blue) run in a 10 dimensional configuration space involving obstacles plotted against iterations averaged over 25 trials in (a). The variance of the trials is shown in (b).

## 6 Conclusion 

This paper presented the results of a thorough analysis of sampling-based algorithms for optimal path planning. It is shown that broadly used algorithms from the literature, while probabilistically complete, are not asymptotically optimal, i.e., they will return a solution to the path planning problem with high probability if one exists, but the cost of the solution returned by the algorithm will not converge to the optimal cost as the number of samples increases. In particular, it is proven that the PRM and RRT algorithms are not asymptotically optimal. A simplified version of PRM is asymptotically optimal, but is computationally expensive. In addition, it is shown that certain heuristic versions of PRM are not only not asymptotically complete, but also not necessarily complete.

In order to address these limitations of existing algorithms, a number of new algorithms are introduced, and proven to be asymptotically optimal and computational efficient, with respect to probabilistically complete algorithms in this class. In other words, asymptotic optimality imposes only a constant factor increase in complexity with respect to probabilistic completeness. The first algorithm, called PRM^∗^, is a variant of PRM, with a variable connection radius that scales as ${\log{(n)}}/n$, where $n$ is the number of samples. In other words, the average number of connections made at each iteration is proportional to $\log{(n)}$. The second new algorithm, called RRG, incrementally builds a connected roadmap, augmenting the RRT algorithm with connections within a ball scaling as ${\log{(n)}}/n$. The third new algorithm, called RRT^∗^, is a version of RRG that incrementally builds a tree. Experimental evidence that demonstrate the effectiveness of the algorithms proposed and support the theoretical claims were also provided.

A common theme in the paper is that, in order to ensure both asymptotic optimality and computational efficiency, connections between samples should be sought within balls of radius scaling as ${\log{(n)}}/n$. If these balls shrink faster as $n$ increases, the algorithms are not asymptotically optimal (but may still be probabilistically complete); on the other hand, if these balls shrink slower, the complexity of the algorithms will suffer. On average, the proposed scaling laws will result in an average number of connections per iteration that is proportional to $\log{(n)}$. Hence, it is natural to consider variants of these algorithms that make connections to $k\hspace{0pt}{\log{(n)}}$ neighbors surely. Indeed, it is shown that these algorithms do share the same asymptotic optimality and computational efficiency properties of their counterparts, as long as $k$ is no smaller than a constant $k_{RRG}^{\ast}$. It is remarkable that this constant only depends on the dimension of the space, and is otherwise independent from the problem instance.

The analysis of the results in the paper relies on techniques used to analyze random geometric graphs. Indeed, the algorithms considered in this paper build graphs that have many characteristics in common with well known classes of random geometric graphs. Interestingly, such geometric graphs exhibit phase transition phenomena, including percolation and connectivity, for thresholds matching those found for probabilistic completeness and asymptotic optimality of sampling-based algorithms. This leads to a natural conjecture that a sampling-based path planning algorithm is probabilistically complete if and only if the underlying random geometric graph percolates, and is asymptotically optimal if and only if the underlying random geometric graph is connected.

The work presented in this paper can be extended in numerous directions. First of all, it would be of interest to establish broader connections between sampling-based path planning algorithms and random geometric graphs, e.g., by proving or disproving the conjecture above, and by possibly improving on current algorithms through a better understanding of the underlying mathematical objects. Similar analysis techniques can also be used to analyze other sampling-based path planning algorithms that were not analyzed in this paper, such as EST. In addition, it is of interest to investigate deterministic sampling-based algorithms, in which samples are generated using deterministic dense sequences of points with, e.g., low dispersion, as opposed to random sequences.

Second, it is of great practical interest to address motion planning problems subject to more complex constraints. For example, motion planning problems for mobile robots should consider the robot's dynamics, and hence differential constraints on the feasible trajectories (these are also called kino-dynamic planning problems). In addition, it is of interest to consider optimal planning problems in the presence of temporal/logic constraints on the trajectories, e.g., expressed using formal specification languages such as Linear Temporal Logic, or the $\mu$-calculus. Such constraints correspond to, e.g., rules of the road constraints for autonomous ground vehicles, mission specifications for autonomous robots, and rules of engagement in military applications. Ultimately, incremental sampling-based algorithms with asymptotic optimality properties may provide the basic elements for the on-line solution of differential games, as those arising when planning in the presence of dynamic obstacles.

Finally, it is noted that the proposed algorithms may have applications outside of the robotic motion planning domain. In fact, the class of sampling-based algorithm described in this paper can be readily extended to deal with problems described by partial differential equations, such as the eikonal equation and the Hamilton-Jacobi-Bellman equation.

## Acknowledgments 

The authors are grateful to Professors M.S. Branicky, G.J. Gordon, and S. LaValle, as well as the anonymous reviewers, for their insightful comments on draft versions of this paper. This research was supported in part by the Michigan/AFRL Collaborative Center on Control Sciences, AFOSR grant #FA 8650-07-2-3744, and by the National Science Foundation, grant CNS-1016213.

## References 

-   [Abramowitz and Stegun (1964) M. Abramowitz and I. A. Stegun, editors. *Handbook of Mathematical Functions*. Dover, 1964.]
-   [Alterovitz et al. (2011) R. Alterovitz, S. Patil, and A. Derbakova. Rapidly-exploring roadmaps: Weighing exploration vs. reginement in optimal motion planning. In *IEEE Conference on Robotics and Automation (ICRA)*, 2011.]
-   [Arya and Mount (2000) S. Arya and D. M. Mount. Approximate range searching. *Computational Geometry: Theory and Applications*, 17:135--163, 2000.]
-   [Arya et al. (1999) S. Arya, D. M. Mount, R. Silverman, and A. Y. Wu. An optimal algorithm for approximate nearest neighbor search in fixed dimensions. *Journal of the ACM*, 45(6):891--923, November 1999.]
-   [Arya et al. (2005) S. Arya, T. Malamatos, and D. M. Mount. Space-time tradeoffs for approximate spherical range counting. In *Symposium on Discrete Algorithms*, 2005.]
-   [Balister et al. (2005) P. Balister, B. Bollobás, A. Sarkar, and M. Walters. Connectivity of random $k$-nearest neighbour graphs. *Advances in Applied Probability*, 37:1--24, 2005.]
-   [Balister et al. (2009a) P. Balister, B. Bollobás, and A. Sarkar. Percolation, connectivity, coverage and colouring of random geometric graphs. In B. Bollobás, R. Kozma, and D. Miklós, editors, *Handbook of Large-Scale Random Networks*, volume 18 of *Bolyai Society Mathematical Studies*, chapter 2, pages 117--142. Springer, 2009a.]
-   [Balister et al. (2009b) P. Balister, B. Bollobás, A. Sarkar, and M. Walters. A critical constant for the $k$ nearest-neighbour model. *Advances in Applied Probability*, 41(1):1--12, 2009b.]
-   [Barraquand and Latombe (1993) J. Barraquand and J. C. Latombe. Robot motion planning: A distributed representation approach. *International Journal of Robotics Research*, 10(6):628--649, 1993.]
-   [Barraquand et al. (1997) J. Barraquand, L. E. Kavraki, J. C. Latombe, T. Li, R. Motwani, and P. Raghavan. A random sampling scheme for path planning. *International Journal of Robotics Research*, 16:759--774, 1997.]
-   [Berenson et al. (2008) D. Berenson, J. Kuffner, and H. Choset. An optimization approach to planning for mobile manipulation. In *IEEE International Conference on Robotics and Automation*, 2008.]
-   [Berenson et al. (2011) D. Berenson, T. Simeon, and S. Srinivasa. Addressing cost-space chasms in manipulation planning. In *IEEE Conference on Robotics and Automation (ICRA)*, 2011.]
-   [Bhatia and Frazzoli (2004) A. Bhatia and E. Frazzoli. Incremental search methods for reachability analysis of continuous and hybrid systems. In R. Alur and G.J. Pappas, editors, *Hybrid Systems: Computation and Control*, number 2993 in Lecture Notes in Computer Science, pages 142--156. Springer-Verlag, Philadelphia, PA, March 2004.]
-   [Bollobás (2001) B. Bollobás. *Random Graphs*. Cambridge University Press, second edition, 2001.]
-   [Bollobás and Riordan (2006) B. Bollobás and O. M. Riordan. *Percolation*. Cambridge University Press, 2006.]
-   [Branicky et al. (2001) M. S. Branicky, S. M. LaValle, K. Olson, and L. Yang. Quasi-randomized path planning. In *IEEE Conference on Robotics and Automation*, 2001.]
-   [Branicky et al. (2003) M. S. Branicky, M. M. Curtis, J. A. Levine, and S. B. Morgan. RRTs for nonlinear, discrete, and hybrid planning and control. In *IEEE Conference on Decision and Control*, 2003.]
-   [Branicky et al. (2006) M. S. Branicky, M. M. Curtis, J. Levine, and S. Morgan. Sampling-based planning, control, and verification of hybrid systems. *IEEE Proc. Control Theory and Applications*, 153(5):575--590, Sept. 2006.]
-   [Brooks and Lozano-Perez (1983) R. Brooks and T. Lozano-Perez. A subdivision algorithm in configuration space for findpath with rotation. In *International Joint Conference on Artificial Intelligence*, 1983.]
-   [Bruce and Veloso (2003) J. Bruce and M.M. Veloso. *Real-Time Randomized Path Planning for Robot Navigation*, volume 2752 of *Lecture Notes in Computer Science*, chapter RoboCup 2002: Robot Soccer World Cup VI, pages 288--295. Springer, 2003.]
-   [Bry and Roy (2011) A. Bry and N. Roy. Rapidly-exploring random belief trees for motion planning under uncertainty. In *IEEE Conference on Robotics and Automation (ICRA)*, 2011.]
-   [Canny (1988) J. Canny. *The Complexity of Robot Motion Planning*. MIT Press, 1988.]
-   [Canny and Reif (1987) J. Canny and J. H. Reif. New lower bound techniques for robot motion planning problems. In *IEEE Symposium on Foundations of Computer Science (FoCS)*, pages 49--60, Los Angeles, CA, 1987.]
-   [Chanzy et al. (2001) P. Chanzy, L. Devroye, and C. Zamora-Cura. Analysis of range search for random k-d trees. *Acta Informatica*, 37:355--383, 2001.]
-   [Choset et al. (2005) H. Choset, K.M. Lynch, S. Hutchinson, G. Kantor, W. Burgard, L.E. Kavraki, and S. Thrun. *Principles of Robot Motion: Theory, Algorithms, and Implementations*. MIT Press, Boston, MA, 2005.]
-   [Cortes et al. (2007) J. Cortes, L. Jailet, and T. Simeon. Molecular disassembly with RRT-like algorithms. In *IEEE International Conference on Robotics and Automation (ICRA)*, 2007.]
-   [Dolgov et al. (2009) D. Dolgov, S. Thrun, M. Montemerlo, and J. Diebel. *Experimental Robotics*, chapter Path Planning for Autonomous Driving in Unknown Environments, pages 55--64. Springer, 2009.]
-   [Dubhashi and Panconesi (2009) D. P. Dubhashi and A. Panconesi. *Concentration of Measure for the Analysis of Randomized Algorithms*. Cambridge University Press, 2009.]
-   [Edelsbrunner and Maurer (1981) H. Edelsbrunner and H. A. Maurer. On the intersection of orthogonal objects. *Information Processing Letters*, 13(4,5):177--181, April 1981.]
-   [Eppstein et al. (1997) D Eppstein, MS Paterson, and F F Yao. On nearest-neighbor graphs. *Discrete and Computational Geometry*, 17:263--282, Jan 1997. URL [http://www.springerlink.com/index/RM3FJ00T9AD4WBX9.pdf](http://www.springerlink.com/index/RM3FJ00T9AD4WBX9.pdf).]
-   [Ferguson and Stentz (2006) D. Ferguson and A. Stentz. Anytime RRTs. In *Proceedings of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*, 2006.]
-   [Finn and Kavraki (1999) P. W. Finn and L. E. Kavraki. Computational approaches to drug design. *Algorithmica*, 25:347--371, 1999.]
-   [Frazzoli et al. (2002) E. Frazzoli, M. A. Dahleh, and E. Feron. Real-time motion planning for agile autonomous vehicles. *Journal of Guidance, Control, and Dynamics*, 25(1):116--129, 2002.]
-   [Ge and Cui (2002) S. S. Ge and Y.J. Cui. Dynamic motion planning for mobile robots using potential field method. *Autonomous Robots*, 13(3):207--222, 2002.]
-   [Gilbert (1961) E. N. Gilbert. Random plane networks. *J. Soc. Indust. Appl. Math.*, 9(4):533--543, 1961.]
-   [Grimmett and Stirzaker (2001) G. Grimmett and D. Stirzaker. *Probability and Random Processes*. Oxford University Press, Third edition, 2001.]
-   [Gupta and Kumar (1998) P. Gupta and P. R. Kumar. Critical power for asymptotic connectivity in wireless networks. In W. M. McEneany, G. Yin, and Q. Zhang, editors, *Stochastic Analysis, Control, Optimization and Applications: A Volume in Honor of W.H. Fleming*, pages 547--566. Birkhäuser, Boston, MA, 1998.]
-   [Gupta and Kumar (2000) P. Gupta and P. R. Kumar. The capacity of wireless networks. *IEEE Trans. on Information Theory*, 46:388--404, 2000.]
-   [Henze (1987) N. Henze. On the fraction of points with specified nearest-neighbour interrelations and degree of attraction. *Advances in Applied Probability*, 19:873--895, 1987.]
-   [Hopcroft et al. (1983) J.E. Hopcroft, J.T. Schwartz, and M. Sharir. Efficient detection of intersections among spheres. *Int. Journal of Robotics Research*, 2:77--80, 1983.]
-   [Hsu et al. (1997) D. Hsu, J. C. Latombe, and R. Motwani. Path planning in expansive configuration spaces. In *IEEE Conference on Robotics and Automation*, 1997.]
-   [Hsu et al. (1999) D. Hsu, J. C. Latombe, and R. Motwani. Path planning in expansive configuration spaces. *Int. J. of Computational Geometry and Applications*, 9(4&5):495--512, 1999.]
-   [Hsu et al. (2002) D. Hsu, R. Kindel, J. C. Latombe, and S. Rock. Randomized kinodynamic motion planning with moving obstacles. *International Journal of Robotics Research*, 21(3):233--255, 2002.]
-   [Hsu et al. (2006) D. Hsu, J. C. Latombe, and H. Kurniawati. On the probabilistic foundations of probabilistic roadmap planning. *International Journal of Robotics Research*, 25:7, 2006.]
-   [Jaillet et al. (2010) L. Jaillet, J. Cortes, and T .Simeon. Sampling-based path planning on configuration-space costmaps. *IEEE Transactions on Robotics*, 26(4):635--646, August 2010.]
-   [Karaman and Frazzoli (2010a) S. Karaman and E. Frazzoli. Optimal kinodynamic motion planning using incremental sampling-based methods. In *IEEE Conf. on Decision and Control*, 2010a.]
-   [Karaman and Frazzoli (2010b) S. Karaman and E. Frazzoli. Incremental sampling-based algorithms for optimal motion planning. In *Robotics: Science and Systems (RSS)*, 2010b.]
-   [Karaman and Frazzoli (2010c) S. Karaman and E. Frazzoli. Incremental sampling-based algorithms for a class of pursuit-evasion games. In *Workshop on Algorithmic Foundations of Robotics (WAFR)*, pages 71--87, 2010c.]
-   [Karaman et al. (2011) S. Karaman, M. Walter, A. Perez, E. Frazzoli, and S. Teller. Anytime motion planning using the RRT^∗^. In *IEEE Conference on Robotics and Automation (ICRA)*, 2011.]
-   [Kavraki and Latombe (1994) L. Kavraki and J. C. Latombe. Randomized preprocessing of configuration space for fast path planning. In *IEEE International Conference on Robotics and Automation*, 1994.]
-   [Kavraki et al. (1996) L. E. Kavraki, P. Svestka, J. C. Latombe, and M. H. Overmars. Probabilistic roadmaps for path planning in high-dimensional configuration spaces. *IEEE Transactions on Robotics and Automation*, 12(4):566--580, 1996.]
-   [Kavraki et al. (1998) L. E. Kavraki, M. N. Kolountzakis, and J. C. Latombe. Analysis of probabilistic roadmaps for path planning. *IEEE Transactions on Roborics and Automation*, 14(1):166--171, 1998.]
-   [Khatib (1986) O. Khatib. Real-time obstacle avoidance for manipulators and mobile robots. *International Journal of Robotics Research*, 5(1):90--98, 1986.]
-   [Koren and Borenstein (1991) Y. Koren and J. Borenstein. Potential field methods and their inherent limitations for mobile robot navigation. In *IEEE Conference on Robotics and Automation*, 1991.]
-   [Koyuncu et al. (2010) E. Koyuncu, N.K. Ure, and G. Inalhan. Integration of path/manuever planning in complex environments for agile maneuvering UCAVs. *Jounal of Intelligent and Robotic Systems*, 57(1--4):143--170, 2010.]
-   [Kuffner and LaValle (2000) J. J. Kuffner and S. M. LaValle. RRT-connect: An efficient approach to single-quert path planning. In *Proceedings of the IEEE International Conference on Robotics and Automation*, 2000.]
-   [Kuffner et al. (2002) J. J. Kuffner, S. Kagami, K. Nishiwaki, M. Inaba, and H. Inoue. Dynamically-stable motion planning for humanoid robots. *Autonomous Robots*, 15:105--118, 2002.]
-   [Kuwata et al. (2009) Y. Kuwata, J. Teo, G. Fiore, S. Karaman, E. Frazzoli, and J.P. How. Real-time motion planning with applications to autonomous urban driving. *IEEE Transactions on Control Systems*, 17(5):1105--1118, 2009.]
-   [Ladd and Kavraki (2004) A. L. Ladd and L. Kavraki. Measure theoretic analysis of probabilistic path planning. *IEEE Transactions on Robotics and Automation*, 20(2):229--242, 2004.]
-   [Latombe (1991) J. C. Latombe. *Robot Motion Planning*. Kluwer Academic Publishers, Boston, MA, 1991.]
-   [Latombe (1999) J. C. Latombe. Motion planning: A journey of robots, molecules, digital actors, and other artifacts. *International Journal of Robotics Research*, 18(11):1119--1128, 1999.]
-   [LaValle (2006) S. M. LaValle. *Planning Algorithms*. Cambridge University Press, 2006.]
-   [LaValle and Kuffner (2001) S. M. LaValle and J. J. Kuffner. Randomized kinodynamic planning. *International Journal of Robotics Research*, 20(5):378--400, May 2001.]
-   [LaValle and Kuffner (2009) S. M. LaValle and J. J. Kuffner. Space filling trees. Technical Report CMU-RI-TR-09-47, Carnegie Mellon University, The Robotics Institute, 2009.]
-   [LaValle et al. (2004) S. M. LaValle, M. S. Branicky, and S. R. Lindemann. On the relationship between classical grid search and probabilistic roadmaps. *International Journal of Robotics Research*, 23(7--8):673--692, 2004.]
-   [Lee and Wong (1977) D. T. Lee and C. K. Wong. Worst-case analysis for region and partial region searches in multidimensional binary search trees and quad trees. *Acta Informatica*, 9:23--29, 1977.]
-   [Likhachev and Ferguson (2009) M. Likhachev and D. Ferguson. Planning long dynamically-feasible maneuvers for autonomous vehicles. *International Journal of Robotics Research*, 28(8):933--945, 2009.]
-   [Likhachev et al. (2004) M. Likhachev, G. Gordon, and S. Thrun. Anytime A\* with provable bounds on sub-optimality. In *Advances in Neural Information Processing Systems*, 2004.]
-   [Likhachev et al. (2008) M. Likhachev, D. Ferguson, G. Gordon, A. Stentz, and S. Thrun. Anytime search in dynamic graphs. *Artificial intelligence Journal*, 172(14):1613--1643, 2008.]
-   [Lin and Manocha (2004) M. C. Lin and D. Manocha. Collision and proximity queries. In J.E. Goodman and J. O'Rourke, editors, *Handbook of Discrete and Computational Geometry*. Chapman and Hall/CRC, second edition, 2004.]
-   [Lindemann and LaValle (2005) S. R. Lindemann and S. M. LaValle. Current issues in sampling-based motion planning. In P. Dario and R. Chatila, editors, *Eleventh International Symposium on Robotics Research*, pages 36--54. Springer, 2005.]
-   [Liu and Badler (2003) Y. Liu and N.I. Badler. Real-time reach planning for animated characters using hardware acceleration. In *IEEE International Conference on Computer Animation and Social Characters*, pages 86--93, 2003.]
-   [Lozano-Perez and Wesley (1979) T. Lozano-Perez and M. A. Wesley. An algorithm for planning collision-free paths among polyhedral obstacles. *Communications of the ACM*, 22(10):560--570, 1979.]
-   [Luders et al. (2010) B. Luders, S. Karaman, E. Frazzoli, and J. P. How. Bounds on tracking error using closed-loop rapidly-exploring random trees. In *American Control Conference*, 2010.]
-   [Meester and Roy (1996) R. Meester and R. Roy. *Continuum Percolation*. Cambridge University Press, 1996.]
-   [Munkres (2000) J. R. Munkres. *Topology*. Prentice Hall, second edition, 2000.]
-   [Nechushtan et al. (2010) O. Nechushtan, B. Raveh, and D. Halperin. Sampling-diagram automata: a tool for analyzing path quality in tree planners. In D. Hsu, V. Isler, J. C. Latombe, and M.C. Lin, editors, *Algorithmic Foundations of Robotics IX*, volume 68 of *Springer tracts in advanced robotics*, pages 285--301. Springer, 2010.]
-   [Niederreiter (1992) H. Niederreiter. *Random Number Generation and Quasi-Monte-Carlo Methods*. Society for Industrial and Applied Mathematics, 1992.]
-   [Penrose (2003) M. D. Penrose. *Random Geometric Graphs*. Oxford University Press, 2003.]
-   [Plaku and Kavraki (2008) E. Plaku and L. E. Kavraki. Quantitative analysis of nearest-neighbors search in high-dimensional sampling-based motion planning. In *Workshop on Algorithmic Foundations of Robotics (WAFR)*, 2008.]
-   [Plaku et al. (2005) E. Plaku, K.E. Bekris, B.Y. Chen, A.M. Ladd, and L.E. Kavraki. Sampling-based roadmap of trees for parallel motion planning. *IEEE Transactions on Robotics*, 21:597--608, 2005.]
-   [Prentice and Roy (2009) S. Prentice and N. Roy. The belief roadmap: Efficient planning in blief space by factoring the covariance. *International Journal of Robotics Research*, 28(11--12):1448--1465, 2009.]
-   [Quintanilla et al. (2000) J. Quintanilla, S. Torquato, and R.M. Ziff. Efficient measurement of the percolation threshold for fully penetrable discs. *Journal of Physics A*, 33(42):L399--L407, 2000.]
-   [Reif (1979) J. H. Reif. Complexity of the mover's problem and generalizations. In *Proceedings of the IEEE Symposium on Foundations of Computer Science*, 1979.]
-   [Resnick (1999) S. I. Resnick. *A probability path*. Birkhäuser, 1999.]
-   [Rimon and Koditschek (1992) E. Rimon and D. E. Koditschek. Exact robot navigation using artificial potential fields. *IEEE Transactions on Robotics and Automation*, 8(5):501--518, 1992.]
-   [Rowe and Alexander (2000) N. C. Rowe and R. S. Alexander. Finding optimal-path maps for path planning across weighted regions. *The International Journal of Robotics Research*, 19:83--95, 2000.]
-   [Sahimi (1994) M. Sahimi. *Applications of Percolation Theory*. Taylor & Francis, 1994.]
-   [Samet (1989a) H. Samet. *Design and Analysis of Spatial Data Structures*. Addison-Wesley, 1989a.]
-   [Samet (1989b) H. Samet. *Applications of Spatial Data Structures: Computer Graphics, Image Processesing and Gis*. Addison-Wesley, 1989b.]
-   [Schrijver (2003) A. Schrijver. *Combinatorial Optimization*, volume A. Springer, 2003.]
-   [Schwartz and Sharir (1983) J. T. Schwartz and M. Sharir. On the 'piano movers' problem: II. general techniques for computing topological properties of real algebraic manifolds. *Advances in Applied Mathematics*, 4:298--351, 1983.]
-   [Shkolnik et al. (2011) A. Shkolnik, M. Levashov, I. R. Manchester, and R. Tedrake. Bounding on rough terrain with the LittleDog robot. Submitted for publication, 2011.]
-   [Six and Wood (1982) H. Six and D. Wood. Counting and reporting intersections of D-ranges. *IEEE Trans. on Computers*, pages 46--55, 1982.]
-   [Stentz (1995) D. Stentz. The focussed D\* algorithm for real-time replanning. In *International Joint Conference on Artificial Intelligence*, 1995.]
-   [Stilman et al. (2007) M. Stilman, J. Schamburek, J. Kuffner, and T. Asfour. Manipulation planning among movable obstacles. In *IEEE International Conference on Robotics and Automation*, 2007.]
-   [Stoyan et al. (1995) D. Stoyan, W. S. Kendall, and J. Mecke. *Stochastic Geometry and Its Applications*. John Wiley & Sons, 1995.]
-   [Tedrake et al. (2010) R. Tedrake, I. R. Manchester, M. M. Tobekin, and J. W. Roberts. LQR-trees: Feedback motion planning via sums of squares verification. *International Journal of Robotics Research (to appear)*, 2010.]
-   [Teller et al. (2010) S. Teller, M. R. Walter, M. Antone, A. Correa, R. Davis, L. Fletcher, E. Frazzoli, J. Glass, J.P. How, A. S. Huang, J. Jeon, S. Karaman, B. Luders, N. Roy, and T. Sainath. A voice-commandable robotic forklift working alongside humans in minimally-prepared outdoor environments. In *IEEE International Conference on Robotics and Automation*, 2010.]
-   [Urmson and Simmons (2003) C. Urmson and R. Simmons. Approaches for heuristically biasing RRT growth. In *Proceedings of the IEEE/RSJ International Conference on Robotics and Systems (IROS)*, 2003.]
-   [Wade (2007) A. R. Wade. Explicit laws of large numbers for random nearest-neighbor-type graphs. *Advances in Applied Probability*, 39:326--342, 2007.]
-   [Wade (2009) A. R. Wade. Asymptotic theory for the multidimensional random on-line nearest-neighbour graph. *Stochastic Processes and their Applications*, 119(6):1889--1911, 2009.]
-   [Wedge and Branicky (2008) N. A. Wedge and M.S. Branicky. On heavy-tailed runtimes and restarts in rapidly-exploring random trees. In *Twenty-third AAAI Conference on Artificial Intelligence*, 2008.]
-   [Xue and Kumar (2004) F. Xue and P. R. Kumar. The number of neighbors needed for connectivity of wireless networks. *Wireless Networks*, 10:169--181, 2004.]
-   [Yershova and LaValle (2007) A. Yershova and S. M. LaValle. Improving motion-planning algorithms by efficient nearest-neighbor searching. *IEEE Transactions on Robotics*, 23(1):151--157, 2007.]
-   [Yershova and LaValle (2008) A. Yershova and S. M. LaValle. Motion planning in highly constrained spaces. Technical report, University of Illinois at Urbana-Champaign, 2008.]
-   [Zucker et al. (2007) M. Zucker, J. J. Kuffner, and M. S. Branicky. Multiple RRTs for rapid replanning in dynamic environments. In *IEEE Conference on Robotics and Automation*, 2007.]

## Appendix 

## Appendix A Notation 

Let $\mathbb{N}$ denote the set of positive integers and $\mathbb{R}$ denote the set of reals. Let ${\mathbb{N}}_{0} = {{\mathbb{N}} \cup {\{ 0\}}}$, and ${\mathbb{R}}_{> 0}$, ${\mathbb{R}}_{\geq 0}$ denote the sets of positive and non-negative reals, respectively. A sequence on a set $A$ is a mapping from $\mathbb{N}$ to $A$, denoted as ${\{ a_{i}\}}_{i \in {\mathbb{N}}}$, where $a_{i} \in A$ is the element that $i \in {\mathbb{N}}$ is mapped to. Given ${a,b} \in {\mathbb{R}}$, closed and open intervals between $a$ and $b$ are denoted by $\lbrack a,b\rbrack$ and $(a,b)$, respectively. The Euclidean norm is denoted by $\parallel \cdot \parallel$. Given a set $\mathcal{X} \subset {\mathbb{R}}^{d}$, the closure of $\mathcal{X}$ is denoted by ${cl}{(\mathcal{X})}$. The closed ball of radius $r > 0$ centered at $x \in {\mathbb{R}}^{d}$, i.e., , i.e., $\left. \{{y \in {\mathbb{R}}^{d}} \middle| {{\|{y - x}\|} \leq r}\} \right.$, is denoted as $\mathcal{B}_{x,r}$; $\mathcal{B}_{x,r}$ is also called the $r$-ball centered at $x$. Given a set $\mathcal{X} \subseteq {\mathbb{R}}^{d}$, the Lebesgue measure of $X$ is denoted by $\mu\hspace{0pt}{(\mathcal{X})}$. The Lebesgue measure of a set is also referred to as its volume. The volume of the unit ball in ${\mathbb{R}}^{d}$, is denoted by $\zeta_{d}$, i.e., $\zeta_{d} = {\mu\hspace{0pt}{(\mathcal{B}_{0,1})}}$. The letter $e$ is used to denote the base of the natural logarithm, also called Euler's number.

Given a probability space $(\Omega,\mathcal{F},{\mathbb{P}})$, where $\Omega$ is a sample space, $\mathcal{F} \subseteq 2^{\Omega}$ is a $\sigma -$algebra, and $\mathbb{P}$ is a probability measure, an event $A$ is an element of $\mathcal{F}$. The complement of an event $A$ is denoted by $A^{c}$. Given a sequence of events ${\{ A_{n}\}}_{n \in {\mathbb{N}}}$, the event $\cap_{n = 1}^{\infty} \cup_{i = n}^{\infty}A_{i}$ is denoted by $\operatorname{lim\ sup}_{n\rightarrow\infty}A_{n}$ (also called the event that $A_{n}$ occurs infinitely often); the event $\cup_{n = 1}^{\infty} \cap_{i = n}^{\infty}A_{i}$ is denoted by $\operatorname{lim\ inf}_{n\rightarrow\infty}A_{n}$. A (real) random variable is a measurable function that maps $\Omega$ into $\mathbb{R}$. An extended (real) random variable can also take the values $\pm \infty$. The expected value of a random variable $Y$ is ${{\mathbb{E}}\hspace{0pt}{\lbrack Y\rbrack}} = {\int_{\Omega}{Y\hspace{0pt}{d{\mathbb{P}}}}}$. A sequence of random variables ${\{ Y_{n}\}}_{n \in {\mathbb{N}}}$ is said to converge surely to a random variable $Y$ if ${\lim_{n\rightarrow\infty}{Y_{n}\hspace{0pt}{(\omega)}}} = {Y\hspace{0pt}{(\omega)}}$ for all $\omega \in \Omega$; the sequence is said to converge almost surely if ${{\mathbb{P}}\hspace{0pt}{({\{{{\lim_{n\rightarrow\infty}Y_{n}} = Y}\}})}} = 1$. Finally, if $\varphi\hspace{0pt}{(\omega)}$ is a property that is either true or false for a given $\omega \in \Omega$, the event that denotes the set of all samples $\omega$ for which $\varphi\hspace{0pt}{(\omega)}$ holds, i.e., $\left. \{{\omega \in \Omega} \middle| {\varphi\hspace{0pt}{(\omega)}\hspace{0pt}\text{~holds}}\} \right.$, is written as $\{\varphi\}$, e.g., $\left. \{{\omega \in \Omega} \middle| {{\lim_{n\rightarrow\infty}{Y_{n}\hspace{0pt}{(\omega)}}} = {Y\hspace{0pt}{(\omega)}}}\} \right.$ is simply written as $\{{{\lim_{n\rightarrow\infty}Y_{n}} = Y}\}$. The Poisson random variable with parameter $\lambda$ is denoted by ${Poisson}\hspace{0pt}{(\lambda)}$. The binomial random variable with parameters $n$ and $p$ is denoted by ${Binomial}\hspace{0pt}{(n,p)}$.

Let $f\hspace{0pt}{(n)}$ and $g\hspace{0pt}{(n)}$ be two functions with domain and range $\mathbb{N}$ or $\mathbb{R}$. The function $f\hspace{0pt}{(n)}$ is said to be $O\hspace{0pt}{({g\hspace{0pt}{(n)}})}$, denoted as ${f\hspace{0pt}{(n)}} \in {O\hspace{0pt}{({g\hspace{0pt}{(n)}})}}$, if there exists two constants $M$ and $n_{0}$ such that ${f\hspace{0pt}{(n)}} \leq {M\hspace{0pt}g\hspace{0pt}{(n)}}$ for all $n \geq n_{0}$. The function $f\hspace{0pt}{(n)}$ is said to be $\Omega\hspace{0pt}{({g\hspace{0pt}{(n)}})}$, denoted as ${f\hspace{0pt}{(n)}} \in {\Omega\hspace{0pt}{({g\hspace{0pt}{(n)}})}}$, if there exists constants $M$ and $n_{0}$ such that ${f\hspace{0pt}{(n)}} \geq {M\hspace{0pt}g\hspace{0pt}{(n)}}$ for all $n \geq n_{0}$. The function $f\hspace{0pt}{(n)}$ is said to be $\Theta\hspace{0pt}{({g\hspace{0pt}{(n)}})}$, denoted as ${f\hspace{0pt}{(n)}} \in {\Theta\hspace{0pt}{({g\hspace{0pt}{(n)}})}}$, if ${f\hspace{0pt}{(n)}} \in {O\hspace{0pt}{({g\hspace{0pt}{(n)}})}}$ and ${f\hspace{0pt}{(n)}} \in {\Omega\hspace{0pt}{({g\hspace{0pt}{(n)}})}}$.

Let $\mathcal{X}$ be a subset of ${\mathbb{R}}^{d}$. A (directed) graph $G = {(V,E)}$ on $\mathcal{X}$ is composed of a vertex set $V$ and an edge set $E$, such that $V$ is a finite subset of $\mathcal{X}$, and $E$ is a subset of $V \times V$. A directed path on $G$ is a sequence $(v_{1},v_{2},\ldots,v_{n})$ of vertices such that ${(v_{i},v_{i + 1})} \in E$ for all $1 \leq i \leq {n - 1}$. Given a vertex $v \in V$, the sets $\left. \{{u \in V} \middle| {{(u,v)} \in E}\} \right.$ and $\left. \{{u \in V} \middle| {{(v,u)} \in E}\} \right.$ are said to be its incoming neighbors and outgoing neighbors, respectively. A (directed) tree is a directed graph, in which each vertex but one has a unique incoming neighbor; the vertex with no incoming neighbor is called the root vertex. Vertices of a tree are often also called nodes.

## Appendix B Proof of Theorem 33 ‣ Rapidly-exploring Random Trees ‣ 4.2.1 Existing algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning") (Non-optimality of RRT) 

For simplicity, the theorem will be proven assuming that (i) the environment contains no obstacles, i.e., $\mathcal{X}_{free} = {\lbrack 0,1\rbrack}^{d}$, and (ii) the parameter $\eta$ of the steering procedure is set large enough, e.g., $\eta \geq {{diam}\hspace{0pt}\left( \mathcal{X}_{free} \right)} = \sqrt{d}$. One one hand, considering this case is enough to prove that the RRT algorithm is not asymptotically optimal, as it demonstrates a case for which the RRT algorithm fails to converge to an optimal solution, although the problem instance is clearly robustly optimal. On the other hand, these assumptions are not essential, and the claims extend to the more general case, but the technical details of the proof are considerably more complicated.

The proof can be outlined as follows. Order the vertices in the RRT according to the iteration at which they are added to the tree. The set of vertices that contains the $k$-th child of the root along with all its descendants in the tree is called the $k$-th branch of the tree. First, it is shown that a necessary condition for the asymptotic optimality of RRT is that infinitely many branches of the tree contain vertices outside a small ball centered at the initial condition. Then, the RRT algorithm is shown to violate this condition, with probability one.

### B.1 A necessary condition 

First, we provide a necessary condition for the RRT algorithm to be asymptotically optimal.

###### Lemma 44 

Let $0\hspace{0pt}{<{{R\hspace{0pt}{<\inf_{y \in \mathcal{X}_{goal}}\parallel}\hspace{0pt}y} - x_{init}}\parallel}$. The event $\{{{\lim_{N\rightarrow\infty}Y_{n}^{RRT}} = c^{\ast}}\}$ occurs only if the $k$-th branch of the RRT contains vertices outside the $R$-ball centered at $x_{init}$ for infinitely many $k$.

###### Proof. 

Let $\{ x_{1},x_{2},\ldots\}$ denote the set of children to the root vertex in the order they are added to the tree. Let $\Gamma\hspace{0pt}{(x_{k})}$ denote the optimal cost of a path starting from the root vertex, passing through $x_{k}$, and reaching the goal region. By our assumption that the measure of the set of all points that are on the optimal path is zero (see Assumption 27 and Lemma 28), the probability that ${\Gamma\hspace{0pt}{(x_{k})}} = c^{\ast}$ is zero for all $k \in {\mathbb{N}}$. Hence,

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( {\bigcup_{k \in {\mathbb{N}}}\left\{ {{\Gamma\hspace{0pt}{(x_{k})}} = c^{\ast}} \right\}} \right)} \leq {\sum\limits_{k = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}\left( {\{{{\Gamma\hspace{0pt}{(x_{k})}} = c^{\ast}}\}} \right)}} = 0}.$$   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Let $A_{k}$ denote the event that at least one vertex in the $k$-th branch of the tree is outside the ball of radius $R$ centered at $x_{init}$ in some iteration of the RRT algorithm. Consider the case when the event $\{{\operatorname{lim\ sup}_{k\rightarrow\infty}A_{k}}\}$ does not occur and the events $\{{{\Gamma\hspace{0pt}{(x_{k})}} > c^{\ast}}\}$ occur for all $k \in {\mathbb{N}}$. Then, $A_{k}$ occurs for only finitely many $k$. Let $K$ denote the largest number such that $A_{K}$ occurs. Then, the cost of the best path in the tree is at least $\sup\left. \{{\Gamma\hspace{0pt}{(x_{k})}} \middle| {k \in {\{ 1,2,\ldots,K\}}}\} \right.$, which is strictly larger than $c^{\ast}$, since $\{{{\Gamma\hspace{0pt}{(x_{k})}} > c^{\ast}}\}$ for all finite $k$. Thus, ${\lim_{n\rightarrow\infty}Y_{n}^{RRT}} > c^{\ast}$ must hold. That is, we have argued that

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\left( {\operatorname{lim\ sup}\limits_{k\rightarrow\infty}A_{k}} \right)^{c} \cap \left( {\bigcap\limits_{k \in {\mathbb{N}}}{\{{{\Gamma\hspace{0pt}{(x_{k})}} > c^{\ast}}\}}} \right)} \subseteq \left\{ {{\lim\limits_{n\rightarrow\infty}Y_{n}^{RRT}} > c^{\ast}} \right\}}.$$   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Taking the complement of both sides and using monotonicity of probability measures,

  -- ---------------------------------------------------------------------------------------------------------------------- -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     ${\mathbb{P}}\hspace{0pt}\left( \left\{ {{\lim\limits_{n\rightarrow\infty}Y_{n}^{RRT}} = c^{\ast}} \right\} \right)$   $\leq$   ${{\mathbb{P}}\hspace{0pt}\left( {\left( {\operatorname{lim\ sup}\limits_{k\rightarrow\infty}A_{k}} \right) \cup \left( {\bigcup_{k \in {\mathbb{N}}}{\{{{\Gamma\hspace{0pt}{(x_{k})}} = c^{\ast}}\}}} \right)} \right)},$           
                                                                                                                            $\leq$   ${{{\mathbb{P}}\hspace{0pt}\left( {\operatorname{lim\ sup}\limits_{k\rightarrow\infty}A_{k}} \right)} + {{\mathbb{P}}\hspace{0pt}\left( {\bigcup_{k \in {\mathbb{N}}}{\{{{\Gamma\hspace{0pt}{(x_{k})}} = c^{\ast}}\}}} \right)}},$   
  -- ---------------------------------------------------------------------------------------------------------------------- -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

where the last inequality follows from the union bound. The lemma follows from the fact that the last term in the right hand side is equal to zero as shown above. ∎∎

### B.2 Length of the first path in a branch 

The following result provides a useful characterization of the RRT structure.

###### Lemma 45 

Let $U = {\{ X_{1},X_{2},\ldots,X_{n}\}}$ be a set of independently sampled and uniformly distributed points in the $d$-dimensional unit cube, ${\lbrack 0,1\rbrack}^{d}$. Let $X_{n + 1}$ be a point that is sampled independently from all the other points according to the uniform distribution on ${\lbrack 0,1\rbrack}^{d}$. Then, the probability that among all points in $U$ the point $X_{i}$ is the one that is closest to $X_{n + 1}$ is $1/n$, for all $i \in {\{ 1,2,\ldots,n\}}$. Moreover, the expected distance from $X_{n + 1}$ to its nearest neighbor in $U$ is $n^{- {1/d}}$.

###### Proof. 

Since the probability distribution is uniform, the probability that $X_{n + 1}$ is closest to $X_{i}$ is the same for all $i \in {\{ 1,2,\ldots,n\}}$, which implies that this probability is equal to $1/n$. The expected distance to the closest point in $U$ is an application of the order statistics of the uniform distribution. ∎∎

An immediate consequence of this result is that each vertex of the RRT has unbounded degree, almost surely, as the number of samples approaches infinity.

One can also define a notion of infinite paths in the RRT, as follows. Let $\Lambda$ be the set of infinite sequences of natural numbers $\alpha = {(\alpha_{1},\alpha_{2},\ldots)}$. For any $i \in {\mathbb{N}}$, let $\pi_{i}:{{\Sigma\rightarrow{\mathbb{N}}^{i}},{{(\alpha_{1},\alpha_{2},\ldots,\alpha_{i},\ldots)}\mapsto{(\alpha_{1},\alpha_{2},\ldots,\alpha_{i})}}}$, be a function returning the prefix of length $i$ of an infinite sequence in $\Lambda$. The lexicographic ordering of $\Lambda$ is such that, given ${\alpha,\beta} \in \Sigma$, $\alpha \leq \beta$ if and only if there exists $j \in {\mathbb{N}}$ such that $\alpha_{i} = \beta_{i}$ for all $i \in {\mathbb{N}}$, $i \leq {j - 1}$, and $\alpha_{j} \leq \beta_{j}$. This is a total ordering of $\Lambda$, since $\mathbb{N}$ is a totally ordered set. Given $\alpha \in \Lambda$ and $i \in {\mathbb{N}}$, let $\mathcal{L}_{\pi_{i}\hspace{0pt}{(\alpha)}}$ be the sum of the distances from the root vertex $x_{init}$ to its $\alpha_{1}$-th child, from this vertex to its $\alpha_{2}$-th child, etc., for a total of $i$ terms. Because of Lemma 45 ‣ Sampling-based Algorithms for Optimal Motion Planning"), this construction is well defined, almost surely, for a sufficiently large number of samples. For any infinite sequence $\alpha \in \Lambda$, let $\mathcal{L}_{\alpha} = {\lim_{i\rightarrow{+ \infty}}\mathcal{L}_{\pi_{i}\hspace{0pt}{(\alpha)}}}$; the limit exists since $\mathcal{L}_{\pi_{i}\hspace{0pt}{(\alpha)}}$ is non-decreasing in $i$.

Consider infinite strings of the form $\mathbf{k} = {(k,1,1,\ldots)}$, $k \in {\mathbb{N}}$, and introduce the shorthand $\mathcal{L}_{\mathbf{k}}:=\mathcal{L}_{(k,1,1,\ldots)}$. The following lemma shows that, for any $k \in {\mathbb{N}}$, $\mathcal{L}_{\mathbf{k}}$ has finite expectation, which immediately implies that $\mathcal{L}_{\mathbf{k}}$ takes only finite values with probability one. The lemma also provides a couple of other useful properties of $\mathcal{L}_{\mathbf{k}}$, which will be used later on.

###### Lemma 46 

The expected value ${\mathbb{E}}\hspace{0pt}{\lbrack\mathcal{L}_{\mathbf{k}}\rbrack}$ is non-negative and finite, and monotonically non-increasing, in the sense that ${{\mathbb{E}}\hspace{0pt}{\lbrack\mathcal{L}_{\mathbf{k} + \mathbf{1}}\rbrack}} \leq {{\mathbb{E}}\hspace{0pt}{\lbrack\mathcal{L}_{\mathbf{k}}\rbrack}}$, for any $k \in {\mathbb{N}}$. Moreover, ${\lim_{k\rightarrow\infty}{{\mathbb{E}}\hspace{0pt}{\lbrack\mathcal{L}_{\mathbf{k}}\rbrack}}} = 0$.

###### Proof. 

Under the simplifying assumptions that there are no obstacles in the unit cube and $\eta$ is large enough, the vertex set $V_{n}^{RRT}$ of the graph maintained by the RRT algorithm is precisely the first $n$ samples and each new sample is connected to its nearest neighbor in $V_{n}^{RRT}$.

Define $Z_{i}$ as a random variable describing the contribution to $\mathcal{L}_{\mathbf{1}}$ realized at iteration $i$; in other words, $Z_{i}$ is the distance of the $i$-th sample to its nearest neighbor among the first $i - 1$ samples if the $i$-th sample is on the path used in computing $\mathcal{L}_{\mathbf{1}}$, and zero otherwise. Then, using Lemma 45 ‣ Sampling-based Algorithms for Optimal Motion Planning"),

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{E}}\hspace{0pt}{\lbrack\mathcal{L}_{\mathbf{1}}\rbrack}} = {{\mathbb{E}}\hspace{0pt}\left\lbrack {\sum\limits_{i = 1}^{\infty}Z_{i}} \right\rbrack} = {\sum\limits_{i = 1}^{\infty}{{\mathbb{E}}\hspace{0pt}{\lbrack Z_{i}\rbrack}}} = {\sum\limits_{i = 1}^{\infty}{i^{- {1/d}}\hspace{0pt}i^{- 1}}} = {{\mathtt{Z}\mathtt{e}\mathtt{t}\mathtt{a}}\hspace{0pt}{({1 + {1/d}})}}},$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

where the second equality follows from the monotone convergence theorem and $\mathtt{Z}\mathtt{e}\mathtt{t}\mathtt{a}$ is the Riemann zeta function. Since ${\mathtt{Z}\mathtt{e}\mathtt{t}\mathtt{a}}\hspace{0pt}{(y)}$ is finite for any $y > 1$, ${\mathbb{E}}\hspace{0pt}{\lbrack\mathcal{L}_{\mathbf{1}}\rbrack}$ is a finite number for all $d \in {\mathbb{N}}$.

Let $N_{k}$ be the iteration at which the first sample contributing to $\mathcal{L}_{k}$ is generated. Then, an argument similar to the one given above yields

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     $${{{\mathbb{E}}\hspace{0pt}{\lbrack\mathcal{L}_{\mathbf{k} + \mathbf{1}}\rbrack}} = {\sum\limits_{i = {N_{k} + 1}}^{\infty}i^{- {({1 + {1/d}})}}} = {{{\mathbb{E}}\hspace{0pt}{\lbrack\mathcal{L}_{\mathbf{1}}\rbrack}} - {\sum\limits_{i = 1}^{N_{k}}i^{- {({1 + {1/d}})}}}}}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

Then, clearly, ${{\mathbb{E}}\hspace{0pt}{\lbrack\mathcal{L}_{\mathbf{k} + \mathbf{1}}\rbrack}} < {{\mathbb{E}}\hspace{0pt}{\lbrack\mathcal{L}_{\mathbf{k}}\rbrack}}$ for all $k \in {\mathbb{N}}$. Moreover, since $N_{k} \geq k$, it is the case that ${\lim_{k\rightarrow\infty}{{\mathbb{E}}\hspace{0pt}{\lbrack\mathcal{L}_{\mathbf{k}}\rbrack}}} = 0$. ∎∎

### B.3 Length of the longest path in a branch 

Given $k \in {\mathbb{N}}$, and the sequence $\mathbf{k} = {(k,1,1,\ldots)}$, the quantity $\sup_{\alpha \geq \mathbf{k}}\mathcal{L}_{\alpha}$ is an upper bound on the length of any path in the $k$-th branch of the RRT, or in any of the following branches. The next result bounds the probability that this quantity is very large.

###### Lemma 47 

For any $\epsilon > 0$,

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( \left\{ {{\sup\limits_{\alpha \geq \mathbf{k}}\mathcal{L}_{\alpha}} > \epsilon} \right\} \right)} \leq \frac{{\mathbb{E}}\hspace{0pt}{\lbrack\mathcal{L}_{\mathbf{k}}\rbrack}}{\epsilon}}.$$   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

First, we state and prove the following intermediate result.

###### Lemma 48 

${{\mathbb{E}}\hspace{0pt}{\lbrack\mathcal{L}_{\alpha}\rbrack}} \leq {{\mathbb{E}}\hspace{0pt}{\lbrack\mathcal{L}_{\mathbf{k}}\rbrack}}$, for all $\alpha \geq \mathbf{k}$.

###### Proof. 

The proof is by induction. Since $\alpha \geq \mathbf{k}$, then ${\pi_{1}\hspace{0pt}{(\alpha)}} \geq k$, and Lemma 46 ‣ Sampling-based Algorithms for Optimal Motion Planning") implies that ${{\mathbb{E}}\hspace{0pt}{\lbrack\mathcal{L}_{({\pi_{1}\hspace{0pt}{(\alpha)}},1,1,\ldots)}\rbrack}} \leq {{\mathbb{E}}\hspace{0pt}{\lbrack\mathcal{L}_{\mathbf{k}}\rbrack}}$. Moreover, it is also the case that, for any $i \in {\mathbb{N}}$ (and some abuse of notation), ${{\mathbb{E}}\hspace{0pt}{\lbrack\mathcal{L}_{({\pi_{i + 1}\hspace{0pt}{(\alpha)}},1,1,\ldots)}\rbrack}} \leq {{\mathbb{E}}\hspace{0pt}{\lbrack\mathcal{L}_{({\pi_{i}\hspace{0pt}{(\alpha)}},1,1,\ldots)}\rbrack}}$, by a similar argument considering a tree rooted at the last vertex reached by the finite path $\pi_{i}\hspace{0pt}{(\alpha)}$. Since ${({\pi_{i + 1}\hspace{0pt}{(\alpha)}},1,1,\ldots)} \geq {({\pi_{i}\hspace{0pt}{(\alpha)}},1,1,\ldots)} \geq {(k,1,1,\ldots)}$, the result follows. ∎∎

###### Proof of Lemma 47 ‣ Sampling-based Algorithms for Optimal Motion Planning"). 

Define the random variable $\overline{\alpha}:={\inf\left. \{{\alpha \geq \mathbf{k}} \middle| {\mathcal{L}_{\alpha} > \epsilon}\} \right.}$, and set $\overline{\alpha}:=\mathbf{k}$ if $\mathcal{L}_{\alpha} \leq \epsilon$ for all $\alpha \geq \mathbf{k}$. Note that $\overline{\alpha} \geq \mathbf{k}$ holds surely. Hence, by Lemma 48 ‣ Sampling-based Algorithms for Optimal Motion Planning"), ${{\mathbb{E}}\hspace{0pt}{\lbrack\mathcal{L}_{\overline{\alpha}}\rbrack}} \leq {{\mathbb{E}}\hspace{0pt}{\lbrack\mathcal{L}_{\mathbf{k}}\rbrack}}$. Let $I_{\epsilon}$ be the indicator random variable for the event $S_{\epsilon}:={\{{{\sup_{\alpha \geq \mathbf{k}}\mathcal{L}_{\alpha}} > \epsilon}\}}$. Then,

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     $${{{\mathbb{E}}\hspace{0pt}{\lbrack\mathcal{L}_{\mathbf{k}}\rbrack}} \geq {{\mathbb{E}}\hspace{0pt}{\lbrack\mathcal{L}_{\overline{\alpha}}\rbrack}} = {{{\mathbb{E}}\hspace{0pt}{\lbrack{\mathcal{L}_{\overline{\alpha}}\hspace{0pt}I_{\epsilon}}\rbrack}} + {{\mathbb{E}}\hspace{0pt}{\lbrack{\mathcal{L}_{\overline{\alpha}}\hspace{0pt}{({1 - I_{\epsilon}})}}\rbrack}}} \geq {\epsilon\hspace{0pt}{\mathbb{P}}\hspace{0pt}{(S_{\epsilon})}}},$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

where the last inequality follows from the fact that $\mathcal{L}_{\overline{\alpha}}$ is at least $\epsilon$ whenever the event $S_{\epsilon}$ occurs. ∎∎

A useful corollary of Lemmas 46 ‣ Sampling-based Algorithms for Optimal Motion Planning") and 47 ‣ Sampling-based Algorithms for Optimal Motion Planning") is the following.

###### Corollary 49 

For any $\epsilon > 0$, ${\lim_{k\rightarrow\infty}{{\mathbb{P}}\hspace{0pt}{({\{{{\sup_{\alpha \geq \mathbf{k}}\mathcal{L}_{\alpha}} > \epsilon}\}})}}} = 0$.

### B.4 Violation of the necessary condition 

Recall from Lemma 44 ‣ Sampling-based Algorithms for Optimal Motion Planning") that a necessary condition for asymptotic optimality is that the $k$-th branch of the RRT contains vertices outside the $R$-ball centered at $x_{init}$ for infinitely many $k$, where $0\hspace{0pt}{<{{R\hspace{0pt}{<\inf_{y \in \mathcal{X}_{goal}}\parallel}\hspace{0pt}y} - x_{init}}\parallel}$. Clearly, the latter event can occur only if longest path in the $k$-th branch of the RRT is longer than $R$ for infinitely many $k$. That is,

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( \left\{ {{\lim\limits_{n\rightarrow\infty}Y_{n}^{RRT}} = c^{\ast}} \right\} \right)} \leq {{\mathbb{P}}\hspace{0pt}\left( {\operatorname{lim\ sup}\limits_{k\rightarrow\infty}\left\{ {{\sup_{\alpha \geq \mathbf{k}}\mathcal{L}_{\alpha}} > R} \right\}} \right)}}.$$   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

The event on the right hand side is monotonic in the sense that ${\{{{\sup_{\alpha > {\mathbf{k} + 1}}\mathcal{L}_{\alpha}} > R}\}} \supseteq {\{{{\sup_{\alpha \geq \mathbf{k}}\mathcal{L}_{\alpha}} > R}\}}$ for all $k \in {\mathbb{N}}$. Hence, $\lim_{k\rightarrow\infty}{\{{{\sup_{\alpha \geq \mathbf{k}}\mathcal{L}_{\alpha}} > R}\}}$ exists. In particular, ${{\mathbb{P}}\hspace{0pt}{({\operatorname{lim\ sup}_{k\rightarrow\infty}{\{{{\sup_{\alpha \geq \mathbf{k}}\mathcal{L}_{\alpha}} > R}\}}})}} = {{\mathbb{P}}\hspace{0pt}{({\lim_{k\rightarrow\infty}{\{{{\sup_{\alpha \geq \mathbf{k}}\mathcal{L}_{\alpha}} > R}\}}})}} = {\lim_{k\rightarrow\infty}{{\mathbb{P}}\hspace{0pt}{({\{{{\sup_{\alpha \geq \mathbf{k}}\mathcal{L}_{\alpha}} > R}\}})}}}$, where the last equality follows from the continuity of probability measures. Since ${\lim_{k\rightarrow\infty}{{\mathbb{P}}\hspace{0pt}\left( \left\{ {{\sup_{\alpha \geq \mathbf{k}}\mathcal{L}_{\alpha}} > R} \right\} \right)}} = 0$ for all $R > 0$ by Corollary 49 ‣ Sampling-based Algorithms for Optimal Motion Planning"), ${{\mathbb{P}}\hspace{0pt}{({\{{{\lim_{n\rightarrow\infty}Y_{n}^{RRT}} = c^{\ast}}\}})}} = 0$.

## Appendix C Proof of Theorem 34 ‣ 4.2.2 Proposed algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning") (Asymptotic optimality of PRM^∗^) 

An outline of the proof is given below, before the details are provided.

### C.1 Outline of the proof 

Let $\sigma^{\ast}$ denote a robustly optimal path. By definition, $\sigma^{\ast}$ has weak $\delta$-clearance. First, define a sequence ${\{\delta_{n}\}}_{n \in {\mathbb{N}}}$ such that $\delta_{n} > 0$ for all $n \in {\mathbb{N}}$ and $\delta_{n}$ approaches zero as $n$ approaches infinity. Construct a sequence ${\{\sigma_{n}\}}_{n \in {\mathbb{N}}}$ of paths such that $\sigma_{n}$ has strong $\delta_{n}$-clearance for all $n \in {\mathbb{N}}$ and $\sigma_{n}$ converges to $\sigma^{\ast}$ as $n$ approaches infinity.

Second, define a sequence ${\{ q_{n}\}}_{n \in {\mathbb{N}}}$. For all $n \in {\mathbb{N}}$, construct a set $B_{n} = {\{ B_{n,1},B_{n,2},\ldots,B_{n,M_{n}}\}}$ of overlapping balls, each with radius $q_{n}$, that collectively "cover" the path $\sigma_{n}$. See Figures 23 ‣ Sampling-based Algorithms for Optimal Motion Planning") and 24 ‣ Sampling-based Algorithms for Optimal Motion Planning"). Let $x_{m} \in B_{n,m}$ and $x_{m + 1} \in B_{n,{m + 1}}$ be any two points from two consecutive balls in $B_{n}$. Construct $B_{n}$ such that (i) $x_{m}$ and $x_{m + 1}$ have distance no more than the connection radius $r\hspace{0pt}{(n)}$ and (ii) the straight path connecting $x_{m}$ and $x_{m + 1}$ lies entirely within the obstacle free space. These requirements can be satisfied by setting $\delta_{n}$ and $q_{n}$ to certain constant fractions of $r\hspace{0pt}{(n)}$.

Let $A_{n}$ denote the event that each ball in $B_{n}$ contains at least one vertex of the graph returned by the PRM^∗^ algorithm, when the algorithm is run with $n$ samples. Third, show that $A_{n}$ occurs for all large $n$, with probability one. Clearly, in this case, the PRM^∗^ algorithm will connect the vertices in consecutive balls with an edge, and any path formed in this way will be collision-free.

Finally, show that any sequence of paths generated in this way converges to the optimal path $\sigma^{\ast}$. Using the robustness of $\sigma^{\ast}$, show that the cost of the best path in the graph returned by the PRM^∗^ algorithm converges to $c\hspace{0pt}{(\sigma^{\ast})}$ almost surely.

### C.2 Construction of the sequence ${\{\sigma_{n}\}}_{n \in {\mathbb{N}}}$ of paths 

The following lemma establishes a connection between the notions of strong and weak $\delta$-clearance.

###### Lemma 50 

Let $\sigma^{\ast}$ be a path be a path that has strong $\delta$-clearance. Let ${\{\delta_{n}\}}_{n \in {\mathbb{N}}}$ be a sequence of real numbers such that ${\lim_{n\rightarrow\infty}\delta_{n}} = 0$ and $0 \leq \delta_{n} \leq \delta$ for all $n \in {\mathbb{N}}$. Then, there exists a sequence ${\{\sigma_{n}\}}_{n \in {\mathbb{N}}}$ of paths such that ${\lim_{n\rightarrow\infty}\sigma_{n}} = \sigma^{\ast}$ and $\sigma_{n}$ has strong $\delta_{n}$-clearance for all $n \in {\mathbb{N}}$.

###### Proof. 

First, define a sequence ${\{\mathcal{X}_{n}\}}_{n \in {\mathbb{N}}}$ of subsets of $\mathcal{X}_{free}$ such that $\mathcal{X}_{n}$ is the closure of the $\delta_{n}$-interior of $\mathcal{X}_{free}$, i.e.,

  -- --------------------------------------------------------------------------------------------------- --
     $$\mathcal{X}_{n}:={{cl}\hspace{0pt}{({{int}_{\delta_{n}}\hspace{0pt}{(\mathcal{X}_{free})}})}}$$   
  -- --------------------------------------------------------------------------------------------------- --

for all $n \in {\mathbb{N}}$. Note that, by definition, (i) $\mathcal{X}_{n}$ are closed subsets of $\mathcal{X}_{free}$, and (ii) any point $\mathcal{X}_{n}$ has distance at least $\delta_{n}$ to any point in the obstacle set $\mathcal{X}_{obs}$.

Then, construct the sequence ${\{\sigma_{n}\}}_{n \in {\mathbb{N}}}$ of paths, where $\sigma_{n} \in \Sigma_{\mathcal{X}_{n}}$, as follows. Let $\psi:{{\lbrack 0,1\rbrack}\rightarrow\Sigma_{free}}$ denote the homotopy with ${\psi\hspace{0pt}{(0)}} = \sigma^{\ast}$; the existence of $\psi$ is guaranteed by weak $\delta$-clearance of $\sigma^{\ast}$. Define

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\alpha_{n}:={{\max\limits_{\alpha \in {\lbrack 0,1\rbrack}}{\{{\left. \alpha \middle| {\psi\hspace{0pt}{(\alpha)}} \right. \in \Sigma_{\mathcal{X}_{n}}}\}}}\quad\text{~and~}}}\quad{\sigma_{n}:={\psi\hspace{0pt}{(\alpha_{n})}}}}.$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Since $\Sigma_{\mathcal{X}_{n}}$ is closed, the maximum in the definition of $\alpha_{n}$ is attained. Moreover, since $\psi\hspace{0pt}{(1)}$ has strong $\delta$-clearance and $\delta_{n} \leq \delta$, $\sigma_{n} \in \Sigma_{\mathcal{X}_{n}}$, which implies the strong $\delta_{n}$-clearance of $\sigma_{n}$.

Clearly, ${\bigcup_{n \in {\mathbb{N}}}\mathcal{X}_{n}} = \mathcal{X}_{free}$, since ${\lim_{n\rightarrow\infty}\delta_{n}} = 0$. Also, by weak $\delta$-clearance of $\sigma^{\ast}$, for any $\alpha \in {(0,1\rbrack}$, there exists some $\delta_{\alpha} \in {(0,\delta\rbrack}$ such that $\psi\hspace{0pt}{(\alpha)}$ has strong $\delta_{\alpha}$-clearance. Then, ${\lim_{n\rightarrow\infty}\alpha_{n}} = 0$, which implies ${\lim_{n\rightarrow\infty}\sigma_{n}} = \sigma^{\ast}$.∎∎

Recall that the connection radius of the PRM^∗^ algorithm was defined as

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     $$r_{n} = {\gamma_{PRM}\hspace{0pt}\left( \frac{\log n}{n} \right)^{1/d}} > {\, 2\hspace{0pt}{({1 + {1/d}})}^{1/d}\hspace{0pt}\left( \frac{\mu\hspace{0pt}{(X_{free})}}{\zeta_{d}} \right)^{1/d}\hspace{0pt}\left( \frac{\log n}{n} \right)^{1/d}}$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

(see Algorithm 4: ‣ 3.3 Proposed algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning") and the definition of the $\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}$ procedure in Section 3.1). Let $\theta_{1}$ be a small positive constant; the precise value of $\theta_{1}$ will be provided shortly in the proof of Lemma 52 ‣ Sampling-based Algorithms for Optimal Motion Planning"). Define

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\delta_{n}:={\min\left\{ \delta,{\frac{1 + \theta_{1}}{2 + \theta_{1}}\hspace{0pt}r_{n}} \right\}}},{{\text{~for all~}\hspace{0pt}n} \in {\mathbb{N}}}}.$$   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------- --

By definition, $0 \leq \delta_{n} \leq \delta$ holds. Moreover, ${\lim_{n\rightarrow\infty}\delta_{n}} = 0$, since ${\lim_{n\rightarrow\infty}r_{n}} = 0$. Then, by Lemma 50 ‣ Sampling-based Algorithms for Optimal Motion Planning"), there exists a sequence ${\{\sigma_{n}\}}_{n \in {\mathbb{N}}}$ of paths such that ${\lim_{n\rightarrow\infty}\sigma_{n}} = \sigma^{\ast}$ and $\sigma_{n}$ has strong $\delta_{n}$-clearance for all $n \in {\mathbb{N}}$.

### C.3 Construction of the sequence ${\{ B_{n}\}}_{n \in {\mathbb{N}}}$ of sets of balls 

First, a construction of a finite set of balls that collectively "cover" a path $\sigma_{n}$ is provided. The construction is illustrated in Figure 23 ‣ Sampling-based Algorithms for Optimal Motion Planning").

###### Definition 51 (Covering balls) 

Given a path $\sigma_{n}:{{\lbrack 0,1\rbrack}\rightarrow\mathcal{X}}$, and the real numbers ${q_{n},l_{n}} \in {\mathbb{R}}_{> 0}$, the set ${\mathtt{C}\mathtt{o}\mathtt{v}\mathtt{e}\mathtt{r}\mathtt{i}\mathtt{n}\mathtt{g}\mathtt{B}\mathtt{a}\mathtt{l}\mathtt{l}\mathtt{s}}\hspace{0pt}{(\sigma_{n},q_{n},l_{n})}$ is defined as a set $\{ B_{n,1},B_{n,2},\ldots,B_{n,M_{n}}\}$ of $M_{n}$ balls of radius $q_{n}$ such that $B_{n,m}$ is centered at $\sigma\hspace{0pt}{(\tau_{m})}$, and

-   [•]

    the center of $B_{n,1}$ is $\sigma\hspace{0pt}{(0)}$, i.e., $\tau_{1} = 0$,

-   [•]

    the centers of two consecutive balls are exactly $l_{n}$ apart, i.e., $\tau_{m}:={\min{\{{\tau \in {\lbrack\tau_{m - 1},1\rbrack}} \mid {{\|{{\sigma\hspace{0pt}{(\tau)}} - {\sigma\hspace{0pt}{(\tau_{m - 1})}}}\|} \geq l_{n}}\}}}$ for all $m \in {\{ 2,3,\ldots,M_{n}\}}$,

-   [•]

    and $M - 1$ is the largest number of balls that can be generated in this manner while the center of the last ball, $B_{n,M_{n}}$ is $\sigma\hspace{0pt}{(1)}$, i.e., $\tau_{M_{n}} = 1$.

Figure 23: An illustration of the CoveringBalls construction. A set of balls that collectively cover the trajectory σn is shown. All balls have the same radius, qn. The spacing between the centers of two consecutive balls is ln.

For each $n \in {\mathbb{N}}$, define

  -- ------------------------------------------------- --
     $${q_{n}:=\frac{\delta_{n}}{1 + \theta_{1}}}.$$   
  -- ------------------------------------------------- --

Construct the set $B_{n} = {\{ B_{n,1},B_{n,2},\ldots,B_{n,M_{n}}\}}$ of balls as $B_{n}:={{\mathtt{C}\mathtt{o}\mathtt{v}\mathtt{e}\mathtt{r}\mathtt{i}\mathtt{n}\mathtt{g}\mathtt{B}\mathtt{a}\mathtt{l}\mathtt{l}\mathtt{s}}\hspace{0pt}{(\sigma_{n},q_{n},{\theta_{1}\hspace{0pt}q_{n}})}}$ using Definition 51 ‣ C.3 Construction of the sequence {𝐵_𝑛}_{𝑛∈ℕ} of sets of balls ‣ Appendix C Proof of Theorem 34 (Asymptotic optimality of PRM∗) ‣ Sampling-based Algorithms for Optimal Motion Planning") (see Figure 23 ‣ Sampling-based Algorithms for Optimal Motion Planning")). By construction, each ball in $B_{n}$ has radius $q_{n}$ and the centers of consecutive balls in $B_{n}$ are $\theta_{1}\hspace{0pt}q_{n}$ apart (see Figure 24 ‣ Sampling-based Algorithms for Optimal Motion Planning") for an illustration of covering balls with this set of parameters). The balls in $B_{n}$ collectively cover the path $\sigma_{n}$.

Figure 24: An illustration of the covering balls for PRM∗ algorithm. The δn-ball is guaranteed to be inside the obstacle-free space. The connection radius rn is also shown as the radius of the connection ball centered at a vertex x ∈ Bn, m. The vertex x is connected to all other vertices that lie within the connection ball.

### C.4 The probability that each ball in $B_{n}$ contains at least one vertex 

Recall that $G_{n}^{{PRM}^{\ast}} = {(V_{n}^{{PRM}^{\ast}},E_{n}^{{PRM}^{\ast}})}$ denotes the graph returned by the PRM^∗^ algorithm, when the algorithm is run with $n$ samples. Let $A_{n,m}$ denote the event that the ball $B_{n,m}$ contains at least one vertex of the graph generated by the PRM^∗^ algorithm, i.e., $A_{n,m} = \left\{ {{B_{n,m} \cap V_{n}^{{PRM}^{\ast}}} \neq \varnothing} \right\}$. Let $A_{n}$ denote the event that all balls in $B_{n}$ contain at least one vertex of the PRM^∗^ graph, i.e., $A_{n} = {\bigcap_{m = 1}^{M_{n}}A_{n,m}}$.

###### Lemma 52 

If $\gamma_{PRM} > {2\hspace{0pt}{({1 + {1/d}})}^{1/d}\hspace{0pt}\left( \frac{\mu\hspace{0pt}{(X_{free})}}{\zeta_{d}} \right)^{1/d}}$, then there exists a constant $\theta_{1} > 0$ such that the event that every ball in $B_{n}$ contains at least one vertex of the PRM^∗^ graph occurs for all large enough $n$ with probability one, i.e.,

  -- ---------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( {\operatorname{lim\ inf}\limits_{n\rightarrow\infty}A_{n}} \right)} = 1}.$$   
  -- ---------------------------------------------------------------------------------------------------------------- --

###### Proof. 

The proof is based on a Borel-Cantelli argument which can be summarized as follows. Recall that $A_{n}^{c}$ denotes the complement of $A_{n}$. First, the sum $\sum_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}{(A_{n}^{c})}}$ is shown to be bounded. By the Borel-Cantelli lemma (Grimmett and Stirzaker, 2001), this implies that the probability that $A_{n}$ holds infinitely often as $n$ approaches infinity is zero. Hence, the probability that $A_{n}$ holds infinitely often is one. In the rest of the proof, an upper bound on ${\mathbb{P}}\hspace{0pt}{(A_{n})}$ is computed, and this upper bound is shown to be summable.

First, compute a bound on the number of balls in $B_{n}$ as follows. Let $s_{n}$ denote the length of $\sigma_{n}$, i.e., $s_{n}:={{TV}\hspace{0pt}{(\sigma_{n})}}$. Recall that the balls in $B_{n}$ were constructed such that the centers of two consecutive balls in $B_{n}$ have distance $\theta_{1}\hspace{0pt}q_{n}$. The segment of $\sigma_{n}$ that starts at the center of $B_{n,m}$ and ends at the center of $B_{n,{m + 1}}$ has length at least $\theta_{1}\hspace{0pt}q_{n}$, except for the last segment, which has length less than or equal to $\theta_{1}\hspace{0pt}q_{n}$. Let $n_{0} \in {\mathbb{N}}$ be the number such that $\delta_{n} < \delta$ for all $n \geq n_{0}$. Then, for all $n \geq n_{0}$,

  -- ---------------------------------------- -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     ${{card}\left( B_{n} \right)} = M_{n}$   $\leq$   $\frac{s_{n}}{\theta_{1}\hspace{0pt}q_{n}} = \frac{{({1 + \theta_{1}})}\hspace{0pt}s_{n}}{\theta_{1}\hspace{0pt}\delta_{n}} = \frac{{({2 + \theta_{1}})}\hspace{0pt}s_{n}}{\theta_{1}\hspace{0pt}r_{n}}$   
                                              $=$      ${\frac{{({2 + \theta_{1}})}\hspace{0pt}s_{n}}{\theta_{1}\hspace{0pt}\gamma_{PRM}}\hspace{0pt}\left( \frac{n}{\log n} \right)^{1/d}}.$                                                                     
  -- ---------------------------------------- -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Second, compute the volume of a single ball in $B_{i}$ as follows. Recall that $\mu\hspace{0pt}{( \cdot )}$ denotes the usual Lebesgue measure, and $\zeta_{d}$ denotes the volume of a unit ball in the $d$-dimensional Euclidean space. For all $n \geq n_{0}$,

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${\mu\hspace{0pt}{(B_{n,m})}} = {\zeta_{d}\hspace{0pt}q_{n}^{d}} = {\zeta_{d}\hspace{0pt}\left( \frac{\delta_{n}}{1 + \theta_{1}} \right)^{d}} = {\zeta_{d}\hspace{0pt}\left( \frac{r_{n}}{2 + \theta_{1}} \right)^{d}} = {\zeta_{d}\hspace{0pt}\left( \frac{\gamma_{PRM}}{2 + \theta_{1}} \right)^{d}\hspace{0pt}\frac{\log n}{n}}$$   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

For all $n \geq I$, the probability that a single ball, say $B_{n,1}$, does not contain a vertex of the graph generated by the PRM^∗^ algorithm, when the algorithm is run with $n$ samples, is

  -- ------------------------------------------------------ ----- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     ${\mathbb{P}}\hspace{0pt}\left( A_{n,1}^{c} \right)$   $=$   $\left( {1 - \frac{\mu\hspace{0pt}{(B_{n,1})}}{\mu\hspace{0pt}{(X_{free})}}} \right)^{n}$                                                                                  
                                                            $=$   $\left( {1 - {\frac{\zeta_{d}}{\mu\hspace{0pt}{(X_{free})}}\hspace{0pt}\left( \frac{\gamma_{PRM}}{2 + \theta_{1}} \right)^{d}\hspace{0pt}\frac{\log n}{n}}} \right)^{n}$   
  -- ------------------------------------------------------ ----- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Using the inequality ${({1 - {{1/f}\hspace{0pt}{(n)}}})}^{r} \leq e^{- {{r/f}\hspace{0pt}{(n)}}}$, the right-hand side can be bounded as

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}{(A_{n,1})}} \leq e^{- {\frac{\zeta_{d}}{\mu\hspace{0pt}{(X_{free})}}\hspace{0pt}{(\frac{\gamma_{PRM}}{2 + \theta_{1}})}^{d}\hspace{0pt}{\log n}}} = n^{- {\frac{\zeta_{d}}{\mu\hspace{0pt}{(X_{free})}}\hspace{0pt}{(\frac{\gamma_{PRM}}{2 + \theta_{1}})}^{d}}}}.$$   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Hence,

  -- -------------------------------------------------------------------------------------------------------------------------------------- -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     ${{\mathbb{P}}\hspace{0pt}\left( A_{n}^{c} \right)} = {{\mathbb{P}}\hspace{0pt}\left( {\bigcup_{m = 1}^{M_{n}}A_{n,m}^{c}} \right)}$   $\leq$   ${\sum\limits_{m = 1}^{M_{n}}{{\mathbb{P}}\hspace{0pt}\left( A_{n,m}^{c} \right)}} = {M_{n}\hspace{0pt}{\mathbb{P}}\hspace{0pt}{(A_{n,1}^{c})}}$                                                                                                                       
                                                                                                                                            $\leq$   $\frac{{({2 + \theta_{1}})}\hspace{0pt}s_{n}}{\theta_{1}\hspace{0pt}\gamma_{PRM}}\hspace{0pt}\left( \frac{n}{\log n} \right)^{1/d}\hspace{0pt}i^{- {\frac{\zeta_{d}}{\mu\hspace{0pt}{(X_{free})}}\hspace{0pt}{(\frac{\gamma_{PRM}}{2 + \theta_{1}})}^{d}}}$            
                                                                                                                                            $=$      $\frac{{({2 + \theta_{1}})}\hspace{0pt}s_{n}}{\theta_{1}\hspace{0pt}\gamma_{PRM}}\hspace{0pt}\frac{1}{{({\log n})}^{d}}\hspace{0pt}n^{- {({{\frac{\zeta_{d}}{\mu\hspace{0pt}{(X_{free})}}\hspace{0pt}{(\frac{\gamma_{PRM}}{2 + \theta_{1}})}^{d}} - \frac{1}{d}})}}$   
  -- -------------------------------------------------------------------------------------------------------------------------------------- -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

where the first inequality follows from the union bound.

Finally, ${\sum_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}{(A_{n}^{c})}}} < \infty$ holds, if ${{\frac{\zeta_{d}}{\mu\hspace{0pt}{(X_{free})}}\hspace{0pt}\left( \frac{\gamma_{PRM}}{2 + \theta_{1}} \right)^{d}} - \frac{1}{d}} > 1$, which can be satisfied for any $\gamma_{P\hspace{0pt}R\hspace{0pt}M} > {2\hspace{0pt}{({1 + {1/d}})}^{1/d}\hspace{0pt}\left( \frac{\mu\hspace{0pt}{(X_{free})}}{\zeta_{d}} \right)^{1/d}}$ by appropriately choosing $\theta_{1}$. Then, by the Borel-Cantelli lemma (Grimmett and Stirzaker, 2001), ${{\mathbb{P}}\hspace{0pt}{({\operatorname{lim\ sup}_{n\rightarrow\infty}A_{n}^{c}})}} = 0$, which implies ${{\mathbb{P}}\hspace{0pt}{({\operatorname{lim\ inf}_{n\rightarrow\infty}A_{n}})}} = 1$.∎∎

### C.5 Connecting the vertices in subsequent balls in $B_{n}$ 

Let $Z_{n}:={\{ x_{1},x_{2},\ldots,x_{M_{n}}\}}$ be any set of points such that $x_{m} \in B_{n,m}$ for each $m \in {\{ 1,2,\ldots,M_{n}\}}$. The following lemma states that for all $n \in {\mathbb{N}}$ and all $m \in {\{ 1,2,\ldots,{M_{n} - 1}\}}$, the distance between $x_{m}$ and $x_{m + 1}$ is less than the connection radius, $r_{n}$, which implies that the PRM^∗^ algorithm will attempt to connect the two points $x_{m}$ and $x_{m + 1}$ if they are in the vertex set of the PRM^∗^ algorithm.

###### Lemma 53 

If $x_{n,m} \in B_{n,m}$ and $x_{n,{m + 1}} \in B_{n,{m + 1}}$, then ${\|{x_{n,{m + 1}} - x_{n,m}}\|} \leq r_{n}$, for all $n \in {\mathbb{N}}$ and all $m \in {\{ 1,2,\ldots,{M_{i} - 1}\}}$.

###### Proof. 

Recall that each ball in $B_{n}$ has radius $q_{n} = \frac{\delta_{n}}{({1 + \theta_{1}})}$. Given any two points $x_{m} \in B_{n,m}$ and $x_{m + 1} \in B_{n,{m + 1}}$, all of the following hold: (i) $x_{m}$ has distance $q_{n}$ to the center of $B_{n,m}$, (ii) $x_{m + 1}$ has distance $q_{n}$ to the center of $B_{n,{m + 1}}$, and (iii) centers of $B_{n,m}$ and $B_{n,{m + 1}}$ have distance $\theta_{1}\hspace{0pt}q_{n}$ to each other. Then,

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\|{x_{n,{m + 1}} - x_{n,m}}\|} \leq {{({2 + \theta_{1}})}\hspace{0pt}q_{n}} = {\frac{2 + \theta_{1}}{1 + \theta_{1}}\hspace{0pt}\delta_{n}} \leq r_{n}},$$   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------- --

where the first inequality is obtained by an application of the triangle inequality and the last inequality follows from the definition of $\delta_{n} = {\min{\{\delta,{\frac{1 + \theta_{1}}{2 + \theta_{1}}\hspace{0pt}r_{n}}\}}}$. ∎∎

By Lemma 53 ‣ Sampling-based Algorithms for Optimal Motion Planning"), conclude that the PRM^∗^ algorithm will attempt to connect any two vertices in consecutive balls in $B_{n}$. The next lemma shows that any such connection attempt will, in fact, be successful. That is, the path connecting $x_{n,m}$ and $x_{n,{m + 1}}$ is collision-free for all $m \in {\{ 1,2,\ldots,M_{n}\}}$.

###### Lemma 54 

For all $n \in {\mathbb{N}}$ and all $m \in {\{ 1,2,\ldots,M_{n}\}}$, if $x_{m} \in B_{n,m}$ and $x_{m + 1} \in B_{n,{m + 1}}$, then the line segment connecting $x_{n,m}$ and $x_{n,{m + 1}}$ lies in the obstacle-free space, i.e.,

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{{\alpha\hspace{0pt}x_{n,m}} + {{({1 - \alpha})}\hspace{0pt}x_{n,{m + 1}}}} \in X_{free}},{{\text{~for all~}\hspace{0pt}\alpha} \in {\lbrack 0,1\rbrack}}}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

###### Proof. 

Recall that $\sigma_{n}$ has strong $\delta_{n}$-delta clearance and that the radius $q_{n}$ of each ball in $B_{n}$ was defined as $q_{n} = \frac{\delta_{n}}{1 + \theta_{1}}$, where $\theta_{1} > 0$ is a constant. Hence, any point along the trajectory $\sigma_{n}$ has distance at least ${({1 + \theta_{1}})}\hspace{0pt}q_{n}$ to any point in the obstacle set. Let $y_{m}$ and $y_{m + 1}$ denote the centers of the balls $B_{n,m}$ and $B_{n,{m + 1}}$, respectively. Since $y_{m} = {\sigma\hspace{0pt}{(\tau_{m})}}$ and $y_{m + 1} = {\sigma\hspace{0pt}{(\tau_{m + 1})}}$ for some $\tau_{m}$ and $\tau_{m + 1}$, $y_{m}$ and $y_{m + 1}$ also have distance ${({1 + \theta_{1}})}\hspace{0pt}q_{n}$ to any point in the obstacle set.

Clearly, ${\|{x_{m} - y_{m}}\|} \leq q_{n}$. Moreover, the following inequality holds:

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\|{x_{m + 1} - y_{m}}\|} \leq {\|{{({x_{m} - y_{m + 1}})} + {({y_{m + 1} - y_{m}})}}\|} \leq {{\|{x_{m + 1} - y_{m + 1}}\|} + {\|{y_{m + 1} - y_{m}}\|}} \leq {q_{n} + {\theta_{1}\hspace{0pt}q_{n}}} = {{({1 + \theta_{1}})}\hspace{0pt}q_{n}}}.$$   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

where the second inequality follows from the triangle inequality and the third inequality follows from the construction of balls in $B_{n}$.

For any convex combination $x_{\alpha}:={{\alpha\hspace{0pt}x_{m}} + {{({1 - \alpha})}\hspace{0pt}x_{m + 1}}}$, where $\alpha \in {\lbrack 0,1\rbrack}$, the distance between $x_{\alpha}$ and $y_{m}$ can be bounded as follows:

  -- ------------------------------------------------------------------------------------------------------------------- ----- ------------------------------------------------------------------------------------------------------------------------------- --
     $\left\| {\left( {{\alpha\hspace{0pt}x_{m}} + {{({1 + \alpha})}\hspace{0pt}x_{m + 1}}} \right) - y_{m}} \right\|$   $=$   $\left\| {{\alpha\hspace{0pt}{({x_{m} - y_{m}})}} + {{({1 + \alpha})}\hspace{0pt}{({x_{m + 1} - y_{m}})}}} \right\|$            
                                                                                                                         $=$   ${\alpha\hspace{0pt}{\|{x_{m} - y_{m}}\|}} + {{({1 + \alpha})}\hspace{0pt}{\|{x_{m + 1} - y_{m}}\|}}$                           
                                                                                                                         $=$   ${{{\alpha\hspace{0pt}q_{n}} + {{({1 + \alpha})}\hspace{0pt}{({1 + q_{n}})}}} \leq {{({1 + \theta_{1}})}\hspace{0pt}q_{n}}},$   
  -- ------------------------------------------------------------------------------------------------------------------- ----- ------------------------------------------------------------------------------------------------------------------------------- --

where the second equality follows from the linearity of the norm. Hence, any point along the line segment connecting $x_{m}$ and $x_{m + 1}$ has distance at most ${({1 + \theta_{1}})}\hspace{0pt}q_{n}$ to $y_{m}$. Since, $y_{m}$ has distance at least ${({1 + \theta_{1}})}\hspace{0pt}q_{n}$ to any point in the obstacle set, the line segment connecting $x_{m}$ and $x_{m + 1}$ is collision-free. ∎∎

### C.6 Convergence to the optimal path 

Let $P_{n}$ denote the set of all paths in the graph $G_{n}^{{PRM}^{\ast}} = {(V_{n}^{{PRM}^{\ast}},E_{n}^{{PRM}^{\ast}})}$. Let $\sigma_{n}^{\prime}$ be the path that is closest to $\sigma_{n}$ in terms of the bounded variation norm among all those paths in $P_{n}$, i.e., ${\sigma_{n}^{\prime}:={\min_{\sigma^{\prime} \in P_{n}}{\|{\sigma^{\prime} - \sigma_{n}}\|}}}.$ Note that the sequence ${\{\sigma_{n}^{\prime}\}}_{n \in {\mathbb{N}}}$ is a random sequence of paths, since the graph $G_{n}^{{PRM}^{\ast}}$, hence the set $P_{n}$ of paths is random. The following lemma states that the bounded variation distance between $\sigma_{n}^{\prime}$ and $\sigma_{n}$ approaches to zero, with probability one.

###### Lemma 55 

The random variable ${\|{\sigma_{n}^{\prime} - \sigma_{n}}\|}_{BV}$ converges to zero almost surely, i.e.,

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( {\left\{ \lim_{n\rightarrow\infty} \right\|\left. {{\sigma_{n}^{\prime} - {\sigma_{n}\parallel}_{BV}} = 0} \right\}} \right)} = 1}.$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

###### Proof. 

The proof of this lemma is based on a Borel-Cantelli argument. It is shown that $\sum_{n \in {\mathbb{N}}}{{\mathbb{P}}\hspace{0pt}{({{\|{\sigma_{n}^{\prime} - \sigma_{n}}\|}_{BV} > \epsilon})}}$ is finite for any $\epsilon > 0$, which implies that $\|{\sigma_{n}^{\prime} - \sigma_{n}}\|$ converges to zero almost surely by the Borel-Cantelli lemma (Grimmett and Stirzaker, 2001). This proof uses a Poissonization argument in one of the intermediate steps. That is, a particular result is shown to hold in the Poisson process described in Lemma 11) ‣ 2.2 Random Geometric Graphs ‣ 2 Preliminary Material ‣ Sampling-based Algorithms for Optimal Motion Planning"). Subsequently, the result is de-Poissonized, i.e., shown to hold also for the original process.

Fix some $\epsilon > 0$. Let ${\alpha,\beta} \in {(0,1)}$ be two constants, both independent of $n$. Recall that $q_{n}$ is the radius of each ball in the set $B_{n}$ of balls covering the path $\sigma_{n}$. Let $I_{n,m}$ denote the indicator variable for the event that the ball $B_{n,m}$ has no point that is within a distance $\beta\hspace{0pt}q_{n}$ from the center of $B_{n,m}$. For a more precise definition, let $\beta\hspace{0pt}B_{n,m}$ denote the ball that is centered at the center of $B_{n,m}$ and has radius $\beta\hspace{0pt}r_{n}$. Then,

  -- ------------------------------------------------------------------------------------------------------------- --
     $$I_{n,m}:=\begin{cases}                                                                                      
     {1,} & {{{{\text{if~}\hspace{0pt}{({\beta\hspace{0pt}B_{n,m}})}} \cap V^{{PRM}^{\ast}}} = \varnothing},} \\   
     {0,} & \text{otherwise.}                                                                                      
     \end{cases}$$                                                                                                 
  -- ------------------------------------------------------------------------------------------------------------- --

Let $K_{n}$ denote the number of balls in $B_{n}$ that do not contain a vertex that is within a $\beta\hspace{0pt}q_{n}$ distance to the center of that particular ball, i.e., $K_{n}:={\sum_{m = 1}^{M_{n}}I_{n,m}}$.

Consider the event that $I_{n,m}$ holds for at most an $\alpha$ fraction of the balls in $B_{n}$, i.e., ${\{{K_{n} \leq {\alpha\hspace{0pt}M_{n}}}\}}.$ This event is important for the following reason. Recall that the vertices in subsequent balls in $B_{n}$ are connected by edges in $G_{n}^{{PRM}^{\ast}}$ by Lemmas 53 ‣ Sampling-based Algorithms for Optimal Motion Planning") and 54 ‣ Sampling-based Algorithms for Optimal Motion Planning"). If only at most an $\alpha$ fraction of the balls do not have a vertex that is less than a distance of $\beta\hspace{0pt}r_{n}$ from their centers (hence, a $({1 - \alpha})$ fraction have at least one vertex within a distance of $\beta\hspace{0pt}r_{n}$ from their centers), i.e., $\{{K_{n} \leq {\alpha\hspace{0pt}M_{n}}}\}$ holds, then the bounded variation difference between $\sigma_{n}^{\prime}$ and $\sigma_{n}$ is at most ${{({{\sqrt{2}\hspace{0pt}\alpha} + {\beta\hspace{0pt}{({1 - \alpha})}}})}\hspace{0pt}L} \leq {\sqrt{2}\hspace{0pt}{({\alpha + \beta})}\hspace{0pt}L}$, where $L$ is a finite bound on the length of all paths in ${\{\sigma_{n}\}}_{n \in {\mathbb{N}}}$, i.e., $L:={\sup_{n \in {\mathbb{N}}}{{TV}\hspace{0pt}{(\sigma_{n})}}}$. That is,

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     $${\{{K_{n} \leq {\alpha\hspace{0pt}M_{n}}}\}} \subseteq \left\{ {{\|{\sigma_{n}^{\prime} - \sigma_{n}}\|}_{BV} \leq {\sqrt{2}\hspace{0pt}{({\alpha + \beta})}\hspace{0pt}L}} \right\}$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

Taking the complement of both sides and using the monotonicity of probability measures,

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( \left\{ {{\|{\sigma_{n}^{\prime} - \sigma_{n}}\|}_{BV} > {\sqrt{2}\hspace{0pt}{({\alpha + \beta})}\hspace{0pt}L}} \right\} \right)} \leq {{\mathbb{P}}\hspace{0pt}\left( {\{{K_{n} \geq {\alpha\hspace{0pt}M_{n}}}\}} \right)}}.$$   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

In the rest of the proof, it is shown that the right hand side of the inequality above is summable for all small ${\alpha,\beta} > 0$, which implies that ${\mathbb{P}}\hspace{0pt}\left( {\{{{\|{\sigma_{n}^{\prime} - \sigma_{n}}\|} > \epsilon}\}} \right)$ is summable for all small $\epsilon > 0$.

For this purpose, the process that provides independent uniform samples from $\mathcal{X}_{free}$ is approximated by an equivalent Poisson process described in Section 2.2. A more precise definition is given as follows. Let $\{ X_{1},X_{2},\ldots,X_{n}\}$ denote the binomial point process corresponding to the $\mathtt{S}\mathtt{a}\mathtt{m}\mathtt{p}\mathtt{l}\mathtt{e}\mathtt{F}\mathtt{r}\mathtt{e}\mathtt{e}$ procedure. Let $\nu < 1$ be a constant independent of $n$. Recall that ${Poisson}\hspace{0pt}{({\nu\hspace{0pt}n})}$ denotes the Poisson random variable with intensity $\nu\hspace{0pt}n$ (hence, mean value $\nu\hspace{0pt}n$). Then, the process $\mathcal{P}_{\nu\hspace{0pt}n}:={\{ X_{1},X_{2},\ldots,X_{{Poisson}\hspace{0pt}{({\nu\hspace{0pt}n})}}\}}$ is a Poisson process restricted to $\mu\hspace{0pt}{(\mathcal{X}_{free})}$ with intensity ${{\nu\hspace{0pt}n}/\mu}\hspace{0pt}{(\mathcal{X}_{free})}$ (see Lemma 11) ‣ 2.2 Random Geometric Graphs ‣ 2 Preliminary Material ‣ Sampling-based Algorithms for Optimal Motion Planning")). Thus, the expected number of points of this Poisson process is $\nu\hspace{0pt}n$.

Clearly, the set of points generated by one process is a subset of the those generated by the other. However, since $\nu < 1$, in most trials the Poisson point process $\mathcal{P}_{\nu\hspace{0pt}n}$ is a subset of the binomial point process.

Define the random variable ${\overset{\sim}{K}}_{n}$ denote the number of balls of that fail to have one sample within a distance $\beta\hspace{0pt}r_{n}$ to their centers, when the underlying point process is $\mathcal{P}_{\nu\hspace{0pt}n}$ (instead of the independent uniform samples provided by the $\mathtt{S}\mathtt{a}\mathtt{m}\mathtt{p}\mathtt{l}\mathtt{e}\mathtt{F}\mathtt{r}\mathtt{e}\mathtt{e}$ procedure). In other words, ${\overset{\sim}{K}}_{n}$ is the random variable that is defined similar to $K_{n}$, except that the former is defined with respect to the points of $\mathcal{P}_{\nu\hspace{0pt}n}$ whereas the latter is defined with respect to the $n$ samples returned by $\mathtt{S}\mathtt{a}\mathtt{m}\mathtt{p}\mathtt{l}\mathtt{e}\mathtt{F}\mathtt{r}\mathtt{e}\mathtt{e}$ procedure.

Since $\{{{\overset{\sim}{K}}_{n} > {\alpha\hspace{0pt}M_{n}}}\}$ is a decreasing event, i.e., the probability that it occurs increases if $\mathcal{P}_{\nu\hspace{0pt}n}$ includes fewer samples, the following bound holds (see, e.g., Penrose, 2003)

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( \left\{ {K_{n} \geq {\alpha\hspace{0pt}M_{n}}} \right\} \right)} \leq {{{\mathbb{P}}\hspace{0pt}\left( {\{{{\overset{\sim}{K}}_{n} \geq {\alpha\hspace{0pt}M_{n}}}\}} \right)} + {{\mathbb{P}}\hspace{0pt}{({\{{{{Poisson}\hspace{0pt}{({\nu\hspace{0pt}n})}} \geq n}\}})}}}}.$$   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Since a Poisson random variable has exponentially-decaying tails, the second term on the right hand side can be bounded as

  -- ----------------------------------------------------------------------------------------------------------------------------- --
     ${{{\mathbb{P}}\hspace{0pt}{({\{{{{Poisson}\hspace{0pt}{({\nu\hspace{0pt}n})}} \geq n}\}})}} \leq e^{- {c\hspace{0pt}n}}},$   
  -- ----------------------------------------------------------------------------------------------------------------------------- --

where $c > 0$ is a constant.

The first term on the right hand side can be computed directly as follows. First, for all small $\beta$, the balls of radius $\beta\hspace{0pt}r_{n}$ are all disjoint (see Figure 25 ‣ Sampling-based Algorithms for Optimal Motion Planning")). Denote this set of balls by ${\overset{\sim}{B}}_{n,m} = {\{{\overset{\sim}{B}}_{n,1},{\overset{\sim}{B}}_{n,2},\ldots,{\overset{\sim}{B}}_{n,M_{n}}\}}$. More precisely, ${\overset{\sim}{B}}_{n,m}$ is the ball of radius $\beta\hspace{0pt}q_{n}$ centered at the center of $B_{n,m}$. Second, observe that the event $\{{K_{n} > {\alpha\hspace{0pt}M_{n}}}\}$ is equivalent to the event that at least an $\alpha$ fraction of all the balls in ${\overset{\sim}{B}}_{n}$ include at least one point of the process $\mathcal{P}_{\nu\hspace{0pt}n}$. Since, the point process $\mathcal{P}_{\nu\hspace{0pt}n}$ is Poisson and the balls in ${\overset{\sim}{B}}_{n}$ are disjoint for all small enough $\beta$, the probability that a single ball in ${\overset{\sim}{B}}_{n}$ does not contain a sample is $p_{n}:={\exp{({- {{{\zeta_{d}\hspace{0pt}{({\beta\hspace{0pt}q_{n}})}^{d}\hspace{0pt}\nu\hspace{0pt}n}/\mu}\hspace{0pt}{(\mathcal{X}_{free})}}})}} \leq {\exp{({- {c\hspace{0pt}\beta\hspace{0pt}\nu\hspace{0pt}{\log n}}})}}$ for some constant $c$. Third, by the independence property of the Poisson point process, the number of balls in ${\overset{\sim}{B}}_{n}$ that do not include a point of the point process $\mathcal{P}_{\nu\hspace{0pt}n}$ is a binomial random variable with parameters $M_{n}$ and $p_{n}$. Then, for all large $n$,

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( \left\{ {{\overset{\sim}{K}}_{n} \geq {\alpha\hspace{0pt}M_{n}}} \right\} \right)} \leq {{\mathbb{P}}\hspace{0pt}\left( \left\{ {{{Binomial}\hspace{0pt}{(M_{n},p_{n})}} \geq {\alpha\hspace{0pt}M_{n}}} \right\} \right)} \leq {\exp{({- {M_{n}\hspace{0pt}p_{n}}})}}}.$$   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Figure 25: The set ${\overset{\sim}{B}}_{n,m}$ of non-intersection balls is illustrated.

Combining the two inequalities above, the following bound is obtained for the original sampling process

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     $${{{\mathbb{P}}\hspace{0pt}\left( \left\{ {K_{n} \geq {\alpha\hspace{0pt}M_{n}}} \right\} \right)} \leq {e^{- {c\hspace{0pt}n}} + e^{- {M_{n}\hspace{0pt}p_{n}}}}}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

Summing up both sides,

  -- -------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\sum\limits_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}\left( \left\{ {K_{n} \geq {\alpha\hspace{0pt}n}} \right\} \right)}} < \infty}.$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------- --

This argument holds for all ${\alpha,\beta,\nu} > 0$. Hence, for all $\epsilon > 0$,

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\sum\limits_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}\left( \left\{ {{\|{\sigma_{n}^{\prime} - \sigma_{n}}\|}_{BV} > \epsilon} \right\} \right)}} < \infty}.$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Then, by the Borel-Cantelli lemma, ${{\mathbb{P}}\hspace{0pt}\left( {\left\{ \lim_{n\rightarrow\infty} \right\|\left. {{\sigma_{n}^{\prime} - {\sigma_{n}\parallel}_{BV}} = 0} \right\}} \right)} = 1$.∎∎

Finally, the following lemma states that the cost of the minimum cost path in the graph returned by the ${PRM}^{\ast}$ algorithm converges to the optimal cost $c^{\ast}$ with probability one. Recall that $Y_{n}^{{PRM}^{\ast}}$ denotes the cost of the minimum-cost path in the graph returned by the ${PRM}^{\ast}$ algorithm, when the algorithm is run with $n$ samples.

###### Lemma 56 

Under the assumptions of Theorem 34 ‣ 4.2.2 Proposed algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning"), the cost of the minimum-cost path present in the graph returned by the ${PRM}^{\ast}$ algorithm converges to the optimal cost $c^{\ast}$ as the number of samples approaches infinity, with probability one, i.e.,

  -- ------------------------------------------------------------------------------------------------------------------------------------------ --
     $${{{\mathbb{P}}\hspace{0pt}\left( \left\{ {{\lim\limits_{n\rightarrow\infty}Y_{n}^{{PRM}^{\ast}}} = c^{\ast}} \right\} \right)} = 1}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------ --

###### Proof. 

Recall that $\sigma^{\ast}$ denotes the optimal path, and that ${\lim_{n\rightarrow\infty}\sigma_{n}} = \sigma^{\ast}$ holds surely. By Lemma 55 ‣ Sampling-based Algorithms for Optimal Motion Planning"), ${\lim_{n\rightarrow\infty}{\|{\sigma_{n}^{\prime} - \sigma_{n}}\|}_{BV}} = 0$ holds with probability one. Thus, by repeated application of the triangle inequality, ${{\lim_{n\rightarrow\infty}{\|{\sigma_{n}^{\prime} - \sigma^{\ast}}\|}_{BV}} = 0},$ i.e.,

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     $${{{\mathbb{P}}\hspace{0pt}\left( {\left\{ \lim\limits_{n\rightarrow\infty} \right\|\left. {{\sigma_{n}^{\prime} - {\sigma^{\ast}\parallel}_{BV}} = 0} \right\}} \right)} = 1}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

Then, by the robustness of the optimal path $\sigma^{\ast}$, it follows that

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     $${{{\mathbb{P}}\hspace{0pt}\left( \left\{ {{\lim\limits_{n\rightarrow\infty}{c\hspace{0pt}{(\sigma_{n}^{\prime})}}} = c^{\ast}} \right\} \right)} = 1}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------ --

That is the costs of the paths ${\{\sigma_{n}^{\prime}\}}_{n \in {\mathbb{N}}}$ converges to the optimal cost almost surely, as the number of samples approaches infinity. ∎∎

## Appendix D Proof of Theorem 35 ‣ 4.2.2 Proposed algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning") (Asymptotic Optimality of $k$-nearest PRM^∗^) 

The proof of this theorem is similar to that of Theorem 34 ‣ 4.2.2 Proposed algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning"). For the reader's convenience, a complete proof is provided at the expense of repeating some of the arguments.

### D.1 Outline of the proof 

Let $\sigma^{\ast}$ be a robust optimal path with weak $\delta$-clearance. First, define the sequence ${\{\sigma_{n}\}}_{n \in {\mathbb{N}}}$ of paths as in the proof of Theorem 34 ‣ 4.2.2 Proposed algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning").

Second, define a sequence ${\{ q_{n}\}}_{n \in {\mathbb{N}}}$ and tile $\sigma_{n}$ with a set $B_{n} = {\{ B_{n,1},B_{n,2},\ldots,B_{n,M}\}}$ of overlapping balls of radius $q_{n}$. See Figures 23 ‣ Sampling-based Algorithms for Optimal Motion Planning") and 26 ‣ Sampling-based Algorithms for Optimal Motion Planning"). Let $x_{m} \in B_{n,m}$ and $x_{m + 1} \in B_{n,{m + 1}}$ be any two points from subsequent balls in $B_{n}$. Construct $B_{n}$ such that the straight path connecting $x_{m}$ and $x_{m + 1}$ lies entirely inside the obstacle free space. Also, construct a set $B_{n}^{\prime}$ of balls such that (i) $B_{n,m}^{\prime}$ and $B_{n,m}$ are centered at the same point and (ii) $B_{n,m}$ contains $B_{n,m}$, and $B_{n,{m + 1}}$, for all $m \in {\{ 1,2,\ldots,{M_{n} - 1}\}}$.

Let $A_{n}$ denote the event that each ball in $B_{n}$ contains at least one vertex, and $A_{n}^{\prime}$ denote the event that each ball in $B_{n}^{\prime}$ contains at most $k\hspace{0pt}{(n)}$ vertices of the graph returned by the $k$-nearest PRM^∗^ algorithm. Third, show that $A_{n}$ and $A_{n}^{\prime}$ occur together for all large $n$, with probability one. Clearly, this implies that the PRM^∗^ algorithm will connect vertices in subsequent ball in $B_{n}$ with an edge, and any path formed by connecting such vertices will be collision-free.

Finally, show that any sequence of paths formed in this way converges to $\sigma^{\ast}$. Using the robustness of $\sigma^{\ast}$, show that the best path in the graph returned by the $k$-nearest PRM^∗^ algorithm converges to $c\hspace{0pt}{(\sigma^{\ast})}$ almost surely.

### D.2 Construction of the sequence ${\{\sigma_{n}\}}_{n \in {\mathbb{N}}}$ of paths 

Let ${\theta_{1},\theta_{2}} \in {\mathbb{R}}_{> 0}$ be two constants, the precise values of which will be provided shortly. Define

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     $${\delta_{n}:={\min\left\{ \delta,{{({1 + \theta_{1}})}\hspace{0pt}\left( \frac{{({1 + {1/d} + \theta_{2}})}\hspace{0pt}\mu\hspace{0pt}{(X_{free})}}{\zeta_{d}} \right)^{1/d}\hspace{0pt}\left( \frac{\log n}{n} \right)^{1/d}} \right\}}}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

Since ${\lim_{n\rightarrow\infty}\delta_{n}} = 0$ and $0 \leq \delta_{n} \leq \delta$ for all $n \in {\mathbb{N}}$, by Lemma 50 ‣ Sampling-based Algorithms for Optimal Motion Planning"), there exists a sequence ${\{\sigma_{n}\}}_{n \in {\mathbb{N}}}$ of paths such that ${\lim_{n\rightarrow\infty}\sigma_{n}} = \sigma^{\ast}$ and $\sigma_{n}$ is strongly $\delta_{n}$-clear for all $n \in {\mathbb{N}}$.

### D.3 Construction of the sequence ${\{ B_{n}\}}_{n \in {\mathbb{N}}}$ of sets of balls 

Define

  -- ------------------------------------------------- --
     $${q_{n}:=\frac{\delta_{n}}{1 + \theta_{1}}}.$$   
  -- ------------------------------------------------- --

For each $n \in {\mathbb{N}}$, use Definition 51 ‣ C.3 Construction of the sequence {𝐵_𝑛}_{𝑛∈ℕ} of sets of balls ‣ Appendix C Proof of Theorem 34 (Asymptotic optimality of PRM∗) ‣ Sampling-based Algorithms for Optimal Motion Planning") to construct a set $B_{n} = {\{ B_{n,1},B_{n,2},\ldots,B_{n,M_{n}}\}}$ of overlapping balls that collectively cover $\sigma_{n}$ as $B_{n}:={{\mathtt{C}\mathtt{o}\mathtt{v}\mathtt{e}\mathtt{r}\mathtt{i}\mathtt{n}\mathtt{g}\mathtt{B}\mathtt{a}\mathtt{l}\mathtt{l}\mathtt{s}}\hspace{0pt}{(\sigma_{n},q_{n},{\theta_{1}\hspace{0pt}q_{n}})}}$ (see Figures 23 ‣ Sampling-based Algorithms for Optimal Motion Planning") and 26 ‣ Sampling-based Algorithms for Optimal Motion Planning") for an illustration).

Figure 26: An illustration of the covering balls for the k-nearest PRM∗ algorithm. The δn ball is guaranteed to contain the balls Bn, m and Bn, m + 1.

### D.4 The probability that each ball in $B_{n}$ contains at least one vertex 

Recall that $G_{n}^{k\hspace{0pt}{PRM}^{\ast}} = {(V_{n}^{k\hspace{0pt}{PRM}^{\ast}},E_{n}^{k\hspace{0pt}{PRM}^{\ast}})}$ denotes the graph returned by the $k$-nearest PRM^∗^ algorithm, when the algorithm is run with $n$ samples. Let $A_{n,m}$ denote the event that the ball $B_{n,m}$ contains at least one vertex from $V_{n}^{k\hspace{0pt}{PRM}^{\ast}}$, i.e., $A_{n,m} = \left\{ {{B_{n,m} \cap V_{n}^{k\hspace{0pt}{PRM}^{\ast}}} \neq \varnothing} \right\}$. Let $A_{n}$ denote the event that all balls in $B_{n,m}$ contains at least one vertex of $G_{n}^{k\hspace{0pt}{PRM}^{\ast}}$, i.e., $A_{n} = {\bigcap_{m = 1}^{M_{n}}A_{n,m}}$.

Recall that $A_{n}^{c}$ denotes the complement of the event $A_{n}$, $\mu\hspace{0pt}{( \cdot )}$ denotes the Lebesgue measure, and $\zeta_{d}$ is the volume of the unit ball in the $d$-dimensional Euclidean space. Let $s_{n}$ denote the length of $\sigma_{n}$.

###### Lemma 57 

For all ${\theta_{1},\theta_{2}} > 0$,

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}{(A_{n}^{c})}} \leq {\frac{s_{n}}{\theta_{1}}\hspace{0pt}\left( \frac{\zeta_{d}}{\theta_{1}\hspace{0pt}{({1 + {1/d} + \theta_{2}})}\hspace{0pt}\mu\hspace{0pt}{(X_{free})}} \right)^{1/d}\hspace{0pt}\frac{1}{{({\log n})}^{1/d}\hspace{0pt}n^{1 + \theta_{2}}}}}.$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

In particular, ${\sum_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}{(A_{n}^{c})}}} < \infty$ for all ${\theta_{1},\theta_{2}} > 0$.

###### Proof. 

Let $n_{0} \in {\mathbb{N}}$ be a number for which $\delta_{n} < \delta$ for all $n > n_{0}$. A bound on the number of balls in $B_{n}$ can computed as follows. For all $n > n_{0}$,

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${M_{n} = {|B_{n}|} \leq \frac{s_{n}}{\theta_{1}\hspace{0pt}q_{n}} = {\frac{s_{n}}{\theta_{1}}\hspace{0pt}\left( \frac{\zeta_{d}}{{({1 + {1/d} + \theta_{2}})}\hspace{0pt}\mu\hspace{0pt}{(X_{free})}} \right)^{1/d}\hspace{0pt}\left( \frac{n}{\log n} \right)^{1/d}}}.$$   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

The volume of each ball $B_{n}$ can be computed as

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\mu\hspace{0pt}{(B_{n,m})}} = {\zeta_{d}\hspace{0pt}{(q_{n})}^{d}} = {{({1 + {1/d} + \theta_{2}})}\hspace{0pt}\mu\hspace{0pt}{(X_{free})}\hspace{0pt}\frac{\log n}{n}}}.$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

The probability that the ball $B_{n,m}$ does not contain a vertex of the $k$-nearest PRM^∗^ algorithm can be bounded as

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     ${{{\mathbb{P}}\hspace{0pt}{(A_{n,m}^{c})}} = \left( {1 - \frac{\mu\hspace{0pt}{(B_{n,m})}}{\mu\hspace{0pt}{(X_{free})}}} \right)^{n} = \left( {1 - {{({1 + {1/d} + \theta_{2}})}\hspace{0pt}\frac{\log n}{n}}} \right)^{n} \leq n^{- {({1 + {1/d} + \theta_{2}})}}}.$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

Finally, the probability that at least one of the balls in $B_{n}$ contains no vertex of the $k$-nearest PRM^∗^ can be bounded as

  -- ------------------------------------- -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     ${\mathbb{P}}\hspace{0pt}{(A_{n})}$   $=$      ${{\mathbb{P}}\hspace{0pt}\left( {\bigcup_{m = 1}^{M_{n}}A_{n,m}} \right)} \leq {\sum\limits_{m = 1}^{M_{n}}{{\mathbb{P}}\hspace{0pt}{(A_{n,m})}}} = {M_{n}\hspace{0pt}{\mathbb{P}}\hspace{0pt}{(A_{n,1})}}$                                      
                                           $\leq$   $\frac{s_{n}}{\theta_{1}}\hspace{0pt}\left( \frac{\zeta_{d}}{{({1 + {1/d} + \theta_{2}})}\hspace{0pt}\mu\hspace{0pt}{(X_{free})}} \right)^{1/d}\hspace{0pt}\left( \frac{n}{\log n} \right)^{1/d}\hspace{0pt}n^{- {({1 + {1/d} + \theta_{2}})}}$   
                                           $=$      ${\frac{s_{n}}{\theta_{1}}\hspace{0pt}\left( \frac{\zeta_{d}}{{({1 + {1/d} + \theta_{2}})}\hspace{0pt}\mu\hspace{0pt}{(X_{free})}} \right)^{1/d}\hspace{0pt}\frac{1}{{({\log n})}^{1/d}\hspace{0pt}n^{1 + \theta_{2}}}}.$                         
  -- ------------------------------------- -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Clearly, ${\sum_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}{(A_{n}^{c})}}} < \infty$ for all ${\theta_{1},\theta_{2}} > 0$. ∎∎

### D.5 Construction of the sequence ${\{ B_{n}^{\prime}\}}_{n \in {\mathbb{N}}}$ of sets of balls 

Construct a set $B_{n}^{\prime} = {\{ B_{n,1},B_{n,2},\ldots,B_{n,M_{n}}\}}$ of balls as $B_{n}^{\prime}:={{\mathtt{C}\mathtt{o}\mathtt{v}\mathtt{e}\mathtt{r}\mathtt{i}\mathtt{n}\mathtt{g}\mathtt{B}\mathtt{a}\mathtt{l}\mathtt{l}\mathtt{s}}\hspace{0pt}{(\sigma_{n},\delta_{n},{\theta_{1}\hspace{0pt}q_{n}})}}$ so that each ball in $B_{n}^{\prime}$ has radius $\delta_{n}$ and the spacing between two balls is $\theta_{1}\hspace{0pt}q_{n}$ (see Figure 26 ‣ Sampling-based Algorithms for Optimal Motion Planning")).

Clearly, the centers of balls in $B_{n}^{\prime}$ coincide with the centers of the balls in $B_{n}$, i.e., the center of $B_{n,m}^{\prime}$ is the same as the center of $B_{n,m}$ for all $m \in {\{ 1,2,\ldots,M_{n}\}}$ and all $n \in {\mathbb{N}}$. However, the balls in $B_{n}^{\prime}$ have a larger radius than those in $B_{n}$.

### D.6 The probability that each ball in $B_{n}^{\prime}$ contains at most $k\hspace{0pt}{(n)}$ vertices 

Recall that the $k$-nearest PRM algorithm connects each vertex in the graph with its $k\hspace{0pt}{(n)}$ nearest vertices when the algorithm is run with $n$ samples, where ${k\hspace{0pt}{(n)}} = {k_{PRM}\hspace{0pt}{\log n}}$. Let $A_{n}^{\prime}$ denote the event that all balls in $B_{n}^{\prime}$ contain at most $k\hspace{0pt}{(n)}$ vertices of $G_{n}^{k\hspace{0pt}{PRM}^{\ast}}$.

Recall that $A_{n}^{\prime c}$ denotes the complement of the event $A_{n}$.

###### Lemma 58 

If $k_{PRM} > {e\hspace{0pt}{({1 + {1/d}})}}$, then there exists some ${\theta_{1},\theta_{2}} > 0$ such that

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}{(A_{n}^{\prime c})}} \leq {\frac{s_{n}}{\theta_{1}}\hspace{0pt}\left( \frac{\zeta_{d}}{{({1 + {1/d} + \theta_{2}})}\hspace{0pt}\mu\hspace{0pt}{(X_{free})}} \right)^{1/d}\hspace{0pt}\frac{1}{{({\log n})}^{1/d}\hspace{0pt}n^{- {{({1 + \theta_{1}})}^{d}\hspace{0pt}{({1 + {1/d} + \theta_{2}})}}}}}}.$$   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

In particular, ${\sum_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}{(A_{n}^{\prime c})}}} < \infty$ for some ${\theta_{1},\theta_{2}} > 0$.

###### Proof. 

Let $n_{0} \in {\mathbb{N}}$ be a number for which $\delta_{n} < \delta$ for all $n > n_{0}$. As shown in the proof of Lemma 57 ‣ Sampling-based Algorithms for Optimal Motion Planning"), the number of balls in $B_{n}^{\prime}$ satisfies

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${M_{n} = {|B_{n}^{\prime}|} \leq \frac{s_{n}}{\theta_{1}\hspace{0pt}q_{n}} = {\frac{s_{n}}{\theta_{1}}\hspace{0pt}\left( \frac{\zeta_{d}}{{({1 + {1/d} + \theta_{2}})}\hspace{0pt}\mu\hspace{0pt}{(X_{free})}} \right)^{1/d}\hspace{0pt}\left( \frac{n}{\log n} \right)^{1/d}}}.$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

For all $n > n_{0}$, the volume of $B_{n,m}^{\prime}$ can be computed as

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\mu\hspace{0pt}{(B_{n,m}^{\prime})}} = {\zeta_{d}\hspace{0pt}{(\delta_{n})}^{d}} = {{({1 + \theta_{1}})}^{d}\hspace{0pt}{({1 + {1/d} + \theta_{2}})}\hspace{0pt}\mu\hspace{0pt}{(X_{free})}\hspace{0pt}\frac{\log n}{n}}}.$$   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Let $I_{n,m,i}$ denote the indicator random variable of the event that sample $i$ falls into ball $B_{n,m}^{\prime}$. The expected value of $I_{n,m,i}$ can be computed as

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{E}}\hspace{0pt}{\lbrack I_{n,m,i}\rbrack}} = \frac{\mu\hspace{0pt}{(B_{n,m}^{\prime})}}{\mu\hspace{0pt}{(X_{free})}} = {{({1 + \theta_{1}})}^{d}\hspace{0pt}{({1 + {1/d} + \theta_{2}})}\hspace{0pt}\frac{\log n}{n}}}.$$   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Let $N_{n,m}$ denote the number of vertices that fall inside the ball $B_{n,m}^{\prime}$, i.e., $N_{n,m} = {\sum_{i = 1}^{n}I_{n,m,i}}$. Then,

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{E}}\hspace{0pt}{\lbrack N_{n,m}\rbrack}} = {\sum\limits_{i = 1}^{n}{{\mathbb{E}}\hspace{0pt}{\lbrack I_{n,m,i}\rbrack}}} = {n\hspace{0pt}{\mathbb{E}}\hspace{0pt}{\lbrack I_{n,m,1}\rbrack}} = {{({1 + \theta_{1}})}^{d}\hspace{0pt}{({1 + {1/d} + \theta_{2}})}\hspace{0pt}{\log n}}}.$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Since ${\{ I_{n,m,i}\}}_{i = 1}^{n}$ are independent identically distributed random variables, large deviations of their sum, $M_{n,m}$, can be bounded by the following Chernoff bound (Dubhashi and Panconesi, 2009):

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( \left\{ {N_{n,m} > {{({1 + \epsilon})}\hspace{0pt}{\mathbb{E}}\hspace{0pt}{\lbrack N_{n,m}\rbrack}}} \right\} \right)} \leq \left( \frac{e^{\epsilon}}{{({1 + \epsilon})}^{({1 + \epsilon})}} \right)^{{\mathbb{E}}\hspace{0pt}{\lbrack N_{n,m}\rbrack}}},$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

for all $\epsilon > 0$. In particular, for $\epsilon = {e - 1}$,

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( \left\{ {N_{n,m} > {e\hspace{0pt}{\mathbb{E}}\hspace{0pt}{\lbrack N_{n,m}\rbrack}}} \right\} \right)} \leq e^{- {{\mathbb{E}}\hspace{0pt}{\lbrack N_{n,m}\rbrack}}} = e^{- {{({1 + \theta_{1}})}^{d}\hspace{0pt}{({1 + {1/d} + \theta_{2}})}\hspace{0pt}{\log n}}} = n^{- {{({1 + \theta_{1}})}^{d}\hspace{0pt}{({1 + {1/d} + \theta_{2}})}}}}.$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Since ${k\hspace{0pt}{(n)}} > {e\hspace{0pt}{({1 + {1/d}})}\hspace{0pt}{\log n}}$, there exists some ${\theta_{1},\theta_{2}} > 0$ independent of $n$ such that ${{e\hspace{0pt}{\mathbb{E}}\hspace{0pt}{\lbrack N_{n,k}\rbrack}} = {e\hspace{0pt}{({1 + \theta_{1}})}\hspace{0pt}{({1 + {1/d} + \theta_{2}})}\hspace{0pt}{\log n}} \leq {k\hspace{0pt}{(n)}}}.$ Then, for the same values of $\theta_{1}$ and $\theta_{2}$,

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( \left\{ {N_{n,m} > {k\hspace{0pt}{(n)}}} \right\} \right)} \leq {{\mathbb{P}}\hspace{0pt}\left( \left\{ {N_{n,m} > {e\hspace{0pt}{\mathbb{E}}\hspace{0pt}{\lbrack N_{n,m}\rbrack}}} \right\} \right)} \leq n^{- {{({1 + \theta_{1}})}^{d}\hspace{0pt}{({1 + {1/d} + \theta_{2}})}}}}.$$   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Finally, consider the probability of the event that at least one ball in $B_{n}$ contains more than $k\hspace{0pt}{(n)}$ nodes. Using the union bound together with the inequality above

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     ${{\mathbb{P}}\hspace{0pt}\left( {\bigcup_{m = 1}^{M_{n}}\left\{ {N_{n,m} > {k\hspace{0pt}{(n)}}} \right\}} \right)} \leq {\sum\limits_{m = 1}^{M_{n}}{{\mathbb{P}}\hspace{0pt}\left( \left\{ {N_{n,m} > {k\hspace{0pt}{(n)}}} \right\} \right)}} = {M_{n}\hspace{0pt}{\mathbb{P}}\hspace{0pt}\left( {\{{N_{n,1} > {k\hspace{0pt}{(n)}}}\}} \right)}$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Hence,

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}{(A_{n}^{\prime c})}} = {{\mathbb{P}}\hspace{0pt}\left( {\bigcup_{m = 1}^{M_{n}}\left\{ {N_{n,m} > {k\hspace{0pt}{(n)}}} \right\}} \right)} \leq {\frac{s_{n}}{\theta_{1}}\hspace{0pt}\left( \frac{\zeta_{d}}{{({1 + {1/d} + \theta_{2}})}\hspace{0pt}\mu\hspace{0pt}{(X_{free})}} \right)^{1/d}\hspace{0pt}\frac{1}{{({\log n})}^{1/d}\hspace{0pt}n^{- {{({1 + \theta_{1}})}^{d}\hspace{0pt}{({1 + {1/d} + \theta_{2}})}}}}}}.$$   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Clearly, ${\sum_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}{(A_{n}^{\prime c})}}} < \infty$ for the same values of $\theta_{1}$ and $\theta_{2}$. ∎∎

### D.7 Connecting the vertices in the subsequent balls in $B_{n}$ 

First, note the following lemma.

###### Lemma 59 

If $k_{PRM} > {e\hspace{0pt}{({1 + {1/d}})}^{1/d}}$, then there exists ${\theta_{1},\theta_{2}} > 0$ such that the event that each ball in $B_{n}$ contains at least one vertex and each ball in $B_{n}^{\prime}$ contains at most $k\hspace{0pt}{(n)}$ vertices occurs for all large $n$, with probability one, i.e.,

  -- ------------------------------------------------------------------------------------------------------------------------------------------ --
     $${{{\mathbb{P}}\hspace{0pt}\left( {\operatorname{lim\ inf}\limits_{n\rightarrow\infty}{({A_{n} \cap A_{n}^{\prime}})}} \right)} = 1}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------ --

###### Proof. 

Consider the event $A_{n}^{c} \cup A_{n}^{\prime c}$, which is the complement of $A_{n} \cap A_{n}^{\prime}$. Using the union bound,

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( {A_{n}^{c} \cup A_{n}^{\prime c}} \right)} \leq {{{\mathbb{P}}\hspace{0pt}{(A_{n}^{c})}} + {{\mathbb{P}}\hspace{0pt}{(A_{n}^{\prime c})}}}}.$$   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Summing both sides,

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\sum\limits_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}{({A_{n}^{c} \cup A_{N}^{\prime c}})}}} \leq {{\sum\limits_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}{(A_{n}^{c})}}} + {\sum\limits_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}{(A_{n}^{\prime c})}}}} < \infty},$$   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

where the last inequality follows from Lemmas 57 ‣ Sampling-based Algorithms for Optimal Motion Planning") and 58 vertices ‣ Appendix D Proof of Theorem 35 (Asymptotic Optimality of 𝑘-nearest PRM∗) ‣ Sampling-based Algorithms for Optimal Motion Planning"). Then, by the Borel-Cantelli lemma, ${{\mathbb{P}}\hspace{0pt}\left( {\operatorname{lim\ sup}_{n\rightarrow\infty}{({A_{n}^{c} \cup A_{n}^{\prime c}})}} \right)} = {{\mathbb{P}}\hspace{0pt}\left( {\operatorname{lim\ sup}_{n\rightarrow\infty}{({A_{n} \cap A_{n}^{\prime}})}^{c}} \right)} = 0$, which implies ${{\mathbb{P}}\hspace{0pt}\left( {\operatorname{lim\ inf}_{n\rightarrow\infty}{({A_{n} \cap A_{n}^{\prime}})}} \right)} = 1$. ∎∎

Note that for each $m \in {\{ 1,2,\ldots,{M_{n} - 1}\}}$, both $B_{n,m}$ and $B_{n,{m + 1}}$ lies entirely inside the ball $B_{n,m}^{\prime}$ (see Figure 26 ‣ Sampling-based Algorithms for Optimal Motion Planning")). Hence, whenever the balls $B_{n,m}$ and $B_{n,{m + 1}}$ contain at least one vertex each, and $B_{n,m}^{\prime}$ contains at most $k\hspace{0pt}{(n)}$ vertices, the $k$-nearest PRM^∗^ algorithm attempts to connect all vertices in $B_{n,m}$ and $B_{n,{m + 1}}$ with one another.

The following lemma guarantees that connecting any two points from two consecutive balls in $B_{n}$ results in a collision-free trajectory. The proof of the lemma is essentially the same as that of Lemma 54 ‣ Sampling-based Algorithms for Optimal Motion Planning").

###### Lemma 60 

For all $n \in {\mathbb{N}}$ and all $m \in {\{ 1,2,\ldots,M_{n}\}}$, if $x_{m} \in B_{n,m}$ and $x_{m + 1} \in B_{n,{m + 1}}$, then the line segment connecting $x_{m}$ and $x_{m + 1}$ lies in the obstacle-free space, i.e.,

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{{\alpha\hspace{0pt}x_{m}} + {{({1 - \alpha})}\hspace{0pt}x_{m + 1}}} \in X_{free}},{{\text{~for all~}\hspace{0pt}\alpha} \in {\lbrack 0,1\rbrack}}}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------- --

### D.8 Convergence to the optimal path 

The proof of the following lemma is similar to that of Lemma 55 ‣ Sampling-based Algorithms for Optimal Motion Planning"), and is omitted here.

Let $P_{n}$ denote the set of all paths in the graph returned by $k\hspace{0pt}\text{-}\hspace{0pt}{PRM}^{\ast}$ algorithm at the end of $n$ iterations. Let $\sigma_{n}^{\prime}$ be the path that is closest to $\sigma_{n}$ in terms of the bounded variation norm among all those paths in $P_{n}$, i.e., ${\sigma_{n}^{\prime}:={\min_{\sigma^{\prime} \in P_{n}}{\|{\sigma^{\prime} - \sigma_{n}}\|}}}.$

###### Lemma 61 

The random variable ${\|{\sigma_{n}^{\prime} - \sigma_{n}}\|}_{BV}$ converges to zero almost surely, i.e.,

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( {\left\{ \lim_{n\rightarrow\infty} \right\|\left. {{\sigma_{n}^{\prime} - {\sigma_{n}\parallel}_{BV}} = 0} \right\}} \right)} = 1}.$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

A corollary of the lemma above is that ${\lim_{n\rightarrow\infty}\sigma_{n}^{\prime}} = \sigma^{\ast}$ with probability one. Then, the result follows by the robustness of the optimal solution (see the proof of Lemma 56 ‣ Sampling-based Algorithms for Optimal Motion Planning") for details).

## Appendix E Proof of Theorem 36 ‣ 4.2.2 Proposed algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning") (Asymptotic optimality of RRG) 

### E.1 Outline of the proof 

The proof of this theorem is similar to that of Theorem 34 ‣ 4.2.2 Proposed algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning"). The main difference is the definition of $C_{n}$ that denotes the event that the RRG algorithm has sufficiently explored the obstacle free space. More precisely, $C_{n}$ is the event that for any point $x$ in the obstacle free space, the graph maintained by the RRG algorithm algorithm includes a vertex that can be connected to $x$.

Construct the sequence ${\{\sigma_{n}\}}_{n \in {\mathbb{N}}}$ of paths and the sequence ${\{ B_{n}\}}_{n \in {\mathbb{N}}}$ of balls as in the proof of Theorem 34 ‣ 4.2.2 Proposed algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning"). Let $A_{n}$ denote the event that each ball in $B_{n}$ contains a vertex of the graph maintained by the RRG by the end of iteration $n$. Compute $n$ by conditioning on the event that $C_{i}$ holds for all $i \in {\{{\lfloor{\theta_{3}\hspace{0pt}n}\rfloor},\ldots,n\}}$, where $0 < \theta_{3} < 1$ is a constant. Show that the probability that $C_{i}$ fails to occur for any such $i$ is small enough to guarantee that $A_{n}$ occurs for all large $n$ with probability one. Complete the proof as in the proof of Theorem 34 ‣ 4.2.2 Proposed algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning").

### E.2 Definitions of ${\{\sigma_{n}\}}_{n \in {\mathbb{N}}}$ and ${\{ B_{n}\}}_{n \in {\mathbb{N}}}$ 

Let $\theta_{1} > 0$ be a constant. Define $\delta_{n}$, $\sigma_{n}$, $q_{n}$, and $B_{n}$ as in the proof of Theorem 34 ‣ 4.2.2 Proposed algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning").

### E.3 Probability that each ball in $B_{n}$ contains at least one vertex 

Let $A_{n,m}$ be the event that the ball $B_{n,m}$ contains at least one vertex of the RRG at the end of $n$ iterations. Let $A_{n}$ be the event that all balls in $B_{n}$ contain at least one vertex of the RRG at the end of iteration $n$, i.e., $A_{n} = {\bigcap_{m = 1}^{M_{n}}A_{n,m}}$, where $M_{n}$ is the number of balls in $B_{n}$. Recall that $\gamma_{RRG}$ is the constant used in defining the connection radius of the RRG algorithm (see Algorithm 5: ‣ 3.3 Proposed algorithms ‣ 3 Algorithms ‣ Sampling-based Algorithms for Optimal Motion Planning")).

###### Lemma 62 

If $\gamma_{RRG} > {2\hspace{0pt}{({1 + {1/d}})}^{1/d}\hspace{0pt}\left( \frac{\mu\hspace{0pt}{(X_{free})}}{\zeta_{d}} \right)^{1/d}}$ then there exists $\theta_{1} > 0$ such that $A_{n}$ occurs for all large $n$ with probability one, i.e.,

  -- --------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( {\operatorname{lim\ inf}_{n\rightarrow\infty}A_{n}} \right)} = 1}.$$   
  -- --------------------------------------------------------------------------------------------------------- --

The proof of this lemma requires two intermediate results, which are provided next.

Recall that $\eta$ is the parameter used in the $\mathtt{S}\mathtt{t}\mathtt{e}\mathtt{e}\mathtt{r}$ procedure (see the definition of Steer procedure in Section 3.1). Let $C_{n}$ denote the event that for any point $x \in X_{free}$, the graph returned by the RRG algorithm includes a vertex $v$ such that ${\|{x - v}\|} \leq \eta$ and the line segment joining $v$ and $x$ is collision-free. The following lemma establishes an bound on the probability that this event fails to occur at iteration $n$.

###### Lemma 63 

There exists constants ${a,b} \in {\mathbb{R}}_{> 0}$ such that ${P\hspace{0pt}{(C_{n}^{c})}} \leq {a\hspace{0pt}e^{- {b\hspace{0pt}n}}}$ for all $n \in {\mathbb{N}}$.

###### Proof. 

Partition $X_{free}$ into finitely many convex sets such that each partition is bounded by a ball a radius $\eta$. Such a finite partition exists by the boundedness of $X_{free}$. Denote this partition by $X_{1}^{\prime},X_{2}^{\prime},\ldots,X_{M}^{\prime}$. Since the probability of failure decays to zero with an exponential rate, for any $m \in {\{ 1,2,\ldots,M\}}$, the probability that $X_{m}^{\prime}$ fails to contain a vertex of the RRG decays to zero with an exponential rate, i.e.,

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\mathbb{P}}\hspace{0pt}\left( \left\{ {{\nexists\hspace{0pt}x} \in {V_{n}^{RRG} \cap X_{m}^{\prime}}} \right\} \right)} \leq {a_{m}\hspace{0pt}e^{- {b_{m}\hspace{0pt}n}}}$$   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

The probability that at least one partition fails to contain one vertex of the RRG also decays to zero with an exponential rate. That is, there exists ${a,b} \in {\mathbb{R}}_{> 0}$ such that

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( {\bigcup_{m = 1}^{M}\left\{ {{\nexists\hspace{0pt}x} \in {V_{n}^{RRG} \cap X_{m}^{\prime}}} \right\}} \right)} \leq {\sum\limits_{m = 1}^{M}{{\mathbb{P}}\hspace{0pt}\left( \left\{ {{\nexists\hspace{0pt}x} \in {V_{n}^{RRG} \cap X_{m}^{\prime}}} \right\} \right)}} \leq {\sum\limits_{m = 1}^{M}{a_{m}\hspace{0pt}e^{- {b_{m}\hspace{0pt}n}}}} \leq {a\hspace{0pt}e^{- {b\hspace{0pt}n}}}},$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

where the first inequality follows from the union bound. ∎∎

Let $0 < \theta_{3} < 1$ be a constant independent of $n$. Consider the event that $C_{i}$ occurs for all $i$ that is greater than $\theta_{3}\hspace{0pt}n$, i.e., $\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}$. The following lemma analyzes the probability of the event that $\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}$ fails to occur.

###### Lemma 64 

For any $\theta_{3} \in {(0,1)}$,

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     $${{\sum\limits_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}\left( \left( {\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right)^{c} \right)}} < \infty}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

###### Proof. 

The following inequalities hold:

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\sum\limits_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}\left( \left( {\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right)^{c} \right)}} = {\sum\limits_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}\left( {\bigcup_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}^{c}} \right)}} \leq {\sum\limits_{n = 1}^{\infty}{\sum\limits_{i = {\lfloor{\theta_{3}\hspace{0pt}i}\rfloor}}^{n}{{\mathbb{P}}\hspace{0pt}{(C_{i}^{c})}}}} \leq {\sum\limits_{n = 1}^{\infty}{\sum\limits_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}{a\hspace{0pt}e^{- {b\hspace{0pt}i}}}}}},$$   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

where the last inequality follows from Lemma 63 ‣ Sampling-based Algorithms for Optimal Motion Planning"). The right-hand side is finite for all ${a,b} > 0$. ∎∎

###### Proof of Lemma 62 ‣ Sampling-based Algorithms for Optimal Motion Planning"). 

It is shown that ${\sum_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}\left( A_{n}^{c} \right)}} < \infty$, which, by the Borel-Cantelli Lemma (Grimmett and Stirzaker, 2001), implies that $A_{n}^{c}$ occurs infinitely often with probability zero, i.e., ${{\mathbb{P}}\hspace{0pt}{({\operatorname{lim\ sup}_{n\rightarrow\infty}A_{n}^{c}})}} = 0$, which in turn implies ${{\mathbb{P}}\hspace{0pt}{({\operatorname{lim\ inf}_{n\rightarrow\infty}A_{n}})}} = 1$.

Let $n_{0} \in {\mathbb{N}}$ be a number for which $\delta_{n} < \delta$ for all $n > n_{0}$. First, for all $n > n_{0}$, the number of balls in $B_{n}$ can be bounded by (see the proof of Lemma 52 ‣ Sampling-based Algorithms for Optimal Motion Planning") for details)

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${M_{n} = {|B_{n}|} \leq {\frac{{({2 + \theta_{1}})}\hspace{0pt}s_{n}}{\theta_{1}\hspace{0pt}\gamma_{RRG}}\hspace{0pt}\left( \frac{n}{\log n} \right)^{1/d}}}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Second, for all $n > n_{0}$, the volume of each ball in $B_{n}$ can be calculated as (see the proof of Lemma 52 ‣ Sampling-based Algorithms for Optimal Motion Planning"))

  -- ------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\mu\hspace{0pt}{(B_{n,m})}} = {\zeta_{d}\hspace{0pt}\left( \frac{\gamma_{PRM}}{2 + \theta_{1}} \right)^{d}\hspace{0pt}\frac{\log n}{n}}},$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------- --

where $\zeta_{d}$ is the volume of the unit ball in the $d$-dimensional Euclidean space.

Third, conditioning on the event $\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}$, each new sample will be added to the graph maintained by the RRG algorithm as a new vertex between iterations $i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}$ and $i = n$. Thus,

  -- ---------------------------------------------------------------------------------------------------------------------------------- -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     ${\mathbb{P}}\hspace{0pt}\left( A_{n,m}^{c} \middle| {\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right)$   $\leq$   $\left( {1 - \frac{\mu\hspace{0pt}{(B_{n,m})}}{\mu\hspace{0pt}{(X_{free})}}} \right)^{n - {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}} \leq \left( {1 - \frac{\mu\hspace{0pt}{(B_{n,m})}}{\mu\hspace{0pt}{(X_{free})}}} \right)^{{({1 - \theta_{3}})}\hspace{0pt}n}$                                                        
                                                                                                                                        $\leq$   $\left( {1 - {\frac{\zeta_{d}}{\mu\hspace{0pt}{(X_{free})}}\hspace{0pt}\left( \frac{\gamma_{RRG}}{2 + \theta_{1}} \right)^{d}\hspace{0pt}\frac{\log n}{n}}} \right)^{{({1 - \theta_{3}})}\hspace{0pt}n}$                                                                                                                  
                                                                                                                                        $\leq$   ${e^{- {\frac{{({1 - \theta_{3}})}\hspace{0pt}\zeta_{d}}{\mu\hspace{0pt}{(X_{free})}}\hspace{0pt}{(\frac{\gamma_{RRG}}{2 + \theta_{1}})}^{d}\hspace{0pt}{\log n}}} \leq n^{- {\frac{{({1 - \theta_{3}})}\hspace{0pt}\zeta_{d}}{\mu\hspace{0pt}{(X_{free})}}\hspace{0pt}{(\frac{\gamma_{RRG}}{2 + \theta_{1}})}^{d}}}},$   
  -- ---------------------------------------------------------------------------------------------------------------------------------- -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

where the fourth inequality follows from ${({1 - {{1/f}\hspace{0pt}{(n)}}})}^{g\hspace{0pt}{(n)}} \leq e^{{{g\hspace{0pt}{(n)}}/f}\hspace{0pt}{(n)}}$.

Fourth,

  -- -------------------------------------------------------------------------------------------------------------------------------- -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     ${\mathbb{P}}\hspace{0pt}\left( A_{n}^{c} \middle| {\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right)$   $\leq$   ${\mathbb{P}}\hspace{0pt}\left( {\bigcup_{m = 1}^{M_{n}}A_{n,m}^{c}} \middle| {\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right)$                                                                                                                                        
                                                                                                                                      $\leq$   $\sum\limits_{m = 1}^{M_{n}}{{\mathbb{P}}\hspace{0pt}\left( A_{n,m}^{c} \middle| {\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right)}$                                                                                                                                    
                                                                                                                                      $=$      $M_{n}\hspace{0pt}{\mathbb{P}}\hspace{0pt}\left( A_{n,1}^{c} \middle| {\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right)$                                                                                                                                                
                                                                                                                                      $\leq$   ${\frac{{({2 + \theta_{1}})}\hspace{0pt}s_{n}}{\theta_{1}\hspace{0pt}\gamma_{RRG}}\hspace{0pt}\left( \frac{n}{\log n} \right)^{1/d}\hspace{0pt}n^{- {\frac{{({1 - \theta_{3}})}\hspace{0pt}\zeta_{d}}{\mu\hspace{0pt}{(X_{free})}}\hspace{0pt}{(\frac{\gamma_{RRG}}{2 + \theta_{1}})}^{d}}}}.$   
  -- -------------------------------------------------------------------------------------------------------------------------------- -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

Hence,

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     $${{\sum\limits_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}\left( A_{n}^{c} \middle| {\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right)}} < \infty},$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

whenever ${{\frac{{({1 - \theta_{3}})}\hspace{0pt}\zeta_{d}}{\mu\hspace{0pt}{(X_{free})}}\hspace{0pt}\left( \frac{\gamma_{RRG}}{2 + \theta_{1}} \right)^{d}} - {1/d}} > 1$, i.e., $\gamma_{RRG} > {{({2 + \theta_{1}})}\hspace{0pt}{({1 + {1/d}})}^{1/d}\hspace{0pt}\left( \frac{\mu\hspace{0pt}{(X_{free})}}{{({1 - \theta_{3}})}\hspace{0pt}\zeta_{d}} \right)^{1/d}}$, which is satisfied by appropriately choosing the constants $\theta_{1}$ and $\theta_{3}$, since $\gamma_{RRG} > {2\hspace{0pt}{({1 + {1/d}})}^{1/d}\hspace{0pt}\left( \frac{\mu\hspace{0pt}{(X_{free})}}{\zeta_{d}} \right)^{1/d}}$.

Finally,

  -- -------------------------------------------------------------------------------------------------------------------------------- -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     ${\mathbb{P}}\hspace{0pt}\left( A_{n}^{c} \middle| {\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right)$   $=$      $\frac{{\mathbb{P}}\hspace{0pt}\left( {A_{n}^{c} \cap \left( {\cap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right)} \right)}{{\mathbb{P}}\hspace{0pt}\left( {\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right)}$   
                                                                                                                                      $\geq$   ${\mathbb{P}}\hspace{0pt}{({A_{n}^{c} \cap {({\cap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}})}})}$                                                                                                                                           
                                                                                                                                      $=$      $1 - {{\mathbb{P}}\hspace{0pt}{({A_{n} \cup {({\cap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}})}^{c}})}}$                                                                                                                                     
                                                                                                                                      $\geq$   $1 - {{\mathbb{P}}\hspace{0pt}{(A_{n})}} - {{\mathbb{P}}\hspace{0pt}\left( {({\cap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}})}^{c} \right)}$                                                                                                 
                                                                                                                                      $=$      ${{{\mathbb{P}}\hspace{0pt}{(A_{n}^{c})}} - {{\mathbb{P}}\hspace{0pt}\left( {({\cap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}})}^{c} \right)}}.$                                                                                              
  -- -------------------------------------------------------------------------------------------------------------------------------- -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

Taking the infinite sum of both sides yields

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\sum\limits_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}{(A_{n}^{c})}}} \leq {{\sum\limits_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}\left( A_{n}^{c} \middle| {\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{n}} \right)}} + {\sum\limits_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}\left( \left( {\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{n}} \right)^{c} \right)}}}}.$$   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

The first term on the right hand side is shown to be finite above. The second term is finite by Lemma 64 ‣ Sampling-based Algorithms for Optimal Motion Planning"). Hence, ${\sum_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}{(A_{n})}}} < \infty$. Then, by the Borel Cantelli lemma, $A_{n}^{c}$ occurs infinitely often with probability zero, which implies that its complement $A_{n}$ occurs for all large $n$, with probability one. ∎∎

### E.4 Convergence to the optimal path 

The proof of the following lemma is similar to that of Lemma 55 ‣ Sampling-based Algorithms for Optimal Motion Planning"), and is omitted here.

Let $P_{n}$ denote the set of all paths in the graph returned by $RRG$ algorithm at the end of $n$ iterations. Let $\sigma_{n}^{\prime}$ be the path that is closest to $\sigma_{n}$ in terms of the bounded variation norm among all those paths in $P_{n}$, i.e., ${\sigma_{n}^{\prime}:={\min_{\sigma^{\prime} \in P_{n}}{\|{\sigma^{\prime} - \sigma_{n}}\|}}}.$

###### Lemma 65 

The random variable ${\|{\sigma_{n}^{\prime} - \sigma_{n}}\|}_{BV}$ converges to zero almost surely, i.e.,

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( {\left\{ \lim_{n\rightarrow\infty} \right\|\left. {{\sigma_{n}^{\prime} - {\sigma_{n}\parallel}_{BV}} = 0} \right\}} \right)} = 1}.$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

A corollary of the lemma above is that ${\lim_{n\rightarrow\infty}\sigma_{n}^{\prime}} = \sigma^{\ast}$ with probability one. Then, the result follows by the robustness of the optimal solution (see the proof of Lemma 56 ‣ Sampling-based Algorithms for Optimal Motion Planning") for details).

## Appendix F Proof of Theorem 37 ‣ 4.2.2 Proposed algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning") (asymptotic optimality of $k$-nearest RRG) 

### F.1 Outline of the proof 

The proof of this theorem is a combination of that of Theorem 35 ‣ 4.2.2 Proposed algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning") and 36 ‣ 4.2.2 Proposed algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning").

Define the sequences ${\{\sigma_{n}\}}_{n \in {\mathbb{N}}}$, ${\{ B_{n}\}}_{n \in {\mathbb{N}}}$, and ${\{ B_{n}^{\prime}\}}_{n \in {\mathbb{N}}}$ as in the proof of Theorem 35 ‣ 4.2.2 Proposed algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning"). Define the event $C_{n}$ as in the proof of Theorem 36 ‣ 4.2.2 Proposed algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning"). Let $A_{n}$ denote the event that each ball in $B_{n}$ contains at least one vertex, and $A_{n}^{\prime}$ denote the event that each ball in $B_{n}^{\prime}$ contains at most $k\hspace{0pt}{(n)}$ vertices of the graph maintained by the RRG algorithm, by the end of iteration $n$. Compute $A_{n}$ and $A_{n}^{\prime}$ by conditioning on the event that $C_{i}$ holds for all $i = {\theta_{3}\hspace{0pt}n}$ to $n$. Show that this is enough to guarantee that $A_{n}$ and $A_{n}^{\prime}$ hold together for all large $n$, with probability one.

### F.2 Definitions of ${\{\sigma_{n}\}}_{n \in {\mathbb{N}}}$, ${\{ B_{n}\}}_{n \in {\mathbb{N}}}$, and ${\{ B_{n}^{\prime}\}}_{n \in {\mathbb{N}}}$ 

Let ${\theta_{1},\theta_{2}} > 0$ be two constants. Define $\delta_{n}$, $\sigma_{n}$, $q_{n}$, $B_{n}$, and $B_{n}^{\prime}$ as in the proof of Theorem 35 ‣ 4.2.2 Proposed algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning").

### F.3 The probability that each ball in $B_{n}$ contains at least one vertex 

Let $A_{n,m}$ denote the event that the ball $B_{n,m}$ contains at least one vertex of the graph maintained by the $k$-nearest RRG algorithm by the end of iteration $n$. Let $A_{n}$ denote the event that all balls in $B_{n,m}$ contain at least one vertex of the same graph, i.e., $A_{n} = {\bigcup_{m = 1}^{M_{n}}A_{n,m}}$. Let $s_{n}$ denote the length of $\sigma_{n}$, i.e., $T\hspace{0pt}V\hspace{0pt}{(\sigma_{n})}$. Recall $\eta$ is the parameter in the $\mathtt{S}\mathtt{t}\mathtt{e}\mathtt{e}\mathtt{r}$ procedure. Let $C_{n}$ denote the event that for any point $x \in X_{free}$, the $k$-nearest RRG algorithm includes a vertex $v$ such that ${\|{x - v}\|} \leq \eta$.

###### Lemma 66 

For any ${\theta_{1},\theta_{2}} > 0$ and any $\theta_{3} \in {(0,1)}$,

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( A_{n}^{c} \middle| {\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right)} \leq {\frac{s_{n}}{\theta_{1}}\hspace{0pt}\left( \frac{\zeta_{d}}{\theta_{1}\hspace{0pt}{({1 + {1/d} + \theta_{2}})}\hspace{0pt}\mu\hspace{0pt}{(X_{free})}} \right)^{1/d}\hspace{0pt}\frac{1}{{({\log n})}^{1/d}\hspace{0pt}n^{{{({1 - \theta_{3}})}\hspace{0pt}{({1 + {1/d} + \theta_{2}})}} - {1/d}}}}}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

In particular, ${\sum_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}{(\left. A_{n}^{c} \middle| {\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right.)}}} < \infty$ for any ${\theta_{1},\theta_{2}} > 0$ and some $\theta_{3} \in {(0,1)}$.

###### Proof. 

Let $n_{0} \in {\mathbb{N}}$ be a number for which $\delta_{n} < \delta$ for all $n > n_{0}$. Then, for all $n > n_{0}$,

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${M_{n} = {|B_{n}|} \leq \frac{s_{n}}{\theta_{1}\hspace{0pt}q_{n}} = {\frac{s_{n}}{\theta_{1}}\hspace{0pt}\left( \frac{\zeta_{d}}{{({1 + {1/d} + \theta_{2}})}\hspace{0pt}\mu\hspace{0pt}{(X_{free})}} \right)^{1/d}\hspace{0pt}\left( \frac{n}{\log n} \right)^{1/d}}}.$$   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

The volume of each ball $B_{n}$ can be computed as

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\mu\hspace{0pt}{(B_{n,m})}} = {\zeta_{d}\hspace{0pt}{(q_{n})}^{d}} = {{({1 + {1/d} + \theta_{2}})}\hspace{0pt}\mu\hspace{0pt}{(X_{free})}\hspace{0pt}\frac{\log n}{n}}}.$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Given $\bigcap_{i = {\lceil{\theta_{3}\hspace{0pt}n}\rceil}}^{n}C_{i}$, the probability that the ball $B_{n,m}$ does not contain a vertex of the $k$-nearest PRM^∗^ algorithm can be bounded as

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     ${{{\mathbb{P}}\hspace{0pt}\left( A_{n,m}^{c} \middle| {\bigcap_{i = {\lceil{\theta_{3}\hspace{0pt}n}\rceil}}^{n}C_{i}} \right)} = \left( {1 - \frac{\mu\hspace{0pt}{(B_{n,m})}}{\mu\hspace{0pt}{(X_{free})}}} \right)^{{({1 - \theta_{3}})}\hspace{0pt}n} = \left( {1 - {{({1 + {1/d} + \theta_{2}})}\hspace{0pt}\frac{\log n}{n}}} \right)^{{({1 - \theta_{3}})}\hspace{0pt}n} \leq n^{- {{({1 - \theta_{3}})}\hspace{0pt}{({1 + {1/d} + \theta_{2}})}}}}.$   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Finally, the probability that at least one of the balls in $B_{n}$ contains no vertex of the $k$-nearest PRM^∗^ can be bounded as

  -- ------------------------------------- -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     ${\mathbb{P}}\hspace{0pt}{(A_{n})}$   $=$      ${{\mathbb{P}}\hspace{0pt}\left( {\bigcup_{m = 1}^{M_{n}}A_{n,m}} \right)} \leq {\sum\limits_{m = 1}^{M_{n}}{{\mathbb{P}}\hspace{0pt}{(A_{n,m})}}} = {M_{n}\hspace{0pt}{\mathbb{P}}\hspace{0pt}{(A_{n,1})}}$                                                                        
                                           $\leq$   ${\frac{s_{n}}{\theta_{1}}\hspace{0pt}\left( \frac{\zeta_{d}}{{({1 + {1/d} + \theta_{2}})}\hspace{0pt}\mu\hspace{0pt}{(X_{free})}} \right)^{1/d}\hspace{0pt}\frac{1}{{({\log n})}^{1/d}\hspace{0pt}n^{{{({1 - \theta_{3}})}\hspace{0pt}{({1 + {1/d} + \theta_{2}})}} - {1/d}}}}.$   
  -- ------------------------------------- -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Clearly, for all ${\theta_{1},\theta_{2}} > 0$, there exists some $\theta_{3} \in {(0,1)}$ such that ${\sum_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}{(A_{n}^{c})}}} < \infty$. ∎∎

### F.4 The probability that each ball in $B_{n}^{\prime}$ contains at most $k\hspace{0pt}{(n)}$ vertices 

Let $A_{n}^{\prime}$ denote the event that all balls in $B_{n}^{\prime}$ contain at most $k\hspace{0pt}{(n)}$ vertices of the graph maintained by the RRG algorithm, by end of iteration $n$.

###### Lemma 67 

If $k_{PRM} > {e\hspace{0pt}{({1 + {1/d}})}}$, then there exists ${\theta_{1},\theta_{2},\theta_{3}} > 0$ such that

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( A_{n}^{\prime c} \middle| {\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right)} \leq {\frac{s_{n}}{\theta_{1}}\hspace{0pt}\left( \frac{\zeta_{d}}{{({1 + {1/d} + \theta_{2}})}\hspace{0pt}\mu\hspace{0pt}{(X_{free})}} \right)^{1/d}\hspace{0pt}\frac{1}{{({\log n})}^{1/d}\hspace{0pt}n^{- {{({1 - \theta_{3}})}\hspace{0pt}{({1 + \theta_{1}})}^{d}\hspace{0pt}{({1 + {1/d} + \theta_{2}})}}}}}}.$$   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

In particular, ${\sum_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}{(\left. A_{n}^{c} \middle| {\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right.)}}} < \infty$ for some ${\theta_{1},\theta_{2}} > 0$ and some $\theta_{3} > 0$.

###### Proof. 

Let $n_{0} \in {\mathbb{N}}$ be a number for which $\lambda_{n} < \delta$ for all $n > n_{0}$. Then, the number of balls in $B_{n}^{\prime}$ and the volume of each ball can be computed as

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${M_{n} = {|B_{n}^{\prime}|} \leq \frac{s_{n}}{\theta_{1}\hspace{0pt}q_{n}} = {\frac{s_{n}}{\theta_{1}}\hspace{0pt}\left( \frac{\zeta_{d}}{{({1 + {1/d} + \theta_{2}})}\hspace{0pt}\mu\hspace{0pt}{(X_{free})}} \right)^{1/d}\hspace{0pt}\left( \frac{n}{\log n} \right)^{1/d}}}.$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\mu\hspace{0pt}{(B_{n,m}^{\prime})}} = {\zeta_{d}\hspace{0pt}{(\lambda_{n})}^{d}} = {{({1 + \theta_{1}})}^{d}\hspace{0pt}{({1 + {1/d} + \theta_{2}})}\hspace{0pt}\mu\hspace{0pt}{(X_{free})}\hspace{0pt}\frac{\log n}{n}}}.$$   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Let $I_{n,m,i}$ denote the indicator random variable of the event that sample $i$ falls into ball $B_{n,m}^{\prime}$. The expected value of $I_{n,m,i}$ can be computed as

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{E}}\hspace{0pt}{\lbrack I_{n,m,i}\rbrack}} = \frac{\mu\hspace{0pt}{(B_{n,m}^{\prime})}}{\mu\hspace{0pt}{(X_{free})}} = {{({1 + \theta_{1}})}^{d}\hspace{0pt}{({1 + {1/d} + \theta_{2}})}\hspace{0pt}\frac{\log n}{n}}}.$$   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Let $N_{n,m}$ denote the number of vertices that fall inside the ball $B_{n,m}^{\prime}$ between iterations $\lfloor{\theta_{3}\hspace{0pt}n}\rfloor$ and $n$, i.e., $N_{n,m} = {\sum_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}I_{n,m,i}}$. Then,

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{E}}\hspace{0pt}{\lbrack N_{n,m}\rbrack}} = {\sum\limits_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}{{\mathbb{E}}\hspace{0pt}{\lbrack I_{n,m,i}\rbrack}}} = {{({1 - \theta_{3}})}\hspace{0pt}n\hspace{0pt}{\mathbb{E}}\hspace{0pt}{\lbrack I_{n,m,1}\rbrack}} = {{({1 - \theta_{3}})}\hspace{0pt}{({1 + \theta_{1}})}^{d}\hspace{0pt}{({1 + {1/d} + \theta_{2}})}\hspace{0pt}{\log n}}}.$$   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Since ${\{ I_{n,m,i}\}}_{i = 1}^{n}$ are independent identically distributed random variables, large deviations of their sum, $M_{n,m}$, can be bounded by the following Chernoff bound (Dubhashi and Panconesi, 2009):

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( \left\{ {N_{n,m} > {{({1 + \epsilon})}\hspace{0pt}{\mathbb{E}}\hspace{0pt}{\lbrack N_{n,m}\rbrack}}} \right\} \right)} \leq \left( \frac{e^{\epsilon}}{{({1 + \epsilon})}^{({1 + \epsilon})}} \right)^{{\mathbb{E}}\hspace{0pt}{\lbrack N_{n,m}\rbrack}}},$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

for all $\epsilon > 0$. In particular, for $\epsilon = {e - 1}$,

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( \left\{ {N_{n,m} > {e\hspace{0pt}{\mathbb{E}}\hspace{0pt}{\lbrack N_{n,m}\rbrack}}} \right\} \right)} \leq e^{- {{\mathbb{E}}\hspace{0pt}{\lbrack N_{n,m}\rbrack}}} = n^{- {{({1 - \theta_{3}})}\hspace{0pt}{({1 + \theta_{1}})}^{d}\hspace{0pt}{({1 + {1/d} + \theta_{2}})}}}}.$$   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Since ${k\hspace{0pt}{(n)}} > {e\hspace{0pt}{({1 + {1/d}})}\hspace{0pt}{\log n}}$, there exists some ${\theta_{1},\theta_{2}} > 0$ and $\theta_{3} \in {(0,1)}$, independent of $n$, such that ${{e\hspace{0pt}{\mathbb{E}}\hspace{0pt}{\lbrack N_{n,k}\rbrack}} = {e\hspace{0pt}{({1 - \theta_{3}})}\hspace{0pt}{({1 + \theta_{1}})}\hspace{0pt}{({1 + {1/d} + \theta_{2}})}\hspace{0pt}{\log n}} \leq {k\hspace{0pt}{(n)}}}.$ Then, for the same values of $\theta_{1}$ and $\theta_{2}$,

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     $${{{\mathbb{P}}\hspace{0pt}\left( \left\{ {N_{n,m} > {k\hspace{0pt}{(n)}}} \right\} \right)} \leq {{\mathbb{P}}\hspace{0pt}\left( \left\{ {N_{n,m} > {e\hspace{0pt}{\mathbb{E}}\hspace{0pt}{\lbrack N_{n,m}\rbrack}}} \right\} \right)} \leq n^{- {{({1 - \theta_{3}})}\hspace{0pt}{({1 + \theta_{1}})}^{d}\hspace{0pt}{({1 + {1/d} + \theta_{2}})}}}}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

Finally, consider the probability of the event that at least one ball in $B_{n}$ contains more than $k\hspace{0pt}{(n)}$ nodes. Using the union bound together with the inequality above

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     ${{\mathbb{P}}\hspace{0pt}\left( {\bigcup_{m = 1}^{M_{n}}\left\{ {N_{n,m} > {k\hspace{0pt}{(n)}}} \right\}} \right)} \leq {\sum\limits_{m = 1}^{M_{n}}{{\mathbb{P}}\hspace{0pt}\left( \left\{ {N_{n,m} > {k\hspace{0pt}{(n)}}} \right\} \right)}} = {M_{n}\hspace{0pt}{\mathbb{P}}\hspace{0pt}\left( {\{{N_{n,1} > {k\hspace{0pt}{(n)}}}\}} \right)}$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Hence,

  -- --------------------------------------------------------------------------------------------------------------------------------------- -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     ${\mathbb{P}}\hspace{0pt}\left( A_{n}^{\prime c} \middle| {\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right)$   $=$      ${\mathbb{P}}\hspace{0pt}\left( {\bigcup_{m = 1}^{M_{n}}\left\{ {N_{n,m} > {k\hspace{0pt}{(n)}}} \right\}} \right)$                                                                                                                                                                                               
                                                                                                                                             $\leq$   ${\frac{s_{n}}{\theta_{1}}\hspace{0pt}\left( \frac{\zeta_{d}}{{({1 + {1/d} + \theta_{2}})}\hspace{0pt}\mu\hspace{0pt}{(X_{free})}} \right)^{1/d}\hspace{0pt}\frac{1}{{({\log n})}^{1/d}\hspace{0pt}n^{- {{({1 - \theta_{3}})}\hspace{0pt}{({1 + \theta_{1}})}^{d}\hspace{0pt}{({1 + {1/d} + \theta_{2}})}}}}}.$   
  -- --------------------------------------------------------------------------------------------------------------------------------------- -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Clearly, ${\sum_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}\left( A_{n}^{\prime c} \middle| {\cap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right)}} < \infty$ for the same values of $\theta_{1}$, $\theta_{2}$, and $\theta_{3}$. ∎. ∎

### F.5 Connecting the vertices in subsequent balls in $B_{n}$ 

###### Lemma 68 

If $k_{PRM} > {e\hspace{0pt}{({1 + {1/d}})}^{1/d}}$, then there exists ${\theta_{1},\theta_{2}} > 0$ such that the event that each ball in $B_{n}$ contains at least one vertex and each ball in $B_{n}^{\prime}$ contains at most $k\hspace{0pt}{(n)}$ vertices occurs for all large $n$, with probability one, i.e.,

  -- ------------------------------------------------------------------------------------------------------------------------------------------ --
     $${{{\mathbb{P}}\hspace{0pt}\left( {\operatorname{lim\ inf}\limits_{n\rightarrow\infty}{({A_{n} \cap A_{n}^{\prime}})}} \right)} = 1}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------ --

First note the following lemma.

###### Lemma 69 

For any $\theta_{3} \in {(0,1)}$,

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     $${{\sum\limits_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}\left( \left( {\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{n}} \right)^{c} \right)}} < \infty}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

###### Proof. 

Since the RRG algorithm and the $k$-nearest RRG algorithm have the same vertex sets, i.e., $V_{n}^{RRG} = V_{n}^{k\hspace{0pt}{RRG}}$ surely for all $n \in {\mathbb{N}}$, the lemma follows from Lemma 64 ‣ Sampling-based Algorithms for Optimal Motion Planning"). ∎∎

###### Proof of Lemma 68 ‣ Sampling-based Algorithms for Optimal Motion Planning"). 

Note that

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------ -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     ${\mathbb{P}}\hspace{0pt}\left( {({A_{n}^{c} \cup A_{n}^{\prime c}})} \middle| {\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right)$   $=$      $\frac{{\mathbb{P}}\hspace{0pt}\left( {A_{n}^{c} \cap \left( {\cap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right)} \right)}{{\mathbb{P}}\hspace{0pt}\left( {\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right)}$   
                                                                                                                                                                  $\geq$   ${\mathbb{P}}\hspace{0pt}\left( {{({A_{n}^{c} \cup A_{n}^{\prime c}})} \cap \left( {\cap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right)} \right)$                                                                                         
                                                                                                                                                                  $\geq$   ${{{\mathbb{P}}\hspace{0pt}{({A_{n}^{c} \cup A_{n}^{\prime c}})}} - {{\mathbb{P}}\hspace{0pt}\left( {({\cap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}})}^{c} \right)}},$                                                                      
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------ -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

where the last inequality follows from the union bound. Rearranging and using the union bound,

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}{({A_{n}^{c} \cup A_{n}^{\prime c}})}} \leq {{{\mathbb{P}}\hspace{0pt}\left( A_{n}^{c} \middle| {\cap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right)} + {{\mathbb{P}}\hspace{0pt}\left( A_{n}^{c} \middle| {\cap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right)} + {{\mathbb{P}}\hspace{0pt}\left( \left( {\cap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right)^{c} \right)}}}.$$   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Summing both sides,

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\sum\limits_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}{({A_{n}^{c} \cup A_{n}^{\prime c}})}}} \leq {{\sum\limits_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}\left( A_{n}^{c} \middle| {\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right)}} + {\sum\limits_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}\left( A_{n}^{\prime c} \middle| {\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right)}} + {\sum\limits_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}\left( \left( {\bigcap_{i = {\lfloor{\theta_{3}\hspace{0pt}n}\rfloor}}^{n}C_{i}} \right)^{c} \right)}}}},$$   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

where the right hand side is finite by Lemmas 66 ‣ Sampling-based Algorithms for Optimal Motion Planning"), 67 vertices ‣ Appendix F Proof of Theorem 37 (asymptotic optimality of 𝑘-nearest RRG) ‣ Sampling-based Algorithms for Optimal Motion Planning"), and 69 ‣ Sampling-based Algorithms for Optimal Motion Planning"), by picking $\theta_{3}$ close to one. Hence, ${\sum_{n = 1}^{\infty}{{\mathbb{P}}\hspace{0pt}{({A_{n}^{c} \cup A_{n}^{\prime c}})}}} < \infty$. Then, by the Borel-Cantelli lemma, ${{\mathbb{P}}\hspace{0pt}{({\operatorname{lim\ sup}_{n\rightarrow\infty}{({A_{n}^{c} \cup A_{n}^{\prime c}})}})}} = 0$, or equivalently ${{\mathbb{P}}\hspace{0pt}{({\operatorname{lim\ inf}_{n\rightarrow\infty}{({A_{n} \cap A_{n}^{\prime}})}})}} = 1$. ∎∎

### F.6 Convergence to the optimal path 

The proof of the following two lemmas are essentially the same as that of Lemma 55 ‣ Sampling-based Algorithms for Optimal Motion Planning"), and is omitted here. Let $P_{n}$ denote the set of all paths in the graph returned by $k\hspace{0pt}\text{-}\hspace{0pt}{RRG}$ algorithm at the end of $n$ iterations. Let $\sigma_{n}^{\prime}$ be the path that is closest to $\sigma_{n}$ in terms of the bounded variation norm among all those paths in $P_{n}$, i.e., ${\sigma_{n}^{\prime}:={\min_{\sigma^{\prime} \in P_{n}}{\|{\sigma^{\prime} - \sigma_{n}}\|}}}.$

###### Lemma 70 

The random variable ${\|{\sigma_{n}^{\prime} - \sigma_{n}}\|}_{BV}$ converges to zero almost surely, i.e.,

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( {\left\{ \lim_{n\rightarrow\infty} \right\|\left. {{\sigma_{n}^{\prime} - {\sigma_{n}\parallel}_{BV}} = 0} \right\}} \right)} = 1}.$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

A corollary of the lemma above is that ${\lim_{n\rightarrow\infty}\sigma_{n}^{\prime}} = \sigma^{\ast}$ with probability one. Then, the result follows by the robustness of the optimal solution (see the proof of Lemma 56 ‣ Sampling-based Algorithms for Optimal Motion Planning") for details).

## Appendix G Proof of Theorem 38 ‣ 4.2.2 Proposed algorithms ‣ 4.2 Asymptotic Optimality ‣ 4 Analysis ‣ Sampling-based Algorithms for Optimal Motion Planning") (Asymptotic optimality of RRT^∗^) 

For simplicity, the proof will assume the steering parameter $\eta$ to be large enough, i.e., $\eta \geq {{diam}\hspace{0pt}{(\mathcal{X})}}$, although the results hold for any $\eta > 0$.

### G.1 Marked point process 

Consider the following marked point process. Let $\{ X_{1},X_{2},\ldots,X_{n}\}$ be a independent uniformly distributed points drawn from $X_{free}$ and let $\{ Y_{1},Y_{2},\ldots,Y_{n}\}$ be independent uniform random variables with support $\lbrack 0,1\rbrack$. Each point $X_{i}$ is associated with a mark $Y_{i}$ that describes the order of $X_{i}$ in the process. More precisely, a point $X_{i}$ is assumed to be drawn after another point $X_{i^{\prime}}$ if $Y_{i^{\prime}} < Y_{i}$. We will also assume that the point process includes the point $x_{init}$ with mark $Y = 0$.

Consider the graph formed by adding an edge $(X_{i^{\prime}},X_{i})$, whenever (i) $Y_{i^{\prime}} < Y_{i}$ and (ii) ${\|{X_{i} - X_{i^{\prime}}}\|} \leq r_{n}$ both hold. Notice that, formed in this way, $G_{n}$ includes no directed cycles. Denote this graph by $G_{n} = {(V_{n},E_{n})}$. Also, consider a subgraph $G_{n}^{\prime}$ of $G_{n}$ formed as follows. Let $c\hspace{0pt}{(X_{i})}$ denote the cost of best path starting from $x_{init}$ and reaching $X_{i}$. In $G_{n}^{\prime}$, each vertex $X_{i}$ has a single parent $X_{i}$ with the smallest cost $c\hspace{0pt}{(X_{i})}$. Since the graph is built incrementally, the cost of the best path reaching $X_{i}$ will be the same as the one reaching $X_{i^{\prime}}$ in both $G_{n}$ and $G_{n}^{\prime}$. Clearly, $G_{n}^{\prime}$ is equivalent to the graph returned by the RRT^∗^ algorithm at the end of $n$ iterations, if the steering parameter $\eta$ is large enough.

Let $Y_{n}$ and the $Y_{n}^{\prime}$ denote the costs of the best paths starting from $x_{init}$ and reaching the goal region in $G_{n}$ and $G_{n}^{\prime}$, respectively. Then, ${\operatorname{lim\ sup}_{n\rightarrow\infty}Y_{n}} = {\operatorname{lim\ sup}_{n\rightarrow\infty}Y_{n}^{\prime}}$ surely. In the rest of the proof, it is shown that ${{\mathbb{P}}\hspace{0pt}{({\{{\operatorname{lim\ sup}_{n\rightarrow\infty}Y_{n}}\}})}} = 1$, which implies that ${{\mathbb{P}}\hspace{0pt}{({\{{\operatorname{lim\ sup}_{n\rightarrow\infty}Y_{n}^{\prime}}\}})}} = 1$, which in turn implies the result.

### G.2 Definitions of ${\{\sigma_{n}\}}_{n \in {\mathbb{N}}}$ and ${\{ B_{n}\}}_{n \in {\mathbb{N}}}$ 

Let $\sigma^{\ast}$ denote an optimal path. Define

  -- ------------------------------------------------------------ --
     $${\delta_{n}:={\min{\{\delta,{4\hspace{0pt}r_{n}}\}}}},$$   
  -- ------------------------------------------------------------ --

where $r_{n}$ is the connection radius of the RRT^∗^ algorithm. Let ${\{\sigma_{n}\}}_{n \in {\mathbb{N}}}$ be the sequence paths, the existence of which is guaranteed by Lemma 50 ‣ Sampling-based Algorithms for Optimal Motion Planning").

For each $n \in {\mathbb{N}}$, construct a sequence ${\{ B_{n}\}}_{n \in {\mathbb{N}}}$ of balls that cover $\sigma_{n}$ as $B_{n} = {\{ B_{n,1},B_{n,2},\ldots,B_{n,M_{n}}\}}:={{\mathtt{C}\mathtt{o}\mathtt{v}\mathtt{e}\mathtt{r}\mathtt{i}\mathtt{n}\mathtt{g}\mathtt{B}\mathtt{a}\mathtt{l}\mathtt{l}\mathtt{s}}\hspace{0pt}{(\sigma_{n},r_{n},{2\hspace{0pt}r_{n}})}}$ (see Definition 51 ‣ C.3 Construction of the sequence {𝐵_𝑛}_{𝑛∈ℕ} of sets of balls ‣ Appendix C Proof of Theorem 34 (Asymptotic optimality of PRM∗) ‣ Sampling-based Algorithms for Optimal Motion Planning")), where $r_{n}$ is the connection radius of the RRT^∗^ algorithm, i.e., $r_{n} = {\gamma_{{RRT}^{\ast}}\hspace{0pt}\left( \frac{\log n}{n} \right)^{1/d}}$. Clearly, the balls in $B_{n}$ are openly disjoint, since the spacing between any two consecutive balls is $2\hspace{0pt}r_{n}$.

### G.3 Connecting the vertices in subsequent balls in $B_{n}$ 

For all $m \in {\{ 1,2,\ldots,M_{n}\}}$, let $A_{n,m}$ denote the event that there exists two vertices ${X_{i},X_{i^{\prime}}} \in V_{n}^{{RRT}^{\ast}}$ such that ${X_{i} \in B_{n,m}},{X_{i^{\prime}} \in B_{n,{m + 1}}}$ and $Y_{i^{\prime}} \leq Y_{i}$, where $Y_{i}$ and $Y_{i^{\prime}}$ are the marks associated with points $X_{i}$ and $X_{i^{\prime}}$, respectively. Notice that, in this case, $X_{i}$ and $X_{i^{\prime}}$ will be connected with an edge in $G_{n}$. Let $A_{n}$ denote the event that $A_{n,m}$ holds for all $m \in {\{ 1,2,\ldots,M\}}$, i.e., $A_{n} = {\bigcap_{m = 1}^{M}A_{n,m}}$.

###### Lemma 71 

If $\gamma_{{RRT}^{\ast}} > {4\hspace{0pt}\left( \frac{\mu\hspace{0pt}{(\mathcal{X}_{free})}}{\zeta_{d}} \right)^{1/d}}$, then $A_{n}$ occurs for all large $n$, with probability one, i.e.,

  -- ---------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( {\operatorname{lim\ inf}\limits_{n\rightarrow\infty}A_{n}} \right)} = 1}.$$   
  -- ---------------------------------------------------------------------------------------------------------------- --

###### Proof. 

The proof of this result is based on a Poissonization argument. Let ${Poisson}\hspace{0pt}{(\lambda)}$ be a Poisson random variable with parameter $\lambda = {\theta\hspace{0pt}n}$, where $\theta \in {(0,1)}$ is a constant independent of $n$. Consider the point process that consists of exactly ${Poisson}\hspace{0pt}{({\theta\hspace{0pt}n})}$ points, i.e., $\{ X_{1},X_{2},\ldots,X_{{Poisson}\hspace{0pt}{({\theta\hspace{0pt}n})}}\}$. This point process is a Poisson point process with intensity ${{\theta\hspace{0pt}n}/\mu}\hspace{0pt}{(X_{free})}$ by Lemma 11) ‣ 2.2 Random Geometric Graphs ‣ 2 Preliminary Material ‣ Sampling-based Algorithms for Optimal Motion Planning").

Let ${\overset{\sim}{A}}_{n,m}$ denote the event that there exists two vertices $X_{i}$ and $X_{i^{\prime}}$ in the vertex set of the RRT^∗^ algorithm such that $X_{i}$ and $X_{i^{\prime}}$ are connected with an edge in ${\overset{\sim}{G}}_{n}$, where ${\overset{\sim}{G}}_{n}$ is the graph returned by the RRT^∗^ when the algorithm is run for ${Poisson}\hspace{0pt}{({\theta\hspace{0pt}n})}$ many iterations, i.e., ${Poisson}\hspace{0pt}{({\theta\hspace{0pt}n})}$ samples are drawn from $\mathcal{X}_{free}$.

Clearly, ${{{\mathbb{P}}\hspace{0pt}{(A_{n,m}^{c})}} = {{\mathbb{P}}\hspace{0pt}{(\left. {\overset{\sim}{A}}_{n,m}^{c} \middle| {\{{{{Poisson}\hspace{0pt}{({\theta\hspace{0pt}n})}} = n}\}} \right.)}}}.$ Moreover,

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     $${{{\mathbb{P}}\hspace{0pt}{(A_{n,m}^{c})}} \leq {{{\mathbb{P}}\hspace{0pt}{({\overset{\sim}{A}}_{n,m}^{c})}} + {{\mathbb{P}}\hspace{0pt}{({\{{{{Poisson}\hspace{0pt}{({\theta\hspace{0pt}n})}} > n}\}})}}}}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

since ${\mathbb{P}}\hspace{0pt}{(A_{n,m}^{c})}$ is non-increasing with $n$ (see, e.g., Penrose, 2003). Since $\theta < 1$, ${{{\mathbb{P}}\hspace{0pt}{({\{{{{Poisson}\hspace{0pt}{({\theta\hspace{0pt}n})}} > n}\}})}} \leq e^{- {a\hspace{0pt}n}}},$ where $a > 0$ is a constant independent of $n$.

To compute ${\mathbb{P}}\hspace{0pt}{({\overset{\sim}{A}}_{n,m}^{c})}$, a number of definitions are provided. Let $N_{n,m}$ denote the number of vertices that lie in the interior of $B_{n,m}$. Clearly, ${{\mathbb{E}}\hspace{0pt}{\lbrack N_{n,m}\rbrack}} = {\frac{\zeta_{d}\hspace{0pt}\gamma_{{RRT}^{\ast}}^{d}}{\mu\hspace{0pt}{(X_{free})}}\hspace{0pt}{\log n}}$, for all $m \in {\{ 1,2,\ldots,M_{n}\}}$. For notational simplicity, define $\alpha:=\frac{\zeta_{d}\hspace{0pt}\gamma_{{RRT}^{\ast}}^{d}}{\mu\hspace{0pt}{(X_{free})}}$. Let $\epsilon \in {(0,1)}$ be a constant independent of $n$. Define the event

  -- -------------------- ------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $C_{n,m,\epsilon}$   $:=$   $\left\{ {N_{n,m} \geq {{({1 - \epsilon})}\hspace{0pt}{\mathbb{E}}\hspace{0pt}{\lbrack N_{n,m}\rbrack}}} \right\} = \left\{ {N_{n,m} \geq {{({1 - \epsilon})}\hspace{0pt}\alpha\hspace{0pt}{\log n}}} \right\}$   
  -- -------------------- ------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Since $N_{n,m,\epsilon}$ is binomially distributed, its large deviations from its mean can be bounded as follows (Penrose, 2003),

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( C_{n,m,\epsilon}^{c} \right)} = {{\mathbb{P}}\hspace{0pt}{({\{{N_{n,m,\epsilon} \leq {{({1 - \epsilon})}\hspace{0pt}{\mathbb{E}}\hspace{0pt}{\lbrack N_{n,m}\rbrack}}}\}})}} \leq e^{- {\alpha\hspace{0pt}H\hspace{0pt}{(\epsilon)}\hspace{0pt}{\log n}}} = n^{- {\alpha\hspace{0pt}H\hspace{0pt}{(\epsilon)}}}},$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

where ${H\hspace{0pt}{(\epsilon)}} = {\epsilon + {{({1 - \epsilon})}\hspace{0pt}{\log{({1 - \epsilon})}}}}$. Notice that $H\hspace{0pt}{(\epsilon)}$ is a continuous function of $\epsilon$ with ${H\hspace{0pt}{(0)}} = 0$ and ${H\hspace{0pt}{(1)}} = 1$. Hence, $H\hspace{0pt}{(\epsilon)}$ can be made arbitrary close to one by taking $\epsilon$ close to one.

Then,

  -- ------------------------------------------------------------- -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     ${\mathbb{P}}\hspace{0pt}{({\overset{\sim}{A}}_{n,m}^{c})}$   $=$      ${\mathbb{P}}\hspace{0pt}{(\left. {\overset{\sim}{A}}_{n,m}^{c} \middle| {C_{n,m,\epsilon} \cap C_{n,{m + 1},\epsilon}} \right.)}\hspace{0pt}{\mathbb{P}}\hspace{0pt}{({C_{n,m,\epsilon} \cap C_{n,{m + 1},\epsilon}})}$                                                                                                                        
                                                                            $+ {{\mathbb{P}}\hspace{0pt}{(\left. {\overset{\sim}{A}}_{n,m}^{c} \middle| {({C_{n,m,\epsilon} \cap C_{n,{m + 1},\epsilon}})}^{c} \right.)}\hspace{0pt}{\mathbb{P}}\hspace{0pt}{({({C_{n,m,\epsilon} \cap C_{n,{m + 1},\epsilon}})}^{c})}}$                                                                                                    
                                                                   $\leq$   ${{{\mathbb{P}}\hspace{0pt}{(\left. {\overset{\sim}{A}}_{n,m}^{c} \middle| {C_{n,m,\epsilon} \cap C_{n,{m + 1},\epsilon}} \right.)}\hspace{0pt}{\mathbb{P}}\hspace{0pt}{({C_{n,m,\epsilon} \cap C_{n,{m + 1},\epsilon}})}} + {{\mathbb{P}}\hspace{0pt}{(C_{n,m,\epsilon}^{c})}} + {{\mathbb{P}}\hspace{0pt}{(C_{n,{m + 1},\epsilon}^{c})}}},$   
  -- ------------------------------------------------------------- -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

where the last inequality follows from the union bound.

First, using the spatial independence of the underlying point process,

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     ${{{\mathbb{P}}\hspace{0pt}\left( {C_{n,m,\epsilon} \cap C_{n,{m + 1},\epsilon}} \right)} = {{\mathbb{P}}\hspace{0pt}\left( C_{n,m,\epsilon} \right)\hspace{0pt}{\mathbb{P}}\hspace{0pt}\left( C_{n,{m + 1},\epsilon} \right)} \leq n^{- {2\hspace{0pt}\alpha\hspace{0pt}H\hspace{0pt}{(\epsilon)}}}}.$   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Second, observe that ${\mathbb{P}}\hspace{0pt}{({{\left. A_{n,m}^{c} \middle| N_{n,m} \right. = k},{N_{n,{m + 1}} = k^{\prime}}})}$ is a non-increasing function of both $k$ and $k^{\prime}$, since the probability of the event ${\overset{\sim}{A}}_{n,m}$ can not increase with the increasing number of points in both balls, $B_{n,m}$ and $B_{n,{m + 1}}$. Then,

  -- ------------------------------------------------------------------------------------------------------------------------------------ -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     ${\mathbb{P}}\hspace{0pt}{(\left. {\overset{\sim}{A}}_{n,m}^{c} \middle| {C_{n,m,\epsilon} \cap C_{n,{m + 1},\epsilon}} \right.)}$   $=$      ${\mathbb{P}}\hspace{0pt}{(\left. {\overset{\sim}{A}}_{n,m}^{c} \middle| {\{{{N_{n,m} \geq {{({1 - \epsilon})}\hspace{0pt}\alpha\hspace{0pt}{\log N_{n,m}}}},{N_{n,{m + 1}} \geq {{({1 - \epsilon})}\hspace{0pt}\alpha\hspace{0pt}{\log N_{n,{m + 1}}}}}}\}} \right.)}$   
                                                                                                                                          $\leq$   ${\mathbb{P}}\hspace{0pt}{(\left. {\overset{\sim}{A}}_{n,m}^{c} \middle| {\{{{N_{n,m} = {{({1 - \epsilon})}\hspace{0pt}\alpha\hspace{0pt}{\log N_{n,m}}}},{N_{n,{m + 1}} = {{({1 - \epsilon})}\hspace{0pt}\alpha\hspace{0pt}{\log N_{n,{m + 1}}}}}}\}} \right.)}$         
  -- ------------------------------------------------------------------------------------------------------------------------------------ -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

The term on the right hand side is one minus the probability that the maximum of $\alpha\hspace{0pt}{\log n}$ number of uniform samples drawn from $\lbrack 0,1\rbrack$ is smaller than the minimum of $\alpha\hspace{0pt}{\log n}$ number of samples again drawn from $\lbrack 0,1\rbrack$, where all the samples are drawn independently. This probability can be calculated as follows. From the order statistics of uniform distribution, the minimum of $\alpha\hspace{0pt}{\log n}$ points sampled independently and uniformly from $\lbrack 0,1\rbrack$ has the following probability distribution function:

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{f_{\min}\hspace{0pt}{(x)}} = \frac{{({1 - x})}^{{\alpha\hspace{0pt}{\log n}} - 1}}{{\mathtt{B}\mathtt{e}\mathtt{t}\mathtt{a}}\hspace{0pt}{(1,{\alpha\hspace{0pt}{\log{(n)}}})}}},$$   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

where ${\mathtt{B}\mathtt{e}\mathtt{t}\mathtt{a}}\hspace{0pt}{( \cdot , \cdot )}$ is the Beta function (also called the Euler integral) (Abramowitz and Stegun, 1964). The maximum of the same number of independent uniformly distributed random variables with support $\lbrack 0,1\rbrack$ has the following cumulative distribution function:

  -- ------------------------------------------------------------------ --
     $${F_{\max}\hspace{0pt}{(x)}} = x^{\alpha\hspace{0pt}{\log n}}$$   
  -- ------------------------------------------------------------------ --

Then,

  -- ------------------------------------------------------------------------------------------------------------------------------------ -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     ${\mathbb{P}}\hspace{0pt}{(\left. {\overset{\sim}{A}}_{n,m}^{c} \middle| {C_{n,m,\epsilon} \cap C_{n,{m + 1},\epsilon}} \right.)}$   $\leq$   $\int_{0}^{1}{F_{\max}\hspace{0pt}{(x)}\hspace{0pt}f_{\min}\hspace{0pt}{(x)}\hspace{0pt}{dx}}$                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                          $=$      $\frac{{\mathtt{G}\mathtt{a}\mathtt{m}\mathtt{m}\mathtt{a}}\hspace{0pt}{({{({1 - \epsilon})}\hspace{0pt}\alpha\hspace{0pt}{\log n}})}\hspace{0pt}{\mathtt{G}\mathtt{a}\mathtt{m}\mathtt{m}\mathtt{a}}\hspace{0pt}{({{({1 - \epsilon})}\hspace{0pt}\epsilon\hspace{0pt}{\log n}})}}{2\hspace{0pt}{\mathtt{G}\mathtt{a}\mathtt{m}\mathtt{m}\mathtt{a}}\hspace{0pt}{({2\hspace{0pt}{({1 - \epsilon})}\hspace{0pt}\alpha\hspace{0pt}{\log{(n)}}})}}$   
                                                                                                                                          $\leq$   $\frac{{{({{({1 - \epsilon})}\hspace{0pt}\alpha\hspace{0pt}{\log n}})}!}\hspace{0pt}{{({{({1 - \epsilon})}\hspace{0pt}\alpha\hspace{0pt}{\log n}})}!}}{2\hspace{0pt}{{({2\hspace{0pt}{({1 - \epsilon})}\hspace{0pt}\alpha\hspace{0pt}{\log n}})}!}}$                                                                                                                                                                                               
                                                                                                                                          $=$      $\frac{{({{({1 - \epsilon})}\hspace{0pt}\alpha\hspace{0pt}{\log n}})}!}{2\hspace{0pt}{({2\hspace{0pt}{({1 - \epsilon})}\hspace{0pt}\alpha\hspace{0pt}{\log n}})}\hspace{0pt}{({{2\hspace{0pt}{({1 - \epsilon})}\hspace{0pt}\alpha\hspace{0pt}{\log n}} - 1})}\hspace{0pt}\cdots\hspace{0pt}1}$                                                                                                                                                     
                                                                                                                                          $\leq$   ${\frac{1}{2^{{({1 - \epsilon})}\hspace{0pt}\alpha\hspace{0pt}{\log n}}} = n^{- {{\log{(2)}}\hspace{0pt}{({1 - \epsilon})}\hspace{0pt}\alpha}}},$                                                                                                                                                                                                                                                                                                  
  -- ------------------------------------------------------------------------------------------------------------------------------------ -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

where ${\mathtt{G}\mathtt{a}\mathtt{m}\mathtt{m}\mathtt{a}}\hspace{0pt}{( \cdot )}$ is the gamma function (Abramowitz and Stegun, 1964).

Then,

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     ${{{\mathbb{P}}\hspace{0pt}{({\overset{\sim}{A}}_{n,m}^{c})}} \leq {n^{- {\alpha\hspace{0pt}{({{2\hspace{0pt}H\hspace{0pt}{(\epsilon)}} + {{\log{(2)}}\hspace{0pt}{({1 - \epsilon})}}})}}} + {2\hspace{0pt}n^{- {\alpha\hspace{0pt}H\hspace{0pt}{(\epsilon)}}}}}}.$   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Since ${2\hspace{0pt}H\hspace{0pt}{(\epsilon)}} + {{\log{(2)}}\hspace{0pt}{({1 - \epsilon})}}$ and $H\hspace{0pt}{(\epsilon)}$ are both continuous and increasing in the interval $(0.5,1)$, the former is equal to ${2 - {\log{(4)}}} > 0.5$ and the latter is equal to $1$ as $\epsilon$ approaches one from below, there exists some $\overline{\epsilon} \in {(0.5,1)}$ such that both ${{2\hspace{0pt}H\hspace{0pt}{(\overline{\epsilon})}} + {{\log{(2)}}\hspace{0pt}{({1 - \overline{\epsilon}})}}} > 0.5$ and ${H\hspace{0pt}{(\overline{\epsilon})}} > 0.5$. Thus,

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     ${{{\mathbb{P}}\hspace{0pt}{({\overset{\sim}{A}}_{n,m}^{c})}} \leq {n^{- {\alpha/2}} + {2\hspace{0pt}n^{- {\alpha/2}}}} = {3\hspace{0pt}n^{- {\alpha/2}}}}.$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Hence,

  -- ------------------------------------------- -------- ------------------------------------------------------------------------------------------------------------------------------------------------------ --
     ${\mathbb{P}}\hspace{0pt}{(A_{n,m}^{c})}$   $\leq$   ${{\mathbb{P}}\hspace{0pt}{({\overset{\sim}{A}}_{n,m}^{c})}} + {{\mathbb{P}}\hspace{0pt}{({{{Poisson}\hspace{0pt}{({\theta\hspace{0pt}n})}} > n})}}$   
                                                 $\leq$   ${3\hspace{0pt}n^{- {\alpha/2}}} + e^{- {a\hspace{0pt}n}}$                                                                                             
  -- ------------------------------------------- -------- ------------------------------------------------------------------------------------------------------------------------------------------------------ --

Recall that $A_{n}$ denotes the event that $A_{n,m}$ holds for all $m \in {\{ 1,2,\ldots,M_{n}\}}$. Then,

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}{(A_{n}^{c})}} = {{\mathbb{P}}\hspace{0pt}\left( \left( {\bigcap_{m = 1}^{M_{n}}A_{n,m}} \right)^{c} \right)} = {{\mathbb{P}}\hspace{0pt}\left( {\bigcup_{m = 1}^{M_{n}}A_{n,m}^{c}} \right)} \leq {\sum\limits_{m = 1}^{M_{n}}{{\mathbb{P}}\hspace{0pt}\left( A_{n,m}^{c} \right)}} = {M_{n}\hspace{0pt}{\mathbb{P}}\hspace{0pt}{(A_{n,1}^{c})}}},$$   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

where the last inequality follows from the union bound. The number of balls in $B_{n}$ can be bounded as

  -- ---------------------------------------------------------------------------------------- --
     $${{|B_{n}|} = M_{n} \leq {\beta\hspace{0pt}\left( \frac{n}{\log n} \right)^{1/d}}},$$   
  -- ---------------------------------------------------------------------------------------- --

where $\beta$ is a constant. Combining this with the inequality above,

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}{(A_{n}^{c})}} \leq {\beta\hspace{0pt}\left( \frac{n}{\log n} \right)^{1/d}\hspace{0pt}\left( {{3\hspace{0pt}n^{- {\alpha/2}}} + e^{- {a\hspace{0pt}n}}} \right)}},$$   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

which is summable for $\alpha > {2\hspace{0pt}{({1 + {1/d}})}}$. Thus, by the Borel-Cantelli lemma, the probability that $A_{n}^{c}$ occurs infinitely often is zero, i.e., ${{\mathbb{P}}\hspace{0pt}{({\operatorname{lim\ sup}_{n\rightarrow\infty}A_{n}^{c}})}} = 0$, which implies that $A_{n}$ occurs for all large $n$ with probability one, i.e., ${{\mathbb{P}}\hspace{0pt}{({\operatorname{lim\ inf}_{n\rightarrow\infty}A_{n}})}} = 1$. ∎∎

### G.4 Convergence to the optimal path 

The proof of the following lemma is similar to that of Lemma 55 ‣ Sampling-based Algorithms for Optimal Motion Planning"), and is omitted here.

Let $P_{n}$ denote the set of all paths in the graph returned by ${RRT}^{\ast}$ algorithm at the end of $n$ iterations. Let $\sigma_{n}^{\prime}$ be the path that is closest to $\sigma_{n}$ in terms of the bounded variation norm among all those paths in $P_{n}$, i.e., ${\sigma_{n}^{\prime}:={\min_{\sigma^{\prime} \in P_{n}}{\|{\sigma^{\prime} - \sigma_{n}}\|}}}.$

###### Lemma 72 

The random variable ${\|{\sigma_{n}^{\prime} - \sigma_{n}}\|}_{BV}$ converges to zero almost surely, i.e.,

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{{\mathbb{P}}\hspace{0pt}\left( {\left\{ \lim_{n\rightarrow\infty} \right\|\left. {{\sigma_{n}^{\prime} - {\sigma_{n}\parallel}_{BV}} = 0} \right\}} \right)} = 1}.$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

A corollary of the lemma above is that ${\lim_{n\rightarrow\infty}\sigma_{n}^{\prime}} = \sigma^{\ast}$ with probability one. Then, the result follows by the robustness of the optimal solution (see the proof of Lemma 56 ‣ Sampling-based Algorithms for Optimal Motion Planning") for details).
