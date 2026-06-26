<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

RL Unplugged: A Suite of Benchmarks for Offline Reinforcement Learning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Offline methods for reinforcement learning have a potential to help bridge the gap between reinforcement learning research and real-world applications. They make it possible to learn policies from offline datasets, thus overcoming concerns associated with online data collection in the real-world, including cost, safety, or ethical concerns. In this paper, we propose a benchmark called RL Unplugged to evaluate and compare offline RL methods. RL Unplugged includes data from a diverse range of domains including games (e.g., Atari benchmark) and simulated motor control problems (e.g., DM Control Suite). The datasets include domains that are partially or fully observable, use continuous or discrete actions, and have stochastic vs. deterministic dynamics. We propose detailed evaluation protocols for each domain in RL Unplugged and provide an extensive analysis of supervised learning and offline RL methods using these protocols. We will release data for all our tasks and open-source all algorithms presented in this paper.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We hope that our suite of benchmarks will increase the reproducibility of experiments and make it possible to study challenging tasks with a limited computational budget, thus making RL research both more systematic and more accessible across the community. Moving forward, we view RL Unplugged as a living benchmark suite that will evolve and grow with datasets contributed by the research community and ourselves. Our project page is available on

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement Learning (RL) has seen important breakthroughs, including learning directly from raw sensory streams, solving long-horizon reasoning problems such as Go, StarCraft II, DOTA, and learning motor control for high-dimensional simulated robots. However, many of these successes rely heavily on repeated online interactions of an agent with an environment. Despite its success in simulation, the uptake of RL for real-world applications has been limited. Power plants, robots, healthcare systems, or self-driving cars are expensive to run and inappropriate controls can have dangerous consequences. They are not easily compatible with the crucial idea of exploration in RL and the data requirements of online RL algorithms. Nevertheless, most real-world systems produce large amounts of data as part of their normal operation.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

There is a resurgence of interest in offline methods for reinforcement learning,^11^1Sometimes referred to as 'Batch RL,' but in this paper, we use 'Offline RL'. that can learn new policies from logged data, without any further interactions with the environment due to its potential real-world impact. Offline RL can help pretrain an RL agent using existing datasets, empirically evaluate RL algorithms based on their ability to exploit a fixed dataset of interactions, and bridge the gap between academic interest in RL and real-world applications.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Offline RL methods have shown promising results on well-known benchmark domains. However, non-standardized evaluation protocols, differing datasets and lack of baselines make algorithmic comparisons difficult. Important properties of potential real-world application domains such as partial observability, high-dimensional sensory streams such as images, diverse action spaces, exploration problems, non-stationarity, and stochasticity are under-represented in the current offline RL literature. This makes it difficult to assess the practical applicability of offline RL algorithms.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The reproducibility crisis of RL is very evident in offline RL. Several works have highlighted these reproducibility challenges in their papers: Peng et al. discusses the difficulties of implementing the MPO algorithm, Fujimoto et al. mentions omitting results for SPIBB-DQN due to the complexity of implementation. On our part, we have had difficulty implementing SAC. We have also found it hard to scale BRAC and BCQ. This does not indicate these algorithms do not work. Only that implementation details matter, comparing algorithms and ensuring their reproducibility is hard. The intention of this paper is to help in solving this problem by putting forward common benchmarks, datasets, evaluation protocols, and code.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The availability of large datasets with strong benchmarks has been the main factor for the success of machine learning in many domains. Examples of this include vision challenges, such as ImageNet and COCO, and game challenges, where simulators produce hundreds of years of experience for online RL agents such as AlphaGo and the OpenAI Five. In contrast, lack of datasets with clear benchmarks hinders the similar progress in RL for real-world applications. This paper aims to correct this such as to facilitate collaborative research and measurable progress in the field.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

To this end, we introduce a novel collection of task domains and associated datasets together with a clear evaluation protocol. We include widely-used domains such as the DM Control Suite and Atari 2600 games, but also domains that are still challenging for strong online RL algorithms such as real-world RL (RWRL) suite tasks and DM Locomotion tasks. By standardizing the environments, datasets, and evaluation protocols, we hope to make research in offline RL more reproducible and accessible. We call our suite of benchmarks "RL Unplugged", because offline RL methods can use it without any actors interacting with the environment.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper offers four main contributions: (i) a unified API for datasets (ii) a varied set of environments (iii) clear evaluation protocols for offline RL research, and (iv) reference performance baselines. The datasets in RL Unplugged enable offline RL research on a variety of established online RL environments without having to deal with the exploration component of RL. In addition, we intend our evaluation protocols to make the benchmark more fair and robust to different hyperparameter choices compared to the traditional methods which rely on online policy selection. Moreover, releasing the datasets with a proper evaluation protocols and open-sourced code will also address the reproducibility issue in RL. We evaluate and analyze the results of several SOTA RL methods on each task domain in RL Unplugged. We also release our datasets in an easy-to-use unified API that makes the data access easy and efficient with popular machine learning frameworks.

