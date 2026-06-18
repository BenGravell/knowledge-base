<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Safe Reinforcement Learning via Shielding

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Reinforcement learning algorithms discover policies that maximize reward, but do not necessarily guarantee safety during learning or execution phases. We introduce a new approach to learn optimal policies while enforcing properties expressed in temporal logic. To this end, given the temporal logic specification that is to be obeyed by the learning system, we propose to synthesize a reactive system called a shield. The shield is introduced in the traditional learning process in two alternative ways, depending on the location at which the shield is implemented. In the first one, the shield acts each time the learning agent is about to make a decision and provides a list of safe actions. In the second way, the shield is introduced after the learning agent. The shield monitors the actions from the learner and corrects them only if the chosen action causes a violation of the specification. We discuss which requirements a shield must meet to preserve the convergence guarantees of the learner. Finally, we demonstrate the versatility of our approach on several challenging reinforcement learning scenarios.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Advances in learning have enabled a new paradigm for developing controllers for autonomous systems that are able to accomplish complicated tasks in possibly uncertain and dynamic environments. For example, in reinforcement learning (RL), an agent acts to optimize a long-term return that models the desired behavior for the agent and is revealed to it incrementally in a reward signal as it interacts with its environment. Increasing use of learning-based controllers in physical systems in the proximity of humans also strengthens the concern of whether these systems will operate safely.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

While convergence, optimality and data-efficiency of learning algorithms are relatively well understood, safety or more generally correctness during learning and execution of controllers has attracted significantly less attention. A number of different notions of safety were recently explored. We approach the problem of ensuring safety in reinforcement learning from a formal methods perspective. We begin with an unambiguous and rich set of specifications of what safety and more generally correctness mean. To this end, we adopt temporal logic as a specification language. For algorithmic purposes, we focus on the so-called safety fragment of (linear) temporal logic. We then investigate the question "how can we let, whenever it is fine, a learning agent do whatever it is doing, and also monitor and interfere with its operation whenever absolutely needed in order to ensure safety?" In this paper, we introduce *shielded learning*, a framework that allows to apply machine learning to control systems in a way that the *correctness* of the system's execution against a given specification is assured during the learning and controller execution phases, regardless of how fast the learning process converges.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the traditional reinforcement learning setting, in every time step, the learning agent chooses an action and sends it to the environment. The environment evolves according to the action and sends the agent an observation of its state and a reward associated with the underlying transition. The objective of the learning agent is to optimize the reward accumulated over this evolution.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our approach introduces a *shield* into the traditional reinforcement learning setting. The shield is computed upfront from the safety part of the given system specification and an abstraction of the agent's environment dynamics. It ensures *safety* and *minimum interference*. With minimum interference we mean that the shield restricts the agent as little as possible and forbids actions only if they could endanger safe system behavior.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We modify the loop between the learning agent and its environment in two alternative ways, depending on the location at which the shield is implemented. In the first one, depicted in Fig. 1, the shield is implemented before the learning agent and acts each time the learning agent is to make a decision and provides a list of safe actions. This list restricts the choices for the learner. The shield provides minimum interference, since it allows the agent to follow any policy as long as it is safe. In the alternative implementation of the shield, depicted in Fig. 2, it monitors the actions selected by the learning agent and corrects them if and only if the chosen action is unsafe.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Shielding offers several pragmatic advantages: Even though the inner working of learning algorithms is often complex, shielding with respect to critical safety specifications may be manageable (as we demonstrate in upcoming sections). The algorithms we present for the computation of shields make relatively mild assumptions on the input-output structure of the learning algorithm (rather than its inner working). Consequently, the correctness guarantees are agnostic---to an extent to be described precisely---to the learning algorithm of choice. Our setup introduces a clear boundary between the learning agent and the shield. This boundary helps to separate the concerns, e.g., safety and correctness on one side and convergence and optimality on the other and provides a basis for the convergence analysis of a shielded reinforcement learning algorithm. Last but not least, the shielding framework is compatible with mechanisms such as function approximation, employed by learning algorithms in order to improve their scalability.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Safety in Reinforcement Learning", "weight": 1.0} -->

An exploration process is called *safe* if no undesirable states are ever visited, which can only be achieved through the incorporation of external knowledge. The safety fragment of temporal logic that we consider is more general than the notion of safety of (which is technically a so-called *invariance property* ). One way of guiding exploration in learning is to provide *teacher advice*. A teacher (usually a human) provides advice (e.g., safe actions) when either the learner or the teacher considers it to be necessary to prevent catastrophic situations. For example, in a Q-learning setting, the agent acts on the teacher's advice, whenever advice is provided. Otherwise, the agent chooses randomly between the set of actions with the highest Q-values. In each time step, the human teacher tunes the reward signal before sending it to the agent. Our work is closely related to teacher-guided RL, since a shield can be considered as a teacher, who provides safe actions only if absolutely necessary. In contrast to previous work, the reward signal does not have to be manipulated by the shield, since the shield corrects unsafe actions in the learning and deployment phases.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Safety in Formal Methods", "weight": 1.0} -->

