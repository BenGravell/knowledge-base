<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

RT-1: Robotics Transformer for Real-World Control at Scale

Topics include Robotics, Transformers, Computer vision, Datasets, Generalization, Control, Learning, RT-1.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

By transferring knowledge from large, diverse, task-agnostic datasets, modern machine learning models can solve specific downstream tasks either zero-shot or with small task-specific datasets to a high level of performance. While this capability has been demonstrated in other fields such as computer vision, natural language processing or speech recognition, it remains to be shown in robotics, where the generalization capabilities of the models are particularly critical due to the difficulty of collecting real-world robotic data. We argue that one of the keys to the success of such general robotic models lies with open-ended task-agnostic training, combined with high-capacity architectures that can absorb all of the diverse, robotic data. In this paper, we present a model class, dubbed Robotics Transformer, that exhibits promising scalable model properties. We verify our conclusions in a study of different model classes and their ability to generalize as a function of the data size, model size, and data diversity based on a large-scale data collection on real robots performing real-world tasks. The project's website and videos can be found at robotics-transformer1.github.io

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

End-to-end robotic learning, with either imitation or reinforcement, typically involves collecting task-specific data in either single-task or multi-task settings that are narrowly tailored to the tasks that the robot should perform. This workflow mirrors the classic approach to supervised learning in other domains, such as computer vision and NLP, where task-specific datasets would be collected, labeled, and deployed to solve individual tasks, with little interplay between the tasks themselves. Recent years have seen a transformation in vision, NLP, and other domains, away from siloed, small-scale datasets and models and towards large, general models pre-trained on broad, large datasets. The keys to the success of such models lie with open-ended task-agnostic training, combined with high-capacity architectures that can absorb all of the knowledge present in large-scale datasets. If a model can "sponge up" experience to learn general patterns in language or perception, then it can bring them to bear on individual tasks more efficiently.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

While removing the need for large task-specific datasets is appealing generally in supervised learning, it is even more critical in robotics, where datasets might require engineering-heavy autonomous operation or expensive human demonstrations. We therefore ask: can we train a single, capable, large multi-task backbone model on data consisting of a wide variety of robotic tasks? And does such a model enjoy the benefits observed in other domains, exhibiting zero-shot generalization to new tasks, environments, and objects?

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Building such models in robotics is not easy. Although recent years have seen several large multi-task robot policies proposed in the literature, such models often have limited breadth of real-world tasks, as with Gato, or focus on training tasks rather than generalization to new tasks, as with recent instruction following methods, or attain comparatively lower performance on new tasks.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

(a) RT-1 takes images and natural language instructions and outputs discretized base and arm actions. Despite its size (35M parameters), it does this at 3 Hz, due to its efficient yet high-capacity architecture: a FiLM conditioned EfficientNet, a TokenLearner, and a Transformer.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

(b) RT-1’s large-scale, real-world training (130k demonstrations) and evaluation (3000 real-world trials) show impressive generalization, robustness, and ability to learn from diverse data.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The two main challenges lie in assembling the right dataset and designing the right model. While data collection and curation is often the "unsung hero" of many large-scale machine learning projects, this is especially true in robotics, where datasets are often robot-specific and gathered manually. As we will show in our evaluations, good generalization requires datasets that combine both scale and breadth, covering a variety of tasks and settings. At the same time, the tasks in the dataset should be sufficiently well-connected to enable generalization, such that the model can discover the patterns between structural similar tasks and perform new tasks that combine those patterns in novel ways. We utilize a dataset that we gathered over the course of 17 months with a fleet of 13 robots, containing $\sim$`<!-- -->`{=html}130k episodes and over 700 tasks, and we ablate various aspects of this dataset in our evaluation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The second challenge lies in the design of the model itself. Effective robotic multi-task learning requires a high capacity model, and Transformer models excel in this regard, particularly when it is necessary to learn many tasks conditioned, as in our case, on language instructions. However, robotic controllers must also be efficient enough to run in real time, which presents a major challenge for Transformers in particular. We propose a novel architecture that we call RT-1 (Robotics Transformer 1), which by encoding high-dimensional inputs and outputs, including camera images, instructions and motor commands into compact token representations to be used by the Transformer, allows for efficient inference at runtime to make real-time control feasible.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our contribution is the RT-1 model and experiments with this model on a large and broad dataset of real-world robotic tasks. Our experiments not only demonstrate that RT-1 can exhibit significantly improved generalization and robustness compared to prior techniques, but also evaluate and ablate many design choices in both the model and in the composition of the training set. Our results show that RT-1 can perform over 700 training instructions at 97% success rate, and can generalize to new tasks, distractors, and backgrounds 25%, 36% and 18% better than the next best baseline, respectively. This level of performance allows us to execute very long-horizon tasks in the SayCan framework, with as many as 50 stages. We further show that RT-1 can incorporate data from simulation or even other robot types, retaining performance on the original tasks and improving generalization to new scenarios. A short overview of RT-1 capabilities is presented in Fig. 0(b) ‣ Figure 1 ‣ 1 Introduction ‣ RT-1: Robotics Transformer for Real-World Control at Scale")^22^2Helper robots shown in Fig. 1-5 are from Everyday Robots.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Robot learning", "weight": 1.0} -->

