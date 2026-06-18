<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale

Topics include Reinforcement learning, Robotics, Learning, MT-Opt.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

General-purpose robotic systems must master a large repertoire of diverse skills to be useful in a range of daily tasks. While reinforcement learning provides a powerful framework for acquiring individual behaviors, the time needed to acquire each skill makes the prospect of a generalist robot trained with RL daunting. In this paper, we study how a large-scale collective robotic learning system can acquire a repertoire of behaviors simultaneously, sharing exploration, experience, and representations across tasks. In this framework new tasks can be continuously instantiated from previously learned tasks improving overall performance and capabilities of the system. To instantiate this system, we develop a scalable and intuitive framework for specifying new tasks through user-provided examples of desired outcomes, devise a multi-robot collective learning system for data collection that simultaneously collects experience for multiple tasks, and develop a scalable and generalizable multi-task deep reinforcement learning method, which we call MT-Opt. We demonstrate how MT-Opt can learn a wide range of skills, including semantic picking (i.e., picking an object from a particular category), placing into various fixtures (e.g., placing a food item onto a plate), covering, aligning, and rearranging.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We train and evaluate our system on a set of 12 real-world tasks with data collected from 7 robots, and demonstrate the performance of our system both in terms of its ability to generalize to structurally similar new tasks, and acquire distinct new tasks more quickly by leveraging past experience. We recommend viewing the videos at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Today's deep reinforcement learning (RL) methods, when applied to real-world robotic tasks, provide an effective but expensive way of learning skills. While existing methods are effective and able to generalize, they require considerable on-robot training time, as well as extensive engineering effort for setting up each task and ensuring that the robot can attempt the task repeatedly. For example, the QT-Opt system can learn vision-based robotic grasping, but it requires over $500,000$ trials collected across multiple robots. While such sample complexity may be reasonable if the robot needs to perform a single task, such as grasping objects from a bin, it becomes costly if we consider the prospect of training a general-purpose robot with a large repertoire of behaviors, where each behavior is learned in isolation, starting from scratch. Can we instead *amortize* the cost of learning this repertoire over multiple skills, where the effort needed to learn whole repertoire is reduced, easier skills serve to facilitate the acquisition of more complex ones, and data requirements, though still high overall, become low for each individual behavior?

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Prior work indicates that multi-task RL can indeed amortize the cost of single-task learning. In particular, insofar as the tasks share common structure, if that structure can be discovered by the learning algorithm, all of the tasks can in principle be learned much more efficiently than learning each of the tasks individually. Such shared representations can include basic visual features, as well as more complex concepts, such as learning how to pick up objects. In addition, by collecting experience simultaneously using controllers for a variety of tasks with different difficulty, the easier tasks can serve to "bootstrap" the harder tasks. For example, the task of placing three food items on a plate may be difficult to complete if the reward is provided only at the end, but picking up a single food item is considerably easier. By learning these tasks together, the easier task serves to aid with exploration for the harder task. Finally, by enabling the multi-task RL policy to learn shared representations, learning new tasks can become easier over time as the system acquires more skills and learns more widely-useful aspects of the environment.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, to realize these benefits for a real-world robotic learning system, we need to overcome a number of major challenges, which have so far made it difficult to produce a large-scale demonstration of multi-task image-based RL that effectively accelerates the acquisition of generalizable real-world robotic skills. First, multi-task reinforcement learning is known to be exceedingly difficult from the optimization standpoint, and the hypothesized benefits of multi-task learning have proven hard to realize due to these difficulties. Second, a real-world multi-task learning framework requires the ability to easily and intuitively define rewards for a large number of tasks. Third, while all task-specific data could be shared between all the tasks, it has been shown that reusing data from non-correlated tasks can be harmful to the learning process. Lastly, in order to receive the benefits from shared, multi-task representation, we need to significantly scale up our algorithms, the number of tasks in the environment, and the robotic systems themselves.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main contribution of this paper is a general multi-task learning system, which we call MT-Opt, that realizes the hypothesized benefits of multi-task RL in the real world while addressing some of the associated challenges.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We address the challenge of providing rewards by creating a scalable and intuitive success-classifier-based approach that allows to quickly define new tasks and their rewards.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show how our system can quickly acquire new tasks by taking advantage of prior tasks via shared representations, novel data-routing strategies, and learned policies.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We find that, by learning multiple related tasks simultaneously, not only can we increase the data-efficiency of learning each of them, but also solve more complex tasks than in a single-task setup.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present our multi-task system as well as examples of some of the tasks that it is capable of performing in Fig. 1.

