<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Taxonomy for Evaluating Generalist Robot Manipulation Policies

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Machine learning for robot manipulation promises to unlock generalization to novel tasks and environments. But how should we measure the progress of these policies towards generalization? Evaluating and quantifying generalization is the Wild West of modern robotics, with each work proposing and measuring different types of generalization in their own, often difficult to reproduce settings. In this work, our goal is to outline the forms of generalization we believe are important for robot manipulation in a comprehensive and fine-grained manner, and to provide reproducible guidelines for measuring these notions of generalization. We first propose STAR-Gen, a taxonomy of generalization for robot manipulation structured around visual, semantic, and behavioral generalization. Next, we instantiate STAR-Gen with two case studies on real-world benchmarking: one based on open-source models and the Bridge V2 dataset, and another based on the bimanual ALOHA 2 platform that covers more dexterous and longer horizon tasks. Our case studies reveal many interesting insights: for example, we observe that open-source vision-language-action models often struggle with semantic generalization, despite pre-training on internet-scale language datasets.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We provide videos and other supplementary material at stargen-taxonomy.github.io.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Learning-based robotics often comes with the promise of generalization. As an example, an ambitious goal is to train a policy on diverse household data so it can enter a new home and fold laundry. This vision has led to many recent works that train robot policies on diverse datasets via imitation learning with the hope of broad generalization. For example, if a robot encounters an unseen item of clothing in a new home, it should infer how to fold it using its extensive prior experience. However, in contrast to other domains like language and vision, we have yet to reach a point in robotics where policies can reliably generalize in this manner.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In pursuit of reliable and broad generalization, recent work has focused on scaling up data collection and developing more expressive models, following the successes of other machine learning fields. Although these advances have led to more capable policies that certainly generalize to some novel scenarios, it is often unclear from existing evaluations how generalist these policies truly are.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

While prior work on learning generalist policies demonstrate various forms of generalization, such as visual robustness to distractor objects, or understanding novel language instructions, there often lacks consistency and exhaustiveness in the evaluations considered. Each work proposes their own forms of generalization and evaluation conditions for measuring them, usually with little transparency into how they were decided upon. As a result, it has become difficult to measure progress toward the real-world deployability of these policies. Despite promising results reported in the literature, real-world deployment of generalist policies has remained largely elusive.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To work towards more comprehensive and systematic evaluations that better capture progress towards deployability, in this work we develop a taxonomy of generalization to guide policy evaluation efforts. To ground our taxonomy, we observe that policies require generalization when there are *perturbations* to the policy's *inputs* or required *outputs*. Thus, our insight is to structure our taxonomy around each input and output modality of a given policy, to more comprehensively consider the various perturbations a policy may need to generalize to.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To this end, we propose $\bigstar$-Gen (STAR-Gen) -- a Systematic Taxonomy of the Axes of Robot Generalization. $\bigstar$-Gen is built around the input and output modalities of visuo-lingual control policies, which have three such modalities: vision, language, and actions. Therefore, we categorize perturbations as visual (changes to visual inputs), semantic (changes in language inputs), and behavioral (changes to action outputs). For each combination of these labels (e.g., visual only, or visual + behavioral), we provide more granular generalization *axes* to guide evaluation. For instance, we include *Object Properties* as an axis for the category semantic, which involves generalizing from the language instruction "put carrot on plate" to "put the orange object on the plate" for the same underlying behavior.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

To demonstrate the utility of our taxonomy in practice, we present a real-world case study of designing a generalization benchmark, BridgeV2-$\bigstar$, based on the popular Bridge V2 dataset. We outline all design choices of our benchmark based on our proposed taxonomy. We then evaluate several state-of-the-art open-source manipulation policies, such OpenVLA, MiniVLA, and a re-implementation of $\pi_{0}$ on this benchmark. BridgeV2-$\bigstar$ not only provides a more detailed, granular view of the generalization capabilities of current models, but also offers a blueprint for designing generalization benchmarks based on any given training dataset.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our evaluations -- consisting of 1600+ robot trials across 13 axes of generalization -- generate several insights into these state-of-the-art models. For example, we find that larger cross-embodiment robot datasets can improve several axes of generalization, but offer limited benefits along axes that existing models struggle with the most. In addition, we find that co-training policies with general vision-langauge data can improve many axes, but has a surprisingly mixed effect on semantic axes. We also find that using an improved action tokenization scheme can broadly improve many axes.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, we present $\bigstar$-Gen, a taxonomy of generalization structured around the three modalities -- vision, language, and actions -- that span the space of generalization for visuo-lingual policies. We perform a case study of instantiating $\bigstar$-Gen as a real-world benchmark, BridgeV2-$\bigstar$. BridgeV2-$\bigstar$ consisted of 1600+ evaluations across 13 axes, and led to new findings on state-of-the-art generalist models, and the impact of various model design decisions. We hope $\bigstar$-Gen provides guidance for training models and evaluating for generalization, to help advance progress for generalist robot policies.

<!-- chunk {"id": "body-0012", "role": "body", "section": "What is Generalization?", "weight": 1.0} -->

In this section, we outline our preliminaries, provide a formal definition of generalization when evaluating robot policies, and list additional assumptions, which we will use later in Section IV-A to design our taxonomy $\bigstar$-Gen.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A Preliminaries", "weight": 1.0} -->

