<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Grasping with Chopsticks: Combating Covariate Shift in Model-free Imitation Learning for Fine Manipulation

Topics include Imitation learning, Robotics, Generalization, Learning, Chopsticks.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Billions of people use chopsticks, a simple yet versatile tool, for fine manipulation of everyday objects. The small, curved, and slippery tips of chopsticks pose a challenge for picking up small objects, making them a suitably complex test case. This paper leverages human demonstrations to develop an autonomous chopsticks-equipped robotic manipulator. Due to the lack of accurate models for fine manipulation, we explore model-free imitation learning, which traditionally suffers from the covariate shift phenomenon that causes poor generalization. We propose two approaches to reduce covariate shift, neither of which requires access to an interactive expert or a model, unlike previous approaches. First, we alleviate single-step prediction errors by applying an invariant operator to increase the data support at critical steps for grasping. Second, we generate synthetic corrective labels by adding bounded noise and combining parametric and non-parametric methods to prevent error accumulation. We demonstrate our methods on a real chopstick-equipped robot that we built, and observe the agent's success rate increase from 37.3% to 80%, which is comparable to the human expert performance of 82.6%.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although complex end effectors are inherently suited to fine manipulation due to fewer design constraints, simple tools are easier to study and deploy, and they are ubiquitous in industrial manipulators. With a *human-in-the-loop*, simple end effectors can also perform general fine manipulation. We choose chopsticks, a simple tool that is very familiar to humans, as an example to learn and automate fine manipulation strategies from human demonstrations. To that end, we have built an automated chopstick-equipped robot comprised of a 6DOF robot arm outfitted with a 1DOF actuated chopstick (Fig. 1). Our goal is to demonstrate autonomous superhuman chopstick dexterity with our robot.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The efficacy of chopsticks' design has inspired researchers to adapt them for diverse robotic applications, such as surgery, micro-manipulation, and meal assistance. However, chopsticks' practicality and generality in applications come at the cost of complexity to control. Their small, curved, and slippery tips require precise movements for grasping small and rigid objects such as a toy marble. Their limited allowance for failures makes them a suitably complex test case for evaluating fine manipulation tasks. Noticeably, humans have demonstrated impressive adaptability in teleoperating a robot equipped with chopsticks to pick up hard-to-grasp small objects. We aim to leverage human demonstrations to learn control policies using *imitation learning*. The challenge we face is further exacerbated by the lack of accurate models for our assembled robotic test-bed, a common constraint for fine manipulation tasks.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The lack of accurate models motivates our study of model-free imitation learning. Here, we have access to demonstration data but not to the expert's policy function or the environment's transition model. Under these conditions, supervised learning methods like *behavior cloning* learn a policy function by matching the expert's action distribution. Minimizing action distribution divergence, however, does not necessarily guarantee the recovery of parsimonious states that lead to task success. A learned agent can suffer from *covariate shift*, i.e., compounding errors in the action space that lead the agent to unseen states during test time. This problem can be especially detrimental for fine manipulation, the success of which critically depends on a few steps that usually occur near the end of a trajectory.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To remedy covariate shift, researchers have proposed *interactive* imitation learning methods, such as DAgger and DART, to query an expert *online* for corrective labels. DAgger rolls out a learned agent and asks the expert for labels on learner visited states, which can be computationally expensive and unnatural on a teleoperation interface. DART injects noise during data collection, disturbs expert teleoperation, and forces the expert to provide corrective labels. However, injecting noise during data collection can burden the expert: adding a small amount of random noise for our fine manipulation task, as DART suggests, would require the expert to spend $43\%$ more time on collecting data.^11^1Though $95\%$ of the noise injected resulted in at most $0.35^{\circ}$ deviation per joint, it lowered the expert success rate by $18\%$ and forced the expert to spend more time completing each trajectory.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

