<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Freeform Preference Learning for Robotic Manipulation

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Reward design remains a central bottleneck for autonomous robot policy improvement, especially in long-horizon manipulation tasks where sparse success labels provide too little signal and binary preferences collapse many competing notions of quality into one ambiguous signal. We introduce Freeform Preference Learning (FPL), a method for learning robot policies from freeform human preferences. Rather than asking annotators which of two trajectories is better overall, FPL lets them define natural-language preference axes, such as speed, safety, quality of placement, or carefulness, and provide pairwise preferences along each axis. These annotations are used to learn a language-conditioned reward model that maps a trajectory and preference label to an axis-specific reward. We use this model to train a reward-conditioned policy that optimizes across the multiple human-specified dimensions. Across four real-world and two simulated long-horizon manipulation tasks, FPL improves over sparse-reward and binary-preference methods by 38 percentage points. Beyond improved performance, FPL learns dense progress signals without explicit subtask segmentation, shows compositionality of behavior not present in the data, and allows users to steer the policy towards different behaviors at test time without retraining. Blog post with videos available at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Rewards are a critical component for autonomous robot improvement. An ideal reward function should provide dense, unambiguous feedback and should capture all aspects of desirable behavior. For example, supervision for the simple task of setting a table should incorporate the configuration of the cutlery, the degree of care taken to not break fragile plates, the comfort of nearby people (e.g. to avoid motions that point a knife towards a person), and the speed of execution, among other aspects. Accurately capturing all of these axes presents a major challenge, both when eliciting supervision from people and when representing all of these factors in a reward function and downstream behavior. Moreover, a reward function that captures these axes but is too sparse, or dense but inaccurate, can lead to unwanted downstream behaviors when optimized against. In this paper, we study how to leverage human supervision to learn reward functions and ultimately robot behavior that captures all dimensions of a person's intent.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Prior works have studied a variety of rewards and reward learning approaches. Perhaps the simplest option is to provide or learn from binary success labels, which should in principle make it easy for people to determine if all criteria are met. However, this reward signal places significant burden on the reinforcement learning algorithm, making it hard to scale to more challenging tasks and to incorporate real-world constraints on behavior beyond basic task completion. Other works learn shaped scalar rewards but still focus on task progress metrics, ignoring important criteria on how a task was performed. Finally, preference learning is a promising paradigm for learning denser reward signals while reducing the burden on human supervisors, but requires them to collapse multiple axes of judgment into a single "overall" binary preference label. In long-horizon tasks this can make preferences difficult to provide and the resulting supervision ambiguous.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To preserve these axes of judgment, our key insight is to allow annotators to provide preference labels on any task-relevant axes of their choosing. This multidimensional supervision can then be used to learn a policy optimized for the combination of these dimensions. We instantiate this idea by asking annotators to specify relevant judgment dimensions in natural language and to provide a binary preference for each axis. The axes can be defined up front or during the annotation process. We then learn a multi-axis reward function that produces a scalar reward score when conditioned on a natural language description of the axis. Finally, we train a promptable policy to optimize the combination of axes described during reward training. Notably, this framework simultaneously improves both the ease of providing unambiguous supervision and the density of supervision for downstream policy optimization.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main contribution of our paper is *Freeform Preference Learning* (*FPL*), a method for eliciting and learning from freeform human preferences. *FPL* learns a language-conditioned reward function from preferences, capturing a variety of task-relevant attributes including quality of result, speed, smoothness, damage, and hygiene. This reward model provides dense supervision for training a multi-axis reward-conditioned policy. We evaluate *FPL* on four real-world tasks---putting a cube in a target bowl, folding shorts, plating a toast, and setting up a table---as well as two simulated tasks. Across settings, policies trained with *FPL* significantly outperform those trained with sparse rewards and binary preference learning methods. We further find that preserving the multi-dimensionality of feedback enables compositional generalization and test-time steerability of the resulting policies as well as qualitatively denser rewards on long-horizon tasks without requiring subtask segmentation.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Learning from Freeform Preferences", "weight": 1.0} -->

