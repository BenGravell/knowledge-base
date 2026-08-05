<!-- arxiv-full-text:v1 {"arxiv_id": "2101.06554", "source": "ar5iv"} -->

## Introduction

Self-driving has recently benefited from deep learning breakthroughs, which have enhanced the performance of autonomy systems significantly. The performance achieved by these systems is tightly coupled to the quality, size and richness of training datasets. Furthermore, as self-driving is a safety critical application it is very important to have a diverse set of testing scenarios that are representative of driving.

Collecting data is a fairly easy process -- a single vehicle can generate several Tb of data a day. However, it is not feasible to label everything that has been collected. For instance, it could cost around \$150K^11^1scale.com to simply annotate the bounding-box of objects in one hour of camera data, assuming average density of 50 objects per image. Hence, it is of key importance to have a mechanism to identify "what to label" such that we can get the most relevant labeled dataset to achieve the highest autonomy performance given a labeling budget.

One of the most relevant areas of research in this spirit is active learning, which has been used as a mechanism to identify interesting examples to label. However, active learning approaches are tied to a model solving a given task^22^2We consider an ensemble to be a model belonging to a specific model class, while in our setting many tasks need to be performed -- a self-driving car needs to perceive the world, predict the future trajectory of all the actors in the scene and perform safe motion planning. Furthermore, the assumption in active learning approaches is that the model is fixed and we are interested in improving its performance via additional labels. However, in current modern self-driving approaches the autonomy stack is constantly changing, and as a consequence, examples that might be informative to label a few weeks ago might not be interesting anymore under the evolution of the perception, and motion forecasting modules. As a consequence, existing self-driving benchmarks have not been created by using active learning, but instead by exploiting random sampling, handcrafted set of heuristics, or manual selection.

In this paper we look at this task with a new lens and define specific criteria to quantize interestingness in order to identify a dataset of challenging and diverse scenarios for self-driving tasks. These criteria are not bound to a specific autonomy architecture or model and does not require multiple iterations of training and evaluation. More specifically, we propose a set of complexity measures to characterize self-driving scenarios. These measures include various factors such as the map, static and dynamic objects surrounding the ego-vehicle, and the executed trajectory of the data collection platform as well as the possible interactions it performs with other road-users. We then utilize these complexity measures inside a novel data selection approach to curate challenging and diverse dataset of traffic scenes. Through extensive experiments using various models in the literature, that such curation approach leads to better generalization of a wide variety of models in different autonomy tasks. More specifically, we show average 6.5% improvement in performance of various perception models and average 6% improvement in motion forecasting models from the recent state-of-the-art compared to other approaches such as active learning.

## Related Work

### Data Selection

Finding hard examples has been used to train models more effectively. In an active training set is maintained and is iteratively updated during training by removing easy examples and adding harder ones based , e.g., classification margins. In hard examples are mined online at ROI level for object detection task. However such methods deal with data that is already labeled.

Data selection has been studied in the active learning literature where batches of unlabeled data are selected for labeling by iteratively training a model on the labeled set and finding informative unlabeled data. Uncertainty-based methods select difficult examples by considering entropy in predicted distributions, uncertainty across a model ensemble or the estimated loss of each example. To avoid training a full model multiple times, proposed to use a simpler model as a proxy to perform efficient data selection. The proxy model can be either a simpler architecture or the original model trained with fewer iterations. Diversity-based approaches aim to select a subset of the unlabeled pool that best represents the entire dataset. describes an scalable production system for active learning in object detection where various scoring and sampling strategies are compared.

Semi-supervised active learning frameworks has also been proposed recently. In labeled data as well as the unlabeled ones are used during model training in each active learning cycle, for example by treating the most confident prediction for unlabeled data as pseudo label. Similarly in the model is trained with a usual loss on labeled data (e.g. cross-entropy) and a consistency loss on unlabeled data which penalize highly inconsistent predictions of slightly distorted samples of an example data.

Active learning and semi-supervised approaches above assume that the model is fixed and we are interested in improving its performance via additional labels. However, our work does not make this assumption since examples that might be informative to label a few weeks ago might not be interesting anymore under the evolution of the different self-driving stack modules.

### Self-driving Datasets

Many self-driving datasets have been released publicly in the past few years. Kitti, most notably, was the first benchmark with a dataset that included multiple sensors of LiDAR and camera supporting the tasks of stereo, optical flow, visual odometry, and 3D object detection. Citiscapes dataset includes annotated images from various cities in multiple seasons, suitable for semantic and instance segmentation. BDD100K dataset offers a diverse set of images that has been crowd-sourced with annotations such as 2D labels, lane markers and weather.

