<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

ChauffeurNet: Learning to Drive by Imitating the Best and Synthesizing the Worst

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our goal is to train a policy for autonomous driving via imitation learning that is robust enough to drive a real vehicle. We find that standard behavior cloning is insufficient for handling complex driving scenarios, even when we leverage a perception system for preprocessing the input and a controller for executing the output on the car: 30 million examples are still not enough. We propose exposing the learner to synthesized data in the form of perturbations to the expert's driving, which creates interesting situations such as collisions and/or going off the road. Rather than purely imitating all data, we augment the imitation loss with additional losses that penalize undesirable events and encourage progress - the perturbations then provide an important signal for these losses and lead to robustness of the learned model. We show that the ChauffeurNet model can handle complex situations in simulation, and present ablation experiments that emphasize the importance of each of our proposed changes and show that the model is responding to the appropriate causal factors. Finally, we demonstrate the model driving a car in the real world.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In order to drive a car, a driver needs to see and understand the various objects in the environment, predict their possible future behaviors and interactions, and then plan how to control the car in order to safely move closer to their desired destination while obeying the rules of the road. This is a difficult robotics challenge that humans solve well, making imitation learning a promising approach. Our work is about getting imitation learning to the level where it has a shot at driving a real vehicle; although the same insights may apply to other domains, these domains might have different constraints and opportunities, so we do not want to claim contributions there.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We built our system based on leveraging the training data (30 million real-world expert driving examples, corresponding to about 60 days of continual driving) as effectively as possible. There is a lot of excitement for end-to-end learning approaches to driving which typically focus on learning to directly predict raw control outputs such as steering or braking after consuming raw sensor input such as camera or lidar data. But to reduce sample complexity, we opt for mid-level input and output representations that take advantage of perception and control components. We use a perception system that processes raw sensor information and produces our input: a top-down representation of the environment and intended route, where objects such as vehicles are drawn as oriented 2D boxes along with a rendering of the road information and traffic light states. We present this mid-level input to a recurrent neural network (RNN), named ChauffeurNet, which then outputs a driving trajectory that is consumed by a controller which translates it to steering and acceleration. The further advantage of these mid-level representations is that the net can be trained on real or simulated data, and can be easily tested and validated in closed-loop simulations before running on a real car.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our first finding is that even with 30 million examples, and even with mid-level input and output representations that remove the burden of perception and control, pure imitation learning is not sufficient. As an example, we found that this model would get stuck or collide with another vehicle parked on the side of a narrow street, when a nudging and passing behavior was viable. The key challenge is that we need to run the system closed-loop, where errors accumulate and induce a shift from the training distribution (Ross et al. ). Scientifically, this result is valuable evidence about the limitations of pure imitation in the driving domain, especially in light of recent promising results for high-capacity models (Laskey et al. ). But practically, we needed ways to address this challenge without exposing demonstrators to new states actively (Ross et al.; Laskey et al. ) or performing reinforcement learning (Kuefler et al. ).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We find that this challenge is surmountable if we augment the imitation loss with losses that discourage bad behavior and encourage progress, and, importantly, augment our data with synthesized perturbations in the driving trajectory. These expose the model to non-expert behavior such as collisions and off-road driving, and inform the added losses, teaching the model to avoid these behaviors. Note that the opportunity to synthesize this data comes from the mid-level input-output representations, as perturbations would be difficult to generate with either raw sensor input or direct controller outputs.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate our system, as well as the relative importance of both loss augmentation and data augmentation, first in simulation. We then show how our final model successfully drives a car in the real world and is able to negotiate situations involving other agents, turns, stop signs, and traffic lights. Finally, it is important to note that there are highly interactive situations such as merging which may require a significant degree of exploration within a reinforcement learning (RL) framework. This will demand simulating other (human) traffic participants, a rich area of ongoing research. Our contribution can be viewed as pushing the boundaries of what you can do with purely offline data and no RL.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Input Output Representation", "weight": 1.0} -->

