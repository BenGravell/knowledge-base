<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Road Ahead in Autonomous Driving: The KITScenes Multimodal Dataset

Topics include Autonomous driving, Driving datasets, Multimodal datasets, HD maps, 4D radar, LiDAR, Online map construction, End-to-end driving.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces KITScenes Multimodal, a European autonomous-driving dataset with synchronized high-resolution cameras, long-range lidar, 4D radar, redundant localization, and unusually detailed 3D HD maps. The dataset is positioned to complement existing driving corpora with richer map topology, irregular urban geography, and benchmarks for mapping, depth, novel-view synthesis, and end-to-end driving.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Existing autonomous driving datasets have enabled major progress, but fall short in sensor fidelity, map completeness, or geographic diversity. We present KITScenes Multimodal, a European dataset built around high-fidelity sensors and maps. Our fully synchronized sensor suite combines high-resolution global-shutter cameras, long-range lidar beyond 400m, 4D imaging radar, and redundant GNSS/INS localization. Our HD maps are, to our knowledge, the most complete of any sensor dataset, validated through autonomous driving trials on open-source software. For the first time in a public dataset, all driving-relevant traffic elements, such as traffic lights, are mapped in 3D to a reprojection-accurate level with full topological connectivity. Recorded in cities with irregular street layouts and mixed traffic modes, our dataset complements existing datasets by broadening the available geographic diversity. We also introduce four benchmarks, each advancing spatial learning for embodied AI: online HD map construction, long-range depth estimation, novel view synthesis, and end-to-end driving.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Autonomous driving datasets \[geiger2012kitti, caesar2020nuscenes, sun2020waymo_perception, ettinger2021waymo_motion\] have enabled significant progress in both computer vision and autonomous driving research. However, existing datasets still fall short of capturing the complexity required for spatially aware driving in dense urban environments. Some lack public annotations or topology-aware map references \[caesar2020nuscenes, sun2020waymo_perception\], while others focus on comparatively simple driving scenarios such as motorways \[fent2024truckscenes, ghilotti2026truckdrive\]. As autonomous driving systems move toward deeper spatial understanding, datasets must support reasoning not only about objects, but also about geometry, road structure, and their geospatial relationships. High-fidelity datasets enriched with geospatial annotations, HD maps, and 3D labels are essential for evaluating such capabilities.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

High-fidelity datasets with geospatial annotations have a limited geographic footprint, with coverage heavily skewed toward North America and Asia. KITTI \[geiger2012kitti\], though seminal, is small-scale; ZOD \[alibeigi2023zenseact\] annotates only single keyframes with image-space labels; and large-scale recording efforts such as those from Nvidia \[nvidia2025physicalai_av\] still lack public annotations. Consequently, complex European urban environments remain underrepresented in current autonomous driving benchmarks, arguably being the most difficult to spatially reason about. This leaves a clear need for datasets that combine high-fidelity sensing, complete geospatial context, and dense 3D annotations.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present KITScenes Multimodal, a dataset recorded across diverse European urban environments using a state-of-the-art robotaxi sensor platform. Our dataset addresses the geographic gap in existing benchmarks while simultaneously raising the bar on both sensor fidelity and geospatial understanding. Our sensor platform combines high-resolution cameras (up to $16.2\text{\,}\mathrm{Mpx}$), long-range lidar with effective range beyond $400\text{\,}\mathrm{m}$, 4D imaging radar, and redundant GNSS, all hardware-synchronized and processed with high-fidelity pipelines that make the data suitable for applications such as neural rendering and novel view synthesis. Besides high fidelity sensor data, we provide the most complete HD maps of any public autonomous driving dataset. Annotated in Lanelet2 \[poggenhans2018lanelet2\], our maps visualized in Figure˜1 cover all regulatory road feature and traffic sign classes, and host our annotated 3D traffic lights, signs, and poles with reprojection-accurate localization.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To demonstrate the unique strengths of the dataset, we introduce four benchmarks: Complete online HD map perception, evaluating relational Lanelet2 map prediction from sensor data; long-range monocular depth estimation, targeting depth beyond $200\text{\,}\mathrm{m}$ where current methods degrade severely; novel view synthesis, exploiting our high-fidelity imagery and dense lidar for 3D scene reconstruction; and multimodal end-to-end models for autonomous driving, predicting future trajectories and scene evolution from camera, lidar, and radar inputs. Our contributions include: A multimodal European driving dataset, recorded in three cities with a high-fidelity robotaxi sensor suite: $72.5\text{\,}\mathrm{Mpx}$ of synchronized global-shutter cameras, seven lidars with over $3\times$ the point density and twice the effective range of the next closest dataset, three 4D imaging radars, and redundant GNSS/INS.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Production-grade Lanelet2 HD maps covering $62\text{\,}{\mathrm{km}}^{2}$ with 29 road-feature classes, 120 traffic-sign classes, and 3D traffic lights, signs, and poles localized to reprojection accuracy. The maps include all regulatory elements required for autonomous navigation and are validated for use in the open-source Autoware \[autoware\] stack, both online and in simulation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Four benchmarks designed to expose the limits of current methods on the path to Level 4 autonomy, targeting capabilities existing datasets cannot benchmark at this fidelity: holistic HD map prediction, depth estimation beyond $200\text{\,}\mathrm{m}$, high-fidelity novel view synthesis, and multi-modal end-to-end driving.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Autonomous Driving Datasets for Perception", "weight": 1.0} -->

