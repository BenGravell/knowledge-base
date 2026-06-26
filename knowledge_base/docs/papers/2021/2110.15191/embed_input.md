<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

URLB: Unsupervised Reinforcement Learning Benchmark

Topics include Reinforcement learning, Unsupervised reinforcement learning, Benchmarks, Reward-free pretraining, DeepMind control suite, Intrinsic rewards, Continuous control, Open-source benchmark.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces URLB, a two-phase benchmark for unsupervised RL in which agents first pretrain without rewards and then adapt to downstream control tasks. The benchmark standardizes environments and baselines, making it easier to compare intrinsic-motivation methods and exposing that existing approaches still struggle on broad continuous-control pretraining.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Deep Reinforcement Learning (RL) has emerged as a powerful paradigm to solve a range of complex yet specific control tasks. Yet training generalist agents that can quickly adapt to new tasks remains an outstanding challenge. Recent advances in unsupervised RL have shown that pre-training RL agents with self-supervised intrinsic rewards can result in efficient adaptation. However, these algorithms have been hard to compare and develop due to the lack of a unified benchmark. To this end, we introduce the Unsupervised Reinforcement Learning Benchmark (URLB). URLB consists of two phases: reward-free pre-training and downstream task adaptation with extrinsic rewards. Building on the DeepMind Control Suite, we provide twelve continuous control tasks from three domains for evaluation and open-source code for eight leading unsupervised RL methods. We find that the implemented baselines make progress but are not able to solve URLB and propose directions for future research.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deep Reinforcement Learning (RL) has been at the source of a number of breakthroughs in autonomous control over the last five years. RL algorithms have been used to train agents to play Atari video games directly from pixels, learn robotic locomotion and manipulation policies from raw sensory input, master the game of Go, and play large-scale multiplayer video games. While these results were significant advances in autonomous decision making, a deeper look reveals a fundamental limitation. The above algorithms produced agents capable of only solving the single task they were trained to solve. As a result, current RL approaches produce brittle policies with poor generalization capabilities, which limits their applicability to many problems of interest. It is therefore important to move beyond today's powerful but narrow RL systems toward generalist systems capable of quickly adapting to new downstream tasks.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, in the fields of Computer Vision (CV) and Natural Language Processing (NLP), large-scale unsupervised pre-training has enabled sample-efficient few-shot adaptation. In NLP, unsupervised sequential modeling has produced powerful few-shot learners. In CV, unsupervised representation learning techniques such as contrastive learning have produced algorithms that are dramatically more label-efficient than their supervised counterparts and more capable of adapting to a host of downstream supervised tasks such as classification, segmentation, and object detection. While these advances in unsupervised learning have also benefited RL in terms of learning efficiently from images as well as introducing new architectures for RL, the resulting agents have remained narrow since they still optimize a single extrinsic reward as before.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Fully unsupervised training of RL algorithms requires not only learning self-supervised representations but also learning policies without access to extrinsic rewards. Recently, unsupervised RL algorithms have begun to show progress toward more generalist systems by training policies without extrinsic rewards. Exploration with self-supervised prediction has enabled agents to explore video games from pixels, mutual information-based approaches have demonstrated self-supervised skill discovery and generalization to downstream tasks in continuous control domains, and maximal entropy RL has yielded policies capable of diverse exploration. However, comparing and developing new algorithms has been challenging due to a lack of a unified evaluation benchmark. Reward-free RL algorithms often use different optimization schemes, different tasks for evaluation, and have different evaluation procedures. Additionally, unlike more mature supervised RL algorithms, there does not exist a unified codebase for unsupervised RL that can be used to develop new methods quickly.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To make benchmarking and developing new unsupervised RL approaches easier, we introduce the Unsupervised Reinforcement Learning Benchmark (URLB). Built on top of the widely adopted DeepMind Control Suite, URLB provides a suite of domains of varying difficulty for unsupervised pre-training with diverse downstream evaluation tasks. URLB standardizes evaluation of unsupervised RL algorithms by defining fixed pre-training and fine-tuning procedures across all baselines. Perhaps most importantly, we open-source code for URLB environments as well as 8 leading baselines that represent the main approaches taken towards unsupervised pre-training in RL to date. Unlike prior code releases for unsupervised RL, URLB uses the same exact optimization algorithm for each baseline which enables transparent benchmarking and lowers the barrier to entry for developing new algorithms. We summarize the main contributions of this paper below: We introduce URLB, a new benchmark for evaluating unsupervised RL algorithms, which consists of three domains and twelve continuous control tasks of varying difficulty to evaluate the adaptation efficiency of unsupervised RL algorithms.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We open-source a unified codebase for eight leading unsupervised RL algorithms. Each algorithm is trained with the same optimization backbone for fairness of comparison.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We find that while the implemented baselines make progress on the proposed benchmark, no existing unsupervised RL algorithm can solve URLB, and consequently identify promising research directions to progress unsupervised RL.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The benchmark environments, algorithmic baselines, and pre-training and evaluation scripts are available at We believe that URLB will make the development of unsupervised RL agents easier and more transparent by providing a unified set of evaluation environments, systematic procedures for pre-training and evaluation, and algorithmic baselines that share the same optimization backbone.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Standardized of Pre-training and Fine-tuning Procedures", "weight": 1.0} -->

