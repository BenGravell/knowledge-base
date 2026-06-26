<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Causal Composition Diffusion Model for Closed-loop Traffic Generation

Topics include Autonomous driving, Safety, Diffusion models, Causal inference, Datasets, Benchmarks, Optimization, Control, Learning, Closed-loop.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Simulation is critical for safety evaluation in autonomous driving, particularly in capturing complex interactive behaviors. However, generating realistic and controllable traffic scenarios in long-tail situations remains a significant challenge. Existing generative models suffer from the conflicting objective between user-defined controllability and realism constraints, which is amplified in safety-critical contexts. In this work, we introduce the Causal Compositional Diffusion Model (CCDiff), a structure-guided diffusion framework to address these challenges. We first formulate the learning of controllable and realistic closed-loop simulation as a constrained optimization problem. Then, CCDiff maximizes controllability while adhering to realism by automatically identifying and injecting causal structures directly into the diffusion process, providing structured guidance to enhance both realism and controllability. Through rigorous evaluations on benchmark datasets and in a closed-loop simulator, CCDiff demonstrates substantial gains over state-of-the-art approaches in generating realistic and user-preferred trajectories. Our results show CCDiff's effectiveness in extracting and leveraging causal structures, showing improved closed-loop performance based on key metrics such as collision rate, off-road rate, FDE, and comfort.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reliable closed-loop traffic simulation is essential for assessing autonomous vehicle (AV) safety in diverse and complex scenarios. Simulations must be both realistic, capturing the intricacies of real-world driving, and controllable, allowing customization aligned with user preferences. However, balancing realism with controllability remains a significant challenge. Previous works often prioritize one aspect, optimizing either realism or user-specified objectives. How to jointly achieve both objectives under safety-critical conditions remains fruitful yet unresolved.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Traffic agent simulation often resorts to either (i) data-driven approaches that generate the most probable trajectories based on scene context or (ii) rule-based approaches that maximize alignment with a user's control. However, both approaches face key limitations for effective scenario generation.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Data-driven scenario generation faces two primary challenges. First, the rarity of collision and near-miss events in public datasets limits the ability of data-driven methods to generate safety-critical scenarios. As shown in prior studies, even a small domain mismatch, such as changes in road structure or the behavior of surrounding vehicles, can cause significant regressions. Second, closed-loop simulation requires that generated trajectories continuously interact with the simulated environment, so current predictions influence future predictions. This feedback loop often creates compounding errors, leading to distributional shifts that challenge the generation of both controllable and realistic behaviors over long horizons.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

On the other hand, rule-based approaches to simulation offer precise user control, but often fail to capture the nuanced, adaptive behaviors of real-world driving, especially in unpredictable scenarios. Their rigidity can make generated behaviors feel scripted and unrealistic, particularly in closed-loop simulations where each action influences future states. This lack of adaptability often leads to compounding errors and a drift from realistic behavior distributions, limiting their effectiveness in complex, long-horizon interactions.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent advances in deep generative models have enabled scalable traffic behavior simulation, facilitating realistic scenario generation from massive offline datasets. Notably, prior works compose explicit rules into scenario generation, such as causal graphs (CG), signal temporal logic (STL), or large language models (LLM), which act as structured constraints to improve the controllability. However, interactive driving scenarios cannot be fully encapsulated by explicit rules alone. Rule-based models struggle to generalize effectively in many safety-critical corner cases, where certain rules may need to be adapted.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our key insight in driving scenarios is that interactions between agents follow an inherent causal structure: each agent's actions depend primarily on the states of a subset of nearby agents. Following this observation, we frame the problem as a Constrained Factored Markov Decision Process (MDP), shaped by these causal dependencies to mirror real-world interactions. Unlike previous approaches that manage conflicts between controllability and realism through reweighting, we directly utilize the causal structure by selectively masking agents with conflicting behaviors. This structure enables our model to uphold both realism and controllability constraints simultaneously, even in safety-critical situations. To implement this approach, we introduce the Causal Composition Diffusion model (CCDiff)---a structure-enhanced diffusion model that combines structure-aware classifier-free guidance with compositional classifier-based guidance. By integrating these elements, our model achieves a balanced, flexible generation of realistic and controllable driving scenarios, as demonstrated in Figure 1. Our contributions can be summarized as follows: We formulate the learning of controllable and realistic closed-loop simulation as a constrained optimization problem, which aims to maximize the user's control preferences while satisfying realism constraints.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose CCDiff, a principled algorithm to solve the constrained optimization problem by identifying the causal structure and injecting it as a structured guidance to the diffusion model.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We systematically evaluate the performance of CCDiff with state-of-the-art in closed-loop scenario generation on the nuScenes dataset, showing benefits in the controllability and realism in generating safety-critical driving scenarios.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Causal reasoning for behavior models", "weight": 1.0} -->

