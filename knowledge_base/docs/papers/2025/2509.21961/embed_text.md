<!-- arxiv-full-text:v1 {"arxiv_id": "2509.21961", "source": "arxiv-html"} -->

## Introduction

Trajectory planning in autonomous driving requires both safety and efficiency. Traditional planners rely on rule-based methods like model predictive control, graph or sampling-based methods, which are interpretable and safety-driven but often fail in complex, real-world conditions. Recent learning-based planners learn policies from data, capturing nuanced human driving behaviors, and can rival classical systems on large-scale benchmarks.

Despite progress, challenges remain. Real driving data exhibits long-tailed distributions, where common behaviors like lane-following dominate while rare but safety-critical cases are underrepresented. This imbalance biases planners toward frequent patterns, reducing reliability in corner cases. Moreover, dataset bias and limited diversity lead to poor generalization---especially in dynamic traffic scenarios unseen during training.

Generative models provide a promising solution. Diffusion models generate trajectories via iterative denoising and can model multi-modal behaviors, but often require many steps or careful guidance for feasibility. Flow matching offers an alternative generative paradigm. Instead of iterative denoising, it trains a continuous transformation mapping a simple prior directly to the data distribution. This enables fast, few-step sampling, while preserving the ability to model multi-modal behaviors.

Motivated by the need for diverse yet fast trajectory generation, we propose *FlowDrive*, a flow-matching planner for autonomous driving. Unlike diffusion planners that produce trajectories via many denoising steps, FlowDrive learns a continuous motion flow that directly transforms random initial noise into diverse driving trajectories, yielding faster sampling. We also observe that naively training such a planner on a standard driving dataset can lead to biased behavior, and the model may overfit to the most common scenarios and neglect underrepresented but critical cases. To address this, we analyze how data imbalance in the training set affects planning performance and introduce a data balancing method that increases the coverage of rare behaviors. Furthermore, we introduce a mechanism to steer FlowDrive's output trajectories in order to systematically diversify the generated candidates. Finally, we evaluate FlowDrive on the nuPlan benchmark and interPlan benchmark.

In summary, the contributions of this paper are: We identify the impact of unbalanced training data on planning performance and propose a data-balancing strategy to improve robustness to rare scenarios. Furthermore, we present FlowDrive, a flow-matching trajectory planner that efficiently generates feasible driving trajectories for autonomous vehicles.

We introduce a guidance mechanism that steers FlowDrive's outputs to produce more diverse trajectory samples. This enables state-of-the-art performance on the nuPlan and interPlan benchmarks, outperforming previous rule-based, learning-based and hybrid baselines.

## Related work

### Learning-based planning methods

Imitation learning directly trains models to mimic expert driving. Cheng et al. show that careful architecture design and augmentation improve closed-loop performance. Cheng et al. propose PLUTO, which adds contrastive learning and data augmentation, surpassing rule-based planners on nuPlan. These works demonstrate that imitation learning can be competitive, but such planners often struggle in rare or unseen scenarios.

Reinforcement Learning (RL) offers an alternative. Zhang et al. introduce CarPlanner, a consistent autoregressive RL planner that stabilizes training and surpasses imitation methods. Tang et al. propose Plan-R1, which combines pre-training on expert data with RL fine-tuning using rule-based rewards, achieving strong results. However, RL methods often rely on carefully designed reward functions and substantial training to achieve strong performance.

### Data balancing for learning-based planners

Recent works have begun to address the problem of data imbalance. Wang et al. propose SafeFusion, which clusters trajectory "vocabularies" and applies balanced sampling with adaptive loss weighting to mitigate the skew between collision and non-collision cases. Similarly, Parekh et al. tackle imbalance in behavior cloning, showing that conventional weighting biases policies toward frequent behaviors while neglecting rare but critical ones, and propose meta-gradient reweighting to improve policy robustness. In this work, we introduce a cluster-based trajectory reweighting strategy applicable to imitation-learning-based planner.

### Diffusion and flow-based models for planning

Diffusion models are widely applied for trajectory generation. Zheng et al. combine prediction and planning in a transformer-based diffusion framework. Liao et al. introduce DiffusionDrive, a diffusion planner that generates multimodal trajectories with truncated Gaussian priors. Yang et al. propose Diffusion-ES, combining diffusion with evolutionary search to optimize trajectories under arbitrary rewards. These works highlight diffusion's flexibility, but also its sampling overhead and reliance on external guidance.