We first define several foundational concepts that we will later use to define generalization: Environment. We define an environment as the tuple $E=(\mathcal{S},\mathcal{O},\mathcal{A},\mathcal{L},f_{o},f_{t})$, where $\mathcal{S}$ is the state space, $\mathcal{O}$ is the observation space derived from $\mathcal{S}$ through observation function $f_{o}:\mathcal{S}\to\mathcal{O}$, $\mathcal{A}$ is the action space, and $f_{t}:\mathcal{S}\times\mathcal{A}\to\mathcal{S}$ is the transition function. We assume $\mathcal{O}$ consists of third-person images of a scene, and $\mathcal{A}$ consists of robot actions.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Preliminaries", "weight": 1.0} -->

Task. Given an environment $E$, we define a task space $T$. A task $\tau\in T$ is defined as $\tau=(p_{\tau}(s_{0}),l_{\tau},R_{\tau})$, where $p_{\tau}(s_{0})$ is an initial state distribution for $E$, $l_{\tau}\in\mathcal{L}$ is a language instruction that specifies the task, and $R_{\tau}:(\mathcal{S}\times\mathcal{A})^{*}\to\{0,1\}$ is a success function that maps a sequence of states and actions to a binary success indicator. This also defines an initial observation distribution $p_{\tau}(o_{0})$ induced by $f_{o}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Preliminaries", "weight": 1.0} -->

Policy. A policy $\pi(a\mid o^{n},l)$ takes in $n\geq 1$ observations, a language instruction, and outputs an action distribution.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Preliminaries", "weight": 1.0} -->

Expert Policy. We define the expert policy as $\pi_{E}(a\mid o^{n},l)$, which produces successful episodes (where success is defined by $R_{\tau}$) for a given task $\tau$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-B Defining Generalization for Visuo-Lingual Policies", "weight": 1.0} -->

Generalization is often defined in prior work as measuring the performance of a policy $\pi$ on some task $\tau^{\prime}$ that lies outside some source distribution of tasks (i.e., in some target distribution). Having a source distribution implies the policy $\pi$ learns from data, such as expert demonstrations in imitation learning (IL), or online samples in reinforcement learning (RL). In this work, we focus on the IL setting and use the terms source distribution and training distribution interchangeably, although our formalism is extendable to any setting with a source distribution and target distribution to generalize to.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-B Defining Generalization for Visuo-Lingual Policies", "weight": 1.0} -->

However, for policies to be deployable in diverse settings, there is an immense space of potential tasks $\tau^{\prime}$ that should be considered (i.e., the target distribution is vast). Furthermore, it can be challenging to define the training distribution for large datasets, making it difficult to characterize how a task captures generalization from the training distribution. Rather than attempting to define evaluation tasks as representing generalization relative to the entire training distribution of a policy, as is often the case in prior work, we define generalization more precisely as *perturbations* to some base task as follows: Base Task. A base task $\tau_{B}$ is a task where an end application desires for a policy to be able to perform the task and perturbations of it. For example, a base task for a cooking robot could be a specific instance of chopping an onion, and it would be desirable for the robot to be robust to different variations of it. Using base tasks allows us to more precisely understand how *changes* to a task affect our policy.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-B Defining Generalization for Visuo-Lingual Policies", "weight": 1.0} -->

Perturbations. We define a perturbation function as a transformation $P:T\to T$, that applies a task delta to a base task $\tau$ to produce a new task $\tau_{P}$. We categorize perturbations induced by a perturbation function based on how the inputs and outputs of a policy $\pi(a\mid o^{n},l)$ are impacted as follows: Visual: $\tau_{P}$ is a visual perturbation of $\tau$ if $p_{\tau}(o_{0})\neq p_{\tau_{P}}(o_{0})$, i.e., the initial distribution of image observations has changed (e.g., the *Viewpoint* change in the top Fig. 1).

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Defining Generalization for Visuo-Lingual Policies", "weight": 1.0} -->

Semantic: $\tau_{P}$ is a semantic perturbation of $\tau$ if $l_{\tau}\neq l_{\tau_{P}}$, i.e., the language instruction has changed (e.g., the left side of Fig. 1).

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Defining Generalization for Visuo-Lingual Policies", "weight": 1.0} -->

Behavioral: $\tau_{P}$ is a behavioral perturbation of $\tau$ if the expert policy $\pi_{E}$ changes its action distribution for the task, i.e., the required optimal behavior changes (e.g., morphing a carrot to a smaller one on the right of Fig. 1).

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Defining Generalization for Visuo-Lingual Policies", "weight": 1.0} -->

Note that this categorization is not mutually exclusive, meaning a perturbation can fall under one or more of the above categories. For example, the behavior of the expert policy often changes with the initial state distribution or the instruction, so behavioral perturbations are often also visual or semantic.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Defining Generalization for Visuo-Lingual Policies", "weight": 1.0} -->

We also note that because a perturbation captures how a base task changes, the same perturbed task $\tau_{P}$ could be associated with multiple different categorizations, depending on the base task. For example, if the base task is "pick up carrot" with a carrot and apple in the scene, and the task is perturbed to "pick up the orange object", then this is semantic only, because the required behavior does not change. However, if the base task is instead "pick up apple", then "pick up the orange object" would be a semantic + behavioral perturbation, because the task now involves picking up a new object.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Defining Generalization for Visuo-Lingual Policies", "weight": 1.0} -->

