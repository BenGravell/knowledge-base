<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

OGPO: Sample Efficient Full-Finetuning of Generative Control Policies

Topics include Policy gradients, Robotics, Diffusion models, Online algorithms, Optimization, Control, Learning, OGPO.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Generative control policies (GCPs), such as diffusion- and flow-based control policies, have emerged as effective parameterizations for robot learning. This work introduces Off-policy Generative Policy Optimization (OGPO), a sample-efficient algorithm for finetuning GCPs that maintains off-policy critic networks to maximize data reuse and propagate policy gradients through the full generative process of the policy via a modified PPO objective, using critics as the terminal reward. OGPO achieves state-of-the-art performance on manipulation tasks spanning multi-task settings, high-precision insertion, and dexterous control. To our knowledge, it is also the only method that can fine-tune poorly-initialized behavior cloning policies to near full task-success with no expert data in the online replay buffer, and does so with few task-specific hyperparameter tuning. Through extensive empirical investigations, we demonstrate the OGPO drastically outperforms methods alternatives on policy steering and learning residual corrections, and identify the key mechanisms behind its performance.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We further introduce practical stabilizers, including success-buffer regularization, conservative advantages, chi^ regularization, and Q-variance reduction, to mitigate critic over-exploitation across state- and pixel-based settings. Beyond proposing OGPO, we conduct a systematic empirical study of GCP finetuning, identifying the stabilizing mechanisms and failure modes that govern successful off-policy full-policy improvement.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Autonomous acquisition of new skills is an important challenge for modern robot manipulation. While imitation learning via behavior cloning (BC) from human demonstration can enable a robot to learn behaviors across several contexts, performance is typically brittle to subtle changes in tasks and environments. These models rarely exhibit high success rates zero-shot in the diversity of settings encountered in deployment. While this fragility can be remedied through additional data collection, a natural question to ask is - can the robustness of pre-trained imitation learning policies be bolstered autonomously without requiring considerably more manual data collection?

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To this end, there has been a strong interest in finetuning pre-trained robotic policies via reinforcement learning (RL), to autonomously improve behavior via self-collected experience. Of particular relevance is the problem of finetuning *Generative Control Policies* (GCPs) - the parametrization of control policies by expressive generative models, such as diffusion or flow models (chi2023diffusion; black2024pi_0; pan2025much). These policies have been extremely effective for modern robotic applications (zhang2024affordance; wolf2025diffusion).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Current methodology for GCP finetuning succumbs to tradeoffs between data efficiency and the extent of policy improvement during training. Approaches focused on sample efficiency combine *off-policy* critic learning, enabling strong experience reuse, with either targeted *partial* finetuning of the GCP, such as steering the initial generation noise or learning residual corrections, or instead use behavior cloning to imitate high-return actions. These approaches learn quickly when the base policy has strong coverage of optimal actions, but struggle with exploring new behavior. On the other hand, methods focused on eliciting maximum final task performance (lei2025rl; ren2024diffusion; mcallister2025flow) use *on-policy* policy gradient updates, which drive aggressive policy improvement at the expense of significantly compromised sample efficiency.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we propose a new algorithm - OGPO for full-finetuning of expressive GCPs, providing both sample-efficient and expressive policy updates via data-efficient off-policy reinforcement learning. Following ren2024diffusion; black2023training, OGPO views GCP optimization as a bi-level MDP, with a nested inner denoising MDP over the action generation steps of a GCP, and an outer environment dynamics MDP over actions actually executed in the environment. Importantly, in real-robotics tasks, there exists a *sample-cost asymmetry*: collecting trajectories from the environment MDP is expensive, while generating action trajectories through the denoising MDP is purely computational and therefore cheap.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

While direct policy optimization in the unrolled bi-level MDP can be very (environment-)sample inefficient (ren2024diffusion; zhang2025reinflow), OGPO leverages the aforementioned sample-cost *asymmetry* to perform *decoupled* policy optimization. Specifically, OGPO performs sample-efficient, off-policy Temporal Difference (TD)-learning to learn a Q function in the environment dynamics MDP over *expensive* environment samples, while using data-inefficient but stable on-policy RL updates to extract policies from the inner denoising MDP over *cheap* GCP samples (see Footnote˜1 left). Doing so allows for an off-policy policy optimization algorithm that is data-efficient (due to TD-learning in the environment dynamics MDP), yet expressive (due to on-policy RL finetuning in the denoising MDP)

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Through careful empirical study, we show that OGPO is able to achieve both stable and expressive updates for finetuning GCPs in challenging robotics tasks. Based on empirical analysis of the shortcomings, we further propose OGPO+, an empirically optimized variant that incorporates improvements in test-time optimization such as Best-of-N planning via Q-functions and policy distillation from successful trajectories obtained via online RL. These improvements allow OGPO+ to achieve state-of-the-art performance on a set of contact-rich simulation environments with varying horizons, degrees of freedom, and precision requirements, while requiring minimal hyperparameter tuning. Surprisingly, we show that OGPO+ is able to fine-tune policies with *zero expert data* in the policy replay buffer. This is a fundamentally new capability that points towards the future possibility of finetuning models with minimal human data collected in a task-specific manner on deployment. We perform a careful set of analyses to understand the impact of the decoupled optimization central to OGPO, and the impact of the design decision made in OGPO+ - showing the efficacy of full-policy finetuning of GCPs under the right design choices.

<!-- chunk {"id": "body-0010", "role": "body", "section": "On-Policy Policy Gradient Methods", "weight": 1.0} -->

*Policy gradient* (PG) methods (e.g., REINFORCE (williams1992simple)) improve policy performance by approximating the gradient of this objective w.r.t.

<!-- chunk {"id": "body-0011", "role": "body", "section": "On-Policy Policy Gradient Methods", "weight": 1.0} -->

where ${r_{t}{(s_{t},a_{t})}}:={\sum_{\geq t}{R{(s,a)}}}$ is the discounted future return from time $t$, and ${\nabla\log}{(\left. a_{t} \middle| s_{t} \right.)}$ denotes the gradient of the logarithm of the *likelihood* of $({a_{t} \mid s_{t}})$. Myriad improvements exist to reduce variance of gradient estimation and accelerate training stability; following (ren2024diffusion; zhang2025reinflow), we build on the PPO algorithm (schulman2017proximal). PG methods are called *on-policy* because they optimize over the *current* policy distribution, limiting data re-use and sample efficiency.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Off-Policy Reinforcement Learning", "weight": 1.0} -->

*Off-policy RL methods* maintain a long horizon replay buffer $\mathcal{D}_{\text{roll}} = {\{{(s_{t},a_{t},s_{t + 1},r_{t},d_{t})}\}}$ consisting of past states $s_{t}$, actions $a_{t}$, subsequent states $s_{t + 1}$ from the environment transitions, the observed rewards $r_{t}$, and the done signal $d_{t}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Off-Policy Reinforcement Learning", "weight": 1.0} -->