LiDAR sensor data particularly has rich 3D information making such datasets suitable for tasks of 3D detection and possibly tracking and motion forecasting. Waymo open dataset includes 2D/3D bounding boxes with camera and LiDAR data collected over large geographical and time of day extent. Argoverse also provides map rasters and graph with lane and intersection annotations. In order to create an interesting and challenging benchmark for trajectory forecasting task, they mine vehicles that are at intersection, performing a turn action or in dense traffic. nuSenes is the first dataset that includes radar data and supports tasks of 3D detection and tracking as well as behavior prediction. The scene selection is achieved manually to include dense traffic, rare classes, dangerous traffic situations, and difficult AV maneuvers. Other datasets include only sensor data without any human annotations of objects.

In contrast to the above mentioned works, we propose a method that combines a systematic semantic analysis of the raw data from all aspects relevant to driving: the complexity of the map, other actor motion and configurations, and last but not least the SDV pose and motion. We utilize these complexity measures in a framework that encourages not only challenging but a diverse selection to arrive at our curated dataset.

## Data Selection via Complexity Measures

In this section we propose a novel approach to decide which frames are more interesting to be labeled in order to create a rich and diverse dataset for training and evaluation. Towards this goal, we define a number of complexity measures driven by the static constructs in a driving scenario (e.g., lane topology, presence of an intersection), the traffic participants (e.g., other vehicles, pedestrians) and the maneuvers that the ego-car performs. Note that our data collection platform is a self-driving vehicle (SDV) and thus we will use these two terms interchangeably.

We assume the existence of a prebuilt HD Map for the areas that we will drive, a localization system that can localize the vehicle with respect to this map, as well as a perception software stack that can be ran on the collected raw data whose by product are object detections for each frame and their associated tracks that link those detections across time.

In the following, we first introduce our method to select challenging and diverse scenarios given a set of complexity measures. We then discuss in detail the complexity measures we exploit in our work.

### Data Selection

Our selection process operates at the snippet level (\\iea sequence of frames) instead of frame level. This allows observing phenomena that have a temporal component such as a lane-change or an interaction between actors, or the change in the speed of the SDV. Moreover, labeling a sequence of consecutive sensor data can be done more efficiently compared to to scattered individual frames. More formally, we define a snippet $s = \left\{ f_{i} \middle| {i = {0,\ldots,{T - 1}}} \right\}$ as a set of $T$ consecutive frames of data. In our experiments, each snippet represents 25 seconds of data with 250 frames. Throughout this paper, we will interchangeably refer to a snippet as a scenario. The purpose of the data selection process is then to pick $K$ non-overlapping snippets from the pool of unlabeled data.

We formulate the snippet selection as an optimization problem where first interesting scenarios are selected, and then the dataset is enhanced to be diverse and complete.

### Selecting Challenging Scenarios

In order to identify a set of challenging scenarios, we first rank the snippets using a scoring function $g$. In particular, we utilize a linear combination of the complexity measures as our "interestingness" score for a given snippet $s$ where $E{(s)}$ is the vector of complexity measures.

It is important to mention that what is considered to be challenging/interesting depends on the target task. F or example, imagine a scenario where the SDV is stopped at a busy intersection with a red light. As there are many interactions between actors, this is an interesting scenario for the tasks of perception and motion forecasting, however, for motion planning, this scenario may not be very useful as the SDV is not moving. On the other hand, there can be many scenarios where the SDV needs to interact with one or two actors of interest in an empty intersection, making this scenario interesting for planning and motion forecasting tasks, but not for detection. Therefore, we use different weight vector $w$ when ranking the snippets for each specific task.

We assume there are $n$ tasks and the goal is to select ${{c_{i},i} = 1},{\ldots,n}$ snippets for each task $i$. Therefore we will have the following optimization: where $\Psi$ is the set of all snippets, $w_{i}$ corresponds to the complexity weight vector specific for task $i$. The constraints simply makes sure there are no overlapping snippet within or across selected sets. Note that for our experiments, we consider two tasks: perception and motion forecasting (i.e. prediction). However, we still consider motion planning when we consider the distribution of the data, since as the downstream task it will have indirect affect on both perception and motion forecasting performance. We choose the weight vector for each task is tuned empirically.