One reason why unsupervised RL has been hard to benchmark to date is that there is no agreed upon procedure for training and evaluating unsupervised RL agents. To this end, we standardize pre-training, fine-tuning, and evaluation in URLB. We split pre-training and fine-tuning into two phases consisting of $N_{PT}$ and $N_{FT}$ environment steps respectively. During pre-training, we checkpoint agents at 100k, 500k, 1M, 2M steps in order to evaluate downstream performance as a function of pre-training steps. For adapting the pre-trained policy to downstream tasks, we evaluate in the data-efficient regime where $N_{FT}$ is 100k, since we are interested in agents that are quick to adapt.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Evaluation", "weight": 1.0} -->

We evaluate the performance of an unsupervised RL algorithm by measuring how quickly it adapts to a downstream task. For each fine-tuning task, we initialize the agent with the pre-trained network parameters, fine-tune the agent for 100k steps and measure its performance on the downstream task. This evaluation procedure is similar to how pre-trained networks in CV and NLP are fine-tuned to downstream tasks such as classification, object detection, and summarization. There exist other means of evaluating the quality of pre-trained RL agents such as measuring the diversity of data collected during exploration or zero-shot generalization of goal-conditioned agents. However, it is challenging to produce a general method to measure data diversity, and while zero-shot generalization with goal-conditioned agents can be powerful such a benchmark would be limited to goal-conditioned RL. For these reasons, data diversity and goal-conditioned zero-shot generalization are less common evaluation metrics. In an effort to provide a general benchmark, we focus on the fine-tuning efficiency of the agent after pre-training which allows us to evaluate a diverse set of baselines.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Unlike unsupervised methods in CV and NLP which focus solely on representation learning, unsupervised pre-training in RL requires both representation learning and behavior learning. For this reason, URLB benchmarks performance for both state-based and pixel-based agents. Benchmarking both state and pixel-based RL separately is important because it allows us to decouple unsupervised behavior learning from unsupervised representation learning. In state-based RL, the agent receives a near-optimal representation of the world through coordinate states. Evaluating state-based unsupervised RL agents allows us to isolate unsupervised behavior discovery without worrying about representation learning as confounding factor. Evaluating pixel-based unsupervised RL agents provides insight into how representations and behaviors can be learned jointly.

<!-- chunk {"id": "body-0014", "role": "body", "section": "URLB Environments", "weight": 1.0} -->

We release a set of domains and downstream tasks for URLB that are based on the DeepMind Control Suite (DMC). The three reasons for building URLB on top of DMC are (i) DMC is already widely adopted and familiar to RL practitioners; (ii) DMC environments can be used with both state and pixel-based inputs; (iii) DMC features environments of varying difficulty which is useful for designing a benchmark that contains both challenging and feasible tasks. URLB evaluates performance on 12 continuous control tasks (3 domains with 4 downstream tasks per domain). From easiest to hardest, the URLB domains and tasks are: Walker (Stand, Walk, Flip, Run): A biped constrained to a 2D vertical plane. Walker is a challenging introduction domain for unsupervised RL because it requires the unsupervised agent to learn balancing and locomotion skills in order to fine-tune efficiently. Quadruped (Stand, Walk, Jump, Run): A quadruped within a a 3D space. Like walker, quadruped requires the agent to learn to balance and move but is harder due to a high-dimensional state and action spaces and 3D environment.

<!-- chunk {"id": "body-0015", "role": "body", "section": "URLB Environments", "weight": 1.0} -->

