<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Π0.5: A Vision-Language-Action Model with Open-World Generalization

Topics include Robotics, Vision-language models, Object detection, Generalization, Control, Learning, Vision-language-action model.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In order for robots to be useful, they must perform practically relevant tasks in the real world, outside of the lab. While vision-language-action (VLA) models have demonstrated impressive results for end-to-end robot control, it remains an open question how far such models can generalize in the wild. We describe pi_0.5, a new model based on pi_0 that uses co-training on heterogeneous tasks to enable broad generalization. pi_0.5\ uses data from multiple robots, high-level semantic prediction, web data, and other sources to enable broadly generalizable real-world robotic manipulation. Our system uses a combination of co-training and hybrid multi-modal examples that combine image observations, language commands, object detections, semantic subtask prediction, and low-level actions. Our experiments show that this kind of knowledge transfer is essential for effective generalization, and we demonstrate for the first time that an end-to-end learning-enabled robotic system can perform long-horizon and dexterous manipulation skills, such as cleaning a kitchen or bedroom, in entirely new homes.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

> Stuff your eyes with wonder... See the world. It's more fantastic than any dream made or paid for in factories. > Ray Bradbury, Fahrenheit 451 Open-world generalization represents one of the biggest open problems in physical intelligence: embodied systems such as robotic arms, humanoids, and autonomous vehicles only truly become useful when they can leave the lab and handle the diverse situations and unexpected events that occur in the real world. Learning-based systems offer a path to enabling broad generalization, particularly with recent advances that have enabled scalable learning systems in domains ranging from natural language processing to computer vision. However, the diversity of situations that a robot might encounter in the real world requires more than just scale: we need to design training recipes that can provide the breadth of knowledge that will allow robots to generalize at many levels of abstraction.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

For example, if a mobile robot is asked to clean up a kitchen that it has never seen before, some behaviors generalize readily if they are well represented in the data with a sufficient range of scenes and objects (e.g., picking up a knife or plate), others might require adapting or modifying existing skills to use them in a new way or in a new sequence, and yet others might require understanding the semantics of the scene based on prior knowledge (e.g., which drawer to open, or which object on the counter is most likely to be a drying rack). How can we structure a training recipe for a robotic learning system that can enable this kind of flexible generalization?

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A person can draw on a lifetime of experience to synthesize appropriate solutions to each of these challenges. Not all of this experience is firsthand, and not all of it comes from rote practice -- for example, we might use facts that we were told by others or read in a book, together with bits of insight from other tasks we have performed in different contexts, combined with direct experience in the target domain. Analogously, we might hypothesize that generalizable robotic learning systems must be able to transfer experience and knowledge from a variety of information sources. Some of these sources are firsthand experience with direct relevance to the task at hand, some require transfer from other robot embodiments, environments, or domains, and some represent entirely different data types, such as verbal instructions, perceptual tasks based on web data, or prediction of high-level semantic commands.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The heterogeneity of these different sources of data present a major obstacle, but fortunately recent advances in vision-language-action (VLA) models provide us with a toolkit that can make this possible: by casting different modalities into the same sequence modeling framework, VLAs can be adapted to train on robot data, language data, computer vision tasks, and combinations of the above.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we leverage this observation to design a co-training framework for VLAs that can utilize heterogeneous and diverse knowledge sources to enable broad generalization. Building on the $\pi_{0}$ VLA, we propose to include a range of different data sources to create the $\pi_{0.5}$ model ("pi oh five"), which can control mobile manipulators to perform a variety of household tasks even in homes that were never seen during training. $\pi_{0.5}$ draws on experience from many sources: in addition to a medium-sized dataset collected directly with mobile manipulators in a variety of real homes (about 400 hours), $\pi_{0.5}$ uses data from other non-mobile robots, data of related tasks collected under laboratory conditions, training examples that require predicting "high-level" semantic tasks based on robot observation, verbal language instructions provided to the robot by human supervisors, and a variety of multi-modal examples created from web data, such as image captioning, question answering, and object localization (see Figure LABEL:fig:teaser).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The overwhelming majority of training examples provided to $\pi_{0.5}$ (97.6% during the first training phase) do not come from mobile manipulators performing household tasks, but from these other sources, such as other robots or data from the web. Nonetheless, $\pi_{0.5}$ is able to control mobile manipulators in entirely new homes not seen during training, perform intricate tasks such as hanging up towels or making beds, and can carry out long-horizon manipulation skills 10 to 15 minutes in length, cleaning an entire kitchen or bedroom based on only a high-level prompt.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The design of $\pi_{0.5}$ follows a simple hierarchical architecture: we first pre-train the model on the heterogeneous mixture of training tasks, and then fine-tune it specifically for mobile manipulation with both low-level action examples and high-level "semantic" actions, which correspond to predicting subtask labels such as "pick up the cutting board" or "rearrange the pillow." At runtime, during each step of inference, the model first predicts the semantic subtask, inferring the behavior that is appropriate to perform next based on the task structure and the semantics of the scene, and then predicts the low-level robot action chunk based on this subtask.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

