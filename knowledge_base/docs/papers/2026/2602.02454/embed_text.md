## Introduction

Robots that learn by trial and error in the real world face an inherent constraint: physical interaction is expensive. Every policy update that depends on executing actions on hardware consumes operator time, risks wear-and-tear, and compounds safety concerns, especially for manipulation, where failures are frequent early in learning. This cost creates a fundamental bottleneck for scaling robot learning from interaction. As a result, many real-robot systems rely on alternatives that reduce or replace on-robot exploration.

One alternative is supervised learning (SFT) from expert demonstrations, where a robot is trained to imitate trajectories collected by teleoperation or scripted controllers. However, demonstration data tend to cover only a narrow slice of the long tail situations, and rarely expose the robot to the kinds of compounding errors and recovery behaviors needed for robust deployment. The second alternative is reinforcement learning (RL) in a software-based simulator. However, software simulators are costly to create for every new scenarios. Furthermore, they often suffer from the sim-to-real gap where visual features differ from real-world images.

Recent work have shown that world models learned from real-robot data can approximate real-robot execution outcomes. These models aim to predict how the visual world evolves under the robot's actions, effectively serving as an action-conditioned video simulator learned from real-world data. Compared to software simulators, video-based world models hold the promise of closing the visual gap and generalizing to a novel initial frame. However, it is unclear whether video world model offers more realistic physics than traditional simulators due to hallucinations. While evaluating physical realism is difficult, we instead tackle the end-to-end problem: does training robot policies inside a learned world model result in better real-robot performance than SFT or RL in a traditional simulator?

In this paper, we explore this question through the lens of large vision-language-action (VLA) policies that map images and language instructions to robot actions. Specifically, we propose World-Gymnast, a training framework that performs RL fine-tuning a VLA policy using a world model (Figure 1). Concretely, World-Gymnast uses the action-conditioned video generation model similar to Quevedo et al. as its world model, enabling the policy to generate imagined rollouts conditioned on action sequences sampled from the VLA and uses a vision-language model (VLM) to compute rewards from predicted video frames. The resulting rewards are used to perform policy gradient updates to the VLA policy. More importantly, World-Gymnast opens up many intriguing possibilities of RL training with a world model, including (i) RL training from an arbitrary image frame, (ii) test-time training on a novel initial frame, and (iii) online iterative world model and policy improvement.

Figure 1: Overview of World-Gymnast. The policy is trained on tasks specified by an initial frame and language instruction. During training, the policy outputs actions which are then passed to the world model (WorldGym ) which generates imagined rollouts. These rollouts are then passed to a VLM which returns a binary task completion reward. This reward is used to update the policy. Once trained, we evaluate the policy on real robots using the AutoEval setup. The resulting real world rollouts (frame-action sequences) from AutoEval can be further used to improve the world model on the particular environment.

We evaluate World-Gymnast on the Bridge robot platform through AutoEval, an automated real-robot evaluation platform open to public. Across a suite of manipulation tasks from AutoEval, we show World-Gymnast substantially outperforms SFT using the original Bridge data and RL in SIMPLER, a software simulator for Bridge created through real-to-sim techniques. Furthermore, since the world model only requires a single initial frame to perform rollouts, we demonstrate intriguing usage of the world model including training on novel language instructions and initial frames injected with distractor objects, test-time training from a real-robot frame, and iterative world model and policy improvement, all of which positively contribute to improved real-robot performance.

## Preliminaries

In this section, we define notations and review model-based RL. We then discuss how foundation world models and vision language models can serve as general dynamics and reward models under the model-based RL formulation.

### Markov Decision Process