Traditional correct-by-construction controller computation techniques are based on computing an abstraction of the environment dynamics and deriving a controller that guarantees to satisfy the specification under the known environment dynamics. Such methods combine *reactive synthesis* with faithful environment modelling and abstraction. Wongpiromsarn et al. define a receding horizon control approach that combines continuous control with discrete correctness guarantees. For simple system dynamics, the controller can be computed directly. For more complex dynamics, both approaches are computationally too difficult. A mitigation strategy is to compute a set of low-level motion primitives to be combined to an overall strategy. Having many motion primitives however also leads to inefficiency. All of the above approaches have in common that a faithful, yet precise enough, abstraction of the physical environment is required, which is not only difficult to obtain in practice, but also introduces the mentioned computational burden. Control methods based on reinforcement learning partly address this problem, but do not typically incorporate any correctness guarantees. Wen et al. propose a method to combine strict correctness guarantees with reinforcement learning.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Safety in Formal Methods", "weight": 1.0} -->

They start with a non-deterministic correct-by-construction strategy and then perform reinforcement learning to limit it towards cost optimality without having to know the cost function a priori. Unlike the approach in the paper, their technique does not work with function approximation, which prevents it from being used in complex scenarios. Junges et al. adopt a similar framework in a stochastic setting. A major difference between the works by Wen et al. and Junges et al. on the one hand and the shielding framework on the other hand is the fact that the computational cost of the construction of the shield depends on the complexity of the specification and a very abstract version of the system, and is independent of the state space components of the system to be controlled that are irrelevant for enforcing the safety specification. Fu et al. establish connections between temporal-logic-constrained strategy synthesis in Markov decision processes and probably-approximately-correct-type bounds in learning. Bloem et al. proposed the idea to synthesize a *shield* that is attached to a system to enforce safety properties at run time. We adopt this idea, and present our own realization of a shield, geared to the needs of the learning setting.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Safety Specifications, Abstractions, and Game Solving", "weight": 1.0} -->

The goal of this paper is to combine the best of two worlds, namely the formal correctness guarantees of a controller with respect to a temporal logic specification, as provided by formal methods (and reactive synthesis in particular), and the optimality with respect to an a priori unknown performance criterion, as provided by reinforcement learning.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Safety Specifications, Abstractions, and Game Solving", "weight": 1.0} -->

Consider the example of a path planner for autonomous vehicles. Many general requirements on system behaviors such as safety concerns may be known and expressed as specifications in temporal logic and can be enforced by reactive controllers. This includes always driving in the correct lane, never jumping the red light, and never exceeding the speed limit. A learning algorithm is able to incorporate more subtle considerations, such as specific intentions for the current application scenario and personal preferences of the human driver, such as reaching some goal quickly but at the same time driving smoothly.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Example 1", "weight": 1.0} -->

We want to learn an energy-efficient controller for a hot water storage tank, depicted in Figure 3. Water stored in the task is kept warm by a heater whose energy consumption depends on the filling level of the tank, but we do not know what the exact relationship is.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Example 1", "weight": 1.0} -->

The outflow is always between 0 and 1 liters per second, and the inflow is known to be between 1 and 2 liters per second whenever the valve is open (and it is 0 otherwise). The capacity of the tank is limited to 100 liters, and whenever the inflow is switched on or off, the setting has to be kept for at least three seconds to limit the wear-out of the valve. Also, the tank must never overflow or run dry.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Example 1", "weight": 1.0} -->

Let us now formalize this example.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Example 1", "weight": 1.0} -->

The specification consists of four conjuncts, where the first two conjuncts enforce the water levels to be between the minimum and maximum thresholds. The next conjunct enforces that if the valve is open and then closed, then it has to stay closed for two more time steps (seconds). The final conjunct enforces that if the valve is closed and then opened, it has to stay open for two more time steps.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Example 1", "weight": 1.0} -->

We can translate the specification to the safety automaton shown in Figure 4. It uses the action sets $\mathcal{A} = {\{{\mathsf{o}\mathsf{p}\mathsf{e}\mathsf{n}},{\mathsf{c}\mathsf{l}\mathsf{o}\mathsf{s}\mathsf{e}\mathsf{d}}\}}$ for the inflow valve state, and the label set $L = {\{{level} < 1,1 \leq {level} \leq 99,{level} > 99\}}$ as needed information about the water tank filling status. What we know about the behavior of the water tank can be summarized as the abstraction automaton given in Figure 5.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Example 1", "weight": 1.0} -->

