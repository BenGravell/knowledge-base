<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

IntentNet: Learning to Predict Intention from Raw Sensor Data

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In order to plan a safe maneuver, self-driving vehicles need to understand the intent of other traffic participants. We define intent as a combination of discrete high-level behaviors as well as continuous trajectories describing future motion. In this paper, we develop a one-stage detector and forecaster that exploits both 3D point clouds produced by a LiDAR sensor as well as dynamic maps of the environment. Our multi-task model achieves better accuracy than the respective separate modules while saving computation, which is critical to reducing reaction time in self-driving applications.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Autonomous driving is one of the most exciting problems of modern artificial intelligence. Self-driving vehicles have the potential to revolutionize the way people and freight move. While a plethora of systems have been built in the past few decades, many challenges still remain. One of the fundamental difficulties is that self driving vehicles have to share the roads with human drivers, which can perform maneuvers that are difficult to predict.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Human drivers understand intention by exploiting the actors' past motion as well as prior knowledge about the scene (e.g. the location of lanes, direction of driving). Previous work attempted to solve this problem by first performing vehicle detection and then extracting intent from the position and motion of detected bounding boxes. This, however, restricts the information that the intent estimation module has access to, resulting in suboptimal estimates. Very recently, FaF directly exploited LiDAR sensor data to predict the future trajectories of vehicles. However, the trajectories were only predicted for 1 second into the future and no intent prediction was done beyond motion estimation.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we take this approach one step further and propose a novel deep neural network that reasons about both high level behavior and long term trajectories. Inspired by how humans perform this task, we design a network that exploits motion and prior knowledge about the road topology in the form of maps containing semantic elements such as lanes, intersections and traffic lights. In particular, our IntentNet is a fully-convolutional neural network that outputs three types of variables in a single forward pass corresponding to: detection scores for vehicle and background classes, high level action probabilities corresponding to discrete intention, and bounding box regressions in the current and future time steps to represent the intended trajectory. Our architecture allows us to jointly optimize all tasks, fixing the distribution mismatch problem between tasks when solving them separately. Importantly, our design also enables the system to propagate uncertainty through the different components. In addition, our approach is computationally efficient by design as all tasks share the heavy neural network feature computation.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate the effectiveness of our approach in the tasks of detection and intent prediction by showing that our system surpasses other real-time, state-of-the art detectors while outperforming previous intent prediction approaches, both in its continuous and discrete counterparts. In the remainder of the paper, we first discuss related work and then present our model followed by experimental evaluation and conclusion.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Object detection", "weight": 1.0} -->

Many proposal based approaches have been developed after the seminal work of RCNN. While these methods perform really well, they are typically not suitable for real-time applications as they are computationally demanding. In contrast, single stage detectors provide a more efficient solution. YOLO breaks down the image into grids and makes multi-class and multi-scale predictions at each cell. SSD added the notion of anchor boxes, which reduces object variance in size and pose. RetinaNet showed that single-stage detectors can outperform two-stage detectors in both speed and accuracy. Geiger et al. improved the ability to estimate object orientation by jointly reasoning about the scene layout. More recently, Vote3Deep proposed to voxelize point clouds and exploit 3D CNNs. Subsequently, FaF and PIXOR exhibited superior performance in terms of speed and accuracy by exploiting a bird's eye view representation. Additionally, aggregated several point clouds from the past. Approaches that use the projection representation (VeloFCN, MV3D ) or handle point clouds directly (PointNet ) have also been proposed. However, these methods suffer from either limited performance or heavy computation and thus are not suitable for self driving.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Object detection", "weight": 1.0} -->

Liang et al. proposed a real time 3D detector that exploits multiple sensors (i.e., camera and LiDAR).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Motion Forecasting", "weight": 1.0} -->

This refers to the task of predicting future locations of an actor given current and past information. DESIRE introduced an RNN encoder-decoder framework in the setting of multiple interacting agents in dynamic scenes. Ma et al. proposed to couple game theory and deep learning to model pedestrians interactions and estimate person-specific behavior parameters. Ballan et al. exploited the interplay between the dynamics of moving agents and the semantics of the scene for scene-specific motion prediction. Soo et al. created an EgoRetinal map to predict plausible future ego-motion trajectories in egocentric stereo images. Hoermann et al. utilized a dynamic occupancy grid map as input to a deep convolutional neural network to perform long-term situation prediction in autonomous driving. SIMP parametrized the output space as insertion areas where the vehicle of interest could go, predicting an estimated time of arrival and a spatial offset. Djuric et al. rasterized representations of each actor's vicinity in order to predict their future motion. FaF pioneered the unification of detection and short term motion forecasting from LiDAR point clouds in driving scenarios.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Intention Prediction", "weight": 1.0} -->

