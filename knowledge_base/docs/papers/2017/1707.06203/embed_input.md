<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Imagination-Augmented Agents for Deep Reinforcement Learning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce Imagination-Augmented Agents (I2As), a novel architecture for deep reinforcement learning combining model-free and model-based aspects. In contrast to most existing model-based reinforcement learning and planning methods, which prescribe how a model should be used to arrive at a policy, I2As learn to interpret predictions from a learned environment model to construct implicit plans in arbitrary ways, by using the predictions as additional context in deep policy networks. I2As show improved data efficiency, performance, and robustness to model misspecification compared to several baselines.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

A hallmark of an intelligent agent is its ability to rapidly adapt to new circumstances and \"achieve goals in a wide range of environments\". Progress has been made in developing capable agents for numerous domains using deep neural networks in conjunction with model-free reinforcement learning (RL), where raw observations directly map to values or actions. However, this approach usually requires large amounts of training data and the resulting policies do not readily generalize to novel tasks in the same environment, as it lacks the behavioral flexibility constitutive of general intelligence.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model-based RL aims to address these shortcomings by endowing agents with a model of the world, synthesized from past experience. By using an internal model to reason about the future, here also referred to as *imagining*, the agent can seek positive outcomes while avoiding the adverse consequences of trial-and-error in the real environment -- including making irreversible, poor decisions. Even if the model needs to be learned first, it can enable better generalization across states, remain valid across tasks in the same environment, and exploit additional unsupervised learning signals, thus ultimately leading to greater data efficiency. Another appeal of model-based methods is their ability to scale performance with more computation by increasing the amount of internal simulation.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The neural basis for imagination, model-based reasoning and decision making has generated a lot of interest in neuroscience; at the cognitive level, model learning and mental simulation have been hypothesized and demonstrated in animal and human learning. Its successful deployment in artificial model-based agents however has hitherto been limited to settings where an exact transition model is available or in domains where models are easy to learn -- e.g. symbolic environments or low-dimensional systems. In complex domains for which a simulator is not available to the agent, recent successes are dominated by model-free methods. In such domains, the performance of model-based agents employing standard planning methods usually suffers from model errors resulting from function approximation. These errors compound during planning, causing over-optimism and poor agent performance. There are currently no planning or model-based methods that are robust against model imperfections which are inevitable in complex domains, thereby preventing them from matching the success of their model-free counterparts.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We seek to address this shortcoming by proposing Imagination-Augmented Agents, which use approximate environment models by \"learning to interpret\" their imperfect predictions. Our algorithm can be trained directly on low-level observations with little domain knowledge, similarly to recent model-free successes. Without making any assumptions about the structure of the environment model and its possible imperfections, our approach learns in an end-to-end way to extract useful knowledge gathered from model simulations -- in particular not relying exclusively on simulated returns. This allows the agent to benefit from model-based imagination without the pitfalls of conventional model-based planning. We demonstrate that our approach performs better than model-free baselines in various domains including Sokoban. It achieves better performance with less data, even with imperfect models, a significant step towards delivering the promises of model-based RL.

<!-- chunk {"id": "body-0007", "role": "body", "section": "The I2A architecture", "weight": 1.0} -->

In order to augment model-free agents with imagination, we rely on environment models -- models that, given information from the present, can be queried to make predictions about the future. We use these environment models to simulate *imagined trajectories*, which are interpreted by a neural network and provided as additional context to a policy network.

<!-- chunk {"id": "body-0008", "role": "body", "section": "The I2A architecture", "weight": 1.0} -->

In general, an environment model is any recurrent architecture which can be trained in an unsupervised fashion from agent trajectories: given a past state and current action, the environment model predicts the next state and any number of signals from the environment. In this work, we will consider in particular environment models that build on recent successes of action-conditional next-step predictors, which receive as input the current observation (or history of observations) and current action, and predict the next observation, and potentially the next reward. We roll out the environment model over multiple time steps into the future, by initializing the imagined trajectory with the present time real observation, and subsequently feeding simulated observations into the model.

<!-- chunk {"id": "body-0009", "role": "body", "section": "The I2A architecture", "weight": 1.0} -->