We solve this optimization problem by first ranking all the snippets and then iteratively picking the next most "interesting" snippet from the queue and removing any overlapping one from the candidate set. We repeat this process for a fix number of iterations until we have reached a fixed budget.

### Selecting Diverse Scenarios

Limiting the data selection to only challenging scenarios will not necessarily lead to a diverse dataset, or to a complete set of scenarios that we might encounter in the real world. The goal of this additional selection step is to identify a set of snippets that ensures completeness and diversity. We quantize the dissimilarity between snippets as a function of their difference in the complexity measures, where in order to get geo-diversity we expand the complexity vectors with the latitude and longitude coordinates of the frames. We then iteratively look for the snippet that is farthest from the current selected set and added to the set to be labeled. In particular, at each iteration we select where $\Psi$ is the set of all unlabeled snippets, $\mathcal{S}$ is the set of already selected snippets, and $d$ is a dissimilarity function.

In order to capture diversity at a granular level, we have define the maximum difference between the closest pair, as our dissimilarity function between snippets where $k$, $l$ index over the frames of the $s_{i}$ and $s_{j}$ snippets respectively. The the full process of data selection is depicted in Algorithm 1.

1:procedure Select(Ψ, E, weight vectors wi for each task, desired number of snippets ki for each task, desired number of diverse snippets kd i v) 3:⊳ Select challenging scnarios 5: for each task j do 9:⊳ Select diverse scnarios Algorithm 1 Data Selection

### Complexity Measures

In order to characterize a traffic scene, we consider the map surrounding the location of the SDV and the detected objects within a region of intersect (ROI) around it. We also consider elements from the scenario that are directly related to the SDV maneuver.

Figure 1: Examples of the infrastructure-related complexity measures. In the top row, the path complexity measure of the lanes increases, from zero curvature to large varying curvature. in the bottom row, the map crossing measures indicates the complexity of the lane-graph topology as can be seen in the scene visualizations.

### Infrastructure-related Complexity Measures

We utilize a diverse set of complexity measures related to the static part of the environment. This contains information about how the vehicles might drive in the scene, the presence of intersections as well as traffic control elements and other road elements such as bike lanes and crosswalk.

### Geometry and topology of driving paths

We define driving paths as a plane curve in ${\mathbb{R}}^{2}$, representing the center-line of the map lanes. A driving path of constant curvature is a straight line or a circle and a vehicle can follow such path simply with a constant steering wheel. On the other hand, paths with variable curvature require more complex steering as shown in Figure 1. We use this intuition to define the complexity of a path. Specifically, we represent a path, $C{(s)}$, as a finite set of $K$ way points sampled along its arc-length, $s$: $\mathcal{C} = \left\{ {C{(s_{i})}} \middle| {{0 \leq s \leq 1},{i = {0,\ldots,K}}} \right\}$. Using a finite-difference method, the curvature (and rate of change in curvature) can be computed for each way point, resulting in the set: $\mathcal{K}_{\mathcal{C}} = \left\{ {\kappa{(s_{i})}} \middle| {{0 \leq s \leq 1},{i = {0,\ldots,K}}} \right\}$. Finally, we propose to use the mean of curvature $\mu{(\mathcal{K}_{\mathcal{C}})}$, and the mean of its derivative, $\mu{({\overset{˙}{\mathcal{K}}}_{\mathcal{C}})}$, as the measure of complexity of the curve: The driving paths in the map can cross each other creating scenes where vehicles can have potentially conflicting goals, and hence interesting. We measure such complexity by $E^{\text{crossing}} = {\sum_{c}v_{c}}$ as with $v_{c}$ being the number of times a driving path $c$ is crossed by other lanes. Figure 1 shows various examples of lanes and their complexity measures.

### Intersections, traffic-lights, and signage

Traffic scenes are generally more interesting at intersections. Hence we consider whether the SDV is at an intersections or not, as well as the complexity of the topology of the intersection by counting the number of roads reaching the intersections and the number of lanes that exist at each road. Besides, we also compute the number of traffic-lights and other signage such as stop-signs or yield-signs.

### Bike-lanes and crosswalks

The existence of bike-lanes and how they interact with vehicle lanes can increase the complexity of a traffic scene. To capture this we use the same vehicle-lane geometry and topology measures mentioned above for bike-lanes. Similarly, we consider crosswalks and how they expand over the vehicle lanes.

### Drivable-area height variation

