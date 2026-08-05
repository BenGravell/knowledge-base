<!-- arxiv-full-text:v1 {"arxiv_id": "2503.01238", "source": "arxiv-latex"} -->

## Introduction

Learning-based robotics comes with the promise of broad generalization. As an example, an ambitious goal is to train a laundry-folding robot on diverse household data that can fold laundry in new homes. If trained effectively, the robot should be able to fold unseen clothing items in new settings using its extensive prior experience. However, we have yet to reach a point in robot manipulation where policies can reliably generalize in this manner. In pursuit of this vision, recent work has focused on scaling up data collection[mandlekar2018roboturk, dasari2019robonet, ebert2021bridge, jang2022bc, brohan2022rt, brohan2023rt, shafiullah2023bringing, bharadhwaj2023roboagent, walke2023bridgedata, fang2023rh20t, khazatsky2024droid, mirchandani2024robocrowd] and developing more expressive models[brohan2023rt, kim24openvla, wang2024scaling, liu2025rdtb, black2024pi\_0], following the successes of other machine learning domains.

While these advances have led to more capable policies, it is often unclear how generalist these policies truly are. Although prior work has shown various forms of generalization, such as visual robustness to distractors, or understanding novel language instructions, there is often a lack of consistency across different evaluations. Each work proposes their own forms of generalization and evaluation conditions, usually with little transparency into how they were decided upon. As a result, it has become difficult to measure progress toward real-world deployability of these policies, which has remained largely elusive, despite promising results in the literature.

To work towards more comprehensive and systematic evaluations, we propose $\bigstar$-Gen\xspace(STAR-Gen) a Systematic Taxonomy of the Axes of Robot Generalization. We observe that policies require generalization when there are perturbations to the policy's inputs or required outputs. Therefore, to ground our taxonomy, we structure $\bigstar$-Gen\xspacebased on the input and output modalities of visuo-lingual control policies: vision, language, and actions. We categorize perturbations as visual, semantic, and/or behavioral based on how they affect these modalities. For each combination of these labels (e.g., visual only, or visual + behavioral), we define more granular generalization axes. For instance, we include Object Properties as a semantic axis, which involves generalizing from put carrot on plate" to put the orange object on the plate".

Visualization of $\bigstar$-Gen\xspacefor the example base task put carrot on plate". $\bigstar$-Gen\xspaceis structured around perturbations to the modalities of visuo-lingual policies (visual, semantic, behavioral), with consideration for each of their combinations, which we refer to as categories. For each category (colored sectors), we further group perturbations into axes (light colored boxes). We provide some example perturbations.

To demonstrate the practical utility of $\bigstar$-Gen\xspace, we present two real-world case studies on benchmarking generalization. First, we develop BridgeV2-$\bigstar$\xspace, a benchmark based on the Bridge V2 dataset[walke2023bridgedata], that is intended to provide a blueprint for designing generalization benchmarks using a reproducible and open-source platform. We outline the design choices of BridgeV2-$\bigstar$\xspacebased on our taxonomy, and use it to evaluate state-of-the-art open-source generalist manipulation policies. $\bigstar$-Gen\xspaceto develop an additional case study based on the bimanual ALOHA 2 platform[aldaco2024aloha]that considers more dexterous, varied, and longer-horizon tasks, supported by a large-scale real-world dataset with thousands of hours of demonstrations. This further demonstrates the broad applicability of our taxonomy to a wide range of settings. $\bigstar$-Gen\xspace, a taxonomy of generalization structured around three modalities vision, language, and actions that span the space of generalization for visuo-lingual manipulation policies. We instantiate $\bigstar$-Gen\xspaceas two real-world case studies that consist of 1600+ robot trials across 14 axes of generalization, which generate more detailed findings on state-of-the-art generalist policies and model design decisions. We hope that by guiding policy training and evaluation efforts, $\bigstar$-Gen\xspacecan help advance progress in robot manipulation.

## Related Work

To achieve broad generalization in robotics, much prior work has focused on scaling up real-world data collection. These efforts typically aim to capture diversity in both environmental conditions and task behavior[mandlekar2018roboturk, dasari2019robonet, ebert2021bridge, walke2023bridgedata, fang2023rh20t, o2023open, khazatsky2024droid]. While these datasets are usually collected with diversity in mind, it is often unclear what forms of diversity matter, or how this diversity should be achieved. Recent works have investigated best practices for generating diverse robot data[@gao2024, lin2024data, saxena2025what]. Although these works consider various notions of diversity during data collection and corresponding axes of generalization during evaluation, these axes are neither exhaustive nor standardized.

