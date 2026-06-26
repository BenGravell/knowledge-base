<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Π0: A Vision-Language-Action Flow Model for General Robot Control

Topics include Robotics, Robustness, Language models, Foundation models, Vision-language models, Datasets, Generalization, Control, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Robot learning holds tremendous promise to unlock the full potential of flexible, general, and dexterous robot systems, as well as to address some of the deepest questions in artificial intelligence. However, bringing robot learning to the level of generality required for effective real-world systems faces major obstacles in terms of data, generalization, and robustness. In this paper, we discuss how generalist robot policies (i.e., robot foundation models) can address these challenges, and how we can design effective generalist robot policies for complex and highly dexterous tasks. We propose a novel flow matching architecture built on top of a pre-trained vision-language model (VLM) to inherit Internet-scale semantic knowledge. We then discuss how this model can be trained on a large and diverse dataset from multiple dexterous robot platforms, including single-arm robots, dual-arm robots, and mobile manipulators. We evaluate our model in terms of its ability to perform tasks in zero shot after pre-training, follow language instructions from people and from a high-level VLM policy, and its ability to acquire new skills via fine-tuning. Our results cover a wide variety of tasks, such as laundry folding, table cleaning, and assembling boxes.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

> A human being should be able to change a diaper, plan an invasion, butcher a hog, conn a ship, design a building, write a sonnet, balance accounts, build a wall, set a bone, comfort the dying, take orders, give orders, cooperate, act alone, solve equations, analyze a new problem, pitch manure, program a computer, cook a tasty meal, fight efficiently, die gallantly. Specialization is for insects. > Robert A. Heinlein, Time Enough for Love Artificial intelligence systems come in all shapes and sizes, from highly specialized systems that solve complex problems inaccessible to the human mind, such as predicting the conformation of a protein, to systems that can produce lifelike high-resolution images or videos based on textual prompts. However, the axis along which human intelligence most outpaces machine intelligence is *versatility*: the ability to solve diverse tasks situated in varied physical environments, while responding intelligently to environmental constraints, language commands, and unexpected perturbations.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Perhaps the most tangible progress toward this kind of versatility in AI can be seen in large language- and vision-language models: systems that are pre-trained on large and very diverse corpora of images and text from the web, and then fine-tuned ("aligned") using more carefully curated datasets meant to induce the desired pattern of behavior and responsiveness. While such models have been shown to exhibit broad instruction-following and problem-solving abilities, they are not truly *situated* in a physical world the way that people are, and their understanding of physical interaction is based entirely on abstract descriptions. If such methods are to make tangible progress toward AI systems that exhibit the kind of physically situated versatility that people possess, we will need to train them on physically situated data --- that is, data from embodied robot agents.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Flexible and general-purpose models that can be tasked to perform a variety of robot behaviors have tremendous practical ramifications, but they may also offer solutions to some of the toughest challenges facing robot learning today, such as availability of data, generalization, and robustness. In natural language and computer vision, general-purpose foundation models that are pre-trained on diverse multi-task data tend to outperform narrowly tailored and specialized solutions. For example, if the goal is to recognize birds in photographs, it is likely more expedient to pre-train on many different image-language associations and then fine-tune or prompt for the bird recognition task, than it is to train on only bird recognition data. Similarly, we may find that for effective specialized robot systems, it is more effective to first pre-train on highly diverse robot data, and then fine-tune or prompt for the desired task.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This can resolve the data scarcity challenge, because many more sources of data are available to a generalist model --- including data from other tasks, other robots, or even non-robot sources --- and it may resolve robustness and generalization challenges, because the diverse data exhibits a greater coverage of observations and actions, providing a variety of scenes, corrections, and recovery behaviors that might not be present in more narrow specialized data. Thus, adopting a large-scale pre-training approach to robot learning has the potential to address many of the field's challenges and make practical learning-enabled robots a reality, while at the same time furthering our understanding of the deepest problems in artificial intelligence.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, developing such generalist robot policies --- i.e., robot foundation models --- involves a number of major challenges. First, any such research must be done at a very large scale, because the full benefits of large-scale pre-training are often not present at smaller scales. Second, it requires developing the right model architectures that can effectively make use of diverse data sources, while at the same time being able to represent the intricate and subtle behaviors necessary to interact with complex physical scenes. Third, it requires the right training *recipe*. This is perhaps the most important ingredient, as much of the recent progress with large models in NLP and computer vision has relied heavily on delicate strategies for curating pre-training and post-training data.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we present a prototype model and learning framework, which we call $\pi_{0}$, that illustrates how each of these three bottlenecks could be tackled. We illustrate our model and system in Figure LABEL:fig:teaser. To incorporate diverse data sources, we begin by utilizing a pre-trained vision-language model (VLM) to import Internet-scale experience. By basing our model on a VLM, we inherit the general knowledge, semantic reasoning, and problem-solving abilities of language- and vision-language models. We then further train our model to incorporate robot actions, turning it into a vision-language-action (VLA) model. In order to make it feasible to utilize a variety of diverse robot data sources, we employ *cross-embodiment training*, where data from many robot types is combined into the same model. These different robot types have different configuration spaces and action representations, including single and dual-arm systems, as well as mobile manipulators. Additionally, in order to make it possible to perform highly dexterous and intricate physical tasks, we use an action chunking architecture with flow matching (a variant of diffusion) to represent complex continuous action distributions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

