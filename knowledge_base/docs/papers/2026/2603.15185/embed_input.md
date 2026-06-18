<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

What Matters for Scalable and Robust Learning in End-to-End Driving Planners?

Topics include Autonomous driving, End-to-end planning, End-to-end learning, Closed-loop, Robustness.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Examines which architectural and training choices actually improve scalable, robust end-to-end driving planners. The paper is valuable as an empirical correction to open-loop-only design intuitions, focusing on closed-loop behavior and robustness.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

End-to-end autonomous driving has gained significant attention for its potential to learn robust behavior in interactive scenarios and scale with data. Popular architectures often build on separate modules for perception and planning connected through latent representations, such as bird's eye view feature grids, to maintain end-to-end differentiability. This paradigm emerged mostly on open-loop datasets, with evaluation focusing not only on driving performance, but also intermediate perception tasks. Unfortunately, architectural advances that excel in open-loop often fail to translate to scalable learning of robust closed-loop driving. In this paper, we systematically re-examine the impact of common architectural patterns on closed-loop performance: high-resolution perceptual representations, disentangled trajectory representations, and generative planning. Crucially, our analysis evaluates the combined impact of these patterns, revealing both unexpected limitations as well as underexplored synergies. Building on these insights, we introduce BevAD, a novel lightweight and highly scalable end-to-end driving architecture. BevAD achieves 72.7% success rate on the Bench2Drive benchmark and demonstrates strong data-scaling behavior using pure imitation learning.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

(a) High-capacity perceptual representation, e.g., high-resolution BEV

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

End-to-end autonomous driving (E2E-AD) has recently achieved great progress, driven by the possibility to optimize the entire stack in a planning-oriented manner. Compared to classical approaches with rule-based components, this enables human-like behavior in complex scenarios and promises performance gains that scale with data. While E2E-AD exists in various flavors, popular approaches often implement modular but fully-differentiable transformer-based architectures with latent intermediate representations, such as bird's eye view (BEV) feature grids. Popularized on open-loop benchmarks such as NuScenes, these works typically do not evaluate in a closed-loop setting. Unfortunately, approaches optimized for open-loop performance often fail to generalize in closed-loop driving scenarios, resulting in a divergence in the directions of architectural advances between works that solely focus on either setting.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we take a step towards consolidating these advances in E2E-AD with a focus on closed-loop driving. As depicted in Fig. 1 we systematically extend the design space proposed in ParaDrive, by re-examining three architectural patterns: The use of high-resolution perceptual representations as input to the planning module, more common to the open-loop setting, disentanglement of trajectories into lateral- and longitudinal components, mainly used in closed-loop driving the use of generative planners, previously underexplored for end-to-end closed-loop driving. By evaluating these patterns jointly, we find that only one configuration admits robust scaling of performance. In particular, we observe that high-resolution perceptual representations, shown to enable state-of-the-art (SotA) performance in open-loop, can be susceptible to causal confusion, and introduce a spatial bottleneck to mitigate this. Furthermore, we show that disentangled trajectory representations and generative planning via diffusion, previously studied only in isolation, provide complementary benefits in modeling multi-modal behavior, and see the strongest scaling properties when using both in conjunction.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Building on these insights, we develop BevAD. It achieves SotA closed-loop driving performance on the challenging Bench2Drive benchmark based on the CARLA simulator, without any bells and whistles, and using camera sensors only. Additionally, we demonstrate that BevAD strongly benefits from data scaling, with difficult skills emerging as the dataset size increases.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Show that high-resolution perceptual representations can hinder learning robust planning and introduce a spatial bottleneck layer for mitigation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Analyze how a disentangled planning representation and diffusion-based planning provide complementary benefits for closed-loop driving.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Integrate these insights and build BevAD, a lightweight and highly scalable E2E-AD architecture that achieves SotA closed-loop driving on Bench2Drive.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Revisiting Common Architectural Patterns", "weight": 1.0} -->

We briefly summarize common architectural patterns that were previously studied in isolation and occur predominantly either in the open-loop or the closed-loop setting.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Revisiting Common Architectural Patterns", "weight": 1.0} -->

