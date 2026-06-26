<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Interpretable Goal-Based Prediction and Planning for Autonomous Driving

Topics include Autonomous driving, Motion prediction, Motion planning, Monte Carlo tree search, Interaction-aware planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Builds an interpretable autonomous-driving stack that uses rational inverse planning to infer other vehicles goals and feeds those beliefs into Monte Carlo tree search for ego planning. The paper emphasizes explainable macro-action reasoning rather than opaque end-to-end trajectory prediction.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose an integrated prediction and planning system for autonomous driving which uses rational inverse planning to recognise the goals of other vehicles. Goal recognition informs a Monte Carlo Tree Search (MCTS) algorithm to plan optimal maneuvers for the ego vehicle. Inverse planning and MCTS utilise a shared set of defined maneuvers and macro actions to construct plans which are explainable by means of rationality principles. Evaluation in simulations of urban driving scenarios demonstrate the system's ability to robustly recognise the goals of other vehicles, enabling our vehicle to exploit non-trivial opportunities to significantly reduce driving times. In each scenario, we extract intuitive explanations for the predictions which justify the system's decisions.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The ability to predict the intentions and driving trajectories of other vehicles is a key problem for autonomous driving. This problem is significantly complicated by the need to make fast and accurate predictions based on limited observation data which originate from coupled multi-agent interactions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To make prediction tractable in such conditions, a standard approach in autonomous driving research is to assume that vehicles use one of a finite number of distinct high-level maneuvers, such as lane-follow, lane-change, turn, stop, etc.. A classifier of some type is used to detect a vehicle's current executed maneuver based on its observed driving trajectory. The limitation in such methods is that they only detect the *current* maneuver of other vehicles, hence planners using such predictions are effectively limited to the timescales of the detected maneuvers. An alternative approach is to specify a finite set of possible *goals* for each other vehicle (such as road exit points) and to plan a full trajectory to each goal from the vehicle's observed local state. While this approach can generate longer-term predictions, a limitation is that the generated trajectories must be matched relatively closely by a vehicle in order to yield high-confidence predictions of the vehicle's goals.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent methods based on deep learning have shown promising results for trajectory prediction in autonomous driving. Prediction models are trained on large datasets that are becoming available through data gathering campaigns involving sensorised vehicles (e.g. video, lidar, radar). Reliable prediction over several second horizons remains a hard problem, in part due to the difficulties in capturing the coupled evolution of traffic. In our view, one of the most significant limitations of this class of methods (though see recent progress ) is the difficulty in extracting interpretable predictions in a form that is amenable to efficient integration with planning methods that effectively represent multi-dimensional and hierarchical task objectives.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our starting point is that in order to predict the future maneuvers of a vehicle, we must reason about *why* -- that is, to what end -- the vehicle performed its past maneuvers, which will yield clues as to its intended goal. Knowing the goals of other vehicles enables prediction of their future maneuvers and trajectories, which facilitates planning over extended timescales. We show in our work (illustrated in Figure 2) how such reasoning can help to address the problem of overly-conservative autonomous driving. Further, to the extent that our predictions are structured around the interpretation of observed trajectories in terms of high-level maneuvers, the goal recognition process lends itself to *intuitive interpretation* for the purposes of system analysis and debugging, at a level of detail suggested in Figure 2. As we develop towards making our autonomous systems more trustworthy, these notions of interpretation and the ability to justify (explain) the system's decisions are key.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To this end, we propose *Interpretable Goal-based Prediction and Planning* (IGP2) which leverages the computational advantages of using a finite space of maneuvers, but extends the approach to planning and prediction of *sequences* (i.e., plans) of maneuvers. We achieve this via a novel integration of rational inverse planning to recognise the goals of other vehicles, with Monte Carlo Tree Search (MCTS) to plan optimal maneuvers for the ego vehicle. Inverse planning and MCTS utilise a shared set of defined maneuvers to construct plans which are explainable by means of *rationality* principles, i.e. plans are optimal with respect to given metrics. We evaluate IGP2 in simulations of diverse urban driving scenarios, showing that the system robustly recognises the goals of other vehicles, even if significant parts of a vehicle's trajectory are occluded, goal recognition enables our vehicle to exploit opportunities to improve driving efficiency as measured by driving time compared to other prediction baselines, and we are able to extract intuitive explanations for the predictions to justify the system's decisions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, our contributions are: A method for goal recognition and multi-modal trajectory prediction via rational inverse planning.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Integration of goal recognition with MCTS planning to generate optimised plans for the ego vehicle.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Evaluation in simulated urban driving scenarios showing accurate goal recognition, improved driving efficiency, and ability to interpret the predictions and ego plans.

