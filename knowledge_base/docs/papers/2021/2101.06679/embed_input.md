<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

End-to-end Interpretable Neural Motion Planner

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we propose a neural motion planner (NMP) for learning to drive autonomously in complex urban scenarios that include traffic-light handling, yielding, and interactions with multiple road-users. Towards this goal, we design a holistic model that takes as input raw LIDAR data and a HD map and produces interpretable intermediate representations in the form of 3D detections and their future trajectories, as well as a cost volume defining the goodness of each position that the self-driving car can take within the planning horizon. We then sample a set of diverse physically possible trajectories and choose the one with the minimum learned cost. Importantly, our cost volume is able to naturally capture multi-modality. We demonstrate the effectiveness of our approach in real-world driving data captured in several cities in North America. Our experiments show that the learned cost volume can generate safer planning than all the baselines.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Self-driving vehicles (SDVs) are going to revolutionize the way we live. Building reliable SDVs at scale is, however, not a solved problem. As is the case in many application domains, the field of autonomous driving has been transformed in the past few years by the success of deep learning. Existing approaches that leverage this technology can be characterized into two main frameworks: end-to-end driving and traditional engineering stacks.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

End-to-end driving approaches take the output of the sensors (e.g., LiDAR, images) and use it as input to a neural net that outputs control signals, e.g., steering command and acceleration. The main benefit of this framework is its simplicity as only a few lines of code can build a model and labeled training data can be easily obtained automatically by recording human driving under a SDV platform. In practice, this approach suffers from the compounding error due to the nature of self-driving control being a sequential decision problem, and requires massive amounts of data to generalize. Furthermore, interpretability is difficult to obtain for analyzing the mistakes of the network. It is also hard to incorporate sophisticated prior knowledge about the scene, e.g. that vehicles should not collide.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, most self-driving car companies, utilize a traditional engineering stack, where the problem is divided into subtasks: perception, prediction, motion planning and control. Perception is in charge of estimating all actors' positions and motions, given the current and past evidences. This involves solving tasks such as 3D object detection and tracking. Prediction^11^1We'll use prediction and motion forecasting interchangeably., on the other hand, tackles the problem of estimating the future positions of all actors as well as their intentions (e.g., changing lanes, parking). Finally, motion planning takes the output from previous stacks and generates a safe trajectory for the SDV to execute via a control system. This framework has interpretable intermediate representations by construction, and prior knowledge can be easily exploited, for example in the form of high definition maps (HD maps).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, solving each of these sub-tasks is not only hard, but also may lead to a sub-optimal overall system performance. Most self-driving companies have large engineering teams working on each sub-problem in isolation, and they train each sub-system with a task specific objective. As a consequence, an advance in one sub-system does not easily translate to an overall system performance improvement. For instance, 3D detection tries to maximize AP, where each actor has the same weight. However, in a driving scenario, high-precision detections of near-range actors who may influence the SDV motion, e.g. through interactions (cutting, sudden stopping), is more critical. In addition, uncertainty estimations are difficult to propagate and computation is not shared among different sub-systems. This leads to longer reaction times of the SDV and make the overall system less reliable.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we bridge the gap between these two frameworks. Towards this goal, we propose the first end-to-end learnable and interpretable motion planner. Our model takes as input LiDAR point clouds and a HD map, and produces interpretable intermediate representations in the form of 3D detections and their future trajectories. Our final output representation is a space-time cost volume that represents the "goodness" of each location that the SDV can take within a planning horizon. Our planner then samples a set of diverse and feasible trajectories, and selects the one with the minimum learned cost for execution. Importantly, the non-parametric cost volume is able to capture the uncertainty and multi-modality in possible SDV trajectories, e.g changing lane v.s keeping lane.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate the effectiveness of our approach in real world driving data captured in several cities in North America. Our experiments show that our model provides good interpretable representations, and shows better performance. Specifically for detection and motion forecasting, our model outperforms recent neural architectures specifically designed on these tasks. For motion planning, our model generates safer planning compared to the baselines.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Deep Structured Interpretable Planner", "weight": 1.0} -->

We propose an end-to-end learnable motion planner that generates accurate space-time trajectories over a planning horizon of a few seconds. Importantly, our model takes as input LiDAR point clouds and a high definition map and produces interpretable intermediate representations in the form of 3D detections and their future motion forecasted over the planning horizon. Our final output representation is a space-time cost volume that represents the "goodness" of each possible location that the SDV can take within the planning horizon. Our planner then scores a series of trajectory proposals using the learned cost volume and chooses the one with the minimum cost.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Deep Structured Interpretable Planner", "weight": 1.0} -->

