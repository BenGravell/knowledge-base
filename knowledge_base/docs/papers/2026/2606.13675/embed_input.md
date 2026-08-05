<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Improving Robotic Generalist Policies via Flow Reversal Steering

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Generalist policies can learn a wide range of skills from diverse robot datasets. In order to solve or improve on challenging new tasks, we need a way to infer and invoke the appropriate actions from the policy's rich behavioral prior, especially when directly commanding the policy fails. We focus on flow matching generalists and propose Flow Reversal Steering (FRS): a method that takes suboptimal but ``reasonable'' actions, finds their latent noises by passing them through the flow policy in reverse, and maps them to nearby generalist action modes. We evaluate FRS across many simulated and real-world manipulation settings. First, FRS can turn coarse semantic guidance from humans or vision-language models (VLMs) into corresponding good robot actions, improving zero-shot control. These gains can be distilled with behavioral cloning by training an auxiliary policy to output noises that the generalist maps to good actions - showing up to 95% absolute task success rate boosts in under a minute of training. Finally, FRS enables policy improvement by bootstrapping reinforcement learning with semantic knowledge, improving on several tasks that standard RL fails to improve .

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robotic foundation models trained on large and diverse datasets provide a powerful recipe for learning multi-task generalist policies. While such policies can often follow many commands, they will inevitably encounter new tasks diverging from their training data that require longer-horizon behaviors or demand adaptation through test-time trial-and-error. The standard recourse in such situations would be to simply add more demonstration data, retrain the generalist, and try again. However, we observe that the knowledge in these models goes beyond simply following instructions -- it provides a rich prior over reasonable behaviors. For example, a policy trained to interact with bowls, sponges, and towels has many of the skills needed when learning new kitchen-cleaning tasks, like wiping countertops or cleaning dishes. Effectively invoking appropriate actions from this prior would allow for rapid adaptation. The question then becomes: how do we best access the prior knowledge in generalist policies when faced with new tasks?

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Policy steering -- that is, guiding the action-sampling process to direct policy outputs to some desired end -- offers a way to use the generalist's "reasonable" action prior in novel tasks by upweighting relevant behaviors. In particular, steering could allow generalists to make use of knowledge from semantic reasoners, such as humans and large vision-language models (VLMs). For instance, when the policy is learning the novel task of cleaning a kitchen countertop, the knowledge that "sponges are used for wiping spills" could be used to steer the policy to reach for the sponge, instead of attempting other behaviors the robot could reasonably do in the scene. We thus want a steering method that is suitable for eliciting good actions from the generalist prior, based on semantic inferences.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many steering methods use diffusion or flow matching, a common parameterization for generalist policies. Notably, flow matching policies learn a deterministic map from noise to action that can be steered by finding the noise values that map to desirable actions within the generalist prior. However, the noise space of flow policies lacks immediately-apparent structure, so past works resort to expensive trial-and-error via reinforcement learning to find good noise values. To effectively steer generalist flow policies, we would instead ideally utilize semantic reasoning to quickly identify noise values that map to semantically-appropriate actions.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We thus propose Flow Reversal Steering (FRS): a novel approach that maps coarse reference actions to their noises by passing them through flow policies in reverse. When denoised, this yields actions that are fine-grained and "in-distribution" for the generalist, while staying roughly consistent with the reference action. Given even a rough sketch of robot behaviors (e.g., the general direction needed to reach for a target object), FRS can "project" that behavior into the generalist's prior to produce a similar fine-grained action.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This mechanism is especially useful for semantic reasoners, such as VLMs, that can roughly infer appropriate robot behaviors, but cannot ground them into dexterous low-level actions. FRS moves the onus of emitting robot actions to the generalist, while reasoners can focus on broad, high-level steering. As FRS also gives corresponding noise vectors, it meshes well with latent-noise policies, which steer flow generalists by changing their distribution of input noises. This can both enable fast and efficient adaptation via noise-space behavioral cloning (BC) and bootstrap noise-space reinforcement learning (RL) for tasks where exploring via the generalist policy is intractable.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate FRS on state-of-the-art generalist vision-language-action policies (VLAs ) through extensive simulated and real-world manipulation experiments. We show how FRS allows humans and VLMs to effectively guide generalists across diverse tasks, even by simply specifying just the rough direction the robot should move. Then, we show how the noises from FRS can be used for robustly learning tasks in just one minute of active BC training on 10 trajectories. Lastly, we find FRS speeds up noise policy RL, where using just one FRS success as prior data enables efficient improvement on tasks that the base VLA nearly always fails.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Related Works", "weight": 1.0} -->