The past decade has seen a rapid growth of autonomous driving datasets. Foundational datasets such as nuScenes \[caesar2020nuscenes\], Waymo Open \[sun2020waymo_perception\], and Argoverse 2 \[wilson2021argoverse2\] established the multimodal paradigm with complementary sensor configurations and annotation schemes. Further datasets \[huang2018apolloscape, mao2021once\] broaden the range of traffic layouts and driving conditions, although detailed map annotations and deployment-oriented perception support remain limited. KITTI \[geiger2012kitti\] and KITTI-360 \[Liao2022PAMI\] remain influential but limited in scale and sensor diversity by current standards. ZOD \[alibeigi2023zenseact\] provides large-scale recordings, yet annotates only a single keyframe per scenario and mainly provides image-space labels. MAN TruckScenes \[fent2024truckscenes\] focuses on motorway trucking rather than complex urban perception.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Autonomous Driving Datasets for Perception", "weight": 1.0} -->

While TruckDrive \[ghilotti2026truckdrive\] features long-range sensors, it likewise targets trucking scenarios, relies on automotive RCCB cameras, and has not released any public data to date. Large-scale fleet recordings such as Nvidia Physical AI AV \[nvidia2025physicalai_av\] provide broad real-world coverage but lack public annotations. A quantified comparison of the sensor setups is shown in Table˜1.

<!-- chunk {"id": "body-0012", "role": "body", "section": "HD Maps and Map Perception Benchmarks", "weight": 1.0} -->

Map representations accompanying public datasets vary substantially in completeness. nuScenes \[caesar2020nuscenes\] and Argoverse 2 \[wilson2021argoverse2\] expose lane geometry via dataset-specific APIs but omit regulatory structure from traffic lights and signs. OpenLane-V2 \[wang2023openlanev2\] adds lane-topology links, but as image-space annotations rather than metric 3D maps. To our knowledge, no prior dataset provides HD maps that are simultaneously reprojection-accurate, complete in regulatory structure (traffic signs, lights, lane assignments), and validated in a planning stack (Table˜2).

<!-- chunk {"id": "body-0013", "role": "body", "section": "HD Maps and Map Perception Benchmarks", "weight": 1.0} -->

As a consequence, so far online HD map construction methods \[li2022hdmapnet, liu2023vectormapnet, liao2022maptr, maptrv2, yuan2024streammapnet, qiao2023bemapnet, ding2023pivotnet, wang2024stream_sqd_mapnet, chen2024maptracker, zhang2024enhancing_HR_mapnet, shi2024globalmapnet, zhang2025mapexpert, yang2025histrackmap, erdougan2025mapping_skeptic\] are evaluated on simple geometric primitives only (lane dividers without type, pedestrian crossings, road borders). Lanelet2 \[poggenhans2018lanelet2\] has emerged as the open academic standard for HD maps, encoding geometry, topology, and 3D regulatory elements in a single graph; it is the native input of Autoware \[autoware\] and translatable to learning-friendly representations using \[immel2024lanelet2mlconverter\].

<!-- chunk {"id": "body-0014", "role": "body", "section": "Long-range Perception, Neural Rendering, and End-to-End Driving", "weight": 1.0} -->