Jaco Arm (Reach top left, Reach top right, Reach bottom left, Reach bottom right): Jaco Arm is a 6-DOF robotic arm with a three-finger gripper. This environment tests the unsupervised RL agent's ability to control the robot arm without locking and perform simple manipulation tasks. It was recently shown that this environment is particularly challenging for unsupervised RL.

<!-- chunk {"id": "body-0016", "role": "body", "section": "URLB Environments", "weight": 1.0} -->

1:Randomly initialized actor πθ, critic Qϕ, and encoder fξ networks, replay buffer 𝒟. 2:Intrinsic rint and extrinsic rext reward functions, discount factor γ. 3:Environment (env), M downstream tasks Tk, k ∈ [1, …, M]. 4:pre-train NPT and fine-tune NFT steps. 5:for t = 1..NPT do ⊳ Part 1: Unsupervised Pre-training 9: Update πθ, Qϕ, and fξ using minibatches from 𝒟 and intrinsic reward rint according to Eqs. 1 and 2. 11:Outputs pre-trained parameters θPT, ϕPT, and ξPT 12:for Tk ∈ [T1, …, TM] do ⊳ Part 2: Supervised Fine-tuning 18: Update πθ, Qϕ, and fξ using minibatches from 𝒟 according to Eqs. 1 and 2. 20: Evaluate performance of RL agent on task Tk Algorithm 1 Unsupervised RL: Unsupervised Pre-training and Supervised Fine-tuning

<!-- chunk {"id": "body-0017", "role": "body", "section": "URLB: Algorithmic Baselines for Unsupervised RL", "weight": 1.0} -->

In addition to introducing URLB, the other primary contribution of this work is open-sourcing a unified codebase for eight leading unsupervised RL algorithms. To date, unsupervised RL algorithms have been hard to compare due to confounding factors such as different evaluation procedures and optimization schemes. While URLB provides standardized pre-training, fine-tuning, and evaluation procedures, current algorithms are hard to compare since they rely on different optimization algorithms. For instance, Curiosity utilizes PPO while APT uses SAC for optimization. Moreover, even if two unsupervised RL methods use the same optimization algorithm, small differences in implementation can result in large performance differences that are independent of the pre-training algorithm. For this reason, it is important to provide a unified codebase with identical implementations of the optimization algorithm for each baseline. Providing such a unified codebase is one of the main contributions of this benchmark.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Backbone RL Algorithm", "weight": 1.0} -->

Since most of the above algorithms rely on off-policy optimization (and some cannot be optimized on-policy at all), we opt for a state-of-the-art off-policy optimization algorithm. While SAC has been the de facto off-policy RL algorithm for many RL methods in the last few years, it is prone to suffering from policy entropy collapse. DrQ-v2 recently showed that using DDPG instead of SAC as a learning algorithm leads to a more robust performance on tasks from DMC. For this reason, we opt for DrQ-v2 as our base optimization algorithm to learn from images, and DDPG, as implemented in DrQ-v2, to learn from states. DDPG is an actor-critic off-policy algorithm for continuous control tasks. The critic $Q_{\phi}$ minimizes the Bellman error where $\overline{\phi}$ is an exponential moving average of the critic weights. The deterministic actor $\pi_{\theta}$ is learned by maximizing the expected returns

<!-- chunk {"id": "body-0019", "role": "body", "section": "Unsupervised RL Algorithms", "weight": 1.0} -->

As part of URLB, we open-source code for eight leading or well-known algorithms across all three of these categories all of which utilize the same optimization backbone. All algorithms provided with URLB differ only in their intrinsic reward while keeping all other parts of the RL architecture the same. We list all implemented baselines in Table 1 and provide a brief overview of the algorithms considered, which are binned into three categories -- knowledge-based, data-based, and competence-based algorithms.^11^1We borrow this terminology from the following unsupervised RL tutorial.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Unsupervised RL Algorithms", "weight": 1.0} -->

For detailed descriptions of each method we refer the reader to Appendix A. ${\|{{g{(\mathbf{z}_{t},\mathbf{a}_{t})}} - {\overset{\sim}{g}{(\mathbf{z}_{t},\mathbf{a}_{t})}}}\|}_{2}^{2}$ log p* (z) − log qw (z) − log p (w) + log d (w|z) Table 1: Unsupervised RL Algorithms implemented in URLB.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Unsupervised RL Algorithms", "weight": 1.0} -->

