<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

RoaD: Rollouts as Demonstrations for Closed-Loop Supervised Fine-Tuning of Autonomous Driving Policies

Topics include Autonomous driving, Imitation learning, Behavior cloning, Closed-loop, Policy learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces Rollouts as Demonstrations, a closed-loop fine-tuning method that augments behavior cloning with guided rollouts from the policy itself. The key idea is to reduce covariate shift by training on states the deployed policy actually visits while still biasing data generation toward expert-quality behavior.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Autonomous driving policies are typically trained via open-loop behavior cloning of human demonstrations. However, such policies suffer from covariate shift when deployed in closed loop, leading to compounding errors. We introduce Rollouts as Demonstrations (RoaD), a simple and efficient method to mitigate covariate shift by leveraging the policy's own closed-loop rollouts as additional training data. During rollout generation, RoaD incorporates expert guidance to bias trajectories toward high-quality behavior, producing informative yet realistic demonstrations for fine-tuning. This approach enables robust closed-loop adaptation with orders of magnitude less data than reinforcement learning, and avoids restrictive assumptions of prior closed-loop supervised fine-tuning (CL-SFT) methods, allowing broader applications domains including end-to-end driving. We demonstrate the effectiveness of RoaD on WOSAC, a large-scale traffic simulation benchmark, where it performs similar or better than the prior CL-SFT method; and in AlpaSim, a high-fidelity neural reconstruction-based simulator for end-to-end driving, where it improves driving score by 41\% and reduces collisions by 54\%.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

^\*\*^footnotetext: Equal contribution, alphabetically sorted.^$\dagger$$\dagger$^footnotetext: Work performed during an internship at NVIDIA Research.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Autonomous vehicle (AV) policies are typically trained with behavior cloning (BC) of human demonstrations, which is scalable but inherently open loop: it assumes i.i.d. inputs and optimizes one-step accuracy under the dataset distribution. Deployed in closed loop, policies influence their own observations, creating a train-test mismatch that induces covariate shift, compounds errors, and reduces robustness to long-tail and interactive scenarios.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

On the other hand, End-to-end (E2E) policies are becoming the new norm of AV policy learning, which map sensor inputs directly to trajectories or controls. By coupling perception, prediction, and planning, they offer data efficiency, simpler deployment, and better long-horizon coordination than hand-engineered stacks.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

While RL directly optimizes closed-loop behavior, it remains impractical for end-to-end driving due to brittle reward design and the cost of safe exploration and high-fidelity simulation. This leaves a gap for a scalable closed-loop training recipe for E2E driving that retains supervised simplicity and data efficiency.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Closed-loop supervised fine-tuning (CL-SFT) has recently emerged as a promising alternative to RL (see Fig. 1). The core idea of CL-SFT is to generate expert-biased on-policy rollouts in simulation and use them as additional demonstrations for fine-tuning, combining the simplicity of supervised learning with the benefits of closed-loop training. The key challenge is how to bias the rollouts towards high-quality behavior such that the fine-tuning step improves the policy. In traffic simulation, Closest Among Top-K (CAT-K) instantiates this idea by selecting, at each step, the closest among a small set of policy-proposed candidate actions to the ground-truth trajectory. On these generated trajectories, CAT-K derives fine-tuning action targets using an inverse dynamics model that chooses the action bringing the agent closest to ground truth.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

