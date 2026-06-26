<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Argoverse 2: Next Generation Datasets for Self-Driving Perception and Forecasting

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce Argoverse 2 (AV2) - a collection of three datasets for perception and forecasting research in the self-driving domain. The annotated Sensor Dataset contains 1,000 sequences of multimodal data, encompassing high-resolution imagery from seven ring cameras, and two stereo cameras in addition to lidar point clouds, and 6-DOF map-aligned pose. Sequences contain 3D cuboid annotations for 26 object categories, all of which are sufficiently-sampled to support training and evaluation of 3D perception models. The Lidar Dataset contains 20,000 sequences of unlabeled lidar point clouds and map-aligned pose. This dataset is the largest ever collection of lidar sensor data and supports self-supervised learning and the emerging task of point cloud forecasting. Finally, the Motion Forecasting Dataset contains 250,000 scenarios mined for interesting and challenging interactions between the autonomous vehicle and other actors in each local scene. Models are tasked with the prediction of future motion for "scored actors" in each scenario and are provided with track histories that capture object location, heading, velocity, and category.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In all three datasets, each scenario contains its own HD Map with 3D lane and crosswalk geometry - sourced from data captured in six distinct cities. We believe these datasets will support new and existing machine learning research problems in ways that existing datasets do not. All datasets are released under the CC BY-NC-SA 4.0 license.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In order to achieve the goal of safe, reliable autonomous driving, a litany of machine learning tasks must be addressed, from stereo depth estimation to motion forecasting to 3D object detection. In recent years, numerous high quality self-driving datasets have been released to support research into these and other important machine learning tasks. Many datasets are annotated "sensor" datasets in the spirit of the influential KITTI dataset. The Argoverse 3D Tracking dataset was the first such dataset with "HD maps" --- maps containing lane-level geometry. Also influential are self-driving "motion prediction" datasets --- containing abstracted object tracks instead of raw sensor data --- of which the Argoverse Motion Forecasting dataset was the first.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the last two years, the Argoverse team has hosted six competitions on 3D tracking, stereo depth estimation, and motion forecasting. We maintain evaluation servers and leaderboards for these tasks, as well as 3D detection. The leaderboards collectively contain thousands of submissions from four hundred teams^11^1This count includes private submissions not posted to the public leaderboards.. We also maintain the Argoverse API and have addressed more than one hundred issues^22^2 From these experiences we have formed the following guiding principles to guide the creation of the next iteration of Argoverse datasets.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Bigger isn't always better. Self-driving vehicles capture a flood of sensor data which is logistically difficult to work. Sensor datasets are several terabytes in size, even when compressed. If standard benchmarks grow further, we risk alienating much of the academic community and leaving progress to well-resourced industry groups. *For this reason, we match but do not exceed the scale of sensor data in nuScenes and Waymo Open *.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Make every instance count. Much of driving is boring. Datasets should focus on the difficult, interesting scenarios where current forecasting and perception systems struggle. *Therefore we mine for especially crowded, dynamic, and kinematically unusual scenarios.* Diversity matters. Training on data from wintertime Detroit is not sufficient for detecting objects in Miami --- Miami has 15 times the frequency of motorcycles and mopeds. Behaviors differ as well, so learned pedestrian motion behavior might not generalize. *Accordingly, each of our datasets are drawn from six diverse cities --- Austin, Detroit, Miami, Palo Alto, Pittsburgh, and Washington D.C. --- and different seasons, as well, from snowy to sunny*.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Map the world. HD maps are powerful priors for perception and forecasting. Learning-based methods that found clever ways to encode map information performed well in Argoverse competitions. *For this reason, we augment our HD map representation with 3D lane geometry, paint markings, crosswalks, higher resolution ground height, and more*.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Self-supervise. Other machine learning domains have seen enormous success from self-supervised learning in recent years. Large-scale lidar data from dynamic scenes, paired with HD maps, could lead to better representations than current supervised approaches. *For this reason, we build the largest dataset of lidar sensor data.* Fight the heavy tail. Passenger vehicles are common, and thus we can assess our forecasting and detection accuracy for cars. However, with existing datasets, we cannot assess forecasting accuracy for buses and motorcycles with their distinct behaviors, nor can we evaluate stroller and wheel chair detection. *Thus we introduce the largest taxonomy to date for sensor and forecasting datasets, and we ensure enough samples of rare objects to train and evaluate models.* With these guidelines in mind we built the three Argoverse 2 (AV2) datasets. Below, we highlight some of their contributions.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The 1,000 scenario *Sensor dataset* has the largest self-driving taxonomy to date -- 30 categories. 26 categories contain at least 6,000 cuboids to enable diverse taxonomy training and testing. The dataset also has stereo imagery, unlike recent self-driving datasets.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The 20,000 scenario *Lidar dataset* is the largest dataset for self-supervised learning on lidar. The only similar dataset, concurrently developed ONCE, does not have HD maps.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The 250,000 scenario *Motion Forecasting Dataset* has the largest taxonomy -- 5 types of dynamic actors and 5 types of static actors -- and covers the largest mapped area of any such dataset.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We believe these datasets will support research into problems such as 3D detection, 3D tracking, monocular and stereo depth estimation, motion forecasting, visual odometry, pose estimation, lane detection, map automation, self-supervised learning, structure from motion, scene flow, optical flow, time to contact estimation, and point cloud forecasting.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Sensor Dataset", "weight": 1.0} -->

