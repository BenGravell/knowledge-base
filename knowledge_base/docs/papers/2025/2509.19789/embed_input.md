<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

RDAR: Reward-Driven Agent Relevance Estimation for Autonomous Driving

Topics include Markov decision process, Autonomous driving, Vehicles, Safety, Attention mechanisms, Datasets, Control, RDAR.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Human drivers focus only on a handful of agents at any one time. On the other hand, autonomous driving systems process complex scenes with numerous agents, regardless of whether they are pedestrians on a crosswalk or vehicles parked on the side of the road. While attention mechanisms offer an implicit way to reduce the input to the elements that affect decisions, existing attention mechanisms for capturing agent interactions are quadratic, and generally computationally expensive. We propose RDAR, a strategy to learn per-agent relevance - how much each agent influences the behavior of the controlled vehicle - by identifying which agents can be excluded from the input to a pre-trained behavior model. We formulate the masking procedure as a Markov Decision Process where the action consists of a binary mask indicating agent selection. We evaluate RDAR on a large-scale driving dataset, and demonstrate its ability to learn an accurate numerical measure of relevance by achieving comparable driving performance, in terms of overall progress, safety and performance, while processing significantly fewer agents compared to a state of the art behavior model.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Humans, when driving, do not pay equal attention to all agents around them (e.g., other vehicles, pedestrians). Transfomer-based attention models offer the promise of attending only to relevant components of the input, but existing attention models are typically quadratic in the size of the input space. Driving models encounter hundreds of input tokens, leading to substantial computational complexity and latency Harmel et al.; Huang et al.; Baniodeh et al..

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In autonomous driving, there is a tension between the limited available compute resources and the desire to take advantage of scaling laws, large models, and test-time compute. Having access to numerical per-agent relevance scores would not only improve the interpretability of large driving models, but also allow compute resources to be prioritized for the features that are most important. In fact, when agents and other scene elements are represented explicitly as tokens, reasoning about interactions between these tokens (typically through self-attention or graph neural network operations) is quadratic and difficult to reduce using low-rank or other approximations that work well for long-sequence data. Reducing the number of tokens under consideration provides quadratic improvements in FLOPs used.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we introduce RDAR (Reward-Driven Agent Relevance), through which we quantify agent relevance through a learned approach. The basic intuition is that if an agent is not relevant towards the driving decisions of the controlled vehicle, then its absence would not change the controlled vehicle's driving behavior significantly. Thus, we quantify per-agent relevance by learning which agents can be masked out from the controlled vehicle's planner input while maintaining a good driving behavior. We formulate agent selection as a reinforcement learning (RL) problem where an action is a binary mask indicating which agents to include in the driving policy input, and which not to. The RDAR scoring policy is trained in the loop with a frozen, pre-trained driving policy and a simulator. At each time step, based on the relevance scores, an agent mask is fed to the driving policy, making the controlled vehicle blind to the lower score agents. As it will be clear from the following sections, this is not a binary classification problem over agents due to the underlying system dynamics (e.g., not observing an agent now could lead to a collision later) and to the unavailability of ground truth labels.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Some examples of relevance (color-coded) computed by our method are shown in Fig. 1.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

A novel reinforcement learning formulation for agent relevance estimation;

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A sampling-based mechanism for agent selection that enables efficient training and inference;

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

A comprehensive evaluation showing that we can maintain driving performance while processing only a handful of surrounding agents.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

We wish to learn a policy $\pi_{\theta}^{R}$ assigning a relevance score to each agent in the driving scene based on its influence on the driving behavior of the controlled vehicle ($\theta$ denotes learnable parameters). We assume a pre-trained driving policy $\pi^{D}$ mapping scene information to driving actions is available. We also assume that, associated with the policy $\pi^{D}$, there is a reward function $r$ encoding some notion of good driving behavior. The RDAR scoring policy $\pi_{\theta}^{R}$ is trained in closed loop with the (frozen) driving policy $\pi^{D}$ and a driving simulator.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

