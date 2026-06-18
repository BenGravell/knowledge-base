<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Comparative Study of Rapidly-exploring Random Tree Algorithms Applied to Ship Trajectory Planning and Behavior Generation

Topics include Rapidly-exploring random tree, Comparison study, Ship trajectory planning, Scenario generation, Electronic navigational charts, R-trees, Constrained Delaunay triangulation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Compares variations of RRT in an application domain for marine ship navigation. The dynamic model is basically the same as for car-like vehicles.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Rapidly Exploring Random Tree (RRT) algorithms, notably used for nonholonomic vehicle navigation in complex environments, are often not thoroughly evaluated for their specific challenges. This paper presents a first such comparison study of the variants Potential-Quick RRT* (PQ-RRT*), Informed RRT* (IRRT*), RRT*, and RRT, in maritime single-query nonholonomic motion planning. Additionally, the practicalities of using these algorithms in maritime environments are discussed and outlined. We also contend that these algorithms are beneficial not only for trajectory planning in Collision Avoidance Systems (CAS) but also for CAS verification when used as vessel behavior generators. Optimal RRT variants tend to produce more distance-optimal paths but require more computational time due to complex tree wiring and nearest neighbor searches. Our findings, supported by Welch`s t-test at a significance level of Alpha = 0.05, indicate that PQ-RRT* slightly outperform IRRT* and RRT* in achieving shorter trajectory length but at the expense of higher tuning complexity and longer run-times. Based on the results, we argue that these RRT algorithms are better suited for smaller-scale problems or environments with low obstacle congestion ratio.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This is attributed to the curse of dimensionality, and trade-off with available memory and computational resources.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Previous Work", "weight": 1.0} -->

Collision-free trajectory planning is a well-studied topic, and we refer the reader to review studies as in (Vagale et al. Huang et al., ) for extensive summaries on the various methods proposed previously, and to for an extensive review on RRT planning dated 2016. This brief review focuses on core versions of RRT having been proposed previously, in addition to ship scenario generation and falsification, respectively. The RRT algorithms are single-query, and thus they are tailored for planning trajectories or paths from a start position to a specified goal. For information on multi-query planning, the reader is referred to e.g. Probabilistic Roadmap methods (PRM) Kavraki et al..

<!-- chunk {"id": "body-0006", "role": "body", "section": "Rapidly-exploring Random Trees", "weight": 1.0} -->

The first baseline RRT planner was introduced by LaValle et al., with the core concept of incrementally sampling configurations or nodes in the obstacle-free space, and wiring of the tree towards these configurations if the trajectory segments in between are collision-free. However, baseline RRT is only probabilistically complete in the sense that the probability of the planner finding a solution approaches $1$ as the number of iterations approaches infinity. This issue was addressed in Karaman and Frazzoli with RRT\*, giving asymptotically optimality guarantees by introducing optimal selection of node parents during tree wiring through nearest neighbor search, and also by rewiring the tree after a new node has been inserted. However, the RRT-based planning still suffered from slow convergence. Since then, a multitude of approaches has been proposed to remedy this, e.g. Smart-RRT\* in Nasir et al. and IRRT\*. The former variant optimizes the found solutions by connecting visible collision-free nodes and utilizing them in the optimized solutions as beacons from which biased samples are drawn at a given percentage.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Rapidly-exploring Random Trees", "weight": 1.0} -->

The intelligent sampling procedure, however, only yields improved local convergence to solutions in the vicinity of the current best solution. IRRT\* employs a hyperellisoid sampling heuristic from a subset of the planning space, formed after an initial solution is found, and which reduces in volume as the planner improves the current best solution. This variant provides formal linear convergence guarantees, although only given the assumption of no obstacles.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Rapidly-exploring Random Trees", "weight": 1.0} -->

More recently, Potential Quick RRT\* (PQ-RRT\*) has been proposed, as a combination of the Artificial Potential Field (APF) based RRT\*, and Quick-RRT\*. As RRT\* is inherently biased towards the exploration of the obstacle-free configuration space, the APF method adds exploitation features through a goal-biased sample adjustment procedure, while the Quick-RRT\* gives an improved convergence rate through ancestor consideration in the wiring and re-wiring. As mentioned, there exist a significant number of other variants in the literature, that e.g. add bi-directional tree growth, utilize learning-based steering functionality or combine A\* with RRT\* in a learning-based fashion. The trade-off between exploitation and exploration in RRT was addressed without nonholonomic system consideration. A large literature review on sampling methods utilized in RRTs was given, which sheds light on the multitude of variants that have been proposed over the years.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Rapidly-exploring Random Trees", "weight": 1.0} -->

In the present work, we only focus on the core versions of directional RRT that have gained traction in the field, namely RRT, RRT\*, IRRT\*, and PQ-RRT\*.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Scenario Generation", "weight": 1.0} -->

This paper also demonstrates a proof-of-concept usage of RRTs for maritime ship behavior scenario generation. We note that this is not new in other domains, as scenario generation and falsification of safety-critical systems have been proposed in e.g. for testing nonlinear systems subject to disturbances, in for generating initial car vehicle states that yield boundary cases where the automated vehicle can no longer avoid collision, and in for adaptive cruise control falsification to search for hazardous leading vehicle behaviors leading to rear-end collisions.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Scenario Generation", "weight": 1.0} -->

What has typically been done in previous work within the maritime domain is to consider constant behaviors for vessels involved in a scenario (Minne Pedersen et al. Torben et al. Bolbot et al., ). Torben et al. used a Gaussian Process to estimate how CAS scores concerning safety and the COLREG, which guides the selection of scenarios to test the system at hand, based on its confidence level of having covered the parameter space describing the set of scenarios. Zhu et al. proposed an Automatic Identification System (AIS) based scenario generation method. Here, AIS data was analyzed and used to estimate Probability Density Functions (PDFs) describing the parameters of an encounter, such as distances between vessels, their speeds, and bearings. The PDFs were then used to generate a large number of scenarios for testing CAS algorithms. The goal was to increase the test coverage for such systems, over that which is possible with only expert-designed and real AIS data scenarios. Again, generated vessels all follow constant velocity, which does not always reflect true vessel behavior in hazardous encounters. Furthermore, one can not expect all vessels in a given situation to broadcast information using AIS, making AIS-generated scenarios partially incomplete sometimes.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Scenario Generation", "weight": 1.0} -->

Porres et al. used the Deep Q Network (DQN) for building a scenario test suite, based on using a neural network to score the performance of randomly generated scenarios. The performance is calculated based on geometric two-ship COLREG compliance and the risk of collision, where the score is used to determine if a given scenario is eligible for simulation and test suite inclusion. The approach should, however, be refined to account for more navigational factors such as grounding hazards in the performance evaluation. Recently, Bolbot et al. introduced a method for finding a reduced set of relevant traffic scenarios with land and disturbance consideration, through Sobol sequence sampling, filtering of scenarios based on risk metrics, and subsequent similarity clustering. Again, constant behavior is assumed for the vessels, but the process of identifying hazardous scenarios shows promise.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Contributions", "weight": 1.0} -->

The paper is the first comparison of the previously proposed RRT, RRT\*, IRRT\*, and Potential Quick-RRT\* (PQ-RRT\*) together, applied in a complex maritime environment for single-query directional planning with consideration of nonholonomic ship dynamics. This is contrary to the disregard for vehicle dynamics and often simpler and regular environments that have typically been used for testing and comparing RRTs in a lot of previous work.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Contributions", "weight": 1.0} -->

The planners are compared in Monte Carlo simulations for cases of varying complexity, with consideration of nonholonomic ship dynamics. The trajectory length results produced by PQ-RRT\* compared to the other RRT planners are analyzed for statistical significance using Welch's Student $t$-test. The chosen variants RRT, RRT\*, IRRT\* and PQ-RRT\* are considered as they represent core improvements of the RRT algorithm over the last 25 years, which we deemed the most interesting to compare. Comparisons of fusions of RRT\* with path complete methods such as A\* as in e.g. Wang et al., bi-directional RRTs, and RRT variants with alternative and more sophisticated steering mechanisms are outside the scope of this work. The same goes for the multitude of sampling strategies proposed in the literature. In addition to the comparison study, the paper also provides guidelines and a discussion around practicalities when applying such algorithms for ship trajectory planning, which can be of use to researchers and practitioners in the field.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Contributions", "weight": 1.0} -->

As a side contribution, we argue through proof-of-concept cases that RRT-based planners are beneficial for vessel test scenario generation due to their rapid generation of initially feasible, although not necessarily optimal, trajectories. As we do not necessarily require that obstacle vessels follow optimal trajectories, they provide a viable approach for the fast generation of random vessel scenarios used in CAS benchmarking. RRTs can also be used to generate more realistic ship intention scenarios that can be exploited in intention-aware CAS such as the Probabilistic Scenario-based Model Predictive Control (PSB-MPC) (Tengesdal et al. ). Lastly, the RRTs can be used in frameworks as in for finding relevant scenarios, where the RRT sampling heuristics can be tailored to the considered navigational factors.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Outline", "weight": 1.0} -->

The article is structured as follows. Preliminaries on ship dynamics and control are given in Section, and background on trajectory planning and RRT variants in Section. Notes on practical aspects to consider when applying RRTs for planning are given in Section, whereas results from applying RRTs for ship behavior generation and trajectory planning are given in Section. Lastly, conclusions are summarized in Section.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Ship Dynamics", "weight": 1.0} -->

When planning motion trajectories over longer time horizons, there is seldom a need to consider high-fidelity vehicle models, as modeling errors and disturbances will compound substantially. However, the model should as a minimum take the vehicle's kinodynamical constraints into account.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Ship Dynamics", "weight": 1.0} -->

with time constants $T_{\chi} > 0$ and $T_{U} > 0$ depending on the ship type. The ship maneuverability constraints $U_{min} \leq U \leq U_{max}$ and ${|\overset{˙}{\chi}|} \leq r_{max}$ on the minimum speed $U_{min}$, maximum speed $U_{max}$ and maximum turn rate $r_{max}$ of the ship are considered to ensure kinodynamic feasibility.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Ship Dynamics", "weight": 1.0} -->

RRTs are capable of considering arbitrarily complex ship dynamics and disturbance models, but we again note that the chosen model yields reduced computational requirements and is suitable for planning trajectories covering larger distances. Over large timespans, external disturbances, and modeling errors will compound substantially over the planning horizon, yielding a low benefit from using high-fidelity vessel models. Note that for lower-level motion control systems used for tracking the RRT trajectory output, it will be important to take the ship dynamics into account. Also, when using RRT to generate random obstacle ship scenarios, one seldom has access to the detailed ship model and motion control system employed by the target ship, further making this model suitable.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Line-of-Sight Guidance", "weight": 1.0} -->

To enable lightweight steering functionality in the RRTs and allowing for orientation or course control, we employ Line-of-Sight (LOS) guidance for steering the ship from a waypoint segment from $\{{\mathbf{p}}_{1},{\mathbf{p}}_{2}\}$, where ${\mathbf{p}}_{1} = {\lbrack x_{1}^{wp},y_{1}^{wp}\rbrack}^{T} \in {\mathbb{R}}^{2}$ is the planar waypoint position. To steer the ship along the straight waypoint segment and towards ${\mathbf{p}}_{2}$, the LOS method first finds the path tangential angle

<!-- chunk {"id": "body-0021", "role": "body", "section": "Line-of-Sight Guidance", "weight": 1.0} -->

where ${atan2}:{{\mathbb{R}}\rightarrow{({- \pi},\pi\rbrack}}$ is the four-quadrant arctangent function. Then, the path deviation $\mathbf{\epsilon}{(t)}$, referenced to the path-fixed frame, is computed as

<!-- chunk {"id": "body-0022", "role": "body", "section": "Line-of-Sight Guidance", "weight": 1.0} -->

The path deviation ${\mathbf{\epsilon}{(t)}} = {\lbrack{s{(t)}},{e{(t)}}\rbrack}^{T}$ consists of the along-track error $s{(t)}$ and cross-track error $e{(t)}$, respectively, where the latter is used with the path tangential angle $\theta_{p}$ to set the desired course-over-ground (COG) $\chi_{d}{(t)}$ as

<!-- chunk {"id": "body-0023", "role": "body", "section": "Line-of-Sight Guidance", "weight": 1.0} -->

where $\Delta$ is the look-ahead distance that determines how fast the ship will turn towards the straight line segment. The desired speed-over-ground (SOG) $U_{d}{(t)}$ can, in general, be varying, but is typically set to a constant in the case of nominal trajectory planning and generation. Without loss of generality, we do not consider environmental disturbances. However, note that compensations for slowly varying disturbances can be considered by adding an integral term. See for illustrations and more information.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

This section formally defines the considered motion planning problem and the RRT-based algorithms compared in this work: Standard RRT, RRT\*, IRRT\* and Potential Quick RRT\* (PQ-RRT\*). As mentioned in the introduction, bi-directional variants such as RRT\*-connect and combinations of RRT with e.g. path-complete methods such as A\* are outside the scope of this work. The following text does not provide an in-depth introduction to each algorithm, and the reader is thus referred to the cited references for more details.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

The optimal trajectory planning problem is stated as follows. Let ${\mathbf{z}}_{start} \in {\mathcal{X}}_{free}$ and ${\mathbf{z}}_{goal} \in {\mathcal{X}}_{free}$ be the initial and final own-ship states, respectively. Further let ${\mathbf{σ}}_{d}:{{\lbrack 0,T_{plan}\rbrack}\rightarrow{\mathcal{X}}}$ be a non-trivial trajectory from start to goal. Then, the objective of the RRT-based planning algorithms is to find the optimal and feasible desired trajectory ${\mathbf{σ}}_{d}^{\ast}$ defined through

<!-- chunk {"id": "body-0026", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

where $T_{plan}$ is the trajectory duration and ${c{( \cdot )}}:{{\mathcal{X}}\rightarrow{\mathbb{R}}}$ the planning problem cost function. In summary, the required inputs and resulting output of the RRT planners are

<!-- chunk {"id": "body-0027", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

${\mathbf{z}}_{start}$, ${\mathbf{z}}_{goal}$ and Electronic Navigational Chart (ENC): Starting state, goal state, and ENC containing grounding hazard information, respectively.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

The output trajectory from the RRT-based planners can be generated offline or online depending on the application and is typically provided as a reference trajectory for the lower-level motion control system onboard the ship to track.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Core RRT-functionality", "weight": 1.0} -->

To solve the described trajectory planning problem, RRT-based planners incrementally and randomly grow a tree $\mathcal{T} = {(\mathcal{V},\mathcal{E})}$ consisting of a state vertex or node set $\mathcal{V} \subset {\mathcal{X}}_{free}$ that are connected through the directed edges in $\mathcal{E} \subseteq {\mathcal{V} \times \mathcal{V}}$. Asymptotic optimality in the number of iterations for the planned trajectory is guaranteed in RRT\* and its variants through the parent-cost dependent wiring and rewiring of the tree in order to find new minimal cost parents. The standard RRT method does, however, not have this property. We note that the convergence rate is highly dependent on the node sampling procedures, in addition to the tree re-wiring mechanism. Common functions used in all the RRT-based planners are given below.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Core RRT-functionality", "weight": 1.0} -->

1\) ${Sample}{(i)}$: Samples a random state $z_{rand} \in {\mathcal{X}}_{free}$. See Section 4.1 for implementation aspects. When applied to random scenario generation, the sampling can be biased towards scenario-related metrics.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Core RRT-functionality", "weight": 1.0} -->

7\) ${Steer}{(z_{1},z_{2})}$: Computes a control input sequence that steers the own-ship from state ${{\mathbf{x}}{}} = {\mathbf{z}}_{1}$ to ${{\mathbf{x}}{(T)}} = {\mathbf{z}}_{2}$ using the LOS method outlined in Section 2.3. The result is the final endpoint state ${\mathbf{z}}_{new}$ and corresponding trajectory ${\mathbf{σ}}_{new}:{{\lbrack 0,T\rbrack}\rightarrow\mathcal{X}}$ with steering horizon $T \in {\lbrack T_{min},T_{max}\rbrack}$. The minimum and maximum steering time $T_{min}$ and $T_{max}$ are parameters to be adjusted based on the geography.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Core RRT-functionality", "weight": 1.0} -->

Narrow channels and inland waterways might require lower steering times to avoid collisions, and vice versa for more open sea areas.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Core RRT-functionality", "weight": 1.0} -->

8\) ${ExtractBestSolution}{(\mathcal{T})}$: Given the tree $\mathcal{T}$, the function extracts the solution

<!-- chunk {"id": "body-0034", "role": "body", "section": "Core RRT-functionality", "weight": 1.0} -->

if any. Otherwise, the algorithm will report failure. The solution trajectory is valid if the corresponding leaf node is inside an acceptance radius $R_{a}$ of the goal ${\mathbf{z}}_{goal}$, and thus its cost is finite.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Core RRT-functionality", "weight": 1.0} -->

The $Steer$ function enables the planner to consider the own-ship dynamics by using the motion model $f{({{\mathbf{x}}{(t)}},{{\mathbf{u}}{(t)}})}$ for simulating a trajectory from a state $z_{1}$ to $z_{2}$. The speed and turn rate (course rate) are saturated to within the considered vessel minimum and maximum speeds $\{ U_{min},U_{max}\}$ and maximum turn rate $r_{max}$ for this particular model, respectively.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Core RRT-functionality", "weight": 1.0} -->

To incorporate dynamic obstacle collision avoidance, one can employ a joint simulator as in Chiang and Tapia in the steering together with adding virtual obstacles for striving towards COLREG compliance, or utilize biased sampling methods as in e.g.. However, this will not be considered in the present work.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Core RRT-functionality", "weight": 1.0} -->

9\) ${DirectGoalGrowth}{(\mathcal{T},{\mathbf{z}}_{goal})}$: Finds the nearest neighbor ${\mathbf{z}}_{nearest} = {{Nearest}{(\mathcal{T},{\mathbf{z}}_{goal})}}$ of the goal state, and attempts to steer the ship towards the state using ${Steer}{({\mathbf{z}}_{nearest},{\mathbf{z}}_{goal})}$ with a sufficiently large steering time, commonly a multiple of $T_{max}$. This returns a new node ${\mathbf{z}}_{new}$, which is added to the tree $\mathcal{T}$ if the steering is successful.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Core RRT-functionality", "weight": 1.0} -->

The baseline RRT algorithm can be described by these functions and is outlined in Algorithm. Here, $N_{iter}^{max}$ is the maximum number of allowable iterations and $\Delta_{goal}$ the iterations between each attempt of $DirectGoalGrowth$. In addition to the maximum iteration constraint, we also under the hood put a constraint on the maximum number of nodes $N_{node}^{max}$ allowable in the RRT planners.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Core RRT-functionality", "weight": 1.0} -->

1:{Initial state zinit, goal state zgoal and ENC }
5: if i % Δgoal = = 0 then DirectGoalGrowth(𝒯,zgoal)
8: znearest ← Nearest(𝒯,zrand)
9: (znew,σnew) ← Steer(znearest,zrand)
10: if IsCollisionFree(σnew) then
11: 𝒯 ← Insert(𝒯,zmin,znew)

<!-- chunk {"id": "body-0040", "role": "body", "section": "RRT\\*", "weight": 1.0} -->

Specific to the RRT\* variant are the $NearestNeighbors$, $FindParent$ and $Rewire$ functions, which give the algorithm probabilistic asymptotic convergence properties. The RRT\* algorithm can be described fully by the functions 1-12 and is outlined in Algorithm.

<!-- chunk {"id": "body-0041", "role": "body", "section": "RRT\\*", "weight": 1.0} -->

Nearest neighbor extraction is a crucial part of RRT\*, and is highly dependent on the search parameter $\gamma$, for which provide some tuning considerations. We note that this parameter must be scaled based on the problem size. If dimensions $> 2$ are considered, with state entries of different units and scales, it will be important to normalize the states. For Euclidean distance-based search in two or three dimensions, this is, however, a necessity.

<!-- chunk {"id": "body-0042", "role": "body", "section": "RRT\\*", "weight": 1.0} -->

1:{Initial state zinit, goal state zgoal and ENC}
5: if i % Δgoal = = 0 then DirectGoalGrowth(𝒯,zgoal)
8: znearest ← Nearest(𝒯,zrand)
9: (znew,σnew) ← Steer(znearest,zrand)
10: if IsCollisionFree(σnew) then
11: 𝒵near ← NearestNeighbors(𝒯,znew)
12: zmin ← FindParent(𝒵near,znearest,znew)
13: 𝒯 ← Insert(𝒯,zmin,znew)
14: 𝒯 ← Rewire(𝒯,𝒵near,zmin,znew)

<!-- chunk {"id": "body-0043", "role": "body", "section": "IRRT\\*", "weight": 1.0} -->

IRRT\* varies from the baseline RRT\* only in the fact that, once an initial solution is found with cost $c_{best}$, an admissible informed sampling heuristic is used onwards. The heuristic is formed from an elliptical domain given by the ${\mathbf{x}}_{start}$ and ${\mathbf{x}}_{goal}$ as focal points, the theoretical minimum cost $c_{min} = {\|{{\mathbf{p}}_{goal} - {\mathbf{p}}_{start}}\|}_{2}$ and current best solution cost $c_{best}$, with ${\mathbf{p}}_{goal}$ and ${\mathbf{p}}_{start}$ being the planar position parts ${\mathbf{x}}_{start}$ and ${\mathbf{x}}_{goal}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IRRT\\*", "weight": 1.0} -->

It is shown that this heuristic enables focused planning towards ${\mathbf{x}}_{goal}$, as opposed to the Voronoi bias property inherited in RRT and RRT\* that lead to planning towards all points in the state space.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IRRT\\*", "weight": 1.0} -->

and which defines the ellipsoid

<!-- chunk {"id": "body-0046", "role": "body", "section": "IRRT\\*", "weight": 1.0} -->

The rotation matrix $\mathbf{C}$ from the hyperellipsoidal frame to the world frame can be found by solving the Wahba problem. However, when sampling planar positions, it can be directly found as a 2D rotation matrix with angle $\theta_{g} = {{atan2}{({y_{goal} - y_{start}},{x_{goal} - x_{start}})}}$. The sampling is in this case reduced to

<!-- chunk {"id": "body-0047", "role": "body", "section": "IRRT\\*", "weight": 1.0} -->

where ${Uniform}{(x;a,b)}$ is a uniform distribution with interval limits $a$ and $b$. The informed sampling procedure is described below, with the IRRT\*-variant being described in Algorithm.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IRRT\\*", "weight": 1.0} -->

13\) ${InformedSample}{(i)}$: Given the current best cost $c_{best}$, sample a new state using. If $c_{best} = \infty$, use the baseline ${Sample}{(i)}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IRRT\\*", "weight": 1.0} -->

1:{Initial state zinit, goal state zgoal and ENC}
5: if i % Δgoal = = 0 then DirectGoalGrowth(𝒯,zgoal)
8: znearest ← Nearest(𝒯,zrand)
9: (znew,σnew) ← Steer(znearest,zrand)
10: if IsCollisionFree(σnew) then
11: 𝒵near ← NearestNeighbors(𝒯,znew)
12: zmin ← FindParent(𝒵near,znearest,znew)
13: 𝒯 ← Insert(𝒯,zmin,znew)
14: 𝒯 ← Rewire(𝒯,𝒵near,zmin,znew)

<!-- chunk {"id": "body-0050", "role": "body", "section": "PQ-RRT\\*", "weight": 1.0} -->

The Potential-Quick RRT\* combines the features of P-RRT\* and Q-RRT\*, which involves sample adjustments using a goal-based potential field attractive force, and ancestor consideration in the tree growth for path length reduction, respectively.

<!-- chunk {"id": "body-0051", "role": "body", "section": "PQ-RRT\\*", "weight": 1.0} -->

14\) ${Ancestor}{(\mathcal{T},{\mathbf{z}},\phi)}$: Given the tree $\mathcal{T}$, a node $\mathbf{z}$ and depth parameter $\phi > 0$, the $\phi$-th parent of $\mathbf{z}$ is returned. If the tree is not deep enough, no ancestor is returned.

<!-- chunk {"id": "body-0052", "role": "body", "section": "PQ-RRT\\*", "weight": 1.0} -->

The PQ-RRT\* is described in Algorithm. In this work, we consider a depth-level of $\phi = N_{ancestry}$ in the $Ancestry$ procedure, whereas a constant depth level of $1$ is used in the $PQRewire$ method, to reduce computational effort. Note that the algorithm as proposed in Li et al. was not tested with kinodynamical constraints and motion planning in the steering, which will induce substantially higher run-times in the algorithm due to the ancestor consideration in the $FindParent$ and ${PQ} - {Rewire}$ routines. On the other hand, better convergence properties are expected due to the PQ features. The sample adjustment procedure uses a hazard clearance parameter $d_{margin}$ that must be set based on acceptable margins, the ship type, and possibly other factors. We note that the selection of the PQ-RRT\* specific parameters is non-trivial, and no guidelines for their selection were provided in Li et al.. The authors highlighted this as a potential limitation of the method.

<!-- chunk {"id": "body-0053", "role": "body", "section": "PQ-RRT\\*", "weight": 1.0} -->

1:{Sampled state zrand, goal state zgoal }
4: Fatt ← (zgoal−zprand)
5: dmin ← DistanceNearestObstacle(𝒳obst,zprand)
6: if dmin &lt; dmargin then
9: ${\mathbf{z}}_{prand}\leftarrow{{\mathbf{z}}_{prand} + {\lambda\frac{{\mathbf{F}}_{att}}{\left\| {\mathbf{F}}_{att} \right\|}}}$

<!-- chunk {"id": "body-0054", "role": "body", "section": "PQ-RRT\\*", "weight": 1.0} -->

1:{Initial state zinit, goal state zgoal and ENC}
5: if i % Δgoal = = 0 then DirectGoalGrowth(𝒯,zgoal)
8: zrand ← AdjustSample(zrand,zgoal)
9: znearest ← Nearest(𝒯,zrand)
10: (znew,σnew) ← Steer(znearest,zrand)
11: if IsCollisionFree(σnew) then
12: 𝒵near ← NearestNeighbors(𝒯,znew)
13: 𝒵ancestors ← Ancestry(𝒯,𝒵near)
14: 𝒵union ← 𝒵near ∪ 𝒵ancestors
15: zmin ← FindParent(𝒵union,znearest,znew)
16: 𝒯 ← Insert(𝒯,zmin,znew)
17: 𝒯 ← PQRewire(𝒯,𝒵near,zmin,znew)

<!-- chunk {"id": "body-0055", "role": "body", "section": "Algorithm Pros and Cons", "weight": 1.0} -->

As it can be non-obvious for the reader to see the immediate main differences between the considered RRT-based planners, we provide Table below to summarize the pros and cons of each algorithm. The jagging and meandering tendency of RRT, RRT\*, and IRRT\* owes to the fact that only a single ancestor is considered in the rewiring, which is also highly dependent on the choice of nearest neighbor search parameter $\gamma$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Algorithm Pros and Cons", "weight": 1.0} -->

Can find initial solutions fast
Highly jagged output trajectories

<!-- chunk {"id": "body-0057", "role": "body", "section": "Algorithm Pros and Cons", "weight": 1.0} -->

High sample rejection rate in vanilla version

<!-- chunk {"id": "body-0058", "role": "body", "section": "Algorithm Pros and Cons", "weight": 1.0} -->

Low jagging and meandering tendency
Higher computational effort required

<!-- chunk {"id": "body-0059", "role": "body", "section": "Sampling", "weight": 1.0} -->

One of the most important parts of RRT is the method by which new states are sampled. Brute force sampling of states ${\mathbf{z}}_{rand} \in \mathcal{X}_{free}$ is not recommended, as the rejection rate will be proportional to the volume of $\mathcal{X}_{obst}$ relative to the total space $\mathcal{X}$. Instead, one can for instance create and sample from a Constrained Delaunay Triangulation (CDT), made from the safe sea area that the ship is to voyage within, similar to. This gives a set $\Theta_{tri}$ of triangles with indices $j = {1,2,\ldots,n_{tri}}$, which in this application reduces the sampling of a new state position ${\mathbf{p}}_{rand} \in {\mathbb{R}}^{2}$ to

<!-- chunk {"id": "body-0060", "role": "body", "section": "Sampling", "weight": 1.0} -->

where $({\mathbf{A}}_{j^{\prime}},{\mathbf{B}}_{j^{\prime}},{\mathbf{C}}_{j^{\prime}})$ are the vertices of triangle $j^{\prime}$, and $WeightedUniform$ is a uniform distribution weighted by the area of each triangle. The random state is then found as ${\mathbf{z}}_{rand} = {\lbrack{\mathbf{p}}_{rand}^{T},0,0\rbrack}^{T}$. An illustration of a CDT of the safe sea area used for sampling in the second planning example is shown in Fig..

<!-- chunk {"id": "body-0061", "role": "body", "section": "Sampling", "weight": 1.0} -->

When using the sample heuristic in IRRT\* bonafide, the same problem of high rejection rates can occur. Here, one can again use CDT, and prune triangles outside the ellipsoidal sampling domain after a new solution is found and the heuristic is put to use. However, this will not be done here.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Data Structures", "weight": 1.0} -->

Another foundation of the RRT algorithms is nearest neighbor searches, used when wiring and re-wiring the tree for RRT\*-variants. For spatial queries as is considered here, it is recommended to use R\*-tree or R-tree-based data structures (Guttman Beckmann et al., ) that are commonly used for storing spatial objects in e.g. databases. They have $O{({log{(n)}})}$ complexity for insertion and distance-related queries for $n$ inserted elements. The trees are created such that leaf nodes of the tree hold spatial data, and parents or branching nodes correspond to the minimum bounding box that contains all of its children. With this structure, the R-tree utilizes data-based partitions into boxes of decreasing size as the tree grows. K-d trees have the same complexity as R-trees, and can also be used. However, note that the bonafide version is suitable only when the nodes are points and does not work well in high dimensions. Once polygons and other objects are introduced for representing the own-ship, static or dynamic hazards, standard k-d trees are also not compatible.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Data Structures", "weight": 1.0} -->

The advantages of using R-trees are the efficient memory layout, tree update procedures and spatial nearest neighbor searching. For cases where the tree will not end up with a high number of objects or when few modifications and removals will be made on the go, it can on the other hand be sufficient to use k-d trees.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Data Structures", "weight": 1.0} -->

These points also apply to the collision checking part, discussed below. Note that it might be worthwhile to consider a Mahalanobis distance metric when it is desired to evaluate the distance with respect to both position and other state variables such as orientation. In this regard, it will be wise to normalize the data before considering distance calculations.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Collision Checking", "weight": 1.0} -->

To accept a new node in the tree $\mathcal{T}$ maintained by the RRT algorithms, collision checks must be performed for each new trajectory segment ${\mathbf{σ}}_{new}$ resulting from the steering function in several parts of the RRT-algorithms. To ensure feasibility with respect to run-time, it is important to pre-process grounding hazard data using line simplification algorithms such as Ramer-Douglas-Peucker to reduce the map data accuracy to the required level. Especially for the maritime domain, one should merge multi polygons arising from hazardous land, shore and seabed objects extracted from Electronic Navigation Charts (ENC), given the considered vessel and its draft. We also recommend removing interior holes of land multi polygons arising from e.g. lakes, as these will naturally not be considered for sea voyages.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Collision Checking", "weight": 1.0} -->

Again, it will also be important in this procedure to use efficient data structures such as R-trees for enabling fast distance computations in collision checking. Adherence to specified hazard clearance margins $d_{safe}$ and control requirements can easily be done by buffering the hazard polygons before running the algorithm. Note that verification of sampled poses along a trajectory being collision-free is not exact, and operation in more confined space with smaller distance margins might require more accurate methods as in e.g..

<!-- chunk {"id": "body-0067", "role": "body", "section": "Collision Checking", "weight": 1.0} -->

Note that collision checking requires significantly less effort when only two-point planar waypoint segments are considered, as opposed to a full trajectory segment with kinodynamical constraint consideration. This can be an option when the goal is to rapidly generate waypoints for a ship to follow, as opposed to a full trajectory to track. Some regard to maximum curvature based on the ship turn rate and speed should then be taken into account when accepting waypoint segments.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Steering", "weight": 1.0} -->

For trajectory planning RRTs, the steering functionality for connecting state pairs $({\mathbf{z}}_{1},{\mathbf{z}}_{2})$ is a crucial part of the tree wiring, especially for non-holonomic systems. Previous methods have proposed e.g. the simplistic Dubin´s path for optimal steering, Bezier spline-based connectivity, learning-based steering and collision checking, LQR-control-based extension and lazy steering with a Neural Network (NN) for determining collision-free and steerable node extensions. In this work, we apply LOS guidance for steering the ship towards new eligible nodes, as a low-cost solution for creating feasible trajectory segments in the maritime domain. One point that requires care in this context, is the early termination of the LOS guidance if the waypoint segment from ${\mathbf{z}}_{1}$ to a new node ${\mathbf{z}}_{2}$ is passed, such that the computational cost of numerical integration of the ship dynamics is kept to a minimum.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Steering", "weight": 1.0} -->

Further note that the integration time step should be increased in tact with the problem size, also related to the computational cost aspect.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Results", "weight": 1.0} -->

We present three cases in which the considered RRT-variants are compared. The first case demonstrates the usage of RRTs for rapid ship behavior generation, where the goal is to generate kinodynamically feasible trajectories for a specified ship scenario. The second case compares common RRT variants for a smaller planning scenario with a typical local minimum problem. Finally, the third case compares the RRT planners in a larger planning scenario. The simulation framework in is used as a platform for developing and testing the planners, which allows for the utilization of Electronic Navigational Charts. The algorithms are implemented in the Rust programming language, and the executable is run on a MacBook Pro with an Apple Silicon M1 chip. We evaluate the obtained solutions with respect to run-time and trajectory lengths, over $N_{MC} = 100$ Monte Carlo (MC) simulations for each case, where the RRTs are provided with different pseudorandom seeds before each run. Aside from summarizing the planner results, we report the statistical significance of the trajectory length results produced by PQ-RRT\* being more distance optimal than other RRT variants or not through Welch's unequal variance Student's $t$-test.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Results", "weight": 1.0} -->

The grounding hazards in the environment are buffered with a horizontal clearance parameter $d_{safe}$ of $0\ m$ in the first two cases, and $5\ m$ in the last case. This will in general be dependent on the map accuracy, ship type, and application. We consider a time step $\delta_{sim}$ of $0.5\ s$ in the first two cases, and $1.0\ s$ in the last case, for the RRT kinematic ship model. For the RRTs, we use R-trees to perform nearest neighbor searching and spatial queries, where grounding hazards (land, shore, and relevant seabed) are extracted and merged considering a vessel draft of $1.0\ m$. The merged hazards are then used to form a safe sea CDT, from which weighted samples are drawn.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Results", "weight": 1.0} -->

Key parameters for the RRT-variants used in the first two cases are given in Table. For the first case, we did not find a configuration of PQ-RRT\* parameters for the sample adjustment procedure that gave a better result than just disabling the APF-based part as a whole and thus used $N_{sa}^{max} = 0$. All methods sample from the safe sea CDT using, except the IRRT\* which uses after a solution has been found. The PQ-RRT\* will adjust the CDT sample using its goal potential field. We note that tuning of the RRT algorithms is non-trivial, and will be specific to the scale considered for the trajectory planning. This is a trade-off between planner run-time, memory requirements, and solution quality. The number of iterations should be adequately high to increase the likelihood of the RRT finding a solution.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Random Vessel Trajectory Generation", "weight": 1.0} -->

The first case is a random vessel trajectory generation scenario where the goal is to generate multiple random trajectories from a given start position. After being built, the resulting RRT variant can be queried efficiently through R-tree spatial nearest neighbor search, and used to rapidly sample random ship trajectories for intention-aware CAS or simulation-based testing of CAS. This is useful in the online setting for CAS, but also for interaction data generation to be used by learning-based CAS algorithms. Training of Reinforcement Learning (RL) agents with the Gymnasium framework typically requires a reset of the environment after each terminated or truncated episode. In this context, RRT algorithms can be used for rapidly generating target ship trajectory scenarios after a reset. As an example, PQ-RRT\* will, in general, produce more path-optimal solutions than RRT and RRT\*, and can thus be used for spawning target ship behavior scenarios with minimal maneuvering, whereas the RRT\* or RRT variants can be used for spawning gradually unpredictable maneuvering target ship behaviors that can be considered as outliers.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Random Vessel Trajectory Generation", "weight": 1.0} -->

Thus, employing multiple RRT algorithm variants for ship scenario generation can improve the ability of learning-based CAS to generalize, and also enlarge the test coverage in the context of simulation-based CAS verification.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Random Vessel Trajectory Generation", "weight": 1.0} -->

Note that, in the scenario-generation context the RRT cost function can be designed to e.g. minimize time to collision or converge towards near misses between the random vessel and the own-ship that runs the CAS to be tested. Furthermore, in the maritime context, COLREG can be misinterpreted and lead to ambiguous and therefore often dangerous situations. Thus, RRTs could be guided towards edge case situations in COLREG where the applicable situation rule(s) are easy to misinterpret. These considerations are a topic for future work.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Random Vessel Trajectory Generation", "weight": 1.0} -->

Fig. shows an example of obstacle ship behavior generation for a CAS head-on situation. To make the figures less dense, we have reduced the maximum allowable tree nodes to $N_{node}^{max} = 4000$ for all planners. In this particular case, we find built RRT, RRT\*, and PQ-RRT\* behaviors close to a randomly sampled position within a corridor given by the initial own-ship position and course and its maximum travel length over the simulation timespan, i.e.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Random Vessel Trajectory Generation", "weight": 1.0} -->

Fig shows another case where we sample behaviors for a CAS crossing situation. In this situation, random position samples are drawn near the predicted closest point of approach (CPA) between the vessels, from which the nearest RRT behaviors or trajectories are fetched, i.e.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Random Vessel Trajectory Generation", "weight": 1.0} -->

where ${\mathbf{p}}_{cpa}$ is the target ship position at CPA, assuming constant speed and course for the two vessels, calculated as in e.g., and where $\mathbf{\Sigma}$ is the covariance parameter adjusting the spread of samples. This strategy allows for generating multiple target ship behaviors that will lead to a collision or near miss with the own-ship unless preventive actions are taken. Since the RRTs are flexible, any of the navigational risk factors as outlined in could be considered as targets for developing either RRT sampling schemes or cost functions.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Random Vessel Trajectory Generation", "weight": 1.0} -->

For each of the example situations, the sampled behaviors parameterized by waypoints are shown. Since the planners consider the underlying ship model dynamics, the waypoints will be feasible, in addition to being collision-free with respect to nearby static hazards. Note that we can also use the trajectory that accompanies the waypoints as well. Further note that we define a reduced-size bounding box considered by the RRT planners, in order to reduce computation time and consider only a subset of the grounding hazards present in the ENC. Once the RRTs are built, a new behavior can be sampled in less than $1\ {ms}$ on the considered computing platform, which makes the approach viable for large-scale scenario production. We also note that the trees can easily be built offline, and then effectively sampled from afterwards in the relevant context.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Smaller Planning Example", "weight": 1.0} -->

In the second case, we consider a smaller planning situation with a constant reference ship speed $U_{d} = {4.0\ {m/s}}$, and allow the planners to find and refine their solution over the maximum allowable iterations and tree nodes up until a maximum time of $50\ s$. The considered location near Kvitsøy in Rogaland, Norway has a map size of ${850\ m} \times {750\ m}$, and features a typical local minimum problem where one can get stuck in the dead end not far from the ship initial position. Note that as the planners sample from a CDT constructed from the safe sea area, the sampling efficiency will be higher, making it easier to avoid local minima issues.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Smaller Planning Example", "weight": 1.0} -->

Results from sample runs are shown in Figure, whereas solution statistics are given in Table. In the table, statistics for the time to find an initial solution $t_{{sol},0}$ are reported, whereas run-time $t_{sol}$ and path length $d_{sol}$ statistics are reported for the final refined trajectory. The metric $\rho_{mc}$ is the success percentage of finding a solution out of all the MC runs. From Figure, it might look like there is a collision due to the orange waypoints crossing a hazard at some point. This is not the case, as the actual ship trajectories wired by the RRTs are collision-free, taking the nonholonomic properties of the ship into account.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Smaller Planning Example", "weight": 1.0} -->

The optimal solution has a path length of approximately $905\ m$. Thus we see that PQ-RRT\*, IRRT\*, and RRT\* can converge to within $6\%$ of the optimum. PQ-RRT\* attains the best results concerning path length, with a marginal difference to IRRT\* and RRT\*. On the other hand, the ancestor consideration in the tree rewiring and extra sampling functionality comes at the cost of higher runtimes. We also see a factor of 10 increase in the run-time between baseline RRT and RRT\*, which is expected due to the more complicated wiring process.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Smaller Planning Example", "weight": 1.0} -->

For IRRT\* we can get marginally better results than RRT\* at lower run-times. This is due to the high sample rejection rate after finding an initial solution, as samples are likely to be taken from $\mathcal{X}_{obst}$ in this map with large hazard coverage. However, accepted samples will have higher values, partially explaining the marginal improvement in solution lengths. It can here be a viable approach to iteratively prune out triangles in the safe sea CDT as the hyperellipsoid forming the sampling heuristic reduces in volume. One should thus implement efficient methods for re-computing the CDT from the new sampling domain or for pruning CDT triangles outside the domain.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Smaller Planning Example", "weight": 1.0} -->

where $\mu_{p,\text{PQ-RRT*}}$ is the mean trajectory length produced by the PQ-RRT\* planner (equal to $963.1\ m$ in the smaller planning example) and $\mu_{p,i}$ the mean trajectory length for the other RRT planners.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Smaller Planning Example", "weight": 1.0} -->

We start by computing Welch's test statistic from the sampled data as

<!-- chunk {"id": "body-0086", "role": "body", "section": "Smaller Planning Example", "weight": 1.0} -->

which follows Student's $t$-distribution under the null hypothesis $H_{0}$, where the pooled standard deviation $s_{i}$ is computed as

<!-- chunk {"id": "body-0087", "role": "body", "section": "Smaller Planning Example", "weight": 1.0} -->

To check whether the null hypothesis $H_{0}$ holds, we use a significance level of $\alpha = 0.05$ and compute the $p$-values $P{({t_{s,i} \geq \left. t_{{1 - \alpha},i} \middle| H_{0} \right.})}$ under the null hypothesis for the observed test statistics. This is done by utilizing the cumulative Student's $t$-distribution function with $N_{{DOF},i}$ degrees of freedom, computed through the Welch--Satterthwaite equation

<!-- chunk {"id": "body-0088", "role": "body", "section": "Smaller Planning Example", "weight": 1.0} -->

which is valid for the case when the sample sizes of the two means are equal. Here, $\varepsilon_{\cdot}$ is the standard deviation of the trajectory length for the relevant planner (equal to $32.0\ m$ in the smaller planning example for PQ-RRT\*). Then, the threshold value used to determine whether we reject the null hypothesis or not is given by $t_{{1 - \alpha},i} = {{tDistributionCDF}{({1 - \alpha},N_{{DOF},i})}}$, where $tDistributionCDF$ is the Student's $t$ cumulative distribution function. The results are summarized in Table, and show that the null hypothesis holds under the significance level of $\alpha = 0.05$ since all the $p$-values are non-significant ($> \alpha$).

<!-- chunk {"id": "body-0089", "role": "body", "section": "Larger Planning Example", "weight": 1.0} -->

The larger planning example considers the region shown in Fig. of size ${5.0\ {km}} \times {5.0\ {km}}$ with multiple islands and smaller grounding hazards, which increases the problem size substantially. Again, the planners are allowed to find and refine a solution over the maximum allowable iterations and nodes, up until a maximum time of $300\ s$. A constant reference speed $U_{d} = {5.0\ {m/s}}$ is utilized. In this case, due to the large map size, we utilize planner parameters as in Table.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Larger Planning Example", "weight": 1.0} -->

Visual results when applying the RRT-variants on the planning area in Fig. are shown for sample runs in Fig.. Table shows performance metrics for the algorithms over the MC runs. Again, we see a marginally better result for the PQ-RRT\* than for IRRT\* and RRT\*. In this planning example, IRRT\* achieves worse results than RRT\* due to the significantly higher sample rejection rate again caused by a large obstacle congestion ratio, amplified by the problem scale.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Larger Planning Example", "weight": 1.0} -->

The optimal solution is approximately $5.2\ {km}$, and thus we see that the optimal algorithm variants only converge to within approximately $30\%$ of the optimum. The convergence issue is attributed to the map size, the optimal solution passing through narrow passages, and the complexity of considering ship dynamics and kinodynamical constraints in the tree wiring. A standard deviation of over $500\ m$ is found for the path length solutions of all variants, which is significantly high.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Larger Planning Example", "weight": 1.0} -->

Again we check the statistical significance of PQ-RRT\* giving more distance-optimal trajectories than the other variants, by using a one-sided Welch's $t$-test as in the previous section, with the hypotheses. The results are summarized in Table, and again it is shown that the null hypothesis holds under the significance level of $\alpha = 0.05$ since all the $p$-values are non-significant.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Discussion", "weight": 1.5} -->

Gauging the results on planning, we see that the RRT-based planners are viable for use in problems of adequate size, i.e. less than ${1\ {km}} \times {1\ {km}}$ in map size. In these cases, the planners can find and optimize the best solution in adequate time. However, for larger maps, the planners struggle. This is attributed to the increased number of samples and iterations required in order to find and refine a solution. Although the planners find initial solutions fast, they have a hard time optimizing the solutions when considering larger map sizes and complex environments. The run-time also increases substantially for larger problem sizes, due to the higher computational cost of re-wiring the tree and propagating new node costs to the leaves. Thus, in such large cases, it can be an option to utilize RRT-based planners without dynamics consideration, where the tree wiring only considers position sampling and the connection of these through collision-free straight-line segments. Alternatively, one can use path complete algorithms such as A\*, to find the solution fast up to a suitable grid resolution, without having randomness in the result.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Discussion", "weight": 1.5} -->

Note that it will then be necessary to post-process the solution to generate a feasible trajectory for the ship to track, unless a motion primitives-based planner is used.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Discussion", "weight": 1.5} -->

We note that IRRT\*, although providing linear algorithm convergence properties for obstacle-free environments, struggles with both planning cases and especially the larger one. This is due to the large volume occupied by obstacles in the configuration space, leading to a significant rejection rate in the informed heuristical sampling. Thus, for IRRT\* to be of practical usage, it requires an improvement. This can be an update and creation of a new CDT for the safe sea domain inside the informed sampling domain, each time a new solution is found.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Discussion", "weight": 1.5} -->

For the PQ-RRT\* with nonholonomic steering, we see a large increase in computational effort due to the ancestry consideration. This was viable for the smaller planning case, but proved to be more limiting in the larger case unless the nonholonomic steering functionality is disabled or higher simulation time steps are used. Also, the algorithm run-time and performance are highly dependent on the sample adjustment procedure, itself being dependent on the three parameters $N_{sa}^{max}$, $\lambda_{sa}$, and $d_{margin}$. In total, this leads to a lower tree node number and can in the worst cases prevent the algorithm from finding solutions. Choosing $\lambda_{sa}$ too small yields negligible gain from the APF-based adjustments, and requires a higher iteration number $N_{sa}^{max}$, which again gives higher algorithm run-time due to an increased number of obstacle distance calculations being required. Conversely, a large $\lambda_{sa}$ can lead to rapid convergence towards local minima.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Discussion", "weight": 1.5} -->

We found that a selection of $\lambda_{sa}$ in the order of $0.1\%$ of the map width, and an adjustment number of around $N_{sa}^{max} \approx 50$ gave a reasonable trade-off between run-time and solution quality for the larger planning case in this work. For the clearance parameter $d_{margin}$ it was found necessary to select a smaller value of around $0.5\ m$, as a high value can prevent the planner from wiring into more confined areas. Because of these factors, we found the tuning of PQ-RRT\* to be significantly more challenging than the other variants. Judging from the marginal improvements found in this work with consideration of nonholonomic steering, we argue that it was easier to employ IRRT\* or RRT\*, which required less tuning effort and achieved comparable performance. In general, we note that the parameter selection is dependent on the vehicle steering system. Another tuning challenge is the selection of $\gamma$, also mentioned in Noreen et al., which has a large influence on performance.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Discussion", "weight": 1.5} -->

As the ball volume reduces with the tree size, too small values of $\gamma$ can lead to negligible search radius and can in the worst case effectively reduce optimal RRT variants to the baseline RRT, where no nearest neighbors other than the closest one are considered in the wiring. A solution to consider is to bound the search radius from below, or for simplicity consider a fixed search radius.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Discussion", "weight": 1.5} -->

We see that the common challenge of RRTs related to a slow convergence rate towards the optimum, is increasing when applying the algorithms to large and complex environments. This is partially due to the sampling inefficiency and node rejection rate issue found in most variants, and for which a significant amount of solutions have been proposed with varying levels of success. Also, for real-time systems and applications where time is a resource, the incremental tree wiring and re-wiring induce a computational cost that must be weighted against performance and optimality. Thus, we deem computationally constrained RRT-based planners without sophisticated sampling strategies and without coupling to graph-search-based methods such as A\*, to be more suitable for smaller problems, or problems where obstacles occupy a smaller portion of the configuration space, or where non-optimal solutions are acceptable. For planning in higher dimensional space, it is also necessary to consider other metrics than the Euclidean one.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this article, multiple algorithms for ship trajectory planning based on RRT have been developed and compared with respect to trajectory length and computational time. The comparison focuses on varying degrees of difficulty in a complex environment containing many non-convex grounding hazards, as opposed to the often simple environments used for testing in previous work.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Practical aspects to consider when employing such algorithms in the maritime domain are also outlined and discussed, to the benefit of researchers and practitioners in the field. It is also shown through an example case that RRT variants can be beneficial in the context of automatic test scenario generation, where target ship trajectories can be sampled efficiently directly from the nodes of a built RRT. The tree can alternatively be used to sample intention scenarios for use in intelligent CAS.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Conclusion", "weight": 1.5} -->

From Monte Carlo simulations on selected cases, we see that PQ-RRT\* attains more distance optimal trajectories, also verified through pair-wise hypothesis testing with Welch's $t$-test when using a significance level $\alpha = 0.05$. Here, IRRT\* and RRT\* follow close behind. This distance optimality comes naturally at the cost of increased run-time due to nearest neighbor searches and parent consideration in both tree wiring and rewiring. IRRT\* struggles with cases where obstacles cover a large part of the configuration space. In larger planning cases, more efficient sampling procedures are needed for optimal RRT\* variants to be viable due to the significant space of configurations that must be covered, causing a similar curse of dimensionality issue. This causes inefficiencies in the trade-off between computational effort, available memory, and performance, as the optimal variants will then spend the majority of their effort wiring and re-wiring their tree.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Conclusion", "weight": 1.5} -->

From the results and through tuning of the algorithm, it was found that the PQ-RRT\* involves much higher complexity in tuning than the other variants, because of the sample adjustment procedure and ancestor consideration. On the other hand, the IRRT\* algorithm here attains a good balance between simpler tuning and obtainable performance. It's informed sampling heuristic should, however, be improved to reduce its sample rejection rate. In the maritime domain, this can be achieved by an iterative pruning or update of a safe sea triangulation used to sample new collision-free configurations.
