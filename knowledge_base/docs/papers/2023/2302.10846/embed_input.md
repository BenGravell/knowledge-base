<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Probabilistic Risk Assessment for Chance-Constrained Collision Avoidance in Uncertain Dynamic Environments

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Balancing safety and efficiency when planning in crowded scenarios with uncertain dynamics is challenging where it is imperative to accomplish the robot's mission without incurring any safety violations. Typically, chance constraints are incorporated into the planning problem to provide probabilistic safety guarantees by imposing an upper bound on the collision probability of the planned trajectory. Yet, this results in overly conservative behavior on the grounds that the gap between the obtained risk and the specified upper limit is not explicitly restricted. To address this issue, we propose a real-time capable approach to quantify the risk associated with planned trajectories obtained from multiple probabilistic planners, running in parallel, with different upper bounds of the acceptable risk level. Based on the evaluated risk, the least conservative plan is selected provided that its associated risk is below a specified threshold. In such a way, the proposed approach provides probabilistic safety guarantees by attaining a closer bound to the specified risk, while being applicable to generic uncertainties of moving obstacles. We demonstrate the efficiency of our proposed approach, by improving the performance of a state-of-the-art probabilistic planner, in simulations and experiments using a mobile robot in an environment shared with humans.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Mobile robots are appealed to work in complex environments shared with humans, such as smart warehouses, autonomous driving and maritime transportation. In these applications, the robot needs to progress toward its goal while safely avoiding static and dynamic obstacles. This task poses great challenges due to the fact that the robot needs to account for the possible uncertainties associated with the future predicted states of moving obstacles, as well as localization errors. These uncertainties make it difficult to decide whether the planned trajectories by the robot are safe or if given specifications, such as safety distance, are not violated. As a consequence, uncertain scenarios require mobile robots to find a reasonable trade-off between safety and efficiency. This gives rise to the the problem of risk-aware motion planning in uncertain dynamic environments.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we address the problem of estimating the risk associated with the collision probability of mobile robots surrounded by moving obstacles and integrating the estimated risk in a local motion planning framework to plan collision-free trajectories while balancing risk and progress. In particular, the probability of collision is estimated by integrating over the spatial domain at which the robot's plan and obstacles' predicted states overlap. The proposed risk metric is, consequently, measured by the maximum risk value over different time instants within a prediction horizon. To that end, we integrate this risk metric into a probabilistic motion planning framework to enhance its efficiency, in terms of traveling time, while maintaining the estimated risk below a specified upper level.

<!-- chunk {"id": "body-0005", "role": "body", "section": "I-A1 Collision Avoidance Under Uncertainty", "weight": 1.0} -->

Optimization-based motion planning algorithms can plan collision-free trajectories in uncertain environments by incorporating the uncertain behavior of dynamic obstacles as constraints into the optimization problem. These algorithms can be classified into two common approaches, namely robust optimization and stochastic optimization. Robust optimization approaches are able to provide safety guarantees by rigorously accounting for bounded sets of uncertainties, that is the probability density function of the uncertainty is non-zero over a bounded domain of the robot's workspace and is zero elsewhere. However, since robust optimization accounts for all possible realization of the uncertainty, its behavior is too conservative and may lead to infeasible solutions in crowded scenarios. On the contrary, stochastic optimization allows for the violation of the constraints as long as the probability of this violation is below an acceptable upper bound, which is specified through chance constraints. In this work, we rely on a stochastic optimization approach.

<!-- chunk {"id": "body-0006", "role": "body", "section": "I-A2 Safety Assessment in Motion Planning", "weight": 1.0} -->

One of the key components in safety analysis for motion planners is the risk metric that quantifies the risk level. For risk-aware motion planning algorithms, this risk metric usually indicates the collision probability due to, among others, the uncertain behavior of dynamic obstacles or imprecise localization of the robot. In, Gaussian process regression is employed to build a probabilistic model of the environment which is used to construct a risk-aware cost function. This cost function is then encoded into an optimal motion planning algorithm. builds spatiotemporal probabilistic risk maps. These maps indicate how risky a planned trajectory (computed by a rapidly-exploring random tree algorithm) will be, and are used to plan the best possible future behavior that maximizes utility while minimizing risk. A similar idea is used in to estimate the risk of violating a predefined safety specification and encode it into a sampling-based trajectory planner to plan minimal-risk trajectories. A drawback of these approaches, however, is the high computational cost due to the extensive trajectory generation as well as the bias in the trajectory selection.

