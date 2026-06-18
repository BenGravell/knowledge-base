## Introduction

Trajectory planning is a fundamental component of autonomous driving systems, directly influencing vehicle safety, efficiency, and the ability to navigate complex and dynamic environments. In recent years, learning-based planning approaches have attracted increasing attention due to their strong adaptability, competitive performance, and minimal reliance on manually designed rules. These methods offer promising solutions for generating trajectories that can respond effectively to various traffic scenarios and rapidly changing road conditions.

However, due to the complexity and diversity of real-world driving scenarios, most existing planning methods, whether based on imitation learning (IL) or reinforcement learning (RL), rely heavily on expert demonstrations for supervision. This dependency introduces two key limitations: (i) expert data rarely covers negative scenarios such as collisions or off-road driving, leaving the model unable to explicitly learn how to avoid them, and (ii) demonstrations are not always optimal and may contain undesirable behaviors. For example, we find that over 10% of the nuPlan training scenes exhibit speeding, and some contain uncomfortable maneuvers or critically low time-to-collision (TTC) values. As a result, models trained purely on expert data risk inheriting these undesirable behaviors without a clear notion of safety, as shown in Figure 2.

To address these limitations, we draw inspiration from the success of large language models (LLMs), which typically adopt a two-stage training paradigm: pre-training as a general-purpose predictor via next-token prediction, followed by RL fine-tuning to align outputs with desired objectives (e.g., format). Our key insight is that trajectory planning can be formulated in a similar way, i.e., first trained as a trajectory predictor on expert driving data, and then fine-tuned using RL to align the trajectory with explicit planning principles, such as safety, comfort, and rule compliance. This decoupled paradigm separates principle alignment from behavior learning, enabling the model to retain human-like behaviors, enhancing safety awareness and discarding undesirable patterns learned from the expert data.

Specifically, we introduce Plan-R1, a two-stage dual-model framework for principle-aligned trajectory planning. In the pre-training stage, trajectories are discretized into motion tokens across time and space, and a general motion predictor is trained with next-motion-token prediction to capture diverse, human-like multi-agent behaviors. In the fine-tuning stage, unlike prior methods that rely on human preference data or additional expert demonstrations, which may introduce biases or undesirable behaviors, we use rule-based rewards that provide consistent and unbiased supervision. To ensure realistic multi-agent interactions and stable optimization, we introduce a dual-model design: a trainable ego planner explores alternative decisions, while a frozen copy of the pre-trained model serves as a reactive world model to predict the responses of surrounding agents. This separation enables ego-centric policy updates without destabilizing non-ego behaviors, yielding stable, interaction-aware joint predictions.

For RL optimization, we adopt Group Relative Policy Optimization (GRPO), which has shown strong performance across various domains. However, we find that its default design is not well suited for trajectory planning. Unlike mathematical reasoning tasks where the goal is simply to produce the correct answer, trajectory planning must jointly optimize multiple, potentially conflicting objectives with carefully designed priorities. For example, collision avoidance must always take precedence over comfort. After pre-training, nearly 80% of trajectory groups contain no safety violations, and their reward variance is dominated by non-safety objectives such as comfort. Standard GRPO normalizes rewards independently within each group, erasing natural scale differences across groups. This causes rare, high-variance safety-violation groups to have normalized advantages comparable to abundant safe groups (Figure 5), diluting safety-critical gradients and shifting optimization toward non-safety objectives. To address this, we propose Variance-Decoupled GRPO (VD-GRPO), which replaces per-group normalization with centering and fixed scaling. By preserving absolute reward magnitudes, safety-critical groups naturally generate larger gradients, ensuring that high-priority safety objectives remain dominant and continue to improve even in late-stage training when such cases become extremely rare.

By addressing both behavior-principle decoupling and long-tailed safety optimization, Plan-R1 provides a unified and scalable solution for safe and feasible trajectory planning. Results on the nuPlan benchmark show that Plan-R1 significantly improves both safety and feasibility, achieving state-of-the-art performance and demonstrating strong generalization to challenging interactive scenarios.

The primary contributions of this paper are:

We introduce a new perspective that formulates trajectory planning as a principle-aligned prediction task, decoupling planning principle alignment from behavior learning to overcome the limitations of expert data.

