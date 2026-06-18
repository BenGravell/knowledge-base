<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Argoverse: 3D Tracking and Forecasting with Rich Maps

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present Argoverse - two datasets designed to support autonomous vehicle machine learning tasks such as 3D tracking and motion forecasting. Argoverse was collected by a fleet of autonomous vehicles in Pittsburgh and Miami. The Argoverse 3D Tracking dataset includes 360 degree images from 7 cameras with overlapping fields of view, 3D point clouds from long range LiDAR, 6-DOF pose, and 3D track annotations. Notably, it is the only modern AV dataset that provides forward-facing stereo imagery. The Argoverse Motion Forecasting dataset includes more than 300,000 5-second tracked scenarios with a particular vehicle identified for trajectory forecasting. Argoverse is the first autonomous vehicle dataset to include "HD maps" with 290 km of mapped lanes with geometric and semantic metadata. All data is released under a Creative Commons license at www.argoverse.org. In our baseline experiments, we illustrate how detailed map information such as lane direction, driveable area, and ground height improves the accuracy of 3D object tracking and motion forecasting. Our tracking and forecasting experiments represent only an initial exploration of the use of rich maps in robotic perception.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We hope that Argoverse will enable the research community to explore these problems in greater depth.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Datasets and benchmarks for a variety of perception tasks in autonomous driving have been hugely influential to the computer vision community over the last few years. We are particularly inspired by the impact of KITTI, which opened and connected a plethora of new research directions. However, publicly available datasets for autonomous driving rarely include *map* data, even though detailed maps are critical to the development of real world autonomous systems. Publicly available maps, *e.g*. OpenStreetMap, can be useful, but have limited detail and accuracy.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Intuitively, 3D scene understanding would be easier if maps directly told us which 3D points belong to the road, which belong to static buildings, which lane a tracked object is, how far it is to the next intersection, etc. But since publicly available datasets do not contain richly-mapped attributes, how to represent and utilize such features is an open research question. Argoverse is the first large-scale autonomous driving dataset with such detailed maps. We investigate the potential utility of these new map features on two tasks -- 3D tracking and motion forecasting, and we offer a significant amount of real-world, annotated data to enable new benchmarks for these problems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We release a large scale 3D tracking dataset with synchronized data from LiDAR, 360^∘^ and stereo cameras sampled across two cities in varied conditions. Unlike other recent datasets, our 360^∘^ is captured at 30fps.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide ground truth 3D track annotations across 15 object classes, with five times as many tracked objects as the KITTI tracking benchmark.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We create a large-scale forecasting dataset consisting of trajectory data for interesting scenarios such as turns at intersections, high traffic clutter, and lane changes.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We release map data and an API which can be used to develop map-based perception and forecasting algorithms. We are the first self-driving vehicle dataset with a semantic vector map of road infrastructure and traffic rules. The inclusion of "HD" map information also means our dataset is the first large-scale benchmark for automatic map creation, often known as map automation.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We are the first to examine the influence of HD map context for 3D tracking and motion forecasting. In the case of 3D tracking, we measure the influence of map-based ground point removal and orientation snapping to lanes. In the case of motion forecasting, we experiment with the creation of diverse predictions from the lane graph and the pruning of predictions by the driveable area map. In both cases, we see higher accuracy with the use of a map.

<!-- chunk {"id": "body-0011", "role": "body", "section": "The Argoverse Dataset", "weight": 1.0} -->

Our sensor data, maps, and annotations are the primary contribution of this work. We also provide an API which connects the map data with sensor information *e.g*. ground point removal, nearest centerline queries, and lane graph connectivity; see the Appendix for more details. The data is available at [www.argoverse.org](www.argoverse.org) under a Creative Commons license. The API, tutorials, and code for baseline algorithms are available at [github.com/argoai/argoverse-api](github.com/argoai/argoverse-api) under an MIT license. The statistics and experiments in this document are based on Argoverse v1.1 released in October 2019.

<!-- chunk {"id": "body-0012", "role": "body", "section": "The Argoverse Dataset", "weight": 1.0} -->