<!-- chunk {"id": "body-0007", "role": "body", "section": "I-A2 Safety Assessment in Motion Planning", "weight": 1.0} -->

Related to our risk definition, and propose an analytic approach to calculate the probability of spatial overlap for a ground vehicle with dynamic obstacles at discrete times. Along the same line as our approach, proposes a framework, using signal temporal logic, which provides probabilistic safety guarantees that can be embedded in a receding horizon controller. However, their approach is restricted to safety constraints on random variables with unimodal distributions. Differently from the aforementioned approaches, in this paper, we propose an approach to incorporate a posterior risk assessment for planned trajectories into a probabilistic motion planning framework that applies to general probability distributions. From it is noted that the observed risk of the planned trajectory is much lower than the upper bound of the specified risk in the chance constraint problem. This conservatism can be attributed to the collision probability marginalization of the planned trajectory. That is, the collision probability at each planning step along the horizon is independent.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

To alleviate the over-conservatism problem with probabilistic motion planners, we propose the following: Multiple probabilistic planners run in parallel with different upper bounds of the specified risk. The set of planners should include the planner where the upper bound of the risk is the desired one, which is the most conservative planner.

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

An online posterior risk assessment is provided to quantify the risk associated with each planned trajectory from the multiple planners.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

Deploy the control commands from the planner with the least conservative behavior as long as its associated risk is below the specified risk of the most conservative planner.

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

In this way, the proposed approach provides probabilistic safety guarantees while achieving a closer bound to the specified risk, resulting in more efficient and less conservative performance.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

(a) Predicted positions of the robot and pedestrian at stage k are visualized in faded orange and green, respectively. One realization of the pedestrian’s uncertainty spatially overlaps with the robot’s planned trajectory.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

(b) Probability density function of the GMM representing pedestrian motion uncertainty at stage k. Only two modes are presented in this Fig.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Dynamic Obstacle Model", "weight": 1.0} -->

Each dynamic obstacle $v \in \mathcal{I}_{v}:={\{ 1,\ldots,n\}}$ is represented by a circle with radius $r_{v}$. The probability measure associated with the uncertainty of the perception of the dynamic obstacles is denoted by $\mathbb{P}$ and defined over the probability space $\Delta$. Without loss of generality, the uncertainty associated with obstacle movement is modeled as a Gaussian Mixture Model, where $n$ is the number of modes of the GMM, $\phi_{i}$ represents the weight of each mode such that ${\sum_{i = 1}^{n}\phi_{i}} = 1$, and $f_{k,i}^{v}{(.)}$ is the probability density function of each mode with mean ${\mathbf{μ}}_{i}$ and covariance $\mathbf{\Sigma}_{i}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B Dynamic Obstacle Model", "weight": 1.0} -->

Assumption 1. We assume that at each stage, a perception module provides the planner with a model of the probability.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-C Probabilistic Collision Avoidance", "weight": 1.0} -->

Definition 1. (Chance-Constrained Collision Avoidance) Given a cost function $J$, the initial state of the robot $\mathbf{x}_{0} = \mathbf{x}_{\text{init}}$, and the state distribution of obstacles $v \in \mathcal{I}_{v}$, the objective is to compute optimal control inputs that guide the robot from its initial state to progress along a reference path, while the collision probability with the moving obstacles at each stage $k$ is below an acceptable threshold $\epsilon_{k}$. The resulting optimization problem is given by where $J_{k}{({\mathbf{x}}_{k},{\mathbf{u}}_{k})}$ represents the stage cost of the robot, and $J_{N}{({\mathbf{x}}_{N})}$ denotes the terminal cost.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-C Probabilistic Collision Avoidance", "weight": 1.0} -->

States ${\mathbf{x}}_{k}$ and inputs ${\mathbf{u}}_{k}$ are bounded by the state and input constraint sets $\mathbb{X}$ and $\mathbb{U}$ respectively. ${\mathbf{δ}}_{k}^{v} \in \Delta_{k}^{v}$ is the realization of the uncertain position of obstacle $v$ at stage $k$. The radius $r$ is the summed radii for the robot's disc $d$, and obstacle $v$. The chance constraint, defined in (3d), constrains the marginal probability of collision at each stage of the trajectory to be below the risk level $\epsilon_{k}$. In this paper, the stage cost $J_{k}{({\mathbf{x}}_{k},{\mathbf{u}}_{k})}$ is defined by the Model Predictive Contouring Control framework proposed in to track a reference path, and a reference velocity while penalizing the control inputs.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-C Probabilistic Collision Avoidance", "weight": 1.0} -->

