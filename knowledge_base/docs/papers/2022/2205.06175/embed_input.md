<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Generalist Agent

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Inspired by progress in large-scale language modeling, we apply a similar approach towards building a single generalist agent beyond the realm of text outputs. The agent, which we refer to as Gato, works as a multi-modal, multi-task, multi-embodiment generalist policy. The same network with the same weights can play Atari, caption images, chat, stack blocks with a real robot arm and much more, deciding based on its context whether to output text, joint torques, button presses, or other tokens. In this report we describe the model and the data, and document the current capabilities of Gato.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

There are significant benefits to using a single neural sequence model across all tasks. It reduces the need for hand crafting policy models with appropriate inductive biases for each domain. It increases the amount and diversity of training data since the sequence model can ingest any data that can be serialized into a flat sequence. Furthermore, its performance continues to improve even at the frontier of data, compute and model scale. Historically, generic models that are better at leveraging computation have also tended to overtake more specialized domain-specific approaches, eventually.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we describe the current iteration of a general-purpose agent which we call Gato, instantiated as a single, large, transformer sequence model. With a single set of weights, Gato can engage in dialogue, caption images, stack blocks with a real robot arm, outperform humans at playing Atari games, navigate in simulated 3D environments, follow instructions, and more.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

While no agent can be expected to excel in all imaginable control tasks, especially those far outside of its training distribution, we here test the hypothesis that training an agent which is generally capable on a *large number* of tasks is possible; and that this general agent can be adapted with little extra data to succeed at an even larger number of tasks. We hypothesize that such an agent can be obtained through scaling data, compute and model parameters, continually broadening the training distribution while maintaining performance, towards covering any task, behavior and embodiment of interest. In this setting, natural language can act as a common grounding across otherwise incompatible embodiments, unlocking combinatorial generalization to new behaviors.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We focus our training at the operating point of model scale that allows real-time control of real-world robots, currently around 1.2B parameters in the case of Gato. As hardware and model architectures improve, this operating point will naturally increase the feasible model size, pushing generalist models higher up the scaling law curve. For simplicity Gato was trained offline in a purely supervised manner; however, in principle, there is no reason it could not also be trained with either offline or online reinforcement learning (RL).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Model", "weight": 1.0} -->

The guiding design principle of Gato is to train on the widest variety of relevant data possible, including diverse modalities such as images, text, proprioception, joint torques, button presses, and other discrete and continuous observations and actions. To enable processing this multi-modal data, we serialize all data into a flat sequence of tokens. In this representation, Gato can be trained and sampled from akin to a standard large-scale language model. During deployment, sampled tokens are assembled into dialogue responses, captions, button presses, or other actions based on the context. In the following subsections, we describe Gato's tokenization, network architecture, loss function, and deployment.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Tokenization", "weight": 1.0} -->

There are infinite possible ways to transform data into tokens, including directly using the raw underlying byte stream. Below we report the tokenization scheme we found to produce the best results for Gato at the current scale using contemporary hardware and model architectures.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Tokenization", "weight": 1.0} -->

Text is encoded via SentencePiece with 32000 subwords into the integer range \[0, 32000).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Tokenization", "weight": 1.0} -->

Images are first transformed into sequences of non-overlapping $16 \times 16$ patches in raster order, as done in ViT. Each pixel in the image patches is then normalized between $\lbrack{- 1},1\rbrack$ and divided by the square-root of the patch size (i.e. $\sqrt{16} = 4$).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Tokenization", "weight": 1.0} -->

Discrete values, e.g. Atari button presses, are flattened into sequences of integers in row-major order. The tokenized result is a sequence of integers within the range of $\lbrack 0,1024)$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Tokenization", "weight": 1.0} -->

Continuous values, e.g. proprioceptive inputs or joint torques, are first flattened into sequences of floating point values in row-major order. The values are mu-law encoded to the range $\lbrack{- 1},1\rbrack$ if not already there (see Figure 14 for details), then discretized to 1024 uniform bins. The discrete integers are then shifted to the range of $\lbrack 32000,33024)$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Tokenization", "weight": 1.0} -->

After converting data into tokens, we use the following canonical sequence ordering.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Tokenization", "weight": 1.0} -->

Text tokens in the same order as the raw input text.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Tokenization", "weight": 1.0} -->