We collected raw data from a fleet of autonomous vehicles (AVs) in Pittsburgh, Pennsylvania, and Miami, Florida, both in the USA. These cities have distinct climate, architecture, infrastructure, and behavioral patterns. The captured data spans different seasons, weather conditions, and times of the day. The data used in our dataset traverses nearly 300 km of mapped road lanes and comes from a subset of our fleet operating area.

<!-- chunk {"id": "body-0013", "role": "body", "section": "The Argoverse Dataset", "weight": 1.0} -->

Sensors. Our vehicles are equipped with two roof-mounted, rotating 32 beam LiDAR sensors. Each LiDAR has a 40^∘^ vertical field of view, with 30^∘^ overlapping field of view and 50^∘^ total field of view with both LiDAR. LiDAR range is up to 200 meters, roughly twice the range as the sensors used in nuScenes and KITTI. On average, our LiDAR sensors produce a point cloud at each sweep with three times the density of the LiDAR sweeps in the nuScenes dataset (ours $\sim {107,000}$ points vs. nuScenes $\sim {35,000}$ points). The two LiDAR sensors rotate at 10 Hz and are out of phase, i.e. rotating in the same direction and speed but with an offset to avoid interference. Each 3D point is motion-compensated to account for ego-vehicle motion throughout the duration of the sweep capture. The vehicles have 7 high-resolution ring cameras recording at 30 Hz with overlapping fields of view, providing 360^∘^ coverage. In addition, there are 2 front-facing stereo cameras sampled at 5 Hz. Faces and license plates are procedurally blurred in camera data to maintain privacy.

<!-- chunk {"id": "body-0014", "role": "body", "section": "The Argoverse Dataset", "weight": 1.0} -->

Finally, 6-DOF localization for each timestamp comes from a combination of GPS-based and sensor-based localization. Vehicle localization and maps use a city-specific coordinate system described in more detail in the Appendix. Sensor measurements for particular driving sessions are stored in "logs", and we provide intrinsic and extrinsic calibration data for the LiDAR sensors and all 9 cameras for each log. Figure 1 visualizes our sensor data in 3D. Similar to, we place the origin of the ego-vehicle coordinate system at the center of the rear axle. All LiDAR data is provided in the ego-vehicle coordinate system, rather than in the respective LiDAR sensor coordinate frames. All sensors are roof-mounted, with a LiDAR sensor surrounded by 7 "ring" cameras (clockwise: facing front center, front right, side right, rear right, rear left, side left, and front left) and 2 stereo cameras. Figure 2 visualizes the geometric arrangement of our sensors.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Maps", "weight": 1.0} -->

Argoverse contains three distinct map components -- a vector map of lane centerlines and their attributes; a rasterized map of ground height, and a rasterized map of driveable area and region of interest (ROI).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Maps", "weight": 1.0} -->

Vector Map of Lane Geometry. Our vector map consists of semantic road data represented as a localized graph rather than rasterized into discrete samples. The vector map we release is a simplification of the map used in fleet operations. In our vector map, we offer lane centerlines, split into lane segments. We observe that vehicle trajectories generally follow the center of a lane so this is a useful prior for tracking and forecasting.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Maps", "weight": 1.0} -->

A lane segment is a segment of road where cars drive in single-file fashion in a single direction. Multiple lane segments may occupy the same physical space (*e.g*. in an intersection). Turning lanes which allow traffic to flow in either direction are represented by two different lanes that occupy the same physical space.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Maps", "weight": 1.0} -->

For each lane centerline, we provide a number of semantic attributes. These lane attributes describe whether a lane is located within an intersection or has an associated traffic control measure (Boolean values that are not mutually inclusive). Other semantic attributes include the lane's turn direction (left, right, or none) and the unique identifiers for the lane's predecessors (lane segments that come before) and successors (lane segments that come after) of which there can be multiple (for merges and splits, respectively). Centerlines are provided as "polylines", *i.e*. an ordered sequence of straight segments. Each straight segment is defined by 2 vertices: $(x_{i},y_{i},z_{i})$ start and $(x_{i + 1},y_{i + 1},z_{i + 1})$ end. Thus, curved lanes are approximated with a set of straight lines.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Maps", "weight": 1.0} -->