This simple architecture provides both the ability to reason about long-horizon multi-stage tasks and the ability to leverage different sources of knowledge for the two levels: the low-level action inference procedure readily benefits from action data collected by other robots, including simpler static robots in other environments, while the high-level inference procedure benefits from semantic examples from the web, high-level annotation prediction, and even verbal commands that can be provided to the robot by human "supervisors" that walk the robot through complex tasks step by step, instructing it (much like how they might instruct a person) on the appropriate subtasks to perform to complete a complex task such as cleaning a room. We illustrate this design in Figure LABEL:fig:teaser.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our central contribution is a system for training a highly generalizable VLA, $\pi_{0.5}$, together with a proof of concept that generalization can emerge from this model when it is trained on appropriately diverse data. We provide a detailed empirical evaluation of both $\pi_{0.5}$'s generalization capabilities and the relevance of different co-training ingredients. To our knowledge, our work is the first to demonstrate an end-to-end learning-enabled robotic system that can perform long-horizon and dexterous manipulation skills, such as cleaning a kitchen or bedroom, in entirely new homes. Our experiments and comparisons further show that this is enabled by transferring knowledge from other robots, high-level semantic prediction, verbal language instruction from human supervisors, web data, and other sources.

<!-- chunk {"id": "body-0012", "role": "body", "section": "The $\\pi_{0.5}$ Model and Training Recipe", "weight": 1.0} -->

We provide an overview of the $\pi_{0.5}$ model and training recipe in Figure 3. The model weights are initialized from a standard VLM trained on data from the web, and training then proceeds in two stages: a pre-training stage intended to adapt the model to diverse robotic tasks, and a post-training stage intended to specialize it to mobile manipulation and equip it with the mechanisms for efficient test-time inference. During pre-training, all tasks, including tasks with robot actions, are represented with discrete tokens, which leads to simple, scalable, and efficient training. During post-training, we adapt the model to also have an action expert, as with $\pi_{0}$, in order to both represent actions with finer granularity and enable more compute-efficient inference for real-time control. At inference-time, the model first produces a high-level subtask for the robot to perform and then, conditioned on this subtask, predicts the low-level actions via the action expert. We describe the model architecture below, followed by a description of each of the phases and their corresponding training tasks.

<!-- chunk {"id": "body-0013", "role": "body", "section": "IV-A The $\\pi_{0.5}$ architecture", "weight": 1.0} -->

The $\pi_{0.5}$ architecture can flexibly represent both action chunk distributions and tokenized text outputs, with the latter used both for co-training tasks (e.g., question-answering) and for outputting high-level subtask predictions during hierarchical inference. The distribution captured by the model can be written as $\pi_{\theta}{(\mathbf{a}_{t:{t + H}},\left.

<!-- chunk {"id": "body-0014", "role": "body", "section": "IV-A The $\\pi_{0.5}$ architecture", "weight": 1.0} -->

\hat{\ell} \middle| {\mathbf{o}_{t},\ell} \right.)}$, where $\mathbf{o}_{t} = {\lbrack\mathbf{I}_{t}^{1},\ldots,\mathbf{I}_{t}^{n},\mathbf{q}_{t}\rbrack}$ consists of the images from all of the cameras and the robot's configuration (joint angles, gripper pose, torso lift pose, and base velocity), $\ell$ is the overall task prompt (e.g., "put away the dishes"), $\hat{\ell}$ represents the model's (tokenized) textual output, which could be either a predicted high-level subtask (e.g., "pick up the plate") or the answer to a vision-language prompt in web data, and $\mathbf{a}_{t:{t + H}}$ is a predicted action chunk.

<!-- chunk {"id": "body-0015", "role": "body", "section": "IV-A The $\\pi_{0.5}$ architecture", "weight": 1.0} -->

