## Introduction

Autonomous driving methods require scene understanding, robotic planning and control, either implicitly, in an end-to-end fashion, or in explicit modules, including perception, prediction of scene geometry and of the future evolution of relevant agents, tracking of the environment, planning and control.

In the last decade, the development of driving methods have been largely driven by learned models trained on driving datasets including KITTI, Cityscapes, nuScenes, Waymo and Argoverse, which predominantly feature urban environments and therefore implicitly bias the development of the field toward short-range perception and low-speed driving. This bias is reflected in the annotation range, which typically extends only $70$--$100$ m from the ego-vehicle.

For normal passenger cars driving in urban environments, short-range perception is sufficient as lower speeds convert the limited spatial range into enough temporal foresight to support the $5$--$10$ seconds planning horizons of modern prediction and planning stacks. For heavy-duty trucks operating at highway speeds, instead, the safety envelope is dominated by their high-inertia braking requirements. At $120$ km/h, a fully-loaded truck requires over $150$--$200$ m to stop, equivalent to $4.5$--$6$ s of look-ahead perception. Therefore, the necessary braking budget is severely compromised by limited sensing horizons: an $80$ m range provides only about $2.4$ seconds of foresight, and even $100$ m yields merely $3.0$ seconds. This entire window is consumed by sensing and planning latencies, eroding the time required for safe braking actuation before the maneuver can even begin. This leaves a critically insufficient margin for the vehicle's deceleration and renders strategic planning, like merging or lane changes, unfeasible.

Driving architectures for long-range perception and planning are non-trivial: Bird's-Eye-View (BEV) and dense voxel representations scale quadratically with distance, leading to exponential growth in compute and memory. Concurrently, the signal-to-noise ratio of distant objects decreases sharply due to sensor resolution limits and atmospheric attenuation. Sparse and range-aware methods alleviate these issues but remain constrained by calibration drift, temporal uncertainty and sparsity of long-range supervision. Moreover, performance on short-range urban benchmarks has begun to saturate, with a decline in the number of submissions and a flattening in the performance gain (Figure 2), with poor generalization capability beyond $100$ m of models designed around these priors.

To close this gap, we introduce *TruckDrive*, the first large-scale dataset specifically designed for long-range, high-speed autonomous driving. TruckDrive, as presented in Figure 1, extends the perception range by a factor of *five* relative to urban benchmarks, compared in Table 1, providing $2$D annotations up to $1,000$ m and corresponding $3$D annotations up to $400$ m, with $15$ to $25$ s temporal clips to support forecasting and end-to-end (E2E) learning. The dataset includes over $475$ k multi-modal synchronized samples, among which $165$ k manually labeled and $310$ k unlabeled for self-supervised and unsupervised research. Our sensor suite integrates high-resolution ($8$MP) short and long focal length cameras, wide-baseline stereo, short and long range $4$D LiDARs and $4$D radars, enabling comprehensive research in perception, prediction and planning.

We evaluate state-of-the-art driving methods for urban datasets in diverse tasks and observe drops between $31$ and $99$% in $3$D perception tasks beyond $150$ m, confirming that they do not generalize to long-range regimes. This exposes a fundamental open challenge in current architectures and motivates new directions in efficient representation learning, sensor fusion and long-horizon reasoning.

We make the following contributions:

We present a long-range, high-fidelity multi-modal driving dataset that combines high-resolution $8$MP cameras, large-baseline stereo, $4$D LiDARs and $4$D radars, enabling dense $3$D annotations up to $400$ m and $2$D annotations up to 1 km.

We provide large-scale data comprising $475$ k samples, including $165$ k labeled and $310$ k unlabeled frames, with full raw sensor streams to support supervised, semi-supervised, and self-supervised research.

We establish a highway-scale benchmark for perception, prediction, planning and E2E driving tasks under high-speed, long-range conditions, finding several failure modes and scaling challenges in existing models.

Figure 2: Performance Saturation on Urban Datasets. We plot the performance of 2D and 3D OD, Tracking, Prediction and Depth Estimation of NuScenes and Kitti leader boards across the years and observe a saturation of these benchmarks.

Cityscapes 3D [gählert2020cityscapes3ddatasetbenchmark]

1x Stereo Pair, 1x Gated, 1x FIR

Waymo - End2End

