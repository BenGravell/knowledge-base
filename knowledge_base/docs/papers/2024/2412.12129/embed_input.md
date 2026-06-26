<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

SceneDiffuser: Efficient and Controllable Driving Simulation Initialization and Rollout

Topics include Driving simulation, Diffusion models, Traffic simulation, Scene generation, Closed-loop simulation, Autonomous driving, Controllable generation, World models.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents SceneDiffuser, a diffusion-based scene-level prior for both traffic-scene initialization and closed-loop rollout. Its amortized denoising scheme lowers inference cost while generalized hard constraints and language-guided constraints make generated driving scenarios more controllable.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Realistic and interactive scene simulation is a key prerequisite for autonomous vehicle (AV) development. In this work, we present SceneDiffuser, a scene-level diffusion prior designed for traffic simulation. It offers a unified framework that addresses two key stages of simulation: scene initialization, which involves generating initial traffic layouts, and scene rollout, which encompasses the closed-loop simulation of agent behaviors. While diffusion models have been proven effective in learning realistic and multimodal agent distributions, several challenges remain, including controllability, maintaining realism in closed-loop simulations, and ensuring inference efficiency. To address these issues, we introduce amortized diffusion for simulation. This novel diffusion denoising paradigm amortizes the computational cost of denoising over future simulation steps, significantly reducing the cost per rollout step (16x less inference steps) while also mitigating closed-loop errors. We further enhance controllability through the introduction of generalized hard constraints, a simple yet effective inference-time constraint mechanism, as well as language-based constrained scene generation via few-shot prompting of a large language model (LLM). Our investigations into model scaling reveal that increased computational resources significantly improve overall simulation realism.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We demonstrate the effectiveness of our approach on the Waymo Open Sim Agents Challenge, achieving top open-loop performance and the best closed-loop performance among diffusion models.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Simulation environments allow efficient and safe evaluation of autonomous driving systems. Simulation involves initialization (determining starting conditions for agents) and rollout (simulating agent behavior over time), typically treated as separate problems. Inspired by diffusion models' success in generative media, such as video generation and video editing (inpainting, extension, uncropping etc.), we propose SceneDiffuser, a unified spatiotemporal diffusion model that addresses both initialization and rollout for autonomous driving, trained end-to-end on logged driving scenes. To our knowledge, SceneDiffuser is the first model to jointly enable scene generation, controllable editing, and efficient learned closed-loop rollout (Fig. 1).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

One challenge in simulation is evaluating long-tail safety-critical scenarios. While data mining can help, such scenarios are often rare. We address this by learning a generative scene realism prior that allows editing logged scenes or generating diverse scenarios. Our model supports scene perturbation (modifying a scene while retaining similarity) and agent injection (adding agents to create challenging scenarios). We also enable synthetic scene generation on roadgraphs with realistic layouts. We design a protocol for specifying scenario constraints, enabling scalable generation, and demonstrate how a few-shot prompted LLM can generate constraints from natural language.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Given a scene, realistically simulating agents and AV behavior is challenging. Unlike motion prediction tasks where entire future trajectories are jointly predicted in a single inference, simulator predictions are iteratively fed back into the model, requiring realism at each step. This poses challenges: distributional drift from compounding errors, high computational cost for models like diffusion, and the need to simulate various perception attributes realistically.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose Amortized Diffusion for simulation rollout generation, a novel approach for amortizing the cost of the denoising inference over a span of physical steps that effectively addresses the challenges of simulation realism due to closed-loop drift and inference efficiency. Amortized diffusion iteratively carries over prior predictions and refines them over the course of future physical steps (see Sec. 3.2 and Fig. 4). This allows our model to produce stable, consistent, and realistic simulated trajectories, while requiring only a single denoising function evaluation at each physical step while jointly simulating all perception attributes at each step. Experiments show that Amortized Diffusion not only requires 16x less model inferences per step, but is also significantly more realistic.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, SceneDiffuser's main contributions are: A unified generative model for scene initialization and rollout, jointly learning distributions for agents, timesteps, and perception features including pose, size and type.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

