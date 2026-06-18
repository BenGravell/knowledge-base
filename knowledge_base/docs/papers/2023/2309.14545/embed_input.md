Motions in Microseconds via Vectorized Sampling-Based Planning

Topics include Motion planning, Robotics, Sampling-based methods, Planning, Control, Sampling.

Modern sampling-based motion planning algorithms typically take between hundreds of milliseconds to dozens of seconds to find collision-free motions for high degree-of-freedom problems. This paper presents performance improvements of more than 500x over the state-of-the-art, bringing planning times into the range of microseconds and solution rates into the range of kilohertz, without specialized hardware. Our key insight is how to exploit fine-grained parallelism within sampling-based planners, providing generality-preserving algorithmic improvements to any such planner and significantly accelerating critical subroutines, such as forward kinematics and collision checking. We demonstrate our approach over a diverse set of challenging, realistic problems for complex robots ranging from 7 to 14 degrees-of-freedom. Moreover, we show that our approach does not require high-power hardware by also evaluating on a low-power single-board computer. The planning speeds demonstrated are fast enough to reside in the range of control frequencies and open up new avenues of motion planning research.

## Introduction

High degree-of-freedom (d o f) robots rely on *motion planning* to move in complex workspaces, either using sampling-based approximations or numerical optimization. These planners are general and can solve realistic, challenging problems in hundreds of milliseconds to dozens of seconds on consumer cpus. However, this level of performance falls short---it is too slow for reactive operation in evolving environments and hampers algorithms for higher-level autonomy such as integrated task and motion planning.

A large literature accelerates motion planning with *coarse-grained* (*e.g.*, thread or process-level) parallelism, but these methods have seen relatively little uptake in practice, as their performance gains do not justify the added complexity. More recent work uses gpu-based parallelism to improve performance, but at the cost of communication overhead, algorithmic limitations, and the additional expense and power consumption of gpu hardware.

Our method significantly outperforms standard implementations of state-of-the-art sbmps on both desktop and low-power single board computers. Moreover, this work will enhance any work that uses motion planning, and our perspective on vector-oriented planning primitives extends beyond cpu simd instructions to other, similar parallelism models, *e.g.*, gpus. The planning speeds demonstrated blur the line between planning and control, and give cause to re-evaluate assumptions about robot motion.

## Discussion

Efficient motion planning is critical for many applications of robotics. In this paper, we demonstrate a novel approach to accelerating motion planning, based on a new perspective on *vector-oriented* operations for simple, high-frequency interleaving of high-performance parallelized and serial sections of code present in most sampling-based motion planning algorithms.

We also believe that our ideas will extend naturally to harder motion planning problems, such as kinodynamic and manifold-constrained planning. Further, because we can produce so many motion plans so fast, we may be able to efficiently provide empirical proofs of *solution nonexistence*, a feat that has long been challenging for sbmp. There may also be potential for using our vector-oriented planners as *local planners* inside higher-level motion planning algorithms.