We train our model end-to-end with a multi-task objective. Our planning loss encourages the minimum cost plan to be similar to the trajectory performed by human demonstrators. Note that this loss is sparse as a ground-truth trajectory only occupies small portion of the space. As a consequence, learning with this loss alone is slow and difficult. To mitigate this problem, we introduce an another perception loss that encourages the intermediate representations to produce accurate 3D detections and motion forecasting. This ensures the interpretability of the intermediate representations and enables much faster learning.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Deep Structured Planning", "weight": 1.0} -->

More formally, let $\mathbf{s} = {\{\mathbf{s}^{0},\mathbf{s}^{1},\cdots,\mathbf{s}^{T - 1}\}}$ be a trajectory spanning over $T$ timesteps into the future, with $\mathbf{s}^{t}$ the location in bird's eye view (BEV) at the timestep $t$. We formulate the planning problem as a deep structured minimization problem as follows

<!-- chunk {"id": "body-0012", "role": "body", "section": "Deep Structured Planning", "weight": 1.0} -->

where $c^{t}$ is our learned cost volume indexed at the timestep $t$, which is a 2D tensor with the same size as our region of interest. This minimization is approximated by sampling a set of physically valid trajectories s, and picking the one with minimum cost. Our model employs a convolutional network backbone to compute this cost volume. It first extracts features from both LiDAR and maps, and then feeds this feature map into two branches of convolution layers that output 3D detection and motion forecasting as well as the planning cost volume respectively. In this section we describe our input representation and network in details.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Input representation", "weight": 1.0} -->

Our approach takes raw point clouds as inputs, captured by a LiDAR mounted on top of the SDV. We employ $T^{\prime} = 10$ consecutive sweeps as observations, in order to infer the motion of all actors. For those sweeps, we correct for ego-motion and bring the point clouds from the past 10 frames to the same coordinate system centered at SDV's current location. To make the input data amenable to standard convolutions, we follow and rasterize the space into a 3D occupancy grid, where each voxel has a binary value indicating whether it contains a LiDAR point. This results in a 3D tensor of size $H$x$W$x$({ZT^{\prime}})$, where $Z,H,W$ represents the height and x-y spatial dimensions respectively. Note that we have concatenated timesteps along the $Z$ dimension, thus avoiding 3D convolutions which are memory and computation intensive.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Input representation", "weight": 1.0} -->

Access to a map is also a key for accurate motion planning, as we need to drive according to traffic rules (e.g., stop at a red light, follow the lane, change lanes only when allowed). Towards this goal, we exploit HD maps that contain information about the semantics of the scene such as the location of lanes, their boundary type (e.g., solid, dashed) and the location of stop signs. Similar to, we rasterize the map to form an $M$ channels tensor, where each channel represents a different map element, including road, intersections, lanes, lane boundaries, traffic lights, etc. Our final input tensor is thus of size $H$x$W$x$({{ZT^{\prime}} + M})$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Backbone", "weight": 1.0} -->

Our backbone is adapted from the detection network of and consists of five blocks. Each block has {2, 2, 3, 6, 5} Conv2D layers with filter number {32, 64, 128. 256, 256}, filter size 3x3 and stride 1. There are MaxPool layers after each of the first 3 blocks. A multi-scale feature map is generated after the first 4 blocks as follows. We resize the feature maps from each of the first 4 blocks to 1/4 of the input size and concatenate them together similar to, in order to increase the effective receptive field. These multi-scale features are then fed into the $5$-th block. The whole backbone has a downsampling rate of 4.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Perception Header", "weight": 1.0} -->

The perception header has two components formed of convolution layers, one for classification and one for regression. To reduce the variance of regression targets, we follow SSD and employ multiple predefined anchor boxes $a_{i,j}^{k}$ at each feature map location, where subscript $i,j$ denotes the location on the feature map and $k$ indexes over the anchors. In total, there are 12 anchors at each location, with different sizes, aspect ratios and orientations. The classification branch outputs a score $p_{i,j}^{k}$ for each anchor indicating the probability of a vehicle at each anchor's location. The regression branch also outputs regression targets for each anchor $a_{i,j}^{k}$ at different time-steps. This includes localization offset $l_{x}^{t},l_{y}^{t}$, size $s_{w}^{t},s_{h}^{t}$ and heading angle $a_{sin}^{t},a_{cos}^{t}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Perception Header", "weight": 1.0} -->