<!-- chunk {"id": "body-0012", "role": "body", "section": "System Overview", "weight": 1.0} -->

A high-level diagram of our multi-task learning system is shown in Fig. 2. We devise a distributed, off-policy multi-task reinforcement learning algorithm together with visual success detectors in order to learn multiple robotic manipulation tasks simultaneously. Visual success detectors are defined from video examples of desired outcomes and labelling prior episodes (Fig. 2A). These success detectors determine how episodes will be leveraged to train an RL policy (Fig. 2B). During evaluation and fine-tuning (Fig. 2C), at each time step, a policy takes as input a camera image and a one-hot encoding of the task, and sends a motor command to the robot. At the end of each episode, the outcome image of this process is graded by a multi-task visual success detector ($SD$) that determines which tasks were accomplished successfully and assigns a sparse reward 0 or 1 for each task. At the next step, the system decides whether another task should be attempted or if the environment should be reset. The above-described setup can scale to multiple robots, where each robot concurrently collects data for a different, randomly-selected task.

<!-- chunk {"id": "body-0013", "role": "body", "section": "System Overview", "weight": 1.0} -->

The generated episodes are used as offline data for training future policies (Fig. 2D) and are available to improve success detectors.

<!-- chunk {"id": "body-0014", "role": "body", "section": "System Overview", "weight": 1.0} -->

We develop multiple strategies that allow our RL algorithm to take advantage of the multi-task training setting. First, we use a single, multi-task deep neural network to learn a policy for all the tasks simultaneously, which enables parameter sharing between tasks. Second, we devise data management strategies that share and re-balance data across certain tasks. Third, since all tasks share data and parameters, we use some tasks as exploration policies for others, which aids in exploration.

<!-- chunk {"id": "body-0015", "role": "body", "section": "System Overview", "weight": 1.0} -->

In order to cope with a large, multi-task dataset, we build on many features of the distributed off-policy RL setup from QT-Opt, and extend it to leverage the multi-task nature of our data. In the following sections, we describe the details of different parts of this large scale, image-based distributed multi-task reinforcement learning based system.

<!-- chunk {"id": "body-0016", "role": "body", "section": "MT-Opt: a Scalable Multi-Task RL System", "weight": 1.0} -->

In this section, we describe our multi-task reinforcement learning method, MT-Opt, which amortizes the cost of learning multiple skills via parameter and data sharing.

<!-- chunk {"id": "body-0017", "role": "body", "section": "IV-A Multi-Task Reinforcement Learning Algorithm", "weight": 1.0} -->

We first introduce notation and RL fundamentals. We denote the multi-task RL policy as $\pi{(\left. \mathbf{a} \middle| {\mathbf{s},\mathcal{T}_{i}} \right.)}$, where $\mathbf{a} \in \mathcal{A}$ denotes the action, which in our case includes the position and the orientation of a robot arm as well as gripper commands, $\mathbf{s} \in \mathcal{S}$ denotes the state, which corresponds to images from the robot's cameras, and $\mathcal{T}_{i}$ denotes an encoding of the $i^{\text{th}}$ task drawn from a categorical task distribution $\mathcal{T}_{i} \sim {p{(\mathcal{T})}}$, which has $n$ possible categories, each corresponding to a different task.

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-A Multi-Task Reinforcement Learning Algorithm", "weight": 1.0} -->