<!-- chunk {"id": "body-0012", "role": "body", "section": "IGP2: Interpretable Goal-based Prediction and Planning", "weight": 1.0} -->

Our general approach relies on two assumptions: each vehicle seeks to reach some (unknown) goal from a set of possible goals, and each vehicle follows a plan generated from a finite library of defined maneuvers.

<!-- chunk {"id": "body-0013", "role": "body", "section": "IGP2: Interpretable Goal-based Prediction and Planning", "weight": 1.0} -->

Additional applicability condition: Maneuver sequence (maneuver parameters in brackets): lane-follow (end of visible lane) Continue next exit Must be in roundabout and not in outer-lane lane-follow (next exit point) Change left/right There is a lane to the left/right lane-follow (until target lane clear), lane-change-left/right Exit left/right Exit point on same lane ahead of car and in correct direction lane-follow (exit point), give-way (relevant lanes), turn-left/right There is a stopping goal ahead of the car on the current lane lane-follow (close to stopping point), stop TABLE I: Macro actions used in our system. Each macro action concatenates one or more maneuvers and automatically sets their parameters.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Maneuvers", "weight": 1.0} -->

We assume that at any time, each vehicle is executing one of the following maneuvers: lane-follow, lane-change-left/right, turn-left/right, give-way, stop. Each maneuver $\omega$ specifies applicability and termination conditions. For example, lane-change-left is only applicable if there is a lane in same driving direction to the left of the vehicle, and terminates once the vehicle has reached the new lane and its orientation is aligned with the lane. Some maneuvers have free parameters, e.g. follow-lane has a parameter to specify when to terminate.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Maneuvers", "weight": 1.0} -->

If applicable, a maneuver specifies a local trajectory ${\hat{s}}_{1:n}^{i}$ to be followed by the vehicle, which includes a reference path in the global coordinate frame and target velocities along the path. For convenience in exposition, we assume that ${\hat{s}}^{i}$ uses the same representation and indexing as $s^{i}$, but in general this does not have to be the case (for example, $\hat{s}$ may be indexed by longitudinal position rather than time, which can be interpolated to time indices). In our system, the reference path is generated via a Bezier spline function fitted to a set of points extracted from the road topology, and target velocities are set using domain heuristics similar to.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-B Macro Actions", "weight": 1.0} -->

Macro actions specify common sequences of maneuvers and automatically set the free parameters (if any) in maneuvers based on context information such as road layout. Table I specifies the macro actions used in our system. The applicability condition of a macro action is given by the applicability condition of the first maneuver in the macro action as well as optional additional conditions. The termination condition of a macro action is given by the termination condition of the last maneuver in the macro action.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-C Velocity Smoothing", "weight": 1.0} -->

To obtain a feasible trajectory across maneuvers for vehicle $i$, we define a velocity smoothing operation which optimises the target velocities in a given trajectory ${\hat{s}}_{1:n}^{i}$. Let ${\hat{x}}_{t}$ be the longitudinal position on the reference path at ${\hat{s}}_{t}^{i}$ and ${\hat{v}}_{t}$ its target velocity, for $1 \leq t \leq n$. We define $\kappa:{x\rightarrow v}$ as the piecewise linear interpolation of target velocities between points ${\hat{x}}_{t}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-C Velocity Smoothing", "weight": 1.0} -->