We begin by describing our top-down input representation that the network will process to output a drivable trajectory. At any time $t$, our agent (or vehicle) may be represented in a top-down coordinate system by $\mathbf{p}_{t},\theta_{t},s_{t}$, where $\mathbf{p}_{t} = {(x_{t},y_{t})}$ denotes the agent's location or pose, $\theta_{t}$ denotes the heading or orientation, and $s_{t}$ denotes the speed. The top-down coordinate system is picked such that our agent's pose $\mathbf{p}_{0}$ at the current time $t = 0$ is always at a fixed location $(u_{0},v_{0})$ within the image.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Input Output Representation", "weight": 1.0} -->

For data augmentation purposes during training, the orientation of the coordinate system is randomly picked for each training example to be within an angular range of $\theta_{0} \pm \Delta$, where $\theta_{0}$ denotes the heading or orientation of our agent at time $t = 0$. The top-down view is represented by a set of images of size $W \times H$ pixels, at a ground sampling resolution of $\phi$ meters/pixel. Note that as the agent moves, this view of the environment moves with it so the agent always sees a fixed forward range, $R_{forward} = {{({H - v_{0}})}\phi}$ of the world -- similar to having an agent with sensors that see only up to $R_{forward}$ meters forward.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Input Output Representation", "weight": 1.0} -->

As shown in Fig. 1, the input to our model consists of several images of size $W \times H$ pixels rendered into this top-down coordinate system. (a) Roadmap: a color (3-channel) image with a rendering of various map features such as lanes, stop signs, cross-walks, curbs, etc. (b) Traffic lights: a temporal sequence of grayscale images where each frame of the sequence represents the known state of the traffic lights at each past timestep. Within each frame, we color each lane center by a gray level with the brightest level for red lights, intermediate gray level for yellow lights, and a darker level for green or unknown lights^11^1We employ an indexed representation for roadmap and traffic lights channels to reduce the number of input channels, and to allow extensibility of the input representation to express more roadmap features or more traffic light states without changing the model architecture.. (c) Speed limit: a single channel image with lane centers colored in proportion to their known speed limit. (d) Route: the intended route along which we wish to drive, generated by a router (think of a Google Maps-style route).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Input Output Representation", "weight": 1.0} -->

(e) Current agent box: this shows our agent's full bounding box at the current timestep $t = 0$. (f) Dynamic objects in the environment: a temporal sequence of images showing all the potential dynamic objects (vehicles, cyclists, pedestrians) rendered as oriented boxes. (g) Past agent poses: the past poses of our agent are rendered into a single grayscale image as a trail of points.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Input Output Representation", "weight": 1.0} -->

We use a fixed-time sampling of $\deltat$ to sample any past or future temporal information, such as the traffic light state or dynamic object states in the above inputs. The traffic lights and dynamic objects are sampled over the past $T_{scene}$ seconds, while the past agent poses are sampled over a potentially longer interval of $T_{pose}$ seconds. This simple input representation, particularly the box representation of other dynamic objects, makes it easy to generate input data from simulation or create it from real-sensor logs using a standard perception system that detects and tracks objects. This enables testing and validation of models in closed-loop simulations before running them on a real car. This also allows the same model to be improved using simulated data to adequately explore rare situations such as collisions for which real-world data might be difficult to obtain. Using a top-down 2D view also means efficient convolutional inputs, and allows flexibility to represent metadata and spatial relationships in a human-readable format.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Input Output Representation", "weight": 1.0} -->

Papers on testing frameworks such as Tian et al., Pei et al. show the brittleness of using raw sensor data (such as camera images or lidar point clouds) for learning to drive, and reinforce the approach of using an intermediate input representation.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Input Output Representation", "weight": 1.0} -->

If $I$ denotes the set of all the inputs enumerated above, then the ChauffeurNet model recurrently predicts future poses of our agent conditioned on these input images $I$ as shown by the green dots in Fig. 1(h).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Input Output Representation", "weight": 1.0} -->

