<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

HEPA: A Self-Supervised Horizon-Conditioned Event Predictive Architecture for Time Series

Topics include Time series, Self-supervised learning, Event prediction, Joint embedding predictive architectures, Survival analysis, Causal transformers, Rare events, Representation learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces HEPA, a time-series architecture that pretrains a causal Transformer encoder with a horizon-conditioned JEPA objective and then fine-tunes a predictor into a monotonic survival CDF over future event horizons. The method targets rare-event prediction with little labeled data and reports strong cross-domain results with a small number of tuned parameters.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Critical events in multivariate time series, from turbine failures to cardiac arrhythmias, demand accurate prediction, yet labeled data is scarce because such events are rare and costly to annotate. We introduce HEPA (Horizon-conditioned Event Predictive Architecture), built on two key principles. First, a causal Transformer encoder is pretrained via a Joint-Embedding Predictive Architecture (JEPA): a horizon-conditioned predictor learns to forecast future representations rather than future values, forcing the encoder to capture predictable temporal dynamics from unlabeled data alone. Second, we freeze the encoder and finetune only the predictor toward the target event, producing a monotonic survival cumulative distribution function (CDF) over horizons.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

With fixed architecture and optimiser hyperparameters across all benchmarks, HEPA handles water contamination, cyberattack detection, volatility regimes, and eight further event types across 11 domains, exceeding leading time-series architectures including PatchTST, iTransformer, MAE, and Chronos-2 on at least 10 of 14 benchmarks, with an order of magnitude fewer tuned parameters and, on lifecycle datasets, an order of magnitude less labeled data.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A turbine blade cracks after 12,000 flight hours. A bearing degrades over weeks of vibration data. A satellite sensor drifts silently for 48 hours before triggering a cascade. These events are rare in operational data, yet they follow partially predictable precursor dynamics: temperatures rise gradually before overheating, vibration amplitudes grow before mechanical failure, and sensor readings deviate systematically before spacecraft faults. A range of machine-learning methods attempt to predict such events from multivariate sensor streams. Remaining-useful-life (RUL) models estimate how long until a machine fails; anomaly detectors flag when sensor readings look abnormal. Although general-purpose architectures exist for both, the two communities develop separate benchmarks, metrics, and evaluation protocols: RUL models never see anomaly benchmarks; anomaly detectors never forecast time-to-failure. Yet all these tasks share the same structure: given observations up to time $t$, estimate the probability $P(\text{event within }\Delta t)$ for each prediction horizon $\Delta t$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This structural uniformity suggests a separation of concerns. The *encoder* learns temporal dynamics from unlabeled data without knowing which event matters downstream. The *predictor*, finetuned with a small number of event labels, specialises the learned dynamics to whichever event is relevant. The key design choice is what the encoder should forecast during pretraining. Value-forecasting approaches, whether supervised or pretrained on large corpora, shape representations around all variation in the signal, including noise irrelevant to the downstream event. The Joint-Embedding Predictive Architecture (JEPA) offers an alternative: by forecasting future *representations* rather than future values, the encoder learns a latent space that retains what is predictable about the future and discards what is not.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We apply this principle to time series as HEPA (Horizon-conditioned Event Predictive Architecture). A causal Transformer encodes observations up to time $t$; a horizon-conditioned predictor maps the encoding and a horizon $\Delta t$ to a predicted future representation, forcing the encoder to internalise dynamics at multiple timescales (fig.˜1). After self-supervised pretraining, the standard JEPA recipe discards the predictor and trains a linear probe on the frozen encoder. We instead retain the predictor: freeze the encoder but finetune the predictor alongside a lightweight event head that outputs a discrete-time survival CDF, ensuring that the predicted event probability never decreases as the horizon grows. This "predictor finetuning" recipe tunes only 198K parameters, roughly $11{\times}$ fewer than end-to-end training, yet is more expressive than a linear probe because the predictor reshapes its horizon-conditioned outputs to align with the downstream event.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our contributions are: One architecture, any event, any domain. A single 2.16 M-parameter architecture with fixed hyperparameters, evaluated on 14 benchmarks across 11 domains via a unified probability surface $p(t,\Delta t)$. HEPA wins on 10 out of 14 benchmarks while tuning $11{\times}$ fewer parameters than PatchTST.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Predictor finetuning as the downstream recipe. Freezing the encoder and finetuning only the predictor and event head tunes $11{\times}$ fewer parameters than end-to-end training. On the C-MAPSS benchmark, where degradation unfolds over hundreds of cycles, HEPA retains 92% of full-label h-AUROC at just 2% of labels. An information-theoretic bound (proposition˜1. ‣ 3.3 Theoretical Analysis ‣ 3 Method ‣ HEPA: A Self-Supervised Horizon-Conditioned Event Predictive Architecture for Time Series")) formalises when and why this works, and the bound's key prediction, that lower pretraining loss implies stronger downstream performance, is consistent with the empirical trend across 14 datasets (fig.˜3).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Self-supervised learning for time series", "weight": 1.0} -->