At each time step, the policy selects an action $\mathbf{a}$ given the current state $\mathbf{s}$ and the current task $\mathcal{T}_{i}$ that is set at the beginning of the episode, and receives a task-dependent reward $r_{i}{(\mathbf{a},\mathbf{s},\mathcal{T}_{i})}$. As in a standard Markov decision process (MDP), the environment then transitions to new state $\mathbf{s}^{\prime}$. The goal of the multi-task RL policy is to maximize the expected sum of rewards for all tasks drawn from the distribution $p{(\mathcal{T})}$. The episode finishes when the policy selects a TERMINATE action or reaches a pre-defined maximum step limit.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A Multi-Task Reinforcement Learning Algorithm", "weight": 1.0} -->

Our goal is to learn an optimal multi-task Q-Function $Q_{\theta}{(\mathbf{s},\mathbf{a},\mathcal{T}_{i})}$ with parameters $\theta$, that estimates the expected sum of rewards that will be achieved after taking the action $\mathbf{a}$ in the current state $\mathbf{s}$ for the task $\mathcal{T}_{i}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-A Multi-Task Reinforcement Learning Algorithm", "weight": 1.0} -->

previously seen transitions $p{(\mathbf{s},\mathbf{a},\mathbf{s}^{\prime})}$. Similarly to, we use the cross-entropy method (CEM) to perform the stochastic optimization to compute the target value function.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-A Multi-Task Reinforcement Learning Algorithm", "weight": 1.0} -->

To extend this approach to the multi-task setting, let $\mathbf{s}^{(i)},\mathbf{a}^{(i)},\mathbf{s}^{\prime{(i)}}$ denote a transition that was generated by an episode $e^{(i)}$ for the $i^{\text{th}}$ task $\mathcal{T}_{i}$. As we discuss next, each transition could in fact be used for multiple tasks. In the multi-task case, using Eq.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-A Multi-Task Reinforcement Learning Algorithm", "weight": 1.0} -->

While this basic multi-task Q-learning system can in principle acquire diverse tasks, with each task learning from the data corresponding to that task, this approach does not take the full advantage of the multi-task aspects of the system, which we introduce next.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B Task Impersonation and Data Rebalancing", "weight": 1.0} -->

One of the advantages of using an off-policy RL algorithm such as Q-learning is that collected experience can be used to update the policy for other tasks, not just the task for which it was originally collected. This section describes how we effectively train with multi-task data through task impersonation and data re-balancing, as summarized in Fig. 3.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B Task Impersonation and Data Rebalancing", "weight": 1.0} -->

We leverage such experience sharing at the whole episode level rather than at the individual transition level. The goal is to use all transitions of an episode $e^{(i)}$ generated by task $\mathcal{T}_{i}$ to aid in training a policy for a set of $k_{i}$ tasks $\mathcal{T}_{\{ k_{i}\}}$. We refer to this process as task impersonation (see Algorithm 1), where the impersonation function $f_{I}$ transforms episode data collected for one task into a set of episodes that can be used to also train other tasks, i.e.: $e^{\{ k_{i}\}} = {f_{I}{(e^{(i)})}}$. Note that in general case $\{ k_{i}\}$ is a subset of all tasks $\{ n\}$, and it depends on the original task $\mathcal{T}_{i}$ that the episode $e^{(i)}$ was collected.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B Task Impersonation and Data Rebalancing", "weight": 1.0} -->

We introduce this term to emphasize the difference with the hindsight relabelling that is commonly used to generate additional successes in a goal-conditioned setting, whereas task-impersonation generates both successes and failures in a task-conditioned setup.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-B Task Impersonation and Data Rebalancing", "weight": 1.0} -->

First, we discuss two base choices for the impersonation function $f_{I}$, then we introduce a more principled solution. Consider an identity impersonation function ${f_{I_{\text{orig}}}{(e^{(i)})}} = e^{(i)}$, where no task impersonation takes place, i.e. an episode $e^{(i)}$ generated by task $\mathcal{T}_{i}$ is used to train the policy exclusively for that task. This baseline impersonation function does not take advantage of the reusable nature of the multi-task data.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-B Task Impersonation and Data Rebalancing", "weight": 1.0} -->