By solving the optimization problem, we obtain a locally optimal sequence of commands $\left\lbrack {\mathbf{u}}_{k}^{\ast} \right\rbrack_{k = 0}^{k = {N - 1}}$ to guide the robot along the reference path while avoiding collisions with dynamic obstacles. Here it should be pointed out that a global reference path is assumed to be provided to our local planner by a means of a global planner. This reference path is composed of $M$ way-points $p_{m}^{r} = {\lbrack x_{m}^{r},y_{m}^{r},\theta_{m}^{r}\rbrack} \in \mathcal{W}$ with $m \in {\{ 1,\ldots,M\}}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Proposed Approach", "weight": 1.0} -->

In this work, we aim to define a risk metric that can be incorporated into a probabilistic motion planner framework to balance safety and efficiency in a comprehensible way. This is motivated by the fact that state-of-the-art probabilistic planners, for navigation in environments with non-gaussian uncertainties, are overly conservative, e.g.,. In particular, we rely on scenario-based MPC proposed in as our probabilistic planner to enhance its efficiency. Nevertheless, the proposed approach is agnostic to the deployed probabilistic planner and can be widely applicable. In scenario-based MPC, the risk bound $\epsilon_{k}$, at each stage $k$ is correlated to the number of samples drawn from the uncertainty. From, it is noted that without manually tuning the number of samples extracted from dynamic obstacles uncertainty, the level of risk associated with the planned trajectory is much lower than the upper bound of the acceptable risk. This, in turn, results in conservative plans. Here it is worth pointing out that tuning the samples manually can only be done a posteriori and thus it is not suitable for online planning where the observed risk is not known a priori.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Proposed Approach", "weight": 1.0} -->

Therefore, we propose to quantify the risk associated with the planned trajectories from multiple scenario-based MPCs, running in parallel with different risk bounds, online and pick the least conservative plan as long as its associated risk is below a specified threshold.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Scenario-based MPC", "weight": 1.0} -->

Similar to, since the chance constraint defined in (3d) is non-convex, we first linearize it with respect to the previously planned robot trajectory ${\hat{\mathbf{x}}}_{k}$. The linearization is applied locally at each stage $k$, and robot disc $d$. This results in By linearizing the collision region with respect to ${\hat{x}}_{k}$, it can be seen that each scenario constraint in (4b) defines a half-space. The free space of the scenario program is, in turn, formed by the intersection of these half-spaces resulting in a convex constraint, that spans a polytope $\mathcal{P}_{k}$, with respect to the robot's position.\Evaluating the chance constraints in a closed loop is not computationally feasible. Thus, it is aimed to formulate them into deterministic constraints using scenario optimization, resulting in a tractable constrained optimization problem that can be solved online in a receding horizon manner.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A Scenario-based MPC", "weight": 1.0} -->

As shown, the probabilistic chance constraints can be transformed to deterministic ones by leveraging a deterministic scenario program (SP) for a finite set of samples/scenarios ${\mathbf{ω}} = \left({\mathbf{δ}}^{},\ldots,{\mathbf{δ}}^{(S)} \right)$, where each scenario is independently extracted from $\mathbb{P}$. Hence, the chance constraint problem can be reformulated as where the chance constraint (4b) has been replaced with the deterministic constraints (5d) for each extracted scenario. The probability that the planned input $\mathbf{u}$ violates the predefined acceptable risk $\epsilon$ is defined as $V{({\mathbf{u}}^{\ast})}$ and upper bounded by a confidence level $\beta$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A Scenario-based MPC", "weight": 1.0} -->

This confidence bound is defined by where ${\mathbb{P}}^{\text{S}}$ is the product probability measure, given by ${\mathbb{P}}^{\text{S}} = {{\mathbb{P}} \times \cdots \times {\mathbb{P}}}$ (S times), and $s$ is the size of the support subsample, that is the minimum number of samples that results in the same solution as the original sample $S$. In other words, if a scenario can be excluded from the scenario set $\mathbf{ω}$ without affecting the optimizer solution, this scenario is then not part of the support subsample. establishes a relationship between sample size, risk, and support subsample. The readers can refer to for a comprehensive overview.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Risk Assessment", "weight": 1.0} -->