Formally defining a notion of agent relevance is not straightforward. However, human drivers have a good intuitive concept of such notion, which allows them to pay selective attention to surrounding agents. With reference to Fig. 2a, a pedestrian crossing in front of the controlled vehicle is a highly relevant agent, because its presence its presence means that the controlled vehicle must come to a stop and yield instead of driving through a crosswalk. At the same time, the pedestrian crossing behind the driver has low relevance. Similar considerations are true for the intersection scenario of Fig. 2b. The vehicle inching into the intersection has high relevance, because its presence means that the controlled vehicle must stop and yield. Instead, the cyclist who just passed through the intersection should not affect the controlled vehicle behavior. Therefore, we can say that an agent is relevant if hypothetically removing it from a driving scenario would cause the controlled vehicle to have a different behavior.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Markov Decision Process formulation", "weight": 1.0} -->

Following the above intuition, we formulate the agent relevance estimation problem as a Markov Decision Process (MDP). The policy $\pi_{\theta}^{R}$ outputs per-agent relevance scores, which can be interpreted as logits of a categorical distribution. If agent $i$ is sampled from this relevance distribution, it gets processed by the driving policy $\pi^{D}$, otherwise it is masked out and ignored by $\pi^{D}$. Given a hyperparameter $k \in {\mathbb{N}}$, an action is then a subset of $k$ surrounding agents, or a $k$-sample, to be processed by $\pi^{D}$. Our goal is thus to learn $\pi_{\theta}^{R}$ such that the return is maximized in expectation. Inaccurate relevance scores would make the driving policy blind to important agents in the scene, leading to low reward behaviors (e.g., collisions).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Markov Decision Process formulation", "weight": 1.0} -->

$S$ is the state space, including the controlled vehicle state, surrounding agent states (expressed in the controlled vehicle reference frame), road network and route information (see Fig.3c);

<!-- chunk {"id": "body-0014", "role": "body", "section": "Markov Decision Process formulation", "weight": 1.0} -->

$A = {\{ 0,1\}}^{N}$ is the action space, consisting of binary masks of size $N$ (number of agents) indicating which agents to include in the planning input. The logits of the action distribution are the relevance scores (details in the following sections);

<!-- chunk {"id": "body-0015", "role": "body", "section": "Markov Decision Process formulation", "weight": 1.0} -->

$r$ is the reward function encoding good driving behavior. This is ideally the same reward or scoring function accompanying $\pi^{D}$;

<!-- chunk {"id": "body-0016", "role": "body", "section": "Markov Decision Process formulation", "weight": 1.0} -->

$P$ is the transition probability function associated to the environment. Note that the environment, from the perspective of the reinforcement learning agent $\pi_{\theta}^{R}$, consists of $\pi^{D}$ and the actual driving environment altogether (see Fig.3a);

<!-- chunk {"id": "body-0017", "role": "body", "section": "Markov Decision Process formulation", "weight": 1.0} -->

The nature of the actions space makes this problem similar to a contextual multi-armed bandit (CMAB) Lu et al., with the subtle difference that in this case the action changes the context, which in CMABs is assumed to be independent of the action.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Agent Selection Mechanism", "weight": 1.0} -->

At each timestep $t$, the RDAR policy $\pi_{\theta}^{R}$ outputs a vector of per-agent relevance scores $\phi_{t} = {\lbrack\phi_{1},\phi_{2},\ldots,\phi_{N}\rbrack}$. At deployment time, the top-$k$ scoring agents are selected, while at training time, agents are randomly sampled to encourage exploration. For sampling, the scores are converted to a categorical distribution $p_{t} = {\lbrack p_{1},p_{2},\ldots,p_{N}\rbrack}$ over the binary agent selection action space through a softmax, where

<!-- chunk {"id": "body-0019", "role": "body", "section": "Agent Selection Mechanism", "weight": 1.0} -->

Drawing one sample from this distribution corresponds to selecting one agent. If we draw exactly one sample, the probability of agent $i$ being selected is $p_{i}$. We can thus get a $k$-sample by drawing $k$ samples sequentially, without replacement, by renormalizing the probabilities at each step. We denote an agent $k$-sample as

<!-- chunk {"id": "body-0020", "role": "body", "section": "Agent Selection Mechanism", "weight": 1.0} -->

where each component $a_{i}$ is the integer index corresponding to the selected agent. Note that this notation and an $N$-dimensional binary vector are equivalent. Then, the probability of selecting an ordered sample of agents without replacement is

<!-- chunk {"id": "body-0021", "role": "body", "section": "Agent Selection Mechanism", "weight": 1.0} -->

