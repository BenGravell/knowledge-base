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

End-to-end (E2E) autonomous driving aims to map raw, multi-view camera streams together with ego state, history, and high-level navigation commands directly to future trajectories and low-level controls using a single policy[hu2023uniad,weng2024paradrive]. A growing trend is to instantiate this policy as a Vision-Language-Action (VLA) foundation model[kawaharazuka2025vlasurvey], pre-trained on large-scale vision-language data and fine-tuned on driving logs. Building on this trend, recent studies introduce inference-time reasoning by generating a text-based chain-of-thought (CoT) before committing to actions[tian2024tokenize, wang2024drivecot, hwang2024emma, zhou2025autovla,wang2025alpamayo]. While this is a natural choice following recent works on reasoning LLMs[wei2022chain], a textual CoT presents several limitations when applied to driving. First, natural language is ill-suited for representing spatiotemporal geometry and multi-agent interactions, which are central to driving decision-making.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second, autoregressively generating long chains of text introduces nontrivial latency, making real-time deployment challenging. Furthermore, the generated actions may significantly diverge from the preceding language rationales (e.g., the text states go left yet the action indicates a right turn) due to weak action-text alignment[wang2025alpamayo]. Accordingly, we argue that text is not the most suitable substrate in driving VLA models.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Latent Chain-of-Thought Reasoning. Compared to text-based CoT, our proposed Latent CoT provides more efficient and aligned reasoning traces for end-to-end driving VLA models.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose {\fontfamily{txtt}\selectfont {LCDrive}}\xspace, a Latent Chain-of-Thought framework for Driving VLA models. Instead of relying on textual CoT, {\fontfamily{txtt}\selectfont {LCDrive}}\xspaceperforms reasoning through vector-space supervised chain-of-thought tokens grounded in a learned latent world model (LWM), as shown infig:teaser. The latent reasoning process alternates between action-proposal tokens and latent world model prediction tokens, thereby simulating counterfactual futures directly in latent space and using those futures to inform the choice of the next action. This interleaved latent CoT forms a structured and compact reasoning trace grounded in the multi-agent interaction process, yielding both higher dynamical precision and lower inference latency. We train {\fontfamily{txtt}\selectfont {LCDrive}}\xspacethrough a three-stage pipeline (fig:pipeline).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Starting from a pretrained non-reasoning VLA, we first cold-start with latent CoT by teacher-forcing the model with ground-truth (GT) world model states and reasoning actions proposed by the model itself. During this process, we simultaneously train a small LWM prediction head to predict LWM embeddings from proposed actions during inference. We then apply reinforcement learning (RL) post-training to refine this initial latent reasoning scaffold and improve final action prediction using trajectory-level rewards.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

{\fontfamily{txtt}\selectfont {LCDrive}}\xspaceon the large-scale PhysicalAI-AV dataset[nvidia2025avdata], consisting of 1727 hours of driving data across challenging urban scenarios with dense multi-agent interactions. Intab:main, we show that {\fontfamily{txtt}\selectfont {LCDrive}}\xspaceimproves trajectory fidelity and driving success compared to the baseline text-CoT VLA models. Qualitative rollouts infig:quali show how coherent latent-CoT reasoning can improve driving performance over text-CoT reasoning. We further include results across different scenario categories as well as extensive ablation experiments to show the superior performance of {\fontfamily{txtt}\selectfont {LCDrive}}\xspace.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

- We rethink the representation of reasoning in VLA models for E2E driving with {\fontfamily{txtt}\selectfont {LCDrive}}\xspace, which conducts latent CoT with latent reasoning tokens strongly aligned with driving actions and a latent world model. - We introduce a training framework combining latent CoT cold start, world model training, and RL post-training, and show that this combination is especially effective for latent reasoning models. - We demonstrate consistent empirical gains on a large, diverse E2E driving benchmark: txttLCDrivelower inference latency, improved driving quality, and larger gains under RL post-training than non-reasoning and text-CoT baselines.

<!-- chunk {"id": "body-0012", "role": "body", "section": "{\\fontfamily{txtt}\\selectfont {LCDrive}}\\xspace: Driving with Latent CoT", "weight": 1.0} -->

Overview of our proposed latent reasoning framework.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Latent Chain-of-Thought Reasoning", "weight": 1.0} -->

We aim to design a compact, action-aligned reasoning process that performs latent counterfactual rollouts in the latent world model state, and keeps the CoT in the same vocabulary as the final trajectory output.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Latent Chain-of-Thought Reasoning", "weight": 1.0} -->

We represent each reasoning branch as an interleaved action and latent world model trace \(R^{(i)}\): A_0^{(i)}, \mathrm{LWM}_1^{(i)}, A_1^{(i)},\mathrm{LWM}_2^{(i)},\ldots,A_{K-1}^{(i)}, \mathrm{LWM}_K^{(i)}\big].$$ Here $A_t^{(i)}$ are action-proposal tokens drawn from the same action vocabulary as the final output, but grouped as a 1.0s block of 10 stepwise tokens: $$A_t^{(i)} \;:=\; \big(a_{10(t-1)+1},\ldots,a_{10t}\big),$$ which makes proposals easy to produce and interpret.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Latent Chain-of-Thought Reasoning", "weight": 1.0} -->

$\mathrm{LWM}^{(i)}_{t+1}$ is the ego-centric latent world state summarizing the same 1.0s window at 10Hz. Reasoning is seeded by the history anchor $\mathrm{LWM}_0$, after which we interleave $(A_t^{(i)},\mathrm{LWM}_{t+1}^{(i)})$ for $t=1\dots K$ to form $R^{(i)}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Latent Chain-of-Thought Reasoning", "weight": 1.0} -->