We decompose the distribution as where the action distribution does not depend on $\ell$, only on $\hat{\ell}$. Thus, high-level inference captures $\pi_{\theta}{(\left. \hat{\ell} \middle| {\mathbf{o}_{t},\ell} \right.)}$, and low-level inference captures $\pi_{\theta}{(\left. \mathbf{a}_{t:{t + H}} \middle| {\mathbf{o}_{t},\hat{\ell}} \right.)}$, with both distributions represented by the same model.

<!-- chunk {"id": "body-0016", "role": "body", "section": "IV-A The $\\pi_{0.5}$ architecture", "weight": 1.0} -->

The model corresponds to a transformer that takes in $N$ multimodal input tokens $x_{1:N}$ (we use the term token loosely here, referring to both discretized and continuous inputs) and produces a sequence of multimodal outputs $y_{1:N}$, which we can write as $y_{1:N} = {f\left( x_{1:N},{A{(x_{1:N})}},{\rho{(x_{1:N})}} \right)}$. Each $x_{i}$ can be a text token ($x_{i}^{w} \in {\mathbb{N}}$), an image patch ($x_{i}^{I} \in {\mathbb{R}}^{p \times p \times 3}$), or an intermediate denoising value of a robot action in flow matching ($x_{i}^{a} \in {\mathbb{R}}^{d}$).

<!-- chunk {"id": "body-0017", "role": "body", "section": "IV-A The $\\pi_{0.5}$ architecture", "weight": 1.0} -->

The observations $\mathbf{o}_{t}$ and $\ell$ form the prefix part of $x_{1:N}$. Depending on the token type, as indicated by $\rho{(x_{i})}$, each token can be processed not only by a different encoder, but also by different expert weights within the transformer. For example, image patches are fed through a vision encoder, and text tokens are embedded with an embedding matrix. Following $\pi_{0}$, we linearly project action tokens $x_{i}^{a}$ into the transformer embedding space and use separate expert weights in the transformer to process the action tokens. The attention matrix ${A{(x_{1:N})}} \in {\lbrack 0,1\rbrack}^{N \times N}$ indicates if a token can attend to another token. Compared to standard causal attention in LLMs, image patch, textual prompt, and continuous action tokens use bidirectional attention.

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-A The $\\pi_{0.5}$ architecture", "weight": 1.0} -->

As we want our model to output both text (to answer questions about the scene or to output next tasks to accomplish) and actions (to act in the world), the output of $f$ is split into text token logits and action output tokens, respectively $\left( y_{1:M}^{\ell},y_{1:H}^{a} \right)$. The first $M$ correspond to text token logits that can be used to sample $\hat{\ell}$ and the later $H$ tokens are produced by a separate action expert, as in $\pi_{0}$, and projected via a linear mapping to continuous outputs used to obtain $\mathbf{a}_{t:{t + H}}$ (see next section). Note that ${M + H} \leq N$, i.e., not all outputs are associated with a loss. The robot proprioceptive state is discretized and input to the model as text tokens. More details about the architecture are in Appendix A-E.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-B Combining discrete & continuous action representations", "weight": 1.0} -->

Similarly to $\pi_{0}$, we use flow-matching to predict continuous actions in the final model. Given $\mathbf{a}_{t:{t + H}}^{\tau,\omega} = {{\tau\mathbf{a}_{t:{t + H}}} + {{({1 - \tau})}\omega}}$, $\omega \sim {\mathcal{N}{(0,\mathbf{I})}}$, where $\tau \in {\lbrack 0,1\rbrack}$ is the flow matching time index, the model is trained to predict the flow vector field $\omega - \mathbf{a}_{t}$. However, as shown, VLA training can be much faster when actions are represented by discrete tokens, particularly when using a tokenization scheme that is efficient for compressing the action chunks (e.g., FAST). Unfortunately, such discrete representations are less well-suited for real-time inference, because they require expensive autoregressive decoding for inference.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-B Combining discrete & continuous action representations", "weight": 1.0} -->

Therefore, an ideal model design would train on discretized actions but still allow for use of flow matching to produce continuous actions at inference time.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B Combining discrete & continuous action representations", "weight": 1.0} -->