<!-- chunk {"id": "body-0011", "role": "body", "section": "RL Unplugged", "weight": 1.0} -->

The RL Unplugged suite is designed around the following considerations: to facilitate ease of use, we provide the datasets with a unified API which makes it easy for the practitioner to work with all data in the suite once a general pipeline has been established. We further provide a number of baselines including state-of-the art algorithms compatible with our API.^22^2See our github project page for the details of our API.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Properties of RL Unplugged", "weight": 1.0} -->

Many real-world RL problems require algorithmic solutions that are general and can demonstrate robust performance on a diverse set of challenges. Our benchmark suite is designed to cover a range of properties to determine the difficulty of a learning problem and affect the solution strategy choice. In the initial release of RL Unplugged, we include a wide range of task domains, including Atari games and simulated robotics tasks. Despite the different nature of the environments used, we provide a unified API over the datasets. Each entry in any dataset consists of a tuple of state ($s_{t}$), action ($a_{t}$), reward ($r_{t}$), next state ($s_{t + 1}$), and the next action ($a_{t + 1}$). For sequence data, we also provide future states, actions, and rewards, which allows for training recurrent models for tasks requiring memory. We additionally store metadata such as episodic rewards and episode id. We chose the task domains to include tasks that vary along the following axes. In Figure 1, we give an overview of how each task domain maps to these axes.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Properties of RL Unplugged", "weight": 1.0} -->

Action space We include tasks with both discrete and continuous action spaces, and of varying action dimension with up to 56 dimensions in the initial release of RL Unplugged.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Properties of RL Unplugged", "weight": 1.0} -->

Observation space We include tasks that can be solved from the low-dimensional natural state space of the MDP (or hand-crafted features thereof), but also tasks where the observation space consists of high-dimensional images (e.g., Atari 2600). We include tasks where the observation is recorded via an external camera (third-person view), as well as tasks in which the camera is controlled by the learning agent (e.g. robots with egocentric vision).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Properties of RL Unplugged", "weight": 1.0} -->

Partial observability & need for memory We include tasks in which the feature vector is a complete representation of the state of the MDP, as well as tasks that require the agent to estimate the state by integrating information over horizons of different lengths.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Properties of RL Unplugged", "weight": 1.0} -->

Difficulty of exploration We include tasks that vary in terms of exploration difficulty for reasons such as dimension of the action space, sparseness of the reward, or horizon of the learning problem.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Properties of RL Unplugged", "weight": 1.0} -->

Real-world challenges To better reflect the difficulties encountered in real systems, we also include tasks from the Real-World RL Challenges, which include aspects such as action delays, stochastic transition dynamics, or non-stationarities.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Properties of RL Unplugged", "weight": 1.0} -->

The characteristics of the data is also an essential consideration, including the behavior policy used, data diversity, i.e., state and action coverage, and dataset size. RL Unplugged introduces datasets that cover those different axes. For example, on Atari 2600, we use large datasets generated across training of an off-policy agent, over multiple seeds. The resulting dataset has data from a large mixture of policies. In contrast, we use datasets from fixed sub-optimal policies for the RWRL suite.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Evaluation Protocols", "weight": 1.0} -->

In a strict offline setting, environment interactions are not allowed. This makes hyperparameter tuning, including determining when to stop a training procedure, difficult. This is because we cannot take policies obtained by different hyperparameters and run them in the environment to determine which ones receive higher reward (we call this procedure online policy selection).^33^3Sometimes referred to as online model selection, but we choose policy selection to avoid confusion with models of the environment as used in model based RL algorithms. Ideally, offline RL would evaluate policies obtained by different hyperparameters using only logged data, for example using offline policy evaluation (OPE) methods (we call this procedure offline policy selection). However, it is unclear whether current OPE methods scale well to difficult problems. In RL Unplugged we would like to evaluate offline RL performance in both settings.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Evaluation Protocols", "weight": 1.0} -->

