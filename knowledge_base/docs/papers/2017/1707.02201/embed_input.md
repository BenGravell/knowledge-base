<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Human Behaviors from Motion Capture by Adversarial Imitation

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Rapid progress in deep reinforcement learning has made it increasingly feasible to train controllers for high-dimensional humanoid bodies. However, methods that use pure reinforcement learning with simple reward functions tend to produce non-humanlike and overly stereotyped movement behaviors. In this work, we extend generative adversarial imitation learning to enable training of generic neural network policies to produce humanlike movement patterns from limited demonstrations consisting only of partially observed state features, without access to actions, even when the demonstrations come from a body with different and unknown physical parameters. We leverage this approach to build sub-skill policies from motion capture data and show that they can be reused to solve tasks when controlled by a higher level controller.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The problem of building a programmable humanoid dates back centuries. In 1495, five years after drawing the Vitruvian Man, Leonardo da Vinci constructed a humanoid automaton in the form of an armored knight. The knight was able to wave, sit up, and open and close its jaw via power delivered by a crank. Unlike most clockwork automata, which could only produce movements along individual limit cycles, the mechanical knight could be re-programmed to vary its movements, enabling refinement of the arm movements or alternative sequences of movements in time.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

From a contemporary perspective, optimal control and reinforcement learning methods are enabling the design of movement controllers that can cope with the high-dimensionality of humanoid bodies, and neural networks are able to store multiple patterns of movement that can be reused, refined, and flexibly sequenced. Working towards a robust procedure for constructing controllers with a range of humanlike movements suited for reuse and refinement when employed in new tasks is the goal of this paper.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Yet current methods for humanoid control fall short of our desires. Methods that rely on pure reinforcement learning (RL) objectives tend to produce insufficiently humanlike and overly stereotyped movement behaviors. The uncanniness of these movements can be improved with meticulous body design (e.g. muscles), controller specialization (e.g. phase variables), and reward function engineering, but these methods require substantial domain expertise. Designing reward functions to capture the intricacies of humanoid behavior is difficult and must be repeated for every new behavior.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A compelling alternative to RL, commonly employed in the computer animation literature, is to use motion capture data as demonstrations to load movements into controllers. These methods typically produce visually pleasing, humanlike movements. However, existing methods for using motion capture come with caveats. Some of these methods use kinematic sequence models, and merely produce sequences of states (possibly violating physical constraints); some methods only produce tracking controllers for specific trajectories; other methods require heavily engineered components like cost functions that dictate how much to weight matching different features of the movement trajectory; yet others reduce model flexibility by designing the parameterizations of gaits or body-environment interaction.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In order to perform imitation learning from motion capture data, we make heavy use of generative adversarial imitation learning (GAIL; ), which is a recent breakthrough in imitation learning that produces an imitation policy in a manner similar to generative adversarial networks. State-action pairs from demonstration data are compared against state-action pairs from the policy. A classifier is trained to discriminate demonstration data from the imitation data, and the imitation policy is given reward for fooling the discriminator. The key benefit of GAIL over previously existing imitation-learning techniques is that the notion of similarity between imitation and demonstration data does not have to be defined based on an explicit, hand-designed metric.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we present a pipeline for training low-level controllers to produce behaviors from motion capture using an extension of GAIL; and embedding the low-level controllers into larger control systems wherein a high-level controller learns by RL to modulate the low-level controller to solve new tasks (Figure 1). The acquisition of multiple behaviors from noisy motion capture data ("real-to-sim\") requires two extensions to the GAIL framework. The original presentation of GAIL was restricted to imitation of single skills from complete state-action trajectories, where the demonstrator shared the same body and policy parameterization as the imitator. We demonstrate: (a) partial state featurizations without demonstrator actions suffice for adversarial imitation; (b) the body structure and physical parameters (i.e. body dynamics) need not match between the demonstrator and the imitator; and (c) robust transitions between behaviors naturally emerge by training on multiple behaviors.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Taken together, our approach produces reusable humanlike skills extracted from very small quantities of noisy human motion capture demonstrations without a great deal of domain engineering.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Methods", "weight": 1.0} -->

