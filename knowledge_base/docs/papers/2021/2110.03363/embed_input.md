<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Evaluating Model-based Planning and Planner Amortization for Continuous Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

There is a widespread intuition that model-based control methods should be able to surpass the data efficiency of model-free approaches. In this paper we attempt to evaluate this intuition on various challenging locomotion tasks. We take a hybrid approach, combining model predictive control (MPC) with a learned model and model-free policy learning; the learned policy serves as a proposal for MPC. We find that well-tuned model-free agents are strong baselines even for high DoF control problems but MPC with learned proposals and models (trained on the fly or transferred from related tasks) can significantly improve performance and data efficiency in hard multi-task/multi-goal settings. Finally, we show that it is possible to distil a model-based planner into a policy that amortizes the planning computation without any loss of performance. Videos of agents performing different tasks can be seen at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent years, model-free RL algorithms have improved and scaled to the point where it is feasible to learn adaptive behavior for high-dimensional systems in diverse circumstances. Despite these improvements, there is a widespread intuition that model-based methods can further improve data efficiency. This has led to recent advances for continuous control problems that demonstrate improved learning efficiency by leveraging model learning during policy training. However, there is also work which urges moderation in interpreting these results, by showing that well-tuned model-free baselines can compare favorably against some model-based approaches.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we focus on model-based RL with learned models and proposals. We use model-predictive control (MPC) to improve the quality of behavior generated from a policy that serves as a proposal for the planning procedure. When acting, the MPC-based search procedure improves the quality of the data collected which serves as a sort of "active exploration". This data can then be used to improve the proposal, in effect consolidating the gains. This hybrid approach interpolates between model-free RL, on one side, and trajectory optimization with a model on the other.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Fundamentally, the spectrum on which this hybrid approach is situated reflects a trade-off in terms of reusability / generality versus compute cost at deployment time. Policies obtained by model-free RL often generalize poorly outside of the situations they have been trained, but are efficient to execute (i.e., they are fully amortized). Models offer potentially greater generalization, insofar as the model is accurate over a broad domain of states, but it can be computationally costly to derive actions from models. Ultimately, the pure planning approach involving deriving actions from models is usually prohibitive and some form of additional knowledge is required to render the search space tractable for real-time settings. Coming from the model-free RL perspective, the natural approach is to learn a policy that serves as a relatively assumption-free proposal for the planning process.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

While in most model-based RL publications the ambition is to speed up policy learning for a single task, we believe this is not necessarily the most promising setting, as it is difficult to dissociate the learning of a dynamics model (which is potentially task independent) from that of a value function (which is task specific). A different intuition is that model-based RL might not accelerate learning on a particular problem, but rather enable efficient behavior learning on new tasks with the same embodiment. In such transfer settings, we might hope that a dynamics model will offer complementary generalization to the policy, and we can transfer the policy, model, or both.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we validate these intuitions about the relative value of the different components of this system. For high-dimensional locomotion problems, we find that even with a good learned model successful model predictive control requires good proposal distributions to succeed. This effect is particularly pronounced in domains with multiple goals (or equivalently multiple different tasks). Building on this insight we show that it is sometimes possible to leverage learned models with a limited search budget to boost exploration and learn policies more efficiently. Policies that are trained by off-policy updates from data acquired through planning do not reliably perform well when used without planning in our experiments. To overcome this problem, and enable planner amortization into a policy that does not require planning at test time, we propose training the policy according to a combination of a *behavioral cloning* objective (on MPC data) and an off-policy update with MPO. When transferring models and proposals to other tasks we find only marginal improvements in data efficiency relative to a well-tuned model-free baseline.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Overall, our results suggest that while MPC with learned models can lead to more data efficiency, and planners can be amortized effectively into compact policies, it is not a silver bullet and model-free methods are strong baselines.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Tasks", "weight": 1.0} -->