At the other end of the data-sharing spectrum is $f_{I_{\text{all}}} = e^{\{ n\}}$, where each task shares data with all remaining $n - 1$ tasks resulting in maximal data sharing. While $f_{I_{\text{orig}}}$ fails to leverage the reusable nature of multi-task data, $f_{I_{\text{all}}}$ can overshare, resulting in many unrelated episodes used as negative examples for the target task. This results in "dilution" of intrinsic negatives for a task. As we will show in Sec. VII-B, this can have disastrous consequences for downstream skill learning.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-B Task Impersonation and Data Rebalancing", "weight": 1.0} -->

To address these issues, we devise a new task impersonation strategy $f_{I_{\text{skill}}}$ that makes use of more fine-grained similarities between tasks. We refer to it as a skill-based task-impersonation strategy, where we overload the term "skill" as a set of tasks that share semantics and dynamics, yet can start from different initial conditions or operate on different objects. For example tasks such as place-object-on-plate and place-object-in-bowl belong to the same skill. Our impersonation function $f_{I_{\text{skill}}}$ allows us to impersonate an episode $e^{(i)}$ only as the tasks belonging to the same skill as $\mathcal{T}_{i}$. This strategy allows us to keep the benefits of data sharing via impersonation, while limiting the "dilution" issue. While in this work we manually decide on the task-skill grouping, this can be further extended by learning the impersonation function itself, which we leave as an avenue for future work.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-B Task Impersonation and Data Rebalancing", "weight": 1.0} -->

In our experiments, we conduct ablation studies comparing $f_{I_{\text{skill}}}$ (ours) with other task impersonation strategies.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-B Task Impersonation and Data Rebalancing", "weight": 1.0} -->

While training, due to the design of our task impersonation mechanism, as well as the variability in difficulty between tasks, the resulting training data stream often becomes highly imbalanced both in terms of the proportion of the dataset belonging to each task, and in terms of the relative frequencies of successful and unsuccessful episodes for each task, see Fig. 3B. We further highlight the imbalancing challenge in the Appendix, where Fig. 12 shows how much "extra" data is created per task thanks to the impersonation algorithm. In practice, this imbalance can severely hinder learning progress. We found the performance of our system is improved substantially by further re-balancing each batch both between tasks, such that the relative proportion of training data for each task is equal, and within each task, such that the relative proportion of successful and unsuccessful examples is kept constant.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-B Task Impersonation and Data Rebalancing", "weight": 1.0} -->

Task impersonation and data re-balancing functions work in sequence and they influence the final composition of the training batch. While this process might result in some transitions being drastically oversampled compared to others (if data for that task is scarce), the success and task re-balancing has a big positive impact on the task performance, which we ablate in our experiments.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-B Task Impersonation and Data Rebalancing", "weight": 1.0} -->

procedure fI(ei: original_episode)
S D {ki}← set of SDs relevant to task Ti
// ek: ei but with rewards for task Tk not Ti
expanded_episodes.append(ek) return expanded_episodes
Algorithm 1 Task Impersonation

<!-- chunk {"id": "body-0033", "role": "body", "section": "Rewards via Multi-Task Success Detectors", "weight": 1.0} -->

In this work, we aim to learn a discrete set of tasks that can be evaluated based only on the final image of an RL episode. This sparse-reward assumption allows us to train a neural-network-based success detector model ($SD$), which given a final image, infers a probability of a task being successful. Similarly to policy learning, we take advantage of the multi-task aspect of this problem and train a single multi-task success detector neural network that is conditioned on the task ID. In fact, we use supervised learning to train a similar neural network architecture model (excluding the inputs responsible for action representation) as for the MT-Opt multi-task policy, which we describe in more detail in the Appendix X-A.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Rewards via Multi-Task Success Detectors", "weight": 1.0} -->

To generate training data for the $SD$, we develop an intuitive interface with which a non-technical user can quickly generate positive examples of outcomes that represent success for a particular task. These examples are not demonstrations -- just examples of what successful completion (i.e., the final state) looks like. The user also shows negative examples of near-misses, or outcomes that are visually similar to the positive samples, but are still failures, such as an object being placed next to a plate rather than on top of it. We present example frames of such training data collection process in Fig. 4.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Rewards via Multi-Task Success Detectors", "weight": 1.0} -->