Causal reasoning has seen extensive applications in trajectory modeling, with previous studies leveraging causal structures to enhance the robustness and generalizability of open-loop behavior prediction models. These efforts have included causal representation learning, backdoor adjustment, counterfactual analysis, and realistic causal interventions. Despite these advances, applying a causal approach to broader trajectory prediction tasks often demands substantial human annotation efforts. To address the challenges of automating spatiotemporal reasoning in traffic scenarios, state-of-the-art methods employ factorized attention mechanisms. However, while previous work applies causal structured reasoning primarily in open-loop settings, the efficacy of causal behavior modeling in closed-loop scenarios for autonomous driving remains under-explored.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Generative models for traffic simulation", "weight": 1.0} -->

Prior arts balance the trade-off between realism and controllability in safety-critical scenario generation by incorporating various constraints, such as inference-time sampling strategies, retrieval-augmented generation, low-rank fine-tuning, and language-conditioned generation. In closed-loop simulation methods, compositional constraints in the training loss are often integrated into the simulation pipeline. For instance, TrafficSim achieves a balance between realism and common sense using a time-adaptive multi-task loss design; SimNet factorizes trajectory sequences using Markov processes; STRIVE imposes structured priors to constrain samples, avoiding unrealistic outcomes; and BITS optimizes closed-loop performance via bi-level imitation. Yet these prior methods struggle to resolve conflicts between controllability and realism objectives when these are at odds during inference.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Diffusion model for sequential decision making", "weight": 1.0} -->

Diffusion models have shown strong controllability in density estimation and generation tasks. Scenario Diffusion adopts latent diffusion, utilizing multi-source conditioning to generate realistic scenarios. In closed-loop traffic simulation, several prior works incorporate compositional classifier-based guidance to steer the diffusion model's sampling process, including signal temporal logic (STL) guidance, language-based guidance, adversarial guidance, and game-theoretic guidance.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Diffusion model for sequential decision making", "weight": 1.0} -->

Appendix Table 4 systematically compares the key features among the prior works and our proposed approach. While related works often focus on generating rule-compliant normal scenarios or enhancing safety-critical scenarios purely through classifier guidance, a fundamental challenge of achieving a balance between controllability and realism under safety-critical conditions remains unresolved.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Constrained Factored Markov Decision Process", "weight": 1.0} -->

We formulate the closed-loop traffic simulation as an MDP problem, then utilize diffusion model for sequential modeling to learn a controllable simulation policy $\pi$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Diffusion Model for Sequence Modeling", "weight": 1.0} -->

