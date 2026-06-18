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

Our key insight in driving scenarios is that interactions between agents follow an inherent causal structure: each agent's actions depend primarily on the states of a subset of nearby agents. Following this observation, we frame the problem as a Constrained Factored Markov Decision Process (MDP), shaped by these causal dependencies to mirror real-world interactions. Unlike previous approaches that manage conflicts between controllability and realism through reweighting, we directly utilize the causal structure by selectively masking agents with conflicting behaviors. This structure enables our model to uphold both realism and controllability constraints simultaneously, even in safety-critical situations. To implement this approach, we introduce the Causal Composition Diffusion model (CCDiff)---a structure-enhanced diffusion model that combines structure-aware classifier-free guidance with compositional classifier-based guidance. By integrating these elements, our model achieves a balanced, flexible generation of realistic and controllable driving scenarios, as demonstrated in Figure.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We formulate the learning of controllable and realistic closed-loop simulation as a constrained optimization problem, which aims to maximize the user's control preferences while satisfying realism constraints.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose CCDiff, a principled algorithm to solve the constrained optimization problem by identifying the causal structure and injecting it as a structured guidance to the diffusion model.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We systematically evaluate the performance of CCDiff with state-of-the-art in closed-loop scenario generation on the nuScenes dataset, showing benefits in the controllability and realism in generating safety-critical driving scenarios.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Causal reasoning for behavior models", "weight": 1.0} -->

Causal reasoning has seen extensive applications in trajectory modeling, with previous studies leveraging causal structures to enhance the robustness and generalizability of open-loop behavior prediction models. These efforts have included causal representation learning, backdoor adjustment, counterfactual analysis, and realistic causal interventions. Despite these advances, applying a causal approach to broader trajectory prediction tasks often demands substantial human annotation efforts. To address the challenges of automating spatiotemporal reasoning in traffic scenarios, state-of-the-art methods employ factorized attention mechanisms. However, while previous work applies causal structured reasoning primarily in open-loop settings, the efficacy of causal behavior modeling in closed-loop scenarios for autonomous driving remains under-explored.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Generative models for traffic simulation", "weight": 1.0} -->

Prior arts balance the trade-off between realism and controllability in safety-critical scenario generation by incorporating various constraints, such as inference-time sampling strategies, retrieval-augmented generation, low-rank fine-tuning, and language-conditioned generation. In closed-loop simulation methods, compositional constraints in the training loss are often integrated into the simulation pipeline. For instance, TrafficSim achieves a balance between realism and common sense using a time-adaptive multi-task loss design; SimNet factorizes trajectory sequences using Markov processes; STRIVE imposes structured priors to constrain samples, avoiding unrealistic outcomes; and BITS optimizes closed-loop performance via bi-level imitation. Yet these prior methods struggle to resolve conflicts between controllability and realism objectives when these are at odds during inference.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Diffusion model for sequential decision making", "weight": 1.0} -->

Diffusion models have shown strong controllability in density estimation and generation tasks. Scenario Diffusion adopts latent diffusion, utilizing multi-source conditioning to generate realistic scenarios. In closed-loop traffic simulation, several prior works incorporate compositional classifier-based guidance to steer the diffusion model's sampling process, including signal temporal logic (STL) guidance, language-based guidance, adversarial guidance, and game-theoretic guidance.