The *Argoverse 2 Sensor Dataset* is the successor to the *Argoverse 1 3D Tracking Dataset*. AV2 is larger, with 1,000 scenes, up from 113 in Argoverse 1, but each AV2 scene is also richer -- there are 23x as many non-vehicle, non-pedestrian cuboids in AV2. The constituent $30\ s$ scenarios in the Argoverse 2 Sensor Dataset were manually selected by the authors to contain crowded scenes with under-represented objects, noteworthy weather, and interesting behaviors, e.g., cut ins and jaywalking. Each scenario is fifteen seconds in duration. Table 1 compares the AV2 Sensor Dataset with a selection of self-driving datasets. Figures 1, 2, and 3 plot how the scenarios of AV2 compare favorably to other datasets in terms of annotation range, object diversity, object density, and scene dynamism.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Sensor Dataset", "weight": 1.0} -->

The most similar sensor dataset to ours is the highly influential nuScenes -- both datasets have 1,000 scenarios and HD maps, although Argoverse is unique in having ground height maps. nuScenes contains radar data while AV2 contains stereo imagery. nuScenes has a large taxonomy -- twenty-three object categories of which ten have suitable data for training and evaluation. Our dataset contains thirty object categories of which twenty-six are well sampled enough for training and evaluation. nuScenes spans two cities, while our proposed dataset spans six.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Sensor Dataset", "weight": 1.0} -->

Name # Scenes Cities Lidar? # Cameras Stereo HD Maps? # Classes # Evaluated Classes Argoverse 1 113 2 ✓ 7 ✓ ✓ 15 3 KITTI 22 1 ✓ 2 ✓ 3 3 nuScenes 1,000 2 ✓ 6 ✓ 23 10 ONCE 581 – ✓ 7 5 3 Waymo Open 1,150 3 ✓ 5 4 4 Argoverse 2 Sensor 1,000 6 ✓ 9 ✓ ✓ 30 26 Argoverse 2 Lidar 20,000 6 ✓ - ✓ - - Table 1: Comparison of the Argoverse 2 Sensor and Lidar datasets with other sensor datasets.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Sensor Suite", "weight": 1.0} -->

Lidar sweeps are collected at $10\ {Hz}$, along with $20\ {fps}$ imagery from 7 cameras positioned to provide a fully panoramic field of view. In addition, camera intrinsics, extrinsics and 6-DOF ego-vehicle pose in a global coordinate system are provided. Lidar returns are captured by two 32-beam lidars, spinning at $10\ {Hz}$ in the same direction, but separated in orientation by $180{^\circ}$. The cameras trigger in-sync with both lidars, leading to a $20\ {Hz}$ frame-rate. The seven global shutter cameras are synchronized to the lidar to have their exposure centered on the lidar sweeping through their fields of view. In the Appendix, we provide a a schematic figure illustrating the car sensor suite and its coordinate frames.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Sensor Suite", "weight": 1.0} -->

Lidar synchronization accuracy. In AV2, we improve the synchronization of cameras and lidars significantly over Argoverse 1. Our synchronization accuracy is within $\lbrack{- 1.39},1.39\rbrack$ $\ {ms}$, which compares favorably to the Waymo Open Dataset, which is reported as $\lbrack{- 6},7\rbrack$ $\ {ms}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Sensor Suite", "weight": 1.0} -->