We then solve the traffic simulation inspired by the recent advancement in diffusion-guided sequential data generation. Denote ${{\mathbf{τ}}{(k)}} \triangleq {\{{({{\mathbf{s}}_{t}{(k)}},{{\mathbf{a}}_{t}{(k)}})}\}}_{t = 1}^{T}$ represent the joint state-action trajectory at the $k$-th diffusion step, $k \in {\{ 0,1,\cdots,K\}}$, where ${\mathbf{τ}}{}$ denotes the original clean trajectory. The forward diffusion process, acting on ${\mathbf{τ}}{}$, gradually corrupts it with Gaussian noise: where $\beta_{1},\ldots,\beta_{K}$ are pre-defined variance schedules at each diffusion step.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Diffusion Model for Sequence Modeling", "weight": 1.0} -->

Over the forward process, the trajectory is transformed into a standard Gaussian distribution: ${q{({{\mathbf{τ}}{(K)}})}} \approx {\mathcal{N}{(\mathbf{0},{\mathbf{I}})}}$. For scenario generation, the reverse diffusion process iteratively denoises from noise to recover the original trajectories. Given a context $\mathbf{c}$ (e.g., map features), the reverse process is: where ${p{({{\mathbf{τ}}{(K)}})}} = {\mathcal{N}{(\mathbf{0},{\mathbf{I}})}}$ is the Gaussian prior, and ${\mathbf{π}}_{\phi,\psi}$ is the scene encoder parameterized by $\phi,\psi$, which will be covered in later sections.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Realism Constrained Score Matching", "weight": 1.0} -->

‣ 3.1 Constrained Factored Markov Decision Process ‣ 3 Problem Formulation ‣ Causal Composition Diffusion Model for Closed-loop Traffic Generation"), with known transition (vehicle) dynamics, we can factorize the objective of the optimal closed-loop scenario generation as follows: | | $\max$ | $P\left(\mathcal{O}_{\sqcup}\Im\infty\Leftrightarrow{\mathbf{τ}}_{\sqcup}\clubsuit{\mathbf{τ}}_{\sqcup\nwarrow\infty}\Rightarrow\Leftrightarrow\max\mathcal{P}\Leftarrow\mathcal{O}_{\sqcup}\Im\infty\clubsuit{\mathbf{τ}}_{\sqcup}\Rightarrow\mathcal{P}\Leftarrow{\mathbf{τ}}_{\sqcup}\clubsuit{\mathbf{τ}}_{\sqcup\nwarrow\infty}\Rightarrow\Leftrightarrow \right.$ | |

<!-- chunk {"id": "body-0019", "role": "body", "section": "Realism Constrained Score Matching", "weight": 1.0} -->

