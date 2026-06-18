<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Realistic Traffic Agents in Closed-loop

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Realistic traffic simulation is crucial for developing self-driving software in a safe and scalable manner prior to real-world deployment. Typically, imitation learning (IL) is used to learn human-like traffic agents directly from real-world observations collected offline, but without explicit specification of traffic rules, agents trained from IL alone frequently display unrealistic infractions like collisions and driving off the road. This problem is exacerbated in out-of-distribution and long-tail scenarios. On the other hand, reinforcement learning (RL) can train traffic agents to avoid infractions, but using RL alone results in unhuman-like driving behaviors. We propose Reinforcing Traffic Rules (RTR), a holistic closed-loop learning objective to match expert demonstrations under a traffic compliance constraint, which naturally gives rise to a joint IL + RL approach, obtaining the best of both worlds. Our method learns in closed-loop simulations of both nominal scenarios from real-world datasets as well as procedurally generated long-tail scenarios. Our experiments show that RTR learns more realistic and generalizable traffic simulation policies, achieving significantly better tradeoffs between human-like driving and traffic compliance in both nominal and long-tail scenarios.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Moreover, when used as a data generation tool for training prediction models, our learned traffic policy leads to considerably improved downstream prediction metrics compared to baseline traffic agents.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Simulation is a critical component to safely developing autonomous vehicles. Designing realistic traffic agents is fundamental in building high-fidelity simulation systems that have a low domain gap to the real world. However, this can be challenging as we need to both capture the idiosyncratic nature of *human-like* driving and avoid unrealistic traffic *infractions* like collisions or driving off-road. Existing approaches used in the self-driving industry lack realism: they either replay logged trajectories in a non-reactive manner or use heuristic policies which yield rigid, unhuman-like behaviors. Using data-driven approaches to learn more realistic policies is a promising alternative.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The dominant data-driven approach has been imitation learning (IL), where nominal human driving data is used as expert supervision to train the agents. However, while expert demonstrations provide supervision for human-like driving, pure IL methods lack explicit knowledge of traffic rules and infractions which can result in unrealistic policies. Furthermore, the reliance on expert demonstrations can be a disadvantage, as long-tail scenarios with rich interactions are very rare, and thus learning is overwhelmingly dominated by more common scenarios with a much weaker learning signal.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement learning (RL) approaches encode explicit knowledge of traffic rules through hand-designed rewards that penalize infractions. These approaches do not rely on expert demonstrations and instead learn to maximize traffic-compliance rewards through trial and error. In the context of autonomy, this allows training on synthetic scenarios that do not have expert demonstrations in order to improve the robustness of learned policies. However, traffic rules alone cannot describe all the nuances of human-like driving, and it is still an open question if one can manually design a reward that can completely capture those intricacies.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Towards learning human-like and traffic-compliant agents, we propose Reinforcing Traffic Rules (RTR), a holistic closed-loop learning method to match expert demonstrations under a traffic-compliance constraint using both nominal offline data and additional simulated long-tail scenarios (Figure 1). We show our formulation naturally gives rise to a unified closed-loop IL + RL objective, which we efficiently optimize by exploiting differentiable dynamics and a per-agent factorization. In contrast to prior works that combine IL and RL, our closed-loop approach allows the model to understand the effects of its actions and suffers significantly less from compounding error. Furthermore, exploiting simulated long-tail scenarios improves learning by exposing the policy to more interesting interactions that would be difficult and possibly dangerous to collect from the real world at scale. Our experiments show that unlike a wide range of baselines, RTR learns realistic policies that better generalize to both nominal and long-tail scenarios *unseen during training*.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The benefits carry forward to *downstream tasks* such as simulating scenarios to train autonomy models; prediction models trained on data simulated with RTR have the strongest prediction metrics on real data, serving as further evidence that RTR has learned more realistic traffic simulation. We believe this serves as a crucial step towards more effective applications of traffic simulation for self-driving.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Learning Infraction-free Human-like Traffic Agents", "weight": 1.0} -->