In this paper we consider a number of locomotion tasks of varying complexity, simulated with the MuJoCo physics simulator. We consider two embodiments: an 8-DoF ant from dm_control and a model of the Robotis OP3 robot with 20 degrees of freedom. For each embodiment, we consider three tasks: walking forward, walking backward and "go-to-target-pose" (GTTP), a challenging task that is the focus of our evaluation. In all tasks, the agent receives egocentric proprioceptive observations (joint angles, velocities and end-effector positions) and additional task observations.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Tasks", "weight": 1.0} -->

In the walking forward and backward tasks the agent is rewarded for maximizing forward (or backward) velocity in the direction of a narrow corridor. For the OP3 robot we also include a small pose regularization term. The task is specified through a relative target direction observation.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Tasks", "weight": 1.0} -->

The GTTP task, which builds on existing motion tracking infrastructure, consists of either body on a plane, with a target pose in relative coordinates as a task-specific observation and proximity to the target pose rewarded. When the agent is within a threshold distance of the target pose (i.e. it achieves the current target), it gets a sparse reward and a new target is sampled. For the ant we use target poses from policies trained on a standard go-to-target task. For the OP3, we use poses from the CMU mocap database (cmu, ) (retargeted to the robot). We use thousands of different target poses; the agent has to learn to transition between them. Thus the GTTP task can be seen as either a single highly diverse task or as a multi-task setting with strongly related tasks and consistent dynamics. We believe the GTTP task should be particularly amenable to model-based methods: it combines a high-dimensional control problem with a diverse goal distribution. This makes it hard to solve quickly with model-free methods. However, since the dynamics are shared between all goal poses, a dynamics models should be beneficial in leveraging the common structure.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Tasks", "weight": 1.0} -->

See supplement for an in-depth motivation and results on tasks from the DeepMind Control Suite.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Model predictive control (MPC) for behavior generation", "weight": 1.0} -->

We consider control obtained by model-based planning that refines initial action-samples from a proposal distribution. MPC executes the first action from the planned action sequence and iteratively re-plans after each timestep (c.f. actor loop in Alg. 1 for behavior generation ‣ 4 Method ‣ Evaluating model-based planning and planner amortization for continuous control")). In this scheme, actions are sampled either from the proposal $\pi_{\theta}$ (with parameters $\theta$) or the planner (PLANNER), forming a mixture distribution that is specified by the probability of choosing planner actions ($p_{plan}$). Setting $p_{plan} = 0$ results in using only samples from the proposal and vice-versa for $p_{plan} = 1$. Setting $p_{plan} = 0.5$ leads to interleaved execution of proposal and planner actions, like the stochastic mixing of student and expert actions in DAgger.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Model predictive control (MPC) for behavior generation", "weight": 1.0} -->

Given: Randomly initialized proposal πθ, (pre-trained or random) model mϕ, random critic Qψ, optionally (pre-trained or random) task-agnostic proposal ρω. // Modules to be learned
Given: Known reward r, planning probability pp l a n, replay buffer ℬ, MPO loss weight α, BC loss weight β, learning rates &amp; optimizers (ADAM) for the different modules. // Known modules and parameters

<!-- chunk {"id": "body-0015", "role": "body", "section": "Model predictive control (MPC) for behavior generation", "weight": 1.0} -->

// MPC loop – Asynchronously on the actors
Initialize ENV and observe state s0. while episode is not terminated do
// Choose between planner and proposal action depending on pp l a n
// Use mixture of (pre-trained) task-agnostic proposal (ρω) and learned proposal (πθ) as proposal for proposal transfer exps (Sec. 5.4). Use pre-trained model for model transfer exps (Sec. 5.3).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Model predictive control (MPC) for behavior generation", "weight": 1.0} -->

// Asynchronously on the learner
Sample batch B of trajectories, each of sequence length T from the replay buffer ℬ
Update action-value function Qψ based on B using Retrace.
Update model mϕ based on B using multi-step loss in Equation 20 (Sec. 4.2)
Update proposal πθ based on B using Equation 4 (Sec. 4.3)
Optionally, for from-scratch experiments, update task-agnostic proposal ρω using behavioural cloning (Equation 1) on transitions in B.
Algorithm 1 Agent combining MPC with model-free RL