While this interface allows us to train the initial version of the multi-task $SD$, additional training data might be required as the robot starts executing that task and runs into states where the $SD$ is not accurate. Such out of distribution images might be caused by various real-world factors such as different lighting conditions, changing in background surroundings and novel states which the robot discovers. We continue to manually label such images and incrementally retrain $SD$ to obtain the most up-to-date $SD$. In result, we label $\approx {5,000}$ images per task and provide more details on the training data statistics in the Appendix, Fig. 14.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Continuous Data Collection", "weight": 1.0} -->

In this section, we present the data collection strategy that we utilize to simultaneously collect data for multiple distinct tasks across multiple robots. Our main observation w.r.t. the multi-task data collection process is that we can use solutions to easier tasks to effectively bootstrap learning of more complex tasks. This is an important benefit of our multi-task system, where an average MT-Opt policy for simple tasks might occasionally yield episodes successful for harder tasks. Over time, this allows us to start training an MT-Opt policy now for the harder tasks, and consequently, to collect better data for those tasks. To kick-start this process and bootstrap our two simplest tasks, we use two crude scripted policies for picking and placing (see Sec. X-B for details) following prior work. In addition, in order to simplify the exploration problem for longer-horizon tasks, we also allow the individual tasks to be ordered sequentially, where one task is executed after another. As such, our multi-task dataset grows over time w.r.t. the amount of per-task data as well as percentage of successful episodes for all the tasks.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Continuous Data Collection", "weight": 1.0} -->

Importantly, this fluid data collection process results in an imbalanced dataset, as shown on Fig. 5. Our data impersonation and re-balancing methods described above address this imbalance by efficiently expanding and normalizing data.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiments", "weight": 1.0} -->

The goal of our real-world experiments is to answer the following questions: How does MT-Opt perform, quantitatively and qualitatively, on a large set of vision-based robotic manipulation tasks? Does training a shared model on many tasks improve MT-Opt's performance? Does data sharing improve performance of the system? Can our multi-task data collection strategy use easier tasks to bootstrap learning of more difficult tasks? Can MT-Opt quickly learn distinct new tasks by adapting learned skills?

<!-- chunk {"id": "body-0039", "role": "body", "section": "VII-A Experimental Setup", "weight": 1.0} -->

MT-Opt provides a general robotic skill learning framework that we use to learn multiple tasks, including semantic picking (i.e., picking an object from a particular category), placing into various fixtures (e.g., placing a food item onto a plate), covering, aligning, and rearranging. We focus on basic manipulation tasks that require repositioning objects relative to each other. A wide range of manipulation behaviors fall into this category, from simple bin-picking to more complex behaviors, such as covering items with a cloth, placing noodles into a bowl, and inserting bottles into form-fitted slots. In the following experiments, we use a set of 12 tasks for quantitative evaluation of our algorithm. These 12 tasks include a set of plastic food objects and divided plate fixtures and they can be split into 'object acquisition' and 'object manipulation' skills. Our most general object acquisition task is lift-any, where the goal is to singulate and lift any object to a certain height. In addition, we define 7 semantic lifting tasks, where the goal is to search for and lift a particular object, such as a plastic carrot.

<!-- chunk {"id": "body-0040", "role": "body", "section": "VII-A Experimental Setup", "weight": 1.0} -->

The placing tasks utilize a divided plate where the simplest task is to place the previously lifted object anywhere on the plate (place-any). Harder tasks require placing the object into a particular section of a divided plate, which could be oriented arbitrarily. See Fig. 6 for a visualization of the tasks.

<!-- chunk {"id": "body-0041", "role": "body", "section": "VII-A Experimental Setup", "weight": 1.0} -->

All of the polices used in our studies are trained with offline RL from a large dataset, which we summarize in Fig. 5. The resulting policy is deployed on 7 robots attempting each task 100 times for evaluation. In order to further reduce the variance of the evaluation, we shuffle the bins after each episode and use a standard evaluation scene (see Appendix, Fig. 16), from which all of the 12 evaluation tasks are feasible.

<!-- chunk {"id": "body-0042", "role": "body", "section": "VII-B Quantitative and Qualitative Evaluation of MT-Opt", "weight": 1.0} -->