where the denominators are the renormalization terms. Note that although we describe the sampling process as sequential, the Gumbel top-$k$ trick enables efficient, single-step sampling without replacement Jang et al.; Kool et al..

<!-- chunk {"id": "body-0022", "role": "body", "section": "Agent Selection Mechanism", "weight": 1.0} -->

Since the scores are the output of our model $\pi_{\theta}^{R}$, equation 5 is exactly what we need for policy gradient updates in an RL framework. Once a $k$-sample is picked, only those $k$ agents are processed by the driving policy $\pi^{D}$. The action output by the driving policy is then applied to the simulator, and the overall state is updated. The simulator also produces the reward signal $r_{t}$ for RDAR. The process is then repeated.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Reinforcement learning framework", "weight": 1.0} -->

We train the policy using an off-policy actor--critic framework with V-trace corrections Espeholt et al..

<!-- chunk {"id": "body-0024", "role": "body", "section": "Reinforcement learning framework", "weight": 1.0} -->

The four components are respectively policy gradient loss, critic loss, entropy regularization loss, and action smoothing loss.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Reinforcement learning framework", "weight": 1.0} -->

where $\rho_{t} = \frac{\pi_{\theta}^{R}{({a_{t} \mid s_{t}})}}{\mu{({a_{t} \mid s_{t}})}}$ are clipped importance weights, $a_{t}$ is the agent $k$-sample at time step $t$ as in equation 2. The ${\hat{A}}_{t}^{\text{v-trace}}$ and $V_{t}^{\text{target}}$ terms are computed following Espeholt et al.. The log-likelihood term in equation 7 is computed as in equation 5. The entropy and smoothing loss components, are calculated on the logits directly and do not depend on the $k$-sample $a_{t}$. The entropy component favors uniformity in the relevance scores, and therefore encourages exploration. The action smoothing component encourages the scores corresponding to the same agent to be consistent across time.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Reinforcement learning framework", "weight": 1.0} -->

It is possible that fewer than $N$ agents are physically present in a scene at a given time, in which case the loss terms corresponding to non-existing agents are masked. Finally, $\lambda_{c}$, $\lambda_{e}$, $\lambda_{s}$ are hyperparameters weighing the loss terms, selected empirically.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Architecture", "weight": 1.0} -->

The RDAR model architecture consists of three main components. An encoder module processes the full scene context (controlled vehicle state, surrounding agent states, road and route information) and computes embeddings. There are two heads: a scoring head, mapping embeddings to agent relevance scores, and a value head, approximating the value function. Note that the value function for the relevance scoring policy has a different meaning than the value function for the driving policy, since the expectation is over all possible $k$-samples rather than all possible driving actions. The three options for the scoring head make use of embedding of varying depth from the encoder. The first option (Fig. 4a) just uses the features from the agent projection layer. In this case, only agent state information is fed to the scoring head. The second option (Fig. 4b) uses the embeddings output by the agent encoder module. In this case, the embeddings also encode agent interactions. The third option (Fig. 4c) uses the output from the scene encoder, and reprojects it back to the agent level through a transformer block.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Architecture", "weight": 1.0} -->

In this case, all information from the driving scene is used to compute agent relevance. The value head is kept the same for the three architectures, and uses all available information.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Training details", "weight": 1.0} -->

The training-time agent sampling procedure described in Section 3 is done through the Gumbel top-$k$ trick Kool et al., natively used, for instance, in the JAX's implementation of the categorical distribution Bradbury et al.. Also at training time, the number $k$ of agents sampled is randomized to make sure the model learns actual relevance scores and not only to differentiate between top-$k$ and non top-$k$ agents. We uniformly sample a different value $k$ per driving scenario. To achieve scale, we use a distributed, asynchronous reinforcement learning infrastructure similar to IMPALA Espeholt et al.. We found these hyperparameter values to give the best performances: learning rate $2 \cdot 10^{- 5}$, $\lambda_{c} = 0.1$, $\lambda_{e} = 0.2$, $\lambda_{s} = 0.05$. No sampling happens at deployment time, and and the top-$k$ agents are selected greadily (analogous to selecting the argmax action in standard RL).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Datasets", "weight": 1.0} -->