At step \(t\), the VLA proposes \(A\_t^{(i)}\) conditioned on sensor tokens, the current world state, and the prior reasoning token sequence: $$A_t^{(i)} \sim \pi_\theta\!\big(\cdot \,\big|\, o_{\text{image}},\,o_{\text{ego}},\,\mathrm{LWM}_0,\,R^{(i)}_{<t}\big).$$ Note that $A_t^{(i)}$ uses the same token vocabulary as the final trajectory prediction $\tau$. These proposals are only used as reasoning context and do notcommit to a specific final plan.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Latent Chain-of-Thought Reasoning", "weight": 1.0} -->

In practice, we compute it with $f_\phi(\mathbf{h}^{\mathrm{VLA}}_t)$, where \(\mathbf{h}^{\mathrm{VLA}}\_t\) is the VLA hidden state after taking \(A\_t^{(i)}\) as input, and \(f\_\phi\)is a lightweight MLP producing LWM tokens.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Latent Chain-of-Thought Reasoning", "weight": 1.0} -->

To allow the model to spend more reasoning tokens on diverse strategies and paths, we enable autoregressive generation of a fixed number of branches \(B\) (default \(B=2\)). All branches share the history anchor \(\mathrm{LWM}\_0\) and are generated sequentially: for \(i=1\ldots B\), we produce \(R^{(i)}\) while conditioning on previously formed traces \(R^{(<i)}\). This lets the model refer to prior latent reasoning when proposing the next branch, promoting diversity and yielding more plausible, complementary counterfactual futures under a bounded token budget. In this paper, we fix both \(K\) and \(B\)at training and evaluation for simplicity.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Latent Chain-of-Thought Reasoning", "weight": 1.0} -->

The complete reasoning context is $$\textsc{Reason} \;=\; \big[\, \mathrm{LWM}_0,\; R^{},\; \ldots,\; R^{(B)} \,\big].$$ Conditioned on the sensor input and \(\textsc{Reason}\) in eq:ar1-seq, the model predicts the 64 stepwise trajectory tokens \(a\_{1:64}\) and decodes the final trajectory \(\hat{\tau}\). The final actions attend to allproposals and their associated latent world model rollouts, forming rich counterfactual context that we will show yields higher-fidelity, safer, and more stable trajectories.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Latent Chain-of-Thought Reasoning", "weight": 1.0} -->

We first use a base non-reasoning VLA to create latent CoT data, and cold start {\fontfamily{txtt}\selectfont {LCDrive}}\xspaceby supervised learning. Then, we conduct reinforcement learning to activate useful reasoning capacity of {\fontfamily{txtt}\selectfont {LCDrive}}\xspace.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

We train {\fontfamily{txtt}\selectfont {LCDrive}}\xspacein three training stages (fig:pipeline).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Stage 0 - Non-reasoning Pretraining", "weight": 1.0} -->

We start from a non-reasoning VLA (Reason \(=\varnothing\)) trained via supervised fine-tuning to predict trajectory tokens from driving data. We keep two copies of this model: one serves as the initialization for {\fontfamily{txtt}\selectfont {LCDrive}}\xspacein the later fine-tuning stage; the other is frozenand used solely to generate action-proposal tokens for latent reasoning.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Stage 1 - CoT Cold Start", "weight": 1.0} -->

In this step, we aim to teach the VLA model the format and structure of latent CoT with teacher forcing. To this end, we construct supervision data for latent CoT Reasontokens through the following steps.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Stage 1 - CoT Cold Start", "weight": 1.0} -->

Action-conditioned LWM targets. For each block \(\tilde{A}^{(i)}\_{t}\), we integrate its ego-frame \(\Delta\)-poses to obtain the ego pose for that 1.0s window, re-center the GT future tracked agent bounding boxes into this ego frame, and encode them to produce a target latent world state: $\tilde{\mathrm{LWM}}^{(i)}_{t+1}$. This yields branch-specific world tokens \(\{\tilde{\mathrm{LWM}}^{(i)}\_{t+1}\}\) that reflect the consequencesof each proposal window.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Stage 1 - CoT Cold Start", "weight": 1.0} -->