Fig. 7 shows the success rates of MT-Opt on the 12 evaluation tasks. We compare the MT-Opt policy to three baselines: i) single-task QT-Opt, where each per-task policy is trained separately using only data collected specifically for that task, ii) an enhanced QT-Opt baseline, which we call QT-Opt Multi-Task, where we train a shared policy for all the tasks but there is no data impersonation or re-balancing between the tasks, and iii) a Data-Sharing Multi-Task baseline that is based on the data-sharing strategy presented, where we also train a single Q-Function but the data is shared across all tasks. Looking at the average performance across all task, we observe that MT-Opt significantly outperforms the baselines, in some cases with $\approx 3 \times$ average improvement. While the single task QT-Opt baseline performs similarly to MT-Opt for the task where we have the most data (see the data statistics in Fig. 5), lift-any, its performance drastically drops (to $\approx {1\%}$) for more difficult, underrepresented tasks, such as lift-can.

<!-- chunk {"id": "body-0043", "role": "body", "section": "VII-B Quantitative and Qualitative Evaluation of MT-Opt", "weight": 1.0} -->

Note, that we are not able run this baseline for the placing tasks, since they require a separate task to lift the object, which is not present in the single-task baseline. A similar observation applies to QT-Opt Multi-Task, where the performance of rare tasks increases compared to QT-Opt, but is still $\approx 4 \times$ worse on average than MT-Opt. Sharing data across all tasks also results in a low performance for semantic lifting and placing tasks and, additionally, it appears to harm the performance of the indiscriminate lifting and placing tasks. The MT-Opt policy, besides attaining the $89\%$ success rate on (lift-any), also performs the 7 semantic lifting tasks and the 4 placing and rearrangement tasks at a significantly higher success rate than all baselines. We explain these performance gaps by the way MT-Opt shares the representations and data, and provide a more comprehensive analysis of these factors in the following experiments. Due to the offline nature of the experiment, this comparison does not take into account the fact that the data for all tasks was collected using the MT-Opt policy.

<!-- chunk {"id": "body-0044", "role": "body", "section": "VII-B Quantitative and Qualitative Evaluation of MT-Opt", "weight": 1.0} -->

Considering the significantly lower success rates of other methods, it is likely that if the data was collected using these approaches, it would yield much lower success rates, and the gap between MT-Opt and the baselines would further increase.

<!-- chunk {"id": "body-0045", "role": "body", "section": "VII-B Quantitative and Qualitative Evaluation of MT-Opt", "weight": 1.0} -->

To further illustrate the learned behavior, we present an example of a successful carrot grasping episode in Fig. 8, where the policy must work the carrot out of the corner before picking it up. The challenges of semantic lifting tasks are exacerbated in a small bin setting, where the objects are often crowded and pressed against the walls of the bin, requiring additional actions to retrieve them. In addition, we note that semantic picking and placing performance differs substantially between the different tasks. While this is due in part to the difficulty of the tasks, this is also caused in large part by the quantity of data available for each object. To examine this, we refer to Fig. 5, showing different amounts and type of data collected for various tasks. Tasks such as lift-carrot and lift-bottle, which have more data, especially on-policy data, have higher success rates than underrepresented tasks, such as lift-box. The performance of these underrepresented tasks could be further improved by focusing the data collection on performing them more often.

<!-- chunk {"id": "body-0046", "role": "body", "section": "VII-C Sharing Representations Between Tasks", "weight": 1.0} -->

To explore the benefits of training a single policy on multiple tasks, we compare the 12-task MT-Opt policy with a 2-task policy that learns lift-any and place-any. Both of these policies are evaluated on these two tasks (lift-any and place-any). We use the same $f_{I_{\text{skill}}}$ task impersonation strategy, and the exact same offline dataset (i.e. both policies use the data from the extra 10 narrower tasks, which is impersonated as lift-any and place-any data) without any on-policy fine-tuning, so data-wise the experiments are identical.

<!-- chunk {"id": "body-0047", "role": "body", "section": "VII-C Sharing Representations Between Tasks", "weight": 1.0} -->

