<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Active Inference as a Unified Model of Collision Avoidance Behavior in Human Drivers

Topics include Active inference, Driver models, Collision avoidance, Human behavior modeling, Autonomous driving, Evidence accumulation, Particle filters, Expected free energy, Traffic safety.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Builds an active-inference model of human collision avoidance that combines looming-based perception, norm-conditioned particle-filter prediction, evidence accumulation, and expected-free-energy policy selection. The model is valuable because it explains response timing, maneuver choice, and execution across several crash-imminent driving scenarios rather than fitting a single narrow behavioral metric.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Collision avoidance - involving a rapid threat detection and quick execution of the appropriate evasive maneuver - is a critical aspect of driving. However, existing models of human collision avoidance behavior are fragmented, focusing on specific scenarios or only describing certain aspects of the avoidance behavior, such as response times. This paper addresses these gaps by proposing a novel computational cognitive model of human collision avoidance behavior based on active inference. Active inference provides a unified approach to modeling human behavior: the minimization of free energy. Building on prior active inference work, our model incorporates established cognitive mechanisms such as evidence accumulation to simulate human responses in two distinct collision avoidance scenarios: front-to-rear lead vehicle braking and lateral incursion by an oncoming vehicle. We demonstrate that our model explains a wide range of previous empirical findings on human collision avoidance behavior. Specifically, the model closely reproduces both aggregate results from meta-analyses previously reported in the literature and detailed, scenario-specific effects observed in a recent driving simulator study, including response timing, maneuver selection, and execution. Our results highlight the potential of active inference as a unified framework for understanding and modeling human behavior in complex real-life driving tasks.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Abstract", "weight": 1.5} -->

Collision avoidance -- involving a rapid threat detection and quick execution of the appropriate evasive maneuver -- is a critical aspect of driving. However, existing models of human collision avoidance behavior are fragmented, focusing on specific scenarios or only describing certain aspects of the avoidance behavior, such as response times. This paper addresses these gaps by proposing a computational cognitive model of human collision avoidance behavior based on active inference. Active inference provides a unified approach to modeling human behavior: the minimization of free energy. Building on prior active inference work, our model incorporates established cognitive mechanisms such as evidence accumulation to simulate human responses in three distinct collision avoidance scenarios: front-to-rear lead vehicle braking, lateral incursion by an oncoming vehicle, and another vehicle failing to yield at an intersection. We demonstrate that our model explains a wide range of empirical findings on human collision avoidance behavior. Specifically, the model closely reproduces both aggregate results from meta-analyses previously reported in the literature and detailed, scenario-specific effects observed in two recent driving simulator studies, including response timing, maneuver selection, and execution. Our results highlight the potential of active inference as a generalizable framework for understanding and modeling human behavior in complex real-life driving tasks.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Abstract", "weight": 1.5} -->

Collision avoidance is a critical skill for human drivers. It involves the rapid detection of threats (such as a vehicle ahead suddenly braking) and deciding on an appropriate evasive maneuver (for instance, braking or swerving). These maneuvers are complex, requiring not only precise execution but also continuous adjustments as the situation evolves. Furthermore, drivers need to account for the uncertainty in the future behavior of other road users: for example, will an oncoming vehicle encroaching into my lane continue across or move back to its own lane? Understanding how humans avoid collisions in traffic can provide insights into high-stakes, split-second decision making which has substantial implications for traffic safety.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Abstract", "weight": 1.5} -->

Behavior models play a key role both in understanding the mechanisms of human collision avoidance and in improving traffic safety. These models are applied in diverse contexts, such as collision risk estimation \[, understanding effects of driver distraction, modeling take-over behavior, representing human agents in simulated test environments, and providing behavioral benchmarks for automated vehicles. Besides immediate practical applications, modeling human collision avoidance behavior is an interesting subject of study in its own right. Being a highly complex and dynamic task with extremely high stakes, collision avoidance provides a unique testbed for theories and models of cognition previously not validated in the real world.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Abstract", "weight": 1.5} -->

Most existing computational models of human collision avoidance are mechanistic, that is, are based on the explicit modeling of cognitive mechanisms underlying response timing and evasive maneuvering. However, they are typically fragmented, focusing either on specific scenario types (e.g., front-to-rear conflicts or merging ), specific explanatory factors (such as off-road glances or cognitive load ), or only reproduce certain aspects of human behavior (such as response times or the extent of steering ). Altogether, these models cover a wide range of scenarios and diverse aspects of collision avoidance behavior. Yet, each one of these mechanistic models on its own is highly specific: they are not designed to generalize to multiple scenarios or describe multiple aspects of human behavior.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Abstract", "weight": 1.5} -->

Recently, machine learning models based on large datasets of human driving have demonstrated the ability to generalize across a wide range of traffic scenarios. Because such models typically generate full motion trajectories, they also have the potential to represent multiple aspects of collision avoidance behavior and not just a single metric of interest. However, a key challenge is that safety-critical behavior such as collision avoidance is often under-represented in the datasets used for training, which makes it hard to achieve representative human-like collision avoidance behavior solely based on learning from data.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Abstract", "weight": 1.5} -->

Thus, there is currently a lack of models that can capture the key aspects of human collision avoidance behavior (response selection, timing, and execution) all at the same time and across different scenarios. This limits both practical applications (due to the need to develop a new model for every new scenario) and fundamental understanding of cognitive mechanisms underlying the behavior of humans in safety-critical situations in traffic (due to the lack of a unified explanation for multiple aspects of behavior).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Abstract", "weight": 1.5} -->

To address this gap, here we present a model of human collision avoidance behavior based on active inference. Originating in computational neuroscience, active inference is a versatile general framework for understanding and modeling sentient behavior in living systems that has been previously used to model human behavior in diverse contexts, including the modeling of human driver behavior such as car following, responses to driving automation failures, and managing uncertainty around occlusions and non-driving-related tasks. Building on the model of Engström et al., our active inference model is designed to reproduce a wide spectrum of human behavior (e.g., chosen maneuver, reaction timing, collision likelihood, etc.) in response to potential collisions. To this end, our model incorporates several well-known cognitive mechanisms to represent the dynamics of human decision making in response to sudden stimuli, such as looming perception and evidence accumulation.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Abstract", "weight": 1.5} -->

We evaluated our model against a range of previously reported empirical findings in three paradigmatic collision avoidance scenarios: 1) the front-to-rear scenario, where a driver needs to respond to a suddenly braking vehicle in front, 2) the opposite-direction lateral incursion scenario, where an oncoming vehicle suddenly cuts across the driver's path, and 3) the intersection right-turn-into-path scenario, where a vehicle coming from the right on a perpendicular road does not yield when turning right into the driver's lane. Testing the model in three markedly different scenarios allowed us to investigate the potential of active inference as a framework for generalizable modeling of human collision avoidance behavior.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Results", "weight": 1.0} -->

In this work, we use active inference as an overarching framework to guide the modeling. The key premise of active inference is that all behavior and cognition can be understood based on the single principle of minimizing free energy. An agent minimizing free energy can be conceptually understood as the agent sensing, and acting upon, the world in such a way as to minimize its surprise over time. In the active inference framework, this amounts to seeking out observations that are expected (unsurprising) and preferred given the type of creature the agent is, reflecting its adaptation to its particular environment or niche (e.g., a fish expects and prefers the sensation of being immersed in water). Agents capable of planning into the future and modeling the consequences of their actions (such as human car drivers), select plans that minimize the expected surprise, or more generally the *expected free energy* (EFE).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Results", "weight": 1.0} -->

Our model implements these principles in the collision avoidance context (Figure 1). Specifically, the modeled agent repeatedly evaluates possible futures under its current policy (i.e., a sequence of planned actions) -- including interactions with other road users -- in terms of their EFE. The driver then selects policies that minimize EFE by realizing observations that align with the driver's preferences such as avoiding collisions (yielding *pragmatic value*) while obtaining new information to reduce uncertainty in the agent's beliefs about the future (yielding *epistemic value*).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Results", "weight": 1.0} -->

Fundamentally, agents cannot have perfect knowledge of the mechanisms underlying the surrounding world (the *generative process*), but instead rely on an internal, not necessarily veridical, representation of their beliefs about the environment, the *generative model*. Importantly, an (ego) agent's *generative model* is probabilistic, with the uncertainty about the state of the world being represented by a set of sample particles. Our model implements these general principles in a time-discrete, sequential process (Figure 2) which incorporates a number of key perceptual, cognitive, and motor mechanisms.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Results", "weight": 1.0} -->

Looming-based perception. First, the agent observes the world and updates its belief (Figure 2a), combining these observations with the expectations derived from the generative model propagating its previous belief forward in time. The model assumes that the agent cannot directly perceive kinematic states of surrounding objects (e.g., positions and velocities), but instead uses the readily available perceptual information: the object's visual angle $\varphi$ subtended at the driver's retina, and its derivative, the angular rate $\overset{˙}{\varphi}$, commonly referred to as *looming*. The model then infers back the kinematic state from those observations, where -- with increasing distances -- equal variations in $\varphi$ lead to increasingly larger variations in the inferred distance and therefore increasing uncertainty about the kinematic state of the other agent. Additionally, the agent's perception accuracy is limited: it cannot perceive looming with absolute values below a threshold ${\overset{˙}{\varphi}}_{0}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Results", "weight": 1.0} -->

Due to this threshold, the agent is unable to detect small relative velocities at long distances; our model thus incorporates this looming threshold as one possible mechanism behind delays in recognizing events like abrupt braking of a lead vehicle.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Results", "weight": 1.0} -->

Behavior prediction via norm-conditioned particle filter. After perceiving the environment, the ego agent predicts the other vehicle's behavior (Figure 2b). For this, our model uses a sample-based approach based on a particle filter. Specifically, the samples representing the agent's updated belief about the other vehicle are propagated forward by the *generative model* (in our case using a bicycle model with additive Gaussian noise). In this way, the model generates multiple distinct kinematically plausible future trajectories of the other vehicle, including the ones that could potentially lead to a collision. This enables the model to anticipate rare, long-tail behaviors of the other vehicle and respond to them appropriately during collision avoidance, but yields overly pessimistic predictions in non-conflict situations. For instance, widely dispersed predictions could lead the agent to anticipate any vehicles in the adjacent lane potentially encroaching into its lane, incentivizing unnecessary evasive actions.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Results", "weight": 1.0} -->

Thus, relying solely on kinematic likelihood for the generation of these samples would lead to overly cautious behavior. In reality, human drivers typically must assume that other road users follow traffic rules and other social norms for driving to allow for efficient interaction. To reflect this, our model's sampling process is biased towards trajectories that are not only kinematically feasible but also *normatively likely*, that is, aligned with societal normative expectations on how to behave on the road. We refer to this biased sampling process as a *norm-conditioned particle filter*. In effect, the model's belief about the other vehicle's future trajectory is initially constrained by normative expectations, such as that vehicles typically remain within their lane unless there is evidence to suggest otherwise. At the same time, the normative probability is bounded from above: trajectories where norm compliance stays constant or improves over time compared to the starting state are assigned an equal normative likelihood, while those with decreasing norm compliance are deemed less likely.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Results", "weight": 1.0} -->