In this paper, the risk is defined as the probability of collision of each of the robot's discs with any of the moving obstacles. Given the planned trajectory $\mathcal{T}$ of the robot for a controller, and the probability density function $f_{k}^{v}{(x,y)}$ that defines the uncertainty of the dynamic obstacle's movement in a 2D plane, it is possible to calculate the cumulative density function (CDF) for each obstacle $v$ at each stage $k$ along the prediction horizon by evaluating the integration of their associated probability density function at the robot's disc predicted position ${\mathbf{x}}_{k}^{d}$.\Definition 2. (Risk Metric) Let $\mathcal{Z}$ denote the set of random variables representing the uncertainty of the pedestrians' motion in the $x$ and $y$ directions.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B Risk Assessment", "weight": 1.0} -->

The risk metric maps the distribution of the random variables to a real number indicating the probability of collision, $\zeta:{\mathcal{Z}\mapsto{\mathbb{R}}}$, by estimating their spatial overlap with the robot's plan $\mathcal{T}$. The probability of collision can, subsequently, be defined as This integration can be approximated numerically using the Monte Carlo method, where the integration domain $D$ is defined as a circle whose center is located at the predicted vehicle pose ${\mathbf{x}}_{k}^{d}$ at stage $k$ along the prediction horizon, and its radius $r$ is the sum of the vehicle and obstacle radii.\After calculating the probability of collision for each pedestrian along the robot's planned trajectory, the predicted risk at the current time step is defined by maximizing the collision probability for all pedestrians at all planning horizon stages.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B Risk Assessment", "weight": 1.0} -->

The max operator in ensures that the worst-case overlap is considered over the planned trajectory. The proposed approach is illustrated in Fig. III, for a single pedestrian and one realization of the associated uncertainty at stage $k$, and summarized in Algorithm 1, where $\varnothing$ indicates that no feasible solution is obtained from any of the controllers.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B Risk Assessment", "weight": 1.0} -->

A set of scenario-based MPCs π ∈ ℐπ:= {1, …, n} with different ϵi ∈ {ϵ1, …, ϵn} values where they are defined in a descending order, and a predefined risk threshold ϵ∘ = ϵn Control input command: u = ⌀ Evaluate the estimated maximum risk ζ from u ← Deploy maximum deceleration Algorithm 1 Risk-Aware scenario-based MPC

<!-- chunk {"id": "body-0028", "role": "body", "section": "Results", "weight": 1.0} -->

In this section, we describe our implementation of the proposed method, for a mobile robot navigating in a crowded environment shared with humans, and evaluate it in simulations and experiments.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A1 Software Setup", "weight": 1.0} -->

The motion planner is implemented as a ROS node in C++. Our simulations use the open-source ROS implementation of the Jackal Gazebo for the robot simulation. To solve SP, we use ForcesPro solver. A horizon of $N = 20$ steps is defined, with a discretization step of 0.2 s, resulting in a time horizon of 4.0 s. The control rate is set to 20 Hz corresponding to a sampling time of 50 ms. The computer running the simulations is equipped with an Intel^®^ Core^TM^ i7 CPU@2.6GHz. The robot dynamics are described by a continuous-time second-order unicycle model. The radius of each robot's circle is set to 0.325 m with $n_{c} = 2$, and the obstacle radius is set to 0.3 m.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-A1 Software Setup", "weight": 1.0} -->

Avg. Min Dist. [m] Table I: Statistical results over 100 experiments for a uni-modal simulation with 6 pedestrians. The comparison is done with respect to the maximum risk endured by the robot, duration, robot velocity, number of times the robot has to come to standstill, and minimum distance to the obstacles. The results are reported as “average (standard deviation)”. The percentage of controller usage with ϵ = 0.2, ϵ = 0.1 and ϵ = 0.05 is 87.98%, 12.02% and 0%, respectively.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A1 Software Setup", "weight": 1.0} -->

Avg. Min Dist. [m] Table II: Results similar to those in I for uni-modal simulation with 10 pedestrians. The percentage of controller usage with ϵ = 0.2, ϵ = 0.1 and ϵ = 0.05 is 87.45%, 7.25% and 5.30%, respectively.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-B Simulation Results", "weight": 1.0} -->