Our model is therefore trained to predict actions *both* through autoregressive sampling of tokens (using the FAST tokenizer) and iterative integration of the flow field, combining the best of both worlds. We use the attention matrix to ensure that the different action representations do not attend to each other. Our model is optimized to minimize the combined loss where $H{(x_{1:M},y_{1:M}^{\ell})}$ is the cross entropy loss between the text tokens and predicted logits (including the FAST encoded action tokens), $y_{1:H}^{a} = {f_{\theta}^{a}{(\mathbf{a}_{t:{t + H}}^{\tau,\omega},\mathbf{o}_{t},\ell)}}$ is the output from the (smaller) action expert, and $\alpha \in {\mathbb{R}}$ is a trade-off parameter.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-B Combining discrete & continuous action representations", "weight": 1.0} -->

This scheme enables us to first pre-train our model as a standard VLM transformer model by mapping actions to text tokens ($\alpha = 0$), and then add additional action expert weights predicting continuous action tokens in a non-autoregressive fashion for fast inference in a post-training stage. We find that following this procedure, which is further explained below, leads to stable pre-training and excellent language following abilities of the VLA model. At inference time we then use standard autoregressive decoding for text tokens $\hat{\ell}$ followed by $10$ denoising steps, conditioned on text tokens, to produce actions $\mathbf{a}_{t:{t + H}}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-C Pre-training", "weight": 1.0} -->

In the first training stage, $\pi_{0.5}$ is trained with a broad range of robot and non-robot data, which we summarize below and illustrate in Figure 4. It is trained as a standard auto-regressive transformer, performing next-token prediction of text, object locations, and FAST encoded action tokens.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-C Pre-training", "weight": 1.0} -->

Diverse *M*obile *M*anipulator data (MM). We use about 400 hours of data of mobile manipulators performing household tasks in about 100 different home environments, some of which are shown in Figure 7, using the robots in Section IV-E. This slice of the training set is the most directly relevant to our evaluation tasks, which consist of similar cleaning and tidying tasks in new, unseen, home environments.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-C Pre-training", "weight": 1.0} -->

Diverse *M*ulti-*E*nvironment non-mobile robot data (ME). We also collected non-mobile robot data, either with a single arm or two arms, in a variety of home environments. These arms were fixed to surfaces or mounting platforms, and because they are significantly lighter and easier to transport, we were able to gather a more diverse dataset in a wider range of homes with them. However, this ME data comes from a different embodiment than the mobile robots.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-C Pre-training", "weight": 1.0} -->

*C*ross-*E*mbodiment laboratory data (CE). We collected data for a wide range of tasks (e.g., bussing a table, folding shirts) in the laboratory, with simpler tabletop environments and a variety of robot types. Some of these tasks are highly relevant to our evaluation (e.g., putting dishes in a bin), while others are not (e.g., grinding coffee beans). This data includes single-arm and dual-arm manipulators, and both static and mobile bases. We also include the open-source OXE dataset. This dataset is an extended version of the dataset used by $\pi_{0}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-C Pre-training", "weight": 1.0} -->

*H*igh-*L*evel subtask prediction (HL). Breaking down high-level task commands such as "clean the bedroom" into shorter subtasks like "adjust the blanket" and "pick up pillow", similar to chain-of-thought prompting for language models, can help a trained policy reason about the current scene and better determine the next action. For robot data in MM, ME, and CE where the task involves multiple subtasks, we manually annotate all data with semantic descriptions of the subtasks and train $\pi_{0.5}$ to jointly predict the subtask labels (as text) as well as the actions (conditioned on the subtask label) based on the current observation and high-level command. This naturally leads to a model that can act both as a high-level policy (outputting subtasks) and low-level policy that executes actions for these subtasks. We also label relevant bounding boxes shown in the current observation and train $\pi_{0.5}$ to predict them before predicting the subtask.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-C Pre-training", "weight": 1.0} -->

Multi-modal *W*eb *D*ata (WD). Finally we include a diverse set of web data involving image captioning (CapsFusion, COCO ), question answering (Cambrian-7M, PixMo, VQAv2 ), and object localization in pre-training. For object localization, we further extend the standard datasets with additional web data of indoor scenes and household objects with bounding box annotations.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-C Pre-training", "weight": 1.0} -->

For all action data, we train the model to predict target joint and end-effector poses. To differentiate the two, we add '$<$control_mode$>$ joint/end effector $<$control_mode$>$' to the text prompt. All action data is normalized to $\lbrack{- 1},1\rbrack$ using the 1% and 99% quantile of each action dimension of the individual dataset. We set the dimensionality of the action $\mathbf{a}$ to a fixed number to accommodate the largest action space among all the datasets. For robots with lower-dimensional configuration and action spaces, we zero-pad the action vectors.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-D Post-training", "weight": 1.0} -->