We aim to learn robot policies to solve language-conditioned tasks from vision. Formally, we consider a sequential decision-making environment. At timestep $t = 0$, the policy $\pi$ is presented with a language instruction $i$ and an initial image observation $x_{0}$. The policy produces an action distribution $\pi{( \cdot |i,x_{0})}$ from which an action $a_{0}$ is sampled and applied to the robot. This process continues, with the policy iteratively producing actions $a_{t}$ by sampling from a learned distribution $\pi{( \cdot |i,{\{ x_{j}\}}_{j = 0}^{t})}$ and applying those actions to the robot. The interaction ends when a termination condition is achieved. The full interaction $i,{\{{(x_{j},a_{j})}\}}_{j = 0}^{T}$ from from the starting step $t = 0$ to terminating step $T$ is referred to as an *episode*.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Robot learning", "weight": 1.0} -->

At the end of an episode, the agent will be given a binary reward $r \in {\{ 0,1\}}$ indicating whether the robot performed the instruction $i$. The goal is to learn a policy $\pi$ that maximizes the average reward, in expectation over a distribution of instructions, starting states $x_{0}$, and transition dynamics.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Robot learning", "weight": 1.0} -->

Transformers. RT-1 uses a Transformer to parameterize the policy $\pi$. Generally speaking, a Transformer is a sequence model mapping an input sequence ${\{\xi_{h}\}}_{h = 0}^{H}$ to an output sequence ${\{ y_{k}\}}_{k = 0}^{K}$ using combinations of self-attention layers and fully-connected neural networks. While Transformers were originally designed for text sequences, where each input $\xi_{j}$ and output $y_{k}$ represents a text token, they have been extended to images as well as other modalities.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Robot learning", "weight": 1.0} -->

Imitation learning. Imitation learning methods train the policy $\pi$ on a dataset $\mathcal{D}$ of demonstrations. Specifically, we assume access to a dataset $\mathcal{D} = {\{{(i^{(n)},{\{{(x_{t}^{(n)},a_{t}^{(n)})}\}}_{t = 0}^{T^{(n)}})}\}}_{n = 0}^{N}$ of episodes, all of which are successful (i.e., have a final reward of $1$). We learn $\pi$ using *behavioral cloning*, which optimizes $\pi$ by minimizing the negative log-likelihood of actions $a_{t}$ given the images and language instructions.

<!-- chunk {"id": "body-0015", "role": "body", "section": "System Overview", "weight": 1.0} -->

The goal of this work is to build and demonstrate a general robot learning system that can absorb large amounts of data and generalize effectively. We use mobile manipulators from Everyday Robots^33^3[everydayrobots.com](everydayrobots.com), which have a 7 degree-of-freedom arm, a two-fingered gripper, and a mobile base (see Fig. 2 (d)). To collect data and evaluate our method, we use three kitchen-based environments: two real office kitchens and a training environment modelled off these real kitchens. The training environment, shown in Fig. 2 (a), consists of partial counters and is constructed for large scale data collection. The two real environments, shown in Fig. 2 (b, c), have similar counter tops to the training environment, but vary in lighting, background, and full kitchen geometry (e.g., there may be a cabinet instead of a drawer or a sink may be visible). We evaluate the performance of our policies across these different environments, measuring the policy's performance and ability to generalize.

<!-- chunk {"id": "body-0016", "role": "body", "section": "System Overview", "weight": 1.0} -->

Our training data consists of human-provided demonstrations, and we annotate each episode with a textual description of the instruction that the robot just performed. The instructions usually contain a verb and one or more nouns describing the target objects. To group these instructions together, we split them into a number of skills (e.g., verbs such as "pick", "open" or "place upright") and objects (e.g., nouns such as "coke can", "apple", or "drawer"). We describe the details of our data collection strategy at scale in Sec. 5.2. Our largest dataset contains over 130k individual demonstrations constituting over 700 distinct task instructions using a large variety of objects (see Fig. 2 (f)). We describe the details of the data collected in Sec. 5.2.

<!-- chunk {"id": "body-0017", "role": "body", "section": "System Overview", "weight": 1.0} -->

