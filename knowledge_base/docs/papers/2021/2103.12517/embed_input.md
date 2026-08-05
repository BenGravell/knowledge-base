<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Scenario-Based Trajectory Optimization in Uncertain Dynamic Environments

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present an optimization-based method to plan the motion of an autonomous robot under the uncertainties associated with dynamic obstacles, such as humans. Our method bounds the marginal risk of collisions at each point in time by incorporating chance constraints into the planning problem. This problem is not suitable for online optimization outright for arbitrary probability distributions. Hence, we sample from these chance constraints using an uncertainty model, to generate "scenarios", which translate the probabilistic constraints into deterministic ones. In practice, each scenario represents the collision constraint for a dynamic obstacle at the location of the sample. The number of theoretically required scenarios can be very large. Nevertheless, by exploiting the geometry of the workspace, we show how to prune most scenarios before optimization and we demonstrate how the reduced scenarios can still provide probabilistic guarantees on the safety of the motion plan. Since our approach is scenario based, we are able to handle arbitrary uncertainty distributions. We apply our method in a Model Predictive Contouring Control framework and demonstrate its benefits in simulations and experiments with a moving robot platform navigating among pedestrians, running in real-time.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Mobile robots are increasingly becoming part of our society, with applications in warehouses, automotive, maritime transportation, etc. In all these domains, it is essential that the robots can safely operate in dynamic environments (e.g., near humans). However, uncertainty is omnipresent, for example, in the future motion paths of the dynamic obstacles or in sensing (i.e., localization) errors. Our goal is to design a local robot motion planning algorithm able to plan collision-free trajectories in the presence of possibly unbounded and arbitrary uncertainties.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Optimization-based motion planning methods avoid collisions by imposing constraints in the optimization problem. Classical methods consider deterministic obstacle predictions, that is, they do not account for the presence of uncertainties. When uncertainties come into the picture, deterministic frameworks fail to achieve safety, since they do not consider the possible spread of outcomes. In the case of bounded uncertainties, that is, if the probability density function is non-zero in a bounded domain of the robot's workspace and is zero elsewhere, then it is possible to set the acceptable level of risk to zero. This approach is referred to as *robust optimization*. On the one hand, this approach allows for the addition of uncertainties in the deterministic framework. On the other hand, the assumption that the distribution is bounded can be limiting (e.g., when obstacle predictions are Gaussian). Additionally, it becomes conservative when the domain of support is large. In the presence of unbounded uncertainties, chance constraint optimization allows one to constrain the probability of collisions to be below an acceptable level of risk. In this work, and likewise to, we consider the marginal probabilities of collision at each point in time.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

This is, we constrain the chance of collision for each step of the trajectory, separately.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Directly evaluating these chance constraints is intractable, especially for arbitrary shapes of the distribution. Instead they are often either approximated (e.g., using particle filters ) or bounded. Approximation techniques have received most attention, due to their sample efficiency. However, the safety of these approaches cannot be guaranteed, especially when operating in unknown environments.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Contribution", "weight": 1.0} -->

In this work, we assume that a perception module provides predictions of the motion of dynamic obstacles together with a description of their (unbounded, possibly non Gaussian) uncertainty. To provide probabilistic safety for each step of the planned trajectory with respect to the modeled uncertainties, our work presents a novel *probabilistic trajectory optimization* framework for motion planning in uncertain dynamic environments, that is, a Scenario-based Model Predictive Contouring Control (S-MPCC) design. Our S-MPCC builds on nonconvex scenario-optimization framework and the model predictive contouring control (MPCC) design of. We show that in contrast with the general a posteriori results, we obtain the perceived risk of our motion plan before optimization. The support subsample, which is the key indicator for the risk, is obtained through the geometry of the problem, leading to efficient evaluation of the samples. While sampling-based chance constrained approaches are generally considered intractable for real-time motion planning, our method is competitive in terms of computation times with state-of-the-art planning methods, while applicable to generic uncertainties. The approach handles multiple obstacles and accounts for the size of the vehicle and obstacles.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contribution", "weight": 1.0} -->