Driving on hilly areas can be more challenging compared to flat roads. We define an additional complexity as the height variance in the drivable surface, \\ie$E^{\text{height}} = {\sigma^{2}{(\mathcal{Z})}}$ where $\mathcal{Z}$ is a set representing the map height of points uniformly sampled on lanes.

### Traffic Participants

Other important aspects of a scenario are how crowded the scene is as well as the diversity of its actors. We thus define the following complexity measures.

### Crowdedness

We measure the number of objects in an ROI around the SDV to capture how crowded a traffic scene is, using the following: where $\mathcal{D}_{t}$ is the set of detections in frame $f_{t}$. We measure this separately for static and dynamic actors to have more granular information. Note that this does not measure how the object can potentially interact with SDV which will be covered by different complexity measures.

### Class and spatial diversity

Many interesting interactions can happen when there are multiple types of actors in a traffic scene. Some classes of actors (e.g. bicyclists) are orders of magnitude more rare than others (e.g., vehicles). We thus measure the diversity of actors: where ${}_{c}^{}\mathcal{D}_{t}^{}$ is the set of detections that belong to class $c$ in frame $f_{t}$. Figure 2 shows various traffic scenes and their actor class diversity measure. In addition we measure the variance of the distance to the SDV for those actors.

### Path and speed diversity

Up to now we have introduced measures related to the existence of certain actors. However, it is important to take into account how those actors move. Similar to the complexity of the driving-paths , we use the curvature of the path that each actor took, along with its first derivative to measure the complexity of the actor's behavior. This measure can capture many interesting events. For example a vehicle that is making a lane-change follows a path with high curvature change. Similarly, pedestrians the change the direction of their motion will lead to high path complexity. Such behaviors of actors will serve as rich examples for training prediction models.

The variation in the speed of actors can also add to the complexity of the traffic scene indicating an interesting interaction of an actor with another one, a traffic-control element, or can simply show an intention to change path. We define a measures reflecting the speed variance of an actor as well as the variance of the mean speed of all actors in a given scene: where $\omega_{i}$ is a discreet speeds computed for the $i^{\text{th}}$ actor and $\Omega$ is the set of average speeds for all the actors.

### SDV Maneuvers

Finally it is important to identify scenarios where the SDV performs complex maneuvers. We thus introduce the following measures to capture how interesting a scenario is as it relates to the SDV.

### Path and speed

We use the same measures of introduced for actors to obtain the complexity of the ego vehicle path and motion. Figure 2 shows various SDV trajectories and their speed and path complexities.

### Route

Some of the the high-level maneuvers of the ego vehicle are naturally less frequent that others, e.g. lane-change and turns v.s lane-following. Therefore, we count such maneuvers to measure the complexity of the SDV route. We also consider whether SDV interacts with traffic-lights or stop-signs while following the route.

### Interactions with other actors

We obtain the number of static and dynamic objects that are within distance to the SDV path as measure of how other objects affect SDV behavior. However distance is not always a sufficient measure. For example, vehicles that are waiting to make an unprotected left turns, or passing through and intersection controlled by stop-sign, may not be close to the ego path, but their behaviors affect SDV's decision and vice versa. To capture this, we measure the number of vehicles that pass through a lane that is in conflict with SDV route. We also count the vehicles that can reach such lanes within a short time horizon to capture potential actors interacting with SDV. Figure 2 shows an example of SDV interacting with another vehicle at an intersection.

### Nudging maneuvers

In some scenarios the SDV needs to partially move out of its lane and come back in order to pass an object or vehicle that is partially blocking the path. We specifically capture these maneuvers as they make the scenario very complex.

Figure 2: Examples of complexity measures related to the traffic participants and the SDV maneuver. The top row shows compares, for example, the static-crowd measure, increasing from left to right, v.s. the dynamic-crowd complexity measure. In the middle row, the class diversity measure increases from right to left, increasing the complexity of the traffic scene. It also indicates how the complexity of SDV path corresponds to the complexity of the scene. Lastly, in the bottom row the path and velocity taken by the actors become more complex from right to left, leading to increasingly more challenging scenarios for tasks such as motion forecasting.

## Experiments

### Experimental Setup

