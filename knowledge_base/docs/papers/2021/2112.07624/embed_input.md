<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Interaction-Aware Trajectory Prediction and Planning for Autonomous Vehicles in Forced Merge Scenarios

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Merging is, in general, a challenging task for both human drivers and autonomous vehicles, especially in dense traffic, because the merging vehicle typically needs to interact with other vehicles to identify or create a gap and safely merge into. In this paper, we consider the problem of autonomous vehicle control for forced merge scenarios. We propose a novel game-theoretic controller, called the Leader-Follower Game Controller (LFGC), in which the interactions between the autonomous ego vehicle and other vehicles with a priori uncertain driving intentions is modeled as a partially observable leader-follower game. The LFGC estimates the other vehicles' intentions online based on observed trajectories, and then predicts their future trajectories and plans the ego vehicle's own trajectory using Model Predictive Control (MPC) to simultaneously achieve probabilistically guaranteed safety and merging objectives. To verify the performance of LFGC, we test it in simulations and with the NGSIM data, where the LFGC demonstrates a high success rate of 97.5% in merging.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Advances in autonomous vehicle technologies are projected to reduce vehicle crashes and fatalities, improve mobility especially for elderly and disabled people, improve fuel economy and emission control, and to promote more efficient land uses. Despite these benefits, there are still many challenges that need to be addressed to deliver a highly (level 4 or level 5) autonomous vehicle. One challenging scenario for both human drivers and autonomous vehicles is highway forced merge, where the merging vehicle needs to choose a proper gap in the highway traffic and potentially force the upstream traffic to slow down so that it can safely merge into that gap. Forced merge typically occurs in mandatory merge scenarios where the current lane is ending, such as at highway on-ramps. When the traffic is dense, interactions and/or cooperation between the merging vehicle and vehicles driving in the target lane are often needed. In particular, a vehicle in the target lane may choose to ignore the merging vehicle (i.e., proceed) and consequently the merging vehicle can only merge behind. Alternatively, the vehicle in the target lane may choose to yield to the merging vehicle (i.e., let the merging vehicle merge in front of it).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In order to successfully merge into a busy traffic, an autonomous vehicle controller needs to appropriately respond to the intentions to proceed or yield of other vehicles. An overly conservative controller may yield to all other vehicles (including those that intend to yield to the autonomous ego vehicle) and eventually fail to merge, while an overly aggressive controller may have conflicts with the vehicles that intend to proceed and lead to vehicle crashes. Meanwhile, the decision whether to proceed or to yield to another vehicle depends not only on the traffic situation (e.g., the relative position and velocity between the two vehicles) but also on its driver's general driving style, personality, mood, etc. For instance, in a similar situation, an aggressive driver may be inclined to proceed while a cautious/conservative driver may tend to yield. This poses a significant challenge to autonomous vehicle planning and control.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

There exists an extensive literature on modeling human driver interactions and autonomous vehicle decision-making during lane change or merging. To handle interaction uncertainties (e.g., due to varied cooperation intentions of other vehicles), the Partially Observable Markov Decision Process (POMDP) framework has been exploited, where the uncertainties are modeled as latent variables and estimated online based on observed trajectories. However, solving a POMDP problem with a large state and/or action space is computationally very demanding. Consequently, conventional POMDP-based approaches typically only consider the interaction of the ego vehicle with one interacting vehicle at a time to minimize the state space dimension. However, in reality a merging scenario can involve simultaneous interactions with multiple vehicles.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement Learning (RL) is another popular approach to developing control policies for lane change or merge scenarios. An RL-based policy can account for the vehicle interactions in certain scenarios through training in an environment capable of representing such interactions. In order to obtain through RL driving policies that behave like human drivers, several researchers chose to use inverse RL to estimate human's reward function for driving. To be able to model different human driver styles and/or interaction intentions, incorporates cooperativeness into the intelligent driver model and formulates different reward functions for different drivers and performs RL based on the models. Although RL-based approaches are appealing in terms of their potentials to handle complex traffic scenarios with multi-vehicle interactions, potential drawbacks of these approaches that hinder their practical application include their lacks of interpretability and explicit safety guarantee, because safety is typically only promoted through certain terms in the reward function rather than enforced through hard constraints.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To achieve more interpretable control, other researchers proposed to explicitly incorporate a prediction model for vehicle interactions in the control algorithm. For instance, uses a "Social Generative Adversarial Network (Social GAN)" to generate predictions of other vehicles' future trajectories in response to ego vehicle's actions. However, the Social GAN does not account for variations of drivers' styles and intentions and needs to be trained with sufficient traffic data. For the latter, it has been reported that multi-vehicle interaction scenarios in released traffic datasets are insufficient. Game-theoretic methods have also been investigated for modeling vehicle interactions in lane change or merge scenarios. It is possible to account for varied driving styles and/or intentions with these game-theoretic methods, for instance, through modeling and online estimation of drivers' cognitive levels or aggressiveness.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose a novel high-level control algorithm, called the Leader-Follower Game Controller (LFGC), for autonomous vehicle planning and control in forced merge scenarios. In the LFGC, drivers' interaction intentions (to proceed or yield) and their resulting vehicle behaviors are represented by an explicit game-theoretic model with multiple concurrent leader-follower pairs, called a leader-follower game. To account for interaction uncertainties, the pairwise leader-follower relationships among the vehicles are assumed to be a priori uncertain and modeled as latent variables. The LFGC estimates the leader-follower relationships online based on observed trajectories and makes optimal decisions for the autonomous ego vehicle using a Model Predictive Control (MPC)-based strategy. The proposed approach thus adapts to the inferred leader-follower relationship estimates to simultaneously achieve probabilistically guaranteed safety and the merging objectives. Note that a similar idea has been investigated in our previous conference paper.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The LFGC presented in this paper differs from the one in in several aspects: 1) Instead of relying on discretization of the state space and the POMDP framework, the LFGC in this paper is designed assuming a continuous state space, which results in smoother trajectories for lower-level controllers to track and which alleviates the computational difficulty associated with discrete spaces. 2) Unlike our previous work in which we use a small number of actions (or motion primitives) to represent vehicle behavior, the LFGC of this paper predicts and plans vehicle motion using two much larger sets of trajectories ($162$ trajectories for the merging ego vehicle and $81$ trajectories for each of the highway interacting vehicles), which leads to finer-resolution controls and the potential for higher performance. 3) The LFGC of this paper is validated based on a comprehensive set of simulation-based test cases including cases where other vehicles are controlled by various types of driver models and cases where their motion follows real traffic data, which is not done.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The LFGC uses a game-theoretic model for vehicle trajectory prediction while accounting for interactions and cooperation and while leading to interpretable control solutions (because the control solutions are based on model predictive control with an interpretable game-theoretic prediction model).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The LFGC handles interaction uncertainties due to varied cooperation intentions of other vehicles by modeling these uncertainties as latent variables and estimating them online based on observed trajectories and Bayesian inference.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The LFGC represents vehicle safety requirements (e.g., collision avoidance) as constraints and pursues optimization subject to satisfying an explicit probabilistic safety characterization (i.e., a user-specified probability bound of safety) in the presence of interaction uncertainties.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