The actions chosen in each rollout result from a rollout policy $\hat{\pi}$ (explained in Section 3.1). The environment model together with $\hat{\pi}$ constitute the imagination core module, which predicts next time steps (Fig 1a). The imagination core is used to produce $n$ trajectories $\hat{\mathcal{T}_{1}},\ldots,\hat{\mathcal{T}_{n}}$. Each imagined trajectory $\hat{\mathcal{T}}$ is a sequence of features $({\hat{f}}_{t + 1},\ldots,{\hat{f}}_{t + \tau})$, where $t$ is the current time, $\tau$ the length of the rollout, and ${\hat{f}}_{t + i}$ the output of the environment model (i.e. the predicted observation and/or reward).

<!-- chunk {"id": "body-0010", "role": "body", "section": "The I2A architecture", "weight": 1.0} -->

Despite recent progress in training better environment models, a key issue addressed by I2As is that a learned model cannot be assumed to be perfect; it might sometimes make erroneous or nonsensical predictions. We therefore do not want to rely solely on predicted rewards (or values predicted from predicted states), as is often done in classical planning. Additionally, trajectories may contain information beyond the reward sequence (a trajectory could contain an informative subsequence -- for instance solving a subproblem -- which did not result in higher reward). For these reasons, we use a rollout encoder $\mathcal{E}$ that processes the imagined rollout as a whole and *learns to interpret it*, i.e. by extracting any information useful for the agent's decision, or even ignoring it when necessary (Fig 1b). Each trajectory is encoded separately as a rollout embedding $e_{i} = {\mathcal{E}{(\hat{\mathcal{T}_{i}})}}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "The I2A architecture", "weight": 1.0} -->

Finally, an aggregator $\mathcal{A}$ converts the different rollout embeddings into a single imagination code $c_{\text{ia}} = {\mathcal{A}{(e_{1},\ldots,e_{n})}}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "The I2A architecture", "weight": 1.0} -->

The final component of the I2A is the policy module, which is a network that takes the information $c_{ia}$ from model-based predictions, as well as the output $c_{\text{mf}}$ of a model-free path (a network which only takes the real observation as input; see Fig 1c, right), and outputs the imagination-augmented policy vector $\pi$ and estimated value $V$. The I2A therefore learns to combine information from its model-free and imagination-augmented paths; note that without the model-based path, I2As reduce to a standard model-free network. I2As can thus be thought of as augmenting model-free agents by providing additional information from model-based planning, and as having strictly more expressive power than the underlying model-free agent.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Rollout strategy", "weight": 1.0} -->

For our experiments, we perform one rollout for each possible action in the environment. The first action in the $\text{i}^{\text{th}}$ rollout is the $\text{i}^{\text{th}}$ action of the action set $\mathcal{A}$, and subsequent actions for all rollouts are produced by a shared rollout policy $\hat{\pi}$. We investigated several types of rollout policies (random, pre-trained) and found that a particularly efficient strategy was to distill the imagination-augmented policy into a model-free policy. This distillation strategy consists in creating a small model-free network $\hat{\pi}{(o_{t})}$, and adding to the total loss a cross entropy auxiliary loss between the imagination-augmented policy $\pi{(o_{t})}$ as computed on the current observation, and the policy $\hat{\pi}{(o_{t})}$ as computed on the same observation.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Rollout strategy", "weight": 1.0} -->

By imitating the imagination-augmented policy, the internal rollouts will be similar to the trajectories of the agent in the real environment; this also ensures that the rollout corresponds to trajectories with high reward. At the same time, the imperfect approximation results in a rollout policy with higher entropy, potentially striking a balance between exploration and exploitation.

<!-- chunk {"id": "body-0015", "role": "body", "section": "I2A components and environment models", "weight": 1.0} -->

In our experiments, the encoder is an LSTM with convolutional encoder which sequentially processes a trajectory $\mathcal{T}$. The features ${\hat{f}}_{t}$ are fed to the LSTM in reverse order, from ${\hat{f}}_{t + \tau}$ to ${\hat{f}}_{t + 1}$, to mimic Bellman type backup operations.^11^1The choice of forward, backward or bi-directional processing seems to have relatively little impact on the performance of the I2A, however, and should not preclude investigating different strategies. The aggregator simply concatenates the summaries. For the model-free path of the I2A, we chose a standard network of convolutional layers plus one fully connected one \e.g.. We also use this architecture on its own as a baseline agent.

