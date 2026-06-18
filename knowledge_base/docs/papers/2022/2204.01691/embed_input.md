<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Do as I Can, Not as I Say: Grounding Language in Robotic Affordances

Topics include Robotics, Large language models, Language models, Natural language.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Large language models can encode a wealth of semantic knowledge about the world. Such knowledge could be extremely useful to robots aiming to act upon high-level, temporally extended instructions expressed in natural language. However, a significant weakness of language models is that they lack real-world experience, which makes it difficult to leverage them for decision making within a given embodiment. For example, asking a language model to describe how to clean a spill might result in a reasonable narrative, but it may not be applicable to a particular agent, such as a robot, that needs to perform this task in a particular environment. We propose to provide real-world grounding by means of pretrained skills, which are used to constrain the model to propose natural language actions that are both feasible and contextually appropriate. The robot can act as the language model's "hands and eyes," while the language model supplies high-level semantic knowledge about the task. We show how low-level skills can be combined with large language models so that the language model provides high-level knowledge about the procedures for performing complex and temporally-extended instructions, while value functions associated with these skills provide the grounding necessary to connect this knowledge to a particular physical environment.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We evaluate our method on a number of real-world robotic tasks, where we show the need for real-world grounding and that this approach is capable of completing long-horizon, abstract, natural language instructions on a mobile manipulator. The project's website and the video can be found at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent progress in training large language models (LLMs) has led to systems that can generate complex text based on prompts, answer questions, or even engage in dialogue on a wide range of topics. These models absorb vast quantities of knowledge from text corpora mined from the web, and we might wonder whether knowledge of everyday tasks that is encoded in such models can be used by robots to perform complex tasks in the real world. But how can embodied agents extract and harness the knowledge of LLMs for physically grounded tasks?

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This question poses a major challenge. LLMs are not grounded in the physical world and they do not observe the consequences of their generations on any physical process. This can lead LLMs to not only make mistakes that seem unreasonable or humorous to people, but also to interpret instructions in ways that are nonsensical or unsafe for a particular physical situation. Figure 1 shows an example -- a kitchen robot capable of executing skills such as "pick up the sponge" or "go to the table" may be asked for help cleaning up a spill ("I spilled my drink, can you help?"). A language model may respond with a reasonable narrative that is not feasible or useful for the robot. "You could try using a vacuum cleaner" is impossible if there is no vacuum in the scene or if the robot is incapable of using one. With prompt engineering, a LLM may be capable of splitting the high-level instruction into sub-tasks, but it cannot do so without the context of what the robot is capable of given its abilities *and* the current state of the robot *and* the environment.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivated by this example, we study the problem of how to extract the knowledge in LLMs for enabling an embodied agent, such as a robot, to follow high-level textual instructions. The robot is equipped with a repertoire of learned skills for "atomic" behaviors that are capable of low-level visuomotor control. We make use of the fact that, in addition to asking the LLM to simply interpret an instruction, we can use it to score the likelihood that an individual skill makes progress towards completing the high-level instruction. Then, if each skill has an affordance function that quantifies how likely it is to succeed from the current state (such as a learned value function), its value can be used to weight the skill's likelihood. In this way, the LLM describes the probability that each skill contributes to completing the instruction, and the affordance function describes the probability that each skill will succeed -- combining the two provides the probability that each skill will perform the instruction *successfully*. The affordance functions make the LLM aware of the current scene, and constraining the completions to the skill descriptions makes the LLM aware of the robot's capabilities.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Furthermore, this combination results in a fully explainable sequence of steps that the robot will execute to accomplish an instruction -- an interpretable plan that is expressed through language.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our method, SayCan, extracts and leverages the knowledge within LLMs in physically-grounded tasks. The LLM (Say) provides a task-grounding to determine useful actions for a high-level goal and the learned affordance functions (Can) provide a world-grounding to determine what is possible to execute upon the plan. We use reinforcement learning (RL) as a way to learn language-conditioned value functions that provide affordances of what is possible in the world. We evaluate the proposed approach on 101 real-world robotic tasks that involve a mobile robot accomplishing a large set of language instructions in a real kitchen in a zero-shot fashion. Our experiments validate that SayCan can execute temporally-extended, abstract instructions. Grounding the LLM in the real-world via affordances nearly doubles the performance over the non-grounded baselines. Additionally, by evaluating the performance of the system with different LLMs, we show that a robot's performance can be improved simply by enhancing the underlying language model.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Large Language Models", "weight": 1.0} -->