Monocular depth estimation is predominantly benchmarked on KITTI \[geiger2012kitti\] and DDAD \[guizilini2020ddad\]; recent foundation models \[depthanything3, ganesan2026unidacuniversalmetricdepth\] achieve strong near-range performance, but existing benchmarks rarely assess depth beyond 80--100 m. Neural scene representations for driving like NeRF-based \[wu2023mars, yang2024emernerf\] and 3D Gaussian Splatting methods \[yan2024street, chen2025omnire, yu2026_recondrive\], are similarly constrained by input image fidelity and lidar density. End-to-end driving models \[hu2023uniad, jiang2023vad\] and world models are evaluated almost exclusively on nuScenes, limiting the sensor configurations and geographies under which they are assessed.

<!-- chunk {"id": "body-0015", "role": "body", "section": "High-Resolution Long-Range Multi-Modal Sensor Setup", "weight": 1.0} -->

KITScenes Multimodal uses a fully synchronized sensor suite. Figure˜2 depicts the sensor positions and their nominal fields of view. To enable sensor fusion up to maximum effective sensing range, we perform intrinsic and extrinsic calibration across all modalities, achieving subpixel intrinsic and $1\text{\,}\mathrm{cm}$ and $0.1\text{\,}\mathrm{\SIUnitSymbolDegree}$ extrinsic accuracy. Further details are listed in Appendix˜A and Appendix˜B.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Cameras", "weight": 1.0} -->

The camera suite comprises six $7.1\text{\,}\mathrm{Mpx}$ surround cameras providing full $360\text{\,}\mathrm{\SIUnitSymbolDegree}$ coverage, one $16.2\text{\,}\mathrm{Mpx}$ high-resolution long-range camera, and a tilted forward-facing stereo setup, yielding a combined resolution of $72.5\text{\,}\mathrm{Mpx}$ per frame, which is more than twice that of the next closest dataset (Table˜1). Existing setups put their focus on dynamic object perception \[caesar2020nuscenes, sun2020waymo_perception, fent2024truckscenes, wilson2021argoverse2\], triggering the cameras when the lidar sweeped across the image center to ensure a minimal delay between both modalities. All cameras use global shutter sensors and are hardware-synchronized, ensuring pixel-accurate temporal alignment.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Cameras", "weight": 1.0} -->

The images are anonymized and compressed with JPEGLI \[szabadka2024jpegli\], a state-of-the-art visually lossless codec described in Section˜A.1. This is the foundation for our high fidelity ground truth for neural rendering and novel synthesis. At the same time, we ensure lidar coverage by redundantly combining multiple lidars with varying sweeping directions.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Lidar", "weight": 1.0} -->

Seven lidar sensors provide $360\text{\,}\mathrm{\SIUnitSymbolDegree}$ coverage with substantial overlap between adjacent units. As shown in Table˜1, the fused point cloud contains on average more than $900\text{\,}\mathrm{k}$ points per frame with peaks above $1.2\text{\,}\mathrm{M}$ points, tripling the effective point density over existing datasets. The use of $1550\text{\,}\mathrm{nm}$ lidars enables an average maximum range of more than $400\text{\,}\mathrm{m}$, nearly doubling that of the next-best dataset. This long-range capability is essential for both online long-range perception and for providing ground truth for benchmarks, such as monocular depth estimation. Figure˜7 compares the per-distance-bin return density for KITScenes and existing autonomous driving datasets, showing that KITScenes provides higher effective point density in every bin and extends usable range beyond $250\text{\,}\mathrm{m}$, where prior datasets fall to zero.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Lidar", "weight": 1.0} -->

nuScenes [caesar2020nuscenes] ONCE [mao2021once] nuPlan Sensors [caesar2021nuplan] Argoverse 2 Sensor [wilson2021argoverse2] WOD Perception [sun2020waymo_perception] MAN TruckScenes [fent2024truckscenes] Zenseact Open [alibeigi2023zenseact] Nvidia PhysicalAI AV [nvidia2025physicalai_av] Monocular cameras, Stereo camera pair, MPix = Total resolution per frame, Comp. = Image compression Table 1: KITScenes Multimodal sets a new state of the art for temporally consistent high-resolution high-fidelity RGB surround vision, highly dense long-range lidar, and ranging modality coverage. We triple the average lidar point density and almost double the typical maximum range; see also Figure˜7.