We propose Plan-R1, a two-stage dual-model framework that first pre-trains a motion predictor on expert data to capture diverse driving behaviors, and then fine-tunes it with rule-based reinforcement learning, requiring no additional expert or preference data.

We identify a key limitation of GRPO: per-group normalization erases cross-group scale differences, diluting safety-critical signals. We address it with Variance-Decoupled GRPO (VD-GRPO) to preserve absolute reward magnitudes, prioritizing safety-critical objectives during optimization.

Plan-R1 achieves state-of-the-art performance on the nuPlan benchmark, significantly improving both safety and feasibility, particularly in challenging reactive settings.

## Related Work

### Learning-based trajectory planning

Learning-based trajectory planning methods can be broadly grouped into imitation learning (IL), reinforcement learning (RL), and hybrid IL+RL approaches. Pure IL and RL have been extensively explored for trajectory planning and achieved notable progress; Cusumano-Towner et al., 2025). However, they both have inherent limitations: IL relies heavily on expert demonstrations, which rarely cover safety-critical events and often contain suboptimal behaviors such as speeding; RL enables behavior discovery beyond demonstrations but suffers from severe sample inefficiency, complex multi-objective reward design, and poor human-likeness in large, dynamic environments.

Recent works therefore explore hybrid IL+RL approaches. One line of research adopts imitation-regularized RL, where the distance to expert trajectory is incorporated into the optimization objective as either a reward signal or a regularizer. For example, BC-SAC jointly optimizes a behavior cloning loss and a Soft Actor-Critic loss to improve safety. These methods stabilize training but remain heavily dependent on expert data, inheriting its biases and undesirable behaviors. Another line follows a pre-training + fine-tuning paradigm inspired by LLMs, such as Gen-Drive and TrajHF. Gen-Drive trains a reward model from collected preference data and fine-tunes the planner via RL. TrajHF fine-tunes the planner using human driving preference data to align with desired driving styles. However, collecting preference data is expensive and may introduce new biases, limiting scalability and reliability. In contrast, our Plan-R1 also adopts a two-stage framework but replaces preference data with rule-based rewards, which provide consistent and unbiased supervision. This allows us to align planning with safety and other principles while preserving the diverse human-like behaviors, achieving safe and robust trajectory planning without extra human supervision.

### Group Relative Policy Optimization (GRPO)

GRPO is a reinforcement learning algorithm originally developed for mathematical reasoning. It samples multiple rollouts under the same context to form a group and normalizes rewards within each group to compute relative advantages, eliminating the need for a value function and avoiding instability from inaccurate value estimation in methods like PPO. This simplicity makes GRPO highly effective for alignment tasks such as reasoning and search. Moreover, DAPO extends GRPO by introducing asymmetric clipping and dynamic sampling to improve optimization stability and efficiency. Dr.GRPO removes the per-group standard deviation term, aiming to reduce problem-level difficulty bias and stabilize optimization in language model training. VD-GRPO is inspired by Dr.GRPO but addresses a fundamentally different problem in a different domain: in safety-critical trajectory planning, rewards are multi-objective and often conflicting, where rare but catastrophic events (e.g., collisions) must be prioritized. We demonstrate that group-wise normalization erases cross-group scale differences, causing rare, high-variance safety-violation groups to have similar advantages to abundant low-variance safe groups, suppressing optimization for safety-critical objectives. VD-GRPO address it by replacing normalization with centering and fixed scaling, ensuring that safety-critical objectives remain dominant throughout training.

## Method

Figure 1: Illustration of our Plan-R1: Stage (a) pre-trains a motion predictor on expert data; Stage (b) fine-tunes it with VD-GRPO using rule-based rewards to align with planning principles.

We propose Plan-R1, a two-stage framework that decouples planning principle alignment from behavior learning. As illustrated in Figure 1, Plan-R1 consists of an autoregressive pre-training stage and a rule-based RL fine-tuning stage. The model is first pre-trained on expert demonstrations to capture diverse human-like motion behaviors, and then fine-tuned with rule-based rewards to align the ego motion with explicit planning principles. In subsection 3.1, we formulate trajectory planning as a principle-aligned sequence prediction task. subsection 3.2 describes the autoregressive pre-training process, while subsection 3.3 presents the fine-tuning stage and introduces Variance-Decoupled GRPO (VD-GRPO) to further address the safety-critical optimization challenge.