We use a very large labeled dataset that consists of 140 hours of manual driving data (20k+ snippets of 25s). The dataset is split into test and validation sets as well as a base training set $\Psi$, ensuring no geographical overlap and similar label distributions. Using our proposed approach (CR), random sampling (RN), and an active learning baseline (AL), we select two separate training sets of size 1,000 and 3,000 snippets from $\Psi$. Similarly, we we select 2 test sets out of the original test set: Easy which is selected randomly, and Hard, which is selected using our proposed approach. We train various perception and motion-forecasting models using the curated training sets, and evaluate them on the two test sets. Specifically for perception-only task we use PointPillars, and PointRCNN. Additionally, we use joint perception-prediction models of ILVM, MultiPath, and ESP in which both tasks are trained end-to-end.

### Metrics

For the perception task, we use mean average precision (mAP) to compare models. Note that this metrics is computed for each class of Vehicles, Bicycles, and Pedestrians. For motion forecasting we use the following metrics: mean average displacement error (meanADE), minimum average displacement error (minADE), and collision rate among actors. The motion prediction metrics are computed over 5s horizon, similar to how they are trained. Following, we evaluate prediction in true positive object detections at a common recall point across models. That means, we find the detection threshold for each model such that all of them are evaluated at the same recall point of the detection Precision-Recall curve.

### Active Learning Baseline (AL)

We compare our dataset curation method against an uncertainty-based active learning approach. More specifically, we select snippets with high entropy predictions generated by a trained prediction model. We use a prediction model with the same backbone as ILVM. However, in order to compute entropy easily, the header is replaced with a simplified model that outputs a distribution $p{(y)}$ with an independent 2D Gaussian for each actor $i$ and time-step $t$, Afterwards, for each frame, we can compute the entropy of the output distribution as, and sum the entropies across all frames in a snippet to obtain a final uncertainty score. Given the size of the base set $\Psi$, it is infeasible to iteratively re-train and re-score all examples more than once. Therefore, we train the prediction model initially on a random subset of $250$ snippets and then select the remaining snippets with the highest entropies to obtain datasets of size 1k and 3k snippets. Specific model details are available in the supplementary materials.

### Results

Table 1 shows the summary of all results where the metrics are averaged per model and object classes (macro-averaging). It is clear that our curation method outperforms the baselines on average in all tasks and training-set sizes. Specifically, in object detection we improve 7.5% and 6.3% in the Easy set over active learning respectively in 1k and 3k settings, and 7.8% and 6.7% in the Hard set. A similar trend is observed in the motion forecasting task. Compared to active learning, our approach gains 10.3% and 8% improvement in prediction metrics for 1k and 3k settings in the Easy test set, and 6.3% and 4% in the Hard set. The results indicate that using the data selected by our proposed method, we can achieve significantly better generalizations in various models and tasks in self-driving. In the following sections we present the result of each model for each task.

Table 1: Detection and Prediction results averaged over the models and actor classes.

### Detection

Table 2 shows the detection metrics for detection-only models a well as joint perception-prediction models. The results indicate that our approach consistently improves Bicycle detections significantly across all models and training set sizes. Similarly for Pedestrians, our approach leads to better mAP in majority of the models. Interestingly for Vehicle detection both our approach and random sampling show strong performance in the Hard test set across different models.

Table 2: Detection results

### Motion Prediction

Table 3 shows the motion forecasting results for various models and curation methods. Similar to detection task, we can see that our approach is performing significantly better across the majority of models for all classes. Specifically in ILVM model, active learning baseline outperforms our approach in some of the metrics. This can be expected as our active learning baseline uses the ILVM backbone for its prediction model. This example validates our assumption that even though active learning can be used to select informative examples to improve the performance of a model, the selected training set is not necessarily useful for training other models in the same or different tasks.

Another interesting metric for motion prediction is collision between the predicted trajectories of actors. Both ILVM and MultiPath prediction models generate trajectories at scene level, modeling the joint probability distribution among actor trajectories. As shown in the last column of Table 3, using our curated data, the models are able to generate more consistent predictions for actors.

Table 3: Prediction results

## Conclusion

In this paper we presented a dataset curation pipeline for self-driving to select unlabeled data for labeling. We described a set of intuitive complexity measures to characterize the traffic scene of the collected data wrt various aspects including the topology of the map, diversity and complexity of surrounding actors and their behaviors, and the executed maneuver of the SDV. We also presented a method to select interesting and challenging sections of the collected logs using the described measures together with adding diverse examples to the final selected set of scenarios. Through extensive experiments using various models for the main tasks of perception and prediction, we demonstrated the effectiveness of our curation strategy compared to active learning methods. We believe future extensionsof our method will be impactful in areas of robotics where complex perception, prediction and ego-action plays a significant role.
