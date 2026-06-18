<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

FactoryBench: Evaluating Industrial Machine Understanding

Topics include Industrial machine understanding, Benchmarks, Time series, Robotic telemetry, Causal reasoning, Large language model evaluation, Question answering, FactoryWave.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces FactoryBench, a benchmark that turns industrial robotic telemetry into structured question-answer tasks across state, intervention, counterfactual, and decision levels. The paper highlights a large gap between frontier LLMs and operational machine understanding, especially for structured causal and decision-making questions grounded in time-series data.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce FactoryBench, a benchmark for evaluating time-series models and LLMs on machine understanding over industrial robotic telemetry. Q&A pairs are organized along four causal levels (state, intervention, counterfactual, decision) instantiating Pearl's ladder of causation, and span five answer formats: four structured formats are scored deterministically and free-form answers are scored by an LLM-as-judge voting protocol. We propose a scalable Q&A generation framework built around structured question templates, present FactoryWave (a dense, multitask, multivariate sensor dataset collected from a UR3 cobot and a KUKA industrial arm), and construct FactoryBench as a large-scale benchmark of over 70k Q&A items grounded in roughly 15k normalized episodes from FactoryWave, AURSAD, and voraus-AD. Zero-shot evaluation of six frontier LLMs shows that no model exceeds 50% on structured levels or 18% on decision-making, revealing a wide gap between current models and operational machine understanding.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Modern robotic manufacturing systems emit dense multivariate telemetry, encoding joint states, torques, forces, velocities, contact events, task phases, and fault indicators. Extracting actionable knowledge from these signals is central to monitoring, diagnostics, anomaly detection, and decision support.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Traditional time-series models excel at narrow tasks such as prediction, classification, and anomaly detection, but they are typically specialized, hard to interpret, output labels without explicit reasoning, and generalize poorly outside their training task, limiting their utility for automated engineering decisions in a factory setting. Large language models, in contrast, possess strong general reasoning and can produce structured technical explanations, but underperform when applied directly to dense numerical time series; specialized transformer-based architectures meanwhile continue to advance time-series forecasting and representation learning.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Evaluating whether language-based systems truly reason about machine behavior, rather than pattern-matching on textual cues, remains challenging. By *machine-behavior understanding* we mean the ability to (i) interpret the current operational state from raw multivariate signals, (ii) predict the effect of an intervention, (iii) reason counterfactually about alternative histories, and (iv) recommend remedial actions grounded in physical and engineering constraints. How current LLMs perform across these four competences on dense industrial telemetry has not yet been systematically measured. General benchmarks such as MMLU, BIG-bench, and MMMU target textual or multimodal understanding and cannot probe machine behavior; closer-in-spirit time-series Q&A benchmarks (TimeSeriesExam, ChatTS, EngineMT-QA, TSAQA, Time-MQA, MTBench, QuAnTS; Table 1) restrict themselves to synthetic or univariate data, omit counterfactual reasoning, or do not involve a robotic system under closed-loop control.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address this gap we propose FactoryBench, a benchmark for machine-behavior reasoning in time-series models and LLMs. FactoryBench is grounded in FactoryWave, a dense multivariate dataset collected from collaborative and industrial one-arm platforms (UR3 at 125 Hz, KUKA at 83 Hz) with synchronized setpoint, context, feedback, and effort signals. Industrial-robot data of this kind is rare in public benchmarks: such systems live in restricted production environments behind proprietary controllers with limited telemetry and plant-level confidentiality. To our knowledge FactoryWave is the first extensive anomaly dataset to (partly) cover an industrial robot, explicitly bridging the cobot-to-industrial-machine gap. To populate the benchmark, we introduce a scalable question-generation framework of 21 structured templates spanning state, intervention, counterfactual, and decision-making reasoning, applicable to general machine data flows; instantiated over FactoryWave (and AURSAD / voraus-AD), they yield the full FactoryBench Q&A corpus.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Four levels of machine understanding", "weight": 1.0} -->