Given the time elapsed between two time steps, $\Deltat$; the maximum velocity and acceleration, $v_{max}$/$a_{max}$; and setting ${x_{1} = {\hat{x}}_{1}},{v_{1} = {\hat{v}}_{1}}$, we define velocity smoothing as | | | ${0 < v_{t} < v_{\max}},{v_{t} \leq {\kappa{(x_{t})}}}$ | | | where $\lambda > 0$ is the weight given to the acceleration part of the optimisation objective. Eq. is a nonlinear non-convex optimisation problem which can be solved, e.g., using a primal-dual interior point method (we use IPOPT).

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-C Velocity Smoothing", "weight": 1.0} -->

From the solution of the problem, $(x_{2:n},v_{2:n})$, we interpolate to obtain the achievable velocities at the original points ${\hat{x}}_{t}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-D Goal Recognition", "weight": 1.0} -->

We assume that each non-ego vehicle $i$ seeks to reach one of a finite number of possible goals $G^{i} \in \mathcal{G}^{i}$, using plans constructed from our defined macro actions. We use the framework of rational inverse planning to compute a Bayesian posterior distribution over $i$'s goals at time $t$ where $L{(\left. s_{1:t} \middle| G^{i} \right.)}$ is the likelihood of $i$'s observed trajectory assuming its goal is $G^{i}$, and $p{(G^{i})}$ specifies the prior probability of $G^{i}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-D Goal Recognition", "weight": 1.0} -->

The likelihood is a function of the reward difference between two plans: the reward $\hat{r}$ of the optimal trajectory from $i$'s initial observed state $s_{1}^{i}$ to goal $G^{i}$ after velocity smoothing, and the reward $\overline{r}$ of the trajectory which follows the observed trajectory until time $t$ and then continues optimally to goal $G^{i}$, with smoothing applied only to the trajectory after $t$. The likelihood is defined as where $\beta$ is a scaling parameter (we use $\beta = 1$). This likelihood definition assumes that vehicles drive approximately *rationally* (i.e., optimally) to achieve their goals while allowing for some deviation. If a goal is infeasible, we set its probability to zero.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-D Goal Recognition", "weight": 1.0} -->

Algorithm 1 shows the pseudo code for our goal recognition algorithm, with further details in below subsections.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-D1 Goal Generation", "weight": 1.0} -->

A heuristic function is used to generate a set of possible goals $\mathcal{G}^{i}$ for vehicle $i$ based on its location and context information such as road layout. In our system, we include goals for the visible end of the current road and connecting roads (bounded by the ego vehicle's view region). In addition to such static goals, it is also possible to add dynamic goals which depend on current traffic. For example, in the dense merging scenario shown in Figure 2(d), stopping goals are dynamically added to model a vehicle's intention to allow the ego vehicle to merge in front.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-D2 Maneuver Detection", "weight": 1.0} -->

Maneuver detection is used to detect the current executed maneuver of a vehicle (at time $t$), allowing inverse planning to complete the maneuver before planning onward. We assume a module which computes probabilities over current maneuvers, $p{(\omega^{i})}$, for each vehicle $i$. One option is Bayesian changepoint detection (e.g. ). The details of maneuver detection are outside the scope of our paper and in our experiments we use a simulated detector (cf. Sec IV-B). As different current maneuvers may hint at different goals, we perform inverse planning for each possible current maneuver for which ${p{(\omega^{i})}} > 0$. Thus, each current maneuver produces its associated posterior probabilities over goals, denoted by $p{(\left. G^{i} \middle| {s_{1:t},\omega^{i}} \right.)}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-D3 Inverse Planning", "weight": 1.0} -->

Inverse planning is done using A\* search over macro actions. A\* starts after completing the current maneuver $\omega^{i}$ which produces the initial trajectory ${\hat{s}}_{1:\tau}$. Each search node $q$ corresponds to a state $s \in \mathcal{S}$, with initial node at state ${\hat{s}}_{\tau}$, and macro actions are filtered by their applicability conditions applied to $s$. A\* chooses the next macro action leading to a node $q'$ which has lowest estimated total cost^11^1Here we use the term "cost" in keeping with standard A\* terminology and to differentiate from the reward function defined in Sec. II. to goal $G^{i}$, given by ${f{(q')}} = {{l{(q')}} + {h{(q')}}}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-D3 Inverse Planning", "weight": 1.0} -->

