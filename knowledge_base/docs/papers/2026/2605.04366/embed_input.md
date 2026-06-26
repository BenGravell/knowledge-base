<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Conditional Flow-VAE for Safety-Critical Traffic Scenario Generation

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Safety-critical scenarios are essential for the development of autonomous vehicles (AVs) but are rare in real-world driving data. While simulation offers a way to generate such scenarios, manually designed test cases lack scalability, and adversarial optimization often produces unrealistic behaviors. In this work, we introduce a conditional latent flow matching approach for scalable and realistic safety-critical scenario generation. Our method uses distribution matching to transform nominal scenes into safety-critical rollouts. Furthermore, we demonstrate that incorporating both simulation and real-world data enables our framework to efficiently generate diverse, data-driven scenarios. Experimental results highlight that our approach is able to more consistently and realistically generate novel safety-critical scenarios, making it a valuable tool for training and benchmarking AV systems.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Safety-critical scenarios play a central role in the development of autonomous vehicles (AVs). Rare events such as sudden cut-ins, near-miss interactions, or unexpected braking are precisely the situations where an AV's decision-making and planning policies are most challenged. Robust performance is essential, yet exposing AV systems to these conditions in the real world is costly and dangerous. Simulation is therefore critical: it enables evaluation under safety-critical conditions before deployment, reducing risk and accelerating development.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

However, acquiring a sufficiently diverse and realistic set of safety-critical scenarios for simulation remains a major challenge. Traditionally, simulation-based approaches typically rely on heavy human curation. For example, identifies potential hazardous events in their ODD and then recreates them in simulation, and manually reconstructs safety-critical scenarios from police crash reports. However, this approach is far too tedious to scale efficiently and cost-effectively. Automated methods like adversarial optimization where agents are constructed to deliberately collide with the ego vehicle can be more easily scaled. However, real traffic participants are not inherently adversarial, and such methods neglect the prevalence of near-miss situations that pose genuine challenges for autonomy systems. In both cases, the resulting scenarios may not reflect the statistics of real world driving.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Alternatively, *distribution matching* approaches are a promising avenue towards traffic simulation that matches the real world. However, distribution matching approaches like imitation learning are notoriously data hungry, but real safety critical scenarios are inherently rare and difficult to obtain. Standard traffic simulation models are trained predominantly on nominal data and thus are naturally biased toward reproducing nominal behaviors rather than generating safety-critical ones. Unfortunately, overly upsampling the limited number of safety-critical scenarios can easily lead to overfitting.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Towards a data-driven approach to generating safety-critical scenarios while preserving behavioral realism, we propose our conditional flow VAE. We supplement the limited number of high-fidelity real safety critical scenarios with lower fidelity but easily scalable synthetic data, and design a model which can maximally take advantage of this data mixture. Specifically, our model captures the semantics of a variety of driving scenarios with a conditional VAE encoder and uses a flow matching transformer to transform the VAE latents from the nominal distribution to the safety-critical counterpart. Then we utilize the VAE decoder to produce safety-critical rollouts from nominal driving scenarios, bridging the gap between rare real-world events and scalable synthetic generation. By incorporating both real-world and simulated data, our approach captures the realism of human driving while supplementing the long tail with synthetic diversity. Empirically, our flow approach outperforms alternative conditioning baselines. Furthermore, we enable controllable scenario difficulty by conditioning on automatically generated heuristic labels, allowing systematic evaluation across varying levels of criticality.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

To summarize, our contributions are threefold: A generative framework for safety-critical scenario generation based on conditional latent flow matching.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Realism through distribution alignment, enabling transitions from nominal to safety-critical outcomes without adversarial artifacts.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Data efficiency and controllability, achieved through the integration of real and simulated data along with difficulty-conditioned generation.