“We want to isolate the lifting phase in the robot’s time series. Assuming a fixed window length of 15 timesteps, at which timestamp should the window begin?”
Can the model understand what the machine is doing and how it is behaving?

<!-- chunk {"id": "body-0009", "role": "body", "section": "Four levels of machine understanding", "weight": 1.0} -->

“A collision with a foam cube occurs at T = 850 ms. Rank signal segments (A–D) in the order you would expect them to appear after the event.”
Can the model reason about how the machine will behave in the face of an event?

<!-- chunk {"id": "body-0010", "role": "body", "section": "Four levels of machine understanding", "weight": 1.0} -->

“Had a payload misconfiguration occurred at T = 200 ms, what would the target torque on joint 2 at T + 50 ms have been in this counterfactual case?”
Can the model reason accurately about theoretical scenarios?

<!-- chunk {"id": "body-0011", "role": "body", "section": "Four levels of machine understanding", "weight": 1.0} -->

“Given the sensor stream below, does the machine show signs of anomalous behavior? If yes, identify the root cause and the steps to fix it.”
Can the model make informed decisions about the machine?

<!-- chunk {"id": "body-0012", "role": "body", "section": "Four levels of machine understanding", "weight": 1.0} -->

Our four-tier hierarchy is explicitly built on top of Pearl's ladder of causation association, intervention, and counterfactual reasoning which has become the organizing principle for causal inference and is increasingly adopted as an evaluation axis for machine-learning systems. We extend the causal hierarchy with a fourth decision-making level that reflects how industrial robotic platforms are actually operated: after interpreting state and causal relationships, operators must select and execute corrective procedures, typically prescribed by vendor manuals (e.g., Universal Robots error-code handbooks). This final level aligns with the diagnose-then-act loop that is standard in fault-tolerant control. Grounding the hierarchy in these established principles ensures that each level probes a qualitatively distinct reasoning skill and that failure modes are interpretable in terms of the underlying causal or decision-theoretic primitive.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Four levels of machine understanding", "weight": 1.0} -->

Level 1: State. This level assesses the agent's ability to interpret the current state of the machine under normal conditions, including identification of operational modes, prediction and recognition of sensor patterns. Questions at this level require accurate extraction and interpretation of time series features.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Four levels of machine understanding", "weight": 1.0} -->

Level 2: Intervention. At this level, the agent must reason about the consequences of interventions or events occurring at the present timestep that might perturb the distribution of machine states. Tasks include predicting the immediate impact of control actions, diagnosing faults as they arise, and understanding causal relationships in real time for both normal and anomalous episodes.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Four levels of machine understanding", "weight": 1.0} -->

Level 3: Counterfactual. This level evaluates the agent's ability to reason about hypothetical scenarios, such as the effect of an event or intervention at a previous timestep. Questions require the agent to simulate alternative histories and assess how outcomes would differ under counterfactual conditions, while still considering the history they know.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Four levels of machine understanding", "weight": 1.0} -->

Level 4: Decision Making. The highest level evaluates the agent's ability to act on its understanding of the system. Given a recorded episode and a task description, the agent must produce a sequence of actions or recommendations to answer that prompt. In FactoryBench, this targets troubleshooting and optimization, and combines the skills exercised at the previous three levels: reading the system state, reasoning about causes, and weighing alternative interventions. It reflects what we expect from an LLM acting as an engineering assistant on the factory floor.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Four levels of machine understanding", "weight": 1.0} -->

By structuring Q&A tasks along these four levels, FactoryBench enables rigorous and granular assessment of machine-behavior reasoning, from basic state recognition to advanced decision support. Figure 4 (Appendix B) instantiates Pearl's three causal levels (L1--L3) on robotic time-series data and adds the L4 decision-making layer that FactoryBench introduces on top. Each question is emitted in one of five answer formats (single-select MCQ, multi-select MCQ, ranking, tensor, free-form); the four structured formats are scored deterministically and free-form answers are scored by an LLM-as-judge voting protocol, with per-format details in Appendix A.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Time series data and causal schema (SCE)", "weight": 1.0} -->