The cost $l{(q')}$ to reach node $q'$ is given by the driving time from $i$'s location in the initial search node to its location in $q'$, following the trajectories returned by the macro actions leading to $q'$. A\* uses the assumption that all other vehicles not planned for use a constant-velocity lane-following model after their observed trajectories. We do not check for collisions during inverse planning. The cost heuristic $h{(q')}$ to estimate remaining cost from $q'$ to goal $G^{i}$ is given by the driving time from $i$'s location in $q'$ to goal via straight line at speed limit. This definition of $h{(q')}$ is admissible as per A\* theory, which ensures that the search returns an optimal plan. After the optimal plan is found, we extract the complete trajectory ${\hat{s}}_{1:n}^{i}$ from the maneuvers in the plan and initial segment ${\hat{s}}_{1:\tau}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-D4 Trajectory Prediction", "weight": 1.0} -->

Our system predicts multiple plausible trajectories for a given vehicle and goal. This is required because there are situations in which different trajectories may be (near-)optimal but may lead to different predictions which could require different behaviour on the part of the ego vehicle. We run A\* search for a fixed amount of time and let it compute a set of plans with associated rewards (up to some fixed number of plans). Any time A\* search finds a node that reaches the goal, the corresponding plan is added to the set of plans. Given a set of smoothed trajectories $\left.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-D4 Trajectory Prediction", "weight": 1.0} -->

\{{\hat{s}}_{1:n}^{i,k} \middle| {\omega^{i},G^{i}}\} \right._{k = 1..K}$ to goal $G^{i}$ with initial maneuver $\omega^{i}$ and associated reward $r_{k} = {R^{i}{({\hat{s}}_{1:n}^{i,k})}}$, we compute a distribution over the trajectories via a Boltzmann distribution where $\gamma$ is a scaling parameter (we use $\gamma = 1$). Similar to Eq., Eq. encodes the assumption that trajectories which are closer to optimal are more likely.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-D4 Trajectory Prediction", "weight": 1.0} -->

Input: vehicle i, current maneuver ωi, observations s1: t Returns: goal probabilities p (Gi|s1: t, ωi) 1: Generate possible goals Gi ∈ 𝒢i from state sti 2: Set prior probabilities p (Gi) (e.g. uniform) 5: Apply velocity smoothing to ŝ1: ni 7: ${\overline{s}}_{1:m}^{i}\leftarrow$ A*(ωi) from ${\overline{s}}_{t}^{i}$ to Gi, with ${\overline{s}}_{1:t}^{i} = s_{1:t}^{i}$ 8: Apply velocity smoothing to ${\overline{s}}_{{t + 1}:m}^{i}$ 9: $\overline{r}\leftarrow$ reward $R^{i}{({\overline{s}}_{1:m}^{i})}$ 10: ${L{(\left.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-D4 Trajectory Prediction", "weight": 1.0} -->

s_{1:t} \middle| {G^{i},\omega^{i}} \right.)}}\leftarrow{\exp{({\beta{({\overline{r} - \hat{r}})}})}}$ Algorithm 1 Goal recognition algorithm Returns: optimal maneuver for ego vehicle ε in state st 1: Search node q.s ← st (r o o t node) 4: Sample current maneuver ωi ∼ p (ωi) 6: Sample trajectory ŝ1: ni ∈ {ŝ1: ni, k|ωi, Gi} with p (ŝ1: ni, k) 8: Select macro action μ for ε applicable in q.s 9: ŝτ: ι← Simulate μ until it terminates, with non-ego vehicles following their sampled trajectories ŝ1: ni 11: if ego vehicle collides during ŝτ: ι then 13: else if ŝιε achieves ego goal Gε then 18: Use to backprop r along search branches (q, μ, q′) that generated the simulation 19: Start next simulation Return maneuver for ε in st, μ ∈ arg

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-D4 Trajectory Prediction", "weight": 1.0} -->