This enables our model to control robots at frequencies of up to 50 Hz for dexterous tasks such as laundry folding (see Figure LABEL:fig:teaser). To combine flow matching with VLMs, we use a novel *action expert* that augments the standard VLM with flow-based outputs.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

As with language models, the architecture of our model is only part of our method. In order to flexibly and robustly perform complex tasks, we need the right training recipe. Our recipe mirrors the pre-training/post-training separation commonly seen in exascale language- and image-language models, where the model is first pre-trained on a very large and diverse corpus, and then fine-tuned on more narrow and more carefully curated data to induce the desired pattern of behavior --- in our case, dexterity, efficiency, and robustness. Intuitively, training only on high-quality data does not teach the model how to recover from mistakes, since mistakes are rarely seen in such data. Training on only lower-quality pre-training data does not teach the model to act efficiently and robustly. Combining both provides the desired behavior: the model attempts insofar as possible to act in a manner similar to the high-quality data, but still has a repertoire of recoveries and corrections that it can deploy in the case of a mistake.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The contributions of our work consist of a novel generalist robot policy architecture based on VLM pre-training and flow matching, and an empirical investigation of pre-training/post-training recipes for such robot foundation models. We evaluate our model out of the box with language commands, with fine-tuning to downstream tasks, and in combination with a high-level semantic policy that outputs intermediate language commands to perform complex and temporally extended tasks. While our model and system make use of a variety of ideas presented in recent work, the combination of ingredients is novel, and the empirical evaluation demonstrates a level of dexterity and generality that goes significantly beyond previously demonstrated robot foundation models. We evaluate our approach by pre-training on over 10,000 hours of robot data, and fine-tuning to a variety of dexterous tasks, including laundry folding (see Figure 2), clearing a table, putting dishes in a microwave, stacking eggs into a carton, assembling a box, and bagging groceries.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Overview", "weight": 1.0} -->

We provide an outline of our model and training procedure in Figure 3. In our training framework, we first assemble a pre-training mixture consisting of a weighted combination of our own dexterous manipulation datasets (Section V-C), collected on 7 different robot configurations for 68 different tasks, and the entire OXE dataset, which contains data from 22 robots. The pre-training phase (Section V-A) also uses diverse language labels, combining *task names* and *segment annotations* (fine-grained labels for sub-trajectories, typically about 2 seconds in length). The purpose of the pre-training phase is to train a *base model* that exhibits broad capabilities and generalization, but is not necessarily specialized for high performance on any one task. This base model can follow language commands and perform a variety of tasks at rudimentary proficiency. For complex and dexterous tasks, we then employ a post-training procedure (Section V-A), which uses high-quality curated data to adapt the model to specific downstream tasks.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Overview", "weight": 1.0} -->

We study both efficient post-training with small to moderate amounts of data, and high-quality post-training with larger datasets for complex tasks such as laundry folding and mobile manipulation.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Overview", "weight": 1.0} -->

Our model, which we describe in Section IV, is based on the PaliGemma vision-language model, which we then further train with our data mixture. To turn the base PaliGemma VLM into $\pi_{0}$, we add action outputs that use flow matching to generate continuous action distributions. We describe this design in detail in the following section. Note that we use PaliGemma for convenience and because of its comparatively small size (which is useful for real-time control), but our framework is compatible with any base pre-trained VLM.

<!-- chunk {"id": "body-0015", "role": "body", "section": "The $\\pi_{0}$ Model", "weight": 1.0} -->

The $\pi_{0}$ model, illustrated in Figure 3, consists primarily of a language model transformer backbone. Following the standard late fusion VLM recipe, image encoders embed the robot's image observations into the same embedding space as language tokens. We further augment this backbone with robotics-specific inputs and outputs --- namely, proprioceptive state and robot actions. $\pi_{0}$ uses conditional flow matching to model the continuous distribution of actions. Flow matching provides our model with high precision and multimodal modeling capability, making it especially well suited to high-frequency dexterous tasks. Our architecture is inspired by Transfusion, which trains a single transformer using multiple objectives, with tokens^11^1In this paper, we use the word "token" to refer to an input/output slot along the sequence dimension, whether the slot corresponds to a discrete variable (e.g., a language token) or a continuous variable (e.g., an image patch or a robot action). corresponding to continuous outputs supervised via a flow matching loss and tokens corresponding to discrete outputs supervised via a cross-entropy loss.

<!-- chunk {"id": "body-0016", "role": "body", "section": "The $\\pi_{0}$ Model", "weight": 1.0} -->

Building on Transfusion, we additionally found that using a separate set of weights for the robotics-specific (action and state) tokens led to an improvement in performance. This design is analogous to a mixture of experts with two mixture elements, where the first element is used for image and text inputs, and the second is used for robotics-specific inputs and outputs. We refer to the second set of weights as the *action expert*.

<!-- chunk {"id": "body-0017", "role": "body", "section": "The $\\pi_{0}$ Model", "weight": 1.0} -->