Nevertheless, recent works have attempted to leverage these datasets for learning generalist robot policies. These works involve training large-scale, visuo-lingual policies on this data, with the goal of generalizing to a wide variety of scenarios [brohan2022rt, brohan2023rt, bharadhwaj2023roboagent, o2023open, kim24openvla, wang2024scaling, liu2025rdtb, black2024pi\_0]. However, each work designs their own evaluations that often focus on a relatively narrow selection of generalization, making it challenging to assess how models make progress towards different forms of generalization.

A compelling alternative is to benchmark generalization in simulation. There has been extensive work in simulated robot manipulation platforms that support task and scene diversity [james2020rlbench, mu2021maniskill, szot2021habitat, ehsani2021manipulathor, li2023behavior, nasiriany2024robocasa]. However, these largely do not come with benchmarks that measure precise notions of generalization. While some works have studied specific distribution shifts in simulation[xing2021kitchenshift, mees2022calvin, xie2024decomposing, pumacay2024colosseum, li2024evaluating], the generalization axes considered are usually inconsistent across works, similar to real-world efforts.

To help unify and provide structure to notions of generalization in robot manipulation, we propose $\bigstar$-Gen\xspace, which considers a superset of generalization axes from prior works. We hope this taxonomy can be useful for developing better datasets and models that make progress towards generalization, and developing better benchmarks to capture this progress.

## What is Generalization?

In this section, we outline our preliminaries, provide a formal characterization of generalization for robot policies, and list some additional assumptions, which we will use later in sec:axes:tax to design our taxonomy $\bigstar$-Gen\xspace.

### Preliminaries

Environment. We define an environment as the tuple $E = (\mathcal{S}, \mathcal{O}, \mathcal{A}, \mathcal{L}, f_o, f_t)$, where $\mathcal{S}$ is the state space, $\mathcal{O}$ is the observation space derived from $\mathcal{S}$ through observation function $f_o: \mathcal{S} \to \mathcal{O}$, $\mathcal{A}$ is the action space, and $f_t: \mathcal{S} \times \mathcal{A} \to \mathcal{S}$ is the transition function. We assume $\mathcal{O}$ consists of third-person images of a scene, and $\mathcal{A}$consists of robot actions.

Task. For an environment $E$, we define a task space $T$. A task $\tau \in T$ is defined as $\tau = (p_\tau(s_0), l_\tau, R_\tau)$, where $p_\tau(s_0)$ is an initial state distribution for $E$, $l_\tau \in \mathcal{L}$ is a language instruction, and $R_\tau: (\mathcal{S} \times \mathcal{A})^* \to \{0, 1\}$ is a success function that maps a state/action sequence to a success indicator. $p_\tau(s_0)$ defines an initial observation distribution $p_\tau(o_0)$ induced by $f_o$.

Policy. A policy $\pi(a \mid o^n, l)$ takes in $n \geq 1$ observations, a language instruction, and outputs an action distribution. We define an expert policy $\pi_E(a \mid o^n, l)$ that produces successful episodes (where success is defined by $R_\tau$) for a given task $\tau$.

### Defining Generalization for Visuo-Lingual Policies

Generalization in robotics is often considered as the performance of a policy $\pi$ on a task $\tau'$ outside its training distribution. To deploy policies in diverse settings, there is a vast space of potential tasks $\tau'$ to consider. Furthermore, it can be challenging to characterize how tasks represent generalization from large datasets. To address these challenges and provide a theoretically grounded framework, we propose structuring our taxonomy of generalization around perturbationsof a given base task, and how they affect the core input and output modalities of a robot policy, which we formalize as follows: Base Task. A base task $\tau_B$is a task where an end application desires a policy to perform the task (e.g., chopping a specific onion) and perturbations of it (e.g., chopping other onions). $\bigstar$-Gen\xspace: Axes of Generalization | Axis | Name | Description | Example Factors | Perturbations. We define a perturbation function as a transformation $P: T \to T$, that applies a task delta to a base task $\tau$ to produce a new task $\tau_P$. We categorize perturbations induced by a perturbation function based on how the inputs and outputs of a policy $\pi(a \mid o^n, l)$are impacted:

- Visual: $\tau_P$ is a visual perturbation of $\tau$ if $p_{\tau}(o_0) \neq p_{\tau_P}(o_0)$ (the initial distribution of image observations has changed.) - Semantic: $\tau_P$ is a semantic perturbation of $\tau$ if $l_\tau \neq l_{\tau_P}$ (the language instruction has changed.) - Behavioral: $\tau_P$ is a behavioral perturbation of $\tau$ if the expert policy $\pi_E$ changes its action distribution for the task (the required optimal behavior changes.)

This categorization is not mutually exclusive, meaning a perturbation can fall under more than one category. This can also be extended to other policy modalities, e.g., if a policy uses tactile information or sound[Lee2018MakingSO], we can further categorize perturbations based on changes to these modalities.

### Additional Assumptions

Atomic Perturbations. We focus on atomic perturbations, which we loosely define as involving a single change (e.g., pick up plate" $\to$ push the cup" is not atomic because it involves both changing plate" to cup" and pick" to push").

Short-Horizon Tasks. There are forms of generalization specific to long-horizon manipulation, such as reordering sub-tasks in a sequence. We do not consider this, and instead focus on perturbations that are broadly applicable to short-horizon tasks. However, in our case study on bimanual manipulation (sec:aloha), we evaluate on longer-horizon tasks to demonstrate that $\bigstar$-Gen\xspacecan also be applied to such settings.

## Axes of Generalization

| | | 4cOliveGreen!20Visual | 5cApricot!40Semantic | 1cRoyalBlue!20B | 4cBlueGreen!20VB | 2cOrchid!20SB | 1cGray!20VSB | | | | | | | | | | | | We present existing generalization benchmarks/datasets and generalist policy learning works through the lens of $\bigstar$-Gen\xspace, including BridgeV2-$\bigstar$\xspace. Columns are different axes in $\bigstar$-Gen\xspace(a subset of 17/22 axes in tab:axes). A checkmark indicates a given axis is considered.

### $\bigstar$-Gen\xspace: A Taxonomy of Generalization

Here we define $\bigstar$-Gen\xspace, our taxonomy of generalization. We aim to organize perturbations in a human-interpretable manner to guide policy evaluation. To this end, we define factors, axes, and categories, which represent different levels of hierarchy in our taxonomy, in decreasing order of granularity.

Factors. We define a factor as a human-interpretable, fine-grained grouping of perturbations that affect a task in a common way. For example, if the lighting in a scene is changed in multiple ways, each would represent a separate perturbation. We can then group all such perturbations under the factor Lighting". Factors can be categorized as visual, semantic, and/or behavioral, based on their constituent perturbations.

Axes. We define an axis as a human-interpretable grouping of similar factors that affect a common set of policy modalities. For example, our taxonomy defines Image Augmentations as an axis of visual factors that can be varied using simple image transforms, such as Lighting" or Image Blur". The axes in our taxonomy are designed to be a practically comprehensive set of the most salient challenges identified in the literature.

Categories. We define a category as a grouping of all axes that affect the same combination of policy modalities. For example, the category visual captures all axes that only affect the initial image observations of a task, including Image Augmentations. There are seven possible categories (the number of combinations of policy modalities). By capturing all combinations of how policy modalities can be affected by a given perturbation, we intend for these categories to provide a complete framing of generalization conditions for robot manipulation.

We outline the axes in $\bigstar$-Gen\xspacein tab:axes. For each axis, we provide a description and examples of constituent factors. While these axes are intended to be applicable to a broad range of tasks, some tasks will not always have meaningful instantiations of an axis. In fig:axes, we show example perturbations of the base task put carrot on plate" for several axes.

### Prior Notions of Generalization

tab:compare, we list prior works that measure generalization and the axes of $\bigstar$-Gen\xspacethey consider, in comparison with BridgeV2-$\bigstar$\xspace, a benchmark we designed using $\bigstar$-Gen\xspace(sec:measuring). As shown, $\bigstar$-Gen\xspaceaims to be a comprehensive superset of prior efforts to measure generalization. There are other nuances between prior works and $\bigstar$-Gen\xspacethat are observable in tab:compare, some of which we describe here.

