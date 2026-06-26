<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Flow Matching-Based Autonomous Driving Planning with Advanced Interactive Behavior Modeling

Topics include Autonomous driving, Flow matching, Interaction-aware planning, Trajectory prediction, Generative model.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proposes Flow Planner, a flow-matching autonomous-driving planner with trajectory tokenization, interaction-aware architecture, and classifier-free guidance. Its contribution is aimed at generating multimodal plans that remain coherent in interaction-heavy driving scenes.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Modeling interactive driving behaviors in complex scenarios remains a fundamental challenge for autonomous driving planning. Learning-based approaches attempt to address this challenge with advanced generative models, removing the dependency on over-engineered architectures for representation fusion. However, brute-force implementation by simply stacking transformer blocks lacks a dedicated mechanism for modeling interactive behaviors that are common in real driving scenarios. The scarcity of interactive driving data further exacerbates this problem, leaving conventional imitation learning methods ill-equipped to capture high-value interactive behaviors. We propose Flow Planner, which tackles these problems through coordinated innovations in data modeling, model architecture, and learning scheme. Specifically, we first introduce fine-grained trajectory tokenization, which decomposes the trajectory into overlapping segments to decrease the complexity of whole trajectory modeling. With a sophisticatedly designed architecture, we achieve efficient temporal and spatial fusion of planning and scene information, to better capture interactive behaviors. In addition, the framework incorporates flow matching with classifier-free guidance for multi-modal behavior generation, which dynamically reweights agent interactions during inference to maintain coherent response strategies, providing a critical boost for interactive scenario understanding.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Experimental results on the large-scale nuPlan dataset and challenging interactive interPlan dataset demonstrate that Flow Planner achieves state-of-the-art performance among learning-based approaches while effectively modeling interactive behaviors in complex driving scenarios.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Ensuring safe and reliable planning remains the highest priority for autonomous driving systems in real-world deployment. However, exceptional challenges stem from complex interactions among traffic participants exhibiting multi-modal driving behaviors, with the difficulty compounding as the number of participants increases. While conventional rule-based approaches can effectively handle most driving scenarios through explicit human-defined constraints and numerical optimization, they are constrained by fundamental limitations, often demanding substantial human engineering efforts and exhibiting poor generalization capability in highly dynamic environments. In contrast, learning-based methods aim to directly learn expert strategies for handling highly interactive scenarios from real-world driving data. These methods have emerged as the dominant choice in both academia and industry, with the expectation that they can achieve reasonable planning through increased data volume and model parameters.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To model sophisticated interactive behaviors in complex traffic scenarios, a learning-based planner must generate trajectories that simultaneously address immediate interactions, anticipate future behaviors of critical traffic participants, and maintain temporally consistent kinematics. This process critically depends on effective temporal and spatial fusion with scene information. However, the heterogeneity of different elements, particularly static map information and dynamic agents' histories, imposes stringent requirements on the fusion mechanism. Early approaches relied on human priors and over-engineered architectures to capture interactions among traffic participants, but these methods proved difficult to scale and often delivered suboptimal performance. While recent work has adopted transformer-based architectures and generative models to improve scalability and performance, vanilla transformer implementations often fail to effectively capture intricate interdependencies among heterogeneous information. In complex scenarios, extensive redundant information can obscure critical traffic participant information during fusion, primarily because these architectures lack specialized designs for interaction modeling.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, the scarcity of high-quality interactive scenarios in training data leads to a critical limitation: naive behavior cloning methods may converge to biased distributions that fail to capture interactive driving behaviors, frequently resulting in safety-critical failures during closed-loop evaluation. Although auxiliary losses can help penalize undesirable behaviors, as commonly done in imitation learning, they typically compromise training stability and require careful, case-by-case design. Besides, some methods incorporate prior knowledge, such as pre-searched reference line, anchor trajectory and goal point, to guide more diverse driving behaviors, but often fail to account for legitimate interactive behaviors that conflict with these structural priors. Alternatively, reinforcement learning can autonomously learn interactive behaviors through trial-and-error, but introduces new challenges including meticulous reward engineering and safety assurance during exploration.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address these challenges, we propose Flow Planner, an advanced learning-based framework melding coordinated innovations in data modeling, architecture design, and learning schemes to enhance interactive driving behavior modeling for autonomous driving planning. Specifically, we first break down the complexity of full-trajectory modeling by decomposing it into overlapping segments. This fine-grained tokenization preserves kinematic continuity within each segment while enabling localized feature extraction through segment-specific token representations. Second, our framework enhances interactive behavior modeling through spatiotemporal fusion of scene and planning tokens. Inspired by scale-adaptive attention, it dynamically optimizes receptive fields for each token to enable effective extraction of critical information. This process also projects heterogeneous conditions from different scene inputs into a unified representation space, further improving performance. Finally, to enable multi-modal behavior generation in complex driving scenarios, we adopt flow matching loss, which offers simpler implementation and faster convergence compared to diffusion-based approaches. Building upon classifier-free guidance, our framework dynamically reweights neighboring agent interactions during inference to maintain coherent planning strategies. Compared to naive behavior cloning approaches, this scene-information-enhanced generation mechanism provides substantial improvements in interactive scenario understanding.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Experimental results on the large-scale real-world benchmark nuPlan and challenging interactive benchmark interPlan show that Flow Planner establishes state-of-the-art performance in closed-loop evaluation among learning-based planners, while demonstrating human-like interactive behaviors in complex traffic scenarios.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Method", "weight": 1.0} -->