Language models seek to model the probability $p{(W)}$ of a text $W = {\{ w_{0},w_{1},w_{2},\ldots,w_{n}\}}$, a sequence of strings $w$. This is generally done through factorizing the probability via the chain rule to be ${p{(W)}} = {\Pi_{j = 0}^{n}p{(\left. w_{j} \middle| w_{< j} \right.)}}$, such that each successive string is predicted from the previous. Recent breakthroughs initiated by neural network-based Attention architectures have enabled efficient scaling of so-called Large Language Models (LLMs). Such models include Transformers, BERT, T5, GPT-3, Gopher, LAMDA, FLAN, and PaLM, each showing increasingly large capacity (billions of parameters and terabytes of text) and subsequent ability to generalize across tasks.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Large Language Models", "weight": 1.0} -->

In this work, we utilize the vast semantic knowledge contained in LLMs to determine useful tasks for solving high-level instructions.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Value functions and RL", "weight": 1.0} -->

Our goal is to be able to accurately predict whether a skill (given by a language command) is feasible at a current state. We use temporal-difference-based (TD) reinforcement learning to accomplish this goal. In particular, we define a Markov decision process (MDP) $\mathcal{M} = {(\mathcal{S},\mathcal{A},P,R,\gamma)}$, where $\mathcal{S}$ and $\mathcal{A}$ are state and action spaces, $P:{{\mathcal{S} \times \mathcal{A} \times \mathcal{S}}\rightarrow{\mathbb{R}}_{+}}$ is a state-transition probability function, $R:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$ is a reward function and $\gamma$ is a discount factor.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Value functions and RL", "weight": 1.0} -->

The goal of TD methods is to learn state or state-action value functions (Q-function) $Q^{\pi}{(s,a)}$, which represents the discounted sum of rewards when starting from state $s$ and action $a$, followed by the actions produced by the policy $\pi$, i.e. ${Q^{\pi}{(s,a)}} = {{\mathbb{E}}_{a \sim {\pi{({a|s})}}}{\sum_{t}{R{(s_{t},a_{t})}}}}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Value functions and RL", "weight": 1.0} -->

In this work, we utilize TD-based methods to learn said value function that is additionally conditioned on the language command and utilize those to determine whether a given command is feasible from the given state. It is worth noting that in the undiscounted, sparse reward case, where the agent receives the reward of $1.0$ at the end of the episode if it was successful and $0.0$ otherwise, the value function trained via RL corresponds to an affordance function that specifies whether a skill is possible in a given state. We leverage that intuition in our setup and express affordances via value functions of sparse reward tasks.

<!-- chunk {"id": "body-0014", "role": "body", "section": "SayCan: Do As I Can, Not As I Say", "weight": 1.0} -->

Problem Statement. Our system receives a user-provided natural language instruction $i$ that describes a task that the robot should execute. The instruction can be long, abstract, or ambiguous. We also assume that we are given a set of skills $\Pi$, where each skill $\pi \in \Pi$ performs a short task, such as picking up a particular object, and comes with a short language description $\ell_{\pi}$ (e.g., "find a sponge") and an affordance function $p{(\left. c_{\pi} \middle| {s,\ell_{\pi}} \right.)}$, which indicates the probability of $c$-ompleting the skill with description $\ell_{\pi}$ successfully from state $s$. Intuitively, $p{(\left. c_{\pi} \middle| {s,\ell_{\pi}} \right.)}$ means "if I ask the robot to do $\ell_{\pi}$, will it do it?".

<!-- chunk {"id": "body-0015", "role": "body", "section": "SayCan: Do As I Can, Not As I Say", "weight": 1.0} -->

In RL terminology, $p{(\left. c_{\pi} \middle| {s,\ell_{\pi}} \right.)}$ is the value function for the skill if we take the reward to be $1$ for successful completion and $0$ otherwise.

<!-- chunk {"id": "body-0016", "role": "body", "section": "SayCan: Do As I Can, Not As I Say", "weight": 1.0} -->

As mentioned above, $\ell_{\pi}$ denotes the textual label of skill $\pi$ and $p{(\left. c_{\pi} \middle| {s,\ell_{\pi}} \right.)}$ denotes the probability that skill $\pi$ with textual label $\ell_{\pi}$ successfully completes if executed from state $s$, where $c_{\pi}$ is a Bernoulli random variable. The LLM provides us with $p{(\left. \ell_{\pi} \middle| i \right.)}$, the probability that a skill's textual label is a valid next step for the user's instruction. However, what we are interested in is the probability that a given skill successfully makes progress toward actually completing the instruction, which we denote as $p{(\left. c_{i} \middle| {i,s,\ell_{\pi}} \right.)}$. Assuming that a skill that succeeds makes progress on $i$ with probability $p{(\left.

<!-- chunk {"id": "body-0017", "role": "body", "section": "SayCan: Do As I Can, Not As I Say", "weight": 1.0} -->

\ell_{\pi} \middle| i \right.)}$ (i.e., its probability of being the right skill), and a skill that fails makes progress with probability zero, we can factorize this as ${p{(\left. c_{i} \middle| {i,s,\ell_{\pi}} \right.)}} \propto {p{(\left. c_{\pi} \middle| {s,\ell_{\pi}} \right.)}p{(\left. \ell_{\pi} \middle| i \right.)}}$. This corresponds to multiplying the probability of the language description of the skill given the instruction $p{(\left. \ell_{\pi} \middle| i \right.)}$, which we refer to as task-grounding, and the probability of the skill being possible in the current state of the world $p{(\left.

<!-- chunk {"id": "body-0018", "role": "body", "section": "SayCan: Do As I Can, Not As I Say", "weight": 1.0} -->

c_{\pi} \middle| {s,\ell_{\pi}} \right.)}$, which we refer to as world-grounding.