High-Resolution Perceptual Representations are employed to improve performance in perception tasks, but are primarily studied in open-loop. While provides some evidence for benefits in closed-loop driving, leading closed-loop methods in CARLA inherently employ lower-capacity representations due to their reduced sensor configuration. We aim to systematically re-examine the impact of the BEV size on learning precise representations for closed-loop driving.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Revisiting Common Architectural Patterns", "weight": 1.0} -->

Disentangled Planning Representations are employed by the top-three closed-loop methods in CARLA as a measure to reduce the ambiguity of multi-modal futures.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Revisiting Common Architectural Patterns", "weight": 1.0} -->

Generative Planners emerged as a principled measure to model multi-modality in driving, but their study is mainly driven by open-loop methods.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Revisiting Common Architectural Patterns", "weight": 1.0} -->

In the remainder of this section, we first introduce our analysis framework (Sec. 3.1), along with the experiment setup (Sec. 3.2). Subsequently, we analyze the impact of the perceptual representation (Sec. 3.3), the patterns for modeling multi-modal future jointly (Sec. 3.4) and the implications on scaling (Sec. 3.5).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Revisiting Common Architectural Patterns", "weight": 1.0} -->

(b) Proposed Scene Tokenizer and Planning Head

<!-- chunk {"id": "body-0017", "role": "body", "section": "Analysis Framework", "weight": 1.0} -->

Our analysis framework as shown in Fig. 2 is built upon ParaDrive for the following key reasons: ParaDrive provides a systematic, module-level architecture for E2E-AD stacks, offering a well-defined foundation; Its planner operates independently from auxiliary task, facilitating a focused analysis of the perception-planner interface; ParaDrive's design, based on a real-world sensor configuration, has demonstrated strong performance on open-loop nuScenes tasks, unlike CARLA-specific methods. Our framework prioritizes training efficiency to scale beyond nuScenes to larger imitation learning datasets for CARLA. This is achieved through a streamlined pipeline (Fig. 2(a)), optimizing the BEV backbone and removing non-essential auxiliary tasks, while maintaining a realistic sensor setup. Key aspects of the components are stated below, further details are found in the supplementary.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Analysis Framework", "weight": 1.0} -->

BEV Backbone. The BEV backbone processes images of $N_{\text{Cam}} = 6$ cameras to produce BEV features $\mathcal{F}_{\text{Bev}}$ with dimensions $H \times W$, comprising RADIO with low-rank adapter as its image backbone and a BEV encoder based on BEVFormer. Significantly improved runtime is achieved by replacing the recurrent BEV feature generation with cached features streamed from short episode snippets during training. Furthermore, we introduce a novel camera augmentation technique, applying a random transformation ${}_{}^{}{}_{}^{}$ to all camera extrinsics to recover from compounding errors during closed-loop inference.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Analysis Framework", "weight": 1.0} -->

Auxiliary Tasks. We implement a DETR-style object decoder with deformable cross-attention to supervise the BEV features during training. We pruned other auxiliary tasks as used in as they did not demonstrably improve closed-loop performance during initial tests, but introduced significant runtime overhead.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Analysis Framework", "weight": 1.0} -->

Planning Head. We adopt a Transformer decoder architecture as depicted in Fig. 2(b): Self-attention among planning queries $\mathcal{Q}_{\text{Plan}}$ enables mutual alignment, while cross-attention to scene tokens $\mathcal{F}_{\text{Scene}}$ allows extraction of global scene features, following. Subsequently, we employ a coarse-to-fine strategy using an optional deformable attention layer, refining $\mathcal{Q}_{\text{Plan}}$ by sampling local, high-resolution BEV features $\mathcal{F}_{\text{Bev}}$. Inspired by diffusion transformers, each multi-head attention block is enclosed by adaLN-Zero transformations, incorporating conditioning from high-level driving commands, the ego-state, and optionally the diffusion timestep. If the planner is a point estimator, the planning queries $\mathcal{Q}_{\text{Plan}}$ are implemented as learnable embeddings.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Analysis Framework", "weight": 1.0} -->