We show how our approach allows the robot to move continuously through its environment while reasoning about its probability of colliding with dynamic obstacles. In our framework, illustrated in Fig. 2, instead of directly solving the chance constrained motion planning problem, we solve an associated deterministic problem obtained as follows. First, we apply a tailored linearization of the chance constraints, then we sample from the linearized chance constraints a large set of deterministic constraints, known as *scenarios*. The number of scenarios drawn is linked with the associated risk of collisions. This allows us to reformulate the original planning problem in a deterministic one, known as a scenario program. Using this approach we effectively resolve the chance constraints in a preprocessing step.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Contribution", "weight": 1.0} -->

Uncertainty of predictions is generally non Gaussian and appears, for example, when Gaussian uncertainty is propagated through nonlinear dynamics. Our method is applicable to generic uncertainties. We demonstrate our framework for Gaussian and non Gaussian uncertainties using an autonomous ground robot, both in simulation and in experiments.

<!-- chunk {"id": "body-0010", "role": "body", "section": "PROBLEM FORMULATION", "weight": 1.0} -->

We consider the motion planning problem of a mobile robot, whose dynamics can be represented by the following nonlinear discrete-time system: where ${\mathbf{x}}_{k} \in {\mathbb{R}}^{n}$ and ${\mathbf{u}}_{k} \in {\mathbb{R}}^{m}$ denote the states and inputs, respectively. The robot can move within a workspace (e.g., the 2D plane when we consider ground robots). In the workspace, the robot must avoid collisions with dynamic obstacles. We model the collision region of the robot $\mathcal{V}_{k}$ at time $k$ as the union of $n_{c}$ circles, and the collision region of the dynamic obstacles $\mathcal{D}_{k}^{v}$ at time $k$ as a single circle.

<!-- chunk {"id": "body-0011", "role": "body", "section": "PROBLEM FORMULATION", "weight": 1.0} -->

The position of dynamic obstacles along the planning horizon of the robot is uncertain. We denote the uncertainty of the obstacles at stage $k$ with a tuple $(\Delta_{k},\mathcal{D}_{k},{\mathbb{P}}_{k,\text{real}})$, where $\Delta_{k}$ is a probability space equipped with a $\sigma$-algebra $\mathcal{D}_{k}$ and a probability measure ${\mathbb{P}}_{k,\text{real}}$. We allow the probability spaces to be unbounded and non Gaussian. We assume that at each step a perception module provides the motion planner with an independent model of the uncertainty, formalized as follows.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The planner is provided with a model ${\mathbb{P}}_{k}$ of the real probability measure ${\mathbb{P}}_{k,\text{real}}$ for each $k$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Assumption 2 implies that the dependency induced, for example, by the dynamics of an obstacle, is handled by the perception module such that the uncertainties are independent as viewed from the perspective of the motion planner. The assumption is common in state-of-the-art perception modules, for example.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Under the, possibly unbounded, uncertainty of the dynamic obstacles, we constrain the marginal probability of collision at each time step of the trajectory using chance constraints, similarly to. Each chance constraint is subject to an acceptable risk level $\epsilon_{k}$, which can be tuned accordingly. This implies that we cannot give a non-conservative bound on the collision risk of the full motion plan. However, by frequently recomputing the motion plan, for example in an MPC framework, the actions in the near future are probabilistically safe and risk in later stages is reconsidered when the robot moves closer.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