We consider a multi-task, finite-horizon, partially observable Markov Decision Process (POMDP), specified by $\mathcal{M} = {(S,A,O,G,R,T,\mathcal{E},H)}$, which consists of state, action, observation, and task spaces, reward, transition, and emission functions, and horizon length. A policy $\pi$ interacts with the environment for a task starting from an initial state ${{g,s_{0}} \sim G},{o_{0} \sim {\mathcal{E}{(s_{0})}}}$, producing a distribution $\pi{( \cdot |o_{t},g)}$ over $A$ from which an action $a_{t}$ is sampled and applied to the environment at each step $t \in {\lbrack 0,H\rbrack}$. The environment produces a scalar reward $r_{t} = {R{(s_{t},g)}}$, and transitions to a new state $s_{t + 1} \sim {T{(s_{t},a_{t})}}$ and emits a new observation $o_{t + 1} \sim {\mathcal{E}{(s_{t + 1})}}$.

The value of a policy $\pi$ can be defined as the total expected future reward:

### Model-Based RL with Foundation Models

RL aims to maximize $\rho{(\pi)}$ through trial-and-error interactions between the policy and the environment. Model-based RL considers the setting where $T$ and $R$ are unknown and need to be estimated from samples from the environment, which can be an offline dataset logged from previous interactions $D = {\{{\tau_{i} = {g,s_{0},o_{0},a_{0},\ldots,s_{H},o_{H},r_{H}}}\}}$. Motivated by characteristics of a real-world system such as image based observations and high control frequencies, the learned model $\hat{T}{( \cdot |\mathbf{o},\mathbf{a})}$ can often take a sequence of previous image observations and a sequence of next actions. After $\hat{T}$ and $\hat{R}$ are estimated from data, a policy can perform rollout in the learned model

Recent work has shown that $\hat{T}$ can be parametrized using an action-conditioned video generation model (world model) while $\hat{R}$ can be parametrized using a vision-language model (VLM).

Policy gradient methods estimates the gradient of Equation 2 with respect to the policy $\pi$, and maximizes $\rho{(\pi)}$ directly via gradient ascent. The most commonly used gradient estimator has the form

where $\hat{A}$ is some advantage function that can be separately estimated via Monte-Carlo returns from $\pi,T,R$. With model-based policy gradient, these advantages can be estimated from Monte-Carlo samples from $\pi,\hat{T},\hat{R}$.

## RL with a World Model

In this section, we describe the RL algorithm World-Gymnast uses in Section 3.1. We then describe emerging training scenarios such as training on out-of-distribution (OOD) language and image in Section 3.2 and test-time training in Section 3.3. Lastly, we explain how World-Gymnast can be combined with classical algorithm such as Dyna to do online iterative world model and policy improvements.

### Model-Based GRPO with World Model Rollouts

To optimize the policy $\pi_{\theta}$ from Equation, World-Gymnast uses the learned world model $\hat{T}$ from Quevedo et al.. We adopt Group Relative Policy Optimization (GRPO), a policy gradient algorithm that estimates $\hat{A}$ using group-based score normalization.

For a given task instruction $g$ and an initial observation $o_{0}$, we generate a group of $K$ independent trajectories $\{\tau_{1},\ldots,\tau_{K}\}$ by rolling out the policy $\pi_{\theta}$ in the world model $\hat{T}$. Specifically, for the $k$-th trajectory, the policy samples an action $a_{t,k} \sim \pi_{\theta}{( \cdot |o_{t,k},g)}$, and the world model predicts the next observation $o_{{t + 1},k} \sim {\hat{T}{(o_{t,k},a_{t,k})}}$. This process repeats until the horizon $H$ is reached, yielding a trajectory $\tau_{k} = {(o_{0,k},a_{0,k},\ldots,o_{H,k})}$. Once the rollouts are complete, we employ a VLM $\hat{R}$ to assign a binary task completion reward to each trajectory $r_{k} = {\hat{R}{(\tau_{k},g)}}$. To compute the advantages, we treat the group of $K$ outputs as a baseline. We compute the mean and standard deviation of the rewards within the group:

The advantage for the $k$-th trajectory is then calculated via normalization:

where $\epsilon$ is a small constant for numerical stability. We assign the trajectory-level advantage to every time step $t$ within that trajectory. That is, ${\hat{A}}_{t,k} = {\hat{A}}_{k}$ for all $t \in {\lbrack 0,{H - 1}\rbrack}$. Finally, we optimize the policy $\pi_{\theta}$ using a PPO-style objective clipped based on the computed advantages. The loss function is defined as:

where ${r_{t,k}{(\theta)}} = \frac{\pi_{\theta}{(\left. a_{t,k} \middle| {o_{t,k},g} \right.)}}{\pi_{\theta_{old}}{(\left. a_{t,k} \middle| {o_{t,k},g} \right.)}}$ denotes the probability ratio.

Following the successful training setup of VLA training using RL in Li et al., we employ some of their techniques: 1) discarding the KL penalty term, 2) dynamic sampling to filter out groups with no variance in reward, 3) clipping higher in GRPO, and 4) using a higher temperature to sample actions during rollouts. These tricks helped stabilize training and improved exploration during training.

### Diverse Training Scenarios in the World Model

A world model pretrained on diverse datasets allows us to generate diverse training configurations (e.g., tasks and initial observations) using only images and langauge instructions. This provides greater flexibility than setting up software based simulations for each new configuration.We now explore an array of possibilities in training a policy in diverse configurations enabled by World-Gymnast.

### Training from Any Frame

We can train the policy with RL using any frames that are close enough to the world model's training distribution as the initial observation $o_{0}$, then rolling out the policy $\pi$, the world model $\hat{T}$, and the reward model $\hat{R}$ to provide learning signals on this initial configuration. This flexibility substantially increases the effective amount of training data available for RL in contrast to SFT which is bottlenecked by the amount of expert demonstrations. RL training from any frame also enables the policy to learn recovery behaviors, thereby improving the robustness of policies.

### Training on Novel Language Instructions

The training data can be further scaled by modifying the language instructions associated with the same initial frame. For instance, we can give a VLM an initial frame and ask for reasonable tasks for a robot to perform from that initial frame. We then give these reasonable tasks as language instructions to the VLA policy to evaluate the policy's performance on OOD language tasks and to further improve the policy on the OOD language tasks through RL. This enables the policy to be trained on new tasks and interact with objects previously present in the environment but not explicitly interacted . Previous work in policy evaluation had shown that pretrained VLA policies often fail at following OOD langauge instructions. We can overcome these limitations of VLAs with RL post-training in a world model.

### Training with Distractions

To improve policy's robustness to irrelevant visual clutter, we leverage image editing tools like Nano Banana to synthesize additional objects as distractors in the input image frames. Training the policy on diverse distractor objects encourages the policy to be more robust when such distractor objects are present during actual deployment and to have better performance in cluttered scenes. This can bridge the gap between robots that work in demos and robots that can work in anyone's messy household.

### Test-Time Training from a Novel Frame

Because World-Gymnast allows a policy to rollout from just an initial frame, when a novel frame is presented to a policy at test time, the policy can trade-off compute for improved policy performance by running RL training in the world model starting from the test frame. This allows rapid adaptation of the policy to novel scenes while avoiding the cost and risk of collecting real-world interaction data.

### Iterative World Model and Policy Improvement

When the visual observations encountered during policy rollouts deviate too much from the original training distribution of the world model, directly rolling out the policy in the world model might lead to compounding modeling errors. Inspired by classical Dyna-style algorithms, World-Gymnast allows an iterative training procedure in which the policy and world model are alternately refined. Specifically, the current policy can be rolled out (with inference-time scaling or test-time training using the world model as a reward function) to collect new environment interactions, which are then incorporated to further fine-tune the world model. The updated world model is subsequently used to generate improved imagined rollouts for policy optimization. This data flywheel enables the world model to progressively adapt to the policy-induced state distribution, while allowing the policy to benefit from increasingly accurate long-horizon predictions from the world model.