This categorization can be extended to additional modalities if the policy relies on them, e.g., if the policy uses tactile information or sound, we can further categorize perturbations based on changes to these modalities.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B Defining Generalization for Visuo-Lingual Policies", "weight": 1.0} -->

Factors. We define a factor as a human-interpretable, fine-grained grouping of perturbations, where all perturbations in a factor affect a task in a common way. For example, the lighting in a scene for a base task could be changed in multiple ways (e.g., varying intensities), each of which would be a different perturbation. We can then group all such perturbations under the factor "Lighting". Factors can be categorized as one or more of visual, semantic, and behavioral, based on the categorization of their constituent perturbations.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B Defining Generalization for Visuo-Lingual Policies", "weight": 1.0} -->

Axes. We define an axis of generalization as a grouping of factors that share a common set of applicable modalities. Axes are designed (subjectively) by humans to group correlated factors together. For example, our taxonomy defines *Image Augmentations* as an axis consisting of visual factors that can be varied using simple and common image transforms, such as "Lighting" or "Image Blur".

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B Defining Generalization for Visuo-Lingual Policies", "weight": 1.0} -->

Based on our formalism, generalization can be defined at multiple granularities. First, we define *generalization to a factor* as the robustness of a policy to perturbations defined by that factor. Then, we define *generalization to an axis* as robustness to factors within that axis. Finally, we define *generalization to a category* as robustness to the axes within that category, where categories are defined by the set of modalities (visual, semantic, behavioral) that are perturbed.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-C Assumptions", "weight": 1.0} -->

We provide more assumptions we make to narrow down the scope of generalization we consider, along with our rationale.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-C Assumptions", "weight": 1.0} -->

Manipulation Tasks. While there exists many classes of robotics tasks where one could study generalization, we build our taxonomy in for robot manipulation tasks. While other domains are of course important, manipulation presents many unique and elusive forms of generalization worth investigating.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-C Assumptions", "weight": 1.0} -->

Atomic Perturbations. We focus on perturbations that are *atomic*, which we loosely define as meaning they can be achieved by a single change to a task. For example, "pick up plate" $\to$ "push the cup" is not *atomic* because this requires two changes to the task: changing "plate" to "cup", and changing "pick" to "push". We do this to study generalization in a more fine-grained manner while not limiting comprehensiveness, because more complex perturbations can be achieved using a composition of atomic perturbations in our taxonomy.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-C Assumptions", "weight": 1.0} -->

Short-Horizon Tasks. Many works study long-horizon manipulation tasks, which consist of sequencing many shorter tasks together. There are many interesting types of generalization specific to the long-horizon setting, such as reordering tasks in a sequence, or perturbing one or multiple tasks in the sequence. In this work, we focus on short-horizon tasks as a starting point. We hope that by establishing a taxonomy for generalization at the this level, this taxonomy can be readily extended in the future to longer horizons.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Axes of Generalization", "weight": 1.0} -->

Our goal is to present a broad taxonomy of generalization that can guide future evaluations of robot policies. First, in Section IV-A, we outline $\bigstar$-Gen, our taxonomy. Next, in Section IV-B, we reframe prior work through the lens of $\bigstar$-Gen, illustrating how it not only encompasses prior efforts, but also provides a comprehensive framing for evaluating policies.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Axes of Generalization", "weight": 1.0} -->

Realistic generic augmentations in image space. lighting, image blur, image contrast Visual changes to scene elements that do not affect behavior. surface color, distractor object appearance, distractor object placement, textures Visual Task Object Visual changes to task-relevant objects that do not affect behavior. manipulated object color, other object color (e.g., container an object is placed in) Changes to camera viewpoints. camera pose, partial occlusion Changes to instruction that require additional knowledge about physical properties of a task-relevant object. referencing objects based on color, mass, size Simple rephrasing of the instruction that does not affect underlying behavior. verb synonyms, removing articles (e.g., “pick up the carrot” → “pick up carrot”) Changes to instruction that involve references to spatial relationships between multiple objects when defining a task, without changing behavior. understanding to be “left” or “right” of an object, to be ”in” an object (e.g., “pick up carrot” → “pick up object in sink”) Changes to instruction that require knowledge of human affordances, or how humans interact with an object.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Axes of Generalization", "weight": 1.0} -->

understanding human comfort, object use cases (e.g., “hand me something I can use to clean up this mess”) Changes to instruction that require external knowledge that can be found on the internet. famous nouns (e.g., celebrities), properties of common objects (e.g., color of a basketball) Unobserved changes to task-relevant objects that affect behavior. task-relevant object mass, friction, fragility Unobserved changes to scene elements that affect behavior. surface friction, temperature Changes to task-relevant object poses in the scene. manipulated object pose, other object pose Changes to scene elements that affect behavior. clutter, surface height Changes to task-relevant objects that affect their geometry. manipulated object size, shape Changes to the robot embodiment that affect behavior. new robot arm, new gripper or hand Specific to bimanual embodiments, symmetry captures changes that require the robot to mirror behavior across arms. using different arm to perform same absolute motion, to perform flipped absolute motion Changes to instruction involving motion descriptors that affect behavior.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Axes of Generalization", "weight": 1.0} -->