We train and evaluate our approach on large-scale proprietary datasets consisting of ten-second long scenarios of real world, diverse urban driving. The training dataset contains around two million scenarios, while the evaluation dataset contains twelve thousand. The data were collected across Las Vegas (LV), Seattle (SEA), San Francisco (SF), and the campus of the Stanford Linear Accelerator Center (SLAC). Note that Las Vegas, Seattle, and San Francisco represent dense urban settings, while SLAC is a suburban academic campus. Training and validation data are not separated by location, so a given validation example may have training examples from the same location at other times. Scenarios are sampled at $5{Hz}$ from real-world driving logs.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Metrics", "weight": 1.0} -->

To quantitatively evaluate our method, we use standard driving metrics which we compute on the 12k scenario evaluation set. In these evaluations, the candidate relevance scoring policies and baselines are used in closed-loop as filters, with the driving policy $\pi^{D}$ processing only a subset $k$ of all the agents present at any one time. At evaluation, we select the top-$k$ scoring agents greedily (analogously to selecting an action through argmax in standard RL).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Metrics", "weight": 1.0} -->

Collisions \[%\]: percentage of scenarios in which a collision occurs (lower is better);

<!-- chunk {"id": "body-0033", "role": "body", "section": "Metrics", "weight": 1.0} -->

Traffic light \[%\]: percentage of scenarios in which a traffic light is violated (lower is better);

<!-- chunk {"id": "body-0034", "role": "body", "section": "Metrics", "weight": 1.0} -->

Stop line \[%\]: percentage of scenarios in which a stop line is skipped (lower is better);

<!-- chunk {"id": "body-0035", "role": "body", "section": "Metrics", "weight": 1.0} -->

Off-road \[%\]: percentage of scenarios in which the vehicle drives off-road (lower is better);

<!-- chunk {"id": "body-0036", "role": "body", "section": "Metrics", "weight": 1.0} -->

Comfort: metric combining four motion aspects -- forward/backward acceleration, turning acceleration, and how suddenly or abruptly these accelerations change. These are weighted, averaged, then converted to a 0-1 score where 1 means smooth driving and 0 means jerky, uncomfortable motion (higher is better).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Metrics", "weight": 1.0} -->

Progress ratio: relative progress along the route with respect to the ground truth human log;

<!-- chunk {"id": "body-0038", "role": "body", "section": "Metrics", "weight": 1.0} -->

Complexity: computation required by the scoring method as a function of the number $N$ of agents in a scene.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Baselines", "weight": 1.0} -->

We compare RDAR to other scoring strategies.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Baselines", "weight": 1.0} -->

Closest-$k$ selection: Select the $k$ closest agents to the controlled vehicle -- equivalent to agents' relevance scores being inversely proportional to their distance to the controlled vehicle;

<!-- chunk {"id": "body-0041", "role": "body", "section": "Baselines", "weight": 1.0} -->

Random-$k$ selection: Randomly select $k$ agents from the scene -- equivalent to agents' relevance scores being drawn uniformly at random;

<!-- chunk {"id": "body-0042", "role": "body", "section": "Baselines", "weight": 1.0} -->

Attribution-based scoring: scores obtained via input attribution Cusumano-Towner et al.. At each timestep, the procedure is as follows: the pre-trained driving policy $\pi^{D}$ is evaluated $N$ + 1 times (one with full scene information and one with each individual agent omitted in turn). For each agent, the Jensen--Shannon divergence between the action from its masked-out pass and the nominal full-scene pass is computed.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Baselines", "weight": 1.0} -->

The overall performance of these baselines when varying $k$ is shown in Fig. 5. When $k = N$ no agents are masked out from the driving policy.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Quantitative results", "weight": 1.0} -->

We report plots showing the trends of the reference metrics when varying the value $k$ in Fig. 5. As expected, all the metrics seem to converge to the baseline's when increasing the number of agents processed by the driving policy, with diminishing returns. We can see that RDAR has comparable performances to the attribution method, and requires only a fraction of the computation time ($O{}$ instead of $O{(N)}$). RDAR is also able to drive with a fraction of percent performance regressions compared to the nominal, full policy, while processing significantly fewer agents. In fact, an RDAR model used in closed-loop with $k \geq 10$ already enables comparable driving performances to the nominal unmasked policy while consuming an order of magnitude fewer agents. With increasing $N$, as expected the collision rates decrease, the comfort scores increase (due to reduced flickering of agent selection). However, traffic infraction rates seem to have an upward trend. This makes sense, as for instance driving on empty roads would make it very easy to avoid infractions, and driving in heavy traffic makes it harder due to the higher risk of collisions.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Quantitative results", "weight": 1.0} -->

