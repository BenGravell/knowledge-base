<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

TruckDrive: Long-Range Autonomous Highway Driving Dataset

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Safe highway autonomy for heavy trucks remains an open and unsolved challenge: due to long braking distances, scene understanding of hundreds of meters is required for anticipatory planning and to allow safe braking margins. However, existing driving datasets primarily cover urban scenes, with perception effectively limited to short ranges of only up to 100 meters. To address this gap, we introduce TruckDrive, a highway-scale multimodal driving dataset, captured with a sensor suite purpose-built for long range sensing: seven long-range FMCW LiDARs measuring range and radial velocity, three high-resolution short-range LiDARs, eleven 8MP surround cameras with varying focal lengths and ten 4D FMCW radars. The dataset offers 475 thousands samples with 165 thousands densely annotated frames for driving perception benchmarking up to 1,000 meters for 2D detection and 400 meters for 3D detection, depth estimation, tracking, planning and end to end driving over 20 seconds sequences at highway speeds.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We find that state-of-the-art autonomous driving models do not generalize to ranges beyond 150 meters, with drops between 31% and 99% in 3D perception tasks, exposing a systematic long-range gap that current architectures and training signals cannot close.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Autonomous driving methods require scene understanding, robotic planning and control, either implicitly, in an end-to-end fashion, or in explicit modules, including perception, prediction of scene geometry and of the future evolution of relevant agents, tracking of the environment, planning and control.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the last decade, the development of driving methods have been largely driven by learned models trained on driving datasets including KITTI, Cityscapes, nuScenes, Waymo and Argoverse, which predominantly feature urban environments and therefore implicitly bias the development of the field toward short-range perception and low-speed driving. This bias is reflected in the annotation range, which typically extends only $70$--$100$ m from the ego-vehicle.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

For normal passenger cars driving in urban environments, short-range perception is sufficient as lower speeds convert the limited spatial range into enough temporal foresight to support the $5$--$10$ seconds planning horizons of modern prediction and planning stacks. For heavy-duty trucks operating at highway speeds, instead, the safety envelope is dominated by their high-inertia braking requirements. At $120$ km/h, a fully-loaded truck requires over $150$--$200$ m to stop, equivalent to $4.5$--$6$ s of look-ahead perception. Therefore, the necessary braking budget is severely compromised by limited sensing horizons: an $80$ m range provides only about $2.4$ seconds of foresight, and even $100$ m yields merely $3.0$ seconds. This entire window is consumed by sensing and planning latencies, eroding the time required for safe braking actuation before the maneuver can even begin. This leaves a critically insufficient margin for the vehicle's deceleration and renders strategic planning, like merging or lane changes, unfeasible.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Driving architectures for long-range perception and planning are non-trivial: Bird's-Eye-View (BEV) and dense voxel representations scale quadratically with distance, leading to exponential growth in compute and memory. Concurrently, the signal-to-noise ratio of distant objects decreases sharply due to sensor resolution limits and atmospheric attenuation. Sparse and range-aware methods alleviate these issues but remain constrained by calibration drift, temporal uncertainty and sparsity of long-range supervision. Moreover, performance on short-range urban benchmarks has begun to saturate, with a decline in the number of submissions and a flattening in the performance gain (Figure 2), with poor generalization capability beyond $100$ m of models designed around these priors.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To close this gap, we introduce *TruckDrive*, the first large-scale dataset specifically designed for long-range, high-speed autonomous driving. TruckDrive, as presented in Figure 1, extends the perception range by a factor of *five* relative to urban benchmarks, compared in Table 1, providing $2$D annotations up to $1{,}000$ m and corresponding $3$D annotations up to $400$ m, with $15$ to $25$ s temporal clips to support forecasting and end-to-end (E2E) learning. The dataset includes over $475$ k multi-modal synchronized samples, among which $165$ k manually labeled and $310$ k unlabeled for self-supervised and unsupervised research. Our sensor suite integrates high-resolution ($8$MP) short and long focal length cameras, wide-baseline stereo, short and long range $4$D LiDARs and $4$D radars, enabling comprehensive research in perception, prediction and planning.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate state-of-the-art driving methods for urban datasets in diverse tasks and observe drops between $31$ and $99$% in $3$D perception tasks beyond $150$ m, confirming that they do not generalize to long-range regimes. This exposes a fundamental open challenge in current architectures and motivates new directions in efficient representation learning, sensor fusion and long-horizon reasoning.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We make the following contributions: We present a long-range, high-fidelity multi-modal driving dataset that combines high-resolution $8$MP cameras, large-baseline stereo, $4$D LiDARs and $4$D radars, enabling dense $3$D annotations up to $400$ m and $2$D annotations up to 1 km.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide large-scale data comprising $475$ k samples, including $165$ k labeled and $310$ k unlabeled frames, with full raw sensor streams to support supervised, semi-supervised, and self-supervised research.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We establish a highway-scale benchmark for perception, prediction, planning and E2E driving tasks under high-speed, long-range conditions, finding several failure modes and scaling challenges in existing models.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Cityscapes 3D [gählert2020cityscapes3ddatasetbenchmark] 1x Stereo Pair, 1x Gated, 1x FIR Waymo - End2End 2x RGB, 2x RGB Fisheye 1x Stereo Pair, 7x Ring Cameras 1x / 3x Stereo Pair, 9x single Table 1: TruckDrive Benchmark Comparison. Cross-dataset summary of sensors, synced samples and useful ranges. TruckDrive couples 7 long range and 3 short range LiDARs with 10 automotive radars, 9 wide/medium field of view cameras and 1 − 3 long-focal-length wide-baseline stereo cameras. It offers 165 thousands annotated samples and additional 310 thousands unlabeled samples and extends the effective perception range to [−400,+400] meters, focusing on highway long-range scenarios to stress perception capabilities beyond conventional benchmarks. ∗NuPlan provides auto-labeled annotations.