The intention of an actor can be seen as the sequence of actions it will take in order to achieve an objective. Fathi et al. developed a probabilistic generative model to predict daily actions using gaze. In the context of intelligent vehicles, Zhang et al. proposed to model high level semantics in the form of traffic patterns through a generative model that also reasons about the geometry and objects present in the scene. Jain et al. proposed an autoregressive HMM to anticipate driving maneuvers a few seconds before they occur by exploiting video from a face and a rear camera together with features from the map. Streubel et al. utilized HMMs to estimate the direction of travel while approaching a 4-way intersection. Kim et al. predicted egocentric intention of lane changes. Recently, Phillips et al. utilized LSTMs to predict cars' intention at generalizable intersections. SIMP suggested to model intention implicitly by defining a discrete set of insertion areas belonging to particular lanes. Unfortunately, most of the work in this area lacks solid evaluation.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Intention Prediction", "weight": 1.0} -->

For instance, used 1 hour of driving data across only 9 intersections for both training and evaluation (cross-validated), while apply the SIMP framework to only 640 meters of highway.\

<!-- chunk {"id": "body-0012", "role": "body", "section": "Intention Prediction", "weight": 1.0} -->

IntentNet is inspired by FaF, which performs joint detection and future prediction. IntentNet achieves a more accurate vehicle detection and trajectory forecasting, enlarges the prediction horizon and estimates future high-level driver's behavior. The key contributions to the performance gain are (i) a more suitable architecture based on an early fusion of a larger number of previous LiDAR sweeps, (ii) a parametrization of the map that allows our model to understand traffic constraints for all vehicles at once and (iii) an improved loss function that includes a temporal discount factor to account for the inherent ambiguity of the future.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Learning to Predict Intention", "weight": 1.0} -->

In this section, we present our approach to jointly detect vehicles and predict their intention directly from raw sensor data. Towards this goal, we exploit 3D LiDAR point clouds and dynamic HD maps containing semantic elements such as lanes, intersections and traffic lights. In the following, we describe our parametrization, network architecture, learning objective and inference procedure.

<!-- chunk {"id": "body-0014", "role": "body", "section": "3D point cloud", "weight": 1.0} -->

Standard convolutional neural networks (CNNs) perform discrete convolutions, assuming a grid structured input. Following, we represent point clouds in bird's eye view (BEV) as a 3D tensor, treating height as our channel dimension. This input parametrization has several key advantages: (i) computation efficiency due to dimensionality reduction (made possible as vehicles drive on the ground), (ii) non-overlapping targets (contrary to camera-view representations, where objects can overlap), (iii) preservation of the metric space (undistorted view) that eases the creation of priors regarding vehicle sizes, and (iv) this representation also makes the fusion of LiDAR and map features trivial as both are defined in bird's eye view. We utilize multiple consecutive LiDAR sweeps (corrected by ego-motion) as the past is fundamental to accurately estimate both intention and motion forecasting. We diverge from previous work and stack together height and time dimensions into the channel dimension as this allows us to use 2D convolutions to fuse time information. As shown in our experiments, this is more effective than the non-padded 3D convolutions proposed.

<!-- chunk {"id": "body-0015", "role": "body", "section": "3D point cloud", "weight": 1.0} -->

This gives us a tensor of size: $(\frac{L}{\DeltaL},\frac{W}{\DeltaW},{\frac{H}{\DeltaH} \cdot T})$, where $L$, $W$ and $H$ are the longitudinal, transversal and normal physical dimensions of the scene; $\DeltaL$, $\DeltaW$ and $\DeltaH$ are the voxel sizes in the corresponding directions and $T$ is the number of LiDAR sweeps.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Dynamic maps", "weight": 1.0} -->

We form a BEV representation of our maps by rasterization. We exploit static information including roads, lanes, intersections, crossings and traffic signs, in conjunction with traffic lights, which contain dynamic information that changes over time (i.e., traffic light state changes between green, yellow and red). We represent each semantic component in the map with a binary map (i.e., 1 or -1). Roads and intersections are represented as filled polygons covering the whole drivable surface. Lane boundaries are parametrized as poly-lines representing the left and right boundaries of lane segments. Note that we use three binary masks to distinguish lane types, as lane boundaries can be crossed or not, or only in certain situations. Lane surfaces are rasterized to distinguish between straight, left and right turns, as this information is helpful for intention prediction. We also use two extra binary masks for bike and bus lanes as a way to input a prior of non-drivable road areas. Furthermore, traffic lights can change the drivable region dynamically. We encode the state of the traffic light into the lanes they govern.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Dynamic maps", "weight": 1.0} -->

