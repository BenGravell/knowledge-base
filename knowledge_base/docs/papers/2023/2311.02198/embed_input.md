<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Imitation Bootstrapped Reinforcement Learning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Despite the considerable potential of reinforcement learning (RL), robotic control tasks predominantly rely on imitation learning (IL) due to its better sample efficiency. However, it is costly to collect comprehensive expert demonstrations that enable IL to generalize to all possible scenarios, and any distribution shift would require recollecting data for finetuning. Therefore, RL is appealing if it can build upon IL as an efficient autonomous self-improvement procedure. We propose imitation bootstrapped reinforcement learning (IBRL), a novel framework for sample-efficient RL with demonstrations that first trains an IL policy on the provided demonstrations and then uses it to propose alternative actions for both online exploration and bootstrapping target values. Compared to prior works that oversample the demonstrations or regularize RL with an additional imitation loss, IBRL is able to utilize high quality actions from IL policies since the beginning of training, which greatly accelerates exploration and training efficiency. We evaluate IBRL on 6 simulation and 3 real-world tasks spanning various difficulty levels. IBRL significantly outperforms prior methods and the improvement is particularly more prominent in harder tasks.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite achieving remarkable performance in many simulation domains, reinforcement learning (RL) has not been widely used in solving robotics and low level continuous control problems, especially in the real world. The main challenges of applying RL to continuous control problems are exploration and sample efficiency. In these settings, reward signals are often sparse by nature, and unlike learning in games where the sparse reward is often achievable within a fixed horizon, a randomly initialized neural policy may never finish a task, resulting in no signals for learning. Besides the hard exploration problem, RL often needs a large number of samples to converge, which hinders its adoption in the real world where massive parallel simulation is not available.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

As a result, most learning-based robotics systems rely on imitation learning (IL) or offline RL with strong assumptions such as access to large specialized datasets. However, those methods come with their own challenges. Expert demonstrations are often expensive to collect and require access to expert operators and domain knowledge. In addition, policies learned from static datasets suffer from distribution shifts when deployed in slightly different environments. Given these challenges, online RL algorithms -- when carefully integrated with IL -- can still play a valuable role in efficiently learning robot policies. An ideal RL algorithm for real world robotics applications should be able to benefit from human demonstrations and strong IL methods for sample-efficient learning. Moreover, it should go far beyond these IL techniques via self-improvement to reach higher performance or to address distribution shift.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The most straightforward way to use demonstration data in RL is to initialize the RL replay buffer with demonstrations and oversample those demonstrations during training. This approach does not leverage the fact that IL policies trained on the demonstrations can indeed provide more useful information -- they can output actions that may not be good enough to solve unseen scenarios, but can still provide some "lower bound" on the action quality when the initial RL actions are highly suboptimal. Another common approach is to pretrain the RL policy with human data and then fine-tune it with RL while applying additional regularization to ensure that the knowledge from demonstrations does not get washed out quickly by the randomly initialized critics. This approach requires balancing the primary RL loss and the secondary IL regularization loss to achieve maximum performance, which may require hyper-parameter tuning that is infeasible in the real world. Additionally, this necessitates using the same architecture to fit IL and RL data, which is undesirable in complex tasks as RL and IL may require very different architectures.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose *imitation bootstrapped reinforcement learning* (IBRL), a method to effectively combine IL and RL for sample-efficient reinforcement learning. IBRL first trains a separate, standalone imitation policy on the provided demonstrations with a powerful neural network that is much deeper than the ones normally used in online RL. Then IBRL explicitly uses this IL policy in two phases to accelerate RL training. First, during the online interaction phase, both the IL policy and RL policy propose an action and the agent executes the action that has a higher Q-value according to the Q-function being trained by the RL. Second, during the training phase of RL, the target for updating the Q-values again bootstraps from the better action among the ones proposed by either the RL or the IL policies. Similar to prior work, we also pre-fill the RL replay buffer with the demonstrations to provide learning signals before the policy collects its first online success. Fig. 1 illustrates the core idea of IBRL, and how an IL policy is explicitly integrated in the interaction and training phase of RL.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

