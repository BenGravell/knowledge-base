<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Pseudo-Simulation for Autonomous Driving

Topics include Autonomous driving, Vehicles, Safety, Causal inference, Datasets, Benchmarks.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Existing evaluation paradigms for Autonomous Vehicles (AVs) face critical limitations. Real-world evaluation is often challenging due to safety concerns and a lack of reproducibility, whereas closed-loop simulation can face insufficient realism or high computational costs. Open-loop evaluation, while being efficient and data-driven, relies on metrics that generally overlook compounding errors. In this paper, we propose pseudo-simulation, a novel paradigm that addresses these limitations. Pseudo-simulation operates on real datasets, similar to open-loop evaluation, but augments them with synthetic observations generated prior to evaluation using 3D Gaussian Splatting. Our key idea is to approximate potential future states the AV might encounter by generating a diverse set of observations that vary in position, heading, and speed. Our method then assigns a higher importance to synthetic observations that best match the AV's likely behavior using a novel proximity-based weighting scheme. This enables evaluating error recovery and the mitigation of causal confusion, as in closed-loop benchmarks, without requiring sequential interactive simulation. We show that pseudo-simulation is better correlated with closed-loop simulations (R^ = 0.8) than the best existing open-loop approach (R^ = 0.7).

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We also establish a public leaderboard for the community to benchmark new methodologies with pseudo-simulation. Our code is available at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reliable evaluation is essential for developing decision-making systems. In the context of autonomous vehicles (AVs), this means assessing the system's ability to navigate complex traffic scenarios efficiently, comfortably, and safely. Existing evaluation strategies typically fall into two categories: closed-loop and open-loop evaluation.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Closed-loop evaluation assesses model performance by placing it in an interactive environment. The AV must safely navigate traffic while making progress toward a designated goal. Although real-world closed-loop deployment offers reliable feedback, it is costly, risky, and not reproducible, making it insufficient on its own for benchmarking at the scale needed to demonstrate robustness. As a more reproducible alternative, closed-loop evaluation is often conducted in simulation. Simulators enable rapid iteration and controlled scenario generation, and provide structured metrics for downstream performance analysis, such as collision or route completion rates.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, accurate simulation remains a significant challenge, particularly for vision-based end-to-end AV systems. Real-world driving is visually complex and behaviorally diverse, making it difficult to replicate in simulation. Most existing platforms are manually constructed by 3D artists and engineers. This limits their realism and the diversity across scenes. Moreover, simulation-based evaluation is a computationally intensive and inherently sequential process. It often relies on large amounts of correlated evaluation frame sequences due to the high frequency of simulation required to ensure fidelity (usually 10Hz or higher).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Open-loop evaluation, on the other hand, measures planning performance by comparing predicted trajectories to expert demonstrations in pre-recorded datasets. Each observation for evaluation includes sensor inputs, a goal location, and the future trajectory executed by a human expert driver. The AV predicts a fixed-horizon trajectory conditioned on the inputs, which is then scored against the expert using either displacement errors or metrics derived from ground-truth (GT) environment annotations, such as lane compliance or estimated collisions. This approach operates entirely on real sensor data and avoids the complexities of interactive simulation, making it scalable and straightforward to apply over large datasets. However, it evaluates behavior only under expert-aligned conditions and does not account for distribution shifts. In deployment, the AV deviates from the demonstrated path, and open-loop protocols do not test its ability to recover from such drift.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address the limitations of existing evaluation protocols, we introduce pseudo-simulation. This new paradigm aims to combine the scalability of open-loop evaluation with a comprehensive assessment traditionally restricted to interactive closed-loop testing. As shown in Fig. 1, our approach evaluates the AV's performance in two stages. Stage 1 uses the originally recorded real-world observations. Stage 2 uses synthetic observations generated based on these original frames. Crucially, these synthetic observations are generated before the evaluation process begins, enabling evaluation in a non-interactive manner. To generate Stage 2 observations, we adapt (to our data) a state-of-the-art driving scene reconstruction and rendering algorithm based on 3D Gaussian Splatting.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate the output trajectories predicted by the AV, considering its performance on both the initial real-world observations (from Stage 1) and the generated synthetic observations (used in Stage 2). Our key idea lies in how we assess performance in Stage 2: we weight the importance of each synthetic observation based on its proximity to the endpoint of the trajectory that the AV initially predicted in Stage 1 (Fig. 1 bottom-right). This weighting strategy allows the evaluation to better reflect the AV's robustness and ability to recover from potential errors when facing conditions similar to what it may encounter in a closed-loop simulation. Our approach also inherently assigns lower weights to synthetic observations that significantly deviate from the initially predicted endpoint, thereby preventing undue penalties for failures in improbable or irrelevant future states.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, pseudo-simulation combines real and pre-rendered synthetic data, enabling scalable, parallel evaluation.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that pseudo-simulation achieves strong correlation with closed-loop results for a set of 83 diverse planners nuPlan, while being substantially more efficient (6$\times$ less environment interactions). To enable standardized benchmarking, we release NAVSIM v2, a framework for benchmarking autonomous driving built upon our proposed evaluation methodology. We find that it reveals previously unknown failure modes in popular AV algorithms, thus establishing it as a challenging new testbed for future research. We hope that pseudo-simulation can accelerate AV development through more efficient experimentation cycles and ensuring that future models prioritize closed-loop robustness.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Pseudo-Simulation", "weight": 1.0} -->