These challenges prompt us to address covariate-shift in model-free imitation learning in a *non-interactive* setting, where we have access to demonstration data but not to an interactive expert. Since covariate shift results from the interplay of single-step errors and their accumulation over time, our key ideas are to increase data support to address single-step errors, and provide corrective labels to address the accumulation of errors. Specifically, we provide: *Enhanced data support* by transforming the data to an object-centric frame that preserves the relative transformation between the end effector and object, while making training data denser around the *critical* region for grasp success.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Corrective labels by injecting noise* into the collected state, assuming the same action may serve as the *corrective label* for the deviated state. Thus, we implicitly enforce smoothness to the learned policy and tell the agent how to recover from deviated states.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Corrective labels by choosing a combination of parametric and non-parametric methods* that improve matching of the action distribution at unseen states. Because of our problem structure, a better match in action distribution leads to a higher likelihood of matching the state distribution, preventing error accumulation.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate our proposal's effectiveness on a physical robot equipped with chopsticks to pick up small cube- and ball-shaped objects, as shown in Fig. 1. Our proposed agent achieves 60% success rates picking up even the most challenging item, a small ball, whereas a naive behavior cloning agent has only a 12% success rate. Our agent achieves an 80% average success rate picking up all three objects tested, comparable to the expert human performance of 82%. We conduct ablation tests, visualize the resulting states' distribution, and observe a smaller covariate shift from our proposed agents. We also validate the generality of the noise injection method on several Mujoco simulated tasks.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our promising empirical results, based on pragmatic assumptions of data support and policy smoothness, open the door for further theoretical analysis of combating covariate shift. Furthermore, although we have focused on the *non-interactive* setting, our techniques directly transfer to the *interactive* setting, enhancing robustness while reducing user burden.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Transform: Increasing Data Support", "weight": 1.0} -->

Our goal is to develop an agent that can generalize from demonstration data to predict an action for any query state. However, we lack data support for some states (e.g., the "unseen state" during rollout). We propose to apply an invariant operator to transform the data, making it denser around the region of interest and thus increasing the data support.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Transform: Increasing Data Support", "weight": 1.0} -->

In manipulation, changing the frame of reference can significantly change the distribution of trajectories (Fig. 2). We could choose a *robot-centric* frame, where the robot base is the origin, or an *object-centric* frame, where the object location is the origin. We propose that using an object-centric frame can reduce the covariate shift and improve the policy generalization, especially for fine manipulation. The transformation to an object-centric frame would result in a denser distribution of trajectories near the origin where the object is located, increasing data support for this critical region that determines grasping success. Using an object-centric frame also allows the policy learned to be invariant to the translation of object location. This makes the learned policy more sample efficient when generalizing to novel object locations.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Noise: Generating Synthetic Corrective Labels", "weight": 1.0} -->

(a) Covariate shift: A learner roll out (black) deviates from the demonstration (red) and error accumulates.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B Noise: Generating Synthetic Corrective Labels", "weight": 1.0} -->

(b) Inject noise into the collected states and reuse the collected action as synthetic corrective labels.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B Noise: Generating Synthetic Corrective Labels", "weight": 1.0} -->

(c) Use non-parametric methods (like a k-NN) to return the agent to proper region when deviations occur.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Noise: Generating Synthetic Corrective Labels", "weight": 1.0} -->

Although the transformation technique we use improves the agent's success rate, we still observe significant deviations during test time that result in task failure (Fig. 3(a)). This is understandable because machine learning algorithms generally need exponentially more data for progressive improvement. Instead of naively collecting more data, we introduce corrective action labels that can help the agent recover from deviations. For example, Venkatraman et al. rolled out trained agents, collected their deviation states and used model-predictive control to generate corrective labels to go back to the demonstrated trajectory. Unfortunately, models sufficiently accurate for fine manipulation can be challenging to build.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Noise: Generating Synthetic Corrective Labels", "weight": 1.0} -->

We propose to generate *synthetic* corrective labels by injecting noise into the collected demonstration *states* ("deviated state") and reusing the collected action ("corrective labels"), thus not requiring access to an expert or a model. Unlike DART and DAgger, which emphasize collecting corrective labels for the states that the agent will visit during rollout (test state distribution), we hypothesize that we do not need to match the deviated states' distribution accurately. Instead, we need to collect enough corrective labels to *cover* the deviated states' distribution. Since we can generate labels for free without burdening an expert, we choose to generate labels for randomly sampled deviated states, thus simplifying the selection of states for which to generate synthetic corrective labels. Fig. 3(b) shows an example where we sample states around a demonstrated state and reuse the demonstrated action as synthetic corrective labels.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Noise: Generating Synthetic Corrective Labels", "weight": 1.0} -->

