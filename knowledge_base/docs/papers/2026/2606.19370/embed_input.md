<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Human-like Autonomy Emerges from Self-play and a Pinch of Human Data

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Self-play reinforcement learning has recently emerged as a way to train driving policies without any human data. It uses cheap, large-scale simulations to substitute expensive, large-scale human driving demonstrations. A key limitation of this approach is that policies trained through pure self-play can learn effective but alien driving conventions incompatible with people. Previous works attempt to mitigate such behavioral misalignments through extensive reward engineering and domain randomization, which are brittle and labor-intensive. Instead of completely discarding human demonstrations, our method treats them as a regularization objective on top of a minimal safe goal-reaching reward. Like the spice in a good stew, we find that a little human data goes a long way: our method uses only 30 minutes of human demonstrations, 2500x fewer than comparable imitation learning approaches. Resulting policies coordinate with held-out human trajectories and complete training in 15 hours on a single consumer-grade GPU. Videos and full source code are available at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Self-play reinforcement learning (RL) has produced superhuman agents in strategic games and, more recently, has shown promise in real-world domains, such as autonomous driving. The approach elegantly sidesteps a central difficulty in multi-agent learning - how to model the opponent - through the following idea: the agent's opponent is a copy of itself. The appeal here is that as the agent improves, so does its co-player. This gives rise to an automatically evolving curriculum that takes the policy from random play to skilled behavior entirely through synthetic simulated experience.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In zero-sum games, this mechanism, with a sparse measure for success (e.g., +1 when winning a game of chess), is enough to produce strong play against arbitrary opponents. Many real-world settings, however, are not zero-sum. Driving, for instance, can be viewed as a mixed-motive game: each player has individual objectives (reaching a destination safely) but must also coordinate with other road users by adhering to shared norms, expectations, and conventions. Self-play RL with only a high-level objective for success provides no guarantees of such alignment; policies may converge to effective but "alien" strategies that are incompatible with human partners. Concretely, an agent trained to "reach a destination safely" may very well learn to do so in reverse, sideways, or on the wrong side of the road if such constraints are not specified in the reward.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Previous works have addressed such misalignment in two ways. One line of work involves manual reward engineering, where reward terms are added iteratively until the desired behavior and conventions emerge. While effective, this strategy is labor-intensive by nature, domain-specific, and brittle since it is not trivial to figure out what reward will produce the desired human-like behavior. A case in point is GIGAFLOW, which required nine individually tuned reward terms and several other domain randomization techniques to produce naturalistic and cautious driving policies. On the other side of the spectrum, we have Imitation Learning \[13, 14, 15, IL\]. In IL, the policy is optimized to directly imitate human driving data, avoiding the need for defining a reward function altogether. However, robustness requires wide state coverage, so these approaches typically need large quantities of human demonstrations.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We take a different approach, grounded in a practical observation about the changing cost structure of experience generation. Modern RL frameworks and simulation infrastructure can generate between 300K and 20M environment steps per second on a single consumer-grade GPU, making synthetic experience generation effectively limitless. Human driving data, by contrast, requires manual collection and remains slow to scale. This suggests a natural role for human data in coordination games: not as the primary source of training signal, but as a lightweight anchor that steers the policy away from effective yet behaviorally alien strategies. Indeed, regularizing self-play RL toward such an anchor has shown promise in producing human-compatible agents in Diplomacy and driving, yet how much data is required to reach human compatibility remains, to our knowledge, unexamined.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We measure it. Anchoring self-play RL to human driving data from the Waymo Open Motion Dataset \[23, WOMD\], we find that a surprisingly small amount of demonstration data improves coordination with human proxies. Paired with roughly 60 years of self-play experience, 30 minutes of human driving data (0.04% of the full WOMD training set) yields a marked improvement, without doing any reward engineering or domain randomization. The effect mirrors an analogy already present in the literature: it is well documented that injecting a small fraction of detrimental data can cause catastrophic model degradation, a phenomenon known as data poisoning. To our knowledge, we are the first to report a comparable effect in the opposite direction within self-play RL; a small fraction of beneficial data disproportionately improves behavior. Much like a pinch of cayenne changes the flavor of an entire dish, a small amount of human data appears to alter the behavior of a self-play policy. Reflective of this effect, we call this data spicing, and name our method spiced self-play.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Concretely, we train a PPO policy under a sparse reward for safe goal reaching, while regularizing it toward a behavioral cloning anchor fit to a small amount of human driving data. We observe that: 30 minutes to 3 hours of human driving data, combined with self-play at scale, is sufficient to improve coordination with human proxies without reward engineering or domain randomization (Figure 1; Sections 4.1, 4.3).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Spiced policies not only have lower collision rates, they also display more human-like behavior in terms of distributional realism and collision severity profiles (Section 4.2).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