Adversarial imitation learning: Ho and Ermon show that their approach, GAIL, encourages the imitator to match the state-occupancy distribution of the demonstrator. In that work, demonstration data were generated by training a first policy via RL on a task with a hand-designed reward function, logging trajectories, and training a second policy of the same architecture as the first to imitate it by GAIL. While impressive, those results constitute a validation of the algorithm in the most favorable setting -- the same body, simulator, and policy architecture are used to produce demonstrations as are used for imitation. In this paper, we demonstrate that adversarial imitation learning can work even when the discriminator only has access to states (not actions) as well as partial state observations. Furthermore, for observed features that are sufficiently invariant across bodies, we do not need to know the underlying physical parameters or dynamics of the body that gave rise to the observations, allowing imitation in more general contexts.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Methods", "weight": 1.0} -->

We describe our variant of generative adversarial imitation learning (GAIL, ). We extend GAIL to settings where we have only partial observations of state or features thereof, excluding actions, and provide a context label to the discriminator to allow for training of multiple behaviors simultaneously (which allows for robust transitioning between behaviors, see Results). We present the architecture diagrammatically in Figure 2 and the algorithm as pseudocode (Algorithm 1).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Methods", "weight": 1.0} -->

We parameterize a stochastic policy with a neural network which generates a Gaussian distribution for each actuator, from which actions are sampled. Both the mean and log-standard-deviation of the action model are trainable. To train this policy, we use the adversarial imitation learning algorithm. Each iteration consists of three essential steps: collect data using the current policy; update the policy using rewards determined by the discriminator; update the discriminator using the demonstration data and generated data. As, policy updating is performed by trust-region policy optimization (TRPO; ). TRPO is particularly convenient in this case due to robustness and its need for only limited hyperparameter tuning, which allows hyperparameter searches to focus on GAN-related hyperparameters (e.g. the relative rate of discriminator updating).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Methods", "weight": 1.0} -->

In contrast to the common practice for GAN training, we found that updating the policy with a reward proportional to $- {\log{({1 - {D{( \cdot )}}})}}$ worked better than a reward proportional to $\log{({D{( \cdot )}})}$. Other details of policy training are provided in the supplement.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Methods", "weight": 1.0} -->

Input: Set of demonstration observations {ztd, ctd}t = 1 … Td
Randomly initialize policy (πθ) and discriminator (Dϕ)
// Perform N training iterations of policy &amp; discriminator updating
Execute policy rollouts to collect Tg timestep observations, {ztg, ctg}t = 1 … Tg
Compute rewards {rt = −log (1−Dϕ (ztg,ctg))}t = 1 … Tg
// Perform M discriminator updates steps
ℓ (ϕ) = ∑t = 1 … Tglog (1−Dϕ (ztg,ctg)) − ∑t = 1 … Tdlog (Dϕ (ztd,ctd))
Update ϕ by a gradient method w.r.t. ℓ (ϕ)

<!-- chunk {"id": "body-0015", "role": "body", "section": "Methods", "weight": 1.0} -->

Simulation: All simulations make use of the physics engine MuJoCo. In this paper, we consider four *bodies*: a bipedal walker, restricted to lateral movement in a vertical plane; two-link and three-link planar arms; and a custom humanoid body introduced below. Bodies consist of mass-bearing segments (*geoms*), which are connected by *joints*. The *root* of a body translates and rotates freely and is not actuated. All other joints are torque-actuated, and it is the role of the *policy* (or controller) to determine what torques to generate.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Methods", "weight": 1.0} -->

Motion capture demonstrations: The CMU Graphics Lab Motion Capture Database (link) provides motion capture models and data for multiple subjects and a wide range of behaviors. We programmatically generated a humanoid body (56 joint-angle DOFs, and a 6 DOF root joint) based on one of the subjects. Although we iteratively and interactively evaluated the general physical plausibility of the body we designed, there is almost surely only limited resemblance between the dynamical properties of the body we produced and those of the actual human whose body produced the motion capture data.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Methods", "weight": 1.0} -->

We use motion capture data from arbitrary subjects, which means we are re-targeting motion capture data across subjects (i.e. mapping joint angles from one body to another). After very limited preprocessing, the demonstration trajectories are dynamically inconsistent and include clear physical violations (penetration and/or floating), so any approach that makes use of this data must be robust to these issues. All experiments use whole clips from the CMU database, with no additional segmentation.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Results", "weight": 1.0} -->