The LFGC is designed in a continuous state space setting, which avoids the computational difficulty resulting from space discretization of previous POMDP-based approaches. This also enables the LFGC to handle more complex scenarios that involve interactions with multiple vehicles.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

The LFGC is validated based on a comprehensive set of simulation-based case studies that include cases where other vehicles are controlled by various types of driver models and cases where their motion follows actual vehicle trajectories in the NGSIM US Highway 101 dataset. For the latter, the LFGC demonstrates a high success rate (in terms of safely completing merges) of $97.5\%$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper is organized as follows: In Section II, we introduce the models that represent vehicle/traffic dynamics, driver objectives, vehicle actions, and the MPC-based control strategy for the autonomous ego vehicle. In Section III, we introduce the leader-follower game model that is used to represent drivers' interaction intentions and their resulting vehicle behaviors in multi-vehicle traffic scenarios. In Section IV, we integrate the MPC-based control strategy with the leader-follower game model and with online estimation of pairwise leader-follower relationships among interacting vehicles based on Bayesian inference, to enable the ego vehicle's actions to adapt in real-time to interacting drivers'/vehicles' intentions. In Section V, we validate the proposed LFGC through multiple simulation-based case studies, including validations against vehicles following our leader-follower game model, the Intelligent Driver Model (IDM), and trajectories from NGSIM US Highway 101 data. Finally, conclusions are given in Section VI.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Models and Control Strategy Descriptions", "weight": 1.0} -->

In this section, we introduce models to represent the vehicle and traffic dynamics and the MPC-based strategy for ego vehicle's trajectory planning.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A Vehicle dynamics", "weight": 1.0} -->

We use the kinematic bicycle model to represent the motion of each vehicle. The kinematic bicycle model is defined by the following set of continuous-time equations,

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A Vehicle dynamics", "weight": 1.0} -->

where we have assumed only front-wheel steering $\delta_{f}$ and no rear-wheel steering (i.e., $\delta_{r} = 0$); $x$ and $y$ are the longitudinal and lateral positions of the vehicle; $v$ is the speed of the vehicle; $\psi$ and $\beta$ are the yaw angle and the slip angle of the vehicle; $l_{f}$ and $l_{r}$ represent the distances from the CG of the vehicle to the front wheel and rear wheel axles; $a$ is the acceleration along the direction of speed $v$. The control inputs are the acceleration and front-wheel steering, $u = {\lbrack a,\delta_{f}\rbrack}^{T}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-A Vehicle dynamics", "weight": 1.0} -->

While vehicle models other than could be used, the above kinematic bicycle model is suitable for our purpose of trajectory prediction and planning in forced merge scenarios -- it can produce sufficiently accurate predictions of vehicle trajectories under given acceleration and front-wheel steering profiles while it is simple and thus computationally efficient.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B Traffic dynamics", "weight": 1.0} -->

We consider a traffic scenario involving $n + 1$ vehicles, including the ego vehicle, denoted by $0$, and $n$ other interacting vehicles $k$, $k \in {\{ 1,\ldots,n\}}$, which correspond to vehicles that are aware of the ego vehicle's merging attempt. Therefore, the traffic state and its dynamics are characterized by the aggregation of all $n + 1$ vehicles' states and dynamics. Specifically, we describe the traffic dynamics using the following discrete-time model,

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-C Reward function", "weight": 1.0} -->

The reward function $R{({\overline{s}}_{t},{\overline{u}}_{t})}$ is a mathematical representation of the driving goals of the driver. Here, we start by considering the interactions between the ego vehicle and one other vehicle, i.e., ${\overline{s}}_{t} = {(s_{t}^{0},s_{t}^{1})}$ and ${\overline{u}}_{t} = {(u_{t}^{0},u_{t}^{1})}$. In this case, the traffic state is composed of the states of these two vehicles, and the reward received by the ego vehicle depends on the states and control inputs of both vehicles. Following, we consider

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-C Reward function", "weight": 1.0} -->

where $r = {\lbrack r_{1},r_{2},r_{3},r_{4},r_{5}\rbrack}^{T}$ and $w \in {\mathbb{R}}_{+}^{5}$ is a vector of weights. The reward terms $r_{1},\ldots,r_{5}$ are defined to represent the following common considerations during driving: 1) safety $(r_{1},r_{2})$, i.e., not colliding with other vehicles and not getting off the road; 2) liveness $(r_{3},r_{4})$, i.e., approaching the destination; and 3) comfort $(r_{5})$, i.e., maintaining a reasonable separation from other vehicles. The reader is referred to for more detailed definitions of $r_{1},\ldots,r_{5}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-D Selecting Trajectories as vehicle actions", "weight": 1.0} -->

Instead of considering a discrete set of acceleration $a$ and steering $\delta_{f}$ levels as, we consider a sampled set of vehicle motion trajectories over a planning horizon of $T = {N\DeltaT}$ \[s\] as the action space for each vehicle. Specifically, each trajectory is a time history of vehicle state $s_{t} = {\lbrack x_{t},y_{t},v_{t},\psi_{t}\rbrack}^{T}$ starting from the vehicle's current state $s_{0}$. Note that the time history of control inputs $u_{t} = {\lbrack a_{t},\delta_{f,t}\rbrack}^{T}$ corresponding to each trajectory can be calculated according to the vehicle dynamics model. Compared to representing vehicle motion using discrete acceleration and steering levels as, the method here can lead to smoother trajectories and finer-resolution controls.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-D Selecting Trajectories as vehicle actions", "weight": 1.0} -->

For interacting vehicles driving in the target lane, we only consider their longitudinal motion, which corresponds to the assumption that these vehicles do not change lanes. Assuming $\psi = 0$ and $\delta_{f} = 0$, the kinematic bicycle model for these vehicles reduces to

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-D Selecting Trajectories as vehicle actions", "weight": 1.0} -->

In this case, a trajectory starting with a given initial condition depends only on the profile of acceleration $a$ over $\lbrack 0,T\rbrack$. In particular, at each sample time instant, we consider $81$ acceleration profiles, which translates into $81$ trajectories through, for each interacting vehicle $k$ driving in the target lane, and we treat these trajectories as its admissible actions. Note that we also enforce the speed limits $v_{t}^{k} \in {\lbrack v_{\min},v_{\max}\rbrack}$ when we generate these trajectories.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-D Selecting Trajectories as vehicle actions", "weight": 1.0} -->

The merging vehicle's maneuvers include both lane keeping and lane change. Trajectories or pieces of trajectories that represent lane keeping are generated using in a similar way as above. For a lane change, we use $5$th-order polynomials to represent lane change trajectories. Specifically, a lane change trajectory is produced by the solution to the following boundary value problem: Find the coefficients $a_{1},\ldots,a_{5}$ and $b_{1},\ldots,b_{5}$ such that the $5$th-order polynomials

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-D Selecting Trajectories as vehicle actions", "weight": 1.0} -->

The variable $\zeta$ in denotes continuous time. We let $\zeta = 0$ correspond to the current sample time instant and assume that 1) the vehicle can start a lane change at any sample time instant $\zeta = {t\DeltaT}$, with $t = {0,\ldots,{N - 1}}$, over the planning horizon, and 2) a complete lane change takes a constant time duration of $T_{lc} = 3$ \[s\].

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-D Selecting Trajectories as vehicle actions", "weight": 1.0} -->

