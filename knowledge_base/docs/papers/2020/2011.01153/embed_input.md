Perceive, Attend, and Drive: Learning Spatial Attention for Safe Self-Driving

In this paper, we propose an end-to-end self-driving network featuring a sparse attention module that learns to automatically attend to important regions of the input. The attention module specifically targets motion planning, whereas prior literature only applied attention in perception tasks. Learning an attention mask directly targeted for motion planning significantly improves the planner safety by performing more focused computation. Furthermore, visualizing the attention improves interpretability of end-to-end self-driving.

## Introduction

Self-driving is one of today's most impactful technological challenges, one that promises to bring safe and affordable transportation everywhere. Tremendous improvements have been made in self-driving perception systems, thanks to the success of deep learning. This has enabled accurate detection and localization of obstacles, providing a holistic understanding of the surrounding world, which is then sent to the motion planner to decide subsequent driving actions.

Despite the eminent success of these perception systems, their detection objective is mis-aligned with the self-driving vehicle's overall goal---to drive safely to the destination. We typically train the perception systems to detect all objects in the sensor range, assigning each object an equal weight even if some objects are not important as they will never interact with the self-driving vehicle. For example, they could be far away or parked on the other side of the road as in Figure 1.

Numerous studies in the past have explored adding sparse attention in deep neural networks to improve computation efficiency in classification and object detection. In order to perform well on the metrics employed in common benchmarks, the attention mask in still needs to cover all actors in the scene, slowing the network when the scene has many vehicles.

In this paper, our aim is to address these inconsistencies such that the amount of computation is optimized towards the end goal of motion planning.

## Conclusion

In this work, we propose an end-to-end learned, sparse visual attention mechanism for self-driving, where the sparse attention mask gates the feature backbone computation. As opposed to existing methods that focus on using attention for perception only, our attention masks are directly optimized for motion planning, which enables our network to output better planned trajectories while achieving more efficiency with higher sparsity. In future work, the attention module can be extended to have recurrent feedbacks from the output layers to better leverage temporal information.