Image patch tokens in raster order.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Tokenization", "weight": 1.0} -->

Nested structures in lexicographical order by key.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Tokenization", "weight": 1.0} -->

Agent timesteps as observation tokens followed by a separator, then action tokens.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Tokenization", "weight": 1.0} -->

Agent episodes as timesteps in time order.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Tokenization", "weight": 1.0} -->

Further details on tokenizing agent data are presented in the supplementary material (Section B).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Embedding input tokens and setting output targets", "weight": 1.0} -->

After tokenization and sequencing, we apply a parameterized embedding function $f{(\cdot;\theta_{e})}$ to each token (i.e. it is applied to both observations and actions) to produce the final model input. To enable efficient learning from our multi-modal input sequence $s_{1:L}$ the embedding function performs different operations depending on the modality the token stems: Tokens belonging to text, discrete- or continuous-valued observations or actions for any time-step are embedded via a lookup table into a learned vector embedding space. Learnable position encodings are added for all tokens based on their local token position within their corresponding time-step.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Embedding input tokens and setting output targets", "weight": 1.0} -->

Tokens belonging to image patches for any time-step are embedded using a single ResNet block to obtain a vector per patch. For image patch token embeddings, we also add a learnable within-image position encoding vector.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Embedding input tokens and setting output targets", "weight": 1.0} -->

We refer to appendix Section C.3 for full details on the embedding function.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Embedding input tokens and setting output targets", "weight": 1.0} -->

As we model the data autoregressively, each token is potentially also a target label given the previous tokens. Text tokens, discrete and continuous values, and actions can be directly set as targets after tokenization. Image tokens and agent nontextual observations are not currently predicted in Gato, although that may be an interesting direction for future work. Targets for these non-predicted tokens are set to an unused value and their contribution to the loss is masked out.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Training", "weight": 1.0} -->

Given a sequence of tokens $s_{1:L}$ and parameters $\theta$, we model the data using the chain rule of probability: Let $b$ index a training batch of sequences $\mathcal{B}$. We define a masking function $m$ such that ${m{(b,l)}} = 1$ if the token at index $l$ is either from text or from the logged action of an agent, and $0$ otherwise. The training loss for a batch $\mathcal{B}$ can then be written as As described above, Gato's network architecture has two main components: the parameterized embedding function which transforms tokens to token embeddings, and the sequence model which outputs a distribution over the next discrete token. While any general sequence model can work for next token prediction, we chose a transformer for simplicity and scalability. Gato uses a 1.2B parameter decoder-only transformer with 24 layers, an embedding size of 2048, and a post-attention feedforward hidden size of 8196 (more details in Section C.1).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Training", "weight": 1.0} -->

Because distinct tasks within a domain can share identical embodiments, observation formats and action specifications, the model sometimes needs further context to disambiguate tasks. Rather than providing e.g. one-hot task identifiers, we instead take inspiration from and use prompt conditioning. During training, for $25\%$ of the sequences in each batch, a prompt sequence is prepended, coming from an episode generated by the same source agent on the same task. Half of the prompt sequences are from the end of the episode, acting as a form of goal conditioning for many domains; and the other half are uniformly sampled from the episode. During evaluation, the agent can be prompted using a successful demonstration of the desired task, which we do by default in all control results that we present here.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Training", "weight": 1.0} -->

Training of the model is performed on a 16x16 TPU v3 slice for 1M steps with batch size 512 and token sequence length $L = 1024$, which takes about 4 days. Architecture details can be found in Section C. Because agent episodes and documents can easily contain many more tokens than fit into context, we randomly sample subsequences of $L$ tokens from the available episodes. Each batch mixes subsequences approximately uniformly over domains (e.g. Atari, MassiveWeb, etc.), with some manual upweighting of larger and higher quality datasets (see Table 1 in Section 3 for details).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Deployment", "weight": 1.0} -->

Deploying Gato as a policy is illustrated in Figure 3. First a prompt, such as a demonstration, is tokenized, forming the initial sequence. By default, we take the first 1024 tokens of the demonstration. Next the environment yields the first observation which is tokenized and appended to the sequence. Gato samples the action vector autoregressively one token at a time. Once all tokens comprising the action vector have been sampled (determined by the action specification of the environment), the action is decoded by inverting the tokenization procedure described in Section 2.1. This action is sent to the environment which steps and yields a new observation. The procedure repeats. The model always sees all previous observations and actions in its context window of 1024 tokens. We found it beneficial to use transformer XL memory during deployment, although it was not used during training.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Datasets", "weight": 1.0} -->