To make it easy to reproduce and build on the current results, we open-source the full codebase. Policies can be trained end-to-end in 15 hours on a single consumer-class GPU.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Imitation learning for autonomous driving", "weight": 1.0} -->

The generation of driving policies is a fundamental challenge across end-to-end autonomous driving, multi-agent trajectory prediction, and reactive traffic simulation. Driven by the widespread availability of large-scale human driving datasets, imitation learning has become the dominant approach across all these domains. Under this imitation learning paradigm, a broad spectrum of methodologies has emerged to fit models to historical data, ranging from marginal and joint forecasting to autoregressive sequence modeling of tokenized trajectories and continuous distribution learning via diffusion and promptable world models. While these generative approaches yield diverse open-loop behaviors, they are fundamentally constrained by the scale of human data required and frequently suffer from compounding covariate shift in closed-loop deployment. To mitigate these shifts, recent hybrid approaches integrate reinforcement learning, yet they typically still rely on extensive human driving data as their primary optimization signal. Our approach systematically inverts this balance: rather than depending on human driving data as the core supervisor, we utilize synthetic, multi-agent RL self-play as the primary engine for discovering robust interactive behaviors, retaining a remarkably small human dataset strictly as a behavioral anchor to ensure conformity to realistic traffic norms.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Self-play reinforcement learning in games", "weight": 1.0} -->

Self-play reinforcement learning has produced superhuman agents in games from Go and Chess to StarCraft II and Stratego, all without human data. Superhuman play is not the same as human-compatible play, however. Many games admit multiple equilibria, and self-play need not converge to equilibria that are compatible with human partners. The failure has been shown in cooperative games such as Hanabi and Diplomacy, where self-play agents develop internally consistent conventions that transfer poorly to human partners. The cause is reward underspecification: when the reward is defined as a score to maximize, there are often many ways to achieve it. In other words, the solution space is large. Previous work attempts to resolve this by designing the reward by hand. For instance, GIGAFLOW demonstrates that reward engineering and domain randomization can produce naturalistic behavior at scale, at the cost of nine individually tuned reward terms. We avoid reward engineering entirely. A small amount of human data serves as a behavioral anchor, and self-play does the rest. This reduces a labor-intensive design problem to a one-hour data collection procedure.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Human-regularized self-play reinforcement learning and search", "weight": 1.0} -->

One alternative to reward engineering is to regularize self-play toward a human anchor policy. This idea has been explored in Diplomacy, where KL regularization toward a human prior during both search and learning produced agents that coordinate more effectively with human partners. Jacob et al. study KL-regularized search more broadly and show that it recovers human-like play across several games. In autonomous driving, the idea has been explored at a limited scale. Previous work showed improved human-likeness and coordination with log-replays through regularized self-play RL in autonomous driving. However, the authors were bottlenecked by experience-generation speed: their simulator ran at 2,000 steps per second. As a result, the policies were trained on only 140 million self-play transitions across 200 scenarios, which required five days of wall-clock time and left little room to study data scaling. More recently, Chang et al. demonstrated that KL-regularized self-play can yield human-like driving policies using SMART as the behavioral anchor.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Human-regularized self-play reinforcement learning and search", "weight": 1.0} -->