We observe that in Miami, lane segments that could be used for route planning are on average $3.84$ $\pm 0.89$ m wide. In Pittsburgh, the average width is $3.97$ $\pm 1.04$ m. Other types of lane segments that would not be suitable for self-driving, *e.g*. bike lanes, can be as narrow as $0.97$ m in Miami and as narrow as $1.06$ m in Pittsburgh.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Maps", "weight": 1.0} -->

Rasterized Driveable Area Map. Our maps include binary driveable area labels at 1 meter grid resolution. A driveable area is an area where it is possible for a vehicle to drive (though not necessarily legal). Driveable areas can encompass a road's shoulder in addition to the normal driveable area that is represented by a lane segment. We annotate 3D objects with track labels if they are within 5 meters of the driveable area (Section 3.2). We call this larger area our *region of interest* (ROI).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Maps", "weight": 1.0} -->

Rasterized Ground Height Map. Finally, our maps include real-valued ground height at 1 meter grid resolution. Knowledge of ground height can be used to remove LiDAR returns on static ground surfaces and thus makes the 3D detection of dynamic objects easier. Figure 3 shows a cross section of a scene with uneven ground height.

<!-- chunk {"id": "body-0022", "role": "body", "section": "3D Track Annotations", "weight": 1.0} -->

The *Argoverse Tracking Dataset* contains 113 vehicle log segments with human-annotated 3D tracks. These 113 segments vary in length from 15 to 30 seconds and collectively contain 11,052 tracked objects. We compared these with other datasets in Table 1. For each log segment, we annotated all objects of interest (both dynamic and static) with bounding cuboids which follow the 3D LiDAR returns associated with each object over time. We only annotated objects within 5 m of the *driveable area* as defined by our map. For objects that are not visible for the entire segment duration, tracks are instantiated as soon as the object becomes visible in the LiDAR point cloud and tracks are terminated when the object ceases to be visible. The same object ID is used for the same object, even if temporarily occluded. Each object is labeled with one of 15 categories, including ON_ROAD_OBSTACLE and OTHER_MOVER for static and dynamic objects that do not fit into other predefined categories. More than 70% of tracked objects are vehicles, but we also observe pedestrians, bicycles, mopeds, and more. Figure 4 shows the distribution of classes for annotated objects.

<!-- chunk {"id": "body-0023", "role": "body", "section": "3D Track Annotations", "weight": 1.0} -->

All track labels pass through a manual quality assurance review process. Figures Argoverse: 3D Tracking and Forecasting with Rich Maps and 1 show qualitative examples of our human annotated labels. We divide our annotated tracking data into 65 training, 24 validation, and 24 testing sequences.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Mined Trajectories for Motion Forecasting", "weight": 1.0} -->

We are also interested in studying the task of *motion forecasting* in which we predict the location of a tracked object some time in the future. Motion forecasts can be critical to safe autonomous vehicle motion planning. While our human-annotated 3D tracks are suitable training and test data for motion forecasting, the motion of many vehicles is relatively uninteresting -- in a given frame, most cars are either parked or traveling at nearly constant velocity. Such tracks are hardly a representation of real forecasting challenges. We would like a benchmark with more diverse scenarios e.g. managing an intersection, slowing for a merging vehicle, accelerating after a turn, stopping for a pedestrian on the road, etc. To sample enough of these *interesting* scenarios, we track objects from 1006 driving hours across both Miami and Pittsburgh and find vehicles with interesting behavior in 320 of those hours. In particular, we mine for vehicles that are either at intersections, taking left or right turns, changing to adjacent lanes, or in dense traffic. In total, we collect 324,557 five second sequences and use them in the forecasting benchmark. Figure 5 shows the geographic distribution of these sequences.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Mined Trajectories for Motion Forecasting", "weight": 1.0} -->