<!-- chunk {"id": "body-0019", "role": "body", "section": "SayCan: Do As I Can, Not As I Say", "weight": 1.0} -->

Connecting Large Language Models to Robots. While large language models can draw on a wealth of knowledge learned from copious amounts of text, they will not necessarily break down high-level commands into low-level instructions that are suitable for robotic execution. If a language model were asked "how would a robot bring me an apple", it may respond "a robot could go to a nearby store and purchase an apple for you". Though this response is a reasonable completion for the prompt, it is not necessarily actionable to an embodied agent, which may have a narrow and fixed set of abilities. Therefore, to adapt language models to our problem statement, we must somehow inform them that we specifically want the high-level instruction to be broken down into sequences of available low-level skills. One approach is careful prompt engineering, a technique to coax a language model to a specific response structure. Prompt engineering provides examples in the context text ("prompt") for the model that specify the task and the response structure which the model will emulate; the prompt used in this work is shown in Appendix D.3 along with experiments ablating it.

<!-- chunk {"id": "body-0020", "role": "body", "section": "SayCan: Do As I Can, Not As I Say", "weight": 1.0} -->

However, this is not enough to fully constrain the output to admissible primitive skills for an embodied agent, and indeed at times it can produce inadmissible actions or language that is not formatted in a way that is easy to parse into individual steps.

<!-- chunk {"id": "body-0021", "role": "body", "section": "SayCan: Do As I Can, Not As I Say", "weight": 1.0} -->

Scoring language models open an avenue to constrained responses by outputting the probabilities assigned by a language model to fixed outputs. A language model represents a *distribution* over potential completions $p{(\left. w_{k} \middle| w_{< k} \right.)}$, where $w_{k}$ is a word that appears at a $k^{\text{th}}$ position in a text. While typical generation applications (e.g., conversational agents) sample from this distribution or decode the maximum likelihood completion, we can also use the model to *score* a candidate completion selected from a set of options. Formally in SayCan, given a set of low-level skills $\Pi$, their language descriptions $\ell_{\Pi}$ and an instruction $i$, we compute the probability of a language description of a skill $\ell_{\pi} \in \ell_{\Pi}$ making progress towards executing the instruction $i$: $p{(\left.

<!-- chunk {"id": "body-0022", "role": "body", "section": "SayCan: Do As I Can, Not As I Say", "weight": 1.0} -->

\ell_{\pi} \middle| i \right.)}$, which corresponds to querying the model over potential completions. The optimal skill according to the language model is computed via $\ell_{\pi} = {{{\arg\max}_{\ell_{\pi} \in \ell_{\Pi}}p}{(\left. \ell_{\pi} \middle| i \right.)}}$. Once selected, the process proceeds by iteratively selecting a skill and appending it to the instruction. Practically, in this work we structure the planning as a dialog between a user and a robot, in which a user provides the high level-instruction (e.g., "How would you bring me a coke can?") and the language model responds with an explicit sequence ("$\text{I would: 1.~}\ell_{\pi}$", e.g., "I would: 1. find a coke can, 2. pick up the coke can, 3. bring it to you").

<!-- chunk {"id": "body-0023", "role": "body", "section": "SayCan: Do As I Can, Not As I Say", "weight": 1.0} -->

This has the added benefit of interpretability, as the model not only outputs generative responses, but also gives a notion of likelihood across many possible responses. Figure 3 (and Appendix Figure 12 in more detail) shows this process of forcing the LLM into a language pattern, where the set of tasks are the skills the low-level policy is capable of and prompt engineering shows plan examples and dialog between the user and the robot. With this approach, we are able to effectively extract knowledge from the language model, but it leaves a major issue: while the decoding of the instruction obtained in this way always consists of skills that are available to the robot, these skills may not necessarily be appropriate for executing the desired high-level task in the *specific* situation that the robot is currently. For example, if I ask a robot to "bring me an apple", the optimal set of skills changes if there is no apple in view or if it already has one in its hand.