Gato is trained on a large number of datasets comprising agent experience in both simulated and real world environments, as well as a variety of natural language and image datasets. The datasets we use and their attributes are listed in Table 1. The approximate number of tokens per control dataset is computed assuming the tokenization mechanism described in Section 2.1.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Datasets", "weight": 1.0} -->

ALE Atari Extended DM Control Suite Pixels DM Control Suite Random Small DM Control Suite Random Large RGB Stacking simulator RGB Stacking real robot Vision / language dataset Table 1: Datasets. Left: Control datasets used to train Gato. Right: Vision & language datasets. Sample weight means the proportion of each dataset, on average, in the training sequence batches.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Simulated control tasks", "weight": 1.0} -->

Our control tasks consist of datasets generated by specialist SoTA or near-SoTA reinforcement learning agents trained on a variety of different environments. For each environment we record a subset of the experience the agent generates (states, actions, and rewards) while it is training.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Simulated control tasks", "weight": 1.0} -->

The simulated environments include Meta-World introduced to benchmark meta-reinforcement learning and multi-task learning, Sokoban proposed as a planning problem, BabyAI for language instruction following in grid-worlds, the DM Control Suite for continuous control, as well as DM Lab designed to teach agents navigation and 3D vision from raw pixels with an egocentric viewpoint. We also use the Arcade Learning Environment with classic Atari games (we use two sets of games that we call ALE Atari and ALE Atari Extended, see Section F.1 for details). We as well include the Procgen Benchmark and Modular RL. We also include four tasks using a simulated Kinova Jaco arm from DM Manipulation Playground, as introduced in Zolna et al.. Section F includes a more in-depth description of these control tasks, along with what RL agent was used to generate the data.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Simulated control tasks", "weight": 1.0} -->

We found it effective to train on a filtered set of episodes with returns at least 80% of the expert return for the task. The expert return measures the maximum sustained performance that the expert agent can achieve. We define it as the maximum over the set of all windowed average returns calculated over all the collected episodes for a task: where $N$ it the total number of collected episodes for the task, $W$ is the window size, and $R_{i}$ is the total return for episode $i$. To obtain accurate estimates, in practice, we set $W$ to be $10\%$ of the total data amount or a minimum of 1000 episodes (i.e. $W = {\min{(1000,{0.1 \times N})}}$).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Vision and language", "weight": 1.0} -->

Gato is trained on MassiveText, a collection of large English-language text datasets from multiple sources: web pages, books, news articles, and code.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Vision and language", "weight": 1.0} -->

We also included several vision-language datasets in Gato's training. ALIGN consists of 1.8B images and their alternative text (alt-text) annotations. LTIP (Long Text & Image Pairs), consists of 312 million images with captions. Conceptual captions and COCO captions are captioning datasets with 3.3M and 120k image-text pairs respectively. The MultiModal MassiveWeb (M3W) dataset includes 43M webpages where both text and images were extracted. We also included visual question-answering datasets. In particular OKVQA and VQAv2 with 9K and 443K triplets of images, questions, and answers. To form a training episode from these, we sample five (image, text) pairs, tokenize them, concatenate, and then pad or randomly crop to the required training sequence length.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Robotics - RGB Stacking Benchmark (real and sim)", "weight": 1.0} -->

As a testbed for taking physical actions in the real world, we chose the robotic block stacking environment introduced by Lee et al.. The environment consists of a Sawyer robot arm with 3-DoF cartesian velocity control, an additional DoF for velocity, and a discrete gripper action. The robot's workspace contains three plastic blocks colored red, green and blue with varying shapes. The available observations include two 128 $\times$ 128 camera images, robot arm and gripper joint angles as well as the robot's end-effector pose. Notably, ground truth state information for the three objects in the basket is not observed by the agent. Episodes have a fixed length of 400 timesteps at 20 Hz for a total of 20 seconds, and at the end of an episode block positions are randomly re-positioned within the workspace. The robot in action is shown in Figure 4 ‣ 3 Datasets ‣ A Generalist Agent").