One of the main contributions of our system is the network architecture, Robotics Transformer 1 (RT-1), an efficient model that can absorb large amounts of data, effectively generalize, and output actions at real-time rates for practical robotic control. RT-1 takes a short sequence of images and a natural language instruction as input and outputs an action for the robot at each time step. To this end, the architecture (shown in Figure 0(a) ‣ Figure 1 ‣ 1 Introduction ‣ RT-1: Robotics Transformer for Real-World Control at Scale")) leverages several elements: first the images and text are processed via an ImageNet pretrained convolutional network conditioned on a pretrained embedding of the instruction via FiLM, followed by a Token Learner to compute a compact set of tokens, and finally a Transformer to attend over these tokens and produce discretized action tokens.

<!-- chunk {"id": "body-0018", "role": "body", "section": "System Overview", "weight": 1.0} -->

The actions consist of seven dimensions for the arm movement (x, y, z, roll, pitch, yaw, opening of the gripper), three dimensions for base movement (x, y, yaw) and a discrete dimension to switch between three modes: controlling the arm, the base, or terminating the episode. RT-1 performs closed-loop control and commands actions at $3$ Hz until it either yields a "terminate" action or hits a pre-set time step limit.

<!-- chunk {"id": "body-0019", "role": "body", "section": "RT-1: Robotics Transformer", "weight": 1.0} -->

In this section, we describe how we tokenize the images, text, and actions, and then discuss the RT-1 model architecture. We then describe how we attain the runtime speed required for real-time control. Lastly, we describe the data collection procedure and the skills and instructions in our dataset.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Model", "weight": 1.0} -->

Our model is built on a Transformer architecture and takes a history of images and task description as input and directly outputs tokenized actions, as shown in Fig. 0(a) ‣ Figure 1 ‣ 1 Introduction ‣ RT-1: Robotics Transformer for Real-World Control at Scale") and in detail in Fig. 3. In the following we describe the components of the model, following the top-to-bottom order in Fig. 3. More detail on model selection at scale are provided in Appendix C.3.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Model", "weight": 1.0} -->

Instruction and image tokenization. The RT-1 architecture relies on a data-efficient and compact tokenization of images and language instruction. RT-1 tokenizes a history of 6 images by passing images through an ImageNet pretrained EfficientNet-B3 model, which takes 6 images of resolution $300 \times 300$ as input and outputs a spatial feature map of shape $9 \times 9 \times 512$ from the final convolutional layer. Unlike Reed et al., we do not patchify the images into visual tokens prior to feeding them to our Transformer backbone. We instead flatten the output feature map from the EfficientNet into $81$ visual tokens which are passed on to the later layers of the network.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Model", "weight": 1.0} -->

To include the language instruction, we condition the image tokenizer on the natural language instruction in the form of a pretrained language embedding, allowing extraction of task-relevant image features early on and improving performance of RT-1. The instruction is first embedded via Universal Sentence Encoder. This embedding is then used as input to identity-initialized FiLM layers added to the pretrained EfficientNet to condition the image encoder. Normally, inserting a FiLM layer into the interior of a pretrained network would disrupt the intermediate activations and negate the benefit of using pretrained weights. To overcome this, we initialize the weights of the dense layers ($f_{c}$ and $h_{C}$) which produce the FiLM affine transformation to zero, allowing the FiLM layer to initially act as an identity and preserve the function of the pretrained weights. We find that identity-initialized FiLM also produces better results when training with an EfficientNet initialized from scratch, without ImageNet pretraining, but it does not surpass the initialization described above. The architecture of the image tokenizer is presented in Fig. 3.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Model", "weight": 1.0} -->

RT-1's image and instruction tokenization via FiLM EfficientNet-B3 is a total of 16M parameters, with 26 layers of MBConv blocks and FiLM layers, which output 81 vision-language tokens.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Model", "weight": 1.0} -->

TokenLearner. To further compress the number of tokens that RT-1 needs to attend over and thus speed up inference, RT-1 uses TokenLearner. TokenLearner is an element-wise attention module that learns to map a large number of tokens into a much smaller number of tokens. This allows us to soft-select image tokens based on their information, passing only the important token combinations to the subsequent Transformer layers. The inclusion of TokenLearner subsamples the $81$ visual tokens that come out of the pre-trained FiLM-EfficientNet layers to just $8$ final tokens that are then passed on to our Transformer layers.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Model", "weight": 1.0} -->

Transformer. These 8 tokens per-image are then concatenated with the other images in the history, forming 48 total tokens (with added position encoding) to be fed into the Transformer backbone of RT-1. The Transformer is a decoder-only sequence model with 8 self-attention layers and 19M total parameters that outputs action tokens.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Model", "weight": 1.0} -->

Action tokenization. To tokenize actions, each action dimension in RT-1 is discretized into $256$ bins. As mentioned previously, the action dimensions we consider include seven variables for the arm movement ($x$, $y$, $z$, roll, pitch, yaw, opening of the gripper), three variables for base movement ($x$, $y$, yaw) and a discrete variable to switch between three modes: controlling arm, base or terminating the episode. For each variable, we map the target to one of the 256 bins, where the bins are uniformly distributed within the bounds of each variable.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Model", "weight": 1.0} -->

Loss. We use a standard categorical cross-entropy entropy objective and causal masking that was utilized in prior Transformer-based controllers.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Model", "weight": 1.0} -->