We rasterize the surface of the lane succeeding the traffic light in one out of three binary masks depending on its state: green, yellow or red. One extra layer is used to indicate whether those lanes are protected by its governing traffic light, i.e. cars in other lanes must yield. This situation happens in turns when the arrow section of the traffic light is illuminated. We estimate the traffic light states using cameras in our self-driving vehicle. We also infer the state of some unobserved traffic lights that directly interact with known traffic light states. For example, a straight lane with unknown traffic light state that collides with a protected turn with green traffic light state can be safely classified as being red. Lastly, traffic signs are also encoded into their governed lane segments, using two binary masks to distinguish between yields and stops. In total, there are 17 binary masks used as map features, resulting in a 3D tensor that represents the map. Fig. 1 shows an example, where different elements (e.g., lane markers in cyan, crossings in magenta, alpha blended traffic lights with their state colored) are depicted.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Output parametrization", "weight": 1.0} -->

Our model predicts drivers' intentions in both discrete and continuous form.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Trajectory regression", "weight": 1.0} -->

For each detected vehicle, we parametrize its trajectory as a sequence of bounding boxes, including current and future locations. Assuming cars are non-deformable objects, we treat their size ($w$, $h$) as a constant estimated by the detector. The pose in each time stamp is 3D and contains the bounding box center ($c_{x}^{t}$, $c_{y}^{t}$) and heading $\phi^{t}$ of the vehicle in BEV coordinates (see Fig. 3.3).

<!-- chunk {"id": "body-0020", "role": "body", "section": "High level actions", "weight": 1.0} -->

We frame the discrete intention prediction problem as a multi-class classification with 8 classes: keep lane, turn left, turn right, left change lane, right change lane, stopping/stopped, parked and other, where other can be any other action such as reversed driving.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Network architecture", "weight": 1.0} -->

Work across different domains has shown that late fusion delivers stronger performance than early fusion. IntentNet exploits a late fusion of LiDAR and map information through an architecture consisting of a two-stream backbone network and three task-specific branches on top (see Figs. 3.3 and 3.3).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Backbone network", "weight": 1.0} -->

Our single-stage model takes two 3D tensors as input: the voxelized BEV LiDAR and the rasterization of our dynamic maps. We utilize a two-stream backbone network, where two different 2D CNNs process each data stream separately. The feature maps obtained from those subcomponents are then concatenated along the depth dimension and fed to the fusion subnetwork. We use a small downsampling coefficient in our network of 8x since each vehicle represents a small set of pixels in BEV, e.g., when using a resolution of 0.2 m/pixel, a car on average occupies 18 x 8 pixels. To provide accurate long term intention prediction and motion forecasting, the network needs to extract rich motion information from the past and geometric details of the scene together with traffic rule information. Note that vehicles typically drive at 50 km/h in urban scenes, traversing 42 meters in only 3 seconds. Thus we need our network to have a sufficiently large effective receptive field to extract the desired information. To keep both coarse and fine grained features, we exploit residual connections. We refer the reader to Fig. 3.3 for more details of our network architecture.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Header network", "weight": 1.0} -->

The header network is composed of three task specific branches that take as input the shared features from the backbone network. The detection branch outputs two scores for each anchor box at each feature map location, one for vehicle and one for background. An anchor is a predefined bounding box with orientation that serves as a prior for detection. Similar to, we use multiple anchors for each feature map location. The intention network performs a multi-class classification over the set of high level actions, assigning a calibrated probability to the 8 possible behaviors at each feature map location. The discrete intention scores are in turn fed into an embedding convolutional layer to provide extra features to condition the motion estimation. The motion estimation branch receives the concatenation of the shared features and the embedding from the high level action scores, and outputs the predicted trajectories for each anchor box at each feature map location.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Learning", "weight": 1.0} -->

Our model is fully differentiable and thus can be trained end-to-end through back-propagation. In particular, we minimize a multi-task loss containing a regression term for the trajectory prediction over $T$ time steps, a binary classification term for the detection (background vs vehicle) and a multi-class classification for discrete intention. Thus

<!-- chunk {"id": "body-0025", "role": "body", "section": "Learning", "weight": 1.0} -->