By keeping the IL policy separate, IBRL does not need explicit regularization loss to prevent catastrophic forgetting and thus eliminate the need to search for proper hyperparameters to balance RL and IL. It also allows the IL to utilize deeper, more powerful networks that may be hard to train in RL with sparse reward. By explicitly considering actions from the IL policy, IBRL improves the quality of exploration and value estimation when the RL policy is inferior. It may also benefit from any potential generalizations of the IL policy in states beyond the limited demonstration data.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate IBRL on 6 simulation and 3 real-world robotics tasks spanning various difficulty levels. All tasks use sparse 0/1 reward. IBRL matches or outperforms strong existing methods on all tasks and the improvement is more significant in harder tasks. In particular, IBRL nearly doubles the performance over the second best method in the hardest simulation task evaluated in this paper. In a challenging real-world deformable cloth hanging task, IBRL performs 2.4$\times$ better than the second best RL method. In fact, prior methods are unable to even surpass the BC baseline after 2 hours of real-world training on this task.

<!-- chunk {"id": "body-0009", "role": "body", "section": "IV-A Core Algorithm", "weight": 1.0} -->

The core idea of IBRL is to first train an IL policy $\mu_{\psi}$ using expert demonstrations and then leverage this standalone reference IL policy in two phases in RL: 1) to help exploration during the online interaction, and 2) to help with target value estimation in TD learning (as shown in Fig. 1). We refer to the first phase as *actor proposal* and the second phase as *bootstrap proposal*.

<!-- chunk {"id": "body-0010", "role": "body", "section": "IV-A Core Algorithm", "weight": 1.0} -->

We focus our discussion on off-policy RL methods since they often have higher sample efficiency by effectively reusing past experiences as well as human demonstrations. Most popular off-policy RL methods for continuous control, such as Soft Actor-Critic (SAC) or Twin Delayed DDPG (TD3) involve training Q-networks to evaluate the action quality and training a separate policy network to generate actions with high Q-values. In IBRL, *actor proposal* generates additional actions alongside the RL policy to assist with exploration while *bootstrap proposal* accelerates Q-network training.

<!-- chunk {"id": "body-0011", "role": "body", "section": "IV-A Core Algorithm", "weight": 1.0} -->

