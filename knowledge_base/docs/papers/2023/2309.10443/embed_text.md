<!-- arxiv-full-text:v1 {"arxiv_id": "2309.10443", "source": "arxiv-html"} -->

## Introduction

Learning-based planners are considered a potentially scalable solution for autonomous driving, supplanting traditional rule-based planners. This has sparked significant research interest in recent years. In particular, imitation-based planners are reported to achieve notable success in simulations and real-world scenarios. Nevertheless, these planners are predominantly trained and evaluated in diverse custom conditions (*e.g*. varying datasets, metrics, and simulation setups) owing to the absence of a standardized benchmark. Consequently, it becomes challenging to compare and summarize effective design choices for constructing practical learning-based systems.

Recently, the release of the large-scale nuPlan dataset, alongside a standardized simulation benchmark, has provided a new opportunity for advancing learned motion planners. Enabled by this fresh benchmark, we conduct in-depth investigations on several common and critical yet not fully studied design choices of the learning-based planner, aiming to provide constructive suggestions for future research. This paper concentrates on two overarching and fundamental facets of the imitation-based planner: the requisite ego features for planning and the efficacious techniques of data augmentation.

The majority of imitation-based planning models follow the success of prediction models and inherently incorporate the past trajectory of the autonomous vehicle (AV) as an input feature, though imitation learning (IL) has frequently been noted for its tendency to acquire shortcuts from historical observations. Our research reaffirms that the past motion of the AV leads to significant closed-loop performance degradation. The planner achieves enhanced performance by solely utilizing the AV's present state. Surprisingly, it attains better closed-loop performance purely using the AV's current pose (position and heading). This implies that additional kinematic attributes typically deemed crucial for planning, such as velocity, acceleration, and steering, lead to a performance decline. To gain deeper insights into this phenomenon, we perform a sensitivity analysis to assess the impact of the AV's states on the resulting trajectory. Our experiments reveal that the planner can learn to exploit shortcuts from its kinematic states, even when past motion data is absent. To mitigate this challenge, we introduced a straightforward yet highly effective attention-based state dropout encoder, enabling the planner that utilize kinematic states to achieve optimal overall performance.

Imitation learning is also known to have compounding errors. Perturbation-based augmentations are a commonly employed strategy to instruct the planner on recovering from deviations. We conduct comprehensive experiments exploring various augmentation techniques, including history perturbation, state perturbation, and future correction. Additionally, we demonstrate the indispensability of proper normalization for the effectiveness of augmentation. Furthermore, we identify an ignored imitation gap within current learning frameworks and illustrate its potential impact.

Finally, by combining our findings, we provide a pure learning-based baseline model that demonstrates strong performance against state-of-the-art competitors on our standardized nuPlan benchmark. Our contributions are summarized as follows: We perform an in-depth investigation on necessary features for ego planning, yielding counter-intuitive results contrary to mainstream practices. Furthermore, we introduced an effective attention-based state dropout encoder that attains the highest overall performance.

We conducted a comprehensive array of experiments involving various augmentation techniques, thereby elucidating an effective strategy to mitigate compounding errors. Additionally, we identified an overlooked imitation gap in current learning frameworks.

By combining our findings, we provide an open baseline model with strong performance. All our code, benchmarks, and models will be publicly released, as a reference for future research.

## Related Work

### Imitation-based planners

are highly favored among learning-based planners due to their ease of convergence and typical scalability with data. They can be categorized into two distinct groups based on their input types: 1\) End-to-end. End-to-end (E2E) methods directly produce future trajectories using raw sensor inputs. Leveraging the closed-loop CARLA benchmark and the collaborative efforts of the open-source community, E2E methods have achieved remarkable advancements within a short span of time: evolving from initial basic CNN-based approaches (LBC, CILRS) to encompass multi-modal fusion (Transfuser, NEAT, MMFN, Interfuser, ThinkTwice), as well as incorporating integrated perception and planning strategies (LAV, ST-P3, VAD). However, due to limitations posed by the simulated environment, these methods typically function at low vehicle speeds, and the behavior of the simulated traffic agents lacks realism and diversity. Emerging and intriguing research, such as data-driven traffic simulation and realistic sensor emulation, holds the potential to mitigate these issues.