We formulate the motion planning problem as follows: where ${\mathbf{u}} = {\{{\mathbf{u}}_{1},\ldots,{\mathbf{u}}_{N}\}} \in {\mathbb{U}}$ are the optimized system inputs subject to input constraints, ${\mathbf{δ}}_{k}^{v} \in \Delta_{k}^{v}$ is the uncertain position of obstacle $v$ at stage $k$ and ${J{({\mathbf{x}}_{k},{\mathbf{u}}_{k})}} \geq 0$ is the cost function specifying performance metrics. The radius $r$ is the sum of vehicle and obstacle radii. To simplify the notation, we assume this radius to be a constant.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The chance constraint, (2c), constrains the probability of collisions between each collision circle $d$ of the vehicle and the collision circle of each dynamic obstacle $v$ at prediction step $k$ to be below the risk level $\epsilon_{k}$, as visualized in Fig. 0(a). The probability measure ${\mathbb{P}}_{k}$ refers to the modeled uncertainty.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Problem is a chance constrained optimization problem. As discussed in Section IV, to solve this problem, we rely on the nonconvex scenario optimization (NSO) framework of, for which we provide an overview in the following section. This framework can in general provide a bound on the risk with respect to the unknown probability distribution ${\mathbb{P}}_{\text{real}}$, by sampling from the real system. In the real-time setting of this paper, however, collecting samples online is intractable. Instead we propose to sample from the model distribution $\mathbb{P}$, as defined in Assumption 1. For consistency of notation, the results of are presented here using the model $\mathbb{P}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "NONCONVEX SCENARIO OPTIMIZATION", "weight": 1.0} -->

The NSO framework allows us to replace chance constraints with deterministic constraints by sampling. Consider the Chance Constrained Problem (CCP) where $\mathbf{u}$ are decision variables, ${\mathbf{δ}} \in \Delta$ is the realization of the uncertainty and the function $g:{{{\mathbb{X}} \times \Delta}\rightarrow{\mathbb{R}}}$ is a nonlinear function associated with the nonconvex constraint ${g{({\mathbf{x}},{\mathbf{δ}})}} \leq 0$. The authors of established a link between CCP and the deterministic Scenario Program (SP): We denote its solution by ${\mathbf{u}}_{SP}^{\ast}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "NONCONVEX SCENARIO OPTIMIZATION", "weight": 1.0} -->

Each of the $S$ constraints in (4b) is constructed by drawing a sample ${\mathbf{δ}}^{i}$ from $\Delta$, and formulating the constraint ${g{({\mathbf{u}},{\mathbf{δ}}^{i})}} \leq 0$ in the scenario where the sample ${\mathbf{δ}}^{i}$ is a realization of the uncertainty. Since each of the samples specifies a scenario, the samples themselves are called scenarios and the constraints (4b) are known as scenario constraints. The violation probability, $V:{{\mathbb{U}}\rightarrow{\lbrack 0,1\rbrack}}$, given by defines the probability that input $\mathbf{u}$ violates a newly observed scenario.

<!-- chunk {"id": "body-0020", "role": "body", "section": "NONCONVEX SCENARIO OPTIMIZATION", "weight": 1.0} -->

The solution of the SP in depends on randomly sampled scenarios and hence its violation probability is a random variable over the product probability measure, given by ${\mathbb{P}}^{\text{S}}$ = ${\mathbb{P}} \times \ldots \times {\mathbb{P}}$ (S times). To link the SP of with the CCP of, we are therefore interested in bounding the probability that $V{({\mathbf{u}}_{SP}^{\ast})}$ satisfies our risk bound $\epsilon$, a probability which we refer to as the confidence. A key definition in this direction is the support subsample.

<!-- chunk {"id": "body-0021", "role": "body", "section": "NONCONVEX SCENARIO OPTIMIZATION", "weight": 1.0} -->

Definition: A support subsample of an SP is a subset of scenarios $\mathcal{S}_{\text{support}} \subseteq \mathcal{S}$ that results in the same optimizer as the original SP. The cardinality of the support subsample, that is, the support subsample size, is denoted by $s$. The smallest support subsample size is denoted by $s^{\ast}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "NONCONVEX SCENARIO OPTIMIZATION", "weight": 1.0} -->

Theorem 1 in provides the following confidence bound Here ${\epsilon{(s)}}:{{\{ 0,\ldots,S\}}\rightarrow{\lbrack 0,1\rbrack}}$ can be designed subject to and ${\epsilon{(S)}} = 1$, an example can be found in \[7, Sec. II\]. Equation theoretically links the sampling size $S$, confidence parameter $\beta$ (complement of the confidence) and risk $\epsilon$, based on the observed support sample size. Notice that in this work, as a consequence of using model distribution $\mathbb{P}$, the bound applies to the modeled uncertainty rather than the real robot, in contrast with \[7, Th. 1\].