Inference speed. In contrast to many applications of large models, such as natural language or image generation, one of the unique requirements for a model that needs to run on real robots in real time is fast and consistent inference speed. Given the human speeds of executing the instructions considered in this work (which we measured to be in the $2 - 4$ secs range), we want the model to be not significantly slower than that. Based on our experiments this requirement corresponds to at least $3$Hz control frequency and the resulting inference time budget for the model, given other latencies in the system, to be less than $100$ms.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Model", "weight": 1.0} -->

This requirement limits the size of the model that we can use. We further explore the impact of model size on inference speed in the experiments. We employ two techniques to speed up inference: (i) reduce the number of tokens generated by a pre-trained EfficientNet model by using TokenLearner, (ii) compute these tokens only once and reuse them for the following windows that overlap for the future inferences. Both of these allow us to speed up the model inference by $2.4$ and $1.7$ times, respectively. Additional details on model inference are in Appendix C.1.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Data", "weight": 1.0} -->

Lift the object off the surface
pick iced tea can

<!-- chunk {"id": "body-0031", "role": "body", "section": "Data", "weight": 1.0} -->

Move Object Near Object
Move the first object near the second
move pepsi can near rxbar blueberry

<!-- chunk {"id": "body-0032", "role": "body", "section": "Data", "weight": 1.0} -->

Place Object Upright
Place an elongated object upright
place water bottle upright

<!-- chunk {"id": "body-0033", "role": "body", "section": "Data", "weight": 1.0} -->

Knock Object Over
Knock an elongated object over
knock redbull can over

<!-- chunk {"id": "body-0034", "role": "body", "section": "Data", "weight": 1.0} -->

Open any of the cabinet drawers
open the top drawer

<!-- chunk {"id": "body-0035", "role": "body", "section": "Data", "weight": 1.0} -->

Close any of the cabinet drawers
close the middle drawer

<!-- chunk {"id": "body-0036", "role": "body", "section": "Data", "weight": 1.0} -->

Place Object into Receptacle
Place an object into a receptacle
place brown chip bag into white bowl

<!-- chunk {"id": "body-0037", "role": "body", "section": "Data", "weight": 1.0} -->

Pick Object from Receptacle and Place on the Counter
Pick an object up from a location and then place it on the counter
pick green jalapeno chip bag from paper bowl and place on counter

<!-- chunk {"id": "body-0038", "role": "body", "section": "Data", "weight": 1.0} -->

Section 6.3 and 6.4 tasks
Skills trained for realistic, long instructions
open the large glass jar of pistachios

<!-- chunk {"id": "body-0039", "role": "body", "section": "Data", "weight": 1.0} -->

Our goal is to build a system that exhibits high performance, generalization to new tasks, and robustness to distractors and backgrounds. We therefore aim to collect a large, diverse dataset of robot trajectories that includes multiple tasks, objects and environments. Our primary dataset consists of $\sim$`<!-- -->`{=html}130k robot demonstrations, collected with a fleet of 13 robots over the course of 17 months. We conducted this large-scale data collection in a series of office kitchen segments, which we refer to as robot classrooms, shown in Fig. 2. More details on data collection are in Appendix C.2.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Data", "weight": 1.0} -->

Skills and instructions. While the definition of a task remains inconsistent in the literature, in this work we count the number of language instructions that the system can perform, where an instruction corresponds to a verb surrounded by one or multiple nouns, such as "place water bottle upright", "move the coke can to the green chip bag" or "open the drawer". RT-1 is able to perform over 700 language instructions in multiple realistic office kitchen environments that we evaluate and describe in detail in the experiments. In order to group the evaluations and draw conclusions on the performance of the system, we group the instructions by the verbs used in them, which we refer to as skills. A more detailed list of instructions is shown in Table 1, with examples and the number of instructions per skill.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Data", "weight": 1.0} -->

The current set of skills includes picking, placing, opening and closing drawers, getting items in and out drawers, placing elongated items up-right, knocking them over, pulling napkins and opening jars. The skills were chosen to demonstrate multiple behaviors with many objects (seen in Fig. 2(e)) to test aspects of RT-1 such as generalization to new instructions and ability to perform many tasks. We then greatly expanded the object diversity for the "pick" skill to make sure that the skills generalize to varied objects (see the expanded set of objects in Fig. 2(f)). The skills were further expanded while we conducted the ablations to include instructions added in the last row of Table 1, which were used for the experiments described in Sec. 6.4 and 6.3. These additional skills focused on realistic, long-horizon instructions in an office kitchen. The entire process of adding tasks and data is described in the Appendix C.4. Since we do not make any assumptions about particular skills when adding new instructions, the system is easily extendable, and we can continuously provide more diverse data to improve its capabilities.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experiments", "weight": 1.0} -->

Can an RT-1 learn to perform a large number of instructions, as well as to generalize in zero shot to new tasks, objects and environments? (Section 6.2)

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experiments", "weight": 1.0} -->

Can we push the resulting model even further by incorporating heterogeneous data sources, such as simulated data or data from different robots? (Section 6.3)

<!-- chunk {"id": "body-0044", "role": "body", "section": "Experiments", "weight": 1.0} -->

How do various methods generalize to long-horizon robotic scenarios? (Section 6.4)

