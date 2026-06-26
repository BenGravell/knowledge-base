<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

RoboPlayground: Democratizing Robotic Evaluation through Structured Physical Domains

Topics include Robotics, Benchmarks, Generalization, Control, RoboPlayground.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Evaluation of robotic manipulation systems has largely relied on fixed benchmarks authored by a small number of experts, where task instances, constraints, and success criteria are predefined and difficult to extend. This paradigm limits who can shape evaluation and obscures how policies respond to user-authored variations in task intent, constraints, and notions of success. We argue that evaluating modern manipulation policies requires reframing evaluation as a language-driven process over structured physical domains. We present RoboPlayground, a framework that enables users to author executable manipulation tasks using natural language within a structured physical domain. Natural language instructions are compiled into reproducible task specifications with explicit asset definitions, initialization distributions, and success predicates. Each instruction defines a structured family of related tasks, enabling controlled semantic and behavioral variation while preserving executability and comparability. We instantiate RoboPlayground in a structured block manipulation domain and evaluate it along three axes. A user study shows that the language-driven interface is easier to use and imposes lower cognitive workload than programming-based and code-assist baselines. Evaluating learned policies on language-defined task families reveals generalization failures that are not apparent under fixed benchmark evaluations.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Finally, we show that task diversity scales with contributor diversity rather than task count alone, enabling evaluation spaces to grow continuously through crowd-authored contributions.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Who gets to decide what it means for a robot to be competent? Today, robotic manipulation systems are evaluated almost exclusively through benchmarks designed by a small number of experts. These benchmarks specify fixed task instances, success conditions, and evaluation protocols, implicitly encoding which behaviors matter and which variations are worth testing. While this paradigm has driven substantial progress, it centralizes control over evaluation and limits both who can define evaluation tasks and what questions can be asked about a system's behavior.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Outside of benchmarks, competence is rarely assessed through a single task instance. Understanding is revealed through exploration and variation: tightening constraints, rephrasing goals, or modifying what counts as success after observing an execution. Language plays a central role in this process. It provides a natural interface for expressing task intent and probing variations, where changes in wording often correspond to differences in spatial relations, constraints, or success criteria. As such, language offers a powerful handle for exploring structured variation in manipulation tasks.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, while language has been used to generate tasks or guide robot behavior, existing benchmarks do not support language-driven exploration as a first-class evaluation interface, where users can iteratively vary task intent, constraints, and success definitions in a reproducible and comparable manner. Evaluation tasks are typically realized as fixed environment configurations with success conditions encoded procedurally in code, while natural language serves only as informal documentation or as input to the policy itself. As a result, introducing new task variations or alternative notions of success requires direct intervention at the level of benchmark implementation, placing meaningful control over evaluation in the hands of domain experts and limiting accessibility for broader users.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Similar limitations have appeared in other domains. In visual reasoning, diagnostic datasets such as CLEVR reframed evaluation around controlled task generation within a structured domain. By focusing on interpretable primitives rather than maximal realism, CLEVR shifted evaluation from static instances to structured families of tasks, enabling clearer attribution of failure modes. In contrast, work in natural language processing has emphasized the dynamics of evaluation over time. Dynamic benchmarking efforts such as Dynabench treat evaluation as a human-in-the-loop process, where users iteratively generate and refine examples to surface model weaknesses. Together, these efforts highlight two complementary principles for informative evaluation: structured task spaces that make variation interpretable, and participatory mechanisms that allow evaluation to grow continuously beyond its initial design.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Evaluating modern manipulation policies requires embracing both principles. An effective evaluation system should satisfy four key desiderata. First, it must be accessible, allowing users to express task intent, constraints, and success criteria using natural language without expertise in simulation internals or benchmark-specific code. Second, it should support continuous growth, enabling the evaluation space to expand over time through contributions from many users rather than remaining fixed. Third, it must ensure reproducibility, so that tasks can be precisely re-executed across models and evaluations, enabling fair comparison as the evaluation space grows. Finally, it should provide structured control, constraining user-authored instructions to remain executable and interpretable while enabling systematic variation and meaningful attribution of failure modes.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose reframing robotic manipulation evaluation as a language-driven, user-authored process over structured physical domains, shifting evaluation from static expert-defined benchmarks to an accessible, reproducible, and continuously expanding task space.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we present RoboPlayground, a language-driven framework for defining robotic manipulation tasks in a structured physical domain. Natural language serves as the primary authoring interface, allowing users to specify task intent, constraints, and success conditions without interacting with benchmark-specific code. Each instruction is compiled into an executable task specification with explicit definitions of assets, initialization distributions, and success predicates, enabling tasks to be precisely re-executed across models and evaluations. Rather than yielding a single fixed task instance, each instruction defines a family of related tasks, whose systematic variations are authored and controlled by users through language within the domain's physical structure, allowing the evaluation space to grow continuously over time while preserving controlled, comparable structure.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We instantiate this framework in a structured manipulation domain that make language-defined tasks executable and systematically variable, rather than free-form descriptions. Within this setting, we demonstrate that language-driven task variation uncovers meaningful behavioral differences and failure modes that are not exposed by fixed benchmark tasks, including sensitivity to constraint changes and brittleness with respect to success definitions.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our evaluation demonstrates that RoboPlayground achieves these goals in practice. Through a controlled user study, we show that the language-driven task authoring interface is substantially easier to use and imposes lower cognitive workload than both programming-centric and code-assist baselines, indicating that non-expert users can reliably construct valid manipulation tasks. Evaluating learned policies on structured families of language-defined tasks reveals systematic generalization failures that are not apparent when testing only on fixed training-distribution benchmarks, including sensitivity to semantic changes and brittleness under altered success definitions. Finally, we show that the evaluation space defined by RoboPlayground scales through contributor diversity rather than task count alone, with crowd-authored task sets exhibiting significantly greater semantic and structural coverage than tasks generated by individual authors. Together, these results suggest that language-driven, structured task generation enables evaluation that is not only more accessible, but also more diagnostic and more representative of the space of behaviors we wish manipulation policies to master.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, this paper makes three contributions. We introduce a language-driven evaluation framework that democratizes manipulation evaluation by making task specification accessible to non-expert users while maintaining reproducibility. We empirically demonstrate that language-defined task families reveal policy behaviors and limitations that are missed by conventional instance-based benchmarks. We show that evaluation spaces can grow continuously through user- and model-authored instructions without sacrificing comparability or scientific rigor.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Evaluation and Benchmarking for Robotic Manipulation", "weight": 1.0} -->