Thus, when another vehicle unexpectedly causes a conflict (for example, by encroaching into the ego vehicle's lane), the model relaxes the assumption of that vehicle's future norm-compliance as well, sampling norm-violating trajectories as long as they remain kinematically plausible.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Results", "weight": 1.0} -->

While there is generally a large set of normative expectations dependent on cultural influence, we chose to only implement specific norm-influencing behaviors in each scenario (e.g., staying in one's lane or yielding to the right of way, see Supplementary Figure LABEL:fig:Norm_prob). A generalized, scenario-independent implementation of such norms is feasible, but with the goal of computational efficiency was not pursued here.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Results", "weight": 1.0} -->

Re-planning full policy based on accumulating surprise. In the next step, based on the set of previously predicted possible trajectories of the other vehicle, the agent considers its own policy, evaluating its current suitability by calculating the *residual information* of the *pragmatic value*, which can be seen as a measure of surprise. This surprise signal -- the (scaled) negative pragmatic value associated with the currently selected policy -- essentially indicates how unsuitable the current policy is given the model's preferred observations and how the situation is expected to develop. The model assumes that the driver continuously accumulates this surprise signal as evidence in favor of full policy re-plan (Figure 2c). On each time step, if the accumulated evidence has not reached a predefined threshold, the agent considers it sufficient to continue with the current policy, and extends this policy one time step into the future (Figure 2d.i and e.i). However, if enough evidence in favor of current policy being unsuitable is accumulated, a set of completely new policies is sampled and a new full policy is selected (Figure 2d.ii and e.ii).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Results", "weight": 1.0} -->

The first action from either the extended or the new full policy is then applied to update the environment for the next time step (Figure 2f). This mechanism, where policy re-planning is contingent on the accumulation of evidence, thus provides a way to represent the dynamics of human decision making and response timing in the model.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Results", "weight": 1.0} -->

Constrained policy sampling. When proposing new candidate policies, either for extension (Figure 2d.i) or full re-plan (Figure 2d.ii), the model uses the *cross-entropy method*. With this method, candidate actions are iteratively resampled, increasingly focusing on the most promising areas of the action space. To represent humans' bounded capacity for planning under time pressure, we limit the number of evaluated policies in this process. Importantly, the sampled acceleration values are constrained to reflect that humans operate the gas and brake pedals with one foot. These constraints include limiting applied jerks (as humans cannot press or release pedals instantaneously) and enforcing a constant holding time of $0.2\ s$ at acceleration $a_{0} \lesssim {0\ {ms}^{- 2}}$ during transitions in both directions between acceleration and deceleration (as humans cannot move their foot between pedals instantaneously).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Results", "weight": 1.0} -->

Policy selection via expected free energy minimization. Among the sampled candidate policies, the model aims to find the policy that minimizes *expected free energy* (EFE) -- the cornerstone of the active inference framework (Figure 2e.i and e.ii). In our model, the pragmatic value part of the EFE is maximized by 1) maintaining a desired longitudinal velocity, 2) staying within the current lane (avoiding unnecessary or unsafe lane changes) and on the road, 3) minimizing control inputs (avoid harsh braking or steering), 4) preventing collisions or at least reducing their severity (measured by the relative impact velocity), and 5) maintaining sufficient safety margins, avoiding situations where collisions may become unavoidable (such as when following a vehicle too closely without a sufficient stopping distance). Finally, maximizing epistemic value encourages 6) policies that are expected to result in a wide variety of reliable observations which may help reducing uncertainty.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Results", "weight": 1.0} -->

However, in the present collision avoidance setting, behavior is mainly expected to be driven by pragmatic, rather than epistemic, value since there is not much the driver can do to reduce uncertainty, especially given that we here assume that the other vehicle is non-reactive to the ego agent's actions.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Model evaluation", "weight": 1.0} -->

We evaluated the model against human data in three scenarios. First, in the front-to-rear scenario, we compared the model to the results of a meta-analysis of brake response times in experimental driving simulator and field studies (e.g., Brookhuis et al. and Lee et al. ), and an analysis of deceleration magnitudes reported in based on two real-world driving datasets captured across the US (the SHRP2 dataset ) and Africa (the ANNEXT dataset ).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Model evaluation", "weight": 1.0} -->

Second, in the opposite-direction lateral incursion scenario, the model was compared to human data from a driving simulator study conducted in UK which was conducted in parallel to the present work. Thus, by contrast to the model evaluation for the front-to-rear scenario, which was based on aggregated data, we were here able to run our model on nearly identical scenarios for which the human data was collected, allowing for more detailed comparisons. We manually fitted the model parameters to reproduce human behavior in the first two scenarios; same parameter values were used for both scenarios.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Model evaluation", "weight": 1.0} -->

Third, to test the ability of the model to generalize to new scenarios, we tested it, with the same parameter settings, in an unseen third scenario conducted in Canada, an intersection right-turn-into-path scenario where another vehicle failed to yield the right of way. Similarly to the lateral incursion scenario, we were able to closely reproduce the scenarios faced by the human participants.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Front-to-rear scenario", "weight": 1.0} -->

In the front-to-rear scenario, the ego vehicle trails the other vehicle which is driving in the same lane; both vehicles have the same initial velocity which was systematically varied in our simulations together with the initial time gap between the vehicles. After a short time of driving at constant speed, the other vehicle starts braking with a high constant deceleration until coming to a stop. Depending on the initial kinematics of the vehicles, the ego agent can avoid collision either solely by braking (Figure 3a) or combined braking and swerving (Figure 3b). The model sometimes avoided a collision by swerving only (i.e., without braking). However, since existing results in the literature on front-to-rear scenarios typically only report on braking response performance, we only compared our model's brake response times to the human response data (i.e., for the analysis of those, steering only responses were not considered).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Front-to-rear scenario", "weight": 1.0} -->