So that the dataset structure itself encodes causality, all time-series signals are organized into three causal groups: Setpoint (the controller's commanded target), Context (physical and configured conditions, split into static episode metadata and dynamic time-series channels), and Effort+Feedback (the machine's measured response). Under healthy operation the response is a known function of setpoint and context; faults manifest as structured residuals from that baseline, giving a single operational fault definition that applies across machines and tasks. Full per-group channel mappings, the formal residual definition, and per-robot calibration details are deferred to Appendix K: full details ‣ FactoryBench: Evaluating Industrial Machine Understanding").

<!-- chunk {"id": "body-0019", "role": "body", "section": "Time series data and causal schema (SCE)", "weight": 1.0} -->

FactoryWave: A custom dataset generated from one-arm robotic platforms executing industrial tasks (e.g., pick-and-place) under varied conditions and systematically injected anomalies.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Time series data and causal schema (SCE)", "weight": 1.0} -->

Open Source Datasets: Adapted datasets such as AURSAD and voraus-AD, offering diverse industrial scenarios and preprocessed to conform to the unified episode structure.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Time series data and causal schema (SCE)", "weight": 1.0} -->

The datasets integrated into FactoryBench are summarized in Table 3 ‣ 3 FactoryBench framework ‣ FactoryBench: Evaluating Industrial Machine Understanding"); all provide the full setpoint--context--effort triplet at 83 Hz or higher and have been (re)labelled to conform to our unified episode schema.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Scalable generation via extensive labeling", "weight": 1.0} -->

Scalable ground-truth generation is the central challenge of any Q&A benchmark grounded in raw data. FactoryBench addresses this by coupling a structured labeling ontology with a context-free grammar (CFG)-style template system, designed by robotics experts and PhD researchers. Each template contains variable slots filled at generation time from one of two sources: label information read directly from the episode data (signal names, timestamps, anomaly labels, root causes), or a predefined sampling distribution attached to that slot (prediction horizons, numerical thresholds, curated vocabularies for discrete options). The discrete vocabularies are seeded from the label sets of AURSAD and voraus-AD, extended to cover FactoryWave-specific cases, and released in full so every instantiation is inspectable and reproducible. The context time series used to fill the variables is sampled uniformly by data source (open source vs FactoryWave), then dataset, experiment, length within controlled bounds, and finally placement, yielding a combinatorial expansion from a small set of carefully designed templates into a large, diverse question pool.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Scalable generation via extensive labeling", "weight": 1.0} -->

Each of the 21 templates is manually authored to probe one specific machine-understanding level while remaining general enough to admit a wide range of instantiations across episode segments, signal names, event descriptions, timestamps, and predicted values. Answer options for single- and multi-select questions are drawn from a shared pool of pre-defined verifiable statements (for example, the question *"What anomaly is present in this robotic sensor time series?"* draws its options from the full catalogue of documented anomalies), each paired with a rule that can be evaluated deterministically against the time series given the densely labelled data, so ground truth is never imputed or inferred but computed directly from the underlying labels; for single-select MCQ items, the option-sampling step additionally enforces that exactly one of the four sampled options evaluates to true on the chosen episode, so the question is unambiguous by construction.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Scalable generation via extensive labeling", "weight": 1.0} -->

This is also our primary defense against the natural concern that template-generated benchmarks can be solved by learning template surface structure rather than the underlying reasoning: every template admits a combinatorially large instantiation space over signal names, timestamps, prediction horizons, payload conditions, and injected-fault types, so two questions sharing the same template rarely overlap in more than a fraction of their variable slots, and the correct answer is never recoverable from the question text alone since it is always determined by the paired time series, which varies across instantiations.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Density of FactoryWave", "weight": 1.0} -->