In this section, we provide a brief introduction to trajectory generation in planning tasks and present Flow Planner, a novel approach that emphasizes interactive behavior modeling, as shown in Figure 1. From the data modeling perspective, we propose fine-grained trajectory tokenization to achieve expressive trajectory modeling. Subsequently, we design a well-curated architecture that enhances interactive behavior modeling through thorough spatiotemporal fusion. Finally, we adopt flow matching with classifier-free guidance to further enhance multi-modal and interactive driving behaviors.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Our work primarily focuses on the planning module of autonomous driving systems, utilizing processed perception as input and evaluating planning capabilities through closed-loop testing. The trajectory generation task can be formulated as a conditional generation problem, where the transformation from a source distribution $p(\tau_{0})$ (typically standard Gaussian) to a target data distribution $q(\tau_{1}|C)$ (e.g., planning trajectories $\tau_{1}$ with scene information $C$) is represented by a probability path.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The model $v_{\theta}(\cdot)$ is trained to predict the velocity along the path connecting sample pairs $(\tau_{0},\tau_{1})$ drawn from the source and target distributions, using the objective: where $\tau_{t}=\alpha_{t}\tau_{1}+\sigma_{t}\tau_{0}$ and the ground truth velocity $v_{t}(\tau_{t},t)=\dot{\tau}_{t}=\dot{\alpha}_{t}\tau_{1}+\dot{\sigma}_{t}\tau_{0}$ is the time derivative of the interpolation between source and target points. The distinction between ODE-based diffusion models and flow matching models lies in their respective designs of probability paths.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

Flow Planner is a transformer-based generative model for motion planning that effectively fuses noisy trajectory $\tau_{t}$ with scene condition $C$. The architecture overview is presented in Figure 1.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

Scene Encoder. We consider the vectorized driving scene information. For each neighboring agent (e.g., vehicle, pedestrian, cyclist), we represent its past $T$ timestep information as $F_{\mathrm{neighbor}}\in\mathbb{R}^{T\times H_{\mathrm{neighbor}}}$, where $H_{\mathrm{neighbor}}$ is the dimension of state information including coordination, velocity, size, and the type of different agents. For each lane, we interpolate the centerline into $N$ uniformly distributed points. Each point contains coordinates, corresponding boundary vectors, speed limit information, and traffic light status, represented as $F_{\mathrm{lane}}\in\mathbb{R}^{N\times H_{\mathrm{lane}}}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

To maximize scenario information preservation while maintaining model efficiency, we employ separate MLP-Mixer architectures to encode both agent and lane features, following: where $\text{MLP}_{seq}$ and $\text{MLP}_{feat}$ are two separate MLPs operating on sequence and feature dimensions respectively, and $F$ is the information of neighboring agents $F_{\mathrm{neighbor}}$ or lanes $F_{\mathrm{lane}}$. Additionally, we consider static objects, encoded using another MLP. The navigation information is represented similarly to lane information and is processed by a separate MLP-Mixer.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