To accomplish imitation learning from human motion capture, we need to show that GAIL can work even when imitator and demonstrator bodies differ and raw control actions are unknown. We first present results using simpler environments to demonstrate that GAIL can be extended to these settings. For these validation experiments, we first train policies via RL using hand-designed reward functions to solve simple tasks and then train imitation policies based on logged demonstrations. This strategy helps us to quantify performance because while we lack objective metrics for assessing the GAIL-trained imitation policies, we can assess imitation policies using the task objective originally used to train the demonstration policy. We then construct policy sub-skills for the complex humanoid using motion capture and then explore the reuse of the sub-skills in the context of tasks inside environments.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Validation of imitation of without actions, using partial observations", "weight": 1.0} -->

Imitation without ground-truth actions: To show that it is sufficient for the discriminator to condition on state information (including velocity) without accompanying actions, we examine imitation learning for a 2D planar walker (see Figure 3, left panel). The walker task consists of 10s episodes, terminating early if the walker torso falls below a threshold. The demonstration policy is continuously rewarded proportionally to the absolute difference between its horizontal velocity and a target speed (5m/s), minus a small control cost. See video of the demonstration, and see supplemental information for additional details. We observe that comparing actions in addition to states by the discriminator provides no benefit for training the imitation policy.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Validation of imitation of without actions, using partial observations", "weight": 1.0} -->

To interpret this result, consider that for fully-actuated bodies in deterministic environments, there exists an inverse mapping between two successive states and the action connecting them. In such a case, the action can be inferred directly from changes of state. More generally, together with the constraints imposed by the form of the body and environment, even without full-actuation or determinism, reasonable actions can be inferred. Furthermore, when the imitator and demonstrator bodies do not match, naive use of action information would actually be detrimental for imitation as the actions may no longer produce similar physical effects.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Validation of imitation of without actions, using partial observations", "weight": 1.0} -->

Features invariant to body transfer: Having dispensed with actions, we are also interested in understanding the extent to which imitation can be performed across bodies, which is sometimes referred to as "re-targeting". As human observers, we expect certain correspondences between equivalent behaviors across bodies. For example, a human may wave to a dolphin and would be gratified to see it "wave" back with a fin, despite different numbers of actuators/DOFs between the respective bodies and "end-effectors". Here, we simply examine whether state-only demonstrations of the position of a two-link arm end-effector sufficiently constrain the re-targeted imitation for an arm with three-links (Figure 3, right panel).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Validation of imitation of without actions, using partial observations", "weight": 1.0} -->

The task consists of 4s episodes during which the target position changes every second. The reward at each timestep is proportional to squared distance between the end-effector and the target center minus a small control cost. We provide videos depicting performance of RL baselines on two-link and three-link arm tasks. See supplemental information for additional details. We again log demonstrations, this time from the RL-trained two-link arm, and we train imitator policies which control either the two- or three-link arms. For imitation, the policy still receives full observation, but the discriminator only has access to a subset of the observation. We see that the two-link arm is able to imitate demonstrations from another two-link arm roughly equivalently well using either the full set of observations or observing only the vector from end-effector to target center (Figure 3, right panel, yellow vs. purple curves). The three-link arm can also be trained to imitate the two-link arm if the discriminator observes only the feature representing the displacement from the end-effector to target vector (Figure 3, right panel, red curve, three-link imitation video).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Validation of imitation of without actions, using partial observations", "weight": 1.0} -->

The choice of the vector from the end-effector to the target as a feature corresponds to the selection of a feature that is nearly invariant to body structure. Thus, the imitator can learn to make the three-link arm move such that it causes the vector between end-effector and target target to match the statistics of the demonstrations.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Training a complex humanoid from motion capture", "weight": 1.0} -->

Having validated extensions to the adversarial imitation learning approach on relatively simple problems, we are now in a position to train policies from motion capture data. We emphasize that, compared with other recent work optimizing generic policies for humanoid bodies by RL (e.g. ), the presently studied body is quite complex, with more than twice as many action dimensions (56 actuated dimensions, vs. 21). See supplemental information for humanoid experimental procedures.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Training a complex humanoid from motion capture", "weight": 1.0} -->