Flow matching avoids iterative denoising with many steps and was originally introduced for realistic image generation. In planning, Xing et al. propose GoalFlow, a goal-conditioned flow matching planner that is integrated into an end-to-end autonomous driving pipeline and focuses on goal-oriented guidance. Nguyen et al. extend flow matching to second-order planning, yielding smoother motions in robotic manipulation tasks. However, flow matching remains largely underinvestigated for trajectory planning and deserves further exploration.

### Guidance for generative models

Guidance is crucial for controlling generative models. In vision, classifier-based and classifier-free guidance steer diffusion sampling toward desired attributes with higher fidelity. In driving, Zheng et al. use a trajectory score model to guide diffusion toward safe plans. Yang et al. apply black-box reward guidance for high-reward trajectories. Xing et al. adapt guidance for flow matching, conditioning trajectories on goal points. Inspired by these works, we introduce a simple method to guide flow matching trajectories in terms of diversity in planning.

## Methodology

We formulate trajectory planning as conditional generative modeling. Given a scene context ${\bm{c}}$ encoding the High-Definition map, real-time traffic light information, static objects and dynamic agents, we aim to draw a feasible and diverse future trajectory ${\bm{x}}$ for the ego vehicle. We represent the trajectory as a vector in $\mathbb{R}^{D}$ (later instantiated as $H$ waypoints, flattened to a vector). FlowDrive learns a time-dependent velocity field ${\bm{v}}_{{\bm{\theta}}}(t,{\bm{x}},{\bm{c}})$ that transports a simple base distribution $p_{0}$ (e.g., Gaussian over trajectory dimensions) to the conditional data distribution $p_{\rm data}({\bm{x}}\mid{\bm{c}})$ by integrating an ordinary differential equation (ODE). We build on flow matching and rectified flow, which enable straight probability paths and thus fast, few-step sampling.

FlowDrive contains three orthogonal components: (i) a conditional flow-matching planner trained with a rectified path, yielding feasible trajectories; (ii) a data balancing scheme that mitigates long-tail biases in driving datasets; and (iii) an inference-time moderated guidance mechanism that steers samples to increase diversity. We now summarize rectified flow preliminaries in Section 3.1 and later introduce other parts.

### Preliminaries: rectified flow and flow matching

Let ${\bm{x}}\in\mathbb{R}^{D}$ denote a data sample (a trajectory) and ${\bm{c}}$ the conditioning context. Let ${\bm{z}}\sim p_{0}$ be a base sample, with $p_{0}=\mathcal{N}({\bm{0}},{\bm{I}})$. Rectified flow (RF) defines a linear, "rectified" path between ${\bm{z}}$ and ${\bm{x}}$: This path induces a family of intermediate distributions $p_{t}(\cdot\mid{\bm{c}})$ connecting $p_{0}$ to $p_{\rm data}(\cdot\mid{\bm{c}})$, governed by the continuity equation with some velocity field ${\bm{v}}^{*}(t,\cdot,{\bm{c}})$: For the rectified path in Equation 1, the target instantaneous velocity along each pair $({\bm{z}},{\bm{x}})$ is constant and equals Flow matching (FM) trains a parametric vector field ${\bm{v}}_{{\bm{\theta}}}(t,{\bm{x}},{\bm{c}})$ to match the target velocity that makes Equation 2 hold along the chosen path. With the rectified path, the standard conditional RF/FM objective samples $t\sim\mathcal{U}$, ${\bm{z}}\sim p_{0}$, forms ${\bm{x}}_{t}$ via Equation 1, and minimizes where $w(t)$ is an optional time-weighting schedule. At inference, samples are generated by integrating the learned probability flow ODE typically with a small number of solver steps thanks to the low curvature of rectified paths. Rectified flow and flow matching are closely related to diffusion models via the probability flow ODE perspective, but avoid simulating stochastic dynamics during training by directly regressing to the target velocity along a chosen path.

In FlowDrive, ${\bm{x}}$ represents the ego-trajectory, ${\bm{c}}$ encodes scene context, and ${\bm{v}}_{{\bm{\theta}}}$ is parameterized by a context encoder and planning decoder. Next, we explain the model architecture of FlowDrive in Section 3.2.

### FlowDrive