After pre-training the model with discrete tokens for 280k gradient steps, we perform a second stage of training that we refer to as post-training. The purpose of this stage is to both specialize the model to our use-case (mobile manipulation in homes), and to add an action expert that can produce continuous action chunks via flow matching. This stage jointly trains with next-token prediction, to preserve text prediction capabilities, and flow matching for the action expert (which is initialized with random weights at the beginning of post-training). We optimize the objective in Equation, with $\alpha = 10.0$ for 80k additional steps. The post-training action dataset consists of the MM and ME robot data, filtered down to successful episodes that are below a fixed length threshold. We include web data (WD) to preserve the model's semantic and visual capabilities, and the slice of HL data corresponding to the multi-environment datasets.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-D Post-training", "weight": 1.0} -->

Additionally, to improve the model's ability to predict appropriate high-level subtasks, we collect *verbal instruction* demonstrations (VI), which are constructed by expert users providing "language demonstrations," selecting appropriate sub-task commands to command the robot to perform mobile manipulation tasks step by step. These examples are collected by "teleoperating" the robot in real time with language to perform tasks with the learned low level policy, essentially providing demonstrations of good high-level subtask outputs for a trained policy.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-E Robot system details", "weight": 1.0} -->

The robot systems used in our mobile manipulation experiments are illustrated in Figure 5. We conducted all of our experiments using two types of mobile manipulators. Both platforms are equipped with two 6 DoF arms with parallel jaw grippers and wrist-mounted monocular RGB cameras, a wheeled holonomic base, and a torso lift mechanism. The state and action spaces for the base correspond to linear (2D) and angular (1D) velocity, and the torso lift mechanism is either 1D (up/down) or 2D (up/down and forward/backward). In addition to the two wrist cameras, the robots have a forward and backward facing camera mounted between the arms. We use all four cameras for high-level inference, and the wrist and forward cameras for the low-level inference process. The total dimensionality of the state and action spaces is 18 or 19, depending on the platform.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-E Robot system details", "weight": 1.0} -->

The control system is very simple: the $\pi_{0.5}$ model directly commands target poses for the arms, gripper, and torso lift, and the target base velocities at 50 Hz (with action chunking). These targets are tracked with simple PD controllers, without any additional trajectory planning or collision detection. All manipulation and navigation control is fully end-to-end.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

The $\pi_{0.5}$ model is designed to generalize broadly to new environments. While it is common to evaluate VLAs in environments that match the training data, we conduct all of our experiments in novel environments that were not seen in training. For quantitative comparisons, we use a set of mock home environments to provide a controlled and reproducible setup, while the most realistic final evaluation is conducted in three real homes that were not part of the training set (see Figure 6). Our experiments focus on the following questions: Can $\pi_{0.5}$ effectively generalize to complex multi-stage tasks in entirely new homes?

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

How does the generalization of $\pi_{0.5}$ scale with the number of distinct environments in the training data?

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

How do the individual co-training ingredients in the $\pi_{0.5}$ training mixture contribute to its final performance?

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

How important is the high-level inference component of $\pi_{0.5}$, and how does it compare to flat, low-level inference as well as oracle high-level baselines?

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-A Can $\\pi_{0.5}$ generalize to real homes?", "weight": 1.0} -->

(a) Example rollouts. We visualize an exemplary π0.5 episode for one task from each home. Top to bottom: putting items in a drawer in Home 1, followed by putting dishes in the sink in Home 2, and putting clothes in the laundry basket in Home 3. The human instruction for each is given on the left, and the high-level subtask prediction from π0.5 is shown beneath each frame in blue.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-A Can $\\pi_{0.5}$ generalize to real homes?", "weight": 1.0} -->

(b) Quantitative evaluation. We show the task progress per task and environment averaged over 10 trials. We find that π0.5’s performance in the mock evaluation setups is representative of its performance in real homes.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-A Can $\\pi_{0.5}$ generalize to real homes?", "weight": 1.0} -->