A novel amortized diffusion method for efficient and realistic rollout generation, significantly improving trajectory consistency and reducing closed-loop error.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Controllable scene initialization methods, including log perturbation, agent injection, and synthetic generation with a novel hard constraint framework and LLM.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Investigation of model scaling, showing increased compute effectively improves realism.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Demonstration of effectiveness on the Waymo Open Sim Agents Challenge, achieving top open-loop performance and the best closed-loop performance among diffusion models.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Data-driven Agent Simulation", "weight": 1.0} -->

A variety of generative models have been explored for scene initialization and simulation, including autoregressive models, cVAEs, cGANs, and Gaussian Mixture Models (GMMs). For closed-loop rollouts, these models have been extended with GMMs, GANs, AR models over discrete motion vocabularies, cVAE, and deterministic policies. Open-loop rollouts have also been explored using cVAE.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Diffusion Models for Agent Simulation", "weight": 1.0} -->

Open-loop Sim Open-loop simulation generates behavior for agents that all lie within one's control, i.e. does not receive any external inputs between steps. Open-loop simulation thus cannot respond to an external planner stack (AV), the evaluation of which is the purpose of simulation. Diffusion models have recently gained traction in multi-agent simulation, particularly in open-loop scenarios (multi-agent trajectory forecasting), using either single-shot or autoregressive (AR) generation. Single-shot approaches employ spatiotemporal transformers in ego-centric or scene-centric frames with motion/velocity deltas. Soft guidance techniques enhance controllability. DJINN uses 2d condition masks for flexible generation.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Diffusion Models for Agent Simulation", "weight": 1.0} -->

Closed-loop Sim Closed-loop simulation with diffusion remains challenging due to compounding errors and efficiency concerns. Chang *et al.* explore route and collision avoidance guidance in closed-loop diffusion, while VBD combines denoising and behavior prediction losses with a query-centric Transformer encoder. VBD found it computationally infeasible to replan at a 1Hz frequency in a receding horizon fashion over the full WOSAC test split due to the high diffusion inference cost, therefore testing in open-loop except over 500 selected scenarios.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Diffusion Models for Agent Simulation", "weight": 1.0} -->

Initial Condition Generation Diffusion-based initial condition generation has also been studied. Pronovost *et al.* adapt the LDM framework to rendered scene images, while SLEDGE and DriveSceneGen diffuse initial lane polylines, agent box locations, and AV velocity.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Diffusion for Temporal World Modeling and Planning", "weight": 1.0} -->

Outside of the autonomous driving domain, diffusion models have proven effective for world simulation through video and for planning. Various diffusion models for 4d data have been proposed, often involving spatiotemporal convolutions and attention mechanisms. In robotics, diffusion-based temporal models leverage Model Predictive Control (MPC) for closed-loop control and have shown state-of-the-art performance for imitation learning.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Diffusion for Temporal World Modeling and Planning", "weight": 1.0} -->

Similar to our Amortized Diffusion approach, TEDi proposes to entangle the physical timestep and diffusion steps for human animation, thereby reducing $O{({T \cdot \mathcal{T}})}$ complexity for $\mathcal{T}$ physical timesteps and $T$ denoising steps to $O{(\mathcal{T})}$. However, we are the first work to demonstrate the effectiveness of this approach for reducing closed-loop simulation errors, and the first to extend it to a multi-agent simulation setting.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Scene Diffusion Setup", "weight": 1.0} -->

We denote the scene tensor as ${\mathbf{x}} \in {\mathbb{R}}^{A \times \mathcal{T} \times D}$, where $A$ is the number of agents jointly modeled in the scene, $\mathcal{T}$ is the total number of modeled physical timesteps, and $D$ is the dimensionality of all the features that are jointly modeled. We learn to predict the following attributes for each agent: positional coordinates $x,y,z$, heading $\gamma$, bounding box dimensions $l,h,w$, and object type $k \sim {\{\text{AV, car, pedestrian, cyclist}\}}$. We model all tasks considered in SceneDiffuser as multi-task inpainting on this scene tensor.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Scene Diffusion Setup", "weight": 1.0} -->