Overview. FlowDrive implements the conditional velocity field ${\bm{v}}_{{\bm{\theta}}}(t,{\bm{x}},{\bm{c}})$ in Section 3.1 with an encoder--decoder architecture (Figure 1). The encoder aggregates heterogeneous scene inputs ${\bm{c}}$ into a set of context tokens; the decoder predicts the velocity field over the trajectory sequence, conditioned on time and the encoder tokens. During training, we minimize the rectified flow loss in Equation 4. At inference, we integrate the probability flow ODE in Equation 5 with a small number of flow steps.

Figure 1: FlowDrive architecture. Left: scene inputs (neighbor history, static objects, lanes/routes with traffic lights and speed limits). Middle: encoder with MLP-Mixer branches and multi-head attention fusion. Right: DiT-based decoder with adaptive layer norm conditioning and cross-attention to context, predicting the velocity field across flow steps.

Scene Inputs and Representation. We follow a scene input representation similar to Diffusion Planner. First, all coordinates are in the local ego frame, with the origin at the current ego position and heading aligned with the ego vehicle's heading direction. For a batch of size $B$: neighbor history has shape $[B,P_{n},T_{p},F_{n}]$ with positions, kinematics, and a one-hot agent type; static objects are $[B,P_{s},F_{s}]$; lanes are polylines $[B,P_{\ell},V,F_{\ell}]$ with local geometry, traffic-light signals, route membership and per-lane speed limit features. We denote the full context as ${\bm{c}}$, and the trajectory sample as a sequence of $H$ steps with action dimension $A$ ($A=4$ for $x,y,\cos,\sin$); we flatten ${\bm{x}}\in\mathbb{R}^{H\times A}$ to $\mathbb{R}^{D}$ when referring to Equation 4. Here, $P_{n}$ denotes the number of neighbor agents; $T_{p}$ the length of the neighbor history; $F_{n}$ the neighbor feature dimension; $P_{s}$ the number of static objects; $F_{s}$ the static-object feature dimension; $P_{\ell}$ the number of lane segments; $V$ the number of points per lane segment; $F_{\ell}$ the per-point lane feature dimension.

All the scene inputs are normalized to zero mean and unit variance. During training, we apply data augmentation to the ego states by randomly perturbing the position, heading and velocity. The normalization and augmentation methods are the same as in Zheng et al..

### Encoder

The encoder builds token embeddings for three branches and fuses them: *Neighbors.* Previous works already explored the potential of MLP-Mixer as a lightweight way in modeling spatiotemporal data. Therefore, we use an MLP-Mixer branch that applies token- and channel-mixing MLPs over the temporal dimension and feature channels of each neighbor, followed by average pooling to obtain one token per neighbor. A small type embedding is added.

*Static objects.* A projection MLP maps per-object features to hidden tokens. Empty or invalid objects are masked out.

*Lanes and routes.* Another MLP-Mixer branch encodes lane polylines, where per-point geometry is first projected, then mixed across points and channels. The token is enriched : (i) traffic light embedding; (ii) speed limit embedding; and (iii) a binary embedding representing whether the current lane is part of the global route. We discuss the design choices to fuse the three embeddings in Section A.4.

The MLP and embedding layers will output $N=P_{n}+P_{s}+P_{\ell}$ tokens, each with a fixed hidden dimension size $d$. A positional embedding is added to each token. Tokens are then fused by $L$ layers of multi-head attention blocks with residual MLPs, yielding a set of context tokens ${\mathbf{C}}\in\mathbb{R}^{N\times d}$ and a binary mask for invalid tokens (e.g. agents, lanes).

### DiT Decoder

The decoder uses and extends the Diffusion Transformer (DiT). Given a noised trajectory (or pure noise) ${\bm{x}}_{t}\in\mathbb{R}^{H\times A}$ at time $t$, we embed per-step actions with an MLP, add a learned positional encoding over horizon steps, resulting in $H$ trajectory tokens. We additionally embed the ego state with an MLP to the same embedding space and append the ego state embedding in front of the trajectory tokens. We discuss the reason in Section A.3. Each DiT block uses adaptive LayerNorm-zero (adaLN-Zero) modulation driven by ${\bm{t}}$ and the mean pooling of valid context tokens, then applies: (i) self-attention and an MLP on the trajectory tokens; and (ii) cross-attention to the encoder tokens (keys/values), considering the token mask. The decoder produces ${\bm{v}}_{{\bm{\theta}}}(t,{\bm{x}}_{t},{\bm{c}})\in\mathbb{R}^{(H+1)\times A}$, where the first output token corresponds to the ego state and is ignored during loss computation w.r.t. the target velocity in Equation 3.