2\) Mid-to-mid. These approaches utilize post-perception outcomes as input and can directly learn from recorded real-world data. Chauffernet introduces the synthesis of perturbed trajectories to mitigate covariate shift, a practice that becomes common in subsequent studies. further augment the training data with on-policy rollouts. Several works have demonstrated the capability to operate real vehicles (SafetyNet, UrbanDriver, SafetyPathNet ). Many include a post-optimizer (DIPP, GameFormer, hotplan, pegasus ) to enhance the planner's robustness. All the abovementioned methods except hotplan use AV's history motion. Our study focuses on this category and provides an in-depth investigation of several critical design choices based on standardized data and benchmarks.

### Beyond imitation

Another line of research aims to overcome the inherent limitations of pure imitation learning (IL), such as utilizing environmental losses, integrating IL with reinforcement learning, and incorporating adversarial training, also known as closed-loop training. Our work shows that the pure IL-based planner has not reached its limit and can be significantly improved with appropriate design.

## Rethink Imitaion-based Planner

Figure 1: A brief overview of our baseline model. Agents, map, and ego features are separately encoded and then concatenated, which are subsequently processed by a stack of transformer encoder layers. The baseline model jointly predicts traffic agents and plans for ego vehicle at the scene level.

We consider the task of urban navigation employing a learned planner, trained by imitating the expert trajectory from the dataset. At each planning iteration, the planner receives various inputs, such as tracking data of surrounding objects up to a 2-second historical window, the current and past kinematic states of the ego vehicle, information about traffic lights, high-definition (HD) maps, speed limits, and the designated route. The planner is tasked with generating a trajectory for the subsequent 8 seconds. It is essential to note that, unless otherwise stated, we employ the unaltered trajectory output from the planner in this paper. We intentionally avoid incorporating performance-enhancing techniques, such as rule-based emergency stops or post-optimization, to assess the planner's inherent performance.

### nuPlan

is a large-scale closed-loop ML-based planning benchmark for autonomous vehicles. The dataset encompasses 1300 hours of recorded driving data collected from four urban centers, segmented into 75 scenario types using automated labeling tools.

### Simulation

We use nuPlan's closed-loop simulator as our simulation environment. Each simulation entails a 15-second rollout at a rate of 10 Hz. It employs an LQR controller for trajectory tracking, while the control commands are utilized to update the state of the autonomous vehicle through an internal kinematic bicycle model. The behavior of background traffic varies based on the simulation mode, which can be non-reactive (log-replay) or reactive.

TABLE I: Results of different input features. For models with history input, “shared” and “separate” encoders indicate whether both the agent and ego vehicles utilize a shared history encoder or distinct ones. For models without history input, + refers to the inclusion of an additional state variable compared to the preceding model in the table. Higher values indicate better performance for all metrics, with the best metric highlighted in bold.

### Metrics

We employ the official evaluation metrics provided by nuPlan, which include the open-loop score (OLS), non-reactive closed-loop score (NR-CLS), and reactive closed-loop score (R-CLS). R-CLS and NR-CLS share identical calculation methodologies, differing only in that R-CLS incorporates background traffic control via an Intelligent Driver Model (IDM) during simulations. The closed-loop score is a comprehensive composite score, achieved through a weighted combination of factors such as traffic rule adherence, human driving resemblance, vehicle dynamics, goal attainment, and other metrics specific to the scenario. The score scales from 0 to 100. For a detailed description and calculation of the metrics, please refer to.

### Baseline

As a baseline, we have adapted the motion-forecasting backbone model from our prior work to address the planning task. Figure 1 provides a concise overview of the baseline model. Despite its simplicity, the architecture primarily comprises multiple Transformer encoders, demonstrating significant modeling capacity. We direct interested readers to the code base for details.

### Benchmark

For all experiments, we standardize the data split for training and evaluation. For the training phase, we utilize all 75 scenario types in the nuPlan training set, limiting the total number of scenarios to 1M frames. For the evaluation phase, we employ 14 scenario types specified by the nuPlan Planning Challenge, each comprising 20 scenarios. We examine two scenario selection schemes: -random: scenarios are randomly sampled from each type and fixed after selection, and -hard: in order to investigate the planner's performance on long-tail scenarios, we execute 100 scenarios of each type using a state-of-the-art rule-based planner (PDM-Closed ), subsequently selecting the 20 least-performing scenarios of each type. Example scenarios can be found on the project page. As the online leaderboard submission is closed, all evaluations are conducted on the nuPlan public test set.