Researchers have injected noise into problems that reduce a high-dimensional input to a low-dimensional output, e.g., for classification and object recognition in visual and language domains. In these works, such tasks are invariant under a wide variety of transformations. However, our robotic manipulation task has *low-dimensional* states and actions, where the mapping learned may not be invariant to the noise. We provide two insights to justify why injecting noise can still be desirable.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B Noise: Generating Synthetic Corrective Labels", "weight": 1.0} -->

First, we apply a *small* amount of additive Gaussian noise to the demonstration state instead of a large amount that could pollute the data by mapping a state to a detrimental action. Inspired, which showed the effectiveness of noise injection for autoencoders by carefully tuning the magnitude of the noise, we generate Gaussian noise $\epsilon \sim {\mathcal{N}{(0,\sigma)}}$ to add to the collected states, where $\sigma$ is the covariance of the noise. For simplicity, we correlate the noise size $\sigma$ with the variance of the data.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B Noise: Generating Synthetic Corrective Labels", "weight": 1.0} -->

Second, because of the structure of our problem, the collected action can serve as the corrective label for the noise-injected deviated state. Our state and action representations both include the end-effector pose. Therefore, when an agent starts drifting from a demonstrated trajectory and enters a deviated state, our algorithm can teach it to return to the original trajectory by reusing the same action label. Injecting noise can also ensure the learned policy is smooth, which is desired since we assume the actions are Lipschitz continuous w.r.t the states.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-C Ensemble: Following the Expert Advice", "weight": 1.0} -->

We can reduce error accumulation at unseen states by choosing methods that more effectively match the action distribution. A neural network's optimization objective is limited to its training data and will not necessarily generalize well to unseen inputs. In contrast, non-parametric methods generate test outputs by combining the training data, their predictions must come from the training data and are therefore constrained. For example, a k-nearest neighbor ($\mathtt{k}\text{-}{\mathtt{N}\mathtt{N}}$) agent will not cause the robot to move its joint positions beyond the interpolation of its training data.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-C Ensemble: Following the Expert Advice", "weight": 1.0} -->

We use $\mathtt{k}\text{-}{\mathtt{N}\mathtt{N}}$ in conjunction with behavior cloning ($\mathtt{B}\mathtt{C}$). Specifically, our agent follows the $\mathtt{k}\text{-}{\mathtt{N}\mathtt{N}}$ predicted action if the query state deviates from the training data (Fig. 3(c)).

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-C Ensemble: Following the Expert Advice", "weight": 1.0} -->

By using the $\mathtt{k}\text{-}{\mathtt{N}\mathtt{N}}$ method, we are *forcing a known action* to a new unseen state during test time to ensure the action distribution during training and testing will match. For our manipulation task, the state and action both include the robot's end-effector pose. Sending a *known action* is equivalent to sending the agent to *a known state*, implicitly reducing the agent's deviation from training data, thus reducing covariate shift. However, nonparametric method's performance is subject to its distance function, which can be difficult to design for high-dimensional data.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-C Ensemble: Following the Expert Advice", "weight": 1.0} -->

The distance function for non-parametric methods serves two purposes: to evaluate the proximity of a query to the stored data points; and to weight and combine the expert labels. Our key observation is that requires only a rough estimate of the distance to decide whether a query state is far from the training data, and needs a carefully tuned distance function to assign weights to expert labels. Therefore, we propose to use a decision tree to invoke a $\mathtt{k}\text{-}{\mathtt{N}\mathtt{N}}$ agent *only* when the distance of the query state is far from its nearest neighbors and invoke a behavior cloning neural network agent otherwise.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-C Ensemble: Following the Expert Advice", "weight": 1.0} -->