<!-- chunk {"id": "body-0023", "role": "body", "section": "PROPOSED APPROACH", "weight": 1.0} -->

Our method relies on the Model Predictive Contouring Control (MPCC) framework to define the objective to optimize to plan a suitable path for the robots. Our method differs from in the way we deal with dynamic obstacles, as detailed in the rest of the section. As such we will refer to our approach as Scenario-MPCC (S-MPCC). To present the method, we consider a single dynamic obstacle and one of the discs used to represent the vehicle^11^1Section IV-D shows how this case extends linearly to multiple dynamic obstacles and multiple discs..

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-A Chance Constraints Linearized in the Robot Position", "weight": 1.0} -->

Chance constraints (2c) are nonconvex in the robot position when sampled (see discs in Fig. 0(c)) and the associated SP may have many local optima and a sizable support subsample. We therefore consider a linearization of the collision regions (depicted by the lines in Fig. 0(c)) before sampling to decrease the support subsample size of the SP. This step reduces the risk of its solution significantly. We modify the constraints as where we linearize the collision region with respect to ${\hat{\mathbf{x}}}_{k}$, the $k$-step ahead prediction of the robot position. We employ the trajectory of the previous planning cycle, forward propagated, as predictor.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-A Chance Constraints Linearized in the Robot Position", "weight": 1.0} -->

That is^22^2We denote by ${\mathbf{x}}_{t|k}$ the $k$-step ahead prediction of the robot trajectory for the MPC planning cycle at time $t$, ${\hat{\mathbf{x}}}_{t|k} = {\mathbf{x}}_{t - {1|{k + 1}}}$ and ${\hat{\mathbf{x}}}_{t|N} = {\mathbf{x}}_{t - {1|N}}$. Hence, we search for collision-free solutions around the planned trajectory of the previous planning cycle. We show in Sec. IV-C that after linearization, the free-space of the resulting SP is convex in the robot position. A comparison between chance constraints (2c) and (7b) for an example is provided in Fig. 1. The linearized chance constraints capture less of the shape of the distribution, but are accurate near ${\hat{\mathbf{x}}}_{k}$ and thus sufficient for motion planning.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-A Chance Constraints Linearized in the Robot Position", "weight": 1.0} -->

Note that the linearizations are performed for each stage of the trajectory, as illustrated in Fig. 0(b).

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-B Scenario Program", "weight": 1.0} -->

For each of the chance constraints in (7b) we construct a set of deterministic constraints by sampling from the uncertainty. The red circles in Fig. 0(c) represent these samples and the black lines are the *scenarios* (Sec. III). The resulting SP is given by The theoretic properties of SPs, discussed in Sec. III, are limited to CCPs with one chance constraint. However, (7b) describes multiple chance constraints, one for every stage of the planned trajectory. We now show that multiple chance constraints can be handled separately, resulting in a probabilistic feasibility property per stage.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-C Probabilistic Safety Guarantees", "weight": 1.0} -->

The key insight that makes our approach tractable is that due to the geometric structure of the problem, the free space may be described by only a small subset of the scenarios. To see this, first note that each scenario constraint in (8c) defines a half-space. The collision-free space, if it exists, is formed by the intersection of half-spaces and is convex, as i) each half-space is convex and ii) the intersection of convex constraints is convex. This results in a free space polytope $\mathcal{P}_{k}$ (see Fig. 0(d)), spanned by those half-spaces that form the boundary of the polytope. We may define this subset of half-spaces by their indices as The usefulness of the set $\mathcal{H}_{k}$ is twofold. First, we may replace (8c) with only those half-spaces that span polytope $\mathcal{P}_{k}$, greatly reducing the size of the online optimization problem.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-C Probabilistic Safety Guarantees", "weight": 1.0} -->

