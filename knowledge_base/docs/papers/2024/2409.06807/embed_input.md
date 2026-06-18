Kino-PAX: Highly Parallel Kinodynamic Sampling-based Planner

Topics include Motion planning, Sampling-based planning, Kinodynamic planning, Graphics processing unit, Parallelized, Real-time planning.

GPU-native kinodynamic sampling-based planner that decomposes the traditionally serial RRT tree-growth process into three massively parallel subroutines. The design aligns with GPU execution hierarchies: independent threads, balanced workloads, low-latency shared memory.

Sampling-based motion planners (SBMPs) are effective for planning with complex kinodynamic constraints in high-dimensional spaces, but they still struggle to achieve real-time performance, which is mainly due to their serial computation design. We present Kinodynamic Parallel Accelerated eXpansion (Kino-PAX), a novel highly parallel kinodynamic SBMP designed for parallel devices such as GPUs. Kino-PAX grows a tree of trajectory segments directly in parallel. Our key insight is how to decompose the iterative tree growth process into three massively parallel subroutines. Kino-PAX is designed to align with the parallel device execution hierarchies, through ensuring that threads are largely independent, share equal workloads, and take advantage of low-latency resources while minimizing high-latency data transfers and process synchronization. This design results in a very efficient GPU implementation. We prove that Kino-PAX is probabilistically complete and analyze its scalability with compute hardware improvements....

## Introduction

Autonomous robotic systems are increasingly deployed in dynamic environments, requiring fast, reactive motion planning that accounts for the robot's complex kinematics and dynamics. Solving the kinodynamic motion planning problem *quickly* is critical for ensuring both functionality and safety. Sampling-based motion planners (SBMPs) have proven effective for various difficult problems, such as complex dynamics, complex tasks, and stochastic dynamics. Nevertheless, they are typically designed for serial computation, limiting their speed to CPU clock rate....

In this paper, we introduce Kino-PAX, a highly parallel kinodynamic SBMP, designed to efficiently leverage parallel devices. Kino-PAX grows a tree of trajectory segments directly in parallel. Our key insight is that the iterative tree growth process can be decomposed into three massively parallel subroutines. We design Kino-PAX to align with the parallel execution hierarchy of these devices, ensuring that threads are largely independent, share equal workloads, and take advantage of low-latency resources while minimizing high-latency data transfers and process synchronizations....

## Conclusion

We have introduced a novel motion planning algorithm for kinodynamic systems that enables a significant parallelization of a process previously considered inherently sequential. Our algorithm is well suited to exploit the recent advancements of modern computing devices and is equipped to scale as hardware continues to improve. Benchmark results show planning times of less than $8$ ms for 6-dimensional systems and less than $25$ ms for a 12-dimensional nonlinear system, representing an improvement of up to three orders of magnitude compared to traditional motion planning algorithms....

### IV-A Tuning Parameter

The exact expressions for $Cov{(\mathcal{R}_{i})}$ and $FreeVol{(\mathcal{R}_{i})}$ are the same as in \[\], which we also show in Sec. III-A3.

### Definition 1 (Probabilistic Completeness)

In summary, our contributions are four-fold: (i) Kino-PAX, a highly parallel kinodynamic SBMP designed to leverage the parallel architecture of GPU-like devices, (ii) a discussion of Kino-PAX's hyperparameters and its efficient application to highly parallel devices, (iii) a thorough analysis and proof of probabilistic completeness, and (iv) benchmarks showing the efficiency and efficacy of...