Tab. 1 shows the actual numbers relative to the $k = 10$ case. The three different architectures proposed in Fig. 4 show comparable performances when used in closed-loop with the driving policy. The model using full scene information (Fig. 4c) leads to the least collisions and higher comfort score. There seems to be a trade-off between collision avoidance and the metrics related to traffic rules, which can be explained by the fact that avoiding collisions could require the controlled vehicle to do an infraction (e.g. driving off-road). In fact, while full scene information allows to minimize collisions, it does that at the cost of slightly higher infraction rates. Similarly, the baseline, unmasked driving policy has higher infraction rates than most masked alternatives. It is also interesting to see that the random scoring policy outperforms all the others when it comes to traffic rules (off-road, traffic lights, stop lines), which comes, as expected, at the cost of much higher collision rates.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Quantitative results", "weight": 1.0} -->

Scores computed using only agent features (Fig. 4a) or attending to the controlled vehicle state (Fig. 4b) achieves good closed-loop driving and requires fewer FLOPs compared to using full scene information (Fig. 4c). On the other hand, full scene information enables enhanced situational awareness and lower collisions. Therefore, the specific RDAR architecture can be chosen based on application needs in terms of memory, real-time compute requirements, or score accuracy.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Qualitative results", "weight": 1.0} -->

We also report some visualizations from some closed-loop evaluation rollouts (the same used to compute the aggregate metrics) in Fig. 6. The scenes represented are challenging, cluttered driving scenes in which incorrect relevance quantification would lead to wrong masking and bad behaviors. In the figures, a colored dot hovers over the top-$10$ agents. These are the agents that are being processed by the driving policy, while the other are ignored. As shown in the color scale in the bottom left of each figure, the red color corresponds to high relevance score, the light blue color corresponds to lower relevance (still, within the top-$10$). These examples are from our best full-scene scoring policy (Fig. 4c). We can see that the agent importance assigned by our model is aligned with human intuition, and highlights high-risk pedestrians, other cars the controlled vehicle must yield to, agents in close proximity.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Discussion and Conclusions", "weight": 1.5} -->

Our model provides insights into which agents influence driving decisions, enabling better understanding of planner behaviors. It can also inform how to allocate costly computation in a principled way--for example, running joint trajectory prediction or computing vision embeddings only for the most relevant agents.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Discussion and Conclusions", "weight": 1.5} -->

This work opens several interesting directions. First, similar relevance-scoring methods could be applied to other components of the driving scene, such as road information. A challenge here is the potential for distribution shifts when masking inputs; in our case such effects are mild, since driving scenarios remain in-distribution regardless of the number or position of agents, but investigating mitigation strategies is important. Second, the scoring policy's action space could be expanded beyond masking. Instead of excluding agents, the prioritization module could be trained to trigger targeted computation on selected agents, such as expensive vision embeddings, so that enhanced representations directly translate into downstream gains like improved driving rewards.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Discussion and Conclusions", "weight": 1.5} -->

While our work is motivated by autonomous driving applications, the principle of learning per-agent relevance naturally extends to other multi-agent and multi-object settings, such as swarm robotics, multi-agent reinforcement learning, or video scene understanding, where only a subset of entities meaningfully influence a decision. By identifying and prioritizing relevant entities, similar approaches could improve scalability, reduce computational costs, and offer insights into the decision-making processes in these domains.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Discussion and Conclusions", "weight": 1.5} -->

We introduced a reinforcement learning approach to estimate agent relevance in driving scenarios. By formulating relevance scoring as an agent-masking MDP, we enable end-to-end training of a scoring policy with a driving policy in the loop. Our method avoids costly post-hoc attribution and repeated forward passes, making it well suited for real-time autonomy stacks. In closed-loop evaluation, we show that comparable driving performance can be achieved while processing an order of magnitude fewer agents, highlighting the benefits of our approach in terms of behavior model introspection and dynamic compute allocation.