Fine-grained Trajectory Tokenization. We start by rethinking the trajectory tokenization in autonomous driving planning, an area that has received inadequate research attention despite its critical importance. Prevalent methods use a single token to represent the whole trajectory, which maintains kinematic consistency but suffers from inefficient scene context fusion due to over-compression. Alternative approaches utilizing either discrete timestep tokens or autoregressive generation successfully achieve temporal fusion within trajectories. However, these methods inevitably encounter compounding error accumulation, presenting a fundamental limitation for closed-loop autonomous driving applications.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

To address these limitations, we propose a balanced modeling framework featuring fine-grained trajectory tokenization that preserves temporal interaction patterns while ensuring consistent behavior across all planning horizons. Specifically, the noised trajectory $\tau_{t}=(x_{1},x_{2},...,x_{L})$ introduced in Section 3.1, which comprises $L$ points in total, is first divided into $K$ segments, each containing $L_{seg}$ points. Additionally, the neighboring segments share an overlap with a length $L_{overlap}$ to ensure the consistency and smoothness of the resembled trajectory. Next, a shared MLP is used to transform the noised segments into the ego-trajectory tokens: where $l^{k}=(k-1)(L_{seg}-L_{overlap})$ is the start timestep of the trajectory segment, and $r^{k}=(k-1)(L_{seg}-L_{overlap})+L_{seg}$ is the end timestep.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

Note that timesteps in trajectories differ conceptually from noise step $t$ in generative models. After that, we adopt the sinusoidal position encoding to inject temporal information. Finally, we concatenate all the segment tokens along the sequence dimension to obtain the ego feature: $F_{ego}=\text{Concat}\left({F}_{ego}^{1},...,F_{ego}^{K}\right)$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

Interaction-enhanced Spatiotemporal Fusion. Although fine-grained trajectory tokenization provides more expressive representations for behavior modeling, the efficient fusion of spatiotemporal information remains unresolved. This process requires bidirectional interaction among numerous information-sparse tokens to enable comprehensive scene understanding and behavior modeling. Another critical challenge lies in effectively fusing these heterogeneous modalities, such as the static information of lanes and the dynamic information of agents. These challenges are what vanilla transformer attention fails to accomplish effectively.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

Inspired by recent work in text-to-image generation, where cross-modality feature fusion is performed in a unified space, we first process heterogeneous features through separate adaptive LayerNorm (adaLN) modules, projecting them into a shared latent space where both timestep conditions and navigation information are injected via modulation mechanisms. Then the processed tokens from one scenario, including the features of lanes $F_{lane}$, neighboring agents $F_{neighbor}$ and ego planning trajectory $F_{ego}$, are concatenated along the sequence dimension: For the subsequent fusion of all tokens ${F}_{global}$, a critical observation reveals that interaction intensity between traffic participants correlates strongly with their spatial distances. For instance, excessively distant roads and vehicles may introduce noise that degrades planning performance. Inspired by scale-adaptive self-attention, we employ learnable receptive fields for individual tokens to incorporate spatial guidance during feature fusion.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

This is achieved through spatial distance-scaled attention score adjustment: where $W^{Q},W^{K},W^{V}$ are the pre-projection weights used to generate query, key, and value for the attention mechanism, $D$ is the pairwise Euclidean distance matrix of the tokens, and $\lambda$ is the receptive scaler generated by a simple linear projection of the tokens. Intuitively, tokens representing traffic participants beyond a certain distance are assigned smaller attention scores, making them less influential in the computation and enabling more adaptive resource allocation.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

Then, the global feature is decomposed into modality-specific tokens, where each modality undergoes distinct adaLN and FFN projections to further mitigate the heterogeneous modality gap: | | | $\displaystyle{F}_{lane},{F}_{neighbor},{F}_{ego}=\text{Chunk}\left({F}_{global}\right),$ | | \(6\) | | | | $\displaystyle{F}_{lane}=\Psi\left(F_{lane}\right),{F}_{neighbor}=\Psi\left(F_{neighbor}\right),{F}_{ego}=\Psi\left(F_{ego}\right),$ | | | where $\Psi$ is the abbreviation of the $\text{FFN}(\text{adaLN}(\cdot))$. Building upon the foundation established in Eq. -, our architecture employs stacked transformer blocks to progressively refine spatiotemporal interactions. Finally, a standard self-attention layer is used for final aggregation.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

The features are then processed through token pooling to obtain ego planning tokens, followed by a final layer $\Psi$ that transforms these representations into the ego vehicle's planned trajectory.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Guided Trajectory Generation via Flow Matching", "weight": 1.0} -->