For diffusion-based planners, $\mathcal{Q}_{\text{Plan}}$ is generated by adding Gaussian noise to the ground truth according to a diffusion schedule such as DDIM and embedding the result into the transformer's input space. By reinterpreting the planning queries as path and velocity tokens instead of trajectory tokens and adjusting supervision accordingly, we can modify the planning representation. This flexible design enables analysis across different formulations without altering the planner's architecture.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Analysis Framework", "weight": 1.0} -->

Controller. Following, we employ two PID controllers to convert planning outputs into steering and acceleration commands. The disentangled planning representation facilitates PID controller design by allowing separate processing of path and speed. To achieve the same for the trajectory representation, we fit a piecewise cubic Hermite polynomial to the temporal waypoints and interpolate at fixed distances, while speed is derived using a second-order difference quotient. This allows consistent PID controller parameters across representations, minimizing the controller's critical impact on closed-loop driving.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Experiment Setup", "weight": 1.0} -->

Data Collection. There are currently two popular data sources for expert demonstrations in CARLA for training imitation learning models: Bench2Drive provides a dataset of expert demonstrations collected by the privileged, RL-based Think2Drive \[33")\] expert along with sensor data and object annotations. The official CARLA leaderboard 2.0 benchmark provides specifications of long routes in CARLA with scenarios alongside, from which a dataset of expert demonstrations can be collected with the privileged, rule-based expert PDM-lite. Simlingo and TF++ split the long routes into shorter segments, each containing one scenario, and uniformly upsample routes with rare scenarios. Due to various known label bugs in the Bench2Drive dataset, we adopt the second approach. We re-collect training data for our six-camera sensor setup using the same route specifications as Simlingo and use these routes for training, unless stated otherwise.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Experiment Setup", "weight": 1.0} -->

Training. We conduct all experiments on 8xA100 80GB GPUs with a total batch size of $128$ in mixed-precision (bfloat16) to balance efficiency, memory usage and stability. AdamW Schedule-free (learning rate: $2^{- 4}$; weight decay: $0.01$) is used for optimization. Our training consists of two stages: A warm-up stage over four epochs to initialize the BEV backbone with perception supervision, followed by a second stage that adds planning supervision. For faster convergence, we freeze the BEV backbone for all second-stage experiments except for studies on data scale.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Experiment Setup", "weight": 1.0} -->

Benchmark and Metrics. We perform closed-loop evaluations on the challenging Bench2Drive benchmark in CARLA. Bench2Drive comprises 220 short test routes, each featuring a single scenario, enabling analysis of specific driving skills. We report the official metrics driving score (DS) and success rate (SR).

<!-- chunk {"id": "body-0026", "role": "body", "section": "High-Resolution Perceptual Representations", "weight": 1.0} -->

Established BEV-based end-to-end architectures connect perception and planning through $H \times W$ high-resolution latent BEV features. We introduce a tokenizer (Fig. 2(b)) that applies masking and patchifying to compress BEV features $\mathcal{F}_{\text{Bev}}$ into scene tokens $\mathcal{F}_{\text{Scene}}$, thereby channeling spatial information through a bottleneck.

<!-- chunk {"id": "body-0027", "role": "body", "section": "High-Resolution Perceptual Representations", "weight": 1.0} -->

Masking. We propose using a key padding mask in the global cross-attention of the planner to exclude BEV cells where planning queries $\mathcal{Q}_{\text{Plan}}$ cannot attend to. Our initial experiments tested various masking strategies, such as removing distant parts to the left and right of the ego vehicle, and sophisticated masks based on the map segmentation outputs. No significant differences were observed, so we use the simplest form, masking out 20% of the left- and right-most BEV cells. Although tailored to CARLA maps, this approach helps to determine if restricting the attention space facilitates learning a robust representation.

<!-- chunk {"id": "body-0028", "role": "body", "section": "High-Resolution Perceptual Representations", "weight": 1.0} -->