Self-supervised learning (SSL) for time-series representation learning falls into three families. Contrastive methods, including TS2Vec, TNC, TimesURL, CPC, and CoST, learn representations by contrasting positive and negative pairs. Masked reconstruction approaches such as PatchTST, SimMTM, and TimesNet recover masked patches in input space. JEPA takes a different path: predicting future *representations* rather than reconstructing inputs, avoiding tying the latent space to value-level fidelity. For time series, TS-JEPA applies temporal masking for classification, and MTS-JEPA adds codebook regularisation for anomaly detection. All these methods discard their pretraining head at inference and probe only the encoder. HEPA instead retains the predictor and finetunes it toward the downstream event, treating the predictor as a learnable bridge between frozen representations and event probabilities. The collapse-prevention mechanism follows the LeJEPA / SIGReg line rather than the EMA schedule of I-JEPA.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Foundation models for time series", "weight": 1.0} -->

Chronos-2, TFM-2.5, MOMENT, Moirai, and UniTS pretrain on large-scale corpora for generic value forecasting. Generative pretraining and LLM repurposing offer alternative transfer strategies. These approaches target future channel values; HEPA targets event probabilities. See also concurrent work on industrial pretraining corpora. The encoder is mid-scale and pretrained per-dataset; what transfers across domains is the *recipe* (architecture + predictor finetuning), not the weights. We benchmark HEPA against four of these foundation models, using identical downstream heads to isolate encoder quality (sections˜5, G and G).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Prognostics, anomaly prediction, and survival modelling", "weight": 1.0} -->

C-MAPSS is the standard remaining-useful-life (RUL) benchmark, where the supervised state of the art is STAR (root mean square error, RMSE, 10.61). Self-supervised approaches to RUL prediction remain limited. Anomaly detection methods such as Anomaly Transformer, DCdetector, and TranAD report point-adjusted F1, a metric shown to inflate scores dramatically by crediting entire segments from a single detection. These domain-specific metrics are incomparable across tasks. HEPA's downstream parameterisation builds on discrete-time survival models, which decompose event probability into per-interval hazards composed into a survival CDF; we adapt this to a multi-horizon event prediction setting. We unify evaluation through h-AUROC, the mean of per-horizon AUROC values computed over the probability surface, which is threshold-free and robust to class imbalance (section˜4). Domain-specific metrics are reported as lossy projections of the same surface for comparability with published baselines.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Architecture and Pretraining", "weight": 1.0} -->

HEPA consists of three components that interact across two phases (fig.˜2). The context encoder $f_{\theta}$ is a causal Transformer ($d{=}256$, 2 layers, 4 heads) that maps observations $\mathbf{x}_{\leq t}$, tokenised into non-overlapping patches of size $P{=}16$ (following PatchTST) with per-context instance normalisation and sinusoidal positional encodings, to a summary embedding $\mathbf{h}_{t}=f_{\theta}(\mathbf{x}_{\leq t})\in\mathbb{R}^{d}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Architecture and Pretraining", "weight": 1.0} -->