2x RGB, 2x RGB Fisheye

1x Stereo Pair, 7x Ring Cameras

1x / 3x Stereo Pair, 9x single

Table 1: TruckDrive Benchmark Comparison. Cross-dataset summary of sensors, synced samples and useful ranges. TruckDrive couples 7 long range and 3 short range LiDARs with 10 automotive radars, 9 wide/medium field of view cameras and 1 − 3 long-focal-length wide-baseline stereo cameras. It offers 165 thousands annotated samples and additional 310 thousands unlabeled samples and extends the effective perception range to [ − 400, + 400] meters, focusing on highway long-range scenarios to stress perception capabilities beyond conventional benchmarks. ∗NuPlan provides auto-labeled annotations.

## Related Work

Public vision datasets \[18 Results"), 15, 38, 67, 68, 9, 56\] have been a catalyst for progress in computer vision, providing a shared basis for developing and comparing novel algorithms. Autonomous driving has followed the same pattern where improvements in detection, prediction and planning have been tightly coupled to increasingly capable datasets.

Early Autonomous Driving Datasets. The field was pioneered by the KITTI dataset and, later, its extensions, among the firsts to provide synchronized camera and LiDAR data with $3D$ bounding boxes annotations. These datasets, however, are limited to a relatively small scale, ranges and scenarios.

Large-Scale Multimodal Autonomous Driving Datasets. The next generation of datasets addressed these limitations by introducing $360$ degrees sensor coverage and a much larger scale. The nuScenes ecosystem provides a full sensor suite for $3$D perception, which was later complemented by nuImages, a large-scale dataset focused on $2$D object detection (OD), and nuPlan, the first large-scale, real-world benchmark for motion planning. Similarly, the Waymo Open Dataset ecosystem offered an unprecedented scale. While initially focused on perception tasks, it has since expanded with the Waymo Motion dataset for trajectory forecasting and the Waymo E2E benchmark for evaluating end-to-end driving models. The Argoverse datasets extended the common perception range up to $150$ meters and the Lyft Level $5$ dataset focused on providing large-scale HD maps.

Task-Focused Autonomus Driving Datasets. Along with the development of large-scale benchmarks, several datasets have made significant contributions by focusing on specific tasks and modalities. Cityscapes $3$D \[gählert2020cityscapes3ddatasetbenchmark\] extended the popular semantic segmentation benchmark with $3$D bounding box annotations, bridging the gap between $2$D and $3$D scene understanding. ApolloScape introduced a massive collection of data with a wide variety of tasks, including $3$D detection, lane segmentation, and dense trajectory information for simulation. Datasets from automotive OEMs, such as A2D2 (Audi), H3D (Honda) and surround-view truck scenes from MAN Truckscenes, provide data from high-quality, industry-grade sensor configurations. KAIST dataset and aiMotive explored highway driving scenarios, although containing respectively only $1.2$k annotated frames and $12$k highway frames. The ONCE dataset has pushed towards reducing annotation dependency by providing a large-scale benchmark for self-supervised learning, while A\*3D and SeeingThroughFog explored active learning strategies or novel sensor setups to improve annotation efficiency in highly challenging weather conditions.

Limits of Existing Autonomous Driving Datasets. As presented in Table 1, prior autonomous driving datasets are dominated by urban, low speed setting and short effective ranges: $3$D labels are rarely present above $80$ meters, annotation density decrease rapidly with distance and long-range sensing is either absent or poorly represented. Moreover, they often offer low annotation amount and sensor modalities are limited to a small set of cameras and short range LiDARs, pushing models to fit specific biases and leaving safe heavy-vehicle driving as an open challenge.

## TruckDrive Dataset

We introduce TruckDrive, a long-range, highway-focused dataset designed for heavy-vehicle autonomy. In this section, we first describe the TruckDrive domain and data collection process, emphasizing its diverse driving conditions, specialized sensor suite for high-speed perception and our cross-modal synchronization strategy. We further detail our annotation pipeline, which combines manual labeling with automated multi-view completion and kinematic refinement. Finally, we provide a quantitative analysis and comparison to foundational datasets (from Table 1), demonstrating gains in range, speed and trajectory coverage.

### Dataset Domain

TruckDrive targets the driving domain of semi-trucks and other large commercial vehicles, covering scenarios that differ significantly from the urban, car-centric datasets commonly used in autonomous driving research. The dataset contains $3,828$ sequences recorded over $2$ years across $8$ U.S. states (NM, TX, VA, NC, TN, AR, WV, AZ), reaching a diversity-area metric of $1,261.3$ km^2^ ($16.5 \times$ WOD). Data collection spans all seasons ($48$% fall, $32$% winter, $15$% spring, $5$% summer) and diverse weather ($80$% sunny/cloudy/overcast, $10$% fog, $10$% precipitation). Sequences last $15–25$ s with an average ego trajectory of $500$ m, comprising mainly highways ($3,244$), followed by extra-urban ($351$) and urban roads ($233$). Driving patterns include $45.8$% cruise/accelerate/brake, $36.5$% lane changes/overtakes, $5.4$% close cut-ins, and $12.3$% complex layouts (work zones, intersections, unprotected turns). Illumination coverage includes $3,285$ daytime, $367$ night, $122$ dusk, and $54$ dawn sequences.

Figure 3: Sensors Position and FoV. Sensor position (top) and the nominal instrumented horizontal field of view (bottom) of, from left to right, radars, LiDARs and cameras, highlighting the unprecedented ranges at which they can operate.

Camera LiDAR Radar RCCB AR0820 4D LR Aeries II 3D SR OS0/OS1 4D ARS540 Make OnSemi AEVA Ouster Continental Type RCCB FMCW 4D 3D FMCW 4D Resolution 3848 × 2168 ∼100 lines 64/128 × 2048 — FOV (H×V) 52.8∘ × 28.9∘ 120∘ × 30∘ 360∘ × 90∘/45∘ ± 4∘– ± 20∘ f (Hz) 5–10 10 20 Raw Captures 6.3M 7.8M 6.0M Sync Timestamps 569k 744k 601k Cross-Modal Sync Timestamps: 475k
Table 2: Sensor Specifications and Raw Data Scale. We present in detail our sensor platform, including RCCB cameras 3D short-range (SR) LiDARs, a 4D long-range (LR) FMCW LiDAR, and 4D radars, capturing 475 thousands synchronized frames

### Long-Range Sensor Setup

Our sensor suite, mounted on a semi-truck, is optimized for reliable perception in high-speed environments. Specifically, we employ $7$ FMCW LiDARs (AEVA Aeries II), capable of measuring up to $400$ meters and providing radial velocity, $3$ short-range LiDARs (Ouster OS0/OS1), to account for blind spots and objects very close to the ego and $10$ $4$D radars (Conti ARS540). Additionally, $11$ to $15$, depending on the configuration, RCCB cameras (9 short/medium focal and $1$ to $3$ long-focal stereo) provide high resolution imaging ($8MP$) at all ranges: QA verifies extrinsic accuracy below $0.015$°, bounding re-projection error beyond $200$m. We report placement and horizontal coverage in Figure 3 and per-sensor specifications in Table 2.

FMCW Velocity. We rely on Frequency-Modulated Continuous-Wave (FMCW) technology, which allows to capture instantaneous radial velocity $v_{r}$ for each point in the point cloud. The velocity measurement is derived from the Doppler-induced phase shift $\Delta\phi$ through

where $\lambda$ is the wavelength and $\theta$ the angle of incidence.

Geo-Inertial Poses (PPK). For accurate ego motion we fuse data from $2$ GNSS and $4$ IMUs in a tailored Post-Processing Kinematic (PPK) pipeline, yielding reliable global poses for synchronized frames. Rare failure cases are complemented with LiDAR SLAM, providing ground-truth trajectories suitable for precise localization.

Sensors Synchronization Each different sensor group is triggered and synced to a common clock, allowing no more than $5$ milliseconds between each unit capture. Cross-modal triggers are temporally aligned to enable near-simultaneous captures. Because our high-resolution cameras use a rolling shutter, showing a row-wise readout, aligning the other modalities to the image start time would induce a systematic temporal offset across rows. Instead, we define the reference timestamp at the image mid-exposure and synchronize LiDAR to this anchor

with a typical $T_{readout}$ of $54$ milliseconds.

### Annotation

We annotate $3$D cuboids through a three-stage pipeline that combines human annotation with automated label refinement. To maximize the richness of the annotated data, human annotators manually curate sequential frames containing complex interactions or edge cases; in total, more than $2000$ scenes are selected. Annotators then label $3$D cuboids and $2$D boxes and assign semantic classes. The selected annotations are subsequently refined automatically to enforce geometric and temporal consistency. For supervised learning tasks, the dataset provides around $140$ k annotated training samples and $25$ k annotated validation samples.

Stage 1: Human Annotation Primitives. During this stage, annotators produce geometric primitives consisting of $3$D cuboids and $2$D boxes (with relative Occlusion and Truncation parameters) and assign semantic labels to all identified objects. $3$D boxes are then iteratively adjusted using their projection into the cameras to reduce offset and avoid "ghost" objects. The annotation procedure results in $85$ classes which we regroup in $9$ main categories as shown in Figure 4(a) ‣ Figure 4 ‣ 3.3 Annotation ‣ 3 TruckDrive Dataset ‣ TruckDrive: Long-Range Autonomous Highway Driving Dataset"). The $9$ classes to be captured are traffic signs, passenger cars, all types of road debris and interferences such as lost cargo, potholes, and cones (collectively referred to as road obstructions), humans, semi-trucks in both their cabins and trailers, $2$-wheeled vehicles, emergency vehicles like police cars, ambulances or road-construction vehicles that can halter the nominal planning behavior and vehicles of different sizes, from heavy-duty vehicles, buses or single unit trucks to RV, trailers and equipment. Vulnerable Road Users are identified and included in the coarser categories.

Stage 2: Primitive Augmentation. For each timestamp we project the initial $3D$ cuboids into all camera views and match them against detections from a $2D$ object detector, by solving a bipartite assignment (Hungarian algorithm) with Intersection-over-Union as cost matrix. When a $2D$ detection has no correspondence, we fall back to the geometric projection or an existing $2D$ label. We handle truncations and perform class-wise Non Maximum Suppression (NMS) to promote high confidence $2D$ detections, resulting in the set of matched 3D detections and 2D-only candidates.

Stage 3: Refinement and Completion. The existing matched $3D$ annotations are transformed into a global coordinate frame and their trajectories are refined through a kinematically constrained optimization, enforcing plausible motion and reducing yaw jitter. Specifically we minimize

subject to a unicycle model

Here, $s_{t}^{k} = {(x_{t}^{k},y_{t}^{k},\psi_{t}^{k},v_{t}^{k},\omega_{t}^{k})}$ is the per-track state, $d_{t}^{k} = {(\ell_{t}^{k},w_{t}^{k},h_{t}^{k})}$ are box sizes, ${c{(s_{t}^{k})}} = {(x_{t}^{k},y_{t}^{k})}$ extracts the box center, hats $\hat{\cdot}$ denote noisy estimates, $\rho{( \cdot )}$ is a robust loss (Huber with scale $\delta_{\rho}$), $ang$ is the angle difference, $\Delta$/$\Delta^{2}$ are first and second finite differences.

For short gaps $t \in {\lbrack t_{1},t_{2}\rbrack}$ with missing frames we initialize bounding boxes by interpolating

then refine jointly using Equations to.

Concurrently, we lift unmatched $2D$ candidates from Stage $2$ into $3D$. For each camera $c$, we project the eight cuboid corners of a 3D hypothesis $p = {(x,y,z,\ell,w,h,\psi)}$ and form the tight axis-aligned 2D box ${\hat{b}}_{c}{(p)}$. We retain only those camera views whose Stage $2$ detection $b_{c,t} = {\lbrack x_{0},y_{0},x_{1},y_{1}\rbrack}$ has sufficient overlap with the hypothesis, defined as ${{IoU}\left( {{\hat{b}}_{c}{(p)}},b_{c,t} \right)} \geq 0.3$, and optimize $p$ so that the projected boxes fit the detections across the retained views

where $z_{g}$ is the local ground height from the accumulated LiDAR map. $3$D objects are then tracked over time with a offline tracker, identity-aligned to ground truth via temporal IoU voting and merged with the smoothed ground-truth boxes to form the final annotation set.

(a) Class Labels Range Distribution

(b) Instances Range Distribution

(c) Ego Speed Distribution

(d) Scene Length Distribution

Figure 4: Dataset Analysis. Our dataset comprises an unprecedented density of instance objects at ranges (greater than 200 meters) yet to be explored in publicly available datasets (a,b), as well as driving speeds 5 times higher (c) and sequences with traveled length up to 8 times longer (d) than existing benchmarks.

### Dataset Analysis

TruckDrive, compared in Table 1 with other benchmarks, introduces an unprecedented sensing configuration with $37$ heterogeneous sensors, double the number available in the second most sensor-rich dataset ($18$), enabling full $360^{\circ}$ perception coverage with both long and short-range redundancy and enhancing robustness in complex environments. TruckDrive's LiDAR extends up to $400$ meters in both the forward and rear directions, twice the maximum range reported in previous benchmarks ($220$ m). The dataset comprises approximately $165,000$ manually annotated frames, which is comparable in scale to the largest publicly available datasets ($230$ k). Per-class instances are distributed uniformly across the full perception range, yielding balanced near and far-field samples (Fig. 4(a) ‣ Figure 4 ‣ 3.3 Annotation ‣ 3 TruckDrive Dataset ‣ TruckDrive: Long-Range Autonomous Highway Driving Dataset")). The density of annotated $3$D boxes decays gradually with distance up to $400$ m (Fig. 4(b) ‣ Figure 4 ‣ 3.3 Annotation ‣ 3 TruckDrive Dataset ‣ TruckDrive: Long-Range Autonomous Highway Driving Dataset")), while $2$D boxes extend well beyond $1000$ m, in contrast to prior urban-focused datasets where annotations beyond $100 - 200$ m are rare and instance density drops sharply after $80$ m. Figures 4(c) ‣ Figure 4 ‣ 3.3 Annotation ‣ 3 TruckDrive Dataset ‣ TruckDrive: Long-Range Autonomous Highway Driving Dataset") and 4(d) ‣ Figure 4 ‣ 3.3 Annotation ‣ 3 TruckDrive Dataset ‣ TruckDrive: Long-Range Autonomous Highway Driving Dataset") highlight highway dynamics in TruckDrive. Speeds span from low on/off ramp segments to up to $130$ km/h, surpassing urban datasets capped below $75$ km/h. Sequences extend to $900$ m (against $400$ m of urban datasets), enabling temporal reasoning at high speed and more faithful evaluation of long-horizon perception and prediction.

## Driving Tasks and Challenges

Figure 5: Driving Tasks and Challenges. We report qualitative results of the best baselines across planning, 2D/3D object detection, depth estimation and scene reconstruction. Even when trained on TruckDrive, existing methods struggle in the long-range, high-speed regime. Planning modules exhibit conservative behavior due to low-speed assumptions. Grid-based BEV models degrade perception as large spatial coverage demands heavy downsampling, erasing safety-critical details such as small debris or lost cargo, while depth methods struggle beyond 200m and in sky regions, revealing limited distance awareness and motivating architectures for highway-scale perception.

We use the proposed dataset at hand to evaluate recent perception and driving methods across typical tasks, such as $2$D and $3$D object detection, tracking, depth estimation, LiDAR forecasting, moving object segmentation, $3$D scene reconstruction and end-to-end planning. This evaluation investigates whether current state-of-the-art approaches, primarily developed and optimized for urban driving datasets, can generalize to the speed, long-range and large-scale highway scenarios present in TruckDrive. To this end, all tested models have been trained on our TruckDrive data. We train all models with a consistent train-validation split made of $140$ and $25$ thousand samples respectively and follow standard metrics and protocols. We couple quantitative with qualitative results for the target domain in Figure 5.

### 2D Object Detection

In nuScenes and KITTI, $2$D performance is largely driven by $3$D detectors due to low image resolution and wide FOV; $3$D NMS in lifted space handles occlusion better than image-space NMS. At kilometer ranges, however, objects in those benchmarks would be sub-pixel, whereas our $8$MP imagery keeps them resolvable, so only $2$D detectors are able detect them. We train state-of-the-art architectures and report results in Table 3.

### 3D Object Detection

We evaluate long-range $3$D object detection using three SOTA models on our dataset, spanning a LiDAR based model, a camera-based method and a common LiDAR-camera fusion architecture. We report average precision over three range bins in Table 4.

### 3D Multi Object Tracking

We evaluate whether state-of-the-art tracking methods can handle the long-horizon scenes and high differential velocities between the ego and other agents in TruckDrive, which stress association over long gaps and occlusions. We report MOT results for a query based approach and two $3$D boxes based methods in Table 5.

Table 3: 2D Object Detection Results. We follow CoCo and report mean average precision (mAP) at 0.50 IoU, mAP at 0.75 IoU, and mAP at short (0 − 50 m, SR), medium (50 − 150 m, MR), long (150 − 250 m, LR), and ultra-long-range (250+, UR).

Table 4: 3D Object Detection Results. We report mAP for 3 baselines using a single or a combination of LiDAR (L) and Camera (C) data, divided into short (0 − 50 m, SR), medium (50 − 150 m, MR), long (150 − 250 m, LR) and full detection ranges.

Table 5: 3D Multi Object Tracking Results. We report AMOTA, AMOTP and Recall for a query based and two LiDAR based methods.† uses inference detections.

### Depth Estimation

We train monocular, stereo and surround depth estimation models under long-range LiDAR supervision to assess the capability of current approaches in the TruckDrive domain. For all subtasks, we report standard task metrics alongside unified, distance-binned depth metrics, ensuring balanced evaluation across ranges and avoiding the near-range bias and limited range-dependent interpretability of disparity-based or relative-error metrics.

Depth Evaluation Ground-Truth. For our benchmark, we build dense LiDAR ground truth by accumulating static points and filtering dynamic objects through the FMCW capabilities of our $4$D LiDAR. The resulting depth map is projected into each frame, where we reintroduce dynamic points based on their timestamps, filter out view-dependent occlusions and enhance temporal consistency using dense depth priors inferred from an ensemble of depth foundation models. Additional details in the Supplementary Material.

Surround Views. Leveraging the wide, calibrated overlap among five high-resolution cameras arranged to ensure extensive, overlapping surround coverage, we train two state-of-the-art models for metric surround depth estimation and report results in Table 6(a) ‣ Table 6 ‣ 4.4 Depth Estimation ‣ 4 Driving Tasks and Challenges ‣ TruckDrive: Long-Range Autonomous Highway Driving Dataset"), evaluated against the dense LiDAR ground truth. Task-specific relative metrics are reported following.

Stereo Views. The forward-facing cameras are arranged in a wide-baseline stereo configuration (approx. $1.57$ m), providing a strong geometric basis for depth perception via triangulation. We evaluate state-of-the-art learning-based stereo matching methods and report results in Table 6(b) ‣ Table 6 ‣ 4.4 Depth Estimation ‣ 4 Driving Tasks and Challenges ‣ TruckDrive: Long-Range Autonomous Highway Driving Dataset"). We report task-specific disparity metrics following the KITTI stereo benchmark.

Monocular View. We benchmark recent existing monocular depth estimation models, which infer depth from single images without geometric priors, to assess their ability to generalize to the scale and appearance of distant objects. Each model is trained twice: once using the same $5$ cameras employed for surround views, and once using the left stereo camera, enabling direct comparison with stereo and surround-view architectures. Results are reported in Table 6(c) ‣ Table 6 ‣ 4.4 Depth Estimation ‣ 4 Driving Tasks and Challenges ‣ TruckDrive: Long-Range Autonomous Highway Driving Dataset"). Task-specific metrics are reported following the KITTI benchmark for monocular depth estimation.

Distance-Binned MAE (Depth)
Task-Specific Depth Metrics

(a) Multi-Camera Surround Depth Estimation

Distance-Binned MAE (Depth)
Task-Specific Disparity Metrics

(b) Stereo Disparity Estimation

Distance-Binned MAE (depth)
Task-Specific Depth Metrics

(c) Monocular Depth Estimation

Table 6: Depth Estimation Results. We report performances for surround (a), stereo (b) and monocular (c) depth estimation tasks. Each method is evaluated with standard accuracy and error metrics at short (0-50m, SR), medium (50-150m, MR), long (150-250m, LR) and ultra (250-1000m, UR) range bins.

### Temporal Scene Modeling and Reconstruction

Predicting future scene geometry is fundamental for safe motion planning. We benchmark recent methods on the LiDAR forecasting task over a challenging $250$ meters Region Of Interest (ROI) ahead of the ego vehicle, comparing a LiDAR-only, a camera-only, and a multi-modal fusion network. We report range-binned results in Table 7. For dynamic modeling, we evaluate a LiDAR-based moving-object segmentation method chosen for its strong out-of-domain generalization. As shown in Table 8, the pretrained model struggles at longer distances, indicating the need for long-range training to improve detection. Beyond discrete object-level tasks, high-fidelity scene reconstruction on long-range data is critical for photorealistic digital twins and dense scene understanding. Therefore, we assess a Neural Radiance Fields (NeRF) and two $3$D Gaussian Splatting (3DGS) methods in Table 9.

Table 7: LiDAR Forecasting Results. We evaluate single and multi-modal state of the arts methods with Chamfer Distances (CD) of 1 and 3 seconds and L1 error.

Table 8: 3D Moving Object Segmentation Results. ‡ indicates results from the public KITTI checkpoint.

Table 9: 3D Reconstruction Quality Results. We report PSNR and SSIM for a NeRF and two 3D Gaussian Splatting methods.

### End2End Driving

Collectively, all tasks above aim at enabling end-to-end planning aligned with TruckDrive's goal of safe, reliable and proactive operation. We train and evaluate UniAD as a recent E2E driving method, extending the ROI from $50$ m to $250$ m and replacing the original camera-only BEV backbone with a LiDAR-based architecture, offering a first E2E benchmark for long-range highway driving. We evaluate UniAD on open-loop planning with standard L2 error, see results in table 10.

Table 10: E2E Planning. We train UniAD on our long range setup and evaluate L2 error for all predicted time intervals.

## Discussion

Our experiments confirm that across all tasks, existing model architectures designed for publicly available short-range data underperform when trained on TruckDrive's long-range regime, with scores monotonically dropping with distance. Camera-only models exhibit the lowest performance, with average $57$% lower mAP for $2$D object detection and up to $99$% lower mAP for $3$D object detection (Far3D ) in far (LR) distances. Architectures relying on camera, limited by compute constraints, necessitate $3 \times$ downsampling of native $8$MP inputs, substantially degrading performance; for instance, Long Range stereo depth estimation exhibits an $8 \times$ MAE increase (BridgeDepth ) due to reduced pixel disparities. LiDAR based and fusion-based architectures are aided in training by the additional long range $3$D representation, but struggle in sustaining the high dimensional complexity of the data and the large translation of objects. As existing methods largely rely on dense BEV representations, extending the maximum range forces either larger grids with fixed resolution, inducing a quadratic memory growth, or coarser cells with fixed grid dimension, degrading localization and association of both smaller objects and far-range instances, as shown Figure 5. As a result, $3$D multi-object tracking performs poorly (average $10$% AMOTA), and we observe drops up to $83\%$ for moving-object segmentation (4DMOS ) and up to $31\%$ for long-range $3$D object detection (BEVFusion ). Finally, UniAD requires extensive down-sampling across the entire architecture to allow the model to fit in the memory. The $250 \times 250$ meters ROI is encoded in a $200 \times 200$ BEV grid over the entire implementation, too coarse to encode useful driving information and not accurate enough to compute meaningful collision metric values. Overall, the model struggles to achieve low L2 planning error even for close future timestamps ($3$ step: $1.71$ m), showcasing how urban-centric architectures fail to scale to long-range and high speed scenarios, highlighting the need for further research to unlock safe and reliable highway driving.

## Conclusion

We introduce an autonomous driving dataset with $2$D annotations up to $1$ km and $3$D annotations up to $400$ m tailored for highway driving. While existing datasets focus on urban passenger car driving, the proposed TruckDrive dataset aims at opening up the research to highway driving where higher speed requires the ego agent to use different trajectories and maneuvers. We specifically focus on heavy-duty commercial trucks, which present an additional layer of complexity due the immense mass and break system lags extending the useful perception range from $80$ m to $400$ m.

Our evaluations on the dataset expose a persistent gap between state-of-the-art methods and the requirements of trucking highway autonomy. Hence, the dataset establishes a benchmark for range-aware, temporally grounded and computationally efficient driving methods that operate safely and reliably at high speed over long distances, and serves as a foundation for future research into driving methods tailored to the unique challenges of highway-scale autonomy, still far less explored than their urban counterpart.