We denote $\nabla\log P \triangleq \nabla\log P{(\mathcal{O}_{\sqcup}\Im\infty\Leftrightarrow{\mathbf{τ}}_{\sqcup}\clubsuit{\mathbf{τ}}_{\sqcup\nwarrow\infty}\Rightarrow}$ The score function of the maximum likelihood objective in equation can be written as: Unlike the normal scenarios where optimizing the imitation basically adheres with the rule compliance reward, safety-critical guidance $R^{(j)}$ can suffer from gradient conflict. Namely, for some ${i \in {\lbrack 1,N\rbrack}},{j \in {\lbrack 1,d_{r}\rbrack}}$, if using a weighted sum of all the objectives as classifier-based guidance would achieve sub-optimal performance, as illustrated in Figure 2(b).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Realism Constrained Score Matching", "weight": 1.0} -->

In order to resolve this gradient conflicting issues, we need to prioritize to control the agents index $i \in {\lbrack N\rbrack}$ that could maximize the reward while maintaining a high likelihood of the learned policies, i.e., a lower realism gap between the learned policies and behavior policies $\pi_{\beta}$: ${\mathbb{D}}{({\pi_{\beta} \parallel \hat{\pi}})}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Proposed Method: CCDiff", "weight": 1.0} -->

We hereby introduce CCDiff to optimize the simulation policy $\pi$ of equation in a scalable and efficient way by decomposing the constrained optimization problem into several small components. We illustrate the pipeline in Figure 2(a). To promote realism, CCDiff first encodes the motion histories of different agents based on the spatial attention, then discovers the decision causal graph $G$ based on the factorized attention masks and kinematic factors. CCDiff then utilizes causal interactive patterns in $G$ to extract the importance rank $\mathbf{ρ}$. Finally, CCDiff optimizes its controllability by masking out those unimportant agents based on $\mathbf{ρ}$ to guide the diffusion reverse sampling process in a structured way. We zoom into the details below.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Causal Composition Scene Encoder", "weight": 1.0} -->

Inspired, the goal of causal composition scene encoder is to generate the most likely action under a parsimonious decision causal graph $G$ with Lagrangian multiplier $\lambda_{\text{sparsity}}$: We parameterize our model $\pi_{\phi,\psi}{(\left. {\mathbf{a}}_{t} \middle| {{\mathbf{s}}_{t},{\mathbf{c}},k;G} \right.)}$ for scenario generation with a transformer-based structures for temporal attention $\phi$, spatial attention modules $\psi$, as well as some decision causal graph $G$. The model output ${\mathbf{a}}_{t}$ is conditioned on the agents' history ${\mathbf{s}}_{t}$, map context $\mathbf{c}$, and diffusion sample step $k$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Causal Composition Scene Encoder", "weight": 1.0} -->

Similar to the scene transformer structure, we first embed the history of ego and surrounding agents with temporal attention layer: $\phi_{\text{ego}}{(s_{t}^{(i)})},\phi_{\text{others}}{({\mathbf{s}}_{t}^{{({- i})}\rightarrow{(i)}})}\rbrack$, here $s_{t}^{(i)}$ is the history of the $i$-th agents, and ${\mathbf{s}}_{t}^{{({- i})}\rightarrow{(i)}}$ are the relative history of all the other agents than $i$. To facilitate the relational reasoning, we incorporate both the absolute and relative features in $\phi_{\text{others}}{(\cdot)}$, including the position, velocity, distance, and time-to-collision (TTC).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Causal Composition Scene Encoder", "weight": 1.0} -->

Then we can aggregate all the temporal information into the following spatial cross-attention layer: In order to further discover useful spatial parent-to-child relationships, we design a two-step causal reasoning to identify the DCG in the spatial-temporal interaction of the traffic agents. First, we set a hard constraint over the neighborhood perception field by trimming down the unnecessary causal connection between agents' states and corresponding actions at time-step $t$. Second, we apply the first tunable hard constraint as a memory mask to the attention weights: where the memory mask $M$ is extracted with relative TTC features $f_{\text{TTC}}{(\cdot)}$ with the surrounding agents given the threshold $C_{\text{ttc}}$ of causal graph $G$: In practice, we can tune the threshold of $C_{\text{ttc}}$ here to control the sparsity of the final causal graph. We then aggregate the map information $\mathbf{c}$ into the decoder.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Causal Ranking", "weight": 1.0} -->

We then use the identified DCG to rank the agents' importance to the safety-critical objectives $R^{(j)}{({\mathbf{τ}})}$: To automate the ranking process, we resort to the estimated causal graph $G$ above. The causal composition scene encoder gives us $G$ and a policy network $\pi_{\phi,\psi}{(\left. {\mathbf{a}}_{t} \middle| {{\mathbf{s}}_{t};G} \right.)}$. Then we design a graph-based community detector on the DCG $G$, then sort the time of occurrences in any cliques for all the nodes from $1$ to $N$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Causal Ranking", "weight": 1.0} -->

After sorting, we have the ranked id sequence ${\{{\rho_{i}{(\tau)}}\}}_{i = 1}^{N}$, then we can pick the top $N_{c}$ key agents ${\{{\rho_{i}{(\tau)}}\}}_{i = 1}^{N_{c}}$ at the scene, which represent the most densely interactive with the other agents. This ranking process empirically helps identify the most interactive and influential agents for the safety-critical objective. We further discuss in the appendix with more details about the specific design of relational features $\phi$ and the community detection algorithms we used.\

<!-- chunk {"id": "body-0027", "role": "body", "section": "Causal Composition Guidance", "weight": 1.0} -->

For the diffusion guidance process, similar to the inpainting technique, we aim to trim down the controllable space by reducing the number of controllable agents with cause-and-effect ranking. With the causal reasoner and importance ranker modules, we sorted out the key agents ${\{{\rho_{k}{(\tau)}}\}}_{k = 1}^{K}$. We then apply both classifier-based and classifier guidance.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Causal Composition Guidance", "weight": 1.0} -->

In CCDiff, we derive a special form of classifier-free guidance as a combination of unconditional scene encoding and causal interventional encoding. At timestep $t$, for the top-$N_{c}$ controllable agents $i \in {\{{{\mathbf{ρ}}_{N_{c}}{(\tau_{t})}}\}}_{i = 1}^{N_{c}}$, the classifier-free guidance is: where $w$ is the guidance scale. For agent $i$, $\pi_{\phi,\psi}{(\left. a_{t}^{(i)} \middle| s_{t}^{(i)} \right.)}$ is the unconditional distribution that only considered the ego histories $\phi{(s_{\text{ego}})}$, and $\pi_{\phi,\psi}{(\left.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Causal Composition Guidance", "weight": 1.0} -->

a_{t}^{(i)} \middle| {\text{PA}_{t}^{G}{(i)}} \right.)}$ is the intervened encoded results given some parental agents in causal graph $G$. This formulation implies that the guided distribution corresponds to a geometric mixture: Thus, classifier-free guidance in diffusion models can be viewed as a do-intervention by specifying the causal parents of $i$-th agents in DCG during the generative process. The guidance scale $w \in {\lbrack 1,2)}$ acts analogously to the strength of intervention, extrapolating the original and intervened distributions. With the causal ranking, we mask out the agents with conflicted gradients as a reweighted classifier-based guidance: In practice, we use the distance-based guidance objective over the trajectories, including the map collision guidance and the agent collision guidance. We also use the same classifier function for all the baseline methods, see detailed description in the appendix C.3.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Training and Inference", "weight": 1.0} -->