Patchifying. Inspired by Vision Transformers, we propose pixel unshuffling for combining patches of $p \times p$ BEV features $\mathcal{F}_{\text{Bev}}$, (pixels) into spatial scene tokens $\mathcal{F}_{\text{Scene}}$, which our planner can globally attend to. We prevent the channel dimension of the scene tokens from growing by $p^{2}$ by projecting the output of pixel unshuffling to a lower-dimensional space, thereby enforcing a bottleneck. We explore $p \in {\{ 1,2,4,5\}}$. This analysis aims to understand how forced compression and sequence length in cross-attention impact learning a robust representation.

<!-- chunk {"id": "body-0029", "role": "body", "section": "High-Resolution Perceptual Representations", "weight": 1.0} -->

Results. We employ a $100 \times 100$ BEV space, consistent with UniAD-tiny, and a disentangled point-estimator planner, aligning with SoTA on Bench2Drive. Tab. 1 presents open- and closed-loop driving metrics for the tokenizer design space. We observe significant improvements in closed-loop driving performance as the scene token count is reduced via masking and patchifying. Specifically, restricting the planner's attention to masked BEV features enhances closed-loop driving, even when the mask is applied solely at test time. Furthermore, summarizing $p \times p$ BEV feature patches into scene tokens reduces the planner's token count by a factor of $p^{2}$, yielding substantial closed-loop performance gains. Despite the reduced BEV resolution, the L1 trajectory error marginally improves for $p \leq 4$. However, this compression strategy collapses for $p \geq 5$, resulting in a significant drop in both closed-loop and open-loop performance.

<!-- chunk {"id": "body-0030", "role": "body", "section": "High-Resolution Perceptual Representations", "weight": 1.0} -->

Discussion. Transformer-based models are known to struggle with identifying relevant information in long (text) sequences, even with modest token counts. We relate this challenge to our setting, where high-resolution BEV inputs create long attention contexts. We hypothesize that the planner overfits to spurious correlations in training data by deriving actions from memorized visual landmarks. Fig. 3 visualizes qualitative examples of planning query mean cross-attention activations. In the absence of masking and patching, it reveals numerous punctual, high activation patterns in distant, often occluded or irrelevant BEV regions, strongly indicating causal confusion. These learned shortcuts are not measurable by open-loop metrics like L1 due to averaging, but lead to catastrophic failures in distinct situations at test time. By reducing the token count through masking and patchifying, our approach mitigates this causal confusion, significantly enhancing closed-loop driving by learning a more robust representation for test time.

<!-- chunk {"id": "body-0031", "role": "body", "section": "High-Resolution Perceptual Representations", "weight": 1.0} -->

Our finding contrasts with prior studies suggesting that higher BEV resolutions enhance downstream tasks such as 3D object detection. This discrepancy stems from a fundamental difference between local detection and global planning tasks. DeformableDETR-style detection heads leverage object locality by decoding queries to specific reference points. While increased BEV resolution enhances localization precision, it does not expand a single query's receptive field. In contrast, planning requires understanding critical scene elements that may not be localized near the immediate trajectory, thus necessitating global cross-attention. In this global context, increasing BEV resolution expands the attention context size, contributing to the observed performance degradation.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Modeling Multi-Modal Behavior", "weight": 1.0} -->

The problem of inherent multi-modality in driving behavior is well-known in research. Leading closed-loop methods in CARLA address this with a disentangled output representation that separates the spatial path from the speed profile instead of entangling them in a trajectory of temporal waypoints. Points on the path are obtained by sampling at fixed distances instead of fixed time intervals, which were shown to be less ambiguous, providing better supervision. Meanwhile, diffusion models can natively address the multi-modality in entangled temporal trajectories with generative modeling. On first glance, both patterns appear to solve a similar problem. To discern the individual contributions and potential synergies of trajectory representation and (non)generative modeling, we systematically evaluate all four combinations. As we observe that the DS and SR tend to obscure the distinct symptoms of driving failures, we additionally introduce static and dynamic infraction rates $\text{IR}_{s}$ and $\text{IR}_{d}$ for this experiment.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Modeling Multi-Modal Behavior", "weight": 1.0} -->