The superscript $t$ stands for time frame, ranging from $0$ (present) to $T - 1$ into the future. Regression is performed at every timesteps, thus producing motion forecasting for each vehicle.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Cost Volume Head", "weight": 1.0} -->

The cost volume head consists of several convolution and deconvolution layers. To produce a cost volume $c$ at the same resolution as our bird-eye-view (BEV) input, we apply two deconvolution layers on the backbone's output with filter number {128, 64}, filter size 3x3 and stride 2. Each deconvolution layer is also followed by a convolution layer with filter number {128, 64}, filter size 3x3 and stride 1. We then apply a final convolution layer with filter number $T$, which is our planning horizon. Each filter generates a cost volume $c^{t}$ for a future timestep $t$. This allows us to evaluate the cost of any trajectory $\mathbf{s}$ by simply indexing in the cost volume $c$. In our experiments, we also clip the cost volume value between -1000 to +1000 after the network. Applying such bounds prevents the cost value shifting arbitrarily, and makes tuning hyper-parameters easier. We next describe our output trajectory parameterization.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Efficient Inference", "weight": 1.0} -->

Given the input LiDAR sweeps and the HD map, we can compute the corresponding cost volume $c$ by feedforward convolutional operations as describe above. The final trajectory can then be computed by minimizing Eq.. Note, however, that this optimization is NP hard^22^2We expect the output trajectory of our planner is physically feasible. This introduces constraints on the solution set. Under these physical constraints, the optimization is NP hard.. We thus rely on sampling to obtain a low cost trajectory. Towards this goal, we sample a wide variety of trajectories that can be executed by the SDV and produce as final output the one with minimal cost according to our learned cost volume. In this section we describe how we efficiently sample physically possible trajectories during inference. Since the cost of a trajectory is computed by indexing from the cost volume, our planner is fast enough for real-time inference.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Output Parameterization", "weight": 1.0} -->

A trajectory can be defined by the combination of the spatial path (a curve in the 2D plane) and the velocity profile (how fast we go along this path). Sampling a trajectory as a set of points in ${(x,y)} \in \Re^{2}$ space is not a good idea, as a vehicle cannot execute all possible set of points in the cartesian space. This is due for example to the physical limits in speed, acceleration and turning angle. To consider these real-world constraints, we impose that the vehicle should follow a dynamical model. In this paper, we employ the bicycle model, which is widely used for planning in self-driving cars. This model implies that the curvature $\kappa$ of the vehicle's path is approximately proportional to the steering angle $\phi$ (angle between the front wheel and the vehicle): ${\kappa = {{2tan{(\phi)}}/L} \approx {{2\phi}/L}},$ where $L$ is the distance between the front and rear axles of the SDV. This is a good approximation as $\phi$ is usually small.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Output Parameterization", "weight": 1.0} -->

We then utilize a Clothoid curve, also known as Euler spiral or Cornu spiral, to represent the 2D path of the SDV. We refer the reader to Fig. 2 for an illustration. The curvature $\kappa$ of a point on this curve is proportional to its distance $\xi$ alone the curve from the reference point, i.e., ${\kappa{(\xi)}} = {\pi\xi}$. Considering the bicycle model, this linear curvature characteristic corresponds to steering the front wheel angle with constant angular velocity. The canonical form of a Clothoid can be defined as

<!-- chunk {"id": "body-0022", "role": "body", "section": "Output Parameterization", "weight": 1.0} -->

Here, $\mathbf{s}{(\xi)}$ defines a Clothoid curve on a 2D plane, indexed by the distance $\xi$ to reference point $\mathbf{s}_{\mathbf{0}}$, $a$ is a scaling factor, $\mathbf{T}_{\mathbf{0}}$ and $\mathbf{N}_{\mathbf{0}}$ are the tangent and normal vector of this curve at point $\mathbf{s}_{\mathbf{0}}$. $S{(\xi)}$ and $C{(\xi)}$ are called the Fresnel integral, and can be efficiently computed.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Output Parameterization", "weight": 1.0} -->

In order to fully define a trajectory, we also need a longitudinal velocity $\overset{˙}{\xi}$ (velocity profile) that specifies the SDV motion along the path $\mathbf{s}{(\xi)}$: ${{\overset{˙}{\xi}{(t)}} = {{\overset{¨}{\xi}t} + {\overset{˙}{\xi}}_{0}}},$ where ${\overset{˙}{\xi}}_{0}$ is the initial velocity of the SDV and $\overset{¨}{\xi}$ is a constant forward acceleration. Combining this and, we can obtain the trajectory points $\mathbf{s}$ in Eq..