Then, for the case where at the current sample time instant the vehicle is in the middle of a lane change (i.e., the vehicle started the lane change $\DeltaT_{lc}$ \[s\] ago), $(x_{\text{ini}},{\overset{˙}{x}}_{\text{ini}},$ ${\overset{¨}{x}}_{\text{ini}},y_{\text{ini}},{\overset{˙}{y}}_{\text{ini}},{\overset{¨}{y}}_{\text{ini}})$ corresponds to the vehicle's current state and is satisfied by at $\zeta = 0$, while

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-D Selecting Trajectories as vehicle actions", "weight": 1.0} -->

Furthermore, we allow the vehicle, when it is in the middle of a lane change, to abort the lane change at any sample time instant $\zeta = {t\DeltaT}$ over the planning horizon. This represents a "change of mind" of the driver when a previously planned lane change becomes no longer feasible/safe. A trajectory for aborting a lane change is generated in a similar way as a lane change trajectory, but the terminal condition $(x_{\text{term}},{\overset{˙}{x}}_{\text{term}},{\overset{¨}{x}}_{\text{term}},y_{\text{term}},{\overset{˙}{y}}_{\text{term}},{\overset{¨}{y}}_{\text{term}})$ corresponds now to the vehicle's state after its returns to its original lane. Finally, we glue together pieces of trajectories for lane keeping, lane change, and aborting lane change to construct complete trajectories over the planning horizon.

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-D Selecting Trajectories as vehicle actions", "weight": 1.0} -->

This way, we obtain a total of $162$ trajectories for the merging vehicle that we treat as admissible actions. Each of these trajectories is characterized by 1) whether and when to start a lane change and 2) whether and when to abort an improper lane change. Fig. 3 illustrates a sampled set of such trajectories when the vehicle has not started a lane change and those when the vehicle is in the middle of a lane change. We denote each of such trajectories as $\gamma_{m}^{0}{(s_{0}^{0})}$, with $m = {1,2,\ldots,162}$, and the collection of such trajectories as ${\Gamma^{0}{(s_{0}^{0})}}:={\{{\gamma_{m}^{0}{(s_{0}^{0})}}\}}_{m = 1}^{162}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-D Selecting Trajectories as vehicle actions", "weight": 1.0} -->

We have defined the choice of a trajectory over a planning horizon for the merging vehicle as its action. Note that the time history of control inputs $u_{t} = {\lbrack a_{t},\delta_{f,t}\rbrack}^{T}$ corresponding to each of these trajectories can be calculated according to the vehicle dynamics model. In the actual implementation, the chosen trajectory can also be commanded to a lower level vehicle motion controller, and in this paper, it is assumed that the motion according to is accurately realized.

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-E Model predictive control strategy", "weight": 1.0} -->

We first consider an MPC-based trajectory planning strategy for the autonomous ego vehicle accounting for the presence of a signle interacting vehicle: At each sample time instant $t$, the ego vehicle computes an optimal trajectory, ${(\gamma_{t}^{0})}^{\ast}$, that maximizes its cumulative reward over the planning horizon according to

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-E Model predictive control strategy", "weight": 1.0} -->

where ${\overline{s}}_{t + \tau} = {(s_{t + \tau}^{0},s_{t + \tau}^{1})}$ represents the predicted traffic state at the discrete time instant $t + \tau$, while $u_{t + \tau}^{0}$ and $u_{t + \tau}^{1}$ represent, respectively, the predicted ego vehicle's and interacting vehicle's control inputs at $t + \tau$. The parameter $\lambda \in {}$ is discounting future reward thereby prioritizing immediate reward.

<!-- chunk {"id": "body-0034", "role": "body", "section": "II-E Model predictive control strategy", "weight": 1.0} -->

In, $R\left( {\overline{s}}_{t + \tau},u_{t + \tau}^{0},u_{t + \tau}^{1} \right)$ represents the reward received by the ego vehicle at $t + \tau$, which is described in Section II-C, and $S_{\text{safe}}$ represents a set of safe traffic states, used to enforce strict safety specifications (such as collision avoidance, road boundary constraints, etc).

<!-- chunk {"id": "body-0035", "role": "body", "section": "II-E Model predictive control strategy", "weight": 1.0} -->

After an optimal trajectory ${(\gamma_{t}^{0})}^{\ast}$ is obtained, the ego vehicle applies the control inputs corresponding to this trajectory, ${(u_{t}^{0})}^{\ast} = {\lbrack{(a_{t}^{0})}^{\ast},{(\delta_{f,t}^{0})}^{\ast}\rbrack}^{T}$, over one sampling period to update its state, and then repeats the above procedure at the next sample time instant $t + 1$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "II-E Model predictive control strategy", "weight": 1.0} -->

Note the following points: 1) The expression corresponds to the case where the ego vehicle interacts with only one other vehicle ($k = 1$). We will extend our MPC strategy to handle multiple vehicle interactions in Section IV-B. 2) The ego vehicle's control inputs over the planning horizon, $\{ u_{t}^{0},\ldots,u_{{t + N} - 1}^{0}\}$, correspond to its planned trajectory $\gamma_{t}^{0}$ and are calculated using $\gamma_{t}^{0}$ and the vehicle dynamics model, as has been discussed in Section II-D. 3) The interacting vehicle's control inputs over the planning horizon, $\{ u_{t}^{1},\ldots,u_{{t + N} - 1}^{1}\}$, are unknown variables.

<!-- chunk {"id": "body-0037", "role": "body", "section": "II-E Model predictive control strategy", "weight": 1.0} -->

In what follows, we introduce a game-theoretic approach that enables predictions of $\{ u_{t}^{1},\ldots,u_{{t + N} - 1}^{1}\}$ in response to the ego vehicle's actions so that make the MPC problem solvable.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Game-Theoretic Model for Vehicle Cooperation Behaviors and Explicit Representation Using Imitation Learning", "weight": 1.0} -->

In this section, we introduce the leader-follower game employed in this paper for modeling the interaction/cooperation between the merging vehicle and vehicles driving in the target lane. In order to simplify the online computations associated with this game-theoretic model, imitation learning is utilized to derive a neural network-based explicit representation of the model, which is used online for predicting the interacting vehicles' trajectories in response to the merging ego vehicle's actions in our MPC-based trajectory planning strategy.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-A Leader-follower game-theoretic model", "weight": 1.0} -->

During a highway forced merge process, the merging vehicle (ego vehicle) interacts with other vehicles driving in the target lane, who may choose to proceed or yield to the merging vehicle depending on the traffic situation and individual driver's preference. In this paper, we consider a game-theoretic model based on pairwise leader-follower interactions, called a leader-follower game, to represent drivers' cooperation intentions and their resulting vehicle behaviors. In this model, a vehicle (or, a driver) who decides to proceed before another vehicle is a leader in this vehicle pair and the one who decides to yield to another vehicle is a follower in the pair. The leader and the follower use different decision strategies. This leader-follower game-theoretic model was originally proposed, where it demonstrated the ability to effectively model drivers' intentions to proceed or yield (e.g., caused by common traffic rules and etiquette) in driving through intersections scenarios. Here, we briefly review this game-theoretic model and introduce its application to our highway forced merge scenarios.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-A Leader-follower game-theoretic model", "weight": 1.0} -->