Each sequence contains the 2D, bird's eye view centroid of each tracked object sampled at 10 Hz. The "focal" object in each sequence is always a vehicle, but the other tracked objects can be vehicles, pedestrians, or bicycles. Their trajectories are available as context for "social" forecasting models. The 324,557 sequences are split into 205,942 train, 39,472 validation, and 78,143 test sequences. Each sequence has one challenging trajectory which is the focus of our forecasting benchmark. The train, validation, and test sequences are taken from disjoint parts of our cities, i.e. roughly one eighth and one quarter of each city is set aside as validation and test data, respectively. This dataset is far larger than what could be mined from publicly available autonomous driving datasets. While data of this scale is appealing because it allows us to see rare behaviors and train complex models, it is too large to exhaustively verify the accuracy of the mined trajectories and, thus, there is some noise and error inherent in the data.

<!-- chunk {"id": "body-0026", "role": "body", "section": "3D Object Tracking", "weight": 1.0} -->

In this section, we investigate how various baseline tracking methods perform on the Argoverse 3D tracking benchmark. Our baseline methods utilize a hybrid approach with LiDAR and ring camera images and operate directly in 3D. In addition to measuring the baseline difficulty of our benchmark, we measure how simple map-based heuristics can influence tracking accuracy. For these baselines, we track and evaluate *vehicles* only.

<!-- chunk {"id": "body-0027", "role": "body", "section": "3D Object Tracking", "weight": 1.0} -->

Given a sequence of $F$ frames, where each frame contains a set of ring camera images and 3D points from LiDAR $\{ P_{i}\mid{i = {1,\ldots,N}}\}$, where $P_{i}$ $\in$ ${\mathbb{R}}^{3}$ of $x,y,z$ coordinates, we want to determine a set of track hypotheses $\{ T_{j}\mid{j = {1,\ldots,n}}\}$ where $n$ is the number of unique objects in the whole sequence, and $T_{j}$ contains the set of object center locations and orientation. We usually have a dynamic observer as our car is in motion more often than not. The tracked vehicles in the scene around us can be static or moving.

<!-- chunk {"id": "body-0028", "role": "body", "section": "3D Object Tracking", "weight": 1.0} -->

Baseline Tracker. Our baseline tracking pipeline clusters LiDAR returns in driveable region (labeled by the map) to detect potential objects, uses Mask R-CNN to prune non-vehicle LiDAR returns, associates clusters over time using nearest neighbor and the Hungarian algorithm, estimates transformations between clusters with iterative closest point (ICP), and estimates vehicle pose with a classical Kalman Filter using constant velocity motion model. The same predefined bounding box size is used for all vehicles.

<!-- chunk {"id": "body-0029", "role": "body", "section": "3D Object Tracking", "weight": 1.0} -->

When no match can be found by Hungarian method for an object, the object pose is maintained using only motion model up to 5 frames before being removed or associated to a new cluster. This enables our tracker to maintain same object ID even if the object is occluded for a short period of time and reappears. If a cluster is not associated with current tracked objects, we initialize a new object ID for it.

<!-- chunk {"id": "body-0030", "role": "body", "section": "3D Object Tracking", "weight": 1.0} -->

Driveable area. Since our baseline is focused on vehicle tracking, we constrain our tracker to the driveable area as specified by the map. This driveable area covers any region where it is possible for the vehicle to drive (see Section 3.1). This constraint reduces the opportunities for false positives.

<!-- chunk {"id": "body-0031", "role": "body", "section": "3D Object Tracking", "weight": 1.0} -->

Ground height. We use map information to remove LiDAR returns on the ground. In contrast to local ground-plane estimation methods, the map-based approach is effective in sloping and uneven environments.

<!-- chunk {"id": "body-0032", "role": "body", "section": "3D Object Tracking", "weight": 1.0} -->