The key idea behind our method, *Freeform Preference Learning* (*FPL*), is to learn from natural language and open-ended feedback instead of traditional binary preferences. Rather than asking annotators for one overall preference between two trajectories, we ask them to describe the axes along which to compare them, such as speed, safety, smoothness, or subtask completion. This yields feedback that is more granular and less ambiguous. We use these freeform preferences to learn a language-conditioned, multi-dimensional reward function that scores trajectories along each specified axis. We then train a policy conditioned on multiple preference dimensions to optimize the behavior with respect to each axis. We describe each component of our proposed algorithm below.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Learning a Reward Function from Freeform Human Feedback", "weight": 1.0} -->

Traditionally, human preferences are collected as a binary signal over an "overall quality" metric, i.e., the annotators are asked "which one of the two trajectories do you prefer?" However, this signal is difficult to provide because the answer often depends on the axis of comparison. For example, if one trajectory is faster while the other is safer, it is unclear which should be preferred overall. This ambiguity is further amplified when preferences are collected over trajectory segments, since the two segments may correspond to different stages of the task and therefore be difficult to directly compare. We instead collect freeform human preferences by showing two full trajectories and asking them to evaluate them along multiple axes, either predefined or specified by the annotator in natural language. Rather than asking a single fixed question about "overall quality", we collect preferences over a variety of axes such as "formality of setup", "speed", "safety", and so.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Learning a Reward Function from Freeform Human Feedback", "weight": 1.0} -->

Given a freeform preference dataset $\mathcal{P}$ made up of natural language labels defining the axes $l_{k}$ and binary preferences $y_{k}$ per axis, we now describe how to learn a reward function $r_{\phi}$ from it.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Learning a Reward Function from Freeform Human Feedback", "weight": 1.0} -->

A simple way to learn from multi-dimensional feedback would be to define a fixed set of $K$ preference axes and train a separate reward function for each one. However, this requires a predefined set of axes and limits generalization across semantically similar descriptions. For example, different annotators may refer to the same concept as "speed", "fast", or "efficient". We instead keep preference axes in natural language and condition a single reward model directly on their text descriptions, leveraging the pretrained representations of vision-language models, see Fig. 2.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Learning a Reward Function from Freeform Human Feedback", "weight": 1.0} -->

The Bradley-Terry model in Eq. 2 is typically used to learn a uni-dimensional reward. We extend this formulation to freeform preferences by conditioning the reward model on the natural-language axis for which each preference was provided. This yields an axis-conditioned reward function $r_{\phi}$ that scores a trajectory with respect to the specified axis, as defined in Eq 3.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Learning a Reward Function from Freeform Human Feedback", "weight": 1.0} -->

For a pair of trajectories $(\tau_{i},\tau_{j})$, an annotator provides per-axis preference labels and language labels $\{(l_{k},y_{k})\mid k=1,\ldots,K_{ij}\}$, where $y_{k}\in\{0,1\}$ indicates the preferred trajectory along axis $k$ and $K_{ij}$ is the total number of preference axes described for the trajectory pair (which may vary across pairs). The multi-dimensional reward model $r_{\phi}$ outputs a single scalar conditioned on the axis label and is trained to minimize the Bradley-Terry negative log-likelihood: Finally, unlike standard preference-based reward models that score individual observations or short segments, we condition the reward model on the observation history. This allows the model to capture temporal dependencies that may be necessary for evaluating trajectory-level preferences.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Learning a Reward Function from Freeform Human Feedback", "weight": 1.0} -->

Given a trajectory $\tau={o_{1},\ldots,o_{T}}$ and a natural-language preference axis $l_{k}$, we define the trajectory-level reward as a sum of per-prefix scores: where $g_{\phi}$ is a multimodal transformer that scores the segment $o_{1:i}$ conditioned on the axis $l_{k}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Policy Extraction on a Multi-Dimensional Reward Function", "weight": 1.0} -->