While effective for traffic modeling, CAT-K is poorly suited to modern E2E policies because it assumes: (i) discrete actions; (ii) deterministic dynamics and known inverse dynamics; (iii) a diverse pretrained policy where at least one action sample lies close to the ground-truth trajectory at each time step; and (iv) that fresh on-policy trajectories can be generated continuously during training. In E2E driving, none of these assumptions usually hold: policies may output multi-token plans or continuous trajectories, as in the case of diffusion policies; the dynamics (including downstream controllers) are stochastic without closed-form inverse dynamics; the action distribution is typically less diverse due to safety- and, predictability-oriented training (unlike traffic agents that deliberately promote diversity); and regenerating closed-loop rollouts at every optimization step is prohibitively expensive.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work we introduce Rollouts as Demonstrations (RoaD), a novel CL-SFT approach that addresses all limitations above (Fig. 2). First, RoaD retains the expert-biased rollout principle, but removes the need for a recovery action by treating the policy's closed-loop rollouts directly as additional demonstrations for SFT. Empirically we find that this strategy achieves performance on par, or better than CAT-K on large-scale traffic-simulation benchmarks. Second, we replace the Top-K selection with sampling K action candidates so that RoaD can be applied to a more general class of policies. Third, when limited action diversity prevents naive RoaD from being guided by the ground truth, we introduce a lightweight recovery-mode policy output that enables following the ground-truth trajectory even when it is not close to any of the top-k most likely actions. Finally, to reduce collection cost, we show that reusing rollout datasets across multiple optimization steps results in only marginal performance degradation, greatly improving data efficiency.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In experiments, we first validate RoaD for traffic simulation using the Waymo Open Simulation Agent Challenge (WOSAC). RoaD outperforms or matches CAT-K, even when it generates CL experiences only once with the base policy, and the performance improves further the more frequently the data is updated. We then apply RoaD to an E2E driving task to fine-tune a VLM-based policy deployed in AlpaSim, an E2E AV simulator that reconstructs real-world 3D scenes using SOTA 3D Gaussian splatting, 3DGUT. RoaD fine-tuning improves driving scores by 41% and reduces collisions by 54% over the base model in previously unseen scenarios.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, our conclusions are as follows.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce a novel CL-SFT algorithm, RoaD, that removes restrictive assumptions made by prior work.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

We apply RoaD to traffic simulation and match or outperform the previous SOTA CL-SFT method.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

We apply RoaD to E2E driving and achieve substantial improvement in closed-loop driving metrics.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

We are given a policy $\pi_{\theta}=p(a_{t}|o_{<t})$ that maps a history of observation inputs $o_{<t}$ to action outputs $a_{t}$. The policy is pre-trained with behavior cloning (BC), using a dataset of expert demonstrations $\mathcal{D}=\{({o}^{E,i}_{0:T},{a}^{E,i}_{0:T})\}_{i=1}^{|\mathcal{D}|}$. Our goal is to perform closed-loop finetuning of $\pi_{\theta}$ to minimize the covariate shift between open-loop training and closed-loop deployment.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

We assume access to a stochastic simulator that generates a next observation given action, previous observation and some internal state $\mathcal{P}(o_{t+1}\mid{o}_{t},a_{t};\cdot)$, but no access to an on-demand expert nor to a reward function.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

The contents of the observation $o_{t}$ are domain specific. In traffic simulation, $o_{t}$ includes the positions, velocities, and orientations of all nearby agents, together with a vectorized map (lane markings, wait lines, etc.); in E2E driving, it includes the ego vehicle's sensor inputs (e.g., multi-view camera images) and estimated egomotion (e.g., pose, steering angle, velocity, and acceleration). We denote by $s_{t}\in\mathbb{R}^{D_{s}}$ the pose of the controlled agent. For notational simplicity, we assume control of a single agent. Since RoaD operates per agent, extending to multi-agent control, as in our traffic simulation experiments, is straightforward.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Unlike prior work, we make no strong assumptions on the structure of $a_{t}$: it may represent a state delta, as is common in traffic simulation; a continuous control signal, a waypoint, or a trajectory. Single-step control inputs are executed through forward dynamics, respecting vehicle motion constraints, while waypoints and trajectories are tracked by low-level controllers. Predicting $T_{\mathrm{pred}}$-step trajectories is common because such *action chunking* encourages long‑horizon reasoning and often improves accuracy with open-loop training. For notational simplicity, we refer to all these outputs uniformly as $a_{t}$ and use $s_{t+1}=f(s_{t},a_{t})$ to denote the agent state evolution over time.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Further, prior work assumed a policy with discrete modes to select top $K$ predictions, such as next-token-prediction (NTP) traffic simulation models that encode actions in a single token. In contrast, we only assume that $\pi_{\theta}$ can generate $K$ independent action samples, allowing for modern E2E driving policies such as Transformers with simple Gaussian outputs, NTP models with multiple tokens per action, or diffusion and flow-matching policies.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Closed-loop supervised fine-tuning and CatK", "weight": 1.0} -->