Annotations. The AV2 Sensor Dataset contains $10\ {Hz}$ 3D cuboid annotations for objects within our 30 class taxonomy (Figure 1). Cuboids have track identifiers that are consistent over time for the same object instance. Objects are annotated if they are within the "region of interest" (ROI) -- within five meters of the mapped "driveable" area.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Sensor Suite", "weight": 1.0} -->

Privacy. All faces and license plates, whether inside vehicles or outside of the driveable area, are blurred extensively to preserve privacy.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Sensor Suite", "weight": 1.0} -->

Sensor Dataset splits. We randomly partition the dataset with train, validation, and test splits of 700, 150, and 150 scenarios, respectively.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Lidar Dataset", "weight": 1.0} -->

The *Argoverse 2 Lidar Dataset* is intended to support research into self-supervised learning in the lidar domain as well as point cloud forecasting. Because lidar data is more compact than the full sensor suite, we can include double-length scenarios ($30\ s$ instead of $15\ s$), and far more -- 20,000 instead of 1,000 -- equating to roughly 40x as many driving hours, for 5x the space budget. The AV2 Lidar Dataset is mined with the same criteria as the Forecasting Dataset (Section 3.3.2) to ensure that each scene is interesting. While the Lidar Dataset does not have 3D object annotations, each scenario carries an HD map with rich, 3D information about the scene.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Lidar Dataset", "weight": 1.0} -->

Our dataset is the largest such collection to date with 20,000 thirty second sequences. The only similar dataset, concurrently released ONCE, contains $1\ M$ lidar frames compared to $6\ M$ lidar frames in ours. Our dataset is sampled at $10\ {Hz}$ instead of $2\ {Hz}$, as in ONCE, making our dataset more suitable for point cloud forecasting or self-supervision tasks where point cloud evolution over time is important.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Lidar Dataset", "weight": 1.0} -->

Lidar Dataset splits. We randomly partition the dataset with train, validation, and test splits of 16,000, 2,000, and 2,000 scenarios, respectively.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Motion Forecasting Dataset", "weight": 1.0} -->

# tracks per scenario 50 - 79 - 75 29 73 # Evaluated object categories 1 1 3 3 1 2 5 Multi-agent evaluation × ✓ ✓ ✓ × ✓ ✓ Mined for Interestingness ✓ × - ✓ × × ✓ Vector Map ✓ × × ✓ ✓ × ✓ Download Size 4.8 GB - 22 GB 1.4 TB 48 GB 120 GB 58 GB # Public Leaderboard Entries† 194 - 935 23 18 3 - Table 2: Comparison between the Argoverse 2 Motion Forecasting dataset and other recent motion forecasting datasets.

Hyphens "-" indicate that attributes are either not applicable, or not available. We define “mined for interestingness” to be true if interesting scenarios/actors are mined after data collection, instead of taking all/random samples. † Public leaderboard counts as retrieved on Aug. 27, 2021.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Motion Forecasting Dataset", "weight": 1.0} -->

Motion forecasting addresses the problem of predicting future states (or occupancy maps) for dynamic actors within a local environment. Some examples of relevant actors for autonomous driving include: vehicles (both parked and moving), pedestrians, cyclists, scooters, and pets. Predicted futures generated by a forecasting system are consumed as the primary inputs in motion planning, which conditions trajectory selection on such forecasts. Generating these forecasts presents a complex, multi-modal problem involving many diverse, partially-observed, and socially interacting agents. However, by taking advantage of the ability to "self-label" data using observed ground truth futures, motion forecasting becomes an ideal domain for application of machine learning.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Motion Forecasting Dataset", "weight": 1.0} -->

Building upon the success of Argoverse 1, the Argoverse 2 Motion Forecasting dataset provides an updated set of prediction scenarios collected from a self-driving fleet. The design decisions enumerated below capture the collective lessons learned from both our internal research/development, as well as feedback from more than 2,700 submissions by nearly 260 unique teams^33^3This count includes private submissions not posted to the public leaderboards. across 3 competitions: Motion forecasting is a safety critical system in a long-tailed domain. Consequently, our dataset is biased towards diverse and interesting scenarios containing different types of focal agents (see section 3.3.2). Our goal is to encourage the development of methods that ensure safety during tail events, rather than to optimize the expected performance on "easy miles".

<!-- chunk {"id": "body-0028", "role": "body", "section": "Motion Forecasting Dataset", "weight": 1.0} -->