Second, the set $\mathcal{H}_{k}$ contains indices of the constraints that may be active during optimization and hence the support subsample is bounded by its cardinality, that is, $s_{k}^{\ast} \leq {|\mathcal{H}_{k}|}$. We use the latter fact to establish the link between the CCP subject to (7b) and SP. There always exists an upper bound, $\overline{s}$, for the cardinality of $\mathcal{H}_{k}$ and for our problem we find experimentally that this upper bound $\overline{s}$ is much smaller than the sample size. That is, for uncertainty distributions where the samples are not cluttered at the boundary, only few scenarios are active.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-C Probabilistic Safety Guarantees", "weight": 1.0} -->

We can now compute sampling size $S_{k}$ offline, using *(i)* Theorem 1, *(ii)* upper bound $\overline{s}$, *(iii)* confidence parameter $\beta_{k}$, and *(iv)* risk $\epsilon_{k}$. The SP we solve online is given: Algorithm 1 summarizes our method. Online, we sample from the distribution and identify the minimal polytope and the support subsample size (line 4-9). We then solve optimization problem (line 10) and use the first input as control input (line 11). In the following we provide a result for improving performance by discarding outlier scenarios.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-C Probabilistic Safety Guarantees", "weight": 1.0} -->

1: Compute Sk from ϵk, $\overline{s}$, for all k 3: Δkt← Retrieve uncertainty from perception module 6: Compute Aki, bki from (7a) for all samples 7: Find ℋk and verify $\left| \mathcal{H}_{k} \right| \leq \overline{s}$

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Bound is conservative. For example if we pick a random discarding algorithm for $\mathcal{R}$, then the samples are still iid and we can use directly with $S = P$, giving which is generally much tighter than. However, even if the bound is conservative we can use it to remove extreme scenarios, leading to generally better performance.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-D Multiple Dynamic Obstacles and Discs", "weight": 1.0} -->

To apply the strategy above to more than one obstacle, we use the fact that scenario optimization is distribution agnostic. We combine the predictions of the obstacles into a probability space $\Delta_{k} = \begin{bmatrix} \Delta_{k}^{0} & \ldots & \Delta_{k}^{V} \end{bmatrix}^{T}$, where samples are denoted ${\mathbf{δ}}_{k} = \begin{bmatrix} {\mathbf{δ}}_{k}^{0} & \ldots & {\mathbf{δ}}_{k}^{V} \end{bmatrix}^{T}$. Although the stacked distribution ${\mathbf{δ}}_{k}$ could be used to model the correlation between the movement of obstacles, we will sample each component separately from individual probability distributions.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-D Multiple Dynamic Obstacles and Discs", "weight": 1.0} -->

The chance constraints (7b) need to include all obstacles and are modified as follows The rest of the method follows analogously to the single obstacle approach but where the scenarios are drawn for each obstacle, resulting in more scenarios to process before obtaining the free space polytope. In the case of multiple vehicle discs, we formulate multiple chance constraints of the form (2c), one for each collision disc. We apply the method described in this Section per disc as samples for each of the discs are independent.

<!-- chunk {"id": "body-0035", "role": "body", "section": "S-MPCC WITH GAUSSIAN UNCERTAINTIES", "weight": 1.0} -->

A common class of uncertainties are the (truncated) Gaussian uncertainties. This section presents a detailed formulation of Algorithm 1, namely Algorithm 2, one can use in the case of (truncated) Gaussian uncertainty.

<!-- chunk {"id": "body-0036", "role": "body", "section": "S-MPCC WITH GAUSSIAN UNCERTAINTIES", "weight": 1.0} -->