Notable differences to their setup include: 1)Vulnerable road users (VRUs; pedestrians and cyclists) were replayed from human data during training, which conflates the anchor's contribution with that of the mixed-in human trajectories and precludes a clean analysis of where the impact comes; 2) Their behavioral anchor is a large tokenized model trained on the full 500,000-scenario Waymo dataset; 3) Policies were trained on 1 billion training transitions, particularly due to the high cost of running inference on SMART. We scale self-play to 20 billion steps, control all agents during self-play training to preclude human contamination of collected human data, and systematically study how much human anchor data is needed to improve human compatibility.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem setup", "weight": 1.0} -->

A human-compatible agent should blend in with human drivers. We approximate interaction with human road users by replaying logged human trajectories in simulation. We evaluate in three settings, illustrated in Figure 2: Self-play. All agents are controlled by the same policy in a decentralized manner.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem setup", "weight": 1.0} -->

Human-replay. Only the self-driving car (SDC) is controlled by the policy; all other agents follow their logged trajectories.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem setup", "weight": 1.0} -->

IDM. The SDC is controlled by the policy; all other agents follow the Intelligent Driver Model, following a precomputed lane-center path for lateral control and using longitudinal accelerations of IDM to maintain a safe gap between the lead vehicle.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem setup", "weight": 1.0} -->

An effective and human-compatible agent should reach its goal without collisions or off-road events across all three settings, each of which probes a distinct failure mode. Human-replay tests whether the policy has internalized human driving conventions against non-reactive co-players. IDM introduces closed-loop dynamics with reactive rule-based co-players. Self-play tests internal consistency and additionally serves as a convergence sanity check.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Metrics", "weight": 1.0} -->

We report several metrics that capture task performance. The score is an aggregate metric; an agent scores 1 if it completes the task of driving to a goal destination before the end of the episode without colliding or going off-road, and 0 otherwise. To diagnose failure modes, we separately report collision rate, at-fault collision rate, off-road rate, and route progress. An ideal agent should score well with its own population as well as the human-replay population. Score-based metrics capture whether agents complete their task safely, but not whether their behavior looks human. We therefore also report distributional realism using the Waymo Open Sim Agent Challenge to compare their behavior to logged trajectories. Finally, we also analyze the severity of the at-fault collisions. Metrics are reported on held-out test scenarios unless stated otherwise; see full definitions and details in Appendix D.2.

<!-- chunk {"id": "body-0020", "role": "body", "section": "World initialization", "weight": 1.0} -->

We use PufferDrive 2.0 for simulation and training. Environments are initialized from the Waymo Open Motion Dataset \[23, WOMD\]: each 9-second scenario provides a roadgraph, a variable set of agents (cars, cyclists, pedestrians) up to $N=32$, and per-agent initial poses and goals drawn from the logs. Each agent is goal-conditioned on a target destination ($x,y$ position) and receives a partial, decentralized, ego-frame observation consisting of its own state, the $N-1$ closest neighbors within 50 m, and up to 128 nearby road segments (road edges, lanes and lines). World initialization and observation space details are provided in Appendix A.1 and A.2, respectively.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Reward function", "weight": 1.0} -->

To isolate the effect of human driving data, we avoid reward engineering and use a sparse reward: $+1$ for reaching the goal, $-1$ for collision or off-road events, and $0$ otherwise. Any differences in human-like behavior, therefore, stem from BC regularization rather than a hand-tuned reward. Episodes terminate once all agents reach their destinations, and we filter out transitions from agents that reach their goals early.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Spiced Self-Play Reinforcement Learning", "weight": 1.0} -->