At lower speeds and larger time gaps, the model typically avoids collisions by braking only. In a representative simulation (Figure 3a), after the leading agent started braking at $t = {0.8\ s}$ (first dashed line), it took the model $0.6\ s$ to perceive this (see the ego agent's belief in the acceleration plot). At that point ($t = {1.4\ s}$, second dashed line), the model recognized the imminent conflict resulting from this change in perceived behavior of the other vehicle, as can be seen by the sudden decrease (increase in negative value) in the collision part of the pragmatic value. This leads to a corresponding increase in the rate of accumulation of the evidence for a re-plan (i.e., surprise). However, it still took another $0.6\ s$ until the accumulated evidence $E$ reached the threshold, delaying the first noticeable agent reaction to $t = {2\ s}$ (third dashed line), where the agent started to execute a new policy -- emergency braking.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Front-to-rear scenario", "weight": 1.0} -->

This policy was selected because it allowed the agent to drastically reduce its EFE via reaching future states with high pragmatic value, in particular thanks to low collision probability. This policy was preferred over the alternative policy of braking and steering into the adjacent lane because the pragmatic value associated with lane changing was more negative than that associated with lower velocity, as the desired (corresponding to the initial) velocity is comparatively low. However, even under this policy, at $t = {2\ s}$, the acceleration has still not changed, due to the pedal constraints. Consequently, the first deceleration of the model can be observed at $t = {2.2\ s}$, resulting in a total response time of $1.4\ s$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Front-to-rear scenario", "weight": 1.0} -->

Smaller time gaps and higher initial velocities can make it kinematically impossible to avoid collision by braking only. In such situations, the model typically opts to steer and brake at the same time (Figure 3b). Here, due to the smaller initial distance, the model's perception delay was noticeably shorter (being only about $0.2\ s$, with the modeled agent perceiving the braking at $t = {1\ s}$, the first dashed line). However, due to the more challenging initial kinematics, it was more difficult for the model to avoid collision, despite the shorter perception delay. In particular, the model switched between different policies three times. Initially, the model recognized the need to slightly brake and then steer around the other vehicle: already at the time of the first re-plan ($t = {1.4\ s}$, second dashed line) the collision component of EFE was substantially reduced by the chosen policy.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Front-to-rear scenario", "weight": 1.0} -->

This policy was mostly sufficient in improving the collision component of the pragmatic value, but as visible in the top panel (planned trajectory ${\overset{\sim}{\mathbf{X}}}_{\text{ego}}$), the agent intends to stay in between lanes for an extended period. This led to two further re-plans ($t = {3.6\ s}$ and $t = {5.4\ s}$, third and fourth dashed lines respectively) to adjust the trajectory. However, even having passed the other vehicle already, the model is not completely successful, with a noticeable lateral position component remaining in the pragmatic value. As the optimal solution of driving in the center of the current lane on a free road should have maximized the pragmatic value, this remaining lateral error is likely the result of the cross-entropy method not identifying the optimal policy. This represents a bounded planning capacity which, as discussed above, is also present in humans and thus an intended feature of our model.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Front-to-rear scenario", "weight": 1.0} -->

By systematically varying the initial kinematics of the vehicles, we assessed the model behavior across a spectrum of front-to-rear scenarios. Due to the stochasticity of the model (foremost in behavior prediction and policy sampling), for each of the 28 sets of initial conditions we ran the simulation of the front-to-rear scenario 32 times. Based on these simulations, we analyzed the model's chosen evasive maneuver, response time, and deceleration magnitude and compared it to human data reported in the driver behavior literature.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Front-to-rear scenario", "weight": 1.0} -->

Regarding brake response times, empirical studies have consistently found a strong dependence on scenario kinematics. Specifically, more kinematically urgent scenarios (e.g., with a small initial time gap and/or hard lead vehicle braking) lead to shorter response times while less urgent scenarios lead to longer response times, with approximately linear relationship between measures of urgency (e.g., the initial time gap) and mean response time. Our model produced behavior that is remarkably consistent with these findings (Figure 3d). Interestingly, compared to the evasive maneuver decisions, velocities do not seem to significantly influence brake response times, nor does the final chosen evasive behavior. Furthermore, model response times remain consistent (approx. $1\ s$) over the range of short time gaps ($0.5\ s$ to $1.5\ s$). This last result could be a consequence of the evidence accumulation mechanism requiring certain minimum time to trigger a re-plan even at a very high rate of incoming evidence. Relatedly, the lack of fast enough responses at short time gaps is a likely explanation for the collisions observed in the model (only at the shortest time gap of $0.5\ s$).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Front-to-rear scenario", "weight": 1.0} -->

However, because the data reported in the literature does not cover such short time gaps, this model prediction remains to be tested in future studies.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Front-to-rear scenario", "weight": 1.0} -->

While response selection and its timing are comprehensively characterized by the choice of evasive maneuver and response times, response execution is a dynamic process and can be characterized by a variety of metrics. Here we focus on deceleration magnitude, which has been previously shown to depend on the kinematics of the front-to-rear scenario: human drivers brake harder in more kinematically urgent scenarios. Our model captured this phenomenon: the magnitude of its braking increased with the inverse time-to-collision at brake onset (Figure 3e). This behavior of the model can be explained by the pragmatic value trade-off between avoiding a collision on the one hand and avoiding the effort of hard braking and losing velocity on the other hand. In other words, the model aimed to not brake harder than necessary to avoid collision.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Opposite-direction lateral incursion scenario", "weight": 1.0} -->

For evaluating model behavior in the opposite-direction lateral incursion scenario, we used human data from a driving simulator study at the University of Leeds, UK, reported by Johnson et al.. In this study, vehicles initially approached each other in opposite lanes when the computer-controlled vehicle unexpectedly steered toward the participant's lane along a predefined path. The study implemented three kinematic variants differing in incursion "steepness": a *steep* incursion crossing in front of the participant at a sharp angle and allowing a relatively easy escape by steering toward the opposite lane; a *medium* incursion at a shallower angle, heading directly toward the participant; a *shallow* incursion only partially entering the participant's lane, making it possible to find an escape path by steering slightly toward the shoulder (the original study used left-hand traffic, so we are here avoiding directional terms to prevent confusion).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Opposite-direction lateral incursion scenario", "weight": 1.0} -->

We re-implemented reversed (i.e., right-hand traffic) versions of these three conditions in our setup (see Supplementary Figure LABEL:fig:PL), enabling a direct comparison between human and model behavior under nearly identical conditions. Each of those three conditions was repeated 64 times.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Opposite-direction lateral incursion scenario", "weight": 1.0} -->

An example of our model implemented in the steep incursion condition is shown in Figure 4a, while Figure 4b shows an example of the medium incursion condition. When looking at the example simulations, we can observe again that the model needs multiple re-plans before deciding on the final avoidance maneuver. Compared to the front-to-rear scenario, where this is likely caused by the model's bounded planning capacity, in the lateral incursion scenario this is due to the high uncertainty inherent in the predicted positions of the encroaching vehicle (top panels). In Figure 4a (steep incursion), a first re-planning is triggered at $4.2\ s$ (first dashed line) but this does not significantly improve the collision component of the pragmatic value. Additionally, the model only initiates minor steering maneuvers and small accelerations/decelerations. Together, this suggests that the high uncertainty about the other vehicle's behavior prevents the agent from finding an evasive policy that is better (has lower EFE) than the current policy, instead delaying the decision, thus gaining time to see how the situation develops.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Opposite-direction lateral incursion scenario", "weight": 1.0} -->

With the collision risk unresolved after the first re-plan, surprise quickly accumulates toward a second re-plan at $4.8\ s$ (second dashed line). By this time, the agents are closer, allowing less space for uncertainty to grow and enabling the model to identify a steering policy that mitigates the collision risk (after the second re-plan, the collision component of the pragmatic value no longer significantly contributes to surprise accumulation). The decision to swerve toward the left is a result of both the other vehicle having crossed sufficiently over to the right side to leave a gap for swerving, and the model's stronger preference for moving into the opposite lane over leaving the road to the right (similar to Figure 1). However, it can be seen in Figure 4a that this trajectory is not optimal. Namely, as can be seen in the top plot, the planned trajectory ${\overset{\sim}{\mathbf{X}}}_{\text{ego}}$ chosen during the second re-plan at $t = {4.6\ s}$ (second dashed line) over-steers when returning to its own lane and consequently risks leaving the road.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Opposite-direction lateral incursion scenario", "weight": 1.0} -->

Thus, slight course corrections will likely be performed later (but this would occur outside the current simulation window).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Opposite-direction lateral incursion scenario", "weight": 1.0} -->

We compared our model to the human data collected in the driving simulator study by Johnson et al.. We closely replicated the scenarios of that study in our simulations (see Supplementary Information LABEL:sec:Oncmoing_dynamics), which allowed direct comparisons between the model and the data with respect to the chosen avoidance behavior and both braking and swerving response times (which were extracted using the same method as; see the Methods section). A key finding of Johnson et al. was that the participants' evasive maneuvering patterns and collision outcomes were strongly determined by the different scenario kinematics in the the three incursion scenarios. In the steep scenario, most participants avoided collisions by steering toward the opposite lane, while in the shallow scenario, participants typically steered toward the shoulder, passing the other vehicle on the "inside". However, in the medium scenario, the majority of participants collided with the oncoming vehicle. Since the urgency (i.e., time to collision at the initial steering of the oncoming vehicle) was constant across scenarios, the high collision rate in the medium case was attributed to greater uncertainty about the other vehicle's future path, leaving no clear escape route.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Opposite-direction lateral incursion scenario", "weight": 1.0} -->

As shown in Figure 4c, our model reproduced these results, reliably avoiding collisions in the steep and shallow scenarios through steering respectively left (toward the center) or right (toward the shoulder). Interestingly, the model also reproduced the human propensity for collision in the medium scenario. Johnson et al. suggested that, conceptually, a key reason why human drivers tended to collide in the medium incursion scenario is the high perceived uncertainty about the oncoming vehicle's future behavior which prevents the driver from finding a sufficiently certain escape path. As described above, the current model offers a detailed computational account for the possible mechanisms underlying this phenomenon: the wide spread (uncertainty) in the behavior predictions about the oncoming vehicle, as well as a bias towards expecting that it will return to its own lane due to the norm-conditioning of the beliefs, prevents the model to find an evasive policy in time to avoid collision (see Figure 4b above). An additional factor behind the observed collision rates was likely also the model's bounded planning capacity.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Opposite-direction lateral incursion scenario", "weight": 1.0} -->

Increasing the model's planning capacity -- by increasing the number of evaluated policies in the cross entropy method tenfold -- resulted in a significant drop in the model's collision rate (from 82.3% to 51.6% in the medium incursion scenario, and from 6.3% to 3.1% for shallow incursions, for further discussion see Supplementary Information LABEL:sec:CEM_parameters).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Opposite-direction lateral incursion scenario", "weight": 1.0} -->

Furthermore, Johnson et al. found that braking and steering response times -- measured from initiation of the incursion to the first reaction -- were generally long, ranging around $3.5\ s$ to $4.5\ s$. While braking response times did not vary noticeably with incursion level, steering response did decrease consistently from the steep towards the shallow scenario. Our model generally reproduced the range of response times, with closely matched median values (Figure 4d), but did not capture the variation in steering response times (especially for the shallow incursion, the model typically steered at least half a second later). One possible explanation may be that many participants avoided collision in the steep scenario primarily by braking before making a final steering adjustment, delaying their recorded steering response. In contrast, the model relied more on steering for collision avoidance, requiring an earlier response. The underlying reasons for these behavioral differences between the model and human drivers are still unclear but may have to do with varying individual preferences for braking versus swerving. Further work is needed to see if these individual differences can be reproduced by the model by varying its velocity, lane change, and lateral control effort preferences.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Intersection scenario", "weight": 1.0} -->

To test the ability of our model to generalize to more complex scenarios and to unseen data, we evaluated it in an intersection scenario against human data that was not used for tuning model parameters. Specifically, we used human response data obtained in a driving-simulator study conducted in Guelph, Canada, by Ziraldo et al. in the context of collision avoidance at intersections. This study implemented a right-turn-into-path scenario, where the participants approached an intersection with the right of way (green light). A computer-controlled vehicle then approached from the right side, on an intersecting road, and performed a right turn on red into the participant's lane. Right turns on red are allowed in US and Canada but the turning vehicle must yield; the participant's vehicle therefore had the right of way. Two variations of this scenario were implemented: In the right-turn-stopped (RS) scenario variant, the other vehicle initially waited at the stop line in front of the intersection and began to accelerate when the modeled agent's time-to-arrival was approximately $4\ s$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Intersection scenario", "weight": 1.0} -->

In the right-turn-not-stopped (RNS) scenario variant, the other vehicle was moving towards the intersection at a constant speed, and was controlled such that, under a constant-velocity assumption, it would cross the stop line when the modeled agent was roughly $1.5\ s$ from entering the intersection. In both scenarios, there was a parallel lane to the left of the modeled agent, allowing it to steer left to avoid a collision. A detailed version of our implementation of these scenario variants can be found in Supplementary Information LABEL:sec:intersection_setup. While Ziraldo et al. had each of their 52 participant face three of those scenarios, we only consider the first responses (26 per scenario type), as significant changes in response times and collision rates between repetitions indicated an anticipation of the conflict scenario. In total, we ran each of those scenario variants 96 times, varying the initial velocity of the modeled agent within the limits specified by Ziraldo et al..

<!-- chunk {"id": "body-0049", "role": "body", "section": "Intersection scenario", "weight": 1.0} -->

In the RS scenario (Figure 5a), after the other vehicle begins to accelerate at $t = {0.6\ s}$ (first dashed line), several time steps pass before the model considers the collision risk to be significant (as reflected in the collision penalty component of the pragmatic value). As evidence (i.e., surprise) thereafter gradually accumulates, the model reaches the re-planning threshold at $t = {3.4\ s}$, selecting a policy that combines braking with a leftward steering adjustment. However, as there is still considerable uncertainty about the other vehicle's future actions -- particularly since the other vehicle is already violating normative expectations by not yielding, reducing the bias introduced by norm conditioning -- the inferred collision risk decreases only slightly. This necessitates an additional re-planning step one second later (third dashed line). Shortly afterward, the ego vehicle passes the other vehicle, resolving the conflict.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Intersection scenario", "weight": 1.0} -->

In the RNS scenario (Figure 5b), the situation becomes critical earlier, as the other vehicle is approaching at constant speed. Since the vehicle does not exhibit any observable braking to yield at the stop line, as would be normatively expected, the model considers it increasingly likely that the other vehicle will encroach into its path. As a result, surprise accumulates based on the increasing collision likelihood. At $t = {1.6\ s}$ (first dashed line), the ego vehicle initiates braking and applies a slight leftward steering adjustment. However, this response is largely insufficient to reduce the collision risk (the collision component of the pragmatic value does not change substantially). While the model generally predicts the other agent to make a right turn, the high uncertainty in this prediction -- given the norm violations by the other vehicle, it is mostly based on kinematic likelihood -- leaves no clear safe escape path. The reaction is also too late for braking (although it is attempted) to prevent a collision.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Intersection scenario", "weight": 1.0} -->

Additional re-planning at $t = {2.4\ s}$ (second dashed line) likewise fails to avert the collision ($t = {3.4\ s}$). Had the model opted for a more extreme steering maneuver at the first re-planning point, it could have avoided the collision. However, in this specific simulation, the added pragmatic value of such an extreme maneuver was unclear at that point due to the high uncertainty about the other agent's future trajectory. Nevertheless, as the policy sampling process is stochastic, the model can occasionally opt for early steep steering and thus avoid collisions in this scenario.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Intersection scenario", "weight": 1.0} -->

Compared the model to human responses in the same scenario, we found that our model closely reproduced the main observations reported. As in the human data, the model successfully avoided most collisions in the RS scenario, but often collided in the RNS scenario (Figure 5c). The slightly lower collision rate of the model in the RNS scenario might be explained by the fact that in this scenario approximately ten percent of human participants collided without any noticeable reaction, which might indicate distraction effects that are not represented in our model. Next to collision rate distributions, our model reproduced the variation in human reaction times in the two scenarios (Figure 5d): responses in the more critical RNS scenario were markedly faster than in the RS scenario in both human data and model simulations. The model closely matched the timing of human responses in both conditions, with median reaction times generally not being apart more than $0.2\ s$. This is especially noteworthy, as it was achieved in an unseen scenario without any parameter tuning. This indicates that the model can generalize to new scenarios and can account for human data that was not used for parameter fitting/tuning.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Intersection scenario", "weight": 1.0} -->

While empirically, this generalizability is limited to interactions with a single target agent, given the strong support for the underlying model components in the literature, it can be hypothesized that the model's generalizability extends further, although this has to be evaluated in future work. Similar to the lateral incursion scenario (Figure 4d), the variances of model's reaction times are smaller compared to the human data. However, this is most likely simply a consequence of using a single model with fixed parameters for all simulations, thereby ignoring potential individual differences between human participants.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Evaluating individual model mechanisms", "weight": 1.0} -->

Comparison to the empirical data (Figures 3, 4, and 5) revealed that our model captured the key aspects of human collision avoidance performance in three different collision avoidance scenarios. To better understand which of the model mechanisms are essential for capturing the empirical observations, we evaluated the performance of seven simpler models which systematically excluded the key mechanisms one-by-one (Figure 6).

<!-- chunk {"id": "body-0055", "role": "body", "section": "Evaluating individual model mechanisms", "weight": 1.0} -->

Removing evidence accumulation. Without evidence accumulation, the model fully re-plans its policy at every time step. Consequently, it starts reacting to changes in the other vehicle's behavior immediately after detecting them. This resulted in a drastic reduction in response times across all scenarios (Figure 6b). Additionally, the model without evidence accumulation predominantly failed to avoid collisions in the shallow incursion scenario, contrasting sharply with human data and the full model. This was mostly caused by the model initiating braking very early. Given the uncertainty about the other vehicle, neither steering left nor steering right allows safe escape paths, so the agent continues braking, coming to a complete stop. At the point in time where the certainty about the other agent is low enough for safely choosing either left or right, the agent can physically no longer avoid a collision (as it cannot move laterally when stopped). An example simulation of this scenario can be found in the Supplementary Information as *Supplementary_Movie_7.mp4*.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Evaluating individual model mechanisms", "weight": 1.0} -->

The fact that collisions happened mostly in the shallow incursion scenarios is likely because in the medium and steep incursion scenarios, premature braking leaves enough space in front of the ego agent for the other vehicle to move across, which is not the case in the shallow incursion. In this scenario, a collision would still occur if the ego agent stayed in its starting lateral position, which makes braking an insufficient avoidance mechanism. Finally, in the intersection scenario, immediate reaction (including both braking and steering) allowed the reduced model to avoid all RNS collisions, in contrast to both the full model and the human data. Based on those observations, the inclusion of evidence accumulation is critical for accounting for empirical data on human response times in all three scenarios, evasive maneuver selection in the shallow lateral incursion scenario, and collision rates in the intersection scenario.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Evaluating individual model mechanisms", "weight": 1.0} -->

Removing added noise in behavior prediction. The model that uses deterministic predictions about the other vehicle produced response times in the front-to-rear scenario that are only slightly longer than for both the full model and the human data (Figure 6c), especially given shorter time-gaps. By contrast, in the opposite-direction lateral incursion and intersection scenarios, removing the noise led to substantially shorter response times. The reason for this apparent discrepancy is that in the front-to-rear scenario, prediction noise results in ego agent's believing that the other vehicle may brake more aggressively, prompting the model to react earlier. In the other scenarios, however, removing the prediction noise decreases the ego agent's uncertainty about the other vehicle, which enables it to find a safe escape path earlier, leading a faster response.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Evaluating individual model mechanisms", "weight": 1.0} -->

In the lateral incursion scenario specifically, this leads to earlier steering responses, which, given how these particular scenarios unfolded, turned out be a more effective avoidance strategy, as evidenced by the absence of collisions in this case. However, this strategy was only more effective after the fact (i.e., with hindsight of how the scenario played out). In another counterfactual scenario, where the oncoming vehicle turns back into its own lane early, swerving could instead result in a collision (see for a discussion of this important point). Prediction noise affected not only response times but also the model's choice of evasive maneuver in the lateral incursion scenario. In particular, the model with deterministic predictions predominantly opted to avoid the other vehicle by steering left regardless of the incursion profile. This allowed the model to avoid collisions in all simulations, but is not consistent with the human data.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Evaluating individual model mechanisms", "weight": 1.0} -->

Similarly, in the intersection scenario, this model ablation successfully avoided all collisions as well. Taken together, these findings underscore that behavior prediction noise is crucial for accurately reproducing human behavior, particularly in the lateral incursion and intersection scenarios. Specifically, uncertainty in the predictions of the other vehicle's actions seems to be a key explanation for why most human drivers ended up in a collision in the medium lateral incursion scenario and the RNS intersection scenario (as discussed above in relation to Figure 4b and Figure 5b, respectively).

<!-- chunk {"id": "body-0060", "role": "body", "section": "Evaluating individual model mechanisms", "weight": 1.0} -->

Removing pedal constraints. The model not constrained by pedal switching delays resulted in approximately $0.2\ s$ faster brake response times in all three scenarios compared to the full model (Figure 6d). This matches the delay of $0.2\ s$ implemented to represent the switch of the driver's foot from the gas pedal to the brake pedal. Although the effect appears simple and straightforward, the implemented pedal constraints are essential for capturing the differences between steering and braking response times observed in human behavior. For example, in the lateral incursion scenario, our model still slightly overestimates steering response times while underestimating braking response times, a discrepancy that could not be corrected by adjusting the surprise threshold for re-planning, as this would shift all response times uniformly.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Evaluating individual model mechanisms", "weight": 1.0} -->

Removing looming perception. We analyzed a version of the model which directly perceived kinematic variables without relying on looming (Figure 6e) as well as one which perceived looming but did not have a looming perception threshold (Figure 6f). In the front-to-rear scenario, both these models differed from the full model and the human data in that they produced faster brake response times at longer time gaps. For the model without the looming threshold, this is due to the fact that greater time gaps (and therefore greater distances) require a larger velocity difference to surpass the looming detection threshold, which delays responses, as it needs more time to accumulate. Furthermore, these results being very similar to the model that did not perceive looming at all (Figure 6e) indicates that in this scenario, the looming threshold was a key factor behind the ability of the model to capture human response times. Additionally, while not specifically analyzed here, this effect is expected to be exacerbated in high speed freeway scenarios where (given the higher speed) the following distances for a given time gap increase, further emphasizing the importance that the model accounts for this phenomenon.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Evaluating individual model mechanisms", "weight": 1.0} -->

In the other two scenarios, removing the looming threshold (or looming perception entirely) did not have any major effects, as the relevant observations in those scenarios are based on lateral movements.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Evaluating individual model mechanisms", "weight": 1.0} -->

In summary, models without either looming perception or looming threshold resulted in qualitative differences between the model and human data on brake response times in the front-to-rear scenario. In addition to the strong theoretical support, this highlights the importance of both looming-based perception and looming perception threshold for scenarios with largely longitudinal dynamics.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Evaluating individual model mechanisms", "weight": 1.0} -->

Removing the norm-conditioned particle filter. Without the norm-conditioned particle filter, the model behavior in the front-to-rear scenario changes only slightly compared to the full model (Figure 6g), showing marginally longer response times. In the lateral incursion scenario, however, the effect is more pronounced, with collisions being less likely in the medium incursion (avoided by leftward steering) and more likely in the shallow incursion. Relative to the full model, this ablation lacks the bias against predicting steeper incursions earlier, which incentivizes steering towards the left. This yields a small advantage in the medium incursion scenario, where avoiding towards the other vehicles lane is typically effective, but increases collision risk in the shallow incursion, where both the full model and humans consider rightward avoidance the better option. Additionally, the ablated model also shows slightly longer reaction times in the lateral incursion scenario. This again follows from the lack of norm conditioning, as without it, the model often predicts that the other vehicle will leave the road before posing a collision risk, whereas the full model -- biased by the normative filter -- believes the other vehicle will stay in its lane.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Evaluating individual model mechanisms", "weight": 1.0} -->

Consequently, in this ablation, with the predicted collision likelihood being lower, surprise accumulates more slowly, and the re-planning threshold is reached later, leading to a slower reaction. In the intersection scenario, removing the norm-conditioned particle filter leads to both faster reaction times and a successful resolution of the conflict in nearly every instance. This is logical, as the expectation that the other vehicle would stop to yield resulted in delayed reaction. Without this bias, potential collisions are taken more seriously and reacted to earlier.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Evaluating individual model mechanisms", "weight": 1.0} -->

While these differences already highlight the importance of the norm-conditioned particle filter, it has the strongest impact in benign (non-conflict) scenarios. In such scenarios, the model with the simple kinematics-based behavior prediction mechanism is unrealistically conservative due to having to plan for all kinematically possible futures of the other vehicle --- a problem that is avoided by the model with norm-conditioned particle filter (see Supplementary Information LABEL:sec:Benign for an example).

<!-- chunk {"id": "body-0067", "role": "body", "section": "Evaluating individual model mechanisms", "weight": 1.0} -->

Removing the epistemic component of EFE. Lastly, we investigated a model variant that ignored the epistemic value when selecting policies. This ablation, with the exception of the reaction times in the front-to-rear scenario, did not result in any significant differences in the model behavior, both in the actual outcome and the derived goodness-of-fit metrics. Consequently, it can be argued that the EFE part of our model could potentially be reduced to pragmatic value alone, which would make the model conceptually similar to a belief-space model predictive control. Nevertheless, the epistemic value does play a role in scenarios where, for instance, observability is limited; there, epistemic value has substantial effect on model behavior (Supplementary Information LABEL:sec:Epistemic). This complements the previous investigations of the role of epistemic value in scenarios requiring visual behavior. For these reasons, we treat the version of the model with epistemic value as the "full" model here to allow for generalization to similar scenarios in the future.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Evaluating individual model mechanisms", "weight": 1.0} -->

Additionally, in the lateral incursion scenario, we examined the impact of our model's bounded reasoning capacity. Specifically, as noted above, increasing the number of policies evaluated during replanning led to a substantial reduction in observed collision rates---ranging from roughly one-third to one-half across scenarios. This suggests that bounded reasoning is a crucial component for accurately modeling human collision-avoidance failures. However, since not all collisions were avoided, other factor (namely, prediction uncertainty and the expectation of norm-compliant behavior) also play a significant role in driving such outcomes.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Evaluating individual model mechanisms", "weight": 1.0} -->

Overall, the seven ablated model variants analyzed above show qualitative differences compared to the full model, and none reproduce human behavior across all three scenarios as well as the full model. This provides further evidence for the importance of all the analyzed model mechanisms in regard to capturing human collision avoidance behavior.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Discussion", "weight": 1.5} -->

Building on previous work, we here presented an active inference-based framework for modeling human collision avoidance behavior based on first principles. To our knowledge, this is the first published computational model that offers a detailed account of human collision avoidance behavior across multiple conflict scenarios. Our model reproduces many key results in the rich literature on collision avoidance in front-to-rear scenarios, in particular the dependence of response times and braking magnitude on scenario kinematics. The model also generated several detailed predictions on how evasive maneuver decisions (braking vs. swerving) vary with scenario kinematics which can be tested in future experiments. Furthermore, we compared the model to detailed human behavior data in an opposite-direction lateral incursion scenario with varying kinematics and an intersection scenario with with a right-turning vehicle failing to yield the right of way, both obtained in driving simulator studies. This analysis demonstrated that the model can reproduce human evasive maneuver decisions, collision outcomes, as well as response times in different variations of these two scenarios. The model also shows strong generalization across scenarios, with the model tuned solely on the front-to-rear and lateral incursion scenario making accurate predictions of human responses in the intersection scenario.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Discussion", "weight": 1.5} -->

A key feature of our proposed model is its ability to flexibly represent closed-loop collision avoidance through dynamic re-planning of policies, including braking, steering, and accelerating actions, in a way that is qualitatively and quantitatively similar to human collision avoidance behavior. In contrast, existing publicly available collision avoidance models either implement a "one-shot", often predetermined, open-loop evasive maneuver or limited aspects of closed-loop control, such as intermittent braking but no steering. Some commercially available models -- the Stochastic Cognitive Model (SCM) from BMW and the driveBOT model from cogniBIT -- reportedly implement human-like closed-loop behavior in collision avoidance scenarios. However, although the SCM is openly available, the published evaluations provide only a limited basis for meaningful comparison. For instance, Fries et al. evaluates SCM on only a few collision-avoidance cases and compares mainly velocity-over-time profiles, without a systematic analysis of diverse metrics across scenario variations. For driveBOT, the evaluations are more comprehensive, but the lack of available information on the detailed working principles of the model precludes a meaningful comparison with our work.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our model achieves closed-loop behavior by continuously evaluating evasive policies based on their expected free energy, pursuing the policy with the lowest EFE, and allowing for further re-planning if the chosen policy turns out to not yield the preferred (and hence expected) outcomes (e.g., due to limited planning accuracy or unexpected changes in how the scenario unfolds). This, in effect, implements a constraint satisfaction mechanism where different model preferences are traded against each other in finding the policy with the highest overall combined pragmatic value and epistemic value. We observed several examples of this (Figures 3) where, for example, the model generally prefers to brake at low speeds (since the loss related to the preferred speed is not as high as the cost of changing lane) and swerve at higher speeds (where the cost of braking in terms of speed loss are higher). This yields detailed predictions of human behaviors in different kinematic situations that could be further tested empirically.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Discussion", "weight": 1.5} -->

Another important aspect of our model is its ability to dynamically account for uncertainty about the future behavior of other agents. This is particularly important in situations like the lateral incursion scenario and the intersection scenario. For instance, in the former, the driver cannot determine *a priori* if the other vehicle will continue crossing the ego vehicle's lane or if it will turn back to its original lane, resulting in a wide range of potential future trajectories of the other vehicle. However, the uncertainty may be reduced as the scenario unfolds, opening up new available escape paths, or *escape affordances*, as was the case in the current steep and shallow incursion scenarios. In such cases, an evasive response that is initiated too early may be premature (and non-optimal) and does not properly reflect human behavior. We saw an example of this in Figure 6c, where in both the lateral incursion and intersection scenario the model without prediction noise responded much faster than humans and the full model, thus avoiding collision in all cases.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Discussion", "weight": 1.5} -->

However, such overconfident evasive maneuvering behavior could be detrimental in other scenarios, for instance if in our lateral incursion scenario the other vehicle would turn back into its original lane. By representing the uncertainty about the other vehicle's future positions using a vehicle dynamics (bicycle) model and a noisy particle filter, our model is able to handle such situations and successfully reproduce human behavior.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Discussion", "weight": 1.5} -->

Furthermore, in particular the intersection scenario showed that it is also important that such noisy predictions are biased towards norm-compliant behavior (Figure 6g). Specifically, without the prior expectation that other vehicle will follow established rules and norms such as yielding the right of way, the model will predict potential collision scenarios earlier, react faster and resolve the conflict safely. However, in many situations this leads to overreactive non-human like collision avoidance behavior. We also demonstrated that the *norm-conditioned particle filter* is necessary to avoid overly conservative (and therefore non-human like) behavior in non-conflict driving scenarios (Supplementary Information LABEL:sec:Benign).

<!-- chunk {"id": "body-0076", "role": "body", "section": "Discussion", "weight": 1.5} -->

In the collision avoidance scenarios simulated in the present study, there is little opportunity for the driver to reduce the uncertainty about the oncoming vehicle's future trajectory through epistemic actions. In other words, there is little the driver can do to obtain further information that could help predict what the other vehicle will do. Thus, as expected, disabling the epistemic value component of the EFE did not significantly change the model behavior. However, as shown in Supplementary Information LABEL:sec:Epistemic and previous work, the epistemic value component in our model does drive policy selection in traffic scenarios with epistemic affordances, that is, situations with opportunities for actions yielding information that may resolve uncertainty. Hence, even if the epistemic value did not have any significant effect on policy selection in the present study, it should still be considered a key aspect of human road user behavior. In particular, in the real world communicative acts such as honking, flashing headlights or initially moving to the right in the lane could reduce uncertainty about the other vehicle driver's intent. Since other agents were here assumed to be non-reactive, such aspects were not addressed in the current work; this is a topic for future development of the model.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Discussion", "weight": 1.5} -->

While active inference models can be implemented computationally in many different ways, we used a stochastic receding-horizon control architecture as the basis for the implementation, following. This shares similarities with prior work in robotics, particularly decision-theoretic approaches that explicitly account for uncertainty in actuation and sensing by propagating belief states into the future, often using particle-based representations, and then selecting actions that optimize expected outcomes based on this projected belief evolution. However, our work diverges from these engineering models in two crucial aspects. First, since our goal is to represent human driver behavior rather than designing a robot/vehicle controller, the modeling focuses on capturing key aspects of human driving, such as response timing and evasive maneuver decision making, rather than optimizing performance based on engineering criteria. Second, our modeled agent minimizes EFE (as prescribed by the active inference framework), while traditional state-based reward functions often employed in the control literature lack such a theoretically-grounded objective derived from first principles.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our model incorporates an explicit mechanism for evidence accumulation to account for human response timing, based on existing models. Evidence accumulation models naturally account for the situation-dependency of response timing in traffic situations: the faster a traffic conflict escalates, the faster the human's response to it. Compared to existing evidence accumulation models, our model introduces some key novel aspects. In particular, in contrast to traditional models that accumulate perceptual evidence (e.g., looming ), our model rather accumulates surprise. Similar ideas have been explored in existing models, based on the notion that a traffic conflict by definition is an extremely rare (and hence surprising) event which always takes place against a "default" expectation of how the situation would normally play out (Figure 1). This is also the key idea behind the NIEON (Non-Impaired driver with their Eyes ON the conflict) response time model which conceptualizes the onset of the stimulus that human drivers respond to in a traffic conflict as the onset of surprise (i.e., the violation of the initial default expectation). The current model generalizes this idea in several ways.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Discussion", "weight": 1.5} -->

First, instead of triggering a predefined action such as braking when the surprising evidence has reached the threshold, the evidence accumulation here triggers the *re-planning* of a new policy, using the EFE-based policy selection mechanism discussed above. Second, the surprise signal that is being accumulated is not just the difference between a predicted and actual signal but rather the negative pragmatic value of the current policy, that is, how "bad" the currently selected default policy is relative to the agent's preferred observations. This provides a straightforward solution to the known problem of how to determine whether a given surprise signal is relevant to the agent.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Discussion", "weight": 1.5} -->

Importantly, our model accumulates surprise deterministically without accumulation noise. Under this assumption, the accumulation rate can be expressed in units of the decision boundary (another key parameter traditionally important in the evidence accumulation literature, interpreted as response caution) and hence we did not need to define a separate decision boundary. Nevertheless, adding such accumulation noise could be seen a future improvement of our model if we want to better match the high variance observed in human reaction times (Figure 4d and Figure 5d). Similarly, the addition of surprise decay could also be considered.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Discussion", "weight": 1.5} -->

While we here model evidence accumulation explicitly, it can in principle be seen as an implicit feature of active inference. However, in practice, it is challenging to accurately represent human response dynamics implicitly in a simplified model like ours. To enable straightforward tuning of the model's response performance to human data, we chose the current explicit modeling of evidence accumulation. As demonstrated by our simulation results (Figure 6b), the inclusion of this mechanism is essential to account for realistic response times in our model.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Discussion", "weight": 1.5} -->

The current model is based on the general model predictive control architecture originally developed for the model of routine driving described in which, in turn, is based on the standard discrete-time active inference EFE model for planning agents formulated as a partially observable Markov decision process. The original routine driving model in focused primarily on the role of epistemic value in resolving uncertainty when driving around visual occlusions and during visual time sharing (drawing from the rat-in-a-T-maze example in ). However, that model was not aimed at describing time-critical behaviors. For instance, in collision avoidance scenarios its responses to sudden stimuli would be overly fast, similar to the version of our model without evidence accumulation (Figure 6b). Extending the original model with not only evidence accumulation, but also other mechanisms such as looming-based perception and norm-conditioned predictions was essential for capturing human collision avoidance behavior (Figure 6). Otherwise, the model we reported here retains the key features of the original routine driving model needed for dealing with uncertainty resolution through epistemic action, thus offering a powerful and general computational framework for modeling driving behavior, also beyond collision avoidance.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Discussion", "weight": 1.5} -->

As, we employed engineering tools like the cross-entropy method and particle filters with discrete and continuous variables. However, while relying on such established methods, our model does not reduce to a combination of them; instead, these methods serve as means for implementing specific cognitive mechanisms within our active inference framework.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our framework is grounded not only in active inference and the free energy principle, but also enactivist approaches to cognitive science. Active inference and enactivist cognitive science share the the foundational notion that behavior in biological agents results from a self-organizing process geared towards sustaining the agent's integrity (existence) over time. This emphasizes a strong continuity between life and mind and offers a natural solution to the problem how the certain aspects of the environment become meaningful and relevant to an agent. Such an existential imperative can be described as the organism striving to maintain itself in a sparse attractive set of preferred agent-environment states, where the attractive set depends on the specific organism in question. Thus, to survive over time, a fish needs to remain in water with the right chemical balance and temperature range, obtain food, avoid being eaten by certain predators etc. This implies that these particular states are meaningful and relevant to the fish which then acts in order to observe these states with a high degree of certainty, thus looking as if it is minimizing free energy over time.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Discussion", "weight": 1.5} -->

By the same token, we endowed our model with a (highly simplified) set of preferred states that are meaningful and relevant to a human car driver (avoid danger of collision, stay on the road, keep up progress, avoid too harsh braking/steering) and defined the model such that it acts (selects and executes policies) in a way that maximizes the chance of observing these preferred states.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Discussion", "weight": 1.5} -->

Related to this, our model also offers a operationalization of the classical notion of *affordance*, traditionally broadly defined by Gibson as what the environment "offers the animal, what it provides or furnishes, either for good or ill" (p. 127). Thus, when our model identifies candidate evasive policies associated with low EFE, these can be understood as affordances in the sense of opportunities for actions that are worth pursuing. The active inference framework offers a further distinction between *pragmatic affordances* yielding unsurprising, familiar and preferred observations and *epistemic affordances* yielding information that can resolve uncertainty about pragmatic affordances (see ) for a further discussion about this expanded notion of affordances and its relation to the classical affordance concept in ecological psychology).

