## Introduction

Agentic systems powered by large language models (LLMs) have been shown to significantly improve productivity and are now widely deployed in industrial settings \[openai2025codex, anthropic2025claudecode, openclaw2026\]. The data generated through agent usage, such as user replies, tool execution results, and GUI state transitions, constitutes a valuable source of insights for improving agent frameworks \[lee2026meta, zhang2024aflow\], building memory systems \[xu2025mem, rasmussen2025zep, wang2025mirix, chhikara2025mem0, packer2023memgpt\], and producing high-quality training data for the models \[ouyang2022training\]. However, both the infrastructure and methodology for leveraging such usage data to improve language models in real time remain little explored.

The effectiveness of real-time learning for agentic models hinges on the careful design of both infrastructure and methodology. On the infrastructure side, the RL server must be flexible enough to integrate with users' diverse and evolving agentic frameworks, and the optimization process must run asynchronously so as not to block inference-time usage. On the methodology side, the algorithm must fully exploit the extracted training signals while maintaining stability throughout optimization. In this work, we propose OpenClaw-RL, a framework that combines infrastructure and algorithmic innovations to achieve efficient and stable online optimization for personal agents.

We extend existing RL infrastructure \[slime_github, fu2025areal, sheng2025hybridflow, hu2024openrlhf\], which typically assumes batch data collection on the RL server, to support continuous learning for agentic models. In our setting, the RL server hosts the model behind an inference API. As user terminals query the model, the resulting interaction data is streamed back to the server over HTTP and used to train the model online. To extract training signals online, we identify the next state as a source of two complementary signal types: evaluative and directive. The evaluative signal is produced by a process reward model (PRM) that implicitly scores the preceding action: a user re-query signals dissatisfaction, a passing test signals success, and an error trace signals failure. Beyond scoring, the next state often carries directive information. For instance, when a user says "you should have checked the file first," the message specifies not only that the response was wrong but also how it should change at the token level. Directive signals are therefore extracted from such next states as token-level hints, providing guidance rather than a scalar reward. By hosting the PRM as a separate server, signal extraction runs asynchronously with respect to policy rollout, so training-signal collection does not block policy inference.

While RLVR methods are limited to scalar rewards and thus cannot convert directive signals into policy gradients \[shao2024deepseekmath, guo2025deepseek, hu2025open, yu2025dapo\], on-policy distillation methods \[agarwal2024policy, shenfeld2026self, hubotter2026reinforcement\] offer an alternative by allowing a teacher model, conditioned on a corrective hint, to provide token-level supervision to the student. Hindsight relabeling approaches \[hubotter2026reinforcement, zhang2023wisdom, shi2026experiential\] show that adding structured correction information to the context can substantially improve outputs, but these methods all operate on fixed datasets. In concurrent work, buening2026aligning improves online policy by directly prompting with next-state information, though the corrective hints remain implicit in the prompt rather than serving as explicit signals.

These distillation methods suffer from training instability and reduced effectiveness due to the distribution mismatch between teacher and student \[li2026rethinking\], a problem that is exacerbated when corrective hints are of low quality. We address this by proposing a novel hint-selection criterion based on the top-$k$ token overlap between teacher and student distributions. Among candidate hints, we select the one whose induced teacher distribution shares the most top-$k$ tokens with the student, either per token or aggregated over the sequence. Because the selected teacher already overlaps with the student in high-probability regions, distillation provides informative gradients while keeping the off-policy importance ratio close to unity, stabilizing the update. In addition, we apply a clip on the token-level log-probability difference to further stabilize training. Our analysis shows that evaluative and directive signals have complementary strengths: directive signals are more informative than the scalar rewards derived from evaluative signals, while evaluative signals are more frequent, since not every next state contains a useful hint. This motivates a hybrid RL objective that combines loss terms.

We demonstrate the effectiveness of OpenClaw-RL by first conducting main experiments on OpenClaw \[openclaw2026\]. Specifically, we simulate settings in which users from different professions use OpenClaw for their own work and evaluate how efficiently the model learns to align with their preferences. We find that OpenClaw-RL outperforms memory and skill-evolution methods in optimization efficiency. Furthermore, we extend the algorithm to a general agentic RL setting to study its robustness. OpenClaw-RL achieves better optimization than RLVR methods while remaining stable.

Beyond personalization, OpenClaw-RL scales to large-scale general agent deployment. Built on the asynchronous slime \[slime_github\] infrastructure, we support cloud-hosted parallel environments across terminal, GUI, SWE, and tool-call settings, covering the most common real-world agent deployment scenarios. To our knowledge, this is the first open-source RL framework to unify these diverse agent types under a single training infrastructure. Across these settings, OpenClaw-RL achieves strong optimization with promising training dynamics, and we further demonstrate that next-state signals are particularly valuable in long-horizon environments where sparse outcome rewards alone provide insufficient learning signal.