Spiced self-play is regularized self-play RL anchored to a small amount of human demonstration data (here driving logs). The anchor is a behavioral cloning policy fit to this data, which regularizes self-play through a KL penalty. We train policies in two stages: a behavioral cloning (BC) anchor is first fit to human data, then frozen and used as a regularizer during self-play RL.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Step 1: Train the anchor policy", "weight": 1.0} -->

To study how the amount of human data affects downstream performance, we train anchor policies on subsets of the full dataset $\mathcal{D}=\{(o_{t}^{i},a_{t}^{i})\}_{i=1}^{T\cdot K}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Step 1: Train the anchor policy", "weight": 1.0} -->

We sample subsets $\mathcal{D}_{n}$ corresponding to $n$ scenarios, yielding roughly $\{10\text{ min},30\text{ min},3\text{ h},30\text{ h}\}$ of human driving data, and fit each anchor ${\color[rgb]{0.85546875,0.46484375,0.3359375}\definecolor[named]{pgfstrokecolor}{rgb}{0.85546875,0.46484375,0.3359375}\tau_{\phi^{n}}}$ by minimizing negative log-likelihood: We use only the self-driving car (SDC) trajectory from each scenario to generate our imitation data, as it is typically the highest-quality trajectory.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Step 1: Train the anchor policy", "weight": 1.0} -->

Each anchor ${\color[rgb]{0.85546875,0.46484375,0.3359375}\definecolor[named]{pgfstrokecolor}{rgb}{0.85546875,0.46484375,0.3359375}\tau_{\phi^{n}}}$ is then frozen for the subsequent self-play stage. Full details are in Appendix A.4.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Step 2: Regularized self-play RL", "weight": 1.0} -->

We train ${\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pi_{\theta}}$ from scratch using Proximal Policy Optimization \[27, PPO\]. The policy $\pi_{\theta}$ is represented by a 650k-parameter neural network.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Step 2: Regularized self-play RL", "weight": 1.0} -->

Each anchor ${\color[rgb]{0.85546875,0.46484375,0.3359375}\definecolor[named]{pgfstrokecolor}{rgb}{0.85546875,0.46484375,0.3359375}\tau_{\phi^{n}}}$ serves as a behavioral regularizer via a KL penalty: where $\rho_{{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pi_{\theta}}}$ is the on-policy state distribution and $\lambda\geq 0$ controls regularization strength.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Step 2: Regularized self-play RL", "weight": 1.0} -->

The KL term pulls ${\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pi_{\theta}}$ toward the anchor on states the policy actually visits, rather than on the offline distribution of $\mathcal{D}_{n}$. Hyperparameters and training details are in Appendices A.1 and B.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experiments", "weight": 1.0} -->

This section summarizes the key results. Additional details and analyses are reported in the appendices. We structure the sections to answer the following questions: Scaling human driving data for regularized self-play RL: How much human data is needed for strong performance in both self-play and human-replay evaluations? (Section 4.1) Behavior and safety analysis: How does a small amount of human demonstration data shape policy behavior beyond task performance? We analyze the effect on distributional realism, collision severity, and driving style (Section 4.2).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments", "weight": 1.0} -->

The role of metadata and scenario diversity: Driving datasets such as WOMD and NuPlan provide scenario metadata---road graphs and initial agent positions---that ground simulation at a fraction of the cost of collecting human driving data. How does the number of training scenarios (maps) used for self-play influence agent performance? (Section 4.3)

<!-- chunk {"id": "body-0031", "role": "body", "section": "Scaling Human Driving Data for Regularized Self-Play RL", "weight": 1.0} -->