maxμQ (r o o t, μ) Algorithm 2 Monte Carlo Tree Search algorithm Figure 2: IGP2 in 4 test scenarios.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-D4 Trajectory Prediction", "weight": 1.0} -->

Ego vehicle shown in blue. Bar plots show goal probabilities for non-ego vehicles. For each goal, up to two of the most probable predicted trajectories to goal are shown with thickness proportional to probability. (a) S1: Ego’s goal is blue goal. Vehicle V1 is on the ego’s road, V1 changes from left to right lane, biasing the ego prediction towards the belief that V1 will exit, since a lane change would be irrational if V1’s goal was to go east. As exiting will require a significant slowdown, the ego decides to switch lanes to avoid being slowed down too. (b) S2: Ego’s goal is blue goal. Vehicle V1 is approaching the junction from the east and vehicle V2 from the west. As V1 approaches the junction, slows down and waits to take a turn, the ego’s belief that V1 will turn right increases significantly, since it would be irrational to stop if the goal was to turn left or go straight. Since the ego recognised V1’s goal is to go north, it predicts that V1 will wait until V2 has passed, giving the ego an opportunity to enter the road.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-D4 Trajectory Prediction", "weight": 1.0} -->

(c) S3: Ego’s goal is green goal. As V1 changes from the inside to the outside lane of the roundabout and decreases its speed, it significantly biases the ego prediction towards the belief that V1 will take the south exit since that is the rational course of action for that goal. This encourages the ego to enter the roundabout while V1 is still in roundabout. (d) S4: Ego’s goal is purple goal. With two vehicles stopped at the junction at a traffic light, vehicle V1 is approaching them from behind, and vehicle V2 is crossing in the opposite direction. When V1 reaches zero velocity, the goal generation function adds a stopping goal (orange) for V1 in its current position, shifting the goal distribution towards it since stopping is not rational for the north/west goals. The interpretation is that V1 wants the ego to merge in front of V1, which the ego then does.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-E Ego Vehicle Planning", "weight": 1.0} -->

To compute an optimal plan for the ego vehicle, we use the goal probabilities and predicted trajectories to inform a Monte Carlo Tree Search (MCTS) algorithm (see Algorithm 2).

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-E Ego Vehicle Planning", "weight": 1.0} -->

The algorithm performs a number of closed-loop simulations ${\hat{s}}_{t:n}$, starting in the current state ${\hat{s}}_{t} = s_{t}$ down to some fixed search depth or until a goal state is reached. At the start of each simulation, for each non-ego vehicle, we first sample a current maneuver, then goal, and then trajectory for the vehicle using the associated probabilities (cf. Section III-D). Each node $q$ in the search tree corresponds to a state $s \in \mathcal{S}$ and macro actions are filtered by their applicability conditions applied to $s$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-E Ego Vehicle Planning", "weight": 1.0} -->