where above the expectation $E$ is taken over $({{s_{t},a_{t},r_{t},s_{t + 1}} \sim \mathcal{B}})$ sampled from the replay buffer $\mathcal{B}$, and each $a_{t + 1}$ is sampled independently from the current target policy ${}_{\left. \right.¯}^{}{( \cdot \mid s_{t + 1})}$. To avoid overestimation bias, we set ${Q_{targ}{(s,a)}} = {\frac{1}{M}{\sum_{i}Q_{i}}}$ to be a mean over critic networks, described in the Appendix (Section˜A.1. ‣ Algorithmic Choices ‣ A.1 Key Design Decisions ‣ Appendix A A Practitioner’s Guide to OGPO")). (fujimoto2018addressing; chen2021randomized).Importantly, (2.3) enables data collected by policies from previous training epochs, thereby increasing sample efficiency.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Generative Control Policies", "weight": 1.0} -->

Current robotic control policies use generative models as parameterizations of control policies. Following (pan2025much), we call these generative control policies (GCPs). GCPs represent a stochastic policy $( \cdot \mid s)$ as a series of iterative computation steps, defined by a mapping $\overline{}:{S \times A \times N}$. Given a state $s_{t}$, the policy first samples $a_{t,K} \sim \overline{}{( \cdot \mid a_{t,k} = \varnothing,k = K,s_{t})}$ where $k$ is a GCP timestep. Next, we sample $a_{t,{k - 1}} \sim \overline{}{( \cdot \mid a_{t,k},k,s_{t})}$ which leads to is an action $a_{t,0}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Generative Control Policies", "weight": 1.0} -->

We compactly denote the distribution of this action given the observation as $a_{t,0} \sim {( \cdot \mid s_{t})}$, turning the GCP into a standard policy. Our iteration conventions are *decreasing* in $K$, those in diffusion models. Following the same conventions, we also refer to the index $k$ as the "denoising step."

<!-- chunk {"id": "body-0016", "role": "body", "section": "Flow-Based GCPs", "weight": 1.0} -->

We focus on a popular class of GCPs: flow-based control policies (black2024pi_0). As discussed in Appendix˜C: A Unifying Abstraction"), our methods and baselines can also be instantiated with Diffusion-based policies (chi2023diffusion) and other controller parameterizations (pertsch2025fast; frans2024one; pan2025much). Flow policies are pretrained using the flow-matching objective: given training pairs $(s,a)$, we sample noise $z \sim {N{(0,\mathbf{I})}}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Flow-Based GCPs", "weight": 1.0} -->