There is a "Goldilocks zone" of task difficulty. Performance on the Argoverse 1 test set has begun to plateau, as shown in Figure 10 of the appendix. Argoverse 2 is designed to increase prediction difficulty incrementally, spurring productive focused research for the next few years. These changes are intended to incentivize methods that perform well on extended forecast horizons (3 s $\rightarrow$ 6 s), handle multiple types of dynamic objects (1 $\rightarrow$ 5), and ensure safety in scenarios from the long tail. Future Argoverse releases could continue to increase the problem difficulty by reducing observation windows and increasing forecasting horizons.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Motion Forecasting Dataset", "weight": 1.0} -->

Usability matters. Argoverse 1 benefited from a large and active research community---in large part due to the simplicity of setup and usage. Consequently, we took care to ensure that existing Argoverse models can be easily ported to run on Argoverse 2. In particular, we have prioritized intuitive access to map elements, encouraging methods which use the lane graph as a strong prior. To improve training and generalization, all poses have also been interpolated and resampled at exactly $10\ {Hz}$ (Argoverse 1 was approximate). The new dataset includes fewer, but longer and more complex scenarios; this ensures that total dataset size remains large enough to train complex models but small enough to be readily accessible.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Data Representation", "weight": 1.0} -->

The dataset consists of 250,000 non-overlapping scenarios (80/10/10 train/val/test random splits) mined from six unique urban driving environments in the United States. It contains a total of 10 object types, with 5 from each of the dynamic and static categories (see Figure 4). Each scenario includes a local vector map and $11\ s$ ($10\ {Hz}$) of trajectory data (2D position, velocity, and orientation) for all tracks observed by the ego-vehicle in the local environment. The first $5\ s$ of each scenario is denoted as the observed window, while the subsequent $6\ s$ is denoted as the forecasted horizon.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Data Representation", "weight": 1.0} -->

Within each scenario, we mark a single track as the "focal agent". Focal tracks are guaranteed to be fully observed throughout the duration of the scenario and have been specifically selected to maximize interesting interactions with map features and other nearby actors (see Section 3.3.2). To evaluate multi-agent forecasting, we also mark a subset of tracks as "scored actors" (as shown in Figure 5), with guarantees for scenario relevance and minimum data quality.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Mining Interesting Scenarios", "weight": 1.0} -->

The source data for Argoverse 2 was drawn from fleet logs tagged with annotations consistent with interesting or difficult-to-forecast events. Each log was trimmed to $30\ s$ and run through an interestingness scoring module in order to bias data selection towards examples from the long-tail of the natural distribution. We employ heuristics to score each track in the scene across five dimensions: object category, kinematics, map complexity, social context, and relation to the ego-vehicle (details in Appendix).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Mining Interesting Scenarios", "weight": 1.0} -->

The final scenarios are generated by extracting non-overlapping $11\ s$ windows where at least one candidate track is fully observed for the entire duration. The highest scoring candidate track is denoted as the "focal agent"; all other fully observed tracks within $30\ m$ of the ego-vehicle are denoted as "scored actors". The resulting dataset is diverse, challenging, and still right-sized for widespread use (see the download size in Table 2). In Figure 6, we show that the resulting dataset is significantly more interesting than Argoverse 1.1 and validate our intuition that actors scoring highly in our heuristic module are more challenging to accurately forecast.

<!-- chunk {"id": "body-0034", "role": "body", "section": "HD Maps", "weight": 1.0} -->

Each scenario in the three datasets described above shares the same HD map representation. Each scenario carries its own local map region, similar to the Waymo Open Motion dataset. This is a departure from the original Argoverse datasets in which all scenarios were localized onto two city-scale maps---one for Pittsburgh and one for Miami. In the Appendix, we provide examples. Advantages of per-scenario maps include more efficient queries and their ability to handle *map changes*. A particular intersection might be observed multiple times in our datasets, and there could be changes to the lanes, crosswalks, or even ground height in that time.

<!-- chunk {"id": "body-0035", "role": "body", "section": "HD Maps", "weight": 1.0} -->

Lane graph. The core feature of the HD map is the lane graph, consisting of a graph $\mathcal{G} = {(\mathcal{V},\mathcal{E})}$, where $\mathcal{V}$ are individual lane segments. In the Appendix, we enumerate and define the attributes we provide for each lane segment. Unlike Argoverse 1, we provide the actual 3D lane boundaries, instead of only centerlines. However, our API provides code to quickly infer the centerlines at any desired sampling resolution. Polylines are quantized to $1\ {cm}$ resolution. Our representation is richer than nuScenes, which provides lane geometry only in 2D, not 3D.

