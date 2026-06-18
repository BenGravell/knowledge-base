DiffStack: A Differentiable and Modular Control Stack for Autonomous Vehicles

Topics include Differentiable planning, Autonomous driving, Prediction, Motion planning, End-to-end learning, Modular.

Presents DiffStack, a fully differentiable and modular autonomous driving stack that combines prediction, planning, and control. By making the entire stack differentiable, it enables end-to-end gradient-based optimization across components, improving performance over non-differentiable modular baselines.

Autonomous vehicle (AV) stacks are typically built in a modular fashion, with explicit components performing detection, tracking, prediction, planning, control, etc. While modularity improves reusability, interpretability, and generalizability, it also suffers from compounding errors, information bottlenecks, and integration challenges. To overcome these challenges, a prominent approach is to convert the AV stack into an end-to-end neural network and train it with data. While such approaches have achieved impressive results, they typically lack interpretability and reusability, and they eschew principled analytical components, such as planning and control, in favor of deep neural networks. To enable the joint optimization of AV stacks while retaining modularity, we present DiffStack, a differentiable and modular stack for prediction, planning, and control. Crucially, our model-based planning and control algorithms leverage recent advancements in differentiable optimization to produce gradients, enabling optimization of upstream components, such as prediction, via backpropagation through planning and control.

## Introduction

Intelligent robotic systems, such as autonomous vehicles (AVs), are typically architected in a modular fashion and comprised of modules performing detection, tracking, prediction, planning, and control, among others. Modular architectures are generally desirable because of their verifiability, interpretability and generalization performance; however, they also suffer from compounding errors, information bottlenecks, and integration challenges.

We introduce DiffStack, a differentiable AV stack with modules for prediction, planning, and control that combines the benefits of modular and data-driven architectures (Fig. 1). The prediction module in DiffStack is a learned neural network that predicts the future motion of agents; the planning and control modules are principled, hand-engineered algorithms that produce AV actions given the current world state and motion predictions.

We evaluate DiffStack in both open-loop and closed-loop simulation settings using the large-scale, real-world nuScenes dataset. Our results show some immediate benefits of differentiable stacks: by training a prediction model with respect to the final control objective, DiffStack increases the effectiveness of predictions for decision making by up to $15\text{\%}$ over a large number of diverse scenarios. DiffStack achieves this , e.g., learning to make fewer prediction errors that would negatively affect planning.

## Limitations & Conclusions

Limitations. One limitation of our work is the open-loop training and log-replay based simulation setup. In lieu of a real-world AV or a simulator with strong behavioral realism, this is standard practice; however, recent efforts on accurate behavior simulation could be leveraged in the future. Our implementation of DiffStack also has limitations. First, it is not differentiable wrt. *all* possible parameters, e.g., no gradients flow from the control loss to the planner's trajectory candidate generator.