With a continuous noise index $\in {\lbrack 0,1\rbrack}$, we define an interpolated action $a_{} = {+ {{({1 -})}z}}$, and optimize a velocity field $v{(a_{} s)}$ by minimizing $E_{(s,a,)} \parallel v{(a_{} s)} - {(a - z)} \parallel^{2}$ (albergo2023stochastic; lipman2022flow). Inference is performed by discretizing an ordinary differential equation (ODE) which reverses the noising process $a_{t,{k - 1}}:={a_{t,k} + {\frac{1}{K}v{(a_{t,k},{k/K},s)}}}$, with $a_{t,0} \sim {N{(0,\mathbf{I})}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Off-Policy Generative Policy Optimization", "weight": 1.0} -->

We propose Off-Policy Generative Policy Optimization, OGPO, an off-policy full-policy finetuning method for generative control policies. We begin by introducing the basic algorithm, and then describe an improved variant, OGPO+. We provide summary pseudocode in Algorithm˜1, and defer full implementation details to Appendix˜B.

<!-- chunk {"id": "body-0019", "role": "body", "section": "OGPO: On-Policy PPO for Off-Policy Policy Extraction", "weight": 1.0} -->

OGPO is designed for applications, such as robotic manipulation, where environment interactions are more costly than computation, and where action gradients with respect to $Q_{targ}$ are noisy or inaccurate (suh2022differentiable). We maintain off-policy critic learning that facilitates data reuse, and propose a *fully parallelizable zero-order optimizer* that solves Eq.˜3.1, avoiding backpropagation through the denoising chain and differentiation with respect to the target network.

<!-- chunk {"id": "body-0020", "role": "body", "section": "OGPO: On-Policy PPO for Off-Policy Policy Extraction", "weight": 1.0} -->

Our starting point is the bi-level MDP formulation adopted from (ren2024diffusion) (Figure˜2). Following (black2023training), we view sequences $a_{{t,K}:0} = {(a_{t,K},\ldots,a_{t,0})}$ as trajectories in an *denoising* MDP, where time is indexed by denoising step $k$, and state and action at step $k$ are $a_{t,k}$ and $a_{t,{k - 1}}$, respectively.

<!-- chunk {"id": "body-0021", "role": "body", "section": "OGPO: On-Policy PPO for Off-Policy Policy Extraction", "weight": 1.0} -->

ren2024diffusion embeds this action-level MDP into the environment-level MDP $M_{\text{Env}}$, resulting in an *bi-level* MDP where states are ${\overline{s}}_{t,k} = {(s_{t},a_{t,k})}$, the actions are $a_{t,{k - 1}}$, and the indices $(t,k)$ are lexicographically increasing in $t$ and decreasing in $k$. Figure˜2 depicts this bi-level MDP: transitions within each gray block occur within the denoising-level MDP, and between gray blocks are transitions in $M_{\text{Env}}$; see Figure˜21 for further details. The DPPO algorithm proposed by (ren2024diffusion) then applies on-policy PPO at the level of this bi-level MDP. Whilst avoiding the aforementioned pathologies associated with backpropagation, this method gives up the sample efficiency afforded by off-policy critic learning.

<!-- chunk {"id": "body-0022", "role": "body", "section": "OGPO: On-Policy PPO for Off-Policy Policy Extraction", "weight": 1.0} -->

Our key insight is that denoising-trajectories can be generated purely *computationally* from policy inference, as they occur in the "imagination" of the GCP. We can then use critic learning to sever the bi-level MDP just before environment-MDP state transitions ( red line, Figure˜2), enabling zero-order optimization applied only to the denoising-level MDP. As compared to backpropagation approaches to solving Eq.˜3.1, our approach avoids (i) backpropagation through time and (ii) differentiating through the Q-function. Moreover, as compared to pure on-policy zero order optimization through the bi-level MDP (ren2024diffusion), our zero-order updates are (i) performed purely computationally, in the "imagination" of the denoising process (ii) fully parallelized across large batch sizes (iii) used to optimize a critic network, facilitating full reuse of environment-level trajectories.

<!-- chunk {"id": "body-0023", "role": "body", "section": "OGPO: On-Policy PPO for Off-Policy Policy Extraction", "weight": 1.0} -->

Moreover, (iv) the problem horizon of the denoising-level MDP scales only with the denoising steps $K$, and not $K \times \text{(task horizon)}$. Concretely, we apply the PPO algorithm (schulman2017proximal), a zero-order policy gradient method, to optimize over the denoising MDP.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Multiple Denoising-Trajectory Sampling", "weight": 1.0} -->

Because denoising-trajectories are generated computationally, they can be resampled *fully in parallel* from *any* given state $s_{t}$ in the replay buffer. Moreover, $Q_{targ}$ can be evaluated without taking a single transition step in the environment. Taking advantage of this, we evaluate our PPO loss over an average of a batch of parallel-sampled trajectories, purely in the "imagination" of the GCP. By analogy to policy optimization in large language models (LLMs), we can think of a state $s_{t}$ in the buffer as a "context" and the denoising trajectory $a_{{t,K}:0}$ as a "response". We draw inspiration from the GRPO algorithm (shao2024deepseekmath) in LLM post-training, where multiple responses are sampled in parallel from a given prompt, and gradients are averaged together to reduce gradient variance.^66^6GRPO includes an additional variance normalization term, which we omit.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Multiple Denoising-Trajectory Sampling", "weight": 1.0} -->

Eq.˜3.3 averages both over the states $s_{t}^{(i)}$ from the buffer ("prompts"), and denoising-trajectories generated in parallel from each given state ("responses"). This yields a normalization factor of $N_{\text{tot}}:={N_{\text{batch}} \cdot N_{\text{group}}}$. Moreover, parallel sampling facilitates estimating the value baseline via a direct Monte-Carlo approximation ${\hat{V}}^{(i)}\leftarrow{\frac{1}{N_{\text{group}}}{\sum_{j}{Q_{targ}{(s^{(i)},a_{0}^{(i,j)})}}}}$, obviating the need to learn a separate value-prediction network.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Debiasing Noise Injection for Flow Policies", "weight": 1.0} -->

We instantiate OGPO for flow-based policies. To evaluate the likelihood /in Eq.˜3.2, we must ensure the denoising-level action likelihoods $a_{{k - 1},t} \mid {a_{k_{t}},s_{t}}$ are non-singular. ReinFlow (zhang2025reinflow) modifies the bi-level PPO algorithm of (ren2024diffusion) for flow-based policies, achieving this by adding additional Gaussian noise to each flow step.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Debiasing Noise Injection for Flow Policies", "weight": 1.0} -->

In OGPO, we anecdotally observe that naively adding noise can degrade policy performance by changing the marginal distributions of actions $a_{t,k}$ generated during denoising. We therefore introduce a correction proposed by albergo2023stochastic which (in the infinite step limit) ensures the per-denoising-step marginal distributions of noise-augmented actions match those of standard flow sampling; see also liu2025flow. See Section˜E.2 for details.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Debiasing Noise Injection for Flow Policies", "weight": 1.0} -->

1: for each environment step until done do
2: Execute at ∼ ¯(⋅∣st), and update buffer ℬ ← (st rt,st + 1,done). 2: % Standard Critic Update
3: Update critic networks …,M using empirical TD Error (2.3) over ℬ ∼ 𝒟roll. 3: % Actor Update via Multiple Denoising Trajectories
5: Sample state s(i) from ℬ, and action trajectories aK: 0(i,j) ∼ ¯(⋅∣s(i)) for 1 ≤ j ≤ Ngroup.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Improving OGPO by Mitigating Critic Over-exploitation", "weight": 1.0} -->

In this section, we identify a major limitation of OGPO: over-exploitation of learned critics due to highly expressive policy updates (Section˜4.1).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Improving OGPO by Mitigating Critic Over-exploitation", "weight": 1.0} -->

OGPO+ (Section˜4.2), which combines OGPO with behavior cloning regularization on *success-only* trajectories

<!-- chunk {"id": "body-0031", "role": "body", "section": "Improving OGPO by Mitigating Critic Over-exploitation", "weight": 1.0} -->

OGPO+CA (Section˜4.3), which uses a *conservative advantage* for policy extraction, thereby *drastically mitigating the "dip" in offline-to-online adaptation*

<!-- chunk {"id": "body-0032", "role": "body", "section": "Improving OGPO by Mitigating Critic Over-exploitation", "weight": 1.0} -->

For a practitioner, we recommend using OGPO+CA for highly stable policy extraction.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Improving OGPO by Mitigating Critic Over-exploitation", "weight": 1.0} -->

We find that Eq.˜4.1 always yields some improvement, but this benefit is most pronounced in pixel-based environments; it makes a marginal difference in state-based runs on pre-training from full data.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

To identify improved design choices, we consider experiments on the state-based and image-based Robomimic tasks, which are described in greater detail in Section˜5.1 Improve Over Popular Baselines?"). For state-based runs, we use all state-information directly; for image based runs, we pass image observations using a frozen PaliGemma VLM backbone from the pre-trained $0.5$ VLA (pifive). Further details are given in Appendix˜I.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Vanilla OGPO Over-exploits Imperfectly Learned Critics", "weight": 1.0} -->

Recall that OGPO makes PPO-style updates to the denoising MDP. The combination of the expressive generative policies and PPO updates on the full-denoising trajectory risks causing OGPO to over-optimize the critic, overfitting to advantages which are poorly estimated.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Success-Speed Tradeoff", "weight": 1.0} -->

The typical "sparse-reward" manipulation setting assigns reward of $- 1$ each time step a task remains uncompleted. Thus, minimizing cumulative reward introduces a tension between completion *rate* and completion *speed*. As a result, OGPO may attempt to finish tasks too quickly, causing success rates to drop, harming future exploration training stability. This success-speed tradeoff is visible in Figure˜4(a), where we see average task length rapidly improves, but success rate plateaus. Anecdotally, we found that the variance-reduced critic update Eq.˜4.1 did not improve this tradeoff.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Overexploitation is Exacerbated in Pixel-Based RL", "weight": 1.0} -->

We observe that vanilla OGPO has more severe exploitation in pixel-based settings. We consider a Robomimic Square environment described above,

<!-- chunk {"id": "body-0038", "role": "body", "section": "Overexploitation is Exacerbated in Pixel-Based RL", "weight": 1.0} -->

where pixels are feautrized using a frozen PaliGemma VLM backbone from $0.5$. To isolate the effects of pixels, we compare four variants: state-based actor/state-based critic; pixel-based actor/state-based critic pixel-based actor/pixel-based state-based actor/pixel-based critic. We plot variants (1-3) in Figure˜5, and omit due to collapsing runs. We that the policy trains effectively for both state-based critic runs &, but fails on &, suggesting that *pixel-based* critics prevent learning. We hypothesize that such critics learn less accurately due to the richer observation space, making them more susceptible to exploitation via OGPO. Anecdotally, we found that the variance-reduced critic update made modest but very limited improvements to the pixel-based critics, suggesting the need for further interventions.