### III-A Input feature makes a difference

This section aims to address the following questions: Is historical motion data essential for planning? If not, do all current states of autonomous vehicles contribute to improving the planner's performance? To address these inquiries, we conducted an investigation involving two sets of variants derived from our baseline model. The results on -random and -hard benchmarks are presented in Table I. Among the two historical variants, one shares its history encoder with other traffic agents, while the other employs a distinct history encoder for the ego vehicle's past motion. In the case of state-only models, we scrutinized several pivotal state variables essential for conventional planners, encompassing vehicle pose, velocity, acceleration, and steering angle. Based on the experimental results, we have the following findings: Figure 2: The left side shows the planning trajectory of the state6 model by adjusting AV’s steering angle from 0.15 to 0.5 rad. The right side illustrates the magnitude of the gradient concerning the trajectory endpoint’s position in relation to the AV’s kinematic states.

Figure 3: Illustration of the attention-based state dropout encoder.

### History is not necessary

While models incorporating historical motion data exhibit superior off-policy evaluation performance (OLS), they manifest significantly poorer performance in closed-loop metrics compared to state-based models. This phenomenon may attributed to the well-established "copycat" problem or learning shortcuts, wherein the planner relies on extrapolation from historical data without a comprehensive grasp of the underlying causal factors. Furthermore, the advantage in open-loop performance of historical models diminishes rapidly as the number of states increases in state-only models. Therefore, we conclude that history motions are not necessary for planning models.

TABLE II: Experimental results of the state dropout encoder (SDE) on -random and -hard benchmark. Models with SDE gain significant improvements on CLS while maintaining high performance on OLS.

### Shortcut learning in kinematic states

Kinematic states, such as velocity and acceleration, serve as vital initial boundary conditions for ensuring safety and comfort in trajectory planning. Nevertheless, we are surprised to find that the state3 model, which exclusively relies on the autonomous vehicle's (AV) pose (comprising position and heading), significantly outperforms other models incorporating kinematic states in terms of CLS metrics. To gain deeper insights into this phenomenon, we study a left-turn case of the state6 model. As depicted in Figure 2a, the model generates an undesired off-road trajectory when changing the steering angle from 0.15 (blue) to 0.5 (red) rad. We hypothesize the model still learns false correlation from the kinematics even without the present of the past observation.

### State dropout encoder

To confront our assumption, we propose an attention-based state dropout encoder (SDE), as shown in Figure 3. Each state variable undergoes individual embedding through a linear layer before being combined with positional encoding. A learnable query aggregates state embeddings through a cross-attention module. During training, each embedded state (except position and heading) token will be dropped with a certain probability. The encoder compels the model to unveil the root causes of behaviors by imposing partial constraints on its access to auxiliary information. Meanwhile, the model can enhance its planning capabilities when kinematic attributes are accessible. We implement the state dropout encoder in the state5 and state6 models, and the results are depicted in Table II. The results indicate that the utilization of SDE significantly enhances the closed-loop performance of the models. Importantly, when compared to state3, state5 and state6 models augmented with SDE exhibit not only improved closed-loop score but also substantially higher open-loop score, providing compelling evidence for the efficacy of SDE. We point out that state3 model is fundamentally ambiguous as it loses all kinematic information (supported by its poor OLS performance). Figure 2(a)(b) displays the comparative planning results of state6 model, while Figure 2(c)(d) presents comparative results for the magnitude of the gradient of the endpoint's position $(X_{T},Y_{T})$ w.r.t. the initial kinematic states $s_{0}$. The results demonstrate that the model employing SDE is less sensitive to variations in kinematic states, resulting in more resilient planning outcomes.

Figure 4: (a) The original scenario. (b) Random noise is added to the AV’s current state and history motion is smoothed. (c) The coordinates of the scenario are re-normalized based on the perturbed position of the AV. (d) A corrected future trajectory is generated using constrained nonlinear optimization.

TABLE III: Results of different augmentation and normalization combinations on -random benchmark. P: Perturbation; RN: Re-Normalization; FC: Future Correction.

### III-B Data augmentation and normalization