Robotic manipulation systems are most commonly evaluated using fixed benchmark suites composed of predefined task instances, environments, and success criteria, such as RLBench, LIBERO, RoboCasa, Behaviour-1k, ManiSkill, Colosseum, Simpler, and RoboEval. While these benchmarks have been instrumental in standardizing evaluation, they define evaluation over a fixed and finite set of expert-authored tasks, with task structure, constraints, and success criteria encoded procedurally and not exposed for user modification. Although some benchmarks include natural language annotations or language-conditioned tasks, language is typically treated as documentation or policy input rather than as part of the executable task specification, making it difficult to introduce task variations or alternative notions of success without modifying benchmark code. Recent work has explored complementary directions for scaling evaluation: RoboArena democratizes who evaluates and where evaluation occurs through crowd-sourced, double-blind pairwise comparisons over unconstrained real-world tasks, while Polaris improves the fidelity and scalability of simulation-based evaluation via real-to-sim scene reconstruction, but retains fixed, expert-authored tasks and success criteria.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Evaluation and Benchmarking for Robotic Manipulation", "weight": 1.0} -->

In contrast, our work focuses on democratizing what is evaluated by enabling users to author, modify, and refine executable task specifications through language, while preserving structure, reproducibility, and comparability.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B LLM-Based Task and Environment Generation", "weight": 1.0} -->

Recent work has explored using large language models to generate robotic tasks, environments, rewards, or curricula at scale. Systems such as GenSim, Gen2Sim, RoboGen, and AnyTask leverage LLMs to synthesize tasks or simulation assets, while Eureka and Eurekaverse use language models to automatically generate reward functions or learning curricula. These approaches primarily target data generation and training diversity, rather than evaluation itself: generated tasks are treated as inputs to learning pipelines, and the task space is not exposed to users as a controllable or interpretable evaluation interface. Task generation is typically decoupled from mechanisms for enforcing reproducibility, tracking task lineage, or systematically relating task variations to evaluation outcomes. Language has also been used to guide robot behavior at execution time, as in SayCan and Code as Policies, where it serves as a high-level planning or control signal while task definitions and success criteria remain fixed and externally specified.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B LLM-Based Task and Environment Generation", "weight": 1.0} -->