We consider a planning task where evaluation proceeds in two stages (Fig. 1). In both stages, an AV (also called planner/ego agent) generates a 4-second trajectory based on sensor inputs and a driving command. The inputs include multi-view camera images and ego status features such as the velocity and motion history. The driving command specifies the intended maneuver in case of ambiguity, e.g., at intersections, and is provided as a discrete label: left, straight, or right. The ego agent outputs a trajectory (i.e., a sequence of desired future waypoints) in its local coordinate frame.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Stage 1: Initial Observations", "weight": 1.0} -->

In Stage 1, we infer the ego agent's motion based on an initial observation from the test dataset. We then simulate a simplified Bird's Eye View (BEV) representation of the scene forward for a fixed time horizon, obtaining a score as well as an endpoint to be used later in Stage 2.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Stage 1: Initial Observations", "weight": 1.0} -->

BEV Simulation. The 4-second trajectory predicted by the agent is executed using a kinematic bicycle model and an LQR controller at 10Hz. The trajectory is committed for the entire simulation horizon, and no closed-loop feedback is provided to the agent during this time. Unlike related prior work, which uses non-reactive traffic to simplify implementation (i.e., neighboring vehicles follow their recorded trajectories without reacting to the ego agent), we improve the simulation realism with reactive traffic. Background vehicles (represented as oriented bounding boxes) respond to the ego agent using a rule-based planner called the Intelligent Driver Model (IDM). Pedestrians, static obstacles, and other non-vehicle actors follow their recorded trajectories without reacting to the ego agent.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Stage 1: Initial Observations", "weight": 1.0} -->

Extended PDM Score. Our metric, the Extended Predictive Driver Model Score (EPDMS), builds on the PDMS introduced in prior work. Besides minor modifications (detailed in the supplementary material), the design of the metric is largely consistent.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Stage 1: Initial Observations", "weight": 1.0} -->

Here, $\mathcal{M}_{\text{pen}} = {\{\text{NC},\text{DAC},\text{DDC},\text{TLC}\}}$ and $\mathcal{M}_{\text{avg}} = {\{\text{TTC},\text{EP},\text{HC},\text{LK},\text{EC}\}}$ (Table 1). Unlike prior work, to prevent penalizing contextually justified maneuvers, we introduce a novel filtering mechanism ($\text{filter}_{m}$) for the EPDMS. If a rule violation is also committed by the human expert driver in the same scene, the penalty is ignored. This avoids penalizing infractions due to label noise or valid behaviors, such as briefly entering the opposite lane to bypass a static obstacle.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Stage 2: Synthetic Observations", "weight": 1.0} -->