Formally, we want to model the data distribution $p(\mathbf{A}_{t}|\mathbf{o}_{t})$, where $\mathbf{A}_{t}=[\mathbf{a}_{t},\mathbf{a}_{t+1},...,\mathbf{a}_{t+H-1}]$ corresponds to an *action chunk* of future actions (we use $H=50$ for our tasks), and $\mathbf{o}_{t}$ is an observation.

<!-- chunk {"id": "body-0018", "role": "body", "section": "The $\\pi_{0}$ Model", "weight": 1.0} -->

The observation consists of multiple RGB images, a language command, and the robot's proprioceptive state, such that $\mathbf{o}_{t}=[\mathbf{I}^{1}_{t},...,\mathbf{I}^{n}_{t},\ell_{t},\mathbf{q}_{t}]$, where $\mathbf{I}^{i}_{t}$ is $i^{\text{th}}$ image (with 2 or 3 images per robot), $\ell_{t}$ is a sequence of language tokens, and $\mathbf{q}_{t}$ is a vector of joint angles. The images $\mathbf{I}^{i}_{t}$ and state $\mathbf{q}_{t}$ are encoded via corresponding encoders and then projected via a linear projection layer into the same embedding space as the language tokens.

<!-- chunk {"id": "body-0019", "role": "body", "section": "The $\\pi_{0}$ Model", "weight": 1.0} -->

For each action $\mathbf{a}_{t^{\prime}}$ in the action chunk $\mathbf{A}_{t}$, we have a corresponding *action token* that we feed through the action expert. During training, we supervise these action tokens using a conditional flow matching loss, where subscripts denote robot timesteps and superscripts denote flow matching timesteps, with $\tau\in$. Recent work in high-resolution image and video synthesis has shown that flow matching can achieve strong empirical performance when combined with a simple linear-Gaussian (or optimal transport) probability path, given by $q(\mathbf{A}_{t}^{\tau}|\mathbf{A}_{t})=\mathcal{N}(\tau\mathbf{A}_{t},(1-\tau)\mathbf{I})$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "The $\\pi_{0}$ Model", "weight": 1.0} -->

In practice, the network is trained by sampling random noise $\epsilon\sim\mathcal{N}(\mathbf{0},\mathbf{I})$, computing the "noisy actions" $\mathbf{A}_{t}^{\tau}=\tau\mathbf{A}_{t}+(1-\tau)\epsilon$, and then training the network outputs $\mathbf{v}_{\theta}(\mathbf{A}_{t}^{\tau},\mathbf{o}_{t})$ to match the denoising vector field $\mathbf{u}(\mathbf{A}_{t}^{\tau}|\mathbf{A}_{t})=\mathbf{A}_{t}-\epsilon$. The action expert uses a full bidirectional attention mask, so that all action tokens attend to each other. During training, we sample the flow matching timestep $\tau$ from a beta distribution that emphasizes lower (noisier) timesteps.

<!-- chunk {"id": "body-0021", "role": "body", "section": "The $\\pi_{0}$ Model", "weight": 1.0} -->

See Appendix A-B for more details.

<!-- chunk {"id": "body-0022", "role": "body", "section": "The $\\pi_{0}$ Model", "weight": 1.0} -->

At inference time, we generate actions by integrating the learned vector field from $\tau=0$ to $\tau=1$, starting with random noise $\mathbf{A}_{t}^{0}\sim\mathcal{N}(\mathbf{0},\mathbf{I})$. We use the forward Euler integration rule: where $\delta$ is the integration step size. We use 10 integration steps (corresponding to $\delta=0.1$) in our experiments. Note that inference can be implemented efficiently by caching the attention keys and values for the prefix $\mathbf{o}_{t}$ and only recomputing the suffix corresponding to the action tokens for each integration step. We provide more details regarding the inference procedure, including the inference time for each part of the model, in Appendix A-D.

<!-- chunk {"id": "body-0023", "role": "body", "section": "The $\\pi_{0}$ Model", "weight": 1.0} -->

While in principle our model can be initialized from scratch or fine-tuned from any VLM backbone, in practice we use PaliGemma as our base model. PaliGemma is an open-source 3 billion parameter VLM that offers a convenient tradeoff between size and performance. We add 300M parameters for the action expert (which is initialized from scratch) for a total of 3.3 billion parameters. We provide a full description of the model architecture in Appendix A-B.

<!-- chunk {"id": "body-0024", "role": "body", "section": "The $\\pi_{0}$ Model", "weight": 1.0} -->

Non-VLM baseline model. In addition to our main VLA model, we also trained a similar baseline model that did not use a VLM initialization for ablation experiments. This model, which we refer to as $\pi_{0}$-small, has 470M parameters, does not use VLM initialization, and has a number of small differences that we found to be helpful for training on our data without VLM initialization, which are summarized in Appendix A-C. This model is used in our comparisons to evaluate the benefits of incorporating VLM pertaining.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Data Collection and Training Recipe", "weight": 1.0} -->