In contrast, our work treats language as a first-class interface for evaluation: natural language instructions are compiled into structured, executable task specifications with explicit asset definitions, initialization distributions, and success predicates, enabling users to author reproducible families of semantically related evaluation tasks that support controlled variation and systematic comparison.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Methods", "weight": 1.0} -->

This section describes how the framework operationalizes the core desiderata: accessibility, continuous growth, reproducibility, and structured control. We first define the design principles and formalize the task representation in Section III-A. We then describe the task orchestration process that make language-defined manipulation tasks executable and interpretable in Section III-B. We then describe how natural language instructions are compiled into concrete, reproducible task artifacts through a validation pipeline that enforces physical realizability and consistency Section III-C. Finally, we introduce a context-aware steering mechanism that enables users to systematically vary tasks and expand the evaluation space over time while preserving explicit comparability between task variants in Section III-D.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Task Representation and Design Principles", "weight": 1.0} -->

Our framework treats natural language as an executable interface for task specification. User instructions are compiled into concrete task realizations that fully determine assets, initialization logic, and success conditions. Rather than producing isolated benchmark instances, the system yields reusable task artifacts that can be shared, re-executed, and systematically varied, enabling evaluation spaces to grow through user contribution without sacrificing scientific rigor. Figure 2 provides an overview of this process. Natural language instructions are compiled into structured task proposals, synthesized into executable implementations, and admitted as task artifacts only after passing a multi-stage validation pipeline. Validated artifacts can then be iteratively refined through context-aware steering, enabling controlled task variation while preserving reproducibility and explicit lineage.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A Task Representation and Design Principles", "weight": 1.0} -->

Formally, we define a manipulation task as a tuple where $\mathcal{A}$ denotes the set of task assets, $\rho_{0}$ is a distribution over initial states, $G:\mathcal{S}\rightarrow\{0,1\}$ is a success predicate over simulator states, $\ell$ is the canonical natural language instruction, and $\mathcal{V}$ is a set of paraphrases used for robustness testing.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Task Representation and Design Principles", "weight": 1.0} -->

This decomposition reflects a deliberate design choice. Logical equivalence at the level of language does not imply equivalence of task realization: differences in tolerances, reset distribution, or success-check timing can lead to divergent evaluation outcomes even when tasks are described identically. Language alone is therefore insufficient as a unit of evaluation.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Task Orchestration Through Language", "weight": 1.0} -->

Given a natural language description $u$, task construction begins by translating language into a structured representation of task intent. Specifically, the system infers and populates a fixed TaskSchema that explicitly specifies the task name, relevant assets, goal conditions, and initialization logic. The use of a fixed schema ensures that all task-relevant fields are present and disambiguated before execution, enabling complete interpretation of the instruction and preventing underspecified task definitions.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Task Orchestration Through Language", "weight": 1.0} -->

Conditioned on the validated task schema, the system then synthesizes an executable task implementation. This process leverages an LLM with access to relevant environment APIs, prior task implementations, and diagnostic error information retrieved based on structural similarity to the proposed task. The LLM produces an intermediate natural-language task specification that articulates the intended objects, goal configuration, and success criteria, which is subsequently compiled into executable code.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Task Orchestration Through Language", "weight": 1.0} -->

Executable tasks are implemented as classes that extend a fixed environment interface. Each task defines methods for environment initialization, reset-time sampling from $\rho_{0}$, and success evaluation corresponding to $G$. This constrained interface enforces uniform structure across task implementations and limits variation arising from authoring style, ensuring that differences in evaluation outcomes reflect task content rather than implementation artifacts.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C Validation and Physical Realizability", "weight": 1.0} -->

Language-defined tasks are only meaningful if they are both executable and physically realizable. Each synthesized task implementation is therefore subjected to a multi-stage validation pipeline before being admitted as a task artifact.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-C Validation and Physical Realizability", "weight": 1.0} -->