<!-- chunk {"id": "body-0024", "role": "body", "section": "SayCan: Do As I Can, Not As I Say", "weight": 1.0} -->

SayCan. The key idea of SayCan is to ground large language models through value functions -- affordance functions that capture the log likelihood that a particular skill will be able to succeed in the current state. Given a skill $\pi \in \Pi$, its language description $\ell_{\pi}$ and its corresponding value function, which provides $p{(\left. c_{\pi} \middle| {s,\ell_{\pi}} \right.)}$, the probability of $c$-ompletion for the skill described by $\ell_{\pi}$ in state $s$, we form an affordance space ${\{{p{(\left. c_{\pi} \middle| {s,\ell_{\pi}} \right.)}}\}}_{\pi \in \Pi}$. This value function space captures affordances across all skills (see Figure 2).

<!-- chunk {"id": "body-0025", "role": "body", "section": "SayCan: Do As I Can, Not As I Say", "weight": 1.0} -->

For each skill, the affordance function and the LLM probability are then multiplied together and ultimately the most probable skill is selected, i.e. $\pi = {{{\arg\max}_{\pi \in \Pi}p}{(\left. c_{\pi} \middle| {s,\ell_{\pi}} \right.)}p{(\left. \ell_{\pi} \middle| i \right.)}}$. Once the skill is selected, the corresponding policy is executed by the agent and the LLM query is amended to include $\ell_{\pi}$ and the process is run again until a termination token (e.g., "done") is chosen. This process is shown in Figure 3 and described in Algorithm 1. These two mirrored processes together lead to a probabilistic interpretation of SayCan, where the LLM provides probabilities of a skill being useful for the high-level instruction and the affordances provide probabilities of successfully executing each skill.

<!-- chunk {"id": "body-0026", "role": "body", "section": "SayCan: Do As I Can, Not As I Say", "weight": 1.0} -->

Combining these two probabilities together provides a probability that this skill furthers the execution of the high-level instruction commanded by the user.

<!-- chunk {"id": "body-0027", "role": "body", "section": "SayCan: Do As I Can, Not As I Say", "weight": 1.0} -->

1:A high level instruction i, state s0, and a set of skills Π and their language descriptions ℓΠ
6: pπLLM = p (ℓπ|i,ℓπn − 1,…,ℓπ0) ⊳ Evaluate scoring of LLM
7: pπaffordance = p (cπ|sn,ℓπ) ⊳ Evaluate affordance function
8: pπcombined = pπaffordance pπLLM
12: Execute πn (sn) in the environment, updating state sn + 1

<!-- chunk {"id": "body-0028", "role": "body", "section": "SayCan: Do As I Can, Not As I Say", "weight": 1.0} -->

[\capbeside\thisfloatsetupcapbesideposition=right,top,capbesidewidth=0.3]figure[\FBwidth]
Figure 3: Given a high-level instruction, SayCan combines probabilities from a LLM (the probability that a skill is useful for the instruction) with the probabilities from a value function (the probability of successfully executing said skill) to select the skill to perform. This emits a skill that is both possible and useful. The process is repeated by appending the skill to the response and querying the models again, until the output step is to terminate. Appendix Figures 12 and 2 focus on the LLM and VFS components.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Implementing SayCan in a Robotic System", "weight": 1.0} -->

Language-Conditioned Robotic Control Policies. To instantiate SayCan, we must provide it with a set of skills, each of which has a policy, a value function, and a short language description (e.g., "pick up the can"). These skills, value functions, and descriptions can be obtained in a variety of different ways. In our implementation, we train the individual skills either with image-based behavioral cloning, following the BC-Z method, or reinforcement learning, following MT-Opt. Regardless of how the skill's policy is obtained, we utilize value functions trained via TD backups as the affordance model for that skill. While we find that the BC policies achieve higher success rates at the current stage of our data collection process, the value functions provided by the RL policies are crucial as an abstraction to translate control capabilities to a semantic understanding of the scene. In order to amortize the cost of training many skills, we utilize multi-task BC and multi-task RL, respectively, where instead of training a separate policy and value function per skill, we train multi-task policies and models that are *conditioned* on the language description.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Implementing SayCan in a Robotic System", "weight": 1.0} -->

Note, however, that this description only corresponds to *low level* skills -- it is still the role of the LLM in SayCan to interpret the high-level instruction and break it up into individual low level skill descriptions.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Implementing SayCan in a Robotic System", "weight": 1.0} -->

To condition the policies on language, we utilize a pre-trained large sentence encoder language model. We freeze the language model parameters during training and use the embeddings generated by passing in text descriptions of each skill. These text embeddings are used as the input to the policy and value function that specify which skill should be performed (see the details of the architectures used in the Appendix C.1). Since the language model used to generate the text embeddings is not necessarily the same as the language model used for planning, SayCan is able to utilize different language models well suited for different abstraction levels -- understanding planning with respect to many skills as opposed to expressing specific skills more granularly.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Implementing SayCan in a Robotic System", "weight": 1.0} -->