CL-SFT adapts a pretrained policy by behavior cloning on states encountered under its own closed-loop rollouts, aligning the training distribution with deployment and mitigating covariate shift. CAT-K provides a practical instantiation with two complementary components: (i) recovery supervision, which defines action targets that move the rollout back toward the expert trajectory at the visited on-policy rollout states; and (ii) expert-proximal rollouts using top $K$ predictions, which bias action selection during rollouts to remain close to the expert, so that the recovery supervision remains valid. Intuitively, CAT-K learns "how to get back on track" while ensuring it never drifts too far from the track in the first place.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Closed-loop supervised fine-tuning and CatK", "weight": 1.0} -->

Formally, the algorithm assumes a tokenized model or a distribution with discrete modes, which can be generally written as $\pi(a_{t}\mid o_{<t})=\sum_{m=1}^{M}\pi(a\mid m)\,\pi(m\mid o_{<t})$, where $M\in\mathbb{N}$ denotes the vocabulary size or number of modes, $\pi(m\mid o_{<t})$ the token prediction or mode-selection distribution, and $\pi(a\mid m)$ the action decoder or action distribution within each mode.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Closed-loop supervised fine-tuning and CatK", "weight": 1.0} -->

In each rollout step, the algorithm selects the top $K$ predictions, $\Xi_{t}=\mathop{\mathrm{top}^{K}}[\pi_{\theta}(a\mid o_{<t})]$, where $\mathop{\mathrm{top}^{K}}[\pi]$ represents finding the $K$ most likely tokens/modes under $\pi(m\mid o_{<t})$ and decoding/sampling the associated action. To bias rollouts toward the expert, the action "closest" to the expert is selected, where $s_{t}$ is the current agent state, $f$ are the deterministic dynamics, $s^{E}_{t+1}$ is the next expert state, and $d(\cdot,\cdot)$ is a distance metric on states, e.g., a weighted $\ell_{2}$ over position, heading, and speed.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Closed-loop supervised fine-tuning and CatK", "weight": 1.0} -->

For each state, recovery actions are defined by projecting the expert continuation onto the action vocabulary, and $\theta$ is updated with behavior cloning on the rollout states: $\mathcal{L}_{\mathrm{BC}}(\theta)=-\frac{1}{NT}\sum_{t=0}^{T-1}\sum_{i=1}^{N}\log\pi_{\theta}(\hat{a}_{t}^{i}\mid o_{<t}),$ where $N$ represents the number of controlled agents.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Closed-loop supervised fine-tuning and CatK", "weight": 1.0} -->

CAT-K is highly effective in achieving this goal for traffic simulation, but is limited when applied to E2E driving, due to the assumptions of deterministic dynamics and known inverse dynamics to construct recovery action targets, and it's reliance on single-step, discrete policies to efficiently compute the top-K operator.

<!-- chunk {"id": "body-0026", "role": "body", "section": "model", "weight": 1.0} -->

SMART-tiny RoaD (ours) Table 1: WOSAC leaderboard for traffic simulation comparing CL-SFT approaches. RMM stands for Realism Meta Metric, the key metric used for ranking. RoaD fine-tuning significantly improves over the base model (SMART-tiny), it outperforms a much larger model from the same model family (SMART-large), and it is on par with the SOTA CL-SFT method, CAT-K.

<!-- chunk {"id": "body-0027", "role": "body", "section": "model", "weight": 1.0} -->

WOSAC local val. split SMART-tiny base model SMART-tiny base model (from) Table 2: Ablation of data collection frequency for traffic simulation, WOSAC 2% validation split. RoaD fine-tuning leads to significant improvement even when closed-loop data is only collected once, achieving similar levels of improvements over the base model as through CAT-K fine-tuning. The more frequently the data is updated the larger the performance gain. Note that results for CAT-K were taken, where likely a different SMART-tiny checkpoint was used as a base model.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Method", "weight": 1.0} -->