The first step of Algorithm 2 is to determine the sample size. We set $\epsilon_{k} = {1 - 0.9889}$, equivalent to the probability mass under the $3\sigma$ interval of a bivariate Gaussian (generally considered as safe). Since the risk has logarithmic dependency on $\beta_{k}$, $\beta_{k}$ is generally small. We pick $\beta_{k} = {1 \cdot 10^{- 6}}$, i.e., one in a million SPs may not be feasible for the original CCP^33^3Note that the designer can choose to keep safety margin in the obstacle radius such that a failure does not have to result in a collision.. The removal size $R = 50$ is empirically determined, verifying that outliers are removed. Upper bound $\overline{s}$ is guessed and increased until it is never exceeded in practice. We find $\overline{s} = 20$. Evaluating, we are able to pick $S_{k} \approx 53050$ (line 1).

<!-- chunk {"id": "body-0037", "role": "body", "section": "S-MPCC WITH GAUSSIAN UNCERTAINTIES", "weight": 1.0} -->

We note that the main dependency of the sample size is the acceptable risk $\epsilon_{k}$. Sampling more scenarios results in a higher probability of safety, but at the cost of more conservative trajectories and increased computation times.

<!-- chunk {"id": "body-0038", "role": "body", "section": "S-MPCC WITH GAUSSIAN UNCERTAINTIES", "weight": 1.0} -->

\bigcup\mathcal{H}_{k}^{\text{range}} \right.$ Algorithm 2 Detailed S-MPCC for (truncated) Gaussian Instead of online sampling, we may sample a set of parameterized samples offline followed by an online transformation. This reduces the online operations, resulting in lower computation times. We describe this approach for the (truncated) Gaussian case. We generate offline a number of batches with $S_{k}$ bivariate Gaussian samples, centered at the origin and with $\mathbf{\Sigma} = {\mathbf{I}}$, where $\mathbf{I}$ is the identity matrix (line 2-4). These samples are obtained using the Box-Muller Transformation (BMT), which also allows us to draw radially truncated Gaussian samples by simply changing the support domain of $u_{1}$ to $\lbrack e^{- \frac{r^{2}}{2}},1\rbrack$. Most of the samples will be in the center of the distribution and will not be relevant online.

<!-- chunk {"id": "body-0039", "role": "body", "section": "S-MPCC WITH GAUSSIAN UNCERTAINTIES", "weight": 1.0} -->

Hence, we run our online algorithm for scenario selection (explained later), offline and aggregate the set of selected scenarios. Scenarios that are not in this set are pruned offline (line 5). In the $3\sigma$ example, approximately $95$% of the scenarios are removed offline.

<!-- chunk {"id": "body-0040", "role": "body", "section": "S-MPCC WITH GAUSSIAN UNCERTAINTIES", "weight": 1.0} -->

Online, we are only required to transform the offline samples from the standard bivariate normal distribution to the estimated mean and variance of the uncertainty (line 8), which is computed using We select for each obstacle only one batch of samples. The obstacle predictions are sampled with that batch for all stages and all time steps. This provides the motion planner with consistent constraints. To further reduce the computational load, we search online only for the $l + R$ scenarios closest to considered vehicle position, where we use $l = 150$ in the following experiments, we assume that this set contains the support subsample. We then apply the discarding algorithm $\mathcal{R}$, which removes the $R$ scenarios furthest from the mean of the distribution (line 9). We construct half-spaces from the remaining $l$ scenario and add four half-spaces to constrain the vehicle in a square workspace. To find the minimal polygon in 2D from this set of half-spaces, we use an intersection based algorithm (line 10). The algorithm explores the intersections in the inner polygon in a counter-clockwise fashion. The lines traveled form the minimal polygon.

<!-- chunk {"id": "body-0041", "role": "body", "section": "S-MPCC WITH GAUSSIAN UNCERTAINTIES", "weight": 1.0} -->

In the following simulations and experiments, we incorporate our dynamic obstacle avoidance method in the MPCC framework. We introduce a cost term that activates when the robot gets close to the boundaries of the free space polygon, to penalize movement close to pedestrians.

<!-- chunk {"id": "body-0042", "role": "body", "section": "S-MPCC WITH GAUSSIAN UNCERTAINTIES", "weight": 1.0} -->