Data augmentation is a common practice for IL-based models to learn how to recover from deviations. In this section, we conduct comprehensive experiments on different data augmentation techniques, aiming to explore effective strategies to mitigate compounding errors. Different augmentation strategies are displayed in Figure 4. In Figure 4(a), an example driving scenario is depicted, with all coordinates normalized relative to the autonomous vehicle's center. In Figure 4(b), randomly sampled noise (perturbation) is added to the AV's current state, and its history states are smoothed accordingly. In Figure 4(c), it is demonstrated that the scenario's coordinates are re-normalized with respect to the autonomous vehicle's center after perturbation. Figure 4(d) showcases the generation of a rectified future trajectory through nonlinear optimization. Essentially, both strategies depicted in Figure 4(b) and 4(d) serve the common objective of guiding the vehicle back to the expert trajectory.

Table III displays the outcomes of experiments conducted with various augmentation strategies on four model variants. Based on these results, the following findings emerge: In the case of the history and state5 models, none of the data augmentations exhibit substantial enhancements. We postulate that the primary challenge faced by these two models is the issue of causal confusion, *i.e*. extrapolation from either historical or kinematic states. For state3 and state6+SDE models, perturbation is of great importance, but only works with proper normalization. For example, state3 model's NR-CLS score boosts from 71.86 to 85.99 with perturbation and re-normalization, which is much higher than solely using perturbation (74.28). This implies it is important to keep the data distribution close between training and testing. Providing a corrected guiding future trajectory does not serve a positive effect. One possible reason is that the manually generated trajectory does not align with the expert's trajectory distribution. Directly using the expert trajectory as supervision is a more effective choice as it keeps the original distribution, and small deviations can be easily fixed by the tracker.

Figure 5: Illustration of the imitation gap and the proposed RL adapter.

TABLE IV: Exprimental results of the log-replay planner (perfect imitation) with different trackers on -random and -hard benchmarks. LQR is the default tracker used by the nuPlan benchmark and the RL adapter is our proposed method to address the imitation gap.

### III-C The hidden imitation gap

### The imitation gap

Within the most popular imitation learning frameworks, models imitate the logged expert's footprints from the dataset. We argue that this learning framework gives rise to a concealed gap in imitation, potentially leading to notable performance degradation. As illustrated in Figure 5, the recorded trajectory, commonly known as the expert trajectory, serves as the ground truth during the training of the imitation-based planner. The generated imitated trajectory is subsequently processed by the downstream tracker and the underlying system dynamics, yielding the final trajectory of the AV. Nevertheless, owing to the lack of knowledge about the tracker and dynamics during training, the actual trajectory may substantially deviate from the recorded trajectory, even when imitation is flawless. This assertion finds support in the experimental findings presented in Table IV. Notably, the NR-CLS of the Log-replay + LQR method on -hard exhibits a significant decrease of $5.65$ in comparison to perfect tracking.

Lon. Acc. limit $\mathbb{1}\left({\overset{˙}{v} > 2.4} \right)$ $\mathbb{1}\left({{\|\overset{¨}{v}\|} > 4.0} \right)$ $\mathbb{1}\left({{\|\overset{˙}{\theta}\|} > 0.95} \right)$ TABLE V: The reward terms and expression of the RL adapter. Action u contains acceleration and steering rate. v and θ refers to the longitudinal and heading angle of the AV.

TABLE VI: Comparison with state-of-the-arts. The runtime includes feature extraction and model inference based on Python code. † indicates these methods’ final output trajectory relies on rule-based strategies or post-optimization.

### RL Adapter

One possible solution is to directly imitate the control command rather than the trajectory points. Nevertheless, this approach is heavily reliant on the specific vehicle model, making it less generalizable and interpretable than the trajectory-based method. An alternative approach involves incorporating a differentiable kinematic model into the trajectory decoder. However, the kinematic model is often oversimplified to ensure differentiability. To tackle this challenge, we introduce a reinforcement learning-based trajectory adapter (RL Adapter) designed to bridge this gap. The RL Adapter transforms the imitated trajectory into the relevant control commands while accounting for the underlying dynamics. The benefits are two-folds. First, it can adapt to various vehicle models without retraining the planner. Second, it imposes no constraints on the vehicle model and remains compatible with non-differentiable vehicle models (*e.g*. high-fidelity real vehicle dynamics model). The training process of the adapter is displayed in Figure 5 and the rewards are shown in Table V. We use PPO for policy optimization and the training finishes in 80K steps with a learning rate of 1e-3. As depicted in Table IV, the RL Adapter performs similarly to perfect tracking, highlighting its capacity to bridge the imitation gap. We notice that it can be integrated into the training process of the planner and leave this as future work.