<!-- chunk {"id": "body-0014", "role": "body", "section": "TruckDrive Dataset", "weight": 1.0} -->

We introduce TruckDrive, a long-range, highway-focused dataset designed for heavy-vehicle autonomy. In this section, we first describe the TruckDrive domain and data collection process, emphasizing its diverse driving conditions, specialized sensor suite for high-speed perception and our cross-modal synchronization strategy. We further detail our annotation pipeline, which combines manual labeling with automated multi-view completion and kinematic refinement. Finally, we provide a quantitative analysis and comparison to foundational datasets (from Table 1), demonstrating gains in range, speed and trajectory coverage.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Dataset Domain", "weight": 1.0} -->

TruckDrive targets the driving domain of semi-trucks and other large commercial vehicles, covering scenarios that differ significantly from the urban, car-centric datasets commonly used in autonomous driving research. The dataset contains $3,828$ sequences recorded over $2$ years across $8$ U.S. states (NM, TX, VA, NC, TN, AR, WV, AZ), reaching a diversity-area metric of $1,261.3$ km^2^ ($16.5\times$ WOD). Data collection spans all seasons ($48$% fall, $32$% winter, $15$% spring, $5$% summer) and diverse weather ($80$% sunny/cloudy/overcast, $10$% fog, $10$% precipitation). Sequences last $15–25$ s with an average ego trajectory of $500$ m, comprising mainly highways ($3,244$), followed by extra-urban ($351$) and urban roads ($233$).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Dataset Domain", "weight": 1.0} -->

Driving patterns include $45.8$% cruise/accelerate/brake, $36.5$% lane changes/overtakes, $5.4$% close cut-ins, and $12.3$% complex layouts (work zones, intersections, unprotected turns). Illumination coverage includes $3,285$ daytime, $367$ night, $122$ dusk, and $54$ dawn sequences.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Dataset Domain", "weight": 1.0} -->

Camera LiDAR Radar RCCB AR0820 4D LR Aeries II 3D SR OS0/OS1 4D ARS540 Make OnSemi AEVA Ouster Continental Type RCCB FMCW 4D 3D FMCW 4D Resolution 3848 × 2168 ∼100 lines 64/128 × 2048 — FOV (H×V) 52.8∘ × 28.9∘ 120∘ × 30∘ 360∘ × 90∘/45∘ ±4∘–±20∘ f (Hz) 5–10 10 20 Raw Captures 6.3M 7.8M 6.0M Sync Timestamps 569k 744k 601k Cross-Modal Sync Timestamps: 475k Table 2: Sensor Specifications and Raw Data Scale. We present in detail our sensor platform, including RCCB cameras 3D short-range (SR) LiDARs, a 4D long-range (LR) FMCW LiDAR, and 4D radars, capturing 475 thousands synchronized frames

<!-- chunk {"id": "body-0018", "role": "body", "section": "Long-Range Sensor Setup", "weight": 1.0} -->