Foundation models for robotics. Large pretrained foundation models can be applied in robotics in two ways: by fine-tuning them on robotic data or by querying them zero-shot. The former can involve training them with BC on large-scale demonstration datasets, with two popular approaches fine-tuning VLMs into vision-language-action models or video generators into world-action models. These policies are exposed to many robotic skills during pretraining, letting them follow many user commands. Vitally, this also captures a prior distribution over "reasonable" behaviors, often including behaviors needed to solve novel tasks the policies initially fail. FRS aims to flexibly elicit behaviors from this prior that are semantically appropriate for novel tasks, which in turn can be used for rapid adaptation and policy improvement. VLMs can also be trained into reward models for RL. This is orthogonal and complementary to our work, as using FRS for RL places no restrictions on the chosen reward function.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Related Works", "weight": 1.0} -->

Both actions and rewards can also be predicted by foundation models without training on robot data. VLMs can both invoke robot behaviors via predefined interfaces or act as reward functions. However, such methods are limited by VLMs' capabilities. While VLMs can effectively compose a limited set of high-level behavioral primitives, they struggle when given lower-level ones, thus giving a tradeoff between performance and flexibility. VLMs also struggle with reward modeling due to their limited fine-grained visual reasoning skills. Our method avoids this issue by relying on the generalist to produce actions. Instead, VLMs can make the high-level semantic inferences they excel, while FRS grounds this coarse feedback into appropriate actions.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Related Works", "weight": 1.0} -->

Diffusion policies and steering. Many generalist policies use diffusion or flow matching, which iteratively denoises Gaussian noise vectors to generate action samples. They can be steered by either modifying this denoising process or changing the partially-noised data inputs that get denoised. Notably, flow matching deterministically maps noise to outputs, so it can be steered by finding pure noises that denoise to good actions. However, finding good noises is challenging -- they are usually identified by trial-and-error with RL. In contrast, we propose combining flow reversal with coarse feedback to quickly identify effective noise. We show how flow reversal enables efficiently training policies that emit noises to steer the generalist toward solving new tasks, while obviating or accelerating the tedious process of discovering good noises via RL.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Related Works", "weight": 1.0} -->

Improving generalist policies. Past methods for improving generalists (like VLAs) with RL often have certain traits. When tuning the full VLA, RL methods tend to use supervised learning -- like distillation -- for policy extraction, avoiding needing action probabilities (which are hard to extract from flow models). They are often batched online, as their size makes true online RL unwieldy. To avoid this issue, other works train separate smaller policies with online RL, often using the base policy prior to constrain behavior to "reasonable" actions, e.g., via residual RL, behavior attenuation with classifier-free guidance, or treating the VLA as a latent action decoder. These policies can then be distilled into the generalist. Our method uses semantic feedback to elicit "reasonable" behaviors during generalist policy improvement, yielding gains beyond existing work which solely use the base policy as a behavior constraint.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Related Works", "weight": 1.0} -->

Flow and diffusion reversal in robotics. While flow or diffusion reversal is common in vision (App. A), fewer works use such techniques in robotics. GenPO inverts actions from a diffusion policy to estimate their likelihood for RL updates. Concurrent to our work, UniSteer inverts human actions via flow reversal to obtain "good" noises, which are used for noise-space RL by adding a behavioral cloning (BC) term. While similar, our approach diverges from these works in three key ways: we use flow reversal to steer generalist flow policies by refining coarse actions, admitting guidance from humans and scalable VLMs; we show how, even without RL, flow reversal enables efficiently training noise policies with just BC; and we show that flow reversal can bootstrap RL with coarse non-human guidance, even if the base policy nearly never succeeds.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Flow Reversal Steering (FRS)", "weight": 1.0} -->