With the enhanced model architecture established, we want to push the upper-bound performance for imitation learning in trajectory generation. Compared to conventional behavior cloning, generative models show better expressiveness in modeling multi-modal and interactive driving behaviors. The most compelling aspect of generative models lies in their ability to dynamically reweight conditional signals during inference through classifier-free guidance, thereby amplifying conditional influence to achieve superior conditioned generation. Specifically, we enhance the conventional behavior cloning approach by combining the scene-conditioned planning trajectory distribution $q(\tau_{1}|C)$ with an unconditioned distribution $q(\tau_{1})$, yielding an enhanced distribution $\tilde{q}(\tau_{1}|C)\propto q(\tau_{1})^{1-\omega}q(\tau_{1}|C)^{\omega}$, where $\omega>1$ is the weighting parameter that controls the condition signal strength. Intuitively, the model learns both the planning behavior without scene conditions and the behavior with scene conditions, enabling it to implicitly capture the behaviors induced by scene conditions.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Guided Trajectory Generation via Flow Matching", "weight": 1.0} -->

This approach strengthens the understanding of complex driving scenarios and improves interactive behavior modeling. Building upon this framework, we can sample from distribution $\tilde{q}(\tau_{1}|C)$ using the guided velocity field as follows: The remaining challenge involves training the model to estimate velocities in Eq.. We address this by training a single model with Bernoulli-masked conditions as follows: In Eq., we employ the reparameterization trick to directly predict ground-truth trajectories. This formulation proves mathematically equivalent to the velocity prediction loss in Eq.. Additionally, we employ the optimal transport path widely used in flow matching, where the velocity estimation follows $v_{\theta}(\tau_{t},t|C)=\left(\tau_{\theta}(\tau_{t},t|C)-\tau_{0}\right)/t$. The same approach applies to unconditioned velocities $v_{\theta}(\tau_{t},t)$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Guided Trajectory Generation via Flow Matching", "weight": 1.0} -->

Finally, we obtain the guided velocity from Eq. and employ an ODE solver for trajectory generation.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Guided Trajectory Generation via Flow Matching", "weight": 1.0} -->

Notably, the conditioned information can be flexibly selected in our framework. In practice, we specifically mask neighboring vehicle information in Eq., as we empirically find this to be most critical for interactive driving behavior. As shown in Figure 1, the unconditioned model fails to account for neighboring vehicles, while the conditioned model overreacts to the nearest vehicle with overly conservative planning behavior. In contrast, our classifier-free guided approach successfully generates reliable planning results that appropriately respond to neighboring vehicle dynamics.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

In our implementation, the entire scenario is first transformed into an ego-centric front-left-up coordinate. To ensure training stability and input consistency, input data as well as ground truth trajectories are first normalized using static measures extracted from training data. In addition, data augmentation has been demonstrated as effective in improving the robustness of planning outputs. During training, the ego vehicle's state at the current frame is first randomly perturbed, and a quintic polynomial is used for interpolating a new trajectory, serving as the ground truth of the augmented sample. During inference, the second-order midpoint method is used for the flow ODE solver. In addition, to ensure the consistency of the generated trajectory, we introduce an extra consistency loss $\mathcal{L}_{consist}$ on the segment overlap during training.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