FactoryWave is collected from two physical robots (UR3 and the KUKA; Figure 2) executing up to three industrial tasks each: pick-and-place, screwing, and peg-in-hole. Each complete task cycle constitutes one episode, recorded at 125 and 83 Hz across over 100 sensor channels covering joint setpoints, feedback, torques, speeds, estimated contact forces, TCP pose, gripper state, and task-phase labels. To compensate for the limited tool-side telemetry exposed by the KUKA KSS controller, we additionally mount a 9-DoF inertial measurement unit on the KUKA gripper and stream its acceleration, angular-rate, and orientation channels in sync with the controller signals. The full per-robot, per-task, per-condition breakdown of the 8,983 episodes is given in Table 8 of Appendix G.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Density of FactoryWave", "weight": 1.0} -->

Episodes are organized into three experiment types. Normal episodes capture nominal operation across three payload levels (light, medium, heavy for pick-and-place). Fault episodes inject one of 27 fault types (spanning gripper failures, misconfigurations, collisions, and peg-in-hole-specific anomalies), each recorded with fault-specific metadata and, where applicable, a precise injection timestep. Counterfactual episodes provide ground truth for Level 3 causal reasoning by approximating the do-operation on physical hardware, via the protocol described next.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Density of FactoryWave", "weight": 1.0} -->

Counterfactual generation approximates the last step of Pearl's ladder on physical hardware, which cannot reproduce a bit-identical pre-injection state. For each baseline we re-execute the task 3--5 times with every controllable condition held fixed (object pose, payload, controller configuration, exact scripted trajectory) and inject the target fault at a fixed timestep $t$. We then keep the run whose pre-injection segment minimizes the signature kernel MMD against the baseline, and use that episode as an approximate ground truth for hypothetical divergence of baseline.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Knowledge graph and protocol extraction", "weight": 1.0} -->

Reliable ground truth for Level 4 troubleshooting questions requires more than episode labels: it demands machine-specific recovery protocols grounded in manufacturer documentation. For each robot in FactoryBench we parse the manufacturer's official runtime error documentation into a structured mapping from error codes to error names, descriptions, and recommended recovery steps, capturing what the controller reports when a fault occurs and what an operator should do to resolve it. We then map every anomaly type studied in FactoryBench to the most likely corresponding manufacturer error code, with PhD-level robotics experts reasoning about the physical cause of each anomaly and identifying which runtime error it would most plausibly trigger on the target robot. Where a physical fault injection (such as gripper misactivation, peg misalignment, or external collision) has no well-defined controller error, the same experts author the recovery protocol directly using the same structure for consistency.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Knowledge graph and protocol extraction", "weight": 1.0} -->

The complete mapping (error-derived and expert-authored protocols alike) is ingested into a knowledge graph alongside robot specifications, task definitions, and signal schema. At question generation time, the pipeline queries this graph to automatically assemble the relevant protocol context and inject it as ground truth into Level 4 troubleshooting Q&A pairs, without requiring per-question human review.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Zero-shot evaluation", "weight": 1.0} -->

We evaluate a cross-vendor panel of frontier LLMs available at submission time: Claude Sonnet 4.6 and GPT-5.1 on the closed-weight side, and DeepSeek V3.2, Mistral Large 3, and Qwen3-235B on the open-weight side. We also include Qwen3-4B in zero-shot mode as a lightweight open-weight reference point. For calibration we report a non-LLM baseline that dispatches per item by answer format: linear regression on the target signal for scalar and tensor templates, and uniform random over the option set for single- and multi-select MCQ and ranking templates. Free-form Level 4 templates are excluded from the baseline (no traditional method maps cleanly to producing a remediation protocol). Figure 3 reports chance-corrected accuracy for the full panel.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Zero-shot evaluation", "weight": 1.0} -->

(a) Chance-corrected accuracy (%) on FactoryBench’s four reasoning levels.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Zero-shot evaluation", "weight": 1.0} -->

(b) GPT-5.1 L4 score distribution by ground-truth root cause (left, troubleshooting) and misconfigured parameter (right, optimization). Each bar shows the proportion of items scored 0/0.5/1; the right-edge value is the per-category mean accuracy.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Most models fail to separate from the simple baseline on Level 1, including the largest in the panel", "weight": 1.0} -->