Action proposals and targets are interleaved to form \(B\) reasoning traces \(R^{(i)}\) (eq:cot\_tokens). The full training sequence in eq:ar1-seq thus becomes $$\big[o_{\text{image}},\,o_{\text{ego}},\, \underbrace{\mathrm{LWM}_0,\; R^{},\ldots,R^{(B)}}_{\textsc{Reason}},\, We input this full sequence to {\fontfamily{txtt}\selectfont {LCDrive}}\xspaceduring training.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Stage 2 - Reinforcement Learning", "weight": 1.0} -->

The second stage post-trains {\fontfamily{txtt}\selectfont {LCDrive}}\xspaceto actively produce useful latent reasoning and output better actions. By directly optimizing the final action conditioned on the latent reasoning process, the model learns to produce useful reasoning tokens beyond merely imitating the frozen model from Stage 1.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Stage 2 - Reinforcement Learning", "weight": 1.0} -->

For each training input, we keep the fixed reasoning budget \((K,B)\) and generate a group of \(G\) stochastic completions: the policy autoregressively generates action-proposal blocks interleaved with latent world states to form branch traces \(R^{(i)}\), and concatenates them into \textsc{Reason}=\big[\mathrm{LWM}\_0,R^{},\ldots,R^{(B)}\big]. Conditioned on Reason and the sensor tokens, the policy then produces the 64 trajectory tokens \(a\_{1:64}\) and decodes \(\hat{\tau}\).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Stage 2 - Reinforcement Learning", "weight": 1.0} -->

We use a single trajectory-accuracy signal: Average Displacement Error (ADE) in meters between the predicted and expert trajectories over the 6.4s horizon: $$\mathrm{ADE}(\hat{\tau},\tau^\star) =\frac{1}{64}\sum_{i=1}^{64}\left\|\,\hat{\mathbf{p}}_i-\mathbf{p}^{\star}_i\right\|_2,$$ where $\mathbf{p}_i$ is the $i$-th 2D ego location along the trajectory. The reward for completion \(j\) is \(r^{(j)}=-\mathrm{ADE}(\hat{\tau}^{(j)},\tau^\star)\).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Stage 2 - Reinforcement Learning", "weight": 1.0} -->

Learning Algorithm. We use Group Relative Policy Optimization (GRPO) for RL training. For each training example, we sample a group of \(G\) completions \(\{\hat{\tau}^{(j)}\}\_{j=1}^{G}\), compute a trajectory-level reward \(r^{(j)}\), and construct centered advantages for each completion: We then maximize the advantage-weighted log-probability of the generated tokens, including both proposal and final action tokens: $$\mathcal{L}_{\text{GRPO}} \log \pi_\theta\!\big(x^{(j)}_t \mid \text{context}^{(j)}_t\big).$$ Empirically, we found that GRPO performs best without KL regularization, so we omit the KL term in the final objective. Note that Stage2 can also be applied to a non-reasoning baseline with \(\textsc{Reason}=\varnothing\).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Stage 2 - Reinforcement Learning", "weight": 1.0} -->

We will show in sec:expt\_main\_results that RL yields substantially larger gains for {\fontfamily{txtt}\selectfont {LCDrive}}\xspacethan the baseline.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Setup", "weight": 1.0} -->

We conduct our experiments on the recently released PhysicalAI-AV dataset[nvidia2025avdata]. It provides large-scale (1700+ hours) real-world multi-camera driving logs with precise ego trajectories and dense multi-agent annotations, enabling realistic end-to-end driving evaluation. In coordination with the dataset authors, we obtained a scenario-balanced subset that maintains consistency with the official public splits of the full dataset: 39,072 training clips (87 hours) and 23,758 validation clips (53 hours). For each clip, we consider 1.6s of history and 6.4s of future ego and surrounding-agent trajectories at 10Hz. tab:scenario, the subset is constructed to balance nominal and eventful scenes: 30% of clips are General Driving and the remaining 70% are evenly distributed across 14 specific scenarios (e.g., lane keeping, intersection navigation, merges, cut-ins), with 5% of the data per category.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Setup", "weight": 1.0} -->

In addition to its significantly larger scale compared to prior E2E driving validation benchmarks (e.g. nuScenes[caesar2020nuscenes] with only 150 validation clips, less than 1 hour), this split provides a near-uniform scenario distribution. It avoids dominance by easy cases (e.g., 73.9% straight driving in nuScenes[li2024egostatus]) and enables fair per-scenario evaluation.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Setup", "weight": 1.0} -->

Metrics.For each input clip, we randomly sample 6 trajectories from the evaluated model. Metrics are then computed for each sample, and the average over all samples is taken to be the overall score of the clip.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Setup", "weight": 1.0} -->

To measure the similarity of the model output with the expert driving behaviors, we report ADE (meters) as the mean $\ell_2$ error between the predicted ego positions and expert positions at 10Hz over the $T = 64$ steps. We also measure the safety of the model driving behavior: OffRoad$_{2.5}$ and OffRoad$_{5.0}$ (%) are the fraction of clips for which any point in the predicted ego footprint leaves the drivable area within the first $T\!\in\!\{2.5,5.0\}$ seconds. Coll@2.5 and Coll@5.0 (%) are the fraction of clips that experience any intersection between the ego polygon and any other agent polygon within the same $S\in\{2.5,5.0\}$s window. Corner Dist (m) measures the mean Euclidean distance between corresponding corners of the predicted and expert ego boxes (with fixed vehicle dimensions) over the 64 steps at 10Hz, capturing both translation and Additional analyses are provided in AppendixC.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Setup", "weight": 1.0} -->

| Reason | GT LWM | RL | $\mathrm{ADE}$ $\downarrow$ | OffRoad$_{2.5}$ $\downarrow$ | OffRoad$_{5.0}$ $\downarrow$ | Coll$_{2.5}$ $\downarrow$ | Coll$_{5.0}$ $\downarrow$ | Corner Dist. $\downarrow$ | Main evaluation results on the PhysicalAI-AV dataset. Lower is better for all metrics, bold is best.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Setup", "weight": 1.0} -->

| 2*Scenario Category | 6cADE @ 6.4 s (in meters, lower is better) | | | | | | ADE split by scenario. Columns are ordered with methods using GTLWM (marked with $^*$) shown first. Bold is best.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Setup", "weight": 1.0} -->

All variants share the same non-reasoning backbone, trajectory tokenizer, and decoder. Unless noted, training uses the PhysicalAI split mentioned above. All models receive identical inputs and differ only in the format of the Reason tokens. 1) No CoT (\(\varnothing\)): VLA without any reasoning tokens; 2) LWM\(\_0\)-only: the model conditions on the history latent world model state \(\mathrm{LWM}\_0\) but performs no interleaved rollout; 3) Latent CoT: our interleaved action-proposal and latent world-model tokens, initialized from \(\mathrm{LWM}\_0\); 4) Text CoT: a language-reasoning baseline that uses English text for reasoning. We mainly compare methods that predict all the LWM tokens needed in the reasoning stage. To show performance upper-bounds, we also compare with methods that take GT LWM tokens within the reasoning space, marked with $^*$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Setup", "weight": 1.0} -->