Broadly capable robot foundation models require not only an expressive and powerful architecture, but also the right dataset and, more importantly, the right training *recipe*. In the same way that LLM training is typically divided into pre-training and post-training phases, we employ a multi-stage training procedure for our model. The goal of the pre-training phase is to expose the model to a diverse range of tasks so that it can acquire broadly applicable and general physical capabilities, while the goal of the post-training phase is to provide the model with the ability to skillfully and fluently execute the desired downstream task. Because of this, the requirements for the pre-training and post-training datasets are distinct: the pre-training dataset should cover as many tasks as possible, and within each of those tasks should cover a diversity of behaviors. The post-training dataset should instead cover behaviors that are conducive to effective task execution, which should exhibit a consistent and fluent strategy.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Data Collection and Training Recipe", "weight": 1.0} -->

Intuitively, the diverse (but lower quality) pre-training data allows the model to recover from mistakes and handle highly varied situations, which might not otherwise occur in the high-quality post-training data, while the post-training data teaches the model to perform the task well.

<!-- chunk {"id": "body-0027", "role": "body", "section": "V-A Pre-training and post-training", "weight": 1.0} -->

We provide an overview of our pre-training mixture in Figure 4. Since each training example corresponds to a timestep --- i.e., a tuple $(\mathbf{o}_{t},\mathbf{A}_{t})$, --- we will quantify data in terms of timesteps in this discussion. $9.1\%$ of the training mixture consists of open-source datasets, including OXE, Bridge v2, and DROID. The robots and tasks in these datasets typically have one or two cameras and use low-frequency control, between 2 and 10 Hz. However, these datasets cover a wide range of objects and environments. To learn dexterous and more complex tasks, we also use 903M timesteps of data from our own datasets, where 106M steps are from single-arm robots and 797M are from dual-arm robots.

<!-- chunk {"id": "body-0028", "role": "body", "section": "V-A Pre-training and post-training", "weight": 1.0} -->

This data has 68 tasks, where each task is composed of complex behaviors --- e.g., the "bussing" task involves putting a wide range of different dishes, cups, and utensils into a bussing bin, and a wide array of trash items into the garbage. Note that this definition of task is significantly different from prior work, which typically uses any combination of noun and verb (e.g., "pick up the cup" vs. "pick up the plate") to constitute a distinct task. Therefore, the actual range of behaviors in our dataset is significantly broader than this number of "tasks" would imply. We discuss the specific robots and tasks in our dataset in more detail in Section V-C.

<!-- chunk {"id": "body-0029", "role": "body", "section": "V-A Pre-training and post-training", "weight": 1.0} -->

Since the datasets are somewhat imbalanced in size (e.g., the more difficult laundry folding tasks are overrepresented), we weight each task-robot combination by $n^{0.43}$, where $n$ is the number of samples for that combination, such that over-represented combinations are down-weighted. The configuration vector $\mathbf{q}_{t}$ and action vectors $\mathbf{a}_{t}$ always have the dimensionality of the largest robot in the dataset (18 in our case, to accommodate two 6-DoF arms, 2 grippers, a mobile base, and a vertically actuated torso). For robots with lower-dimensional configuration and action spaces, we zero-pad the configuration and action vectors. For robots with fewer than three images, we also mask out the missing image slots.

<!-- chunk {"id": "body-0030", "role": "body", "section": "V-A Pre-training and post-training", "weight": 1.0} -->

In the post-training phase, we fine-tune our model with a smaller task-specific dataset to specialize it to particular downstream applications. As mentioned previously, our definition of "task" is fairly broad --- e.g., the "bussing" task requires manipulating a wide range of different objects. Different tasks require very different datasets, with the simplest of the tasks necessitating only 5 hours and the most complex tasks using 100 or more hours of data.

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-B Language and high-level policies", "weight": 1.0} -->

More complex tasks that require semantic reasoning and high-level strategy, such as table bussing, can also benefit from a high-level policy that decomposes high-level tasks (such as "bus the table") into more immediate subtasks (such as "pick up the napkin" or "throw the napkin into the trash"). Since our model is trained to process language inputs, we can use a high-level VLM to make these semantic inferences, a method that is analogous to LLM/VLM planning methods such as SayCan. We use such a high-level policy to assist our model with high-level strategy for several of our experimental tasks, as we will discuss in Section VI.

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-C Robot system details", "weight": 1.0} -->

Our dexterous manipulation datasets include 7 different robot configurations and 68 tasks. We summarize these platforms in Figure 5, and discuss them below: UR5e. An arm with a parallel jaw gripper, with a wrist-mounted and over-the-shoulder camera, for a total of two camera images and a 7-dimensional configuration and action space.

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-C Robot system details", "weight": 1.0} -->

Bimanual UR5e. Two UR5e setups, for a total of three camera images and a 14-dimensional configuration and action space.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-C Robot system details", "weight": 1.0} -->

Franka. The Franka setup has two cameras and an 8-dimensional configuration and action space.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-C Robot system details", "weight": 1.0} -->

Bimanual Trossen. This setup has two 6-DoF Trossen ViperX arms in a configuration based on the ALOHA setup, with two wrist cameras and a base camera, and a 14-dimensional configuration and action space.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-C Robot system details", "weight": 1.0} -->