Given an inpainting mask $\overline{\mathbf{m}} \in {\mathbb{B}}^{A \times \mathcal{T} \times D}$, the corresponding inpainting context values $\overline{\mathbf{x}}:={\overline{\mathbf{m}} \odot {\mathbf{x}}}$, a set of global context $\mathbf{c}$ (such as roadgraph and traffic signals), and a validity mask for a given agent at a given timestep $\overline{\mathbf{v}} \in {\mathbb{B}}^{A,\mathcal{T}}$ (to account for there being $< A$ agents in the scene or for occlusion), we train a diffusion model to learn the conditional probability $p{(\left.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Scene Diffusion Setup", "weight": 1.0} -->

Feature Normalization To simplify the diffusion model's learning task, we normalize all feature channels before concatenating them along $D$ to form the scene tensor. We first encode the entire scene in a scene-centric coordinate system, namely the AV's coordinate frame just before the simulation commences. We then scale $x,y,z$ by fixed constants, $l,h,w$ by their standard deviation, and one-hot encode $k$. See Appendix A.6 for more details. This simple yet generalizable process allows us to jointly predict float, boolean, and even categorical attributes by converting into a normalized space of floats. After generating a scene tensor $\mathbf{x}$, we apply a reverse process to obtain the generated features.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Scene Diffusion Setup", "weight": 1.0} -->

Scene Diffusion Tasks Different tasks are fomulated as inpainting problems (Fig. 2).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Scene Diffusion Setup", "weight": 1.0} -->

*Scene Generation (SceneGen)*: Given the full trajectory of some agents, generate the full trajectory of other agents. We have ${\overline{\mathbf{m}}}_{\text{scenegen}} \in {\mathbb{R}}^{A,1,1}$ (broadcastable to $\mathcal{T}$ timesteps and $D$ features), where ${\overline{\mathbf{m}}}_{\text{scenegen, a}} \sim {Pr{({X = {A_{\text{select}}/A_{\text{valid}}}})}}$, where $A_{\text{select}} \sim {\mathcal{U}{(0,A_{\text{valid}})}}$ is the number of agents sampled to be selected as inpainting conditions out of $A_{\text{valid}}$ valid agents in the scene.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Scene Diffusion Setup", "weight": 1.0} -->

*Behavior Prediction (BP)*: Given past and current data for all agents, predict the future for all agents. We have ${\overline{\mathbf{m}}}_{\text{bp}} \in {\mathbb{R}}^{1,\mathcal{T},1}$ (broadcastable to $A$ agents and $D$ features), where ${\overline{\mathbf{m}}}_{\text{bp},\tau} = {\mathcal{I}{({\tau < \mathcal{T}_{history}})}}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Scene Diffusion Setup", "weight": 1.0} -->

*Conditional SceneGen and Behavior Prediction*: Both scenegen and behavior prediction masks are multiplied by a control mask at training time to enable controllable scenegen and controllable behavior prediction at inference time.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Scene Diffusion Setup", "weight": 1.0} -->

This allows us to condition on certain channels, such as positions $x,y$ with or without specifying other features such as type and heading.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Scene Diffusion Setup", "weight": 1.0} -->

Architecture We present a schematic for the SceneDiffuser architecture in Fig. 3, consisting of two end-to-end trained models: a global context encoder and a transformer denosier backbone. Validity $\overline{\mathbf{v}}$ is used as a transformer attention mask within the transformer denoiser backbone.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Scene Diffusion Setup", "weight": 1.0} -->

Diffusion Sampler We use DPM++ with a Heun solver. We utilize 16 denoising steps for our one-shot experiments and for our amortized diffusion warmup process.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Scene Rollout", "weight": 1.0} -->

Future prediction with no replanning ('One-Shot') is not used in simulation due to its non-reactivity, and forward scene inference, under the standard diffusion paradigm ('Full AR'), is computationally intensive due to the double for-loop over both physical rollout steps and denoising diffusion steps. Moreover, executing only the first step while discarding the remainder leads to inconsistent plans that result in compounding errors. We adopt an amortized autoregressive ('Amortized AR') rollout, aligning the diffusion steps with physical timesteps to amortize diffusion steps over physical time, requiring a single diffusion step at each simulation step while reusing previous plans.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Scene Rollout", "weight": 1.0} -->

We illustrate the three algorithms in Algorithm 1-3 using the same model trained with a noise mixture $t \sim {\{{\mathcal{U}{}};\hat{\mathbf{t}}\}}$ (Eqn. 2). We also illustrate Algorithm 3 in Fig. 4. We denote the total number of timesteps $\mathcal{T} = {H + F}$, where $H,F$ denote the number of past and future steps. We denote ${\mathbf{x}}:={\mathbf{x}}^{\lbrack{{- H}:F}\rbrack}$ to be the temporal slicing operator where ${\mathbf{x}}^{\lbrack 0\rbrack}$ is the final history step.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Scene Rollout", "weight": 1.0} -->

Input: Global context $\mathbf{c}$ (roadgraph and traffic signals), history states ${\mathbf{x}}^{\lbrack{{- H}:0}\rbrack}$, validity $\overline{\mathbf{v}}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Scene Rollout", "weight": 1.0} -->

Output: Simulated observations for unobserved futures ${\hat{\mathbf{x}}}^{\lbrack{1:F}\rbrack}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Controllable Scene Generation", "weight": 1.0} -->

To simulate long-tail scenarios such as rare behavior of other agents, it is important to effectively insert controls into the scene generation process. To do so, we input an inpainting context scene tensor $\overline{\mathbf{x}}$, where some pixels are pre-filled. Through pre-filled feature values in $\overline{\mathbf{x}}$, we can specify a particular agent of a specified type to be appear at a specific position at a specific timestamp.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Controllable Scene Generation", "weight": 1.0} -->

Data Augmentation via Log Perturbation The diffusion framework makes it straightforward to produce additional perturbed examples of existing ground truth (log) scenes. Instead of starting from pure noise ${\mathbf{z}}_{t} \sim {\mathcal{N}{(0,{\mathbf{I}})}}$ and diffusing backwards from $t\rightarrow 0$, we take our original log scene ${\mathbf{x}}'$ and add noise to it such that our initial ${\mathbf{z}}_{t} = {{\alpha_{t}{\mathbf{x}}'} + \mathbf{\epsilon}_{t}}$ where $\mathbf{\epsilon}_{t} \sim {\mathcal{N}{(0,{\sigma_{t}{\mathbf{I}}})}}$. Starting the diffusion process at $t = 0$ yields the original data, while $t = 1$ produces purely synthetic data.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Controllable Scene Generation", "weight": 1.0} -->