Evaluation by online policy selection (see Figure 2 (left)) is widespread in the RL literature, where researchers usually evaluate different hyperparameter configurations in an online manner by interacting with the environment, and then report results for the best hyperparameters. This enables us to evaluate offline RL methods in isolation, which is useful. It is indicative of performance given perfect offline policy selection, or in settings where we can validate via online interactions. This score is important, because as offline policy selection methods improve, performance will approach this limit. But it has downsides. As discussed before, it is infeasible in many real-world settings, and as a result it gives an overly optimistic view of how useful offline RL methods are today. Lastly, it favors methods with more hyperparameters over more robust ones.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Evaluation Protocols", "weight": 1.0} -->

Evaluation by offline policy selection (see Figure 2 (right)) has been less popular, but is important as it is indicative of robustness to imperfect policy selection, which more closely reflects the current state of offline RL for real-world problems. However it has downsides too, namely that there are many design choices including what data to use for offline policy selection, whether to use value functions trained via offline RL or OPE algorithms, which OPE algorithm to choose, and the meta question of how to tune OPE hyperparameters. Since this topic is still under-explored, we prefer not to specify any of these choices. Instead, we invite the community to innovate to find which offline policy selection method works best.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Evaluation Protocols", "weight": 1.0} -->

Importantly, our benchmark allows for evaluation in both online and offline policy selection settings. For each task, we clearly specify if it is intended for online vs offline policy selection. For offline policy selection tasks, we use a naive approach which we will describe in Section 4. We expect future work on offline policy selection methods to improve over this naive baseline. If a combination of offline RL method and offline policy selection can achieve perfect performance across all tasks, we believe this will mark an important milestone for offline methods in real-world applications.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Tasks", "weight": 1.0} -->

For each task domain we give a description of the tasks included, indicate which tasks are intended for online vs offline policy selection, and provide a description of the corresponding data. Let us note that we have not modified how the rewards are computed in the original environments we used to generate the datasets. For the details of those reward functions, we refer to the papers where the environments were introduced first.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Control Suite", "weight": 1.0} -->

DeepMind Control Suite is a set of control tasks implemented in MuJoCo. We consider a subset of the tasks provided in the suite that cover a wide range of difficulties. For example, Cartpole swingup a simple task with a single degree of freedom is included. Difficult tasks are also included, such as Humanoid run, Manipulator insert peg, Manipulator insert ball. Humanoid run involves complex bodies with 21 degrees of freedom. And Manipulator insert ball/peg have not been shown to be solvable in any prior published work to the best of our knowledge. In all the considered tasks as observations we use the default feature representation of the system state, consisting of proprioceptive information such as joint positions and velocity, as well as additional sensors and target position where appropriate. The observation dimension ranges from 5 to 67.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Control Suite", "weight": 1.0} -->

Data Description Most of the datasets in this domain are generated using D4PG. For the environments Manipulator insert ball and Manipulator insert peg we use V-MPO to generate the data as D4PG is unable to solve these tasks. We always use 3 independent runs to ensure data diversity when generating data. All methods are run until the task is considered solved. For each method, data from the entire training run is recorded. As offline methods tend to require significantly less data, we reduce the sizes of the datasets via sub-sampling. In addition, we further reduce the number of successful episodes in each dataset by $2/3$ so as to ensure the datasets do not contain too many successful trajectories. See Table 3.1 for the size of each dataset. Each episode in this dataset contains 1000 time steps.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Control Suite", "weight": 1.0} -->

Manipulator insert ball Finger turn hard Manipulator insert peg Table 1. DM Control Suite tasks. We reserved five tasks for online policy selection (top) and the rest four are reserved for the offline policy selection (bottom). See Appendix E for reasoning behind choosing this particular task split.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Control Suite", "weight": 1.0} -->

Rodent two tap Rodent bowl escape Table 2. DM Locomotion tasks. We reserved four tasks for online policy selection (top) and the rest three are reserved for the offline policy selection (bottom). See Appendix E for reasoning behind choosing this particular task split.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Locomotion", "weight": 1.0} -->

These tasks are made up of the corridor locomotion tasks involving the CMU Humanoid, for which prior efforts have either used motion capture data or training from scratch. In addition, the DM Locomotion repository contains a set of tasks adapted to be suited to a virtual rodent. We emphasize that the *DM Locomotion* tasks feature the combination of challenging high-DoF continuous control along with perception from rich egocentric observations.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Locomotion", "weight": 1.0} -->