where $\sigma \in L = {\{\text{leader},\text{follower}\}}$ represents the leader or follower role in the game, $R_{\sigma}\left( {\overline{s}}_{t + \tau},u_{l,{t + \tau}},u_{f,{t + \tau}} \right)$ is the reward function for the leader or the follower defined as in Section II-C, and $u_{l,{t + \tau}}$ and $u_{f,{t + \tau}}$, $\tau = {0,\ldots,{N - 1}}$, are the control inputs corresponding to $\gamma_{l,t}$ and $\gamma_{f,t}$ as described in Section II-D.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-A Leader-follower game-theoretic model", "weight": 1.0} -->

The decision model - can be explained as follows: A follower represents a driver who intends to yield. Due to uncertainty about the other driver's action, the follower decides to take an action that maximizes her worst-case reward through and. Such a "max-min" decision strategy of the follower models the yielding behavior because it assumes the other driver can take actions freely. Similarly, a leader represents a driver who intends to proceed and assumes the other driver will yield. Therefore, the leader uses the follower model to predict the other driver's action and takes an action that maximizes the leader own reward under the predicted follower's action through and. This leader-follower game model is partly inspired by the Stackelberg game model, but relaxes several assumptions of the Stackelberg model that generally do not hold for driver interactions in traffic. The reader is referred to for more discussions of this leader-follower game model and of its effectiveness for modeling driver interactions in multi-vehicle scenarios.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-A Leader-follower game-theoretic model", "weight": 1.0} -->

Note that although the asymmetric leader-follower roles in the decision model - are used to represent drivers' intentions to proceed and yield, respectively, the model does not imply that a leader interacting vehicle will always force a merging vehicle to merge behind it or a follower interacting vehicle will always let a merging vehicle merge in front of it. For instance, a merging vehicle may merge in front of a leader interacting vehicle in the following two situations: 1) The merging vehicle is ahead of the interacting vehicle with a sufficiently large distance to allow safe merging. 2) The merging vehicle is about to reach the end of its lane. Because getting off the road yields a large penalty (see Section II-C), the merging vehicle may choose to merge ahead of the interacting vehicle to avoid the large penalty as long as its merging will not lead to a collision between the two vehicles (it will not merge if the merging will cause a collision because the penalty for collision is even larger than for getting off the road). The above observations clarify that the leader-follower roles in our decision model - are not assigned by vehicle spatial positions (i.e., a leader is not necessarily a vehicle in front).

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-A Leader-follower game-theoretic model", "weight": 1.0} -->

Moreover, this model allows a merging vehicle to force the traffic in the target lane to let it merge into: As the merging vehicle approaches the end of its lane, it is increasingly inclined to merge to avoid the penalty for getting off the road even if all of the interacting vehicles in the target lane are leaders (i.e., their drivers all originally intend to proceed) and the current gaps are not large enough in terms of comfort. The model - enables these leader interacting vehicles to predict the merging vehicle's upcoming merging maneuver. Then, for their own safety and comfort, they will slow down to enlarge the gap and, consequently, warrant the merging. Therefore, our leader-follower model - is suitable for trajectory prediction and planning in forced merge scenarios.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-B Explicit representation of leader-follower game policy through imitation learning", "weight": 1.0} -->

Based on -, we are able to predict other vehicles' decision and trajectories given the knowledge of drivers' intentions and the current traffic state information. Hence, we can denote leader's optimal action policy as $\gamma_{l}^{\ast}{({\overline{s}}_{t})}$ and follower's optimal action policy as $\gamma_{f}^{\ast}{({\overline{s}}_{t})}$. Obtaining $\gamma_{l}^{\ast}{({\overline{s}}_{t})}$ and $\gamma_{f}^{\ast}{({\overline{s}}_{t})}$ require going through -, and the repeated online computations involving - can be time consuming. As a result, we want to explicitly represent $\gamma_{l}^{\ast}$ and $\gamma_{f}^{\ast}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-B Explicit representation of leader-follower game policy through imitation learning", "weight": 1.0} -->

Here, ${{\gamma_{\sigma}^{\ast}{({\overline{s}}_{t})}},\sigma} \in L$ are maps that map current traffic state to a predicted trajectory that other vehicle will follow. These maps are determined according to -. Instead of algorithmically determining $\gamma_{l}^{\ast}{({\overline{s}}_{t})}$ and $\gamma_{f}^{\ast}{({\overline{s}}_{t})}$, we follow and exploit the use of supervised learning, more specifically, imitation learning, to represent $\gamma_{\sigma}^{\ast}{({\overline{s}}_{t})}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-B Explicit representation of leader-follower game policy through imitation learning", "weight": 1.0} -->

Imitation learning can be considered as a supervised learning problem, where an autonomous agent tried to learn a policy by observing expert's demonstrations. The expert demonstration can be generated either by a human operator or an artificial intelligent agent. In this work, we treat $\gamma_{\sigma}^{\ast}{({\overline{s}}_{t})}$ obtained by - as the expert policy.

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-B Explicit representation of leader-follower game policy through imitation learning", "weight": 1.0} -->

In particular, the "Dataset Aggregation" algorithm has been utilized to obtain an imitated policy ${\hat{\gamma}}_{\sigma}$. The overall learning objective for the Dataset Aggregation algorithm can be described,

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-B Explicit representation of leader-follower game policy through imitation learning", "weight": 1.0} -->

where $\gamma_{\theta}$ represents a policy with respect to which optimization is performed and which is parameterized by $\theta$ (e.g. neural network weights), and $\mathcal{L}$ represents a loss function. More detailed discussions on the imitation learning and the "Dataset Aggregation" algorithm can be found in and.

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-B Explicit representation of leader-follower game policy through imitation learning", "weight": 1.0} -->

The model - and the imitation learning policies can be used to predict the other vehicles' decisions and future trajectories under the knowledge of their drivers' cooperation intentions. However, in a given traffic scenario, we may not know the other drivers' cooperation intentions a priori, because a driver's intention depends not only on the traffic situation (e.g., the relative position and velocity between two vehicles) but also on the driver's style/type (e.g., aggressive versus conservative). To deal with prior uncertainties about other vehicles' cooperation intentions, in what follows we describe an approach where such uncertainties are modeled as latent variables and the autonomous vehicle planning and control problem exploits estimating other vehicle's cooperation intentions as well as using predictive control method to obtain the optimal trajectory.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Decision Making under Cooperation Intention Uncertainty", "weight": 1.0} -->

In this section, we describe the decision making algorithm, called the Leader-Follower Game Controller (LFGC), for the highway forced merge scenario under cooperation intention uncertainty. During the forced merge process, we generate an estimate of other driver's cooperation intention, as described in this section. Based on the estimate of cooperation intention, we apply the control strategy presented in under multi-vehicle interactions settings by considering pairwise interactions.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-A Estimation of interacting vehicle's cooperation intention", "weight": 1.0} -->