1:Input: policy πθ, dataset 𝒟, candidate action set size K, number of rollouts Nroll, number of training steps Ntrain, recovery parameters (δrec, Nrec) 2:Initialize dataset 𝒟gen = {} 4: Start simulation with scenario s0: TE ∼ 𝒟 7: Choose closest to expert (Eq. 5) 9: Use recovery mode output at ← at′ (Eq. 8) 13: Add rollout to dataset 𝒟gen ← (o0: T, a0: T) 16: Update θ with (ot, at) ∼ 𝒟gen and the RoaD loss (Eq. 3) Our goal is a CL-SFT recipe that works with modern E2E driving policies and reduces the covariate shift between open-loop training and closed-loop deployment without requiring a reward function. Our proposed method, rollouts as demonstrations (RoaD), keeps CAT-K's bias-toward-expert idea but removes its main constraints while remaining simple and data-efficient.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Rollouts as demonstrations (RoaD)", "weight": 1.0} -->

The key idea of RoaD is to treat the policy's own expert‑guided, closed‑loop rollouts as additional supervision for fine‑tuning. Formally, let $\mathcal{R}_{{s}^{E}_{0:T}}^{\mathcal{P}}[\pi_{\theta}]$ denote the expert‑guided rollout operator for $\pi_{\theta}$ given the simulator $\mathcal{P}$ and expert (GT) trajectory ${s}^{E}_{0:T}$. We accumulate generated rollouts in a dataset, and fine‑tune the policy by behavior cloning: The expert guidance is designed to produce trajectories that are simultaneously near on‑policy (i.e. sampled from $\pi_{\theta}$), but also higher‑quality than unassisted rollouts. Because this data is collected on-policy, it covers states the policy is likely to encounter, reducing covariate shift between training and deployment.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Rollouts as demonstrations (RoaD)", "weight": 1.0} -->

In practice, $\mathcal{R}_{{s}^{E}_{0:T}}[\pi_{\theta}]$ can be implemented by biasing the policy's output toward the expert continuation, for example using Top‑$K$ selection (Eq. 1) or Sample‑$K$ (see Sec. 4.2).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Rollouts as demonstrations (RoaD)", "weight": 1.0} -->

Crucially, compared to CAT-K, RoaD does not require the construction of target recovery actions which are challenging to construct under stochastic or non-invertible dynamics, and are often low-quality for policies that output future trajectories rather than single-step actions. Instead, it uses the future trajectory itself as the target. In the following, we discuss three further modifications which makes RoaD applicable to E2E driving.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Sample-$K$ expert-guided rollouts", "weight": 1.0} -->

To preserve expert guidance without discrete top-$K$ enumeration, we draw $K$ action candidates from the current policy distribution (e.g., trajectory samples or diffusion/flow-matching draws), and select the candidate closest to the expert continuation under a generalized distance metric (Eq. 6): This Sample-K relaxation maintains the "closest-to-expert" bias while accommodating continuous policy outputs and large vocabularies.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Sample-$K$ expert-guided rollouts", "weight": 1.0} -->

When $a_{t}$ represent trajectories, the distance function $d(\cdot,\cdot)$ can be implemented as a trajectory-level (generalized) distance between predicted trajectories and the future expert trajectory. A concrete choice is a weighted step-wise distance over a comparison horizon $H_{t}$, where $\tilde{s}_{t+k}(a_{t})$ denotes the predicted state at step $t+k$ implied by action $a_{t}$, and $w_{k}\!\geq\!0$ are arbitrary weights.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Recovery-mode policy output", "weight": 1.0} -->

E2E driving policies often exhibit limited action diversity as they are trained to drive safely and predictably, preventing naive sampling from reliably producing a candidate near the expert. To address this, we introduce an optional recovery-mode policy output that nudges the policy toward the expert when all sampled actions are too far from the expert.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Recovery-mode policy output", "weight": 1.0} -->

Concretely, when the chosen action $a_{t}$ is a trajectory, we linearly interpolate between $a_{t}$ and the expert continuation, acting as guidance rather than a discrete override. Let the prediction horizon be $F$. We reuse the notation $\tilde{s}_{t+k}(a_{t})$ from Eq. 6 to denote the predicted state at step $t+k$ implied by $a_{t}$. Recovery is triggered when the generalized distance to the expert exceeds a threshold: Upon triggering, we define a weight vector $\lambda\in^{F}$ (e.g., a linear schedule $\lambda_{k}=\min(1,k/N_{\text{rec}})$) and blend the trajectories as which defines the recovery trajectory $a^{\prime}_{t}$. The weight vector $\lambda$ subsumes all parameters of the schedule; in practice we use a simple linear ramp over the first $N_{\text{rec}}$ steps.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Recovery-mode policy output", "weight": 1.0} -->