In Stage 2, the agent's behavior is inferred on pre-generated synthetic observations. The scoring pipeline from Stage 1 is repeated for each of these synthetic observations. Stage 2 scores correspond to a range of plausible futures. We propose to weight their contributions towards a final combined score based on the proximity of Stage 2 start points to the Stage 1 endpoint. This prioritizes futures that are more likely. We show some examples of such generated scenes in Fig. 2. In the following, we provide details regarding the scenario pre-generation, scoring, and score aggregation processes. Note that we choose to create synthetic observations after unrolling for 4 seconds, instead of directly at the Stage 1 start point, since this allows background traffic to react to the updated ego state, and it provides a physically plausible history trajectory, which is a required planner input.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Stage 2: Synthetic Observations", "weight": 1.0} -->

Start Point Sampling. As a data pre-processing step prior to the evaluation of any specific planner, we generate Stage 2 synthetic observations that approximate the range of possible rollout endpoints for Stage 1 observations in the dataset. Each Stage 2 observation must have a valid start point and heading, with an associated motion history, and multi-view camera image inputs for a planner.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Stage 2: Synthetic Observations", "weight": 1.0} -->

We sample start points around the expert driver's observed endpoint after 4 seconds in the scene. Importantly, this sampling does not depend on the Stage 1 endpoint produced by a planner, but only the expert driving trajectories from the original dataset, available prior to evaluation. We define a sampling region around this expert endpoint: laterally, viewpoints are sampled every 0.5 meters up to 2.0 meters on each side; longitudinally, viewpoints are sampled every 5.0 meters. The longitudinal sampling spans the physically plausible range from the minimum stopping distance to the maximum reachable distance (assuming accelerations of $\pm$`<!-- -->`{=html}4.0 m/s^2^ for 4 seconds). This naturally produces more potential states for high-speed scenarios (up to 20 in practice) compared to low-speed ones.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Stage 2: Synthetic Observations", "weight": 1.0} -->

Heading and History Generation. For each sampled start point, we generate a plausible heading and motion history by matching it to the nearest trajectory in a human driving dataset. This matching process includes filtering: we discard candidate trajectories if they differ in velocity by more than 1.0 m/s, acceleration by more than 1.0 m/s^2^, or heading by more than 20 degrees relative to the expert. We then apply rejection sampling to remove any remaining start points that violate the multiplicative EPDMS constraints (NC, DAC, DDC and TLC). Finally, we discard scenes from the neural reconstruction pipeline if fewer than five valid synthetic observations remain after filtering.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Stage 2: Synthetic Observations", "weight": 1.0} -->

Neural Reconstruction and Rendering. We employ a state-of-the-art dynamic scene reconstruction approach to achieve high-fidelity neural rendering. Specifically, we use a modified version of Multi-Traversal Gaussian Splatting (MTGS). As in MTGS, we model scene dynamics with a scene graph. However, unlike MTGS, which uses multiple nearby driving traversals for jointly optimizing a 3D scene representation, we use only a single traversal. This significantly expands the pool usable data, as only a subset of our dataset includes multiple co-located traversals. To reduce localization noise, we calculate accurate initial camera pose estimates via LiDAR registration and bundle adjustment, followed by camera pose optimization during the MTGS training process. Before reconstruction, we filter out scenes affected by significant sensor failures (water droplets or flares). After reconstruction, we apply a semi-automatic filtering step to discard reconstructed scenes of low visual quality (details in supplementary material).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Stage 2: Synthetic Observations", "weight": 1.0} -->

$\mathcal{A}_{\text{2}}$, in turn, aggregates $\{ s_{2}^{i}\}$ based on their initial positions $\{ x^{i}\}$, which denote the start points of the $i$-th Stage 2 scenario. $\hat{x}$ is the ego agent's endpoint reached at the end of the Stage 1 simulation. In our experiments, we conduct an empirical study on different aggregation functions.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Results", "weight": 1.0} -->