### Problem formulation

Trajectory planning is inherently sequential, making autoregressive modeling a natural choice. We extend this formulation into a principle-aligned autoregressive prediction task by explicitly incorporating high-level planning principles (e.g., safety, comfort, traffic rule compliance). In this formulation, the ego vehicle's trajectory is generated jointly with the predicted motions of surrounding agents, enabling the planner to model realistic multi-agent interactions. Formally, given a scene context $C$ and a set of planning principles $P$, our goal is to generate the joint future motions $Y = {\{ y_{t,n}\}}_{{t = 1}:{{F,n} = 0}:N}$ for all agents, where $F$ is the planning horizon, $N$ is the number of surrounding agents, $y_{t,n}$ denotes the motion of agent $n$ at time step $t$, and the ego vehicle is indexed by $n = 0$. Directly modeling $p{({Y \mid {C,P}})}$ is intractable, but leveraging temporal causality and short-term conditional independence allows factorization as:

where the last approximation assumes that surrounding agents' future motions are independent of the ego vehicle's planning principles $P$. This yields two sub-problems: (i) predicting each surrounding agent's motion $p_{a}{({y_{t,n} \mid {y_{{< t},{0:N}},C}})}$, and (ii) generating the ego vehicle's trajectory $\pi_{e}{({y_{t,0} \mid {y_{{< t},{0:N}},C,P}})}$ with additional conditioning on planning principles. The agent predictor $p_{a}$ can be learned via next-motion prediction on large-scale datasets, whereas modeling the ego planner $\pi_{e}$ is more challenging because it must not only produce human-like motions while satisfying $P$. Since $p_{a}$ is trained on large-scale human driving data that implicitly reflects $P$, it provides a strong prior for $\pi_{e}$. However, this alignment is only implicit and imperfect: human demonstrations may still contain unsafe or suboptimal behaviors, and $p_{a}$ itself cannot guarantee strict adherence to $P$. To address this, we initialize $\pi_{e}$ with $p_{a}$ and fine-tune it using reinforcement learning, where rule-based rewards explicitly ensure compliance with $P$.

### Autoregressive pre-training

### Tokenization

To enable autoregressive modeling, continuous trajectories are first discretized into motion tokens. Temporally, trajectories are segmented at fixed intervals. Spatially, the K-disk clustering algorithm is applied to the resulting motion segments based on their average corner distance, producing a motion token vocabulary. Each token represents a prototypical displacement and heading change over a fixed time step. For each agent, the trajectory is thus transformed into a sequence of motion tokens spanning the prediction horizon.

### Model architecture

Our model employs a transformer decoder with factorized attention to model multi-agent spatio-temporal interactions, as shown in Figure 1 (a). The architecture is designed to capture the temporal dynamics of each agent's trajectory and its interactions with the map and neighboring agents. Following prior work, motion tokens are processed through a stack of attention-based fusion blocks. Each block consists of three components: Temporal self-attention, modeling motion continuity and capturing temporal dependencies for each agent; Agent-map cross-attention, integrating spatial constraints by attending to road elements and ensuring compliance with the road network; Agent-agent cross-attention, capturing local interactions with neighboring agents to reason about dynamic behaviors. To maintain translation and rotation invariance, relative spatio-temporal position embeddings are applied to all attention modules. Both ego and non-ego agents share the same encoder structure, and all attention computations are implemented in a query-centric manner for efficient multi-agent rollout.

### Training objective

The model is trained with a next-motion-token prediction objective, minimizing the negative log-likelihood of the next token for all agents:

This objective enables the model to approximate the latent distribution of human driving behaviors, capturing diverse and realistic motion patterns from large-scale expert data. At this stage, the model simply imitates human-like behavior without explicit planning principles.

### Reinforcement learning fine-tuning

While autoregressive pre-training captures human-like motion patterns, it does not explicitly enforce high-level planning principles. To address this gap, we fine-tune the ego motion predictor using reinforcement learning, as shown in Figure 1 (b), optimizing it to better align with predefined planning principles such as safety, comfort, and rule compliance. The generation process is formulated as a sequential decision-making problem, where the ego agent iteratively selects motion tokens to maximize rewards that reflect desirable planning behaviors.