Our sensor suite, mounted on a semi-truck, is optimized for reliable perception in high-speed environments. Specifically, we employ $7$ FMCW LiDARs (AEVA Aeries II), capable of measuring up to $400$ meters and providing radial velocity, $3$ short-range LiDARs (Ouster OS0/OS1), to account for blind spots and objects very close to the ego and $10$ $4$D radars (Conti ARS540). Additionally, $11$ to $15$, depending on the configuration, RCCB cameras (9 short/medium focal and $1$ to $3$ long-focal stereo) provide high resolution imaging ($8MP$) at all ranges: QA verifies extrinsic accuracy below $0.015$°, bounding re-projection error beyond $200$m. We report placement and horizontal coverage in Figure 3 and per-sensor specifications in Table 2.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Long-Range Sensor Setup", "weight": 1.0} -->

FMCW Velocity. We rely on Frequency-Modulated Continuous-Wave (FMCW) technology, which allows to capture instantaneous radial velocity $v_{r}$ for each point in the point cloud. The velocity measurement is derived from the Doppler-induced phase shift $\Delta\phi$ through where $\lambda$ is the wavelength and $\theta$ the angle of incidence.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Long-Range Sensor Setup", "weight": 1.0} -->

Geo-Inertial Poses (PPK). For accurate ego motion we fuse data from $2$ GNSS and $4$ IMUs in a tailored Post-Processing Kinematic (PPK) pipeline, yielding reliable global poses for synchronized frames. Rare failure cases are complemented with LiDAR SLAM, providing ground-truth trajectories suitable for precise localization.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Long-Range Sensor Setup", "weight": 1.0} -->

Sensors Synchronization Each different sensor group is triggered and synced to a common clock, allowing no more than $5$ milliseconds between each unit capture. Cross-modal triggers are temporally aligned to enable near-simultaneous captures. Because our high-resolution cameras use a rolling shutter, showing a row-wise readout, aligning the other modalities to the image start time would induce a systematic temporal offset across rows. Instead, we define the reference timestamp at the image mid-exposure and synchronize LiDAR to this anchor with a typical $T_{\mathrm{readout}}$ of $54$ milliseconds.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Annotation", "weight": 1.0} -->

We annotate $3$D cuboids through a three-stage pipeline that combines human annotation with automated label refinement. To maximize the richness of the annotated data, human annotators manually curate sequential frames containing complex interactions or edge cases; in total, more than $2000$ scenes are selected. Annotators then label $3$D cuboids and $2$D boxes and assign semantic classes. The selected annotations are subsequently refined automatically to enforce geometric and temporal consistency. For supervised learning tasks, the dataset provides around $140$ k annotated training samples and $25$ k annotated validation samples.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Annotation", "weight": 1.0} -->

Stage 1: Human Annotation Primitives. During this stage, annotators produce geometric primitives consisting of $3$D cuboids and $2$D boxes (with relative Occlusion and Truncation parameters) and assign semantic labels to all identified objects. $3$D boxes are then iteratively adjusted using their projection into the cameras to reduce offset and avoid "ghost" objects. The annotation procedure results in $85$ classes which we regroup in $9$ main categories as shown in Figure 4(a) ‣ Figure 4 ‣ 3.3 Annotation ‣ 3 TruckDrive Dataset ‣ TruckDrive: Long-Range Autonomous Highway Driving Dataset"). The $9$ classes to be captured are traffic signs, passenger cars, all types of road debris and interferences such as lost cargo, potholes, and cones (collectively referred to as road obstructions), humans, semi-trucks in both their cabins and trailers, $2$-wheeled vehicles, emergency vehicles like police cars, ambulances or road-construction vehicles that can halter the nominal planning behavior and vehicles of different sizes, from heavy-duty vehicles, buses or single unit trucks to RV, trailers and equipment.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Annotation", "weight": 1.0} -->

Vulnerable Road Users are identified and included in the coarser categories.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Annotation", "weight": 1.0} -->

Stage 2: Primitive Augmentation. For each timestamp we project the initial $3D$ cuboids into all camera views and match them against detections from a $2D$ object detector, by solving a bipartite assignment (Hungarian algorithm) with Intersection-over-Union as cost matrix. When a $2D$ detection has no correspondence, we fall back to the geometric projection or an existing $2D$ label. We handle truncations and perform class-wise Non Maximum Suppression (NMS) to promote high confidence $2D$ detections, resulting in the set of matched 3D detections and 2D-only candidates.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Annotation", "weight": 1.0} -->