Basic validation. Basic validation enforces software correctness independent of physics simulation. Generated code is subjected to static analysis to detect syntactic errors and forbidden patterns, compiled in an isolated execution environment to detect import and definition errors, and instantiated to detect runtime failures during object creation or reset-time sampling.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-C Validation and Physical Realizability", "weight": 1.0} -->

Goal-state verification. To enforce physical realizability of the success predicate, tasks are instantiated directly in the goal configuration and simulated forward under zero action to allow contacts to settle. The success predicate $G$ must evaluate to true after settling and remain true over an extended horizon, ensuring that the goal configuration is both achievable and stable under the simulator's physics model.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-C Validation and Physical Realizability", "weight": 1.0} -->

Iterative repair. When validation fails, the failure is classified according to its source (e.g., syntax, API usage, runtime instantiation, goal satisfaction, or physical instability), and a corresponding repair operator proposes a localized modification to the task implementation. Repairs may adjust object placements, relax geometric constraints, or rewrite components of the success predicate, depending on the failure type. Validation is then re-run on the repaired implementation. This process repeats until all checks pass or a fixed retry budget is exhausted, ensuring that admitted tasks satisfy executability and physical consistency while remaining faithful to the original language intent.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-D Controlled Task Modifications", "weight": 1.0} -->

A validated task artifact defines a reference task instance from which a family of related tasks can be derived. To enable systematic task variation without sacrificing comparability, the framework provides a context-aware steering mechanism that interprets user modification requests and constrains how tasks may evolve.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-D Controlled Task Modifications", "weight": 1.0} -->

Given a modification request, the system first interprets the intent and extracts structured parameters such as dimensional changes, ordering constraints, or asset-type substitutions. It then classifies the request into one of five steering categories: *Tweak*, *Extend*, *Modify*, *Pivot*, or *Fresh*. Each category specifies explicit preservation guarantees over the task components $(\mathcal{A},\rho_{0},G)$. For example, *Tweak* and *Extend* preserve the original task structure and success predicate, enabling direct comparability with the reference task, while *Modify* and *Pivot* permit progressively broader semantic or structural changes when required by the user intent.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-D Controlled Task Modifications", "weight": 1.0} -->

Task evolution is tracked through versioned snapshots that record structured summaries of assets, goals, and code hashes. When a modification requires asset types incompatible with the current version, the system selects a compatible prior snapshot as the reference. This allows coherent multi-step refinement without manual bookkeeping. Each validated variant produces a new snapshot, yielding version-controlled task families with explicit lineage suitable for systematic evaluation and controlled analysis of task variation.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Results", "weight": 1.0} -->

We evaluate RoboPlayground along three axes that are central to its role as a democratized evaluation framework for robotic manipulation: (i) the usability of its task authoring interface, (ii) the diagnostic value of the resulting task set for assessing policy generalization, and (iii) the scalability of task creation under open-world, crowd-driven use. Across all experiments, we focus on whether RoboPlayground enables task specifications that are both easier to author and more informative for evaluation than existing alternatives.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A Usability of the Task Authoring Interface", "weight": 1.0} -->

Experimental setting. We evaluate the usability of RoboPlayground in comparison to two baseline task authoring interfaces, GenSim and Cursor, using a within-subjects user study ($N=26$). Participants were asked to construct an identical manipulation task (build a 3D structure using blocks under various constraints) using each system. All participants interacted with all three systems, enabling paired comparisons of perceived usability, cognitive workload, and user preference. We measure usability using the System Usability Scale (SUS), cognitive workload using NASA-TLX subscales \[8: results of empirical and theoretical research")\], and overall preference through usability and forced-choice rankings. Results are summarized in Table I.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A Usability of the Task Authoring Interface", "weight": 1.0} -->

RoboPlayground achieves higher perceived usability than baselines. Across participants ($N{=}26$), RoboPlayground attains the highest System Usability Scale (SUS) score ($83.4\pm 6.9$; mean $\pm$ 95% confidence interval margin), well above the conventional acceptability threshold of 68. GenSim and Cursor achieve substantially lower mean SUS ($52.5\pm 9.3$ and $68.8\pm 7.8$, respectively). Paired Wilcoxon signed-rank tests confirm that RoboPlayground significantly outperforms both GenSim ($p{<}0.001$) and Cursor ($p{=}0.0017$), so the advantage is not limited to the weakest baseline: RoboPlayground is rated more usable than a strong general-purpose assistant interface as well. The interval for GenSim is the widest of the three, consistent with more heterogeneous experiences in that condition, whereas RoboPlayground shows the tightest margin among systems, indicating comparatively consistent high ratings.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-A Usability of the Task Authoring Interface", "weight": 1.0} -->