## Experiments

We now evaluate the performance of policies trained in World-Gymnast. We explain the experimental setup in Section 4.1, followed by comparisons to policies trained with software simulators and SFT in Section 4.2. We then demonstrate the capabilities of World-Gymnast in supporting diverse training from images with distractors, novel language instructions, and scaling the number of RL tasks in Section 4.3. Finally, we evaluate test-time scaling and iterative policy and world model improvement in Section 4.4 and Section 4.5.

### Experimental Setup

### Tasks and Pipeline

We evaluate the efficacy of World-Gymnast using the curated evaluation dataset used in Kim et al.. The dataset follows the BridgeData V2 setup with the WidowX robot and is designed to test policy generalization across visual, motion, physical, and semantic variations, as well as language grounding, over 17 tasks (Appendix C).

We further leverage the data scaling capabilities enabled by World-Gymnast, such as image editing, language augmentation, and novel task setups, to improve generalization of the trained RL policy. To train with World-Gymnast, a task just requires an initial frame and language instruction. During training, World-Gymnast rolls out the policy for up to 40 steps in WorldGym and a binary task completion reward is assigned to the rollout by GPT-4o.

Once training is complete, we evaluate the performance of the policy on WorldGym to estimate real robot performance and ensure policy is safe for testing, following its default configuration unless otherwise specified (Appendix A.4). We finally run the policy on AutoEval, a real-robot evaluation framework that currently supports 4 tasks across 2 setups. AutoEval evaluates each policy--task pair over 10 trials; we repeat this evaluation 5 times to estimate the standard error.

### Base Models

Successful RL finetuning requires a reasonably competent initial policy. To this end, we use OpenVLA-OFT as our base model. OpenVLA-OFT provides an optimized finetuning recipe to build on top of OpenVLA which was originally trained on Open X-Embodiment dataset. We use the BridgeData V2 to finetune our base model. Following the idea , we made several modifications to the official implementation of OpenVLA-OFT: 1) Disable the proprioception and secondary camera inputs to match the observation space used by our policy, 2) Use LLAMA-2 LM head as action head instead of the default L1 loss one to get action probabilities essential for RL. For WorldGym, we used a 600M parameter variant pretrained on Open X-Embodiment dataset.

### Training Details

For RL training, we use 4 NVIDIA H200 GPUs (140GB each) for full-parameter finetuning over 1--2 days. We use the following training parameters: learning rate $5 \cdot 10^{- 6}$, group size $8$, size of training batch $20$, length of action chunk $5$, clip ratio ($\epsilon_{high} = 0.28$, $\epsilon_{low} = 0.2$), temperature $1.6$. More detailed hyperparameter setup is available in Appendix A.4.

Open the drawer

Close the drawer

Put the eggplant into the blue sink

Put the eggplant into the yellow basket

Table 1: Real-robot success rate from AutoEval of World-Gymnast compared to running RL in a software simulator SIMPLER. RL with a world model significantly outperforms RL in a simulator in terms of real-robot success for 3 out of the 4 tasks.

### Evaluating RL with World-Gymnast

### Comparing World-Gymnast to a Software Simulator

We compare World-Gymnast against traditional simulator-based RL. We select SIMPLER, a real-to-sim policy evaluation framework, as our baseline since it provides the closest simulator-based approximation to the Bridge robot and tasks used in our evaluation. We train on all available tasks in SIMPLER (Appendix B.2) and further include digital twins for the AutoEval setup. When initializing RL from the base SFT policy, we observed low task completion rate in SIMPLER for all tasks except close the drawer, although the policy often moved in the correct direction but failed to fully complete the task. As a result, using a binary completion reward led to collapsed reward variance, preventing effective policy updates. To overcome this problem, we define the reward for a rollout as the sum of partial rewards from each step. We share more details of reward design in Appendix B.2.