Concurrently, we lift unmatched $2D$ candidates from Stage $2$ into $3D$. For each camera $c$, we project the eight cuboid corners of a 3D hypothesis $p=(x,y,z,\ell,w,h,\psi)$ and form the tight axis-aligned 2D box $\hat{b}_{c}(p)$. We retain only those camera views whose Stage $2$ detection $b_{c,t}=[x_{0},y_{0},x_{1},y_{1}]$ has sufficient overlap with the hypothesis, defined as $\mathrm{IoU}\!\big(\hat{b}_{c}(p),\,b_{c,t}\big)\geq 0.3$, and optimize $p$ so that the projected boxes fit the detections across the retained views where $z_{g}$ is the local ground height from the accumulated LiDAR map.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Annotation", "weight": 1.0} -->

$3$D objects are then tracked over time with a offline tracker, identity-aligned to ground truth via temporal IoU voting and merged with the smoothed ground-truth boxes to form the final annotation set.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Annotation", "weight": 1.0} -->

(a) Class Labels Range Distribution (b) Instances Range Distribution (c) Ego Speed Distribution (d) Scene Length Distribution Figure 4: Dataset Analysis. Our dataset comprises an unprecedented density of instance objects at ranges (greater than 200 meters) yet to be explored in publicly available datasets (a,b), as well as driving speeds 5 times higher (c) and sequences with traveled length up to 8 times longer (d) than existing benchmarks.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Dataset Analysis", "weight": 1.0} -->

TruckDrive, compared in Table 1 with other benchmarks, introduces an unprecedented sensing configuration with $37$ heterogeneous sensors, double the number available in the second most sensor-rich dataset ($18$), enabling full $360^{\circ}$ perception coverage with both long and short-range redundancy and enhancing robustness in complex environments. TruckDrive's LiDAR extends up to $400$ meters in both the forward and rear directions, twice the maximum range reported in previous benchmarks ($220$ m). The dataset comprises approximately $165,000$ manually annotated frames, which is comparable in scale to the largest publicly available datasets ($230$ k). Per-class instances are distributed uniformly across the full perception range, yielding balanced near and far-field samples (Fig. 4(a) ‣ Figure 4 ‣ 3.3 Annotation ‣ 3 TruckDrive Dataset ‣ TruckDrive: Long-Range Autonomous Highway Driving Dataset")).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Dataset Analysis", "weight": 1.0} -->

The density of annotated $3$D boxes decays gradually with distance up to $400$ m (Fig. 4(b) ‣ Figure 4 ‣ 3.3 Annotation ‣ 3 TruckDrive Dataset ‣ TruckDrive: Long-Range Autonomous Highway Driving Dataset")), while $2$D boxes extend well beyond $1000$ m, in contrast to prior urban-focused datasets where annotations beyond $100-200$ m are rare and instance density drops sharply after $80$ m. Figures 4(c) ‣ Figure 4 ‣ 3.3 Annotation ‣ 3 TruckDrive Dataset ‣ TruckDrive: Long-Range Autonomous Highway Driving Dataset") and 4(d) ‣ Figure 4 ‣ 3.3 Annotation ‣ 3 TruckDrive Dataset ‣ TruckDrive: Long-Range Autonomous Highway Driving Dataset") highlight highway dynamics in TruckDrive. Speeds span from low on/off ramp segments to up to $130$ km/h, surpassing urban datasets capped below $75$ km/h.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Dataset Analysis", "weight": 1.0} -->

Sequences extend to $900$ m (against $400$ m of urban datasets), enabling temporal reasoning at high speed and more faithful evaluation of long-horizon perception and prediction.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Driving Tasks and Challenges", "weight": 1.0} -->

We use the proposed dataset at hand to evaluate recent perception and driving methods across typical tasks, such as $2$D and $3$D object detection, tracking, depth estimation, LiDAR forecasting, moving object segmentation, $3$D scene reconstruction and end-to-end planning. This evaluation investigates whether current state-of-the-art approaches, primarily developed and optimized for urban driving datasets, can generalize to the speed, long-range and large-scale highway scenarios present in TruckDrive. To this end, all tested models have been trained on our TruckDrive data. We train all models with a consistent train-validation split made of $140$ and $25$ thousand samples respectively and follow standard metrics and protocols. We couple quantitative with qualitative results for the target domain in Figure 5.

