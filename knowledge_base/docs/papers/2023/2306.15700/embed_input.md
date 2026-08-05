<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Imitation with Spatial-Temporal Heatmap: 2nd Place Solution for NuPlan Challenge

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents our 2nd place solution for the NuPlan Challenge 2023. Autonomous driving in real-world scenarios is highly complex and uncertain. Achieving safe planning in the complex multimodal scenarios is a highly challenging task. Our approach, Imitation with Spatial-Temporal Heatmap, adopts the learning form of behavior cloning, innovatively predicts the future multimodal states with a heatmap representation, and uses trajectory refinement techniques to ensure final safety. The experiment shows that our method effectively balances the vehicle's progress and safety, generating safe and comfortable trajectories. In the NuPlan competition, we achieved the second highest overall score, while obtained the best scores in the ego progress and comfort metrics.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The NuPlan challenge is the world's first large-scale planning benchmark for autonomous driving. It offers approximately 1300 hours of human driving data sourced from four different cities across the US and Asia with highly complex and diverse scenarios. Unlike previous competitions, NuPlan focuses more on long-term planning rather than short-term motion prediction. It also provides a highly realistic simulator for conducting closed-loop evaluation that aligns more closely with real-world scenarios. Amidst the numerous competitors, our methodology stood out as the second place in the competition.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We use an imitation learning approach with several innovations, including using a spatial-temporal heatmap to represent the distributions of the ego future trajectory, and using a multitasking learning approach to predict and model the surrounding dynamic objects. With these dynamic and static future environment, we find the optimal trajectory with a post-solver. Our ablation studies demonstrate the effectiveness of these techniques.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Methodology", "weight": 1.0} -->

In this section, we describe our model as shown in Fig. 1. Our system comprises two stages: the behavior cloning stage and the trajectory refinement stage. In the first stage, the model is trained by supervised learning to generate the initial plan, multi-modal heatmap, and the future behavior of surrounding agents. The second stage focuses on refining the initial trajectory, taking into account the vehicle's kinematics, comfort, and safety constraints. We first introduce our input representation, and then elaborate the structure of our model, and lastly give a more detailed description of the trajectory refinement stage.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Input Representation", "weight": 1.0} -->

In the context of autonomous driving, raster serves as a grid-based representation of the environment. They offer a snapshot of the surroundings, where the grids contain essential information of road layout, traffic conditions, and vehicle status. Raster provides a structured format that is particularly useful for processing spatial domain information.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Input Representation", "weight": 1.0} -->

For this competition, we created a six-channel raster, each channel realizing an environmental modality, including ego vehicle's current state, other agents's history, current map information and navigation route, etc.. The ego channel represents our vehicle's state and position. The road map channel encapsulates physical layout features, transformed from a vector-based map. Baseline-path channel displays all lanes within a specific range. Agent channels encode traffic participants other than the ego car, using 2D representations on the raster grid. The route raster outlines a navigation route for the planning model to follow. Finally, the ego speed channel fills the 2D raster with the ego vehicle's speed. This multi-channel raster input offers a comprehensive spatio-temporal environmental depiction, enabling the model to comprehend and anticipate traffic dynamics.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Network Structure", "weight": 1.0} -->

Encoder To encode the input data, we employ ResNet as our convolutional neural network (CNN) encoder. Specifically, we utilize in our implementation. The encoder is responsible for generating multi-scale features denoted as $C_{1},C_{2},C_{3},C_{4},C_{5}$, where $C_{i}$ represents the feature map with a spatial size of $\frac{H}{2^{i}} \times \frac{W}{2^{i}}$, serving as the input for the subsequent components.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Network Structure", "weight": 1.0} -->

Neck The neck component in our model follows the architecture of Unet, which facilitates the integration of features at multiple resolutions, enabling the model to capture both fine-grained and high-level contextual information.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Heads", "weight": 1.0} -->

Our method employs three distinct heads dedicated to different tasks, namely ego trajectory prediction, ego heatmap prediction and surrounding agents occupancy predictions.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Heads", "weight": 1.0} -->

