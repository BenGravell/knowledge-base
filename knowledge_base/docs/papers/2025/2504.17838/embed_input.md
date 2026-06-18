<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

CaRL: Learning Scalable Planning Policies with Simple Rewards

Topics include Autonomous driving, Reinforcement learning, Policy learning, Policy optimization, Sample efficiency.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Shows that privileged RL for autonomous-driving planning can scale better with a simple route-completion reward than with heavily shaped reward sums. CaRL is notable for treating reward simplicity as the enabling ingredient for large-batch PPO and strong closed-loop driving performance.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We investigate reinforcement learning (RL) for privileged planning in autonomous driving. State-of-the-art approaches for this task are rule-based, but these methods do not scale to the long tail. RL, on the other hand, is scalable and does not suffer from compounding errors like imitation learning. Contemporary RL approaches for driving use complex shaped rewards that sum multiple individual rewards, \eg~progress, position, or orientation rewards. We show that PPO fails to optimize a popular version of these rewards when the mini-batch size is increased, which limits the scalability of these approaches. Instead, we propose a new reward design based primarily on optimizing a single intuitive reward term: route completion. Infractions are penalized by terminating the episode or multiplicatively reducing route completion. We find that PPO scales well with higher mini-batch sizes when trained with our simple reward, even improving performance. Training with large mini-batch sizes enables efficient scaling via distributed data parallelism. We scale PPO to 300M samples in CARLA and 500M samples in nuPlan with a single 8-GPU node.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The resulting model achieves 64 DS on the CARLA longest6 v2 benchmark, outperforming other RL methods with more complex rewards by a large margin. Requiring only minimal adaptations from its use in CARLA, the same method is the best learning-based approach on nuPlan. It scores 91.3 in non-reactive and 90.6 in reactive traffic on the benchmark while being an order of magnitude faster than prior work.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider the task of privileged planning, in which an autonomous vehicle drives using ground truth perception inputs. Such planners are traditionally rule-based. While rule-based approaches work well for regular driving, they require special scenario-specific rules to solve more complex scenarios, which is unlikely to scale to the long tail of driving scenarios.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Training neural planners with imitation learning (IL) is a popular alternative to rule-based approaches, because these methods can scale with data. Yet surprisingly, these methods underperform compared to rule-based or hybrid approaches. A common explanation for this behavior is that IL suffers from a distribution shift between the open-loop training objective and the closed-loop inference task.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Closed-loop training, in particular Reinforcement Learning (RL), is a promising alternative. A key problem in RL for driving is designing an appropriate reward function. Early work in RL for driving used principled, simple rewards, such as maximizing forward speed and terminating upon infractions. Empirically, however, learning with such simple rewards only succeeded in environments without other actors, where simple behaviors suffice. In settings where other dynamic actors are present, which require more complex behavior, such as reacting to sudden changes in the environment, simple rewards were empirically found to provide insufficient supervision. As a result, recent designs provide denser feedback to simplify learning, combining many rewards additively, such as one reward for speed, orientation, position, and comfort. The downsides of this approach are that the tradeoffs between rewards need to be carefully tuned, local minima are introduced, and the agent exploits undesirable shortcuts. These tradeoffs harm scalability: For example, we observe that increasing the mini-batch size by a factor of 4 with a complex reward reduces the performance of Proximal Policy Optimization (PPO) drastically, due to a local optimum of the reward.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Larger mini-batch sizes smooth the gradient, which can make optimization more prone to local optima. Additionally, many popular rewards rely on simplistic rule-based planners to compute their reward terms. This upper bounds the performance, as the decisions from the rules are rewarded as if they were optimal.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose an alternative reward design that does not rely on rule-based planners. The design learns policies with route completion (RC) as the only source of reward. To learn to avoid infractions, we end the episode upon any major infraction, e.g. collision, and reduce the obtained route completion multiplicatively while the agent is violating soft constraints, e.g., exceeding the speed limit.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