<!-- chunk {"id": "body-0016", "role": "body", "section": "I2A components and environment models", "weight": 1.0} -->

Our environment model (Fig. 2) defines a distribution which is optimized by using a negative log-likelihood loss $l_{\text{model}}$. We can either pretrain the environment model before embedding it (with frozen weights) within the I2A architecture, or jointly train it with the agent by adding $l_{\text{model}}$ to the total loss as an auxiliary loss. In practice we found that pre-training the environment model led to faster runtime of the I2A architecture, so we adopted this strategy.

<!-- chunk {"id": "body-0017", "role": "body", "section": "I2A components and environment models", "weight": 1.0} -->

For all environments, training data for our environment model was generated from trajectories of a partially trained standard model-free agent (defined below). We use partially pre-trained agents because random agents see few rewards in some of our domains. However, this means we have to account for the budget (in terms of real environment steps) required to pretrain the data-generating agent, as well as to then generate the data. In the experiments, we address this concern in two ways: by explicitly accounting for the number of steps used in pretraining (for Sokoban), or by demonstrating how the same pretrained model can be reused for many tasks (for MiniPacman).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Agent training and baseline agents", "weight": 1.0} -->

Using a fixed pretrained environment model, we trained the remaining I2A parameters with asynchronous advantage actor-critic (A3C). We added an entropy regularizer on the policy $\pi$ to encourage exploration and the auxiliary loss to distill $\pi$ into the rollout policy $\hat{\pi}$ as explained above. We distributed asynchronous training over 32 to 64 workers; we used the RMSprop optimizer. We report results after an initial round of hyperparameter exploration (details in Appendix A). Learning curves are averaged over the top three agents unless noted otherwise.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Agent training and baseline agents", "weight": 1.0} -->

A separate hyperparameter search was carried out for each agent architecture in order to ensure optimal performance. In addition to the I2A, we ran the following baseline agents (see Appendix B for architecture details for all agents).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Agent training and baseline agents", "weight": 1.0} -->

Standard model-free agent. For our main baseline agent, we chose a model-free standard architecture similar to, consisting of convolutional layers ($2$ for MiniPacman, and $3$ for Sokoban) followed by a fully connected layer. The final layer, again fully connected, outputs the policy logits and the value function. For Sokoban, we also tested a 'large' standard architecture, where we double the number of all feature maps (for convolutional layers) and hidden units (for fully connected layers). The resulting architecture has a slightly larger number of parameters than I2A.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Agent training and baseline agents", "weight": 1.0} -->

Copy-model agent. Aside from having an internal environment model, the I2A architecture is very different from the one of the standard agent. To verify that the information contained in the environment model rollouts contributed to an increase in performance, we implemented a baseline where we replaced the environment model in the I2A with a 'copy' model that simply returns the input observation. Lacking a model, this agent does not use imagination, but uses the same architecture, has the same number of learnable parameters (the environment model is kept constant in the I2A), and benefits from the same amount of computation (which in both cases increases linearly with the length of the rollouts). This model effectively corresponds to an architecture where policy logits and value are the final output of an LSTM network with skip connections.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Sokoban experiments", "weight": 1.0} -->

We now demonstrate the performance of I2A over baselines in a puzzle environment, Sokoban. We address the issue of dealing with imperfect models, highlighting the strengths of our approach over planning baselines. We also analyze the importance of the various components of the I2A.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Sokoban experiments", "weight": 1.0} -->

Sokoban is a classic planning problem, where the agent has to push a number of boxes onto given target locations. Because boxes can only be pushed (as opposed to pulled), many moves are irreversible, and mistakes can render the puzzle unsolvable. A human player is thus forced to plan moves ahead of time. We expect that artificial agents will similarly benefit from internal simulation. Our implementation of Sokoban procedurally generates a new level each episode (see Appendix D.4 for details, Fig. 3 for examples). This means an agent cannot memorize specific puzzles.^22^2Out of 40 million levels generated, less than 0.7% were repeated. Training an agent on 1 billion frames requires less than 20 million episodes. Together with the planning aspect, this makes for a very challenging environment for our model-free baseline agents, which solve less than 60% of the levels after a billion steps of training (details below). We provide videos of agents playing our version of Sokoban online.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Sokoban experiments", "weight": 1.0} -->