We will show in Section 6 how to compute a shield from an abstraction automaton and a safety specification automaton. We will then revisit this example and give the resulting shield that enforces the specification. The shield will enforce that when the water level in the tank becomes too low, the inflow valve is opened until some minimum level of $4$ is reached, and it will also prevent the inflow from being opened when the level is above $93$. The latter is necessary as the valve has to stay open for at least three time steps. So as the inflow may be up to 2 liters/second during this time and the outflow may be 0, there is otherwise an overflow risk. As the shield is generated using the specification, it plans ahead for this not to happen, so it must prevent the opening of the inflow valve if the level is above $93$. Note that for more complicated specifications, the shield behavior can become much more complicated as well.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Framework for Shielded Reinforcement Learning", "weight": 1.0} -->

In this section, we introduce a *correct-by-construction* reactive system, called a shield, into the traditional learning process. We propose two different ways to modify the loop between the learning agent and its environment: In Sec. 5.1 we introduce the shield *before* the learning agent. In each time step, the shield modifies the list of actions available to the learner by providing a list of safe actions that the learning agent can choose. In Sec. 5.2 the shield is implemented *after* the learning agent. The shield monitors the actions selected by the learning agent, and overwrites them if and only if the chosen action is unsafe. Based on the location at which the shield is applied, we call it *preemptive* shielding and *post-posed* shielding, respectively. For both settings we make the following assumptions.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

\(i\) The environment can be modeled as an MDP $\mathcal{M} = {(S,s_{I},\mathcal{A},\mathcal{P},\mathcal{R})}$. (ii) We have constructed an abstraction $\varphi^{\mathcal{M}}$. (iii) The learner accepts elements from $S \times Q$ as state input (for the state space of the shield $Q$).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

We describe the operation of a learner and a shield together in this section, and give the construction for computing the shield in the next section. In both preemptive and post-posed shielding, the shield will be given as a reactive system $\mathcal{S} = {(Q,q_{0},\Sigma_{I},\Sigma_{O},\delta,\lambda)}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Preemptive Shielding", "weight": 1.0} -->

Fig. 6 depicts the preemptive shielding setting. The interaction between the agent, the environment and the shield is as follows: At every time step $t$, the shield computes a set of all safe actions $\{ a_{t}^{1},\ldots,a_{t}^{k}\}$, i.e., it takes the set of all actions available, and removes all unsafe actions that would violate the safety specification $\varphi_{s}$. The agent receives this list from the shield, and picks an action $a_{t} \in {\{ a_{t}^{1},\ldots,a_{t}^{k}\}}$ from it. The environment executes action $a_{t}$, moves to a next state $s_{t + 1}$, and provides the reward $r_{t + 1}$. The task of the shield is basically to modify the set of available actions of the agent in every time step such that only safe actions remain.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Preemptive Shielding", "weight": 1.0} -->

More formally, for a preemptive shield, we have $\Sigma_{O} = 2^{\mathcal{A}}$, as the shield outputs the set of actions for the learner to choose from for the respective next step. The shield observes the label of the last MDP state in the sequence so far and provides the set of safe actions. For selecting the next transition of the finite-state machine that represents the shield, it also makes use of the action actually chosen by the agent. So for the input alphabet of the shield, we have $\Sigma_{I} = {\Sigma_{I}^{1} \times \Sigma_{I}^{2}}$ with $\Sigma_{I}^{1} = L$ and $\Sigma_{I}^{2} = \mathcal{A}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Properties of Preemptive Shielding", "weight": 1.0} -->

The preemptive shielding approach can also be seen as transforming the original MDP $\mathcal{M}$ into a new MDP $\mathcal{M}^{\prime} = {(S^{\prime},s_{I},\mathcal{A}^{\prime},\mathcal{P}^{\prime},\mathcal{R}^{\prime})}$ with the unsafe actions at each state removed, and where $S^{\prime}$ is the product of the original MDP and the state space of the shield. For each $s \in S^{\prime}$, we create a new subset of available actions $\mathcal{A}_{s}^{\prime} \subseteq \mathcal{A}_{s}$ by applying the shield to $\mathcal{A}_{s}$ and eliminating all unsafe actions.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Properties of Preemptive Shielding", "weight": 1.0} -->

From each state $s \in S^{\prime}$, the transition function $\mathcal{P}^{\prime}$ contains only transition distributions from $\mathcal{P}$ for actions contained in $\mathcal{A}_{s}^{\prime}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Post-Posed Shielding", "weight": 1.0} -->

We propose a second shielding setting, in which the shield is placed after the learning algorithm, as shown in Fig. 7. The shield monitors the actions of the agent, and substitutes the selected actions by safe actions whenever this is necessary to prevent the violation of $\varphi^{s}$. In each step $t$, the agent selects an action $a_{t}^{1}$. The shield forwards $a_{t}^{1}$ to the environment, i.e., $a_{t} = a_{t}^{1}$. Only if $a_{t}^{1}$ is unsafe with respect to $\varphi_{s}$, the shield selects a different safe action $a_{t} \neq a_{t}^{1}$ instead. The environment executes $a_{t}$, moves to $s_{t + 1}$ and provides $r_{t + 1}$. The agent receives $a_{t}$ and $r_{t + 1}$, and performs policy updates based on that information.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Post-Posed Shielding", "weight": 1.0} -->