## Comparison to State of the Art

### Implementation details

Integrating our findings, we propose a fully learning-based baseline planning model called Planning Transformer (PlanTF). Specifically, we employ the state6 model, incorporating a state attention dropout encoder with a dropout rate of 0.75. During training, we apply state perturbation with a probability of 0.5. The model is trained using a batch size of 128 and a weight decay of 1e-4 for 25 epochs. The initial learning rate is set to 1e-3, decaying to zero in a cosine manner.

### Methods

We compare PlanTF's performance with several state-of-the-art planners. RasterModel is a CNN-based planner provided . UrbanDriver is a vectorized planner based on PointNet-based polyline encoders and Transformer. Here we use its open-loop re-implementation and history perturbation is employed during training. GameFormer is a DETR-like interactive prediction and planning framework based on the level-k game, which incorporates a post-optimizer to generate the final trajectory. PDM\* is the winning solution of the 2023 nuPlan Planning Challenge. PDM-Closed is a purely rule-based approach that ensembles the IDM with different hyperparameters. PDM-Hybrid is a variant of PDM-closed that adds an offset predictor to improve its open-loop prediction performance. PDM-Open is the pure learning component without the IDM-based planner. Results are reproduced using their publicly available code and trained on our standard 1M data split.

### Results

Table VI presents comparative results for the -random and -hard benchmarks. First, the proposed PlanTF significantly outperforms all other pure imitation-based methods across all metrics, particularly in terms of closed-loop performance. It is also the only learning-based method that surpasses the widely recognized IDM, highlighting the importance of proper design in IL. Second, when compared to rule-based and hybrid methods, PlanTF delivers outstanding OLS while maintaining highly competitive CLS, without the need for any tricky hand-crafted rules or strategies. Notably, our approach achieves the highest NR-CLS on the -hard benchmark, indicating that although rule-based methods perform well in ordinary scenarios (-random), they struggle to generalize in long-tail situations (-hard). In contrast, PlanTF demonstrates stronger generalization capabilities.

## Conclusion

In this study, we systematically examine several crucial design aspects of imitation-based planners by utilizing the standardized nuPlan benchmark. Our findings reveal that catastrophic shortcut learning generally occurs for input features, such as historical motions and single-frame kinematic states. This leads to the unexpected outcome that planning solely based on the AV's current position results in superior closed-loop performance. To mitigate this issue, we introduce a straightforward attention-based state dropout encoder (SDE) that effectively addresses the shortcut learning problem. With the implementation of SDE, the state6 model achieves the best overall performance. Data augmentation is another significant factor in imitation-based planners. Our results demonstrate that perturbation is vital for reducing compounding errors, but only effective with appropriate feature normalization. Furthermore, we observe that the original expert trajectory remains a reliable training ground truth, even when subjected to perturbation. In addition to these findings, we identify a neglected imitation gap caused by the model's lack of awareness of the underlying system dynamics, which considerably impacts the planner's performance. To rectify this issue, we propose a reinforcement learning-based adapter. By incorporating our findings, the proposed purely learning-based baseline model, PlanTF, demonstrates impressive performance compared to state-of-the-art approaches and is on par with methods that employ intricate rule-based strategies or post-optimization. This highlights the importance of proper design choices for imitation learning-based planners.

### Limitation and future work

Despite pushing the boundaries of pure imitation-based planners, our method is constrained by the fundamental mismatch between open-loop training and closed-loop testing. Incorporating closed-loop information and system dynamics into the training process constitutes our future research direction.

### Additional results on benchmark

We present the comparative results (Table. VII) on the benchmark. contains 1180 scenarios from 14 scenario types.

TABLE VII: Comparision to SOTAs on the benchmark. The results of other methods are taken .

### Ablation on the state dropout rate

Table VIII shows the ablation study on different dropout rate the of state6+SDE model.

TABLE VIII: Ablation study on the state dropout rate of the SDE.