Table I shows results of the comparison between 12-task and 2-task policies. The 12-task policy outperforms the 2-task policy *even on the two tasks that the 2-task policy is trained on*, suggesting that training multiple tasks not only enables the 12-task policy to perform more tasks, but also improves its performance on the tasks through sharing of representations. In particular, the 12-task MT-Opt policy outperforms the 2-task policy by $7\%$ and $22\%$ for the tasks lift-any and place-any, respectively. These results suggest that the additional supervision provided by training on more tasks has a beneficial effect on the shared representations, which may explain the improved performance of the 12-task policy on the indiscriminate lifting and placing tasks.

<!-- chunk {"id": "body-0048", "role": "body", "section": "VII-C Sharing Representations Between Tasks", "weight": 1.0} -->

Parameter Sharing Ablation (Success Rate)

<!-- chunk {"id": "body-0049", "role": "body", "section": "VII-D Data Sharing Between Tasks", "weight": 1.0} -->

To test the influence of data-sharing and rebalancing on the multi-task policy's performance, we compare our task impersonation strategy $f_{I_{\text{skill}}}$ introduced in Sec. IV-B to a baseline impersonation function that does not share the data between the tasks $f_{I_{\text{orig}}}$, as well as a baseline where each task is impersonated for all other tasks $f_{I_{\text{all}}}$ -- a maximal data sharing strategy. In our skill-based task impersonation strategy $f_{I_{\text{skill}}}$, the data is expanded only for the class of tasks having similar visuals, dynamics and goals. In addition to $f_{I_{\text{skill}}}$ task impersonation, we re-balance each training batch between the tasks as well as within each task to keep the relative proportion of successful and unsuccessful trials the same.

<!-- chunk {"id": "body-0050", "role": "body", "section": "VII-D Data Sharing Between Tasks", "weight": 1.0} -->

The results of this experiment are in Table II, with the full results reported in the Appendix, Table IV. Sharing data among tasks using our method of task impersonation and re-balancing provides significant performance improvement across all the evaluation tasks, with improvements of up to $10x$ for some tasks. The full data-sharing strategy performs worse than both the no-data-sharing baseline and our method, suggesting that naïvely sharing all data across all tasks is not effective. Because of our data-collection strategy, the resulting multi-task dataset contains much more data for broader tasks (e.g., lift-any) than for more narrow, harder tasks (e.g., lift-box), as shown in Fig. 5. Without any additional data-sharing and re-balancing, this data imbalance causes the baseline strategy $f_{I_{\text{orig}}}$ to attain good performance for the easier, overrepresented tasks, but poor performance on the harder, underrepresented tasks (see Table II, first row), whereas our method performs substantially better on these tasks.

<!-- chunk {"id": "body-0051", "role": "body", "section": "VII-D Data Sharing Between Tasks", "weight": 1.0} -->

Data Strategies Ablation (min, mean, max, mean of low data tasks)

<!-- chunk {"id": "body-0052", "role": "body", "section": "VII-E Using Easier Tasks to Bootstrap Harder Tasks", "weight": 1.0} -->

To explore question, we study whether learning an easier but broader task (lift-any) can help with a structurally related task that is harder but more specific (lift-sausage). We separate out the data for lift-sausage which (as shown in Fig. 5) consists of $5400$ episodes collected for that task (i.e. $4600$ failures and $800$ successes). In addition, there are $11200$ episodes of successful sausage lifting and as many as $740K$ failures that were collected during the lift-any task. Combining the lift-sausage data and the extra successes from lift-any yields $16600$ episodes ($12000$ successes and $4600$ failures). To investigate the influence of MT-Opt and task impersonation on the task-bootstrap problem, we compare our 12-task MT-Opt policy to a single-task policy trained on these $16600$ episodes. These include the exact same set of successful lift-sausage episodes as MT-Opt, but does not include the failures from other tasks.

<!-- chunk {"id": "body-0053", "role": "body", "section": "VII-E Using Easier Tasks to Bootstrap Harder Tasks", "weight": 1.0} -->