For the executed action $a_{t}$, the agent updates its policy using $r_{t + 1}$. The question is what the reward for $a_{t}^{1}$ should be in case we have $a_{t} \neq a_{t}^{1}$. We discuss two different approaches.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Post-Posed Shielding", "weight": 1.0} -->

Assign a punishment $r_{t + 1}^{\prime}$ to $a_{t}^{1}$. The agent assigns a punishment $r_{t + 1}^{\prime} < 0$ to the unsafe action $a_{t}^{1}$ and learns that selecting $a_{t}^{1}$ at state $s_{t}$ is unsafe, without ever violating $\varphi^{s}$. However, there is no guarantee that unsafe actions are not part of the final policy. Therefore, the shield has to remain active even after the learning phase.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Post-Posed Shielding", "weight": 1.0} -->

Assign the reward $r_{t + 1}$ to $a_{t}^{1}$. The agent updates the unsafe action $a_{t}^{1}$ with the reward $r_{t + 1}$. Therefore, picking unsafe actions can likely be part of an optimal policy by the agent. Since an unsafe action is always mapped to a safe one, this does not pose a problem and the agent never has to learn to avoid unsafe actions. Consequently, the shield is (again) needed during the learning and execution phases.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Properties of Post-Posed Shielding", "weight": 1.0} -->

The big advantage of post-posed shielding is that it works even if the learning algorithm is already in the execution phase and therefore follows a fixed policy. In every step, the learning algorithm only sees the state of the MDP (without the state of the shield), and then the shield corrects the learner's actions whenever this is necessary to ensure safe operation of the system. The learning agent does not even need to know that it is shielded.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Properties of Post-Posed Shielding", "weight": 1.0} -->

In order to be less restrictive to the learning algorithm, we propose that in every time step, the agent provides a ranking ${rank_{t}} = {(a_{t}^{1},\ldots,a_{t}^{k})}$ on the allowed actions, i.e., the agent wants $a_{t}^{1}$ to be executed the most, $a_{t}^{2}$ to be executed the second most, etc. The ranking does not have to contain all available actions, i.e. $1 \leq {|{rank_{t}}|} \leq n$, where $n$ is the number of available actions in step $t$. The shield selects the first action $a_{t} \in {rank_{t}}$ that is safe according to $\varphi^{s}$. Only if all actions in $rank_{t}$ are unsafe, the shield selects a safe action $a_{t} \notin {rank_{t}}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Properties of Post-Posed Shielding", "weight": 1.0} -->

Both approaches for updating the policy discussed before can naturally be extended for a ranking of several actions. A second advantage of having a ranking on actions is that the learning agent can perform several policy updates at once; e.g., if all actions in $rank_{t}$ are unsafe, the agent can perform ${|{rank_{t}}|} + 1$ policy updates in one step by using the rewards $r_{t + 1}^{\prime}$ or $r_{t + 1}$ for all of them, depending on which of the above variants is used.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Shield Synthesis Algorithm for Reinforcement Learning", "weight": 1.0} -->

A shield $\mathcal{S}$ is introduced into the traditional learning process, either before or after the learning agent. In both cases, $\mathcal{S}$ enforces two properties: *correctness* and *minimum interference*. First, $\mathcal{S}$ enforces correctness against a given safety specification $\varphi^{s}$ at run time. With minimum interference, we mean that the shield restricts the agent as rarely as possible. The shield $\mathcal{S}$ is computed by reactive synthesis from $\varphi^{s}$ and an MDP abstraction $\varphi^{\mathcal{M}}$ that represents the environment in which the agent shall operate.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Shield Synthesis Algorithm for Reinforcement Learning", "weight": 1.0} -->

In this section, we give an algorithm to compute shields for preemptive shielding and post-posed shielding. We prove that the computed shields enforce the correctness criterion, and are the minimally interfering shields among those that enforce $\varphi^{s}$ on all MDPs for which $\varphi^{\mathcal{M}}$ is an abstraction.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Shield Synthesis Algorithm for Reinforcement Learning", "weight": 1.0} -->

The first steps of constructing the shield are the same for both variations of shielding. Given is an RL problem in which an agent has to learn an optimal policy for an unknown environment that can be modelled by an MDP $\mathcal{M} = {(S,s_{I},\mathcal{A},\mathcal{P},\mathcal{R})}$ while satisfying a safety specification $\varphi^{s} = {(Q,q_{0},\Sigma,\delta,F)}$ with $\Sigma = {\Sigma_{I} \times \Sigma_{O}}$ and $\mathcal{A} = \Sigma_{O}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Shield Synthesis Algorithm for Reinforcement Learning", "weight": 1.0} -->