<!-- chunk {"id": "body-0024", "role": "body", "section": "Sampling", "weight": 1.0} -->

Since we utilize Clothoid curves, sampling a path corresponds to sampling the scaling factor $a$ in Eq.. Considering the city driving speed limit of 15m/s, we sample $a$ uniformly from the range of 6 to 80m. Once $a$ is sampled, the shape of the curve is fixed.^33^3We also sample a binary random variable indicating it's a canonical Clothoid or a vertically flipped mirror. They correspond with turning left or right respectively. We then use the initial SDV's steering angle (curvature) to find the corresponding position on the curve. Note that Clothoid curves cannot handle circle and straight line trajectories well, thus we sample them separately. The probability of using straight-line, circle and Clothoid curves are 0.5, 0.25, 0.25 respectively. Also, we only use a single Clothoid segment to specify the path of SDV which we think is enough for the short planning horizon.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Sampling", "weight": 1.0} -->

In addition, we sample constant accelerations $\overset{¨}{\xi}$ ranging from $- {{5m}/s^{2}}$ to ${5m}/s^{2}$ which specifies the SDV's velocity profile. Combining sampled curves and velocity profiles, we can project the trajectories to discrete timesteps and obtain the corresponding waypoints (See Fig 2) for which to evaluate the learned cost.

<!-- chunk {"id": "body-0026", "role": "body", "section": "End-to-End Learning", "weight": 1.0} -->

Our ultimate goal is to plan a safe trajectory while following the rules of traffic. We want the model to understand where obstacles are and where they will be in the future in order to avoid collisions. Therefore, we use a multi-task training with supervision from detection, motion forecasting as well as human driven trajectories for the ego-car. Note that we do not have supervision for cost volume. We thus adopt max-margin loss to push the network to learn to discriminate between good and bad trajectories.

<!-- chunk {"id": "body-0027", "role": "body", "section": "End-to-End Learning", "weight": 1.0} -->

This multi-task loss not only directs the network to extract useful features, but also make the network output interpretable results. This is crucial for self-driving as it helps understand failure cases and improves the system. In the following, we describe each loss in more details.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Perception Loss", "weight": 1.0} -->

Our perception loss includes classification loss, for distinguishing a vehicle from the background, and regression loss, for generating precise object bounding boxes. For each predefined anchor box, the network outputs a classification score as well as several regression targets. This classification score $p_{i,j}^{k}$ indicates the probability of existence of a vehicle at this anchor. We employ a cross-entropy loss for the classification defined as

<!-- chunk {"id": "body-0029", "role": "body", "section": "Perception Loss", "weight": 1.0} -->

where $q_{i,j}^{k}$ is the class label for this anchor (i.e., $q_{i,j}^{k} = 1$ for vehicle and $0$ for background). The regression outputs include information of position, shape and heading angle at each time frame $t$, namely

<!-- chunk {"id": "body-0030", "role": "body", "section": "Perception Loss", "weight": 1.0} -->

where superscript $a$ means anchor and $l$ means label. We use a weighted smooth L1 loss over all these outputs. The overall perception loss is

<!-- chunk {"id": "body-0031", "role": "body", "section": "Perception Loss", "weight": 1.0} -->

Note that the regression loss is summed over all vehicle correlated anchors, from the current time frame to our prediction horizon $T$. Thus it teaches the model to predict the position of vehicles at every time frame.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Perception Loss", "weight": 1.0} -->

To find the training label for each anchor, we associate it to its neighboring ground-truth bounding box, similar to. In particular, for each anchor, we find all the ground-truth boxes with intersection over union (IoU) higher than $0.4$. We associate the highest one among them to this anchor, and compute the class label and regression targets accordingly. We also associate any non-assigned ground-truth boxes with their nearest neighbor. The remaining anchors are treated as background, and are not considered in the regression loss. Note that one ground-truth box may associate to multiple anchors, but one anchor can at most be associated with one ground-truth box. During training, we also apply hard negative mining to overcome imbalance between positive and negative samples.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Planning Loss", "weight": 1.0} -->