We train the model with using the classical DDPM diffusion with classifier-free guidance. Specifically, the loss we solve is $\min_{\phi,\psi}{{\mathbb{G}}\left\| {{\pi_{\phi,\psi}{({{\mathbf{τ}}{(k)}},{\mathbf{c}},k;{G{(\tau)}})}} - {{\mathbf{a}}{}}} \right\|^{2}}$. We introduce counterfactual conditions by randomly dropping the DCG $G$ of the scene transformer by replacing the decision causal graph $G$ as a diagonal matrix, so all agents' actions are only conditioned on the ego history. At inference time, we combine both classifier-based and classifier-free guidance to facilitate better controllability, see algorithm 1.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Training and Inference", "weight": 1.0} -->

Dropout puncond, threshold Cρ, Cttc Guidance loss {𝒥i}i = 1N, trajectories τ, map c. while k = K, …, 1 do ⊳ Inference Sampling G(τ) ← M(τ) ⋅ αattn ⊳ Causal masking ρ(τ) ← ranking(G) ⊳ Importance ranking ${{\mathbf{a}}{({k - 1})}}\leftarrow{{{\mathbf{a}}{({k - 1})}} + {\sum_{i = 1}^{d_{r}}{{{{\mathbf{ρ}}_{i}{(\tau)}} \cdot {\nabla R}}{({\mathbf{s}},{{\mathbf{a}}{({k - 1})}})}}}}$ τ(k − 1) ← fdyn(s, a(k − 1)) ⊳ Vehicle dynamics return Generated trajectory τ. Algorithm 1 CCDiff for Scenario Generation

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiment", "weight": 1.0} -->