<!-- chunk {"id": "body-0017", "role": "body", "section": "Model predictive control (MPC) for behavior generation", "weight": 1.0} -->

The PLANNER subroutine takes in the current state $s_{t}$, the proposal $\pi_{\theta}$ (with parameters $\theta$), a model $m_{\phi}$ (with parameters $\phi$) that predicts next state $s_{t + 1}$ given current state $s_{t}$ and action $a_{t}$, the known reward function $r{(s_{t},a_{t},s_{t + 1})}$. Optionally, a learned state-value function $V_{\psi}{(s)}$ (with parameters $\psi$) that predicts the expected return from state $s$ can be provided. While we consider sample based planners, primarily a Sequential Monte Carlo based non-iterative planner (SMC, Alg. 2) and the Cross-Entropy Method (CEM, Alg. 3), other planners could be used. See Sec. B of the supplement for more details.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Model predictive control (MPC) for behavior generation", "weight": 1.0} -->

The hybrid agent in Alg. 1 for behavior generation ‣ 4 Method ‣ Evaluating model-based planning and planner amortization for continuous control") has several learnable components: the model $m_{\phi}$, the proposal $\pi_{\theta}$ as well as the (optional) value function $V_{\psi}$; these are learned based on data generated by the MPC loop on the actor and we measure learning progress w.r.t environment steps collected. Note that we assume the reward function is known since it is under the control of the practitioner in most robotics applications.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Learning dynamics models", "weight": 1.0} -->

Successfully applying model predictive control requires learning good dynamics models. In this paper, we train predictive models $m_{\phi}$ that take in the current state $s_{t}$ and action $a_{t}$ and predict the next state $s_{t + 1} = {m_{\phi}{(s_{t},a_{t})}}$. This model has both learned and hand-designed components; the task-agnostic proprioceptive observations are predicted via "black-box" neural networks while any non-proprioceptive -- task-specific -- observations (e.g. relative pose of the target) are calculated in closed form from the predicted proprioceptive observations in combination with a known kinematic model of the robot. The learned components are parameterized as a set of deterministic feed-forward MLPs, one per observation group (e.g. joint positions), and predict the next observation from the current observations and action. This model is trained end-to-end via a multi-step squared error (Eqn.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Learning dynamics models", "weight": 1.0} -->

20) between an open loop sequence of predicted states and true states sampled from the replay buffer. We use deterministic models as they are more amenable to multi-step losses and an ablation study (Sec. E.4 of the supplement) as well as a recent benchmarking effort did not find a consistent difference between deterministic and stochastic model ensembles in the context of model-based planning. Training happens from scratch, concurrently with policy learning. See Sec. C of the supplementary material for further details.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Learning proposal distributions", "weight": 1.0} -->

As we will show, planning with a good dynamics model by itself is insufficient for solving challenging continuous control problems. That is, generating behavior according to the MPC loop in Alg. 1 for behavior generation ‣ 4 Method ‣ Evaluating model-based planning and planner amortization for continuous control") with a goal-unaware proposal fails to solve the challenging GTTP tasks even when planning with the ground-truth model and a known reward function. This is due to the fact that the action space is large, and the planning algorithm is limited by computational constraints and a finite horizon. In order for planning to succeed, we find it vital to provide planners with an action proposal distribution, which facilitates search by increasing the probability of sampling plausible, task-relevant actions. In addition, we show that the learned proposal can itself be deployed without planning at test time; this can be particularly useful in compute constrained settings where planning on the robot may not be feasible.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Learning proposal distributions", "weight": 1.0} -->

But what constitutes a good proposal? A natural answer to this question is that a good proposal produces actions, for each state, that lead to task success, and the planner selects the best among already good candidate actions. A simple strategy to obtain such a proposal is to iteratively amortize the planning process. That is, starting from any proposal, execute the planner for a given amount of time to return an improved action and fit the returned action; this will sharpen the proposal and lead to the planner focusing on better actions in the next iteration. This idea has been used in the RL community before and underlies modern search based algorithms such as AlphaZero.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Learning proposal distributions", "weight": 1.0} -->