<!-- chunk {"id": "body-0020", "role": "body", "section": "HD Map Annotation", "weight": 1.0} -->

Lane border [-0.08em]type WOD Perception [sun2020waymo_perception] nuPlan Sensors† [caesar2021nuplan] AV2 TbV [av2_trust_but_verify] Nvidia PhysicalAI AV [nvidia2025physicalai_av] nuScenes [caesar2020nuscenes] Argoverse 2 Sensor [wilson2021argoverse2] OpenLane-V2 [wang2023openlanev2] †Remarks: nuPlan Sensor [caesar2021nuplan]: shorthand for the 10% of scenes in nuPlan with available sensor data. traffic light states available trough offline state estimation, no linkage to sensor data. NVIDIA PhysicalAI AV: entries transparent filled based on current publically available release plans, not verified. OpenLaneV2: built on top of sensor data of AV2 and nuScenes, with limited set of labeled traffic element 2D bounding boxes in a visible range of 25x50m at 2Hz. All sensors: full suite and quality of original sensor dataset available.

<!-- chunk {"id": "body-0021", "role": "body", "section": "HD Map Annotation", "weight": 1.0} -->

OSS AD stack: Native support of HD map for simulation and closed-loop driving with open-source software autonomous driving stack. Full spatial learning: support for full resolution multimodal 360∘ surround view learning with a at least a base set of BEV annotations. Table 2: Comparison of related datasets comprised of HD maps and sensor data, datasets from Table˜1 without HD maps are not listed. Legend: yes, partial/limited, no;: unreleased data; ↑: large coverage based on dataset description which is not reported or reproduced area coverage.

<!-- chunk {"id": "body-0022", "role": "body", "section": "HD Map Annotation", "weight": 1.0} -->

We provide pixel-accurate 3D maps that can be directly used in the open-source Autoware \[autoware\] stack, both for simulation and real-world autonomous driving. All maps are annotated in Lanelet2 \[poggenhans2018lanelet2\], an established open-source format for semantic HD maps. Beyond geometry, each map encodes the full regulatory structure required for autonomous driving: Road level polylines are annotated with one of 29 classes, (*e.g*., road border, dashed, zebra-crossing *etc*.) traffic signs are classified based on 220 German road traffic code classes \[carnot2026gtsign\] (with 120 observed), traffic lights types are grouped into four categories (car, bike, pedestrian, misc). All traffic signs and lights are explicitly assigned to the lanes they govern via toplogical links in the Lanelet2 format. Traffic lights, road signs, and poles are annotated based on lidar and camera data as 3D shapes including orientation that are reprojection-accurate to the calibrated camera images \[pauls2021automatic\].

<!-- chunk {"id": "body-0023", "role": "body", "section": "HD Map Annotation", "weight": 1.0} -->

This reprojection accuracy directly connects map labels to image pixels, enabling HD map annotations to be used as pixel-level training signal for perception models without any additional alignment step, as shown in Section˜4.1.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Dataset Statistics", "weight": 1.0} -->

Our current release contains $1007$ \\qtyrange1060 scenarios totaling $5.7\text{\,}\mathrm{h}$ and $162\text{\,}\mathrm{km}$ of synchronized multimodal recording at $10\text{\,}\mathrm{Hz}$. Details on the split and label statistics can be found in Appendix˜G. The dataset currently spans Karlsruhe, Frankfurt, and Sindelfingen, chosen for their unique environments of a planned 18^th^ century radial layout, a dense metropolitan financial district core, and a suburban-industrial mix. Recordings took place across summer 2025 and winter 2025/26 to expose models to seasonal appearance changes and a wide coverage as visualized in Figure˜3.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Benchmarks", "weight": 1.0} -->

Our benchmarks span spatial learning from map-level scene understanding to multimodal end-to-end driving. They expose limitations of existing methods that prior datasets cannot reveal.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Online HD Map Construction", "weight": 1.0} -->