<!-- chunk {"id": "body-0087", "role": "body", "section": "Discussion", "weight": 1.5} -->

Thanks to generality of active inference, models based on it have been developed for virtually every facet of biologically-based cognition and behavior, in organisms ranging from single cells, plants, individual animals and humans to social and cultural phenomena, which provides a great source of concepts and ideas for modeling different aspects of human road user behavior. Thus, importantly, we see active inference not just as a computational approach to model development, but as a general theoretical framework for understanding road user behavior that can guide modeling at a conceptual level and generate hypotheses for experimental studies. At the same time, the great majority of existing active inference models use relatively simple toy scenarios, thereby limiting its applicability to real-world human behavior. By operationalizing active inference in the context of a dynamically rich task, that is, collision avoidance and evaluating it against human data from both simulated and real-world driving, this study pushes the boundaries of active inference applications toward the modeling of complex human naturalistic behaviors.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Discussion", "weight": 1.5} -->

While, as discussed above, our model represents a significant advancement in human collision avoidance modeling, it has several limitations that can be addressed in future work. First, in this work we essentially hand-tuned the model parameters to fit the human data from the two collision avoidance scenarios. Whereas this highlights the model's generalizability and interpretability, especially considering its good performance on the third (intersection) scenario not used for tuning, such an approach is impractical at scale. Future research should explore systematic parameter optimization methods, for example using the approach suggested by Wei et al..