While the underlying game logic operates in a $10 \times 10$ grid world, our agents were trained directly on RGB sprite graphics as shown in Fig. 4 (image size $80 \times 80$ pixels). There are no aspects of I2As that make them specific to grid world games.

<!-- chunk {"id": "body-0025", "role": "body", "section": "I2A performance vs. baselines on Sokoban", "weight": 1.0} -->

Since using imagined rollouts is helpful for this task, we investigate how the length of individual rollouts affects performance. The latter was one of the hyperparameters we searched over. A breakdown by number of unrolling/imagination steps in Fig. 4 (right) shows that using longer rollouts, while not increasing the number of parameters, increases performance: 3 unrolling steps improves speed of learning and top performance significantly over 1 unrolling step, 5 outperforms 3, and as a test for significantly longer rollouts, 15 outperforms 5, reaching above 90% of levels solved. However, in general we found diminishing returns with using I2A with longer rollouts. It is noteworthy that 5 steps is relatively small compared to the number of steps taken to solve a level, for which our best agents need about 50 steps on average. This implies that even such short rollouts can be highly informative. For example, they allow the agent to learn about moves it cannot recover from (such as pushing boxes against walls, in certain contexts).

<!-- chunk {"id": "body-0026", "role": "body", "section": "I2A performance vs. baselines on Sokoban", "weight": 1.0} -->

Because I2A with rollouts of length 15 are significantly slower, in the rest of this section, we choose rollouts of length 5 to be our canonical I2A architecture.

<!-- chunk {"id": "body-0027", "role": "body", "section": "I2A performance vs. baselines on Sokoban", "weight": 1.0} -->

It terms of data efficiency, it should be noted that the environment model in the I2A was pretrained (see Section 3.2). We conservatively measured the total number of frames needed for pretraining to be lower than 1e8. Thus, even taking pretraining into account, I2A outperforms the baselines after seeing about 3e8 frames in total (compare again Fig. 4 (left)). Of course, data efficiency is even better if the environment model can be reused to solve multiple tasks in the same environment (Section 5).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Learning with imperfect models", "weight": 1.0} -->

One of the key strengths of I2As is being able to handle learned and thus potentially imperfect environment models. However, for the Sokoban task, our learned environment models actually perform quite well when rolling out imagined trajectories. To demonstrate that I2As can deal with less reliable predictions, we ran another experiment where the I2A used an environment model that had shown much worse performance (due to a smaller number of parameters), with strong artifacts accumulating over iterated rollout predictions (Fig. 5, left). As Fig. 5 (right) shows, even with such a clearly flawed environment model, I2A performs similarly well. This implies that I2As can learn to ignore the latter parts of the rollout as errors accumulate, but still use initial predictions when errors are less severe. Finally, note that in our experiments, surprisingly, the I2A agent with poor model ended outperforming the I2A agent with good model. We posit this was due to random initialization, though we cannot exclude the noisy model providing some form of regularization --- more work will be required to investigate this effect.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Learning with imperfect models", "weight": 1.0} -->

*Learning* a rollout encoder is what enables I2As to deal with imperfect model predictions. We can further demonstrate this point by comparing them to a setup without a rollout encoder: as in the classic Monte-Carlo search algorithm of Tesauro and Galperin, we now explicitly estimate the value of each action from rollouts, rather than learning an arbitrary encoding of the rollouts, as in I2A. We then select actions according to those values. Specifically, we learn a value function $V$ from states, and, using a rollout policy $\hat{\pi}$, sample a trajectory rollout for each initial action, and compute the corresponding estimated Monte Carlo return ${\sum_{t \leq T}{\gamma^{t}r_{t}^{a}}} + {V{(x_{T}^{a})}}$ where ${({(x_{t}^{a},r_{t}^{a})})}_{t = 0..T}$ comes from a trajectory initialized with action a.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Learning with imperfect models", "weight": 1.0} -->