Learning a reasonable cost volume is challenging as we do not have ground-truth. To overcome this difficulty, we minimize the max-margin loss where we use the ground-truth trajectory as a positive example, and randomly sampled trajectories as negative examples. The intuition behind is to encourage the ground-truth trajectory to have the minimal cost, and others to have higher costs. More specifically, assume we have a ground-truth trajectory $\{{(x^{t},y^{t})}\}$ for the next $T$ time steps, where $(x^{t},y^{t})$ is the position of our vehicle at the $t$ time step. Define the cost volume value at this point $(x^{t},y^{t})$ as ${\hat{c}}^{t}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Planning Loss", "weight": 1.0} -->

Then, we sample $N$ negative trajectories, the $i^{th}$ among which is $\{{(x_{i}^{t},y_{i}^{t})}\}$ and the cost volume value at these points are $c_{i}^{t}$. The sampling procedure for negative trajectories is similar as we described in Section. 3.2, except there is 0.8 probability that the negative sample doesn't obey SDV's initial states, e.g. we randomly sample a velocity to replace SDV's initial velocity. This will provide easier negative examples for the model to start. The overall max-margin loss is defined as

<!-- chunk {"id": "body-0035", "role": "body", "section": "Planning Loss", "weight": 1.0} -->

The inner-most summation denotes the discrepancy between the ground-truth trajectory and one negative trajectory sample, which is a sum of per-timestep loss. ${\lbrack\rbrack}_{+}$ represents a ReLU function. This is designed to be inside the summation rather than outside, as it can prevent the cost volume at one time-step from dominating the whole loss. $d_{i}^{t}$ is the distance between negative trajectory and ground-truth trajectory ${\|{{(x^{t},y^{t})} - {(x_{i}^{t},y_{i}^{t})}}\|}_{2}$, which is used to encourage negative trajectories far from the ground-truth trajectory to have much higher cost. $\gamma_{i}^{t}$ is the traffic rule violation cost, which is a constant if and only if the negative trajectory $t$ violates traffic rules at time $t$, e.g. moving before red-lights, colliding with other vehicles etc.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Planning Loss", "weight": 1.0} -->

This is used to determined how 'bad' the negative samples are, as a result, it will penalize those rule violated trajectories more severely and thus avoid dangerous behaviors. After computing the discrepancy between the ground-truth trajectory and each negative sample, we only optimize the worst case by the $\max$ operation. This encourages the model to learn a cost volume that discriminates good trajectories from bad ones.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we evaluate our approach on a large scale real-world driving dataset. The dataset was collected over multiple cities across North America. It consists of 6,500 scenarios with about 1.4 million frames, the training set consists of 5,000 scenarios, while validation and test have 500 and 1,000 scenarios respectively. Our dataset has annotated 3D bounding boxes of vehicles for every 100ms. For all experiments, we utilize the same spatial region, which is centered at the SDV, with 70.4 meters both in front and back, 40 meters to the left and right, and height from -2 meters to 3.4 meters. This corresponds to a 704x400x27 tensor. Our input sequence is 10 frames at 10Hz, while the output is 7 frames at 2Hz, thus resulting in a planning horizon of 3 seconds.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiments", "weight": 1.0} -->

In the following, we first show quantitative analysis on planning on a wide variety of metrics measuring collision, similarity to human trajectory and traffic rule violation. Next we demonstrate the interpretability of our approach, through quantitative analysis of detection and motion forecasting, as well as visualization of the learned cost volume. Last, we provide an ablation study to show the effects of different loss functions and different temporal history lengths.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Planning Results", "weight": 1.0} -->

We evaluate a wide variety of planning metrics. L2 Distance to Real Trajectory: This evaluates how far away the planned trajectory is from the real executed trajectory. Note that the real trajectory is just one of the many possible trajectories that a human could do, and thus this metric is not perfect. Future Potential Collision Rate: This is used to see if the planned trajectory will overlap with other vehicles in the future. For a given timestep t, we compute the percentage of occurrence of collisions up to time t, thus lower number is preferred. Lane Violation: this metric counts the percentage of planned trajectories crossing a solid yellow line. Note that lower is better, and here crossing is defined if the SDV touches the line.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Planning Results", "weight": 1.0} -->

We implement many baselines for comparison including: Ego-motion forecasting (Ego-motion): Ego-motion provides a strong cue of how the SDV would move in the future. This baselines takes only SDV's past position as input and uses a 4-layer MLP to predict the future locations. Imitation Learning (IL): We follow the imitation learning framework, and utilize a deep network to extract features from raw LiDAR data and rasterized map. For fair comparison, we use the same backbone described (Sec. 3.1) and same input parameterization (Sec. 3.1) than our approach. In addition, the same MLP from Ego-motion forecasting baseline is used to extract features from ego-motion. These two features are then concatenated and fed into a 3 layer MLP to compute the final prediction. Adaptive Cruise Control (ACC): This baseline implements the simple behavior of following the leading vehicle. The vehicle follows the lane center-line, while adaptively adjusting its speed to maintain a safe distance from the vehicle ahead. When there is no lead vehicle, a safe speed limit is followed.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Planning Results", "weight": 1.0} -->