<!-- chunk {"id": "body-0039", "role": "body", "section": "OGPO+: Regularizing OGPO With Behavior Cloning of Successful Trajectories", "weight": 1.0} -->

To remedy critic overexploitation, OGPO+ incorporates a regularization term applied only to actions from successful trajectories. This biases policy improvement toward replicating only the actions that led to success (oh2018self). Specifically, we maintain a *success buffer* $\mathcal{D}_{\text{succ}} \subseteq \mathcal{D}_{\text{roll}}$ containing transitions from episodes that achieve task success. During training, we sample mini-batches from $\mathcal{D}_{\text{succ}}$ and compute

<!-- chunk {"id": "body-0040", "role": "body", "section": "OGPO+: Regularizing OGPO With Behavior Cloning of Successful Trajectories", "weight": 1.0} -->

where BcLoss is the appropriate behavior cloning objective (e.g., denoising score matching for diffusion policies, or flow matching loss for flow policies). Success-imitations ground the policy toward known good actions, while the PPO objective more aggressively explores improvements.

<!-- chunk {"id": "body-0041", "role": "body", "section": "OGPO+: Regularizing OGPO With Behavior Cloning of Successful Trajectories", "weight": 1.0} -->

(Optional) Best-of-N Inference. In many domains, such as language modeling, evaluating the quality of an action, or "verification" is learned more quickly and accurately than "generation" of good actions. This verification-generation gap (setlur2025e3) motivates the popular practice of Best-of-$N$ sampling (brown2024large), where one generates multiple proposal actions, and selects the best using a learned verifier.

<!-- chunk {"id": "body-0042", "role": "body", "section": "OGPO+: Regularizing OGPO With Behavior Cloning of Successful Trajectories", "weight": 1.0} -->

Best-of-$N$ sampling has seen widespread adoption in RL training of robotics policies (mark2024policy; dong2025expo; li2025reinforcement), using the target critic as verifier. In, OGPO+ we do the same with a slightly modified critic $Q_{\text{BoN}}$ described in Section˜A.1. ‣ Algorithmic Choices ‣ A.1 Key Design Decisions ‣ Appendix A A Practitioner’s Guide to OGPO"). We remark that, due to the aggressive policy extraction, Best-of-$N$ inference yields only marginal additional performance; the success buffer, as described above, is crucial. Thus, we recommend *omitting* Best-of-$N$ when inference cost is constrained.

<!-- chunk {"id": "body-0043", "role": "body", "section": "OGPO+CA: Mitigating the Offline-to-Online Performance Dip via Conservative Advantages", "weight": 1.0} -->

A second challenge in offline-to-online RL is the pervasive "dip" in performance that arises transitioning from offline pretraining to online RL. Warm-starting methods like (uchendu2023jump; zhou2024efficient) propose the use of high update-to-data (UTD) ratios and/or offline datasets during online RL, and the use of pessimistic critic updates. Anecdotally, we find that neither of these methods suffice. Moreover, from Figure˜7(a), we see that both over- and under-estimation of the $Q$ values are possible, and both outliers potentially destabilize training. Thus, we instead to have the policy extraction step maximize the conservative advantages. This is made possible because our zero-order extraction takes advantages directly, and also accounts for the fact that global additive errors in critic values are less salient than incorrect *advantage* estimation.

<!-- chunk {"id": "body-0044", "role": "body", "section": "OGPO+CA: Mitigating the Offline-to-Online Performance Dip via Conservative Advantages", "weight": 1.0} -->

where we recall $A_{j,m} = {{Q_{_{m}}{(s^{(i)},a_{0}^{(i,j)})}} - {\frac{1}{N_{\text{group}}}{\sum_{i^{\prime} = 1}^{N_{\text{group}}}{Q_{_{m}}{(s^{(i)},a_{0}^{(i,j)})}}}}}$ is the group-wise advantage using the $m$-th network in the ensemble. Eq.˜4.5 provides a non-zero advantage (and thus updates the policy) if and only if *all advantages* have the same sign, thereby robustifying updates to estimation errors in the critic networks. As shown in Figure˜7(b), we we see that policy extraction with conservative advantages also improves the calibration of critic estimation, in that critic values in earlier states of training more tightly track those in later stages.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conservative Advantages (OGPO+CA) Enable Stable Training on Images", "weight": 1.0} -->

Finally, we consider Robomimic tasks with image observations paired with robot proprioception information as a challenging setting for Q-learning and subsequently, policy extraction. From Fig.˜8 Enable Stable Training on Images ‣ 4 Improving OGPO by Mitigating Critic Over-exploitation"), we see that merely SFT via success buffer is not sufficient to guide policies to convergence. We observe that besides preventing the offline-to-online performance "dip", OGPO+CA also plays a crucial role in stabilizing policy improvement in high dimensional settings where learning Q-values over the large embedding spaces, proprioceptions, and actions is challenging. Moreover, baselines such as DSRL and EXPO fail to converge in image-based settings with no offline data in the replay buffer.

<!-- chunk {"id": "body-0046", "role": "body", "section": "When does Full-Finetuning (OGPO) Improve Over Popular Baselines?", "weight": 1.0} -->

In this section, we carefully compare OGPO, OGPO+, and OGPO+CA to a number of popular baselines to elucidate the merits and limits of its design philosophy--- full policy fine-tuning, off-policy critic learning, and PPO policy extraction. Our experiment environments are representative of many common challenges in robot learning (e.g. high precision, long horizon, mixed data quality), and baselines cover competing design philosophies (e.g. steering, residual learning).

<!-- chunk {"id": "body-0047", "role": "body", "section": "When does Full-Finetuning (OGPO) Improve Over Popular Baselines?", "weight": 1.0} -->

Summary of Findings. We summarize comparisons to other off-policy methods in Table˜1 Improve Over Popular Baselines?"). Each method has two columns: left denotes if the method converges with task-optimized hyperparameters, and right denotes fixed hyperparameters across all tasks within the criterion (see Appendix˜J). The markings are explained in the table caption.

<!-- chunk {"id": "body-0048", "role": "body", "section": "When does Full-Finetuning (OGPO) Improve Over Popular Baselines?", "weight": 1.0} -->