In the MPC setting we can formalize the idea as follows: let $\pi_{\mathcal{B}}{(\left. a \middle| s \right.)}$ refer to the stochastic mixture of $\text{PLANNER}{(s_{t},\pi_{\theta},m_{\phi},r,V_{\psi})}$ and $\pi_{\theta}{(\left. a \middle| s \right.)}$ with probability $p_{\text{plan}}$ (i.e., as actions are selected according to the MPC loop in Alg. 1 for behavior generation ‣ 4 Method ‣ Evaluating model-based planning and planner amortization for continuous control")).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Learning proposal distributions", "weight": 1.0} -->

And let $\mathcal{D}_{\pi_{\mathcal{B}}}$ be a dataset of states and actions collected by executing this policy -- note that in practice for data efficiency reasons we consider a dataset $\mathcal{D}_{{\overset{\sim}{\pi}}_{\mathcal{B}}}$, where ${\overset{\sim}{\pi}}_{\mathcal{B}}$ is the average behavior distribution during training, which changes over time due to the proposal and model being learned. Clearly, assuming the planning procedure produces improved actions, we expect that ${\overset{\sim}{\pi}}_{\mathcal{B}}$ is at least as good as the average proposal policy ${\overset{\sim}{\pi}}_{\theta}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Learning proposal distributions", "weight": 1.0} -->

i.e. the proposal is learned by amortizing the planner via behavioral cloning of the planner actions.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Learning proposal distributions", "weight": 1.0} -->