Our model, {\fontfamily{txtt}\selectfont {LCDrive}}\xspace, is Latent CoT with Predicted LWM; we also report performance with and without the RL training stage.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Setup", "weight": 1.0} -->

Qualitative Results. Qualitative comparison of textual and latent reasoning in driving VLA models. Latent CoT captures fine-grained spatial relationships and multi-agent interactions while using a smaller inference budget, leading to more stable and accurate trajectory predictions. In each case, we highlight the main misalignment of the Text CoT reasoning with the final trajectory.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Setup", "weight": 1.0} -->

Text CoT baseline. Since obtaining Text-CoT labels for the PhysicalAI-AV dataset[nvidia2025avdata] is non-trivial, we use model weights provided by the AR1 team[wang2025alpamayo]. The model shares the same AR1 architecture, and is pretrained on a large proprietary dataset of driving logs that is an over $100\times$ larger superset of our training set, followed by finetuning on a smaller set of Text-CoT-paired data (though still $\sim10\times$larger than our training set). Given its substantially larger training corpus and direct supervision on carefully-curated text CoT dataset, this baseline is expected to perform better than models trained only on PhysicalAI-AV.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Setup", "weight": 1.0} -->

We adopt a Qwen3-0.5B[qwen3] LLM as the language-action module and a DINOv2[oquab2023dinov2] ViT as the image encoder, following the AR1 architecture design[wang2025alpamayo]. Each input clip uses two front-view cameras (wide 120\({}^{\circ }\) and telephoto 30\({}^{\circ }\)) with 320$\times$512 resolution visual inputs. The encoded image tokens are concatenated with ego tokens and Reasontokens before being fed into the decoder.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Setup", "weight": 1.0} -->

Stage-0 non-reasoning pretrain: We initialize from the pre-trained AR1 checkpoint, then train a non-reasoning model for 100k steps on the PhysicalAI-AV training split using batch size 128, learning rate 4e-5, and cosine annealing. Stage-1 CoT cold start: We then enable latent reasoning and train for 10k steps with the same optimizer settings. Action proposals are generated from the frozen non-reasoning model using temperature 0.6 and top-p $= 0.98$. The loss in eqn:stage1\_loss is weighted by $\lambda= 0.1$. Stage-2 GRPO: We finally apply RL post-training with GRPO for 3k steps using group size 8, effective batch size 32 sampled completions per update, and a learning rate of 1e-6. We set $K=5$ and $B = 2$ based on the cost-performance saturation analysis in AppendixD, where this setting provides a strong trade-off between reasoning budget, branch diversity, and final trajectory accuracy.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Setup", "weight": 1.0} -->

For all approaches, we use temperature 0.6 and top-p $= 0.98$during sampling of the 6 trajectories per input.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Main Results", "weight": 1.0} -->

We show the main result in Table[tab:main]. We first compare the oracle models that use the LWM states (GT LWM). When provided with ground-truth LWM, Latent CoT$^{*}$ substantially outperforms simply conditioning on the history state (LWM$_0$-only$^{*}$): ADE improves from 1.393 to 1.268, and RL further reduces it to 1.197 while also improving safety (e.g., reducing Coll$_{5.0}$from 0.905 to 0.867). These results indicate that counterfactual reasoning with LWM tokens is an effective substrate for planning with an accurate world state.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Main Results", "weight": 1.0} -->

Note that RL is beneficial only when the model conducts reasoning. The first two rows show that adding RL to LWM$_0$-only$^{*}$ yields no gain in ADE and worsens OffRoad$_5$, whereas RL on Latent CoT$^{*}$ consistently improves both accuracy and safety. This suggests that RL helps the model better exploit latent CoT rollouts during post-training.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Main Results", "weight": 1.0} -->

In the practical (non-oracle) setting, our model {\fontfamily{txtt}\selectfont {LCDrive}}\xspaceremains strong. {\fontfamily{txtt}\selectfont {LCDrive}}\xspaceoutperforms the non-reasoning baseline by a clear margin (ADE 1.626 vs. 1.762; OffRoad$_{2.5}$ 1.219 vs. 1.753; Coll$_5$ 0.836 vs. 2.207), indicating that learned LWM tokens are highly informative at inference time. Relative to the GT-LWM oracle, the predicted-LWM setting preserves most of the gains over the non-reasoning policy, indicating that latent CoT remains robust to world-model prediction errors.Moreover, adding RL on top of predicted LWM further improves accuracy and safety, delivering a clear additional gain. This demonstrates that RL remains beneficial even when the world model is learned, and that it helps the policy exploit the latent CoT interface more effectively.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Main Results", "weight": 1.0} -->

Compared with the Text CoT baseline, {\fontfamily{txtt}\selectfont {LCDrive}}\xspaceis comparable without RL and clearly better with RL. Before RL, {\fontfamily{txtt}\selectfont {LCDrive}}\xspace(ADE 1.668) is on par with Text CoT (1.650). After RL, {\fontfamily{txtt}\selectfont {LCDrive}}\xspaceachieves 1.626 ADE and lower risk (OffRoad$_{2.5}$ 1.219 vs. 1.391; Coll$_5$ 0.836 vs. 0.905), despite Text CoT using a muchlarger CoT-annotated training set.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Main Results", "weight": 1.0} -->

Overall, we conclude that LWM tokens provide a more effective reasoning medium than text; RL is especially impactful when paired with latent CoT, reliably translating internal rollouts into better final actions, and latent CoT consistently improves driving quality over non-reasoning counterparts. txttLCDrivea $1.8\times$ reasoning speedup over Text CoT on an RTX A5000 under identical decoding settings. This gain comes from the reasoning stage, since input encoding and final action decoding are shared across methods while latent CoT uses a shorter, more structured token sequence. See AppendixB for wall-clock latency and training-compute details.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Main Results", "weight": 1.0} -->