<!-- chunk {"id": "body-0010", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Together, these advances provide a practical and principled way to generate realistic safety-critical scenarios.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Challenging Scenario Generation", "weight": 1.0} -->

Scenario generation includes a two-fold objective of actor placement and actor roll-out. The former objective generates a new scenario initialization from scratch or modifies existing scenarios. It often specifies the actor placement and initialization states so that the downstream simulation may yield safety-critical outcomes,. In this paper, we focus on generating safety-critical scenarios from a nominal initialization with a roll-out model, where we train a model to directly control the actor maneuvers to be applied upon any nominal initialization.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Challenging Scenario Generation", "weight": 1.0} -->

Early approaches rely on manually designed scenarios and heuristic rules, often embedded in simulation platforms such as CARLA. These methods offer clear control over vehicle maneuvers by manually specifying the planning trajectory and kinematic constraints. However, they are often limited in scalability and diversity, as each scenario must be explicitly scripted by engineers. The scenario parameters also need to be decided carefully to ensure that there is no collision or other undesired behaviors.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Challenging Scenario Generation", "weight": 1.0} -->

The advent of data-driven approaches allows the machine learning model design that focuses on learning from mass-scale driving datasets like WOMD. With generative machine learning model architectures like VAE, autoregressive models and diffusion models, these methods are often trained on behavior cloning objectives that allow high reconstruction L2 scores on the eval data. They also utilize common knowledge like collision loss and traffic signals to enhance realism. However, the behavior cloning objective implies that the model is fitted to the distribution of the training dataset, where most of the data are nominal, which hinders the ability to diversify towards safety-critical rollouts.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Challenging Scenario Generation", "weight": 1.0} -->

Another approach is to apply an adversarial objective to the actors in the scenario. Many of those apply similar strategies where they manipulate the learned representation of the actors in the latent space. STRIVE utilizes an optimization objective on the latent space of the CVAE. Other methods use reinforcement learning based editing. The actors in the scenario are often set with an adversarial objective to cause collisions with the ego actor. While effective at exposing the weakness of planners, these methods often compromise realism: real traffic actors are not inherently adversarial, thus the resulting trajectories may be unnatural. Besides, the method also requires the presence of a planner module for the ego vehicle, leading to more complex training architecture.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B VAE and Flow Matching Model", "weight": 1.0} -->

Variational Autoencoder models are useful in representation learning, where it efficiently compresses the input features into a latent space, so that a decoder can utilize them for downstream tasks. It is desired to manipulate in the latent space to achieve specific objectives. Research in computer vision has shown that the representation space can be decomposed into subcomponents and then used for domain translation. In the context of autonomous driving, VAE encodes traffic scenarios efficiently conditioned on the past states and high-level scenario information, and a decoder head is usually applied to generate per-actor roll-outs. Previous work have shown that the VAE embedding space contains useful information that is valuable for interpretable maneuver generation. In our work, we show that the nominal and safety-critical scenarios reside in different subsections of the latent space and a transfer map can be learned to map the nominal latents to the safety-critical latents.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B VAE and Flow Matching Model", "weight": 1.0} -->

A flow matching model is a type of generative model that learns to transform samples from a simple base distribution into samples from a complex target distribution following a continuous flow. Instead of learning a discrete sequence of transformations (like normalizing flows) or stepping with random noises (like diffusion), flow matching learns a vector field that describes explicitly how data should move between source and target distributions over time. During inference, the flow model uses a sampler to step through the timesteps from 0 to 1 along the learned field to map the sample from the source distribution to the target distribution. Key developments, including Rectified Flow, allows flowing from an arbitrary source distribution instead of the standard Gaussian. The method is widely applied to various tasks like text-to-image generation, and robotics. It is also easy to apply conditioning on the flow model to boost the performance. Compared to diffusion, the computational efficiency and stable training objective make it preferable for learning the transfer from nominal scenarios into safety-critical ones within the latent space.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A Traffic Modeling", "weight": 1.0} -->

We define the problem scope as generating a traffic scenario with $N$ actors in a finite horizon of $T$ time steps. We use $Y^{t}=\{y_{1}^{t},y_{2}^{t},...,y_{N}^{t}\}$ to denote the actor states at time $t$. For each vehicle state we define $y_{i}^{t}=(b_{x},b_{y},b_{z},b_{\theta},b_{v},b_{l},b_{w},b_{h})$, which describes the 3D position, yaw, velocity, and the length, width, and height of a vehicle's bounding box.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Traffic Modeling", "weight": 1.0} -->

The model observes the high-definition map $\mathbf{M}$ and past $H$ states $Y^{-H:0}$ and outputs the vehicle control action sequence $A^{t}=\{a_{1}^{t},a_{2}^{t},...,a_{n}^{t}\}$, where $a_{i}^{t}=(a_{accel},a_{steer})$. The goal of traffic modeling is typically to learn to model the distribution over future actor states.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-C Variational Autoencoder", "weight": 1.0} -->

The variational autoencoder is a latent variable approach to generative modeling where $z$ is some latent variable meant to capture unobserved aspects of the generative process. An encoder $q_{\theta}(z|x)$, decoder $p_{\theta}(x|z)$ and prior $p_{\theta}(z)$ can be jointly learned to optimize the evidence lower bound: where $\mathcal{D}_{\text{KL}}$ is the Kullback-Leibler divergence. After learning, sampling from $p(x)$ amounts to sampling from the prior followed by the decoder. VAEs can be extended to support conditional generation by extending the encoder, decoder and prior to be conditional distributions as well, e.g. $q_{\theta}(z|x,c)$, $p_{\theta}(x|z,c)$, $p_{\theta}(z|c)$ respectively.

<!-- chunk {"id": "body-0020", "role": "body", "section": "METHODOLOGY", "weight": 1.0} -->

The overall framework of the conditional flow VAE is depicted in Fig. 2.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-A Latent flow matching", "weight": 1.0} -->

We take a distribution matching approach for safety-critical scenario generation. Let $p_{N}$ be the nominal distribution of traffic scenarios for which we have many samples, and $p_{S}$ be the safety-critical distribution, for which we have comparatively fewer samples. Our approach learns a flow from $p_{N}$ to $p_{S}$. Doing so allows us to learn to sample new scenarios from $p_{S}$ by transporting samples from $p_{N}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-A Latent flow matching", "weight": 1.0} -->

To begin, we follow and model general traffic scenarios using a conditional VAE: In this case, the encoder (posterior) is given as $q_{\theta}(Z|\mathbf{M},Y^{-H:0},Y^{1:T})$. Note that we learn the conditional VAE on the mixture of $p_{N}$ and $p_{S}$, meaning the model is trained on samples from both distributions.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-A Latent flow matching", "weight": 1.0} -->

We now define the *safety-critical* aggregate posterior as Intuitively, this is the distribution over $Z$ for safety-critical scenarios. We sample from $q^{S}$ using the VAE posterior on safety-critical scenarios. The flow model then aims to learn a transport between the prior and this safety-critical latent distribution by optimizing where $Z_{t}=tZ_{1}+(1-t)Z_{0}$, and $Z_{1}\sim q_{\theta}^{S}$ and $Z_{0}\sim p_{\theta}(Z|\mathbf{M},Y^{-H:0})$. This objective trains the model to map prior latents to safety-critical latents.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-A Latent flow matching", "weight": 1.0} -->

There are several advantages to our approach. By training the VAE on the mixture of nominal and safety-critical data, we are able to learn better overall realistic driving by making use of all data, as opposed to learning only on safety-critical data. However, the explicit flow objective allows us to steer our sampling towards the safety-critical distribution. Compared to trajectory space, flowing in latent space also allows us to control the degree of safety criticality by doing a partial flow (e.g. until $t=0.5$), since the decoder still maps intermediate results in latent space to plausible futures.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B Training Recipe", "weight": 1.0} -->

We follow a two-stage training procedure inspired by latent space manipulation practices in computer vision. In the first stage, we train a conditional VAE on both nominal and safety-critical scenarios to establish a stable and semantically meaningful latent representation for both types. In the second stage, we train the flow model exclusively on safety-critical scenarios to learn the distributional transport from nominal to safety-critical latents. We found that this staged design is essential for reliable convergence. This is because empirically we observed that for a single stage end-to-end training approach, the prior and posterior distributions of the VAE undergo large shifts in the early iterations, while the flow model simultaneously attempts to learn the mapping with high learning rates. As a result, the flow model is effectively trained on a non-stationary target, which often leads to instability. By decoupling the stages, the VAE first provides a fixed latent space learned under a combination of imitation and traffic-compliance objectives. The subsequent flow model is then trained with a flow objective, which benefits from theoretical convergence guarantees under a fixed latent space.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-C Architecture", "weight": 1.0} -->

We now describe the neural network architecture used for the different components of our approach.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Backbone", "weight": 1.0} -->

A transformer based architecture is used as the backbone network for the VAE and flow transformer. We adopt several common techniques used in traffic modelling. We first extract state features from each actor using a simple MLP. Map features are extracted using an off-the-shelf map encoder. Map and actor state features are then augmented with PairPose relative positional features allowing for viewpoint-invariance. Our transformer comprises interleaved actor-to-map, actor-to-actor and actor-to-time attention layers; relative positional encodings between actors are used to preserve viewpoint-invariance. To save on computational cost, actor-to-actor and actor-map attention is limited to the top-$k$ closest actors or lane graph nodes, essentially forming a local context for each actor.

<!-- chunk {"id": "body-0028", "role": "body", "section": "VAE", "weight": 1.0} -->

Following prior work on multi-agent traffic simulation, we employ a conditional variational autoencoder (CVAE) approach to learn latent embeddings that capture rich scene semantics and the multi-agent interactions. The prior $p_{\theta}(Z|\mathbf{M},Y^{-H:0})$ and posterior $q_{\theta}(Z|\mathbf{M},Y^{-H:0},Y^{1:T})$ use the same backbone described above, differing only in the number of timesteps of actor states observed, sharing the map encoder. Note that, similar to, we predict a separate latent for each actor. The decoder also uses the same backbone; the latent is fused into the actor feature, and a steering and acceleration is predicted per actor.

<!-- chunk {"id": "body-0029", "role": "body", "section": "VAE", "weight": 1.0} -->

(a) Urban cut-in scenario (b) Highway cut-in scenario (c) Highway hard-brake scenario Figure 3: Qualitatives. From top to bottom: original nominal scenario, VAE reconstruction, STRIVE, our model.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Flow model", "weight": 1.0} -->

With the stable latent representation established from the CVAE, safety-critical rollout generation requires transforming nominal latents into their safety-critical counterparts. We frame this as a distribution matching problem: safety-critical behaviors (e.g., hard braking, aggressive cut-ins) occupy distinct subregions of the latent space, and our goal is to learn a mapping from nominal priors to these critical submanifolds.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Flow model", "weight": 1.0} -->

We use the same transformer backbone for our flow model. Our transformer backbone is conditioned on the actor state feature to implement flow matching in latent space. We combine the flow matching context along with the actor-level features to form the following input features: where $t_{\text{denoise}}$ is the denoising time step drawn from the uniform distribution $U$. $X$ is actor state and map features. $E_{T}$ is the sinusoidal positional encoding of the denoising time step. $E_{x}$ is an interpolation between the prior latent $Z_{\text{prior}}$ and the posterior latent $Z_{\text{posterior}}$. Since the flow model only conditions on the scene initialization, an optional maneuver indicator is accepted to control the level of aggressiveness of maneuver. We classify each scenario in the training dataset into one of the three categories: nominal, safety-critical, and very safety-critical. The label is computed with heuristics on vehicle kinematics and time-to-collision. $E_{c}$ is the maneuver label projected with an MLP.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Flow model", "weight": 1.0} -->

During inference, we discard the posterior encoder and use the prior encoder only since ground-truth futures are unavailable. Given any initialization state, the prior encoder produces a latent $Z_{\text{prior}}$, which is then transformed by the Flow Transformer into a steered latent $Z_{pred}$. This latent is decoded through the CVAE decoder to acquire the final actor states.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-D Dataset", "weight": 1.0} -->

Performing distribution matching between nominal and safety-critical rollouts requires access to safety-critical scenarios observed in real driving logs. However, due to their inherent sparsity in naturalistic datasets, none of the widely used open-source autonomous driving corpora explicitly curate such subsets. To address this limitation, we adopt a simulation--real data mixing strategy that balances scalability with realism. For real safety-critical scenarios, we conduct targeted data mining over a catalogue of real driving logs. We extract approximately 500 unique scenarios with challenging situations; e.g., actors perform abrupt cut-ins, aggressive braking, etc. The result of this data mining is a set of smaller scale but high-fidelity demonstrations of realistic human driving behaviors under challenging conditions.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-D Dataset", "weight": 1.0} -->

To supplement the real safety critical scenarios, we leverage simulation. Our goal is to generate realistic scenarios which introduce diverse behaviors that can help transfer to real safety critical scenarios. We use existing deep-learning based traffic simulation models for nominal traffic, with the addition of a "hero actor" selected among existing actors with heuristics, or additionally inserted into the scene. It is parameterized by Intelligent Driver Model (IDM) heuristics and programmed to execute either a cut-in or a hard braking maneuver. Overall, this procedure provides reasonably fine-grained control over desired maneuvers and generates many new scenarios. We leverage rejection sampling to throw away simulations that fail a small set of basic checks due to a failure in the heuristics. This allows us to generate an order of magnitude more safety critical scenarios than we have mined from real logs. We also found that the diversity of the simulation generated scenarios helps improve the model performance. We created three versions of simulation data with different heuristics: one with the most safety-critical maneuvers, one with kinematic constraints (deceleration, TTC, etc.) approximately tuned to the real data. It turns out that using both versions of simulation data achieves the best performance.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-D Dataset", "weight": 1.0} -->

While the resulting behaviors themselves remain limited in diversity, empirically we will show that they still provide benefits and partially transfer to the real evaluation set.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-D Dataset", "weight": 1.0} -->

During training, we blend real and simulated scenarios using a hyperparameter $\alpha_{real}$, which determines the relative proportion of real and sim data. Each training batch has an $\alpha_{real}\%$ chance to draw a sample from the real dataset, and a $(1-\alpha_{real})\%$ chance to draw from a sim sample. This mechanism allows us to smoothly adjust the balance between realism and scalability, and to study the effect of sim--real composition on downstream performance. As real safety-critical data alone is too scarce to provide sufficient coverage of the scenario space, while sim-only data introduces a domain gap, $\alpha_{real}$ serves as a way to balance the two, which we empirically validate in Section V-D.

<!-- chunk {"id": "body-0037", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

We first evaluate end-to-end our approach's ability to generate realistic safety-critical scenarios. Section V-B shows that compared to baselines, scenarios generated by our approach more closely match held-out real safety-critical scenarios both quantitatively and qualitatively. Next, we investigate the first key aspect of our approach: our conditional flow architecture. We ablate our design choices and show that both conditioning and flow are important to achieving good results (Section V-C). The other key aspect of our approach is our data composition, and the use of simulation data to supplement real examples. In Section V-D, we evaluate our approach trained on various different data compositions and show that a simple balance of simulation and real safety-critical examples provides the best results. Finally, we study the controllability of our approach in Section V-E. We showcase how our model responds to the conditioning, and how intermediate flow timesteps can be an additional lever for controlling the specific degree of safety criticality.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-A1 Dataset", "weight": 1.0} -->

We conduct experiments with an in-house self-driving dataset. Our dataset spans both highway and urban driving, consisting of approximately 20,000 traffic scenarios. Each snippet contains 20s of driving data. Approximately 10,000 snippets are from real logs, 10,000 are simulated safety critical scenarios as described in Section IV-D. Additionally, as described in Section IV-D we have curated approximately 500 real safety critical snippets. The remaining training samples are also upsampled. We hold out 20% of the real safety critical data for evaluation.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-A2 Metrics", "weight": 1.0} -->

Evaluating a generative model for scenario generation is non-trivial and requires multiple metrics measuring realism and safety-criticality. We propose our experiments on the following suite of metrics. minSTTC and Near Miss Rate To evaluate if our method learns to construct near-miss cases from the training distribution, we propose a scenario-level minimum time to collision metric (minSTTC). For each scenario sample, we calculate the minimal time to collision between the ego actor and the closest leading actor throughout the entire rollout with an upper bound of 10 seconds. We report the median of the minSTTC because in the cases where no likely collision is going to happen, the minSTTC is likely to be large. We consider a more effective safety-critical scenario as inducing a small TTC without causing any collision. We also report the percentage of scenarios where the minSTTC is less than 3 seconds, which we consider as a near miss that challenges the planner.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-A2 Metrics", "weight": 1.0} -->

Distribution JSD Following common practice, we compute the distributional kinematics metrics of actors. Smaller divergence indicates that the model captures the essence of safety-critical maneuvers. We measure against common kinematic metrics that characterize actor maneuver: linear and angular speed and acceleration.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-A2 Metrics", "weight": 1.0} -->

Collision Rate We evaluate the average percentage of actors colliding in each scenario based on a small IOU threshold between the bounding boxes of the actors. Collision rate should generally be low even for safety-critical scenarios, since none of the ground truth data has any collisions. However, models can obtain low collision rate by generating nominal scenarios, so other metrics like minSTTC must also be considered.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-A2 Metrics", "weight": 1.0} -->

Reconstruction We also provide L2 reconstruction to the ground truth trajectory as another way to measure realism to supplement distribution JSD.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-B Generating Realistic Safety Critical Scenarios", "weight": 1.0} -->

We compare against 3 baselines *VAE* is the base model, trained on the same data as our approach.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-B Generating Realistic Safety Critical Scenarios", "weight": 1.0} -->

*VAE + Curation* is the base CVAE model, trained only on safety critical scenarios (both real and sim) *Strive* is a SOTA baseline which performs optimization in latent space. We use the same base CVAE as our approach.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-B Generating Realistic Safety Critical Scenarios", "weight": 1.0} -->

Table I shows the results. Compared with the baseline CVAE models, our model achieves comparable kinematics metrics while generating more safety-critical scenarios. Our model generates smaller minSTTC with higher near-miss rate. Because the baseline CVAE is trained on the base mixture distribution, it does not produce as many safety-critical scenarios, as we can see by its relatively worse minSTTC and Near Miss rate. Our VAE + Curation baseline obtains higher near miss rate but is less realistic overall. This is because the omitted nominal data still contains valuable learning signal, in particular for background traffic, etc. STRIVE also obtains a high near miss rate but suffers from realism. We believe that this is because the prior model does not provide strong enough regularization. Also, the adversarial optimization is not explicitly aware of the real world distribution of safety-critical scenarios. On the other hand our flow approach obtains the best of both worlds as it is able to generate a large percentage of near miss scenarios while maintaining good performance in the other metrics.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-B Generating Realistic Safety Critical Scenarios", "weight": 1.0} -->

Qualitatively (Fig. 3), we can see that with an ordinary highway scenario, our model perturbs the maneuver of the leading actor by causing it to perform a hard brake, leading the ego vehicle to follow as well. On the second occasion, the model causes the actor in the neighbor lane to cut into ego vehicle's lane aggressively, also causing a hard brake from the ego actor. One side benefit of the flow method is that the model automatically chooses the actor to interact with the ego vehicle as well as the maneuver to perform, so that there is no need for explicit interaction design.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-C Conditional Flow Ablation", "weight": 1.0} -->

We now ablate the key architectural choices of our approach: the flow transformer, and the additional conditioning. The flow-only model simply removes the conditioning from the flow transformer. For the conditioning-only model, we add a similar conditioning encoder to the VAE prior. Table I shows the results. As expected, without any flow or conditioning to steer the sampling, the base model has trouble generating safety critical rollouts. We see that conditioning on its own is also ineffective. Our hypothesis is that adding conditioning during the VAE training potentially harms representation learning as it potentially provides too much of a shortcut. On its own, flow is already effective, but adding conditioning to flow results in the best overall model.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-D Data Composition", "weight": 1.0} -->

We evaluate our model performance with different mixtures of real data in Table III. For these experiments, the same base VAE is used, but we adjust the mixed ratio of sim and real data when training the flow model. We see that using sim or real only is ineffective, due to lower fidelity data, and smaller scale data respectively. Combining them shows the best results, with a sweet spot at around 50%.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-E Controllability Studies", "weight": 1.0} -->

Controllability is another desired property for our model because it allows us to generate different levels of safety-critical scenarios, which could be used to gradually test the performance upper bound of the autonomy system. In this part, we compare the difference of the rollouts from the same initialization but with different maneuver labels. In Table IV, we show the performance of the model with different maneuver labels. We see minSTTC decreases and near-miss rate increases as the maneuver label becomes more challenging, while the unconditional model lies somewhere in between. We also found that controllability could also be achieved by manipulating the flow time steps. We sample the latents along the inference time steps and decode them to visualize the reconstruction. Fig. 4 shows that the model rollout is nominal at $t=0$, and becomes safety-critical at $t=1$, providing more refined control of scenario generation when used in conjunction with the maneuver labels.

<!-- chunk {"id": "body-0050", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

In this paper, we proposed Flow VAE, a method for data-driven safety-critical traffic scenario rollout generation. Flow VAE is a flow matching transformer that learns to transfer the latents from nominal initialization into safety-critical ones. We also show that using a mixture of sim and real data, we are able to scalably generate safety-critical scenarios with a small dataset. Our ablation studies validate our architectural and data composition design choices, and we further show multiple methods to control our model at varying granularity.

<!-- chunk {"id": "body-0051", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

Our real data curation and synthetic generation are proof-of-concept and can be improved. For instance higher fidelity vehicle models involving friction could better address sim-to-real and allow for more interesting scenarios involving slipping. Scaling up data collection and synthetic generation techniques could allow for increasingly diverse safety critical scenarios to be generated. While we showed controllability in the degree of safety criticality (through maneuver labels and number of flow timesteps), controlling the maneuver itself could be an interesting future direction.
