<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Latent Chain-of-Thought World Modeling for End-to-End Driving

Topics include Autonomous driving, Vision-language-action models, Latent reasoning, World models, Chain-of-thought, Planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces LCDrive, which moves chain-of-thought-style driving reasoning into a latent world-model representation rather than natural language. The paper is relevant to VLA driving systems because it treats reasoning and action selection as a shared latent planning process over possible outcomes.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recent Vision-Language-Action (VLA) models for autonomous driving explore inference-time reasoning as a way to improve driving performance and safety in challenging scenarios. Most prior work uses natural language to express chain-of-thought (CoT) reasoning before producing driving actions. However, text may not be the most efficient representation for reasoning. In this work, we present Latent-CoT-Drive (LCDrive): a model that expresses CoT in a latent language that captures possible outcomes of the driving actions being considered. Our approach unifies CoT reasoning and decision making by representing both in an action-aligned latent space. Instead of natural language, the model reasons by interleaving action-proposal tokens, which use the same vocabulary as the model's output actions; and world model tokens, which are grounded in a learned latent world model and express future outcomes of these actions. We cold start latent CoT by supervising the model's action proposals and world model tokens based on ground-truth future rollouts of the scene. We then post-train with closed-loop reinforcement learning to strengthen reasoning capabilities.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

On a large-scale end-to-end driving benchmark, LCDrive achieves faster inference, better trajectory quality, and larger improvements from interactive reinforcement learning compared to both non-reasoning and text-reasoning baselines.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

End-to-end (E2E) autonomous driving aims to map raw, multi-view camera streams together with ego state, history, and high-level navigation commands directly to future trajectories and low-level controls using a single policy. A growing trend is to instantiate this policy as a Vision-Language-Action (VLA) foundation model, pre-trained on large-scale vision-language data and fine-tuned on driving logs. Building on this trend, recent studies introduce inference-time reasoning by generating a text-based chain-of-thought (CoT) before committing to actions. While this is a natural choice following recent works on reasoning LLMs, a textual CoT presents several limitations when applied to driving. First, natural language is ill-suited for representing spatiotemporal geometry and multi-agent interactions, which are central to driving decision-making. Second, autoregressively generating long chains of text introduces nontrivial latency, making real-time deployment challenging. Furthermore, the generated actions may significantly diverge from the preceding language rationales (e.g., the text states "go left" yet the action indicates a right turn) due to weak action-text alignment.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Accordingly, we argue that text is not the most suitable substrate in driving VLA models.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose LCDrive, a Latent Chain-of-Thought framework for Driving VLA models. Instead of relying on textual CoT, LCDrive performs reasoning through vector-space supervised chain-of-thought tokens grounded in a learned latent world model (LWM), as shown in Fig.˜1. The latent reasoning process alternates between action-proposal tokens and latent world model prediction tokens, thereby simulating counterfactual futures directly in latent space and using those futures to inform the choice of the next action. This interleaved latent CoT forms a structured and compact reasoning trace grounded in the multi-agent interaction process, yielding both higher dynamical precision and lower inference latency. We train LCDrive through a three-stage pipeline (Fig.˜3). Starting from a pretrained non-reasoning VLA, we first cold-start with latent CoT by teacher-forcing the model with ground-truth (GT) world model states and reasoning actions proposed by the model itself. During this process, we simultaneously train a small LWM prediction head to predict LWM embeddings from proposed actions during inference.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We then apply reinforcement learning (RL) post-training to refine this initial latent reasoning scaffold and improve final action prediction using trajectory-level rewards.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate LCDrive on the large-scale PhysicalAI-AV dataset, consisting of 1727 hours of driving data across challenging urban scenarios with dense multi-agent interactions. In Tab.˜1, we show that LCDrive improves trajectory fidelity and driving success compared to the baseline text-CoT VLA models. Qualitative rollouts in Fig.˜4 show how coherent latent-CoT reasoning can improve driving performance over text-CoT reasoning. We further include results across different scenario categories as well as extensive ablation experiments to show the superior performance of LCDrive.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions. The main contributions of our work are: We rethink the representation of reasoning in VLA models for E2E driving with LCDrive, which conducts latent CoT with latent reasoning tokens strongly aligned with driving actions and a latent world model.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce a training framework combining latent CoT cold start, world model training, and RL post-training, and show that this combination is especially effective for latent reasoning models.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate consistent empirical gains on a large, diverse E2E driving benchmark: LCDrive delivers lower inference latency, improved driving quality, and larger gains under RL post-training than non-reasoning and text-CoT baselines.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Driving VLA Models", "weight": 1.0} -->