In Eq. 1, current pose $\mathbf{p}_{0}$ is a known part of the input, and then the ChauffeurNet performs N iterations and outputs a future trajectory$\{\mathbf{p}_{\deltat},\mathbf{p}_{2\deltat},\ldots,\mathbf{p}_{N\deltat}\}$ along with other properties such as future speeds. This trajectory can be fed to a controls optimizer that computes detailed driving control (such as steering and braking commands) within the specific constraints imposed by the dynamics of the vehicle to be driven. Different types of vehicles may possibly utilize different control outputs to achieve the same driving trajectory, which argues against training a network to directly output low-level steering and acceleration control. Note, however, that having intermediate representations like ours does not preclude end-to-end optimization from sensors to controls.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Model Design", "weight": 1.0} -->

Broadly, the driving model is composed of several parts as shown in Fig. 2. The main ChauffeurNet model shown in part (a) of the figure consists of a convolutional feature network (FeatureNet) that consumes the input data to create a digested contextual feature representation that is shared by the other networks. These features are consumed by a recurrent agent network (AgentRNN) that iteratively predicts successive points in the driving trajectory. Each point at time $t$ in the trajectory is characterized by its location $\mathbf{p}_{t} = {(x_{t},y_{t})}$, heading $\theta_{t}$ and speed $s_{t}$. The AgentRNN also predicts the bounding box of the vehicle as a spatial heatmap at each future timestep. In part (b) of the figure, we see that two other networks are co-trained using the same feature representation as an input.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Model Design", "weight": 1.0} -->

The Road Mask Network predicts the drivable areas of the field of view (on-road vs. off-road), while the recurrent perception network (PerceptionRNN) iteratively predicts a spatial heatmap for each timestep showing the future location of every other agent in the scene. We believe that doing well on these additional tasks using the same shared features as the main task improves generalization on the main task. Fig. 2(c) shows the various losses used in training the model, which we will discuss in detail below.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Model Design", "weight": 1.0} -->

Fig. 3 illustrates the ChauffeurNet model in more detail. The rendered inputs shown in Fig. 1 are fed to a large-receptive field convolutional FeatureNet with skip connections, which outputs features $F$ that capture the environmental context and the intent. These features are fed to the AgentRNN which predicts the next point $\mathbf{p}_{k}$ on the driving trajectory, and the agent bounding box heatmap $B_{k}$, conditioned on the features $F$ from the FeatureNet, the iteration number $k \in {\{ 1,\ldots,N\}}$, the memory $M_{k - 1}$ of past predictions from the AgentRNN, and the agent bounding box heatmap $B_{k - 1}$ predicted in the previous iteration.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Model Design", "weight": 1.0} -->

The memory $M_{k}$ is an additive memory consisting of a single channel image. At iteration $k$ of the AgentRNN, the memory is incremented by 1 at the location $\mathbf{p}_{k}$ predicted by the AgentRNN, and this memory is then fed to the next iteration. The AgentRNN outputs a heatmap image over the next pose of the agent, and we use the arg-max operation to obtain the coarse pose prediction $\mathbf{p}_{k}$ from this heatmap. The AgentRNN then employs a shallow convolutional meta-prediction network with a fully-connected layer that predicts a sub-pixel refinement of the pose $\delta\mathbf{p}_{k}$ and also estimates the heading $\theta_{k}$ and the speed $s_{k}$. Note that the AgentRNN is unrolled at training time for a fixed number of iterations, and the losses described below are summed together over the unrolled iterations.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Model Design", "weight": 1.0} -->

This is possible because of the non-traditional RNN design where we employ an explicitly crafted memory model instead of a learned memory.

<!-- chunk {"id": "body-0021", "role": "body", "section": "System Architecture", "weight": 1.0} -->

Fig. 4 shows a system level overview of how the neural net is used within the self-driving system. At each time, the updated state of our agent and the environment is obtained via a perception system that processes sensory output from the real-world or from a simulation environment as the case may be. The intended route is obtained from the router, and is updated dynamically conditioned on whether our agent was able to execute past intents or not. The environment information is rendered into the input images described in Fig. 1 and given to the RNN which then outputs a future trajectory. This is fed to a controls optimizer that outputs the low-level control signals that drive the vehicle (in the real world or in simulation).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Imitating the Expert", "weight": 1.0} -->