Trajectory head The trajectory head generates the initial plan, which is composed of two fully-connected layers. The output trajectory is denoted as $\tau \in {\mathbb{R}}^{T \times 3}$, where $T$ represents the number of time steps and 3 denotes the three-dimensional parameters (e.g., x, y, heading) of the predicted trajectory.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Heads", "weight": 1.0} -->

Heatmap head Inspired by HOME, we adopt a bird-eye-view heatmap representation for ego trajectory. Differently, we model ego location at each time step. Each pixel in the output image represents a location on the ground, and the value at each pixel indicates the probability or confidence associated with the presence of each trajectory point at that particular location. In order to predict the ego plan on a more finely-grained scale, we up-sample the original feature to 0.25m × 0.25m/pixel.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Heads", "weight": 1.0} -->

To generate the target output, we use a Gaussian distribution centered around the ground truth position. This approach allows the model to capture the uncertainty and multi-modality in the each trajectory point prediction.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Heads", "weight": 1.0} -->

Occupancy head To model the surrounding dynamic environment, we employ the occupancy head, which predicts the motion behavior of other agents in the form of probabilistic occupancy grids. Specifically, the occupancy head predicts occupancy logits for each timestep t and shares the same feature resolution as the input raster.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Collision Avoidance Map", "weight": 1.0} -->

To better serve downstream applications, it is necessary to transform the predicted ego vehicle pose, the predicted occupancy probability of surrounding agents, and the static information (HD maps) into a collision probability density map. The collision probability density map represents the probability of collision at a given location in the coordinate system of the predicted future trajectory. Innovatively, we leverage the group convolution operator on the GPU to efficiently execute this step and achieve real-time performance. Specifically, we merge other agents' predicted occupancy ${\hat{O}}_{\text{agents}}$, static objects ${\overset{\sim}{O}}_{\text{static}}$, and the drivable area ${\overset{\sim}{O}}_{\text{drivable}}$ into a non-drivable area map ${\hat{O}}_{\text{non-drivable}}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Collision Avoidance Map", "weight": 1.0} -->

With the predicted ego vehicle pose $\hat{\tau_{t}}$, we create a convolution kernel $W{(\hat{\tau_{t}},H_{ego},W_{ego})}$ that matches the shape and future pose of the ego vehicle.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Post-Solver", "weight": 1.0} -->

Similar to UniAD, we employ CasADi ipopt solver, which takes into account the vehicle's kinematics, comfort, predicted heatmap probability, and collision probability density map. By adjusting the initial trajectory through the post solver, we aim to achieve a safe and comfortable trajectory for vehicle control. Specifically, we denote the output trajectory as the parameter $\tau \in {\mathbb{R}}^{T \times 3}$, the imitated initial trajectory as $\hat{\tau} \in {\mathbb{R}}^{T \times 3}$, the collision probability density map as $\hat{O} \in {\mathbb{R}}^{h \times w \times T}$, the heatmap prediction as $\hat{H} \in {\mathbb{R}}^{h \times w \times T}$. The cost function $f{(\cdot)}$ is calculated: | | ${f{(\left.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Post-Solver", "weight": 1.0} -->

$\lambda_{\text{o}}$, $\lambda_{\text{h}}$ are the hyperparameters, and the kinematic function set $\Phi$ has five terms including jerk, curvature, curvature rate, acceleration and lateral acceleration.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Post-Solver", "weight": 1.0} -->

To speed up the inference, we sample the $S_{o}$ nearest occupied pixels and the top $S_{h}$ heatmap pixels at each time step. Moreover, to ensure the model can output trajectories that are consistent with actual physical conditions, we add some hard constraints, including dynamic constraints for the ego vehicle, state constraints, and control constraints.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Learning", "weight": 1.0} -->