<!-- chunk {"id": "body-0045", "role": "body", "section": "Experiments", "weight": 1.0} -->

How do generalization metrics change with varying amounts of data quantity and data diversity? (Section 6.5)

<!-- chunk {"id": "body-0046", "role": "body", "section": "Experiments", "weight": 1.0} -->

What are the important and practical decisions in the design of the model and how do they affect performance and generalization? (Appendix Section D.4)

<!-- chunk {"id": "body-0047", "role": "body", "section": "Experiments", "weight": 1.0} -->

Throughout this section we will compare to two baseline state of the art architectures, Gato and BC-Z. Importantly both of these are trained on our data described in detail in Sec. 5.2 (which is an important part of our system) since the original models in these publications would not exhibit generalization properties required for our evaluation tasks. Gato is, similarly to RT-1, based on a Transformer architecture, but varies from RT-1 in multiple aspects. First, it computes image tokens without the notion of language and each image token embedding is computed separately for each image patch, as opposed to early language fusion and global image embedding in our model. Second, it does not use a pre-trained text embedding to encode the language string. It also does not include inference time considerations that are necessary for real robots as discussed in Sec. 5.1 such as TokenLearner and the removal of auto-regressive actions.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Experiments", "weight": 1.0} -->

In order to run Gato on real robots at a high enough frequency, we also limit the size of the model compared to the original publication, which was 1.2B parameters (resulting in on robot inference time of $1.9$s), to be of similar size to RT-1 (37M parameters for Gato vs. 35M for RT-1). BC-Z is based on a ResNet architecture, and was used in SayCan. BC-Z differs from RT-1 in that it is a feedforward model that does not use previous timesteps, and it uses continuous actions rather than discrete action tokens. In addition to the original BC-Z model size, we also compare our method to a larger version of BC-Z that has a similar number of parameters to RT-1 and refer to it as BC-Z XL. We study and analyze how each of these design decisions changes performance in Appendix Sections D.4 and D.5.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate the success rate in experiments to measure performance on training instructions, generalization to unseen instructions, robustness to backgrounds and distractors, and performance in long-horizon scenarios, as detailed below. Throughout this section, we evaluate our approach and baselines with over 3000 real-world trials, making one of the largest scale evaluation of a robot learning system to-date.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

As mentioned in Section 4, we evaluate RT-1 with a set of mobile manipulators from Everyday Robots in three environments: two real office kitchens and a training environment modelled off these real kitchens. The training environment, shown in Fig. 2 (a), consists of partial counters while the two real environments, shown in Fig. 2 (b, c), have similar counter tops to the training environment, but vary in lighting, background, and full kitchen geometry (e.g., there may be a cabinet instead of a drawer or a sink may be visible). The policies are evaluated for performance on training tasks as well as generalization to new tasks, robustness to unseen environments, and performance when chained together for long-horizon tasks, as detailed below.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Seen task performance. To evaluate performance on seen instructions, we evaluate performance on instructions sampled from the training set. Note, however, that this evaluation still involves varying the placement of objects and other factors of the setup (e.g., time of day, robot position), requiring the skills to generalize to realistic variability in the environment. In all, we test over 200 tasks in this evaluation: 36 for picking objects, 35 for knocking objects, 35 for placing things upright, 48 for moving objects, 18 for opening and closing various drawers, and 36 for picking out of and placing objects into drawers.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Unseen tasks generalization. To evaluate generalization to unseen tasks, we test 21 novel, unseen instructions. These instructions are distributed across skills and objects. This ensures that at least some instances of each object and skill were present in the training set but they will be combined in novel ways. For example, if "pick up the apple" is held out, then there are other training instructions that include the apple. The list of all unseen instructions can be found in the Appendix D.1.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Robustness. To evaluate robustness, we perform 30 real-world tasks for distractor robustness and 22 tasks for background robustness. The background robustness was tested by evaluating in new kitchens (which have different lighting and background visuals) and with different counter surfaces (e.g., a patterned table cloth). Example configurations of the robustness evaluation scenarios are depicted in Fig. 4.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Long-horizon scenarios. We also evaluate generalization to more realistic long-horizon scenarios, which each require executing a sequence of skills. The goal of this evaluation is to combine multiple generalization axes such as new tasks, objects, environments and test the overall generalization capabilities in realistic settings. These evaluations consist of 15 long-horizon instructions in two real kitchens, which require executing sequences of skills consisting of $\sim 10$ distinct steps, with each step of roughly comparable scope as the training instructions. These steps are obtained automatically from higher level instructions, such as "how would you throw away all the items on the table?" by using the SayCan system, as described in detail in Section 6.4 and Appendix D.3.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Can RT-1 learn to perform a large number of instructions, and to generalize to new tasks, objects and environments?", "weight": 1.0} -->

