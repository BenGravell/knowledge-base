<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Control-limited Differential Dynamic Programming

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Trajectory optimizers are a powerful class of methods for generating goal-directed robot motion. Differential Dynamic Programming (DDP) is an indirect method which optimizes only over the unconstrained control-space and is therefore fast enough to allow real-time control of a full humanoid robot on modern computers. Although indirect methods automatically take into account state constraints, control limits pose a difficulty. This is particularly problematic when an expensive robot is strong enough to break itself. In this paper, we demonstrate that simple heuristics used to enforce limits (clamping and penalizing) are not efficient in general. We then propose a generalization of DDP which accommodates box inequality constraints on the controls, without significantly sacrificing convergence quality or computational effort. We apply our algorithm to three simulated problems, including the 36-DoF HRP-2 robot. A movie of our results can be found here goo.gl/eeiMnn.