In the following parts of the experiments, we aim to answer the following three research questions (RQs): RQ1: Under different sizes of total controllable agents, how are the realism and controllability of the safety-critical scenarios generated by CCDiff compared to the baselines? RQ2: With a longer generation horizon and lower frequency, how are the realism and controllability of the safety-critical scenarios generated by CCDiff compared to the baselines? RQ3: How much does the causal reasoning module in CCDiff contribute to the overall performance?

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiment", "weight": 1.0} -->

The remaining parts of the experiment section first introduce our experiment settings, then compare our methods with baselines in the controllability and realism to answer the research questions. Finally, we conduct ablation studies to show the effect of individual modules in CCDiff.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Datasets", "weight": 1.0} -->

We use the nuScenes dataset and traffic behavior simulation (tbsim) for model training and evaluation. We train all models on scenes from the train split and evaluate on 100 scenes randomly sampled from the validation split. During evaluation phase, we initialize all the models with the same set of initial layouts and initial history trajectories of 3 seconds, the model is responsible of generating the future 10 seconds of trajectories for the driving agents in a closed-loop manner.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Baselines", "weight": 1.0} -->

We implement the following baselines in the above platform settings. To systematically illustrate the effectiveness of CCDiff, we include the following SOTAs for comparison: SimNet, TrafficSim, BITS, Strive, and CTG. We compare all the baselines with CCDiff in the publicly available nuScenes dataset and baseline implementations^11^1 For a fair comparison with all the baselines, we use the rasterized map used in the previous works and encode them with ResNet-18 for the map conditioning $\mathbf{c}$ for all the methods.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Metrics", "weight": 1.0} -->

We compare the performance of CCDiff and all the baselines with the following categories of metrics: Controllability Score (CS): we use the scenario-wise collision rate (SCR) used in as the controllability metrics. Among all the testing scenarios, we calculate the proportion of the scenarios where at least one collision event occurred between different agents. We then standardize SCR among all the methods to get the CS, a higher-the-better score between 0 and 1.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Metrics", "weight": 1.0} -->

Realism Score (RS): How to quantify realism is an open problem in evaluating traffic scenarios. In order to get a more interpretable and direct way to quantify realism, we adopt three widely-used quantitative metrics to evaluate the realism of the scenarios: (i) scenario off-road rate (ORR) used, (ii) final displacement error (FDE, $m$) and (iii) comfort distance (CFD), which is used in in to quantify the realism of the similarity in the smoothness of agents' trajectories in the generated scenarios. We standardize all the metrics among all the methods respectively and average them to get the RS, a higher-the-better score between 0 and 1.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Metrics", "weight": 1.0} -->

Multi-objective optimization metrics: with the RS and CS, we further quantify the optimality of the solution based on generational distance (GD) and inverted generational distance (IGD), the average minimum distance between the methods and Pareto frontier.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Multi-agent Scenario Generation (RQ1)", "weight": 1.0} -->

To address RQ1, we train our model on the training split of the nuScenes dataset and vary the number of controllable agents from 2 agents to the full sets of agents for all baselines at inference time by running a closed-loop generation at 2$Hz$ (0.5$s$). We then evaluate the CS and RS of generated scenarios under different numbers of controllable agents and report the comparison between CCDiff with SOTAs in Table 1 ‣ 5 Experiment ‣ Causal Composition Diffusion Model for Closed-loop Traffic Generation") and Figure 4(a).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Multi-agent Scenario Generation (RQ1)", "weight": 1.0} -->

From the table, we can see that CCDiff outperforms SimNet, TrafficSim, and BITS in both controllability and realism for almost all the cases, whereas TrafficSim only outperforms CCDiff in one controllability score. STRIVE shows some good controllability in generating safety-critical scenarios, yet its realism score is the poorest among all. The closest competitor, CTG, shows comparable performance in realism, yet CCDiff outperforms CTG in the controllability metrics, especially when the size of controllable agents goes larger as we gradually scale up the number of controllable agents from 2 to 5 and eventually to the full size of agents at the scene. From Figure 4(a), we can also see that CCDiff enjoys significantly better realism and controllability score on the most upper right side, Pareto front More detailed results for the SCR, ORR, FDE, and CFD are illustrated in the appendix Table 5. The consistent benefits of CCDiff in RS and CS compared to other baselines confirm that composing causal structure in the diffusion model facilitates the algorithm to generate reasonable safety-critical scenarios.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Multi-agent Scenario Generation (RQ1)", "weight": 1.0} -->