To answer our first question, we analyze the overall performance, generalization, and robustness capabilities of RT-1 compared to previously proposed models. Specifically, we compare to the model architectures used by Gato and BC-Z, as well as a larger version of BC-Z, which we refer to as BC-Z XL. Note, however, that all models are trained on the same data as RT-1, and the evaluation only compares the model architectures, not the task sets, datasets, or overall robotic systems. The capabilities of RT-1 are determined to a large extent by the dataset and task set, which we believe improves significantly over prior works (e.g. BC-Z uses 100 tasks and the original Gato model trains a stacking task with various shapes), and thus this comparison should be viewed as rather favorable to the prior models, which also benefit from the large and diverse dataset and task set that we collected.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Can RT-1 learn to perform a large number of instructions, and to generalize to new tasks, objects and environments?", "weight": 1.0} -->

The results are shown in Table 2. Across each category, we find that RT-1 outperforms the prior models significantly. On seen tasks, RT-1 is able to perform 97% of the more than 200 instructions successfully, which is 25% more than BC-Z and 32% more than Gato. On unseen tasks, RT-1 shows it is capable of generalizing to novel instructions, performing 76% of the never-before-seen instructions, 24% more than the next best baseline. While such generalization to novel instructions is made possible due to natural language conditioning of the policy, as the policy is able to understand new combinations of previously seen concepts, all of the baselines are also conditioned on natural language and in principle enjoy the same benefits. We further ablate different components of RT-1 in the next section to better understand what aspects of our method contribute the most to this difference. On distractors and backgrounds, we find that RT-1 is quite robust, successfully executing 83% of the distractor robustness tasks and 59% of the background robustness tasks (36% and 18% higher than the next best alternative, respectively).

<!-- chunk {"id": "body-0057", "role": "body", "section": "Can RT-1 learn to perform a large number of instructions, and to generalize to new tasks, objects and environments?", "weight": 1.0} -->

Overall, we find that RT-1 has high general performance, while exhibiting impressive degrees of generalization and robustness. We show example trajectories of the RT-1 agent including instructions that cover different skills, environments and objects in Fig. 5. We also present additional trajectory examples for different generalization tests in the Appendix, which include backgrounds (Fig. 10), and distractors (Fig. 12).

<!-- chunk {"id": "body-0058", "role": "body", "section": "Can RT-1 learn to perform a large number of instructions, and to generalize to new tasks, objects and environments?", "weight": 1.0} -->

Generalization to realistic instructions. Next, we test whether our method generalizes enough across all the different axes that we evaluated previously to be deployed in a real kitchen, which poses multiple distribution shifts all at once such as new tasks combinations, object distractors as well as a novel environment.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Can RT-1 learn to perform a large number of instructions, and to generalize to new tasks, objects and environments?", "weight": 1.0} -->

To evaluate our algorithm in realistic scenarios in a real kitchen, we construct task sequences to accomplish a number of realistic goals. The robot restocks several snacks in drawers, tidies up knocked over condiment bottles and closes drawers left open by humans, prepares a snack with an orange and a napkin and fetches lost sunglasses and an octopus toy from several places in the kitchen. The detailed instructions used in these scenarios are listed in the Appendix D.1. The office kitchen involves a dramatic shift from the training environment and we categorize tasks across these scenarios with varying levels of generalization: $L1$ for generalization to the new counter-top layout and lighting conditions, $L2$ for additionally generalization to unseen distractor objects, $L3$ for additional generalization to drastically new task settings, new task objects or objects in unseen locations such as near a sink. The three levels that correspond to the three tasks of restocking, preparing a snack and fetching a lost object in the real kitchen are depicted in the last row of Fig. 4. Example trajectories for different levels are presented in the Appendix in Fig. 11.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Can RT-1 learn to perform a large number of instructions, and to generalize to new tasks, objects and environments?", "weight": 1.0} -->

We report the per-task success rate in these realistic scenarios along with the varying generalization levels in Table 3 and find RT-1 to be the most robust on all levels. Gato generalizes fairly well at the first level but it performs significantly drops for the more difficult generalization scenarios. BC-Z and its XL equivalent perform fairly well at $L2$ level and better than Gato at $L3$ but they are still not at the generalization level of RT-1.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Can we push the resulting model further by incorporating heterogeneous data sources such as simulation or data from different robots?", "weight": 1.0} -->

Next, we explore the limits of RT-1 for utilizing highly heterogeneous data. We demonstrate how RT-1 can incorporate and learn from vastly different data sources and improve from such data without sacrificing its original-tasks performance across the varied tasks inherent in this data. To this end, we conduct two experiments: RT-1 trained and tested on both real data and simulation data and RT-1 trained across large datasets of different tasks, originally collected by different robots. More information on each is provided in Appendix D.2.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Can we push the resulting model further by incorporating heterogeneous data sources such as simulation or data from different robots?", "weight": 1.0} -->