To learn realistic infraction-free agents, we propose a unified learning objective to match expert demonstrations under an infraction-based constraint. We show how our formulation naturally gives rise to a joint closed-loop IL + RL approach which allows learning from both offline collected human driving data when possible, and additional simulated long-tail scenarios containing rich interactions that would otherwise be difficult or impossible to collect in the real world.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Learning", "weight": 1.0} -->

To learn a multiagent traffic policy that is as human-like as possible while avoiding infractions, we consider the reverse KL divergence to the expert distribution with an infraction-based constraint $\underset{\pi}{\arg\min}$ $D_{\text{KL}}\left( {{P^{\pi}{(\tau)}} \parallel {P^{E}{(\tau)}}} \right)$ s.t. ${{\mathbb{E}}_{P^{\pi}}\left\lbrack {R{(\tau)}} \right\rbrack} \geq 0$ $${R^{(i)}{({\mathbf{s}},a^{(i)})}} = \begin{cases}
\end{cases}$$ where $R^{(i)}$ is a per-agent reward function that penalizes any infractions (collision and off-road events).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Learning", "weight": 1.0} -->

For a rich learning environment, we consider both a dataset $D$ of nominal expert trajectories $\tau^{E} \sim P^{E}$ collected by driving in the real world, and additional simulated *long-tail scenarios*. Unlike real world logs, these scenarios contain what we denote as *hero* agents, which induce interesting interactions like sudden cut-ins, etc. (details in Section 3.4). More precisely, let $\pi_{\theta}$ be our learner policy. Let ${\mathbf{s}}_{0}^{S} \sim \rho_{0}^{S}$ be the initial state sampled from the long-tail distribution and $\pi_{{\mathbf{s}}_{0}}^{S}$ represent the policy of the hero agent. The overall multiagent policy is given as

<!-- chunk {"id": "body-0012", "role": "body", "section": "Learning", "weight": 1.0} -->

The overall initial state distribution is then given as $\rho_{0} = {{{({1 - \alpha})}\rho_{0}^{D}} + {\alpha\rho_{0}^{S}}}$, where $\rho_{0}^{D}$ corresponds to the offline nominal distribution, and $\alpha \in {\lbrack 0,1\rbrack}$ is a hyperparameter that balances the mixture.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Learning", "weight": 1.0} -->

Taking the Lagrangian of Equation 8 decomposes the objective into an IL and RL component,

<!-- chunk {"id": "body-0014", "role": "body", "section": "Learning", "weight": 1.0} -->

where $\lambda$ is a hyperparameter balancing the two terms, and $H{(\pi)}$ is an additional entropy regularization term ^22^2The causal entropy term is included as an entropy regularizer in some learning algorithms such as PPO. In our setting, we empirically found that it was not necessary to include.. Notably, we optimize IL and RL jointly in a closed-loop manner, as the expectation is taken with respect to the on-policy distribution $P^{\pi}{(\tau)}$. Compared to open-loop behavior cloning, the closed-loop IL component allows the model to experience states induced by its own policy rather than only the expert distribution, increasing its robustness to distribution shift. Furthermore, while the additional reward constraint may not change the optimal solution of the unconstrained problem (the expert distribution may be infraction-free), it can provide additional learning signal through RL.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Learning", "weight": 1.0} -->

The RL component ${\mathbb{E}}_{P^{\pi}}\left\lbrack {R{(\tau)}} \right\rbrack$ can be optimized using standard RL techniques and exploits both offline-collected nominal scenarios and simulated long-tail scenarios containing rich interactions. However, the imitation component $\mathcal{L}^{\text{IL}}$ is only well-defined when expert demonstrations are available and thus only applied to nominal data. We start from an initial state ${\mathbf{s}}_{0}^{E} \sim \rho_{0}^{D}$ and have the policy $\pi_{\theta}$ control all agents in closed-loop simulation.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Learning", "weight": 1.0} -->

The loss is the distance between the ground truth and policy-induced trajectory ^33^3 As we do not have access to $P^{E}$ directly to query log-likelihood, using a distance is essentially making the assumption that ${P^{E}{(\tau)}} \propto {\exp\left\lbrack {- {D{(\tau^{E},\tau)}}} \right\rbrack}$..

<!-- chunk {"id": "body-0017", "role": "body", "section": "Learning", "weight": 1.0} -->