Fine-tuning with RoaD (ours) Fine-tuning with re-rendered expert trajectories Continued large-scale training with BC Base model pre-trained with BC Table 3: End-to-end simulation results over the AV NuRec dataset. RoaD fine-tuning significantly increases the driving score, and it outperforms both continued open-loop training with real data, as well as fine-tuning with re-rendered expert trajectories.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Recovery-mode policy output", "weight": 1.0} -->

RoaD (no expert guidance) RoaD (3 rollouts, default) RoaD (fine-tune once, default) RoaD (fine-tune twice) RoaD (4.2k steps, default) Table 4: Ablation study for E2E driving. The setting is identical to the main experiments apart from the ablated property. steps refer to the number of optimization steps for fine-tuning. K denotes the number of trajectory samples for expert-guided rollouts. Results indicate that both expert guidance and recovery mode are important in the algorithm; and performance gains are observed over a wide range of hyperparameters.

<!-- chunk {"id": "body-0038", "role": "body", "section": "CL-SFT with off-policy data", "weight": 1.0} -->

CAT-K regenerates rollouts at each gradient step, which is feasible in BEV traffic simulation, but prohibitive for E2E driving due to the high cost of rendering sensor inputs. To reduce this collection cost, we evaluate reusing the same rollout dataset across multiple optimization steps, similar to a replay buffer in off-policy RL, including the extreme case of generating only a single dataset at the start of fine-tuning. Empirically, we find that rollout data reuse incurs only small degradation, making RoaD practical when high‑fidelity rollouts are expensive to obtain.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiments", "weight": 1.0} -->

We validate our method for traffic simulation on the WOSAC benchmark, and for E2E driving using the AlpaSim simulator and the NVIDIA Physical AI - AV NuRec Dataset.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Traffic simulation", "weight": 1.0} -->

We first validate RoaD for traffic simulation using the WOSAC benchmark. Note that our primary goal here is not to outperform CAT-K, but to show that the simplified RoaD approach can achieve comparable performance to CAT-K while also being applicable to E2E driving due to fewer restrictive assumptions.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

We follow the experimental setup of and use RoaD to fine-tune the SMART-tiny model on the WOMD dataset. The model receives 1 second of trajectory history for all agents, it outputs delta x-y actions, and at test time it is rolled out for 8 seconds with 0.1s time steps. Note that for this experiment we do not use the recovery mode as traffic models are naturally diverse enough.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

Metrics. Evaluation follows the WOSAC protocol. For each scenario, we generate 32 rollouts for all agents in the scene and compare the resulting joint behavior distribution to human driven trajectories. We report the following metrics which, excluding minADE, measure the distributional similarity between the policy and the data. The principal metric on the leaderboard is Realism Meta Metric (RMM), which combines three distributional metrics: kinematic metrics, e.g. velocities and accelerations; interactive metrics, e.g., collisions; and map-based metrics, e.g. off-road driving. For the exact definition of the metrics we refer to. Additionally we also report minADE, i.e., minimum Average Displacement Error, a widely used metric for trajectory prediction.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Results", "weight": 1.0} -->

Main results on WOSAC. Tab. 1 provides results on the public WOSAC leaderboard. RoaD fine-tuning significantly improves over the base model (SMART-tiny), it outperforms a much larger model from the same model family (SMART-large), and it is on-par with the SOTA CL-SFT method, CAT-K. We note that multiple works on the leaderboard, concurrently developed with ours, such as SMART-R1 achieve higher RMM using a combination of CL-SFT with CAT-K, and RL fine-tuning. However, these approaches require highly specialized rewards derived from the WOSAC evaluation metrics, and a large number of environment interactions, making them unsuitable for E2E driving. A snapshot of the complete leaderboard at the time of submission is included in the Appendix.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Results", "weight": 1.0} -->

Re-using CL experience. To assess the effect of reusing previously generated CL-SFT data, we ablate the data refresh frequency in Tab. 2, evaluating locally on 2% of the WOMD validation set following. As expected, more frequent refreshes yield higher performance, though the incremental gains are modest. Importantly, even when closed-loop data is generated only once at the start of fine-tuning, RoaD already delivers a substantial improvement. Given the high cost of data rendering, this motivates our default E2E setup (Sec. 5.2) of generating CL-SFT data only once. For completeness, we also ablate repeated data generation and observe additional, albeit smaller, improvements in the E2E experiment.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Results", "weight": 1.0} -->