Training the Low-Level Skills. We utilize both BC and RL policy training procedures to obtain the language-conditioned policies and value functions, respectively. To complete the description of the underlying MDP that we consider, we provide the reward function as well as the skill specification that is used by the policies and value functions. As mentioned previously, for skill specification we use a set of short, natural language descriptions that are represented as language model embeddings. We utilize sparse reward functions with reward values of $1.0$ at the end of an episode if the language command was executed successfully, and $0.0$ otherwise. The success of language command execution is rated by humans where the raters are given a video of the robot performing the skill, together with the given instruction. If two out of the three raters agree that the skill was accomplished successfully, the episode is labelled with a positive reward.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Implementing SayCan in a Robotic System", "weight": 1.0} -->

To learn language-conditioned BC policies at scale in the real world, we build on top of BC-Z and use a similar policy-network architecture (shown in Fig. 10). To learn a language-conditioned RL policy, we use MT-Opt in the Everyday Robots simulator using RetinaGAN sim-to-real transfer. We bootstrap the performance of simulation policies by utilizing simulation demonstrations to provide initial successes, and then continuously improve the RL performance with online data collection. We use a network architecture similar to MT-Opt (shown in Fig. 9). The action space of our policies includes the six degrees of freedom of the end-effector pose as well as gripper open and close commands, x-y position and yaw orientation delta of the mobile base of the robot, and the *terminate* action. Additional details on data collection and training are in Appendix Section C.2.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Implementing SayCan in a Robotic System", "weight": 1.0} -->

Robotic System and Skills. For the control policies, we study a diverse set of manipulation and navigation skills using a mobile manipulator robot. Inspired by common skills one might pose to a robot in a kitchen environment, we propose 551 skills that span seven skill families and 17 objects, which include picking, placing and rearranging objects, opening and closing drawers, navigating to various locations, and placing objects in a specific configurations. In this study we utilize the skills that are most amenable to more complex behaviors via composition and planning as well as those that have high performance at the current stage of data collection; for more details, see Appendix D.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

Experimental Setup. We evaluate SayCan with a mobile manipulator and a set of object manipulation and navigation skills in two office kitchen environments. Figure 4 shows the environment setup and the robot. We use 15 objects commonly found in an office kitchen and 5 known locations with semantic meaning (two counters, a table, a trash can, and the user location). We test our method in two environments: a real office kitchen and a mock environment mirroring the kitchen, which is also the environment in which the robot's skills were trained. The robot used is a mobile manipulator from Everyday Robots ^22^2 with a 7 degree-of-freedom arm and a two-fingered gripper. The LLM used is 540B PaLM unless stated otherwise for LLM ablations. We refer to SayCan with PaLM as PaLM-SayCan.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

Instructions. To evaluate PaLM-SayCan, we test across 101 instructions from 7 instruction families, summarized in Table 1 and enumerated in Appendix E.1. These were developed to test various aspects of SayCan and were inspired by crowd sourcing via Amazon Mechanical Turk and in-person kitchen users, as well as benchmarks such as ALFRED and BEHAVIOR. The instructions span multiple axes of variation: time-horizon (from single primitives to 10+ in a row), language complexity (from structured language to fully crowd-sourced requests), and embodiment (variations over the robot and environment state). Table 1 details examples for each family.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

NL queries for a single primitive
Let go of the coke can

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

NL queries focused on abstract verbs
Restock the rice chips on the far counter

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

Structured language queries, mirror NL Verbs
Move the rice chips to the far counter.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

Queries to test SayCan’s understanding of the current state of the environment and robot
Put the coke on the counter. (starting from different completion stages)

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

Queries in unstructured formats
My favorite drink is redbull, bring one

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

Long-horizon queries that require many steps of reasoning
I spilled my coke on the table, throw it away and bring me something to clean

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

Metrics. To understand the performance of the proposed method we measure two main metrics. The first is plan success rate, which measures whether the skills selected by the model are correct for the instruction, regardless of whether or not they actually successfully executed. We ask 3 human raters to indicate whether the plan generated by the model can achieve the instruction, and if 2 out of 3 raters agree that the plan is valid, it is marked a success. Note that for many instructions there may be multiple valid solutions. For example if the instruction is to "bring a sponge and throw away the soda can", the plan can choose to bring sponge first or throw away the soda can first.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

The second metric is execution success rate, which measures whether the full PaLM-SayCan system actually performs the desired instruction successfully. We ask 3 human raters to watch the robot execution. The raters are asked to answer the question "whether the robot achieves the task specified by the task string?" We mark an execution successful if 2 out of 3 raters agree that it is successful.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Results", "weight": 1.0} -->