It is difficult to obtain accurate action labels for human driving data in practice, so we only consider states in our loss, i.e. ${D{(\tau^{E},\tau)}} = {\sum_{t = 1}^{T}{d{({\mathbf{s}}_{t}^{E},{\mathbf{s}}_{t})}}}$ where $d$ is a distance function (e.g. Huber).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Learning", "weight": 1.0} -->

Optimization: To optimize Equation 4, we first note that the $\mathcal{L}^{IL}$ component is differentiable by using the reparameterization trick when sampling from the policy^44^4We found that directly using the mean action provides good results without the need for sampling. and differentiating through the transition dynamics (kinematic bicycle model). We refer the reader to the appendix for more details. To optimize the $\mathcal{L}^{RL}$ component, we design a centralized and fully observable variant of PPO. While it is possible to directly optimize the policy with the overall scene reward ${R{({\mathbf{s}},{\mathbf{a}})}} = {\sum_{i = 1}^{N}{R^{(i)}{({\mathbf{s}},a^{(i)})}}}$, we instead optimize each agent individually with their respective individual reward $R_{i}{({\mathbf{s}},a_{i})}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Learning", "weight": 1.0} -->

While this factorized approach may ignore second-order interaction effects, it considerably simplifies the credit assignment problem leading to more efficient learning. More precisely, we compute factorized value targets $V^{(i)} = {\sum_{t = 0}^{T}{\gamma^{t}R_{t}^{(i)}{({\mathbf{s}}_{t},a_{t}^{(i)})}}}$, and the factorized PPO policy loss is given as $\mathcal{L}^{\text{policy}} = {\sum_{i = 1}^{N}{\min{({r^{(i)}A^{(i)}},{\text{clip}{(r^{(i)},{1 - \epsilon},{1 + \epsilon})}A^{(i)}})}}}$ where the probability ratio is factorized, i.e. $r^{(i)} = {{{\pi{(\left.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

Our traffic model $\pi_{\theta}$ architecture uses common ideas from SOTA traffic agent motion forecasting literature in order to extract context and map features and predict agent actions (Figure 2). Recall that a state ${\mathbf{s}} = {\{ s^{},\ldots,s^{(N)},{\mathbf{m}}\}}$ consists of each individual agent's states $s^{(i)}$ that contain the agent's kinematic state over a history horizon $H$, and an HD map $\mathbf{m}$. From each agent's state history, a shared 1D CNN and GRU are used to extract agent history context features $h_{a}^{(i)} = {f{(s^{(i)})}}$. At the same time, a GNN is used to extract map features from a lane graph representation of the map input $h_{m} = {g{({\mathbf{m}})}}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

A HeteroGNN then jointly fuses all agent context features and map features before a shared MLP decodes actions for each agent independently.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

We use independent normal distributions to represent the joint agent policy, i.e. ${\pi{(\left. a^{(i)} \middle| {\mathbf{s}} \right.)}} = {\mathcal{N}{(\mu^{(i)},\sigma^{(i)})}}$, and thus ${\pi{(\left. {\mathbf{a}} \middle| {\mathbf{s}} \right.)}} = {\prod_{i = 1}^{N}{\pi{(\left. a^{(i)} \middle| {\mathbf{s}} \right.)}}}$. Note that agents are only independent *conditional* on their shared past context, and thus important interactive reasoning is still captured.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

Our value model uses the same architecture but does not share parameters with the policy; we compute $\{ h_{0}^{v},\ldots,h_{N}^{v}\}$ in a similar fashion, and decode per-agent value estimates ${\hat{V}}^{(i)} = {\text{MLP}^{v}{(h^{(i)})}}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Simulated Long-tail Scenarios", "weight": 1.0} -->

Nominal driving logs can be monotonous and provide weak learning signal when repeatedly used for training. In reality, most traffic infractions can be attributed to rare and long-tail scenarios belonging to a handful of scenario families which can be difficult and dangerous to collect from the real world at scale. In this work, we procedurally generate long-tail scenarios to supplement nominal logs for training and testing. Following the self-driving industry standard, we use *logical scenarios* which vary in the behavioral patterns of particular hero agents with respect to an ego agent (e.g. cut-, hard-braking, merging, etc.). Designed by expert safety engineers, each logical scenario is parameterized by $\theta \in \Theta$ which controls lower-level aspects of the scenario such as behavioral characteristics of the hero agent (e.g. time-to-collision or distance triggers, aggressiveness, etc.), exact initial placement and kinematic states, and geolocation. A *concrete scenario* can then be procedurally generated in an automated fashion by sampling a logical scenario and corresponding parameters $\theta$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Simulated Long-tail Scenarios", "weight": 1.0} -->

While these scenarios cannot be used for imitation as they are simulated and do not have associated human demonstrations, they provide a rich reinforcement learning signal due to the interesting and rare interactions induced by the hero agents.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experiments", "weight": 1.0} -->

Scenario sets: Our experiments use two datasets that represent nominal and long-tail scenarios respectively. The Nominal dataset consists of a set of highway logs which capture varying traffic densities and road topologies while containing expert demonstrations. The dataset consists of 465 snippets for training and 115 for testing, where each snippet lasts for 20 seconds. We use LongTail to denote the scenario set generated using the process outlined in Section 3.4 which contain rare actor maneuvers like sudden cut-ins. We use 25 logical scenarios to generate a total of 333 concrete scenarios, where 167 concrete scenarios are used for training and 166 are held-out for evaluation. This evaluation set is held-out on the parameter level and measures in-distribution generalization. We also evaluate on an additional set of held out logical scenarios to measure out-of-distribution generalization, with more details in Section 4.1.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experiments", "weight": 1.0} -->

Metrics: We evaluate our traffic models' ability to 1) match human-like driving and 2) avoid infractions. For the former, we measure similarity to the demonstration data by computing the final displacement error (FDE), which measures the L2 distance between the agent's simulated and ground truth (GT) position after 5 seconds. Furthermore, we use Jensen-Shannon Divergence (JSD) between histograms of scenario features (agent acceleration) in order to measure distributional realism. Finally, to measure infraction rates, we consider collision and driving off-road. We use a bootstrap resampling over evaluation snippets to compute uncertainty estimates. Results with more extensive metrics (and their definitions) can be found in the appendix.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Benchmarking Traffic Models", "weight": 1.0} -->

Comparison to state-of-the-art: We evaluate RTR and several baselines on both nominal and long-tail scenarios. For comparability, we use the same input representation and model architecture as described in Section 3.3 for all methods. Our first two baselines are representative of state-of-the-art imitation learning approaches for traffic simulation. BC is our single-step behavior cloning baseline following. The IL baseline is trained using closed-loop policy unrolling. Next, RL is trained using our proposed factorized version of PPO with the reward in Equation 20. The RL-Shaped baseline includes an additional reward for driving at the speed-limit to encourage more human-like driving. Finally, BC+RL is an RL augmented BC baseline following.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Benchmarking Traffic Models", "weight": 1.0} -->

Figures 3 and 4 show the results; a full table can be found in the appendix. Firstly, the BC model achieves poor realism because it suffers from distribution shift during closed-loop evaluation as it encounters states unseen during training due to compounding error. Next, we see RL achieves low infraction rates but results in unhuman-like driving (Figure 5). This is because it is difficult for reward alone to capture realistic driving. Efforts in reward shaping result in improvements but are ultimately still insufficient. We see BC+RL improves upon BC infractions but still lacks realism. This is because BC is an open-loop objective and only provides signal in expert states, while only the RL signal is present in non-expert states. Thus, the policy still suffers from compounding error with respect to imitation. On the other hand, closed-loop IL performs better as it is more robust to compounding error, but still struggles on the long-tail scenario set without explicit supervision. Finally, the *holistic* closed-loop IL and RL approach of RTR improves infraction rates while maintaining reconstruction and JSD metrics.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Benchmarking Traffic Models", "weight": 1.0} -->

We see RTR outperforms even pure RL in terms of infraction rate on long-tail scenarios, suggesting that including long-tail scenarios during training can help the model generalize to held-out evaluation long-tail scenarios.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Benchmarking Traffic Models", "weight": 1.0} -->

Out-of-distribution generalization: Recall from Section 3.4 that logical scenarios define a family of scenarios and concrete scenarios define variations within a family. While we have evaluated in-distribution generalization by using held-out concrete scenarios, we further evaluate on *held-out logical scenarios*. We use 11 held-out logical scenarios with new map topologies and behavioral patterns to procedurally generate an additional out-of-distribution set consisting of 84 concrete scenarios. Our results show that RTR generalizes to this set better than baselines (Figure 7, Table 7).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Downstream Evaluation", "weight": 1.0} -->

One downstream application of traffic simulation is generating synthetic data for training autonomy models. We evaluate if the improved realism of RTR transfers in this context. Each model is used to generate a synthetic dataset of 589 scenarios which we use to train a SOTA prediction model before evaluating its performance on held-out real data. Besides FDE, the cross-track error (CTE) of predicted trajectories projected onto the GT are used as prediction metrics. More experiment details can be found in the appendix. Table 1 shows that using RTR to generate training data results in the best prediction model. This provides evidence that RTR has learned more realistic behavior and has a lower domain gap compared to baselines, showing that our approach can improve the application of traffic simulation in developing autonomous vehicles.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Additional Analysis", "weight": 1.0} -->

Long-tail scenarios: We evaluate our approach of using procedurally generated scenarios against the alternative of mining hard scenarios from data by curating a set of logs from Nominal that the IL model commits an infraction. Figure 9 shows that using only curated scenarios does not transfer well to the long-tail set, and in fact introduces a regression in the nominal scenarios, suggesting the model is overfitting to the curated scenarios. Up-sampling curated scenarios (Nom+Cur) also fails -- relying purely on offline data may require prohibitively larger scale data collection.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Additional Analysis", "weight": 1.0} -->

Factorized multiagent RL: To ablate our factorized per-agent approach to multiagent PPO, we compare to a standard PPO implementation where the scene-level reward $R{({\mathbf{s}},{\mathbf{a}})}$ is used as supervision for the joint policy rather than each individual agent reward $R^{(i)}{({\mathbf{s}},a^{(i)})}$. Figure 9 shows that the factorized loss outperforms the alternative, likely due to the fact that multiagent credit assignment is extremely difficult when using the scene-level reward, leading to poor sample efficiency.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Additional Analysis", "weight": 1.0} -->

Balancing the trade-off: Recall from Section 3.2 that RTR balances human-like driving and avoiding infractions by weighting the IL vs. RL loss with $\lambda$ and nominal vs. long-tail training with $\alpha$ (e.g. $\lambda = \alpha = 0$ is the IL baseline). We found increasing the relative weight of RL and long-tail scenarios generally improves infraction avoidance while increasing the relative weight of IL and nominal training generally improves other realism metrics as expected (Table 2). However, RTR is not particularly sensitive; many configurations are within noise and all configurations dominate the baseline Pareto frontier.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Additional Analysis", "weight": 1.0} -->

Imitation learning signal: We consider the alternative of using a frozen pretrained IL policy as regularization instead of our approach of using offline data. A frozen policy potentially provides more accurate closed-loop supervision, as a Euclidian-based distance loss with demonstration data may be inaccurate if the rollout has diverged. We evaluate two baselines: KL Reward and KL Loss, where the KL between the current and frozen policy is added to the reward or loss respectively. Our results in Table 3 show that using demonstration data is still the most performant, suggesting that the inaccuracy from an imperfect IL policy is larger than that of using a distance-based loss.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Conclusion and Limitations", "weight": 1.5} -->

We have presented RTR, a method for learning realistic traffic agents with closed-loop IL+RL using both real-world logs and procedurally generated long-tail scenarios. While we have shown substantial improvements over baselines in simulation realism and downstream tasks, we recognize some existing limitations. Firstly, while using logical scenarios as a framework for procedural generation exploits human prior knowledge and is currently an industry standard, manually designing scenarios can be a difficult process, and ensuring an adequate coverage of all possible scenarios is an open problem. Exploring automated alternatives like adversarial approaches to scenario generation would be an interesting future direction. Secondly, while we have explored the downstream task of generating an offline dataset to train prediction models, other applications like training and testing the entire autonomy stack end-to-end in closed-loop is a promising future direction.