speed (e.g., “quickly” or “slowly”) Changes to instruction that involve references to spatial relationships between multiple objects when defining a task, that affect behavior. changing spatial references relative to the same object (e.g., “pick object left of the sink” → “pick object right of the sink”) Replacing nouns with other nouns already in the scene. other manipulated object (e.g., ”pick carrot” → ”pick knife” when both are in the scene) Changes to action verbs that require new behavior. new action to perform on task-relevant object (e.g., ”pick bottle” → ”rotate bottle”) New Object Property Changes to task-relevant object properties that affect object appearance and language instruction, but not behavior. new object color when base language instruction refers to the object color Visual + Semantic + Behavioral Changes to task-relevant objects to new objects with different visual appearances, semantic descriptions, and physical characteristics. new manipulated object (e.g., carrot → zucchini) TABLE I: ★-Gen: Axes of Generalization

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-A $\\bigstar$-Gen: A Taxonomy of Generalization", "weight": 1.0} -->

We structure our taxonomy $\bigstar$-Gen around the three modalities visuo-lingual manipulation policies use to interact with the world: visual (image inputs), semantic (language task inputs), and behavioral (action outputs).

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-A $\\bigstar$-Gen: A Taxonomy of Generalization", "weight": 1.0} -->

As defined in Section III, all perturbations to a base task affect visuo-lingual policies through combinations of these three modalities. Therefore, we can categorize perturbations (and thus factors and axes) into seven distinct *categories* based on the combination of modalities they modify.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-A $\\bigstar$-Gen: A Taxonomy of Generalization", "weight": 1.0} -->

Visual: Factors and axes in this category modulate image inputs for the initial state, but do not affect the required behavior in the base task or the language instruction. Example factors include lighting, camera pose, and distractor objects (see the green sector of Fig. 1).

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-A $\\bigstar$-Gen: A Taxonomy of Generalization", "weight": 1.0} -->

Semantic: Semantic factors and axes modulate the language instruction without changing the initial image or the required behavior. Example factors include replacing verbs with synonyms, and changing the instruction to use spatial relationships such as "in the " (see the orange sector of Fig. 1).

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-A $\\bigstar$-Gen: A Taxonomy of Generalization", "weight": 1.0} -->

Behavioral: Behavioral factors and axes only affect required behavior without affecting policy inputs. Therefore, all isolated behavioral factors are necessarily *unobserved* from single observations. Example factors include changes to object mass or friction (see the blue sector of Fig. 1). These factors are often challenging for policies due to their unobservability.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-A $\\bigstar$-Gen: A Taxonomy of Generalization", "weight": 1.0} -->

Visual + Behavioral: These factors and axes affect the initial image and required behavior, without changing the language instruction. As we show in Section IV-B, many factors that prior work consider as "behavior" generalization fall into this category. Example factors include manipulated object poses and surface/table heights (see the cyan sector of Fig. 1).

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-A $\\bigstar$-Gen: A Taxonomy of Generalization", "weight": 1.0} -->

Semantic + Behavioral: These factors and axes affect the language instruction and required behavior, without affecting the initial image. Example factors include changing the speed of a behavior ("quickly" vs. "slowly") in language, or specifying prepositional phrases like "into" or "in front of" that change the required behavior (see the purple sector of Fig. 1).

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-A $\\bigstar$-Gen: A Taxonomy of Generalization", "weight": 1.0} -->

Visual + Semantic: These factors and axes affect the initial image and language instruction, without requiring change to behavior. An example of this would be if the base instruction is "pick up the purple cup" and the cup changes color to blue, which changes the instruction to "pick up the blue cup". This is still an *atomic* perturbation, but since the color was specified in the original instruction, the instruction must also be changed. Had the initial instruction been "pick up the cup" and the cup was already blue, then "pick up the blue cup" would be a semantic perturbation. See the brown sector of Fig. 1.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-A $\\bigstar$-Gen: A Taxonomy of Generalization", "weight": 1.0} -->

Visual + Semantic + Behavioral: This category of factors and axes affect all three modalities at once. An example is going from "pick up the carrot" to "pick up the zucchini" -- this single perturbation affects the initial image, the language, and the behavior required to pick up the new object.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-A $\\bigstar$-Gen: A Taxonomy of Generalization", "weight": 1.0} -->

Within each of these high level *categories* of generalization, there are many potential *axes*. We list the axes we define in $\bigstar$-Gen in Table I. For each axis, we provide a description and list some example factors that fall under it. Importantly, not all base tasks will have meaningful instantiations of each axis in practice, which we will discuss more in Section VI.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-A $\\bigstar$-Gen: A Taxonomy of Generalization", "weight": 1.0} -->

In Fig. 1, we show example tasks for several axes, for the base task of "put carrot on plate". For example, an instantiation of *Visual Scene* (V-SC) for this task could be the introduction of a distracting object such as corn into the corner of the sink, which does not affect the desired behavior of the robot (picking up the carrot and placing it on the plate).

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-A $\\bigstar$-Gen: A Taxonomy of Generalization", "weight": 1.0} -->

Compositionality. The axes and factors in $\bigstar$-Gen are defined for *atomic* perturbations. We can *compose* these to obtain more complex notions of generalization, provided this is meaningful. For example, we can compose a perturbation for the visual axis *Viewpoint* with a perturbation for the semantic axis *Object Properties*, to create a compositional perturbation.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-B Prior Notions of Generalization", "weight": 1.0} -->