<!-- chunk {"id": "body-0033", "role": "body", "section": "2D Object Detection", "weight": 1.0} -->

In nuScenes and KITTI, $2$D performance is largely driven by $3$D detectors due to low image resolution and wide FOV; $3$D NMS in lifted space handles occlusion better than image-space NMS. At kilometer ranges, however, objects in those benchmarks would be sub-pixel, whereas our $8$MP imagery keeps them resolvable, so only $2$D detectors are able detect them. We train state-of-the-art architectures and report results in Table 3.

<!-- chunk {"id": "body-0034", "role": "body", "section": "3D Object Detection", "weight": 1.0} -->

We evaluate long-range $3$D object detection using three SOTA models on our dataset, spanning a LiDAR based model, a camera-based method and a common LiDAR-camera fusion architecture. We report average precision over three range bins in Table 4.

<!-- chunk {"id": "body-0035", "role": "body", "section": "3D Multi Object Tracking", "weight": 1.0} -->

We evaluate whether state-of-the-art tracking methods can handle the long-horizon scenes and high differential velocities between the ego and other agents in TruckDrive, which stress association over long gaps and occlusions. We report MOT results for a query based approach and two $3$D boxes based methods in Table 5.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Depth Estimation", "weight": 1.0} -->

We train monocular, stereo and surround depth estimation models under long-range LiDAR supervision to assess the capability of current approaches in the TruckDrive domain. For all subtasks, we report standard task metrics alongside unified, distance-binned depth metrics, ensuring balanced evaluation across ranges and avoiding the near-range bias and limited range-dependent interpretability of disparity-based or relative-error metrics.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Depth Estimation", "weight": 1.0} -->

Depth Evaluation Ground-Truth. For our benchmark, we build dense LiDAR ground truth by accumulating static points and filtering dynamic objects through the FMCW capabilities of our $4$D LiDAR. The resulting depth map is projected into each frame, where we reintroduce dynamic points based on their timestamps, filter out view-dependent occlusions and enhance temporal consistency using dense depth priors inferred from an ensemble of depth foundation models. Additional details in the Supplementary Material.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Depth Estimation", "weight": 1.0} -->

Surround Views. Leveraging the wide, calibrated overlap among five high-resolution cameras arranged to ensure extensive, overlapping surround coverage, we train two state-of-the-art models for metric surround depth estimation and report results in Table 6(a) ‣ Table 6 ‣ 4.4 Depth Estimation ‣ 4 Driving Tasks and Challenges ‣ TruckDrive: Long-Range Autonomous Highway Driving Dataset"), evaluated against the dense LiDAR ground truth. Task-specific relative metrics are reported following.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Depth Estimation", "weight": 1.0} -->

Stereo Views. The forward-facing cameras are arranged in a wide-baseline stereo configuration (approx. $1.57$ m), providing a strong geometric basis for depth perception via triangulation. We evaluate state-of-the-art learning-based stereo matching methods and report results in Table 6(b) ‣ Table 6 ‣ 4.4 Depth Estimation ‣ 4 Driving Tasks and Challenges ‣ TruckDrive: Long-Range Autonomous Highway Driving Dataset"). We report task-specific disparity metrics following the KITTI stereo benchmark.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Depth Estimation", "weight": 1.0} -->

Monocular View. We benchmark recent existing monocular depth estimation models, which infer depth from single images without geometric priors, to assess their ability to generalize to the scale and appearance of distant objects. Each model is trained twice: once using the same $5$ cameras employed for surround views, and once using the left stereo camera, enabling direct comparison with stereo and surround-view architectures. Results are reported in Table 6(c) ‣ Table 6 ‣ 4.4 Depth Estimation ‣ 4 Driving Tasks and Challenges ‣ TruckDrive: Long-Range Autonomous Highway Driving Dataset"). Task-specific metrics are reported following the KITTI benchmark for monocular depth estimation.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Depth Estimation", "weight": 1.0} -->

Distance-Binned MAE (Depth) Task-Specific Depth Metrics (a) Multi-Camera Surround Depth Estimation Distance-Binned MAE (Depth) Task-Specific Disparity Metrics (b) Stereo Disparity Estimation Distance-Binned MAE (depth) Task-Specific Depth Metrics (c) Monocular Depth Estimation Table 6: Depth Estimation Results. We report performances for surround (a), stereo (b) and monocular (c) depth estimation tasks. Each method is evaluated with standard accuracy and error metrics at short (0-50m, SR), medium (50-150m, MR), long (150-250m, LR) and ultra (250-1000m, UR) range bins.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Temporal Scene Modeling and Reconstruction", "weight": 1.0} -->