We assume some abstraction $\varphi^{\mathcal{M}} = {(Q_{\mathcal{M}},q_{0,\mathcal{M}},{\mathcal{A} \times L},\delta_{\mathcal{M}},F_{\mathcal{M}})}$ of $\mathcal{M}$ for some MDP observer function $f:{S\rightarrow L}$ to be given. Since $\varphi^{s}$ models a restriction of the traces of the MDP and the learner together that we want to enforce, we assume it to have $\Sigma = {L \times \mathcal{A}}$, i.e., it reads the part of the system behavior that the abstraction is concerned. We perform the following steps for both shield types.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Shield Synthesis Algorithm for Reinforcement Learning", "weight": 1.0} -->

We translate $\varphi^{s}$ and $\varphi^{\mathcal{M}}$ to a safety game $\mathcal{G} = {(G,g_{0},\Sigma_{I},\Sigma_{O},\delta,F^{g})}$ between two players. In the game, the environment player chooses the next observations from the MDP state (i.e., elements from $L$), and the system chooses the next action.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Shield Synthesis Algorithm for Reinforcement Learning", "weight": 1.0} -->

In the construction, the state space of the game is the product between the specification automaton state set and the abstraction state set. The safe states in the game (in the set $F^{g}$) are the ones at which either the specification automaton is in a safe state, or the abstraction is in an unsafe state. The latter case represents that the observed MDP behavior differs from the behavior that was modeled in the abstraction. For game solving, it is important that such cases (whose occurrence in the field witnesses the incorrectness of the abstraction) count as winning for the system player, as the system player only needs to work correctly in environments that conform to the abstraction.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Shield Synthesis Algorithm for Reinforcement Learning", "weight": 1.0} -->

Next, we compute the winning region $W \subseteq F^{g}$ of $G$ by standard safety game solving as described.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Shield Synthesis Algorithm for Reinforcement Learning", "weight": 1.0} -->

To simplify $\mathcal{S}$, it makes sense to optionally remove all states that are unreachable from $q_{0,\mathcal{S}}$ after constructing $\mathcal{S}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Shield Synthesis Algorithm for Reinforcement Learning", "weight": 1.0} -->

To exemplify these steps, let us reconsider the example from Section 4. Building the product game between the specification automaton and the MDP abstraction leads to a game with 602 states (if we merge all states in $F \times Q_{\mathcal{M}}$ into a single error state and all states in $Q \times {({Q_{\mathcal{M}} \smallsetminus F_{\mathcal{M}}})}$ into a single [paradise state] from which the game is always won by the system). If we solve the game, then most of the states are winning, but a few are not. Figure 8 shows a small fraction of the game that contains such non-winning states. We can see that, in state $(q_{3},q_{d})$, the system should not choose action $close$, as otherwise the system cannot avoid to reach $q_{fail}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Shield Synthesis Algorithm for Reinforcement Learning", "weight": 1.0} -->

It could be the case that $q_{fail}$ is actually not reached (when the environment chooses to let the level stay the same for a step), but we cannot be sure because we have to consider all evolutions of the environment to be possible that are consistent with our abstraction. Thus, the shield needs to deactivate the $close$ action in state $(q_{3},q_{d})$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Shield Synthesis Algorithm for Reinforcement Learning", "weight": 1.0} -->

The shield allows all actions that are guaranteed to lead to a state in $W$, no matter what the next observation is. Since these states, by the definition of the set of winning states, are exactly the ones from which the system player can enforce not to ever visit a state not in $F$, the shield is minimally interfering. It disables all actions that may lead to an error state (according to the abstraction).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Shield Synthesis Algorithm for Reinforcement Learning", "weight": 1.0} -->

The construction of a post-posed shield is very similar to the construction of the preemptive shield. The main difference is that the post-posed shield always outputs a single action. Thus, the last step of the construction above should read as follows.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Shield Synthesis Algorithm for Reinforcement Learning", "weight": 1.0} -->

The construction can be extended naturally if a ranking of actions ${rank}_{t} = {\{ a_{t}^{1},\ldots,a_{t}^{n}\}}$ is provided by the agent. Then, the shield selects the first action $a_{t} = a_{t}^{i}$ that is allowed by $\varphi^{s}$. Only if all actions in ${rank}_{t}$ are unsafe, the shield is allowed to deviate and to select a safe action $a_{t} \notin {rank_{t}}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Correctness and Minimal Interference of the Shields", "weight": 1.0} -->

We now prove that the shields computed according to the definitions indeed have the claimed properties, namely correctness, and minimal interference. For brevity, we detail the case of preemptive shields. The line of reasoning for post-posed shielding is similar.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Correctness", "weight": 1.0} -->