While conceptually appealing, prior empirical findings suggest that such a simple reward does not provide enough feedback for the policy to learn effectively. We reproduce the most popular CARLA RL planner Roach on the CARLA leaderboard 2.0 and show that it naively performs worse when trained with the simpler reward. However, unlike the complex reward, increasing the mini-batch size from 256 to 1024 drastically improves learning performance, with the simple reward outperforming the complex Roach reward. This is illustrated in Fig..

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Large mini-batch sizes, made possible by our reward, enable training with much more data, as data collection can be efficiently parallelized. We scale our training to 300 million samples on CARLA, 30x more than prior work, with one compute server and mini-batch size of 16384. This results in a massive performance improvement.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our final model, named CaRL, outperforms Roach and the recent world model RL-planner Think2Drive on the longest6 v2 benchmark, by 42 and 57 Driving Score (DS) respectively. We also implement our method on the nuPlan simulator, which measures performance in realistic everyday scenarios via log replay. We show that with minimal changes, our method can achieve 91 closed-loop score on the benchmark in both non-reactive and reactive traffic. The resulting model is both 1.7 (non-reactive) and 7.9 (reactive) points better than the prior best learning based approach, Diffusion Planner, while being 10x faster at inference time.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Compared to other approaches, there has been little RL research in planning. One reason might be that there is no publicly available RL code base for both the CARLA and nuPlan simulators. To foster reproducible research, we published our code at

<!-- chunk {"id": "body-0014", "role": "body", "section": "Improving Scalability for RL", "weight": 1.0} -->

Implementing RL on the CARLA leaderboard 2.0 is challenging because the simulator is slow. In this section, we hence propose better hyperparameters and an optimized code base for RL in CARLA. These changes make it possible to train on-policy RL methods on the CARLA leaderboard 2.0 efficiently. Related work is discussed in Appendix Section A.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Enabling higher learning rates", "weight": 1.0} -->

Selecting a robust base set of hyperparameters for PPO is important in planning because the slow simulators and long training times prevent automatic hyperparameter tuning. In this section, we show that the PPO Atari hyperparameter set enables us to train better models faster, compared to the standard Roach hyperparameters used in CARLA, reducing the computational cost of our experiments. One advantage of the Atari hyperparameters is that they enable training at higher learning rates. This effect can be intuitively explained by examining the number of off-policy steps performed by PPO.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Enabling higher learning rates", "weight": 1.0} -->

Off-policy steps: Policy gradient methods like PPO estimate the gradient of the policy's performance and perform gradient ascent. It is possible to get an unbiased estimate of this gradient for on-policy learning, i.e., if only one optimizer step is used before the data is discarded and new data recollected. Strict on-policy methods like REINFORCE or A2C do this, but are sample inefficient. PPO instead increases data efficiency by performing multiple gradient steps per iteration, approximating the off-policy policy gradient. The resulting approximation error is controlled by limiting policy change via the clipping heuristic. Another heuristic is that the policy is only updated for a few gradient steps, limiting policy change implicitly. Policies typically do not change a lot per gradient step, although this is dependent on the learning rate.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Enabling higher learning rates", "weight": 1.0} -->

Table compares the number of off-policy steps between the standard CARLA parameters from Roach and the Atari parameters.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Enabling higher learning rates", "weight": 1.0} -->

Roach performs 959 off-policy steps (the first step is on-policy), 60 times more than the Atari parameters. One would expect that this introduces large policy changes and hence off-policy error, and it is surprising that Roach converges at all. The reason for this is the small learning rate, which is 25x lower than the Atari learning rate, leading to smaller policy changes, hence balancing this effect. Training Roach with the (higher) Atari learning rate and schedule, without changing other hyperparameters, leads to a degenerate policy resulting in a drop of DS from $22 \pm 14$ to $2 \pm 1$ DS.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Enabling higher learning rates", "weight": 1.0} -->