World-Gymnast outperformed training with SIMPLER on all tasks except close the drawer, as shown in Table 1. For close the drawer task, the base policy has already performed pretty well prior to RL. It is worth noting that the RL training set for World-Gymnast does not include these tasks in the training set, whereas the SIMPLER baseline was also trained on these exact environment-task setups (the digital twins) and yet the policy exhibited poor transfer to real world.

Figure 2: Qualitative evaluation of policy rollouts in WorldGym with distractors. We compare rollout quality among SFT, World-Gymnast and World-Gymnast-Distract under visual distractions. The task on the left is put blue cup on plate and the SFT policy clearly picks up the wrong cup, while both World-Gymnast variants are able to correctly execute the task. On the right task (put carrot on plate), we can see SFT struggle again and seems to grab the dinosaur along with the carrot. Both World-Gymnast variants are again successful but World-Gymnast-Distract has better grasping and placing movements. It is worth noting that even with the visual artifacts introduced by the imperfect world model, the policies transfer effectively to the real robot setting.

Open the drawer

Close the drawer

Put the eggplant into the blue sink

Put the eggplant into the yellow basket

Table 2: Real-robot task success rate of World-Gymnast and supervised learning approaches. Standard errors are calculated between groups of 10 consecutive roll-outs.

### Comparing World-Gymnast to Supervised Learning

We also compare World-Gymnast with supervised fine-tuning methods. Following the recipe of OpenVLA-OFT, we fine-tune a OpenVLA 7B policy on expert trajectories from the Bridge V2 dataset for 20k steps. This policy, denoted as SFT in Table 2, is also the base model on which we conduct RL training. Recent works like Ctrl-World further utilize the world model for policy improvement by generating synthesized roll-outs filtered by a reward model as additional supervision. Similar to Ctrl-World, we roll out the base SFT policy in our world model for the same amount of steps as World-Gymnast did for RL training, and filtered for successful trajectories on OpenVLA evaluation tasks using a VLM. We then conduct another iteration of supervised fine-tuning with a mixture of data from Bridge V2 plus the successful synthesized roll-outs with a $1:1$ sampling rate. The resulting policy, denoted Iter-SFT in Table 2, is then evaluated on real world held-out tasks through AutoEval.

As shown in Table 2, World-Gymnast achieves the best performance compared with supervised learning and Iter-SFT, with a 18-fold and nearly 10-fold improvements from the base policy on *Put the eggplant into the blue sink* and *Put the eggplant into the yellow basket*, respectively. Notably, Iter-SFT improves slightly on the harder tasks, but the performance degrades on the easier ones. One possible explanation is that RL, through active exploration and on-policy updates, learns more generalizable behaviors. In contrast, iterative SFT may overfit to synthetic experience and is more vulnerable to world model hallucinations and inaccurate VLM success judgments.

### Evaluating Diverse Settings World-Gymnast Offers

### Evaluating Training with Distractors

We use Nano Banana to generate a new dataset using the pre-existing frames from the OpenVLA Bridge task suite. The new dataset adds random objects to distract the policy from successfully achieving the given task. We then train a new policy with RL (World-Gymnast-Distract) by including these new frames in the training data. Next, we evaluate the performance of SFT, World-Gymnast and World-Gymnast-Distract on a held-out set of distractor frames. WorldGym evaluations show World-Gymnast-Distract is the most robust, while SFT is the easiest to distract (Figure 2). Additionally, we evaluate World-Gymnast-Distract on the original OpenVLA tasks in WorldGym and observe improved success rates (Table 3). This indicates that adding distractor-augmented data improves performance not only under visual perturbations but also on the original tasks. Qualitative rollout comparisons in Figure 2 further illustrate that under visual distractions, World-Gymnast-Distract executes more reliable grasping and placement behaviors than SFT and World-Gymnast, while maintaining correct object grounding despite visual artifacts from the world model.

### Evaluating Training with Novel Language Instructions