Online HD map construction aims to predict a structured, drivable map directly from onboard sensor data, without relying on pre-built prior maps. Existing benchmarks evaluate the prediction of simple geometric primitives such as lane dividers and pedestrian crossings \[maptrv2\], leading to a saturation of existing benchmarks, as shown in Figure˜4(a). We enable a substantially more complete formulation: our Lanelet2 maps encode lane topology, regulatory elements, traffic signs, and traffic lights with their lane assignments, allowing models to be evaluated on predicting the full Lanelet2 map structure. As a baseline for topology prediction, we extend MapQR \[liu2024mapqr\] with a graph neural network (GNN) head that consumes the map element tokens from the decoder and predicts pairwise relations between all predicted map elements (hereafter called MapQR-Topo). Architecture and implementation details are described in Section˜H.1.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Results", "weight": 1.0} -->

In Table˜3, we evaluate MapTRv2 \[maptrv2\] as a widely adopted camera-only baseline and SDTagNet \[immel2026sdtagnet\] as a representative of methods that leverage SD map priors. Both exhibit a large performance drop on our complete formulation compared to existing benchmarks, revealing a gap hidden by the currently limited task scope, with SDTagNet benefiting more from the richer formulation. This suggests that structured prior knowledge becomes increasingly valuable as the task approaches real-world complexity. An example of prediction outputs is provided in Figure˜4(b). A qualitative example the predicted topology by MapQR-Topo is shown in Figure˜17 in the Appendix.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Results", "weight": 1.0} -->

(a) Historical SOTA progression of online HD map construction models [liu2023vectormapnet, liao2022maptr, maptrv2, yuan2024streammapnet, wang2024stream_sqd_mapnet, chen2024maptracker, zhang2024enhancing_HR_mapnet, shi2024globalmapnet, zhang2025mapexpert, yang2025histrackmap, immel2026sdtagnet, erdougan2025mapping_skeptic] on AV2 [wilson2021argoverse2]. A saturation on the current datasets, perception range and task complexity can be seen after the introduction of Maptracker [chen2024maptracker].

<!-- chunk {"id": "body-0029", "role": "body", "section": "Results", "weight": 1.0} -->

(b) Example online HD map construction prediction of SDTagNet [immel2026sdtagnet] on a validation sample. While showing new capabilities such as 3D detection of non-ground elements thanks to the extensive map labels, a large gap in prediction of complete 3D HD maps remains.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Results", "weight": 1.0} -->

SDTagNet [immel2026sdtagnet] Table 3: Evaluation of online HD map perception models. For readability, the classes are grouped into 6 categories for the average precision: Lane Markings (LM), Lane Centerlines (LC), Road Infrastructure (RI), Traffic Lights (TL), Traffic Signs (TS) and Road Markings (RM). For the topology prediction baseline MapQR-Topo we additionally report the topology score.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Long-range Monocular Depth Estimation", "weight": 1.0} -->

Monocular depth estimation has made rapid progress on near-range benchmarks, yet autonomous driving at highway speeds and in complex intersections requires reliable depth estimates well beyond $100\text{\,}\mathrm{m}$. We show that current depth estimation models trained and evaluated on existing datasets fail to generalize to long-range distances, as their training signal is dominated by close-range lidar returns. We provide a dedicated benchmark for long-range monocular depth estimation, enabling the first systematic evaluation of depth estimation at ranges that extend beyond $400\text{\,}\mathrm{m}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Long-range Monocular Depth Estimation", "weight": 1.0} -->

UniDAC [ganesan2026unidacuniversalmetricdepth] Depth Anything 3 [depthanything3] MapAnything [keetha2026mapanything] Table 4: Range-stratified metric depth estimation exposes a ranking inversion: MapAnything dominates overall and at \qtyrange[range-phrase=–]0100 but degrades severely beyond it, while UniDAC, ranked last overall, is the strongest long-range estimator. Regardless, all methods perform poorly beyond 200 m.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Long-range Monocular Depth Estimation", "weight": 1.0} -->

We report established metrics for monocular depth evaluation: absolute relative error (AbsRel) and threshold accuracy $\delta_{1}$. Scores are reported stratified into close range (\\qtyrange\[range-phrase=--\]0100), medium range (\\qtyrange\[range-phrase=--\]100200) and far range (\\qty\>200), and overall. A detailed description of the setup and ground truth generation can be found in Section˜H.2.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Results", "weight": 1.0} -->