We find that OGPO is able to learn in sparse-reward tasks with mixed/partial data quality and on high-precision/long horizon tasks, whereas other methods struggle in one or more of these regimes. It also exhibits (often times drastic) gains in sample efficiency compared to these methods, and order-of-magnitude improvements related to the on-policy DPPO algorithm. However, OGPO is less performant on the dense-reward tasks from the Adroit Hand benchmark (Figure˜11 Improve Over Popular Baselines?")).

<!-- chunk {"id": "body-0049", "role": "body", "section": "When does Full-Finetuning (OGPO) Improve Over Popular Baselines?", "weight": 1.0} -->

Comparisons are detailed further in Section˜5.2 Improve Over Popular Baselines?"). Sample efficiency improvements v.s. DPPO are expected (off- vs. on-policy), and we attribute gains against off-policy baselines to exploration behavior and expressive policy updates, studied in Section˜6.1. Appendix˜H ablates the merits of zero-order policy updates vs. backpropagation through time, the role of *negative-advantage gradients* in encouraging exploration, and the enhancements distinguishing OGPO and OGPO+.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Baselines. We compare against the baselines mentioned in Section˜7.3, which are described in more detail in Appendix˜F In short, we consider: (i) DPPO (ren2024diffusion), representative of on-policy learning, (ii) DSRL (wagenmaker2025steering), representative of off-policy noise steering (iii) EXPO (dong2025expo), representative of learning residual corrections to the GCP, and (iv) to a variant of QC (li2025reinforcement) representative of behavior cloning policy extraction. We do not compare to ReinFlow (zhang2025reinflow) due to reported reduced sample efficiency compared to DPPO, making the latter a more compelling baseline. We also skip comparison to PA-RL (mark2024policy) for reasons described in Section˜F.6 ‣ Appendix F Baselines"). Lastly, we introduce a steering+residual learning baseline, (v) S/R, combining DSRL and EXPO to (hypothetically) yield the benefits of both. For a fair comparison with OGPO+, we implement each baseline with its own best-practices, as described in Appendix˜F.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Environments. Our simulation environments are chosen to elicit key challenges faced in modern robot learning: *Robomimic:* To test high-precision robotic control, we use three Robomimic tasks (robomimic2021): Square (medium-horizon insertion), Toolhang (long-horizon multi-step insertion), Transport (bi-manual long-horizon transfer). Square and Transport use Multi-Human (MH) datasets; Toolhang uses Proficient-Human (PH) with BC stopped at 50% success. *Franka Kitchen:* We use the Franka-Kitchen benchmark (gupta2019relay) with a Franka robot manipulating 4 kitchen objects, testing sensitivity to multi-step trajectories with complete demonstrations ($\text{Kitchen-Complete})$, randomized subtask orders (Kitchen-Mixed), and sequential partial trajectory data (Kitchen-Partial).

<!-- chunk {"id": "body-0052", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

*Adroit:* To test performance in dextrous manipulation tasks with dense-reward, we use the 24-DoF Adroit Hand benchmark:Door-v1, Hammer-v1, Pen-v1, Relocate-v1 for door opening, hammering, pen reorientation, and object relocation. Expert datasets from D4RL/Minari. *LIBERO:* Finally, to test image-based language-conditioned manipulation, we use the Robomimic and LIBERO benchmarks (liu2023libero). Further details are given in Appendix˜I.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Experimental Regime: Online RL from a BC Checkpoint. We emulate real-world robot learning settings where large-scale pretrained policies with varying levels of online success rates are deployed to learn novel tasks without access to offline datasets during online RL. Thus, we pre-train a flow GCP for all baselines, clip it to at most 50% success rate, and use the same BC checkpoint for all baselines in online RL without additional data. Full details in Section˜J.1.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Comparison to other methods", "weight": 1.0} -->

Expressivity: Full-Policy Finetuning (OGPO) vs. Steering (DSRL) vs. Residual (EXPO). Next, we compare OGPO to performant off-policy alternatives that do not fine-tune the full GCP across 11 aforementioned tasks. *Steering* (DSRL) can be sample-efficient but relies on sufficient base policy action coverage, leading to suboptimal performance when the base policy's performance is poor, such as in Kitchen tasks. Further, by not updating later steps of the GCP, steering struggles on high-precision tasks such as the Adroit task suite. We also empirically found it to be sensitive to hyperparameters; in some tasks, DSRL performance crashes despite heavy tuning. We attribute some of this instability to our use of DSRL on a flow-based GCP instead of a diffusion-based GCP; the original paper uses diffusion GCPs for low-data-coverage experiments. However, we are also more sample-efficient than DSRL's paper-reported numbers on shared tasks.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Comparison to other methods", "weight": 1.0} -->

*Residual learning* (EXPO) performs well when the base policy is strong and thus only minor residual corrections are needed (it is highly performant in Adroit in Figure˜9 Improve Over Popular Baselines?")), but, like steering (DSRL), it generally performs poorly or is unstable when the base policy performance starts lower (Kitchen and most Robomimic tasks). We note that when given offline data, EXPO can perform well (see Figure˜11 Improve Over Popular Baselines?")), but our experimental regime is without access to the pre-training data. Our *Steering + Residual Learning* (S/R) baseline combines EXPO and DSRL; we plot sample efficiency curves in Robomimic tasks in Figure˜24, where we see that it is better than EXPO/DSRL alone in Square, albeit still worse compared to OGPO, and demonstrates unstable training in the high precision Toolhang task.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Comparison to other methods", "weight": 1.0} -->

Off-Policy Learning vs. Self-Distillation/Behavior Cloning (BC) with QC. Next, we compare *policy extraction* methods. We find the action-chunked BPTT variant proposed in the QC paper to perform poorly (Fig.˜16) on flow policies, and thus use a variant that explores online with Best-of-$N$ action sampling and fine-tunes the BC policy on transitions from the online replay buffer. QC plateaus at lower performance for most tasks, requires more task-specific hyperparameter tuning, and has worse sample efficiency. We attribute this to SFT's inability to expand the support of the GCP action distribution, required for sufficient exploration.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Comparison to other methods", "weight": 1.0} -->

Off-Policy OGPO vs. On-Policy DPPO. Finally, we compare OGPO+ against DPPO, where the major difference between the two is that OGPO+ truncates the bi-level MDP proposed by DPPO at the end of each denoising trajectory with terminal rewards coming from an off-policy Q-function,

<!-- chunk {"id": "body-0058", "role": "body", "section": "Comparison to other methods", "weight": 1.0} -->

while DPPO treats the entire bi-level MDP as a single MDP to train with on-policy RL. On final success rates across Robomimic Square and Transport, this off-policy modification results in DPPO taking $\sim 10 \times$ longer to reach the final success rates achieved by OGPO+. Overall, we find that both OGPO and OGPO+ outperform DPPO's paper-reported results in both sample efficiency and final performance across all shared tasks, even with matched network architectures and action chunk lengths.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Does OGPO Encourage Exploration?", "weight": 1.0} -->