How much collected human driving data does regularized self-play need, and how does this compare to imitation learning-only based approaches? It is worth noting that one reason the second question matters is that any apparent data efficiency on our side could simply reflect the homogeneity of the Waymo Open Dataset rather than an actual property of the method. We benchmark against unregularized self-play RL; a goal-conditioned RL policy that is trained to reach a goal without colliding with other agents or going off-road (Section 3.1). This provides a human-data-free lower bound. We also benchmark to SMART-tiny-CLSFT, the state-of-the-art IL approach in this domain. SMART is trained on the same nested driving data subsets; we additionally include the open-sourced SMART-tiny-CATK checkpoint, trained on all 500k WOMD training scenarios, as an IL upper bound (Appendix B.3).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Scaling Human Driving Data for Regularized Self-Play RL", "weight": 1.0} -->

Human demos used reg. self-play (ours) reg. self-play (ours) reg. self-play (ours) reg. self-play (ours) Table 1: Performance versus amount of human demonstrations for the best trained policies on 10k held-out randomly sampled scenarios. For SMART, we report the best-performing variant at each data scale (details Appendix G.1). Top-3 values per column are highlighted (best, 2nd, 3rd); the best value per column is additionally shown in bold. The unregularized self-play row uses no human driving data.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Spiced self-play RL surpasses IL with a fraction of the human driving data", "weight": 1.0} -->

As shown in Figure 3 and Table 1, spiced self-play outperforms SMART-tiny-CLSFT across all data regimes and metrics. With as little as 30 minutes to 3 hours of human data, spiced self-play achieves the lowest at-fault collision rate (0.6-0.7%); a 2.5$\times$ improvement over SMART-tiny-CLSFT trained on the entire Waymo train dataset (52 days; 1.6%). The advantage is most pronounced at low human data: at 30 minutes, spiced self-play yields an 11$\times$ reduction in at-fault collision rate and 46$\times$ in self-play collision rate relative to SMART. Against standard self-play RL (at-fault CR: 2.1%; ), spiced self-play achieves a 3.5$\times$ improvement, demonstrating the value of an anchor trained on minimal human data as a regularizer. Regularized self-play RL with the 30-hour anchor leads to similar results.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Self-play exposes agents to a changing population of partners", "weight": 1.0} -->

The environment of a self-play RL policy is non-stationary: early policies have near-random behavior and become increasingly competent. This is in contrast to a single-agent RL setting, where the partner distribution is fixed. We observe that the self-play setting is associated with an increase in convergence to mutually consistent conventions. Spiced self-play agents achieve low collision rates in both self-play and cross-play with human logs (below 1.5% in each). SMART, trained on 52 days of human data, incurs a 6% self-play collision rate but only 1.6 % when paired with logs. Two factors can explain this gap: sample count (20 billion transitions versus 225 million for SMART, Figure 1) and training paradigm (SMART is optimized open-loop for log-likelihood, then finetuned closed-loop to stay near the log distribution, and is never exposed to the partner distribution self-play naturally provides). To test for the role of the partner distribution, we compare self-play agents with agents trained directly against the human-replay population (single-agent RL against static partners).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Self-play exposes agents to a changing population of partners", "weight": 1.0} -->

The latter perform well within that population (at-fault collision rate 0.2--0.3%) but do worse in self-play (0.8--1.2%). This is consistent with exposure to reactive, evolving partners contributing to robustness (Figure 19).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Behavior and Safety Analysis", "weight": 1.0} -->

The goal of this section is to understand the behavioral differences between unregularized and regularized self-play policies beyond straightforward performance metrics.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Spiced policies exhibit lower-severity collisions", "weight": 1.0} -->

Collision rates, as reported in Sections 4.1 and 4.3, measure how often agents fail, but not how bad the failures are. This distinction matters when policies are deployed alongside humans. Following Waymo's most recent safety report, we quantify collision severity via the change in velocity at impact ($\Delta v$), a widely studied proxy for occupant injury risk. As shown in Table 9 and Figure 4, regularization reduces both the frequency and the severity of failures. The mean per-event $\Delta v$ drops from $2.09$ m/s to $1.71$ m/s, and the maximum observed impact velocity falls from $13.71$ m/s to $8.09$ m/s. The improvement is more apparent when we focus on the tail of collision events: $14.3\%$ of unregularized collisions exceed $15$ mph, the threshold above which serious injury risk rises substantially, compared to $7.5\%$ for the regularized model.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Spiced policies exhibit lower-severity collisions", "weight": 1.0} -->

