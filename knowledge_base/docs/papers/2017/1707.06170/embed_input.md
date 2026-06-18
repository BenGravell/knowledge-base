<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Model-based Planning from Scratch

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Conventional wisdom holds that model-based planning is a powerful approach to sequential decision-making. It is often very challenging in practice, however, because while a model can be used to evaluate a plan, it does not prescribe how to construct a plan. Here we introduce the "Imagination-based Planner", the first model-based, sequential decision-making agent that can learn to construct, evaluate, and execute plans. Before any action, it can perform a variable number of imagination steps, which involve proposing an imagined action and evaluating it with its model-based imagination. All imagined actions and outcomes are aggregated, iteratively, into a "plan context" which conditions future real and imagined actions. The agent can even decide how to imagine: testing out alternative imagined actions, chaining sequences of actions together, or building a more complex "imagination tree" by navigating flexibly among the previously imagined states using a learned policy. And our agent can learn to plan economically, jointly optimizing for external rewards and computational costs associated with using its imagination. We show that our architecture can learn to solve a challenging continuous control problem, and also learn elaborate planning strategies in a discrete maze-solving task.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our work opens a new direction toward learning the components of a model-based planning system and how to use them.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model-based planning involves proposing sequences of actions, evaluating them under a model of the world, and refining these proposals to optimize expected rewards. Several key advantages of model-based planning over model-free methods are that models support generalization to states not previously experienced, help express the relationship between present actions and future rewards, and can resolve states which are aliased in value-based approximations. These advantages are especially pronounced in problems with complex and stochastic environmental dynamics, sparse rewards, and restricted trial-and-error experience. Yet even with an accurate model, planning is often very challenging because while a model can be used to evaluate a plan, it does not prescribe how to construct a plan.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Existing techniques for model-based planning are most effective in small-scale problems, often require background knowledge of the domain, and use pre-defined solution strategies. Planning in discrete state and action spaces typically involves exploring the search tree for sequences of actions with high expected value, and apply fixed heuristics to control complexity (e.g., A\*, beam search, Monte Carlo Tree Search coulom2006efficient ). In problems with continuous state and action spaces the search tree is effectively infinite, so planning usually involves sampling sequences of actions to evaluate according to assumptions about smoothness and other regularities in the state and action spaces busoniu2010reinforcement; hren2008optimistic; munos2011optimistic; weinstein2012bandit. While most modern methods for planning exploit the statistics of an individual episode, few can learn across episodes and be optimized for a given task. And even fewer attempt to learn the actual planning strategy itself, including the transition model, the policy for choosing how to sample sequences of actions, and procedures for aggregating the proposed actions and evaluations into a useful plan.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Here we introduce the Imagination-based Planner (IBP), a model-based agent which learns from experience all aspects of the planning process: how to construct, evaluate, and execute a plan. The IBP learns when to act versus when to imagine, and if imagining, how to select states and actions to evaluate which will help minimize its external task loss and internal resource costs. Through training, it effectively develops a planning algorithm tailored to the target problem. The learned algorithm allows it to flexibly explore, and exploit regularities, the state and action spaces. The IBP framework can be applied to both continuous and discrete problems. In two experiments we evaluated a continuous IBP implementation on a challenging continuous control task, and a discrete IBP in a maze-solving problem.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

A fully learnable model-based planning agent for continuous control.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

An agent that learns to construct a plan via model-based imagination.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

An agent which uses its model of the environment in two ways: for imagination-based planning and gradient-based policy optimization.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

A novel approach for learning to build, navigate, and exploit "imagination trees".

<!-- chunk {"id": "body-0011", "role": "body", "section": "Model", "weight": 1.0} -->

The definition of planning we adopt here involves an agent proposing sequences of actions, evaluating them with a model, and following a policy that depends on these proposals and their predicted results. Our IBP implements a recurrent policy capable of planning via four key components (Figure 1). On each step, the manager chooses whether to imagine or act. If acting, the controller produces an action which is executed in the world. If imagining, the controller produces an action which is evaluated by the model-based imagination. In both cases, data resulting from each step are aggregated by the memory and used to influence future actions. The collective activity of the IBP's components supports various strategies for constructing, evaluating, and executing a plan.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Model", "weight": 1.0} -->