In this section, we first show how to train the model above to imitate the expert.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Agent Position, Heading and Box Prediction", "weight": 1.0} -->

The AgentRNN produces three outputs at each iteration $k$: a probability distribution $P_{k}{(x,y)}$ over the spatial coordinates of the predicted waypoint obtained after a spatial softmax, a heatmap of the predicted agent box at that timestep $B_{k}{(x,y)}$ obtained after a per-pixel sigmoid activation that represents the probability that the agent occupies a particular pixel, and a regressed box heading output $\theta_{k}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Agent Position, Heading and Box Prediction", "weight": 1.0} -->

where the superscript gt denotes the corresponding ground-truth values, and $\mathcal{H}{(a,b)}$ is the cross-entropy function. Note that $P_{k}^{gt}$ is a binary image with only the pixel at the ground-truth target coordinate $\lfloor\mathbf{p}_{k}^{gt}\rfloor$ set to one.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Agent Meta Prediction", "weight": 1.0} -->

The meta prediction network performs regression on the features to generate a sub-pixel refinement $\delta\mathbf{p}_{k}$ of the coarse waypoint prediction as well as a speed estimate $s_{k}$ at each iteration.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Past Motion Dropout", "weight": 1.0} -->

During training, the model is provided the past motion history as one of the inputs (Fig. 1(g)). Since the past motion history during training is from an expert demonstration, the net can learn to "cheat" by just extrapolating from the past rather than finding the underlying causes of the behavior. During closed-loop inference, this breaks down because the past history is from the net's own past predictions. For example, such a trained net may learn to only stop for a stop sign if it sees a deceleration in the past history, and will therefore never stop for a stop sign during closed-loop inference. To address this, we introduce a dropout on the past pose history, where for $50\%$ of the examples, we keep only the current position $(u_{0},v_{0})$ of the agent in the past agent poses channel of the input data. This forces the net to look at other cues in the environment to explain the future motion profile in the training example.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Beyond Pure Imitation", "weight": 1.0} -->

In this section, we go beyond vanilla cloning of the expert's demonstrations in order to teach the model to arrest drift and avoid bad behavior such as collisions and off-road driving by synthesizing variations of the expert's behavior.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Synthesizing Perturbations", "weight": 1.0} -->

Running the model as a part of a closed-loop system over time can cause the input data to deviate from the training distribution. To prevent this, we train the model by adding some examples with realistic perturbations to the agent trajectories. The start and end of a trajectory are kept constant, while a perturbation is applied around the midpoint and smoothed across the other points. Quantitatively, we jitter the midpoint pose of the agent uniformly at random in the range $\lbrack{- 0.5},0.5\rbrack$ meters in both axes, and perturb the heading by $\lbrack{- {\pi/3}},{\pi/3}\rbrack$ radians. We then fit a smooth trajectory to the perturbed point and the original start and end points. Such training examples bring the car back to its original trajectory after a perturbation. Fig. 5 shows an example of perturbing the current agent location (red point) away from the lane center and the fitted trajectory correctly bringing it back to the original target location along the lane center.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Synthesizing Perturbations", "weight": 1.0} -->

We filter out some perturbed trajectories that are impractical by thresholding on maximum curvature. But we do allow the perturbed trajectories to collide with other agents or drive off-road, because the network can then experience and avoid such behaviors even though real examples of these cases are not present in the training data. In training, we give perturbed examples a weight of $1/10$ relative to the real examples, to avoid learning a propensity for perturbed driving.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Collision Loss", "weight": 1.0} -->

Since our training data does not have any real collisions, the idea of avoiding collisions is implicit and will not generalize well. To alleviate this issue, we add a specialized loss that directly measures the overlap of the predicted agent box $B_{k}$ with the ground-truth boxes of all the scene objects at each timestep.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Collision Loss", "weight": 1.0} -->