Table 2 shows the performance of PaLM-SayCan across 101 tasks. In the mock kitchen, PaLM-SayCan achieved a planning success rate of 84% and an execution rate of 74%. We also investigate PaLM-SayCan out of the lab setting and in the real kitchen to verify the performance of the policies and value functions in this setting. We find a reduction of planning performance by 3% and execution by 14%, indicating PaLM-SayCan and the underlying policies generalize reasonably well to the full kitchen. The full task list and results can be found in the Appendix Table 6, and videos of experiment rollouts and the decision making process can be found on the project website: [say-can.github.io](say-can.github.io).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Results", "weight": 1.0} -->

(a) “I just worked out, can you bring me a drink and a snack to recover?”

<!-- chunk {"id": "body-0047", "role": "body", "section": "Results", "weight": 1.0} -->

(b) “I left out a coke, apple, and water, can you throw them away and then bring me a sponge to wipe the table?”

<!-- chunk {"id": "body-0048", "role": "body", "section": "Results", "weight": 1.0} -->

When comparing the performance of different instruction families in Table 2 (see Table 1 for an explanation of families), we see that the natural language nouns performed worse than natural language verbs, due to the number of nouns possible (15 objects and 5 locations) versus number of verbs. The structured language tasks (created to ablate the performance loss of spelling out the solution versus understanding the query) were planned correctly 93% of the time, while their natural language verb counterparts were planned correctly 100%. This indicates the language model effectively parses the queries. The embodiment tasks were planned correctly 64% of the time, generally with failures as a result of affordance function misclassification. PaLM-SayCan planned and executed crowd-sourced natural queries with performance on par with other instruction families. PaLM-SayCan performed worst on the most challenging long-horizon tasks, where most failures were a result of early termination by the LLM (e.g., bringing one object but not the second).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Results", "weight": 1.0} -->

We also find that PaLM-SayCan struggles with negation (e.g., "bring me a snack that isn't an apple") and ambiguous references (e.g. asking for drinks with caffeine), which is a known issue inherited from underlying language models. Overall, 65% of the errors were LLM failures and 35% were affordance failures.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Results", "weight": 1.0} -->

Returning to our initial example, "I spilled something, can you help?", an ungrounded language model would respond with statements like "I can call you a cleaner" or "I can vacuum that up for you", which given our robot are unreasonable. We have shown that PaLM-SayCan responds "I would: 1. find a sponge, 2. pick up the sponge, 3. bring it to you, 4. done" and is able execute this sequence on the robot in a real kitchen. This requires long-horizon reasoning over a required order, an abstract understanding of the instruction, and knowledge of both the environment and robot's capabilities.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Results", "weight": 1.0} -->

Ablating Language. To study the importance of the LLM, we conduct two ablation experiments using the language-conditioned policy (see Sections 4-4). In *BC NL* we feed the full instruction $i$ into the policy -- this approach is representative of standard RL or BC-based instruction following methods. In *BC USE* we project the high-level instruction into the set of known language commands via the Universal Sentence Encoder (USE) embeddings by embedding the instruction, all the tasks, and the combinatorial set of sequences tasks (i.e., we consider "pick coke can" as well as "1. find coke can, 2. pick coke can" and so on), and selecting the highest cosine similarity instruction. The results in Table 2 illustrate the necessity of the language grounding where *BC NL* achieves 0% in all tasks and *BC USE* achieves 60% for single primitives, but 0% otherwise.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Results", "weight": 1.0} -->

Ablating Value Functions. Table 2 illustrates the necessity of the affordance grounding. We compare PaLM-SayCan to *No VF*, which removes the value function grounding (i.e., choosing the maximum language score skill) and to *Generative*, which uses the generative output of the LLM and then projects each planned skill to its maximal cosine similarity skill via USE embeddings. The latter in effect compares to, which loses the explicit option probabilities, and thus is less interpretable and cannot be combined with affordance probabilities. For *Generative* we also tried BERT embeddings, but found poor performance. The *No VF* and *Generative* approaches performed similarly, achieving 67% and 74% planning success rate respectively, and worse than PaLM-SayCan's 84%.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Results", "weight": 1.0} -->

Ablating the Language Model. SayCan is able to improve with improved language models. The LLM used herein was PaLM, a 540B parameter model. In this section we ablate over 8B, 62B, and 540B parameter models as well as the 137B parameter FLAN model which is finetuned on a "instruction answering" dataset. Appendix Table 7 shows each model on a set of generative problems, where we find that generally larger models perform better, though the difference between the 62B and 540B model is small. Results in other works, such as Chain of Thought Prompting, indicate this difference may be more pronounced on more challenging problems -- this is shown in Section 5.2. We also find that PaLM outperforms FLAN. Though FLAN was fine-tuned on instruction answering, the broader and improved dataset for PaLM may make up for this difference in training.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Results", "weight": 1.0} -->