Specifically, given the predicted segments, we apply L2 loss on the overlap of neighboring predicted segments: where $\hat{\tau}^{k:k+1}$ denotes the portion of the predicted trajectory from segment $k$ that overlaps with segment $k+1$, and $\hat{\tau}^{k+1:k}$ represents the portion of the predicted trajectory from segment $k+1$ that overlaps with segment $k$. This consistency loss is added to the flow matching loss with a loss scaling hyperparameter $\alpha>0$ to form the final objective $\mathcal{L}=\mathcal{L}_{flow}+\alpha\cdot\mathcal{L}_{consist}$. Note that the converged model is equivalent to the one supervised by merely the vanilla flow matching objective. During inference, the predicted values of the overlapping areas are averaged in a straightforward manner to generate the final prediction.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section we conducted extensive experiments to demonstrate the performance of our model. We will start by briefly introducing the benchmarks on which the experiments are performed, and the primary baselines we compared our model. Next, we will focus on several representative cases that intuitively illustrate the advantage of our method, comparing it with the previous state-of-the-art method in specific scenarios. Then, we will delve into the details of our designs and showcase their effectiveness through a further ablation study.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Benchmarks. In this study, our model is trained on nuPlan featuring a large-scale real-world driving dataset collected across four different cities. This dataset covers up to 75 scenario types, including diverse scenarios with multi-vehicle interaction and complex lane structures. Specifically, the model is trained on the 1M training split, following. For evaluation, the model is tested on both nuPlan and interPlan, and we mainly focus on the closed-loop performance of the planners, where an LQR controller is used for simulation. We test the model in both non-reactive and reactive settings using the following three benchmarks in nuPlan: $$, a validation dataset with 1118 scenarios in total; $$ -random: over 200 randomly selected scenarios from the scenario types assigned by the nuPlan Planning Challenge; and $$ -hard: a collection of the worst-performing scenarios by rule-based PDM, comprising 272 scenarios. Each of the three benchmarks covers 14 different types of scenarios respectively. We argue that the benchmark can evaluate model's performance and capability more comprehensively owing to its sufficient capacity, while -random benchmark may introduce extra uncertainty, hindering the fairness of evaluation.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Whereas Flow Planner achieves overall state-of-the-art performance across three benchmarks, we primarily leveraged for further experiments. In addition, we evaluate our model using the full-scale interPlan benchmark, which contains 335 challenging interactive scenarios with specially augmented traffic agents quantity and behavior, as shown in Fig. 2, in reactive mode. This benchmark highlights model's capability of modeling interactive behavior in complex and unexpected scenarios, providing a more appropriate evaluation of our method.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Baselines. For a comprehensive analysis of the effectiveness of our method, we conduct comparative experiments with prevailing methods, including rule-based, imitation learning, and hybrid methods that refine the learning-based model with rule-based trajectory post-processing. Specifically, we compare our method with the following baselines: IDM:a classic rule-based method, also used for neighboring vehicles control in closed-loop reactive evaluation; PDM:the first place of nuPlan contest, which proposed a rule-based model (PDM-Closed), a learning-based model (PDM-Open) as well as a hybrid version (PDM-Hybrid), all relying on road centerline; PLUTO: an imitation learning-based model with extra contrastive objectives and post-processing; GameFormer: a transformer-based model for interactive prediction based on game-theory, with extra refinement process; Diffusion Planner: the state-of-the-art model based on diffusion model for multi-modal trajectory generation.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Flow Planner w/ refine. (Ours) Flow Planner (Ours) Table 1: The overall performance of Flow Planner and other learning-based baseline models. Evaluation is conducted in both non-reactive and reactive mode. The highest score of each benchmark is marked with a, and the second-best scores appear in bold. In addition, we use * to mark the methods directly leveraging road centerline extracted from the map.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Main Results and Case Study", "weight": 1.0} -->

Main Results. The overall evaluation results are shown in Table 1. Flow Planner achieves state-of-the-art performance in the learning-based settings, without rule-based refinement. It is noteworthy that Flow Planner achieves 90.43, which is the largest and most representative benchmark of the three. As far as we know, it is the first learning-based method to surpass the 90-score mark without any prior knowledge on this benchmark, while other learning-based models require extra rule-based refinement to reach 90+ performance. With the similar post-processing module, our model Flow Planner w/ refine. achieved competitive performance on the nuPlan benchmark compared with previous rule-based and hybrid methods. To find out the specific improvement brought by our method, we further report the performance of Flow Planner and baseline methods in several specific types of scenarios in nuPlan. As is shown in Table 2, Flow Planner outperforms the two strong baselines significantly in scenarios where interaction with neighboring vehicles is frequent, including unprotected left turns and traffic light intersections.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Main Results and Case Study", "weight": 1.0} -->

In addition, on the interPlan benchmark in which most scenarios require dense interaction with the environment, as is shown in Table 3, we achieve 8.92-point improvement over Diffusion Planner, demonstrating the strong capability of interactive modeling. It can also be inferred from the table that Flow Planner exhibits robust interactive behavior modeling ability even when interacting with jaywalking pedestrians, whose behavior is tricky to predict due to the lack of relevant data and their volatile movement.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Main Results and Case Study", "weight": 1.0} -->

Starting right turn Starting left turn Waiting for pedestrian Flow Planner (Ours) Table 2: Performance of different planners in specific scenarios of, where "Intersection" corresponds to the "Starting straight traffic light intersection traversal" scenario.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Main Results and Case Study", "weight": 1.0} -->

