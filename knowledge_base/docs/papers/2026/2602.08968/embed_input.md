<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

stable-worldmodel-v1: Reproducible World Modeling Research and Evaluation

Topics include World models, Reproducibility, Model-based reinforcement learning, Benchmarks, Planning, Software.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces stable-worldmodel, a modular research ecosystem for implementing, evaluating, and comparing world-model agents. The paper is primarily an infrastructure and reproducibility contribution, intended to reduce publication-specific code drift and standardize world-model evaluation workflows.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

World Models have emerged as a powerful paradigm for learning compact, predictive representations of environment dynamics, enabling agents to reason, plan, and generalize beyond direct experience. Despite recent interest in World Models, most available implementations remain publication-specific, severely limiting their reusability, increasing the risk of bugs, and reducing evaluation standardization. To mitigate these issues, we introduce stable-worldmodel (SWM), a modular, tested, and documented world-model research ecosystem that provides efficient data-collection tools, standardized environments, planning algorithms, and baseline implementations. In addition, each environment in SWM enables controllable factors of variation, including visual and physical properties, to support robustness and continual learning research. Finally, we demonstrate the utility of SWM by using it to study zero-shot robustness in DINO-WM.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A promising paradigm toward building capable and general-purpose embodied agents involves learning dynamics models of the world, commonly referred to as World Models (WM, Ha and Schmidhuber ). Despite rapid progress and growing community interest, research on WMs remains fragmented and lacks shared benchmarks comparable to those in vision, reinforcement learning, or language modeling. This diversity of paradigms, design choices, and environments complicates meaningful comparison between methods. Systematic re-implementation of utilities further exacerbates this issue: for example, two recent works, PLDM and DINO-WM, re-implement the same Two-Room environment with substantial divergence (81 deletions, 86 additions, and 18 updates), underscoring the lack of shared infrastructure. Moreover, beyond comparing performance across disparate environments, controlled variations within a single environment are essential to isolate key factors, probe generalization, and better understand the inductive biases and failure modes of WMs.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we introduce stable-worldmodel, a new research ecosystem designed to facilitate streamlined and reproducible experimentation and benchmarking WMs. We design a simple, easy-to-use API that allows custom dataset collection, training, and evaluation, as well as integration of novel algorithms and environments to support future growth and development. A comparison with other recent latent world model codebases is provided in Table 1.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Stable World Model Ecosystem: An Overview", "weight": 1.0} -->

Stable World Model (SWM) goal is to support researchers by reducing the idea-to-experiment time gap. We build the library around the philosophy that people already have their codebase or tool for training their model. Therefore, our library should focus on providing support for their training with a ready-to-use environment and utilities for data collection or model evaluation. In the rest of this section, we provide an overview of the user API and the different components of the library. A full overview of a typical world model pipeline with SWM is provided in Listing LABEL:lst:swm-pusht.

<!-- chunk {"id": "body-0007", "role": "body", "section": "The World interface: streamlined WM research", "weight": 1.0} -->

1 import stable_worldmodel as swm 3 world = swm.World(’swm/PushT-v1’, num_envs=8) 4 world.set_policy(YourExpertPolicy) 6 world.reset # initialize the world 7 world.step # update the world state with policy 8 world.infos # current world state (dict) Listing 1: World Interface Logic. After specifying the environment ID (e.g., swm/PushT-v1) and the number of simulations, a policy can be attached to enable online interaction with the environment. At any time, all simulation-related information can be accessed via the infos dictionary.

<!-- chunk {"id": "body-0008", "role": "body", "section": "The World interface: streamlined WM research", "weight": 1.0} -->

The core abstraction in SWM is the World. A World wraps one or more Gymnasium tow environments and provides a unified interface for simulation, data collection, debugging, and evaluation. Internally, it leverages Gymnasium's synchronous environment API to manage and step multiple environments within a single object.

<!-- chunk {"id": "body-0009", "role": "body", "section": "The World interface: streamlined WM research", "weight": 1.0} -->

Unlike the widely used Gymnasium interface, a World does not return observations, rewards, or termination flags from reset or step. Instead, all data produced by the environments is stored in a single internal dictionary, world.infos, which is updated in place at every reset or step. Both methods operate synchronously over all environments, making the complete simulation state accessible at any time via world.infos.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The World interface: streamlined WM research", "weight": 1.0} -->

Action selection in SWM is handled by a policy object attached to the World. The step method does not take actions as input; instead, at each step, the world queries its policy to obtain actions for all environments. A policy is a lightweight Python object implementing a get_action method, which takes the current world.infos as input and returns one action per environment. This design cleanly decouples control logic from environment execution, allowing policies to be swapped without modifying the world interface.

<!-- chunk {"id": "body-0011", "role": "body", "section": "The World interface: streamlined WM research", "weight": 1.0} -->