Our method, Flow Reversal Steering (FRS), takes "coarse" actions and refines them using a generalist policy into similar, higher-quality actions. In Sec. 4.1 ‣ Improving Robotic Generalist Policies via Flow Reversal Steering"), we show how flow reversal can identify noises that bias the flow matching policy into sampling actions of the same mode as the coarse one. Then, in Sec. 4.2 ‣ Improving Robotic Generalist Policies via Flow Reversal Steering"), we consider how humans or VLMs can provide such coarse guidance to the robot, based on their semantic knowledge. Flow reversal converts these rough sketches of robot behaviors into in-distribution actions. Finally, in Sec. 4.3 ‣ Improving Robotic Generalist Policies via Flow Reversal Steering"), we present ways to use these semantically-guided trajectories to efficiently learn and improve at new tasks. See Fig. 3 ‣ Improving Robotic Generalist Policies via Flow Reversal Steering") for an illustrative overview.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Reversing the Flow Velocity Field", "weight": 1.0} -->

Since flow denoising is deterministic for a given input, flow can be reversed to determine the noise $a_{0}$ that corresponds to a given reference action $a_{1}$ by simply integrating the ODE it defines backwards in time. That is, using Euler integration: We denote this noising process as $\hat{a}_{0}\leftarrow\mu_{\theta}^{-1}(a_{1},o)$, as it inverts $\mu_{\theta}$, where the hat denotes a computed noise, not a sampled one. This does not modify the learned model $v_{\theta}$ at all -- flow reversal needs the same computations as standard flow denoising, just starting from an action instead of noise and swapping the order of integration. In turn, $\hat{a}_{0}$ can be passed through standard flow denoising to yield $\hat{a}_{1}\leftarrow\mu_{\theta}(\hat{a}_{0},o)$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Reversing the Flow Velocity Field", "weight": 1.0} -->

As $h\rightarrow 0$, this exactly reconstructs the reference $\hat{a}_{1}=a_{1}$. However, for finite iterations, integration error means that $\hat{a}_{1}$ only approximately reconstructs $a_{1}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Reversing the Flow Velocity Field", "weight": 1.0} -->

Empirically, we find that this results in reconstructed actions $\hat{a}_{1}$ being similar but not identical to the reference $a_{1}$, while also being "in-distribution" for BC policy $\pi_{\theta}$. This yields actions from the generalist that are biased towards reference behaviors, rather than perfectly reconstructing them. We call this Flow Reversal Steering (FRS).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Reversing the Flow Velocity Field", "weight": 1.0} -->

We show an illustrative example of FRS with an actual VLA in Fig. 3 ‣ Improving Robotic Generalist Policies via Flow Reversal Steering") (see App. B and Fig. 12 for more), using ten noising/denoising steps ($h=0.1$). The steered actions follow the same general direction as their respective coarse reference, albeit biased by the affordances in the scene -- e.g., when the gripper is above the table and empty, the steered actions tend to move down towards objects to grasp; Figure 4: Noising via the forward diffusion process vs. reverse flow integration. Both have the same marginals, but the former uses noise interpolation (so all signal is gone by t = 0), while the latter deterministically maps from data to noise and back. when the gripper is holding something, it tend to move up to lift the object or towards containers to place it. These are the "reasonable" actions internalized by the generalist policy.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Reversing the Flow Velocity Field", "weight": 1.0} -->