We further evaluate {\fontfamily{txtt}\selectfont {LCDrive}}\xspaceacross diverse driving scenarios. As shown intab:scenario, {\fontfamily{txtt}\selectfont {LCDrive}}\xspaceachieves consistent improvements over both non-reasoning and text-CoT baselines in nearly all categories. Compared with the non-reasoning model, {\fontfamily{txtt}\selectfont {LCDrive}}\xspacereduces ADE by 715% on most complex maneuvers such as Intersection Navigation, Turning Maneuver, and Merging, which require anticipating multi-agent interactions. The largest relative gains appear in Traffic Control Compliance, Speed Control, and Nudge Static Obstacle Maneuver, demonstrating that LWM-based reasoning effectively anticipates other agents' future states.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Main Results", "weight": 1.0} -->

Compared with the Text CoT model, txttLCDrivea lower overall ADE (1.626 vs.1.650) despite Text CoT using a much larger CoT-annotated corpus. Per-scenario results are mixed: txttLCDriveby large margins on scenarios such as General Driving (1.166 vs.1.434), Speed Control (1.376 vs.2.037), and Nudge Static Obstacle (1.387 vs.1.855), while Text CoT is stronger on Cut-In (1.884 vs.2.385) and Lead Vehicle Following (1.455 vs.1.708). Overall, txttLCDrive's gains are concentrated in scenarios requiring proactive reasoning about future states, whereas Text CoT retains an edge in reactive settings.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Main Results", "weight": 1.0} -->

The oracle results (Latent CoT $^*$) further illustrate the potential of latent reasoning. When supplied with perfect LWM, latent CoT reduces the ADE by large margins across nearly all categories (e.g., 1.300 in Intersection Navigation and 0.542 in Stop for Vehicle). Adding RL on top of oracle LWM yields even stronger results in difficult scenarios such as Cut-In (1.220) and Lane Change(1.897), showing that latent reasoning becomes especially powerful given accurate multi-agent futures.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Main Results", "weight": 1.0} -->

Overall, latent CoT provides broad, uniform improvements across the full spectrum of driving tasks, with better anticipation, more stable long-horizon predictions, and improved performance on categories requiring interaction understanding and traffic rule compliance.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

fig:quali, we compare textual and latent reasoning traces. Text CoT provides high-level narratives that remain generic and miss fine-grained spatial relationships, while also containing many non-essential tokens that inflate latency. In contrast, {\fontfamily{txtt}\selectfont {LCDrive}}\xspaceproduces compact interleaved action-proposal and world-model tokens that encode scene dynamics, enabling multi-step reasoning with far fewer tokens while better matching ground truth.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

For each scene, we show the reasoning trace whose action tokens are most similar to the final trajectory. Since {\fontfamily{txtt}\selectfont {LCDrive}}\xspacedoes not require decoding LWM tokens into human-interpretable form, we use the GT-LWM Latent CoT* model from tab:mainfor visualization.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Conclusion", "weight": 1.5} -->

{\fontfamily{txtt}\selectfont {LCDrive}}\xspace: a model that replaces natural language CoT with compact, action-aligned latent reasoning for autonomous driving. By interleaving action-proposal and world-model tokens, our approach unifies inference-time reasoning and decision making within a single latent world modeling process, enabling the model to reason about candidate actions via their predicted future outcomes while avoiding the inefficiencies of text-based explanations. Experiments on large-scale real-world driving data show that latent CoT reduces inference latency, improves trajectory quality, and enables further gains from RL post-training over both non-reasoning and text-CoT baselines. These gains persist across scenarios and with predicted LWM.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conclusion", "weight": 1.5} -->

There are a few limitations: training latent CoT requires GT supervision (e.g., agent bounding boxes) to ground the representationthese auxiliary targets may still be hard to obtain at scale (though autolabeling efforts are closing this gap[sal2024eccv,ravi2024sam2,huang2025vipe,Lee\_OpenBox\_NeurIPS\_2025]); our model does not recover human-interpretable representations from latent CoT tokens; and it lacks adaptive reasoning lengths.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Latent World Model Encoder", "weight": 1.0} -->

Our latent world model (LWM) encodes the surrounding agents around the ego vehicle (excluding the ego vehicle) into a compact set of tokens for latent chain-of-thought reasoning. Concretely, each LWM state summarizes a fixed $1.0\,\mathrm{s}$ window at $10\,\mathrm{Hz}$in an ego-centric frame.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Latent World Model Encoder", "weight": 1.0} -->

Per-agent temporal encoder. For each clip, we select the $N$ nearest agents (based on distance in the current frame). The raw per-timestep state of each agent includes position, heading, dimensions, velocity, and other kinematic attributes. We stack these over a $1.0\,\mathrm{s}$ window (10 frames) to obtain $$\texttt{agent\_state} \in \mathbb{R}^{B \times N \times T \times F},$$ where $B$ is the batch size, $N$ the number of agents, $T{=}10$ the number of timesteps, and $F$ the number of input features. We first augment the state with $4$ oriented corner points of the 3D bounding box (projected to BEV), resulting in $8$ additional normalized features per timestep.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Latent World Model Encoder", "weight": 1.0} -->

A linear layer projects the concatenated features from dimension $(F{+}8)$ to a latent dimension $d_{\mathrm{lwm}}$, after which we apply: 1) a learned timestep embedding added along the temporal axis; 2) an agent-type embedding (shared over timesteps) added per agent; 3) a stack of MLP residual blocks along the feature dimension. This produces a sequence of per-agent, per-timestep features of shape $\mathbb{R}^{B \times N \times T \times d_{\mathrm{lwm}}}$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Latent World Model Encoder", "weight": 1.0} -->