After selecting a macro action $\mu$ using some exploration technique (we use UCB1 ), the state in the current search node is forward-simulated based on the trajectory generated by the macro action $\mu$ and the sampled trajectories of non-ego vehicles, resulting in a partial trajectory ${\hat{s}}_{\tau:\iota}$ and new search node $q'$ with state ${\hat{s}}_{\iota}$. Forward-simulation of trajectories uses a combination of proportional control and adaptive cruise control (based on IDM ) to control a vehicle's acceleration and steering. Termination conditions of maneuvers are monitored in each time step based on the vehicle's observations. Collision checking is performed on ${\hat{s}}_{\tau:\iota}$ to check whether the ego vehicle collided, in which case we set the reward to $r\leftarrow r_{coll}$ which is back-propagated using, where $r_{coll}$ is a method parameter.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-E Ego Vehicle Planning", "weight": 1.0} -->

Otherwise, if the new state ${\hat{s}}_{\iota}$ achieves the ego goal $G^{\varepsilon}$, we compute the reward for back-propagation as $r\leftarrow{R^{\varepsilon}{({\hat{s}}_{t:n})}}$. If the search reached its maximum depth $d_{max}$ without colliding or achieving the goal, we set $r\leftarrow r_{term}$ which can be a constant or based on heuristic reward estimates similar to A\* search.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-E Ego Vehicle Planning", "weight": 1.0} -->