While it is expected that the generative performance of the language model will improve with better language models, it is unclear how the LLM size influences the final robotics success rate. Table 3 shows PaLM 540B and FLAN on robot running the full SayCan algorithm. The results show that the system using PaLM with affordance grounding (PaLM-SayCan) chooses the correct sequence of skills 84% of the time and executes them successfully 74% of the time, reducing errors by half compared to FLAN. This is particularly exciting because it represents the first time we can see how an improvement in language models translates to a similar improvement in robotics. This result indicates a potential future where the fields of language processing and robotics can collaboratively improve each other and scale together.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Case Studies of New Capabilities of PaLM-SayCan", "weight": 1.0} -->

PaLM-SayCan enables new capabilities. First, we show that it is very easy to incorporate new skills into the system, and use drawer manipulation as an example. Second, we show by leveraging chain of thought reasoning, we are able to solve complex tasks that require reasoning. Finally we show the system can work with multilingual queries, without explicitly being designed to.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Case Studies of New Capabilities of PaLM-SayCan", "weight": 1.0} -->

Adding Skills: Drawer Manipulation (Appendix E.3). SayCan is capable of integrating new skills by simply adding the new skills as options for the LLM and providing accompanying value functions and add an example in the prompt with that skill. For example, with the skills open, close, and go to the drawer, SayCan is capable of solving tasks such as "restock the coke and pepsi into the drawer". Over 21 queries we found a planning rate of 100% and an execution rate of 33% (due to failures of the chained manipulation policy), with no loss in performance for other instructions.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Case Studies of New Capabilities of PaLM-SayCan", "weight": 1.0} -->

Chain-of-thought planning rollout with PaLM-SayCan.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Case Studies of New Capabilities of PaLM-SayCan", "weight": 1.0} -->

Human: Can you bring a fruit-flavored drink without caffeine?

<!-- chunk {"id": "body-0059", "role": "body", "section": "Case Studies of New Capabilities of PaLM-SayCan", "weight": 1.0} -->

Explanation: The user has asked for a drink that is fruit-flavored and does not have caffeine, I will bring the lime soda.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Case Studies of New Capabilities of PaLM-SayCan", "weight": 1.0} -->

Robot: 1. find a lime soda, 2. pick up the lime soda, 3. bring it to you, 4. put down the lime soda, 5. done

<!-- chunk {"id": "body-0061", "role": "body", "section": "Case Studies of New Capabilities of PaLM-SayCan", "weight": 1.0} -->

Human: Bring me the spicy chips.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Case Studies of New Capabilities of PaLM-SayCan", "weight": 1.0} -->

Explanation: The user has asked for chips that are spicy, I will bring the Jalapeno chips.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Case Studies of New Capabilities of PaLM-SayCan", "weight": 1.0} -->

Robot: 1. find the jalapeno chips, 2. pick up the jalapeno chips, 3. bring it to you, 4. put down the jalapeno chips, 5.done

<!-- chunk {"id": "body-0064", "role": "body", "section": "Case Studies of New Capabilities of PaLM-SayCan", "weight": 1.0} -->

Human: The snack is too small, bring me something more filling.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Case Studies of New Capabilities of PaLM-SayCan", "weight": 1.0} -->

Explanation: The user has asked for a snack that is more filling, I will bring the multigrain chips.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Case Studies of New Capabilities of PaLM-SayCan", "weight": 1.0} -->

Robot: 1. find the multigrain chips, 2. pick up the multigrain chips, 3. bring it to you, 4. put down the multigrain chips, 5. done

<!-- chunk {"id": "body-0067", "role": "body", "section": "Case Studies of New Capabilities of PaLM-SayCan", "weight": 1.0} -->

Chain of Thought Reasoning. SayCan can be integrated with recent work improving LLM reasoning, such as Chain of Thought. One limitation of vanilla SayCan is that it doesn't handle tasks that involves negation. This is inherited from underline language models, and studied in the NLP community. However, we found by using chain-of-thought prompting we can improve SayCan on this front.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Case Studies of New Capabilities of PaLM-SayCan", "weight": 1.0} -->

For chain-of-thought prompting-based SayCan, we need to modify the prompt to include a part called "Explanation". We also slightly change how we use the language model. Instead of directly using the scoring interface to rank possible options, we first use the generative decoding of LLM to create an explanation, and then use the scoring mode, by including the explanation into the prompt. The full prompt is shown in Appendix E.4 Listing 3.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Case Studies of New Capabilities of PaLM-SayCan", "weight": 1.0} -->