In this section, we study three key questions to examine our proposed idea of pseudo-simulation.

<!-- chunk {"id": "body-0024", "role": "body", "section": "How well-aligned is pseudo-simulation with closed-loop evaluation?", "weight": 1.0} -->

Benchmark. To evaluate how well pseudo-simulation aligns with closed-loop simulation, we conduct a correlation analysis with the nuPlan simulator. nuPlan supports fully reactive rollouts for privileged planners with access to ground-truth perception and HD maps. We include a total of 83 planners, comprising both rule-based and learned models, to represent a wide range of behaviors and performance levels. For rule-based methods, we use 10 constant kinematics baselines, 15 IDM planners, and 15 PDM-Closed variants. For learned approaches, we evaluate 22 PlanCNN models with varying input modalities and 24 Urban Driver models differing in architecture and training configurations. For these experiments, we use a reduced version of EPDMS, excluding the TLC, LK, and EC metrics, because nuPlan does not support these for closed-loop evaluation.

<!-- chunk {"id": "body-0025", "role": "body", "section": "How well-aligned is pseudo-simulation with closed-loop evaluation?", "weight": 1.0} -->

We measure the alignment between EPDMS and nuPlan's closed-loop score (CLS) using Pearson's linear ($r$) and Spearman's rank ($\rho$) correlation coefficients, as well as the coefficient of determination ($R^{2}$). Since $R^{2}$ is calculated by fitting a linear model between EPDMS and CLS, it is equivalent to the square of Pearson's correlation coefficient here ($R^{2} = r^{2}$). This assumes that an ideal pseudo-simulation metric should show a linear relationship with closed-loop scores, requiring no adjustments for scale or bias. We evaluate each planner on a filtered subset of nuPlan, described in detail in the supplementary material, to collect both closed-loop and pseudo-simulation scores. This subset includes 244 initial observations (Stage 1) and 4164 synthetic observations (Stage 2).

<!-- chunk {"id": "body-0026", "role": "body", "section": "How well-aligned is pseudo-simulation with closed-loop evaluation?", "weight": 1.0} -->

Results. First, we create a scatter plot comparing the 8-second closed-loop scores from the nuPlan simulator against the results of our 2$\times$`<!-- -->`{=html}4 second pseudo-simulation, which aims to approximate these closed-loop scores. As shown in Fig. 3, pseudo-simulation exhibits strong correlation with closed-loop results across a broad range of planners, particularly among learned planners. In contrast, prior open-loop evaluation metrics such as average displacement error and nuPlan's open-loop score show nearly no correlation to closed-loop evaluation, consistent with the findings of.

<!-- chunk {"id": "body-0027", "role": "body", "section": "How well-aligned is pseudo-simulation with closed-loop evaluation?", "weight": 1.0} -->

In Fig. 4 (a), we compare single-stage open-loop simulation (at 4 and 8 seconds) to our two-stage pseudo-simulation variant. The two-stage setup achieves significantly higher alignment, reaching a Pearson correlation of $r = 0.89$ (corresponding to $R^{2} = 0.8$), compared to $r = 0.83$ ($R^{2} = 0.7$) for the single-stage baselines. Furthermore, compared to standard reactive closed-loop evaluation, our pseudo-simulation method exposes a wider range of potential failures. This typically results in lower average EPDMS values compared to CLS values. By injecting synthetic deviations, pseudo-simulation effectively reveals edge cases that might not be encountered during standard testing.

<!-- chunk {"id": "body-0028", "role": "body", "section": "How well-aligned is pseudo-simulation with closed-loop evaluation?", "weight": 1.0} -->