In Table II we list prior works (both benchmarks and policy learning efforts) that measure generalization along with the axes of $\bigstar$-Gen they consider. For conciseness, we leave out axes that were not present in any of these works. A checkmark indicates that an axis is considered by a benchmark, although we note that different works that have a checkmark for a given axis may cover them to different levels of comprehensiveness.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-B Prior Notions of Generalization", "weight": 1.0} -->

We find in Table II that only a subset of our axes are measured in each prior work. We do not include compositional or long-horizon forms of generalization in this analysis, but these are also sparsely represented in prior work. We find that most dataset and benchmarking works (top rows of Table II) focus evaluation effort on visual related axes, while semantic axes are less explored by most of them. Policy learning works (bottom rows of Table II) focus less on visual, and do more rigorous evaluation of certain visual + behavioral axes. Semantic also tends to be under-evaluated in these works.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-B Prior Notions of Generalization", "weight": 1.0} -->

Thus, we find $\bigstar$-Gen to be a superset of prior attempts to measure generalization. While not observable in Table II, we find that prior works are also generally not as fine-grained as our taxonomy in their categorization of generalization -- for example RT-2 simply groups many of our visual + behavior axes under the blanket category "Behavior Generalization".

<!-- chunk {"id": "body-0051", "role": "body", "section": "Frequently Asked Questions", "weight": 1.0} -->

Having defined the axes of generalization in $\bigstar$-Gen and compared it to prior work in Section IV-B, readers might have questions about our taxonomy and its assumptions. In this section, we provide answers to several possible questions.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Frequently Asked Questions", "weight": 1.0} -->

*Q: Is $\bigstar$-Gen meant to be comprehensive?* *A*: The axes presented in $\bigstar$-Gen are meant as a starting point for the field, and although we did our best to make this list comprehensive, there could certainly exist other meaningful axes. In contrast, we consider the *categories* in $\bigstar$-Gen (e.g., visual + behavioral) to be exhaustive for the policies we consider, since they are built from the seven unique combinations of our policy modalities.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Frequently Asked Questions", "weight": 1.0} -->

*Q: Are the axes and factors in $\bigstar$-Gen subjective?* *A*: Yes, the axes and factors in $\bigstar$-Gen are human-specified in a subjective manner, so there are certainly other ways to group perturbations into factors, and factors into axes. However, our goal is not to design an objective way to categorize generalization, as this is an inherently subjective process. Instead, we aim to provide greater structure and comprehensiveness when categorizing generalization using human interpretable concepts, like "task-relevant objects" and "verbs".

<!-- chunk {"id": "body-0054", "role": "body", "section": "Frequently Asked Questions", "weight": 1.0} -->

*Q: What is the purpose of defining a taxonomy if it is inherently subjective?* *A*: As we will see in Section VI, our taxonomy give us the vernacular to discuss more fine-grained types of generalization. We intend this taxonomy to be a starting point for practitioners to gain greater insights about their models, and recognize the potential for reshaping our taxonomy as our understanding of how to effectively evaluate generalization grows.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Frequently Asked Questions", "weight": 1.0} -->

*Q: Is each axis equally important for generalization?* *A*: Whether or not an axis is "important" is very subjective, and depends on specific applications. Instead, we categorize different types of generalization more systematically to aid researchers and practitioners in evaluating their robot policies based on the needs of their downstream applications.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Frequently Asked Questions", "weight": 1.0} -->

*Q: Can you quantify how much different perturbations affect a base task?* *A*: It would be interesting to consider the "edit distance" that a perturbation induces from a base task, to quantify how much generalization is required. However, we do not consider this in $\bigstar$-Gen, due to the challenging nature of defining such distances. Some options for this could include image or text embeddings for visual or semantic perturbations, dynamic time warping for behavioral, or using multi-modal foundation models. Future work can investigate correlating such metrics with empirical generalization.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Case Study: Evaluating Generalization for Real-World Robot Manipulation", "weight": 1.0} -->

$\bigstar$-Gen provides a broad framework for generalization in robot manipulation, but how should practitioners use this framework to evaluate policies? In this section, we walk through a case study on instantiating a useful, real-world benchmark from $\bigstar$-Gen. We develop this benchmark, which we call BridgeV2-$\bigstar$, based on the widely used Bridge V2 dataset. We evaluate several state-of-the-art models, including OpenVLA and a reimplementation of $\pi_{0}$. In Section VI-A, we outline our desiderata for this benchmark and our guiding principles for how generalization tasks were chosen from our taxonomy. Then in Section VI-B, we provide our exact instantiation of the benchmark, including the data and specific tasks used for each category and axis of generalization. Finally, in Section VI-C, we report our results on this benchmark for several models and variations. Our granular taxonomy of generalization empowers us to make several interesting insights about these different models.

<!-- chunk {"id": "body-0058", "role": "body", "section": "VI-A Benchmark Desiderata", "weight": 1.0} -->

There is a vast set of factors and axes within our taxonomy, especially if we consider combinatorial choices of multiple axes. Thus, an immediate practical concern in designing a benchmark is how to budget effort toward different evaluation settings. We strike the following balance in our benchmark: Base Tasks: We choose four base tasks that do not deviate significantly from the support of the pre-training dataset (i.e., tasks that involve scenes and objects classes found in the dataset). We choose tasks that have practical instantiations of as many axes as possible.

<!-- chunk {"id": "body-0059", "role": "body", "section": "VI-A Benchmark Desiderata", "weight": 1.0} -->