<!-- chunk {"id": "body-0036", "role": "body", "section": "Robotics - RGB Stacking Benchmark (real and sim)", "weight": 1.0} -->

There are two challenges in this benchmark: *Skill Mastery* (where the agent is provided data from the 5 test object triplets it is later tested on) and *Skill Generalization* (where data can only be obtained from a set of training objects that excludes the 5 test sets).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Robotics - RGB Stacking Benchmark (real and sim)", "weight": 1.0} -->

We used several sources of training data for these tasks. In Skill Generalization, for both simulation and real, we use data collected by the best generalist sim2real agent from Lee et al.. We collected data only when interacting with the designated RGB-stacking *training objects* (this amounts to a total of 387k successful trajectories in simulation and 15k trajectories in real). For Skill Mastery we used data from the best per group experts from Lee et al. in simulation and from the best sim2real policy on the real robot (amounting to 219k trajectories in total). Note that this data is only included for specific Skill Mastery experiments in Section 5.4.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Capabilities of the generalist agent", "weight": 1.0} -->

In this section, we summarize the performance of Gato when trained on the above described data. That is, all results across all tasks are derived from a single pretrained model with a single set of weights. Results with fine-tuning will be presented in Section 5.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Simulated control tasks", "weight": 1.0} -->

We report performance as a percentage, where $100\%$ corresponds to the per-task expert and $0\%$ to a random policy. For each simulated control task we trained our model, we roll out the Gato policy on the corresponding environment 50 times and average the defined scores. As shown in Figure 5, Gato performs over 450 out of 604 tasks at over a $50\%$ expert score threshold.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Simulated control tasks", "weight": 1.0} -->

In ALE Atari Gato achieves the average human (or better) scores for 23 Atari games^11^1The full list of games: Assault, Atlantis, Bank heist, Battle zone, Bowling, Crazy climber, Defender, Fishing derby, Gopher, Hero, Ice hockey, Jamesbond, Kangaroo, Kung fu master, Name this game, Pong, Road runner, Robotank, Tennis, Time pilot, Up n down, Wizard of wor, Zaxxon., achieving over twice human score for 11 games. While the single-task online RL agents which generated the data still outperform Gato, this may be overcome by adding capacity or using offline RL training rather than purely supervised (see Section 5.5 where we present a specialist single domain ALE Atari agent achieving better than human scores for 44 games).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Simulated control tasks", "weight": 1.0} -->

On BabyAI Gato achieves over 80% of expert score for nearly all levels^22^2The only three tasks below 80% success rate are GoToImpUnlock (59%), Unlock (74%), and BossLevel (75%).. For the most difficult task, called BossLevel, Gato scores 75%. The two other published baselines we could find, BabyAI 1.0 and BabyAI 1.1, scored 77% and 90%, respectively, having trained on this single task alone using a million demonstrations.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Simulated control tasks", "weight": 1.0} -->

On Meta-World Gato achieves more than 50% for all 44 out of 45 tasks that we trained, over 80% for 35 tasks, and over 90% for 3 tasks. On canonical DM Control Suite, Gato achieves better than 50% of the expert score on 21 out of 30 tasks from state, and more than 80% for 18 tasks.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Robotics", "weight": 1.0} -->

First person teleoperation enables the collection of expert demonstrations. However, such demonstrations are slow and costly to collect. Data-efficient behavior cloning methods are therefore desirable for training a generalist robot manipulator and offline pretraining is thus a well-motivated area of research. To that end, we evaluated Gato on the established RGB Stacking benchmark for robotics.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Skill Generalization Performance", "weight": 1.0} -->

The Skill Generalization challenge from the RGB Stacking robotics benchmark tests the agent's ability to stack objects of previously unseen shapes. The agent is trained on a dataset consisting of episodes of the robot stacking objects with a variety of different shapes. Five triplets of object shapes are, however, not included in the training data and serve as test triplets. We evaluated the trained generalist for 200 episodes per test triplet on the real robot. Table 2 shows that our generalist agent's success rate on each test triplet is comparable to the single task BC-IMP (filtered BC) baseline in Lee et al..

<!-- chunk {"id": "body-0045", "role": "body", "section": "Text samples", "weight": 1.0} -->