We evaluate UniDAC \[ganesan2026unidacuniversalmetricdepth\], Depth Anything 3 \[depthanything3\], and MapAnything \[keetha2026mapanything\], all reported to achieve dataset-agnostic SOTA monocular depth estimation. They provide strong performance at close range, but fall short as early as \\qty75 (see Figure˜7). Table˜4 reveals a critical limitation of aggregate evaluation: overall metrics mask severe performance inversions across depth ranges. MapAnything dominates the \\qtyrange\[range-phrase=--\]0100 range and ranks first overall, yet degrades significantly beyond it. UniDAC, ranked last overall, is in fact the strongest long-range estimator by a significant margin. Regardless, no method achieves reliable performance beyond \\qty200 (further evaluations in Section˜H.2). With its comprehensive LiDAR setup, KITScenes is uniquely positioned (see Figure˜7) to expose such limitations, providing the long-range ground truth density necessary to benchmark methods where current autonomous driving datasets fall short.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Novel View Synthesis", "weight": 1.0} -->

Neural scene representations and novel view synthesis (NVS) methods have emerged as powerful tools for autonomous driving simulation and data augmentation. Common NVS methods \[yan2024street, chen2025omnire, yu2026_recondrive\] are evaluated using pixel-based metrics, but this strongly relies on the availability of ground truth images at target viewpoints, which are typically restricted to the original driven trajectory. While lateral novel view synthesis is critical for autonomous driving simulation, its quality is often judged only through qualitative inspection \[yu2026_recondrive\] and image-based metrics \[unisim, ni2025recondreamer\]. However, those often fail to reveal subtle structural distortions that can significantly impact downstream perception tasks. To probe geometric fidelity at novel lateral poses, we introduce a map-based NVS evaluation benchmark using traffic sign recall.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Novel View Synthesis", "weight": 1.0} -->