Figure 2: Optimize your OpenClaw simply by using it. We provide simulation results here.

### Contributions

Infrastructure for real-time personal agentic RL. We extend existing RL infrastructure to a server-client architecture that supports continuous, real-time learning from deployed agents. The system is flexible enough to integrate with users' diverse and evolving agent frameworks running on remote terminals, automatically extracts two complementary training signals, evaluative and directive, from observed next states, and runs signal extraction and policy optimization asynchronously so that neither blocks inference-time usage.

Stable hybrid RL objective with overlap-guided distillation. We propose a hybrid RL objective that unifies evaluative and directive signals into a single update, exploiting their complementary strengths. We introduce *overlap-guided hint selection*, which chooses the corrective hint whose induced teacher distribution maximally overlaps with the student's top-$k$ tokens, together with a log-probability-difference clip that bounds per-token advantages. Together, these keep the off-policy importance ratio close to unity and yield efficient, stable optimization.

First unified RL infrastructure for real-world agent settings. OpenClaw-RL is the first open-source RL framework to unify terminal, GUI, SWE, and tool-call agents under a single training infrastructure with cloud-hosted parallel environments, covering the most common real-world deployment scenarios and enabling direct comparison across agent types.

Comprehensive evaluation across personalization and general agentic RL. We first simulate users from different professions using OpenClaw simultaneously and show that OpenClaw-RL can make the model align to per-user preferences within around 10.3 sessions, more efficiently than memory and skill-evolution methods. We further extend the algorithm to a general agentic RL setting, where it achieves better optimization than RLVR baselines while remaining stable.

## OpenClaw-RL Infrastructure: Unified System for Personal and General Agents

We unify automatic optimization of personal OpenClaw agents and large scale agentic RL for general agents, including terminal, GUI, SWE, and tool-call settings, within a single framework.

We first describe the server--client architecture that enables integration with diverse and evolving agent frameworks through a stateless API (§2.1). We then present the fully decoupled asynchronous pipeline that extracts evaluative and directive signals from next states without blocking inference (§2.2). Finally, we show how the same infrastructure scales from sparse, session-based personal agent streams to dense, parallelized general agent across terminal, GUI, SWE, and tool-call settings (§2.3).

### Flexible Server--Client Architecture for Live Agents

OpenClaw-RL is built around an inference-API server--client architecture (Figure 1). The RL server hosts the policy $\pi_{\theta}$ behind a stateless completion API; users' agent frameworks, which may run on personal devices, terminals, or cloud instances, query the policy through this API and stream their interaction data back to the server over HTTP. This design imposes no constraint on the structure of the user-side framework: any agent that can issue API requests can act as a data source, and that framework may evolve, change tools, or be replaced entirely without reconfiguring the server.

Each API request is classified as either a *main-line turn* or a *side turn*. Main-line turns comprise the agent's primary responses and tool execution results, which form trainable samples. Side turns cover auxiliary queries, memory organization, and environment transitions; they are forwarded to the model but do not produce training data. Each request also carries a session identifier, allowing the server to demultiplex concurrent interaction streams from multiple users and attribute each turn to the correct conversation session. This classification allows the RL framework to precisely identify which turns belong to which sessions, enabling targeted training on main-line turns only. For personal agents, the model is connected through a confidential API for private and secure deployment, and multiple users can be served simultaneously without cross-session interference. For large-scale training of general agents, cloud-hosted environments connect through the same API, enabling scalable parallelization without architectural changes.

### Asynchronous Signal Extraction from Next States

The core architectural principle of OpenClaw-RL is full decoupling: policy serving, environment hosting, reward judging, and policy training run as four completely independent asynchronous components with no blocking dependencies between them. The model serves the next user request while the PRM judges previous responses and the trainer applies gradient updates. Weight updates are pushed to the serving engine at well-defined boundaries, so live users always see a consistent policy and never wait for training. The message of each new main-line request contains the reaction to the previous turn, whether a user's reply or an environment's execution result. This becomes the next-state signal $s_{t + 1}$ for the previous turn. The PRM is hosted as a separate inference server and is responsible for automatic signal extraction: given an action $a_{t}$ and the next state $s_{t + 1}$, it produces both an evaluative score and, when applicable, a directive hint. Because PRM judging is decoupled from policy serving, signal extraction can use a stronger model and run multiple votes per sample without affecting user-facing latency. This decoupling is what makes continuous training from live, heterogeneous interaction streams practical: no stream needs to be paused or batched to accommodate another component's schedule.