Bimanual ARX & bimanual AgileX. This setup uses two 6-DoF arms, and supports either ARX or AgileX arms, with three cameras (two wrist and one base) and a 14-dimensional configuration and action space. This class encompasses two distinct platforms, but we categorize them together because of their similar kinematic properties.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-C Robot system details", "weight": 1.0} -->

Mobile Trossen & mobile ARX. This setup is based on the Mobile ALOHA platform, with two 6-DoF arms on a mobile base, which are either ARX arms or Trossen ViperX arms. The nonholonomic base adds two action dimensions, for a 14-dimensional configuration and 16-dimensional action space. There are two wrist cameras and a base camera. This class encompasses two distinct platforms, but we categorize them together because of their similar kinematic properties.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-C Robot system details", "weight": 1.0} -->

Mobile Fibocom. Two 6-DoF ARX arms on a holonomic base. The base adds three action dimensions (two for translation and one for orientation), for a 14-dimensional configuration and 17-dimensional action space.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-C Robot system details", "weight": 1.0} -->

We summarize the proportion of our dataset from each robot in Figure 4.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

Our experimental evaluation consists of out-of-box evaluation experiments that compare our base (pre-trained) model to alternative model designs with direct prompting, as well as detailed fine-tuning experiments that evaluate our model on challenging downstream tasks, comparing it to other methods that have been proposed for dexterous manipulation. We study the following research questions: How well does $\pi_{0}$ perform after *pre-training* on a variety of tasks that are present in the pre-training data? We study this question by directly evaluating $\pi_{0}$, with comparisons to other robot foundation models.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

How well does $\pi_{0}$ follow language commands? These experiments compare $\pi_{0}$ to $\pi_{0}$-small, a smaller version of our model without VLM initialization, to evaluate its performance on following language commands. We evaluate with both human-provided commands and commands specified by a high-level VLM policy, as discussed in Section V-B.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

How does $\pi_{0}$ compare to methods that have been proposed specifically for addressing dexterous manipulation tasks? These experiments study downstream tasks for which we can either fine-tune our model from the pre-trained initialization, or train it from scratch on task-specific data, comparing to prior methods that were proposed for dexterous manipulation. We aim to evaluate both the benefits of our architecture and our pre-training procedure.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

Can $\pi_{0}$ be adapted to complex, multi-stage tasks? In our final set of experiments, we fine-tune $\pi_{0}$ to a set of particularly complex tasks, including folding laundry and bussing a table. These tasks take between 5 and 20 minutes to complete. Some require guidance from a high-level policy.

<!-- chunk {"id": "body-0044", "role": "body", "section": "VI-A Evaluating the base model", "weight": 1.0} -->

In our first set of experiments, we evaluate the model after pre-training on our full mixture, without any post-training, to evaluate how well our base model can perform a variety of tasks. We compare to other robot foundation models in the literature: both VLAs and smaller models that are trained from scratch on the same pre-training mixture. We evaluate on the following tasks, visualized in Figure 6, with each task commanded to the same base model via a language command.

<!-- chunk {"id": "body-0045", "role": "body", "section": "VI-A Evaluating the base model", "weight": 1.0} -->

Shirt folding: the robot must fold a t-shirt, which starts flattened.

<!-- chunk {"id": "body-0046", "role": "body", "section": "VI-A Evaluating the base model", "weight": 1.0} -->

Bussing easy: the robot must clean a table, putting trash in the trash bin and dishes into the dish bin. The score indicates the number of objects that were placed in the correct receptacle.

<!-- chunk {"id": "body-0047", "role": "body", "section": "VI-A Evaluating the base model", "weight": 1.0} -->

Bussing hard: a harder version of the bussing task, with more objects and more challenging configurations, such as utensils intentionally placed on top of trash objects, objects obstructing each other, and some objects that are not in the pre-training dataset.

<!-- chunk {"id": "body-0048", "role": "body", "section": "VI-A Evaluating the base model", "weight": 1.0} -->

Grocery bagging: the robot must bag all grocery items, such as potato chips, marshmallows, and cat food.

<!-- chunk {"id": "body-0049", "role": "body", "section": "VI-A Evaluating the base model", "weight": 1.0} -->

Toast out of toaster: the robot removes toast from a toaster.

<!-- chunk {"id": "body-0050", "role": "body", "section": "VI-A Evaluating the base model", "weight": 1.0} -->

Providing comparisons for these experiments is challenging because very few prior models can operate at this scale. We compare to OpenVLA, a 7B parameter VLA model that was originally trained on the OXE dataset. We train OpenVLA on our full mixture. This is a very difficult mixture for OpenVLA, which does not support action chunking or high-frequency control. We also compare to Octo, a smaller 93M parameter model. While Octo is not a VLA, it does use a diffusion process to generate actions, providing a valuable point of comparison for our flow matching VLA. We also train Octo on the same mixture as our model. Due to time constraints, we were unable to train OpenVLA and Octo for the same number of epochs as our full model. We therefore also compare to a "compute parity" version of our model, which is trained for only 160k steps (as opposed to 700k steps for our main model), which is equal to or lower than the number of steps provided to the baselines (160k for OpenVLA, 320k for Octo).