To answer Question, we evaluated $\pi_{0.5}$ in three real homes that were not present in the training set, using both types of robots. In each of the homes, the robots were instructed to perform a bedroom and kitchen cleaning task. The evaluation rubrics for each task are provided in Appendix A-B and roughly correspond to the percentage of steps in each task that were completed successfully (e.g., placing half the dishes in the sink corresponds to around 50%). The results in Figure 7 show that $\pi_{0.5}$ was able to consistently succeed on a variety of tasks in each home (we note that, additionally, the model is capable of performing many more tasks than used in our quantitative evaluation). Many of the tasks involve multiple stages (e.g., moving multiple objects) lasting about 2 to 5 minutes. For these trials, the model is provided with a simple high-level command (e.g., "place the dishes in the sink"), and the high-level inference process autonomously determines appropriate steps (e.g., "pick up the cup").

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-A Can $\\pi_{0.5}$ generalize to real homes?", "weight": 1.0} -->

This level of in-the-wild generalization goes significantly beyond the results demonstrated with prior vision-language-action models, both in terms of the degree of novelty that the model must handle, and the task duration and complexity.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-B How does generalization scale with the number of scenes?", "weight": 1.0} -->

In the next set of experiments, we aim to measure how generalization scales with the number of environments seen in the training data. We vary the number of environments in the mobile manipulation data and measure its impact on generalization by training with data from 3, 12, 22, 53, 82, and 104 locations. Since applying the entire pre-training and post-training recipe to each of these datasets is prohibitively compute-intensive, for these experiments we pre-train on the mixture of robot action prediction data *without* mobile manipulation data, and then compare models post-trained on datasets that comprise mobile manipulation data from varying numbers of environments. While the datasets split by location in principle differ in size, in practice the number of training steps (40k) is chosen such that each model sees the same number of unique data samples, which allows us to control for dataset size when varying the number of locations used within a post-training experiment.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-B How does generalization scale with the number of scenes?", "weight": 1.0} -->

Each model is evaluated in the mock environments shown in Figure 6, which are not seen in training. We conduct two types of evaluations. First, to evaluate overall performance on multi-stage tasks, we use the standard rubric in Appendix A-B and the mock test homes to evaluate each model's end-to-end performance on putting dishes in the sink, packing items into a drawer, putting away laundry, and making a bed. Second, we conduct a more fine-grained evaluation of each model's ability to follow language instructions and interact with novel objects, where the robot must pick up specific objects from a kitchen counter based on language commands. These experiments use both in-distribution objects from similar categories as those in the training data (but new instances), as well as out-of-distribution objects from unseen categories. The latter necessitates broad semantic generalization.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-B How does generalization scale with the number of scenes?", "weight": 1.0} -->

The results of the first experiment are shown in Figure 8. The average performance among the tasks generally improves with more training locations. To quantify how much the final model (with 104 locations) bridges the generalization gap, we include a control (shown in green) that is trained directly on data from the test homes. This control attains similar performance as the final 104-location model, suggesting that our co-training recipe effectively enables broad generalization, reaching similar performance to a model trained on the test environment. To confirm that this generalization performance requires our full co-training recipe, we additionally include two baselines that *do not* use any of the other co-training tasks in the pre-training phase, but instead train directly on either data from the test environment (light green) or mobile manipulation data from the 104 training locations (light yellow). The performance for both those baselines is significantly worse --- this indicates that the other data sources leveraged by our full training recipe are essential for good generalization, even when the policy has seen robot data from test homes.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-B How does generalization scale with the number of scenes?", "weight": 1.0} -->

When not using data from test homes, pre-training with our recipe is especially important, as can be seen by the large gap between the green bars and light yellow bar in Figure 8.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-B How does generalization scale with the number of scenes?", "weight": 1.0} -->

The results of the second experiment (language following) are shown in Figure 9. We report the language following rate, which measures how often the robot selects the object indicated in the language command, and success rate, which measures how often the robot successfully places that object in the correct location (either inside the drawer or inside the sink, depending on the test scenario). We separately measure performance on object categories seen in training (but new object instances) and unseen ("out-of-distribution") object categories. Details of this experiment are shown and discussed in Appendix A-C. Figure 9 shows that, as the number of locations in the training data increases, both language following performance and success rate improve. As expected, the performance on in-distribution objects improves more quickly than that of out-of-distribution objects. As each new environment introduces new household items, the model becomes generally more robust and starts to generalize to task categories that were not present in the training data.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-C How important is each part of our co-training recipe?", "weight": 1.0} -->