By invoking $\mathtt{k}\text{-}{\mathtt{N}\mathtt{N}}$ only when the agent is far away, we bypass the need to carefully design a distance function for it, favor $\mathtt{B}\mathtt{C}$'s scalability with data when we are inside the training data distribution, and rely on $\mathtt{k}\text{-}{\mathtt{N}\mathtt{N}}$ to correct the agent's deviation when we are outside the training data distribution.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A Experimental Setup", "weight": 1.0} -->

We built a 6-DOF robot (Fig. 4(a)) equipped with a pair of chopsticks as its end effector in order to develop algorithms that control the chopsticks to pick up challenging objects: a cube with a $1$ cm edge length, a ball with a $2$ cm diameter, and another ball with $1.4$ cm diameter, as shown in Fig. 4(c). The kinematic model for our inexpensive hardware is not highly accurate since the robot is assembled from parts with joints that are not strictly rigid. Even with the best calibration, inaccuracies still accumulate along robot links and result in position errors ranging from 1 mm to 6 mm at the robot's end effector. This implies that the difference between the calculated chopstick tip position and its actual position is comparable to the radius of the small objects used in our experiments. For each object, we collected $500$ trajectories from an expert teleoperating the robot to pick up the object (Fig. 4(b)). The data collection setup is the same as in our previous work.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-A Experimental Setup", "weight": 1.0} -->

Our agent had access to the tracked location of the objects and the robot's end-effector pose. We defined success as *grasping* the objects using chopsticks, *lifting* them above the workstation, and *holding* them in the air for $1$ s. We evaluated the performance of each method on each object by computing the success rate over 25 trials. During evaluation, we divided the square workstation plate into a $5 \times 5$ grid (Fig. 4(c)) and placed the object in the center of each grid cell to ensure effective coverage over the entire workspace. See Appendix V-A for more details.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B Experimental Procedure", "weight": 1.0} -->

We compared our methods in Section II with human demonstrations during teleoperation ($\mathtt{E}\mathtt{x}\mathtt{p}\mathtt{e}\mathtt{r}\mathtt{t}$) and a replay of the successful demonstrations ($\mathtt{R}\mathtt{e}\mathtt{p}\mathtt{l}\mathtt{a}\mathtt{y}$). $\mathtt{R}\mathtt{e}\mathtt{p}\mathtt{l}\mathtt{a}\mathtt{y}$ tests the *repeatability* of our hardware. We chose successful demonstrations, placed objects at *exactly the same locations* used during data collection, and replayed the demonstrations to see if the robot could pick up the objects.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B Experimental Procedure", "weight": 1.0} -->

We used two baselines. The first is a parametric method, $\mathtt{B}\mathtt{C}$+$\mathtt{R}\mathtt{o}\mathtt{b}\mathtt{o}\mathtt{t}\mathtt{C}$, a neural-network based behavior cloning agent that uses the default robot-centric frame. The second is a non-parametric method, $\mathtt{k}\text{-}{\mathtt{N}\mathtt{N}}$+$\mathtt{R}\mathtt{o}\mathtt{b}\mathtt{o}\mathtt{t}\mathtt{C}$, which is a k-nearest-neighbor agent that also uses the robot-centric frame.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B Experimental Procedure", "weight": 1.0} -->

We evaluated three methods as described in Section II: using the object-centric frame to train behavior cloning and the k-nearest neighbors agents, $\mathtt{B}\mathtt{C}$+$\mathtt{O}\mathtt{b}\mathtt{j}\mathtt{C}$ and $\mathtt{k}\text{-}{\mathtt{N}\mathtt{N}}$+$\mathtt{O}\mathtt{b}\mathtt{j}\mathtt{C}$, respectively, injecting a small amount of Gaussian noise into the behavior cloning agent, $\mathtt{B}\mathtt{C}$+$\mathtt{O}\mathtt{b}\mathtt{j}\mathtt{C}$+$\mathtt{N}\mathtt{o}\mathtt{i}\mathtt{s}\mathtt{e}$, and combining the parametric method

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A Success Rates for Fine Manipulation", "weight": 1.0} -->