<!-- chunk {"id": "body-0051", "role": "body", "section": "VI-A Evaluating the base model", "weight": 1.0} -->

We also include a version of the OpenVLA model that we fine-tuned only on the UR5e data, without cross-embodiment training, in the hopes of providing an even stronger baseline on the UR5e tasks. Finally, we include a comparison to the $\pi_{0}$-small model described in Section IV, which can be viewed as a scaled-down version of our model without VLM pre-training.

<!-- chunk {"id": "body-0052", "role": "body", "section": "VI-A Evaluating the base model", "weight": 1.0} -->

The evaluation metric uses a normalized score averaged over 10 episodes per task and method, where an episode receives a score of 1.0 for a full success, and a fractional score for partial success. For example, the score for bussing is the fraction of objects that are correctly placed in the proper receptacle. We describe the scoring rubrics in Appendix A-E. The results, shown in Figure 7, show that $\pi_{0}$ attains by far the best results across the board on all the out-of-box tasks, with near perfect success rates on shirt folding and the easier bussing tasks, and large improvements over all baselines. The "parity" version of $\pi_{0}$, which is trained for only 160k steps, still outperforms all the baselines, and even $\pi_{0}$-small outperforms OpenVLA and Octo. OpenVLA struggles on these tasks because its autoregressive discretization architecture does not support action chunks. The UR5e-only OpenVLA model performs better, but is still far below the performance of $\pi_{0}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "VI-A Evaluating the base model", "weight": 1.0} -->

Octo does support action chunks, but has a comparatively limited representational capacity. This comparison illustrates the importance of combining large, expressive architectures with the ability to model complex distributions via flow matching or diffusion. Additionally, the comparison to $\pi_{0}$-small illustrates the importance of incorporating VLM pre-training. Unfortunately, it is hard to make this last comparison fair: $\pi_{0}$-small uses fewer parameters, but larger models are difficult to use without pre-training. Overall, these experiments show that $\pi_{0}$ provides a powerful pre-trained model with the ability to effectively perform a variety of tasks with a variety of robots, with much better performance than prior models.

<!-- chunk {"id": "body-0054", "role": "body", "section": "VI-B Following language commands", "weight": 1.0} -->

In the next set of experiments, we fine-tune the base $\pi_{0}$ model to follow language commands in a set of evaluation domains. We compare this fine-tuned $\pi_{0}$ model with the $\pi_{0}$-small model described in Section IV, which we found to be the strongest baseline in the previous section. Recall that $\pi_{0}$-small does *not* use a VLM initialization. This experiment therefore aims to measure how much VLM pre-training boosts our model's ability to follow language instructions. Note that $\pi_{0}$-small is also a significantly smaller model --- unfortunately, it is difficult to remove this confounder, because VLM initialization serves both to make it practical to train a much larger model without overfitting, and to improve language instruction following. We nonetheless hope that this experiment sheds light on the language capabilities of $\pi_{0}$. The language instructions for each task consist of objects to pick up and locations to place those objects, with language-labeled segments that are about 2 seconds in length. Each full task consists of numerous such segments.

<!-- chunk {"id": "body-0055", "role": "body", "section": "VI-B Following language commands", "weight": 1.0} -->

The tasks in this evaluation consist of: Bussing: the robot must clean a table, placing dishes and cutlery in a bin, and trash into a trash bin.

<!-- chunk {"id": "body-0056", "role": "body", "section": "VI-B Following language commands", "weight": 1.0} -->

Grocery bagging: the robot must pack grocery items, such as bags of coffee beans, barley, marshmallow, seaweed, almonds, spaghetti, and cans into a bag.

<!-- chunk {"id": "body-0057", "role": "body", "section": "VI-B Following language commands", "weight": 1.0} -->

In Figure 8, we show the language-conditioned tasks in our evaluation and present the evaluation results. We evaluate five different conditions. $\pi_{0}$-flat (and $\pi_{0}$-small-flat) corresponds to directly command the model with the task description (e.g., "bag the groceries"), without intermediate language commands. $\pi_{0}$-human (and $\pi_{0}$-small-human) provides intermediate step commands (e.g., which object to pick and where to place it) from an expert human user. These conditions evaluate each model's ability to follow more detailed language commands: while these intermediate commands provide considerable information for how to perform the task, the model must be able to understand and follow those commands to benefit from them. Finally, $\pi_{0}$-HL evaluates $\pi_{0}$ with high-level commands provided by a high-level VLM, as discussed in Section V-B. This condition is also autonomous, without any human expert.

<!-- chunk {"id": "body-0058", "role": "body", "section": "VI-B Following language commands", "weight": 1.0} -->

The results in Figure 9, averaging over 10 trials per task, show that the language following accuracy of $\pi_{0}$ is significantly better than that of $\pi_{0}$-small. This suggests a significant improvement from the larger pre-trained VLM initialization. This capability translates to an improvement in performance with expert human guidance ($\pi_{0}$-human) and with high-level model guidance ($\pi_{0}$-HL). The results indicate that $\pi_{0}$'s language following ability directly translates into better autonomous performance on complex tasks with high-level guidance.