### Data balancing

In this paper we use the nuPlan dataset for training, but the balancing strategies below are generic and applicable to any dataset of trajectories and scenes. Prior works report severe skew in driving behavior frequencies (e.g., large amounts of stationary or lane-following samples versus very few rare maneuvers). As an example, on $~10^{6}$ sampled training scenarios from nuPlan dataset, one might observe only $\sim 1$ sampled scenario for changing_lane_with_lead, but $\sim 350{,}000$ samples for a simple stationary scenario. Such imbalance biases a planner toward the frequent modes, undermining robustness in safety-critical cases.

We adopt two complementary sampling strategies, both implemented in our dataset loader.

Figure 2: Precomputed clusters of normalized ego futures used for cluster-based sampling. Colored polylines indicate cluster centers; translucent points show a subset of sampled trajectories per cluster.

Figure 3: Sample counts per cluster after applying different training-time sampling strategies. Cluster-based sampling produces the most balanced distributions over the clusters.

### Scenario-based Sampling

Each training sample is assigned a scenario type (for nuPlan: merging, turning, stopping for traffic lights, changing lane, etc.). We count the frequency of each scenario type across the training set and use inverse-frequency weights to construct a weighted sampler (with normalization) so that underrepresented scenario types are sampled more often. Concretely, if $f_{s}$ is the fraction of samples belonging to scenario type $s$, we define a weight $w_{s}=1/(f_{s}+\varepsilon)$ and normalize $\{w_{s}\}$ to mean 1.0. During training, the dataloader draws indices proportional to these weights.

### Cluster-based Sampling

To directly balance the distribution of ground-truth ego trajectories, we precompute clusters of normalized trajectories over the horizon and then upweight samples from rare clusters. Specifically, we embed each ego trajectory into a fixed-length vector (stacked $x,y$ across time), run k-means to obtain $K=20$ clusters, and store the cluster centers and per-cluster statistics (mean and standard deviation). Figure 2 visualizes the precomputed cluster centers and some randomly sampled trajectories. Given the cluster assignment for each training sample, we compute inverse-frequency weights per cluster, analogous to the scenario-based scheme, and use them in the weighted sampler. This encourages exposure to a wider variety of motion patterns (e.g., strong turns, low and high speeds, or lane changes) during training.

### Effect on Sampling Distribution

Figure 3 compares the number of trajectories drawn per cluster across three settings: no weighted sampling, scenario-based sampling, and cluster-based sampling. Without any weighting, the samples are heavily skewed toward cluster 0 (stationary trajectories). Scenario-based sampling slightly reduces the stationary trajectory frequency, but enhances other frequent clusters (e.g., cluster 4 and 6). In contrast, cluster-based sampling substantially flattens the cluster distribution and increases coverage of rare motion patterns.

We will present an ablation in Section 4.4 comparing these strategies in terms of closed-loop driving score on the nuPlan benchmark.

### Moderated guidance on flow matching trajectories

While FlowDrive achieves strong closed-loop results (see Section 4), we observed that single-pass trajectories can lack lateral diversity in scenes where lateral maneuvers would increase the driving score (see examples in Section A.6). Prior state-of-the-art planners on nuPlan---e.g. the Diffusion Planner and the PDM planner ---therefore apply post-hoc, rule-based lateral offsets on the final trajectories to induce diversity. In contrast, we introduce a *moderated guidance* that injects small, structured perturbation *inside* the flow integration.

### Moderated Guidance

Let the (noised) trajectory state at flow time $t$ be so ${\bm{x}}_{t}\in\mathbb{R}^{H\times 4}$, where $h=1,\dots,H$ indexes the trajectory horizon steps. We operate only on the positional part $\mathbf{p}_{t,h}^{\text{pos}}=(x_{t,h},y_{t,h})$. The orientation components $(\cos\theta_{t,h},\sin\theta_{t,h})$ are left unchanged. Define unit tangent and normal (left-hand) directions w.r.t. the current heading angle of the ego vehicle $\theta$ (one can use the average heading of the lane centerline as well): Let $\mathcal{T}_{g}\subset$ (discrete flow times) be a set of flow times at which guidance is injected. The binary schedule $\alpha(t)=\mathbf{1}\{t\in\mathcal{T}_{g}\}$ activates guidance only at those steps. A monotonically increasing horizon weight $\beta(h)=h/H$ means larger perturbation is injected into later waypoints.