E2E driving systems learn a direct mapping from raw sensor inputs to trajectories or controls, aiming to reduce handcrafted components and human bias in the traditional perception-prediction-planning pipeline. Although this has shown effectiveness in common scenarios, classical E2E models struggle in long-tail driving scenarios due to limited world knowledge and weak reasoning structure. With the rise of foundation models, recent work has explored using pre-trained LLMs and multimodal LLMs as core building blocks for end-to-end driving policies. Early approaches incorporate these models primarily as backbones while still directly predicting actions from multimodal inputs. More recent methods introduce textual chain-of-thought before action prediction, leveraging the common-sense reasoning capabilities of LLM backbones to improve motion planning, particularly in rare or complex scenarios. Different from previous works, our work departs from text-based CoT in driving VLAs and instead performs reasoning directly in a latent representation space.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Latent World Models", "weight": 1.0} -->

An alternative to model-free driving policy learning is to leverage latent world models (LWMs). LWMs learn a generalized latent dynamics function that predicts the action-conditioned future evolution of the environment given current observations and planned actions. In autonomous driving, LWMs have recently emerged as flexible dynamic models that complement end-to-end policies. Some works jointly learn latent dynamics and the driving policy from expert demonstrations, enabling the agent to model multi-agent interactions and future outcomes directly in latent space. Other efforts leverage trained latent world models to generate additional demonstrations for data augmentation or to serve as neural simulators for reinforcement learning-based policy training \[14, 21")\]. These approaches highlight the promise of latent dynamics as a way to introduce structure and interaction-awareness into the learning process.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Language-Free Paradigms for Reasoning", "weight": 1.0} -->

While textual CoT has become a popular strategy for eliciting reasoning in multimodal models, it is not always an ideal medium for tasks that require geometry understanding and dynamics modeling. In addition, textual CoT often contains many non-essential tokens that do not contribute to the underlying reasoning process, inflating token usage and slowing inference without proportional improvements in decision quality. Recently, a line of work has begun to explore latent reasoning in LLMs, where intermediate computations are performed directly in latent space rather than in natural language. This paradigm enables more compact and informed reasoning, often with a more cost-effective inference budget. Building on these ideas, subsequent works extend latent reasoning to vision-language models, achieving latent spatial reasoning. In driving, EMMA is closed-source, while OmniDrive and visual CoT methods mainly target VQA, retrieval, or spatial reasoning rather than direct action generation, making AR1 the closest open-source text-CoT baseline available for comparison. In this work, we adopt this emerging paradigm within driving foundation models and perform reasoning entirely in latent space, showing that latent reasoning is both more effective and more efficient than textual reasoning for driving.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Task", "weight": 1.0} -->

We aim to design a policy that maps sensor streams and ego state inputs to future trajectories. Following previous works on reasoning VLA for driving, we regard E2E driving as modeling an autoregressive distribution over a token sequence that concatenates input information, (optional) reasoning trace, and the future trajectory of the ego vehicle $\tau$: where each component conditions on all previous ones. Throughout the paper, "E2E" refers to this inference-time mapping from sensor inputs to trajectory tokens. The inputs of the model include $o_{\text{image}}$, $M$ front-view (or multi-camera) frames over the last $L$ steps; and $o_{\text{ego}}$, egomotion history. Given these inputs, the model produces (optional) Reason tokens followed by the future trajectory of the ego vehicle $\tau$. We parameterize $\tau$ as the full 6.4

<!-- chunk {"id": "body-0017", "role": "body", "section": "Input Tokenizers", "weight": 1.0} -->

Image tokenizer: Following standard VLM practice, each frame in $o_{\text{image}}$ is tokenized independently using a ViT-based encoder (e.g., ), producing a sequence of visual tokens $\;o_{\mathrm{img}}=\mathrm{Tok}_{\mathrm{img}}\!\big(V_{t-L:t}^{1:M}\big)$. Tokens from different camera views and timestamps are concatenated to form the full visual token sequence. Egomotion tokenizer: The ego vehicle's historical kinematics (speed, yaw rate, past $k$ control actions) are embedded into a compact set of tokens $\;o_{\mathrm{ego}}=\mathrm{Tok}_{\mathrm{ego}}(e_{t})$ with learned positional encoding.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Trajectory Tokenizer", "weight": 1.0} -->