Local scene set Re-rendered expert trajectories Table 5: Sim2sim transfer results. Policies are fine-tuned with 3DGS generated data, and evaluated in previously unseen 75 scenarios reconstructed either as 3DGS (default setting) or as a NeRF (sim2sim transfer). As expected, performance reduces when transferring fine-tuned policies to a new simulation environment, but fine-tuning with RoaD improves over the base model even in the transfer setting.

<!-- chunk {"id": "body-0046", "role": "body", "section": "End-to-end driving", "weight": 1.0} -->

Our main result is that CL-SFT with RoaD can significantly improve closed-loop performance in E2E driving.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

End-to-end VLA policy We employ a VLA-based policy structured similar to. The policy takes in 1.6s ego motion history, and a sequence of timestamped images from two onboard cameras (front facing wide-angle and tele camera), and generates 6.4s trajectory sample output, which is then tracked by a downstream controller when executed in closed-loop. The policy is trained with a large-scale dataset comprising of 20,000 hours of human driving data from 25 countries, covering a variety of scenarios including highway and urban driving, weather conditions, day and night times. A 1700+ hour subset of this dataset is publicly available.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

Simulation environment. For E2E driving experiments, we employ AlpaSim, a closed-loop simulator built on SOTA neural scene reconstruction. The system reconstructs real-world driving logs as temporal 3D Gaussian Splatting (3D-GS) scenes and renders novel camera views when the ego vehicle diverges from the recorded path. We employ custom controllers that track predicted trajectories with separate lateral and longitudinal control, using a 200 ms control delay and ego-motion noise. The vehicle dynamics is governed by a dynamically extended bicycle model. The controller, control delay and dynamics model are designed to imitate real-word driving as closely as possible. All other traffic participants, including vehicles and pedestrians, replay their logged trajectories. Qualitative examples from AlpaSim are shown in Fig. 4.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

Fine-tuning. To fine-tune the VLA policy we generate 20s long simulated CL data using 8251 3D-GS scenes reconstructed from real-world driving logs, 3x rollouts per scene by default. We fine-tune for 4.2k steps (approximately one epoch of non-overlapping trajectory data) with frozen encoders to mitigate overfitting to visual artifacts.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

Pre-trained VLA policy RoaD fine-tuned VLA policy Figure 4: Qualitative comparison of policy rollouts in our E2E simulator. Top row: before fine-tuning, the policy navigates this intersection poorly, ends up in a wrong lane and fails to avoid a collision with a stationary vechicle. Bottom row: after fine-tuning with RoaD, the policy handles the intersection correctly and avoids any collision.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

Metrics To evaluate models, we use 920 openly accessible challenging 3D-GS scenes from the NVIDIA Physical AI - AV NuRec Dataset, and generate 3 rollouts per scenes. In Tabs. 3, 4 and 5, mean values are computed over all scenes and rollouts, standard deviations are computed by taking the mean across scenes and computing the standard deviation across rollouts, estimating the evaluation uncertainty. The standard deviation over the full RoaD training, including data generation, fine-tuning, and evaluation with three rollouts per scene, is too expensive to perform for every model. For the driving score of our main result in Tab. 3 we found it to be $\pm 0.0057$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

We report the following metrics. The driving score measures the average distance traveled (in kilometers) between incident events, where an incident corresponds to either off-road driving or a collision. The collision rate denotes the proportion of scenarios in which the ego vehicle is involved in a close encounter or collision for which it is deemed responsible, i.e., excluding rear-end and side contacts. The off-road rate captures the fraction of scenarios where the ego vehicle leaves the drivable area; this value appears relatively high because in the AV NuRec Dataset only the region bounded by lane markings is considered drivable. Finally, the distance traveled denotes the distance traveled by the ego vehicle in meters.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