RoboPlayground reduces perceived cognitive workload relative to baselines. Cognitive workload is summarized as the unweighted mean of five NASA-TLX subscales (Mental Demand, Temporal Demand, Effort, Frustration, and reversed Performance), each normalized to 0--100 and oriented so that lower is better. RoboPlayground yields the lowest mean composite score ($18.6\pm 7.7$; mean $\pm$ 95% confidence interval margin), compared to $41.8\pm 9.0$ for GenSim and $36.7\pm 10.4$ for Cursor. Paired Wilcoxon signed-rank tests show that RoboPlayground significantly reduces perceived workload relative to both GenSim ($p{=}0.0007$) and Cursor ($p{=}0.0019$).

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-A Usability of the Task Authoring Interface", "weight": 1.0} -->

GenSim and Cursor do not differ significantly from each other on this composite ($p{=}0.22$), whereas RoboPlayground separates clearly from each baseline; Cursor also exhibits the widest TLX margin among the three, indicating somewhat more spread in workload ratings even though the paired comparison to RoboPlayground remains significant.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-A Usability of the Task Authoring Interface", "weight": 1.0} -->

Participants consistently prefer RoboPlayground over baseline interfaces. Subjective measures reinforce the quantitative usability and workload results. RoboPlayground achieves the best mean usability rank ($1.3\pm 0.3$; lower is better), with GenSim and Cursor at $2.7\pm 0.2$ and $2.0\pm 0.2$, respectively. A Friedman test shows strong differences in rankings across systems ($p{<}0.001$), and post-hoc paired Wilcoxon tests confirm that RoboPlayground is ranked significantly better than both GenSim ($p{=}0.0001$) and Cursor ($p{=}0.0078$). In forced-choice overall preference, $69\%$ of participants select RoboPlayground, compared to $23\%$ for Cursor and $8\%$ for GenSim. A chi-square goodness-of-fit test rejects a uniform split across the three options ($p{=}0.0003$), consistent with concentration of preference on RoboPlayground.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-A Usability of the Task Authoring Interface", "weight": 1.0} -->

Together, the ranking and preference distributions indicate a stable, statistically supported tilt toward RoboPlayground over both baselines.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Evaluating Policies on Training and Generated Generalization Tasks", "weight": 1.0} -->

Red Block Left Place Two Blue Place Two Blocks Place Two Blocks TABLE II: Results on in-distribution and generalization tasks. Success rates (%) with standard errors across six policies evaluated on training (in-distribution) tasks (top) and held-out generalization tasks (bottom). The best result per task is shown in bold. Generalization tasks are constructed by perturbing training tasks along one or more axes: semantic (S), denoting language perturbations, visual (V), denoting visual appearance differences in the initial state, and behavioural (B), denoting changes in the required behaviour, adhering to the definitions. The perturbation type for each generalization task is shown in the row labeled Perturbation, with semantic perturbations indicated in blue, visual perturbations in green, and behavioural perturbations in red.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-B Evaluating Policies on Training and Generated Generalization Tasks", "weight": 1.0} -->

Tasks. All policies are trained on a shared set of base manipulation tasks covering spatial relations, stacking, alignment, semantic disambiguation, and targeted placement. For each training task, we generate successful demonstration trajectories using CuTAMP and hold the resulting dataset fixed across policies, ensuring that performance differences reflect policy behavior rather than differences in supervision. Evaluation is performed on (i) tasks drawn from the training distribution, and (ii) user generated generalization tasks that require adaptation beyond the training distribution. Generalization tasks are constructed by applying controlled modifications to base tasks using RoboPlayground, including semantic changes to language instructions, visual changes to object attributes and initial configurations (e.g. partially stacked versus scattered on table), and behavioral changes that alter the required action sequences or temporal structure. These transformations follow the task taxonomy described, and are designed to isolate specific dimensions of generalization while preserving task validity.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-B Evaluating Policies on Training and Generated Generalization Tasks", "weight": 1.0} -->