Lane Direction. Determining the vehicle orientation from LiDAR alone is a challenging task even for humans due to LiDAR sparsity and partial views. We observe that vehicle orientation rarely violates lane direction, especially so outside of intersections. Fortunately, such information is available in our dataset, so we adjust vehicle orientation based on lane direction whenever the vehicle is not at the intersection and contains too few LiDAR points.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Evaluation", "weight": 1.0} -->

We leverage standard evaluation metrics commonly used for multiple object tracking (MOT). The MOT metric relies on a distance/similarity metric between ground truth and predicted objects to determine an optimal assignment. Once an assignment is made, we use three distance metrics for MOTP: MOTP-D (centroid distance), MOTP-O (orientation error), and MOTP-I (Intersection-over-Union error). MOTP-D is computed by the 3D bounding box centroid distance between associated tracker output and ground truth, which is also used in MOTA as detection association range. Our threshold for "missed" tracks is 2 meters, which is half of the average family car length in the US. MOTP-O is the smallest angle difference about the z (vertical) axis such that the front/back object orientation is ignored, and MOTP-I is the amodal shape estimation error, computed by the $1 - {IoU}$ of 3D bounding box after aligning orientation and centroid as in nuScenes. For all three MOTP scores, lower scores indicate higher accuracy.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Evaluation", "weight": 1.0} -->

In our experiments, we run our tracker over the 24 logs in the *Argoverse 3D Tracking* test set. We are also interested in the relationship between tracking performance and distance. We apply a threshold (30, 50, 100 m) to the distance between vehicles and our ego-vehicle and only evaluate annotations and tracker output within that range. The results in Table 2 show that our baseline tracker performs well at short range where the LiDAR sampling density is higher, but struggles for objects beyond 50 m.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Evaluation", "weight": 1.0} -->

We compare our baseline tracker with three ablations that include: 1) using map-based ground removal and lane direction from the map; 2) using naive plane-fitting ground removal and lane direction from the map; 3) using map-based ground removal and no lane direction from the map. The results in Table 3 show that map-based ground removal leads to better 3D IoU score and slightly better detection performance (higher MOTA) than a plane-fitting approach at longer ranges, but slightly worse orientation. On the other hand, lane direction from the map significantly improves orientation performance, as shown in Figure 6.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Evaluation", "weight": 1.0} -->

We have employed relatively simple baselines to track objects in 3D. We believe that our data enables new approaches to map-based and multimodal tracking research.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Motion Forecasting", "weight": 1.0} -->

In this section, we describe our pipeline for motion forecasting baselines.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Motion Forecasting", "weight": 1.0} -->

1\. Preprocessing: As described in Section 3.3, we first mine for "interesting" sequences where a "focal" vehicle is observed for 5 seconds. As context, we have the centroids of all other tracked objects (including the AV itself) which are collapsed into one "other" class.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Motion Forecasting", "weight": 1.0} -->

Forecasting Coordinate System and Normalization. The coordinate system we used for trajectory forecasting is a top-down, bird's eye view (BEV). There are three reference coordinate frames of interest to forecasting: The raw trajectory data is stored and evaluated in the *city* coordinate system (See Section C of the Appendix). For models using lane centerlines as a reference path, we defined a *2D curvilinear coordinate system* with axes tangential and perpendicular to the lane centerline. For models without the reference path (without a map), we normalize trajectories such that the observed portion of the trajectory starts at the origin and ends somewhere on the positive x axis. If $(x_{i}^{t},y_{i}^{t})$ represent coordinates of trajectory $V_{i}$ at timestep $t$, then this normalization makes sure that $y_{i}^{T_{obs}} = 0$, where $T_{obs}$ is last observed timestep of the trajectory (Section 5.1).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Motion Forecasting", "weight": 1.0} -->

We find this normalization works better than leaving trajectories in absolute map coordinates or absolute orientations.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Motion Forecasting", "weight": 1.0} -->