Temporal pooling per agent. To summarize the $T{=}10$ timesteps into a single feature per agent, we use a learnable query vector and a cross-attention layer along the time axis. The query attends to the $T$ timestep features with an attention mask that ignores invalid timesteps, yielding one vector per agent: $$\texttt{LWM\_agent} \in \mathbb{R}^{B \times N \times d_{\mathrm{lwm}}}.$$ Two-token LWM summarization. The latent world model state $\mathrm{LWM}_t$ used in LCDrive is a compact summary of all agents in the $1.0\,\mathrm{s}$ window.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Latent World Model Encoder", "weight": 1.0} -->

We train an additional attention layer with $M << N$ learnable query tokens, each of dimension $d_{\mathrm{lwm}}$, to attend over the $N$ agent features: $$\mathrm{LWM}_t = \texttt{Attn}\bigl(Q_{M},\; \texttt{LWM\_agent}\bigr) \in \mathbb{R}^{B \times M \times d_{\mathrm{lwm}}}.$$ These $M$ tokens keep the LWM interface extremely compact for latent reasoning. In this paper, we use $N=64$ and $M=2$, maintaining a compact representation of LWM while capturing rich agent state information.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Stage 1: CoT Cold Start", "weight": 1.0} -->

1, we teach the model the structure of latent chain-of-thought (CoT) by teacher forcingboth the action-proposal tokens and the corresponding latent world model (LWM) tokens. Here we focus on how we construct the supervised reasoning sequence.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Stage 1: CoT Cold Start", "weight": 1.0} -->

Action proposals from a frozen GT-LWM model. We start from the LWM$_0$-only model with ground-truth LWM inputs (Row1 of Tab.1 in the main paper). This model is trained without latent reasoning and serves as a strong teacher that produces full 6.4s trajectories.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Stage 1: CoT Cold Start", "weight": 1.0} -->

Each sampled trajectory is then sliced into $K$ non-overlapping 1.0s action blocks of length 10: $${A}^{(i)}_t:= \bigl({a}^{(i)}_{10t+1}, \ldots, {a}^{(i)}_{10(t+1)}\bigr), These blocks define the targetaction-proposal tokens that our latent CoT policy imitates during cold start.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Stage 1: CoT Cold Start", "weight": 1.0} -->

Action-conditioned LWM supervision. For each branch $i$ and block index $t$, we construct an LWM supervision token ${\mathrm{LWM}}^{(i)}_{t+1}$ that encodes the future world state conditioned on the proposal ${A}^{(i)}_t$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Stage 1: CoT Cold Start", "weight": 1.0} -->

Starting from the ground-truth ego pose at the beginning of the window, we integrate the sequence of 10 motion-primitive codes in ${A}^{(i)}_t$ to obtain the ego pose trajectory over that 1.0s interval. 1) take the ground-truth bounding boxes of all tracked agents from the PhysicalAI-AV dataset; 2) transform these boxes into the ego-centric frame defined by the integrated ego pose (translation and rotation); 3) feed the resulting agent states into the LWM encoder described in the last subsection. The encoder yields a compact latent world-model summary for that 1.0s window, which we store as the target token $\mathrm{LWM}^{(i)}_{t+1}$. Repeating this for all blocks $t = 0,\ldots,K{-}1$ produces an interleaved supervision trace

<!-- chunk {"id": "body-0067", "role": "body", "section": "Stage 2: Reinforcement Learning", "weight": 1.0} -->

For the reinforcement learning stage of {\fontfamily{txtt}\selectfont {LCDrive}}\xspace, we adopt the cosmos-rl framework as our RL backbone. All RL experiments are conducted on a single 8-GPU node. We allocate 6 GPUs as rollout actors, each running an independent sampler replica of {\fontfamily{txtt}\selectfont {LCDrive}}\xspacein inference mode; 2 GPUs as learners, jointly performing GRPO optimization and broadcasting updated parameters to all actors. This partitioning enables high-throughput rollout while keeping optimization stable and fully GPU-resident.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Stage 2: Reinforcement Learning", "weight": 1.0} -->

The learning objective is the GRPO loss described in the main paper, but applied to all latent CoT tokens. This allows RL to restructure and refine the latent reasoning process itself, beyond imitation from Stage1. Empirically, we observe that latent reasoning benefits significantly more from RL than non-reasoning baselines, highlighting the importance of RL-based optimizationthrough the latent world-model interface.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Runtime and Compute Details", "weight": 1.0} -->

We report wall-clock inference latency and training compute to substantiate the efficiency claims in the main paper.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Runtime and Compute Details", "weight": 1.0} -->

We benchmark all methods on a single NVIDIA RTX A5000 (24GB) with identical decoding settings (temperature 0.6, top-p 0.98) and batch size 1. tab:supp\_runtime breaks the total latency into three phases: input encoding, reasoning, and action decoding. Because the backbone, input pipeline, and action decoder are shared across all methods, the latency difference comes entirely from the reasoning phase. txttLCDrive42 latent reasoning tokens in 1,388ms compared to 72 text tokens in 2,447ms for Text CoT, yielding a $1.8\times$ reasoning speedup with the same peak VRAM. A lighter configuration (LCDrive-Light, 24 tokens) further reduces reasoning time to 755ms ($3.2\times$). Note that AR1 achieves 99ms on-vehicle latency via distillation, TensorRT export, and optimized hardware; as txttLCDrivethe same backbone, these optimizations are directly applicable. tab:supp\_compute summarizes the LCDrive-specific training cost.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Runtime and Compute Details", "weight": 1.0} -->