High Traffic Density Flow Planner (Ours) Table 3: Performance of different planners on interPlan and scores on specific scenarios Case Study. To further demonstrate the effectiveness of our method, we select representative interactive scenarios to compare the behavior of different models in the closed-loop testing. As is shown in Figure.3, we selected two scenarios from nuPlan benchmark, and report the different behavior of our Flow Planner and Diffusion Planner. Specifically, in (a), Diffusion Planner failed to account for a vehicle approaching quickly from the rear-left. It changed lanes despite being slower than the approaching car, resulting in a collision. In contrast, Flow Planner recognized the fast-approaching vehicle and, realizing that the safety distance was insufficient, aborted the lane change to avoid collision; while in (b), Diffusion Planner did not consider a right-turning vehicle from the oncoming lane. It entered the turn at a low speed, leading to a collision. Flow Planner, however, identified that the right-turning vehicle would arrive later and chose a higher entry speed, safely completing the turn. More closed-loop planning results where Flow Planner exhibits interactive behavior modeling capability are shown in Appendix A.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

We ablate the key designs of our method to further study their effects on model performance. The overall ablation path is shown in Table LABEL:tab:ablation_path, where we start with a base model by simply stacking self attention layers to form the decoder while keeping the scene encoder unchanged. The model is then gradually enriched to form the final architecture, so as to better reflect the improvements gained from each component.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

+ Classifier-free Guidance in Section 3.3 Table 4: Ablation path of key components on nuPlan and interPlan, and performance on specific interPlan scenarios. Below we use NA for Nudge Around, HTD for High Traffic Density and JW for Jaywalk Table 5: Ablation on the number of trajectory segments on nuPlan Benchmark.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

Trajectory Tokenization. The choice of trajectory segment number and the length of overlap directly affect the balance of consistency and flexibility of the generated trajectory. Therefore, we trained different models with different choices of segment number, and evaluated them, as shown in Table 5 and Figure 4. Note that the overlap length is set to 0 when the segment length is 1 (fully scattered) or 80 (whole trajectory), and half the length of the trajectory segment in other cases. It can be revealed from the table and figure that as the length of segments increases, the smoothness of the generated trajectory increases as well as the model performance. However, when the trajectory is coarsely segmented, the trajectory tokens become cumbersome to model the multi-modal distribution of interactive behavior since a single token is responsible for a relatively long horizon of trajectory, which can contain several different interactions with neighboring agents.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

Scale-Adaptive Attention and Separate AdaLN and FFN. Scale-adaptive attention enables more efficient feature fusion between numerous tokens extracted from the scenario. However, there exists inherent heterogeneity between the features collected from different types of instances in the scenario, and thus the straightforward implementation of adaptive attention does not introduce visible improvement. With the separate adaLN and FFN modules projecting the heterogeneous features into a shared space, a prominent performance improvement can be seen from Table LABEL:tab:ablation_path when the scale-adaptive attention is cooperatively implemented.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

Classifier-free Guidance. The scale of classifier-free guidance is a flexible hyperparameter that can be tuned at inference. Therefore, we ablated different choices of guidance scale using the same checkpoint. The results are illustrated in Table 6. It can be seen from the table that as the scale of guidance increases, the model's performance also improves. However, an overwhelmingly large scale can also lead to deterioration in performance, since the norms of the conditioned and unconditioned velocity are not perfectly aligned, and a scale too large may lead to irreversible deviation on the flow path. Ideally, a proper scale applied during inference can induce even better performance compared with the fully conditioned generation, as is shown in Figure 1.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduce Flow Planner, a novel learning-based framework for autonomous driving planning that advances interactive behavior modeling through three coordinated innovations. First, fine-grained trajectory tokenization enables expressive behavior representation. A well-designed architecture then facilitates comprehensive spatiotemporal fusion to enhance interaction modeling. Finally, flow matching combined with classifier-free guidance captures the multi-modal nature of real driving behaviors, which further attunes to interactive behavior during inference. Over the nuPlan benchmark, Flow Planner achieves state-of-the-art closed-loop performance among imitation-learning methods, while demonstrating capability in modeling interactive behaviors in complex driving scenarios. Due to space limit, more discussion on limitations and future direction can be found in Appendix E.