We train Roach with its hyperparameters and the Atari hyperparameters. The results are shown in Table. Surprisingly, we observe a 10-hour reduction in training time while the policy achieves 11 DS better performance. The reduction in training time comes from using 5 times fewer epochs, whereas the performance improvement might come from a combination of hyperparameters. We therefore use the Atari hyperparameters as the basis for our model.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Enabling higher learning rates", "weight": 1.0} -->

Roach uses a Beta distribution to parametrize its action space. During inference, sampling from the distribution is typically replaced with a statistic of the distribution to turn off exploration. Roach proposes to use the mode of the distribution when ${\alpha,\beta} > 1$. Using the mode biases the policy's behavior, as PPO optimizes the expected performance under the action distribution (the mean). We observe that using the mean achieves 1 DS better performance with the same models, and reduces the standard deviation by 3 points.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Optimizing a Single Reward", "weight": 1.0} -->

Many current RL planners use a reward function that consists of multiple additive terms, including terms to reward the inverse distance to the desired vehicle speed, desired vehicle position, and desired orientation. This is reminiscent of imitation learning because these "desired" states are computed using handcrafted rules akin to a rule-based planning method, or even directly with human labels. As noted in the Appendix of, their rule-based planner is suboptimal and sometimes assigns higher rewards to suboptimal states. The advantage of these complex, shaped rewards is that they can simplify learning. They provide dense, rich feedback, which simplifies the credit assignment problem of RL.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Optimizing a Single Reward", "weight": 1.0} -->

These rewards have, however, many downsides. The handcrafted rules, being suboptimal, can upper-bound performance, and these rewards introduce loopholes and local minima that the optimization can get stuck, or the agent can exploit. One example of a failure case we observe with the Roach reward is that the policy sometimes learns to wait at green traffic lights. This is a simple behavior that obtains a large return with the Roach reward. The model is constantly rewarded by the optimal speed reward if it has speed 0 at a red light. Because traffic lights are often red for a long time and green for a short amount of time in CARLA, the policy sometimes learns to exploit that it can just wait for the next red light for easy rewards, when the light turns green for a short duration. This problem is illustrated in Appendix Fig.. Eventually, many training seeds escape this local minima, but we still observe that the final policy drives slower than usual when approaching green lights, presumably trying to catch the next red light. This is illustrated in Appendix Fig..

<!-- chunk {"id": "body-0023", "role": "body", "section": "Optimizing a Single Reward", "weight": 1.0} -->

The reward at time step $t$ is computed by multiplying the percentage of the route completed during this simulator time step $RC_{t}$ with soft penalty factors $p_{t} \in {\lbrack 0,1\rbrack}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Optimizing a Single Reward", "weight": 1.0} -->

The soft penalties $p_{t}$ are $1$ if their condition is not violated and otherwise have a value $\in {\lbrack 0,1)}$ depending on the type of infraction. Soft penalties are constraints that the agent should typically adhere to, such as staying within the speed limit, but may violate in order to avoid a hard penalty like a collision. It is important that soft penalty factors that the agent cannot avoid violating early on in training, such as comfort, need to be $> 0$. Otherwise, the agent would receive no reward. It is possible to apply a soft penalty for multiple frames e.g. to penalize actions while the car is not moving or increase the penalty strength.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Optimizing a Single Reward", "weight": 1.0} -->

Any major infraction, like a collision, is treated as a hard penalty. Hard penalties simply end the episode. The principle is that any hard constraints of the optimization problem are formulated as terminal states, ensuring that violating them results in suboptimal performance as no further reward can be collected. $T$ is a terminal penalty that is applied at the end of the episode, depending on the infraction. It can be used to induce an ordering between infractions, but it needs to be sufficiently small that the agent is not penalized for starting to drive early on in training. We use $T = 1$ for collisions and red light infractions, and $T = 0$ for everything else. The full description of penalties we use can be found in Appendix Section F.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Optimizing a Single Reward", "weight": 1.0} -->