For $t \in {}$, higher values increase diversity and decrease resemblance to the log. See Figs. 1 and 15 (Appendix).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Controllable Scene Generation", "weight": 1.0} -->

Language-based Few-shot Scene Generation The diffusion model inpaint constraints can be defined through structured data such as a Protocol Buffer^33^3 ('proto'). Protos can be converted into inpainting values, and we leverage the off-the-shelf generalization capabilities of a publicly accessible chat app powered by a large language model (LLM)^44^4\The chat app is available at gemini.google.com, powered by Gemini V1.0 Ultra at the time of access., to generate new Scene Diffusion constraints protos solely using natural language via few-shot prompt engineering. We show example results generated by the LLM in Fig. 14. Details in the Appendix (A.7).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Generalized Hard Constraints", "weight": 1.0} -->

Users of simulation often require agents to have specific behaviors while maintaining realistic trajectories. However, diffusion soft constraints require a differentiable cost for the constraint and do not guarantee constraint satisfaction. Diffusion hard constraints are modeled as inpainting values and are limited in their expressivity.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Generalized Hard Constraints", "weight": 1.0} -->

Inspired by dynamic thresholding in the image generation domain, where intermediate images are dynamically clipped to a range at every denoising step, we introduce *generalized hard constraints* (GHC), where a generalized clipping function is iteratively applied at each denoising step. We modify Eqn. 1 such that at each denoising step ${\mathbf{μ}}_{t\rightarrow s} = {{\frac{\alpha_{ts}\sigma_{s}^{2}}{\sigma_{t}^{2}}{\mathbf{z}}} + {\frac{\alpha_{s}\sigma_{ts}^{2}}{\sigma_{t}^{2}}\text{clip}{({\mathbf{x}})}}}$, where $\text{clip}{( \cdot )}$ denotes the GHC-specific clipping operator. See more details on constraints in Appendix A.9.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Generalized Hard Constraints", "weight": 1.0} -->