The experimental results are shown in Table. I, and the best performers in each column are highlighted. Our parametric method baseline, $\mathtt{B}\mathtt{C}$+$\mathtt{R}\mathtt{o}\mathtt{b}\mathtt{o}\mathtt{t}\mathtt{C}$, and nonparametric method baseline, $\mathtt{k}\text{-}{\mathtt{N}\mathtt{N}}$+$\mathtt{R}\mathtt{o}\mathtt{b}\mathtt{o}\mathtt{t}\mathtt{C}$, had relatively low success rates. However, the causes of their failures differ. $\mathtt{B}\mathtt{C}$+$\mathtt{R}\mathtt{o}\mathtt{b}\mathtt{o}\mathtt{t}\mathtt{C}$ has difficulty picking up objects that are placed farther away from the robot.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A Success Rates for Fine Manipulation", "weight": 1.0} -->

The agent tends to reach towards the wrong location after moving over a long distance to approach the object, highlighting the covariate shift's impact. In contrast, the $\mathtt{k}\text{-}{\mathtt{N}\mathtt{N}}$+$\mathtt{R}\mathtt{o}\mathtt{b}\mathtt{o}\mathtt{t}\mathtt{C}$ agent's poses look more similar to expert demonstrations. However, its trajectories are not smooth and sometimes end abruptly on top of the object without picking it up. This occurs because $\mathtt{k}\text{-}{\mathtt{N}\mathtt{N}}$ does not guarantee a smooth policy function; even after careful tuning of the distance function, it was challenging to eliminate the jerky motions. $\mathtt{k}\text{-}{\mathtt{N}\mathtt{N}}$'s sudden stops are due to direct imitation of the training data.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A Success Rates for Fine Manipulation", "weight": 1.0} -->

During demonstration, the human expert often slowed or even paused their movements around the object, adjusting the approaching pose before closing the chopsticks and lifting the object. The distance function we chose fails to select and mix the more relevant action labels. This confirms the sensitivity of $\mathtt{k}\text{-}{\mathtt{N}\mathtt{N}}$ to its distance function.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-A Success Rates for Fine Manipulation", "weight": 1.0} -->

Transforming to the $\mathtt{O}\mathtt{b}\mathtt{j}\mathtt{C}$ frame improved the success rates for $\mathtt{k}\text{-}{\mathtt{N}\mathtt{N}}$ and $\mathtt{B}\mathtt{C}$ by $20$% and $6.7$%, respectively. $\mathtt{k}\text{-}{\mathtt{N}\mathtt{N}}$ becomes less likely to generate jerky motions or stop since it benefits from the increased data support. $\mathtt{B}\mathtt{C}$ still suffers from covariate shift, but the agent has a higher likelihood of reaching towards the object due to denser data distribution near it.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-A Success Rates for Fine Manipulation", "weight": 1.0} -->

Injecting noise to $\mathtt{B}\mathtt{C}$+$\mathtt{O}\mathtt{b}\mathtt{j}\mathtt{C}$ during training increases its success rate by $28\%$. When the items are *close* to the robot, the agent has an almost $100\%$ success rate picking up even the most challenging item. For objects that are far away, the robot sometimes picks up the object by successfully reaching the location; at other time, it ends up merely rotating the chopsticks.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-A Success Rates for Fine Manipulation", "weight": 1.0} -->

Using a decision tree to combine our best parametric method ($\mathtt{B}\mathtt{C}$+$\mathtt{O}\mathtt{b}\mathtt{j}\mathtt{C}$+$\mathtt{N}\mathtt{o}\mathtt{i}\mathtt{s}\mathtt{e}$) and non-parametric method ($\mathtt{k}\text{-}{\mathtt{N}\mathtt{N}}$+$\mathtt{O}\mathtt{b}\mathtt{j}\mathtt{C}$) yields the highest performing agent that achieves near-expert performance. During test time, if a state's distance to its nearest neighbors exceeds a threshold, the agent triggers the non-parametric method to bring the state back. We observe that almost all rollouts trigger the non-parametric method at least once.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-A Success Rates for Fine Manipulation", "weight": 1.0} -->

No matter how far an object is placed, the $\mathtt{E}\mathtt{n}\mathtt{s}\mathtt{e}\mathtt{m}\mathtt{b}\mathtt{l}\mathtt{e}$ agent can reach it in a "standard" way that is similar to the pose demonstrated by the expert. Failures occasionally occur as the agent misses the grasping point by some sub-mm error.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Covariate Shift Across Methods", "weight": 1.0} -->