The $6.4$ s future trajectory at $10$ Hz is represented using 64 discrete trajectory tokens $\tau=a_{1:64}$, one token per time step. Each $a_{i}$ indexes a motion-primitive bin corresponding to the ego-frame $\Delta$-pose $(\Delta x,\Delta y,\Delta\psi)$. We build a 1024-code vocabulary via $k$-means on training $\Delta$-poses. We encode continuous trajectories by quantifying them to indices $a_{1:64}$ with nearest-code assignment. We decode discrete indices back to $\Delta$-poses via codebook lookup and integrate them over time to recover continuous trajectories $\hat{\tau}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Latent World Model (LWM)", "weight": 1.0} -->

We introduce an ego-centric latent world model state $\mathrm{LWM}_{t}$ that captures vectorized agent boxes and poses from online perception. Each $\mathrm{LWM}_{t}$ summarizes a fixed 1.0 s window at 10 Hz (10 frames) as a fixed-size set of vectorized representations (ego + $K_{\text{agents}}$ nearest agents). $\mathrm{LWM}_{0}$ encodes the most recent history window up to the current time, which *starts* the reasoning process. It can be *given* from online perception (detection, tracking) or *predicted* by the VLA model itself. $\mathrm{LWM}_{1},\mathrm{LWM}_{2},\ldots$ represent future $1.0$ s windows produced during latent reasoning, conditioned on proposal actions.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Latent World Model (LWM)", "weight": 1.0} -->

We encode each $\mathrm{LWM}$ into a small set of latent worldmodel tokens $\mathrm{LWM}_{0}$ via a light Transformer module.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Reasoning Tokens", "weight": 1.0} -->

The presence of Reason is optional and used differently across different models. For the *non-reasoning* baseline model, we set $\textsc{Reason}=\varnothing$. For a fair comparison, the baseline may *optionally* condition on *only* $\textsc{Reason}=\big[\mathrm{LWM}_{0}\big]$ as context. For *text-based CoT* models (e.g., AR1 ), Reason consists of a sequence of natural-language tokens that verbally describe intermediate reasoning before action prediction. In this paper, we propose *latent CoT*, where Reason is instantiated as a short interleaved sequence of latent tokens composed of *action-proposal* tokens and counterfactual latent world-model tokens, initialized from the latent state $\mathrm{LWM}_{0}$. By default, $\mathrm{LWM}_{0}$ is predicted by the VLA model itself given the sensor inputs as context. We detail the construction of latent Reason tokens in the following section.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Latent Chain-of-Thought Reasoning", "weight": 1.0} -->

We aim to design a compact, action-aligned reasoning process that performs latent counterfactual rollouts in the latent world model state, and keeps the CoT in the same vocabulary as the final trajectory output.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Token Scheme", "weight": 1.0} -->

We represent each reasoning branch as an interleaved action and latent world model trace $R^{(i)}$: Here $A_{t}^{(i)}$ are *action-proposal* tokens drawn from the same action vocabulary as the final output, but grouped as a 1.0s block of 10 stepwise tokens: which makes proposals easy to produce and interpret. $\mathrm{LWM}^{(i)}_{t+1}$ is the ego-centric latent world state summarizing the *same* 1.0 s window at 10 Hz. Reasoning is seeded by the history anchor $\mathrm{LWM}_{0}$, after which we interleave $(A_{t}^{(i)},\mathrm{LWM}_{t+1}^{(i)})$ for $t=1\dots K$ to form $R^{(i)}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Action Proposal", "weight": 1.0} -->

At step $t$, the VLA proposes $A_{t}^{(i)}$ conditioned on sensor tokens, the current world state, and the prior reasoning token sequence: Note that $A_{t}^{(i)}$ uses the same token vocabulary as the final trajectory prediction $\tau$. These proposals are only used as reasoning context and do *not* commit to a specific final plan.

<!-- chunk {"id": "body-0025", "role": "body", "section": "LWM Prediction", "weight": 1.0} -->

Given the proposal as context, we predict the next latent world state: Here, $\pi_{\theta}$ denotes the action policy and $q_{\phi}$ the LWM transition model. In practice, we compute it with $f_{\phi}(\mathbf{h}^{\mathrm{VLA}}_{t})$, where $\mathbf{h}^{\mathrm{VLA}}_{t}$ is the VLA hidden state after taking $A_{t}^{(i)}$ as input, and $f_{\phi}$ is a lightweight MLP producing LWM tokens.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Multi-Branch Reasoning", "weight": 1.0} -->