Unfortunately, in cases where the planner cannot find an improvement on the proposal (as is the case for random proposals in our experiments), the above objective may lead to premature convergence at sub-optimal behavior (see e.g. Wang & Ba ). To ameliorate this issue, we can consider hybrid updates that both amortize the planner, but also directly favor actions that lead to an improvement in terms of cumulative return via an off-policy RL policy update. We will use the MPO algorithm, although other recent RL algorithms could be used instead. More precisely, the MPO policy improvement step involves using a learned action-value function ${Q^{\pi_{\theta}}{(s,a)}} \approx {{\mathbb{E}}_{\pi_{\theta}}{\lbrack{{\left. {\sum_{t}{\gamma^{t}r_{t}{(s_{t},a_{t})}}} \middle| s_{0} \right.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Learning proposal distributions", "weight": 1.0} -->

It is known that the solution of this optimization is given in closed form as ${q{(\left. a \middle| s \right.)}} \propto {\pi_{\theta}{(\left. a \middle| s \right.)}{\exp{({{Q^{\pi_{\theta}}{(s,a)}}/\eta})}}}$, where $\eta$ is a dual variable optimized such that the KL-constraint on the policy is fulfilled.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Learning proposal distributions", "weight": 1.0} -->

where $\pi_{\theta^{\prime}}$ is the last reference policy (fixed for this optimization). In practice MPO uses an additional trust-region constraint to stabilize learning. We can combine the two objectives (Eqns. 1 and 3) for improving the proposal via a simple weighting to obtain the complete objective

<!-- chunk {"id": "body-0029", "role": "body", "section": "Learning proposal distributions", "weight": 1.0} -->

The full agent showing the actor and learner loops is shown in Alg. 1 for behavior generation ‣ 4 Method ‣ Evaluating model-based planning and planner amortization for continuous control"). In our experiments we compare several variants corresponding to different choices of $p_{plan}$, $\alpha$ and $\beta$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Evaluating pre-trained models and proposals", "weight": 1.0} -->

In a first set of experiments we study how MPC (Alg. 1 for behavior generation ‣ 4 Method ‣ Evaluating model-based planning and planner amortization for continuous control"), $p_{\text{plan}} = 1$) performs on the locomotion tasks considered in the paper. We evaluate performance with two different models, the ground truth MuJoCo simulator and a pre-trained model that is trained on data from a successful agent on the corresponding task (see Sec. 4.2). We also consider two different proposal distributions: a zero-mean Gaussian proposal and a task-agnostic proposal that is pre-trained with a behavioral cloning objective on logged data from a successful agent (similar to the prior distribution in Galashov et al., see Sec. D.2). This pre-trained proposal depends only on proprioceptive information but not task specific observations, and therefore is a reasonable prior capturing average behavior. We assume a known reward function but do not use a learned value function.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Evaluating pre-trained models and proposals", "weight": 1.0} -->

The best results of a large hyper parameter sweep are shown in Table 1, together with performance of the two proposals and baseline performance of a successful agent whose data was used to train the pre-trained model and proposal (labelled 'Near-Optimal performance').

<!-- chunk {"id": "body-0032", "role": "body", "section": "Evaluating pre-trained models and proposals", "weight": 1.0} -->

When planning with a zero-mean Gaussian proposal and the ground truth dynamics, both planners improve significantly on the performance of the Gaussian proposal for the simpler Ant tasks but not for the harder OP3 tasks (this may be in part because the OP3 tasks terminate if the robot falls, which makes planning hard). Planning with a pre-trained model and the Gaussian proposal performs similar to the proposal itself on the harder OP3 tasks but there is a small improvement, albeit less than when planning with the ground truth dynamics, for the simpler Ant tasks. Specifically on the Ant GTTP task, planning leads to better rewards but fails to consistently achieve target poses and there remains a large qualitative difference between the planner results and near-optimal performance.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Evaluating pre-trained models and proposals", "weight": 1.0} -->

When planning with the pre-trained task-agnostic proposal instead, the performance far exceeds the results from planning with the Gaussian proposal or executing the pre-trained proposal without any planning. This highlights the need for a suitable proposal, especially for the high-dimensional OP3 tasks, further motivating our approach to leverage model-free RL to learn a proposal for MPC. When planning with a pre-trained proposal, using the ground truth dynamics or a pre-trained model achieve similar performance, indicating that our pre-trained models are suitable for planning. Lastly, both planners perform similarly across most of the tasks, though on the harder GTTP tasks SMC slightly outperforms CEM. We use SMC throughout the paper as it makes better use of the proposal compared to CEM which uses the proposal only for plan initialization (see supplement for full results).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Leveraging MPC with a learned model and proposal", "weight": 1.0} -->

Next, we evaluate different approaches to learning a proposal from scratch for MPC based on the approach discussed in Sec. 4.3.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Leveraging MPC with a learned model and proposal", "weight": 1.0} -->

MPO: MPO with a distributional critic similar to Hoffman et al.. Corresponds to ${\alpha = 1},{{\beta = 0},{p_{plan} = 0}}$ from Eqn. 4 and Alg. 1 for behavior generation ‣ 4 Method ‣ Evaluating model-based planning and planner amortization for continuous control"). MPO hyper-parameters are tuned for each task (and listed in supplement).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Leveraging MPC with a learned model and proposal", "weight": 1.0} -->

MPC+MPO: MPC to collect data. MPO objective for learning (${\alpha = 1},{{\beta = 0},{p_{plan} = 0.5}}$).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Leveraging MPC with a learned model and proposal", "weight": 1.0} -->

MPO+BC: Adding MPO and BC objectives (${\alpha = 1},{{\beta > 0},{p_{plan} = 0}}$), where $\beta$ is tuned per task.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Leveraging MPC with a learned model and proposal", "weight": 1.0} -->

MPC+MPO+BC: MPC to collect data. Combined MPO+BC objective (${\alpha = 1},{{\beta > 0},{p_{plan} = 0.5}}$).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Leveraging MPC with a learned model and proposal", "weight": 1.0} -->

The model is trained from scratch for the MPC variants (see Sec. 4.2). We choose $p_{plan} = 0.5$ for all our MPC experiments as it worked better than $p_{plan} = 1.0$, and use 250 samples and a planning horizon of 10 for SMC (see supplement for ablations). We tune the BC objective weight $\beta$ per task.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Leveraging MPC with a learned model and proposal", "weight": 1.0} -->

We also tested our approach on simpler forward and backward walking tasks for both the Ant and OP3 bodies. Figure 2 (right column) shows the results from the backward walking tasks. For the Ant (top row), MPC+MPO significantly outperforms MPO early on during training but reaches similar asymptotic performance while for the OP3 (bottom row) the difference between MPO and MPC+MPO is small throughout training. Interestingly, on these simpler tasks the proposal for MPC+MPO matches the actor performance and the addition of the BC objective results only in minor performance improvements. We posit that a well-tuned implementation of the model-free MPO baseline achieves near-optimal performance on these tasks and provides a strong baseline that is hard to beat both in terms of data efficiency and performance even with the true reward function and bootstrapping with a learned critic. We present forward walking results showing similar trends in the supplement where we also describe experiment setup and hyperparameters in detail. Lastly, since the BC objective substantially improves results for both MPO and MPC+MPO we use the BC variants in all further experiments. Videos of learned behaviors can be seen at our website.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Leveraging MPC with a learned model and proposal", "weight": 1.0} -->

Ablations: We additionally ran several experiments ablating our design choices. The results of these experiments can be found in the supplement. Figure 7 and Figure 8 show the results of varying $p_{plan}$ as well as the number of samples used by the planner and the planning horizon, respectively. In Figure 9 we show the effect of bootstrapping with the learned value function within MPC. Figure 14 and Figure 15 compare deterministic models with PETS-style stochastic models in our setting. Furthermore, in Figure 16 we report results using ensembles rather than a single model. Finally, Figure 17 shows results on the walker and humanoid tasks in the DeepMind Control Suite.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Model transfer", "weight": 1.0} -->

In this section, we study how well models can transfer between tasks. We first explore to what extent a learned model can boost performance on a complex task. As a control experiment we transfer learned models from the OP3 GTTP task to the same task. We consider three different settings (in addition to the baseline MPO+BC) where a) no model is transferred and one is trained from scratch on the target task (MPC+MPO+BC), b) the transferred model is finetuned on the target task (MPC+MPO+BC+Finetune) and c) the transferred model is kept frozen throughout training on the target task (MPC+MPO+BC+Frozen). In this experiment (Figure 3 left column, solid lines) we find little improvements in learning speed or asymptotic performance when transferring a model vs learning from scratch. Transferring a frozen model (which can fail to generalize to out of distribution data) performs slightly worse vs finetuning the transferred model. This trend also holds in other transfer settings such as transferring models from the forward walking task to GTTP and transferring from the GTTP task to backward walking (Figure 3, center/right column, respectively, solid lines).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Model transfer", "weight": 1.0} -->