Given lateral and longitudinal magnitudes $\delta_{\text{lat}}$ and $\delta_{\text{lon}}$, the moderated update applied before evaluating the next velocity field in the ODE solver (Equation 5) is which updates ${\bm{x}}_{t}$ to ${\bm{x}}^{\prime}_{t}$. This in-the-loop perturbation lets the learned velocity field subsequently reconcile the guided displacement with scene context, unlike post-hoc shifts. Lateral offsets ($\delta_{\text{lat}}$) promote modal diversity (overtaking, nudging), while longitudinal offsets ($\delta_{\text{lon}}$) can reshape speed profiles. Qualitative examples on joint guidance with lateral and longitudinal offsets are shown in Figure 10 in appendix. From our experiments, longitudinal guidance brought no improvement on closed-loop performance; thus in all experiments we set $\delta_{\text{lon}}=0$ and sample $\delta_{\text{lat}}\in$ (e.g. $[-0.5,-0.25,0,0.25,0.5]$), producing the diverse candidates in Figure 4.

(a) Inject at $\mathcal{T}_{g,1}=\{\tfrac{1}{4}\}$.

(b) Inject at $\mathcal{T}_{g,2}=\{\tfrac{1}{2}\}$.

(c) Inject at $\mathcal{T}_{g,3}=\{\tfrac{3}{4}\}$.

Figure 4: Effect of injecting moderated lateral offsets at different flow steps. Black trajectories are with 0 offset, green trajectories are with offsets [−0.5, −0.25, 0.25, 0.5].

Figure 5: Moderated lateral offsets induce multi-modality. Beyond lane-following green trajectories, guided samples explore safe overtaking when context allows (black).

### Diversity and Multi-modality

Lateral offsets often unlock multi-modal behaviors that are otherwise rare in training data. For instance, in car-following with a slow leading vehicle, small offsets encourage overtake-like solutions if the adjacent lane is free; see Figure 5.

### When to Inject Guidance

We inject guidance only at a single flow time step ($|\mathcal{T}_{g}|=1$), allowing the model to reconcile the perturbation through its learned velocity field at later time steps. Figure 4 compares injecting $\delta_{\text{lat}}$ at early, mid, and late flow steps--- specifically with $\mathcal{T}_{g,1}=\{\tfrac{1}{4}\},\mathcal{T}_{g,2}=\{\tfrac{1}{2}\},\mathcal{T}_{g,3}=\{\tfrac{3}{4}\}$. Early injections enjoy more time for the model to reconcile context, whereas very late injections behave similarly to post-hoc shifts and often violate lane-boundary constraints. Empirically, we found that injecting at $\mathcal{T}_{g,2}=\{\tfrac{1}{2}\}$ offers the best trade-off between diversity and feasibility; this choice is used by default in our experiments.

In contrast to manual post-processing, our guidance approach keeps the model "in the loop", letting scene-conditioning absorb and correct the perturbation.

## Experiments

### Benchmarks and experimental setup

We evaluate FlowDrive on the large-scale nuPlan benchmark and the interaction-focused interPlan benchmark. On nuPlan, we report results on the official and -hard splits in both non-reactive and reactive simulator modes. InterPlan is a closed-loop driving benchmark based on the nuPlan dataset and framework. It modifies original nuPlan scenarios by augmenting agent counts and behaviors so that more intelligent maneuvers become necessary, such as sudden intruding pedestrians and nudging around parked vehicles. Both benchmarks use a composite driving score between 0 and 100 that combines safety, progress, and comfort metrics to evaluate closed-loop performance. All training details and hyperparameters are listed in Section A.2.