(b) Radially truncated Gaussian (c) Width truncated Gaussian Figure 3: Simulations using our S-MPCC with 6 crossing pedestrians for 3 types of uncertainties. The top row visualizes the robot (blue) and pedestrian (red) trajectories, where newer positions are depicted with lighter shades. The bottom row visualizes the free space and active samples at stages 1, 8 and 15 in red, orange and yellow. All samples considered online are shown in black. The robot’s current and predicted occupied area are denoted in black and blue, respectively.

<!-- chunk {"id": "body-0043", "role": "body", "section": "S-MPCC WITH GAUSSIAN UNCERTAINTIES", "weight": 1.0} -->

Max Collision Prob. Stage 1 (# Violations) Time to Completion Mean (Std.) [m] Computation Time Mean (Max) [ms] TABLE I: Statistic results of the probability of collision with respect to the estimated uncertainty for the first stage (evaluated using Monte Carlo sampling) and violations of the specified risk, the task completion time and the computation times. The results are collected from 100 simulations of a crossing scenario for n ∈ {2, 4, 6} pedestrians.

<!-- chunk {"id": "body-0044", "role": "body", "section": "RESULTS", "weight": 1.0} -->

In this section, we present simulation and real-world results for a mobile robot navigating among pedestrians. Moreover, we present a qualitative analysis and performance results of our method against two baselines: MPCC and Collision Avoidance with Deep RL (CADRL).

<!-- chunk {"id": "body-0045", "role": "body", "section": "VI-A Experimental Settings", "weight": 1.0} -->

Our experimental platform is the Clearpath Jackal robot equipped with an Intel i5 CPU@2.6GHz. For the robot and pedestrian's localization we have used the OptiTrack system. Our simulations use the open-source ROS implementation of the Jackal Gazebo for the robot simulation and Social Forces model for pedestrian simulation.

<!-- chunk {"id": "body-0046", "role": "body", "section": "VI-A Experimental Settings", "weight": 1.0} -->

To solve SP, we use the ForcesPro solver. The robot dynamics are described by a continuous-time second-order unicycle model. The model is discretized with steps of $200$ ms. The time horizon is set to $3$ seconds divided into $15$ stages. The sampling period for control is $50$ ms.

<!-- chunk {"id": "body-0047", "role": "body", "section": "VI-B Simulation Results", "weight": 1.0} -->

We compare the proposed method against two methods for Gaussian uncertainties. The first is a baseline MPCC approach in which the ellipses used to represent the obstacles are obtained from the level sets of a known Gaussian distribution of the uncertainties. For comparison, we use the same tuning for both approaches (the interested reader can refer to for details on the definition of the cost function and general constraints). The main difference between the two approaches is the handling of dynamic obstacles (i.e., ellipsoidal level sets vs. scenario constraints). The second method for comparison is CADRL. We use the open source ROS implementation in the following simulations. Similar to MPCC we employ ellipsoidal level sets as the collision region of the obstacles.\The simulation environment consists of a straight road where pedestrians are crossing freely, as depicted in Fig. 3. The robot objective is to follow the centerline of the road. We evaluate our method for 2, 4 and 6 pedestrians. The uncertainty of the pedestrian predictions is Gaussian with a variance of $\mathbf{\Sigma} = {0.1^{2}{\mathbf{I}}}$. We set a pedestrian radius of zero.

<!-- chunk {"id": "body-0048", "role": "body", "section": "VI-B Simulation Results", "weight": 1.0} -->

Fig. 3(a) depicts one simulation of S-MPCC with 6 pedestrians. Aggregated results over 100 simulations are presented in Table I. In all tested cases, collisions are prevented by S-MPCC, while additionally the risk, evaluated over the perceived uncertainty, remains below the specified $3\sigma$ threshold. The MPCC method frequently switches between locally optimal trajectories resulting in collisions when it becomes infeasible. CADRL is reactive, which in the simulated environment leads it to positions where collisions may not be avoided. This behavior becomes worse with more obstacles. Interestingly, we find that S-MPCC results in smoother trajectories than both methods which results in earlier arrival at the goal. The downside is that the computation time of our method is higher. The computation time may be decreased by considering only the pedestrians close to the estimate ${\hat{\mathbf{x}}}_{k}$. We repeated the simulation with $6$ pedestrians in this case. The computation time was reduced to $6.86$ ms mean and $40.94$ ms maximum.\Figure 4: Experimental results with the robot avoiding two crossing pedestrians.

<!-- chunk {"id": "body-0049", "role": "body", "section": "VI-B Simulation Results", "weight": 1.0} -->

The orange circles depict the robot’s plan, while the blue and green circles the pedestrians’ (constant velocity) predictions. The solid black lines depict the road boundaries.

<!-- chunk {"id": "body-0050", "role": "body", "section": "VI-B Simulation Results", "weight": 1.0} -->

Evaluation of S-MPCC for non Gaussian uncertainties is depicted in Fig. 3. Here, the previous Gaussian predictions are radially truncated at $3.5\sigma$ (Fig. 3(b)) and truncated in their width at $2.5\sigma$ (Fig. 3(c)). In this scenario, width truncated uncertainties incorporate the domain knowledge that pedestrians are expected to cross at a crosswalk. Level set based approaches are not applicable in this case, as the geometry of the level sets depends on the specified risk threshold. We adapt the pedestrian locations to simulate a crosswalk. In contrast to the previous simulations, we specify an obstacle radius of 0.3 m and a variance of $\mathbf{\Sigma} = {0.08^{2}{\mathbf{I}}}$. We evaluate the probability of collision in the first stage, with respect to the estimated uncertainty over 100 tests using Monte Carlo sampling. We find a maximum risk of $0.00305$ for radial truncation and $0.02038$ for width truncation.

<!-- chunk {"id": "body-0051", "role": "body", "section": "VI-B Simulation Results", "weight": 1.0} -->

The violation of our method in the case of width truncation corresponds to a single case where the horizon is not long enough to correctly assess the risk of the full task a priori. This leads the robot to a state where our method cannot find a trajectory that satisfies the risk bound along the horizon and the optimization becomes infeasible. By increasing the horizon, the risk can be anticipated earlier, improving feasibility at the cost of larger computation times. The maximum risk over the other simulations was at most $0.0070$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "VI-C Real-World Results", "weight": 1.0} -->