On each iteration, $i$, the IBP either executes an action in the world or imagines the consequences of a proposed action. The actions executed in the world are indexed by $j$, and the sequence of imagination steps the IBP performs before an action are indexed by $k$. Through the planning and acting processes, two types of data are generated: external and internal. External data includes observable world states, $s_{j}$, executed actions, $a_{j}$, and obtained rewards, $r_{j}$. Internal data includes imagined states, ${\hat{s}}_{j,k}$, actions, ${\hat{a}}_{j,k}$, and rewards, ${\hat{r}}_{j,k}$, as well as the manager's decision about whether to act or imagine (and how to imagine), termed the "route", $u_{j,k}$, the number of actions and imaginations performed, and all other auxiliary information from each step.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Model", "weight": 1.0} -->

We summarize the external and internal data for a single iteration as $d_{i}$, and the history of all external and internal data up to, and including, the present iteration as, $h_{i} = {(d_{0},\ldots,d_{i})}$. The set of all imagined states since the previous executed action are $\{{\hat{s}}_{j,0},\ldots,{\hat{s}}_{j,k}\}$, where ${\hat{s}}_{j,0}$, is initialized as the current world state, $s_{j}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Model", "weight": 1.0} -->

The manager, $\pi^{M}:{\mathcal{H}\rightarrow\mathcal{P}}$, is a discrete policy which maps a history, $h \in \mathcal{H}$, to a route, $u \in \mathcal{U}$. The $u$ determines whether the agent will execute an action in the environment, or imagine the consequences of a proposed action. If imagining, the route can also select which previously imagined, or real, state to imagine. We define $\mathcal{U} = {\{{act},{\hat{s}}_{j,0},\ldots,{\hat{s}}_{j,k}\}}$, where $act$ is the signal to act in the world, and the ${\hat{s}}_{j,l}$ signals to propose and evaluate an action from imagined state, ${\hat{s}}_{j,l}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Model", "weight": 1.0} -->

The controller, $\pi^{C}:{{\mathcal{S} \times \mathcal{H}}\rightarrow\mathcal{A}}$, is a contextualized action policy which maps a state $s \in \mathcal{S}$ and a history to an action, $a \in \mathcal{A}$. The state which is provided as input to the controller is determined by the manager's choice of $u$. If executing, the actual state, $s_{j}$, is always used. If imagining, the state ${\hat{s}}_{j,l}$ is used, as mentioned above. There are different possible imagination strategies, detailed below, which determine which state is used for imagination.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Model", "weight": 1.0} -->

The imagination, $I:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathcal{S} \times \mathcal{R}}}$ is a model of the world, which maps states, $s \in \mathcal{S}$, and actions, $a \in \mathcal{A}$, to consequent states, $s^{\prime} \in \mathcal{S}$, and scalar rewards, $r \in \mathcal{R}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Model", "weight": 1.0} -->