### Dual-Model rollout

A key challenge in RL fine-tuning is to realistically simulate how surrounding agents react to the ego vehicle's actions. A naive solution is to replay ground-truth (GT) behaviors of surrounding agents, which ignores ego interventions and thus yields unrealistic, non-reactive simulations. We address this issue with a dual-model design: a trainable ego planner $\pi_{e}$ interacts with a frozen copy of the pre-trained model $p_{a}$, which acts as a reactive world model for surrounding agents. During rollouts, $\pi_{e}$ explores alternative decisions while $p_{a}$ predicts the responses of other agents based on the evolving joint history, enabling interaction-aware simulation without requiring additional training for $p_{a}$. This separation allows ego-centric policy updates without destabilizing non-ego dynamics, resulting in stable and realistic multi-agent rollouts.

### Rule-based Rewards

Unlike pure RL-based planning, our approach does not need to learn realistic human-like behaviors from scratch. This is because the pre-trained model already generates plausible, human-like motions, which greatly simplifies reward design: it only needs to target specific aspects such as safety, comfort, and rule compliance, without the burden of modeling basic driving realism. Here, we design a set of interpretable, rule-based reward functions covering key aspects such as collision avoidance, driving area compliance, comfort, speed limit compliance, and progress. Following, we compute the total reward as the product of two components: a set of multiplicative safety indicators (i.e., collision avoidance, driving area compliance) and a weighted sum of soft cost terms (e.g., comfort, speed limit compliance, progress):

where $\mathbf{1}_{k,t} \in {\{ 0,1\}}$ denotes whether safety constraint $k$ is satisfied at step $t$, and $r_{j}{(y_{t})}$ is the score of cost term $j$ with weight $w_{j}$. This formulation ensures that violations of critical safety conditions will nullify the total reward, while soft planning objectives are optimized only when safety constraints are satisfied. Details of the reward implementation are provided in Appendix C.

### Variance-Decoupled GRPO

We adopt Group Relative Policy Optimization (GRPO) to fine-tune the ego policy. GRPO eliminates the need for an explicit value function by computing relative advantages within each sampled group, reducing implementation complexity and avoiding instability caused by inaccurate value estimation.

During fine-tuning, the pre-trained trajectory predictor serves as a fixed reference policy $\pi_{\text{ref}}$, while the ego policy $\pi_{e}$ is updated to better align with planning principles. For each scenario, a group of $G$ future trajectories $\{ Y^{1},\ldots,Y^{G}\}$ is sampled from the old ego policy $\pi_{e_{\text{old}}}$, and the loss is:

where ${\hat{A}}_{t}^{g} = {\sum_{\tau = t}^{F}{\overset{\sim}{R}{(y_{\tau}^{g})}}}$ is the cumulative advantage of token $t$. Standard GRPO normalizes rewards within each group as ${\overset{\sim}{R}{(y_{t}^{g})}} = {{({{R{(y_{t}^{g})}} - \mu_{R}})}/\sigma_{R}}$, with $\mu_{R},\sigma_{R}$ being the group mean and standard deviation. The KL divergence term regularizes the update, keeping the fine-tuned policy close to the reference policy and thereby retaining human-like behaviors learned during pre-training.

However, directly applying GRPO to trajectory planning yields limited improvements. We attribute this to a key limitation of GRPO in multi-objective planning: group-wise normalization erases cross-group scale differences (Figure 5). As a result, rare safety-violation groups are normalized to have similar advantages as the abundant safe groups. Since most safe groups only exhibit minor fluctuations in comfort or other secondary objectives, critical safety signals become indistinguishable during optimization. Over time, the optimizer gradually shifts its focus toward these abundant non-safety objectives, leading to severe under-optimization of rare but catastrophic safety cases.

To address this issue, we propose Variance-Decoupled GRPO (VD-GRPO), which replaces per-group normalization with centering and a fixed global scaling constant $c$:

By decoupling normalization from variance, VD-GRPO preserves absolute reward scales across groups, ensuring safety-critical objectives remain dominant over secondary goals. High-variance groups, typically corresponding to rare catastrophic cases, naturally produce larger gradients, amplifying safety signals without manual reweighting. This enables continuous improvement on rare but important safety cases even in late-stage training.