We adopted a multi-task learning approach. For the prediction of the initial trajectory and pose of the ego vehicle, we employed a weight-decay L1 loss as shown in eq 6. For the heatmap supervision, we utilized the penalty-reduced pixelwise logistic regression with focal loss as shown in eq 7, where ${\hat{H}}_{t}$ is the predicted ego vehicles's location at time t, and ${\overset{\sim}{H}}_{t}$ is the target ground truth. Positive samples correspond to the locations of the expert trajectory, denoted as $\overset{\sim}{\tau}$. All other locations are considered negative samples, with penalties attenuated by a Gaussian kernel. For the occupancy, we applied binary cross-entropy loss. And lastly we take a weighted sum as the final loss.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Experiments", "weight": 1.0} -->

We generated the rasterized input within a ${{112m} \times 112}m$ region at a resolution of 0.5m/pixel, resulting in an input spatial size of $224 \times 224$. To optimize our model, we employ the Adam optimizer along with a multiple-step policy. The initial learning rate was set to $2 \times 10^{- 4}$, and a weight decay of $5 \times 10^{- 4}$ was applied. Furthermore, we assign the following loss coefficients: $\lambda_{\text{occ}} = 100$, $\lambda_{\text{hm}} = 1.0$, and $\lambda_{\text{imi}} = 1.0$. The model was trained for 20 epochs with a batch size of 32.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Experiments", "weight": 1.0} -->

Regarding the data, we employed a random sampling strategy where 50,000 frames per scenario type were selected from the training dataset, resulting in a total of approximately 1.5 million frames.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Experiments", "weight": 1.0} -->

To enhance the model's performance, we introduced perturbations during training, inspired by the methodology proposed by ChauffeurNet. Specifically, we applied a uniformly distributed random jittering to the current pose of the ego agent within the ranges of \[0, 1.0\] meters along the x-axis and \[-1.0, 1.0\] meters along the y-axis. Additionally, the heading was perturbed by an angle between \[-0.25, 0.25\] in radians. To ensure smooth trajectories, we fit a trajectory starting at the perturbed point and ended at the original end point, under a variety of dynamic constraints. These perturbed training examples enabled the ego car to recover its normal trajectory if experiencing a deviation from its normal route.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

In this section, we conduct an ablation study on the aforementioned techniques, as shown in Tab. 1. We can observe that perturbation improved both open-loop and close-loop performances. As a form of data augmentation, perturbation can significantly enhance the data utilization rate. For the heatmap prediction, we saw a substantial enhancement in close-loop performance, particularly in close-loop reactive scenarios and collision rate. This demonstrates that the spatial-temporal heatmap could be a better representation of planning compared to single trajectory. In later visualizations in Sec. 4.3, we can observe the effectiveness of the heatmap representation in modeling multi-modality and uncertainty. Furthermore, the bird's eye view spatial representation aligns well with our raster input, guiding the model's convergence. Furthermore, by incorporating the post-solver, we noticed a significant boost in close-loop performance, notably in collision and drivable area compliance, validating the effectiveness of post-optimization in the modeled environment.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Learderboard", "weight": 1.0} -->

Here, we present our ranking on the private test set in the NuPlan competition, as shown in Tab. 2. Notably, We achieve the highest comfort and ego progress among all competitors.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Visualizations", "weight": 1.0} -->

In this section, we present a qualitative assessment of our planner's performance through closed-loop simulation results, under representative driving scenarios. These scenarios are visualized as sequential snapshots of the closed-loop rollouts. The top row displays images generated using the nuboard visualization tool, illustrating the smooth movement of the ego vehicle, denoted by a white rectangle. The bottom row demonstrates corresponding model predictions. Here, the heatmap predictions are indicated in red, pixels of potential collision or boundary exceedance that warrant close attention are marked in yellow, and the final planned trajectory for the ego vehicle is shown as green dots. Fig. 4. 4. 4 shows the visualization of some of our planning results.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we introduce our winning solution for the NuPlan challenge. We adopt a novel spatial-temporal heatmap representation for planning, along with a corresponding post-solver to ensure a final plan that is both safe and comfortable. Experimental results validate the effectiveness of every component, highlighting our method's aptitude for balancing the ego progress and safety while generating safe and comfortable trajectories.