2\. Feature Engineering: We define additional features to capture social or spatial context. For social context, we use the minimum distance to the objects in front, in back, and the number of neighbors. Such heuristics are meant to capture the social interaction between vehicles. For spatial context, we use the map as a prior by computing features in the lane segment coordinate system. We compute the lane centerline corresponding to each trajectory and then map $(x_{i}^{t},y_{i}^{t})$ coordinates to the distance along the centerline $(a_{i}^{t})$ and offset from the centerline $(o_{i}^{t})$. In the subsequent sections, we denote social features and map features for trajectory $V_{i}$ at timestep $t$ by $s_{i}^{t}$ and $m_{i}^{t}$, respectively.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Motion Forecasting", "weight": 1.0} -->

3\. Prediction Algorithm: We implement Constant Velocity, Nearest Neighbor, and LSTM Encoder-Decoder based models using different combinations of features. The results are analyzed in Section 5.3.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Problem Description", "weight": 1.0} -->

The forecasting task is framed as: given the past input coordinates of a vehicle trajectory $V_{i} = {(X_{i},Y_{i})}$ where $X_{i} = {(x_{i}^{t},y_{i}^{t})}$ for time steps $t = {\{ 1,\ldots,T_{obs}\}}$, predict the future coordinates $Y_{i} = {(x_{i}^{t},y_{i}^{t})}$ for time steps $\{{t = {T_{{obs} + 1},\ldots,T_{pred}}}\}$. For a car, 5 s is sufficient to capture the salient part of a trajectory, *e.g*. crossing an intersection. In this paper, we define the motion forecasting task as observing 20 past frames (2 s) and then predicting 30 frames (3 s) into the future.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Problem Description", "weight": 1.0} -->

Each forecasting task can leverage the trajectories of other objects in the same sequence to capture the social context and map information for spatial context.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Evaluation of Multiple Forecasts", "weight": 1.0} -->

Predicting the future is difficult. Often, there are several plausible future actions for a given observation. In the case of autonomous vehicles, it is important to predict *many* plausible outcomes and not simply the *most likely* outcome. While some prior works have evaluated forecasting in a deterministic, unimodal way, we believe a better approach is to follow the evaluation methods similar to DESIRE, Social GAN, R2P2 and wherein they encourage algorithms to output multiple predictions. Among the variety of metrics evaluated in was the minMSD over $K$ number of samples metric, where $K = 12$. A similar metric is used in where they allow $K$ to be up to 50. We follow the same approach and use minimum Average Displacement Error (minADE) and minimum Final Displacement Error (minFDE) over $K$ predictions as our metrics, where $K = {1,3,6,9}$. Note that minADE refers to ADE of the trajectory which has minimum FDE, and not minimum ADE, since we want to evaluate the single best forecast. That said, minADE error might not be a sufficient metric.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Evaluation of Multiple Forecasts", "weight": 1.0} -->

As noted in and, metrics like minMSD or minFDE can only evaluate how good is the best trajectory, but not how good are all the trajectories. A model having 5 good trajectories will have the same error as the model having 1 good and 4 bad trajectories. Further, given the multimodal nature of the problem, it might not be fair to evaluate against a single ground truth. In an attempt to evaluate based on the quality of predictions, we propose another metric: Drivable Area Compliance (DAC). If a model produces $n$ possible future trajectories and $m$ of those exit the drivable area at some point, the DAC for that model would be ${({n - m})}/n$. Hence, higher DAC means better quality of forecasted trajectories. Finally, we also use Miss Rate (MR) with a threshold of 1.0 meter. It is again a metric derived from the distribution of final displacement errors.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Evaluation of Multiple Forecasts", "weight": 1.0} -->

If there are $n$ samples and $m$ of them had the last coordinate of their best trajectory more than 2.0 m away from ground truth, then miss rate is $m/n$. The map-based baselines that we report have access to a semantic vector map. As such, they can generate K different hypotheses based on the branching of the road network along a particular observed trajectory. We use centerlines as a form of hypothetical reference paths for the future. Our heuristics generate $K = 10$ centerlines. Our map gives us an easy way to produce a compact yet diverse set of forecasts. Nearest Neighbor baselines can further predict variable number of outputs by considering different number of neighbors.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Results", "weight": 1.0} -->