We re-render the scene at seven lateral offsets $\Delta y\in\{-3,\ldots,+3\}$ m and project ground-truth traffic signs from our HD map into each shifted viewpoint, applying lidar-based occlusion filtering to retain only unoccluded signs. We report traffic sign recall at both a low resolution ($280{\times}518$, matching the model's output) and a high resolution ($1600{\times}2844$, the cropped sensor resolution), with the real photograph serving as the per-scale upper bound. A full description is given in Section˜H.3.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Results", "weight": 1.0} -->

As shown in Table˜5, evaluating ReconDrive \[yu2026_recondrive\] reveals a sharp collapse in structural fidelity: even at the driven trajectory ($\Delta y{=}0$), upsampling to the sensor's cropped resolution yields a $27.8\%$ relative recall drop, nearly four times the $7.6\%$ drop at low resolution. This indicates that the reconstruction lacks fine-grained structural detail. With lateral translation, degradation exceeds $80\%$ relative recall loss at $\Delta y{=}\pm 3$ m, showing that current NVS methods struggle to maintain geometric integrity in novel views, a limitation hidden by standard photometric metrics. A qualitative example of lacking 3D consistency is shown in Figure˜9, where the traffic sign fails to maintain its true 3D position after a viewpoint shift. More details, further qualitative comparison in Figure˜19 and standard photometric metrics are provided in Section˜H.3.

<!-- chunk {"id": "body-0038", "role": "body", "section": "End-to-End Driving", "weight": 1.0} -->

End-to-end driving and neural world models are evaluated almost exclusively on nuScenes, narrowing the sensor configurations, geographies, and map-grounded behaviours under which they are assessed. KITScenes Multimodal supports three input tiers on identical scenes, i.e., a single front-view camera, the full $360\text{\,}\mathrm{\SIUnitSymbolDegree}$ surround-view, and the complete multi-modal suite with lidar and radar, enabling controlled modality ablations with a novel combination of benchmark metrics. Headline baselines reported here are camera-only; sensor and timing data for all tiers are released, leaving multi-modal e2e training as an open challenge. Evaluation setup, split details, and the held-out test-e2e leaderboard split are described in Section˜H.4.

<!-- chunk {"id": "body-0039", "role": "body", "section": "End-to-End Driving", "weight": 1.0} -->

Beyond standard ADE and FDE \[alahi2016social\], we leverage our centimetre-accurate Lanelet2 maps and a lidar-derived occupancy layer to evaluate three map-grounded safety metrics: *drivable-surface survival*, *collision-free rate*, and *centerline distance*, serving as an offline proxy for safety properties usually assessed only in closed-loop simulation. To decouple correctness from a single expert trajectory, we additionally adopt the *Multi-Maneuver Score* (MMS) \[wagner2026longtail\], scoring each prediction against the best of at least three human-annotated admissible maneuvers per scene. Metric definitions and per-horizon profiles are detailed in Section˜H.4.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Results", "weight": 1.0} -->

DMAD [shen2025dmad] SSR [li2025ssr] (non-temp.)

<!-- chunk {"id": "body-0041", "role": "body", "section": "Results", "weight": 1.0} -->

SSR [li2025ssr] (temporal) Epona [zhang2025epona] (AR, 10) Epona [zhang2025epona] (AR, 100) Epona [zhang2025epona] (SS, 10) Epona [zhang2025epona] (SS, 100) For SSR, non-temp. uses only the current keyframe whereas temporal aggregates BEV features across multiple frames. Epona is evaluated with single-step (SS) or autoregressive (AR) rollouts; 10 and 100 denote the number of diffusion denoising steps. Table 6: End-to-end results on 200 nine-second e2e samples with all metrics evaluated at the 3 s horizon. ADE and FDE follow [alahi2016social]; the map-grounded metrics drivable-surface survival, collision-free rate, and centerline distance leverage our HD maps together with a lidar-based occupancy layer. ADE is additionally broken out by scene category. Best values are bold, second-best underlined.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Results", "weight": 1.0} -->

We zero-shot evaluate four open-source baselines: UniAD \[hu2023uniad\] and DMAD \[shen2025dmad\], multi-task perception, prediction, and planning models trained with navigation commands on nuScenes; SSR \[li2025ssr\], which plans directly with a self-supervised BEV regulariser; and Epona \[zhang2025epona\], an autoregressive front-view diffusion world model trained on nuPlan without navigation commands. Table˜6 reveals a substantial domain gap, least pronounced for Epona, which is consistent with its larger pretraining corpus. The same ordering holds under the multi-maneuver criterion in Table˜18. Figure˜9 illustrates a qualitative example of end-to-end predictions.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Dynamic-object annotations", "weight": 1.0} -->

The current release does not include 3D bounding boxes, tracks, or instance segmentation for dynamic agents. These annotations will be added in a future release.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Dataset scale", "weight": 1.0} -->

At $5.7\text{\,}\mathrm{h}$ of current recorded data, KITScenes Multimodal is smaller in raw volume than recent large-scale sensor corpora such as nuPlan Sensor (${\approx}120$ h) or Nvidia Physical AI AV (${\approx}1700$ h). However, these datasets target fundamentally different tasks and provide neither the same annotation types nor comparable sensor fidelity. Progress in spatial machine learning is increasingly driven by two complementary regimes: large-scale pre-training, where data volume is central, and curated evaluation or fine-tuning data with benchmark protocols that reflect target deployment behavior. Our dataset primarily supports the latter, offering sensor fidelity, annotation completeness, and benchmark breadth that are difficult to replicate at corpus scale.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Open-loop end-to-end evaluation", "weight": 1.0} -->

While the maps are validated end-to-end through closed-loop driving trials in Autoware \[autoware\] as shown in Appendix˜F, our end-to-end benchmark evaluates open-loop trajectory prediction only. While the released artifacts enable closed-loop evaluation in the Autoware simulator, we leave such experiments to future work.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented KITScenes Multimodal, a European multi-modal driving dataset that pairs a state-of-the-art sensor suite with high-resolution synchronized global-shutter cameras, lidar reaching beyond $400\text{\,}\mathrm{m}$, and 4D imaging radar with the most complete public HD maps of any dataset, covering $62\text{\,}{\mathrm{km}}^{2}$ of area and validated by closed-loop autonomous-driving trials. Across our four benchmarks, online HD map construction, long-range depth estimation, novel view synthesis, and end-to-end driving, current state-of-the-art methods leave systematic capability gaps that prior datasets cannot surface, from complete map prediction at full Lanelet2 fidelity, through long-range depth and geometrically consistent novel views, to map-grounded trajectory evaluation in cluttered European urban scenes. By coupling deployment-grade maps with long-range, high-fidelity sensing, KITScenes Multimodal offers a controlled testbed for the spatial-reasoning capabilities required on the path to L4 autonomy.