Traffic controls (traffic lights, stop signs) are observed as a stationary obstacle, similar to a stopped lead vehicle. Plan w/ Manual Cost (Manual): This baselines uses the same trajectory parameterization and sampling procedure as our approach. However it utilizes a manually designed cost using perception and motion forecasting outputs. In detail, we rasterize all possible roads the SDV can take going forward and set it to a low cost of 0; all detected objects's bounding box defines area of a high cost set to 255; cost of any other area is set to a default value 100. This baseline is designed to show the effectiveness of our learned cost volume as it utilize the same sampling procedure as our approach but just a different cost volume.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Planning Results", "weight": 1.0} -->

As shown in Tab. 1, our approach has lower future collision rate at all timesteps by a large margin. Note that Ego-motion and IL baselines give lower L2 numbers as they optimize directly for this metric, however they are not good from planning perspective as they have difficulty reasoning about other actors and collide frequently with them. Comparing to the manual cost baseline and ACC, we achieve both better regression numbers and better collision rates, showing the advantage of our learned cost volume over manual a designed cost. For lane violation, ACC is designed to follow the lane, thus it has about 0 violation by definition. Comparing to other baselines, we achieve much smaller violation number, showing our model is able to reason and learn from the map.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Interpretability", "weight": 1.0} -->

Interpretability is crucial for self-driving as it can help understand failure cases. We showcase the interpretability of our approach by showing quantitative results on 3D detection and motion forecasting and visualization our learned cost-map for all timesteps into the future.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Detection", "weight": 1.0} -->

We compare against several state-of-the-art real-time detectors, validating that our holistic model understand the environment. Our baselines include a MobileNet adapted, FaF, IntentNet and Pixor, which are specifically designed for LiDAR-based 3D object detection. The metric is mAP with different IoU thresholds, and vehicles without LiDAR points are not considered. As shown in Tab. 4, our model archives best results on 0.7 IoU threshold, which is the metric of choice for self-driving. Qualitative results can also be found in Fig. 3.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Motion Forecasting", "weight": 1.0} -->

Tab. 2 shows quantitative motion forecasting results, including L1 and L2 distance to ground-truth locations. We also provides the L2 distance from our predictions to the ground-truth position along and perpendicular to the ground-truth trajectory. These help explain if the error is due to wrong velocity or direction estimation. We use baselines, which are designed for motion forecasting with raw LiDAR data. Our model performs better in all metric and all time steps. Note that IntentNet uses high-level intentions as additional information for training. Qualitative results are shown in Fig.3.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Cost Map Visualization", "weight": 1.0} -->

In Fig. 3, we visualize a few different driving scenarios. Each figure gives a top-down view of the scene, showing the map, LiDAR point clouds, detection, motion forecasting and planning results including learned cost map. Each figure represents one example, where we overlay the cost map from different timesteps. We use different color to represent the lower cost region for different timesteps (indicated by color legend). As we can see, our model learns to produce a time-dependent cost map. In particular, the first column demonstrates multi-modality, second column shows lane-following in heavy traffic and the last column shows collision avoidance.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

We conduct ablation studies and report the results in Table 3. Our best model is Model 5, comparing to Model 1 which is optimized only for detection and motion forecasting, it achieves similar performance in terms of detection and motion forecasting. Model 2 trains directly with planning loss only, without the supervision of object bounding boxes and performs worse. Model 3 exploits different input length, where longer input sequence gives better results. Model 4 is trained without the traffic rule penalty $\gamma$ in Eq. 8. It performs worse on planning, as it has no prior knowledge to avoid collision.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have proposed a neural motion planner that learns to drive safely while following traffic rules. We have designed a holistic model that takes LiDAR data and an HD map and produces interpretable intermediate representations in the form of 3D detections and their future trajectories, as well as a cost map defining the goodness of each position that the self-driving car can take within the planning horizon. Our planer then sample a set of physically possible trajectories and chooses the one with the minimum learned cost. We have demonstrated the effectiveness of our approach in very complex real-world scenarios in several cities of North America and show how we can learn to drive accurately.