All runs use a single node with $8\times$NVIDIA A100 (80GB) GPUs. Stage0 initializes from the pre-trained AR1 checkpoint (No-CoT). Stage1 (Latent CoT cold start) takes 34 wall-clock hours (272 GPU-hours) with batch size 128. Stage2 (RL via GRPO) takes 46 wall-clock hours (369 GPU-hours) with policy optimization batch size 96. The total LCDrive-specific training cost is 641 GPU-hours beyond the AR1 checkpoint.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Runtime and Compute Details", "weight": 1.0} -->

| Method | Input (ms) | Reason (ms) | Action (ms) | Total (ms) | Tokens | Reason tok/s | VRAM (MB) | Detailed wall-clock inference benchmark on an RTX A5000 (24 GB) with identical decoding settings and batch size 1. The backbone, input pipeline, and final action decoder are shared; the speedup comes from the shorter reasoning phase.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Runtime and Compute Details", "weight": 1.0} -->

| Stage | Hardware | Wall-clock | GPU-hours | LCDrive-specific training compute. The total excludes the pre-trained AR1 checkpoint used for initialization.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Reasoning Action Analysis", "weight": 1.0} -->

To better understand the behavior of latent chain-of-thought reasoning before/after reinforcement learning, we analyze the relationship between the proposal actions generated during the reasoning stage and the final action output by the policy. For each validation clip, {\fontfamily{txtt}\selectfont {LCDrive}}\xspacegenerates $B{=}2$ reasoning branches, each producing a 50-step rollout trajectory, decoded from the action proposal tokens $A_t^{(i)}$. The final decoded trajectory has 64 steps; we truncate it to the first 50 steps for consistent comparison.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Reasoning Action Analysis", "weight": 1.0} -->

Reasoning action analysis of {\fontfamily{txtt}\selectfont {LCDrive}}\xspacewith/without RL training, using GT LWM. All values are ADE (m). $\hat{\tau}_0$ and $\hat{\tau}_1$ denote the two proposal rollouts, $\hat{\tau}_{\mathrm{final}}$ the final action trajectory (trimmed to 50 steps), and $\tau^\star$the ground-truth future trajectory. We define four metrics as below. All metrics are reported as Average Displacement Error (ADE) in meters.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Reasoning Action Analysis", "weight": 1.0} -->

$$\text{Diversity} = \mathrm{ADE}\bigl(\hat{\tau}_0,\, \hat{\tau}_1\bigr),$$ - measures how different the two proposal branches are. $$\text{Alignment} = \min_{k\in\{0,1\}} \mathrm{ADE}\bigl(\hat{\tau}_{\mathrm{final}},\, \hat{\tau}_k\bigr),$$ - measures how closely the final action aligns with at least one proposal. $$\text{Quality} = \frac{1}{2} \sum_{k\in\{0,1\}} \mathrm{ADE}\bigl(\hat{\tau}_k,\, \tau^\star\bigr),$$ - measures how good the proposals are with respect to the ground-truth trajectory.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Reasoning Action Analysis", "weight": 1.0} -->

$$\text{Final-Action} = \mathrm{ADE}\bigl(\hat{\tau}_{\mathrm{final}},\, \tau^\star\bigr),$$ - the standard ADE of the final action relative to ground truth.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Reasoning Action Analysis", "weight": 1.0} -->

We evaluate {\fontfamily{txtt}\selectfont {LCDrive}}\xspaceusing GT LWM and compare the result with and without RL, and show the result in tab:reasoning\_action\_analysis. We summarize two key aspects of the reasoning behavior: (i) how latent reasoning behaves in general, and (ii) how reinforcement learning further improves it. Together, these results reveal the functional role of latent chain-of-thought reasoning in {\fontfamily{txtt}\selectfont {LCDrive}}\xspace. We have the following observations: 1) Final actions improve upon the reasoning proposals. In both settings, we observe that Final-Action Quality $<$ Reasoning Quality. This means that even though the reasoning branches provide two candidate future plans, the decoder does not simply copy a branch. Instead, it selects the more promising proposal and further refinesit to produce a more accurate final trajectory. This refinement effect becomes even stronger after RL. 2) Strong alignment between reasoning proposals and the final action.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Reasoning Action Analysis", "weight": 1.0} -->

Across both models, the ReasoningAction Alignment score remains small, indicating that the final trajectory lies close to at least one of the proposal branches. This shows that the proposal actions are actively used. After RL, the alignment improves (0.614 $\rightarrow$ 0.581), indicating that RL strengthens the integration between proposals and the final action. Note that the Reasoning-Action Alignment score is consistently lower than the Reasoning Quality score. This means that the final action lies closer to one of the reasoning proposals than either proposal lies to the ground truth. Thus, the final plan is strongly aligned with the latent reasoning process, showing that {\fontfamily{txtt}\selectfont {LCDrive}}\xspacerelies on and refines the reasoning rollouts when producing its final trajectory. 3) Reasoning branches maintain meaningful diversity. The Diversity score for both models indicates the two branches represent distinct motion hypotheses. This is essential in multi-agent driving scenarios with inherent uncertainty. RL slightly reduces diversity (0.412 $\rightarrow$ 0.353), but the branches remain significantly different.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Reasoning Action Analysis", "weight": 1.0} -->

In other words, RL makes exploration more targeted towards better proposal quality (0.976 $\rightarrow$0.961).

<!-- chunk {"id": "body-0081", "role": "body", "section": "Reasoning Action Analysis", "weight": 1.0} -->

Overall, we find that the final action trajectory is tightly aligned with the latent reasoning proposals, yet still achieves clearly lower ADE to the ground truth than the proposals themselves, showing that the model both uses and refines the proposed futures. Compared to the latent CoT model without RL, RL post-trainingfurther reduces both proposal and final-action errors and strengthens the alignment between proposals and the final decision.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Ablation Study on Reasoning Depth", "weight": 1.0} -->