Categories: We aim to evaluate categories that are both relevant to and allowed by the base tasks and the pre-training data distribution (i.e., Bridge V2).

<!-- chunk {"id": "body-0060", "role": "body", "section": "VI-A Benchmark Desiderata", "weight": 1.0} -->

Axes: We prioritize axes within each category that are instantiable for the base tasks.

<!-- chunk {"id": "body-0061", "role": "body", "section": "VI-A Benchmark Desiderata", "weight": 1.0} -->

Factors: We evaluate one or two factors per axis.

<!-- chunk {"id": "body-0062", "role": "body", "section": "VI-A Benchmark Desiderata", "weight": 1.0} -->

While the number of base tasks, axes, and factors can be scaled up arbitrarily, we found these specifications to strike a balance between providing utility and practical evaluation time.

<!-- chunk {"id": "body-0063", "role": "body", "section": "VI-B Instantiating $\\bigstar$-Gen on Bridge V2", "weight": 1.0} -->

Based on the above desiderata, we now discuss our choices for base tasks, axes, and models in this case study.

<!-- chunk {"id": "body-0064", "role": "body", "section": "VI-B Instantiating $\\bigstar$-Gen on Bridge V2", "weight": 1.0} -->

Dataset. We chose Bridge V2 as our pre-training dataset and platform, since prior work has shown meaningful generalization from training on it, and training environments from Bridge V2 have previously been reproduced for evaluation in other locations.

<!-- chunk {"id": "body-0065", "role": "body", "section": "VI-B Instantiating $\\bigstar$-Gen on Bridge V2", "weight": 1.0} -->

Choosing Base Tasks. We consider the following base tasks in our evaluation. Illustrations of these task setups are shown in Table V and Table VIII in Section A-I.

<!-- chunk {"id": "body-0066", "role": "body", "section": "VI-B Instantiating $\\bigstar$-Gen on Bridge V2", "weight": 1.0} -->

We choose these base tasks based on the support of the pre-training data. In particular, our tasks are instantiated in a replication of a sink environment that was used in Bridge V2, and was also used to evaluate generalization in prior work. We do this to promote generalization induced by the pre-training dataset, as otherwise it is less likely that policies would observe any significant degree of generalization.

<!-- chunk {"id": "body-0067", "role": "body", "section": "VI-B Instantiating $\\bigstar$-Gen on Bridge V2", "weight": 1.0} -->

We choose these specific tasks to cover different levels of alignment with the original tasks from Bridge V2 for this sink environment. We provide greater discussion of this in Section A-A. These tasks were also chosen because they allow for a wide range of perturbations from $\bigstar$-Gen.

<!-- chunk {"id": "body-0068", "role": "body", "section": "VI-B Instantiating $\\bigstar$-Gen on Bridge V2", "weight": 1.0} -->

Axes in BridgeV2-$\bigstar$. In Table III we list all axes and factors we evaluate (also shown in the BridgeV2-$\bigstar$ row of Table II). distractors, surface color Visual Task Object other object color common obj properties, typos manipulated object pose manipulated object size, shape new action on object new manipulated object TABLE III: The axes from ★-Gen evaluated in BridgeV2-★ These axes span 5/7 of the categories and 13/22 axes in $\bigstar$-Gen. A list of exact tasks is provided in Section A-I. Behavioral axes were difficult to instantiate because most perturbations that do not alter visuals or language also do not affect behavior, especially for our base tasks. For example, changing the weight of the carrot does not meaningfully change required behavior. Similarly, instantiating our sole axis for visual + semantic (*New Object Property*) was infeasible, as our base tasks do not refer to object properties. We encourage future work to consider a wider variety of base tasks (and associated pre-training datasets) that support assessing more of our axes.

<!-- chunk {"id": "body-0069", "role": "body", "section": "VI-B Instantiating $\\bigstar$-Gen on Bridge V2", "weight": 1.0} -->

Candidate Policies. We focus our evaluation on state-of-the-art open-source imitation learning policies that have shown meaningful generalization in the literature. Hence, we analyze three vision-language-action (VLA) models based on large pre-trained foundation models and fine-tuned on robot data.

<!-- chunk {"id": "body-0070", "role": "body", "section": "VI-B Instantiating $\\bigstar$-Gen on Bridge V2", "weight": 1.0} -->

OpenVLA: Open-source VLA with 7B parameters based on a Prismatic-Llama backbone.

<!-- chunk {"id": "body-0071", "role": "body", "section": "VI-B Instantiating $\\bigstar$-Gen on Bridge V2", "weight": 1.0} -->

MiniVLA: Open-source VLA with 1B parameters and vector quantized tokenization with action chunking, based on a Prismatic-Qwen backbone. $\pi_{0}$: Third-party re-implementation of a 3B parameter VLA using flow-based action chunking, based on a PaliGemma backbone.

<!-- chunk {"id": "body-0072", "role": "body", "section": "VI-B Instantiating $\\bigstar$-Gen on Bridge V2", "weight": 1.0} -->

Evaluation Procedure. To evaluate our models, we adopt a co-fine-tuning strategy. First, we start from a version of each model that is pre-trained only on Bridge V2. Then, we collect a small number of base task demonstrations from our evaluation environment, and then co-fine-tune on Bridge V2 and this data. We do this for the following reasons: Including in-domain data allows us to clearly define what it means to be "in-distribution", and how different evaluation conditions deviate from this, without needing to replicate the exact environment and tasks present in the prior data, which can be challenging. Having a precise notion of "in-distribution" is important, as otherwise it is ambiguous how to designate any given evaluation condition as some form of generalization.