## Experiments

Rule-based &amp; Hybrid

Table 1: Comparison with SOTAs on nuplan benchmark. The best result is in bold and the second best result is underlined. *: with rule-based post-processing. NR/R: non-reactive/reactive mode.

Figure 2: Comparison of closed-loop ego trajectories. Trajectories are color-coded: orange indicates speeding segments, while green represents compliant motion. The expert trajectory (a) shows a clear speeding segment. Both PLUTO (b) and Diffusion Planner (c) mimic this behavior, indicating that planners trained solely on expert data tend to inherit undesirable patterns.In contrast, Plan-R1 (d) avoids speeding, demonstrating the effectiveness of rule-based reinforcement learning fine-tuning.

### Experimental setup

### Datasets

We evaluate our method on the nuPlan benchmark, a large-scale platform for trajectory planning in autonomous driving. The dataset contains over 1,300 hours of expert driving logs collected across four cities, covering diverse and challenging urban driving scenarios. Simulation runs for 15 seconds at 10 Hz: the ego vehicle executes its planned trajectory using a bicycle model and an LQR controller, while surrounding agents either follow replayed trajectories or react through the IDM policy. Following PLUTO, we sample 1M training instances for autoregressive pre-training. To reduce the computational cost of closed-loop rollouts during reinforcement learning, we build a smaller fine-tuning set of 100K scenarios. Evaluation is performed on the standard, -random, and -hard splits under both non-reactive and reactive settings.

### Metrics

We evaluate planning performance in closed-loop simulation using two standard metrics: Non-Reactive Closed-Loop Score (NR-CLS) and Reactive Closed-Loop Score (R-CLS). NR-CLS replays logged trajectories for surrounding agents, while R-CLS uses the IDM planner to generate reactive behaviors, providing a more challenging and realistic evaluation. Both metrics assess 15-second rollouts across key driving objectives such as collision avoidance and speed limit compliance, with scores ranging from 0 to 100 (higher is better).

Table 2: Ablation study on the importance of ruled-based RL fine-tuning and VD-GRPO.

Figure 3: Comparison of closed-loop ego trajectories generated by the pre-trained baseline (a) and Plan-R1 (b). Orange indicates speeding segments, and cyan marks static obstacles. The baseline exhibits issues such as off-road driving (left), speeding (middle), and collision with static obstacles (right), while Plan-R1 avoids these failures, producing safe and feasible trajectories.

### Comparison with SOTAs

### Quantitative results

We compare our method, Plan-R1, against a wide range of existing planners on the nuPlan benchmark, as shown in Table 1. Plan-R1 matches the strongest prior method, Diffusion Planner, under the non-reactive setting, showing that RL fine-tuning preserves expert-like behavior. In the more challenging reactive setting, where surrounding agents dynamically respond to the ego vehicle, Plan-R1 achieves state-of-the-art scores of 87.69 (), 77.20 (-hard), and 90.04 (-random), surpassing Diffusion Planner by +4.89, +7.98 and +7.11 points, respectively. This demonstrates Plan-R1's superior ability to handle highly interactive scenarios, thanks to the dual-model design and rule-based principle alignment. Following Diffusion Planner, we also apply the existing refinement module for post-processing without any parameter tuning, where Plan-R1 still achieves the highest NR-CLS and R-CLS of 94.72 and 93.54 on, respectively. These results validate the effectiveness of our two-stage framework: pre-training establishes a strong behavioral prior, while RL fine-tuning explicitly optimizes for safety and feasibility, enabling Plan-R1 to generate trajectories that are both robust and compliant.

### Qualitative Results

We conduct a case study where the expert trajectory violates the local speed limit. As shown in Figure 2, both PLUTO and Diffusion Planner, trained solely on expert demonstrations, replicate this speeding behavior. In contrast, Plan-R1 maintains a compliant velocity throughout the rollout, demonstrating its ability to correct undesirable behaviors inherited from expert data. This highlights the effectiveness of rule-based RL fine-tuning in overcoming the limitations of expert-only training, producing more reliable behaviors.

### Ablation studies

### The importance of rule-based RL fine-tuning