We also show qualitative studies for long-horizon generation in the Appendix Figure 28.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Long-horizon Closed-loop Generation (RQ2)", "weight": 1.0} -->

To address RQ2, we evaluate CCDiff's performance in long-horizon safety-critical scenario generation by changing the simulation frequency in $T$ seconds. We test the generation results with $T \in {\{{0.5s},{1s},{2s},{3s},{4s},{5s}\}}$, which corresponds to a closed-loop simulation frequency between 0.2$Hz$ to 2$Hz$. We demonstrate the comparison of realism and controllability results in Table 2 ‣ 5 Experiment ‣ Causal Composition Diffusion Model for Closed-loop Traffic Generation") and Figure 4(b). CCDiff consistently outperform BITS and STRIVE in both CS and RS as the planning horizon enlarges. TrafficSim outperforms all the other baselines with the best controllability, while its realism in long-horizon generation is second-worst and only better than BITS. SimNet marginally outperforms CCDiff in realism, yet its controllability is the worst among all. CCDiff outperforms CTG with a comparable realism score and higher controllability at longer horizons.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Long-horizon Closed-loop Generation (RQ2)", "weight": 1.0} -->

Figure 4(b) confirms our approach has the best proximity to the multi-objective Pareto frontier and has best coverage in the realistic zone. We also show qualitative studies for long-horizon generation in Appendix Figure 11-29.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Ablation study (RQ3)", "weight": 1.0} -->

To answer RQ3, we evaluate our methods with different ablation variants related to the causal composition, including (i) CCDiff w/o encoder, which removes sparsity constraints $\lambda_{\text{sparsity}}$ of the causal composition scene encoder, (ii) CCDiff w/o factored guide, which replaces the factorized guidance with the whole state space guidance, (iii) CCDiff w/ human and (iv) CCDiff w/ distance which replace the causal ranking algorithms with distance-based ranking and human ranking. We demonstrate the quantitative results in Table 6. The non-causal guidance variants and non-causal encoder variants show a performance drop in the collision rate (controllability), yet the w/o encoder variants outperform in kinematic comfort. Among all the ablation variants, different ranking strategies result in the largest performance drop for the multi-agent controllable generation settings.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Ablation study (RQ3)", "weight": 1.0} -->

Compared to our causal ranking, human ranking and distance-based ranking strategy suffers from a performance drop with 5 to 10% in the collision rate and, more than 0.5% in the off-road rate, 1$m$ for FDE, and also larger CFD. This signifies the importance of applying the proper guidance to the correct agents at the traffic scene when doing safety-critical generation.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we propose CCDiff, a causal composition diffusion model that aims to improve the controllability and realism in closed-loop safety-critical scenario generation for autonomous driving. Based on the formulation of constrained factored MDP, CCDiff promotes realism by first identifying the underlying causal structure between agents, then incorporating it in the scene encoder and ranking the importance of agents based on causal knowledge. CCDiff uses both interventional classifier-free guidance and masked classifier guidance to improve controllability in safety-critical scenario generation. In multi-agent generation and long-horizon generation settings, CCDiff outperforms SOTA methods over nuScenes data in closed-loop evaluation. One limitation of the current work is that the design of the causal reasoning pipeline relies on hyperparameter tuning and it is hard to directly evaluate. It would be interesting to construct a traffic reasoning benchmark and incorporate a foundation model to further scale up the traffic reasoning and generation process.