### Scalability: From Personal Agents to Real-World Agent Deployment

OpenClaw-RL is designed to operate across the full spectrum from single-user personal agents to large-scale multi-environment general agent deployment. For personal agents, the environment is a single user's device and the interaction stream is sparse, session-based, and highly personalized. Built on slime \[slime_github\], OpenClaw-RL inherits a scalable training infrastructure for general agents, and we further support cloud-hosted environments across diverse agent settings. Hundreds of parallel environments hosted on cloud services produce a dense stream of structured execution signals, enabling scalable RL training.

Specifically, OpenClaw-RL supports a broad set of general-agent scenarios that cover the most common real-world deployment settings in our open-source implementation (Table 1). Terminal agents are a core component of computer-use systems: they are efficient, cheap to scale, and naturally aligned with the text-based interface of LLMs \[claudecode2026, codexcli2026, seta\]. GUI agents cover capabilities that terminal agents cannot access directly, such as visual interfaces and pointer-based interactions, making them necessary for more general computer-use tasks \[wang2025ui, qin2025ui, wang2025opencua, xue2026evocua\]. SWE agents represent a particularly important class of coding agents, where the environment provides rich executable feedback through tests, diffs, and static analysis \[cao2026qwen3\]. Tool-call agents are also critical, since external tools improve both reasoning capability and factual accuracy \[feng2025retool\].

user response / tool-call results

Shell execution sandbox
stdout/stderr, exit code

Screen state + accessibility tree
Visual state diff, task progress

Code repository + test suite
Test verdicts, diff, lint output

API/function execution
Return values, error traces

Table 1: Supported agent settings and their environment characteristics.

Figure 3: Method Overview. For personal agents, we support both binary-reward optimization and on-policy distillation training. In our experiments, we find that their combination yields significant performance gains. For general agentic RL, in addition to standard RLVR, we provide integrated step-wise rewards and a simple but effective standardization approach [wang2026rlanything].

## Methodology: Learning from Next-State Signals

We convert next-state signals from heterogeneous interaction streams, including personal conversations, terminal interactions, GUI interactions, SWE tasks, and tool-call traces, into policy gradients.

We first show that the next state yields two complementary signal types, evaluative and directive, and introduce a hybrid RL objective that unifies them in a single per-token loss (§3.1). We then address the central stability challenge of hint-conditioned distillation by proposing overlap-guided hint selection and a log-probability-difference clip (§3.2). Finally, we describe how step-wise process rewards are integrated with outcome rewards to handle long-horizon general agentic settings (§3.3).

### Two Complementary Signals and A Hybrid RL Objective

Scalar PRM vote

Information per sample

Every scored turn
Turns with meaningful hint
Every scored turn

Table 2: Complementary properties of the evaluative and directive signals, and the hybrid objective.

### Evaluative signal

Given $(a_{t},s_{t + 1})$, the PRM is queried $m$ times and each query returns a vote in $\{{+ 1},{- 1},0\}$. We take the majority $r_{t} \in {\{{+ 1},{- 1},0\}}$ as the scalar reward at step $t$. The evaluative signal is dense by construction: every scored turn contributes a sample, regardless of whether the user reaction is explicit, such as "that worked," or implicit, such as a re-query or a passing test.

### Directive signal

When evaluating $(a_{t},s_{t + 1})$, the PRM is also asked to decide whether $s_{t + 1}$ contains a *meaningful* correction in the first place: extracting a hint is only worthwhile when the next state actually carries directive content, and forcing extraction otherwise would yield low-quality hints that destabilize training. If the answer is yes, the PRM distills $s_{t + 1}$ into a concise hint $h$ enclosed in \[HINT_START\]...\[HINT_END\]; if no, the turn produces no directive signal and contributes only the evaluative one. The hint is appended to the prompt as $s_{t}^{h} = {s_{t} \oplus h}$, and a teacher distribution $\pi_{T}{( \cdot \mid s_{t}^{h})}$ is obtained by querying the same model under the hint-augmented prompt. The resulting signal is a full token-level distribution rather than a scalar, but it is also sparse: the directive signal fires only on the subset of turns where the PRM judges a meaningful correction to be present. For instance, a user's terse "thanks, looks good" or a passing test result carries strong evaluative content but no directive content; while an error trace pointing at a specific line yields a usable hint.

### Complementary analysis