By aggressively exploiting the critic (Section˜4), OGPO generates actions beyond the support of the offline data distribution used in the BC phase (Figure˜13, *left*), resulting in high task success as well high *task efficiency*, measured in terms of time-steps to completion.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Does OGPO Encourage Exploration?", "weight": 1.0} -->

Whereas diversity, optimality and task efficiency are often regarded as being at odds (huang2025self; setlur2025e3), we show that OGPO accomplishes all simultaneously. Below, we present extensive evidence for this finding, and propose a mental model, summarized in Figure˜13, *right*, as to how OGPO achieves this affect.

<!-- chunk {"id": "body-0061", "role": "body", "section": "OGPO drives greater trajectory diversity", "weight": 1.0} -->

We study the PushT task (chi2023diffusion), a classical example of trajectory-level multimodality, where a blue-dot pushes a gray "T" to the green goal configuration (Figure˜14). We consider two reward settings: the classical sparse reward $r = {- {\mathbf{I}{\{\text{not done}\}}}}$, and an "action-compensated" reward $r = {- {({{\mathbf{I}{\{\text{not done}\}}} + {\| a_{t}\|}})}}$ which penalize per-step action magnitudes (due to PushT's physics enabling unbounded actions). We compare OGPO against natural baseslines and visualize the learned trajectories in Figure˜14. Here, dark points represent the initial actions in the trajectory, and the color lightens to yellow ones as the time-step progresses.

<!-- chunk {"id": "body-0062", "role": "body", "section": "OGPO drives greater trajectory diversity", "weight": 1.0} -->

In the absence of action-compensation, OGPO learns to take larger action that complete the trajectory in fewer time steps (task-efficiency), and with full success.^77^7Note that without action-compensation, path-*length* is not constrained, only time to completion.

<!-- chunk {"id": "body-0063", "role": "body", "section": "OGPO drives greater trajectory diversity", "weight": 1.0} -->

Still, OGPO *preserves a relatively wide manifold of valid actions* (ren2024diffusion), and seems to *preserve additional trajectory-level modes*. On adding an action compensation term, OGPO takes smaller steps and prunes many of its modes, favoring modes which allow shorter path-length. This makes sense as OGPO directly exploits the critic, yielding actions closer to optimal and further from the base policy.

<!-- chunk {"id": "body-0064", "role": "body", "section": "OGPO drives greater trajectory diversity", "weight": 1.0} -->

Comparing to the baselines, QC and DSRL show limited manifold expansion, remaining closer to the BC initialization. EXPO's residual policy facilitates support expansion but not optimal policy extraction. This can be seen by a range of corrective actions being taken near the T-shape handle. Lastly, we test OGPO-NN, which zeros out all negative advantages and retains only positive advantages. Whereas prior work (setlur2025e3) would suggest that negative advantages *increase exploration*, we find that they also seem necessary for "sharpening" (huang2025self) towards optimal modes.

<!-- chunk {"id": "body-0065", "role": "body", "section": "OGPO preserves action variance \"orthogonal\" to task success", "weight": 1.0} -->

We now uncover the *concrete mechanism* by which OGPO preserves both *action* and *trajectory*-level diversity. We compare OGPO to relevant baselines on Toolhang, isolating two critical states at times $t = 9$ (the needle being transported toward the hole) and $t = 28$ (the wrench being inserted) from a single, shared demonstration trajectory with maximal variance in Q-values. Each policy is trained from the same BC checkpoint, removing spurious variation^88^8note that QC uses additional critic distillation during the BC phase, leading to different actions after offline training.

<!-- chunk {"id": "body-0066", "role": "body", "section": "OGPO preserves action variance \"orthogonal\" to task success", "weight": 1.0} -->

For each time step, we pool together 64 actions from policies trained with each baseline, compute a common UMAP embedding (mcinnes2018umap), and visualize them in Figure˜15, color coding actions by method. For the OGPO actions, we also plot arrows that compute the gradient ${\nabla_{a}Q}{(s,a)}$ of the mean $Q$ function (from after training), which gives the local direction of steepest ascent for actions to improve the critic value (see caption for details).

<!-- chunk {"id": "body-0067", "role": "body", "section": "OGPO preserves action variance \"orthogonal\" to task success", "weight": 1.0} -->

When $> 0.6$ we consider majority of actions having the same ${\nabla_{a}Q}{(s,a)}$ unit vectors, and $\leq 0.6$ as there not being a consensus, at which, we compute K-means clusters over ${\nabla_{a}Q}{(s,a)}$ with cluster centers shown as black crosses in Figure˜15. We include snapshots across four phases of training, from offline to completion.

<!-- chunk {"id": "body-0068", "role": "body", "section": "OGPO preserves action variance \"orthogonal\" to task success", "weight": 1.0} -->

Our findings reveal that OGPO increases variance in a *selective* manner. At $t = 9$, there is minimal trajectory level diversity due to the ensuing precision requirements. Thus we see OGPO exhibits the *most aggressive* shrinking of action variance. However, at $t = 28$, greater action action variance is permitted, and preserved even at the *end of training* (Figure˜15, *bottom right*). However, OGPO does not increase variation isotropically: rather, the remaining action-variance as even *orthogonal* to the critic gradient. Note that, along these directions, differences in actions have *zero effect on critic values*, to first order. Therefore, we find the OGPO *allocates large variance along directions which do not affect task success*.

<!-- chunk {"id": "body-0069", "role": "body", "section": "OGPO preserves action variance \"orthogonal\" to task success", "weight": 1.0} -->

At the same time, OGPO (a) sharpens the distribution orthogonal to these directions (resulting in the "thin" ellipsoid seen in Mid/End training in at $t = 28$), while (b) aggressively "stretching" the action distribution to align with critic gradients in parts of the action distribution when gradients ${\nabla_{a}Q}{(s,a)}$ exhibit strong consensus, e.g. $> 0.6$. Thus, OGPO can *both* optimize the critic for task performance/completion time while *simultaneously* preserving as much action diversity as possible.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Mental model: mode-preservation via orthogonal action variance", "weight": 1.0} -->

Here, we propose a mental model for how OGPO's selective "stretching" tendency preserves trajectory-level multimodality. We depict a mental-model of this trajectory-level multimodality in Figure˜13. We consider a task with two modes---navigating left or right around an obstacle. The optimal branching point is depicted with (*red dots*). Below these, the optimal actions approach the obstacle, whereas above, they move around it. In the center, ${\nabla_{a}Q}{(s,a)}$ points vertically (either up or down). OGPO preserves variance orthogonal to this direction, preserving actions which ultimately branch into the left and right-modes. Thus, allocating variance at the "decision point", while "stretching" actions at the extremes, sharpens the trajectory distribution around *both* feasible modes.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Why does OGPO preserve exploration?", "weight": 1.0} -->

An important question to ask is: why does OGPO preserve exploration better than alternatives? A comprehensive account would warrant further study, which we defer to future work. Here, we hypothesize that the key factor which allows OGPO to preserve variance comes from finetuning all the steps of the generative process; in Appendix Fig.˜23, we observe that other full-finetuning methods (e.g. FPO++ (yi2026flow)), also preserve variance, though to a slightly lesser degree. We hope to pursue the full breadth of this question in a future study.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Does PPO policy extraction outperform natural alternatives (AWR, FPO)?", "weight": 1.0} -->

PPO likelihood+clip
PPO likelihood+clip

<!-- chunk {"id": "body-0073", "role": "body", "section": "Does PPO policy extraction outperform natural alternatives (AWR, FPO)?", "weight": 1.0} -->

PPO likelihood+clip
PPO likelihood+clip

<!-- chunk {"id": "body-0074", "role": "body", "section": "Does PPO policy extraction outperform natural alternatives (AWR, FPO)?", "weight": 1.0} -->

exp(CFM))+clip
(exp(CFM))+clip