Note that flow reversal is distinct from the forward diffusion process, which linearly interpolates data with Gaussian noise $a_{t}=t\cdot a_{1}+(1-t)\cdot a_{0};\ a_{0}\sim\mathcal{N}(0,I)$. While this is used for training flow models, it rapidly destroys the information in the output, whereas flow reversal identifies the noise which deterministically maps to the reference action (Fig. 4 ‣ Improving Robotic Generalist Policies via Flow Reversal Steering")). Past works propose using forward diffusion for steering by partially noising reference actions, then passing them through denoising. However, we find these methods to be highly sensitive to how much noise is added, and thus hard to tune and ineffective (Sec. 5.2).

<!-- chunk {"id": "body-0020", "role": "body", "section": "High-Level Semantic Reasoning for Steering", "weight": 1.0} -->

We now consider sources of semantically-reasonable reference actions as inputs to FRS. Naturally, humans can guide robots to solve tasks, though standard methods, like teleoperation, are costly and tedious (though can also be used with flow reversal, see Sec. 4.3 ‣ Improving Robotic Generalist Policies via Flow Reversal Steering")). Similarly, VLMs can roughly identify appropriate robot high-level behaviors, even if they cannot emit fine robot actions. Thus, we need a way for these reasoners to tap into their semantic knowledge and easily ground it in coarse actions for guiding the robot.

<!-- chunk {"id": "body-0021", "role": "body", "section": "High-Level Semantic Reasoning for Steering", "weight": 1.0} -->

When running FRS online, we opt to have both human and VLM reasoners emit simple directional actions to guide the robot. That is, the reasoner can choose Cartesian directions based on how they think the manipulator's end effector should move (see App. D). This is programmatically turned into a rough steering action chunk that servos the robot straight in the specified direction. Unsurprisingly, such action chunks are ineffective when directly executed (Sec. 5.2), but are nonetheless suitable as reference actions $a_{1}$ for steering. Finally, both reasoners also have the option to defer to the base policy when steering is inappropriate, e.g., when executing precise grasps.

<!-- chunk {"id": "body-0022", "role": "body", "section": "High-Level Semantic Reasoning for Steering", "weight": 1.0} -->

The online FRS inference loop thus involves querying the human or VLM reasoner at each step to infer the general direction the robot should move; converting that motion into a corresponding directional reference action $a_{1}$; using flow reversal to map it back to noise $\hat{a}_{0}\leftarrow\mu^{-1}_{\theta}(a_{1},o)$; and denoising it back into an action to execute $\hat{a}_{1}\leftarrow\mu_{\theta}(\hat{a}_{0},o)$. This steers the generalist's action generation based on what the high-level reasoner infers to be useful for the task.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Improving Generalist Policies with FRS", "weight": 1.0} -->

Now that the reasoner can guide the robot toward semantically-sensible behaviors, how can this be used to improve performance? We propose three paradigms for using FRS to improve policies.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Improving Generalist Policies with FRS", "weight": 1.0} -->

Zero-shot online steering. The simplest way is to use FRS zero-shot, having the reasoner steer the policy every step. That is, each time the generalist policy would be queried during deployment, the human or VLM reasoner is queried to produce a semantically-meaningful coarse reference action, which is passed through flow reversal and denoising before being executed.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Improving Generalist Policies with FRS", "weight": 1.0} -->

However, constantly querying the reasoner can become expensive (especially for human reasoners), so we also aim to use FRS's elicited trajectories for learning. While these rollouts can work with any policy learning algorithm, it synergizes especially well with noise policy learning (Sec. 3). FRS yields noises immediately aligned with the coarse inferences of semantic reasoners, alleviating the usual difficulty of finding good noises with random trial-and-error when training noise policies via RL. This advantage enables two novel methods for efficient generalist policy learning with FRS.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Improving Generalist Policies with FRS", "weight": 1.0} -->

Supervised learning on FRS noise actions. We can treat flow reversal noises as "expert" noise actions for supervised learning, rather than RL. Given observation-noise pairs $(o,\hat{a}_{0})$ run BC: thereby distilling FRS's good noise actions into $\pi_{\phi}^{\text{noise}}(\hat{a}_{0}\mid o)$. At test time, it is treated exactly like a DSRL noise policy, inferring noises $\hat{a}_{0}$ at each step that get mapped to actions by the generalist $\hat{a}_{1}\leftarrow\mu_{\theta}(\hat{a}_{0},o)$. Naturally, we call this Diffusion Steering via Behavioral Cloning (DSBC).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Improving Generalist Policies with FRS", "weight": 1.0} -->

There are two ways to acquire the noises for supervising DSBC. First, we can use noises from online rollouts of zero-shot FRS collected as described above. As these noises have been denoised and executed, they are verified as mapping to good actions if they lead to task success. Second, DSBC can also be applied to existing robotic demonstrations. Given an observation $o$ and corresponding demonstrator action $a_{1}$, flow reversal can augment each frame with noise $\hat{a}_{0}\leftarrow\mu^{-1}_{\theta}(a_{1},o)$ approximately mapping to $a_{1}$, providing entirely offline data for DSBC. The lack of online execution yields a practical trade-off: as flow reversal does not perfectly reconstruct reference actions, offline DSBC does not ensure that reconstructed actions are free from suboptimality or error. However, this also permits precise reference actions from any suitable teleoperation or control interface.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Improving Generalist Policies with FRS", "weight": 1.0} -->

Bootstrapping RL with FRS. When used in conjunction with DSRL, FRS's noise trajectories can be used as prior data and behavior regularization via two simple changes. First, we augment the policy learning loss by adding an auxiliary DSBC loss over successful FRS rollouts, $\mathfrak{D}^{+}$. That is, rather than simply training $\pi_{\phi}^{\text{noise}}$ to maximize $Q^{\text{noise}}$ as standard DSRL does, we train $\pi_{\phi}^{\text{noise}}$ via: Second, we prefill DSRL's buffer $\mathfrak{B}$ with FRS trajectories (optionally including failed ones). This enables improvement from experience beyond zero-shot FRS and DSBC. We call this DSRL + FRS.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Improving Generalist Policies with FRS", "weight": 1.0} -->

These changes improve the efficiency of RL by encouraging the noise policy to explore around FRS's semantically-meaningful behaviors, contrasting the random noise sampling early in DSRL. Furthermore, since robot trajectories do not usually have noise actions, training noise policies with prior data is usually challenging or expensive and requires, for example, distilling robot action space Q-functions into noise action space. Flow reversal circumvents this by rapidly and cheaply identifying good underlying noises from reference actions, including from offline data.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments", "weight": 1.0} -->

We now evaluate Flow Reversal Steering by answering: Can FRS improve performance without any training by having VLMs guide generalists towards semantically-reasonable behaviors? Can we use the improved trajectories from FRS to rapidly learn new tasks? Can FRS help generalists more efficiently improve from experience? See App. E and App. F for more experimental details.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Simulation. We use LIBERO for scalable simulated evaluations. Our zero-shot results consider the full Spatial, Object, and Goal splits, as well as all 62 tasks in 90 that our base policy achieves $\leq$ 40% success on (Sec. 5.2). We then use a 15-task subset of LIBERO-90 where FRS achieves sufficient success to train DSBC policies (Sec. 5.3). Finally, we run DSRL + FRS on that subset, as well as a harder 10-task subset where the base policy nearly completely fails (Sec. 5.4). To allow room for improvement, we use base VLAs that have not been trained on the LIBERO splits that we run them, following Wagenmaker et al.. For LIBERO-90, we use OpenPi's $\pi_{0.5}$-LIBERO, which is trained on all splits except 90. For all others, we use $\pi_{0.5}$ fine-tuned by Jain et al., trained solely on 90. We focus on VLM steering to accommodate LIBERO's scale.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Real world. We also aim to validate FRS's effectiveness on real robots. We use the DROID setup to evaluate FRS in the real world, with $\pi_{0.5}$-DROID as our base flow VLA for steering. As DROID's primary challenge comes from its diversity, we choose a set of six task that require interacting with objects in scenes that admit many possible reasonable behaviors.

<!-- chunk {"id": "body-0033", "role": "body", "section": "FRS Boosts Zero-Shot Performance on Challenging Manipulation Tasks", "weight": 1.0} -->

We first test if using FRS to refine VLMs' semantic guidance can boost zero-shot performance.

<!-- chunk {"id": "body-0034", "role": "body", "section": "FRS Boosts Zero-Shot Performance on Challenging Manipulation Tasks", "weight": 1.0} -->

Comparisons. We compare FRS with several baselines. First, we run the base policy without steering, to confirm that applying FRS to that same policy improves performance. Second, to show that VLM actions alone are too coarse, we directly execute the VLM's actions, as is done in zero-shot control methods. Last, to show that FRS is good for steering, we compare with prior policy steering methods: partial noising, where reference actions are interpolated with Gaussian noise before being denoised, providing biased initializations for sampling (Sec. 4.1 ‣ Improving Robotic Generalist Policies via Flow Reversal Steering")); and sample-and-rank, where the policy samples multiple actions in parallel, ranks them post-hoc with a scoring function (in our case, cosine similarity with the VLM reference action), then executes the best one. For each split, all approaches use the same flow VLA as the base policy, the same VLM system prompt, and the same Gemini-ER-1.6 VLM. See Sec. E.1 and Sec. D.2.

<!-- chunk {"id": "body-0035", "role": "body", "section": "FRS Boosts Zero-Shot Performance on Challenging Manipulation Tasks", "weight": 1.0} -->

Results. As shown in Fig. 6, FRS outperforms the base policy. Critically, in 11 of the 42 LIBERO tasks where the base policy gets $\leq$ 2% (0 or 1 success out of 50 attempts), our method yields a substantial absolute success increase of at least 10%. While the base VLA may struggle to stumble upon even a single success, FRS allows VLMs to steer the policy towards meaningful behaviors, thereby providing much earlier rewards -- and thus, beneficial learning signals -- for RL (Sec. 5.4).

<!-- chunk {"id": "body-0036", "role": "body", "section": "FRS Boosts Zero-Shot Performance on Challenging Manipulation Tasks", "weight": 1.0} -->

We also find directly executing VLM actions is ineffective. This both supports the intuition that VLMs struggle with outputting precise low-level actions zero-shot and also shows how FRS is not simply reconstructing the VLM actions, but using them to steer towards better -- yet still semantically-similar -- fine-grained actions from the VLA. Finally, not only are partial noising and sample-and-rank less performant than FRS, they only boost 4 and 3 hard tasks, respectively. These baselines tend to work well when the VLA already has high probability on good behaviors, not on hard tasks where success is rare, while FRS is able to still learn in this case.

<!-- chunk {"id": "body-0037", "role": "body", "section": "FRS Enables Diffusion Steering via Behavior Cloning", "weight": 1.0} -->

We now show how good trajectories from FRS yield expert noise actions, which can be distilled via DSBC. We focus on online DSBC here, and present offline DSBC LIBERO results in Sec. E.2.2.

<!-- chunk {"id": "body-0038", "role": "body", "section": "FRS Enables Diffusion Steering via Behavior Cloning", "weight": 1.0} -->

Comparisons. We start by considering online DSBC on zero-shot FRS data. Alongside the base policy and zero-shot VLM FRS as baselines, we also compare against running standard BC on the FRS successful trajectories (using the same small architecture as the DSBC noise policy). We note that FRS's successful rollouts can be distilled back into the full VLA as well, but doing so uses much more compute than training an auxiliary policy. See Sec. E.2.

<!-- chunk {"id": "body-0039", "role": "body", "section": "FRS Enables Diffusion Steering via Behavior Cloning", "weight": 1.0} -->

Results. As shown in Fig. 6, DSBC distills the zero-shot gains of FRS, improving over the base VLA. One empirical benefit of DSBC is that when the noise policy makes mistakes and enters out-of-distribution states, it is often able to recover. We posit that, while the noise policy's actions may be bad at these OOD states, the VLA treats those noises akin to its noise prior, mapping them to "reasonable" in-distribution actions. Essentially, the DSBC noise policy is implicitly robust against compounding error, as it "falls back" to the VLA's behavioral prior in unfamiliar states. As DSBC can rely on the VLA's action prior, it is better to run BC on noise actions than regular actions. In LIBERO, DSBC outperforms standard BC (though, as LIBERO has little randomization, memorizing a small dataset can still work ). This difference is more salient in the real world, where standard BC with a small flow policy completely fails (Fig. 8).

<!-- chunk {"id": "body-0040", "role": "body", "section": "FRS Enables Diffusion Steering via Behavior Cloning", "weight": 1.0} -->

DSBC is also sample-, compute-, and time-efficient. In LIBERO, it trains on only 18 rollouts per task on average. On real robots, it needs just 10 rollouts per task to achieve high performance (Sec. 5.5). The policy is likewise small -- in total, training takes around 1 GB of GPU memory (as the VLA does not need to be loaded during training), whereas fine-tuning a full VLA requires hundreds of GBs. Finally, due to the model and data size, DSBC policies take under a minute to train.

<!-- chunk {"id": "body-0041", "role": "body", "section": "FRS Accelerates and Improves Reinforcement Learning", "weight": 1.0} -->

We finally aim to show how FRS can be used with RL to learn from experience. This allows it to surpass both the fixed performance of zero-shot FRS and distilling FRS's data with DSBC.

<!-- chunk {"id": "body-0042", "role": "body", "section": "FRS Accelerates and Improves Reinforcement Learning", "weight": 1.0} -->

Settings and comparisons. We run RL in two LIBERO-90 settings. First, we consider the 15 tasks from Sec. 5.3 where zero-shot VLM FRS is especially effective (yielding $\geq$`<!-- -->`{=html}10% improvement), and run DSRL + FRS by selecting 20 random FRS rollouts to prefill the replay buffer (in place of some initial prefill rollouts). Our baselines are thus two standard VLA RL methods that do not use FRS data: standard DSRL and residual RL (akin to PLD ). Second, we consider 10 harder LIBERO-90 tasks where the base VLA nearly always fails and zero-shot VLM FRS achieves only 8%. This tests if FRS is useful for RL, even if steering rarely succeeds. We thus run DSRL + FRS with only one successful steered trajectory, which can take upwards of 50 trials, given the tasks' difficulty. As densifying rewards is another way to guide RL with VLMs, we also compare against using RoboMeter as a reward model.

<!-- chunk {"id": "body-0043", "role": "body", "section": "FRS Accelerates and Improves Reinforcement Learning", "weight": 1.0} -->

All methods run RL on a small policy to steer a VLA, albeit in different ways. We thus control for the VLA, the small policy's architecture, and the underlying RL algorithm (SAC). See Sec. E.3.

<!-- chunk {"id": "body-0044", "role": "body", "section": "FRS Accelerates and Improves Reinforcement Learning", "weight": 1.0} -->

Results. DSRL + FRS is the most effective and sample-efficient RL method in both our LIBERO settings. As shown in Fig. 7 (left), running RL with FRS rollouts as prior data yields significant gains over standard RL, enabling both faster learning and higher final success rate across 15 tasks. For our second setting, where the base VLA has success rate near 0%, DSRL + FRS again enables effective improvement as Fig. 7 (right) shows. Naive DSRL struggles to learn -- only reaching a final success rate of around 30%, likely due to the poor performance of the base policy. By leveraging VLM FRS to direct the learner to successful behaviors in early stages of learning, DSRL + FRS is able to overcome this, quickly improving and converging to a significantly higher final success rate.

<!-- chunk {"id": "body-0045", "role": "body", "section": "FRS is Practical and Effective for Real-World Manipulation", "weight": 1.0} -->

Lastly, we show FRS is effective in real-world generalist manipulation (Fig. 8). As steering offloads the effort of producing fine actions to the policy, FRS lets humans solve tasks while only giving very crude feedback (i.e., one Cartesian directional action per action chunk), compared to the dense supervision provided during teleoperation. The successful human-steered trajectories can then be used for DSBC. Across six tasks that the base VLA struggles, we find that corresponding DSBC policies boost average absolute performance by 60% by training on just 10 successful human FRS rollouts per task. Equivalent standard BC flow policies trained on the FRS robot actions completely fail to learn these tasks in this data regime, as they cannot inherently rely on the VLA action prior in unfamiliar situations (see Sec. 5.3). As in the LIBERO DSBC experiments, each training run takes under a minute and requires around 1 GB of GPU memory.

<!-- chunk {"id": "body-0046", "role": "body", "section": "FRS is Practical and Effective for Real-World Manipulation", "weight": 1.0} -->

Lastly, we show how DSBC can be used to bootstrap trajectories for simple online RL, as we demonstrate on the challenging towel-hanging task by boosting performance from 5% base, to 50% via DSBC, and then to 80% post-RL (App. F).

<!-- chunk {"id": "body-0047", "role": "body", "section": "FRS is Practical and Effective for Real-World Manipulation", "weight": 1.0} -->

Real-world offline DSBC. Offline DSBC can use standard robotic trajectories (i.e., with only robot actions saved, and no noises), enabling learning with more optimal demonstrations than what is possible through a coarse steering interface. We test this with a real-world task that naïve directional steering struggles on due to imprecision. We collect 20 episodes of the task "hang the tape on the stand" via regular teleoperation (i.e., without noises). Then, we use $\pi_{0.5}$-DROID flow reversal to augment all episodes' actions with their corresponding noises, which DSBC learns. This noise outperforms the base VLA and standard BC, which struggles to learn precise, temporally-coherent behaviors in our low-data regime (Fig. 9). This validates flow reversal as a simple way for noise policies to make use of standard offline robot data without noises.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Discussion", "weight": 1.5} -->

We introduce Flow Reversal Steering (FRS), a way to convert coarse semantic guidance into precise actions by reversing flow generalist policies. Through extensive simulated and real-world tasks with state-of-the-art VLAs, we show how FRS allows reasoners, like humans and VLMs, to guide policies towards reasonable behaviors for novel tasks. This enables rapid policy learning through our novel Diffusion Steering via Behavior Cloning (DSBC) method or by bootstrapping DSRL. While we showed FRS's effectiveness, some parts are limited. We hope that FRS provides an alternative paradigm for efficiently improving generalist policies, where learning is not only guided by optimizing reward functions, but task-relevant semantic knowledge as well.