where $B_{k}$ is the likelihood map for the output agent box prediction, and $Obj_{k}^{gt}$ is a binary mask with ones at all pixels occupied by other dynamic objects (other vehicles, pedestrians, etc.) in the scene at timestep $k$. At any time during training, if the model makes a poor prediction that leads to a collision, the overlap loss would influence the gradients to correct the mistake. However, this loss would be effective only during the initial training rounds when the model hasn't learned to predict close to the ground-truth locations due to the absence of real collisions in the ground truth data. This issue is alleviated by the addition of trajectory perturbation data, where artificial collisions within those examples allow this loss to be effective throughout training without the need for online exploration like in reinforcement learning settings.

<!-- chunk {"id": "body-0032", "role": "body", "section": "On Road Loss", "weight": 1.0} -->

Trajectory perturbations also create synthetic cases where the car veers off the road or climbs a curb or median because of the perturbation. To train the network to avoid hitting such hard road edges, we add a specialized loss that measures overlap of the predicted agent box $B_{k}$ in each timestep with a binary mask $Road^{gt}$ denoting the road and non-road regions within the field-of-view.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Geometry Loss", "weight": 1.0} -->

We would like to explicitly constrain the agent to follow the target geometry independent of the speed profile. We model this target geometry by fitting a smooth curve to the target waypoints and rendering this curve as a binary image in the top-down coordinate system. The thickness of this curve is set to be equal to the width of the agent. We express this loss similar to the collision loss by measuring the overlap of the predicted agent box with the binary target geometry image $Geom^{gt}$. Any portion of the box that does not overlap with the target geometry curve is added as a penalty to the loss function.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Auxiliary Losses", "weight": 1.0} -->

Similar to our own agent's trajectory, the motion of other agents may also be predicted by a recurrent network. Correspondingly, we add a recurrent perception network PerceptionRNN that uses as input the shared features $F$ created by the FeatureNet and its own predictions $Obj_{k - 1}$ from the previous iteration, and predicts a heatmap $Obj_{k}$ at each iteration. $Obj_{k}{(x,y)}$ denotes the probability that location $(x,y)$ is occupied by a dynamic object at time $k$. For iteration $k = 0$, the PerceptionRNN is fed the ground truth objects at the current time.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Auxiliary Losses", "weight": 1.0} -->

Co-training a PerceptionRNN to predict the future of other agents by sharing the same feature representation $F$ used by the PerceptionRNN is likely to induce the feature network to learn better features that are suited to both tasks. Several examples of predicted trajectories from PerceptionRNN on logged data are shown on our website here.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Auxiliary Losses", "weight": 1.0} -->

We also co-train to predict a binary road/non-road mask by adding a small network of convolutional layers to the output of the feature net $F$. We add a cross-entropy loss to the predicted road mask output $Road{(x,y)}$ which compares it to the ground-truth road mask $Road^{gt}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Auxiliary Losses", "weight": 1.0} -->

Fig. 6 shows some of the predictions and losses for a single example processed through the model.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Imitation Dropout", "weight": 1.0} -->

The imitation losses cause the model to imitate the expert's demonstrations, while the environment losses discourage undesirable behavior such as collisions. To further increase the effectiveness of the environment losses, we experimented with randomly dropping out the imitation losses for a random subset of training examples. We refer to this as "imitation dropout". In the experiments, we show that imitation dropout yields a better driving model than simply under-weighting the imitation losses. During imitation dropout, the weight on the imitation losses $w_{imit}$ is randomly chosen to be either 0 or 1 with a certain probability for each training example.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Data", "weight": 1.0} -->

The training data to train our model was obtained by randomly sampling segments of real-world expert driving and removing segments where the car was stationary for long periods of time. Our input field of view is ${{80m} \times 80}m$ (${W\phi} = 80$) and with the agent positioned at $(u_{0},v_{0})$, we get an effective forward sensing range of $R_{forward} = {64m}$. Therefore, for the experiments in this work we also removed any segments of highway driving given the longer sensing range requirement that entails. Our dataset contains approximately 26 million examples which amount to about 60 days of continuous driving. As discussed in Section 3, the vertical-axis of the top-down coordinate system for each training example is randomly oriented within a range of $\Delta = {\pm 25^{\circ}}$ of our agent's current heading, in order to avoid a bias for driving along the vertical axis. The rendering orientation is set to the agent heading ($\Delta = 0$) during inference.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Data", "weight": 1.0} -->