Models. We evaluate six policies spanning different action head architectures and fine-tuning strategies. Four are built on a shared Qwen3-VL-4B-Instruct vision-language backbone and differ in their action decoding mechanism: Adapter appends learnable action query tokens to the VLM sequence and decodes actions via an MLP-ResNet regression head with an L1 objective; GR00T conditions a flow-matching diffusion transformer (DiT) on the VLM's final hidden states, adopting a dual-system architecture inspired by GR00T N1.5; Dual extends this flow-matching action head with a secondary DINOv2 visual encoder whose patch features are concatenated with the VLM hidden states before conditioning; and Qwen-OFT regresses actions from special action-token positions via an MLP head, following the OpenVLA-OFT design. As external baselines, we include Pi-0.5, a proprietary VLA with flow-matching action generation, evaluated both with full finetuning and with low-rank adaptation (Pi-0.5 (LoRA)). All models are trained end-to-end on identical demonstration data.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-B Evaluating Policies on Training and Generated Generalization Tasks", "weight": 1.0} -->

Details of training configurations and generalization tasks are outlined in the appendix.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-B Evaluating Policies on Training and Generated Generalization Tasks", "weight": 1.0} -->

Training-distribution performance. We first report performance on tasks drawn from the training distribution (top section of Table II) to provide context for subsequent generalization results. All models achieve moderate to high success on tasks involving simple spatial relations and single-object placement, with GR00T, Dual, and Qwen-OFT consistently outperforming Pi-0.5 and Adapter on most placement and relational tasks. GR00T achieves the highest overall in-distribution performance, reaching 96% on Place Two Blocks on Patch and leading on stacking-related tasks. However, all models exhibit a consistent difficulty gradient: performance degrades sharply on training tasks requiring greater compositional structure or longer-horizon execution, such as multi-block stacking and color block alignment, where even the strongest model does not exceed 22%. Adapter shows notably uneven in-distribution performance, achieving competitive results on some tasks (e.g., 78% on patch placement) while lagging substantially on others (e.g., 26% on left placement).

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-B Evaluating Policies on Training and Generated Generalization Tasks", "weight": 1.0} -->

The Pi-0.5 (LoRA) variant underperforms all other models across nearly every training task, suggesting that low-rank adaptation alone is insufficient to retain the base model's capabilities in this setting.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-B Evaluating Policies on Training and Generated Generalization Tasks", "weight": 1.0} -->

Generalization results reveal a clear asymmetry across perturbation types. Across held-out evaluation tasks, all models generalize unevenly across perturbation axes, though the degree of degradation varies by architecture. Performance remains relatively strong under visual perturbations that alter perceptual attributes while preserving execution structure: GR00T achieves 90% on Place Two Blocks on Green Patch and 86% on Place Two Blue Blocks on Patch, and Dual similarly transfers well on these tasks (72% and 80%, respectively). Semantic perturbations alone yield mixed but non-zero success for most models, with GR00T reaching 78% on Yellow Block Left Placement and 62% on Green on Blue Stack, and Dual achieving 74% and 56% on the same tasks, indicating meaningful robustness to relational re-specification. Adapter, however, largely fails under semantic perturbation (e.g., 4% on Yellow Block Left Placement, 0% on Green on Blue Stack), suggesting that adapter-based finetuning may overfit to surface-level task features. In contrast, tasks involving behavioural perturbations consistently expose severe failure modes across *all* architectures.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-B Evaluating Policies on Training and Generated Generalization Tasks", "weight": 1.0} -->

Tasks requiring multi-stage execution, non-monotonic progress (e.g., unstack-restack), or compositional sequencing yield near-zero success universally---no model exceeds 2% on Yellow on Red Unstack Restack or Stack Two Blocks on Patch, and Blue Block Stacking elicits 0% across the board. These failures occur despite reasonable performance on simpler stacking or placement tasks in isolation, suggesting limited procedural and compositional generalization rather than a lack of basic manipulation competence. Pi-0.5 (LoRA) further degrades performance across nearly all perturbation axes, confirming increased sensitivity to deviations from training task structure under constrained adaptation. Together, these results establish behavioural perturbations as the dominant source of generalization failure *independent of model architecture* and motivate evaluation protocols that explicitly probe execution structure.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-B Evaluating Policies on Training and Generated Generalization Tasks", "weight": 1.0} -->