<!-- chunk {"id": "body-0089", "role": "body", "section": "Discussion", "weight": 1.5} -->

Second, the current model assumes that other agents are non-reactive (i.e., in the generative model's state transition function, other agents' states are independent from each other and the ego agent). This assumption therefore limits the model to scenarios where interactions are only weakly linked, and is unlikely to hold in the general case. For example, norms about priority -- such as at unsignalized intersection -- are generally interactive, with one agent's norm compliance depending on the other agents' behavior. Thus, future work should extend the model to include reactive agents by implementing interactive norms and communicative or epistemic actions that allow agents to probe or signal intentions. Such extensions would strengthen the model's applicability and allow simulations of multi-agent interactions under active inference. Moreover, the current model (as well as the original routine driving model in ) only reasons at a shallow "unsophisticated" level about how actions bring about future observations with varying degrees of uncertainty. Further work could explore the possibilities of incorporating *sophisticated inference*, which enables "deeper" levels of recursive reasoning about how future observations would lead to updated beliefs and corresponding new actions.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Discussion", "weight": 1.5} -->

This may be particularly relevant when modeling interactions between road users.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Discussion", "weight": 1.5} -->

Third, the model currently only accounts for perceptual limitations in terms of visual angle and looming. However, looming only represents the relative motion of objects moving longitudinally towards the observer and, strictly speaking, only applies to objects located along a straight path of travel relative to the gaze direction of the observer (in our case, this means objects located straight ahead of the ego vehicle). Thus, additional perceptual variables are needed to represent perceptual thresholds on the detection of perpendicular motion (e.g., a pedestrian moving into the street ahead) or representing relative motion of objects that are otherwise perpendicular from the observer's gaze and heading direction. In addition, the perceptual effects of environmental and stimulus-related factors such as weather (e.g., reduced visibility due to fog, heavy rain or snow), lighting conditions (daylight, dusk, night, effects of headlights etc.), glare and stimulus conspicuity would ideally need to be accounted.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Discussion", "weight": 1.5} -->