Data about the prior map of the environment (roadmap) and the speed-limits along the lanes is collected apriori. For the dynamic scene entities like objects and traffic-lights, we employ a separate perception system based on laser and camera data similar to existing works in the literature (Yang et al.; Fairfield and Urmson ). Table 1 lists the parameter values used for all the experiments in this paper. The model runs on a NVidia Tesla P100 GPU in 160ms with the detailed breakdown in Table 2.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Models", "weight": 1.0} -->

We train and test not only our final model, but a sequence of models that introduce the ingredients we describe one by one on top of behavior cloning. We start with $\mathcal{M}_{0}$, which does behavior cloning with past motion dropout to prevent using the history to cheat. $\mathcal{M}_{1}$ adds perturbations without modifying the losses. $\mathcal{M}_{2}$ further adds our environment losses $\mathcal{L}_{env}$ in Section 5.2. $\mathcal{M}_{3}$ and $\mathcal{M}_{4}$ address the fact that we do not want to imitate bad behavior -- $\mathcal{M}_{3}$ is a baseline approach, where we simply decrease the weight on the imitation loss, while $\mathcal{M}_{4}$ uses our imitation dropout approach with a dropout probability of $0.5$. Table 3 lists the configuration for each of these models.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Closed Loop Evaluation", "weight": 1.0} -->

To evaluate our learned model on a specific scenario, we replay the segment through the simulation until a buffer period of $\text{max}{(T_{pose},T_{scene})}$ has passed. This allows us to generate the first rendered snapshot of the model input using all the replayed messages until now. The model is evaluated on this input, and the fitted controls are passed to the vehicle simulator that emulates the dynamics of the vehicle thus moving the simulated agent to its next pose. At this point, the simulated pose might be different from the logged pose, but our input representation allows us to correctly render the new input for the model relative to the new pose. This process is repeated until the end of the segment, and we evaluate scenario specific metrics like stopping for a stop-sign, collision with another vehicle etc. during the simulation. Since the model is being used to drive the agent forward, this is a *closed-loop* evaluation setup.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Model Ablation Tests", "weight": 1.0} -->

Here, we present results from experiments using the various models in the closed-loop simulation setup. We first evaluated all the models on simple situations such as stopping for stop-signs and red traffic lights, and lane following along straight and curved roads by creating 20 scenarios for each situation, and found that *all the models worked well in these simple cases*. Therefore, we will focus below on specific complex situations that highlight the differences between these models.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Model Ablation Tests", "weight": 1.0} -->

ℳ2 with Imitation Dropout
Dropout probability = 0.5 (see Section 5.3).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Nudging around a parked car", "weight": 1.0} -->

To set up this scenario, we place the agent at an arbitrary distance from a stop-sign on an undivided two-way street and then place a parked vehicle on the right shoulder between the the agent and the stop-sign. We pick 4 separate locations with both straight and curved roads then vary the starting speed of the agent between 5 different values to create a total of 20 scenarios. We then observe if the agent would stop and get stuck behind, collide with the parked car, or correctly pass around the parked car, and report the aggregate performance in Fig. 7(row 1). We find that other than $\mathcal{M}_{4}$, all other models cause the agent to collide with the parked vehicle about half the time. The baseline $\mathcal{M}_{0}$ model can also get stuck behind the parked vehicle in some of the scenarios. The model $\mathcal{M}_{4}$ nudges around the parked vehicle and then brings the agent back to the lane center. This can be attributed to the model's ability to learn to avoid collisions and nudge around objects because of training with the collision loss the trajectory perturbation.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Nudging around a parked car", "weight": 1.0} -->