A few successful rollouts of the model at evaluation time is shown in Table 4. As we can see, with chain of thought prompting, the model can handle negations and tasks that require reasoning.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Case Studies of New Capabilities of PaLM-SayCan", "weight": 1.0} -->

Multilingual Queries (Appendix E.5). While not explicitly designed to work with multilingual queries, PaLM-SayCan is able to handle them. The LLM was trained on multilingual corpora and thus SayCan can handle multilingual queries other than English. The results of SayCan on multilingual queries are summarized in Table. 9, and there is almost no performance drop in planning success rate when changing the queries from English to Chinese, French and Spanish.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Case Studies of New Capabilities of PaLM-SayCan", "weight": 1.0} -->

Closed-Loop Planning. As presented herein, SayCan only receives environmental feedback through value functions at the current decision step, meaning if a skill fails or the environment changes, the necessary feedback may not be available. Owing to the extendibility and the natural language interface, Huang et al. builds upon SayCan to enable closed-loop planning by leveraging environment feedback (from e.g., success detectors, scene descriptors, or even human feedback) through an inner monologue.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Open Source Environment", "weight": 1.0} -->

We have open-sourced an implementation of SayCan in a Google Colab notebook at [say-can.github.io/#open-source](say-can.github.io/#open-source). The environment is shown in Figure 8 and is a tabletop with a UR5 robot and randomly generated sets of colored blocks and bowls. The low-level policy is implemented with CLIPort, which is trained to output a pick and place location. Due to the lack of a value function for this policy, the affordances are implemented with a ViLD object detector. GPT-3 is used as the open source language model. Steps are output in the form "pick up the object and place it in location", leveraging the ability of LLMs to output code structures.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Open Source Environment", "weight": 1.0} -->

Task: move all the blocks into their matching colored bowls.
Step 1. pick up the blue block and place it in the blue bowl
Step 2. pick up the green block and place it in the green bowl
Step 3. pick up the yellow block and place it in the yellow bowl

<!-- chunk {"id": "body-0074", "role": "body", "section": "Conclusions, Limitations and Future Work", "weight": 1.0} -->

We presented SayCan, a method that enables leveraging and grounding the rich knowledge in large language models to complete embodied tasks. For real-world grounding, we leverage pre-trained skills, which are then used to condition the model to choose natural language actions that are both feasible and contextually appropriate. More specifically, we use reinforcement learning as a way to learn value functions for the individual skills that provide affordances of what is possible in the world, and then use textual labels for these skills as potential responses that are scored by a language model. This combination results in a symbiotic relationship where the skills and their value functions can act as the language model's "hands and eyes," while the language model supplies high-level semantic knowledge about how to complete a task. We evaluated the proposed approach on a number of real-world robotic tasks that involve a mobile manipulator robot accomplishing a large set of long-horizon natural language instructions in a real kitchen. We also demonstrated an exciting property of our method where a robot's performance can be improved simply by enhancing the underlying language model.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Conclusions, Limitations and Future Work", "weight": 1.0} -->

While SayCan presents a viable way to ground language models in agents' affordances, it has a number of limitations. First, we expect this method to inherit the limitations and biases of LLMs, including the dependence on the training data. Secondly, we observe that even though SayCan allows the users to interact with the agents using natural language commands, the primary bottleneck of the system is in the range and capabilities of the underlying skills. To illustrate this, we present representative failure cases in Appendix E. Future work that extends the repertoire of skills and improves their robustness would mitigate this limitation. In addition, at the current stage, the system is not easily able to react to situations where individual skills fail despite reporting a high value, though this could potentially be addressed by appropriate prompting of the language model for a correction.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Conclusions, Limitations and Future Work", "weight": 1.0} -->

There are many other potential avenues for future work. A natural question that this work raises is how the information gained through grounding the LLM via real-world robotic experience can be leveraged to improve the language model itself, both in terms of its factuality and its ability to perform common-sense reasoning about real-world environments and physics. Furthermore, since our method uses generic value functions to score affordances, it is intriguing to consider what other sources of grounding could be incorporated in the same manner, such as non-robotic contexts.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Conclusions, Limitations and Future Work", "weight": 1.0} -->

In the future, it is also interesting to examine whether natural language is the right ontology to use to program robots: natural language naturally incorporates contextual and semantic cues from the environment, and provides a level of abstraction which enables robots do decide on how to execute a strategy based on its own perception and affordances. At the same time, as opposed to, e.g., hindsight goal images, it requires supervision and it might not be the most descriptive medium for certain tasks.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Conclusions, Limitations and Future Work", "weight": 1.0} -->

Lastly, SayCan presents a particular way of connecting and factorizing the challenges of language understanding and robotics, and many further extensions can be proposed. Ideas such as combining robot planning and language, using language models as a pre-training mechanism for policies and many other ways of combining language and interaction are exciting avenues for future research.