In this section, we evaluate the effect of multimodal predictions, social context, and spatial context (from the vector map) to improve motion forecasting over horizons of 3 seconds into the future.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Results", "weight": 1.0} -->

NN: Nearest Neighbor regression where trajectories are queried by $(x_{i}^{t},y_{i}^{t})$ for $t = {\{ 1,\ldots,T_{obs}\}}$. To make $K$ predictions, we performed a lookup for $K$ Nearest Neighbors.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Results", "weight": 1.0} -->

NN+map(prune): This baseline builds on $NN$ and prunes the number of predicted trajectories based on how often they exit the drivable area. Accordingly, this method prefers predictions which are qualitatively good, and not just Nearest Neighbors.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Results", "weight": 1.0} -->

NN+map(prior) m-G,n-C: Nearest Neighbor regression where trajectories are queried by $(a_{i}^{t},o_{i}^{t})$ for $t = {\{ 1,\ldots,T_{obs}\}}$. m-G, n-C refers to $m$ guesses (m-G) allowed along each of $n$ different centerlines (n-C). Here, $m > 1$, except when $K = 1$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Results", "weight": 1.0} -->

NN+map(prior) 1-G,n-C: This is similar to the previous baseline. The only difference is that the model can make only 1 prediction along each centerline.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Results", "weight": 1.0} -->

LSTM+map(prior) 1-G,n-C: Similar to LSTM but with input as $(a_{i}^{t},o_{i}^{t},m_{i}^{t})$ and output as $(a_{i}^{t},o_{i}^{t})$, where $m_{i}^{t}$ denotes the map features obtained from the centerlines. Distances $(a_{i}^{t},o_{i}^{t})$ are then mapped to $(x_{i}^{t},y_{i}^{t})$ for evaluation. Further, we make only one prediction along each centerline because we used a deterministic model.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Results", "weight": 1.0} -->

The results of these baselines are reported in Table 4. When only 1 prediction is allowed, NN based baselines suffer from inaccurate neighbors and have poor minADE and minFDE. On the other hand, LSTM based baselines are able to at least learn the trajectory behaviors and have better results. $LSTM$ baselines with no map are able to obtain the best minADE and mindFDE for $K = 1$. Also, baselines which use map as prior have a much higher DAC. Now, as $K$ increases, $NN$ benefits from the map prior and consistently produces better predictions. When map is used for pruning, it further improves the selected trajectories and provides the best minADE and minFDE. LSTM+map(prior) 1-G,n-C outperforms NN+map(prior) 1-G,n-C highlighting the fact that LSTM does a better job generalizing to curvilinear coordinates. Further, using the map as a prior always provides better DAC, proving that our map helps in forecasting trajectories that follow basic map rules like staying in the driveable area.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Results", "weight": 1.0} -->

Another interesting comparison is between NN+map(prior) 1-G,n-C and NN+map(prior) m-G,n-C. The former comes up with many reference paths (centerlines) and makes one prediction along each of those paths. The latter comes up with fewer reference paths but produces multiple predictions along each of those paths. The latter outperforms the former in all 3 metrics, showing the importance of predicting trajectories which follow different velocity profiles along the same reference paths. Figure 8 reports the results of an ablation study for different values of m and n. Finally, when having access to HD vector maps and being able to make multiple predictions ($K = 6)$, even a shallow model like NN+map(prior) m-G,n-C is able to outperform a deterministic deep model LSTM+social ($K = 1$) which has access to social context.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Discussion", "weight": 1.5} -->

Argoverse represents two large-scale datasets for autonomous driving research. The Argoverse datasets are the first such datasets with rich map information such as lane centerlines, ground height, and driveable area. We examine baseline methods for 3D tracking with map-derived context. We also mine one thousand hours of fleet logs to find diverse, real-world object trajectories which constitute our motion forecasting benchmark. We examine baseline forecasting methods and verify that map data can improve accuracy. We maintain a public leaderboard for 3D object tracking and motion forecasting. The sensor data, map data, annotations, and code which make up Argoverse are available at our website *Argoverse.org*.