To allow the model to spend more reasoning tokens on diverse strategies and paths, we enable autoregressive generation of a fixed number of branches $B$ (default $B=2$). All branches share the history anchor $\mathrm{LWM}_{0}$ and are generated sequentially: for $i=1\ldots B$, we produce $R^{(i)}$ while conditioning on previously formed traces $R^{(<i)}$. This lets the model refer to prior latent reasoning when proposing the next branch, promoting diversity and yielding more plausible, complementary counterfactual futures under a bounded token budget. In this paper, we fix both $K$ and $B$ at training and evaluation for simplicity.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Action Prediction", "weight": 1.0} -->

The complete reasoning context is Conditioned on the sensor input and Reason in Eq.˜1, the model predicts the 64 stepwise trajectory tokens $a_{1:64}$ and decodes the final trajectory $\hat{\tau}$. The final actions attend to *all* proposals and their associated latent world model rollouts, forming rich counterfactual context that we will show yields higher-fidelity, safer, and more stable trajectories.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

We train LCDrive in three training stages (Fig.˜3).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Stage 0 - Non-reasoning Pretraining", "weight": 1.0} -->

We start from a *non-reasoning* VLA (Reason $=\varnothing$) trained via supervised fine-tuning to predict trajectory tokens from driving data. We keep two copies of this model: one serves as the initialization for LCDrive in the later fine-tuning stage; the other is frozen and used solely to generate action-proposal tokens for latent reasoning.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Stage 1 - CoT Cold Start", "weight": 1.0} -->

In this step, we aim to teach the VLA model the format and structure of latent CoT with teacher forcing. To this end, we construct supervision data for latent CoT Reason tokens through the following steps.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Action-conditioned LWM targets", "weight": 1.0} -->

For each block $\tilde{A}^{(i)}_{t}$, we integrate its ego-frame $\Delta$-poses to obtain the ego pose for that 1.0 s window, re-center the GT future tracked agent bounding boxes into this ego frame, and encode them to produce a target latent world state: $\tilde{\mathrm{LWM}}^{(i)}_{t+1}$. This yields branch-specific world tokens $\{\tilde{\mathrm{LWM}}^{(i)}_{t+1}\}$ that reflect the *consequences* of each proposal window.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Supervision sequence", "weight": 1.0} -->

Action proposals and targets are interleaved to form $B$ reasoning traces $R^{(i)}$ (Eq.˜3). The full training sequence in Eq.˜1 thus becomes We input this full sequence to LCDrive during training.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Stage 2 - Reinforcement Learning", "weight": 1.0} -->

The second stage post-trains LCDrive to actively produce useful latent reasoning and output better actions. By directly optimizing the final action conditioned on the latent reasoning process, the model learns to produce useful reasoning tokens beyond merely imitating the frozen model from Stage 1.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Rollout", "weight": 1.0} -->

For each training input, we keep the fixed reasoning budget $(K,B)$ and generate a group of $G$ stochastic completions: the policy autoregressively generates *action-proposal* blocks interleaved with latent world states to form branch traces $R^{(i)}$, and concatenates them into $\textsc{Reason}=\big[\mathrm{LWM}_{0},R^{},\ldots,R^{(B)}\big].$ Conditioned on Reason and the sensor tokens, the policy then produces the 64 trajectory tokens $a_{1:64}$ and decodes $\hat{\tau}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Reward", "weight": 1.0} -->

We use a single trajectory-accuracy signal: *Average Displacement Error (ADE)* in meters between the predicted and expert trajectories over the 6.4 s horizon: where $\mathbf{p}_{i}$ is the $i$-th 2D ego location along the trajectory. The reward for completion $j$ is $r^{(j)}=-\mathrm{ADE}(\hat{\tau}^{(j)},\tau^{\star})$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Learning Algorithm", "weight": 1.0} -->

We use Group Relative Policy Optimization (GRPO) for RL training. For each training example, we sample a group of $G$ completions $\{\hat{\tau}^{(j)}\}_{j=1}^{G}$, compute a trajectory-level reward $r^{(j)}$, and construct centered advantages for each completion: $A^{(j)}=r^{(j)}-\frac{1}{G}\sum_{k}r^{(k)}$. We then maximize the advantage-weighted log-probability of the *generated* tokens, including both proposal and final action tokens: Empirically, we found that GRPO performs best without KL regularization, so we omit the KL term in the final objective. Note that Stage 2 can also be applied to a non-reasoning baseline with $\textsc{Reason}=\varnothing$. We will show in Sec.˜4.2 that RL yields substantially larger gains for LCDrive than the baseline.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Dataset", "weight": 1.0} -->