Data description Note that for the purposes of data collection on the CMU humanoid tasks, we use expert policies trained according to Merel et al., with only a single motor skill module from motion capture that is reused in each task. For the rodent task, we use the same training scheme as proposed by Merel et al.. For the CMU humanoid tasks, each dataset is generated by $3$ online methods whereas each dataset of the rodent tasks is generated by $5$ online methods. Similarly to the control suite, data from entire training runs is recorded to further diversify the datasets. Each dataset is then sub-sampled and the number of its successful episodes reduced by $2/3$. Since the sensing of the surroundings is done by egocentric cameras, all datasets in the locomotion domain include per-timestep egocentric camera observations of size $64 \times 64 \times 3$. The use of egocentric observation also renders some environments partially observable and therefore necessitates recurrent architectures. We therefore generate sequence datasets for tasks that require recurrent architectures. For dataset sizes and sequence lengths of see Table 3.1.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Atari 2600", "weight": 1.0} -->

The Arcade Learning environment (ALE) is a suite consisting of a diverse set of $57$ Atari 2600 games. It is a popular benchmark to measure the progress of online RL methods, and Atari has recently also become a standard benchmark for offline RL methods as well. In this paper, we are releasing a large and diverse dataset of gameplay following the protocol described by Agarwal et al., and use it to evaluate several discrete RL algorithms.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Atari 2600", "weight": 1.0} -->

Data Description The dataset is generated by running an online DQN agent and recording transitions from its replay during training with sticky actions. As stated, for each game we use data from five runs with $50$ million transitions each. States in each transition include stacks of four frames to be able to do frame-stacking with our baselines.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Atari 2600", "weight": 1.0} -->

In our release, we provide experiments on the $46$ of the Atari games that are available in OpenAI gym. OpenAI gym implements more than $46$ games, but we only include games where the online DQN's performance that has generated the dataset was significantly better than the random policy. We provide further information about the games we excluded in Appendix F. Among our $46$ Atari games, we chose nine to allow for online policy selection. Specifically, we ordered all games according to the their difficulty,^44^4The details of how we decide the difficulty of Atari games are provided in Appendix G. and picked every fifth game as our offline policy section task to cover diverse set of games in terms of difficulty. In Table 3, we provide the full list of games that we decided to include in RL Unplugged.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Atari 2600", "weight": 1.0} -->

Name This Game Table 3: Atari games. We have 46 games in total in our Atari data release. We reserved 9 of the games for online policy selection (top) and the rest of the 37 games are reserved for the offline policy selection (bottom).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Real-world Reinforcement Learning Suite", "weight": 1.0} -->

Dulac-Arnold et al. identify and evaluate respectively a set of $9$ challenges that are bottlenecks to implementing RL algorithms, at scale, on applied systems. These include high-dimensional state and action spaces, large system delays, system constraints, multiple objectives, handling non-stationarity and partial observability. In addition, they have released a suite of tasks called realworldrl-suite^55^5See for details. which enables a practitioner to verify the capabilities of their algorithm on domains that include some or all of these challenges. The suite also defines a set of standardized challenges with varying levels of difficulty. As part of the "RL Unplugged" collection, we have generated datasets using the 'easy' combined challenges on four tasks: Cartpole Swingup, Walker Walk, Quadruped Walk and Humanoid Walk.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Real-world Reinforcement Learning Suite", "weight": 1.0} -->

Data Description The datasets were generated as described in Section 2.8 of; note that this is the first data release based on those specifications. We used either the no challenge setting, which includes unperturbed versions of the tasks, or the easy combined challenge setting (see Section 2.9 of ), where data logs are generated from an environment that includes effects from combining all the challenges. Although the no challenge setting is identical to the control suite, the dataset generated for it is different as it is generated from fixed sub-optimal policies. These policies were obtained by training $3$ seeds of distributional MPO until convergence with different random weight initializations, and then taking snapshots corresponding to roughly $75\%$ of the converged performance. For the no challenge setting, three datasets of different sizes were generated for each environment by combining the three snapshots, with the total dataset sizes (in numbers of episodes) provided in Table 4. The procedure was repeated for the easy combined challenge setting. Only the "large data" setting was used for the combined challenge to ensure the task is still solvable. We consider all RWRL tasks as online policy selection tasks.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Baselines", "weight": 1.0} -->