Predicting future scene geometry is fundamental for safe motion planning. We benchmark recent methods on the LiDAR forecasting task over a challenging $250$ meters Region Of Interest (ROI) ahead of the ego vehicle, comparing a LiDAR-only, a camera-only, and a multi-modal fusion network. We report range-binned results in Table 7. For dynamic modeling, we evaluate a LiDAR-based moving-object segmentation method chosen for its strong out-of-domain generalization. As shown in Table 8, the pretrained model struggles at longer distances, indicating the need for long-range training to improve detection. Beyond discrete object-level tasks, high-fidelity scene reconstruction on long-range data is critical for photorealistic digital twins and dense scene understanding. Therefore, we assess a Neural Radiance Fields (NeRF) and two $3$D Gaussian Splatting (3DGS) methods in Table 9.

<!-- chunk {"id": "body-0043", "role": "body", "section": "End2End Driving", "weight": 1.0} -->

Collectively, all tasks above aim at enabling end-to-end planning aligned with TruckDrive's goal of safe, reliable and proactive operation. We train and evaluate UniAD as a recent E2E driving method, extending the ROI from $50$ m to $250$ m and replacing the original camera-only BEV backbone with a LiDAR-based architecture, offering a first E2E benchmark for long-range highway driving. We evaluate UniAD on open-loop planning with standard L2 error, see results in table 10.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our experiments confirm that across all tasks, existing model architectures designed for publicly available short-range data underperform when trained on TruckDrive's long-range regime, with scores monotonically dropping with distance. Camera-only models exhibit the lowest performance, with average $57$% lower mAP for $2$D object detection and up to $99$% lower mAP for $3$D object detection (Far3D ) in far (LR) distances. Architectures relying on camera, limited by compute constraints, necessitate $3\times$ downsampling of native $8$MP inputs, substantially degrading performance; for instance, Long Range stereo depth estimation exhibits an $8\times$ MAE increase (BridgeDepth ) due to reduced pixel disparities. LiDAR based and fusion-based architectures are aided in training by the additional long range $3$D representation, but struggle in sustaining the high dimensional complexity of the data and the large translation of objects.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Discussion", "weight": 1.5} -->

As existing methods largely rely on dense BEV representations, extending the maximum range forces either larger grids with fixed resolution, inducing a quadratic memory growth, or coarser cells with fixed grid dimension, degrading localization and association of both smaller objects and far-range instances, as shown Figure 5. As a result, $3$D multi-object tracking performs poorly (average $10$% AMOTA), and we observe drops up to $83\%$ for moving-object segmentation (4DMOS ) and up to $31\%$ for long-range $3$D object detection (BEVFusion ). Finally, UniAD requires extensive down-sampling across the entire architecture to allow the model to fit in the memory. The $250\times 250$ meters ROI is encoded in a $200\times 200$ BEV grid over the entire implementation, too coarse to encode useful driving information and not accurate enough to compute meaningful collision metric values.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Discussion", "weight": 1.5} -->

Overall, the model struggles to achieve low L2 planning error even for close future timestamps ($3$ step: $1.71$ m), showcasing how urban-centric architectures fail to scale to long-range and high speed scenarios, highlighting the need for further research to unlock safe and reliable highway driving.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduce an autonomous driving dataset with $2$D annotations up to $1$ km and $3$D annotations up to $400$ m tailored for highway driving. While existing datasets focus on urban passenger car driving, the proposed TruckDrive dataset aims at opening up the research to highway driving where higher speed requires the ego agent to use different trajectories and maneuvers. We specifically focus on heavy-duty commercial trucks, which present an additional layer of complexity due the immense mass and break system lags extending the useful perception range from $80$ m to $400$ m.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our evaluations on the dataset expose a persistent gap between state-of-the-art methods and the requirements of trucking highway autonomy. Hence, the dataset establishes a benchmark for range-aware, temporally grounded and computationally efficient driving methods that operate safely and reliably at high speed over long distances, and serves as a foundation for future research into driving methods tailored to the unique challenges of highway-scale autonomy, still far less explored than their urban counterpart.