Within Stage 2, we assess the impact of the weighting used to combine scores across synthetic viewpoints. Fig. 4 (b) shows the correlation with closed-loop scores for different kernel variances. We observe that smaller variances lead to improved results. $\sigma^{2} = 0.05$ and our default configuration of $\sigma^{2} = 0.1$ give the highest correlations. In additional experiments (included in the supplementary material), we find that other approaches, such as simple averaging, $k$-nearest neighbors ($k$-NN), and hybrid $k$-NN/Gaussian weighting are less effective than our default configuration.

<!-- chunk {"id": "body-0029", "role": "body", "section": "How well-aligned is pseudo-simulation with closed-loop evaluation?", "weight": 1.0} -->

To combine metrics across stages, we compare multiplicative aggregation, aggregation by the arithmetic mean, and a hybrid strategy where penalty metrics (e.g., collision and drivable area compliance) are multiplied while the remaining terms are averaged. Fig. 4 (c) summarizes the correlation of each strategy with closed-loop scores. Multiplicative aggregation shows both higher linear and rank correlation than the other approaches. This outcome is likely because most subscores are binary (i.e., 0 or 1). Consequently, multiplication appears to be a more suitable method for estimating the overall score for an 8-second interval based on two 4-second segments.

<!-- chunk {"id": "body-0030", "role": "body", "section": "How well-aligned is pseudo-simulation with closed-loop evaluation?", "weight": 1.0} -->

Finally, we examine the effect of limiting the number of synthetic views in Stage 2. Fig. 4 (d) reports correlation values when using 100%, 50%, and 25% of our available synthetic viewpoints. At 100% density, each scenario contains 12 synthetic observations on average in Stage 2 for each real observation in Stage 1, resulting in 13 planner inferences per scenario. In comparison, closed-loop simulation in nuPlan requires 80 planner inferences per scenario, corresponding to an 8-second rollout at 10Hz. This is 6$\times$ higher than pseudo-simulation. While subsampling reduces the number of synthetic views, the correlation to closed-loop scores remains strong. Even when using only 25% density, i.e., approximately three Stage 2 observations per scene, the correlation remains above 0.85. This indicates that pseudo-simulation maintains reliability even with reduced observation coverage.

<!-- chunk {"id": "body-0031", "role": "body", "section": "What new challenges and insights does our leaderboard provide?", "weight": 1.0} -->

Benchmark. Our public NAVSIM v2 leaderboard^11^1 features challenging driving scenarios (e.g. unprotected turns and dense traffic, see Fig. 2). It uses a subset of nuPlan that we refer to as navhard, involving 450 Stage 1 and 5462 Stage 2 observations. The goal of the leaderboard is to ensure standardized evaluation, as subtle differences (e.g., enabling/disabling the human-based filtering mechanism, or using a newer numpy version) can have an effect on the computed metrics. Therefore, we discourage the use of self-reported and unofficial "NAVSIM v2" benchmark splits, such as reporting the EPDMS on the NAVSIM v1 navtest dataset without conducting two-stage pseudo-simulation. Instead, submission to our leaderboard can ensure both consistency and visibility of submissions.

<!-- chunk {"id": "body-0032", "role": "body", "section": "What new challenges and insights does our leaderboard provide?", "weight": 1.0} -->

For our analysis, we select five baseline planners with varying input modalities, as well as six community-contributed submissions: LTFv6, RAP, ZTRS, GuideFlow, SimScale, and DrivoR. Our baselines include the Constant Velocity (CV) and Ego-history MLP, Latent TransFuser (LTF), the most established baseline for image-only planning for nuPlan, and PDM-Closed (PDM-C), the best privileged planner on nuPlan. To tackle the complex scene types and visual perturbations of navhard, we propose a new simple and robust baseline architecture called NavFormer^22^2 This model employs a BEVFormer encoder to process surround-view camera inputs, in contrast to LTF which only encodes forward-facing camera data. Following PARA-Drive, object tracking and map segmentation decoders provide auxiliary perception supervision. Finally, NavFormer uses a Hydra-MDP decoder head for planning.

<!-- chunk {"id": "body-0033", "role": "body", "section": "What new challenges and insights does our leaderboard provide?", "weight": 1.0} -->

