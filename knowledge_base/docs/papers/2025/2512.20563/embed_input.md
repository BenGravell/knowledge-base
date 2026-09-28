<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

LEAD: Minimizing Learner-Expert Asymmetry in End-to-End Driving

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Simulators can generate virtually unlimited driving data, yet imitation learning policies in simulation still struggle to achieve robust closed-loop performance. Motivated by this gap, we empirically study how misalignment between privileged expert demonstrations and sensor-based student observations can limit the effectiveness of imitation learning. More precisely, experts have significantly higher visibility (e.g., ignoring occlusions) and far lower uncertainty (e.g., knowing other vehicles' actions), making them difficult to imitate reliably. Furthermore, navigational intent (i.e., the route to follow) is under-specified in student models at test time via only a single target point. We demonstrate that these asymmetries can measurably limit driving performance in CARLA and offer practical interventions to address them. After careful modifications to narrow the gaps between expert and student, our TransFuser v6 (TFv6) student policy achieves a new state of the art on all major publicly available CARLA closed-loop benchmarks, reaching 95 DS on Bench2Drive and more than doubling prior performances on Longest6~v2 and.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Additionally, by integrating perception supervision from our dataset into a shared sim-to-real pipeline, we show consistent gains on the NAVSIM and Waymo Vision-Based End-to-End driving benchmarks. Our code, data, and models are publicly available at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Closed-loop evaluation is essential in robotics, in particular autonomous driving, because strong open-loop prediction does not necessarily translate into robust closed-loop control. While real-world closed-loop testing remains essential, its cost motivates the widespread use of simulators such as CARLA for benchmarking driving policies. Within this setting, a two-stage imitation learning paradigm, often called Learning by Cheating (LBC), has proven highly effective. First, a privileged expert policy is constructed using ground-truth state information (e.g., the precise map layout), allowing it to plan without perception errors. The second stage then trains a student policy to reproduce the expert's actions from sensory observations (e.g., cameras). A rich body of recent literature supports this methodology.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In initial work following this paradigm, constructing a reliable expert was itself a major challenge, and empirical progress was closely tied to expert quality: early improvements in expert behavior translated directly into better student performance. As a result, expert design focused primarily on maximizing performance, driven by the expectation that stronger experts would yield stronger students. Once expert policies achieved strong benchmark performance, most work treated them as fixed sources of supervision, prioritizing model improvements over further expert redesign. This approach was successful when models were the bottleneck, but the landscape has shifted. With student policies now plateauing well below expert performance, the expert itself deserves renewed attention.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our work studies, in detail, the generalization gap between expert and student policies. We identify and analyze several sources of misalignment between expert and student that systematically hinder effective imitation in CARLA, as illustrated in Fig. 1. This motivates a new expert (and corresponding dataset), LEAD, explicitly designed to reduce Learner--Expert Asymmetry in Driving.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In parallel to expert misalignment, a second limitation arises from how student policies are conditioned on navigation intent. Prior work observes a pronounced *target point bias*, where policies over-emphasize the immediate goal location and under-utilize driving context. This behavior is commonly attributed to weak scene representations. Our work shows that target point bias persists even when scene representations are made stronger. Instead, we attribute it to two additional factors. First, driving intent is often insufficiently specified: a single target point does not provide information to disambiguate multi-step maneuvers such as lane changes, making direct goal pursuit a convenient shortcut. Second, the geometric target point coordinates are frequently injected late within the decoder of the driving policy, preventing meaningful interaction with perception features from the encoder and increasing the target point's influence relative to them. Together, these two factors lead to the most dominant failure modes that negatively impact closed-loop performance of our baseline policy.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Building on these insights, we introduce TransFuser v6 (TFv6), which reduces these asymmetries to achieve substantially improved closed-loop driving. When trained on a large, diverse dataset generated by the LEAD expert, TFv6 achieves a new state of the art on Bench2Drive with 95 DS, an improvement of 8 DS compared to the previously established best performance. This is significant progress given the gap between the best-performing and fifth-best-performing published methods is approximately 2 DS. Finally, we aggregate the LEAD dataset with real-world datasets into a unified training pipeline, where pre-training on LEAD yields consistent improvements on the NAVSIM and Waymo End-to-End Driving benchmarks. In summary, our contributions span: Reducing asymmetries. We systematically analyze and reduce learner--expert asymmetries in CARLA by aligning expert supervision with the student's observable state and strengthening the student's navigation intent, improving the effectiveness of imitation-based driving.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Mitigating target point bias. We show that the target point bias persists with existing mitigation strategies and identify insufficient as well as poorly integrated intent conditioning as its key contributing factors.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

A complete training stack. We release LEAD, a large-scale CARLA dataset and training pipeline enabling state-of-the-art closed-loop driving performance and measurable sim-to-real gains on NAVSIM and Waymo.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Minimizing Learner-Expert Asymmetry", "weight": 1.0} -->

In this section, we study the impact of various learner-expert asymmetries in a controlled manner. Using a fixed, strong baseline, we systematically reduce learner--expert mismatch by aligning the information used for expert driving and navigation with what is available to the student policy. Holding model architecture and dataset scale constant allows us to attribute performance differences to this alignment.

<!-- chunk {"id": "body-0012", "role": "body", "section": "State Alignment", "weight": 1.0} -->

TFv5 is supervised by the privileged rule-based expert PDM-Lite. PDM-Lite computes a dense route using A\* search over the lane graph and refines this trajectory to avoid static obstacles. Potential collisions are forecast using ground-truth 3D bounding boxes and precise dynamic state information, which directly triggers braking behavior. While this design is simple and highly effective, it inherently relies on highly privileged information. As a result, expert actions may depend on non-observable actors (*visibility asymmetry*) or on motion estimates with unrealistically high precision (*uncertainty asymmetry*). While these issues are widely recognized, addressing them in practice remains challenging. To this end, we now provide an overview of how we adapt PDM-Lite to better reflect the information available to the student policy. Further implementation details are provided in supplementary material.

<!-- chunk {"id": "body-0013", "role": "body", "section": "State Alignment", "weight": 1.0} -->

Reducing Visibility Asymmetry: To prevent expert decisions based on unobservable information, we constrain the expert's planning inputs to signals accessible through the student's sensors.

<!-- chunk {"id": "body-0014", "role": "body", "section": "State Alignment", "weight": 1.0} -->

For dynamic actors, we exclude those outside the student's camera view, such as pedestrians behind the vehicle, while accounting for actor extent and environmental conditions including weather and time of day. This avoids expert reactions to unobservable hazards.

<!-- chunk {"id": "body-0015", "role": "body", "section": "State Alignment", "weight": 1.0} -->

We apply similar constraints to traffic infrastructure. The stopping logic for traffic lights only considers lights within the camera frustum. For traffic signs, explicit speed limit information is not provided to the model and signs are only intermittently visible. We therefore cap the expert's target speed to the minimum of the posted limit and the typical flow of nearby vehicles, both of which are inferable from local traffic context.

<!-- chunk {"id": "body-0016", "role": "body", "section": "State Alignment", "weight": 1.0} -->

Reducing Uncertainty Asymmetry: To account for uncertainty in student perception, we adjust the expert's braking behavior.

<!-- chunk {"id": "body-0017", "role": "body", "section": "State Alignment", "weight": 1.0} -->

Beyond reacting to predicted collision courses, the expert now brakes in the presence of nearby observable hazards, reducing reliance on precise velocity or acceleration estimates that the student cannot reliably infer.

<!-- chunk {"id": "body-0018", "role": "body", "section": "State Alignment", "weight": 1.0} -->

We further adapt expert behavior based on expected perception reliability. Under low-visibility conditions such as nighttime or heavy rain, we reduce the expert's driving speed to reflect decreased perceptual confidence.

<!-- chunk {"id": "body-0019", "role": "body", "section": "State Alignment", "weight": 1.0} -->

During unprotected turns at junctions, we enlarge the bounding boxes of oncoming actors for collision checks, encouraging safety decisions that rely on conservative spatial margins rather than precise motion prediction.

<!-- chunk {"id": "body-0020", "role": "body", "section": "State Alignment", "weight": 1.0} -->

Using this state-aligned expert LEAD, we collect data with identical spatial coverage and scale to the original dataset. As shown in Table 1, training TFv5 on LEAD improves the Driving Score on Longest6 v2 by +11 points and on Bench2Drive by +1.37 points, while the expert's own performance remains the same (Table 5).

<!-- chunk {"id": "body-0021", "role": "body", "section": "State Alignment", "weight": 1.0} -->

TFv5 trained with… LEAD dataset (Ours) Table 1: Effect of State Alignment.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Intent Alignment", "weight": 1.0} -->

After improving the quality of driving demonstrations, we observe two failure modes remain particularly prominent: When the active target point is distant or placed in an unusual position relative to the ego vehicle, such as behind it in a roundabout, trajectory prediction breaks down entirely, producing disjoint and unusable planning outputs.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Intent Alignment", "weight": 1.0} -->

When the target lies on an adjacent lane, the policy becomes goal-fixated and steers aggressively toward it, ignoring static and dynamic hazards in the surrounding traffic context. The same behavior can be observed when the target point is inside static obstacles.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Intent Alignment", "weight": 1.0} -->

Notably, these failures occur even under clear weather, open road layouts, and low traffic density, where perception and expert supervision are unambiguous. This points us to limitations in the model rather than the expert, specifically, under-specified intent conditioning and the target point bias. We address these via architectural changes, and call the resulting model TFv6. Following, we remove the Gated-Recurrent-Unit-based (GRU-based) refinement stage after the planning queries attend to BEV tokens and represent target point as an explicit token alongside the BEV tokens. Before embedding, the target point is normalized to $$ using the training dataset statistics. Table 2 summarizes the effects of this change, showing improvements of $+6$ DS on Longest6 v2 and $+2$ DS on Bench2Drive. The improvement is driven by a marked reduction of the first failure mode, in which the planner previously failed to produce a coherent trajectory on several Longest6 v2 routes when target points were distant or unusually positioned. Furthermore, we observe generally that the policy is less sensitive to the exact location of the target point.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Intent Alignment", "weight": 1.0} -->

For the second failure mode, beyond poorly integrated target points, we hypothesize that the navigation signal itself is too sparse. To increase the density of navigation conditioning, we replace single-target conditioning with a compact three-point route representation consisting of the previous, current, and future targets. We further reduce the distance threshold at which the current target point is switched out, causing future targets to become relevant earlier and provide stronger supervision to the policy during training. For example, when the current target point is only 2-3 meters away, it provides insufficient information about the long-term path to be taken, for which the policy can now rely on the future target point. Together, these changes substantially improve closed-loop performance, as shown in Table 3. Implementation details and qualitative visualizations are provided in the supplementary material.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Intent Alignment", "weight": 1.0} -->

TFv6 trained with… With three TPs Table 3: Effect of Multiple Target Points (TPs).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Discussion", "weight": 1.5} -->

Fig. 2 summarizes how state and intent alignment contribute to infraction counts. While infractions in general decrease with each improvement, the weakened target point bias, achieved through intent alignment, leads to an increase in route deviation, since the model no longer aggressively snaps back toward the target points after getting off route.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Discussion", "weight": 1.5} -->

Late Goal Conditioning as a Bottleneck: Although the GRU was originally introduced to model temporal dependencies, its role in modern policy architectures is limited. The planning queries already integrate spatial and temporal context through stacked self- and cross-attention, making the GRU largely redundant. Inserted after a substantially more expressive transformer decoder (six layers at 256 dimensions), the GRU forms a shallow bottleneck with a single recurrent layer and 64 hidden units. Rather than facilitating richer interactions between scene context and the target point, this bottleneck constrains the representation and defaults to reinforcing the influence of the stronger available signal, namely the target point.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Discussion", "weight": 1.5} -->

Furthermore, the GRU conditions only the planned path and steering on the target point, while target speed prediction is handled independently of the target point. This design becomes problematic under distribution shift at deployment. During training, the policy is exposed exclusively to on-route data, where steering and speed remain implicitly consistent under nominal route-following behavior. Once the vehicle deviates from the route, the GRU-induced decoupling leads to errors: steering is strongly biased toward the target point, while speed prediction is no longer calibrated with respect to the resulting steering behavior.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments", "weight": 1.0} -->

Having established in Section 3 with a controlled ablation study that aligned supervision and conditioning significantly improve closed-loop performance, we now train TFv6 on an expanded version of LEAD. This dataset is larger and more diverse in terms of towns, lighting, weather conditions, sensor configurations, and scenario coverage. We evaluate across five benchmarks spanning both simulation and real-world driving. Our main experiments focus on long-horizon closed-loop evaluation in CARLA, where we also analyze sensor configurations, and show that combining cameras with LiDAR and radar yields the best performance. Finally, we show that synthetic pre-training on LEAD consistently improves performance on multiple real-world open-loop benchmarks, indicating that synthetic data can provide transferable benefits beyond simulation.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Closed-Loop Benchmarks", "weight": 1.0} -->

Building on the controlled ablations in Section 3, we now evaluate TFv6 on long-horizon closed-loop benchmarks. In addition to Longest6 v2 and B2D, where the test towns are seen during training, we further consider the challenging validation benchmark, which consists of 20 routes on an unseen town that are on average 12.39 km long, featuring roughly 100 scenarios per route of 38 different types. Unlike the prior two benchmarks, methods are not allowed to train on data collected in that town, therefore testing the ability of methods to generalize to novel environments (akin to "level 5" autonomy). validation is among the most challenging driving benchmarks.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Closed-Loop Benchmarks", "weight": 1.0} -->

Metrics: We adopt the standard CARLA Leaderboard 2.0 metrics from Section 3.1. On long routes, however, the Driving Score (DS) can be counterintuitive: because the Infraction Score (IS) decays exponentially with each violation, agents are sometimes rewarded for stopping early rather than driving further. We therefore report the Normalized Driving Score (NDS), defined as RC $\times$ I, where I is a distance-normalized version of IS. For Bench2Drive, we additionally report Success Rate (SR), the fraction of infraction-free completions. Similar to Section 3, reported results are averaged over three independent random seeds.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Closed-Loop Benchmarks", "weight": 1.0} -->

Training: We train TFv6 using a dataset collected with the LEAD expert. The dataset is larger than the one used in Section 3, containing 73 hours of driving instead of 40 hours. We train TFv6 with 4 L40S GPUs for roughly one week in mixed-precision. Further training and data curation details can be found in the supplementary material.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Closed-Loop Benchmarks", "weight": 1.0} -->

Radar Features: Radar is a common sensor modality in autonomous driving but rarely included in current CARLA benchmarks. To further reduce the learner-expert asymmetry, LEAD provides the student policy with four radar units (each with 75 detections per frame). As is common in industrial-grade radars, we pre-process the raw radar detections with a light-weight learned module to provide meaningful object-level features for the downstream policy. The pre-processing details are provided in the supplementary material. As shown in Fig. 3, these object-level radar features bypass the sensor fusion encoder and are input directly into the planning decoder as additional context tokens alongside dense BEV and status information.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Closed-Loop Benchmarks", "weight": 1.0} -->

Baselines: In addition to TFv5 (Section 3.1), we include several competitive baselines in our evaluation. SimLingo is a recent vision--language--action model that won the CARLA Leaderboard Challenge 2024, which also builds on PDM-Lite. HiP-AD is a camera-only end-to-end method and the current published state of the art on B2D. Note that HiP-AD was trained on a different dataset, which is optimized for B2D. Finally, UniAD is a widely used end-to-end approach that employs sequential auxiliary tasks for perception and planning.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Closed-Loop Benchmarks", "weight": 1.0} -->

Table 4 shows the results on the CARLA benchmark. Note that we use the best version of our model here, including the radar and LiDAR input modalities, and a RegNet backbone (with detailed ablations provided later in Table 5). To highlight the impact of generalization, we also evaluate TFv6 trained with data from ( Train), but shade the results in gray to make it clear that these are only for analysis.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Closed-Loop Benchmarks", "weight": 1.0} -->

TFv6 outperforms TFv5 in terms of both DS and NDS, and in both the 'Val' and 'Train' settings, by large margins. Interestingly, there is still a significant generalization gap, where TFv6 achieves 14.65 NDS on Train which drops to 4.04 NDS on Validation. This emphasizes the importance of validation benchmarks where methods do not train on any data collected in the validation town. Qualitatively, TFv6 drives more safely than TFv5 as indicated by its higher IS and I metrics.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Closed-Loop Benchmarks", "weight": 1.0} -->

‘ Val’ – withheld during training ‘ Train’ – Trained on all towns Table 4: Benchmarking on CARLA. Results are averaged over three trained models with different training seeds. *Results included for completeness, though this setting is not the recommended default for this benchmark.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Closed-Loop Benchmarks", "weight": 1.0} -->

Bench2Drive Results: In Table 5, we see that scaling the data, backbone, and sensor modalities brings TFv6 within 2 DS of LEAD on B2D, but a 10-point SR gap remains. This discrepancy reflects how DS treats short routes: an infraction near the end has little impact when most progress is already secured. SR, being all-or-nothing, captures errors that DS discounts. This gap indicates the policy is less robust than DS alone suggests.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Closed-Loop Benchmarks", "weight": 1.0} -->

Longest6 v2 Results: On Longest6 v2, the improvement over TFv5 and SimLingo, both winners of CARLA Challenge 2024, is even more pronounced, with gains of +39 DS and +21 RC. While HiP-AD performs competitively on short-route benchmarks, its substantially lower performance on Longest6 v2 illustrates the challenges of long-horizon evaluation. This highlights the importance of evaluating driving policies on extended routes, where the likelihood of encountering rare and challenging scenarios increases with route length, exposing weaknesses that short-route benchmarks may miss. CARLA is currently the only widely used simulator that supports long-form evaluation. Most recent benchmarks and simulation frameworks are limited to short-form driving due to log-replay or reconstruction-based designs that inherently prevent long-horizon testing. Generative approaches may offer a path forward in addressing this limitation.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Closed-Loop Benchmarks", "weight": 1.0} -->

Ablation: Table 5 also shows several ablations on different sensor setups with TFv6. We find that using a wide front camera-setup with 140° FOV with a combination of LiDAR and Radar sensors yields the best results. Additionally, we show that the RegNetY-032 backbone provides a notable performance improvement compared to the smaller ResNet-34 backbone, consistent with the findings of. Finally, despite not being optimized for driving performance, LEAD matches the performance of PDM-Lite on Bench2Drive and Longest6 v2, indicating that improved learner--expert alignment does not require sacrificing expert competence.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Real-World Data Benchmarks", "weight": 1.0} -->

To complement our closed-loop CARLA evaluation, we further assess transfer to multiple open-loop real-world benchmarks for end-to-end driving.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Real-World Data Benchmarks", "weight": 1.0} -->

NAVSIM v1 evaluates 4-second trajectory rollout using multi-view camera inputs, historical states, and discrete commands over a 1.5-second history. Performance is measured using the Predictive Driver Model Score (PDMS), which aggregates collision avoidance, progress, time-to-collision, driving-area compliance and comfort.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Real-World Data Benchmarks", "weight": 1.0} -->

NAVSIM v2 extends v1 with a two-stage pseudo-simulation evaluation pipeline designed to better approximate closed-loop behavior. In the first stage, trajectories are evaluated from real-world observations using an extended version of PDMS (EPDMS), incorporating additional rule-based and sub-metrics. The second stage evaluates the same planner on pre-rendered synthetic observations generated via 3D Gaussian Splatting. Stage 2 scores are aggregated using a proximity-based weighting scheme that prioritizes synthetic start states close to the planner's Stage 1 predicted endpoint, yielding a final score that reflects robustness to small deviations and error recovery.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Real-World Data Benchmarks", "weight": 1.0} -->

WOD-E2E consists of driving scenes that over-sample rare, safety-critical events ($<0.03\%$ of daily driving). It evaluates 5-second predicted trajectories using the Rater Feedback Score (RFS), a human-annotated metric designed to capture multi-modal, long-tail driving behavior by assigning full expert credit within predefined trust regions and exponentially decaying the score otherwise.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Real-World Data Benchmarks", "weight": 1.0} -->

Training: We collect CARLA data with the camera parameters of target benchmarks, specifically sampled to emphasize dense agent interactions and matching lighting conditions. We only use the perception labels from the synthetic CARLA data to avoid the driving-style mismatch between human data collectors and LEAD. For the NAVSIM benchmarks, we use the full navtrain split and a subset of 100k frames from CARLA for training. We train on mixed data in the first 30 epochs, which smoothly excludes the synthetic data, followed by 90 epochs exclusively training on navtrain. For WOD-E2E, we subsample 300k frames uniformly for each epoch. Here, we pre-train for 30 epochs exclusively on CARLA data, followed by 30 epochs of fine-tuning on the WOD-E2E training split. We provide further information about hyper-parameters and data filtering in our supplementary material.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Real-World Data Benchmarks", "weight": 1.0} -->

Since LiDAR and radar data are not available in all the benchmarks, we drop these modalities and replace the LiDAR with a positional encoding, as done in Latent TransFuser (LTF). We call the resulting method LTFv6 to indicate that this version matches the TFv6 architecture.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Real-World Data Benchmarks", "weight": 1.0} -->

As shown in Table 6, while we achieve modest improvements in absolute terms, they are consistent across benchmarks and training setups. On NAVSIM, LTFv6 improves in the ego progress, drivable area compliance, and traffic light compliance sub-metrics with minor trade-offs in comfort. Our proposed joint pre-training further increases the LTFv6 score across all benchmarks, demonstrating the value of synthetic data despite the presence of distribution shifts. Note that ego status can be interpreted as a lower bound while the expert driver upper bounds differ across benchmarks: NAVSIM v1 and WOD-E2E report human driving performance, whereas NAVSIM v2 uses a privileged planner as the upper bound. Further comparisons are provided in the supplementary material.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We study how misalignment between privileged experts and student policies affects closed-loop driving. By reducing visibility, uncertainty, and intent asymmetries, we introduce LEAD, a student-centric expert and dataset designed to produce more transferable supervision. This alignment yields substantial closed-loop performance gains even without architectural changes, underscoring expert design as a practical lever in simulation-based imitation learning.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Beyond supervision, our experiments show that policy behavior is further constrained by how navigation intent is specified and integrated. Under-specified and late goal-point conditioning amplifies target point bias and promotes shortcut learning, limiting closed-loop robustness in CARLA. Restructuring intent conditioning to be denser and injected earlier enables a more balanced interaction between scene understanding and goal following, leading to more stable behavior over long horizons.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Combining aligned supervision with improved intent conditioning, our new model TFv6 achieves state-of-the-art performance across both short- and long-horizon CARLA benchmarks, with particularly strong gains on challenging long-horizon evaluations where errors accumulate over time. We also provide preliminary evidence of the benefits of co-training on data from simulation and the real world for benchmarks such as NAVSIM and Waymo. Together, these results suggest that continued progress in simulation-based end-to-end driving will benefit from treating expert design and goal specification as integral, co-evolving components of the learning system. As end-to-end driving performance in simulation improves, progress increasingly depends on factors beyond model capacity and data scale.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Limitations", "weight": 1.5} -->

We conclude by discussing several limitations of our study and directions for future work.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Limitations", "weight": 1.5} -->

Remaining Gap to Expert: Despite narrowing the learner--expert gap, a meaningful difference remains (Table 5). We attribute this largely to inherent limitations of behavior cloning, such as compounding errors and the inability to recover from off-route deviations. Closed-loop training via DAgger or reinforcement learning is a promising direction to further close this gap.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Limitations", "weight": 1.5} -->

Sim-to-Real Transfer: Our work investigates perception co-training but does not address planning co-training, where policy behaviors are trained by combining supervision from human driving trajectories and LEAD. Moreover, sim-to-real evaluation is currently limited to open-loop and pseudo-closed-loop benchmarks; demonstrating closed-loop real-world benefits remains future work.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Limitations", "weight": 1.5} -->

Expert Design Scope: Our study is restricted to a rule-based expert in simulation, and the proposed alignment requires domain-specific tuning. Whether similar principles apply to learned experts, human demonstrations, or real-world driving remains open.