The two signals are complementary along two axes. In *frequency*, the evaluative signal is available on every scored turn, while the directive signal is only available on the subset of turns where the next state carries an extractable correction. In *information density*, the evaluative signal compresses an entire turn into a single scalar, while the directive signal carries per-token guidance through the teacher distribution $\pi_{T}$. RLVR can only consume the former and pure on-policy distillation can only consume the latter; neither alone uses the full content of $s_{t + 1}$.

### Hybrid objective

We therefore combine both signals into a single per-token loss for token $i$

where $\mathcal{L}_{i}^{\text{GRPO}}$ is the standard PPO clipped surrogate driven by the scalar advantage $A_{i}^{\text{grpo}}$, and $\mathcal{L}_{i}^{\text{OPD}}$ is the distillation loss defined in equation 1. By default $w_{\text{RL}} = w_{\text{OPD}} = 1$. The two terms share the same trajectory and the same policy updates; the hybrid objective integrates their complementary strengths in frequency and information density (Table 2). In experiments, we will demonstrate that this hybrid objective improves optimization for both real-time personalization and agentic RL.

### Overlap-Guided Hint Selection

A central failure mode of on-policy distillation is teacher-student distribution mismatch: when the teacher distribution $\pi_{T}$ places mass on tokens the student has near-zero density , the off-policy importance ratio explodes and the gradient becomes unstable \[li2026rethinking\]. Because we obtain the teacher by conditioning the same model on a hint $h$, the choice of hint directly controls the magnitude of mismatch: a vague or off-target hint pulls the teacher far from the student, while a precise one keeps the two distributions close on the tokens that matter.

Figure 4: Overlap-guided hint selection method overview.

### Overlap as a selection signal

We exploit this observation by selecting hints based on the geometry of the induced teacher distribution rather than on hint length, teacher confidence, or other surface heuristics. Given $y$ the generated response by the student, let $S_{i}^{q} = {top}\text{-}k{\{\pi_{\text{old}}{( \cdot \mid s_{t},y_{< i})}\}}$ denote the student's top-$k$ vocabulary at response token position $i$, and $S_{i,h}^{p} = {top}\text{-}k{\{\pi_{T}{( \cdot \mid s_{t}^{h},y_{< i})}\}}$ the teacher's top-$k$ vocabulary at position $i$ under candidate hint $h$. We define the overlap signal

which counts how many of the student's high-probability tokens remain high-probability under the hint-conditioned teacher. Among $M$ candidate hints, we consider two selection schemes:

where the sequence-level mode picks one hint per trajectory and the token-level mode picks a different hint at each position. The token-level option is motivated by the fact that the empirical OPD loss is itself token-level rather than sequence-level (Appendix C). In our experiments, the two schemes achieve similar performance, with the sequence-level mode tending to be more stable in general agentic RL settings. Higher overlap means the teacher and the student already agree on what the response should look like at the level of vocabulary support, so distillation can move the student toward the teacher within its own high-density region rather than toward unfamiliar tokens.

### Top-$k$ OPD loss with log-probability-difference clip

Once $h^{\star}$ is chosen, we restrict the distillation loss to a vocabulary subset $S_{i}$, set to $S_{i}^{q}$ by default \[li2026rethinking, shenfeld2026self\]. For each $v \in S_{i}$, we form an importance-weighted advantage from the log-probability gap between teacher and student, $A_{v} = {\Delta_{v} \cdot w_{v}}$, where ${\ell_{\text{old}}{(v)}} = {{\log\pi_{\text{old}}}{({v \mid {s_{t},y_{< i}}})}}$, ${\ell_{T,h^{\star}}{(v)}} = {{\log\pi_{T}}{({v \mid {s_{t}^{h^{\star}},y_{< i}}})}}$,

The weight $w_{v}$ concentrates the advantage on tokens the student is actually likely to sample, while the clip on $\Delta_{v}$ bounds the per-token log-probability gap at $C$, capping the magnitude of any single distillation update even when the teacher is locally far from the student. With the per-vocab ratio $\rho_{v} = {\exp\left( {{\ell_{\text{cur}}{(v)}} - {\ell_{\text{old}}{(v)}}} \right)}$, where ${\ell_{\text{cur}}{(v)}} = {{\log\pi_{\text{cur}}}{({v \mid {s_{t},y_{< i}}})}}$, the distillation loss takes the clipped-surrogate form summed over the subset:

with $\varepsilon_{\text{lo}} = 0.2$ and $\varepsilon_{\text{hi}} = 0.28$ following standard PPO clipping \[schulman2017proximal, yu2025dapo\]. The overlap-guided choice of $k^{\star}$ keeps $\rho_{v}$ near unity on the supervised tokens, while the $\Delta$-clip caps advantage magnitudes; together they bound both factors of the surrogate and yield stable updates without discarding the directional information carried by the hint.