<!-- chunk {"id": "body-0059", "role": "body", "section": "VI-C Learning new dexterous tasks", "weight": 1.0} -->

In the next set of experiments, we evaluate our model on new tasks that differ significantly from the pre-training data, requiring entirely new behaviors. For these evaluations, we fine-tune the model using various amounts of data for each new task. While each task is new, we partition the tasks into "tiers" depending on how much they differ from tasks in the pre-training data. The tasks, shown in Figure 10, are: UR5e stack bowls. This task requires stacking bowls, with four bowls of different sizes. Since this task requires grasping and moving dishes like the bussing task in the pre-training data, we place it in the "easy" tier. The training data contains a variety of bowls, and the evaluations use a mix of seen and unseen bowls.

<!-- chunk {"id": "body-0060", "role": "body", "section": "VI-C Learning new dexterous tasks", "weight": 1.0} -->

Towel folding. This task requires folding a towel. Since this is similar to shirt folding, which is present in pre-training, we place it in the "easy" tier.

<!-- chunk {"id": "body-0061", "role": "body", "section": "VI-C Learning new dexterous tasks", "weight": 1.0} -->

Tupperware in microwave. This task requires opening a microwave, putting a plastic container inside it, and closing it. The containers come in different shapes and colors, and the evaluations use a mix of seen and unseen containers. The container manipulation resembles pre-training data, but the microwave is not found in pre-training.

<!-- chunk {"id": "body-0062", "role": "body", "section": "VI-C Learning new dexterous tasks", "weight": 1.0} -->

Paper towel replacement. This task requires removing an old cardboard paper towel tube from a holder and replacing it with a fresh paper towel roll. Because no such items are found in pre-training, we consider this "hard."

<!-- chunk {"id": "body-0063", "role": "body", "section": "VI-C Learning new dexterous tasks", "weight": 1.0} -->

Franka items in drawer. This task requires opening a drawer, packing items into a drawer, and closing it. Because there is no similar task with the Franka robot in pre-training, we consider this "hard."

<!-- chunk {"id": "body-0064", "role": "body", "section": "VI-C Learning new dexterous tasks", "weight": 1.0} -->

We compare our model after fine-tuning both to OpenVLA and Octo, which also employ a pre-training and fine-tuning recipe. Since our aim is to evaluate the specific models (rather than the architectures), we use the publicly available pre-trained checkpoints for these models, which are trained on OXE, and then fine-tune them to each task. We also compare to ACT and Diffusion Policy, which are designed specifically for learning dexterous tasks from smaller datasets. ACT and Diffusion Policy are trained *only* on the fine-tuning datasets, which are of similar size to the individual datasets used in the ACT and Diffusion Policy experiments. We evaluate $\pi_{0}$ by fine-tuning from our pre-trained base model, as well as by training from scratch. This comparison is meant to evaluate the individual benefits of the $\pi_{0}$ architecture and our pre-training procedure. We hypothesize that the $\pi_{0}$ architecture with VLM initialization should already provide a stronger starting point for the individual tasks, while the pre-training procedure should further improve its performance, especially with smaller fine-tuning datasets.

<!-- chunk {"id": "body-0065", "role": "body", "section": "VI-D Mastering complex multi-stage tasks", "weight": 1.0} -->

In our final set of experiments, we tackle a range of challenging multi-stage tasks via a combination of fine-tuning and language. For some of these tasks, data is present in pre-training, but fine-tuning is required to attain mastery. For some, no data is present in pre-training. The tasks in this evaluation, shown in Figure 12, are: Figure 13: Post-training results on complex tasks in terms of average scores over 10 trials. The full pre-trained π0 model attains more than 50% of the maximum score across all of the tasks, and typically outperforms the ablations, with especially significant improvements on the hardest tasks.

<!-- chunk {"id": "body-0066", "role": "body", "section": "VI-D Mastering complex multi-stage tasks", "weight": 1.0} -->

Laundry folding: This task requires a static (non-mobile) bimanual system to fold articles of clothing. The clothing items start in a randomized crumpled state in a bin, and the goal is to take out the item, fold it, and place it on top of a stack of previously folded items. The randomized initial configuration of the crumpled laundry presents a major challenge, since the policy needs to generalize to any configuration. This task is present in pre-training.

<!-- chunk {"id": "body-0067", "role": "body", "section": "VI-D Mastering complex multi-stage tasks", "weight": 1.0} -->

Mobile laundry: Here, the Fibocom mobile robot in Figure 5 has to fold laundry, facing many of the same challenges while controlling orientation and translation. This task is present in pre-training.

<!-- chunk {"id": "body-0068", "role": "body", "section": "VI-D Mastering complex multi-stage tasks", "weight": 1.0} -->

Dryer unloading: Here, the Fibocom mobile robot has to take laundry out of a dryer and place it into a hamper. This task is present in pre-training.

<!-- chunk {"id": "body-0069", "role": "body", "section": "VI-D Mastering complex multi-stage tasks", "weight": 1.0} -->

Box building: The robot has to assemble a cardboard box that starts in a flattened state. This task presents a number of major challenges: the box needs to bent in the right way, and the robot needs to hold down parts of the box while folding others, utilizing both arms and even the surface of the table to brace during folding motions. The robot might need to retry some folds, requiring a reactive and intelligent strategy. This task is not present in pre-training.