The reward design follows the following principles: The amount of reward obtainable is finite. There is only 100 RC to be collected in total, preventing infinite reward loopholes like the car waiting at a green light. The reward only specifies what to do, not how to do it. Our reward does not include any rule-based planners. The global optimum of the reward is the same as the global optimum of the metric. This ensures that solving the learning problem results in an optimal policy, wrt. the metric. Our reward closely aligns with the DS metric, with some additional penalties like speeding. The agent obtains the optimal reward when completing the route without infraction, which also yields the optimal DS.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Optimizing a Single Reward", "weight": 1.0} -->

Our reward is simple and gives much fewer local hints to the policy than other rewards. It avoids the problems of typical reward designs, but might be harder to optimize. Table shows that PPO struggles to perform well without the rule-based dense supervision of the Roach reward, dropping performance by 13 points at the standard mini-batch size of 256. Interestingly, this trend reverses when we scale the mini-batch size to 1024. When training PPO with the dense Roach reward at 1024 mini-batch size, we observe that the model gets stuck in the local minimum of not driving on many routes, which yields good position and orientation rewards but suboptimal speed rewards. At the end of training, the model started to learn to accelerate but hasn't learned to steer yet, leading to a poor driving policy with 2 DS. One hypothesis is that larger mini-batch sizes smooth the optimization, making it more prone to local minima. In contrast, our reward does not have these tradeoffs between different reward components, and PPO improves drastically when increasing the mini-batch size to 1024, improving DS by 17 points.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Optimizing a Single Reward", "weight": 1.0} -->

Additionally, our reward outperforms the roach reward by 4 points in DS and reduces training variance from $\pm 7$ to $\pm 3$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Scaling Data", "weight": 1.0} -->

There are two ways to increase mini-batch size in PPO while keeping the number of gradient steps per epoch unchanged. In the previous section, we increased the mini-batch size by performing 4x more simulator steps per PPO iteration with 4x fewer PPO iterations, because this method has similar resource requirements. If more resources are available, the number of parallel simulators can instead be increased, which raises the overall sample throughput. This also requires additional GPUs for model inference and training, which we utilize via the DD-PPO scaling approach without preemption for the experiment in this section. DD-PPO works like distributed data parallelism from supervised learning.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Scaling Data", "weight": 1.0} -->

Prior works trained PPO for driving with 1-10 million samples. This is typical for classic PPO, but 10-100 times less than what recent breakthroughs in robotics used. Prior work may not have scaled up data because increasing mini-batch size, which is required to scale efficiently, can yield degenerate performance, as Table showed. Our reward enables us to scale our model from 10 million to 300 million samples using a single node with 8 A100 (40G) GPUs and 108 EPYC Rome CPU cores for 1 week. Table shows that increasing the samples and mini-batch size leads to a large improvement of 33 DS. The baseline features some changes compared to the model in the last section, which are discussed in Appendix Section B. The 300M result is an average of three seeds.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

This section shows the advantages of our method over several other planning approaches on the CARLA longest6 v2 benchmark and nuPlan. All experiments were run by us with the same setting to ensure a fair comparison and avoid the common benchmarking errors that permeate the literature.

<!-- chunk {"id": "body-0032", "role": "body", "section": "CARLA", "weight": 1.0} -->

Benchmark: We use the longest6 v2 benchmark, and metrics as described in Section 2.1.

<!-- chunk {"id": "body-0033", "role": "body", "section": "CARLA", "weight": 1.0} -->

Baselines: Roach is a popular RL planner trained with the PPO algorithm. Think2Drive is a recent RL planner that uses the world model-based approach DreamerV3. We reproduce both Roach and Think2Drive based on the details provided in the respective publications. PDM-Lite is a rule-based planning method in CARLA. The planners considered in this work are privileged, meaning they have access to ground truth perception inputs. These inputs could realistically be predicted by a perception stack, albeit at lower accuracy. PDM-Lite is special in that it extracts additional information about the scenarios from the CARLA leaderboard that is not predicted by any existing perception stack. PDM-Lite knows which scenario type will appear and what the scenario parameters are, and uses this information to solve some of the scenarios with specialized rules that are specific to the scenario. Such an approach works for the small variety of scenarios encountered in CARLA, but is unrealistic to scale to the long tail. PDM-Lite is therefore perhaps better viewed as an auto-labeling method for imitation planners. PlanT is the SotA imitation planner for the CARLA leaderboard 1.0.