Now that we have described how to learn a language-conditioned reward function from freeform feedback on trajectory pairs, we discuss how best to use this supervision to learn a policy. One option would be to collapse the different dimensions into a scalar reward by a weighted sum and optimize it with standard RL techniques. Although this is simple and would leverage the benefits of easier-to-provide feedback, policy optimization can also benefit significantly from more detailed supervision. Collapsing all the axes into a single scalar is more prone to reward hacking and exhibiting the problems of reward shaping. Moreover, as we show in Section 5.2, preserving the decomposed rewards enables the learned policy to exhibit compositionality of behaviors not present in the original dataset, as well as at test-time steerability without retraining with a different reward. To realize these benefits, we train a policy conditioned on natural-language reward axes and their corresponding scores.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Policy Extraction on a Multi-Dimensional Reward Function", "weight": 1.0} -->

In principle, there are many base RL algorithms that we can extend to the language-conditioned setting with a language-conditioned reward function. We opt to use a particularly simple approach, based on prior work that trains reward-conditioned policies. Because we would like our policy to be able to optimize all representative axes of preferences rather than just one, we select a comprehensive set of $K_{\pi}$ preference axes for policy training $L=\{l_{k}|k=1\dots K_{\pi}\}$. These can be selected as representative axis descriptions that appear in the reward model training dataset, either manually or through automatic summarization to remove synonym phrases. Then, we condition the policy on all of the axis descriptions $l_{k}$ and corresponding trajectory rewards $r_{\phi}(\tau|l_{k})$. More formally, our policy training objective is: This approach can be used in both an offline and online RL setting. In the former case, this policy optimization step is performed once on an offline preference dataset.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Policy Extraction on a Multi-Dimensional Reward Function", "weight": 1.0} -->

In the latter case, we repeat this process: collecting roll-out data from the latest policy, soliciting preference annotations on this new data, and then updating the policy.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Policy Extraction on a Multi-Dimensional Reward Function", "weight": 1.0} -->

Initial offline dataset 𝒟, number of iterations N, π0 initial policy 𝒫 ← ∅; Initialize preference buffer 𝒫 ← 𝒫 ∪ 𝒫n; Collect 𝒫n freeform preferences over pairs from 𝒟 rϕn← Train reward model on 𝒫 (Eq. 3) Ln← Extract preference axes from 𝒫 πn← Train πn using rϕn on 𝒟 (see Eq 5) return final policy πN Algorithm 1 FPL: Freeform Preference Learning Notably, the preference axes described by human annotators may evolve over multiple iterations as the policy becomes more capable, and likewise, the set of $K_{\pi}$ preference axes for policy optimization can also change and expand. This naturally can yield a curriculum where initial preferences focus on initial stages of the task or coarse attributes of behavior, while later preferences can focus on later stages of the task and fine details. The full iterative training process is outlined in Algorithm 1.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Policy Extraction on a Multi-Dimensional Reward Function", "weight": 1.0} -->

At test-time, *FPL* can steer the policy towards high-performing behaviors by varying the target rewards used for conditioning. Because the reward model outputs are unbounded, selecting values that both elicit the desired behavior and remain in distribution can be difficult. We therefore standardize rewards per axis over $\mathcal{D}$, yielding a normalized scale for more easily querying the policy at test time.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Analysis & Experimental Evaluation", "weight": 1.0} -->

Our experimental section is designed to answer the following questions: (a) Does *FPL* learn effective policies through freeform human preferences? (b) Do policies learned through *FPL* exhibit compositionality of behaviors unseen in the data? (c) Does *FPL* exhibit steerability of rewards at test time? (d) Does *FPL* learn denser reward functions for long-horizon tasks?