Prior works are often not as fine-grained as $\bigstar$-Gen\xspacein their categorization of generalization. For example, RT-2[brohan2023rt] simply groups many of our visual + behavior axes under the blanket category Behavior Generalization". Prior works also often categorize perturbations in ways that are only applicable to certain tasks. For example, Colosseum[pumacay2024colosseum] considers Receiver Object" (RO) perturbations (e.g., the rack" in put wine in rack"), which does not apply to tasks without such objects. In $\bigstar$-Gen\xspace, we address this by considering different levels of hierarchy, where our high-level categorization is amenable to all tasks, while our lower levels may be more task-specific.

Lastly, prior works differ in how their evaluation protocols consider perturbations, often in less practical ways. For example, OpenVLA [kim24openvla] considers perturbations with respect to a portion of training data from a large-scale mixture (OXE), for a scene that their evaluation setting aims to emulate. However, it can be difficult to replicate scenes from an outside data source, possibly leading to unintended perturbations. In BridgeV2-$\bigstar$\xspace, we define $\bigstar$-Gen\xspaceperturbations with respect to in-domain data from the evaluation scene, to more easily control for this.

## Case Study 1: Bridge V2

$\bigstar$-Gen\xspaceprovides a broad framework for generalization in robot manipulation, but how should it be used to evaluate policies? In this section, we use $\bigstar$-Gen\xspaceto instantiate BridgeV2-$\bigstar$\xspace, a real-world benchmark based on Bridge V2[walke2023bridgedata]. We first describe our benchmark and our rationale for its design. Then, we use it to evaluate several state-of-the-art open-source models and variations. Our goal is for BridgeV2-$\bigstar$\xspaceto demonstrate how $\bigstar$-Gen\xspacecan be used to design generalization benchmarks using a reproducible and open-source platform.

### Instantiating $\bigstar$-Gen\xspace on Bridge V2

Dataset. We use Bridge V2[walke2023bridgedata] as our pre-training dataset and platform, since it has been used in multiple prior works to study generalization[walke2023bridgedata, kim24openvla, team2024octo], and its training environments have been reliably reproduced for evaluation[yang2024robot, hejna2024re, team2024octo, kim24openvla].

Base Tasks. We consider the base tasks put carrot on plate", put knife on plate", flip pot upright", and put plate in sink". We choose these base tasks based on the support of the pre-training data. In particular, they are instantiated in a replication of a sink environment from Bridge V2 that was used to evaluate generalization in prior work[kim24openvla]. We choose these specific tasks to cover different levels of alignment with the original tasks from Bridge V2 for this sink environment.

Axes and factors in BridgeV2-$\bigstar$\xspace.

We evaluate 4 in-distribution base tasks and 55 perturbations that cover 13/22 axes in $\bigstar$-Gen\xspace. We do not cover some axes due to incompatibility with our base tasks. We list our evaluated axes and factors in tab:bridge\_axes, and visualize some base tasks and their perturbations in fig:visual\_bridge and fig:visual\_behavioral\_bridge. We further detail our evaluation conditions in our Appendix (can be found on our stargen-taxonomy.github.iowebsite).

Policies. We focus our evaluation on state-of-the-art open-source imitation learning policies that have demonstrated generalization for Bridge V2 tasks in prior work. Specifically, we analyze three vision-language-action (VLA) models that fine-tune foundation models on robot data: OpenVLA [kim24openvla], MiniVLA [belkhale2024minivla], and a third-party reimplementation of $\pi_0$ [black2024pi\_0, ren2024pi]. These models cover a range of design decisions that reflect the state of generalist manipulation policies.

Examples of visual perturbations in BridgeV2-$\bigstar$\xspace. Left: in-distribution base task scene. From left to right: we vary sink color (V-SC), plate color (V-OBJ), and camera angle (V-VIEW).

Examples of object poses (VB-POSE\xspace) in BridgeV2-$\bigstar$\xspace.

Evaluation Procedure.We evaluate our models using a co-fine-tuning procedure. First, we pre-train each model only on Bridge V2. Next, we collect base task demonstrations from our evaluation environment, and co-fine-tune on this with Bridge V2. We denote co-fine-tuned models with (FT). put carrot" and put knife" base tasks, we collect 10 demonstrations per base task. For the flip pot" and put plate" base tasks, we collect 50 demonstrations per base task. We execute policies until the robot succeeds, reaches a dangerous/irrecoverable state, or terminates after 100 timesteps. We perform five trials per condition for each model.

BridgeV2-$\bigstar$\xspacemain results. We report aggregated success rates for each model and axis, including in-distribution (ID).