The predictor $g_{\phi}$ is a 2-layer multilayer perceptron (MLP) that takes the encoder output $\mathbf{h}_{t}$ together with a prediction horizon $\Delta t$ and produces a predicted embedding of the future interval: During pretraining, $\Delta t$ is sampled from a log-uniform distribution over $[1,\Delta t_{\text{max}}]$, forcing the encoder to internalise dynamics at multiple timescales. The same encoder $f_{\theta}$, applied bidirectionally to $\mathbf{x}_{(t,t+\Delta t]}$ with attention pooling, produces the target representation $\mathbf{h}^{*}_{(t,t+\Delta t]}\in\mathbb{R}^{d}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Architecture and Pretraining", "weight": 1.0} -->

Both encoders are trained jointly via the optimizer; a SIGReg (Sketched Isotropic Gaussian Regularisation) term $\mathcal{L}_{\mathrm{SIG}}$ on the predictor output prevents representation collapse, replacing the exponential moving average (EMA) momentum schedule used in standard JEPA (section˜I.3). SIGReg constrains the predicted representations toward an isotropic Gaussian, which Balestriero and LeCun prove is the optimal embedding distribution for minimising downstream prediction risk in joint-embedding architectures; this eliminates collapse without ad-hoc heuristics. A single mixing weight $\alpha{=}0.1$ controls its contribution to the total loss (section˜I.3).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Relation to canonical JEPA", "weight": 1.0} -->

HEPA differs from BYOL/I-JEPA/V-JEPA-style joint-embedding predictive architectures in two ways: (a) the target encoder is a weight-shared copy of $f_{\theta}$ rather than an EMA copy or a stop-gradient branch, and (b) collapse is prevented by SIGReg (isotropic Gaussian constraint on the predictor output) rather than by the online/target asymmetry. Trivial collapse $\hat{H}=H^{*}=$const is prevented jointly by SIGReg *and* by the asymmetric inputs ($\mathbf{x}_{\leq t}$ for the online branch vs. $\mathbf{x}_{(t,t+\Delta t]}$ for the target branch): the predictor never sees the future window directly. This puts HEPA closer to LeJEPA / SIGReg variants than to the original I-JEPA recipe.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Relation to canonical JEPA", "weight": 1.0} -->

The pretraining loss combines an L1 prediction objective (chosen over L2 because L1 distributes gradient magnitude equally across samples, avoiding domination by outlier predictions) with the SIGReg regulariser: where $\alpha$ balances the two terms. Because the target encoder shares weights with the online encoder, no stop-gradient is needed; both receive gradients through the optimizer. No labels are used. Pretraining takes under one minute per dataset on a single A10G GPU, with the full 14-dataset, 5-seed sweep completing in under two hours. Per-dataset preprocessing details are in appendix˜L.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Downstream: Predictor Finetuning", "weight": 1.0} -->

After pretraining, we freeze the encoder $f_{\theta}$ and finetune only the predictor $g_{\phi}$ together with a lightweight linear event head. This "predictor finetuning" (pred-FT) recipe tunes 198K parameters, compared to 2.16M for end-to-end training and 513 for a frozen linear probe. Finetuning reshapes the predictor's per-horizon outputs to separate event-relevant from event-irrelevant dynamics, making it more expressive than a linear probe, while the frozen encoder supplies the pretrained dynamical knowledge that makes few labels sufficient. End-to-end finetuning achieves equivalent h-AUROC at full labels (table˜4); pred-FT's advantage is computational efficiency and robustness under label scarcity (section˜5.4).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Downstream: Predictor Finetuning", "weight": 1.0} -->

The predictor is run at each of $K$ discrete horizons $\Delta t=1,\ldots,K$ (unit steps; $K{=}150$ for C-MAPSS/TEP, $K{=}200$ otherwise). A shared linear head maps each predicted representation to a per-interval *conditional hazard*: where $\sigma$ is the sigmoid function and $\lambda_{\Delta t}(t)$ approximates $P(\text{event in }(\Delta t{-}1,\Delta t]\mid T^{*}>\Delta t{-}1,\mathbf{x}_{\leq t})$, with $T^{*}$ denoting the time to the first event after $t$. The event probability surface is then parameterised as a discrete-time survival CDF: Because each factor $(1-\lambda_{j})\in$, the survival product is non-increasing in $\Delta t$, so $p(t,\Delta t)$ increases monotonically with the prediction horizon by construction.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Downstream: Predictor Finetuning", "weight": 1.0} -->