The survival curve in Figure 4 (right) shows the two groups are nearly indistinguishable at low $\Delta v$, with the gap opening sharply above $5$ m/s and widening through the severe range. Regularization thus produces policies that not only collide less often but also cause less damage when they do collide.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Regularized self-play improves realism with minimal data", "weight": 1.0} -->

Unregularized self-play scores 0.680 on the WOSAC meta-score, with the largest deficits in the kinematic and interactive groups. Anchoring to 30 minutes of human data increases this to 0.725; the meta-score does not improve with additional data, suggesting BC anchor quality is the limiting factor. SMART-tiny CLSFT achieves the highest realism score (0.755), yet underperforms on collision rate and task completion across every data bin (Section 4.1), confirming that distributional similarity to logged human trajectories does not necessarily imply safety or competence. Additional results and graphs are in Appendix F.3.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Regularized policies display more social driving behavior", "weight": 1.0} -->

We perform a qualitative analysis with representative videos available at The most salient difference is that regularized policies are more considerate of surrounding traffic: they maintain greater following distances, avoid cutting, and yield at intersections relative to unregularized self-play agents. RL policies are trained to maximize the expected cumulative discounted return. An undesirable side-effect of this is that policies tend to achieve their task in the least number of steps possible. This is different than what humans do. A human driver will aim to get to her destination on time, but is not trying to get there as quickly as possible; satisficing rather than optimizing. As visible in the videos and supported by the average episode length, regularization partially corrects for this: regularized agents complete their episodes in 64 steps on average ($\pm 3.5$), compared to 38 ($\pm 2.6$) steps for unregularized self-play.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Regularized policies display more social driving behavior", "weight": 1.0} -->

This effect is also visible in the displacement errors to the human-replays in Table 2, which we decompose into a longitudinal component (along the direction of travel) and a lateral component (perpendicular to it). Lateral error reflects whether the policy follows the human's path through the scene (e.g., lane choice, turns) while longitudinal error reflects whether it travels that path at a human-like pace. A policy that rushes ahead stays on the right route but reaches each point too early or too late. We observe a clear difference: the unregularized longitudinal L2 (13.33 m) is over five times its lateral L2 (2.39 m). Regularization more than halves the longitudinal error (to 5.56 m) and nearly halves the lateral error (to 1.27 m), so the regularized policy follows human-like paths and traverses them at a human-like speed. The videos confirm both effects: the large longitudinal gap comes from unregularized RL policies driving very fast, and the lateral gap usually comes from their swerving around the replayed logs.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Scenario diversity is essential for learning general policies", "weight": 1.0} -->

Aside from human driving data, a cheaper source of simulation grounding data is scenario metadata: road graphs, initial positions, and velocities. Recent work has shown that regularized self-play RL grounded by target-city metadata can adapt driving policies to new cities. A natural follow-up question is how much the diversity provided by metadata matters for training generalizable policies, which is what we explore here. We train regularized and unregularized self-play RL agents on subsets $\mathcal{M}_{k}$ with $|\mathcal{M}_{k}|\in\{10,100,1{,}000,10{,}000,50{,}000\}$ scenarios, holding the BC anchors $\tau^{n}$ and reward function $r$ fixed. This isolates the effect of environment initialization and diversity besides the agent behaviors.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Scenario diversity is essential for learning general policies", "weight": 1.0} -->