Implications. Together, these results demonstrate that success on a fixed set of training-distribution tasks can substantially overestimate a policy's robustness. By enabling the generation of creative task variants that probe specific semantic, visual, and behavioral dimensions of generalization, RoboPlayground enables fine-grained diagnosis of policy capabilities and failure modes that are obscured by static task definitions.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-C Scalability and Diversity of RoboPlayground", "weight": 1.0} -->

((a)) t-SNE visualization of task embeddings grouped by user.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-C Scalability and Diversity of RoboPlayground", "weight": 1.0} -->

((c)) Cumulative diversity as tasks are added per user.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-C Scalability and Diversity of RoboPlayground", "weight": 1.0} -->

For evaluation, diversity matters not as raw task count, but as coverage of distinct task intents and constraint combinations that probe different policy behaviors. We evaluate how task diversity in RoboPlayground scales with the number of contributors and the number of authored tasks. Each contributor authors up to 50 valid manipulation tasks in the blocks domain using the same interface and asset set. To quantify diversity, we compute average pairwise distances between task representations using semantic sentence embeddings, and analyze both pooled task sets across contributors and cumulative task sets authored by individuals. In the appendix, we report additional analyses using alternative diversity measures, which show consistent trends.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-C Scalability and Diversity of RoboPlayground", "weight": 1.0} -->

Inter-user diversity scales with contributors. Figure 4(a) shows the distribution of tasks authored by individual users. A t-SNE projection reveals that some users occupy distinct regions of the embedding space, while others exhibit substantial overlap, suggesting systematic differences in how contributors conceptualize and describe manipulation goals within the domain. When tasks are pooled across users (10 tasks per user), the mean pairwise diversity increases monotonically with the number of contributors (Fig. 4(b)). Even after substantial saturation, adding the final three contributors yields a consistent, non-zero increase in diversity, indicating that new contributors continue to introduce semantically novel task formulations.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-C Scalability and Diversity of RoboPlayground", "weight": 1.0} -->

Intra-user diversity exhibits diminishing returns. In contrast, Figure 4(c) shows that when tasks are added incrementally from a single user, cumulative diversity grows rapidly at first but quickly plateaus. This behavior is consistent across most users, suggesting that individual authors often explore a limited region of the task space, potentially shaped by their preferred abstractions, phrasing, and constraint patterns. Even prolific contributors produce increasingly redundant task variations over time.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-C Scalability and Diversity of RoboPlayground", "weight": 1.0} -->

Complementarity of multiple contributors. Notably, the combined task pool outperforms any individual contributor in terms of cumulative diversity, as showin in Figure 4(c). This gap highlights the complementary nature of crowd-authored task generation: different users introduce distinct semantic concepts, compositional structures, and constraint combinations that are rarely discovered by a single author alone. Qualitative inspection of task clusters confirms the presence of novel formulations of spatial relations, multi-object constraints, and success conditions that are absent from single-author collections.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-C Scalability and Diversity of RoboPlayground", "weight": 1.0} -->

Overall, these results show that RoboPlayground scales not merely by increasing task count, but by expanding coverage of the underlying task space through contributor diversity. By expanding coverage across task intent and constraint structure, RoboPlayground enables evaluation to reveal brittleness to even seemingly minor semantic variations.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Ablative Studies", "weight": 1.0} -->

+ feasibility checking (all gates on) None (all disabled)

<!-- chunk {"id": "body-0056", "role": "body", "section": "Ablative Studies", "weight": 1.0} -->

+ in-context examples (all gates on) None (all disabled)

<!-- chunk {"id": "body-0057", "role": "body", "section": "Ablative Studies", "weight": 1.0} -->

+ specialist agents (all gates on) None (all disabled)

<!-- chunk {"id": "body-0058", "role": "body", "section": "Ablative Studies", "weight": 1.0} -->