Another way in which the model's perceptual fidelity could be improved is by explicitly modeling the human field of view, including the different functional properties of foveal versus peripheral vision which can be combined with the visual behavior model outlined in the original model.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Discussion", "weight": 1.5} -->

Beyond perceptual limitations, the use of more realistic perceptual variables such as the optically specified longitudinal time-to-collision ($\tau$ in ), bearing angle (specifying perpendicular collision course ) and global optic flow rate or edge rate (specifying self motion relative to the ground ) could be further explored. This would allow for defining observation and state spaces in the model which are more aligned with the ecological information available to human drivers.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Discussion", "weight": 1.5} -->

Fourth, while mechanisms for dealing with partial observability during occlusions and visual time sharing were explored, further work is needed to develop more comprehensive solutions for representing and reasoning about multiple agents hidden behind occluding objects or appearing outside the driver's field of view (see also Wei et al. ); this could help translate the model to more complex and crowded conflict scenarios.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Discussion", "weight": 1.5} -->

Fifth, the model's generalizability beyond the presented scenarios from the Anglo-American cultural context has not been evaluated. Three types of assumptions are especially noteworthy: the low-level control assumption that drivers use the same foot for acceleration and braking, the higher-level assumptions about other peoples behavior encoded in normative likelihoods (for example, the different rules regarding right turns on red light in North America and Europe), and the own preferences defining acceptable behavior (such as infringing on other agents' lanes). As those assumptions are subject to cultural influences, they may not transfer seamlessly to other regions of the world. A future model could be made more robust by making such assumptions explicit and learnable (e.g., by modeling them as additional latent (belief) states or context variables dependent on a country).

<!-- chunk {"id": "body-0096", "role": "body", "section": "Discussion", "weight": 1.5} -->

Finally, while the current policy sampling and kinematic-based particle filter approach were demonstrated to work well in the current scenarios, this could be a limiting factor in scaling the model to a wider range of scenarios, especially when modeling pre-conflict scenarios with more complex road infrastructures and road user interactions. To overcome this limitation, machine-learning-based data-driven models could be leveraged to generate possible futures in our generative model's state transition function, either stand-alone or in combination with the current kinematics-based predictions, thus potentially further enhancing the generalizability of the model. In principle, such data-driven models, if employed in a closed-loop manner, could potentially serve as an alternative to our proposed active inference model in its entirety, given their clear advantages in inference time -- no expensive policy selection process is needed -- as well as their superior ability to learn from large human datasets in complex geometric environments. These characteristics, after all, allowed those models to show remarkable, and increasing accuracy in the prediction of routine driving behavior. However, research on evaluating such models in collision avoidance scenarios is lacking.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Discussion", "weight": 1.5} -->

To understand their current capabilities, we tested one of the state-of-the-art machine-learned models (ADAPT ) in the lateral-incursion scenario (Supplementary Information LABEL:sec:Oncoming_ML). We found that the data-driven model did not capture human behavior well, likely due to simplistic learning objectives and under-representation of critical scenarios in the training data. Furthermore, the black-box nature of such models restricts them to an exclusively descriptive/predictive role, without providing insight into the underlying cognitive mechanisms driving human behavior.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Discussion", "weight": 1.5} -->

Overall, our work contributes to the recent body of research with new evidence that active inference can serve as a general framework for computational road user modeling. Along with the emerging real-world applications of active inference in robotics and artificial intelligence, this work can aid in the development of agents used for the simulation-based evaluation of advanced driver assistance systems and automated vehicles.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Model principles", "weight": 1.0} -->

Our model follows the architecture of the original model initially formulated by Engström et al., and combines some of the original elements of that model with multiple new mechanisms. In particular, our model retains the representation of probabilistic beliefs using sets of samples and the correspondingly sample-based estimation of the expected free energy (see equation ) as well as the cross entropy method used for policy selection. In addition to these mechanisms, we introduced looming perception, evidence accumulation, the norm-conditioned particle filter, and the constraints on acceleration profiles (see Figure 6 for the analysis of the impact of these new mechanisms on model behavior). We also modified the Bayesian belief update (equation ) and the calculation of the epistemic value (equation ).

<!-- chunk {"id": "body-0100", "role": "body", "section": "Model principles", "weight": 1.0} -->

In our active inference model, the environment is represented by the *generative process*, with a state of the world ${\mathbf{η}} \in \mathcal{E}$ which is partially observable by the agent. The agent can influence the environment with its actions ${\mathbf{a}} \in \mathcal{A}$ (according to the state transition probability $\hat{p}{(\left. {\mathbf{η}}^{\prime} \middle| {{\mathbf{η}},{\mathbf{a}}} \right.)}$), resulting in observations ${\mathbf{o}} \in \mathcal{O}$, whose dependence on the world state is described in $\hat{p}{(\left. {\mathbf{o}} \middle| {\mathbf{η}} \right.)}$ (the $\hat{p}$ is used to show these function be part of the *generative process*).

<!-- chunk {"id": "body-0101", "role": "body", "section": "Model principles", "weight": 1.0} -->

The agent has an internal model of the world, the *generative model*, with the corresponding partially observable state ${\mathbf{s}} \in \mathcal{S}$, and the corresponding state transition function $p{(\left. {\mathbf{s}}^{\prime} \middle| {{\mathbf{s}},{\mathbf{a}}} \right.)}$ and observation probability $p{(\left. {\mathbf{o}} \middle| {\mathbf{s}} \right.)}$. As the *generative model* is an abstraction of the real world described by the *generative process*, $\mathbf{η}$ and $\mathbf{s}$ do not necessarily have to represent the same state spaces ($\mathcal{E} \neq \mathcal{S}$).

<!-- chunk {"id": "body-0102", "role": "body", "section": "Model principles", "weight": 1.0} -->