The single-task policy learned from the $16600$ episodes yields performance of $3\%$. MT-Opt, which uses impersonated successes and failures, achieves $39\%$ success for the same task, a $\approx 10 \times$ improvement. Both experiments use identical data representing successful episodes. The benefits of MT-Opt are twofold here. First, we leverage an easier lift-any task to collect data for the harder lift-sausage task. Second, the less obvious conclusion can be drawn based on the additional failures impersonated from all other tasks. This large set of failures, which often include successful grasps of non-target objects, when further re-balanced as described in Sec. IV-B, results in the significant boost in performance of this task. This demonstrates the value of both successful and unsuccessful data collected by other tasks for learning new tasks.

<!-- chunk {"id": "body-0054", "role": "body", "section": "VII-F Learning New Tasks with MT-Opt", "weight": 1.0} -->

MT-Opt can learn broad skills, and then further specialize them to harder but more specific tasks, such as lift-sausage. This retroactive relabelling of prior data is one way to learn new tasks including lifting objects of other properties such as size, location, color or shape.

<!-- chunk {"id": "body-0055", "role": "body", "section": "VII-F Learning New Tasks with MT-Opt", "weight": 1.0} -->

In addition, MT-Opt can learn new tasks via proactive adaptation of known tasks, even ones that are visually and behaviorally different than those in the initial training set. To demonstrate this, we perform a fine-tuning experiment, bootstrapping from the MT-Opt 12-task model described in Sec. VII-B. In particular, we use the MT-Opt policy to collect data for a previously unseen tasks of lift-cloth and cover-object tasks (see Fig. 8 bottom row for an example episode). Unlike the lift-sausage tasks from the above section, prior to starting collection of these new tasks, no episodes in our offline dataset can be relabelled as successes for these two new tasks.

<!-- chunk {"id": "body-0056", "role": "body", "section": "VII-F Learning New Tasks with MT-Opt", "weight": 1.0} -->

We follow the continuous data collection process described in Sec. VI: we define and train the success detector for the new tasks, collect initial data using our lift-any and a place-any policies, and fine-tune a 14-task MT-Opt model that includes all prior as well as the newly defined tasks. While the new tasks are visually and semantically different, in practice the above mentioned policies give reasonable success rate necessary to start the fine-tuning. We switch to running the new policies on the robots once they are at parity with the lift-any and place-any policies. After $11K$ pick-cloth attempts and $3K$ cover-object attempts (requiring $< 1$ day of data collection on 7 robots), we obtain an extended 14-task MT policy that performs cloth picking at $70\%$ success and object covering at $44\%$ success. The policy trained only for these two tasks, without support of our offline dataset, yields performance of $33\%$ and $5\%$ respectively, confirming the hypothesis that MT-Opt method is beneficial even if the target tasks are sufficiently different, and the target data is scarce.

<!-- chunk {"id": "body-0057", "role": "body", "section": "VII-F Learning New Tasks with MT-Opt", "weight": 1.0} -->

By collecting additional $10K$ pick-cloth episodes and $6K$ cover-object episodes, we further increase the performance of 14-task MT-Opt to $92\%$ and $79\%$, for cloth picking and object covering respectively. We perform this fine-tuning procedure with other novel tasks such as previously unseen transparent bottle grasping, which reaches a performance of $60\%$ after less than $4$ days of data collection. Note that in this experiment, we additionally take advantage of the pre-trained MT-Opt policy for collecting the data for the new task. Similarly to other ablations, collecting data using the two-task policy would yield lower success rate per task, leading to larger difference in performance.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented a general multi-task learning framework, MT-Opt, that encompasses a number of elements: a multi-task data collection system that simultaneously collects data for multiple tasks, a scalable success detector framework, and a multi-task deep RL method that is able to effectively utilize the multi-task data. With real-world experiments, we carefully evaluate various design decisions and show the benefits of sharing weights between the tasks and sharing data using our task impersonation and data re-balancing strategies. We demonstrate examples of new skills that the system is able to generalize to including placing into new fixtures, covering, aligning, and rearranging. Finally, we show how MT-Opt can quickly acquire new tasks by leveraging the shared multi-task representations and exploration strategies.