Absorbing simulation data. Table 4 shows the ability of RT-1, and baselines, to absorb both real and simulation data. To test this, we take all of the real demonstration data but we also provide additional simulation data that includes objects that the robot has never seen in the real world. Specifically, we specify different generalization scenarios: for seen skills with real objects the training data has real data of that instruction (i.e., performance on seen tasks), for seen skills with sim objects the training data has sim data of that instruction (e.g. "pick up a sim object", which was present in sim), and for unseen skills with sim objects the training data has sim data of that object but there are no examples of the instruction describing the skill with that object either in sim or in real (e.g., "move a sim object to apple", even though the robot has only practiced in picking that sim object and not moving it near other objects). All evaluations are done in the real world but to limit the number of instructions evaluated, we focus on pick and move-to skills.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Can we push the resulting model further by incorporating heterogeneous data sources such as simulation or data from different robots?", "weight": 1.0} -->

We find in Table 4 that for RT-1, we do not lose performance adding simulation data compared to the Real Only dataset. We do however, see a significant increase in performance (from 23% to 87%) on objects and tasks seen only in simulation, to approximately the performance of the those in real, demonstrating an impressive degree of domain transfer. We also see a significant increase in performance on unseen instructions from 7% to 33%; impressive given the object in question has never been seen in real and the instruction never seen at all. Overall, we find that RT-1 is able to efficiently absorb new data, even from a very different domain.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Can we push the resulting model further by incorporating heterogeneous data sources such as simulation or data from different robots?", "weight": 1.0} -->

Sim Objects (not seen in real)

<!-- chunk {"id": "body-0065", "role": "body", "section": "Can we push the resulting model further by incorporating heterogeneous data sources such as simulation or data from different robots?", "weight": 1.0} -->

Absorbing data from different robots. To push the data absorption limits of RT-1, we conduct an additional set of experiments where we combine two data sources that originate from different robots: Kuka IIWA as well as the Everyday Robots mobile manipulators used in the experiments so far. The Kuka data contains all the successful examples collected in QT-Opt, which corresponds to 209k episodes, where the robot was indiscriminately grasping objects in a bin (see an example of a Kuka episode in Table. 5). To test whether RT-1 can effectively absorb these two very different datasets, which we refer to as the standard "Classroom eval", as well as the performance on the newly constructed tasks that reflect the bin-picking setup present in the Kuka data, which we refer to as the "Bin-picking eval" (see Fig. 6).

<!-- chunk {"id": "body-0066", "role": "body", "section": "Can we push the resulting model further by incorporating heterogeneous data sources such as simulation or data from different robots?", "weight": 1.0} -->

We would like to emphasize the difficulty of this setting by noting the major differences between the datasets. Not only are the robots that collected the data different in appearance and action space, but also the environment they were deployed in has different appearance and dynamics. In addition the QT-Opt data presents a completely different action distribution -- it was collected by an RL agent as opposed to human demonstrations present in our dataset.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Can we push the resulting model further by incorporating heterogeneous data sources such as simulation or data from different robots?", "weight": 1.0} -->

The results are presented in Table 5. We observe that the model that mixes the RT-1 data and the Kuka data has only a minimal decrease in the original tasks' performance (i.e. Classroom eval), i.e. $2\%$. Even more importantly, in the Bin-picking eval, we observe that the model trained on multi-robot data performs at $39\%$ compared to the $22\%$ of the model that was trained only on the RT-1 data. This is a $17\%$ performance difference (almost 2x). Additionally, RT-1 trained on Kuka bin-picking data and evaluated on the bin-picking tasks with the Everyday Robots (EDR) robot achieves 0% performance, confirming that it is difficult to transfer a behavior from another robot morphology. However, mixing the data from both robots allows RT-1 to infer the correct actions of the EDR robot even when faced with the states observed by Kuka robots. This is achieved without explicit demonstrations of bin-picking on EDR robot and by taking advantage of past experiences collected by Kuka robots.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Can we push the resulting model further by incorporating heterogeneous data sources such as simulation or data from different robots?", "weight": 1.0} -->

These results indicate that RT-1's absorption properties also include the ability to acquire new skills through observing other robots' experiences and present an exciting avenue of future work where we combine many more multi-robot datasets to enhance the robot capabilities.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Can we push the resulting model further by incorporating heterogeneous data sources such as simulation or data from different robots?", "weight": 1.0} -->

Kuka bin-picking data + EDR data

<!-- chunk {"id": "body-0070", "role": "body", "section": "How do various methods generalize long-horizon robotic scenarios?", "weight": 1.0} -->

In the next set of experiments we evaluate whether our method generalizes enough to be used in long-horizon realistic kitchen settings. To answer this question, we execute RT-1 and various baselines within the SayCan framework in two different real kitchens. Since SayCan combines many low-level instructions to perform high-level instructions, the number of possible high-level instructions increases combinatorially with skills, so the skill-breadth of RT-1 can be fully seen (for more details on the SayCan algorithm please refer to Ahn et al. ). The success rate of long-horizon tasks also decreases exponentially with the length of the task, so high success rates in manipulation skills are particularly important. Furthermore, as mobile manipulation tasks require both navigation and manipulation, the policies ability to be robust to base position is crucial. More detail is provided in Appendix D.3.