Another approach to scaling data is augmenting language instructions in pre-existing tasks. We test this approach by creating 4 new tasks involving new interactions with objects already present in the scene. We combine this new data with the OpenVLA dataset and train a new policy, World-Gymnast-Language. Next we evaluate the performance of World-Gymnast-Language on the held-out split from OpenVLA data and observe that World-Gymnast-Language has improved performance over World-Gymnast (Table 3). This suggests that creating more tasks by introducing novel language instructions on existing frames can further improve the generalization performance of VLA policies.

Table 3: Comparing RL on diverse settings. Leveraging the diverse capabilities of world modeling, World-Gymnast allows significant improvement in the task success rates for multiple settings.

### Scaling the Number of Training Tasks

One advantage of World-Gymnast is its ability to train on a diverse set of tasks starting from any initial frame. To scale up data, we randomly selected 5 additional tasks from the Bridge dataset. We then train on these tasks in addition to the OpenVLA tasks and call this variant World-Gymnast-Scaled. We evaluate the performance of World-Gymnast-Scaled in WorldGym on the OpenVLA held-out task split and observed improvement compared to World-Gymnast, as shown in Table 3. These results suggest that World-Gymnast can effectively leverage additional training tasks to improve performance.

### Evaluating Test-Time Optimization

Pretrained policies often struggle at generalizing well to novel real world scenarios. While online data collection followed by finetuning can address this gap, it is prohibitively expensive in terms of time and effort. With a pretrained world model, we show that World-Gymnast improves the performance of a base policy through test-time training without real world roll-outs. Specifically, provided only with the initial observation and the task instructions of the 4 scenarios from AutoEval, we fine-tune our base policy with RL (details in Appendix A.4) using imagined roll-outs generated by the world model in a zero-shot manner from the testing frame. Test time training significantly improves the performance and robustness of close the drawer in the real world, improving the success rate from $62 \pm {6\%}$ success rate to $100 \pm {0\%}$ for the *Close the drawer* task. However, we noted that test-time training overfits the model to this single task, and performance in other tasks generally degrade. Test-time training across diverse tasks is an interesting venue of future work.

### Evaluating Iterative World and Policy Improvement

Figure 3: Qualitative comparison of rolling out the same action sequence on the real robot from AutoEval, from software simulator SIMPLER, from WorldGym, and from World-Gymnast with online world model updates. Rollouts from World-Gymnast adheres more closely to the real world than SIMPLER, suggesting improving the world model through Dyna improves the quality of the rollout.

A unique advantage of World-Gymnast is that the world model can be iteratively updated with real world roll-outs for initial frames that are out-of-distribution of the pretrained world model. During policy evaluation with AutoEval, we save the task instructions, observations, and action sequences to improve our world model. Iteratively, we collected around 100 trajectories per task for all 4 tasks, on which we finetune the world model for a total of 120k steps. Figure 3 provides a qualitative result demonstrating the improvement of the world model in playing a sequence of actions for *Open the drawer* task, which shows much less sim-to-real gap than SIMPLER and than WorldGym without online updates. Using the Dyna style world model updated with online data as an RL environment, World-Gymnast improves the success rate of the base RL model for close the drawer in AutoEval to $95\%$.

## Related Work

### Model-Based Reinforcement Learning

Model-based RL has long been studied in the RL literature, which learns a dynamics model from previously collected data and rolling out the learned dynamics model for policy evaluation and improvement. Much of the model-based RL research has been focusing on learning one dynamics model per system in the lower dimensional state space as opposed to in the pixel space, which, despite being a simpler modeling problem, limits knowledge sharing across systems. With large transformer architectures, learning image-based world models followed by RL has become plausible, but mostly in games or simulated domains with visually simplistic and abundant data. Our work differs from existing model-based RL in that we focus on using a single world model learned on broad data from many policies and tasks to train a generalist VLA policy on novel language instructions and scenes. We also directly tackle the sim-to-real gap by comparing against RL in traditional simulators, further showing the value of model-based RL where the model is learned from real-world data.