Knowledge-based Baselines: Knowledge-based methods aim to increase knowledge about the world by maximizing prediction error. As part of the knowledge-based suite, we implement the Intrinsic Curiosity Module (ICM), Disagreement, and Random Network Distillation (RND). All three methods utilize a function $g$ to either predict the dynamics $g{(\left. \mathbf{z}_{t + 1} \middle| {\mathbf{z}_{t},\mathbf{a}_{t}} \right.)}$ (ICM, Disagreement) or predict the output of a random network $g{(\mathbf{z}_{t},\mathbf{a}_{t})}$ (RND), where $\mathbf{z}$ is the encoding of $\mathbf{o}$. ICM and RND maximize prediction error while Disagreement maximizes prediction uncertainty.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Unsupervised RL Algorithms", "weight": 1.0} -->

Data-based Baselines: Data-based methods aim to achieve data diversity by maximizing entropy. We implement APT and ProtoRL both of which maximize entropy $H{(\mathbf{z})}$ in different ways. Both methods utilize a particle estimator to maximize the entropy by maximizing the distance between k-nearest neighbors (kNN) for each state or observation embedding $\mathbf{z}$. Since computing kNN over the entire replay buffer is expensive, APT estimates entropy across transitions in a randomly sampled minibatch. ProtoRL improves on APT by clustering the replay buffer with a contrastive deep clustering algorithm SWaV. The centroids of the clusters are called prototypes, which are used by ProtoRL to estimate entropy.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Unsupervised RL Algorithms", "weight": 1.0} -->

Competence-based Baselines: Competence-based algorithms, learn an explicit skill vector $\mathbf{w}$ by maximizing the mutual information between the encoded observation and skill $I{(\mathbf{z};\mathbf{w})}$. This mutual information can be decomposed in two ways, ${I{(\mathbf{z};\mathbf{w})}} = {{H{(\mathbf{z})}} - {H{(\left. \mathbf{z} \middle| \mathbf{w} \right.)}}} = {{H{(\mathbf{w})}} - {H{(\left. \mathbf{w} \middle| \mathbf{z} \right.)}}}$. We provide baselines for both decompositions. The former decomposition is utilized in skill discovery algorithms such as DIAYN, VIC, VALOR, which are conceptually similar. For URLB, we implement DIAYN.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Unsupervised RL Algorithms", "weight": 1.0} -->

The latter decomposition, though less common, is implemented in the APS, which uses a particle estimator for the entropy term and successor features to represent the conditional entropy. Lastly, we implement SMM which combines both decompositions into one objective. Note that the SMM paper describes both skill-based and skill-free variants, so it can be categorized as both competence and data-based.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate the algorithms listed in Table 1 by pre-training with the intrinsic reward objective and fine-tuning on the downstream task as described in Section 3.2. For DrQ-v2 optimization we fix the hyper-parameters from and for algorithm-specific hyper-parameters we perform a grid sweep and pick the best performing parameters. We benchmark both state and pixel-based experiments and keep all non-algorithm-specific architectural details the same with a full description available in Appendix B. Performance on each downstream task is evaluated over ten random seeds and we display the mean scores and standard errors. We summarize the main results of our evaluation in Figures 3 and 4, which show evaluation scores grouped by algorithm category, described in Section 4.2, and environment, described in Section 3.3. An extensive list of results across all algorithms considered in this work can be found in Appendix C.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experiments", "weight": 1.0} -->

By benchmarking a wide array of exploration algorithms on both state and pixel-based tasks we are able to get perspective on the current state of unsupervised RL. Overall, we find that while unsupervised RL shows promise, it is still far from solving the proposed benchmark and many open questions need to be addressed to make progress toward unsupervised pre-training for RL. We note that solving the benchmark means matching the asymptotic DrQ-v2 (for pixels) and DDPG (for states) performance within 100k steps of fine-tuning. The motivation for this definition is that unsupervised RL agents get access to unlimited reward-free environment interactions. After pre-training, we seek to develop agents that adapt quickly to the desired downstream task. We list our observations below: O1: None of the implemented unsupervised RL algorithms solve the benchmark. Despite access to up to 2M pre-training steps, after 100k steps of fine-tuning no method matches asymptotic performance on most tasks.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experiments", "weight": 1.0} -->

The best-performing benchmarked algorithms achieve $40 - {70\%}$ normalized return whereas the benchmark is considered solved when the agent achieves near $100\%$ normalized returns. This suggests that we are still far as a community from efficient generalization in deep RL.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experiments", "weight": 1.0} -->