where $t = 0$ is the current frame and $t > 0$ the future, $\theta$ the model parameters and $\lambda$ a temporal discount factor to ensure distance times into the future do not dominate the loss as they are more difficult to predict. We mow define the loss functions we employ in more details.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Detection", "weight": 1.0} -->

where $i,j$ are the location indices on the feature map and $k$ is the index over the predefined set of anchor boxes; $q_{i,j,k}$ is the class true label and $p_{i,j,k;\theta}$ the predicted probability. We define as positive samples, i.e. $q_{i,j,k} = 1$, those predefined anchor boxes having an associated ground truth box. In particular, for each anchor box, we find the ground truth box with the biggest intersection over union (IoU). If the IoU is bigger than a threshold of 0.5, we assign 1 to its corresponding label $q_{i,j,k}$. In case there is a ground truth box that has not been assigned to any anchor box, we assign it to the highest overlapping anchor box ignoring the threshold. Due to the imbalance of positive and negative samples we have found it helpful to not only use focal loss but also to apply hard negative mining during training.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Detection", "weight": 1.0} -->

Thus, we rank all negative samples by their predicted score $p_{i,j,k}$ and take the top negative samples with a ratio of 3:1 with respect to the number of positive samples.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Trajectory regression", "weight": 1.0} -->

We frame the detector regression targets as a function of the dimensions of their associated anchor boxes. As we reason in BEV, all objects have similar size as no perspective effect is involved. Thus, we can exploit object shape priors and make anchor boxes similar to real object sizes. This helps reduce the variance of the regression targets, leading to better training. In particular, we define

<!-- chunk {"id": "body-0029", "role": "body", "section": "Trajectory regression", "weight": 1.0} -->

We apply a weighted smooth L1 loss to the regression targets associated to the positive samples only. Note that for the future time steps ($t\epsilon{\lbrack 1,{T - 1}\rbrack}$), the target set $\mathcal{R}_{t}$ does not include the bounding box size ($\overline{w}$, $\overline{h}$), which are only predicted at the current time step ($t = 0$).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Trajectory regression", "weight": 1.0} -->

where $t$ is the prediction time step, $x_{r;\theta}^{t}$ refers to the predicted value of the $r$-th regression target, $y_{r}^{t}$ is the ground truth value of such regression target, and $\chi_{r}$ is the weight assigned to the r-th regression target.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Intention prediction", "weight": 1.0} -->

We employ a cross entropy loss over the set of high level actions. To address the high imbalance in the intention distribution, we downsample the dominant classes {keep lane, stopping/stopped and parked} by 95%. We found this strategy to work better than re-weighting the loss by the inverse frequency in the training set. Note that we do not discard those examples for detection and trajectory regression.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Inference", "weight": 1.0} -->

During inference, IntentNet produces 3D detections with their respective continuous and discrete intentions for all vehicles in the scene in a single forward pass. Preliminary detections are extracted by applying a threshold of 0.1 to the classification probabilities, with the intention of achieving high recall. From these feature map locations, we examine the regression targets and anchor boxes, and use NMS to de-duplicate detections. Since our model can predict future waypoints for each vehicle, it provides a strong prior for associating detections among different time steps. At any time step, we have a detection from the current forward pass and predictions produced at previous time steps. Therefore, by comparing the current location against past predictions of the future, we decode tracklets for each vehicle in the scene. This simple tracking system proposed in FaF also allows us to recover missing false negatives and discard false positives by updating the classification scores based on previous predictions.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

We evaluate our approach in the tasks of detection, intention prediction and motion forecasting. To enable this, we collected a large scale dataset from a roof-mounted LiDAR on top of a self-driving vehicle driving around several cities in North America. It contains over 1 million frames collected from over 5,000 different scenarios, which are sequences of 250 frames captured sequentially at 10 Hz. Our labels are tracklets of 3D non-axis align bounding boxes. The dataset is highly imbalanced and thus challenging, containing the following number of examples of each behavior; keep lane: 10805k, turn left: 546k, turn right: 483k, left change lane: 290k, right change lane: 224k, stopping/stopped: 12766k, parked: 29110k and others: 100k.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Implementation details", "weight": 1.0} -->