Action $a$ is chosen with probability proportional to $\exp{({- {{({{\sum_{t = 0..T}{\gamma^{t}r_{t}^{a}}} + {V{(x_{T}^{a})}}})}/\delta}})}$, where $\delta$ is a learned temperature. This can be thought of as a form of I2A with a fixed summarizer (which computes returns), no model-free path, and very simple policy head. In this architecture, only $V,\hat{\pi}$ and $\delta$ are learned.^33^3the rollout policy is still learned by distillation from the output policy We ran this rollout encoder-free agent on Sokoban with both the accurate and the noisy environment model. We chose the length of the rollout to be optimal for each environment model (from the same range as for I2A, i.e. from 1 to 5).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Learning with imperfect models", "weight": 1.0} -->

As can be seen in Fig. 5 (right),^44^4Note: the MC curves in Fig. 5 only used a single agent rather than averages. when using the high accuracy environment model, the performance of the encoder-free agent is similar to that of the baseline standard agent. However, unlike I2A, its performance degrades catastrophically when using the poor model, showcasing the susceptibility to model misspecification.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Further insights into the workings of the I2A architecture", "weight": 1.0} -->

So far, we have studied the role of the rollout encoder. To show the importance of various other components of the I2A, we performed additional control experiments. Results are plotted in Fig. 4 (left) for comparison. First, I2A with the copy model (Section 3.3) performs far worse, demonstrating that the environment model is indeed crucial. Second, we trained an I2A where the environment model was predicting no rewards, only observations. This also performed worse. However, after much longer training (3e9 steps), these agents did recover performance close to that of the original I2A (see Appendix D.2), which was never the case for the baseline agent even with that many steps. Hence, reward prediction is helpful but not absolutely necessary in this task, and imagined observations alone are informative enough to obtain high performance on Sokoban. Note this is in contrast to many classical planning and model-based reinforcement learning methods, which often rely on reward prediction.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Imagination efficiency and comparison with perfect-model planning methods", "weight": 1.0} -->

In previous sections, we illustrated that I2As can be used to efficiently solve planning problems and can be robust in the face of model misspecification. Here, we ask a different question -- if we *do* assume a nearly perfect model, how does I2A compare to competitive planning methods? Beyond raw performance we focus particularly on the efficiency of planning, i.e. the number of imagination steps required to solve a fixed ratio of levels. We compare our regular I2A agent to a variant of Monte Carlo Tree Search (MCTS), which is a modern guided tree search algorithm. For our MCTS implementation, we aimed to have a strong baseline by using recent ideas: we include transposition tables, and evaluate the returns of leaf nodes by using a value network (in this case, a deep residual value network trained with the same total amount of data as I2A; see appendix D.3 for further details).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Imagination efficiency and comparison with perfect-model planning methods", "weight": 1.0} -->

Running MCTS on Sokoban, we find that it can achieve high performance, but at a cost of a much higher number of necessary environment model simulation steps: MCTS reaches the I2A performance of $87\%$ of levels solved when using 25k model simulation steps on average to solve a level, compared to 1.4k environment model calls for I2A. Using even more simulation steps, MCTS performance increases further, e.g. reaching $95\%$ with 100k steps.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Imagination efficiency and comparison with perfect-model planning methods", "weight": 1.0} -->

If we assume access to a high-accuracy environment model (including the reward prediction), we can also push I2A performance further, by performing basic Monte-Carlo search with a trained I2A for the rollout policy: we let the agent play whole episodes in simulation (where I2A itself uses the environment model for short-term rollouts, hence corresponding to using a model-within-a-model), and execute a successful action sequence if found, up to a maximum number of retries; this is reminiscent of nested rollouts. With a fixed maximum of 10 retries, we obtain a score of $95\%$ (up from $87\%$ for the I2A itself). The total average number of model simulation steps needed to solve a level, including running the model in the outer loop, is now 4k, again much lower than the corresponding MCTS run with 100k steps. Note again, this approach requires a nearly perfect model; we don't expect I2A with MC search to perform well with approximate models. See Table 2 for a summary of the imagination efficiency for the different methods.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Generalization experiments", "weight": 1.0} -->

Lastly, we probe the generalization capabilities of I2As, beyond handling random level layouts in Sokoban. Our agents were trained on levels with $4$ boxes. Table 2 shows the performance of I2A when such an agent was tested on levels with different numbers of boxes, and that of the standard model-free agent for comparison. We found that I2As generalizes well; at $7$ boxes, the I2A agent is still able to solve more than half of the levels, nearly as many as the standard agent on $4$ boxes.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Learning one model for many tasks in MiniPacman", "weight": 1.0} -->