We evaluate three variants of our planner. FlowDrive^-^: a purely learning-based variant that executes the trajectory produced by the decoder directly, without weighted sampling or any post-processing. FlowDrive: FlowDrive^-^ with cluster-based sampling. FlowDrive\*: a hybrid variant that applies our moderated guidance during flow integration (Section 3.4) and a light post-processing pass on top of FlowDrive. The post-processing includes: (i) generating 30 candidates using a set of lateral guidance offsets. (ii) trajectory smoothing and enforcing speed limits of each trajectory (explanation given in Section A.3). (iii) scoring them with the rule-based scorer from PDM planner, and executing the top-scoring plan. We provide ablation study of the number of candidates on driving scores in Section A.4.

### Baselines

We compare against representative rule-based, learning-based, and hybrid planners (with rule-based post-processing). FlowDrive\* is as a hybrid variant. IDM: the classical Intelligent Driver Model for longitudinal car-following and collision avoidance. PDM-Planner: a modular policy decomposition planner with hand-crafted rules and model-based pathing, provided as a strong rule-based baseline in nuPlan. GameFormer: a transformer-based planner that models multi-agent interactions with game-theoretic inductive bias for safe decision making. PlanTF: a transformer planner that formulates planning as sequence modeling with end-to-end training on expert demonstrations. PLUTO: an imitation-learning planner enhanced with contrastive learning and augmentations that achieves strong closed-loop scores on nuPlan. Diffusion Planner: a transformer-based diffusion generative planner that denoises trajectories under flexible guidance.

### Quantitative results

Table 1 presents the quantitative results. Without data balancing, FlowDrive^-^ still outperforms previous learning-based planners in almost all columns. With cluster-based sampling, FlowDrive surpasses them by noticeable margins. Remarkably, despite using no post-processing, its scores are very close to the strong hybrid baselines PDM-Hybrid and PLUTO. Adding moderated guidance and post-processing (FlowDrive\*) then pushes performance further to the top, achieving state-of-the-art across nearly all columns among all planner categories. Note that the scores are mostly extracted from previous publications. On interPlan, we compute the scores for each baseline using the official code if available. More qualitative results are presented in Section A.6.

Diffusion Planner w/ refine.

Table 1: Closed-loop scores on nuPlan, -hard, and (Non-Reactive, NR; Reactive, R) and interPlan. Higher is better. Within each category block, best is bold; second-best is underlined. A dash “–” indicates the result is unavailable or not reproducible due to missing code.

### Ablation studies

### Ablation on Data Balancing Methods

We compare the three sampling strategies on nuPlan (R). As shown in Table 2(a), scenario-label imbalance is not the main bottleneck: reweighting by scenario type performs worse than no weighting (FlowDrive^-^), while balancing by trajectory pattern (FlowDrive) yields the largest improvement. We present more detailed scores on different scenarios on (R) comparing FlowDrive^-^ and FlowDrive in Table 5.

Inference flow steps (b) Training and inference flow steps Table 2: Ablation studies on nuPlan (R). Best is bold.

### Ablation on Flow Training and Inference Steps

We use Euler ODE solver to discretize flow time steps. We train three FlowDrive models with varying training flow steps, all with cluster-based sampling method, and apply different number of flow steps at inference (Table 2(b)). We find that using 2k flow steps at training and 8 flow steps at inference gives the best result, which achieves runtime of 40 milliseconds per inference pass on a single NVIDIA GeForce RTX 2080 Ti GPU. To compare, the Diffusion Planner has a inference time of 50 milliseconds with 10 diffusion steps. With batching, generating 30 trajectories with guidance offsets increases the runtime only to 43 milliseconds. More ablation studies are presented in Section A.4.

## Conclusion and discussions

We introduced FlowDrive, a conditional flow-matching planner that generates trajectories efficiently via a learned rectified flow. Two components enable its strong performance: (i) cluster-based data balancing that reweights training samples by ego-trajectory pattern, increasing the coverage of rare motion modes; and (ii) moderated, in-the-loop guidance that systematically expands diversity while keeping the trajectories scene-consistent. On nuPlan and interPlan, FlowDrive outperforms all previous learning-based methods by large margins. With moderated guidance and light post-processing (FlowDrive\*), it achieves new state-of-the-art across nearly all benchmark splits while remaining efficient.

Future work will investigate the jerky raw trajectories from FlowDrive and try to develop improved smoothness constraints during flow matching training. We will further explore richer learned guidance signals encoding safety or intent, steering with control vectors and RL fine-tuning with Flow Matching Policy Gradients or ReinFlow to shift the velocity field toward regions producing higher efficiency, comfort, and safety.