While this result is perhaps surprising, it does agree with our initial investigation of planning with learned models (Table 1) where we saw poor performance on all our tasks without a good proposal for the planner to leverage. Transferring a good model still does not solve the initial exploration problem, especially on the harder tasks. Videos of learned behaviors can be seen here.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Proposal (and model) transfer", "weight": 1.0} -->

In addition to transferring learned models across tasks we also consider transferring learned proposals. On each source task we train a proposal that is dependent only on proprioceptive information and lacks task-specific information (similar to the one used in subsection 5.1) and can thus be freely transferred across tasks. As a simple approach to transfer a pre-trained proposal we used it for action generation while keeping the learning objective unchanged. Concretely, we use a mixture of the reloaded proposal from a source task and the learned proposal on the target task as our proposal distribution ($\pi_{\theta}$) for the MPC loop in algorithm 1 for behavior generation ‣ 4 Method ‣ Evaluating model-based planning and planner amortization for continuous control"). The mixture weight of the reloaded proposal is annealed linearly from 1 to 0 in a fixed number of learning steps (tuned per task); see Sec. E.3 of the supplementary material for further details.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Proposal (and model) transfer", "weight": 1.0} -->

Again, we first transfer the proposal trained on the GTTP task to the same task (Figure 3, left column, dashed lines). Transferring the proposal leads to faster learning for both MPO+BC and MPC+MPO+BC as well as to a smaller extent, better asymptotic performance. Transferring the model and proposal together (MPC+MPO+BC+Finetune, MPC+MPO+BC+Frozen) does not lead to any additional improvements, further strengthening our intuitions from the model transfer experiments.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Proposal (and model) transfer", "weight": 1.0} -->