### Step-wise Reward for General Agentic RL

How to combine the outcome and process rewards in general agentic RL?

### Why Process Rewards Are Vital for Agentic Tasks

In long-horizon agentic tasks, outcome-only rewards provide gradient signal only at the terminal step, leaving the vast majority of turns unsupervised. A PRM assigns a reward to each turn based on the next-state signal, providing dense credit assignment throughout the trajectory. Recent work has provided strong empirical evidence for this. RLAnything \[wang2026rlanything\] demonstrates that integrating step-wise PRM signals with outcome rewards consistently outperforms outcome-only training across GUI agents, text-game agents, and coding tasks. We build directly on this insight in OpenClaw-RL: our PRM judges each turn using the live next-state signal as evidence, and we demonstrate empirically (§4.5) that this dense signal is helpful for long-horizon RL settings.

### Integrate Outcome and Process Rewards

Verifiable outcomes are standard supervision signals in RLVR settings. Following RLAnything \[wang2026rlanything\], we integrate outcome and process rewards by simply adding them together, using $o + {\sum_{i = 1}^{m}{r_{i}/m}}$ as the reward for step $t$, where the $r_{i}$ are independently assigned by PRM$(a_{t},s_{t + 1})$. Unlike GRPO, the presence of step-wise rewards makes it less straightforward to compute advantages. feng2025group group similar states and perform standardization within each group. However, in real-world settings such as terminal agents, states are not easily clustered. Therefore, we directly group actions with the same step index, which we find effective in our empirical studies.

## Experiments

### Personal Agent Setup

We use LLMs to simulate users from different professions interacting with OpenClaw on work tasks, and evaluate how efficiently the model learns to align with each user's preferences. Three settings are considered---student, TA, and teacher---described below. In every session, the simulated user delegates a single task to OpenClaw on their personal computer; tasks are drawn from GSM8K \[cobbe2021training\]. The user's first message in each session is hard-coded and does not disclose their preferences, allowing us to assess whether the model has internalized prior experience by examining its response to this opening message. We consider the optimization effect to have been achieved once the model's response to the first message satisfies the user's preferences in three consecutive sessions. The OpenClaw policy and reward model in this setting is Qwen3-4B-Thinking-2507 \[yang2025qwen3\]. We set the learning rate to $1 \times 10^{- 5}$ and the log-probability-difference clipping coefficient to $C = 1$, and trigger a training step after every 16 collected samples. Users are simulated with Qwen3-32B to ensure faithful role-following. See more details in Appendix A.1.

Student who uses OpenClaw to do homework. In this setting, a student uses OpenClaw on a personal computer to complete homework while trying to avoid the appearance of relying on AI. A response is identified as AI-like when it contains markers such as bold text, numbered lists, or over-formatting like boxed final answers. The student interacts with OpenClaw to complete the homework in a non-AI-like style and asks for revisions whenever the response is AI-like.

TA who uses OpenClaw to grade homework. Once the student finishes the homework, the TA uses OpenClaw to grade the assignments. The TA wants the grading to be specific and detailed, and considers a grading response insufficient when its length is below 100 tokens.

Teacher who uses OpenClaw to comment. After grading, the teacher uses OpenClaw to write comments for the student based on the TA's feedback. The teacher wants comments to be friendly and patient, identified by warm phrases such as "well done!" or "excellent!"

### General Agent Setup

### Models

We use Qwen3-8B \[qwen3\], Qwen3VL-8B-Thinking \[bai2025qwen3\], Qwen3-4B \[qwen3\], and Qwen3-4B-SFT in terminal, GUI, SWE, and tool-call settings, respectively. Qwen3-4B-SFT is the model from slime_github, fine-tuned on the dataset of feng2025retool. The PRMs for GUI and tool-call agents are Qwen3VL-8B-Thinking and Qwen3-4B, respectively.

### Datasets

We use SETA RL data \[seta\], OSWorld-Verified \[xie2024osworld\], SWE-Bench-Verified \[jimenez2023swe\], and DAPO RL data \[yu2025dapo\] to train the terminal, GUI, SWE, and tool-call agents, respectively. The GUI agent is evaluated on the training set (excluded chrome and multi-apps tasks). The tool-call agent is evaluated on AIME 2024 \[AIME2024\]. For the terminal and SWE agents, we report the average rollout-task accuracy over a window of RL steps.

### Hyperparameters