We train different variants of {\fontfamily{txtt}\selectfont {LCDrive}}\xspacewith different reasoning depth $K$ and branch factor $B$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Ablation Study on Reasoning Depth", "weight": 1.0} -->

In this section, we study the trade-off between the reasoning token budget and trajectory accuracy by varying the $K$ and branch factor $B$ of {\fontfamily{txtt}\selectfont {LCDrive}}\xspace(GT LWM, Non-RL). For each variant, we construct the CoT supervision target in Stage 1 CoT Cold start stage with different settings of $K$ and $B$. Then, we train the model with teacher forcing with different reasoning depths and branch factors, keeping all other components and hyperparameters fixed across runs. Importantly, we do not apply RL fine-tuning and we do notuse predicted LWM tokens in this study, since our goal here is to quantify the tradeoff of reasoning cost and final action performance of latent CoT.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Ablation Study on Reasoning Depth", "weight": 1.0} -->

We then evaluate each model on the validation dataset and compare the performance in fig:efficiency\_curve. We also compare them with the non-reasoning baseline (LWM$_0$-only with GT LWM). The horizontal axis plots the number of reasoning tokens generated per input clip, and the vertical axis shows the resulting ADE We have the following observations: 1) Latent CoT provides consistent improvements over the baseline The leftmost point corresponds to the non-reasoning model. Introducing even a minimal amount of latent reasoning (e.g., $K{=}1$, $B{=}2$with 24 tokens) produces a clear reduction in ADE. This demonstrates that a small number of interleaved action-proposal and latent world-model tokens already provides useful counterfactual context for the final trajectory prediction. 2) Increasing reasoning budget yields meaningful gains As we increase $(K,B)$, performance improves smoothly, indicating that deeper latent reasoning enables the model to explore more steps into the future and produce better action plans based on that.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Ablation Study on Reasoning Depth", "weight": 1.0} -->

The largest gains are obtained when moving from shallow reasoning (e.g., $K{=}1,2$) to larger reasoning depth ($K{=}3$$5$). Beyond this range, improvements are smaller but still positive, showing that {\fontfamily{txtt}\selectfont {LCDrive}}\xspaceremains effective with different levels of token budgets. 3) Branching ($B$) leads to complementary improvements to depth ($K$) Branches encourage diverse counterfactual futures. Models with multiple branches (e.g., $K{=}5,B{=}2$) outperform the one with the same depth but fewer branches This aligns with our diversity analysis: exploring alternative counterfactual futures provides richer reasoning signals for the final policy.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Ablation Study on Reasoning Depth", "weight": 1.0} -->

Overall, this curve indicate that latent reasoning offers a highly effective cost-performance tradeoff: a modest reasoning budget (120 tokens) achieves strong trajectory accuracy while remaining relatively cheap. These results demonstrate that {\fontfamily{txtt}\selectfont {LCDrive}}\xspacecan flexibly trade inference cost for planning quality. Even lightweight latent CoT substantially enhances the end-to-end driving performance.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Inference Cost Analysis", "weight": 1.0} -->

We next compare the inference cost of latent chain-of-thought (Latent CoT) reasoning in {\fontfamily{txtt}\selectfont {LCDrive}}\xspacewith a text-based CoT baseline.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Inference Cost Analysis", "weight": 1.0} -->

Latent CoT inference cost. In {\fontfamily{txtt}\selectfont {LCDrive}}\xspace, each reasoning step $k \in \{1,\dots,K\}$ simulates a $1.0\,\mathrm{s}$ future window and produces: (i) $10$ discrete action tokens (representing the ego trajectory at 10Hz), and (ii) $2$ latent world model (LWM) tokens. For a model with reasoning depth $K$ and branch factor $B$, the total number of latent reasoning tokens is therefore $$N_{\text{latent}} \approx (10 + 2) \times K \times B,$$ plus a small constant overhead for the special tokens. At inference time, the inference cost of latent reasoning scales linearly with Text CoT baseline cost. For comparison, we tokenize the text CoT reasoning produced by the text-CoT baseline and compute the statistics over the validation dataset.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Inference Cost Analysis", "weight": 1.0} -->

Over this dataset we obtain an average length of $71.8$ tokens, and a long tail up to $252$ tokens per clip. Thus, a typical text-CoT explanation requires on the order of $70$$80$additional tokens at inference time.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Inference Cost Analysis", "weight": 1.0} -->

From the cost performance curve in Fig.[fig:efficiency\_curve], we find that {\fontfamily{txtt}\selectfont {LCDrive}}\xspacealready achieves significant improvements over the non-reasoning baseline using only a small, fixed latent budget of roughly $20$$60$ tokens (e.g., shallow configurations such as $(K,B)=$, $$, or $$). These settings use comparable or fewer tokens than typical text CoT, showing that compact latent reasoning is very cost-effective. As we increase the latent reasoning depth and branch factor, the model consistently achieves better trajectory accuracy, and remains superiorto the text-CoT baseline (as shown in Table 1 of our paper) when using similar total tokens. This suggests that latent world-model rollouts provide more actionable planning signal per token than free-form natural language reasoning.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Inference Cost Analysis", "weight": 1.0} -->

Potential for further latent reasoning. Our current action tokenizer produces $10$ tokens per second of motion. A promising next step is to design a more aggressive motion tokenizer (e.g., fewer tokens per second or multi-step primitives), which would linearly reduce the latent reasoning token count Because these tokens are structured and low-entropy compared to text, they are much easier to compress than natural-language CoT, indicating significant room for future latency and cost reductions while preserving the benefits of latent reasoning.