To gauge the covariate shift for different agents, we visualize the distributions of their test states. We collect 25 rollouts from each agent, record the robot-visited states, and plot the state distribution after dimensionality reduction using Principal Component Analysis (PCA), as shown in Fig. 5. First, we observe that $\mathtt{B}\mathtt{C}$ encounters more covariate shift than $\mathtt{k}\text{-}{\mathtt{N}\mathtt{N}}$, i.e., that states visited by $\mathtt{k}\text{-}{\mathtt{N}\mathtt{N}}$ are closer to the demonstrated states, confirming that a better matching of action distribution will lead to a better match of state distribution. Second, injecting noise into $\mathtt{B}\mathtt{C}$ results in less covariate shift than no noise, verifying that noise injection can provide effective correcting labels.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-C Noise Injection: Validation through MuJoCo Environments", "weight": 1.0} -->

We apply the noise injection method to MuJoCo simulated environments to test the method's generality. We use demonstration data, train $5$ behavior cloning agents under consecutive random seeds as baselines, and train another $5$ agents with noise injection for comparison. Figure 6 compares performances before and after noise injection. A paired T-test shows that $p < 0.05$ for all environments. There is strong evidence that, on average, noise injection improves the imitation learner.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-C Noise Injection: Validation through MuJoCo Environments", "weight": 1.0} -->

Though the performance gains for some simulated environments are not as significant as those we see for our real robot, we think the difference may be due to the demonstration source. We use "real" human data for our real robot experiment versus the "synthetic expert demonstration" generated by a reinforcement learning (RL) agent for the MuJoCo tasks. Human experts are known to exhibit multi-modal behaviors during demonstrations, whereas trained RL agents tend to have single modes in their reaction. Given that noise injection improves the success rate for our physical robot task by a considerable $28$%, further inquiry is needed to determine if noise injection is better at enhancing learning from multi-modal demonstration data.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Discussion", "weight": 1.5} -->

We leave some topics for future work. During noise injection, for simplicity, we experiment only with independent multivariate Gaussian noise with a ﬁxed size of covariance. It is worth exploring how to formalize the bounded noise and analyzing how different task domains may beneﬁt from different noise shapes. For the ensemble model, future work could explore an alternative way to switch between $\mathtt{k}\text{-}{\mathtt{N}\mathtt{N}}$ and $\mathtt{B}\mathtt{C}$ agents in the $\mathtt{E}\mathtt{n}\mathtt{s}\mathtt{e}\mathtt{m}\mathtt{b}\mathtt{l}\mathtt{e}$ model, perhaps by learning a threshold condition from the data.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our work critically depend on two key assumptions. First, to increase data support by applying an invariant operator, we assume the existence of a *critical* region that demands more data support. Second, to reuse collected action labels and leverage a nonparametric method to generate corrective labels, a more accurate match of action distribution should lead to a more accurate match of the states. The assumption holds if a part of the state and action representation is directly connected, e.g., the robot state contains its joint position, and the robot command accepts the target joint position. The assumption does not hold, for example, if the robot is torque-controlled; in these cases, further exploration on how a learner can generate synthetic corrective labels is needed.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Discussion", "weight": 1.5} -->

Nevertheless, our proposals do not assume access to a model or an interactive expert and are therefore more easily applicable to fine manipulation tasks. Compared to DAgger and DART, which collect corrective labels from experts, we can generate synthetic corrective labels for free. Because of the relatively lower cost of doing so, we generate labels for randomly sampled state distributions that *cover* the deviated state distribution without accurately *matching* it. Though our proposals focus on a non-interactive setting, they can directly transfer to an interactive one.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Discussion", "weight": 1.5} -->

We choose model-free imitation learning because an *accurate* model for fine manipulation is rare. However, it remains to be seen how to leverage an *inaccurate* model in imitation learning. This work is but a first step towards exploring general-purpose autonomous fine manipulation using simple tools. We look forward to extending it by combining model-free and model-based methods to manipulate a more diverse set of hard-to-grasp small objects.