The model demonstrates rudimentary dialogue and image captioning capabilities. Figure 7 contains a representative sample of Gato's image captioning performance. Figure 7 shows some hand-picked examples of plain text dialogue exchange.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Scaling Laws Analysis", "weight": 1.0} -->

In Figure 8, we analyze the aggregate in-distribution performance of the pretrained model as a function of the number of parameters in order to get insight into how performance could improve with increased model capacity. We evaluated 3 different model sizes (measured in parameter count): a 79M model, a 364M model, and a 1.18B model (Gato). We refer to Section C for details on the three model architectures.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Scaling Laws Analysis", "weight": 1.0} -->

Here, for all three model sizes we plot the normalized return as training progresses. To get this single value, for each task we calculate the performance of the model as a percentage of expert score (the same as done in Section 4.1). Then for each domain listed in Table 1 we average the percentage scores across all tasks for that domain. Finally, we mean-aggregate the percentage scores across all domains. We can see that for an equivalent token count, there is a significant performance improvement with increased scale.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Out of distribution tasks", "weight": 1.0} -->

In this section we want to answer the following question: *Can our agent be used to solve a completely new task efficiently?* For this reason, we held-out all data for four tasks from our pre-training set: cartpole.swingup (DM Control Suite domain), assembly-v2 (Meta-World domain), order_of_apples_forage_simple (DM Lab domain), and boxing (ALE Atari domain). These four tasks will serve as testbeds for evaluating the out-of-distribution capabilities of Gato.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Out of distribution tasks", "weight": 1.0} -->

Ideally, the agent could potentially learn to adapt to a new task via conditioning on a prompt including demonstrations of desired behaviour. However, due to accelerator memory constraints and the extremely long sequence lengths of tokenized demonstrations, the maximum context length possible does not allow the agent to attend over an informative-enough context. Therefore, to adapt the agent to new tasks or behaviours, we choose to fine-tune the agent's parameters on a limited number of demonstrations of a single task, and then evaluate the fine-tuned model's performance in the environment. Fine-tuning is very similar to pretraining with minor changes, such as different learning rate schedule; see Section E for details.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Out of distribution tasks", "weight": 1.0} -->

We want to measure how choice of data used during pretraining influences post-fine-tuning performance. To this end, we compare Gato (trained on all data) to variants trained on ablated datasets: A model pretrained only on data from the same domain as the task to be fine-tuned, same domain only data.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Out of distribution tasks", "weight": 1.0} -->

A model pretrained only on non-control data, no control data.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Out of distribution tasks", "weight": 1.0} -->

A model fine-tuned from scratch, i.e. no pretraining at all, scratch.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Out of distribution tasks", "weight": 1.0} -->

Considering as all these experiments require training a new model from scratch and then also fine-tuning, we present results using the less compute-intensive 364M parameter architecture described in Section 5.1. Results are shown in Figure 9.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Out of distribution tasks", "weight": 1.0} -->

Fine-tuning performance on both cartpole.swingup and assembly-v2 tasks, both of which do not require image processing, present similar trends. Pretraining on all the datasets yields the best results, followed by pretraining on the same domain only. This difference is smaller for assembly-v2 but consistent for all few shot datasets. For these non-image-based environments, we see either no benefit (cartpole.swingup) or even negative transfer (assembly-v2) when pretraining on no control datasets, which only contain images and text data.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Out of distribution tasks", "weight": 1.0} -->

Results for DM Lab order_of_apples_forage_simple are slightly different. Pretraining on DM Lab data only is already enough to approach the maximum reward of 19 and hence there is no observable benefit of adding data from different environments. What is different when compared to previously analysed no-vision environments is that pretraining on no control data helps, which can be possibly explained by the fact that agents in the DM Lab environment are fed images which, despite being simulated, are natural looking. Therefore, transfer from image captioning or visual grounded question answering tasks is possible.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Out of distribution tasks", "weight": 1.0} -->

We were not able to observe any benefit from pretraining on boxing. The randomly initialized model seems to work better than any of the pretrained variants considered. We hypothesise that this is caused by the game's input images being visually very distinct from the other data, suggesting transfer is difficult. We discuss this Atari challenge further in our related work section.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Fine-tuning on Robotic Stacking Tasks", "weight": 1.0} -->