Scaling robot data Scaling LLM backbones We investigate VLA design decisions. (a) Scaling robot datasets can help. (b) Larger LLMs can provide a modest benefit to semantic axes. (c) VQA co-training can help, but has a mixed effect on semantic axes. (d) VQ action chunking can help.

### Main Results

fig:main-results, we report our main results on BridgeV2-$\bigstar$\xspace, which consist of 885 trials. We find that existing generalist policies tend to struggle on most axes. In particular, semantic generalization is mostly weak, despite the use of language model backbones. This has interesting implications: e.g., instead of relying only on language model initialization to improve semantic generalization, perhaps other mechanisms are needed, such as improving robot language annotations[smith2024steer].

Each model tends to have similar strengths and weaknesses. However, there are some notable differences that the fine-grained nature of our benchmark helps reveal. For example, OpenVLA is noticeably worse at visual generalization, while MiniVLA struggles more with visual + behavioral. OpenVLA is the best at understanding object properties, but still struggles with other semantic axes. $\pi_0$ generally performs the best, possibly due to a more capable VLM backbone (PaliGemma [beyer2024paligemma]), and/or better architecture (flow-based action chunking).

| Visual | Semantic | Visual + Behavioral | Semantic + Behavioral | Across Categories | Average Pearson correlations of performance for axes within the same category (left) and across categories. (right) Axes Correlations. To further motivate our high-level categorization based on policy modalities, we investigate performance correlations across models for axes within the same category, compared to across categories. In tab:axes\_correlations, we find that correlations are higher within categories, except for semantic. We hypothesize this is because our semanticaxes can require much different forms of reasoning (e.g., understanding object properties is much different than language rephrasing).

Prioritizing Axes.From these results, we provide some general guidelines on axes to prioritize in future work.

- Visual-only axes generally exhibit stronger generalization than behavioral axes (with the exception of Viewpoint). We hypothesize this is because VLA vision-language pre-training is more likely to convey visual robustness than generalization to new behavior. Therefore, future work on generalist manipulation should de-prioritize visual-only axes (except Viewpoint) in favor of - While semantic generalization is weak, whether to prioritize these axes depends on how the policy is deployed. If the policy is used with open-ended language, then these axes are important. However, if language is more constrained (e.g., a system where a separate model provides a limited set of instructions), they can be de-prioritized.

### Investigating VLA Design Decisions

While our main results provide insights on model capabilities, it is difficult to disentangle what contributes to generalization. To better understand this, we conduct additional targeted evaluations on model design choices, with $t$-tests to assess statistical significance.

Scaling Robot Data. In fig:ablations-1(a) we compare our Bridge-only OpenVLA with a version trained on a significantly larger, cross-embodiment OXE mixture[o2023open]. Consistent with prior work[o2023open, kim24openvla], we find that larger and more diverse datasets can significantly improve forms of generalization, such as for visual + behavioral axes $(M=0.22$ vs. $M=0.48), t = -2.76, p = 0.028$. However, the axes on which the Bridge-only model struggled the most (Viewpoint\xspace, Morphed Objects\xspace, Multi-Object Referencing\xspace) do not improve significantly.

Scaling LLM Backbones. In fig:ablations-1(b) we compare VLA policies that differ only in the large language model (LLM) backbone. Specifically, we compare OpenVLA (Bridge, FT), using Llama 2 7B [touvron2023llama], and MiniVLA (Bridge, VQ, FT), using Qwen2.5 0.5B[yang2024qwen2]. The only major difference between these two models is their LLM backbone. We find that while the larger LLM improves semantic axes, it is not by a significant amount $(M=0.18$ vs. $M=0.35), t = -1.87, p = 0.104$. Absolute performance for these and other axes also remain low, suggesting that scaling LLMs only has limited benefits.

VQA Co-training. In fig:ablations-1(c), we investigate co-training with visual-question answering (VQA) data, which prior work has shown to improve generalization[brohan2023rt]. We find this can help, such as for visual axes $(M=0.30$ vs. $M=0.45), t = -2.39, p = 0.048$. However, there is surprisingly a mixed effect for semantic axes $(M=0.38$ vs. $M=0.42), t = -0.51, p = 0.626$, improving three of them, but hurting Object Properties\xspace. This indicates room for improvement, possibly by using data targeted for embodied reasoning[zawalski2024robotic].