We qualitatively demonstrate the effect of hard constraints for unconditional scene generation in Fig. 8. Applying hard constraints post-diffusion removes overlapping agents but results in unrealistic layouts, while applying the hard constraints after each diffusion step both removes the overlapping agents and takes advantage of the prior to improve the realism of the trajectories. We find that the basis on which the hard constraints operate is important: a good constraint will modify a significant fraction of the scene tensor (for example, shifting an agent's entire trajectory rather than just the overlapping waypoints), or else the model \"rejects\" the constraint on the next denoising step.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

Dataset We use the Waymo Open Motion Dataset (WOMD) for both our scene generation and agent simulation experiments. WOMD includes tracks of all agents and corresponding vectorized maps in each scenario, and offers a large quantity of high-fidelity object behaviors and shapes produced by a state-of-the-art offboard perception system.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Simulation Rollout", "weight": 1.0} -->

Benchmark We evaluate our closed-loop simulation models on the Waymo Open Sim Agent Challenge (WOSAC) metrics (see Appendix A.1), a popular sim agent benchmark used in many recent works. Challenge submissions consist of x/y/z/$\gamma$ trajectories representing centroid coordinates and heading of the objects' boxes that must be generated in closed-loop and with factorized AV vs. agent models. WOSAC uses the test data from the Waymo Open Motion Dataset (WOMD). Up to 128 agents (one of which must represent the AV) must be simulated in each scenario for the 8 second future (comprising 80 steps of simulation), producing 32 rollouts per scenario for evaluation. In a small departure from the official setting, we utilize the logged validity mask as input to our transformer and unify the AV and agents' rollout step for simplicity.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Simulation Rollout", "weight": 1.0} -->

Evaluation In Tab. 12, we show results on WOSAC. We show that Amortized AR (10 Hz) not only requires 16x fewer model inference calls, but is also significantly more realistic than Full AR at a 10Hz replan rate. In Amortized AR, we re-use the plan from the previous step, leading to increased efficiency and consistency. The one-shot inference setting is equivalent to Full AR with no replanning (0.125 Hz) and achieves comparably higher realism, though as it is not executed in closed-loop, it is not reactive to external input in simulation, and thus not a valid WOSAC entry.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Simulation Rollout", "weight": 1.0} -->

In Figs. 6 and 8, we investigate the effects of varied replan rates to simulation realism. While high replan frequency leads to significant degredation in realism under the Full AR rollout paradigm, Amortized AR significantly reduces error accumulation while being $16 \times$ more efficient.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Simulation Rollout", "weight": 1.0} -->

In Tab. 1, we compare against the WOSAC leaderboard with the aforementioned modifications. We achieve top open-loop performance and the best closed-loop performance among diffusion models.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Simulation Rollout", "weight": 1.0} -->

One-Shot Full AR Amortized AR (10 Hz) (10 Hz) Composite Score (M/1) 0.730 0.492 0.673 Composite Score (L/1) 0.736 - 0.703 # Fn Evals 16 16 ⋅ 80 = 1280 80 + 16 = 96 Composite Metric Collision Rate Offroad Rate (↑) (↓) (↓) -AdaLN-Zero -7.99% +65.2% +29.3% -Spatial-Attn -14.5% +209% +11.8% -MultiTask -2.04% +39.6% +3.24% -Size,Type 0.68% -6.85% +2.90% Figure 11: Distrib. realism metrics on WOSAC. L/1 denotes the Large model of patch size 1. Figure 12: Design analysis and ablation studies.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Scene Generation", "weight": 1.0} -->

Unconstrained Scene Generation We use the unconditional scene generation task as a means to quantitatively measure the distributional realism of our model. We condition the scene using the same logged road graph and traffic signals, as well as the logged agent validity to control for the same number of agents generated per scene. All agent attributes are generated by the model.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Scene Generation", "weight": 1.0} -->

Due to a lack of public benchmarks for this task, we adopt a slightly modified version of the WOSAC metrics, where different metrics buckets are aggregated per-scene instead of per-agent, due to the lack of one-to-one correspondence between agents in the generated scene versus the logged scene (see Appendix A.2 for more details). Metrics are aggregated over all agents that are ever valid in the 9 second trajectory.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Scene Generation", "weight": 1.0} -->

We show our model's realism metrics in Tab. 10. Even compared to the oracle performance (comparing logged versus logged distributions), our model achieves comparable realism scores in every realism bucket. Introducing hard constraints on collisions can significantly improve the composite metric by preventing collisions, while scaling the model without hard constraints improves most realism metrics as the model learns to generate more realistic trajectories. The realism metrics only apply to trajectories and do not account for generated agent type and size distributions. We compare the generated size distributions versus log distributions in Fig. 10 and find the marginal and joint distributions both closely track the logged distribution. We show more examples of diverse, unconstrained scene generation when conditioning on the same global context in Appendix A.8 Fig. 16.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Scene Generation", "weight": 1.0} -->

Constrained Scene Generation and Augmentation The controllability we possess in the scene generation process as a product of our diffusion model design can be useful for targeted generation and augmentation of scenes. In Fig. 14, we show qualitative results of scenes with constrained agents generated either via manually defined configs or by a few-shot prompted LLM. Extended qualitative results are listed in Appendix A.7.3.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Model Design Analysis and Ablation Studies", "weight": 1.0} -->

Scaling Analysis Given two options of scaling model compute, either by increasing transformer temporal resolution by decreasing temporal patch sizes, or increasing the number of model parameters, we investigate the performance of multiple transformer backbones: {Model Size} $\times$ {Temporal Patch Size} = {L, M, S} $\times$ {8, 4, 2, 1}. We vary model size by jointly scaling the number of transformer layers, hidden dimensions, and attention heads (see Sec. A.6 of Appendix for details). We show quantitative results from this model scaling in Fig. 2 and qualitative comparisons in Fig. 14. Increasing both temporal resolution and number of model parameters improves realism of the simulation.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Model Design Analysis and Ablation Studies", "weight": 1.0} -->

Multi-task Compatibility We find that multitask co-training across BP, SceneGen and with random control masks improves performance compared to a single-task, BP only model on the sim agent rollout task, notably reducing collision and offroad rates. We find that jointly learning multiple agent features ($x,y,z,\gamma$, size, type) achieves on-par performance with a pose-only ($x,y,z,\gamma$) model.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Model Design Analysis and Ablation Studies", "weight": 1.0} -->

Model Architecture Ablation As shown in Tab. 12, replacing AdaLN-Zero conditioning with cross attention leads to a 7.99% decrease in realism performance, largely due to significantly higher collision rates and offroad rates. Removing the agent-wise spatial attention layer very significantly increases collision rate, as it removes the mechanism for agents to learn a joint distribution.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have introduced SceneDiffuser, a scene-level diffusion prior designed for traffic simulation. SceneDiffuser combines scene initialization with scene rollout to provide a diffusion-based approach to closed-loop agent simulation that is efficient (through amortized autoregression) and controllable (through generalized hard constraints). We performed scaling and ablation studies and demonstrated model improvements with computational resources. On WOSAC, we demonstrate competitive results with the leaderboard and state-of-the-art performance among diffusion methods.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Limitations While our amortized diffusion approach is, to our knowledge, the only and best performing closed-loop diffusion-based agent model with competitive performance, we do not exceed current SOTA performance for other autoregressive models. We do not explicitly model validity masks and resort to logged validity in this work. Future work looks to also model the validity mask.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Broader Impact This paper aims to improve AV technologies. With our work we aim to make AVs safer by providing more realistic and controllable simulations. The generative scene modeling techniques developed in this work could have broader social implications regarding generative media and content generation, which poses known social benefits as well as risks of misinformation.