<!-- chunk {"id": "body-0034", "role": "body", "section": "CARLA", "weight": 1.0} -->

It uses bounding boxes as input, which are processed with a transformer and predicts waypoints. We reproduce PlanT for the CARLA leaderboard 2.0 by training it to imitate PDM-Lite. Implementation details about the baselines can be found in Appendix Section E.

<!-- chunk {"id": "body-0035", "role": "body", "section": "CARLA", "weight": 1.0} -->

Our method, CaRL, achieves 64 DS on longest6 v2 as shown in Table. It significantly advances the SotA in RL planning, outperforming the best prior method, Roach, by 42 DS. It particularly reduces pedestrian (Ped) and vehicle (Veh) collisions compared to other RL baselines. The recent world model-based Think2Drive method only achieves a DS of 7 and is even outperformed by the Roach method when both methods are trained with the hyperparameters proposed by the respective papers. CaRL is the best learning based method outperforming PlanT by 2 DS while using a smaller model and less inference compute. The rule-based method PDM-Lite still achieves the best DS with 73 in particular due to its high route completion and low collisions. PDM-Lite outperforms CaRL because it is more consistent at solving some of the safety-critical scenarios. PDM-Lite drives relatively slow on average, which may help it avoid collisions but as a result incurs many min-speed infractions (MS).

<!-- chunk {"id": "body-0036", "role": "body", "section": "CARLA", "weight": 1.0} -->

CaRL drives 31% faster than PDM-Lite on average (16.4 km/h vs 12.5 km/h), which is indicated by its 4.5 times lower MS infraction.

<!-- chunk {"id": "body-0037", "role": "body", "section": "CARLA", "weight": 1.0} -->

We additionally report the average runtime per time step in milliseconds (ms), including preprocessing observations, on the last route of longest6 v2. Times are measured with an RTX 3090 GPU and an i9-10850K CPU. We observe that the RL-based methods are more efficient than the rule-based and imitation-based methods. This is because the model size of RL policies is typically smaller than models used in imitation learning. CaRL runs 2 times faster than the state-of-the-art approach PDM-Lite. It also uses a similar compute budget at inference as other RL-based approaches while driving substantially better.

<!-- chunk {"id": "body-0038", "role": "body", "section": "nuPlan", "weight": 1.0} -->

Benchmark: NuPlan is a closed-loop simulator using real-world data. As metric, we use the closed-loop score (CLS), which is a weighted average of progress, time-to-collision, speed-limit compliance, and comfort, scaled in 0-100. Additionally, the score is set to zero if any hard penalty is violated e.g., collisions. We evaluate all methods using non-reactive log replay (NR) and reactive background traffic (R), where other vehicles are controlled with the IDM. Following, we use the benchmark that includes 1118 simulations from the validation split.

<!-- chunk {"id": "body-0039", "role": "body", "section": "nuPlan", "weight": 1.0} -->

Baselines: PDM-Closed is an extension of IDM with multiple trajectory proposals, internal simulation, and scoring. PLUTO outputs multiple learned trajectories and scores, which can be combined with the scoring mechanism of PDM-Closed. PlanTF vectorizes agents and map elements and processes them with a transformer to forecast non-ego agents, and regress a trajectory. Diffusion Planner applies a diffusion transformer to generate the ego trajectory conditioned on a vectorized scene representation. Log Replay tracks the human trajectory with an LQR controller.

<!-- chunk {"id": "body-0040", "role": "body", "section": "nuPlan", "weight": 1.0} -->