We set the learning rate to $10^{- 6}$, the KL coefficient to $0.01$, the lower and upper clip ratios to $0.2$ and $0.28$. We sample 8 tasks per step for the GUI and SWE, 16 for terminal, and 32 for the tool-call setting. For each task, we draw 8 samples. The maximum numbers of interaction steps for GUI, SWE, and terminal are 30, 20, and 10, respectively. See more details in Appendix A.2.

### Hybrid RL Extension Setup

We study our algorithm's extension to general RL settings, focusing on multi-turn tool-call \[feng2025retool\] and RLVR. For the tool-call setting, we use Retool-4B, which is supervised-fine-tuned on the Retool dataset \[feng2025retool\], with Qwen3-8B as the PRM. For the RLVR setting, we use DeepSeek-R1-Distill-Qwen-1.5B as the policy model and Qwen3-4B as the PRM, training on DAPO \[yu2025dapo\] and evaluating on AIME \[AIME2024\]. We set the learning rate to $10^{- 6}$, the KL coefficient to $0.01$, the log-probability-difference clipping coefficient to $C = 2$, and the lower and upper PPO clip ratios to $\varepsilon_{\text{lo}} = 0.2$ and $\varepsilon_{\text{hi}} = 0.28$. We sample 32 tasks per training step, with the policy drawing 8 independent rollouts per task. We provide more details in Appendix A.3.

Optimize all at the same time (joint)
Optimize for each individual (separate)

Table 3: Optimization efficiency of different methods across settings. Our hybrid RL attains the best overall performance. Notably, jointly optimizing for multiple users amplifies the gains from RL, whereas the efficiency of memory and skill-evolution is largely unaffected. The reported metric is the minimum number of sessions required to achieve the optimization effect, as defined in Section 4.1. We run 5 independent trials with Qwen3-4B-Thinking-2507 and report the mean.

Figure 5: We supports scalable RL for general agents across terminal, GUI, SWE, and tool-call settings.

### OpenClaw-RL Effectively Optimizes Personal Agents

We evaluate optimization efficiency by measuring how quickly the model learns to align with user preferences during OpenClaw usage. We consider three types of users, each with distinct jobs and preferences. In addition to optimizing the model for a single user, OpenClaw-RL supports multiple individuals sharing the same model, with the model jointly optimized across their interactions. As shown in Table 3, our algorithm achieves the desired optimization effect with only about 10 conversation sessions under joint optimization and 15 under separate optimization, demonstrating its efficiency and practicality for real-world applications. We also provide concrete before-and-after optimization examples across these three settings (Figure 2), showing that the model's output pattern shifts toward the user's preferences through simple conversational interaction.

### Unified RL Framework Across Terminal, GUI, SWE, and Tool-Call

We conduct experiments across widely used, real-world agent settings, including terminal, GUI, SWE, and tool-call scenarios (Figure 5). Our framework handles diverse model sizes and modalities, with large-scale environment parallelization to improve training scalability: we use 128 parallel environments for terminal agents, 64 for GUI and SWE agents, and 32 for tool-call agents. To evaluate the importance of process rewards in long-horizon tasks, we conduct RL training with integrated outcome and process rewards in the tool-call (250 steps) and GUI (120 steps) settings. Combining both reward types further improves performance: integrated rewards reach 0.25 and 0.33 in tool-call and GUI respectively, compared with 0.19 and 0.31 under outcome-only optimization. One trade-off is that hosting a PRM requires additional resources compared with outcome-only training.

Figure 6: Hybrid RL in multi-turn agentic RL and RLVR settings. Left: the ReTool multi-turn RL setting; right: RLVR. “PRM + Outcome” denotes the integrated approach introduced in Section 3.3, while “Outcome” refers to standard GRPO with verifiable outcome rewards.

Hybrid RL sequence optimal
Hybrid RL token optimal

Table 4: Ablation on model and method. Sequence-optimal and token-optimal hint selection achieve similar efficiency, both outperforming random hint selection. We use Qwen3-32B here and report the mean over 5 independent runs. The student, TA, and teacher settings are jointly optimized.

### Hybrid RL is More Efficient

We compare the optimization efficiency of hybrid RL against its simple ablations using $\mathcal{L}_{i}^{\text{GRPO}}$ (GRPO) and $\mathcal{L}_{i}^{\text{OPD}}$ (OPD), as well as memory and skill-evolution methods Mem0 \[chhikara2025mem0\] and Cognee \[markovic2025optimizinginterfaceknowledgegraphs\]. As shown in Table 3, hybrid RL is substantially more efficient than either GRPO or OPD alone, further validating our analysis of the complementary nature of these two objectives. Hybrid RL also reaches the target performance faster than the skill- and memory-evolving baselines. Notably, these baselines impose additional context overhead at inference time, whereas our RL approach only updates model weights, offering a more sustainable long-term solution. Under the joint optimization setting, the memory and skill-evolution methods perform comparably to their separate-optimization counterparts, while hybrid RL benefits significantly more from joint optimization. We hypothesize that this is because the three optimization objectives are inherently coupled for the policy model.