We conduct our experiments on the recently released PhysicalAI-AV dataset. It provides large-scale (1700+ hours) real-world multi-camera driving logs with precise ego trajectories and dense multi-agent annotations, enabling realistic end-to-end driving evaluation. In coordination with the dataset authors, we obtained a *scenario-balanced* subset that maintains consistency with the official public splits of the full dataset: 39,072 training clips (87 hours) and 23,758 validation clips (53 hours). For each clip, we consider 1.6 s of history and 6.4 s of future ego and surrounding-agent trajectories at 10 Hz.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Dataset", "weight": 1.0} -->

As summarized in Tab.˜2, the subset is constructed to balance nominal and eventful scenes: 30% of clips are *General Driving* and the remaining 70% are evenly distributed across 14 specific scenarios (e.g., lane keeping, intersection navigation, merges, cut-ins), with 5% of the data per category. In addition to its significantly larger scale compared to prior E2E driving validation benchmarks (e.g. nuScenes with only 150 validation clips, less than 1 hour), this split provides a near-uniform scenario distribution. It avoids dominance by easy cases (e.g., 73.9% straight driving in nuScenes ) and enables fair per-scenario evaluation.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Metrics", "weight": 1.0} -->

For each input clip, we randomly sample 6 trajectories from the evaluated model. Metrics are then computed for each sample, and the average over all samples is taken to be the overall score of the clip.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Metrics", "weight": 1.0} -->

To measure the similarity of the model output with the expert driving behaviors, we report ADE (meters) as the mean $\ell_{2}$ error between the predicted ego positions and expert positions at 10 Hz over the $T=64$ steps. We also measure the safety of the model driving behavior: OffRoad~2.5~ and OffRoad~5.0~ (%) are the fraction of clips for which *any* point in the predicted ego footprint leaves the drivable area within the first $T\!\in\!\{2.5,5.0\}$ seconds. Coll@2.5 and Coll@5.0 (%) are the fraction of clips that experience *any* intersection between the ego polygon and any other agent polygon within the same $S\in\{2.5,5.0\}$ s window. Corner Dist (m) measures the mean Euclidean distance between corresponding corners of the predicted and expert ego boxes (with fixed vehicle dimensions) over the 64 steps at 10 Hz, capturing both translation and heading errors. Additional analyses are provided in Appendix C.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Metrics", "weight": 1.0} -->

Latent CoT (LCDrive) Table 1: Main evaluation results on the PhysicalAI-AV dataset. Lower is better for all metrics, bold is best.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Metrics", "weight": 1.0} -->

ADE @ 6.4 s (in meters, lower is better) Stop for Vehicle Nudge Static Obstacle Maneuver Traffic Control Compliance Vulnerable Road Users (VRU) Lead Vehicle Following Lane Keeping Curve Table 2: ADE split by scenario. Columns are ordered with methods using GT LWM (marked with ∗) shown first. Bold is best.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Baselines", "weight": 1.0} -->

All variants share the same non-reasoning backbone, trajectory tokenizer, and decoder. Unless noted, training uses the PhysicalAI split mentioned above. All models receive identical inputs and differ only in the format of the Reason tokens. We compare 1) No CoT ($\varnothing$): VLA without any reasoning tokens; 2) LWM~0~-only: the model conditions on the history latent world model state $\mathrm{LWM}_{0}$ but performs no interleaved rollout; 3) Latent CoT: our interleaved action-proposal and latent world-model tokens, initialized from $\mathrm{LWM}_{0}$; 4) Text CoT: a language-reasoning baseline that uses English text for reasoning. We mainly compare methods that *predict* all the LWM tokens needed in the reasoning stage. To show performance upper-bounds, we also compare with methods that take *GT* LWM tokens within the reasoning space, marked with ^∗^.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Baselines", "weight": 1.0} -->

Our model, LCDrive, is Latent CoT with *Predicted LWM*; we also report performance with and without the RL training stage.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Text CoT baseline", "weight": 1.0} -->