<!-- chunk {"id": "body-0071", "role": "body", "section": "How do various methods generalize long-horizon robotic scenarios?", "weight": 1.0} -->

Table 6 shows our results (on instructions in Appendix Table 12). Except for original SayCan, all methods get 87% as planning success rate, and RT-1 performs the best, with 67% execution success rate in Kitchen1. Kitchen2 constitutes a much more challenging generalization scene, since the Robot Classroom training scenes are modeled after Kitchen1 (see the pictures of the kitchens in Fig. 2). Due to this generalization difficulty, SayCan with Gato is not able to finish any long horizon task, and SayCan with BC-Z is able to achieve a success rate of 13%. The original SayCan paper did not evaluate performance in a new kitchen. Surprisingly, the manipulation performance does not see a visible drop from Kitchen1 to Kitchen2 for our method. In the supplementary video, we show that this enables us to operate unseen drawers in Kitchen2, and that we can use SayCan-RT1 to plan and execute ultra-long horizon tasks, with as many as 50 steps.

<!-- chunk {"id": "body-0072", "role": "body", "section": "How do various methods generalize long-horizon robotic scenarios?", "weight": 1.0} -->

SayCan tasks in Kitchen1
SayCan tasks in Kitchen2

<!-- chunk {"id": "body-0073", "role": "body", "section": "How do generalization metrics change with varying amounts of data quantity and data diversity?", "weight": 1.0} -->

While previous works have shown the scaling abilities of Transformer-based models with the number of model parameters, in many robotics works the model size is often not the primary bottleneck, and the maximum size is limited by the latency requirement for running such models on real robots. Instead, in this study we focus on ablating the influence of dataset size and diversity, as they play an important role in the traditionally data-limited robot learning field. Since data collection is particularly expensive for real robots, it is important to quantify what kind of data our models need to achieve a certain performance and generalization. Thus, our last question focuses on the scaling properties of RT-1 with different data properties.

<!-- chunk {"id": "body-0074", "role": "body", "section": "How do generalization metrics change with varying amounts of data quantity and data diversity?", "weight": 1.0} -->

In Table 7 we show the performance, generalization, and robustness of RT-1 as we decrease the dataset size (% data) and the dataset diversity (% tasks). To separate the axes of dataset size and diversity, we create smaller datasets with the same task diversity by removing data from the tasks with the largest data, capping the number of examples per task at 200 (resulting in 51% of the data), 100 (37% of the data), and 50 (22.5% of the data). To create a narrow dataset, we remove the tasks with the least data, thus keeping 97% of the overall data but only 75% of the tasks. As we decrease dataset size, we see a general trend of decreasing performance and a steeper trend of decreasing generalization. As we make the dataset more narrow, we see much steeper performance reductions, particularly in terms of generalization. In fact, removing 25% of the tasks while keeping 97% of the data achieves an equivalent generalization performance to reducing the dataset size by as much as 49%. Our key takeaway is thus that data diversity is more essential than data quantity.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Conclusions, Limitations and Future Work", "weight": 1.0} -->

We presented Robotics Transformer 1, RT-1, a robot learning method that can effectively absorb large amounts of data and scales with data quantity and diversity. We trained RT-1 on a large dataset of demonstrations containing over 130k episodes collected over the course of 17 months with 13 robots. In our broad set of experiments, we demonstrated that our method that can perform over 700 instructions at 97% success rate and effectively generalize to new tasks, objects and environments better than previously published baselines. We also demonstrated that RT-1 can successfully absorb heterogeneous data from simulation and other robot morphologies without sacrificing original-tasks performance and while improving generalization to new scenarios. Lastly, we showed how this level of performance and generalization allowed us to execute very long-horizon tasks in the SayCan framework, with as many as 50 steps.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Conclusions, Limitations and Future Work", "weight": 1.0} -->

While RT-1 presents a promising step towards large-scale robot learning with an data-absorbent model, it comes with a number of limitations. First, it is an imitation learning method, which inherits the challenges of that class of approaches such as the fact that it may not be able to surpass the performance of the demonstrators. Second, the generalization to new instructions is limited to the combinations of previously seen concepts and RT-1 is not yet able to generalize to a completely new motion that has not been seen before. Lastly, our method is presented on a large but not very dexterous set of manipulation tasks. We plan to continue extending the set of instructions that RT-1 enables and generalizes to to address this challenge.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Conclusions, Limitations and Future Work", "weight": 1.0} -->

As we explore future directions for this work, we hope to scale the number of robot skills faster by developing methods that allow non-experts to train the robot via directed data collection and model prompting. While the current version of RT-1 is fairly robust especially to distractor objects, its robustness to backgrounds and environments could be further improved by greatly increasing the environment diversity. We also hope to improve the reaction speeds and context retention of RT-1 through scalable attention and memory.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Conclusions, Limitations and Future Work", "weight": 1.0} -->

To allow the research community to build on top of this work, we have open-sourced the code for RT-1 ^44^4 which we hope will provide researchers with a valuable resource for future research for scaling up robot learning.