### Hybrid RL Generalizes to Agentic RL

We apply our hybrid RL framework to large-batch training settings, including multi-turn agentic RL and RLVR. For multi-turn RL, hint generation focuses on tool-call feedback at each turn, and only turns deemed worth annotating by the PRM are included in the OPD data. For RLVR, the PRM has access to the ground-truth answer when generating hints for incorrect solutions, but is prompted to avoid leaking any specifics of the solution itself. As shown by the training curves in Figure 6, hybrid RL generalizes well to both agentic RL and RLVR under these large-batch settings, outperforming both the outcome-only and integrated-reward baselines.

Figure 7: -. Comparison of hint selection methods in multi-turn RL and RLVR. Selecting hints via top-k overlap effectively improves both training stability and final performance. We find the sequence optimal method tends to be more stable than token optimal, particularly in the RLVR setting. Distribution of the log-probability difference between teacher and student. We observe that this difference can be highly extreme, motivating us to introduce a clipping mechanism.

Si = Siq (student top-k)
Si = Siq ∩ Si, h⋆p (top-k overlap)

Table 5: Ablation on k and the support set Si. We find that larger values of k tend to improve optimization, although the gain becomes very small when k ≥ 4. Using the top-k overlap as the support set leads to a minor decrease in performance. We choose the joint optimization setting here.

### Overlap-Guided Hint Selection Improves Efficiency and Stability

We compare different hint selection strategies in this section. As shown in the left panel of Figure 7, randomly selecting hints leads to training instability in the agentic RL setting. In the RLVR setting (Figure 7, right), both training efficiency and stability are adversely affected. Moreover, Table 4 shows that random selection yields substantially worse optimization efficiency than the sequence-optimal and token-optimal methods. Together, these results demonstrate the effectiveness of selecting hints via top-$k$ overlap. Comparing the two optimal-selection variants, we find that sequence-optimal selection tends to be more stable than token-optimal selection in large-batch training (Figure 7).

### Log-Probability Difference Is Vital for Stability

We analyze training stability through token-level log-probability shifts. After sampling responses from the base generator, we fix each response and rescore the same token sequence under the original prompt and a hint-augmented prompt. The per-token difference measures how much the hint changes the likelihood of already-generated tokens, thereby isolating conditioning effects from generation randomness. As shown in Figure 7, the difference can take highly extreme values, indicating sharp divergence between teacher and student distributions on the same response. Such unbounded log-probability differences can amplify noisy updates and destabilize optimization. This is also observed in the Retool setting: without sufficient outcome-supervision control, the average response length keeps increasing, leading to final truncation ratios of $0.2$ and $0.5$ for clipping and non-clipping methods, respectively. These results show that clipping improves stability by suppressing extreme log-probability shifts and preventing uncontrolled length growth (see details in Appendix B.2).

### Ablation on $k$ and Support Set $S_{i}$

We first study the influence of $k$ on the optimization effect. From Table 5, we observe that larger values of $k$ lead to stronger optimization effects only when $k \leq 4$, which aligns with the finding in \[li2026rethinking\]. In the degenerate case, namely token-level OPD, the performance drops very significantly. Therefore, in all our main experiments, we choose $k = 4$ to maintain efficiency while preserving the maximum effect. We also explore using top-$k$ overlap as the support set $S_{i}$, which offers an efficiency advantage, and find that the performance drops slightly.

### Explore Different Policy and Reward Models

We also evaluate OpenClaw-RL using Qwen3-32B as the policy in the joint optimization setting (Table 4), demonstrating the robustness of our method on a larger model. However, we find that a larger model does not guarantee a faster optimization than a smaller one. We further use Qwen3-8B as a PRM teacher to guide the training of Qwen3-4B-Thinking-2057 in OpenClaw (Table 7), where we find the performance is very similar to using Qwen3-4B-Thinking-2057 as the teacher itself.

## Related Work

### RL for LLMs

RLHF \[christiano2017deep, ziegler2019fine\] established the PPO-based alignment pipeline. DPO \[rafailov2023direct\] further bypasses explicit reward modeling via closed-form preference optimization; GRPO \[shao2024deepseekmath\] eliminates the critic network through group-relative advantage estimation, and was further scaled by DeepSeek-R1 \[guo2025deepseek\] and DAPO \[yu2025dapo\]. ReasonFlux \[yang2025reasonflux\] takes an orthogonal approach by applying hierarchical RL to optimize sequences of thought templates rather than raw token-level CoTs, achieving significant gains through structured reasoning. These systems operate in batch-offline mode, where data collection and training happen in separate phases with fixed datasets. OpenClaw-RL instead trains continuously from live interaction signals without any data pre-collection phase.