Results. Table 2 presents the detailed subscores for each planner, broken down by Stage 1 (original observations) and Stage 2 (synthetic observations). In terms of overall performance, PDM-Closed achieves the highest EPDMS of 56.6, closely followed by recent scalable architectures like DrivoR. Comparing performance across stages, we observe a general drop in subscores from Stage 1 to Stage 2 for all methods, suggesting their sensitivity to the distribution shifts introduced in Stage 2. Notably, while PDM-Closed excels in most metrics, it exhibits lower performance in comfort metrics such as HC and EC. Our evaluation on navhard reveals this specific failure mode of PDM-Closed, highlighting a trade-off that was overlooked in prior benchmarks.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Does the proposed neural rendering yield sufficient visual fidelity?", "weight": 1.0} -->

Benchmark. To assess the fidelity of our synthetic observations, we evaluate the impact of our neural rendering on the downstream perception and planning performance of a pre-trained model using the navhard dataset. Specifically, we employ the LTF model from Table 2. Although primarily an end-to-end planner, LTF outputs intermediate Bird's Eye View (BEV) segmentations and, crucially, is trained only on real-world data. This allows us to measure the domain gap introduced by our rendering: we evaluate LTF's performance on synthetic data and compare it to its performance on real data. We use mean Intersection over Union (mIoU) over the drivable area, walkway, and vehicle classes output by LTF to evaluate BEV perception, and the EPDMS metric to evaluate planning.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Does the proposed neural rendering yield sufficient visual fidelity?", "weight": 1.0} -->

Results. We present our findings in Table 3(a) ‣ Table 3 ‣ 4.3 Does the proposed neural rendering yield sufficient visual fidelity? ‣ 4 Results ‣ Pseudo-Simulation for Autonomous Driving"). First, we evaluate perception performance using the LTF model. Comparing Stage 1 to Stage 2 views, we observe a drop in mIoU from 46.0 to 37.6. Despite this degradation in segmentation quality, planning performance remains largely stable, with EPDMS decreasing only slightly from 62.3 to 61.0. While mIoU captures semantic segmentation fidelity, it does not directly reflect planner-relevant errors. For our data, the observed reduction in mIoU does not appear to impair semantic cues needed for planning. This suggests that our synthetic observations preserve the most critical information.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Does the proposed neural rendering yield sufficient visual fidelity?", "weight": 1.0} -->

Next, we evaluate performance under perturbed synthetic Stage 2 inputs. Here, mIoU drops marginally from 37.6 to 36.9, while EPDMS declines substantially to 44.2. This larger drop is consistent with trends observed previously (Section 4.2), where non-privileged planners showed greater sensitivity to deviations from expert trajectories. The small change in mIoU between the synthetic settings of Stage 1 and Stage 2, compared to the greater drop in EPDMS, suggests that the observed planning degradation is primarily driven by the planner's sensitivity to the distribution shift, rather than by perception inaccuracies stemming from rendering artifacts.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Does the proposed neural rendering yield sufficient visual fidelity?", "weight": 1.0} -->

(a) Synthetic data quality for downstream tasks.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Does the proposed neural rendering yield sufficient visual fidelity?", "weight": 1.0} -->