We use a birds eye view (BEV) region with $L = 144$, $W = 80$ meters from the center of the autonomous vehicle and $H = 5.8$ meters from the ground, for both training and evaluation. We set the resolution to be ${\DeltaL} = {\DeltaW} = {\DeltaH} = 0.2$ meters. We use $T = 10$ past LiDAR sweeps to provide enough context in order to perform accurate long term prediction of 3 seconds. Thus, our input is a 3D tensor of shape $({29 \cdot 10},720,400)$. We use 5 predefined anchor boxes of size 3.2 meters and $1:{1,1}:{2,2}:{1,1}:{6,6}:1$, and a threshold of 0.1 for the classification score to consider a detection positive during inference. We train our model from scratch using Adam optimizer, a learning rate of 1e-4 and a weight decay of 1e-4. We employ a temporal discount factor $\lambda = 0.97$ for our future predictions.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Implementation details", "weight": 1.0} -->

We used a batch of size 6 for each GPU and perform distributed training on 8 Nvidia 1080 GPUs for around 24h.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Detection results", "weight": 1.0} -->

We compare mean average precision (mAP) at different IoU levels with other object detectors that can also run inference in real-time (i.e., less than 100ms) including SqueezeNet, SSD, MobileNet, FaF and FaF' (adaptation of FaF where the motion forecasting header is trivially extended to predict 3 seconds). As shown in Table 4, our model is clearly superior across all IoU levels. Note that all models use the same anchor boxes and downsampling factor for the comparison to be consistent.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Detection results", "weight": 1.0} -->

L1 error along track (m)
L1 error across track (m)
L1 error heading (deg)

<!-- chunk {"id": "body-0038", "role": "body", "section": "Trajectory regression results", "weight": 1.0} -->

To the best of our knowledge, FaF is the only previous work that performs joint detection and motion forecasting from LiDAR. As shown in Table 1 IntentNet outperforms both FaF and FaF' in both along and across track errors as well as heading. The performance leap is a combination of network architecture improvements and the usage of prior knowledge in the form of maps. To be fair, the metrics are reported over the intersection of true positives of all the four models, which represents over 90 % of the validation set. In addition, Fig. 4 depicts regression metrics split by high level action. We highlight that IntentNet is able to learn complex velocity profiles such as the ones in turns and lane changes, keeping the along track error almost as low as in lane keeping.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Intention prediction", "weight": 1.0} -->

We compare our approach with the models proposed, adapting their classifiers to perform our task, which is a generalization of theirs. Phillips et al. extract several handcrafted features including base features such as velocity, acceleration, number of lanes to the curb and the median and headway distance to preceding vehicle, at the current time step; history features containing such information for previous time steps; traffic features containing up to six neighbours base features and rule features such as whether the car can turn left/right from its lane. We then train their model in our dataset. Table 2 shows the results of their two best performers models: an MLP and an LSTM. Our model clearly outperforms the baselines, especially on the less represented high level actions where the baselines are unable to recognize turns or lane changes. Note that we also tried applying the same downsampling method we use to the baselines but it resulted in worse overall performance and therefore was omitted here. As shown, IntentNet is able to generalize despite the extreme imbalance in the behavior distribution.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Ablation study", "weight": 1.0} -->

We conducted an ablation study in order to evaluate how much each of the contributions proposed in this paper helped towards achieving the final results, which is shown in Table 3. Using a 2D CNN with early fusion of the different LiDAR sweeps delivers a much robust detector, being able to understand the time dimension better than a 3D CNN as proposed. Increasing the context from 0.5 seconds to 1 second (5 to 10 input LiDAR sweeps) gives us a small gain, decreasing the long term L2 error. Notice that even though the detector is able to have higher recall while using the same confidence threshold (0.1), the regressions become better in average (even when taking into account those harder examples). Adding the loss for the discrete intention estimation degrades the detector/regressor performance due to the fact that it is very hard to predict behavior purely based on motion. However, after adding the map, the system is able to predict the high level behavior of vehicles and thus adding the loss improves general performance.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Qualitative results", "weight": 1.0} -->

Fig. 5 shows our results in the 144 x 80 meters region. We can see 3 pairs of frames belonging to different scenarios. We display the detections and continuous intent prediction in the top row and discrete intent prediction in the bottom row. Our model is able to predict lane changes and detect big size vehicles (left), have a high precision and recall in cluttered scenes (center) and predict turns (right).

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper we introduce IntentNet, a learnable end-to-end model that is able to tackle the tasks of detection and intent prediction of vehicles in the context of self-driving cars. By exploiting 3D point clouds produced by a LiDAR sensor and prior knowledge of the scene coming from an HD map, we are able to achieve higher performance than previous work across all tasks, with a single neural network. In the future, we plan to investigate how more sophisticated algorithms can model the statistical dependencies between discrete and continuous intention. We also plan to extend our approach to handle pedestrians and bicyclists.