The memory, $\mu:{{\mathcal{D} \times \mathcal{H}}\rightarrow\mathcal{H}}$, recurrently aggregates the external and internal data generated from one iteration, $d \in \mathcal{D}$, to update the history, i.e., $h_{i} = {\mu{(d_{i},h_{i - 1})}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Model", "weight": 1.0} -->

Constructing a plan involves the IBP choosing to propose and imagine actions, and building up a record of possible sequences of actions' expected quality. If a sequence of actions predicted to yield high reward is identified, the manager can then choose to act and the controller can produce the appropriate actions.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Model", "weight": 1.0} -->

We explored three distinct imagination-based planning strategies: "$1$-step", "$n$-step", and "tree" (see Figure 2). They differ only by how the manager selects, from the actual state and all imagined states since the last action, the state from which to propose and evaluate an action. For $1$-step imagination, the IBP must imagine from the actual state, ${\hat{s}}_{j,0}$. This induces a depth-$1$ tree of imagined states and actions (see Figure 2, first row of graphs). For $n$-step imagination, the IBP must imagine from the most recent previously imagined state, ${\hat{s}}_{j,k}$. This induces a depth-$n$ chain of imagined states and actions (see Figure 2, second row of graphs). For trees, the manager chooses whether to imagine from the actual state or any previously imagined state since the last actual action, $\{{\hat{s}}_{j,0},\ldots,{\hat{s}}_{j,k}\}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Model", "weight": 1.0} -->

This induces an "imagination tree", because imagined actions can be proposed from any previously imagined state (see Figure 2, third row of graphs).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Spaceship task", "weight": 1.0} -->

We evaluated our model in a challenging continuous control task adapted from the "Spaceship Task" in hamrick2017metacontrol, which we call "Spaceship Task 2.0". The agent must pilot an initially stationary spaceship in 2-D space from a random initial position at a radius between $0.6$ and $1$ distance units, and a random mass between $0.004$ and $0.36$ mass units, to its mothership, which is always set to position $$. The agent can fire its thrusters with a force of its choice, which accelerates its velocity by $F = {ma}$. There are five stationary planets in the scene, at random positions at a radius between $0.4$ and $1$ distance units and with masses that vary between $0.08$ and $0.4$ mass units. The planets' gravitational fields accelerate the spaceship, which induces complex, non-linear dynamics. A single action entailed the ship firing its thrusters on the first time step, then traveling under ballistic motion for 11 time steps under the gravitational dynamics.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Spaceship task", "weight": 1.0} -->

There are several other factors that influence possible solutions to the problem. The spaceship pilot must pay a linearly increasing price for fuel (${price} = {0.0002\text{~or~}0.0004}$ cost units), when the force magnitude is greater then a threshold value of $8$ distance units, i.e., ${fuel}\_{cost} = \max{(0,{({force}\_{magnitude} - 8)} \cdot {price}}$). This incentivizes the pilot to choose small thruster forces. We also included multiplicative noise in the control, which further incentivizes small controls and also bounds the resolution at the future states of the system can be accurately predicted.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Neural network implementation and training", "weight": 1.0} -->

We implemented our continuous IBP for the spaceship task using standard deep learning building blocks. The memory, $\mu$, was an LSTM hochreiter1997long. Crucially, the way the continuous IBP encodes a plan is by embedding $h_{i}$ into a "plan context", $c_{i}$, using $\mu$. Here the inputs to $\mu$ were the concatenation of a subset of $h_{i}$. For imagining, they were: $(p_{j,k},s_{j},{\hat{s}}_{j,p_{j,k}},{\hat{a}}_{j,k},{\hat{s}}_{j,{k + 1}},{\hat{r}}_{j,k},j,k,c_{i - 1})$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Neural network implementation and training", "weight": 1.0} -->

And the imagination-based model of the environment, $I$ was an interaction network (IN) battaglia2016interaction, a powerful neural architecture to model graph-like data. It took as input $({\hat{s}}_{j,k},{\hat{a}}_{j,k})$ and returned ${\hat{s}}_{j,{k + 1}}$ for imagining, and took $(s_{j},a_{j})$ and returned $s_{j + 1}$ for acting.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Neural network implementation and training", "weight": 1.0} -->

The continuous IBP was trained to jointly optimize two loss terms, the external task and internal resource losses. The task loss reflects the cost of executing an action in the world, including the fuel cost and final $L2$ distance to the mothership. The resource loss reflects the cost of using the imagination on a particular time step and only affects the manager. It could be fixed across an episode, or vary with the number of actions taken so far, expressing the constraint that imagining early is less expensive than imagining on-the-fly. The total loss that was optimized was the sum of the task and resource losses.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Neural network implementation and training", "weight": 1.0} -->

The training consisted of optimizing, by gradient descent (Adam kingma2014adam ), the parameters of the agent with respect to the task loss and internal resource costs. The computational graph of the IBP architecture was divided into three distinct subgraphs: 1) the model, 2) the manager, and 3) the controller and memory. Each subgraph's learnable parameters were trained simultaneously, on-policy, but independently from one another.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Neural network implementation and training", "weight": 1.0} -->

The $I$ model was trained to make next-step predictions of the state in a supervised fashion, with error gradients computed by backpropagation. The data was collected from the observations the agent makes when acting in the real world. Because $\pi^{M}$'s outputs were discrete, we used the REINFORCE algorithm williams1992simple to estimate its gradients. Its policy was stochastic, so we also applied entropy regularization during training to encourage exploration. The rewards for the manager consist of the negative sum between the internal and external loss (the cost of each step is payed at each step, while the $L_{2}$ loss is payed at the end of the sequence).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Neural network implementation and training", "weight": 1.0} -->