<!-- chunk {"id": "body-0073", "role": "body", "section": "VI-B Instantiating $\\bigstar$-Gen on Bridge V2", "weight": 1.0} -->

Collecting new data is needed to have greater flexibility when choosing base tasks, such that we can choose tasks where many axes of generalization can be applied, or tasks that are required for a given application.

<!-- chunk {"id": "body-0074", "role": "body", "section": "VI-B Instantiating $\\bigstar$-Gen on Bridge V2", "weight": 1.0} -->

It is realistic in many scenarios to require in-domain data to perform a given task effectively, so this procedure represents a realistic use case for generalist policies.

<!-- chunk {"id": "body-0075", "role": "body", "section": "VI-B Instantiating $\\bigstar$-Gen on Bridge V2", "weight": 1.0} -->

We denote co-fine-tuned models with (FT), while models without this designation are evaluated zero-shot without in-domain data. In Section A-G, we compare models with and without co-fine-tuning to further motivate this procedure.

<!-- chunk {"id": "body-0076", "role": "body", "section": "VI-B Instantiating $\\bigstar$-Gen on Bridge V2", "weight": 1.0} -->

We generate perturbations of our base tasks to evaluate for generalization. We measure generalization with respect to these base tasks, not the pre-training data. We describe our rationale for this more thoroughly in Section A-B. For each task (base tasks and their perturbations), we minimize randomness in the initial conditions (e.g., we attempt to limit variation in object poses across demonstrations and evaluations). When constructing perturbed tasks, we only modify the initial conditions of the base task in the manner specified by a given factor, so that success rates only reflect generalization to the specified perturbation, and not other inadvertent changes.

<!-- chunk {"id": "body-0077", "role": "body", "section": "VI-C Main Results", "weight": 1.0} -->

(a) Scaling robot data (b) Scaling LLM backbones (d) Vector quantized action chunking Figure 3: We investigate different VLA design decisions to assess their impact on generalization. We report success rates across all trials for each model and axis. (a) Scaling robot dataset size and diversity can improve multiple axes of generalization. (b) Using a larger LLM backbone can improve semantic generalization, but only to a limited extent. (c) VQA co-training can improve some axes, but has a mixed effect on semantic axes. (d) Vector quantized action chunking can improve multiple axes.

<!-- chunk {"id": "body-0078", "role": "body", "section": "VI-C Main Results", "weight": 1.0} -->

In Fig. 2, we report our main results on our BridgeV2-$\bigstar$ benchmark, which consists of in-distribution base task performance, and 55 task variations that span 13 of our axes, for a total of 885 real-world evaluations. We find that existing generalist policies tend to struggle on most of our considered axes. In particular, semantic generalization is weak across all models, despite them leveraging large language model backbones trained on internet-scale data. This has interesting implications: e.g., rather than relying soley on improvements in language modeling to improve semantic generalization, perhaps other mechanisms are needed, such as improving language annotations in robot datasets.

<!-- chunk {"id": "body-0079", "role": "body", "section": "VI-C Main Results", "weight": 1.0} -->

Each model tends to have similar strengths and weaknesses across our different axes. However, there are some notable differences between each model that the fine-grained nature of our benchmark helps reveal. For example, OpenVLA is noticeably worse at visual generalization than the other models, while MiniVLA struggles more with forms of visual + behavioral generalization. OpenVLA performs the best at understanding object properties which could be due to it having the largest language model backbone, but it still struggles with other forms of semantic generalization. $\pi_{0}$ generally performs the best across all axes, possibly due to a more capable VLM backbone (PaliGemma), and/or better architecture design (flow-based action chunking). However, like the other models, $\pi_{0}$ still generally struggles in terms of absolute performance for most axes. We provide detailed results for each evaluation condition in the Section A-J.

<!-- chunk {"id": "body-0080", "role": "body", "section": "VI-C Main Results", "weight": 1.0} -->

OpenVLA (Bridge, VQA, FT) Semantic (S-PROP + S-LANG) Visual (V-SC + V-OBJ) Visual + Behavioral (VB-POSE + VB-ISC) TABLE IV: Compositional results for two axes from each of semantic, visual, and visual + behavioral.

<!-- chunk {"id": "body-0081", "role": "body", "section": "VI-D Investigating VLA Design Decisions", "weight": 1.0} -->

To better understand how the design space of VLA policies affects generalization, we experiment with several VLA design decisions. We report findings from 390 additional evaluations for two base tasks ("put carrot" and "put knife") in Figure 3.

<!-- chunk {"id": "body-0082", "role": "body", "section": "VI-D Investigating VLA Design Decisions", "weight": 1.0} -->

Scaling Robot Data. In Fig. 3(a) we compare our Bridge-only version of OpenVLA with a version that instead uses a mixture of data from OXE for pre-training and co-fine-tuning. It is important to note that OXE is a significantly larger dataset that contains Bridge V2, along with data from over 20 other robot embodiments. Consistent with prior work, we find that larger and more diverse robot datasets can significantly improve overall generalization. However, we observe that while generalization improves along several axes (especially some semantic and visual axes), those that the Bridge-only model struggled with the most (e.g., *Viewpoint*, *Morphed Objects*, *Multi-Object Referencing*) do not improve significantly. This indicates that further efforts are needed to address the most significant deficiencies in current generalist policies.