According to Section III, we can model other driver's behavior based on their cooperation intentions using the leader-follower game. A yielding vehicle may have similar behavior as a follower in the game, while a proceeding (not yielding) vehicle may be modeled as a leader in the game. In this sense, we can estimate interacting vehicle's cooperation intention by estimating their leader or follower roles in the leader-follower game.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-A Estimation of interacting vehicle's cooperation intention", "weight": 1.0} -->

To achieve that, we consider the traffic dynamics model and the leader or follower's optimal actions and. From the perspective of the ego vehicle, the interacting vehicle is playing a leader-follower game with it, and the traffic dynamics model can be written as

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-A Estimation of interacting vehicle's cooperation intention", "weight": 1.0} -->

where $u_{t}^{0}$ is the control of ego vehicle, $u_{t}^{1}$ is the control of the interacting vehicle and is determined by the leader-follower game, $\sigma \in L = {\{\text{leader},\text{follower}\}}$ represents either leader of follower, and ${(u_{\sigma,t}^{1})}^{\ast}{({\overline{s}}_{t})}$ is the first control input corresponding to the optimal trajectory of $\gamma_{\sigma}^{\ast}{({\overline{s}}_{t})}$ in and. Now the only input to is the control of the ego vehicle $u_{t}^{0}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-A Estimation of interacting vehicle's cooperation intention", "weight": 1.0} -->

However, in reality, the interacting vehicle's decision does not necessarily follow the optimal policy computed from and. In order to account for the difference between the leader-follower policy and the actual policy of the interacting vehicle, we assume the system is propagated by with an additive Gaussian noise, i.e.,

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-A Estimation of interacting vehicle's cooperation intention", "weight": 1.0} -->

where $w$ is the additive Gaussian noise with 0 mean and covariance $W$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-A Estimation of interacting vehicle's cooperation intention", "weight": 1.0} -->

The ego vehicle is assumed to have a prior belief on $\sigma$, denoted as ${\mathbb{P}}{({\sigma = l})}$, with $l \in L = {\{\text{leader},\text{follower}\}}$. Then based on all previous traffic states and on all actions taken by the ego vehicle,

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-A Estimation of interacting vehicle's cooperation intention", "weight": 1.0} -->

the ego vehicle needs to compute or maintain a posterior belief of interacting vehicle's leader or follower role, ${\mathbb{P}}{({\sigma = \left. l \middle| \xi_{t} \right.})}$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-A Estimation of interacting vehicle's cooperation intention", "weight": 1.0} -->

The conditional posterior belief of interacting vehicle's leader or follower's role is computed using the hybrid estimation algorithm proposed.

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-A Estimation of interacting vehicle's cooperation intention", "weight": 1.0} -->

Specifically, identification of the interacting vehicle's leader or follower role can be achieved,

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-A Estimation of interacting vehicle's cooperation intention", "weight": 1.0} -->

where ${\mathbb{P}}{( \cdot | \cdot )}$ is the conditional probability; $\pi_{lk}$ denotes the transition probability of the interaction vehicle's role from $k$ to $l$; and $\Lambda_{l,t}$ is the likelihood function of the interacting vehicle as role $l$, defined,

<!-- chunk {"id": "body-0061", "role": "body", "section": "IV-A Estimation of interacting vehicle's cooperation intention", "weight": 1.0} -->

where $\mathcal{N}{(r_{l,t},0,W)}$ denotes the probability density function of the normal distribution with mean 0 and covariance $W$ evaluated at $r_{l,t}$; and $c_{t}$ is the normalization constant.

<!-- chunk {"id": "body-0062", "role": "body", "section": "IV-A Estimation of interacting vehicle's cooperation intention", "weight": 1.0} -->

Assuming the interacting vehicle's role remains unchanged over the merge period, i.e., $\pi_{lk} = 1$ when $l = k$ and $\pi_{lk} = 0$ when $l \neq k$, the posterior belief of the interacting vehicle's leader or follower role can be updated using the following equation,

<!-- chunk {"id": "body-0063", "role": "body", "section": "IV-A Estimation of interacting vehicle's cooperation intention", "weight": 1.0} -->

where ${\mathbb{P}}{({\sigma = \left. l \middle| \xi_{t - 1} \right.})}$ is the previous belief of the interacting vehicle's leader or follower role.

<!-- chunk {"id": "body-0064", "role": "body", "section": "IV-B Control strategy for multi-vehicle interactions", "weight": 1.0} -->

When the traffic is busy, there may exist multiple vehicles on highway that may interfere with the ego vehicle's merge, such as in the case shown in Fig. 1. One low complexity solution would be for the ego vehicle to only consider interaction with the first vehicle, and after the first vehicle becomes farther away, the ego vehicle starts to interact with the second vehicle. However, this may slow down the estimate of later vehicles' intentions, and in the case of highway forced merge, this can lead to the ego vehicle missing an opportunity to merge.

<!-- chunk {"id": "body-0065", "role": "body", "section": "IV-B Control strategy for multi-vehicle interactions", "weight": 1.0} -->

Another solution is to interact with multiple vehicles at the same time. In this case, a model needs to be constructed to predict interacting vehicle's actions. Although 2-player leader-follower game described in Section III can be extended to multi-player leader-follower game by considering a multi-level decision hierarchy and then solving for the Nash-equilibrium, such extensions may exponentially increase the computational time as the number of players increase. The Stackelberg equilibrium can be hard to obtain when there are more than 3 players. As a result, we propose a computationally tractable approach to extend the framework to multi-vehicle interactions by considering pairwise interactions.

<!-- chunk {"id": "body-0066", "role": "body", "section": "IV-B Control strategy for multi-vehicle interactions", "weight": 1.0} -->

When there are $m$ interacting vehicles, we consider pairwise interactions of the ego vehicle and each interacting vehicle. Then we can construct $m$ traffic states denoted as ${{\overline{s}}^{k},k} \in {\{ 1,\ldots,m\}}$ which contains the states of the ego vehicle and $k$th interacting vehicle, and the dynamic model of each ${\overline{s}}^{k}$ is given by

<!-- chunk {"id": "body-0067", "role": "body", "section": "IV-B Control strategy for multi-vehicle interactions", "weight": 1.0} -->

Similarly, we can denote by $\sigma^{k} \in L = {\{\text{leader},\text{follower}\}}$ the pairwise leader or follower role of the $k$th interacting vehicle and by $\xi_{t}^{k}$ the collection of all previous pairwise traffic states and actions taken by the ego vehicle, i.e.,

<!-- chunk {"id": "body-0068", "role": "body", "section": "IV-B Control strategy for multi-vehicle interactions", "weight": 1.0} -->

Then we can utilize to update the belief of each interacting vehicle's leader or follower role, ${{{\mathbb{P}}{({\sigma^{k} = \left. l \middle| \xi_{t}^{k} \right.})}},l} \in L = {\{\text{leader},\text{follower}\}}$. The MPC-based control strategy presented in can be reformulated as

<!-- chunk {"id": "body-0069", "role": "body", "section": "IV-B Control strategy for multi-vehicle interactions", "weight": 1.0} -->