+ reference selection (all gates on) TABLE III: Ablation Study. We evaluate the contribution of each pipeline component through cumulative addition. Starting with all gates disabled for that module, we progressively enable components to measure their incremental impact. All success metrics are percentages (n = 26); LLM Alignment is scored out of 100. Green values with ↑ indicate improvement from the previous row.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Ablative Studies", "weight": 1.0} -->

We conduct a cumulative ablation study to quantify the functional contribution of each component in the task generation pipeline. For each module, we begin with all components disabled and progressively enable individual gates. This design disentangles changes in semantic task specification from improvements in robustness and correctness under session-level evaluation (Table III).

<!-- chunk {"id": "body-0060", "role": "body", "section": "Ablative Studies", "weight": 1.0} -->

Metrics. We report complementary metrics capturing distinct failure modes. Compile and Smoke Test measure code correctness and execution stability; Task Success measures end-to-end satisfaction of the success predicate; Human Verification evaluates perceived task validity; and LLM Alignment measures consistency between the natural language instruction and the implemented success condition.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Ablative Studies", "weight": 1.0} -->

Evaluation setting. Ablations are evaluated on ten benchmark testcases, each consisting of multiple related tasks evaluated as a single session. Some testcases involve multi-stage task refinement via context-aware steering; additional details are provided in the Appendix.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Ablative Studies", "weight": 1.0} -->

Task Proposal. Task proposal components primarily affect semantic grounding rather than executability. Enabling asset inference improves Human Verification (88.5 to 92.3) but slightly reduces LLM Alignment (74.0 to 71.5), while leaving execution metrics unchanged. Adding feasibility checking improves both Human Verification (92.3 to 96.2) and LLM Alignment (71.5 to 73.6) without affecting executability.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Ablative Studies", "weight": 1.0} -->

Code Generation. Code generation components primarily improve robustness to systematic implementation errors. Across ablations, compilation and smoke test success remain near-perfect. API review, error checks, and in-context examples incrementally improve LLM Alignment (70.8 to 73.6) while preserving end-to-end executability.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Ablative Studies", "weight": 1.0} -->

Validation. Validation is the dominant determinant of task correctness. With validation disabled, Task Success drops to 12.0 despite high compilation rates. Text-level validation alone recovers Task Success to 96.2, while the full validation stack achieves perfect Task Success, Compile, Smoke Test, and Human Verification.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Ablative Studies", "weight": 1.0} -->

Context Steering. Context steering influences semantic coherence across multi-step task sessions. Intent interpretation and version history tracking improve Task Success, Human Verification, and LLM Alignment, while routing without history degrades semantic consistency. With full context steering enabled, execution metrics remain perfect.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Ablative Studies", "weight": 1.0} -->

Summary. Overall, task proposal and context steering shape semantic intent and coherence, code generation improves robustness, and validation enforces correctness. Improvements in Task Success do not monotonically track alignment metrics, motivating a modular, gated design that balances expressiveness and executability.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Discussions", "weight": 1.0} -->

This work explores how robotic manipulation evaluation changes when task specification is opened to a broader set of contributors. By treating language as an executable interface, RoboPlayground allows users to express task intent, constraints, and success criteria directly, rather than relying on fixed, expert-authored benchmarks. In doing so, it reframes evaluation as a process shaped not only by models and metrics, but by the people defining what is being tested.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Discussions", "weight": 1.0} -->

Language-driven evaluation becomes meaningful when grounded in a shared physical structure. Compiling language into explicit assets, initialization logic, and success predicates enables users to author and vary tasks in ways that remain reproducible and comparable. Within this structure, semantic differences in task descriptions translate into controlled differences in evaluation, allowing policies to be assessed across families of related tasks rather than isolated instances.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Discussions", "weight": 1.0} -->

Lowering the barrier to task authoring also changes how evaluation spaces grow. Our results show that task diversity scales more strongly with contributor diversity than with task count alone, indicating that opening task specification to many users leads to broader and more complementary coverage of the task space. In this sense, RoboPlayground democratizes not only access to evaluation, but influence over what behaviors are examined.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Discussions", "weight": 1.0} -->

We instantiate the framework in a deliberately constrained block manipulation domain to emphasize interpretability and control. Extending structured, language-driven evaluation to richer domains will require careful design, but the underlying principle remains: scalable evaluation benefits from being both structured and open to user-driven contribution.