Three of six LLMs fail to clear the L1 baseline (28.4%): GPT-5.1 (30.9%), by parameter-count and inference-cost proxies the largest in the panel, only matches it, and DeepSeek V3.2 (25.0%) and Qwen3-4B (21.8%) sit clearly below. Only Mistral Large 3 (34.6%), Qwen3-235B (36.0%), and Claude Sonnet 4.6 (46.8%) establish a margin. Raw scale does not reliably confer the ability to extract precise state from dense industrial signals; L1 measures something general-purpose pretraining does not optimize.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Models that struggle on Level 1 still outperform the baseline on Levels 2 and 3", "weight": 1.0} -->

Qwen3-4B (27.5%, 28.8%), DeepSeek V3.2 (29.1%, 28.5%), and GPT-5.1 (30.0%, 31.7%) all clear the bar on L2 and L3 despite scoring below it on L1. That being said, the model rank order is nearly identical across L1--L3: Claude Sonnet 4.6 stays in the lead at L2 and L3 (47.1%, 45.9%), Qwen3-235B is the strongest open-weight model and tops L3 (43.6%), and Mistral Large 3 follows (31.7%, 36.3%). This shows a strong correlation between the score of Levels 1--3, and point towards the fact that a stronger state comprehension translates into better intervention and counterfactual reasoning: L2 and L3 build on L1 ability rather than substituting for it.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Level 4 scores collapse absolutely, revealing an industrial readiness gap", "weight": 1.0} -->

Every model collapses below 18%: the leader reaches 17.7% and the other five score between 2.9% and 7.6%. Claude Sonnet 4.6, dominant on L1--L3, crashes to 4.3% on L4, on par with the weakest models in the panel. The model receives the time series and a machine description but must produce the root-cause diagnosis and multi-step recovery procedure from its own knowledge. The L1--3 scores below 50% already indicate a gap in state, intervention, and counterfactual understanding; the L4 collapse exposes a deeper one: models either lack the machine-specific technical knowledge to diagnose faults and prescribe remediation, or cannot ground that knowledge in the observed signals. Closing this gap is the central challenge FactoryBench is designed to measure.

<!-- chunk {"id": "body-0036", "role": "body", "section": "GPT-5.1 leads on the most practically relevant level despite underperforming on the others", "weight": 1.0} -->

The L4 ordering reshuffles completely relative to L1--L3: GPT-5.1, only fourth of six on the structured levels, leads L4 at 17.7%, more than twice the next-best. L4 requires naming the root cause and producing a multi-step remediation procedure grounded in manufacturer documentation; we conjecture that GPT-5.1's reversal reflects disproportionate exposure to structured industrial documentation in pretraining, letting it match a protocol to a fault description even when its signal comprehension is weak. The pattern reveals a dissociation between *signal comprehension* and *protocol retrieval*: optimizing for one does not deliver the other.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Within Level 4, GPT-5.1 shows asymmetric failure modes across troubleshooting and optimization", "weight": 1.0} -->

Breaking GPT-5.1's L4 performance down by question type (Figure 3(b)) exposes a structural difference in *how* the model fails. On troubleshooting ($n = {1,011}$, mean 0.174) the score distribution is sharply bimodal: 79.6% zero, 14.4% perfect, only 5.9% partial. The perfect-score mass concentrates on *nominal* (no-fault) episodes (Figure 3(b), left): GPT-5.1 emits "no anomaly" correctly on 33% of healthy episodes, accounting for 92% of all perfects. The remaining 11 perfects fall on collision, payload, and screw-thread faults whose signal signature is strong and unmistakable: a TCP force spike, a speed-scaling collapse, or a large torque drift.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Within Level 4, GPT-5.1 shows asymmetric failure modes across troubleshooting and optimization", "weight": 1.0} -->