### Agentic RL and Tool-Use

Foundational agent paradigms such as ReAct \[yao2023react\], Toolformer \[schick2023toolformer\], and FireAct \[chen2023fireact\] enable multi-step interaction with external tools, but rely on demonstrations rather than online RL. Recent work applies RL to specific agent settings, SWE-agent \[yang2024sweagent\] and ReTool \[feng2025retool\] for code and tool-use, DigiRL \[bai2024digirl\] and WebRL \[qi2025webrl\] for GUI agents, ArCHer \[zhou2024archer\] and LOOP \[chen2025reinforcement\] for multi-turn credit assignment, but each targets a single environment with a dedicated training pipeline. DemyAgent \[yu2025demystifying\], RLAnything \[wang2026rlanything\], and CURE \[wang2025cure\] advance agentic RL further by investigating data quality and closed-loop reward model co-optimization.

### Process Reward Models

PRMs demonstrate that step-level supervision outperforms outcome-only supervision for math reasoning. Math-Shepherd \[wang2024math\] automates step-wise supervision via Monte Carlo estimation without human annotations; GenPRM \[zhao2025genprm\] scales PRM with generative chain-of-thought verification. ReasonFlux-PRM \[zou2025reasonfluxprm\] extends PRMs to trajectory-aware evaluation for long-CoT reasoning, providing both offline data selection and online dense process-level rewards. PRIME \[cui2025prime\] learns implicit process rewards from outcome labels. RLAnything \[wang2026rlanything\] provides the large-scale evidence that step-wise PRM signals are essential for long-horizon agentic tasks, with jointly optimized reward model signals surpassing human-labeled supervision. We extend PRM-style judging to the online setting, where process rewards are inferred from live next-state signals rather than pre-collected ground truth, across heterogeneous long-horizon agentic settings.

### On-Policy Distillation and Hindsight Methods

On-policy distillation \[agarwal2024policy, shenfeld2026self, hubotter2026reinforcement\] trains a student on token-level supervision from a teacher evaluated at the student's own rollouts, transferring fine-grained guidance that scalar-reward RLVR \[shao2024deepseekmath, guo2025deepseek, hu2025open, yu2025dapo\] cannot. Self-distillation conditions a strong teacher on a corrective hint: hindsight relabeling \[hubotter2026reinforcement, zhang2023wisdom, shi2026experiential\] formalizes this on fixed datasets rather than extracting hints automatically, while concurrent work by buening2026aligning prompts online with next-state information but leaves the hints implicit rather than as explicit training signals. A central challenge is teacher-student distribution mismatch, which causes instability \[li2026rethinking\] and worsens with low-quality hints. We propose an overlap-guided selection criterion that picks the hint whose teacher distribution most overlaps with the student's top-$k$ tokens; combined with a log-probability-difference clip, this improves efficiency and stability.

### RL Training Infrastructure

OpenRLHF \[hu2024openrlhf\], AReal \[fu2025areal\], veRL \[sheng2025hybridflow\], ROLL \[wang2025reinforcement\] and slime \[slime_github\] decouple rollout and training engines for scalable RL training. Built on slime, OpenClaw-RL enables four fully decoupled asynchronous loops, serving, rollout, PRM judging, and training, allowing continuous training from live multi-stream interactions with zero interruption to serving. This capability is absent from prior RL infrastructure, which assumes batch data collection rather than live deployment.

## Conclusion

Every agent interaction produces a next-state signal that encodes how the agent performed and, often, how it should have acted differently. OpenClaw-RL is built on a single insight: these signals are stream-agnostic, and one policy can learn from all of them simultaneously. Personal conversations, terminal executions, GUI interactions, SWE tasks, and tool-call traces all flow into the same training loop. OpenClaw-RL shows that deployed agent interactions can be converted into useful online supervision by combining frequent evaluative signals with sparser but richer directive signals, with stable learning ensured through overlap-guided hint selection and log-probability-difference clipping. Two important challenges remain for real-world deployment. First, negative or adversarial user feedback, such as misleading corrections or malicious instructions, may poison the model if used directly for online updates, necessitating stronger training-data filtering. Second, a model optimized for personal usage may encode user-specific preferences and private information, making it an attractive target for attacks; protecting privacy and improving the safety of personalized online learning remain important directions for future work.