No distributional assumptions are required: each $\lambda_{\Delta t}$ is a free function of $\mathbf{h}_{t}$ via the predictor network. The finetuning loss sums positive-weighted binary cross-entropy (BCE) over horizons: where $y(t,\Delta t)=\mathds{1}[\text{event in }(t,t{+}\Delta t]]$ and $w^{+}=N_{\text{neg}}/N_{\text{pos}}$ compensates for class imbalance.^11^1We apply BCE to the cumulative event probability $p(t,\Delta t)$ rather than to the per-step hazards $\lambda_{j}(t)$ against per-step indicators (the standard discrete-survival likelihood, e.g. nnet-survival).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Downstream: Predictor Finetuning", "weight": 1.0} -->

This is a deliberate design choice: BCE on the cumulative surface acts as a smoothing regulariser across horizons (each hazard $\lambda_{j}$ contributes to BCE for every $\Delta t\geq j$), which empirically improves h-AUROC under our positive-weighted regime but distorts the probability scale (appendix O).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

Predictor finetuning rests on a premise: the pretrained encoder retains enough event-relevant information that a small downstream head can extract it. We formalise when this holds and connect the bound to experiments.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

Let $X_{\leq t}$ denote observations up to time $t$, and let $E_{t+\Delta t}\in\{0,1\}$ be a binary indicator that equals 1 if an event occurs in the interval $(t,t{+}\Delta t]$ and 0 otherwise. The encoder produces $H_{t}=f_{\theta}(X_{\leq t})\in\mathbb{R}^{d}$; the target encoder produces $H^{*}=\bar{f}_{\theta}(X_{(t,t+\Delta t]})\in\mathbb{R}^{d}$ from the future interval; and the predictor produces $\hat{H}=g_{\phi}(H_{t},\Delta t)$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

We define the event posterior $\eta(h)\coloneqq P(E_{t+\Delta t}{=}1\mid H^{*}{=}h)$ and the marginal event rate $\pi_{e}\coloneqq P(E_{t+\Delta t}{=}1)$, using $\pi_{e}$ to distinguish it from the probability surface $p(t,\Delta t)$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Evaluation Framework", "weight": 1.0} -->

The model outputs a probability surface $p(t,\Delta t)$ (eq.˜4) for each observation time $t$ and prediction horizon $\Delta t$. This surface is the complete prediction; every metric is computed deterministically from it (fig.˜4), enabling direct comparison with published baselines without retraining.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Evaluation Framework", "weight": 1.0} -->

As a cross-domain metric, we use h-AUROC: the mean of per-horizon AUROC values pooled over $(t,\Delta t)$ cells. Per-horizon prevalence varies wildly across datasets, and even within a single surface: on C-MAPSS-1, the event "failure within $\Delta t$ steps" has prevalence 0.5% at $\Delta t{=}1$ and 96% at $\Delta t{=}150$, a ${\sim}200{\times}$ range. Pooled area under the precision-recall curve (AUPRC) over all $(t,\Delta t)$ cells inherits a 0.957 baseline on C-MAPSS-1, because a model predicting only per-horizon prevalence already scores there. h-AUROC solves this by decomposing the surface into independent per-horizon binary classification problems, each with a universal 0.5 baseline that does not depend on prevalence. The uniform average treats all horizons equally; in practice, specific horizons matter more (long-range for turbine maintenance, short-range for arrhythmia).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Evaluation Framework", "weight": 1.0} -->

We use the uniform average for cross-domain comparability; the full surface is always stored for application-specific weighting. Domain-specific metrics (RMSE for remaining-useful-life, PA-F1 for anomaly detection) are derived as projections of the same surface for comparability with published baselines (appendix˜J). All numbers are reported as mean $\pm$ std across 5 seeds (HEPA, PatchTST, iTransformer, MAE) or 3 seeds (Chronos-2).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Setup", "weight": 1.0} -->