Section 4.2 demonstrates that the base Gato capable of a diverse array of tasks can perform competitively on the RGB Stacking Skill Generalization benchmark. In this section, we would like to answer the following question: *How does our agent improve on robotics tasks when allowed to fine-tune similarly to how we fine-tune on new tasks in Section 5.2?* We consider different model sizes and analyse the impact of pretraining datasets on the Skill Generalization benchmark, as well as a novel out of distribution task. Further analysis of fine-tuning with dataset ablations is in Appendix I.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Skill Generalization", "weight": 1.0} -->

First, we would like to show that fine-tuning on object-specific data, similarly to what was done by Lee et al., is beneficial. Therefore, we fine-tuned Gato separately on five subsets of demonstrations from the test dataset. Each subset was obtained by random partitioning of a test dataset consisting of demonstrations gathered by a generalist sim-to-real agent stacking real test objects. We consider this setting, which is comparable to the fine-tuning baselines on RGB stacking tasks; and use the 5k dataset that their behavior cloning 5k results are obtained. To best match their experiments, we change our return filtering scheme during training: instead of using only successful stacks, we condition on the normalized return of the episode.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Fine-tuning and Model Size", "weight": 1.0} -->

To better understand the benefit of large models for few-shot adaptation in robotics domains, we conducted an ablation on model parameter size. This section focuses on in-simulation evaluation. Figure 10 compares the full 1.18B parameter Gato with the smaller 364M and 79M parameter variants for varying amounts of fine-tuning data. Although the 364M model overfits on one episode, causing performance to drop, there is a clear trend towards better adaptation with fewer episodes as the number of parameters is scaled up. The 79M model performs clearly worse than its bigger counterparts. The results suggest that the model's greater capacity allows the model to use representations learned from the diverse training data at test time.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Adaptation to Perceptual Variations", "weight": 1.0} -->

While the Skill Generalization task is an effective benchmark for motor Skill Generalization to shape variations, it does not test the agent's ability to adapt to perceptual variations and permutations in the objective specification. To further evaluate Gato's generalization capabilities, we devised a new task in the RGB stacking benchmark where the goal is to stack the blue object on the green object, for test triplet 1 (see Figure 11). First, we used a 3D mouse to collect 500 demonstrations of this task on the real robot, for a total of 2 hours and 45 minutes of demonstration data, and fine-tuned Gato on these episodes. Notably, all of the simulated and real robotics data in the pretraining set shows the robot successfully stacking the red object on the blue object, and the data does not include the object shapes in the test set. We found that additionally adding simulated demonstrations of the stack blue on green task to the fine-tuning dataset improved performance, and 10% was an ideal sampling ratio for this data.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Adaptation to Perceptual Variations", "weight": 1.0} -->

We achieved a final 60% success rate after evaluating fine-tuned Gato on the real robot, while a BC baseline trained from scratch on the blue-on-green data achieved only 0.5% success (1/200 episodes). Qualitatively, the BC baseline would consistently move towards the blue object and occasionally pick it up and place it on top of the green object, but a full, stable stack was almost never achieved.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Robotics: Skill Mastery", "weight": 1.0} -->

Similarly to the Skill Generalization challenge discussed in Section 4.2, the Skill Mastery challenge consists in training a robotic arm to stack blocks of different shapes. However, the Skill Mastery allows the agent to train on data involving the object shapes used for evaluation, i.e. the *test* set in Skill Generalization becomes a part of the Skill Mastery *training* set. Thus, this challenge serves to measure Gato's performance on in-distribution tasks (possibly with initial conditions not seen in the training demonstrations). Our Skill Mastery results use an earlier version of the Gato architecture described in Appendix H, with no fine-tuning.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Robotics: Skill Mastery", "weight": 1.0} -->

Table 3 compares the group-wise success percentage and the average success across object groups for Gato and the established BC-IMP baseline. Gato exceeds or closely matches BC-IMP's performance on all but one training triplet.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Specialist single-domain multi-task agents", "weight": 1.0} -->

In this section we show results obtained with two specialist (rather than generalist) agents. Both of them were trained on data from a single domain only and rolled out 500 times for each training task without any per-task fine-tuning.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Meta-World", "weight": 1.0} -->