Episode initialization: We must first determine the distribution of states for the beginning of episodes. Naively, the initial state distribution could be manually engineered to be some specific starting pose with small variability. When training using RL, we observe that unnatural initial poses (whether fixed or variable) can yield different, unnatural locomotion behavior. In our setting where we expect to learn from motion capture, it is reasonable to initialize to poses randomly sampled from motion capture data. If we merely initialize the body from the motion capture poses and train from an RL objective to run forward, we can already observe a visually striking difference in the naturalness of the gait, though the gait is still fairly non-humanlike (see Fig 4). (see video). This effect is both dramatic and reliable.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Training a complex humanoid from motion capture", "weight": 1.0} -->

Imitation from partial observations: Our first attempt at imitation learning made use of a small set of motion capture data consisting of clips of a few steps of walking (\<30s human data; supplement for details). Observations available to the policy initially consisted of non-root joint angles and joint velocities as well as absolute velocity (3D root velocity) -- this constitutes a full observation of the body/environment and had worked fine for RL. However, naive application of adversarial imitation, where the discriminator receives all features available to policy, did not work well (see video for representative results of diverse policies unsatisfactorily trained by adversarial imitation from walking behavior). This failure can be traced to the fact that the motion capture demonstrations have noise and are dynamically inconsistent for the imitator body. We observe in particular that the arms (and the legs to a lesser extent) move in an unnaturally jerky fashion, suggesting that discriminator comparison based on joint angles poorly constrains the behavior, perhaps due to compounding errors in the sequence of joint angles from the torso to the hands.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Training a complex humanoid from motion capture", "weight": 1.0} -->

We consequently removed all non-egocentric features provided to either the policy or discriminator. Additionally, we provided both the policy and discriminator with built-in mujoco sensors corresponding to a "velocimeter" that computes velocities axis-aligned to the root orientation frame, a "gyroscope\" that provides egocentric rotational velocity, an "accelerometer\" that indicates uprightness, as well as custom 3D vectors from the root (pelvis) to the feet (x2), hands (x2), and head (see Figure 5, left panel for schematic depiction of end-effector features). Analogous to learning from end-effector features in the arm case, we only exposed these indirect measurements (velocimeter, gyros, and end-effector vectors) to the discriminator. With these features, the apparent quality of the imitation behavior dramatically improved (Figure 5, top-right, or video).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Training a complex humanoid from motion capture", "weight": 1.0} -->

Getting up from the ground: To examine a qualitatively distinct behavior, we attempted to learn a policy to get up from the ground in a humanlike way. For this task, we added the imitation-reward from the discriminator with a small reward for having the head at standing height. In this case we used a mixture of clips for getting up from a diversity of starting states (see supplement). A moderately robust policy was learned that gets up from a variety of starting states and stands (see Figure 5, right-bottom, or video). While many seeds learned to robustly get up, not all seeds learned to remain standing after getting up (instead, looping the standing up behavior and then falling).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Training a complex humanoid from motion capture", "weight": 1.0} -->

Stylized movement from scratch, using single demonstrations: To further explore single behavior acquisition from limited demonstration data, we attempted to imitate non-standard gait styles using single clips. We attempted this for small number of clips without a hyperparameter search (for the simple walk, various but not all hyperparameters performed reasonably, and we selected a single successful hyperparameter setting to try here) and while imitation from single clips did not yield perfect behavior and did not work for every clip we tried, some resulting policies were robust and captured the essence of the style (e.g. drunk-style policy, chicken-style policy; videos include user-interactive application of small exogenous forces to guide/redirect the movement). We view it as quite non-trivial that it is possible to train a policy to generate a moderately robust behavior from a single clip (roughly 10s of a person with a different body performing that behavior).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Training a complex humanoid from motion capture", "weight": 1.0} -->

In addition to the above behaviors, we trained policy sub-skills for running and turning (video).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Contextual modulation and task-based control", "weight": 1.0} -->

Up to this point, all policies we have discussed are trained to perform one skill. To build systems capable of flexible behavior, we want to transition among sub-skills. We found that switching mid-trajectory between separately-trained, single-skill policies did not lead to robust transitioning as the intermediate states were outside the state distributions of one or the other policy.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Contextual modulation and task-based control", "weight": 1.0} -->