The reward $r$ is back-propagated through search branches $(q,\mu,q')$ that generated the simulation, using a 1-step off-policy update function (similar to Q-learning) where $\delta$ is the number of times that macro action $\mu$ has been selected in $q$. After the simulations are completed, the algorithm selects the best macro action for execution in $s_{t}$ from the root node, ${\arg{\max_{\mu}Q}}{({root},\mu)}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Evaluation", "weight": 1.0} -->

We evaluate IGP2 in simulations of diverse urban driving scenarios, showing that: our inverse planning method robustly recognises the goals of non-ego vehicles; goal recognition leads to improved driving efficiency measured by driving time; and intuitive explanations for the predictions can be extracted to justify the system's decisions.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-A Scenarios", "weight": 1.0} -->

We use two sets of scenario instances. For in-depth analysis of goal recognition and planning, we use four defined local interaction scenarios shown in Figure 2. For each of these scenarios, we generate 100 instances with randomly offset initial longitudinal positions ($\sim {\lbrack{- 10},{+ 10}\rbrack}$ meters) and initial speed sampled from range $\lbrack 5,10\rbrack$ m/s for each vehicle including ego vehicle. Here the ego vehicle observes the whole scenario. To further assess IGP2's ability to complete full routes with random traffic, we use two random town layouts shown in Figure 3. Each town spans an area of 0.16 square kilometers and consists of roads, crossings, and roundabouts with 2--4 lanes each. Each junction has one defined priority road. The ego vehicle's observation radius in towns is 50 meters. Non-ego vehicles are spawned within 25 meters outside the ego observation radius, with random road, lane, speed, and goal. The total number of non-ego vehicles within the ego radius and spawning radius is kept at 8 to maintain a consistent medium-to-high level of traffic.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-A Scenarios", "weight": 1.0} -->

In each town we generate 10 instances by choosing random routes for the ego vehicle to complete. The ego vehicle's goal is continually updated to be the outermost point on the route within the ego observation radius. In all simulations, the non-ego vehicles use manual heuristics to select from the maneuvers in Section III-A to reach their goals. All vehicles use independent proportional controllers for acceleration and steering, and IDM for automatic distance-keeping. Vehicle motion is simulated using a kinematic bicycle model.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-B Algorithms & Parameters", "weight": 1.0} -->

We compare the following algorithms in scenarios S1--S4. IGP2: full system using goal recognition and MCTS. IGP2-MAP: like IGP2, but MCTS uses only the most probable goal and trajectory for each vehicle. CVel: MCTS without goal recognition, replaced by constant-velocity lane-following prediction after completion of current maneuver. CVel-Avg: like CVel, but uses velocity averaged over the past 2 seconds. Cons: like CVel, but using a conservative give-way maneuver which always waits until all oncoming vehicles on priority lanes have passed. In the town scenarios we focus on IGP2 and Cons, and additionally compare to SH-CVel which works similarly to MPDM: it simulates each macro action followed by a default Continue macro action, using CVel prediction for non-ego vehicles, then choosing the macro action with maximum estimated reward. (SH stands for "short horizon" as the search depth is effectively limited to 1.)

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-B Algorithms & Parameters", "weight": 1.0} -->

We simulate noisy maneuver detection (cf. Sec. III-D2) by giving $0.9$ probability to the current executed maneuver of the non-ego vehicle and the rest uniformly to other maneuvers. Prior probabilities over non-ego goals are uniform. A\* computes up to two predicted trajectories for each non-ego vehicle and goal. MCTS is run at a frequency of 1 Hz, performs $K = 30$ simulations with a maximum search depth of $d_{max} = 5$, and uses $r_{coll} = r_{term} = {- 1}$. We set $\lambda = 10$ for velocity smoothing (cf. Eq. ).

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-C2 Driving times", "weight": 1.0} -->

Table II shows the average driving times required of each algorithm in scenarios S1--S4. Goal recognition enabled IGP2 and IGP2-MAP to reduce their driving times. (S1) All algorithms change lanes to avoid being slowed down by V1, leading to same driving times, however IGP2 and IGP2-MAP initiate the lane change before all other algorithms by recognising V1's intended goal. (S2) Cons waits for $V_{1}$ to clear the lane, which in turn must wait for $V_{2}$ to pass. IGP2 and IGP2-MAP anticipate this behaviour, allowing them to enter the road earlier. CVel and CVel-Avg wait for $V_{1}$ to reach near-zero velocity. (S3) IGP2 and IGP2-MAP are able to enter early as they recognise $V_{1}$'s goal to exit the roundabout, while CVel, CVel-Avg, and Cons wait for $V_{1}$ to exit.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-C2 Driving times", "weight": 1.0} -->

(S4) Cons waits until $V_{1}$ decides to close the gap after which the ego can enter the road. IGP2 and IGP2-MAP recognise $V_{1}$'s goal and merge in front.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-C2 Driving times", "weight": 1.0} -->

IGP2-MAP achieved shorter driving times than IGP2 on some scenario instances (such as S3 and S4). This is because IGP2-MAP commits to the most-likely goal and trajectory of other vehicles, while IGP2 also considers residual uncertainty about goals and trajectories which may lead MCTS to select more cautious actions in some situations. The limitation of IGP2-MAP can be seen when simulating unexpected (irrational) behaviours in other vehicles. To test this, we compared IGP2 and IGP2-MAP on instances from S3 and S4 which were modified such that V1, after slowing down, suddenly accelerates and continues straight (rather than exiting as in S3, or stopping as in S4). In these cases we observed a 2-3% collision rate for IGP2-MAP (in all collisions, V1 collided into the ego) while IGP2 produced no collisions. These results show that IGP2 exhibits safer driving than IGP2-MAP by accounting for uncertainty over goals and trajectories.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-C3 Interpretability", "weight": 1.0} -->

We are able to extract intuitive explanations for the predictions and decisions made by IGP2. The explanations are given in the caption of Figure 2.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We proposed an autonomous driving system, IGP2, which integrates planning and prediction over extended horizons by reasoning about the goals of other vehicles via rational inverse planning. Evaluation in diverse urban driving scenarios showed that IGP2 robustly recognises the goals of non-ego vehicles, resulting in improved driving efficiency while allowing for intuitive interpretations of the predictions to explain the system's decisions. IGP2 is general in that it uses relatively standard planning techniques that could be replaced with other techniques (e.g. POMDP-based planners ), and the general principles underlying our approach could be applied to other domains in which mobile robots interact with other robots/humans. Important future directions include goal recognition in the presence of occluded objects which can be seen by the non-ego vehicle but not the ego vehicle, and accounting for human irrational biases.