<!-- chunk {"id": "body-0036", "role": "body", "section": "HD Maps", "weight": 1.0} -->

Driveable area. Instead of providing driveable area segmentation in a rasterized format, as we did in Argoverse 1, we release it in a vector format, i.e. as 3D polygons. This offers multiple advantages, chiefly in compression, allowing us to store separate maps for tens of thousands of scenarios, yet the raster format is still easily derivable. The polygon vertices are quantized to $1\ {cm}$ resolution.

<!-- chunk {"id": "body-0037", "role": "body", "section": "HD Maps", "weight": 1.0} -->

Ground surface height. Only the sensor dataset includes a dense ground surface height map (although other datasets still have sparse 3D height information on polylines). Ground surface height is provided for areas within a $5\ m$ isocontour of the driveable area boundary, which we define as the *region of interest* (ROI). We do so because the notion of ground surface height is ill-defined for the interior of buildings and interior of densely constructed city blocks, areas where ground vehicles cannot observe due to occlusion. The raster grid is quantized to a $30\ {cm}$ resolution, a higher resolution than the $1\ m$ resolution in Argoverse 1.

<!-- chunk {"id": "body-0038", "role": "body", "section": "HD Maps", "weight": 1.0} -->

Area of Local Maps. Each scenario's local map includes all entities found within a $100\ m$ dilation in $l_{2}$-norm from the ego-vehicle trajectory.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiments", "weight": 1.0} -->

Argoverse 2 supports a variety of downstream tasks. In this section we highlight three different learning problems: 3D object detection, point cloud forecasting, and motion forecasting --- each supported by the sensor, lidar, and motion forecasting datasets, respectively. First, we illustrate the *challenging* and *diverse* taxonomy within the Argoverse 2 sensor dataset by training a state-of-the-art 3D detection model on our twenty-six evaluation classes including "long-tail" classes such as stroller, wheel chairs, and dogs. Second, we showcase the utility of the Argoverse 2 lidar dataset through *large-scale*, self-supervised learning through the point cloud forecasting task. Lastly, we demonstrate motion forecasting experiments which provide the first baseline for broad taxonomy motion prediction.

<!-- chunk {"id": "body-0040", "role": "body", "section": "3D Object Detection", "weight": 1.0} -->

Method mCDS (↑) mAP (↑) mATE (↓) mASE (↓) mAOE (↓) CenterPoint (Ours) 0.14 0.18 0.49 0.34 0.72 Detectors 0.34 0.41 0.40 0.30 0.54 BEVFusion 0.37 0.46 0.40 0.30 0.50 Table 3: 3d object detection results on the Argoverse 2 Sensor Dataset, taken from the leaderboard on Dec 21, 2022. Detectors is the winner of the CVPR 2022 Workshop on Autonomous Driving Argoverse 2 3D Object Detection challenge.

<!-- chunk {"id": "body-0041", "role": "body", "section": "3D Object Detection", "weight": 1.0} -->