The first agent uses the smallest architecture introduced in Section 5.1, i.e. 79M parameters, and is trained on all 50 Meta-World tasks. While Gato has access to the state of the MuJoCo physics engine and unlimited task seeds, the agent presented here has no access to any extra features or tasks and uses the canonical API as. This experiment is to show that the architecture proposed in our paper can be used to obtain state-of-the-art agents also at small scale. The training procedure was to train single-task MPO experts on each of the MT-50 tasks individually, recording the trajectories produced while training. This experience is then combined, or distilled, into a single agent, which achieves 96.6% success rate averaged over all 50 tasks. To the best of our knowledge this agent is the first one to accomplish nearly 100% average success rate simultaneously (multi-task) for this benchmark. See Table 7 in the supplementary material (Section K) for the full list of tasks and corresponding success rates of our agent.

<!-- chunk {"id": "body-0066", "role": "body", "section": "ALE Atari", "weight": 1.0} -->

We also trained a specialist agent on all 51 ALE Atari tasks. As the Atari domain is much more challenging than Meta-World, we used the Gato architecture with 1.18B parameters.

<!-- chunk {"id": "body-0067", "role": "body", "section": "ALE Atari", "weight": 1.0} -->

The resulting agent performs better than the average human for 44 games (see Section 4.1 for details on our evaluation and scoring). We want to note that the performance of online experts used to generate training data for the other 7 games were also below the average human. Hence, the specialist Atari agent achieved better than human performance for all games where data contained super-human episodes.

<!-- chunk {"id": "body-0068", "role": "body", "section": "ALE Atari", "weight": 1.0} -->

The specialist Atari agent outperforms our generalist agent Gato, which achieved super-human performance on 23 games. It suggests that scaling Gato may result in even better performance. We, however, purposely restricted Gato's size such that it can be run in real-time on the real robot.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Attention Analysis", "weight": 1.0} -->

We rendered the transformer attention weights over the image observations for various tasks, to gain a qualitative sense of how Gato attends to different regions of the image across tasks (see Figure 12). Further details and visualizations for more tasks can be found in Appendix J. These visualizations clearly show that attention tracks the task-relevant objects and regions.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Embedding Visualization", "weight": 1.0} -->

To understand how Gato encodes differently information per task, we visualized per-task embeddings.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Embedding Visualization", "weight": 1.0} -->

We analysed 11 tasks. For each task, we randomly sample 100 episodes and tokenize each of them. Then, from each episode we take a subsequence of 128 tokens, compute their embeddings (at layer 12, which is half the total depth of the transformer layers) and average them over the sequence. The averaged embeddings for all tasks are used as input to PCA, which reduces their dimensionality to 50. Then, T-SNE is used to get the final 2D embeddings.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Broader Impact", "weight": 1.0} -->

Although generalist agents are still only an emerging area of research, their potential impact on society calls for a thorough interdisciplinary analysis of their risks and benefits. For the sake of transparency, we document the intended use cases of Gato in the model card in Appendix A. However, the tools for mitigating harms of generalist agents are relatively underdeveloped, and require further research before these agents are deployed.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Broader Impact", "weight": 1.0} -->

Since our generalist agent can act as a vision-language model, it inherits similar concerns as discussed. In addition, generalist agents can take actions in the the physical world; posing new challenges that may require novel mitigation strategies. For example, physical embodiment could lead to users anthropomorphizing the agent, leading to misplaced trust in the case of a malfunctioning system, or be exploitable by bad actors. Additionally, while cross-domain knowledge transfer is often a goal in ML research, it could create unexpected and undesired outcomes if certain behaviors (e.g. arcade game fighting) are transferred to the wrong context. The ethics and safety considerations of knowledge transfer may require substantial new research as generalist systems advance.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Broader Impact", "weight": 1.0} -->

Technical AGI safety may also become more challenging when considering generalist agents that operate in many embodiments. For this reason, preference learning, uncertainty modeling and value alignment are especially important for the design of human-compatible generalist agents. It may be possible to extend some of the value alignment approaches for language to generalist agents. However, even as technical solutions are developed for value alignment, generalist systems could still have negative societal impacts even with the intervention of well-intentioned designers, due to unforeseen circumstances or limited oversight. This limitation underscores the need for a careful design and a deployment process that incorporates multiple disciplines and viewpoints.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Broader Impact", "weight": 1.0} -->