The agent is uncertain about the state of the generative model, represented by the probability density function $q{({\mathbf{s}})}$ (referred to as the agent's belief about the state $\mathbf{s}$). Following, in our model the agent represents its belief distributions $q{({\mathbf{s}})}$ in a non-parametric way as a set of $N$ samples ${\mathbf{S}} = {\{{\mathbf{s}}_{1},\ldots,{\mathbf{s}}_{N}\}}$ (i.e., a particle filter).

<!-- chunk {"id": "body-0103", "role": "body", "section": "Model principles", "weight": 1.0} -->

The agent then tries to minimize its free energy, both in the belief $q{({\mathbf{s}})}$ it forms (*variational free energy*) and the actions $\mathbf{a}$ it chooses (*expected free energy*). The action and policy selection is based on the existence of a preference prior $p{({\mathbf{o}})}$ depicting preferred observations.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Perception", "weight": 1.0} -->

The agent's visual perception in our model is based on looming (Supplementary Information LABEL:sec:Looming) -- the optical information immediately available to humans about the relative motion of objects straight ahead in the direction of travel. Specifically, the relative position and motion of objects along the forward path of the agent is perceived in terms of the visual angle $\varphi$ subtended by the object at the retina of the observer, and its derivative, the angular rate $\overset{˙}{\varphi}$ (looming). Due to the nonlinear relationship between the observer's distance to the observed vehicle (in Figure 2a referred to as $\Deltax$) and $\varphi$ (with increasing distances, equal variations $\delta\Deltax$ lead to increasingly smaller $\delta\varphi$), perception errors for $\varphi$ and $\overset{˙}{\varphi}$ will lead, respectively, to increasing inference errors and therefore uncertainty about the position and speed of the leading other vehicle at increasing distances. We represent this aspect in the model by setting the noise in $p{(\left.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Perception", "weight": 1.0} -->

{\mathbf{o}} \middle| {\mathbf{s}} \right.)}$ to be constant across $\varphi$ and its derivatives.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Perception", "weight": 1.0} -->

At a certain distance, $\overset{˙}{\varphi}$ is no longer perceptible to the human eye, which implies a minimal threshold for looming detection. To account for this, the model incorporates a detection threshold on $\overset{˙}{\varphi}$ (i.e., for small $|\overset{˙}{\varphi}|$, the means of the observation probabilities $p{(\left. {\mathbf{o}} \middle| {\mathbf{s}} \right.)}$ for velocities and acceleration were set to the values corresponding to $\overset{˙}{\varphi} = 0$). This means that changes in the other vehicle's velocity cannot be perceived by a human driver beyond a certain distance, resulting for example in a delayed recognition if the lead vehicle suddenly brakes.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Behavior prediction", "weight": 1.0} -->

This belief propagation scheme represents *unsophisticated inference* in the technical sense that it does not condition the beliefs about future states on corresponding counterfactual observations. While it would theoretically be possible to use a form of *sophisticated inference* that accounts for such conditioning, we here used the unsophisticated approach for simplicity, similar to the original model and most existing active inference models.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Behavior prediction", "weight": 1.0} -->

Importantly, our state transition function $p{(\left. {\mathbf{s}}^{\prime} \middle| {{\mathbf{s}},{\mathbf{a}}} \right.)}$ function is composed out of two parts, with

<!-- chunk {"id": "body-0109", "role": "body", "section": "Behavior prediction", "weight": 1.0} -->

Here, $p_{o}{(\left. {\mathbf{s}}^{\prime} \middle| {{\mathbf{s}},{\mathbf{a}}} \right.)}$ is the standard kinematic likelihood function (as used in ), while the *projected normative probability* ${\breve{p}}_{\text{n}}{({\mathbf{s}}^{\prime})}$ biases the agent to predict future states which currently, and over the near future, are aligned with the norm-compliant behavior of other vehicles. This represents the human tendency to avoid overly pessimistic predictions about the behavior of other traffic participants by instead assuming that they will adhere to road rules and other established traffic norms; for example, assuming that oncoming vehicles will stay in their lane or yield the right of way, without evidence to the contrary, is necessary for fluent driving.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Behavior prediction", "weight": 1.0} -->

applying the *normative probability* $p_{\text{n}}$ to the current time as well as short- and medium-term predictions $\breve{\mathbf{s}}$ ($H_{n}$ is setting the medium-term prediction horizon) to evaluate their norm compliance. This ensures that the model's predictions are not only biased against actions which lead to immediate norm violations, but also against those that put the other vehicle into a position where norm compliance becomes kinematically less likely over time (e.g., initiating a turn while in a straight lane does not immediately lead to the vehicle leaving the road, but might put the vehicle in a position where staying on the road becomes kinematically impossible). Crucially, the use of the current norm-compliance as an upper bound ensures that once norm-violating behavior is observed, the model no longer places trust into norms as a way of constraining predictions about other agents' behavior. In collision avoidance scenarios initiated by the unexpected, norm-violating behavior of other agents, this allows the model to account for all kinematically possible but low-probability "extreme" (long-tail) behaviors.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Behavior prediction", "weight": 1.0} -->

This approach -- which we call *norm-conditioned particle filter* -- helps aligning the model's predictions with realistic driving scenarios while accounting for norm violations when necessary. Even though the norms relevant for our studied scenarios (lane following, yielding the right of way) could in general be implemented globally based on map information (for example a detailed graph), for simplicity and computational efficiency we chose to implement in each scenario only those norms that are relevant to that scenario (Supplementary Information LABEL:sec:Normative_Belief_F2R, LABEL:sec:Normative_Belief_ODLI and LABEL:sec:Normative_Belief_Intersection; see also Supplementary Information LABEL:sec:state_transition for details on sampling from $p{(\left. {\mathbf{s}}^{\prime} \middle| {{\mathbf{s}},{\mathbf{a}}} \right.)}$).

<!-- chunk {"id": "body-0112", "role": "body", "section": "Policy sampling", "weight": 1.0} -->

Based on the predicted behavior of the other vehicle, the agent selects its policy $\mathbf{π}$. Here, policies are defined as sequences of $H$ future actions; following the bicycle model, the actions are defined in terms of acceleration $a_{\text{long}}$ and steering rate $\omega$. These actions are selected using the cross-entropy method, which iteratively resamples sets of $M$ candidate policies $K$ times, where the resampling focuses around the subset of the $\betaM$ best samples from the previous iteration. Specifically, the agent takes the mean and variance of this promising subset (ignoring potential correlations), and then samples a new set with size $M$ from the corresponding normal distribution. In contrast to the original model that randomly picked the final sampling output from the last iteration's set, here we specifically choose the best sample.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Policy sampling", "weight": 1.0} -->

To better represent human behavior, the model incorporates a pedal constraint to filter out unrealistic changes in acceleration (Supplementary Information LABEL:sec:Control_limits). As human drivers generally control acceleration by operating the brake and gas pedal with a single foot and cannot move the foot between pedals instantaneously, the model imposes a constant holding time interval of $0.2\ s$ at $a_{0} \lesssim {0\ {ms}^{- 2}}$ (similar to ), such that if the model transitions from a current acceleration $a_{\text{long}} > a_{0}$ to a target acceleration $a_{\text{long},f} < a_{0}$, it must first decelerate to $a_{0}$, maintain that value for $0.2\ s$, and then proceed to $a_{\text{long},f}$. The same applies for acceleration changes in the other direction.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Policy roll-out and evaluation", "weight": 1.0} -->

To evaluate a policy $\pi$, the agent first uses the bicycle model to roll out its possible future states based on $\mathbf{π}$. In the general case, the possible future states of the agent and the other vehicle are coupled, hence the agent rolls out its policies jointly with the predicted futures of the other vehicle. For the reason of simplicity, however, our model assumes that in $p{(\left. {\mathbf{s}}^{\prime} \middle| {{\mathbf{s}},{\mathbf{a}}} \right.)}$ the other vehicle is unresponsive to the actions of the ego vehicle, allowing us to separate behavior prediction and policy roll-outs.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Policy roll-out and evaluation", "weight": 1.0} -->

Active inference then rests on the fundamental assumption that an agent prefers policies which minimize its expected free energy (EFE) $G$ over the prediction horizon of $H$ time steps; in other words, the best policy is the one with the lowest EFE.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Policy roll-out and evaluation", "weight": 1.0} -->

The pragmatic values $g_{\text{pragm}}$ is defined as

<!-- chunk {"id": "body-0117", "role": "body", "section": "Policy roll-out and evaluation", "weight": 1.0} -->

while we use the Shannon entropy $\mathcal{H}$ to calculate the epistemic value

<!-- chunk {"id": "body-0118", "role": "body", "section": "Policy roll-out and evaluation", "weight": 1.0} -->

The first term in Equation is known as the *posterior predictive entropy* and represents the extent to which a policy is expected to yield a variety of different observations. The second term, known as *expected ambiguity* represents the diversity of observations expected for a given state, that is, the extent to which the observations of that state are unreliable (e.g., due to reduced visibility).

<!-- chunk {"id": "body-0119", "role": "body", "section": "Policy roll-out and evaluation", "weight": 1.0} -->

When evaluating the pragmatic value, we assume that the preference (i.e. the distribution of desired observations) $p{({\mathbf{o}})}$ accounts for four aspects of the agent's objective: a) to maintain its desired longitudinal velocity, b) to minimize the magnitude of control inputs, c) to remain on the road and within its current lane (e.g., avoiding lane markers or opposite lanes), d) prevent collisions, and e) avoiding hazardous situations.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Policy roll-out and evaluation", "weight": 1.0} -->

For $p_{\text{safe}}{({\mathbf{o}})}$, the model specifically seeks to avoid states where, under the assumption that the other vehicle begins braking suddenly with a deceleration of $a_{\text{OV},\min}$, the ego vehicle would fail to avoid a collision despite initiating maximum braking after a response time of $1\ s$.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Surprise-based re-planning", "weight": 1.0} -->

Our model assumes that on every time step, the agent performs planning incrementally, unless it observes a surprising event, in which case it re-plans the full policy. Practically, on every time step the agent takes the policy chosen in the previous time step, disregards its first action (as it was already executed) and assumes that the remaining actions constitute all but the last actions of the new policy. The above policy selection mechanism is then used to generate the last action of the new policy.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Surprise-based re-planning", "weight": 1.0} -->

Traditionally in evidence accumulation literature, the accumulation rate is referred to as drift rate, which is interpreted as the quality of the incoming evidence and can be linked to the decision-maker's efficiency of processing the perceptual information. Here, we follow Engström et al.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Surprise-based re-planning", "weight": 1.0} -->

Under this definition, the surprise is the difference between the highest pragmatic value possible and the actual pragmatic value of a policy. For instance, if a policy would result in the most preferred observation, the agent would not accumulate any additional evidence. However, if a policy would lead to an undesired (i.e., *a priori* unlikely) observation, much evidence for a re-plan would be gained.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Surprise-based re-planning", "weight": 1.0} -->

If the accumulated evidence is below the threshold of $1$, the model then follows the extended policy. Otherwise, it generates a completely new policy, applying the above policy selection mechanism to every action in the policy.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Surprise-based re-planning", "weight": 1.0} -->

Finally, after the policy is determined, its first action ${\mathbf{a}}_{t}$ is used to update the state of the actual world.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Front-to-rear scenario", "weight": 1.0} -->

In this scenario, we used the vehicle trajectory and driver input data to extract brake response times and deceleration magnitudes. To that end, we followed Markkula et al., extracting response times by fitting a piecewise-linear function to the recorded velocity data; the brake response time was then determined as the time instant when the first constant line switches to one with falling velocity. The slope of this line was used as the estimated deceleration magnitude.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Front-to-rear scenario", "weight": 1.0} -->

When evaluating the goodness of fit of a model to the ground-truth human data, we used the mean absolute error $I$. Given a dataset $D_{0} = {\{{(x,y)}\mid{{x \in X_{0}},{y \in Y_{0}}}\}}$ and a linear approximation of the ground truth ${y_{\text{data}}{(x)}} = {{a_{\text{data}}x} + b_{\text{data}}}$ over the support interval $\lbrack x_{0},x_{1}\rbrack$, we first discarded all sample pairs from $D_{0}$ for which $x \notin {\lbrack x_{0},x_{1}\rbrack}$, resulting in $D$, after which we computed the residuals

<!-- chunk {"id": "body-0128", "role": "body", "section": "Front-to-rear scenario", "weight": 1.0} -->

We assumed the residuals can be approximated by a linear function

<!-- chunk {"id": "body-0129", "role": "body", "section": "Front-to-rear scenario", "weight": 1.0} -->

where $\sigma_{E}$ is the empirical standard deviation of $E$. We placed Gaussian priors

<!-- chunk {"id": "body-0130", "role": "body", "section": "Front-to-rear scenario", "weight": 1.0} -->

with $\sigma_{X}$ denoting the empirical standard deviation of $X$. The posterior $p{(\alpha,{\beta \mid D})}$ was then obtained using standard Bayesian linear regression. Defining

<!-- chunk {"id": "body-0131", "role": "body", "section": "Front-to-rear scenario", "weight": 1.0} -->

When analyzing response times (Figure 3d and second row of Figure 6), we set $x_{0} = {0.9\ s}$ and $x_{1} = {3.6\ s}$. Meanwhile, for the acceleration error (Figure 3e and third row of Figure 6), we set $x_{0} = {0\ s^{- 1}}$ and $x_{1} = {1.0\ s^{- 1}}$.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Opposite-direction lateral incursion scenario", "weight": 1.0} -->

In this scenario, we extracted brake and steering response times following Johnson et al., by interpolating along the acceleration $a_{\text{long}}$ and steering angle $\delta$ data to find the time at which ${- 1}\ {ms}^{- 2}$ and $0.0077\ {rad}$ (i.e., a steering wheel angle of $5^{\circ}$) are exceeded, to extract brake and steering response times respectively.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Opposite-direction lateral incursion scenario", "weight": 1.0} -->

When evaluating model fit of our model variants to the human data in this scenario, we used the Jensen-Shannon divergence (a measure of dissimilarity of two categorical distributions) to compare predicted outcomes and the Wasserstein distance (a proper metric) for reaction times. Given the relatively small size of the ground truth dataset, we applied nonparametric bootstrapping with 10000 resamples to estimate the sampling variability of each metric.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Intersection scenario", "weight": 1.0} -->

To extract response times, here we followed the same approach as in the lateral incursion scenario. We only compared our model to the first collision instance shown to each participant in the experiment of Ziraldo et al. to ensure that the underlying data represents natural reactions of human drivers. Importantly, the human steering reaction times were extracted based on steering wheel angles. However, as Ziraldo et al. did not report how this relates to the steering angle of the vehicle (which our model works with), there might be some discrepancy here, as we had to rely on the relationship reported by Johnson et al.. In this scenario we used the same bootstrapped metrics as in the lateral incursion scenario (i.e., Jensen-Shannon divergence for collision probabilities and Wasserstein distance for response times).

<!-- chunk {"id": "body-0135", "role": "body", "section": "Statistic significance", "weight": 1.0} -->

To determine whether one model variant provided a statistically significant better fit than another, we computed the signal-to-noise ratio of the difference between models, defined as the mean difference in metric values divided by its estimated standard deviation (using sampling from posterior distributions or bootstrapping as described above). A signal-to-noise ratio exceeding 3 was considered indicative of a meaningful difference, following standard statistical heuristics. Here, the difference is computed as the mean metric difference between models, and under the assumption of independence, the standard deviation of the difference is approximated as the square root of the sum of the individual variances.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Model parameters", "weight": 1.0} -->

Time step size
Model of routine driving

<!-- chunk {"id": "body-0137", "role": "body", "section": "Model parameters", "weight": 1.0} -->

Noise applied to other vehicle’s acceleration during belief update

<!-- chunk {"id": "body-0138", "role": "body", "section": "Model parameters", "weight": 1.0} -->

Noise applied to other vehicle’s steering rate during belief update

<!-- chunk {"id": "body-0139", "role": "body", "section": "Model parameters", "weight": 1.0} -->

Noise applied to other vehicle’s acceleration during behavior prediction

<!-- chunk {"id": "body-0140", "role": "body", "section": "Model parameters", "weight": 1.0} -->

Noise applied to other vehicle’s steering rate during behavior prediction

<!-- chunk {"id": "body-0141", "role": "body", "section": "Model parameters", "weight": 1.0} -->

Prediction horizon for the projected normative probability

<!-- chunk {"id": "body-0142", "role": "body", "section": "Model parameters", "weight": 1.0} -->

Mean of preference distribution of agent’s velocity v
Model of routine driving

<!-- chunk {"id": "body-0143", "role": "body", "section": "Model parameters", "weight": 1.0} -->

Standard deviation of preference distribution of agent’s velocity v

<!-- chunk {"id": "body-0144", "role": "body", "section": "Model parameters", "weight": 1.0} -->

Standard deviation of preference distribution of agent’s acceleration a

<!-- chunk {"id": "body-0145", "role": "body", "section": "Model parameters", "weight": 1.0} -->

Standard deviation of preference distribution of agent’s steering rate ω

<!-- chunk {"id": "body-0146", "role": "body", "section": "Model parameters", "weight": 1.0} -->

Pragmatic value for leaving the road

<!-- chunk {"id": "body-0147", "role": "body", "section": "Model parameters", "weight": 1.0} -->

Pragmatic value for driving on a lane boundary or in opposing lanes

<!-- chunk {"id": "body-0148", "role": "body", "section": "Model parameters", "weight": 1.0} -->

Pragmatic value after collision with relative velocity of 10 ms−1

<!-- chunk {"id": "body-0149", "role": "body", "section": "Model parameters", "weight": 1.0} -->

Number of iterations of policy sampling
Model of routine driving

<!-- chunk {"id": "body-0150", "role": "body", "section": "Model parameters", "weight": 1.0} -->

β M samples with lowest EFE are used as base for next iteration
Model of routine driving

<!-- chunk {"id": "body-0151", "role": "body", "section": "Model parameters", "weight": 1.0} -->

Distribution to sample accelerations aτ in first CEM iteration
Model of routine driving (mean) and Tuned parameter (std)

<!-- chunk {"id": "body-0152", "role": "body", "section": "Model parameters", "weight": 1.0} -->

Distribution to sample steering rates ωτ in first CEM iteration
Model of routine driving (mean) and Tuned parameter (std)

<!-- chunk {"id": "body-0153", "role": "body", "section": "Model parameters", "weight": 1.0} -->

Acceleration applied when no pedal is pressed

<!-- chunk {"id": "body-0154", "role": "body", "section": "Model parameters", "weight": 1.0} -->

Each of the key model mechanisms has a number of parameters associated with it (see Table Model parameters for an overview of the 26 most essential parameters). For 12 of them, the exact values have been directly adopted from the literature, in particular the original model. Another thirteen model parameters were treated as free parameters, and were manually tuned to qualitatively match the empirical observations. It was not the purpose of this study to obtain the closest possible fit to human data, so no exhaustive parameter optimization was performed. To analyze the impact that changes of model parameters have on its performance, we conducted a sensitivity analysis (Figures 7 and 8). Specifically, we varied the thirteen tuned parameters from Table Model parameters one at a time, while keeping the other parameters fixed. For most parameters, this explored deviation by roughly one order of magnitude, if not otherwise constrained. For each of the new parameter sets, we reran all the simulation in the three scenarios described in the Results section, and calculated the goodness-of-fit metrics (Figure 6). Using the methods described in the previous Metrics section to estimate the uncertainty of those metrics inherent in the limited number of simulations and human demonstrations, we express those in the corresponding box-plots.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Model parameters", "weight": 1.0} -->

The most consequential parameter is the evidence drift rate λ (Equation ), where moderate deviations can lead to large changes in reaction times and therefore substantially worse goodness of fit (the goodness of fit metrics Ia and W in Figure 7 can degrade on the order of seconds). Model behavior also deteriorates, as seen in the Jensen–Shannon divergences. This is expected, as for example a sufficient increase in λ to trigger re-planning at (nearly) every timestep would in principle be equivalent to removing the evidence accumulation mechanism completely from the model, which was shown to be disadvantageous for reproducing human behavior in Figure 6b. However, our chosen parameter value appears to involve a slight trade-off. In the lateral incursion and intersection scenarios, small increases in λ can improve the accuracy of reaction times while worsening outcome prediction, whereas small decreases show the opposite trend. Meanwhile, the other hand-tuned policy selection parameter, the number of simultaneously evaluated policies M, had even weaker impact (Figure 7). There, for IΔ and DJS, increasing or decreasing M negatively affects the goodness of fit, but there was no evidence that these differences were statistically significant.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Model parameters", "weight": 1.0} -->

Meanwhile, for Ia and W, lower M values did yield better fit to the data, but the improvements were marginal. Parameters of the state transition function did have a major effect on model behavior (Figure 7). For σa, 0 and σω, 0 (the noise assigned to the other vehicles’ control actions in the generative model’s state transition function), we generally observed a U-shaped response across all considered metrics, indicating that deviations from the chosen values led to poorer fit to the data, although not all differences were statistically significant. Similarly, σa and σω (the corresponding noise in the policy roll-out during behavior prediction, second column) chosen for the final model generally yielded best goodness-of-fit. The horizon for calculating the projected normative probability Hn was less influential: it only impacted model behavior in terms of front-to-rear reaction times (IΔ) and the prediction of collision outcomes in the intersection scenario (DJS). For the parameters of the preference function p (o) (Equation ), two primary effects can be observed (Figure 8).

<!-- chunk {"id": "body-0157", "role": "body", "section": "Model parameters", "weight": 1.0} -->

First, the choice of σv and σa is important for producing a reasonable fit for the deceleration magnitude applied in the front-to-rear scenario (Ia in Figure 8). Second, the choice of collision cost gC is critical, with slight deviations from the selected value leading to substantial decreases in model performance (Figure 8). Consequently, fine-tuning of this parameter is of high importance. Varying the remaining parameters did not result in statistically significant changes, suggesting that their coarse calibration is sufficient. However, this is somewhat expected, as the initial trajectories of the ego agents often are aligned with the preferences expressed in those parameters, which mostly influence the specific avoidance maneuver chosen, but not the specific reaction times. This can be seen in the specific metric expressing such behavior (Ia), where especially σv and σa have a significant impact. Especially notable is that – with parameters tuned only on the first two scenarios without any exposure to the intersection scenario – the chosen parameters perform similarly well in the intersection scenario, suggesting good model generalizability.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Model parameters", "weight": 1.0} -->

Taken together, this parameter sensitivity analysis indicates that 1) most of the sensitivity of the model is primarily concentrated in λ and gC; 2) most parameters are robust to minor perturbations; and 3) while not necessarily optimal, our final parameter settings achieve good fit to human data, with no parameter variations leading to substantially better goodness-of-fit across all three scenarios. Data availability statement
The simulation data generated with our active inference model and its ablations in this study have been deposited in the OSF database. As mentioned in the corresponding captions, videos of the results shown in Figures 3, 4, 5 are provided in the Supplementary Materials. Source data underlying the figures is available as a Source Data file. Code availability statement
The code used for the data analysis and modeling in this study is available at with DOI:~10.5281/zenodo.20049511. The code is provided under a non-commercial license that permits use for research, teaching, personal experimentation, and scientific publication. This includes use of the licensed materials for benchmarking in academic or applied research publications.