<!-- chunk {"id": "body-0020", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

In order to empirically respond to the questions above, we consider four real-world manipulation tasks and two simulation tasks.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Real-world. *Put cube into target bowl* is a diagnostic task for steerability, where the policy is reward-conditioned to place the cube into one of three bowls. *Fold shorts* tests deformable-object manipulation, requiring the robot to fold shorts in three folds while optimizing speed and alignment. *Plate toast* tests dexterous tool use, requiring the robot to transfer toast from a tray to a plate while using the spatula smoothly. *Set up the table* is a long-horizon task in which the robot places two plates, cutlery, and a cup, testing task completion, formality, and carefulness. All real-world tasks use the DROID setup, with two camera views as observations and joint-velocity control for a Franka robot. The tasks are shown in Figure 7; further details are in Appendix 7.1.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Simulation. We use two Robomimic-based tasks. *Object rearrangement* requires placing two objects into the correct containers and in the correct order. *Bimodal square* tests compositionality, the target behavior is to place the nut on the right peg quickly, while the initial dataset contains fast left-peg trajectories and slow right-peg trajectories. We also evaluate *bimodal square (inverted)* to test whether the same policy can be steered at test time to place the nut on the left peg. More details can be found in Appendix 7.2.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

All tasks start from offline demonstrations with varying quality and strategies. We report mean and standard error, using 20 rollouts per real-world method and three seeds in simulation (see Apdx. 7).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

Comparisons. We compare *FPL* against five baselines. *Single Preferences* learns from standard pairwise preferences over a single "overall quality" axis, using the same reward-conditioned policy extraction as *FPL* for a fair comparison. *Advantage Conditioning* following Intelligence et al., we train a value function from success signal and time-to-go supervision, and condition the policy on the resulting advantage. *Weighted Regression* uses the multi-dimensional reward model learned by *FPL*, but extracts the policy with weighted regression using the average of rewards across the axes $L$. *Filtered BC* trains on the offline dataset together with successful policy rollouts, providing a sparse reward policy-extraction baseline. *BC* trains with imitation learning over the original offline dataset without reward learning or iterative improvement.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

Single Preferences (match pairs) Single Preferences (match comparisons) Table 1: Simulation results comparing FPL against baselines across simulation environments. Multi-dimensional preferences as leveraged by FPL provide the best supervision. FPL can successfully solve with the same policy the bimodal square and bimodal square inverted benchmarks by changing the reward conditioning at test-time.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

*FPL* learns performant policies from freeform human preferences. In Figure 3, we show that *FPL* outperforms all baselines in the real-world, improving by 38 overall percentage points over the next best method. We find that single overall preferences are often ambiguous in long-horizon tasks. For example, in *plate toast*, one trajectory may use the gripper fingers instead of the spatula, making it unhygienic, while another may use the spatula but drop the toast. In such cases deciding which trajectory is "better overall" is difficult and leads to noisy supervision. Sparse success/failure rewards are also insufficient: in *setup table*, the robot must complete several sequential subtasks, so rewarding only perfect executions provides too little signal, while rewarding imperfect executions can reinforce undesirable behavior. In practice, sparse-reward baselines learned to place the items in the correct locations but did not learn to place the items carefully and often dropped the plates instead of placing them with care. In contrast, *FPL* provides axis-specific supervision, allowing the policy to improve both the task completion and qualitative aspects of behavior.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

In simulation, *FPL* outperforms all baselines, as shown in Table 1. The gap is particularly clear in the *object rearrangement* task where the long-horizon and noisiness of the offline dataset has few complete successes. In this setting, success/failure signal is too sparse to correctly learn a successful policy. By contrast, preference-based methods provide denser signal. But, single overall preferences still collapse multiple behaviors into one ambiguous signal. As a result the policies learned from single preferences achieve the correct arrangement of objects but fail since they often drop objects from too high above the target. *FPL*, however, uses multi-dimensional preferences to capture the different important axes for the task separately, leading to successful policies.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

*FPL* exhibits compositionality of behaviors. We study this in the *bimodal square* simulation environment, where the goal is to place the nut on the right peg. As shown in Figure 4, the offline dataset has both fast and slow demonstrations for the left peg but *only* slow demonstrations for the right peg. *FPL* achieves faster right peg placements than those seen in the training data, while the single preference baseline does not improve beyond the demonstrated behaviors. This shows that *FPL* can compose behaviors through the preference axes, in this case the target placement at faster speed, whereas the baselines cannot (see Table 6). We attribute this compositionality to multi-dimensional reward learning together with reward-conditioned policy extraction.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

*FPL* exhibits test-time steerability. We evaluate steerability using the *inverted* version of *bimodal square*, where the same trained policy is conditioned to place the nut on the left peg instead of the right peg. As we show in the *inverted* columns of Table 1 and Figure 5, *FPL* is the only method that achieves high performance on both the original and the inverted tasks with the same policy. This is enabled by reward-conditioned policy extraction on multi-dimensional rewards: because *FPL* trains on trajectories across the replay buffer without filtering, the policy observes both high- and low-scoring behaviors along each axis and can be steered at test time by changing the target reward conditioning.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Qualitative Analysis", "weight": 1.0} -->

*FPL* qualitatively produces denser reward signals on long-horizon tasks without explicit task segmentation. In Figure 6, we qualitatively compare reward models learned with *FPL* and binary preference feedback on an example rollout from the *setup table* task. Although neither model is trained with explicit subtask boundaries, the reward learned with *FPL* temporally localized the corresponding events such as placing the big plate, small plate, cup, and cutlery. This makes the learned reward more interpretable and suggests that freeform, axis-specific preferences can provide a denser signal for long-horizon tasks. In contrast, the binary-preference reward produces a large reward spike near the end of the episode, despite no major subtask being completed at that point showing then an error in the credit assignment.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Qualitative Analysis", "weight": 1.0} -->

Freeform preferences axes naturally change throughout iterations. With the policy performance improving at each iteration, the annotators change from more coarse feedback to more concrete and perfectionist feedback. In Figure 10, we observe that in the early iterations of *fold shorts* task, the annotator focuses on whether each fold happens at all, and later ones, once folding is reliable, whether there are wrinkles and final alignment are perfected.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Qualitative Analysis", "weight": 1.0} -->

Freeform preferences produced diverse preference axes. Allowing annotators to specify preference axes in natural language yields a diverse set of labels. In the *plate toast* task, we obtained 295 trajectory-pair comparisons and over 1477 axis-level comparisons spanning 41 distinct labels (see Figure 14 in Appendix 8). This suggests the annotators naturally use a wide range of criteria when evaluating robot behavior, motivating the need for preference learning methods that preserve this structure rather than collapse feedback into a single overall score.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Qualitative Analysis", "weight": 1.0} -->

Freeform preferences reduce annotation time per label. As shown in Figure 9(b), collecting freeform preferences is approximately 50% faster per label than collecting single binary preferences. Because annotators provide multiple axis-specific judgments for each trajectory pair, the cost of viewing the videos is shared across several labels, which reduces the annotation overhead.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Limitations & Conclusion", "weight": 1.5} -->

To conclude, we introduced *FPL*, a method for learning robot policies from freeform human preferences. By collecting preferences with natural-language axes, *FPL* provides denser and less ambiguous supervision than single binary preferences. Across four real-world tasks and two simulation settings, *FPL* outperforms the baselines. We show that preserving the multi-dimensional structure of human feedback enables compositionality of behaviors and test-time steerability of the learned policy as well as qualitatively learn reward models with better credit assignment.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Limitations & Conclusion", "weight": 1.5} -->

Several limitations remain. Preference learning requires collecting human preferences, which is more expensive than fully unsupervised approaches. Reward-conditioned policy learning requires selecting appropriate reward values at test time, automating this selection is an important direction for future work. Finally, the current policy is conditioned on a fixed set of preference axes, and extending this method to handle variable axes is a promising direction as VLAs become more capable.