Since obtaining Text-CoT labels for the PhysicalAI-AV dataset is non-trivial, we use model weights provided by the AR1 team. The model shares the same AR1 architecture, and is pretrained on a large proprietary dataset of driving logs that is an over $100\times$ larger superset of our training set, followed by finetuning on a smaller set of Text-CoT-paired data (though still $\sim 10\times$ larger than our training set). Given its substantially larger training corpus and direct supervision on carefully-curated text CoT dataset, this baseline is expected to perform better than models trained only on PhysicalAI-AV.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Implementation", "weight": 1.0} -->

We adopt a Qwen3-0.5B LLM as the language-action module and a DINOv2 ViT as the image encoder, following the AR1 architecture design. Each input clip uses two front-view cameras (wide 120^∘^ and telephoto 30^∘^) with 320$\times$`<!-- -->`{=html}512 resolution visual inputs. The encoded image tokens are concatenated with ego tokens and Reason tokens before being fed into the decoder.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Implementation", "weight": 1.0} -->

Stage-0 non-reasoning pretrain: We initialize from the pre-trained AR1 checkpoint, then train a non-reasoning model for 100k steps on the PhysicalAI-AV training split using batch size 128, learning rate 4e-5, and cosine annealing. Stage-1 CoT cold start: We then enable latent reasoning and train for 10k steps with the same optimizer settings. Action proposals are generated from the frozen non-reasoning model using temperature 0.6 and top-p $=0.98$. The loss in Eq.˜4 is weighted by $\lambda=0.1$. Stage-2 GRPO: We finally apply RL post-training with GRPO for 3k steps using group size 8, effective batch size 32 sampled completions per update, and a learning rate of 1e-6. We set $K=5$ and $B=2$ based on the cost-performance saturation analysis in Appendix D, where this setting provides a strong trade-off between reasoning budget, branch diversity, and final trajectory accuracy.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Implementation", "weight": 1.0} -->

For all approaches, we use temperature 0.6 and top-p $=0.98$ during sampling of the 6 trajectories per input.

<!-- chunk {"id": "body-0049", "role": "body", "section": "PhysicalAI-AV evaluation", "weight": 1.0} -->

We show the main result in Table 1. We first compare the oracle models that use the LWM states (GT LWM). When provided with ground-truth LWM, Latent CoT^∗^ substantially outperforms simply conditioning on the history state (LWM~0~-only^∗^): ADE improves from 1.393 to 1.268, and RL further reduces it to 1.197 while also improving safety (e.g., reducing Coll~5.0~ from 0.905 to 0.867). These results indicate that counterfactual reasoning with LWM tokens is an effective substrate for planning with an accurate world state.

<!-- chunk {"id": "body-0050", "role": "body", "section": "PhysicalAI-AV evaluation", "weight": 1.0} -->

Note that RL is beneficial only when the model conducts reasoning. The first two rows show that adding RL to LWM~0~-only^∗^ yields no gain in ADE and worsens OffRoad~5~, whereas RL on Latent CoT^∗^ consistently improves both accuracy and safety. This suggests that RL helps the model better exploit latent CoT rollouts during post-training.

<!-- chunk {"id": "body-0051", "role": "body", "section": "PhysicalAI-AV evaluation", "weight": 1.0} -->

In the practical (non-oracle) setting, our model LCDrive remains strong. LCDrive outperforms the non-reasoning baseline by a clear margin (ADE 1.626 vs. 1.762; OffRoad~2.5~ 1.219 vs. 1.753; Coll~5~ 0.836 vs. 2.207), indicating that learned LWM tokens are highly informative at inference time. Relative to the GT-LWM oracle, the predicted-LWM setting preserves most of the gains over the non-reasoning policy, indicating that latent CoT remains robust to world-model prediction errors. Moreover, adding RL on top of predicted LWM further improves accuracy and safety, delivering a clear additional gain. This demonstrates that RL remains beneficial even when the world model is learned, and that it helps the policy exploit the latent CoT interface more effectively.

<!-- chunk {"id": "body-0052", "role": "body", "section": "PhysicalAI-AV evaluation", "weight": 1.0} -->

Compared with the Text CoT baseline, LCDrive is comparable without RL and clearly better with RL. Before RL, LCDrive (ADE 1.668) is on par with Text CoT (1.650). After RL, LCDrive achieves 1.626 ADE and lower risk (OffRoad~2.5~ 1.219 vs. 1.391; Coll~5~ 0.836 vs. 0.905), despite Text CoT using a much larger CoT-annotated training set.