We pretrain a separate HEPA encoder per dataset from unlabeled training data. Architecture and hyperparameters are identical across all domains; only the input projection (sensor count $S$) changes. All comparison methods share the same 198K-param downstream MLP head, positive-weighted BCE loss, and evaluation protocol; only the frozen encoder differs. Dense unit-step horizons are used throughout: $K{=}150$ for C-MAPSS and TEP, $K{=}200$ for all others. The dataset overview (14 datasets, 11 domains) is in table˜3.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Main Results", "weight": 1.0} -->

Domain-specific SOTA metric C-MAPSS-1 [-1pt]turbine failure C-MAPSS-4 [-1pt]multi-cond.+fault SMAP [-1pt]sensor anomaly PSM [-1pt]server anomaly TEP [-1pt]process fault Weather [-1pt]heat spike VIX [-1pt]vol regime Matched downstream heads (HEPA 198K pred-FT; baselines 264K dt-MLP), positive-weighted BCE, identical protocol. K = 150 for C-MAPSS/TEP, K = 200 otherwise. Domain SOTAs are detection or RUL baselines; HEPA domain metrics projected from p(t, Δt) at the matching horizon (Δt = 1 for PA-F1/F1, 𝔼[Δt] for RMSE; appendix˜J). PA-F1 = point-adjusted F1. Pairwise Welch’s t-tests in appendix˜N. †Beijing-AQ PatchTST: 3 stations at 100%. Bottom block has no published domain SOTA.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Main Results", "weight": 1.0} -->

Additional baselines (MOMENT, TFM-2.5, Moirai, MTS-JEPA) in appendices˜G and H. Table 1: Main results (mean ± std; 5 seeds for HEPA, PatchTST, iTransformer, MAE; 3 seeds for Chronos-2). All methods use matched-capacity downstream heads on frozen encoders (appendix˜C). Each dataset has two rows: 100% labels and 10% labels (gray). Bold = best mean per row.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Main Results", "weight": 1.0} -->

Table˜1 compares HEPA against two classes of methods. The primary comparison is *architectural*: PatchTST, iTransformer, and a masked autoencoder (MAE) baseline use the same per-dataset regime with identical downstream heads, isolating the effect of JEPA pretraining versus alternative self-supervised and supervised objectives. The secondary comparison is against the *foundation model* Chronos-2, which pretrains on a large external corpus and operates in a fundamentally different regime. A full comparison against MTS-JEPA (matched protocol) is in appendix˜H; HEPA wins on 8 out of 9 datasets where MTS-JEPA could be reproduced (TEP excluded: the public MTS-JEPA release does not include a chemical-process benchmark).

<!-- chunk {"id": "body-0032", "role": "body", "section": "HEPA vs. architectural baselines", "weight": 1.0} -->