Subtler anomalies (task-phase sequencing errors like an unintended loosening step, or flag-level state changes) produce no catastrophic event; GPT-5.1 then over-interprets the signal, attributing the change to a software bug or controller race rather than the expected phase transition, and scores zero or 0.5. Large-$n$ fault categories (loosening phase, missing screw, extra component) sit at $\leq {11\%}$ partial and $\leq {1\%}$ perfect: even when GPT-5.1 senses that something is off, it cannot recover the canonical root cause from the signal.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Within Level 4, GPT-5.1 shows asymmetric failure modes across troubleshooting and optimization", "weight": 1.0} -->

On optimization ($n = 102$, mean 0.201) GPT-5.1 *never* achieves a perfect score (41 partial, 61 zero; Figure 3(b), right). Ground-truth optimization answers are single-parameter corrections (e.g. "payload mass is set to 0.0 kg but the actual payload weighs 1.5 kg; update the installation settings"). GPT-5.1 instead emits lists of 8--12 generic motion-tuning suggestions (reduce acceleration, retune PID gains, add waypoints, lower speed scaling, enable force-mode compliance) and mentions payload configuration only as one undifferentiated item without specifying direction or magnitude, earning 0.5 at best (according to our grading policy). Together these patterns show that even though GPT-5.1 outperforms every other model by a wide margin on L4, it remains weak at decision-making in an industrial context.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Modular and extensible by design", "weight": 1.0} -->

FactoryBench is built to grow. The Q&A generator decouples reasoning templates from the underlying robot, task, and signal schema: every template is parameterized over generic primitives (signal names, phase indices, anomaly labels, fault categories) rather than hard-coded to a machine, so adding a new platform only requires populating the labeling ontology and per-robot signal mapping. All existing templates then instantiate automatically, and the format scorers, knowledge graph, and judge prompts carry over. Planned extensions include further robots and machine families (industrial arms, mobile manipulators, CNC and additive-manufacturing platforms), tasks (assembly variants, polishing, inspection), gripper and end-effector types, and templates targeting under-represented reasoning patterns. Each addition slots into the existing schema without breaking prior versions; the versioned release track pins every reported number to a fixed dataset state while the benchmark continues to grow.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Limitations", "weight": 1.5} -->

FactoryBench has two substantive limitations. First, Level 3 *counterfactual* ground truth on physical hardware is fundamentally approximate and resource-intensive to generate: two real runs cannot share an identical pre-injection state, so our signature-kernel-MMD-selected CF pair is the closest empirical proxy for the do-operation rather than the do-operation itself, and L3 scores therefore conflate model reasoning with proxy quality (simulation closes the gap only at the cost of physical realism). Second, as the first benchmark of its sort our Q&A pairs use a simplified fault model: industrial faults in production are typically compound, gradual, and detected through aggregate KPIs, while ours are atomic, fast, and drawn from a closed catalogue of 27 injected mechanisms, making FactoryBench a measurement of in-distribution fault *recognition* rather than the fault *detection* problem operators actually face.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduced FactoryBench, a four-level benchmark for machine understanding over industrial robotic telemetry, grounded in FactoryWave and structured around Pearl's causal hierarchy. Zero-shot evaluation of six frontier LLMs shows that signal comprehension and protocol-grounded decision-making are distinct capabilities that do not co-develop: models that lead on Levels 1--3 collapse on Level 4, while GPT-5.1 reverses rank at L4 despite being mediocre on the structured levels. Absolute scores remain well below 50% on L1--3 and below 18% on L4, with no model close to saturation. A natural follow-up direction is tool-augmented LLM agents that delegate quantitative subtasks to specialised tools (time-series foundation models, classical signal-processing modules, anomaly detectors, or other domain-specific components; Appendix H ‣ FactoryBench: Evaluating Industrial Machine Understanding")) and reserve the LLM for the linguistic, classification, and decision-making templates where it has the structural advantage.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The gap is structural, not incidental: until models can read industrial signals, reason causally about them, and translate that reasoning into operator-grade decisions, they have no business on the factory floor. FactoryBench draws that line, and gives the community the instrument to measure every step taken toward crossing it.