We provide baseline 3D detection results using a state-of-the-art, anchorless 3D object detection model -- CenterPoint. Our CenterPoint implementation takes a point cloud as input and crops it to a $200\ m$ $\times$ $200\ m$ grid with a voxel resolution of \[$0.1\ m$, $0.1\ m$\] in the $xy$ (bird's-eye-view) plane and $0.2\ m$ in the $z$-axis. To accommodate our larger taxonomy, we include six detection heads to encourage feature specialization. Figure 7 characterizes the performance of our 3D detection baseline using the nuScenes average precision metric. Our large taxonomy allows us to evaluate classes such as "Wheeled Device" (e-Scooter), "Stroller", "Dog", and "Wheelchair" and we find that performance on these categories with strong baselines is poor despite significant amounts of training data.

<!-- chunk {"id": "body-0042", "role": "body", "section": "3D Object Detection", "weight": 1.0} -->

In Table 3, we provide a snapshot of submissions to the Argoverse 2 3D Object Detection Leaderboard.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Point Cloud Forecasting", "weight": 1.0} -->

We perform point cloud forecasting according to the experimental protocol of SPF2 using the Argoverse 2 Lidar Dataset. Given a sequence of past scene point clouds, a model is required to predict a sequence of future scene point clouds. We take the scene point clouds in the past $1\ s$ ($10\ {Hz}$) in the range image format as input, and then predict the next $1\ s$ of range images. SPFNet predicts two output maps at each time step -- the first output map is the predicted range values, while the second output is a validity mask. Previous point cloud forecasting models were evaluated on smaller datasets such as KITTI or nuScenes. To explore how the amount of training data affects the performance, we use increasing amounts of data for training the same model architecture, up to the full training set of 16,000 sequences.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Evaluation", "weight": 1.0} -->

We use three metrics to evaluate the performance of our forecasting model: *mean IoU*, *$l_{1}$-norm*, and *Chamfer distance*. The *mean IoU* evaluates the predicted range mask. The *$l_{1}$-norm* measures the average $l_{1}$ distance between the pixel sets of predicted range image and the ground-truth image, which are both masked out by the ground-truth range mask. The *Chamfer distance* is obtained by adding up the Chamfer distances in both directions (forward and backward) between the ground-truth point cloud and the predicted scene point cloud which is obtained by back-projecting the predicted range image.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Results of SPF2 and Discussion", "weight": 1.0} -->

Table 4 contains the results of our point cloud forecasting experiments. With increasing training data, the performance of the model grows steadily in all three metrics. These results and the works from the self-supervised learning literature indicate that a large amount of training data can make a substantial difference. Another observation is that the Chamfer distances for predictions on our dataset are significantly higher than predictions on KITTI. We conjecture that this could be due to two reasons: the Argoverse 2 Lidar Dataset has a much larger sensing range (above $200\ m$ versus $120\ m$ of the KITTI lidar sensor), which tends to significantly increase the value of Chamfer distance. the Argoverse 2 Lidar Dataset has a higher proportion of dynamic scenes compared with KITTI Dataset.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Motion Forecasting", "weight": 1.0} -->

We present several forecasting baselines which try to make use of different aspects of the data. Those which are trained using the focal agent only and do not capture any social interaction include: constant velocity, nearest neighbor, and LSTM encoder-decoder models (both with and without a map-prior). We also evaluate WIMP as an example of a graph-based attention method that captures social interaction. All hyper-parameters are obtained from the reference implementations.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Baseline approaches are evaluated according to standard metrics. Following, we use minADE and minFDE as the metrics; they evaluate the average and endpoint L2 distance respectively, between the best forecasted trajectory and the ground truth. We also use Miss Rate (MR) which represents the proportion of test samples where none of the forecasted trajectories were within 2.0 meters of ground truth according to endpoint error. The resulting performance illustrates both the community's progress on the problem and the significant increase in dataset difficulty when compared with Argoverse 1.1.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Baseline Results. Table 5 summarizes the results of baselines. For K=1, Argoverse 1 showed that a constant velocity model (minFDE=7.89) performed better than NN+map(prior) (minFDE=8.12), which is not the case here. This further proves that Argoverse 2 is kinematically more diverse and cannot be solved by making constant velocity assumptions. Surprisingly, NN and LSTM variants that make use of a map prior perform worse than those which do not, illustrating the scope of improvement in how these baselines leverage the map. For K=6, WIMP significantly outperforms every other baseline. This emphasizes that it is imperative to train expressive models that can leverage map prior and social context along with making diverse predictions. The trends are similar to our past 3 Argoverse Motion Forecasting competitions: Graph-based attention methods (e.g. ) continued to dominate the competition, and were nearly twice as accurate as the next best baseline (Nearest Neighbor) at K=6. That said, some of the rasterization-based (e.g. ) methods also showed promising results.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Finally, we also evaluated baseline methods in the context of transfer learning and varied object types, the results of which are summarized in the Appendix.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Evaluation", "weight": 1.0} -->

In Table 6, we provide a snapshot of submissions to the Argoverse 2 Motion Forecasting Leaderboard.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Discussion. In this work, we have introduced three new datasets that constitute Argoverse 2. We provide baseline explorations for three tasks -- 3d object detection, point cloud forecasting and motion forecasting. Our datasets provide new opportunities for many other tasks. We believe our datasets compare favorably to existing datasets, with HD maps, rich taxonomies, geographic diversity, and interesting scenes.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Limitations. As in any human annotated dataset, there is label noise, although we seek to minimize it before release. 3D bounding boxes of objects are not included in the motion forecasting dataset, but one can make reasonable assumptions about the object extent given the object type. The motion forecasting dataset also has imperfect tracking, consistent with state-of-the-art 3D trackers.