where ${\hat{u}}_{\sigma,t}^{k}{({\overline{s}}_{t + \tau}^{k})}$ is the first control input corresponding to the trajectory of the trained policy ${\hat{\gamma}}_{\sigma}{({\overline{s}}_{t + \tau}^{k})}$, and $\varepsilon \in {\lbrack 0,1\rbrack}$ represents a (user-specified) required probability level of constraint satisfaction.

<!-- chunk {"id": "body-0070", "role": "body", "section": "IV-B Control strategy for multi-vehicle interactions", "weight": 1.0} -->

The expectation in the objective function can be computed according to

<!-- chunk {"id": "body-0071", "role": "body", "section": "IV-B Control strategy for multi-vehicle interactions", "weight": 1.0} -->

where ${\overline{s}}_{l,{t + \tau}}^{k}$ is the predicted traffic state given that the interacting vehicle's role is $l$,

<!-- chunk {"id": "body-0072", "role": "body", "section": "IV-B Control strategy for multi-vehicle interactions", "weight": 1.0} -->

and the last constraint in can be evaluated,

<!-- chunk {"id": "body-0073", "role": "body", "section": "IV-B Control strategy for multi-vehicle interactions", "weight": 1.0} -->

Note that the last constraint in enforces the following condition,

<!-- chunk {"id": "body-0074", "role": "body", "section": "IV-B Control strategy for multi-vehicle interactions", "weight": 1.0} -->

which means that the probability of any pairwise interactions entering unsafe states (e.g., collision and out of road boundaries) is less than $\varepsilon$.

<!-- chunk {"id": "body-0075", "role": "body", "section": "IV-B Control strategy for multi-vehicle interactions", "weight": 1.0} -->

and applying the last constraint, it follows that

<!-- chunk {"id": "body-0076", "role": "body", "section": "IV-B Control strategy for multi-vehicle interactions", "weight": 1.0} -->

The major differences between and are the following: 1) $\{ u_{t}^{1},u_{t + 1}^{1},\ldots,u_{{t + N} - 1}^{1}\}$ presented in are unknown, while, they are obtained based on trained policy from the imitation learning; 2) The maximization of the cumulative reward in is changed to maximization of the expected cumulative reward in to account for probabilistic belief about the interacting vehicle's leader/follower role; 3) The expected cumulative reward is changed to the sum of the expected reward of all pairwise interactions to account for uncertain behavior of multiple vehicles; 4) The hard constraint is changed to a probabilistic chance constraint with $\varepsilon \in {\lbrack 0,1\rbrack}$ being a design parameter.

<!-- chunk {"id": "body-0077", "role": "body", "section": "IV-B Control strategy for multi-vehicle interactions", "weight": 1.0} -->

The decision making algorithm proceeds as follows: At the sampling time $t$, the ego vehicle measures the current states of each pairwise interaction and adds them together with the previous control input to the observation vectors $\xi_{t}^{k}$. The belief about each vehicle's leader or follower role is updated according to based on $\xi_{t}^{k}$. Then, the MPC-based control strategy is utilized to obtain the optimal trajectory ${(\gamma^{0})}^{\ast}$ by searching through all trajectories introduced in Section II-D, and the ego vehicle applies the first control input ${(u_{t}^{0})}^{\ast}$ over one sampling period to update its states. The whole procedure is repeated at the next sampling time.

<!-- chunk {"id": "body-0078", "role": "body", "section": "IV-B Control strategy for multi-vehicle interactions", "weight": 1.0} -->

Note that the control strategy is "interaction-aware" due to the following reasons: 1) It predicts other vehicles' trajectories under varied interaction intentions based on the leader-follower game-theoretic model -. 2) The predictions are closed-loop. Specifically, for different trajectory plans of the ego vehicle, $\gamma^{0} \in {\Gamma^{0}{(s_{t}^{0})}}$, the corresponding trajectory predictions of the other vehicles under certain intentions are different. This is the case because the predicted other vehicles' actions are traffic state-dependent while the predicted traffic states depend on the planned ego vehicle's trajectory. 3) The objective function in is a conditional expectation and the constraint to represent safety is a conditional probability, both of which are conditioned on the latest estimates of other vehicles' intentions (i.e., leader or follower), ${\mathbb{P}}{({\sigma^{k} = \left. l \middle| \xi_{t}^{k} \right.})}$. Meanwhile, the other vehicles' intentions are estimated based on their previous interaction behaviors.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Simulation and Validation Results", "weight": 1.0} -->

In this section, we present validation results of applying the proposed Leader-Follower Game Controller (LFGC) for autonomous vehicle forced merge problems. Specifically, we consider three simulation validations, and in these simulations, the LFGC assumes that interacting vehicles are playing leader-follower game with the ego vehicle and estimates their leader/follower roles in the game. We also assume that once in the mandatory lane change situation, the ego vehicle prepositions itself towards the lane marker with turn signals to declare its merge intention and starts the forced merge process. As a result, interacting vehicles are aware of the ego vehicle's merging intention and react accordingly. We first validate the LFGC with interacting vehicles controlled by leaders or followers in the leader-follower game. Then we test the LFGC versus interacting vehicles controlled by other types of drivers or actual traffic data. Specifically, we test the cases where interacting vehicles are controlled by intelligent driver model (IDM) and where interacting vehicles are following the actual US Highway 101 traffic data present in the Next Generation Simulation website. Note that our simulations are performed in MATLAB R2019a on an PC with Intel Xeon E3-1246 v3 @ 3.50 GHz CPU and 16 GB RAM.

<!-- chunk {"id": "body-0080", "role": "body", "section": "V-A Interacting vehicles driven by leader/follower", "weight": 1.0} -->

We first test our proposed LFGC when interacting vehicles are simulated and controlled by leaders/followers in the game. The scenario we considered is shown in Fig. 4, where the autonomous ego vehicle (blue) in the acceleration lane needs to merge onto the highway before the end of acceleration lane while multiple other vehicles (red, pink, green) are currently driving on the highway. The ego vehicle starts the forced merge process by biasing towards lane markers and flashing turn signals at the moment shown in Fig. 4. In such a scenario, the autonomous vehicle needs to interact with other vehicles to merge safely.

<!-- chunk {"id": "body-0081", "role": "body", "section": "V-A Interacting vehicles driven by leader/follower", "weight": 1.0} -->

For the LFGC, the planning horizon is selected as $N = 4$ and the chance constraint parameter is chosen as $\varepsilon = 0.1$. Note that a larger $N$ may result in better long-term performance but also lead to longer computational time, while a smaller $N$ may emphasize on immediate benefits and hence fail to merge in many scenarios. For highway forced merge considered in this paper, $N$, in general, needs to be chosen such that it is longer than the duration of the lane change (i.e., ${N\DeltaT} \geq T_{\text{lc}}$). The initial beliefs are set to ${{\forall k} \in {\{ 1,2,3\}}},{{{\mathbb{P}}{({\sigma^{k} = \text{leader}})}} = {{\mathbb{P}}{({\sigma^{k} = \text{follower}})}} = 0.5}$. Fig. 5 shows the results when the ego vehicle is interacting with different combinations of leaders and followers.

<!-- chunk {"id": "body-0082", "role": "body", "section": "V-A Interacting vehicles driven by leader/follower", "weight": 1.0} -->