Ablation Study. Additionally, we evaluate novel view synthesis fidelity using the LPIPS metric on 8 navhard scenes, where lower scores indicate higher perceptual similarity. Here, the training and test viewpoints were sampled at alternating 10Hz intervals from the expert trajectory to ensure disjoint inputs and outputs for evaluation. As shown in Table 3(b) ‣ Table 3 ‣ 4.3 Does the proposed neural rendering yield sufficient visual fidelity? ‣ 4 Results ‣ Pseudo-Simulation for Autonomous Driving"), the baseline Street Gaussians method obtains an LPIPS of 0.354. Our MTGS-based variant without optimizations improves this score to 0.322, while our full method incorporating LiDAR registration, bundle adjustment, and pose optimization achieves the best LPIPS of 0.253. Combining these results with the perception and planning evaluations in Table 3(a) ‣ Table 3 ‣ 4.3 Does the proposed neural rendering yield sufficient visual fidelity? ‣ 4 Results ‣ Pseudo-Simulation for Autonomous Driving"), we believe our neural rendering pipeline provides sufficient visual fidelity to approximate planning evaluation as in closed-loop settings.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduce pseudo-simulation, a new evaluation paradigm which demonstrates a high correlation to computationally expensive closed-loop simulations. Our experiments show how it better captures crucial aspects of AV evaluation like error recovery than open-loop evaluation. Pseudo-simulation offers significant potential impacts for AV development. It enables more efficient iteration cycles, promotes system robustness by rigorously testing sensitivity to perturbations, and ultimately enhances safety through more comprehensive evaluations. We hope our public navhard benchmark, featuring pre-rendered data and standardized metrics via an online leaderboard, can foster community adoption of pseudo-simulation for standardized comparisons of AV systems.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Limitations and Future Work", "weight": 1.5} -->

Correlation with Real-World Deployment. Our current validation focuses on establishing correlation with established simulation benchmarks. We do not yet demonstrate or claim direct correlation with performance metrics from real-world vehicle deployment. Bridging this gap between simulation-based evaluation and predicting real-world outcomes remains an important direction for future investigation. Rather than replacing real-world validation, frameworks to augment real-world evaluations with simulation can be applied more effectively with our work

<!-- chunk {"id": "body-0041", "role": "body", "section": "Limitations and Future Work", "weight": 1.5} -->

Pre-Processing Computational Cost. The current pipeline relies on a per-scene optimization process (based on MTGS) to generate the synthetic views, requiring approximately 1-2 hours per scene on current hardware. While manageable for our dataset scale (under 1000 scenes), this computational cost limits scalability for extremely large datasets. Exploring recent advancements in potentially faster, feedforward 3D scene representation and rendering methods could offer a path towards significantly reducing this overhead in the future.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Limitations and Future Work", "weight": 1.5} -->

Rendering Fidelity and Evaluation. Despite achieving excellent quantitative results on rendering fidelity (LPIPS) and downstream task performance (mIoU, EPDMS), some visual artifacts may persist in the generated synthetic views. Our evaluation primarily focuses on algorithmic metrics. Future work may also benefit from incorporating human perceptual studies to gain a more comprehensive understanding of perceived realism and the potential impact of any remaining artifacts. Furthermore, combining neural rendering techniques like ours with state-of-the-art generative diffusion models might offer possibilities for enhancing rendering quality.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Limitations and Future Work", "weight": 1.5} -->

Background Traffic Realism. The current approach utilizes relatively simple, rule-based traffic models for background agents within the synthetic observations. This results in these agents strictly following road-centerline paths during Stage 2 evaluation. In future work, we aim to incorporate more sophisticated, potentially learned, traffic models that can adapt background agent behavior dynamically based on the ego agent's actions. Another possible extension is adversarial background traffic designed to further emphasize the need for robustness. These extensions could enable the evaluation of more complex, interactive scenarios and improve evaluation fidelity without compromising the scalability of the pseudo-simulation approach.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Limitations and Future Work", "weight": 1.5} -->

Human Flag Filtering. Our filtering strategy disregards rule violations also committed by human experts. While this helps reduce false positives, it could also risk overlooking important failure and edge cases, since human driving is not always a gold standard for safety. Future work could further refine the human flag filtering and explore this trade-off to ensure more reliable evaluation.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Limitations and Future Work", "weight": 1.5} -->

Metric Design Choices. We choose multiplicative aggregation because most sub-scores are binary-valued, and multiplication captures compounding failures, e.g., a collision should significantly impact the final score. Our Gaussian weighting is selected for its strong empirical performance with minimal assumptions. Exploring more principled formulations for aggregation and weighting remains an interesting future direction.