In a nutshell, $\text{IR}_{s}$ and $\text{IR}_{d}$ capture the prevalence of failures due to wrong path planning and inappropriate acceleration respectively; details can be found in the supplementary.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Modeling Multi-Modal Behavior", "weight": 1.0} -->

Results. As shown in Tab. 2 the disentangled representation significantly reduces static infractions, regardless of the modeling approach. Particularly for point-estimators, this reflects strongly in the overall closed-loop scores, matching prior studies. We conclude that the disentangled representation is favorable for learning robust steering. Generative modeling with diffusion reduces dynamic infractions, regardless of trajectory representation. As a result, the entangled diffusion-based variant achieves similar overall SR than the disentangled point-estimator, though their failure modes are quite different. Further, we observe complementary benefits for employing both diffusion-based modeling and disentangled representation, stated with the highest overall SR. The lower driving score stems from -1.6% route completion, since the diffusion model is less willing to make an infraction for the sake of route progress.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Diminishing Returns when Scaling Non-Generative Planners", "weight": 1.0} -->

The promise of scaling performance with data is one of the main advantages of E2E-AD. Since generative planning can capture the full distribution of behavior, we hypothesize that it shows stronger benefits from scaling the dataset size. In the following, we hence examine the scaling behavior of diffusion- compared to point estimator-based planning.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Diminishing Returns when Scaling Non-Generative Planners", "weight": 1.0} -->

Scaling Data. To scale training data beyond current datasets, we build a route generator that exhaustively plans short semantically plausible single scenario routes in all CARLA towns. While being capable of building $> 10^{6}$ unique route-scenario combinations (see supplementary), we only consider 8,000 uniformly sampled scenarios as additional training data in our scaling experiments. For conducting data scaling experiments, we leverage established protocols: We create five training splits from the joint set of Simlingo's and our routes, each approximately doubling in size. These splits are cumulative (each being a subset of the larger ones ), maintaining the same scenario distribution across all splits. We train all models on each data scaling split until convergence.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Diminishing Returns when Scaling Non-Generative Planners", "weight": 1.0} -->

Results. As reported in Fig. 4, both variants improve monotonically in SR as we double the training dataset. In the low data regime, the point estimator slightly outperforms the diffusion-based planner. After an inflection point (about 8000 training scenes), the growth rate decelerates, matching prior studies on closed-loop scaling laws for point estimate planners. On the other hand, diffusion-based planning maintains its linear rate of improvement until our largest data scaling split, and thereby substantially outperforms the point-estimator counterpart. Interestingly, we cannot observe any saturation for the diffusion-based planner, unlike reported for closed-loop tests with point-estimator regressors. This opens up opportunities for further improvements in the presence of larger datasets.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Diminishing Returns when Scaling Non-Generative Planners", "weight": 1.0} -->

Emerging Skills. The scaling gains can also be broken down in terms of multi-ability evaluation protocol from Bench2Drive, where we observe that difficult skills emerge at larger training split sizes. For example, this is the case for the *Give Way* and *Merging* skills as required for the yielding scenario depicted in Fig. 5. Detailed results can be found in the supplementary.

<!-- chunk {"id": "body-0039", "role": "body", "section": "BevAD", "weight": 1.0} -->

Integrating the above insights, BevAD emerges as a lightweight and highly scalable E2E-AD architecture from our analysis framework in Fig. 2. It applies synergies of architectural patterns, previously studied in isolation, for dealing with multi-modality in driving and combats overfitting with effective BEV compression. We compare BevAD to previous state-of-the-art in CARLA, providing a quantitative demonstration of BevAD's results (Sec. 4.1) along with qualitative results (Sec. 4.2) and real-world experiments on NAVSIM (Sec. 4.3).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Comparison to State of the Art", "weight": 1.0} -->