Next we transfer proposals between different source and target tasks, which yielded some nuanced insights into the need for compatibility of the tasks. Figure 3 (center column, dashed lines) shows the results when transferring a proposal from the forward walking task to the GTTP task and Figure 3 (right column, dashed lines) presents proposal transfer results from the GTTP task to backward walking. Interestingly, proposal transfer hurts both MPC+MPO+BC and MPO+BC in both these cases, especially for the high-dimensional OP3, leading to slower learning and lower final performance on both the target tasks. These results provide complementary insights regarding proposal transfer: there should be good overlap between the data distributions of the source and target tasks for proposal transfer to succeed. This is not the case in these transfer experiments; forward walking has a very narrow goal distribution compared to GTTP making the resulting proposal far too peaked, and while a proposal from the GTTP task would be quite broad (see supplementary video for some trajectory rollouts) it is highly unlikely to capture the behavior of walking backwards.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Proposal (and model) transfer", "weight": 1.0} -->

Overall, these results provide encouragement that combining the right proposal, potentially trained on a diverse set of tasks, together with model-based planning can lead to efficient and performant learning on downstream tasks. For more transfer results and plots showing amortized policy performance see the supplement.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our initial experiments highlighted that a good dynamics model is not enough to solve challenging locomotion tasks with model predictive control when computation time is limited, especially in tasks with high task and control complexity. In such settings a good proposal is necessary to guide the planner. Motivated by this finding we study different approaches to learning proposals for MPC, considering variants that combine the learning objective from MPO, a model-free RL algorithm, together with a behavioral cloning objective for efficient planner amortization. We also evaluate transfer performance across tasks where either the proposal, learned model, or both are transferred. Overall our results show that for the locomotion domains considered in this paper, MPC with a learned model and proposal can yield modest improvements in data efficiency relative to well-tuned model-free baselines. We found that the gains are larger as task and control complexity increase. On simpler walking tasks we saw very small improvements that are further diminished if an amortized policy is desired at test time. On our most challenging task, the OP3 go to target pose task, we see both significantly faster learning speed and improved asymptotic performance.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Discussion", "weight": 1.5} -->

A common justification for model-based approaches is the intuition that models can more easily transfer to related tasks since the dynamics of a body are largely task independent. We attempted to validate this intuition but had difficulty achieving large gains in data efficiency even when transferring to the same task. We speculate that this finding is related to the difficulty of planning with a limited search budget in a multi-goal/multi-task setting even with a near perfect model. If the overall system is limited by the lack of a good proposal then model transfer by itself may have a negligible effect. When transferring models and proposals to new simpler tasks we also did not find substantial benefits. There are a number of other potential pitfalls in this setting in addition to the lack of a good proposal. If a proposal leads to trajectories that are inconsistent with the state distribution on which the model was trained, MPC may add little value. As we observed when transferring from the go-to-target-pose tasks to walking backwards, an unsuitable proposal may limit asymptotic performance. Additionally, on tasks with fairly narrow goal distributions a well-tuned model-free method can perform just as well as a model-based agent.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Discussion", "weight": 1.5} -->

This suggests tasks with multi-task/multi-goal settings provide a good test bed to showcase the strengths of model-based approaches and aid further research.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Discussion", "weight": 1.5} -->

On the whole, the gains from MPC with learned models in our setting are meaningful, but not so dramatic as to be a silver bullet, a finding similar to Springenberg et al.; Hamrick et al.. This paper focused on learning complex locomotion tasks from state features, using a structured dynamics model as well as focusing on MPC as the way to leverage the model. There are a number of additional settings where models can be used differently and may aid transfer. For example, in partially observed tasks with pixel observations, transferring models and representations may lead to improvements in data efficiency.