A shield works correctly if for every trace ${s_{0}a_{0}s_{1}a_{1}\ldots} \in {({S \times \mathcal{A}})}^{\omega}$ that MDP, shield and learner can together produce, we have that ${({f{(s_{0})}},a_{0})}{({f{(s_{1})}},a_{1})}\ldots$ is in the language of the specification automaton $\varphi^{S}$ for the MDP labeling function $f$. Additionally, the shield must always report at least one available action at every step.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Correctness", "weight": 1.0} -->

By the construction of the shield, it only has reachable states $(q^{S},q^{\mathcal{M}})$ that are in the set of winning positions. For all possible next labels $l \in L$, there exists at least one action such that if the action is taken, then the next state $(q^{\prime S},{}_{}^{})$ is winning as well. Therefore, the shield cannot deadlock. As far as correctness is concerned, the $q^{S}$ component of the run of the shield will always reflect the state of the safety automaton along the trace, and since a winning strategy makes sure that only winning states are ever visited along a play, by the definition of $F^{g}$, the error state of $\varphi^{S}$ can only be visited after the error state for the abstraction MDP has been visited (and hence the abstraction turned out to be incorrect).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Minimal Interference", "weight": 1.0} -->

Let the shield, learner, and MDP together produce a prefix trace $s_{0}a_{0}s_{1}a_{1}s_{2}a_{2}\ldotss_{k}$ that induces a (prefix) run ${q_{0}q_{1}\ldotsq_{k - 1}} \in Q^{\ast}$ of the safety automaton $\varphi^{S}$ that we used as the representation of the specification for building the shield. Assume that the shield deactivates an action $a_{k + 1}$ that is available from state $s_{k}$ in the MDP.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Minimal Interference", "weight": 1.0} -->

We show that the shield had to deactivate $a_{k + 1}$ as there is another MDP that is consistent with the observed behavior and the abstraction for which, regardless of the learner's policy, there is a non-zero probability to violate the specification after the trace prefix $s_{0}a_{0}s_{1}a_{1}s_{2}a_{2}\ldotss_{k}a_{k + 1}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Minimal Interference", "weight": 1.0} -->

Assume now that action $a_{k + 1}$ was activated after the prefix trace $s_{0}a_{0}s_{1}a_{1}s_{2}a_{2}\ldotss_{k}$ while the shield is in a state $(q^{\mathcal{S}},q^{\mathcal{M}})$. We have that $\mathcal{M}^{\prime}$ is an MDP in which every finite-length label sequence that is possible in the abstraction for some action sequence has a non-zero probability to occur if the action sequence is chosen. Due to the construction of the shield by game solving, action $a_{k + 1}$ is only deactivated in state $(q^{\mathcal{S}},q^{\mathcal{M}})$ if in the game, the environment player had a strategy to violate $\varphi^{S}$ using only traces allowed by the abstraction. Since $\varphi^{S}$ is a safety property, the violation would occur in finite time.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Minimal Interference", "weight": 1.0} -->

Since in $\mathcal{M}^{\prime}$, all finite traces that can occur in the abstraction have a non-zero probability, activating $a_{k + 1}$ (and the learner choosing $a_{k + 1}$) would imply a non-zero proability to violate the specification in the future, no matter what the learner does in the future. Hence, the shield could not prevent a violation in such a case, and $a_{k + 1}$ needs to be deactivated.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Convergence", "weight": 1.0} -->

Define an MDP $\mathcal{M} = {(S,s_{I},\mathcal{A},\mathcal{P},\mathcal{R})}$, with discrete state set $S$, discrete state-dependent action sets $\mathcal{A}_{s}$, and state-dependent transition functions $\mathcal{P}_{s}{(a,{s’})}$ that define the probability of transitioning to state $s’$ when taking action $a$ in state $s$. Assume also that a shield $\mathcal{S} = {(Q_{\mathcal{S}},q_{0,\mathcal{S}},\Sigma_{I,\mathcal{S}},\Sigma_{O,\mathcal{S}},\delta_{\mathcal{S}},\lambda_{\mathcal{S}})}$ is given for $\mathcal{M}$ and for some MDP labeling function $f:{S\rightarrow L}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Convergence", "weight": 1.0} -->

For both preemptive and post-posed shielding, we can build a product MDP $\mathcal{M}^{\prime}$ that represents the behavior of the shield and the MDP together. Since $\mathcal{M}’$ is a standard MDP, all learning algorithms that converge on standard MDPs can be shown to converge in the presence of a shield under this construction. Note that for the postposed shield case, this argument requires that whenever an action ranking is chosen by the learner that does not contain a safe action, there is a fixed probability distribution over the safe actions executed by the learner instead. This distribution may depend on the state of the MDP and the shield and the selected ranking, but must be constant over time, as otherwise we could not model the joint behavior of the shield and the environment MDP as a product MDP.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Convergence", "weight": 1.0} -->