Once a policy is attached to a World, it can be used to record datasets or perform evaluation. Dataset recording executes the policy over episodes and logs all information contained in world.infos, while evaluation runs the same execution loop without data persistence. In both cases, the behavior and properties of the resulting trajectories are entirely determined by the chosen policy and world configuration. An illustrative example of dataset recording is provided in Listing LABEL:lst:swm-fov. Additional details about the dataset and evaluation are reported in Appendix B.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Environments and Factor of Variations", "weight": 1.0} -->

SWM is designed as a collection of diverse environments that span a wide range of design choices, including continuous and discrete state/action spaces, different action modalities, and varied agent embodiments. These environments differ not only in their task structure but also in their underlying dynamics or observation spaces, as illustrated in Figure 1. Such diversity allows evaluation across qualitatively distinct settings and supports broad comparisons of learning algorithms. However, evaluating generalization solely across different environments can obscure more fine-grained sources of variation that commonly arise within a single task or domain.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Environments and Factor of Variations", "weight": 1.0} -->

A key feature of SWM is the notion of factors of variation (FoV). Each environment in the library exposes a set of optional controllable properties that enable systematic customization of the environment configuration. These factors of variation span multiple aspects, including visual attributes (e.g., color, shape, textures, lighting), geometric properties (e.g., size, orientation, position), and physical parameters (e.g., friction, damping, mass, gravity). By explicitly exposing these controls, SWM enables fine-grained studies of robustness, generalization, domain shift, and continual learning within a single, unified environment. We provide a toy example in Listing LABEL:lst:swm-fov. More details about FoV can be found in Appendix B 1 import stable_worldmodel as swm 3 world = swm.World(’swm/PushT-v1’, num_envs=2) 4 world.set_policy(YourExpertPolicy) 6 print(world.single_variation_space.names) # available FoV 8 # dataset with changing all agent FoV, and T color.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Environments and Factor of Variations", "weight": 1.0} -->

9 world.record_dataset(10 dataset_name=’pusht_demo’,episodes=4, seed=0, 11 options={"variation": ["agent", "block.color"]}, Listing 2: SWM Factor of Variation Logic. During data collection or world reset, factors of variation (FoV) can optionally be specified via the options argument. In this illustrative Push-T example, all agent-related FoVs (e.g., color and size) are sampled, along with the color of the T-shaped object.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Environments and Factor of Variations", "weight": 1.0} -->

Internally, FoVs are implemented as a new type of Gymnasium dictionary Space (in addition to the standard action and observation space), which stores an internal value that can be initialized, sampled with or without constraint.

<!-- chunk {"id": "body-0016", "role": "body", "section": "SWM Evaluation Suite: Tasks, Planning Algorithms, and Baselines", "weight": 1.0} -->

Evaluating world models is inherently challenging, as existing works rely on diverse evaluation settings. SWM provides built-in support for goal-conditioned evaluation, where the agent is tasked to reach a specified goal representation, such as a target state, image, or reward condition. Performance is measured in terms of success rate, defined as the percentage of evaluation episodes that end satisfying the goal condition.

<!-- chunk {"id": "body-0017", "role": "body", "section": "SWM Evaluation Suite: Tasks, Planning Algorithms, and Baselines", "weight": 1.0} -->

In SWM, evaluation can be conducted through the World interface and applied to the currently attached policy. These methods are evaluate and evaluate_from_dataset. SWM is agnostic to the choice of policy. Yet, we provided some utilities to facilitate planning with Model Predictive Control (MPC) or Feed-Forward action prediction. We provided further details on the specifics of each evaluation method and different MPC solvers in Appendix B.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Experiments: DINO-WM Zero-Shot Robustness", "weight": 1.0} -->

We now demonstrate how SWM can be used as a research tool to analyze model robustness. Specifically, we leverage SWM to evaluate the robustness of our reproduction of DINO-WM under both in-distribution and out-of-distribution evaluation settings, as well as its zero-shot generalization to environmental variations (e.g., agent color and background) in the Push-T environment. First, we observe that although DINO-WM performs well when evaluated on expert demonstrations, achieving a success rate of 94.0%, its performance deteriorates sharply under distribution shift. When evaluated on reaching states drawn from trajectories collected by a random policy, the success rate drops to 12.0%, revealing a strong dependence on the provenance of evaluation data. Next, using SWM as a controlled evaluation framework, we probe DINO-WM's zero-shot robustness to a range of factors of variation, as summarized in Table 2. Across all tested perturbations, the model exhibits consistently low scores, indicating limited robustness to unseen environmental variations despite the task structure remaining unchanged.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Conclusion and Future Directions", "weight": 1.5} -->

With a streamlined API SWM promotes standardized evaluation, which we hope will accelerate progress in world-model research. We plan some future updates focusing on tools for improving debugging and interpretation of world models. Moreover, we will work on adding new environment support to the library with a focus on physical simulation or real-world tasks. Finally, our long-term vision aims to provide a standardized benchmark to keep track of the state-of-the-art in controllable world models, e.g., via a Hugging Face Benchmark.