We find that the number of training scenarios (a proxy for map diversity) is an important ingredient for generalization, both to held-out maps and to the human-replay population. As shown in Figure 5, both unregularized and regularized self-play improve drastically with the amount of metadata. For unregularized self-play, the at-fault collision rate drops from 14% at 10 scenarios to 0.5-1% at 50k scenarios, and the human-replay collision rate falls from 25.2% to 2% over the same range. Regularized self-play follows the same trend and reaches lower absolute values: with a 30-min BC anchor, the human-replay at-fault collision rate drops from 14% at 10 scenarios to 0.7% at 50k scenarios. The gap between the self-play performance (pairing policy with itself) and the human-replay population approaches 0.2% for regularized policies, and is 1.5% for unregularized self-play.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We consider a series of experiments aimed at putting the mixing of human driving data with synthetic simulated experience on a more scientific footing. Our central finding is that a small amount of human data, roughly 30 minutes to 3 hours of human driving data, can dramatically move the needle towards human-compatible driving agents. This is three orders of magnitude less than SOTA imitation learning baselines and is achieved without reward engineering or domain randomization techniques. The broader implication is that when simulation is cheap, and some clear metrics for desirable behavior are available, human driving data may be best used not as the primary training signal but as a lightweight anchor that steers policies away from effective-but-alien equilibria.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Limitations", "weight": 1.5} -->

Robustness in tight coordination scenarios: We perform an additional analysis to better understand the limitations of the resulting regularized policies. We curate a small dataset consisting of the top 200 most difficult interactive scenarios (see Appendix D.1). Repeating the analysis from Section 4.1 on this set of harder scenarios shows that, while the ranking of the policies holds (reg. self-play RL policies still outperform the SMART and unregularized self-play baselines by the same margins), the absolute at-fault collision rate increases from 0.7% to 2.1-2.8%. This indicates that there is room for improvement in the robustness of the resulting policies. Arguably, not all of these contacts reflect policy failures: some are caused by replay agents cutting abruptly into the SDC's lane, leaving almost no physically feasible avoidance response. What constitutes a fair collision-avoidance benchmark beyond at-fault heuristics is itself a difficult open question in both industry and academia. Nevertheless, an important direction for future work is to improve the robustness of regularized policies. See Appendix G for the results, an in-depth discussion, and ideas to improve along this axis.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Limitations", "weight": 1.5} -->

External validity of evals: Our evaluations use human replays and IDM-controlled agents in simulation as proxies for coordination with humans. The extent to which performance in these settings transfers to on-road deployment remains an open question.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Limitations", "weight": 1.5} -->

Sensitivity to the anchor: Many underlying details by which regularizing the RL policy to the pre-trained BC anchor improves human-likeness remain incompletely understood. How do the properties of the anchor distribution, such as its entropy, affect the outcome? Results show that the regularized policies substantially outperform their anchors (see Figure 9, Table 7), indicating that RL corrects for at least some suboptimal behavior in the anchor. It is unclear how sensitive this is to the BC policy's closed-loop quality, or how the correction occurs precisely.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Combining human demonstrations with synthetic simulated experience", "weight": 1.0} -->

Our key finding raises a deeper question that we have only touched the surface of, but is worth exploring further. Given the ability to generate simulated self-play experience on demand, what is the complementary value of a bit of human data? Can we predict how much human data, and of what kind, is worth collecting for a given application X with structure Y? In the present work, we can loosely intuit two effects. First, the resulting regularized self-play RL policies are more human-like because the actor distributions stay close to the anchor distributions (see Section F.2). Second, the resulting policies are more robust because they are exposed to broader coverage of the state space during training: the self-play agents learn from 20B transitions and start from random play, whereas the IL baseline is trained on a fixed dataset of 225 million expert transitions (Figure 1, Center). But count is a crude explanation; not all transitions are equally informative. Recent work on epiplexity takes a step toward formalizing this notion of data value, but in its current form, is a theoretical measure that we cannot yet compute or apply to data selection in practice.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Combining human demonstrations with synthetic simulated experience", "weight": 1.0} -->

Developing tools to help determine what kind of human data is needed to learn a given behavior, and predicting how much is needed before collecting it, is a promising direction for future work.