<!-- chunk {"id": "body-0053", "role": "body", "section": "PhysicalAI-AV evaluation", "weight": 1.0} -->

Overall, we conclude that LWM tokens provide a more effective reasoning medium than text; RL is especially impactful when paired with latent CoT, reliably translating internal rollouts into better final actions, and latent CoT consistently improves driving quality over non-reasoning counterparts.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Inference-time efficiency", "weight": 1.0} -->

LCDrive achieves a $1.8\times$ reasoning speedup over Text CoT on an RTX A5000 under identical decoding settings. This gain comes from the reasoning stage, since input encoding and final action decoding are shared across methods while latent CoT uses a shorter, more structured token sequence. See Appendix B for wall-clock latency and training-compute details.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Scenario breakdown", "weight": 1.0} -->

We further evaluate LCDrive across diverse driving scenarios. As shown in Tab.˜2, LCDrive achieves consistent improvements over both non-reasoning and text-CoT baselines in nearly all categories. Compared with the non-reasoning model, LCDrive reduces ADE by 7--15% on most complex maneuvers such as Intersection Navigation, Turning Maneuver, and Merging, which require anticipating multi-agent interactions. The largest relative gains appear in Traffic Control Compliance, Speed Control, and Nudge Static Obstacle Maneuver, demonstrating that LWM-based reasoning effectively anticipates other agents' future states.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Scenario breakdown", "weight": 1.0} -->

Compared with the Text CoT model, LCDrive achieves a lower overall ADE (1.626 vs. 1.650) despite Text CoT using a much larger CoT-annotated corpus. Per-scenario results are mixed: LCDrive wins by large margins on scenarios such as General Driving (1.166 vs. 1.434), Speed Control (1.376 vs. 2.037), and Nudge Static Obstacle (1.387 vs. 1.855), while Text CoT is stronger on Cut-In (1.884 vs. 2.385) and Lead Vehicle Following (1.455 vs. 1.708). Overall, LCDrive's gains are concentrated in scenarios requiring proactive reasoning about future states, whereas Text CoT retains an edge in reactive settings.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Scenario breakdown", "weight": 1.0} -->

The oracle results (Latent CoT^∗^) further illustrate the potential of latent reasoning. When supplied with perfect LWM, latent CoT reduces the ADE by large margins across nearly all categories (e.g., 1.300 in Intersection Navigation and 0.542 in Stop for Vehicle). Adding RL on top of oracle LWM yields even stronger results in difficult scenarios such as Cut-In (1.220) and Lane Change (1.897), showing that latent reasoning becomes especially powerful given accurate multi-agent futures.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Scenario breakdown", "weight": 1.0} -->

Overall, latent CoT provides broad, uniform improvements across the full spectrum of driving tasks, with better anticipation, more stable long-horizon predictions, and improved performance on categories requiring interaction understanding and traffic rule compliance.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

In Fig.˜4, we compare textual and latent reasoning traces. Text CoT provides high-level narratives that remain generic and miss fine-grained spatial relationships, while also containing many non-essential tokens that inflate latency. In contrast, LCDrive produces compact interleaved action-proposal and world-model tokens that encode scene dynamics, enabling multi-step reasoning with far fewer tokens while better matching ground truth.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

For each scene, we show the reasoning trace whose action tokens are most similar to the final trajectory. Since LCDrive does not require decoding LWM tokens into human-interpretable form, we use the GT-LWM Latent CoT\* model from Tab.˜1 for visualization.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We present LCDrive: a model that replaces natural language CoT with compact, action-aligned latent reasoning for autonomous driving. By interleaving action-proposal and world-model tokens, our approach unifies inference-time reasoning and decision making within a single latent world modeling process, enabling the model to reason about candidate actions via their predicted future outcomes while avoiding the inefficiencies of text-based explanations. Experiments on large-scale real-world driving data show that latent CoT reduces inference latency, improves trajectory quality, and enables further gains from RL post-training over both non-reasoning and text-CoT baselines. These gains persist across scenarios and with predicted LWM.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusion", "weight": 1.5} -->

There are a few limitations: training latent CoT requires GT supervision (e.g., agent bounding boxes) to ground the representation---these auxiliary targets may still be hard to obtain at scale (though autolabeling efforts are closing this gap ); our model does not recover human-interpretable representations from latent CoT tokens; and it lacks adaptive reasoning lengths.