Adaptation: We use different baselines for CARLA and nuPlan because the code of these planners is only compatible with either CARLA or nuPlan. Prior work only evaluated on one of the two simulators. For a more rigorous evaluation, we reproduce CaRL on nuPlan as well. This requires one special adaptation. The simulation duration in nuPlan is a constant 15 seconds, even when the ego agent has already completed the route. Since we primarily reward route completion, the agent would get no reward signal after completing the route. To account for this simulator detail, we additionally reward the agent with a constant survival bonus at every frame during training, which gives the agent an incentive to avoid infractions after completing the route. We train CaRL with 500M samples on nuPlan since the simulation is faster. We refer the reader to Appendix Section B.6 for further implementation details.

<!-- chunk {"id": "body-0041", "role": "body", "section": "nuPlan", "weight": 1.0} -->

As shown in Table, rule-based methods are highly effective in nuPlan, with PDM-Closed achieving over 92 reactive and non-reactive CLS. IL planners achieve reasonable performance (85-90) in non-reactive traffic but have difficulties adapting from the non-reactive setting (as seen during training) to the reactive IDM traffic. E.g., Diffusion Planner (without post-processing) achieves a strong non-reactive CLS of 90 but a weaker reactive score of 83. PLUTO and PlanTF have similar performance drops. CaRL works well in both settings, achieving the highest CLS of all learned planners with 91.3 in the non-reactive and 90.6 CLS in reactive mode, respectively. CaRL runs $7 - 17 \times$ faster than the baselines, due to its small 2M parameter network. We measure runtimes in ms on an A5000 with an i9-13900K. The inference time of CaRL is slightly larger on nuPlan than on CARLA because nuPlan has more dynamic actors, which increases rendering times of the observation. We provide further results and baselines in Appendix E.2.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Contemporary RL methods for driving often use complex rewards that induce tradeoffs between multiple reward terms. We observe that these tradeoffs prevent scalability. Training with large mini-batch sizes with PPO leads to degenerate policies, likely since the optimization gets stuck in a local minimum of the reward. We propose an alternative reward design based on optimizing a single reward: route completion. Infractions either terminate the episode or multiplicatively reduce route completion. We show that this enables learning with large mini-batch sizes, which in turn enables efficient scaling to more samples by parallelizing data collection. We scale PPO to 300M samples in CARLA using a mini-batch size of 16384 and show that this leads to a performance improvement of 33 DS on the longest6 v2 benchmark. CaRL achieves 91 CLS on nuPlan in both non-reactive and reactive traffic, outperforming all prior learning-based approaches.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We investigate urban driving at moderate speeds of up to 80 km/h. Problems specific to high-speed driving on highways are not considered.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our work improves the SOTA of RL for driving in simulation. For RL to become relevant for real cars, Sim2Real transfer needs to be demonstrated, which we leave for future work.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We train CaRL with the 7 scenario types of longest6 v2. The CARLA leaderboard 2.0 offers more scenario types, which we have not investigated in this work.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusion", "weight": 1.5} -->

For the CARLA vehicle physics, there are no human reference values for comfortable driving. Comfort is not a physical quantity but a subjective human feeling, so bounds need to be set based on human data. We set wide bounds to ensure that the model can comply with the comfort infraction, but the resulting behavior might not be comfortable in a real car. Future work may tune these bounds for smoother driving in CARLA.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusion", "weight": 1.5} -->

CaRL has two main failure modes in CARLA: missing exits in highway off-ramps and other cars crashing into its rear in scenarios where another car runs a red light (rear-end collisions are counted as the agent's fault in CARLA). We show examples in the Appendix Section C.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our reward does not encode that getting to the goal faster is better. This is because most RL algorithms naturally encode a notion of urgency via a discount factor.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Both Longest6 v2 and are level 4 training benchmarks, where training on the evaluation town is allowed. We have not investigated level 5 generalization to new towns.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our reward gives fewer local hints than other rewards. We have deliberately chosen an RL algorithm (PPO) that uses Monte-Carlo returns for optimization, which sum up rewards. This might alleviate the absence of locality. RL algorithms based on Q-learning, that rely on local TD-prediction, such as Soft-Actor Critic, may have a harder time optimizing our reward, although we have not investigated other algorithms.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We think these limitations can be addressed and are promising directions for future work.