To study Question, we compare our full $\pi_{0.5}$ model to other training mixtures to study the importance of each mixture component, again using end-to-end task performance in the mock homes and the language following evaluation described in Section V-B. As a reminder, our full recipe uses data from mobile manipulators in many environments (MM), static manipulators in many environments (ME), and diverse cross-embodiment data collected in laboratory settings (CE). It also includes high-level data where the prediction corresponds to a high-level language command (HL), and web data corresponding to captioning, VQA, and object localization tasks (WD). Post-training also uses verbal instruction data (VI), which we analyze in Section V-E. In these experiments, we ablate different parts of the mixture: no WD: this ablation excludes web data. no ME: this ablation excludes multi-environment non-mobile data. no CE: this ablation excludes the laboratory cross-embodiment data.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-C How important is each part of our co-training recipe?", "weight": 1.0} -->

no ME or CE: this ablation excludes both data sources from other robots, such that the model is trained on only data from the target mobile manipulator platform as well as web data.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-C How important is each part of our co-training recipe?", "weight": 1.0} -->

The results on the full mock home tasks are shown in Figure 10 (detailed breakdown of performance on each task in Appendix A-D). First, we see in the results that excluding *either* of the two cross-embodiment data sources (ME and CE) significantly degrades performance, indicating that $\pi_{0.5}$ benefits considerably from cross-embodiment transfer, from both other environments (ME) and other tasks (CE). Excluding both sources harms performance even more. Interestingly, the difference in performance with the no WD ablation is not statistically significant in this experiment, though we show later that web data has a large impact on language following (below) and high-level subtask inference (Section V-E).

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-C How important is each part of our co-training recipe?", "weight": 1.0} -->

The results of the language following experiment, shown in Figure 11, show a similar trend as Figure 10 --- excluding ME or/and CE data leads to a significant degradation in performance. What differs now is that removing web data (no WD) causes significantly worse performance on out-of-distribution (OOD) objects --- we conjecture that training with web data, which contains very broad knowledge of physical objects, allows the model to understand and follow language commands involving *unseen* object categories.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-D How does $\\pi_{0.5}$ compare to other VLAs?", "weight": 1.0} -->

We compare $\pi_{0.5}$ to the original $\pi_{0}$ VLA as well as an improved version of $\pi_{0}$ which we denote as $\pi_{0}$-FAST+Flow. This version is trained via the joint diffusion and FAST action prediction formulation from Equation, but on action data only, without the HL or WD datasets. These models provide a strong point of comparison, since $\pi_{0}$ has been demonstrated to perform strongly on complex and dexterous mobile manipulation tasks, and the enhancement in $\pi_{0}$-FAST+Flow brings it as close to $\pi_{0.5}$ as possible. $\pi_{0.5}$ builds on these models with a combination of co-training tasks. For a fair comparison, all models receive the same cross-embodiment robot training set and are trained for a comparable number of steps.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-D How does $\\pi_{0.5}$ compare to other VLAs?", "weight": 1.0} -->

The differences then are: $\pi_{0.5}$ additionally uses HL and WD data; $\pi_{0.5}$ uses a hybrid training procedure, with discrete tokenized training in the pre-training phase, and training with a flow matching action expert *only* in the post-training phase, while $\pi_{0}$ always uses the action expert. $\pi_{0}$-FAST+Flow follows the hybrid training recipe but is trained only with data containing robot actions and thus cannot perform high-level inference. The results in Figure 12 show that $\pi_{0.5}$ significantly outperforms both $\pi_{0}$ and our enhanced version. This result holds even when we allow for longer training up to 300k training steps of $\pi_{0}$, confirming that as in Pertsch et al. training with FAST tokens is more effective in terms of compute than pure diffusion based training.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-E How important is high-level inference?", "weight": 1.0} -->

Finally, we evaluate the importance of high-level inference, and compare the performance of several alternative high-level inference methods. The high-level inference mechanism in $\pi_{0.5}$ takes in a high-level command (e.g., "clean the bedroom") and outputs the subtask to complete (e.g., "pick up pillow"), which is then used as context for inferring the lower-level actions, analogously to chain of thought inference. While $\pi_{0.5}$ uses a unified architecture where the *same* model performs both high-level and low-level inference, we can also construct baseline methods that either forego the high-level inference process and feed the task prompt directly into the low-level system, as is common in standard VLA models, or use another model for high-level inference to ablate the importance of different dataset components in terms of their impact on the high-level policy.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-E How important is high-level inference?", "weight": 1.0} -->