The $\pi^{C}$ and $\mu$ were trained jointly. Because the $\pi^{M}$'s output was non-differentiable, we treated the routes it chose for a given episode as constants during learning. This induced a computational graph which varied as a function of the route value, where the route was a switch that determined the gradients' backward flow. In order to approximate the error gradient with respect to an action executed in the world, we used stochastic value gradients (SVG) heess2015learning. We unrolled the full recurrent loop of imagined and real controls, and computed the error gradients using backpropagation through time. $\pi^{C}$ and $\mu$ are trained only to minimize the external loss, i.e. the fuel cost and the final L2 distance to the mothership, but not including the imagination cost. The training regime is similar to the one used in hamrick2017metacontrol.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Neural network implementation and training", "weight": 1.0} -->

In terms of strategies that we relied, beside 1-step and n-step we used only a restricted version of the imagination-tree strategy where the manager only selected from $\{{act},{\hat{s}}_{j,0},{\hat{s}}_{j,k}\}$ as depicted in Figure 2. While this reduced the range of trees the model can construct, it was presumably easier to train because it had a fixed number of discrete route choices, independent of $k$. Future work should explore using RNNs or local navigation within the tree to handle variable sized sets of route choices for the manager.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Results", "weight": 1.0} -->

Our first results show that the $1$-step lookahead IBP can learn to use its model-based imagination to improve its performance in a complex, continuous, sequential control task. Figure 3's first row depicts several example trajectories from a $1$-step IBP that was granted three external actions and up to two imagined actions per external action (a maximum of nine imagined and external actions). The IBP learned to often use its first two external actions to navigate to open regions of space, presumably to avoid the complex nonlinear dynamics imposed by the planets' gravitational fields, and then use its final action to seek the target location. It used its imagined actions to try out potential actions, which it refined iteratively. Figure 4a shows the performance of different IBP agents, which are granted one, two, and three external actions, and different maximum numbers of imagined actions. The task loss always decreased as a function of the maximum number of imagined actions. The version which was allowed only one external action (blue line) roughly corresponded to Hamrick et al.'s hamrick2017metacontrol IBMC.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Results", "weight": 1.0} -->

The IBP agents that could not use their imagination (left-most points, 0 imaginations per action) represents the SVG baselines on this domain: they could use their model to compute policy gradients during training, but could not use their model to evaluate proposed actions. These results provide clear evidence of the value of imagination for sequential decision-making, even with only 1-step lookahead.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Results", "weight": 1.0} -->

We also examined the $1$-step lookahead IBP's use of imagination as greater resource costs, $\tau$, were imposed (Figure 4b), and found that it smoothly decreased the total number of imagination steps to avoid this additional penalty, eventually using no imagination at all when under high values of $\tau$. The reason the low-cost agents (toward the left side of Figure 4b) did not use the full six imaginations allowed is because of the small entropy reward, which incentivized it to learn a policy with increased variance in its route choices. Figure 4c shows that the result of increased imagination cost, and decreased use of imagination was that the task loss increased.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Results", "weight": 1.0} -->

We also trained an $n$-step IBP in order to evaluate whether the IBP could construct longer-term plans, as well as a restricted imagination-tree IBP to determine whether it could learn more complex plan construction strategies. Figure 3's second row shows $n$-step IBP trajectories, and the third and fourth rows show two imagination-tree IBP trajectories. In this praticular task, after each execution the cost of an imagination step increases, making it more advantageous to plan early. Our results (Figure 4d-e) show that $n$-step IBP performance is better than $1$-step, and that an imagination-tree IBP outperforms both, especially when more maximum imagination steps are allowed, for two values of the fuel cost we applied. Note that imagination-tree IBP becomes more useful as the agent has more imagination steps to use.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiment 2: Discrete mazes", "weight": 1.0} -->

In the second, preliminary experiment, a discrete 2D maze-solving task, we implemented a discrete IBP to probe its use of different imagination strategies. For simplicity, the imagination used a perfect world model. The controller is given by a tabular representation, and the history represents incremental changes to it, caused by imagination steps. The memory's aggregation functionality was implemented by accumulating the updates induced by imagination steps into the history. The controller's policy was determined by the sum of the learned Q-value and the history tensor. The manager was a convolutional neural network (CNN) that took as input the current Q table, history tensor, and map layout.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiment 2: Discrete mazes", "weight": 1.0} -->