In Fig. 5, the left column ((a-1) to (d-1)) shows the ego vehicle belief about each of the other vehicles being a leader in the game, ${{{{\mathbb{P}}{({\sigma^{k} = \text{leader}})}},k} = 1},{2,3}$. The right column shows the time history results of the ego vehicle and other vehicles behaviors during this forced merge process.

<!-- chunk {"id": "body-0083", "role": "body", "section": "V-A Interacting vehicles driven by leader/follower", "weight": 1.0} -->

Fig. 5(a) shows the results when the ego vehicle is interacting with three leaders. The ego vehicle is able to capture interacting vehicle's intentions that all vehicles are more likely to be leaders in the game as shown in Fig. 5(a-1). After obtaining this information, the ego vehicle decides to slow down after $t = 1$ \[s\] and waits to merge after all interacting vehicles pass. When the ego vehicle is interacting with one leader (vehicle 1) and two followers (vehicle 2 and 3), the ego vehicle recognizes interacting vehicle's intentions correctly as shown in Fig. 5(b-1). Then the ego vehicle starts to slow down after $t = 1$ \[s\], and successfully merges between vehicles 1 and 2, which is shown in Fig. 5(b-2). Shown in Fig. 5(c) are the results of the ego vehicle interacting with two leaders (vehicles 1 and 2) and one follower (vehicle 3).

<!-- chunk {"id": "body-0084", "role": "body", "section": "V-A Interacting vehicles driven by leader/follower", "weight": 1.0} -->

In this case, the ego vehicle observes that vehicles 1 and 2 speed up and do not yield to it, so the ego vehicle decides to slow down and merge between vehicles 2 and 3. We also perform the test when the ego vehicle interacts with three followers, and the results are shown in Fig. 5(d), where the ego vehicle observes all vehicles yielding intentions, speeds up and merges in front of all interacting vehicles. The average computational time for solving at each time step is 0.182 \[s\].

<!-- chunk {"id": "body-0085", "role": "body", "section": "V-A Interacting vehicles driven by leader/follower", "weight": 1.0} -->

For all cases shown in Fig. 5, the initialized beliefs are the same, which means the ego vehicle does not know ahead of time whether the interacting vehicle is a leader or a follower. As a result, the ego vehicle relies on its observations to estimate interacting vehicles leader/follower role. The proposed LFGC can capture interacting vehicles' intentions and making decisions accordingly when all interacting vehicles are controlled by the leader/follower in leader-follower game.

<!-- chunk {"id": "body-0086", "role": "body", "section": "V-B Interacting vehicles driven by intelligent driver model", "weight": 1.0} -->

The validation results shown in Section V-A assumes that other drivers make decisions based on the leader-follower game. The LFGC assumes other drivers are playing leader-follower game with the ego vehicle, estimates their roles in the game, and makes decision accordingly. This means that the environment in Section V-A behaves just as the LFGC expects. However, the actual behavior of other drivers might be different from leader-follower game's policy. As a result, we want to further investigate how the framework responds to other types of driver models.

<!-- chunk {"id": "body-0087", "role": "body", "section": "V-B Interacting vehicles driven by intelligent driver model", "weight": 1.0} -->

In this section, we employ the intelligent driver model (IDM) to control other vehicles and interact with the ego vehicle. The ego vehicle is still controlled by the LFGC and tries to estimate interacting vehicles' intentions by estimating their corresponding leader or follower roles. IDM is a continuous-time car-following model and is described by to.

<!-- chunk {"id": "body-0088", "role": "body", "section": "V-B Interacting vehicles driven by intelligent driver model", "weight": 1.0} -->

where $x$ is the longitudinal position; $v$ is the longitudinal velocity; $v_{0}$ is the desired velocity of the vehicle; $\phi = {x - x_{t} - l_{t}}$ is the following distance with $x_{t}$ being the position of the target vehicle and $l_{t}$ being the length of the target vehicle; ${\Deltav} = {v - v_{t}}$ is the velocity difference of the vehicle and the target vehicle; $\phi^{\ast}{(v,{\Deltav})}$ is obtained according to,

<!-- chunk {"id": "body-0089", "role": "body", "section": "V-B Interacting vehicles driven by intelligent driver model", "weight": 1.0} -->

where $a_{m},\phi_{0},T,b$ are parameters of the IDM model. The physical interpretation of these parameters are the maximum acceleration $a_{m}$, the minimum car following distance $\phi_{0}$, the desired time headway $T$, and the comfortable deceleration $b$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "V-B Interacting vehicles driven by intelligent driver model", "weight": 1.0} -->

For the validation tests, we consider the scenario shown in Fig. 6. In Fig. 6, there is another vehicle ahead of all vehicles (black vehicle 4), and it is driving at a constant speed. The ego vehicle is still the same as in Section V-A and is controlled by the LFGC, which means that from the ego vehicle perspective, it is playing leader-follower game with all interacting vehicles. For these three interacting vehicles (vehicle 1 to 3), they are controlled by IDM to follow either front vehicle (vehicle 4) or the ego vehicle with certain time headway $T$. The IDM model parameters are listed in Table I. Note that the ego vehicle regards vehicle 4 as the environmental vehicle and assumes it is driving at constant speed.

<!-- chunk {"id": "body-0091", "role": "body", "section": "V-B Interacting vehicles driven by intelligent driver model", "weight": 1.0} -->

Different desired time headway in IDM may reflect conservativeness of the drivers. If the interacting vehicle intends to yield to the ego vehicle, we model it to use IDM to follow the ego vehicle with certain time headway. This means each interacting vehicle has an option to follow either the front vehicle or the ego vehicle.

<!-- chunk {"id": "body-0092", "role": "body", "section": "V-B Interacting vehicles driven by intelligent driver model", "weight": 1.0} -->

For the LFGC, the setting is the same as in Section V-A. The planning horizon is selected as $N = 4$ and the chance constraint parameter is chosen as $\varepsilon = 0.1$. The initial beliefs are set to ${{\forall k} \in {\{ 1,2,3\}}},{{{\mathbb{P}}{({\sigma^{k} = \text{leader}})}} = {{\mathbb{P}}{({\sigma^{k} = \text{follower}})}} = 0.5}$. Fig. 7 shows the results when the ego vehicle is interacting with other vehicles controlled by IDM with different target vehicles and different desired time headway.

<!-- chunk {"id": "body-0093", "role": "body", "section": "V-B Interacting vehicles driven by intelligent driver model", "weight": 1.0} -->

In Fig. 7(a), the first interacting vehicle (vehicle 1) intends to yield to the ego vehicle, so it chooses to follow the ego vehicle with 1 \[s\] time headway, while the last two interacting vehicles are following the front vehicles with 0.5 \[s\] headway. From Fig. 7(a-1), the ego vehicle thinks that vehicle 1 has a high probability being a follower in the game and chooses to merge in front of vehicle 1 as depicted in Fig. 7(a-2). Fig. 7(b) shows another case where the first interacting vehicle (vehicle 1) follows the front vehicle with 0.5 \[s\] headway, and the second interacting vehicle intends to yield to the ego vehicle and follows the ego vehicle with 0.5 \[s\] headway. Then in this case, from the ego vehicle perspective, vehicle 1 has higher probability being a leader in the game, while vehicle 2 has a higher probability being a follower in the game, and hence the ego vehicle successfully merges in front of vehicle 2 in this case. Two other non-yield cases are shown in Fig. 7(c) and (d).