We consider the following methods and ablations, all of which use the full $\pi_{0.5}$ low-level inference process with different high-level policies: $\pi_{0.5}$ model for high-level and low-level inference. no WD: an ablation of $\pi_{0.5}$ that excludes web data. no VI: an ablation of $\pi_{0.5}$ that excludes the verbal instruction (VI) data. implicit HL: no high-level inference at runtime but includes high-level data in training, which may teach the model about subtasks implicitly. no HL: no high-level inference, and no high-level data in training at all.

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-E How important is high-level inference?", "weight": 1.0} -->

GPT-4: use GPT-4 as the high-level policy, evaluating the importance of training the high-level policy on robot data. To align the model with our domain, we prompt GPT-4 with a description of the task and a list of the most used labels to choose. human HL: use an expert human as an "oracle" high-level policy, to provide an upper bound on performance.

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-E How important is high-level inference?", "weight": 1.0} -->

The results of these experiments are shown in Figure 13. The full $\pi_{0.5}$ model performs the best, and outperforms even the human HL "oracle" baseline. Perhaps surprisingly, the second best model is the implicit HL ablation, which does *not* perform any high-level inference, but includes the full data mixture, i.e. also subtask prediction, in training. This strongly suggests the importance of the co-training recipe used by our model: while there is a benefit to explicitly infer high-level subtasks, a significant portion of that benefit is already obtained simply by including subtask *prediction* data in the training mixture. The no HL ablation, excluding HL task even in training, performs significantly worse. The results also show that the relatively small verbal instruction dataset, which only constitutes about 11% of the high-level mobile manipulation examples, is critical to strong performance as the no VI ablation is significantly weaker. The no WD ablation is also significantly worse, indicating that much of the benefit of web data (perhaps unsurprisingly) lies in improving the high-level policy.

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-E How important is high-level inference?", "weight": 1.0} -->

Finally, the zero-shot GPT-4 ablation attains the worst performance, indicating the importance of adapting VLMs with robot data. We provide a detailed breakdown of performance on each task in Appendix A-D, Figure 17.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

We described $\pi_{0.5}$, a co-trained model that builds on the $\pi_{0}$ VLA to integrate a variety of data sources and enable generalization to new environments. The $\pi_{0.5}$ VLA can control mobile manipulators to perform tasks in homes that were never seen in the training data, cleaning kitchens and bedrooms, making beds, hanging towels, and performing other multi-stage and dexterous behaviors. $\pi_{0.5}$ is trained on about 400 hours of mobile manipulation data, but includes a much larger amount of data from other robots, including non-mobile manipulators in diverse environments and data collected under laboratory conditions. It is also co-trained jointly with data from the web, as well as high-level prediction data for outputting language commands based on robot observations. The generalization capabilities of $\pi_{0.5}$ demonstrate that this co-training recipe facilitates effective transfer, enabling highly generalizable control of a mobile manipulator with only a medium-sized mobile manipulation dataset. $\pi_{0.5}$ is not without its limitations.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

While our VLA exhibits broad generalization, it still makes mistakes. Some environments present persistent challenges (e.g., unfamiliar handles on drawers, or cabinets that are physically hard for the robot to open), some behaviors present challenges with partial observability (e.g., the robot arm occluding a spill that should be wiped), and in some cases the high-level sub-task inference is easily distracted (e.g., closing and opening a drawer multiple times while putting away items). Addressing these challenges with better co-training, transfer, and larger datasets is a promising direction for future work. Other future work directions could address the technical constraints of our method. While $\pi_{0.5}$ can perform a variety of behaviors to clean up kitchens and bedrooms, it processes relatively simple prompts. The complexity of the prompts that the model can accommodate is determined by the training data, and more complex preferences and instructions could be incorporated by producing more intricate and diverse annotations, either with human labelers or synthetically.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

The model also uses a relatively modest context, and incorporating richer context and memory could make the model significantly more capable in settings with more partial observability, such as tasks that require navigating between different rooms or remembering where objects are stored. More broadly, $\pi_{0.5}$ explores a particular combination of heterogeneous data sources, but the specific sources of data can be explored even more broadly. For instance, the ability of our system to learn from verbal instructions provides a powerful new supervision modality, and future work could explore this and other ways that people can provide robots with additional contextual knowledge. We hope that our work will serve as a foundation for a new generation of VLAs that exhibit broad generalization to diverse real-world environments.