<!-- chunk {"id": "body-0070", "role": "body", "section": "VI-D Mastering complex multi-stage tasks", "weight": 1.0} -->

To-go box: This task requires moving several food items from a plate into a to-go box, requiring packing the items into the box so that they do not stick out, and then closing the box with both arms. This task is not present in pre-training.

<!-- chunk {"id": "body-0071", "role": "body", "section": "VI-D Mastering complex multi-stage tasks", "weight": 1.0} -->

Packing eggs: The robot needs to take six eggs out of a bowl and pack them into an egg carton, and then close the carton. The eggs need to be grasped in a manner appropriate to their pose inside the bowl, and then placed into open slots in the carton. This presents challenges due to the egg shape, slipperiness, and the need for careful placement. Closing the box requires the use of both arms. This task is not present in pre-training.

<!-- chunk {"id": "body-0072", "role": "body", "section": "VI-D Mastering complex multi-stage tasks", "weight": 1.0} -->

The results, showing average scores per task over 10 trials, are presented in Figure 13. The scoring rubrics are in Appendix A-E. A score of 1.0 represents a perfect execution, while partial scores correspond to partially completed tasks (e.g., 0.5 indicates that half the objects were bussed correctly). These tasks are very difficult, and we were not able to solve them with other methods. We therefore use these tasks to compare to ablations of our approach, evaluating $\pi_{0}$ after pre-training and fine-tuning, out of the box after pre-training only ("out-of-box"), and training on the fine-tuning data without any pre-training ("scratch"). The results show that $\pi_{0}$ can solve many of these tasks, with our full pre-training and fine-tuning recipe performing best across the board. Note that many of these more difficult tasks show a very large improvement from using the pre-trained model, indicating that pre-training is especially useful with harder tasks.

<!-- chunk {"id": "body-0073", "role": "body", "section": "VI-D Mastering complex multi-stage tasks", "weight": 1.0} -->

The absolute performance of $\pi_{0}$ varies across the tasks, likely due to differences in task difficulty and the degree to which the tasks are represented in pre-training. We recommend that readers watch the task videos on the accompanying website for a more complete impression of these tasks and their complexity. We believe that this level of autonomous performance on such challenging tasks represents a new state of the art in dexterous robot manipulation with learned policies.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Discussion, Limitations, and Future Work", "weight": 1.5} -->

We presented a framework for training a robot foundation model, which we refer to as $\pi_{0}$, that consists of pre-training on highly diverse data, followed by either out-of-box evaluation or fine-tuning to complex downstream tasks. Our empirical evaluation studies tasks that combine dexterity, generalization, and temporally extended multi-stage behaviors. Our model incorporates Internet-scale vision-language model (VLM) pre-training with flow matching for representing complex high-frequency action chunks. Our pre-training mixture consists of 10,000 hours of dexterous manipulation data from 7 different robot configurations and 68 tasks, in addition to large amounts of previously collected robot manipulation data from OXE, DROID, and Bridge. To our knowledge, this represents the largest pre-training mixture ever used for a robot manipulation model. Our fine-tuning experiments include over 20 tasks, where we show that our model outperforms a variety of baselines, including prior VLA models and models designed specifically for dexterous manipulation. We also examine how our post-training recipe can enable highly complex tasks, such as folding multiple articles of clothing from arbitrary initial configurations or assembling boxes.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Discussion, Limitations, and Future Work", "weight": 1.5} -->

Our framework broadly resembles the training procedures employed for large language models, which typically consist of pre-training a base model on very large datasets scraped from the web, followed by a post-training procedure that aims to "align" the model to enable it to follow instructions and perform user commands. It is generally recognized that most of the "knowledge" in such models is acquired in the pre-training phase, while the post-training phase serves to tell the model how it should leverage that knowledge to fulfill user commands. Our experiments imply that an analogous phenomenon might take place with robot foundation models, where pre-trained models have some zero-shot capabilities, but complex tasks like laundry following require fine-tuning with high-quality data. Training on only this high-quality data results in a brittle model that does not reliably recover from mistakes, while running the pre-trained model in zero shot does not always exhibit the fluent strategies demonstrated in the post-training data.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Discussion, Limitations, and Future Work", "weight": 1.5} -->

We hope that our results will serve as a stepping stone toward general and broadly applicable robot foundation models. Our experiments suggest that such models may soon be a reality, but there are a number of limitations and ample room for future work. First, our experiments do not yet provide a comprehensive understanding of how the pre-training datasets should be composed: we combined all data available to us, but understanding what type of data is more helpful to add and how it should be weighted remains an open problem. Not all tasks in our evaluation work reliably, and it remains unclear how to predict how much and what kind of data is needed to attain near-perfect performance. Finally, it remains to be seen how much positive transfer there is in combining highly diverse data, particularly from different tasks and different robots: although our results suggest that universal pre-trained robot foundation models might become a reality, it is left for future work to understand whether this universality extends to much more distinct domains, such as autonomous driving, navigation, and legged locomotion.