Each simulation terminates after the first incident. Evaluation in reconstructed scenes is inherently sensitive to rendering artifacts, particularly when the ego vehicle diverges from the logged path. To reduce the impact of such artifacts, we exclude any events where the ego deviates by more than 4 m from the original trajectory. Nonetheless, a portion of recorded incidents remain attributable to visual artifacts or imperfect scene reconstructions.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Results", "weight": 1.0} -->

Main results. The main results for E2E driving are reported in Tab. 3. RoaD fine-tuning increases the driving score in previously unseen scenarios by 41% and reduces collisions by 54%. RoAD outperform fine-tuning with expert demonstrations re-rendered in the same simulation environment, indicating that the performance gains of RoaD are not only from adjusting to simulation artifacts. RoaD also outperforms continued large-scale open-loop training using real-world driving data, indicating that the performance gains are not simply due to further training steps. Fig. 4 shows a qualitative example: while the base policy encounters a collision, after fine-tuning with RoaD, the policy handles the intersection correctly without collision.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Results", "weight": 1.0} -->

Ablation studies. Ablation results in Tab. 4 indicate that both expert guidance during rollouts and recovery-mode policy outputs are important for best performance in E2E driving. Furthermore, RoaD is not strongly sensitive to its hyperparameters, including the number of rollouts generated per scene, re-collecting CL data and further fine-tuning the policy, changing the number of optimization steps used for fine-tuning, or the number of trajectory samples ($K$) during CL data generation. In all alternative settings, RoaD improves upon the base model. While some hyper-parameter choices can further increase performance, in particular, increasing $K$ and re-collecting CL data for additional fine-tuning, these also increase the computational costs of RoaD. On the other hand, we found that fine-tuning for too many optimization steps can slightly reduce performance, likely due to a lack of co-training with the original large-scale training data in our experiments.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Results", "weight": 1.0} -->

Data scaling. Given the high cost of scene reconstruction for E2E CL-SFT (i.e. generating 3D-GS artifacts), scalability of RoaD with the number of rollouts per scene is an important question. To this end, in Fig. 3 we vary the number of rollouts generated per scene for CL-SFT. RoaD performance improves monotonically as more rollouts are added to its SFT dataset, while fine-tuning with re-simulated expert demonstrations cannot make use of multiple rollouts.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Results", "weight": 1.0} -->

Sim2sim transfer. Finally, in our experiments so far we have generated CL fine-tuning data in the same simulation environment where the policy is evaluated. Given a gap between simulation and the real-world, the policy may overfit to artifact of the simulation and in turn it may degrade in real-world deployment. While addressing sim2real gap is not in the scope of this work, to shed some light on this issue, we perform a sim2sim transfer experiment, where the policies are fine-tuned with 3DGS generated data, and evaluated in either 3DGS (default setting) or NeRF reconstructions (sim2sim transfer). For this experiment, we use an in-house scenarios set consisting of 75 scenarios cureted for dense ego-agent interactions. Results are reported in Tab. 5. As expected, performance reduces when transferring fine-tuned policies to a new simulation environment, but fine-tuning with RoaD improves over the base model even in the transfer setting, indicating that RoaD has potential to improve real-world driving performance, despite possible sim2real gaps.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We presented RoaD, a simple closed-loop supervised fine-tuning (CL-SFT) method that treats the policy's own expert-guided rollouts as additional demonstrations. By avoiding discrete recovery targets and introducing a lightweight recovery mode, RoaD removes key assumptions that limit prior CL-SFT approaches and makes the recipe applicable to modern E2E driving policies, allowing closed-loop training without the need for reward functions.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Across vectorized traffic simulation and high-fidelity E2E driving, RoaD consistently improves closed-loop performance over strong baselines. Because RoaD can achieve substantial improvements even when closed-loop data is only collected once, it is a promising, data-efficient, approach for training E2E driving policies in closed-loop.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Limitation of all CL-SFT approaches include the reliance of a pre-trained policy with sufficiently high performance, the assumption that the expert trajectory remains good behavior despite small deviations by the actor, and a distance metric for expert-guided rollouts. Further, our method relies on a high-fidelity simulator such as AlpaSim. Results on sim2sim transfer suggest that RoaD has potential to improve real-world driving performance, despite possible sim2real gaps. Future work may more explicitly address sim-to-real transfer and reduce overfitting to simulation, e.g., by co-training on simulated and real images, or introducing feature similarity bottlenecks.