Comparing model $\mathcal{M}_{3}$ and $\mathcal{M}_{4}$, it is apparent that "imitation dropout" was more effective at learning the right behavior than only re-weighting the imitation losses. Note that in this scenario, we generate several variations by changing the starting speed of the agent relative to the parked car. This creates situations of increasing difficulty, where the agent approaches the parked car at very high relative speed and thus does not have enough time to nudge around the car given the dynamic constraints. A 10% collision rate for $\mathcal{M}_{4}$ is thus not a measure of the absolute performance of the model since we do not have a perfect driver which could have performed well at all the scenarios here. But in relative terms, this model performs the best.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Recovering from a trajectory perturbation", "weight": 1.0} -->

To set up this scenario, we place the agent approaching a curved road and vary the starting position and the starting speed of the agent to generate a total of 20 scenario variations. Each variation puts the agent at a different amount of offset from the lane center with a different heading error relative to the lane. We then measure how well the various models are at recovering from the lane departure. Fig. 7(row 2) presents the results aggregated across these scenarios and shows the contrast between the baseline model $\mathcal{M}_{0}$ which is not able to recover in any of the situations and the models $\mathcal{M}_{3}$ and $\mathcal{M}_{4}$ which handle all deviations well. All models trained with the perturbation data are able to handle 50% of the scenarios which have a lower starting speed.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Recovering from a trajectory perturbation", "weight": 1.0} -->

At a higher starting speed, we believe that $\mathcal{M}_{3}$ and $\mathcal{M}_{4}$ do better than $\mathcal{M}_{1}$ and $\mathcal{M}_{2}$ because they place a higher emphasis on the imagination losses.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Slowing down for a slow car", "weight": 1.0} -->

To set up this scenario, we place the agent on a straight road at varying initial speeds and place another car ahead with a varying but slower constant speed, generating a total of 20 scenario variations, to evaluate the ability to slow for and then follow the car ahead. From Fig. 7(row 3), we see that some models slow down to zero speed and get stuck. For the variation with the largest relative speed, there isn't enough time for most models to stop the agent in time, thus leading to a collision. For these cases, model $\mathcal{M}_{3}$ which uses imitation loss re-weighting works better than the model $\mathcal{M}_{4}$ which uses imitation dropout. $\mathcal{M}_{4}$ has trouble in two situations due to being over aggressive in trying to maneuver around the slow car and then grazes the left edge of the road. This happens in the two extreme variations where the relative speed between the two cars is the highest.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Input Ablation Tests", "weight": 1.0} -->

With input ablation tests, we want to test the final $\mathcal{M}_{4}$ model's ability to identify the correct causal factors behind specific behaviors, by testing the model's behavior in the presence or absence of the correct causal factor while holding other conditions constant. In simulation, we have evaluated our model on 20 scenarios with and without stop-signs rendered, and 20 scenarios with and without other vehicles in the scene rendered. The model exhibits the correct behavior in all scenarios, thus confirming that it has learned to respond to the correct features for a stop-sign and a stopped vehicle.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Logged Data Simulated Driving", "weight": 1.0} -->

For this evaluation, we take logs from our real-driving test data (separate from our training data), and use our trained network to drive the car using the vehicle simulator keeping everything else the same i.e. the dynamic objects, traffic-light states etc. are all kept the same as in the logs. Some example videos are shown here and they illustrate the ability of the model in dealing with multiple dynamic objects and road controls.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Real World Driving", "weight": 1.0} -->

We have also evaluated this model on our self-driving car by replacing the existing planner module with the learned model $\mathcal{M}_{4}$ and have replicated the driving behaviors observed in simulation. The videos of several of these runs are available here and they illustrate not only the smoothness of the network's driving ability, but also its ability to deal with stop-signs and turns and to drive for long durations in full closed-loop control without deviating from the trajectory.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Real World Driving", "weight": 1.0} -->

(a) Prediction Error for models ℳ0 and ℳ4 on unperturbed evaluation data.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Real World Driving", "weight": 1.0} -->

(b) Prediction Error for models ℳ0 and ℳ1 on perturbed evaluation data.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Open Loop Evaluation", "weight": 1.0} -->