<!-- chunk {"id": "body-0083", "role": "body", "section": "VI-D Investigating VLA Design Decisions", "weight": 1.0} -->

Scaling LLM Backbones. In Fig. 3(b) we compare VLA policies that share the same architecture and differ only in the large language model (LLM) backbone. Specifically, we compare OpenVLA (Bridge, FT), using Llama 2 7B, and MiniVLA (Bridge, --VQ, FT), using Qwen2.5 0.5B. Note that this version of MiniVLA does not use vector quantized action chunking (designated as --VQ), and the only major difference between these two models is their LLM backbone. We find that the larger LLM backbone does improve semantic generalization, which makes intuitive sense. However, there still remain large deficiencies in terms of absolute performance for these axes, and there is much less effect on the others, suggesting that scaling LLMs only has limited benefits.

<!-- chunk {"id": "body-0084", "role": "body", "section": "VI-D Investigating VLA Design Decisions", "weight": 1.0} -->

VQA Co-training. In Fig. 3(c), we investigate co-training with general visual-question answering (VQA) data, which has been suggested in prior work to improve VLA generalization. We find that VQA co-training does generally help, but surprisingly has a mixed effect for semantic axes, improving 3 of them (*Language Rephrase*, *Multi-Object Referencing*, *Internet Knowledge*), but hurting another (*Object Properties*). This could indicate room for improvement when co-training VLAs, such as by using targeted VQA data for inducing various forms of policy generalization, rather than general VQA data.

<!-- chunk {"id": "body-0085", "role": "body", "section": "VI-D Investigating VLA Design Decisions", "weight": 1.0} -->

Vector Quantized Action Chunking. In Fig. 3(d), we investigate the effect of removing vector quantized action chunking (--VQ) from MiniVLA, and instead using the binning-based tokenization from OpenVLA. We find that for nearly all axes (except *Interacting Scene*), this change hurts generalization. This is perhaps because action chunking helps the policy resolve action uncertainty and multi-modality by committing to certain action sequences, as hypothesized in prior work.

<!-- chunk {"id": "body-0086", "role": "body", "section": "VI-D Investigating VLA Design Decisions", "weight": 1.0} -->

Compositionality. As mentioned in Section IV-A, we can compose the axes in $\bigstar$-Gen to form new types of generalization. While our primary focus in this work is studying single axes at a time, we provide some example compositional results in Table IV, which consists of 210 additional evaluations. We once again see that training on the larger OXE mixture seems to improve many semantic axes, specifically the composition of referring to object properties in language and rephrasing language instructions (S-PROP + S-LANG), possibly due to a larger variety of language instructions in the training data. Furthermore, some models are fairly robust to combinations of distractors and object colors (V-SC + V-OBJ), with MiniVLA and $\pi_{0}$ being the most performant, similarly as in the main results. Some models are also surprisingly robust to the composition of different object poses and scene factors (VB-POSE + VB-ISC), with $\pi_{0}$ performing the best in this setting.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Discussion", "weight": 1.5} -->

We present $\bigstar$-Gen, a taxonomy of generalization for robot manipulation. We hope this taxonomy can help improve the comprehensiveness and preciseness of generalization benchmark design as generalist robot policies improve in capabilities. Our taxonomy not only thoroughly considers the space of visuo-lingual policy generalization, but is also straightforward to instantiate in practice. We demonstrate the considerations and design process for an instantiation of the $\bigstar$-Gen benchmark on the popular Bridge V2 Dataset and evaluate state-of-the-art VLA models along 13 axes of different combinations of visual, semantic, and behavioral generalization. Our analysis leads to key insights about generalist policy design choices: Larger LLMs can help generalization to a limited extent, primarily for semantic axes.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Discussion", "weight": 1.5} -->

Larger, cross embodiment datasets can help with many generalization axes, but do not significantly improve the largest deficiencies in existing models.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Discussion", "weight": 1.5} -->

Vector quantized action chunking improves generalization over binning-based tokenization without chunking.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Discussion", "weight": 1.5} -->

Co-training on VQA datasets can help with overall generalization, but only to a limited extent, and with surprisingly mixed results for semantic axes.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Discussion", "weight": 1.5} -->

Limitations and Future Work. Due to constraints imposed by real-world evaluation time (1600+ trials), we only evaluate a subset of factors and their compositions that we believe most effectively demonstrate the benefits of $\bigstar$-Gen. We hope that future work can build more benchmarks based our taxonomy, such as by considering datasets that support more complex behavior and diverse settings like DROID. Also, we still design our evaluation conditions in BridgeV2-$\bigstar$ using human oversight, leaving room for possible bias. We believe future work can instead automate benchmark design using generative models, which we provide a preliminary demonstration of on our website, and describe in more detail in Appendix B.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Discussion", "weight": 1.5} -->

While we consider $\bigstar$-Gen to be a strong starting point, we believe that future work can revise and expand our taxonomy based on the needs of robotics practitioners. Also, while we show that $\bigstar$-Gen can help prove insights about current generalist policies and their design decisions, we also hope that $\bigstar$-Gen can help inform data collection efforts to achieve the forms of generalization considered in our taxonomy.