We evaluated our method on real navigation situations with pedestrians. In the experiment, the robot navigates on a road following the lane central line when two pedestrians cross the robot's path. We modeled the noise on the pedestrian predictions as Gaussian distributions truncated at $3.5\sigma$. Fig. 4 provides snapshots of one experiment^44^4A video of the experiments and simulations accompanies this paper..

<!-- chunk {"id": "body-0053", "role": "body", "section": "CONCLUSIONS AND FUTURE WORK", "weight": 1.0} -->

In this paper we presented a Scenario-based Model Predictive Contouring Control (S-MPCC) method for mobile robot motion planning in the presence of dynamic obstacles with arbitrary position distributions. The main idea was to pursue a scenario-based method (translating probabilistic constraints into deterministic ones), generating scenarios from a model of the uncertainty. By using geometry considerations we were able to prune the possible outcomes (scenarios), while providing a bound on the marginal risk with respect to the modeled probability distribution. We demonstrated in simulations that the proposed method outperformed two recent baselines, in the sense that it generated trajectories that were significantly safer and more efficient. This came at a higher processing cost, but the method is still real-time capable. We furthermore illustrated the proposed method in a real-world experiment with a moving robot platform navigating among pedestrians. To further reduce the uncertainties and improve the navigation of the robot, incorporating the interactions between robot and pedestrians would be useful. The risk bounds that our method provides on the modeled uncertainty can still be improved by alleviating the standing assumption that requires our uncertainty models per stage to be independent. Additionally, the risk bound on the planned trajectory is relatively conservative.

<!-- chunk {"id": "body-0054", "role": "body", "section": "CONCLUSIONS AND FUTURE WORK", "weight": 1.0} -->

A tighter bound can be useful for planning safer long term motion, especially when the robot dynamics are slow. Alleviating these limitations are part of our future work.