In our final set of experiments, we demonstrate how a single model, which provides the I2A with a general understanding of the dynamics governing an environment, can be used to solve a collection of different tasks. We designed a simple, light-weight domain called MiniPacman, which allows us to easily define multiple tasks in an environment with shared state transitions and which enables us to do rapid experimentation.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Learning one model for many tasks in MiniPacman", "weight": 1.0} -->

In MiniPacman (Fig. 6, left), the player explores a maze that contains food while being chased by ghosts. The maze also contains power pills; when eaten, for a fixed number of steps, the player moves faster, and the ghosts run away and can be eaten. These dynamics are common to all tasks. Each task is defined by a vector $w_{\text{rew}} \in {\mathbb{R}}^{5}$, associating a reward to each of the following five events: moving, eating food, eating a power pill, eating a ghost, and being eaten by a ghost. We consider five different reward vectors inducing five different tasks. Empirically we found that the reward schemes were sufficiently different to lead to very different high-performing policies^55^5For example, in the 'avoid' game, any event is negatively rewarded, and the optimal strategy is for the agent to clear a small space from food and use it to continuously escape the ghosts. (for more details on the game and tasks, see appendix C.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Learning one model for many tasks in MiniPacman", "weight": 1.0} -->

To illustrate the benefits of model-based methods in this multi-task setting, we train a single environment model to predict both observations (frames) and events (as defined above, e.g. \"eating a ghost\"). Note that the environment model is effectively shared across all tasks, so that the marginal cost of learning the model is nil. During training and testing, the I2As have access to the frame and reward predictions generated by the model; the latter was computed from model event predictions and the task reward vector $w_{\text{rew}}$. As such, the reward vector $w_{\text{rew}}$ can be interpreted as an 'instruction' about which task to solve in the same environment \cf. the Frostbite challenge of. For a fair comparison, we also provide all baseline agents with the event variable as input.^66^6It is not necessary to provide the reward vector $w_{\text{rew}}$ to the baseline agents, as it is equivalent a constant bias.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Learning one model for many tasks in MiniPacman", "weight": 1.0} -->

We trained baseline agents and I2As separately on each task. Results in Fig. 6 (right) indicate the benefit of the I2A architecture, outperforming the standard agent in all tasks, and the copy-model baseline in all but one task. Moreover, we found that the performance gap between I2As and baselines is particularly high for tasks 4 & 5, where rewards are particularly sparse, and where the anticipation of ghost dynamics is especially important. We posit that the I2A agent can leverage its environment and reward model to explore the environment much more effectively.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Discussion", "weight": 1.5} -->

We presented I2A, an approach combining model-free and model-based ideas to implement *imagination-augmented RL*: learning to interpret environment models to augment model-free decisions. I2A outperforms model-free baselines on MiniPacman and on the challenging, combinatorial domain of Sokoban. We demonstrated that, unlike classical model-based RL and planning methods, I2A is able to successfully use imperfect models (including models without reward predictions), hence significantly broadening the applicability of model-based RL concepts and ideas.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Discussion", "weight": 1.5} -->

As all model-based RL methods, I2As trade-off environment interactions for computation by pondering before acting. This is essential in irreversible domains, where actions can have catastrophic outcomes, such as in Sokoban. In our experiments, the I2A was always less than an order of magnitude slower per interaction than the model-free baselines. The amount of computation can be varied (it grows linearly with the number and depth of rollouts); we therefore expect I2As to greatly benefit from advances on dynamic compute resource allocation (e.g. Graves ). Another avenue for future research is on abstract environment models: learning predictive models at the \"right\" level of complexity and that can be evaluated efficiently at test time will help to scale I2As to richer domains.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Discussion", "weight": 1.5} -->

Remarkably, on Sokoban I2As compare favourably to a strong planning baseline (MCTS) with a perfect environment model: at comparable performance, I2As require far fewer function calls to the model than MCTS, because their model rollouts are guided towards relevant parts of the state space by a learned rollout policy. This points to further potential improvement by training rollout policies that \"learn to query\" imperfect models in a task-relevant way.