In an open-loop evaluation, we take test examples of expert driving data and for each example, compute the $L_{2}$ distance error between the predicted and ground-truth waypoints. Unlike the closed-loop setting, the predictions are not used to drive the agent forward and thus the network never sees its own predictions as input. Fig. 8(a) shows the $L_{2}$ distance metric in this open-loop evaluation setting for models $\mathcal{M}_{0}$ and $\mathcal{M}_{4}$ on a test set of 10,000 examples. These results show that model $\mathcal{M}_{0}$ makes fewer errors than the full model $\mathcal{M}_{4}$, but we know from closed-loop testing that $\mathcal{M}_{4}$ is a far better driver than $\mathcal{M}_{0}$. This shows how open-loop evaluations can be misleading, and closed-loop evaluations are critical while assessing the real performance of such driving models.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Open Loop Evaluation", "weight": 1.0} -->

We also compare the performance of models $\mathcal{M}_{0}$ and $\mathcal{M}_{1}$ on our perturbed evaluation data w.r.t the $L_{2}$ distance metric in Fig. 8(b). Note that the model trained without including perturbed data ($\mathcal{M}_{0}$) has larger errors due to its inability to bring the agent back from the perturbation onto its original trajectory. Fig. 9 shows examples of the trajectories predicted by these models on a few representative examples showcasing that the perturbed data is critical to avoiding the veering-off tendency of the model trained without such data.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Failure Modes", "weight": 1.0} -->

At our ground resolution of $20$ cm/pixel, the agent currently sees $64$ m in front and $40$ m on the sides and this limits the model's ability to perform merges on T-junctions and turns from a high-speed road. Specific situations like U-turns and cul-de-sacs are also not currently handled, and will require sampling enough training data. The model occasionally gets stuck in some low speed nudging situations. It sometimes outputs turn geometries that make the specific turn infeasible (e.g. large turning radius). We also see some cases where the model gets over aggressive in novel and rare situations for example by trying to pass a slow moving vehicle. We believe that adequate simulated exploration may be needed for highly interactive or rare situations.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Sampling Speed Profiles", "weight": 1.0} -->

The waypoint prediction from the model at timestep $k$ is represented by the probability distribution $P_{k}{(x,y)}$ over the spatial domain in the top-down coordinate system. In this paper, we pick the mode of this distribution $\mathbf{p}_{k}$ to update the memory of the $AgentRNN$. More generally, we can also sample from this distribution to allow us to predict trajectories with different speed profiles. Fig. 10 illustrates the predictions $P_{1}{(x,y)}$ and $P_{5}{(x,y)}$ at the first and the fifth iterations respectively, for a training example where the past motion history has been dropped out. Correspondingly, $P_{1}{(x,y)}$ has a high uncertainity along the longitudinal position and allows us to pick from a range of speed samples. Once we pick a specific sample, the ensuing waypoints get constrained in their ability to pick different speeds and this shows as a centered distribution at the $P_{5}{(x,y)}$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Sampling Speed Profiles", "weight": 1.0} -->

The use of a probability distribution over the next waypoint also presents the interesting possibility of constraining the model predictions at inference time to respect hard constraints. For example, such constrained sampling may provide a way to ensure that any trajectories we generate strictly obey legal restrictions such as speed limits. One could also constrain sampling of trajectories to a designated region, such as a region around a given reference trajectory.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this paper, we presented our experience with what it took to get imitation learning to perform well in real-world driving. We found that key to its success is synthesizing interesting situations around the expert's behavior and augmenting appropriate losses that discourage undesirable behavior. This constrained exploration is what allowed us to avoid collisions and off-road driving even though such examples were not explicitly present in the expert's demonstrations. To support it, and to best leverage the expert data, we used middle-level input and output representations which allow easy mixing of real and simulated data and alleviate the burdens of learning perception and control. With these ingredients, we got a model good enough to drive a real car. That said, the model is not yet fully competitive with motion planning approaches but we feel that this is a good step forward for machine learned driving models. There is room for improvement: comparing to end-to-end approaches, and investigating alternatives to imitation dropout are among them. But most importantly, we believe that augmenting the expert demonstrations with a thorough exploration of rare and difficult scenarios in simulation, perhaps within a reinforcement learning framework, will be the key to improving the performance of these models especially for highly interactive scenarios.