In this particular instance we explored IBP as a search strategy. We created mazes for which states would be aliased in the tabular Q representation. Each maze could have multiple candidate goal locations, and in each episode a goal location was selected at random from the candidates. An agent was instantiated to use a single set of Q-values for each maze and all its different goal locations. This would also allow a model-based planning agent to use imagined rollouts to disambiguate states and generalize to goal locations unseen during training.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiment 2: Discrete mazes", "weight": 1.0} -->

More results on these maze tasks can be found in the supplementary material.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiment 2: Discrete mazes", "weight": 1.0} -->

Single Maze Multiple Goals: We start by exploring state aliasing and generalization to out-of-distribution states. Figure 6 top row shows the prototypical setup we consider for this exploration, along with imagination rollout examples. During training, the agent only saw the first three goal positions, selected at random, but never the fourth. The reward was -1 for every step, except at the end, when the agent received as reward the number of steps left in its total budget of 20 steps.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiment 2: Discrete mazes", "weight": 1.0} -->

The amount of available actions at each position in the maze was small, so we limited the manager to a fixed policy that always expanded the next leaf node in the search tree which had the highest value. Figure 6 also showed the effect of having different number of imaginations to disambiguate the evaluated maze. With sufficient imagination steps, not only could the agent find all possible goals, but most importantly, it could resolve new goal positions not experienced during training.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiment 2: Discrete mazes", "weight": 1.0} -->

Multiple Mazes Multiple Goals: Here we illustrate how a learned manager adapts to different environments and proposes different imagination strategies. We used different mazes, some with more possible goal positions than others, and with different optimal strategies. We introduced a regularity that the manager could exploit: we made the wall layouts be correlated with the number of possible goal positions. The IBP learned a separate tabular control policy for each maze, but used a shared manager across all mazes.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experiment 2: Discrete mazes", "weight": 1.0} -->

This experiment also exposes a limitation of the simple imagination-tree strategy, where the manager can only choose to imagine only from $\{{\hat{s}}_{j,0},{\hat{s}}_{j,k}\}$. It can only proceed with imagining or reset back to the current world state. So if a different path should be explored, but part of its path overlaps with a previously explored path, the agent must waste imagination steps in reconstructing this overlapping segment.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experiment 2: Discrete mazes", "weight": 1.0} -->

One preliminary way to address this is to allow the manager to work with fixed-length macro actions done by the control policy, which effectively increases the imagination trees' branching factor while making the tree more shallow. In Supplementary Materials we show the benefits of using macros on a scaled up (7$\times$`<!-- -->`{=html}7) version of the tasks considered in Figure 6. Figure 5 shows the most common imagination trees constructed by the agent, highlighting the diversity of the IBP's learned planning strategies.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Discussion", "weight": 1.5} -->

We introduced a new approach for model-based planning that learns to construct, evaluate, and execute plans. Our continuous IBP represents the first fully learnable method for model-based planning in continuous control problems, using its model for both imagination-based planning and gradient-based policy optimization. Our results in the spaceship task show how the IBP's learned planning strategies can strike favorable trade-offs between external task loss and internal imagination costs, by sampling alternative imagined actions, chaining together sequences of imagined actions, and developing more complex imagination-based planning strategies. Our results on a 2D maze-solving task illustrate how it can learn to build flexible imagination trees, which inform its plan construction process and improve overall performance.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Discussion", "weight": 1.5} -->

In the future, the IBP should be applied to more diverse and natural decision-making problems, such as robotic control and higher-level problem solving. Other environment models should be explored, especially those which operate over raw sensory observations. The fact that the imagination is differentiable can be exploited for another form of model-based reasoning: online gradient-based control optimization.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our work demonstrates that the core mechanisms for model-based planning can be learned from experience, including implicit and explicit domain knowledge, as well as flexible plan construction strategies. By implementing essential components of a planning system with powerful, neural network function approximators, the IBP helps realize the promise of model-based planning and opens new doors for learning solution strategies in challenging problem domains.