To create the reference path, a series of waypoints are defined and connected with a clothoid. The goal of the robot is to track the reference path as closely as possible while avoiding colliding with its surrounding dynamic obstacles, which are crossing freely. The baseline that we compare our results against is the scenario-based MPC approach proposed, with different risk levels $\epsilon$. In the following simulations, three scenario-based MPCs run in parallel with different acceptable risk levels, 0.05, 0.1, and 0.2. These values are chosen as a proof of concept of the proposed method. An upper bound of collision probability (CP), along a single planned trajectory, is set to 0.05. After each planning cycle, the maximum risk associated with each planned trajectory, from the three planners, is estimated according to, then the control commands from the controller with the least conservative solution, i.e., the one with the maximum risk level, are applied as long as the associated risk is less than $\epsilon_{\circ} = 0.05$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-B Simulation Results", "weight": 1.0} -->

In case no feasible solution is obtained from all controllers without violating the threshold risk level, emergency braking is deployed so that the robot decelerates.\Several metrics are defined to compare the safety and efficiency of the proposed approach with the baseline. As safety metrics, we measure the maximum probability of collision per stage along the robot's planned trajectory, and the average minimum distance between the robot and the pedestrians, that is the distance between the robot's and pedestrian's circles' boundaries together with the percentage of physical collisions. As efficiency metrics, average speed, duration, and the temporary freezing percentage, that is the situations in which the robot has to come to a standstill in order to retain safety, are calculated. We consider a scenario as a temporary freezing scenario when the robot takes more than 2.0 s before it starts to accelerate again from a standstill. The reference velocity of the robot is set to 2.0 m/s whereas the velocity of the pedestrians is set to 1.0 m/s. The setup of the simulation is shown in Fig. 2.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-B1 Pedestrians with Gaussian noise", "weight": 1.0} -->

In the first scenario, the uncertainty of the pedestrian predictions is uni-modal Gaussian with a variance of $\mathbf{\Sigma}_{w} = {0.5^{2}{\mathbf{I}}}$. We define the pedestrian dynamics as where $v \in {\mathbb{R}}^{2}$ describes a constant velocity. Aggregated results in environments with 6 and 10 pedestrians, over 100 simulations, are presented in Tables I and II respectively. As shown in Table I, the controller with $\epsilon = 0.05$ achieves the lowest collision probability compared to other controllers, however, at the expense of resulting in excessively conservative trajectories. This conservatism can also be observed in the percentage of temporary freezing, in which the controller cannot find a solution that satisfies the risk bound along the planning horizon and the robot decelerates to a standstill. It can also be seen that the temporary freezing behavior decreases as the acceptable risk level increases, but this happens at the expense of violating the acceptable risk level $\epsilon_{\circ}$, for the controller with $\epsilon = 0.2$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-B1 Pedestrians with Gaussian noise", "weight": 1.0} -->

On the contrary, by switching between the controllers based on the associated risk level, we can obtain less conservative results where the performance is comparable to the behavior of the controller with $\epsilon = 0.2$, but, most importantly, without violating $\epsilon_{\circ}$. Since the maximum collision probability for the controller with $\epsilon = 0.1$ never exceeds $\epsilon_{\circ}$, our method did not switch to the controller with $\epsilon = 0.05$, as the same safety level can be achieved with a less conservative behavior. A task is denoted as incomplete when the robot deviates from the reference path and does not get back to it by the end of the scenario while avoiding obstacles. The controller with $\epsilon = 0.2$, together with our method achieves the best performance with respect to task completeness. Similar behavior has been obtained in the environment with 10 pedestrians, as depicted in Table II.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B1 Pedestrians with Gaussian noise", "weight": 1.0} -->

In this environment the controller with $\epsilon = 0.2$ achieves the best performance with respect to the efficiency metrics, however it results in a higher maximum collision probability $11.1\%$, and 3 physical crashes with one of the pedestrians. Again our approach manages to balance between safety and efficiency by obtaining shorter trajectories while providing a closer bound to the acceptable risk level, $0.0454/0.05$, and without leading to physical collisions, or many temporary freezing behavior.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B1 Pedestrians with Gaussian noise", "weight": 1.0} -->

Avg. Min Dist. [m] Table III: Statistical results over 100 experiments for a multi-modal simulation with 6 pedestrians. The comparison is done with respect to the maximum risk endured by the robot, duration, robot velocity, number of times the robot has to come to standstill, and minimum distance to the obstacles. The results are reported as “average (standard deviation)”. The percentage of controller usage with ϵ = 0.2, ϵ = 0.1 and ϵ = 0.05 is 83.67%, 5.22% and 1.11%, respectively.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B1 Pedestrians with Gaussian noise", "weight": 1.0} -->