<!-- chunk {"id": "body-0075", "role": "body", "section": "Does PPO policy extraction outperform natural alternatives (AWR, FPO)?", "weight": 1.0} -->

We observe that OGPO uses a simple API: apply *any RL* algorithm to the denoising MDP whose terminal rewards are given by the critic.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Does PPO policy extraction outperform natural alternatives (AWR, FPO)?", "weight": 1.0} -->

where the policy loss under a parameter, for state $s$, denoising chain $a^{K:0}$, and advantage estimate ${\hat{A}}^{G}$ consists of a loss depending on $s,a^{K:0}$, and weighting depending on the advantage. To compare with alternatives, we decompose the loss into a separate terms depending on the advantage sign.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Does PPO policy extraction outperform natural alternatives (AWR, FPO)?", "weight": 1.0} -->

We now describe a number of alternatives based on this formulation Table˜2? ‣ 6 Understanding and Ablating The Merits of OGPO"). First, we compare to AW-OGPO, which uses exponentiated advantages as in peng2019advantage, but instead reweighs the OGPO likelihood ratio given in Eq.˜3.2. For both OGPO and AW-OGPO, we also introduce a positive-only variants of OGPO-NN and AW-OGPO-NN which zero the loss/weighting when advantages are zero. In addition, we introduce AWR-FM, a natural baseline which up-weights the conditional flow-matching (CFM) loss rather than PPO likelihoods. Generally, this underperforms AW-OGPO, so we omit the no-negative advantage variant. For all AWR-style runs, we perform per-task hyperparameter tuning to determine an optimal temperature parameter to ensure a steelman comparison. Finally, we compare to extraction via FPO++ (yi2026flow), which applies a number of novel design decisions detailed in Section˜H.4 ‣ Appendix H Ablations and Limitations of OGPO/OGPO+").

<!-- chunk {"id": "body-0078", "role": "body", "section": "Does PPO policy extraction outperform natural alternatives (AWR, FPO)?", "weight": 1.0} -->

All methods use the same replay data, critic training, and group-wise advantages.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Does PPO policy extraction outperform natural alternatives (AWR, FPO)?", "weight": 1.0} -->

As shown in Figure˜17? ‣ 6 Understanding and Ablating The Merits of OGPO"), AWR-FM fails across the Robomimic tasks, indicating that pure advantage-weighting of the flow loss is insufficiently expressive compared to likelihoods that use the full denoising MDP. Using the full likelihoods in AW-OGPO, positive-only AW-OGPO, and OFPO++ yields stronger performance, although not on par with OGPO+CA. In particular, the positive-variant of AW-OGPO outperforms that of normal AW-OGPO, by virtue of being more aggressive (note that regular AW-OGPO still has positive weights on likelihoods when advantages are negative), but still cannot reach full success on Toolhang. On the other hand, OFPO++ collapses on the long-horizon Transport task.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Does PPO policy extraction outperform natural alternatives (AWR, FPO)?", "weight": 1.0} -->

Unlike AW-OGPO/AW-OGPO-NN, removing negative-advantage gradients makes a minimal impact on OGPO for tasks like Square and Toolhang, where merely imitating high-valued action samples is sufficient to sharpen policy distributions (Figure˜17? ‣ 6 Understanding and Ablating The Merits of OGPO")). However, for a task like Transport, where avoiding suboptimal policy modes is critical for task success, we observe worse performance for both OGPO-NN as well as AW-OGPO-NN. This suggests that negative advantages are important for mitigating suboptimal action distributions learned during pretraining.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Which Further Design Decisions Explain the Performance of OGPO and OGPO+?", "weight": 1.0} -->

The following ablations are designed to systematically isolate various subcomponent decisions within OGPO and to explain which design choices align with maximizing sample efficient policy extraction. First, we compare OGPO's zeroth-order policy extraction to Backpropagation Through Time (BPTT) that backpropagates first order gradients via Q functions and through the entire GCP denoising chain. As shown in Figure˜16 directly backpropagating through the denoising chain often fails catastrophically, supporting our choice to optimize the GCP via importance sampling rather than through ${\nabla_{a}Q}{(s,a)}$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Which Further Design Decisions Explain the Performance of OGPO and OGPO+?", "weight": 1.0} -->

Second, using Figure˜19 as reference, Best-of-$N$ inference provides only marginal gains by itself and can increase oscillations when the critic is imperfect. This is consistent with the role of Best-of-$N$ as a verifier of critic learning at inference time, rather as a significant mechanism for policy improvement (chow2025inference; huang2025is). In contrast, the success buffer used in OGPO+ consistently improves sample efficiency and asymptotic performance by anchoring policy improvement to successful behavior.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Which Further Design Decisions Explain the Performance of OGPO and OGPO+?", "weight": 1.0} -->

We provide a mathematical basis for the intuition that conditional flow matching (CFM) loss between $\overline{}$, and the success buffer actions increases the GCP lower-bound on successful modes in Section˜E.3. Moreover, we modify the advantage computation from $\hat{A} = \frac{{Q_{targ}{(s_{t},a_{t,0})}} - \hat{V}}{\hat{}}$, where ${\hat{}}^{(i)}\leftarrow\sqrt{\frac{1}{N_{\text{group}}}{\sum_{j}\left( {{Q_{targ}{(s^{(i)},a_{0}^{(i,j)})}} - {\hat{V}}^{(i)}} \right)^{2}}}$ and find that GRPO-style variance normalization hurts performance.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Which Further Design Decisions Explain the Performance of OGPO and OGPO+?", "weight": 1.0} -->