O2: Unsupervised RL is not universally better than random initialization. We also observe that fine-tuning an unsupervised RL baseline is not always preferable to fine-tuning from a random initialization. In particular when learning from states, a random initialization is competitive with most baselines. However, when learning from pixels fine-tuning from random initialization degrades suggesting that representation learning is an important component of unsupervised pre-training.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experiments", "weight": 1.0} -->

O3: There exists a large gap in performance between exploring from states and exploring from pixels. Another observation that supports representation learning as an important aspect of exploration is that exploration algorithms degrade substantially when learning from pixels compared to learning from state. Shown in Figure 3, most algorithms lose $20 - {50\%}$ when learning from pixels compared to state and especially so on the harder environments (Quadruped, Jaco Arm). These results suggest that better representation learning during pre-training is an important research direction.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments", "weight": 1.0} -->

O4: In aggregate, competence-based approaches underperform knowledge-based and data-based approaches. While knowledge-based and data-based approaches both perform competitively across URLB, we find that competence-based approaches are lagging behind. Specifically, there is no competence-based approach that achieves state-of-the-art mean performance on any of the URLB tasks, which points to competence-based unsupervised RL as an impactful research direction with significant room for improvement.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

O5: There is not a single leading unsupervised RL algorithm for both states and pixels. We observe that there is no single state-of-the-art algorithm for unsupervised RL. At 2M pre-training steps, APT and ProtoRL are the leading algorithms for state-based URLB while ICM achieves leading performance on pixel-based URLB despite the existence of more sophisticated knowledge-based methods (see Figure 5).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

O6: For many unsupervised RL algorithms, rather than monotonically improving performance decays as a function of pre-training steps. We desire and would expect that the fine-tuning efficiency of unsupervised RL algorithms would improve as a function of pre-training steps. Surprisingly, we find that for 9 out of 18 experiments shown in Figure 4, performance either does not improve or even degrades as a function of pre-training steps. We see this as potentially the biggest drawback of current unsupervised RL approaches -- they do not scale with the number of environment interactions. Developing algorithms that improve monotonically as a function of pre-training steps is an open and impactful line of research.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

O7: New fine-tuning strategies will likely be needed for fast adaptation. While not investigated in depth in this benchmark, new fine-tuning strategies could play a large role in the adoption of unsupervised RL. Perhaps part of the issue raised in O6 could be addressed with better fine-tuning. The algorithms in URLB are all fine-tuned by initializing the actor-critic with the pre-trained weights and fine-tuning with an extrinsic reward. There are likely other better strategies for fine-tuning, particularly for competence based approaches that are conditioned on the skill $\mathbf{w}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented URLB, a benchmark designed to measure the performance of unsupervised RL algorithms. URLB consists of a suite of twelve evaluation tasks of varying difficulty from three domains and standardized procedures for pre-training and evaluation. We've open-sourced implementations and evaluation scores for eight leading unsupervised RL algorithms from all major algorithm categories. To minimize confounding factors, we utilized the same optimization method across all baselines. While none of the implemented baselines solve URLB, many make substantial progress suggesting a number of fruitful directions for unsupervised RL research. We hope that this benchmark makes the development and comparison of unsupervised RL algorithms easier and clearer.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Limitations. There are a number of limitations for both URLB and unsupervised RL methods in general. While URLB tasks are designed to be challenging, they are far from the visual and combinatorial complexity of real-world robotics. However, existing algorithms are unable to solve the benchmark meaning there is substantial room for improvement on the URLB tasks before moving on to even more challenging ones. While we present standardized pre-training and evaluation procedures, there can be many other ways of measuring the quality of the exploration algorithm. For instance, the quality of pre-training can be evaluated not only through policy adaptation but also through dataset diversity which we do not consider in this paper. In this work, similar to the Atari and DMC benchmarks for supervised RL we do not consider goal-conditioned RL which can be quite powerful for exploration. For generality, we chose the currently most commonly used evaluation procedure that allowed us to benchmark a diverse set of leading exploration algorithms but, of course, other choices are available and would be interesting to investigate in future work.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Potential negative impacts. Unsupervised RL has the benefits of requiring zero extrinsic reward interactions during pre-training, and due to this the resulting agents may develop policies that are not aligned with human intent. This could be problematic in the long-term if not addressed early and carefully because as unsupervised robotics get more capable they can inadvertently inflict harm on themselves or the environment. Methods for constraining exploration within a broad set of human preferences (e.g. explore without harming the environment) is an interesting and important direction for future research in order to produced safe agents.