A comprehensive comparison of BevAD to other methods on Bench2Drive with respect to training data, sensor configuration, supervision signals and performance can be found in Tab. 3. For a fair comparison, our model is denoted as BevAD-S when trained solely on Simlingo routes, and BevAD-M when trained with additional routes from our scaling study. We consider UniAD and VAD as baselines since their module-level architecture is most similar to BevAD. We report the overall closed-loop driving score and success rate on the 220 test routes of Bench2Drive. The significant improvements of +34.8 DS and +38.9 SR of BevAD-S compared to UniAD highlight the effectiveness of our tokenization as well as the complementary benefits of disentangled output representation and diffusion-based policy. By uniformly scaling up training scenarios, BevAD-M outperforms all prior methods in terms of DS and SR, as well as the concurrent BridgeDrive in terms of DS. We refer to the supplementary for the more fine-grained multi-ability evaluation and analysis on driving skill evolution.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

In the challenging *YieldToEmergencyVehicle* scenario, BevAD demonstrates the ability to yield to a rapidly approaching emergency vehicle from behind. Fig. 5 illustrates that BevAD acquires this skill after scaling up training data. Prior methods failed in such scenarios, either due to the lack of 360-degree camera perception or insufficient training data. This underscores BevAD's effective utilization of its surrounding view BEV perception and its scalability. Additional qualitative closed-loop demonstrations are provided in the supplementary material.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

Failure Cases. We analyze common failure modes of BevAD-M: Red Light Infractions occur in 19% of unsuccessful closed-loop runs. For example, the driving model runs a red light in the PedestrianCrossing scenario after pedestrians have crossed, suggesting causal confusion. Route Deviations occur when BevAD ignores lane change commands, causing incorrect exits on multi-lane roads. We attribute this to weak conditioning signals from navigation commands, which are often insufficient for timely lane changes. Strengthening conditioning with target points can mitigate this issue by guiding the model towards the correct lane center similar to, though it increases reliance on precise map localization. Miscellaneous Collisions result from delayed reactions in time-critical scenarios or occur in situations that involve strong interaction with other vehicles, such as merging into flows.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Real-world Experiments", "weight": 1.0} -->

We evaluate our method's real-world applicability on the NAVSIM planning benchmark. To match NAVSIM's expected planning representation, we adapt the diffusion planner to predict trajectories with associated yaw angles over a four-second horizon, and train BevAD end-to-end on the navtrain split for eight epochs. We summarize performance on the navtest split in Tab. 4, using the official NAVSIM metrics. BevAD outperforms representative baselines UniAD and ParaDrive by 3.2 and 2.6 PDMS, respectively, primarily due to improvements in drivable area compliance (DAC) and ego-progress (EP). Notably, BevAD achieves this performance with only object detection and planning supervision, in contrast to baselines that also leverage online-mapping and occupancy prediction supervision. BevAD's lightweight design yields a 570 GPU-hour (A100-80GB) training compute budget, 10x less than ParaDrive.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Real-world Experiments", "weight": 1.0} -->

Furthermore, we ablate the tokenizer design on real-world data: As shown in Tab. 4, removing masking degrades overall performance by 0.7 PDMS, while removing patchifying ($p = 1$) results in a 1.0 PDMS degradation. This demonstrates the effective generalization of our masking and tokenizing scheme to a real-world setting.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion and Limitations", "weight": 1.5} -->

We presented BevAD, a lightweight and highly scalable E2E-AD model that achieves SotA closed-loop driving on Bench2Drive. BevAD emerges from our systematic analysis of common architectural patterns, previously studied in isolation. We show that high-resolution BEV features can lead to overfitting, which we mitigate by forcing the planner to learn bottleneck. Additionally, planning with diffusion complements disentangled planning output representations, particularly excelling when scaled with data.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusion and Limitations", "weight": 1.5} -->

We acknowledge several limitations. First, while compressing the BEV along its spatial dimension significantly improved closed-loop driving, our approach may not directly extend to high-speed highway scenarios, which require long-range perception. A principled, context-adaptive BEV masking strategy remains for future work. Second, our analysis of failure cases suggests potential causal confusions. Mitigating these, perhaps via incorporating world knowledge from VLMs or with reinforcement learning, requires further investigation.