We found that adversarial imitation training using one context per behavior, as described in Figure 2, encourages the policy to find efficient transitions between behaviors. Accordingly, we found it possible to train a single low-level controller capable of switching among running straight, veering left, and veering right based on an externally set one-of-three context (from a total of only 286 time-resampled frames; \<10s of data). During training, the context was random and switched every 5s, but at run-time, it is possible to modulate it interactively to control the character. This multi-skill, low-level controller could be controlled either by keyboard-determined modulation of the context, or, as we will show, by a higher-level controller.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Contextual modulation and task-based control", "weight": 1.0} -->

As a first example, we restored the low-level controller in a new environment corresponding to a half of a soccer field and modulate the low-level controller by keyboard-control to score a goal (Figure 6, or video).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Contextual modulation and task-based control", "weight": 1.0} -->

Additionally, we considered whether it is possible to refine previously learned skills. We exposed the existing policy and body to a staircase track and fine-tuned the running policy to surmount stairs by RL with a simple reward for forward velocity (Figure 6, or video). Without tuning, the running policy falls quickly on the stairs, but the refined policy is able to ascend and descend stairs of two discrete slopes, while retaining its ability to locomote on flat ground.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Contextual modulation and task-based control", "weight": 1.0} -->

Finally, we considered modulation of the controller by a higher-level controller. The higher level controller could be trained by a variety of methods and could interact with the policy in a variety of ways. Here, we used a simple two-layer neural network as the higher-level controller and trained it to use a local, top-down depth camera to send context signals to the lower-level controller, resulting in autonomous navigation. Its reward corresponded to forward movement along a linear (3D) track (see Figure 6 or video: the probe trial is a representative rollout on a novel procedurally generated instance of the course). See supplemental information for additional details.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Relationships with related work", "weight": 1.0} -->

Generative sequence modeling: There has been a great deal of research into sequence models of plausible movements, not in the context of physical control. For example, modeling the kinematic trajectories of a motion capture data in the absence of physics has been actively studied in the neural network literature.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Relationships with related work", "weight": 1.0} -->

Physical control: In the field of graphics-oriented character animation, much attention has been paid to building realistic movement behaviors, though the results often require significant domain expertise. Representative methods for producing terrestrial locomotion have made use of specialized gait controllers (for a quadruped; for a biped ) or systems explicitly producing foot placements. Curated motion capture has been employed, for example, in beautiful work to simulate pigeon flight as well as in the context of high performance open-loop trajectory planning for humanoid behaviors. These tools have supported amazing demonstrations of sequenced sub-skills in obstacle courses; however, the sub-skills are each individually highly-engineered, albeit quite elegantly. Trajectory optimization (or planning) without motion capture can also yield impressive results (e.g. ). Furthermore, trajectories optimized using model-based approaches can be distilled into a neural network policy.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Relationships with related work", "weight": 1.0} -->

Deep RL methods, by contrast, provide hope that many of these results can be replicated and perhaps improved upon in the near future with substantially less domain knowledge. Exciting recent work has used deep RL for 2D locomotion of creatures and very recently for 3D humanoid. Other recent work successfully makes use of a specialized neural network architecture for motion capture sequence modeling to enable robust humanoid behavior. While these have used comparatively less domain knowledge than the other approaches in animation, the priority in these papers has been to produce aesthetically pleasing motions over constructing generic tools. Our work makes fewer assumptions about how policies should track the motion capture data, uses a more general learning approach, and builds in less structure in controllers and reward functions.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Discussion", "weight": 1.5} -->

Looking beyond the scope of engineering skilled motor behaviors for humanoids, we think there is a broader issue to consider in the design of artificial agents. To communicate complex behaviors to agents, it is often most straightforward to demonstrate them. In contrast, it is extremely difficult to formalize different behaviors with simple reward functions.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Discussion", "weight": 1.5} -->

Therefore, a core motivation to use imitation learning is that we lack good objective functions to describe complex behaviors. This necessarily presents an obstacle when developing and assessing algorithms as well as when monitoring convergence (not dissimilar from the difficulty of assessing generated samples from GANs). At present, we must rely on human judgment of the quality of the behaviors we have produced.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Discussion", "weight": 1.5} -->

So far, we have only demonstrated learning on a somewhat restricted, albeit diverse, set of behaviors and have only demonstrated limited reuse. Accordingly, subsequent steps in this research program will include scaling to a much wider behavioral repertoire and leveraging the learned sub-skills for even more challenging tasks.