### Sim-to-Real RL

Reinforcement learning in physics-based simulations has been widely adopted to overcome the sample inefficiency of real-world training. To bridge the reality gap, prior works have relied heavily on domain randomization, which varies visual and physical parameters to cover real-world distributions, or domain adaptation. These strategies have achieved notable success in locomotion and rigid-body manipulation. However, traditional simulators face a scalability bottleneck for generalist manipulation: they require explicit object modeling, manual scene engineering, and struggle to faithfully render the diverse visual textures and deformable dynamics of the real world. Unlike these approaches, World-Gymnast leverages a world model learned directly from real-world data, effectively bypassing the need for manual asset creation and physics parameter tuning.

Video Generation for Robot Learning. Video-based learning for robotics has enabled visual representation learning, goal extraction, planning, and imitation from expert actions. Recent works reframe decision-making as a text conditioned video generation task, enabling policy learning from video predictions, and use generative models to simulate agent-environment interactions. Most of these work use generated video plans as visual actions and train separate inverse dynamics to extract robot actions from generated videos. While text-to-video generation can be effective for long-horizon planning, it is less clear how to self-improve these models that use video-generation as policies. We study the problem of using video generation solely as environment and using RL with generated rollouts to improve policy performance. Notably, World-Gymnast in principle can be used to improve any policies beyond VLA policies, including policies that are parametrized through video generation.

### Policy Evaluation using World Models

Recent work have shown that world models learned from real-robot data can approximate real-robot execution outcomes, and hence be used to evaluate robot policies. While evaluating policies in a world model is by all means an important application of world models, we focus on the end-to-end problem of improving policy performance using a world model, the effect of which can be tested on real robot.

### RL with a Video Based World Model

Our work is the most similar to Zhu et al. which uses RL to improve a policy in a video world model, but we focus on real-world evaluation with easily accessible evaluation settings using a open-source VLA policy (OpenVLA), world model (WorldGym), and evaluation platform (AutoEval). We also focus on exploring the emergent capabilities of RL in a world mdoel, including training from any initial frame with novel language instructions, test-time training, and iterative world model and policy improvement.

## Conclusion and Limitations

We have presented World-Gymnast, an RL framework for fine-tuning VLA policies using a learned world model. We show that existing training paradigms, including SFT and software-simulator-based RL, are expensive, restrictive, and often produce policies with limited generalization. In contrast, using a world model to rollout policies and VLM for reward is cheap, scalable and more robust to OOD scenarios.

A key advantage of world-model-based training is the ability to generate diverse training data from minimal inputs. Since World-Gymnast requires only an initial scene and a task description, it naturally supports data augmentation through image editing, language variation, and the reuse of scenes from novel environments. This flexibility further enables test-time training, planning, and iterative improvement of both the policy and the world model.

### Limitations

One limitation of World-Gymnast is that it cannot generalize to an arbitrary initial frame if the initial frame is far from the world model's training distribution. This calls for future research of pretraining robot world models on broad robot datasets. Another limitation of World-Gymnast is the reliance on a pretrained VLM for task success, which can produce hallucinations that leads to suboptimal RL training. Exploring ways to improve the reward model, such as training reward models, is an important future direction. Furthermore, utilizing dense rewards from VLMs and preventing reward hacking are also promising directions for future work.

## Impact Statement

This work introduces World-Gymnast, a framework for training robot policies within a generative world model. Our approach has the potential to democratize robotic research by reducing the dependency on expensive physical hardware and manual simulator engineering, thereby lowering the barrier to entry for developing capable generalist robots. While this method significantly mitigates the physical risks and costs associated with real-world training, we acknowledge that reliance on generative video models introduces the risk of policies exploiting hallucinated physics. Consequently, despite the improved sim-to-real transfer demonstrated in our results, policies trained in such environments should undergo rigorous safety verification before deployment in safety-critical real-world settings.