In both the post-posed and preemptive cases, we make use of the fact that the learner has access to the state of the shield and can base its actions on it in this argument. Shields can be relatively large---especially for complex abstractions and specifications---as they have both the state spaces of the abstraction and the specification automaton as factors. On the other hand, for specifications of the form "at all points during the execution, the label of the MDP states should have a certain form", the specification automaton has only a single state (plus an error state). The state space of the shield is then exactly the state space of the abstraction (plus paradise states and error states). If the abstraction state can furthermore be determined from the respective last MDP state label, then the shield can be modified to have a single state (plus error states and paradise states). The requirements from Assumption 1 can then be relaxed by allowing the learner to only observe the state of the MDP (rather than the states of both the MDP and the shield) because, if the MDP behaves according to the abstraction, then the paradise state is never visited.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Convergence", "weight": 1.0} -->

At the same time, the shield ensures that no error state is ever visited. Hence, the state space of $\mathcal{M}^{\prime}$ can be restructured to have to the same state space of $\mathcal{M}$. In such a case, it suffices for the learner to observe the current state as state of $\mathcal{M}$ rather than $\mathcal{M}^{\prime}$. To the learner, this is indistinguishable from operating on $\mathcal{M}$ without a shield.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Experiments", "weight": 1.0} -->

We applied shielded reinforcement learning in four domains: a robot in 9x9 and 15x9 grid worlds, a self-driving car scenario, an Atari^®^ game called *Seaquest™*, and the water tank example from Section 4. For clarity, we compare between a subset of shielding settings which we later specify for each problem. The simulations were performed on a computer equipped with an Intel^®^ Core™i7-4790K and 16 GB of RAM running a 64-bit version of Ubuntu^®^ 16.04 LTS. Source code, input files, and detailed instructions to reproduce our experiments are available for download.^11^1

<!-- chunk {"id": "body-0059", "role": "body", "section": "Grid world Example", "weight": 1.0} -->

We performed two experiments on a robot in a grid world. Snapshots of these environments are shown in Fig. 9. In both experiments, the robot's objective is to visit all the colored regions in a given order while maintaining one or both of the following safety properties.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Grid world Example", "weight": 1.0} -->

$\varphi_{1}^{s}$: the robot must not crash into walls or the moving opponent agent. This specification applies to both experiments.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Grid world Example", "weight": 1.0} -->

$\varphi_{2}^{s}$: the robot must not stay on a bomb for more than two consecutive steps. This specification applies only to the 9x9 experiment.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Grid world Example", "weight": 1.0} -->

Fig. 10 shows the deterministic finite automata corresponding to $\varphi_{1}^{s}$ and $\varphi_{2}^{s}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Grid world Example", "weight": 1.0} -->

If the robot visits all marked regions in a given order (called episode), a reward is granted, and if a safety property is violated, a penalty is applied. The agent uses tabular Q-learning with an $\epsilon$-greedy explorer that is capable of multiple policy updates at once.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Grid world Example", "weight": 1.0} -->

In the 9x9 grid-world, we synthesized a shield from $\varphi_{1}^{s} \land \varphi_{2}^{s}$ and the (precise) environment abstraction in $2$ seconds. In the 15x9 experiment, we synthesized a shield from the (precise) environment abstraction and $\varphi_{1}^{s}$ to prevent crashes into the wall and the moving opponent agent in $0.6$ seconds.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Grid world Example", "weight": 1.0} -->

Fig. 11 shows that only the unshielded versions experience negative rewards. Furthermore, the shielded versions are not only safe, but also tend to learn more rapidly. Whenever an unsafe action is picked, the agent updates at least two actions with a ${|{rank_{t}}|} = 1$ shield, and up to 4 actions with a ${|{rank_{t}}|} = 3$. Fig. 11 (right) shows that only the shielded version ${|{rank_{t}}|} = 3$ without penalty (blue, dashed) finds the optimal path, resulting in a higher average reward. In scenarios with ${|{rank_{t}}|} = 1$ (red) or with penalties (solid), the agent computes a suboptimal path. In Fig. 11 (left), we compare between no shielding (red, dashed), no shielding with large penalties for unsafe actions (blue, solid), and a ${|{rank_{t}}|} = 3$ post-posed shielding with penalties for corrected actions (green, solid).

<!-- chunk {"id": "body-0066", "role": "body", "section": "Grid world Example", "weight": 1.0} -->

The unshielded version with large penalty does not reach the maximum reward score as the other two versions. In addition, the unshielded version does not speed up the learning of the agent as the ${|{rank_{t}}|} = 3$ does.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Self-Driving Car Example", "weight": 1.0} -->