HEPA wins on 10 out of 14 benchmarks at 100% labels, including all four C-MAPSS variants and the newly added FD004 (the hardest subset: six fault modes, six operating conditions). HEPA's representation-level prediction captures temporal structure that supervised training (PatchTST) and reconstruction-based SSL (MAE) miss, particularly on datasets with extended precursor dynamics (C-MAPSS, GECCO, PSM, TEP). MAE is a strong second: it matches or exceeds HEPA on spacecraft telemetry (SMAP) and power systems (ETTm1), suggesting that reconstruction-based pretraining transfers well when the dominant failure mode is gradual drift. iTransformer's variate-attention mechanism excels on MBA (h-AUROC 0.84 vs. HEPA's 0.75), where arrhythmia patterns are localised across specific leads.

<!-- chunk {"id": "body-0033", "role": "body", "section": "HEPA vs. Chronos-2", "weight": 1.0} -->

HEPA matches or exceeds Chronos-2 on most benchmarks. Per-dataset JEPA excels when events have extended precursors that the local training data fully represents; large-corpus pretraining helps when event signatures resemble patterns seen at scale.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Honest losses", "weight": 1.0} -->

HEPA is below the best baseline on four datasets at 100% labels. The pattern is interpretable: BATADAL and MBA have sensor-localised events where channel-fusion tokenisation dilutes the relevant subset, so per-variate attention (iTransformer) or channel-independent training (PatchTST) wins; MAE's reconstruction objective transfers well when the dominant failure mode is gradual drift (SMAP, ETTm1). Adopting a sensor-as-token strategy within the HEPA encoder is a natural way to close this gap.

<!-- chunk {"id": "body-0035", "role": "body", "section": "What Does Pretraining Learn?", "weight": 1.0} -->

Figure˜3 visualises encoder representations after self-supervised pretraining on C-MAPSS-1. Without any labels, the encoder organises representations into a smooth degradation manifold: PC1 alone captures 61% of variance and tracks time-to-failure monotonically within each engine (median per-engine Spearman ${\rho}{=}{+}0.97$, $84\%$ of engines ${\rho}{>}0.9$). Engines starting from different healthy regions converge toward a shared failure region. This structure explains why so few labels suffice: the encoder has already separated healthy from degraded states.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Label Efficiency", "weight": 1.0} -->

All methods in table˜1 freeze their encoder and train only a downstream head, so all benefit from pretraining under label scarcity. The question is whether HEPA's representations degrade more gracefully. Table˜2 shows that on C-MAPSS, where degradation unfolds over hundreds of cycles and the JEPA predictor achieves low pretraining loss, HEPA retains 92% of full-label h-AUROC with just 2 training engines out of 85. C-MAPSS-3 retains 97% at 10% labels. This is consistent with proposition˜1. ‣ 3.3 Theoretical Analysis ‣ 3 Method ‣ HEPA: A Self-Supervised Horizon-Conditioned Event Predictive Architecture for Time Series"): low $\varepsilon$ on lifecycle datasets means the encoder already separates healthy from degraded states, so the finetuned predictor needs only a few labelled examples to map them to event probabilities.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Label Efficiency", "weight": 1.0} -->

The advantage is not universal. At 10% labels across all 14 datasets (table˜1, gray rows), HEPA wins on 6 out of 14, compared to 10 out of 14 at full labels. On anomaly datasets without extended precursors (SMAP, PSM, GECCO at 10%), the frozen-encoder setup limits how much any method can degrade, so margins compress. The label-efficiency story is strongest where HEPA's pretraining loss is lowest: extended-precursor lifecycle datasets.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conclusion & Future Work", "weight": 1.5} -->

HEPA demonstrates that self-supervised JEPA pretraining combined with predictor finetuning provides a practical recipe for event prediction. The encoder learns temporal dynamics from unlabelled data; the predictor learns which dynamics signal the target event. One architecture handles degradation forecasting, anomaly prediction, and arrhythmia detection across 14 benchmarks in 11 domains, matching or exceeding PatchTST, iTransformer, MAE, and Chronos-2 on the majority of benchmarks while tuning an order of magnitude fewer parameters. On lifecycle datasets, the recipe is robust to extreme label scarcity: 92% of full-label performance with 2% of labels on C-MAPSS, consistent with the information-retention guarantee of proposition˜1. ‣ 3.3 Theoretical Analysis ‣ 3 Method ‣ HEPA: A Self-Supervised Horizon-Conditioned Event Predictive Architecture for Time Series"). Because the recipe is domain-agnostic, the same architecture that predicts turbine failure from flight-recorder data can flag arrhythmia risk from ECG streams or detect water contamination from sensor networks, each time requiring only a handful of event labels.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Conclusion & Future Work", "weight": 1.5} -->

Looking ahead, cross-domain pretraining on corpora such as FactoryNet is the natural next step toward industrial deployment, and sensor-as-token strategies could close the gap on systems where event-relevant information is concentrated in a few channels. On the theory side, deriving fully empirical versions of the information-retention bound that estimate $L$ and $C_{\eta}$ directly from data remains an interesting open problem. Wherever multivariate sensors record the precursors to rare but consequential events, HEPA offers a path from unlabelled streams to actionable predictions.