We provide baseline results for a number of published algorithms for both continuous (DM Control Suite, DM Locomotion), and discrete action (Atari 2600) domains. We will open-source implementations of our baselines for the camera-ready. We follow the evaluation protocol presented in Section 2.2. Our baseline algorithms include behavior cloning (BC ); online reinforcement learning algorithms (DQN, D4PG, IQN ); and recently proposed offline reinforcement learning algorithms (BCQ, BRAC, RABM, REM ). Some algorithms only work for discrete or continuous actions spaces, so we only evaluate algorithms in domains they are suited to. Detailed descriptions of the baselines and our implementations (including hyperparameters) are presented in Section A in the supplementary material.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Baselines", "weight": 1.0} -->

Naive approach for offline policy selection For the tasks we have marked for offline policy selection, we need a strategy that does not use online interaction to select hyperparameters. Our naive approach is to choose the set of hyperparameters that performs best overall on the online policy selection tasks from the same domain. We do this independently for each baseline. This approach is motivated by how hyperparameters are often chosen in practice, by using prior knowledge of what worked well in similar domains. If a baseline algorithm drops in performance between online and offline policy selection tasks, this indicates the algorithm is not robust to the choice of hyperparameters. This is also cheaper than tuning hyperparameters individually for all tasks, which is especially relevant for Atari. For a given domain, a baseline algorithm and a hyperparameter set, we compute the average^66^6We use the arithmetic mean with the exception of Atari where we use median following. score over all tasks allowing online policy selection. The best hyperparameters are then applied to all offline policy selection tasks for this domain. The details of the experimental protocol and the final hyperparameters are provided in the supplementary material.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Control Suite", "weight": 1.0} -->

In Figure 4, we compare baselines across the online policy selection tasks (left) and offline policy selection tasks (right). A table of results is included in Section B of the supplementary material. For the simplest tasks, such as Cartpole swingup, Walker stand, and Walker walk, where the performance of offline RL is close to that of online methods, D4PG, BRAC and RABM are all good choices. But the picture changes on the more difficult tasks, such as Humanoid run (which has high dimension action spaces), or Manipulator insert ball and manipulator insert peg (where exploration is hard). Strikingly, in these domains BC is actually among the best algorithms alongside RABM, although no algorithm reaches the performance of online methods. This highlights how including tasks with diverse difficulty conditions in a benchmark gives a more complete picture of offline RL algorithms.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Locomotion", "weight": 1.0} -->

In Figure 5, we compare baselines across the online policy selection tasks (left) and offline policy selection tasks (right). A table of results is included in Section C of the supplementary material. This task domain is made exclusively of tasks that are high action dimension, hard exploration, or both. As a result the stark trends seen above continue. BC, and RABM perform best, and D4PG performs quite poorly. We also could not make BCQ or BRAC perform well on these tasks, but we are not sure if this is because these algorithms perform poorly on these tasks, or if our implementations are missing a crucial detail. For this reason we do not include them. This highlights another key problem in online and offline RL. Papers do not include key baselines because the authors were not able to reproduce them, see eg. By releasing datasets, evaluation protocols and baselines, we are making it easier for researchers such as those working with BCQ to try their methods on these challenging benchmarks.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Atari 2600", "weight": 1.0} -->

In Figure 6, we present results for Atari using normalized scores. Due to the large number of tasks, we aggregate results using the median as done in (individual scores are presented in Appendix D). These results indicate that DQN is not very robust to the choice of hyperparameters. Unlike REM or IQN, DQN's performance dropped significantly on the offline policy selection tasks. BCQ, REM and IQN perform at least as well as the best policy in our training set according to our metrics. In contrast to other datasets (Section 4.1 and 4.2), BC performs poorly on this dataset. Surprisingly, the performance of off-the-shelf off-policy RL algorithms is competitive and even surpasses BCQ on offline policy selection tasks. Combining behavior regularization methods (e.g., BCQ) with robust off-policy algorithms (REM, IQN) is a promising direction for future work.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We are releasing RL Unplugged, a suite of benchmarks covering a diverse set of environments, and datasets with an easy-to-use unified API. We present a clear evaluation protocol which we hope will encourage more research on offline policy selection. We empirically evaluate several state-of-art offline RL methods and analyze their results on our benchmark suite. The performance of the offline RL methods is already promising on some control suite tasks and Atari games. However, on partially-observable environments such as the locomotion suite the offline RL methods' performance is lower. We intend to extend our benchmark suite with new environments and datasets from the community to close the gap between real-world applications and reinforcement learning research.