We first evaluate the effect of adding rule-based RL fine-tuning to the pre-trained model. As shown in Table 2, GRPO fine-tuning consistently improves the overall score (e.g., +3.04 NR-CLS, +5.54 R-CLS) and most individual metrics (e.g., +2.29 drivable area compliance), showing that rule-based RL explicitly enhances safety awareness while also correcting undesirable behaviors, such as speeding, that are inherited from human demonstrations. Qualitative results in Figure 3 further illustrate this improvement: the pre-trained baseline exhibits off-road driving, speeding, and collision with static obstacle, while the RL fine-tuned model produces safe and feasible trajectories.

### The effect of VD-GRPO

While standard GRPO significantly improves soft objectives such as progress (+2.47) and speed compliance (+3.08), it causes a drop of -0.96 in the critical collision avoidance metric, which is undesirable. To investigate this issue, we analyze the distributions of absolute advantage values ($|\hat{A}|$) for safe and unsafe (violation) groups, as shown in Figure 5 (a). Even though our reward function (Equation 3) assigns absolute priority to safety indicators such as collision avoidance via multiplicative terms, the two distributions almost completely overlap in the low-advantage region, while safe groups with small variance from soft-term fluctuations produce disproportionately large advantages, and unsafe groups with higher variance yield smaller advantages. This stems from GRPO's group-wise normalization, which erases reward scale differences across groups and dilutes rare yet critical safety signals.

As shown in Figure 5 (b), VD-GRPO addresses this issue by preserving absolute reward magnitudes, allowing safety-critical (unsafe) groups to naturally produce larger advantages and remain dominant throughout training. We further track the proportion of unsafe groups during training (Figure 5), where VD-GRPO reduces this ratio from 6.7% to 4.7% (29.8% reduction), indicating substantially safer planning behaviors. Results in Table 2 further confirm these benefits: collision avoidance +3.45, drivable area compliance +0.39, NR-CLS +2.58, and R-CLS +1.69 compared to GRPO. These findings demonstrate that VD-GRPO effectively amplifies rare yet critical safety signals, continuously improving safety while maintaining balanced performance on secondary objectives.

### Dual-model design

We conduct an ablation study to verify the effectiveness of our dual-model design (Table 3). Simply replaying logged trajectories of surrounding agents (GT replay) yields an R-CLS score of 87.44, which is better than the pre-trained model but substantially below our full method. This indicates that non-reactive simulation provides limited benefit, as it fails to capture realistic multi-agent interactions and thus cannot fully support effective reinforcement learning fine-tuning. Replacing GT replay with a learned world model substantially improves performance: our reactive world model achieves an R-CLS of 90.04, demonstrating the importance of interaction-aware simulation. To isolate this effect from model capacity, we also compare against a pre-trained baseline with doubled parameters (Pre-train ($2 \times$)). While the larger model provides a modest gain of +2.13, it is far smaller than the +7.23 improvement achieved by introducing the reactive world model. This confirms that the performance gain primarily stems from our dual-model design rather than network size. These results highlight the critical role of modeling responsive surrounding-agent behaviors during RL fine-tuning, enabling stable optimization and superior closed-loop performance. Finally, more results and ablation studies can be found in Appendix A and Appendix B.

Figure 5: Proportion of unsafe groups during training.

Table 3: Ablation on model capacity and world model (WM) choices.

Figure 4: Distributions of |Â| for safe vs. unsafe groups.

## Conclusion

We presented Plan-R1, a two-stage framework that decouples planning principle alignment from behavior learning for safe and feasible trajectory planning. In the first stage, a motion predictor is pre-trained on expert demonstrations to capture diverse, human-like driving behaviors. In the second stage, the ego policy is fine-tuned with rule-based rewards to explicitly align planning with principles such as safety, comfort, and traffic rule compliance. To address the limitation of standard GRPO, where group-wise normalization suppresses optimization for rare but critical safety violations, we proposed Variance-Decoupled GRPO (VD-GRPO), which preserves absolute reward magnitudes so that safety-critical objectives remain dominant throughout training. Experiments on the nuPlan benchmark demonstrate that Plan-R1 significantly enhances safety and feasibility, achieving state-of-the-art performance, particularly in challenging reactive settings.