Avg. Min Dist. [m] Table IV: Results similar to those in III for multi-modal simulation with 10 pedestrians. The percentage of controller usage with ϵ = 0.2, ϵ = 0.1 and ϵ = 0.05 is 81.02%, 15.22% and 3.76%, respectively.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B1 Pedestrians with Gaussian noise", "weight": 1.0} -->

(d) A snapshot from experiment Figure 3: Experimental results with the robot avoiding two crossing pedestrians at different time instants. The blue circles depict the robot’s plan, whereas the lime and green circles visualize the pedestrians’ predictions where newer positions are depicted with lighter shades. The solid black line represents the reference path, and the black circles illustrate current positions. The robot takes 7.8 s to complete the task with 0.0416/0.05 max CP, 1.56 m/s average speed, and 25.784 ms computation time. The percentage of controller usage with ϵ = 0.2, ϵ = 0.1 and ϵ = 0.05 is, 94.13%, 5.87% and 0%, respectively.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-B2 Pedestrians with Gaussian Mixture Model", "weight": 1.0} -->

In this section, we model the pedestrian movement by a Markov Chain that changes the pedestrian movement from horizontal to diagonal, with $p = 0.975$ of staying in horizontal state and $p = 0.025$ of switching to diagonal state, in addition to the Gaussian noise of the previous simulation. The pedestrian dynamics are given by where $B$ is either $B_{h} = \begin{bmatrix} \end{bmatrix}^{T}$ or $B_{d} = \begin{bmatrix} \end{bmatrix}^{T}$ based on the state of the Markov Chain. The uncertainties associated with this motion can be modeled as a Gaussian Mixture Model where each state transition in the Markov Chain leads to a separate mode with an associated probability (21 modes in total). Similar to the first scenario, the results are validated in environments with 6 and 10 pedestrians respectively. The results for 6 pedestrians are summarized in Table III. The results are in line with the 6-pedestrian Gaussian case.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-B2 Pedestrians with Gaussian Mixture Model", "weight": 1.0} -->

Here it can be noted that our approach outperforms the baselines on almost all risk metrics, while attaining, compared to the baseline with $\epsilon = 0.05$, a higher but still safe CP of 0.0486. By balancing the minimum distances to the pedestrians, the temporal freezing behavior is reduced compared to the other controllers which results in faster trajectories. Moreover, the robot manages to get back to the reference path in almost all simulations. For the case of 10 pedestrians, results are summarized in Table IV, where collisions occur for all methods in this environment. A significant improvement in the number of physical collisions, from 8$\%$ to 2$\%$, can be observed with respect to the baseline with $\epsilon = 0.2$ while attaining a comparable efficiency. 12.1$\%$ and 10.2$\%$ improvements are obtained in the trajectory duration, and speed respectively, compared to the baseline with $\epsilon = 0.05$. In all simulations, the average computation time of the full control loop of our approach is 74.68 ms with a maximum computation time of 91.16 ms which makes it real-time capable.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-C Real-World Results", "weight": 1.0} -->

We evaluated our method on a real robot navigating on a road, following the lane central line, while two pedestrians cross the road. A snapshot from our experiment^11^1A video of the experiments and simulations accompanies this paper. is shown in Fig. 3, where quantitative results are illustrated in its caption.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we showed that our proposed hybrid approach provides probabilistic safety guarantees while achieving a closer bound to the specified risk for a mobile robot operating among humans with uni-modal and multi-modal Gaussian uncertainties. This is attained by running multiple probabilistic planners in parallel with different specified risk levels and quantifying the risk associated with each planned trajectory. The risk metric is estimated by integrating over the domain at which the robot trajectory and predicted pedestrian states spatially overlap at each stage along the prediction horizon. Accordingly, the plan with the least conservative behavior is chosen provided that its associated risk is below the risk level of the most conservative planner. Our simulations and experiments showed that the robot could follow the trajectories planned by the least conservative controller, most of the time, and only switches to more conservative controllers when the estimated risk violates the specified threshold. In such a way, the robot can plan faster trajectories while attaining the same safety level as the most conservative controller. Future works shall explore elaborated risk metrics in case the robot has a biased prediction for obstacle motion uncertainty and a criterion to set the risk upper bound for the probabilistic planner.
