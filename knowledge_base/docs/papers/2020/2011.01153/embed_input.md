Perceive, Attend, and Drive: Learning Spatial Attention for Safe Self-Driving

In this paper, we propose an end-to-end self-driving network featuring a sparse attention module that learns to automatically attend to important regions of the input. The attention module specifically targets motion planning, whereas prior literature only applied attention in perception tasks. Learning an attention mask directly targeted for motion planning significantly improves the planner safety by performing more focused computation. Furthermore, visualizing the attention improves interpretability of end-to-end self-driving.

## Introduction

Self-driving is one of today's most impactful technological challenges, one that promises to bring safe and affordable transportation everywhere. Tremendous improvements have been made in self-driving perception systems, thanks to the success of deep learning. This has enabled accurate detection and localization of obstacles, providing a holistic understanding of the surrounding world, which is then sent to the motion planner to decide subsequent driving actions.

Despite the eminent success of these perception systems, their detection objective is mis-aligned with the self-driving vehicle's overall goal---to drive safely to the destination. We typically train the perception systems to detect all objects in the sensor range, assigning each object an equal weight even if some objects are not important as they will never interact with the self-driving vehicle. For example, they could be far away or parked on the other side of the road as in Figure 1....

## Conclusion

In this work, we propose an end-to-end learned, sparse visual attention mechanism for self-driving, where the sparse attention mask gates the feature backbone computation. As opposed to existing methods that focus on using attention for perception only, our attention masks are directly optimized for motion planning, which enables our network to output better planned trajectories while achieving more efficiency with higher sparsity. In future work, the attention module can be extended to have recurrent feedbacks from the output layers to better leverage temporal information.

where $g_{i,j} = {- {\log{({- {\log u}})}}}$, and $u$ is sampled from $\text{Uniform}{\lbrack 0,1\rbrack}$. At inference time, hard attention $A_{i,j}$ can be obtained by comparing the logits,

Multi-task headers: Given the features computed by the backbone, $X \in {\mathbb{R}}^{128 \times \frac{H}{4} \times \frac{W}{4}}$, NMP uses two separate headers for perception & prediction, and motion planning. The perception & prediction header consists of separate branches for classification and regression. The classification branch outputs a score for each anchor box at each spatial location over the feature map $X$, while the regression branch outputs regression targets for each anchor box, including targets for localization offset, size, and heading angle....