Understanding how the models process information, and any emergent capabilities, requires significant experimentation. External retrieval has been shown to improve both interpretability and performance, and hence should be considered in future designs of generalist agents.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Broader Impact", "weight": 1.0} -->

Although still at the proof-of-concept stage, the recent progress in generalist models suggests that safety researchers, ethicists, and most importantly, the general public, should consider their risks and benefits. We are not currently deploying Gato to any users, and so anticipate no immediate societal impact. However, given their potential impact, generalist models should be developed thoughtfully and deployed in a way that promotes the health and vitality of humanity.

<!-- chunk {"id": "body-0077", "role": "body", "section": "RL data collection", "weight": 1.0} -->

Gato is a data-driven approach, as it is derived from imitation learning. While natural language or image datasets are relatively easy to obtain from the web, a web-scale dataset for control tasks is not currently available. This may seem at first to be problematic, especially when scaling Gato to a higher number of parameters.

<!-- chunk {"id": "body-0078", "role": "body", "section": "RL data collection", "weight": 1.0} -->

That being said, there has already been extensive investigation into this issue. Offline RL aims at leveraging existing control datasets, and its increasing popularity has already resulted in the availability of more diverse and larger datasets. Richer environments and simulations are being built (e.g. Metaverse), and increasing numbers of users already interact with them among thousands of already deployed online games (e.g. there exists a large dataset of Starcraft 2 games). Real-life data has also been already stored for ML research purposes; for example, data for training self-driving cars is acquired from recording human driver data. Finally, while Gato uses data consisting of both observations and corresponding actions, the possibility of using large scale observation-only data to enhance agents has been already studied. Thanks to online video sharing and streaming platforms such as Youtube and Twitch, observation-only datasets are not significantly more difficult to collect than natural language datasets, motivating a future research direction to extend Gato to learn from web data.

<!-- chunk {"id": "body-0079", "role": "body", "section": "RL data collection", "weight": 1.0} -->

While the previous paragraph focuses on alleviating drawbacks of data collection from RL agents, it is important to note that this approach presents a different set of tradeoffs compared to scraping web data and can be actually more practical in some situations. Once the simulation is set up and near SOTA agent trained, it can be used to generate massive amounts of high quality data. That is in contrast to the quality of web data which is notorious for its low quality.

<!-- chunk {"id": "body-0080", "role": "body", "section": "RL data collection", "weight": 1.0} -->

In short, we believe that acquiring suitable data is another research question on its own, and this is an active area of research with growing momentum and importance.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Prompt and short context", "weight": 1.0} -->

Gato is prompted with an expert demonstration, which aids the agent to output actions corresponding to the given task. This is particularly useful since there is otherwise no task identifier available to the agent (that is in contrast to many multi-task RL settings). Gato infers the relevant task from the observations and actions in the prompt.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Prompt and short context", "weight": 1.0} -->

However, the context length of our agent is limited to 1024 tokens which translates to the agent sometimes attending to only a few environment timesteps in total. This is especially the case for environments with image observations, where depending on the resolution each observation can result in more than one hundred tokens each. Hence for certain environments only a short chunk of a demonstration episode fits in the transformer memory.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Prompt and short context", "weight": 1.0} -->

Due to this limited prompt context, preliminary experiments with different prompt structures resulted in very similar performance. Similarly, early evaluations of the model using prompt-based in-context learning on new environments did not show a significant performance improvement compared to prompt-less evaluation in the same setting.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Prompt and short context", "weight": 1.0} -->

Context-length is therefore a current limitation of our architecture, mainly due to the quadratic scaling of self-attention. Many recently proposed architectures enable a longer context at greater efficiency and these innovations could potentially improve our agent performance. We hope to explore these architectures in future work.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Transformer sequence models are effective as multi-task multi-embodiment policies, including for real-world text, vision and robotics tasks. They show promise as well in few-shot out-of-distribution task learning. In the future, such models could be used as a default starting point via prompting or fine-tuning to learn new behaviors, rather than training from scratch.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Given scaling law trends, the performance across all tasks including dialogue will increase with scale in parameters, data and compute. Better hardware and network architectures will allow training bigger models while maintaining real-time robot control capability. By scaling up and iterating on this same basic approach, we can build a useful general-purpose agent.