<!-- chunk {"id": "body-0094", "role": "body", "section": "V-B Interacting vehicles driven by intelligent driver model", "weight": 1.0} -->

Fig. 7(c) shows the results of all interacting vehicles following the front vehicle with 0.5 \[s\] headway. From the ego vehicle perspective, all interacting vehicles are more likely to be leaders in the game, so the ego vehicle successfully merges after all vehicles pass. In Fig. 7(d), all interacting vehicles follow the front vehicle with 1.5 \[s\] headway. In this case, the ego vehicle finds that vehicle 2's behavior is conservative and thinks vehicle 2 has a higher probability being a follower in the game. Hence, the ego vehicle successfully merges between vehicles 1 and 2. The average computational time for solving at each time step is 0.198 \[s\].

<!-- chunk {"id": "body-0095", "role": "body", "section": "V-B Interacting vehicles driven by intelligent driver model", "weight": 1.0} -->

For all cases shown in Fig. 7, the ego vehicle starts with the same initial belief. This means that the ego vehicle does not know other drivers conservativeness (represented by desired time headway) and intentions (represented by target vehicles) a priori. The ego vehicle relies on the LFGC to estimate their intentions, make decisions accordingly and is able to merge successfully.

<!-- chunk {"id": "body-0096", "role": "body", "section": "V-C Interacting vehicles following traffic data", "weight": 1.0} -->

We have already tested the LFGC with other vehicles driven by leader/follower in the leader-follower game and by IDM models. We want to further test the controller's performance against real traffic data. Specifically, we use the US highway 101 traffic dataset from the Next Generation Simulation (NGSIM) website, which is collected by the United States Federal Highway Administration and is considered as one of the largest publicly available sources of naturalistic driving data. The US highway 101 dataset has been extensively studied in the literature.

<!-- chunk {"id": "body-0097", "role": "body", "section": "V-C Interacting vehicles following traffic data", "weight": 1.0} -->

More specifically, we consider a portion of the US101 traffic dataset that contains 30 minutes of vehicles trajectories on the US101 highway. The time period ranges from 7:50 to 8:20 am, which represents the buildup of congestion around the morning peak hours. The dataset contains position and velocity trajectories as well as vehicle dimensions for around 6000 vehicles, and the information is recorded every 0.1 \[s\]. The top view of the portion of the US101 highway that is used for collecting the data is shown in Fig. 8. The studied section consists of five main lanes of the highway, one on-ramp to the highway, one off-ramp exiting the highway, and also one auxiliary lane that is used to merge into the highway and exit the highway.

<!-- chunk {"id": "body-0098", "role": "body", "section": "V-C Interacting vehicles following traffic data", "weight": 1.0} -->

As discussed, the US101 dataset contains a significant amount of noise due to video analysis and numerical differentiation. To overcome this drawback, the Savitzky-Golay filter is utilized to smooth vehicles' positions and update their corresponding velocities. The Savitzky-Golay filter performs well for signal differentiation and smoothing the US101 dataset with window length 21. One original vehicle trajectory and the corresponding smoothed vehicle trajectory are shown in Fig. 9.

<!-- chunk {"id": "body-0099", "role": "body", "section": "V-C Interacting vehicles following traffic data", "weight": 1.0} -->

For the validation tests of the LFGC, we focus on the on-ramp and the auxiliary lane to identify all merging vehicles. After identifying the merging vehicles and the corresponding scenario, we identify the interacting vehicles according to Fig. 10. Specifically, we consider the first vehicle in the target lane that is within 2 \[s\] time headway in front of the ego vehicle as the first interacting vehicle and regard the consecutive vehicles as the second and third vehicles. For all other vehicles present in the scenario, the ego vehicle will regard them as environmental vehicles and assume they drive at constant speed. One identified merging scenario is shown in Fig. 11.

<!-- chunk {"id": "body-0100", "role": "body", "section": "V-C Interacting vehicles following traffic data", "weight": 1.0} -->

For each merging scenario, instead of letting the ego vehicle to follow the traffic data, we use the LFGC to control ego vehicle's action and resulting trajectory. For all other vehicles including interacting vehicles and environmental vehicles, they follow their corresponding trajectories present in the US101 traffic dataset. Then, the LFGC needs to estimate interacting vehicles' intentions and control the ego vehicle to merge appropriately. Note that interacting vehicles and environmental vehicles may interact with the merging vehicle in the actual traffic during the data collection. Since the LFGC may take different actions from human's operation, interacting vehicles' or environmental vehicles' behaviors are not responding to the ego vehicle's action. Instead, their behaviors are pre-determined by the traffic dataset.

<!-- chunk {"id": "body-0101", "role": "body", "section": "V-C Interacting vehicles following traffic data", "weight": 1.0} -->

Statistics of validating the LFGC based on the US101 traffic dataset are shown in Table II. There are a total of 198 merge cases present in the dataset that happen from 7:50 to 8:20 am. The average computational time for solving at each time step among all merge cases is 0.259 \[s\]. In 193 merge cases, the LFGC successfully maneuvers the ego vehicle to merge to the target lane. The LFGC fails in 5 cases including 4 \"Fail to Merge\" cases and 1 \"Collision\" case. The reason for these failure cases is primarily due to either 1) the LFGC cannot obtain a high belief on interacting vehicles' driving intentions and hence needs to take conservative action to avoid collision, or 2) the traffic is dense such that there is no safe margin for the ego vehicle to merge without intersecting with other vehicles' collision boxes.

<!-- chunk {"id": "body-0102", "role": "body", "section": "V-C Interacting vehicles following traffic data", "weight": 1.0} -->

In Fig. 12, we present screenshots for one successful merges. In these figures, the blue vehicle is controlled by the LFGC, and the grey box represent the actual position of the ego vehicle in the dataset. All other vehicles (including red interacting vehicles and black environmental vehicles) are following their corresponding trajectories in the dataset. The ego vehicle controlled by the LFGC makes similar decisions compared to the human driver (grey box): Both the LFGC and the human driver try to speed up and merge in front of the truck (Vehicle 1) at first. However, after recognizing that the truck is more likely to proceed without yielding, the ego vehicle decides to slow down and merges after the truck.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Summary", "weight": 1.0} -->

In this paper, we proposed a Leader-Follower Game Controller (LFGC) for autonomous vehicle planning and control in merge scenarios. The LFGC treats interaction uncertainties due to different driver intentions as latent variables, estimates on-board other driver intentions, and chooses actions to facilitate ego vehicle's merge. In particular, the LFGC is able to perform a receding horizon optimization subject to an explicit probabilistic safety characterization i.e., subject to constraints representing vehicle safety requirements. By considering pairwise interactions of the ego vehicle and interacting vehicles, the LFGC is able to handle interactions with multiple vehicles in a computational tractable way. Finally, multiple simulation-based validations are performed to demonstrate effectiveness of the LFGC, including scenarios that other vehicles are following leaders or followers in the game, the Intelligent Driver Model (IDM), and actual US Highway 101 data.