This example considers an agent that learns to drive around a block in a clockwise direction in an environment with the size of 480x480 pixels. In each step, the car moves 3 pixel in the direction of its heading and can make a maximum turn of $7.5$ degrees on the shortest direction to the commanded heading. After each step, the value of the reward and the new state of the car are returned. The state consists of the following four variables: the car's position in the x-axis, its position in the y-axis, the cosine and the sine of its heading. The safety specification in this example is to avoid crashing into a wall. The input to the shield is calculated from the car's state. It represents the side of the car with a distance less than 60 pixels away from any of the walls. Both of the preemptive and the post-posed shields were synthesized in $2$ seconds. In each step, a positive reward is given if the car moves a step in a clockwise direction and a penalty is given if it moves in a counter-clockwise direction. A crash into the wall results in a penalty and a restart.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Self-Driving Car Example", "weight": 1.0} -->

The agent uses a Deep Q-Network (DQN) with a Boltzmann exploration policy. This network consists of four input nodes for the state variables, eight outputs nodes for the headings and three hidden layers.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Self-Driving Car Example", "weight": 1.0} -->

The plot in Fig. 12 shows that the accumulated rewards for unshielded reinforcement learning (red, dashed) increases over time, but still experiences crashes at the end of the simulation. The shielded version without punishment (blue, solid) learns more rapidly than the unshielded learning scenario and never crashes.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Atari^®^ 2600 Seaquest™", "weight": 1.0} -->

*Seaquest™* is a underwater combat game in which the agent controls a submarine. The agent has to pick up divers under water, while avoiding or destroying various objects, and must get to the surface before it runs out of oxygen. The goal of the agent is to maximize the game score.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Atari^®^ 2600 Seaquest™", "weight": 1.0} -->

For our experiments, we used the OpenAI Gym^11^1 library that integrates the Arcade Learning Environment (ALE), and a Python implementation^22^2 of DeepMind's Deep Reinforcement Learning approach. The agent receives as input only RGB images of the screen as in Fig. 13 (right). The agent is used purely as a black box, only changing actions that violate the specification described below.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Atari^®^ 2600 Seaquest™", "weight": 1.0} -->

We model two simple safety properties. First, the submarine has to surface before oxygen runs out ($\varphi_{1}^{s}$). Secondly, the submarine is not allowed to surface if it has enough oxygen but has not collected any divers yet ($\varphi_{2}^{s}$). The specification $\varphi^{s} = {\varphi_{1}^{s} \land \varphi_{2}^{s}}$ decides when the submarine has to surface and when it is not allowed to surface, depending on the actual depth, the status of the oxygen reserves, and the number of collected divers. We compute all inputs of the shield from the state of the Atari^®^ simulator. The results illustrated in Fig. 13 (left) show that shielding the learner did not change its performance, however, the safety properties $\varphi_{1}^{s} \land \varphi_{2}^{s}$ were not violated when shielding the learner.

<!-- chunk {"id": "body-0073", "role": "body", "section": "The Water Tank Example", "weight": 1.0} -->

In the example shown in Fig. 3, the tank must never run dry or overflow by controlling the inflow switch ($\varphi_{1}^{s}$). In addition, the inflow switch must not change its mode of operation before 3 time steps have passed since the last mode change ($\varphi_{2}^{s}$). Refer to example 1 of section 4, for a full description of the abstract water tank dynamics and specification. We generated a concrete MDP for this example in which the energy consumption depends only on the state and there are multiple local minima. A post-posed shield was synthesized from $\varphi_{1}^{s} \land \varphi_{2}^{s}$, in less than a second.

<!-- chunk {"id": "body-0074", "role": "body", "section": "The Water Tank Example", "weight": 1.0} -->

Fig. 14 shows that both shielded (dashed lines) and unshielded Q-learning and SARSA experiments (solid lines) do reach an optimal policy. However, the shielded implementations reach the optimal policy in a significantly shorter time than the unshielded implementations.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We developed a method for reinforcement learning under safety constraints expressed as temporal logic specifications. The method is based on shielding the decisions of the underlying learning algorithm from violating the specification. We proposed an algorithm for the automated synthesis of shields for given temporal logic specifications. Even though the inner working of a learning algorithm is often complex, the safety criteria may still be enforced by possibly simple means. Shielding exploits this possibility.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Conclusion", "weight": 1.5} -->

A shield depends only on the monitored input-output behavior, the environment abstraction, and the correctness specifications -- it is independent of the intricate details of the underlying learning algorithm.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We demonstrated the use of shielded learning on several reinforcement learning scenarios. In all of them, the shielded agents perform at least as well as the unshielded ones. In most cases, our approach even improved the learning performance.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The main downside of our approach is that in order to prevent the learner from making unsafe actions, some approximate model of when which action is unsafe needs to be available. We argue that this is unavoidable if the allowed actions depend on the state of the environment, as otherwise there is no way to know which actions are allowed. Our experiments show, however, that in applications in which safe learning is needed, the effort to construct an abstraction is well-spent, as our approach not only makes learning safe, but also shows great promise of improving learning performance.