Finally, we ablate the offline-to-online Q-learning recipe proposed in Warm Start RL (WSRL, zhou2024efficient) with and without Calibrated Q-Learning (CalQL, (nakamoto_cal-ql_2024)), and compare against OGPO, OGPO+, and OGPO+CA. We find that CalQL+WSRL slightly improves vanilla OGPO, but fail to mitigate the policy collapse as prevented by OGPO+ and OGPO+CA.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Generative Control Policies", "weight": 1.0} -->

The success of diffusion models in image generation (ho2020denoising; song2020denoising; rombach2022high) has inspired their adoption for robotic control. Diffusion Policy (chi2023diffusion) demonstrated that denoising diffusion probabilistic models (DDPMs) can effectively parameterize visuomotor policies by iteratively denoising action sequences conditioned on observations. Flow-matching policies (lipman2022flow; liu2022flow) offer a more efficient alternative by learning velocity fields that transport noise to action distributions through ordinary differential equations (ODEs), achieving comparable performance with fewer integration steps.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Generative Control Policies", "weight": 1.0} -->

Recent work has sought to improve the generative modeling capacity. Notably, shortcut models (frans2024one) condition on desired step sizes to enable few-step generation, while consistency models (song2023consistency) distill multi-step diffusion into single-step generation. Recently, (pan2025much) introduced Minimally Iterative Policies (MIP), demonstrating that two-step regression-based policies can match full flow model performance, suggesting that distributional learning may be less critical than previously believed. Orthogonally, tokenized autoregressive policies such as FAST (pertsch2025fast) encode continuous action chunks via discrete cosine transforms to enable efficient training of vision-language-action (VLA) models on high-frequency control data.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Generative Control Policies", "weight": 1.0} -->

For OGPO, we demonstrate flow and diffusion-based policies as representative of the general IGP formulation and leave generalization to other formulations as future work.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Reinforcement Learning for Robotic Policy Finetuning", "weight": 1.0} -->

The incorporation of Reinforcement Learning (RL) into robotic policy training mirrors the post-training paradigm in large language models (ouyang2022training; shao2024deepseekmath). On-policy methods such as REINFORCE (williams1992simple) and PPO (schulman2017proximal) update policies using only data from the current policy iteration, ensuring stable but sample-inefficient learning. DPPO (ren2024diffusion) extends PPO to diffusion policies by computing policy gradients through the denoising chain, while Reinflow (zhang2025reinflow) applies similar principles to flow-matching policies.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Reinforcement Learning for Robotic Policy Finetuning", "weight": 1.0} -->

Off-policy algorithms promise greater sample efficiency by maintaining replay buffers of past experiences. Classical approaches such as SAC (haarnoja2018soft), TD3 (fujimoto2018addressing), and REDQ (chen2021randomized) learn Q-functions from off-policy data to guide policy updates. Temporal difference learning mitigates the requirement of the policy to compute Monte Carlo return to the go. However, naive application to IGPs in the RL-finetuning regime can exhibit training instabilities due to large initial distributional shifts and value overestimation. To mitigate these, (mark2024policy; li2025reinforcement) proposed using Q functions merely to rank stochastic policy actions and fine-tuning the policy using the Best-of-N actions. However, driving policy improvement via Q-function ranking can be inefficient as it requires exploration away from the mean values of the flow policy.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Reinforcement Learning for Robotic Policy Finetuning", "weight": 1.0} -->

Concurrently, RL-100 (lei2025rl) presents a comprehensive real-world RL framework built on diffusion policies, demonstrating deployment-grade success rates across eight manipulation tasks. RL-100 adopts the same bi-level MDP formulation and clipped PPO surrogate as DPPO, unifying imitation and reinforcement learning under a single objective across both offline and online stages, and additionally incorporates consistency distillation for high-frequency deployment. While RL-100 demonstrates impressive real-world reliability, its policy optimization remains fully on-policy, requiring iterative offline data expansion to achieve sample efficiency. OGPO instead decouples the bi-level MDP via off-policy critic learning, achieving comparable or superior sample efficiency in simulation without requiring multiple rounds of offline RL pre-training.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Finetuning Strategies for Generative Control Policies", "weight": 1.0} -->

Existing approaches to finetuning GCPs differ along the axis of *what* is optimized. Steering methods, exemplified by DSRL (wagenmaker2025steering), optimize the distribution over initial noise $a_{K}$ while freezing the pretrained denoising network. This constrains policy improvement within the support of the pretrained IGP distribution. Residual policy approaches such as EXPO (dong2025expo) train an additional network $^{\text{res}}$ that modifies the final action $a_{\text{res}} = {{}_{}^{}{(a_{t,0},s_{t})}}$, allowing mode shifts within the BC policy support but fails to facilitate discovery of new behaviors.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Finetuning Strategies for Generative Control Policies", "weight": 1.0} -->

Policy-agnostic RL (PA-RL) (mark2024policy) and Q-chunking (QC) (li2025reinforcement) employ Q-functions to rank behavior cloned policies with high-value actions or use ${\nabla_{a}Q}{(s,a)}$. Q-learning with Adjoint Matching (QAM) (li2026q) uses adjoint matching to convert the critic's action-gradient into a step-wise training objective for expressive flow or diffusion policies, avoiding direct backpropagation through the full denoising process. In the image generation domain, Flow-GRPO (liu2025flow) concurrently applied GRPO (shao2024deepseekmath) to flow matching models for text-to-image alignment, sharing with OGPO the ODE-to-SDE conversion for injecting stochasticity into deterministic flow policies and the use of group-relative advantage estimation over parallel denoising trajectories.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Finetuning Strategies for Generative Control Policies", "weight": 1.0} -->

However, Flow-GRPO operates in the on-policy, bandit-like setting: rewards are terminal (image-level), the "environment" is a single-step generation with no dynamics, and advantages are estimated via group normalization of final rewards rather than learned Q-functions.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Finetuning Strategies for Generative Control Policies", "weight": 1.0} -->

In contrast, OGPO addresses the multi-step robotic control setting, where off-policy TD-learning is essential for sample efficiency across long environment horizons, and the two-level MDP structure enables reuse of costly environment transitions while performing on-policy updates purely within the denoising MDP. However, in addition to zero-order optimization via Q functions, OGPO performs SFT via Success Buffer actions for enhanced sample efficiency.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Conclusion and Limitations", "weight": 1.5} -->

We introduce OGPO, an approach that combines the best of on-policy and off-policy methods for fine-tuning generative control policies (GCPs) and enjoys high success rates and sample efficiency across numerous tasks. However, OGPO still has limitations, the most important being that the parallel denoising rollouts required to estimate Q-values can be prohibitively expensive for large VLA models due to the high inference costs. Future work focusing on Q-function learning fidelity can help ameliorate this limitation by reducing the number of parallel GCP rollouts.
