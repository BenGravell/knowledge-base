Group Marching Tree: Sampling-Based Approximately Optimal Motion Planning on GPUs

Topics include Motion planning, Kinodynamic planning, Sampling-based planning, Real-time planning, Approximate optimality, Graphics processing unit, Parallelized, GMT*, FMT*.

GMT* adapts FMT*'s lazy dynamic-programming tree expansion for massively parallel execution on GPUs by replacing the sequential expansion of the single minimum-cost sample with simultaneous expansion of the entire group of active samples whose cost falls below an increasing threshold. This group approximation introduces a bounded suboptimality constant but eliminates sequential data structures and reduces thread divergence. Achieves ~10 ms planning on desktop GPUs and ~30 ms on embedded GPUs.

This paper presents a novel approach, named the Group Marching Tree (GMT*) algorithm, to planning on GPUs at rates amenable to application within control loops, allowing planning in real-world settings via repeated computation of near-optimal plans. GMT*, like the Fast Marching Tree (FMT) algorithm, explores the state space with a "lazy" dynamic programming recursion on a set of samples to grow a tree of near-optimal paths. GMT*, however, alters the approach of FMT with approximate dynamic programming by expanding, in parallel, the group of all active samples with cost below an increasing threshold, rather than only the minimum cost sample. This group approximation enables low-level parallelism over the sample set and removes the need for sequential data structures, while the "lazy" collision checking limits thread divergence - all contributing to a very efficient GPU implementation. While this approach incurs some suboptimality, we prove that GMT* remains asymptotically optimal up to a constant multiplicative factor.

## Introduction

Robotic systems are increasingly operating in real-world settings---away from the structure, repetition, and certainty of the factory floor---that require a robot to not only sense its environment and state in real time, but to react accordingly. Acting in these paradigms often necessitates motion plans be computed on the basis of limited state and environmental knowledge, both of which may vary rapidly as information is gathered and the robot's surroundings change.

*Statement of Contributions.* In this work, we propose the use of approximate dynamic programming (ADP) methods that leverage algorithm parallelism for greater speed while incurring only a bounded degree of suboptimality. We present the Group Marching Tree (GMT^∗^) algorithm that, like the Fast Marching Tree algorithm (FMT^∗^), performs a "lazy" dynamic programming recursion on a set of samples in the state space to grow a tree of near-optimal cost-to-arrive paths.

## Conclusion

We have introduced and analyzed a novel planning algorithm, the Group Marching Tree algorithm (GMT^∗^), that trades off parallelism for optimality in order to leverage GPU hardware. The computational speed of GMT^∗^ allows us to approach the problem of planning in real-world settings---particularly focusing on the uncertain, dynamic environments that naturally arise from active robot sensing and the uncertain, disturbed motion of systems in the field---by replanning at rates commensurate with the control loop frequency.

This paper leaves several important research avenues open. Foremost, we plan to validate this approach experimentally on a platform with state and environmental sensing. We further plan to provide a more detailed theoretical analysis of GMT^∗^, such as providing time and space complexity analysis and potentially proving tighter suboptimality bounds. We additionally plan to explore extensions to other planning paradigms, which the computational speed of GMT^∗^ may enable.