Online Interaction: *Actor Proposal.* In sparse reward robotics tasks, such as picking up a block and receiving reward only when the block is picked up, randomly initialized Q-networks and policy networks may hardly obtain any successes even after a long period of interaction, resulting in no signal for learning. IBRL helps mitigate the exploration challenge by using a standalone IL policy $\mu_{\psi}$ trained on human demonstrations $\mathcal{D}$. IBRL uses this reference IL policy to propose an alternative action $a^{\text{IL}} \sim {\mu_{\psi}{(s)}}$ in addition to the action $a^{\text{RL}} \sim {\pi_{\theta}{(s)}}$ proposed by the RL policy at each online interaction step. Then, IBRL queries the target Q-network $Q_{\phi'}$ and selects the action with higher Q-value between the two candidates.

<!-- chunk {"id": "body-0012", "role": "body", "section": "IV-A Core Algorithm", "weight": 1.0} -->

That is, during online interaction, IBRL takes an action that provides the higher Q-value between the one proposed by the imitation policy $\mu_{\psi}$ and the one proposed by the RL policy $\pi_{\theta}$ that is being trained: This is the *actor proposal* phase of IBRL (Fig. 1 middle).

<!-- chunk {"id": "body-0013", "role": "body", "section": "IV-A Core Algorithm", "weight": 1.0} -->

Similarly, when computing the training targets for the Q-networks, instead of bootstrapping from $Q_{\phi'}{(s_{t + 1},{\pi_{\theta'}{(s_{t + 1})}})}$, we can bootstrap from the higher value between $Q_{\phi'}{(s_{t + 1},a_{t + 1}^{\text{IL}})}$ and $Q_{\phi'}{(s_{t + 1},a_{t + 1}^{\text{RL}})}$ where $a_{t + 1}^{\text{IL}}$ is sampled from the imitation policy while $a_{t + 1}^{\text{RL}}$ is sampled from the target actor $\pi_{\theta'}$: This essentially assumes that the future rollout will be carried out by a policy that always picks the action between $\{ a^{\text{IL}},a^{\text{RL}}\}$ with

<!-- chunk {"id": "body-0014", "role": "body", "section": "IV-A Core Algorithm", "weight": 1.0} -->

the higher Q-value for every time step, which is precisely the greedy version of the exploration policy in IBRL. We refer to this phase of IBRL as *bootstrap proposal* (Fig. 1 right).

<!-- chunk {"id": "body-0015", "role": "body", "section": "IV-A Core Algorithm", "weight": 1.0} -->

In summary, IBRL replaces the policy $\pi_{\theta}$ in vanilla RL algorithms with a hybrid policy ${\operatorname{argmax}_{a \in {\{ a^{\text{IL}},a^{\text{RL}}\}}}Q_{\phi'}}{(s,a)}$ in both inference and training. The idea of IBRL can be combined with any actor-critic style off-policy RL algorithm such as TD3 or SAC. In this paper, we use TD3 as our RL backbone because it has demonstrated strong performance and high sample efficiency in challenging RL from image settings. Similar to prior works, we initialize the replay buffer with demonstrations but do not oversample those demonstrations. We provide detailed pseudocode of IBRL with TD3 backbone in Appendix.

<!-- chunk {"id": "body-0016", "role": "body", "section": "IV-A Core Algorithm", "weight": 1.0} -->

Soft IBRL Variant. The discussion so far focuses on a greedy instantiation of IBRL that always selects the action with the higher Q-value. Although we find that this instantiation works well in practice -- especially in the realistic settings where the model processes raw pixels with deep image encoders -- it is worth noting that, in theory, this method may get stuck in a local optimum.

<!-- chunk {"id": "body-0017", "role": "body", "section": "IV-A Core Algorithm", "weight": 1.0} -->

Consider a tabular setting where the update of one $Q{(s,a)}$ does not lead to changes in other Q-values; then the Q-value of the optimal action $Q{(s,a^{\ast})}$ will never be updated if its initial value is smaller than $Q{(s,a^{\text{IL}})}$, leading to a suboptimal solution.

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-A Core Algorithm", "weight": 1.0} -->

This problem, however, can be easily circumvented by using a *soft* variant of IBRL that samples actions according to a Boltzmann distribution over Q-values instead of taking the $\operatorname{argmax}$, i.e., changing Eq. 1 of actor proposal to and changing Eq. 2 of bootstrap proposal to where ${p_{Q}{(a)}} \propto {\exp{({\beta Q{(s,a)}})}}$ for $a \in {\{ a^{\text{IL}},a^{\text{RL}}\}}$ with $\beta \geq 0$ being the inverse of the temperature that controls the sharpness of the distribution.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A Core Algorithm", "weight": 1.0} -->

Essentially, soft IBRL replaces the $\operatorname{argmax}$ operation with a $softmax$ to avoid the possibility of masking out optimal actions. In practice, we find this soft version works better than the normal IBRL in the state-based settings. However, this is not essential in the more realistic pixel-based settings, possibly because with deep image encoders, changing the Q-value for certain observation-action pairs will likely cause changes to the Q-values of many other correlated inputs, which brings sufficient stochasticity to the learning process and thus mitigates the masking effect. We demonstrate the effectiveness of soft IBRL in state-based experiments in Section V-C while using the normal $\operatorname{argmax}$ version for all pixel-based experiments due to its simplicity and the fact that it does not require additional hyperparameter tuning.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-B Benefits of IBRL", "weight": 1.0} -->

When using RL with access to prior demonstrations, recent work has shown that straightforward approaches such as oversampling the demonstrations as in RLPD or Hybrid RL and BC pretraining followed by RL with BC regularization on the policy in approaches such as ROT are powerful techniques that are commonly used in real world robotics settings due to their simplicity, performance, and robustness. In this section, we will discuss how IBRL's way of integrating IL with RL introduces additional important benefits in comparison to these methods.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B Benefits of IBRL", "weight": 1.0} -->

Automatic balancing between RL and IL policies. First, IBRL does not require picking hyper-parameters nor annealing schedules for the BC regularization weight. Unlike prior methods, IBRL does not need to worry about the IL policy being washed out in the early stage of training nor does it need to worry about the BC causing RL to be suboptimal in the later stage of training. In IBRL, the balance between IL and RL changes automatically as the policy and critic improves.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-B Benefits of IBRL", "weight": 1.0} -->

Leveraging IL in both exploration and training. The explicit consideration of IL actions during both exploration and training through the $\operatorname{argmax}$ operation (or $softmax$ in the soft variant) can lead to better exploration and training targets when the RL policy is underperforming. We show later that both actor proposal and bootstrap proposal are crucial for maximum sample efficiency in ablations.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B Benefits of IBRL", "weight": 1.0} -->

Modular and flexible architecture choices for IL and RL. The modular design of IBRL easily enables selecting the "best of both worlds" from an IL and RL perspective. For example, we can use different network architectures that are most suited for the RL and IL tasks respectively. In Section V-C, we show that the widely used deep ResNet-18 encoder that achieves strong performance in IL performs poorly as the visual backbone for RL, while a shallow ViT encoder that performs worse in IL works quite well in RL. IBRL's modular integration of RL and IL also allows different action representations for IL and RL, such as unimodal Gaussian for RL but mixture of Gaussians for IL. This opens an avenue towards integrating some more powerful IL methods with RL, which we leave for future research.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-C Architectural Improvements", "weight": 1.0} -->

Regularization with Actor Dropout. Many prior works have demonstrated the benefit of regularization in RL for continuous control. Additionally, as we discussed earlier, popular RL techniques that leverage prior data, such as oversampling demonstrations in training or adding BC regularization loss to policy update, implicitly introduce additional regularization to RL that has shown to be useful. We observe that regularizing IBRL with dropout in the policy network (actor) $\pi_{\theta}$, which we refer to as *actor dropout*, can further improve its stability and sample efficiency, especially in more challenging tasks where initial signals are noisy as successful episodes are less frequent. Although dropout has been previously applied in the *critic* to reduce overfitting on the value estimate, to the best of our knowledge, the application of dropout in *actor* has not been well-studied before. We find that adding actor dropout in IBRL significantly improves sample efficiency, even when other regularization techniques such as image augmentation (DrQ) or Q-ensembling (RED-Q) are also present.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-C Architectural Improvements", "weight": 1.0} -->

Moreover, actor dropout accelerates convergence without increasing the update-to-data (UTD) ratio and requires negligible extra compute.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-C Architectural Improvements", "weight": 1.0} -->

Improved Vision Encoder and Critic Designs. Prior online RL in continuous control works have mostly inherited the architecture from DrQ, which consists of shallow ConvNet followed by linear layers. Despite its strong performance in many settings, we find this architecture to be a major bottleneck in more challenging tasks. Meanwhile, naïvely applying common deep architectures without massive training data from parallel simulators leads to poor performance. Therefore, we introduce a new Q-network design with a shallow ViT style image encoder for learning from pixels, illustrated in Fig. 2. The general idea is to use Transformer layers so that relevant information from different parts of the image can be exchanged efficiently in a relatively shallow architecture that is expressive and yet easy to optimize. We first divide input images into *overlapping* patches and apply two convolution layers to get patch embeddings before feeding them into one Transformer layer. Then, we flatten the post-ViT patch embeddings in each channel and append the action and optionally proprioception data to each flattened channel before feeding them through an MLP to fuse this information.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-C Architectural Improvements", "weight": 1.0} -->

To reduce dimensionality of the features without using large linear layers, we multiply the feature matrix with learned spatial embeddings and sum over the channel dimension to get a 1-D vector before feeding them into the final Q-MLP. As TD3 utilizes two Q-heads for double Q-learning, we replicate the entire structure after the ViT for each Q-head. Similar to prior work, the actor is a fully connected network that takes the output of the ViT encoder as input. We show that this architecture greatly improves the performance of IBRL in complex manipulation tasks in Section V-C and show that it also improves baselines in the Appendix.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experiments in Simulation", "weight": 1.0} -->

We first conduct experiments in simulation environments to comprehensively compare IBRL against state-of-the-art methods in terms of performance and sample efficiency. We also perform ablations to understand the importance of different design choices.

<!-- chunk {"id": "body-0029", "role": "body", "section": "V-A Experimental Setup", "weight": 1.0} -->

Our evaluation suite consists of 4 tasks from Meta-World and 2 tasks from Robomimic. All environments use the sparse $0/1$ task completion reward at the end of each episode. The 4 Meta-World tasks are a subset of the tasks evaluated in MoDem. They span the medium, hard and very hard tiers of this benchmark as categorized. Since Meta-World does not come with human demonstrations, we use the scripted expert policies from to generate 3 demonstrations per task. Although we use harder-than-average tasks from Meta-World, these tasks are often simple, and additionally, scripted demonstrations are inevitably different -- much less noisy and cleaner -- than human demonstrations, making these tasks too simple to distinguish between some of the stronger methods. Robomimic is a well-established benchmark with significantly more complex tasks and demonstrations collected by human teleoperators. We use two test scenarios: a medium-difficulty task PickPlaceCan (Can) with 10 demonstrations and a hard task NutAssemblySquare (Square) with 50 demonstrations. As documented, the Square task is particularly challenging for RL as RL methods without demonstrations have been unsuccessful even with hand-engineered dense rewards and substantial tuning.

<!-- chunk {"id": "body-0030", "role": "body", "section": "V-B Implementation of IBRL and Baselines", "weight": 1.0} -->

IBRL uses TD3 for RL and BC for IL. The BC policies in all pixel-based experiments use a ResNet-18 vision encoder. We integrate common best practices for RL such as random-shift image augmentation in pixel-based RL and RED-Q in state-based RL to ensure best performance. Unless specified otherwise, IBRL always use actor dropout by default. Please see the Appendix for more implementation details and a complete list of hyper-parameters. We compare IBRL with three powerful baselines, RLPD, RFT and MoDem, that have been shown to outperform various other methods.

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-B Implementation of IBRL and Baselines", "weight": 1.0} -->

RLPD loads the demonstrations in the replay buffer and oversamples them during online RL such that 50% of the transitions in each batch come from demonstrations.

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-B Implementation of IBRL and Baselines", "weight": 1.0} -->

RFT (regularized fine-tuning) is a technique where the RL policy $\pi$ is first pre-trained with demonstrations and then fine-tuned with online RL. During RL, it adds a BC loss $\alpha\lambda{(\pi)}L_{\text{BC}}$ where $\alpha$ is the weight of the BC loss and $\lambda$ is an annealing schedule. We use the soft Q-filtering technique from Regularized Optimal Transport (ROT) to dynamically anneal $\lambda$. We use the best $\alpha = 0.1$ found through hyper-parameter sweeping.

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-B Implementation of IBRL and Baselines", "weight": 1.0} -->

RLPD and RFT share the same TD3 backbone as IBRL. In our experiments, unless otherwise specified, IBRL, RLPD, and RFT share the same non-algorithmic building blocks including network architecture, normalization, random-shift image augmentation, RED-Q, etc. We make these implementation decisions to ensure strong baselines and controlled comparisons against IBRL.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-B Implementation of IBRL and Baselines", "weight": 1.0} -->

MoDem is a model-based approach that pre-trains a policy with BC and uses it to generate rollouts which are then used to pre-train a world model and critic. We use the original open-source implementation of MoDem. For our Meta-World experiments, we generate the prior demonstrations differently from the original paper, but we have confirmed that our rerun of MoDem with these demonstrations performs better on average than the results reported in the original paper.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-C Overall Results on Meta-World and Robomimic", "weight": 1.0} -->

IBRL matches or exceeds baselines in Meta-World. In Meta-World, we focus on the core algorithmic contributions of IBRL. Therefore, we disable actor dropout for IBRL. We also *do not* use our ViT-based architecture for IBRL, RFT, and RLDP but instead use the widely adopted ConvNet architecture from DrQ to ensure a fair comparison with MoDem as it is complicated to tune network architectures for MoDem.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-C Overall Results on Meta-World and Robomimic", "weight": 1.0} -->

Fig. 3 shows the results of IBRL against three baselines in each Meta-World task separately as well as in aggregation (rightmost). IBRL and RFT universally outperform RLPD and MoDem across all tasks in terms of both sample efficiency and final performance, solving all tasks within 40K samples. RFT has a small advantage over IBRL in the early stage of training thanks to its pretrained encoder and policy network. However, IBRL catches up quickly and achieves high performance within the same amount of samples, significantly outperforming RLPD which is also randomly initialized. Because the tasks are relatively simple, the IBRL's advantage of integrating a more powerful IL model is less beneficial here, which may partially explain the similar performance between IBRL and RFT. However, it is worth noting that RFT requires additional tuning to find a proper range for the base regularization ratio $\alpha$. In contrast, IBRL has no additional hyper-parameters during the RL stage, making it more desirable for real world applications where large scale hyper-parameter search is infeasible. Lastly, the more complex MoDem method performs much worse than IBRL and the two simpler baselines.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-C Overall Results on Meta-World and Robomimic", "weight": 1.0} -->

Given that MoDem's computational cost is significantly higher than the other two baselines (10 hours for MoDem vs. 1 hour for the three model-free methods), we exclude MoDem in the more difficult and computationally intensive Robomimic experiments.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-C Overall Results on Meta-World and Robomimic", "weight": 1.0} -->

IBRL significantly exceeds baselines in Robomimic. In Robomimic, we run all methods with our new ViT-based architecture as existing architectures become a major bottleneck in Square, the most complicated task in our simulation experiments. We also run state-based experiments to demonstrate the effectiveness of IBRL in isolation from network designs. We run IBRL with actor dropout to highlight our empirical improvement upon existing strong baselines. The ablations over different components of IBRL are in the next section.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-C Overall Results on Meta-World and Robomimic", "weight": 1.0} -->

Fig. 4 shows the performance of IBRL alongside the two strong baselines, RLPD and RFT. IBRL outperforms the baselines across all four settings. The performance of the BC policy (gray dashed lines) illustrates the relative difficulty of the tasks. For example, Square (pixel) is much harder than Can (pixel); BC performs much worse in Square despite having $5 \times$ as much demonstration data as Can. In the relatively simpler Can (pixel) task, all three methods are able to eventually solve the task, but IBRL solves it with fewer interaction steps and more stable training. In the Square (pixel) task, IBRL is the only method that is able to solve it within 0.5M samples, while the baselines attain less than 60% success. In state-based setting, the improvement is even more striking as the existing methods fail to learn completely. Overfitting may be a major issue that leads to the failures of baselines in state-based experiments as we later see that their performance improves significantly after adding actor dropout, despite still being worse than IBRL.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-D Ablations on Robomimic", "weight": 1.0} -->

We perform ablations on the more challenging Robomimic tasks to understand the contribution of each components of IBRL. We first show that adding actor dropout to the baselines is not sufficient to match IBRL's performance. Then we ablate over the algorithmic components of IBRL and show that all of them contribute to its success. Finally, we show that our ViT-based architecture significantly improves sample efficiency and final performance for all RL methods.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-D Ablations on Robomimic", "weight": 1.0} -->

Actor dropout on baselines. To ensure that the advantage of IBRL over the baselines are not solely from actor dropout, we augment both RLPD and RFT with actor dropout and show their performance in Fig. 5. First of all, IBRL still outperforms the strongest variant among the four baselines, "RFT with Actor Dropout", showing that actor dropout is not the only reason behind IBRL's new SoTA performance. However, it is worth noting that actor dropout significantly improves RFT in both pixel- and state-based settings and RLPD in state-based setting. In the state-based setting, actor dropout essentially helps the two baselines solve the task, although at a lower sample efficiency than IBRL. Adding actor dropout to RFT essentially leads to a new approach that greatly surpasses existing methods excluding IBRL. This suggests that this technique should be considered for other methods beyond IBRL, especially considering that it adds negligible extra computational cost.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-D Ablations on Robomimic", "weight": 1.0} -->

Algorithmic components of IBRL. To understand the importance of key algorithmic components in IBRL, we perform ablations over actor proposal, bootstrap proposal, and actor dropout in Fig. 6. Overall, all three components are crucial for IBRL's strong performance. First, we can see that actor dropout is a powerful technique that improves sample efficiency and helps IBRL to escape sub-optimal solutions. Nonetheless, we emphasize that the core ideas of IBRL play a crucial role even when actor dropout is enabled: removing either the bootstrap proposal or actor proposal causes significant performance deterioration even when actor dropout is enabled. IBRL w/o Bootstrap Proposal shares a similar high-level structure to PEX, where a reference policy is used for proposing actions during exploration only. However, PEX trains the reference policy with offline RL and does not use actor dropout. IBRL is significantly less sample efficient without bootstrap proposal, indicating that using the IL policy in the target value computation leads to better training targets and faster convergence. We also verify the importance of the actor proposal; IBRL's performance decreases when removing actor proposal because it becomes less efficient at finding good actions in early stage of training.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-D Ablations on Robomimic", "weight": 1.0} -->

It is interesting to see that IBRL w/o Bootstrap Proposal performs worse than IBRL w/o Actor Proposal, which further emphasizes the importance of using the IL policy during training.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-D Ablations on Robomimic", "weight": 1.0} -->

Ablation of Network Architecture. We demonstrate the effectiveness of our ViT-based architecture in Fig. 7. In both tasks, our ViT architecture achieves better performance than the widely adopted DrQ network. The near zero performance of DrQ network in Square also reflects the difficulty of the task compared to the ones used in prior RL works. We also test the deep ResNet-18 encoder, the same one used in our BC policy, in RL. Note that this ResNet-18 replaces BatchNorm with GroupNorm as BatchNorm is known to cause RL to diverge when used with moving average target networks. Compared with the deeper and more computationally expensive ResNet-18, our proposed ViT architecture achieves better sample efficiency and final performance while also taking $50\%$ less wall-clock time to train. Although the ViT performs better in online RL tasks, we also see from Fig. 7 (dashed lines) that the higher capacity ResNet-18 still dominates in BC.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-D Ablations on Robomimic", "weight": 1.0} -->

Thus, we empirically confirm that BC and RL may prefer different architectures, which is reasonable given that the training goals are different (fitting behaviors in the training data vs. extrapolating to better behaviors while avoiding overfitting to unsuccessful early exploration data). Prior works such as RFT are forced to use the same architecture to fit both RL and demonstration data, which may limit their performance. In contrast, IBRL allows us to choose different architectures that are most suitable for RL and IL respectively, which echoes with one of the benefits of IBRL discussed in Section IV-B.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Real World Experiments", "weight": 1.0} -->

To fulfill IBRL's promise of performing sample-efficient policy improvement in real-world applications, we evaluate it on three real-world manipulation tasks of increasing difficulty and compare it against RFT and RLPD.

<!-- chunk {"id": "body-0047", "role": "body", "section": "VI-A Experimental Setup", "weight": 1.0} -->

We design three tasks named Lift, Drawer and Hang. The first two tasks use a Franka Emika Panda robot and the third task uses a Franka Research 3 robot. Both robots are equipped with a Robotiq 2F-85 gripper. Actions are 7-dimensional consisting of 6 dimensions for end-effector position and orientation deltas under a Cartesian impedance controller and 1 dimension for absolute position of the gripper. Policies run at 10 Hz. For each task, we collect a small number of prior demonstrations via teleoperation with an Oculus VR controller, and then run different RL methods for a fixed number of interaction steps. All methods use the exact same hyper-parameters and network architectures as in Robomimic tasks. We illustrate the three tasks in Fig. 8 and briefly describe them here.

<!-- chunk {"id": "body-0048", "role": "body", "section": "VI-A Experimental Setup", "weight": 1.0} -->

Lift: The objective is to pick up a foam block. The initial location of the block is randomized over roughly 22cm by 22cm-28cm trapezoid, which covers the entire area visible from the wrist-camera when the robot is at the home position. We collect 10 demonstrations for this task due to its simplicity. It uses wrist-camera images as observations.

<!-- chunk {"id": "body-0049", "role": "body", "section": "VI-A Experimental Setup", "weight": 1.0} -->

Drawer: The objective is to open the top drawer in a set of plastic drawers in a fixed position. The initial pose of the robot is randomized by adding noise up to 10% of the joint limit to each joint. We collect 30 prior demonstrations and use wrist-camera images as observations.

<!-- chunk {"id": "body-0050", "role": "body", "section": "VI-A Experimental Setup", "weight": 1.0} -->

Hang: The objective is to hang a deformable soft cloth on a metal hook. The initial location of the cloth is randomized over a roughly 28cm by 30cm rectangular region, and the hook is in a fixed position. The cloth is initialized so that its long side is roughly perpendicular to the hook. We use 30 prior demonstrations. This task uses third-person camera images as observations because the wrist-camera loses sight of the hook after picking up the cloth.

<!-- chunk {"id": "body-0051", "role": "body", "section": "VI-A Experimental Setup", "weight": 1.0} -->

As the primary goal of our real-world evaluations is to compare sample-efficiency and performance of various algorithms, we design rule-based success detectors and perform manual reset between episodes to ensure accurate reward and initial conditions. The details of the success detection and reset mechanism are in the Appendix. Note that sparse $0/1$ reward from the success detector is the only source of reward.

<!-- chunk {"id": "body-0052", "role": "body", "section": "VI-B Results", "weight": 1.0} -->

Fig. 8 shows the training curves of IBRL and baselines in the three tasks. Different tasks allow different interaction budgets based on their difficulty. The training curve measures the success rate of episodes between each 1000-step interval while the policy is being updated and exploration noise for action is enabled. Overall, we see that IBRL learns consistently faster than RLPD and RFT across all three environments and is the only method that is able to outperform BC in the most challenging Hang task under a 30K interaction budget.

<!-- chunk {"id": "body-0053", "role": "body", "section": "VI-B Results", "weight": 1.0} -->

We take the last checkpoints of each method and perform 20 evaluations. All methods are evaluated using the same set of initial conditions for fairness. Table I summarizes the results.

<!-- chunk {"id": "body-0054", "role": "body", "section": "VI-B Results", "weight": 1.0} -->

In Lift, we first evaluate all methods using a uniform distribution of initial positions of the block and then evaluate them in a "Hard Eval" setting where the block is initialized at the boundary such that only part of the block is visible from the wrist-camera at the beginning of each episode. IBRL achieves the highest score in both settings. In the hard setting, performance of all methods decreases, especially for BC whose performance drops to $0$ as it has not seen such cases in the demonstrations. However, IBRL still maintains a near perfect $95\%$ success rate as it learns faster during RL and thus has seen more different initial positions. This illustrates that IBRL is highly suitable for real-world policy improvement to combat potential distribution shifts or to tackle unseen cases during original data collection.

<!-- chunk {"id": "body-0055", "role": "body", "section": "VI-B Results", "weight": 1.0} -->

The Drawer task is more challenging than Lift as it requires grasping of the small drawer handle followed by a precise horizontal motion to open the drawer. We provide 30 demonstrations and run each method for 16K interaction steps. IBRL achieves the strongest performance at 95% success. From the learning curve in Fig. 8, we can clearly see that IBRL solves the task with far fewer samples. To verify this, we evaluate an "early stop" checkpoint after 10K interaction steps and find that IBRL already attains a perfect score while the baselines can only succeed in less than 15% of the time. In fact, RLPD and RFT still cannot fully solve this task even after 16K steps, making IBRL at least $40\%$ more sample efficient than the baselines in this task.

<!-- chunk {"id": "body-0056", "role": "body", "section": "VI-B Results", "weight": 1.0} -->

The Hang task is the hardest task as the robot must learn to pick the cloth up from the center and release it above the hook with enough precision so that the cloth rests on the hook and does not fall. We provide 30 demonstrations and run each method for 30K interaction steps. BC performs relatively well on this task because the demonstrations from the human expert are clean and always grasp and drop at the optimal location, which reduces the possible state space that the policy needs to handle. However, the deformable nature of the cloth makes it especially hard for RL as small differences in the grasp or drop locations may lead to drastically different outcomes that are hard to predict. Despite a significantly higher online interaction budget of 30K steps, RFT and RLPD are not able to even reach the performance level of BC. In contrast, IBRL exceeds the success rate of BC by $20\%$. Fig. 9 illustrates rollouts of BC and IBRL on two different initial conditions. In the top row, IBRL is able to solve the task with fewer steps than the BC policy. The bottom row shows a different scenario where BC fails to pick up the towel within the episode limit of 150 steps while IBRL can still solve the task.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Discussion", "weight": 1.5} -->

Summary. We present IBRL, a novel way to use human demonstrations for sample efficient RL by first training an IL policy and using it in RL to propose actions to improve online interaction and training time target Q-value estimation. We show that IBRL outperforms prior SoTA methods across 6 simulation tasks spanning wide range of difficulty levels and the improvement is particularly more significant in harder tasks. In real-world robotics tasks, IBRL also outperforms prior methods by a large margin in terms of sample-efficiency and final performance, making it an ideal solution for rapid real-world policy improvement to either improve upon an existing IL policy or help address performance deterioration caused by distribution shift. While we instantiated IBRL with specific choices of IL and RL algorithms, the framework is general and can in principle accommodate any IL method and off-policy RL method.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Discussion", "weight": 1.5} -->

Limitations and Future Work. In our real-world experiments, we focus on evaluating the performance of IBRL so we resort to manual reset to minimize noise from unsuccessful resets. A large scale deployment of IBRL in the real world should ideally enable autonomous reset, which we leave for future work. Additionally, the modular design of IBRL opens new avenues for integrating various IL methods with RL. An exciting direction for future research is to extend IBRL to take advantage of recent IL advancements such as diffusion policies or learning with hybrid actions for even better performance.