VQ Action Chunking. In fig:ablations-1(d), we investigate using binning-based tokenization instead of vector quantized action chunking with MiniVLA. We find that VQ action chunking helps nearly all axes, including visual axes by a significant amount $(M=0.38$ vs. $M=0.62), t = -2.38, p = 0.049$. This highlights the importance of action chunking and tokenization methods, as also suggested by prior work[zhao2023learning, pertsch2025fast].

## Case Study 2: Bimanual Manipulation

Next, we use $\bigstar$-Gen\xspaceto develop an additional case study based on the bimanual ALOHA 2 platform[aldaco2024aloha].

Examples of visual perturbations in our bimanual case study. Left: in-distribution base task. From left to right: we vary distractor objects (V-SC), table background (V-SC), and lighting (V-AUG).

### Experimental Setup

We use a proprietary robot dataset of thousands of hours of teleoperated demonstrations collected on a fleet of ALOHA 2 robots. This allows us to assess generalization for tasks with more variety, dexterity, and horizon length than those considered in BridgeV2-$\bigstar$\xspace, such as tightening a water bottle and folding a dress. We evaluate on 17 in-distribution base tasks with 68 perturbations that cover 7 axes in $\bigstar$-Gen\xspace. These are the same conditions used to evaluate generalization for Gemini Robotics[team2025gemini] (see Appendix C.1.3 in the technical report), but recategorized according to $\bigstar$-Gen\xspaceaxes. We visualize examples of conditions for visual axes in fig:visual, semantic axes in fig:semantic, and visual + behavioral axes in fig:visual\_behavioral.

Examples of semantic perturbations in our bimanual case study. Left: in-distribution base task instruction. From left to right: we test robustness to typos (S-INT), language (S-INT), understanding object size (S-PROP), and rephrasing (S-LANG).

Examples of visual + behavioral perturbations in our bimanual case study. Left: changes to object pose (VB-POSE) from in-distribution. Right: changes to object geometry (VB-MOBJ).

We evaluate 3 models: a multi-task diffusion policy [chi2023diffusion], a reimplementation of $\pi_0$[black2024pi\_0], and Gemini Robotics On-Device (GRoD)[deepmind2025gemini\_robotics\_on\_device], a proprietary VLA. We report policy task progress. We refer to[team2025gemini] for more details on our evaluation conditions, protocol, and the diffusion and $\pi_0$policies.

### Results

We report our results in fig:aloha\_results, which consist of 390 trials. We find that GRoD consistently outperforms the other models, which we speculate is due to its strong VLM backbone and other architectural enhancements. In particular, $\bigstar$-Gen\xspacehelps identify perturbations that GRoD is robust to while the other models fail almost entirely, such as translating the instruction to a new language (example in fig:semantic). We use this case study to demonstrate the broad applicability of $\bigstar$-Gen\xspacewith more diverse, dexterous, and long-horizon tasks.

Results from our bimanual manipulation case study. We report aggregated task progress for each model and axis.

## Discussion

We present $\bigstar$-Gen\xspace, a taxonomy of generalization for robot manipulation. Our taxonomy not only thoroughly considers the space of visuo-lingual policy generalization, but is also straightforward to instantiate. We demonstrate the considerations and design process for instantiating $\bigstar$-Gen\xspaceon a real-world, reproducible benchmark, eliciting key insights about generalist policy capabilities design choices. We further demonstrate using $\bigstar$-Gen\xspaceto study generalization for a wider set of tasks and policies on the ALOHA 2 platform. We hope that $\bigstar$-Gen\xspacecan help improve the comprehensiveness of generalization benchmark design to generate better insights.

Limitations and Future Work. Due to constraints imposed by real-world evaluation time (1600+ trials), we only evaluate a subset of axes and factors that we believe most effectively demonstrate the utility of $\bigstar$-Gen\xspace. We hope that $\bigstar$-Gen\xspacecan guide future benchmarking efforts that expand the scope considered in our evaluations, such as using simulation to more efficiently and comprehensively measure policy generalization. $\bigstar$-Gen\xspaceto be a strong starting point, we believe that future work can revise and expand our taxonomy based on the needs of robotics practitioners. Specifically, while we have argued for the completeness of our high-level categories, our set of fine-grained axes is empirically derived. Future work may identify new generalization challenges that could be incorporated as new axes within our framework.
